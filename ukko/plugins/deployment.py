# coding: UTF-8

import re
import logging

# Slackbot
from slackbot.bot import respond_to

# GRPC
from grpc.beta import implementations

# Deployment protocol buffer
from ukko import deployment_pb2
from ukko.deployment_pb2 import (
    DeploymentEvent,
    DeploymentArtefact,
    DeploymentRequest
)

# Deployment settings
from slackbot.settings import (
    DEPLOYMENT_TIMEOUT_SECONDS,
    DEPLOYMENT_PROJECTS,
    DEPLOYMENT_CHANNELS,
)


logger = logging.getLogger(__name__)

# This is a naive in-memory store
registered_projects = {}

for project_name, project_config in DEPLOYMENT_PROJECTS.iteritems():
    for channel_id in project_config.get('channels', []):
        registered_projects.setdefault(channel_id, []).append(project_name)

for channel_id, channel_config in DEPLOYMENT_CHANNELS.iteritems():
    for project_name in channel_config['projects']:
        registered_projects.setdefault(channel_id, []).append(project_name)


@respond_to('register project ([a-z\-]+)$', re.IGNORECASE)
def register_project(message, project):

    channel = message.body['channel']
    logger.info("register project {} to channel {}".format(project, channel))

    channel_projects = registered_projects.setdefault(channel, [])
    if project in channel_projects:
        message.reply("Project *{}* was already registered to this channel".format(project))
    else:
        channel_projects.append(project)
        message.reply("Register project *{}* to this channel".format(project))


@respond_to('deploy to ([a-z]+)$', re.IGNORECASE)
@respond_to('deploy to ([a-z]+) from ([a-z0-9\-_/]+)$', re.IGNORECASE)
def deploy_to_environment(message, environment, branch=None):

    channel = message.body['channel']

    channel_projects = registered_projects[channel]
    if len(channel_projects) > 1:
        text = "I found more than one project for this channel, what should I do?"
        message.reply(text)
        return

    project = channel_projects[0]
    deploy(message, project, environment, branch)


@respond_to('deploy ([a-z0-9\-]+) to ([a-z]+)$', re.IGNORECASE)
@respond_to('deploy ([a-z0-9\-]+) to ([a-z]+) from ([a-z0-9\-_/]+)$', re.IGNORECASE)
def deploy_project_to_environment(message, project, environment, branch=None):

    channel = message.body['channel']

    if project not in registered_projects[channel]:
        text = "Please register this project with this channel first."
        message.reply(text)
        return

    deploy(message, project, environment, branch)


def deploy(message, project, environment, branch=None):

    project_settings = DEPLOYMENT_PROJECTS.get(project, None)
    if not project_settings:
        text = "Sorry, I don't know how to deploy project *{project}*"
        message.reply(text.format(project=project))
        return

    environment_settings = project_settings.setdefault('environments', {}).get(environment, None)
    if not environment_settings:
        text = "Sorry, I don't know how to deploy to *{environment}*"
        message.reply(text.format(environment=environment))
        return

    if branch is None:
        branch = environment_settings.get('default_branch', None)
        if branch is None:
            text = "Sorry, you need to define a branch name when deploying to *{environment}*"
            message.reply(text.format(environment=environment))
            return

    deploy_filename = project_settings.get('build_filename')
    deploy_s3_bucket = project_settings.get('s3_bucket')
    deploy_s3_key = '{deploy_project}/{deploy_branch}/{deploy_filename}'.format(
        deploy_project=project,
        deploy_branch=branch,
        deploy_filename=deploy_filename,
    )

    deploy_artefact = DeploymentArtefact(
        s3_bucket=deploy_s3_bucket,
        s3_key=deploy_s3_key,
        bundle_type=deployment_pb2.DeploymentArtefact.ZIP)

    request = DeploymentRequest(
        project=project,
        environment=environment,
        artefact=deploy_artefact)

    text = 'Ok, deploying project *{project}* to environment *{environment}* from s3://{s3_bucket}/{s3_key}'
    message.reply(text.format(project=request.project,
                              environment=request.environment,
                              s3_bucket=deploy_artefact.s3_bucket,
                              s3_key=deploy_artefact.s3_key))

    deployer_settings = project_settings.get('deployer', {})
    host = deployer_settings.get('host', 'localhost')
    port = int(deployer_settings.get('port', 50000))

    logger.info("Connecting to Deployer server at %s:%d...", host, port)
    deploy_channel = implementations.insecure_channel(host, port)
    deploy_stub = deployment_pb2.beta_create_Deployer_stub(deploy_channel)

    # Send deployment request and stream deployment events
    events = deploy_stub.Deploy(request, DEPLOYMENT_TIMEOUT_SECONDS)

    last_status = None
    for event in events:

        last_status = event.status

        if event.status == DeploymentEvent.CREATED:
            # text = 'Deploying project *{project}* to environment *{environment}*...'
            text = '[Created] {message}'
            message.send(text.format(project=request.project, environment=request.environment, message=event.message))

        elif event.status == DeploymentEvent.QUEUED:
            # text = 'Waiting to deploy project *{project}* to environment *{environment}*...'
            text = '[Queued] {message}'
            message.send(text.format(project=request.project, environment=request.environment, message=event.message))

        elif event.status == DeploymentEvent.IN_PROGRESS:
            # text = 'Deploying project *{project}* to environment *{environment}*...'
            text = '[InProgress] {message}'
            message.send(text.format(project=request.project, environment=request.environment, message=event.message))

        elif event.status == DeploymentEvent.SUCCEEDED:
            # text = 'Project *{project}* deployed to environment *{environment}* successfully'
            text = '[Succeeded] {message}'
            message.send(text.format(project=request.project, environment=request.environment, message=event.message))

        elif event.status == DeploymentEvent.FAILED:
            # text = 'Deployment of project *{project}* to environment *{environment}* failed!'
            text = '[Failed] {message}'
            message.send(text.format(project=request.project, environment=request.environment, message=event.message))

        elif event.status == DeploymentEvent.STOPPED:
            # text = 'Deployment of project *{project}* to environment *{environment}* was stopped'
            text = '[Stopped] {message}'
            message.send(text.format(project=request.project, environment=request.environment, message=event.message))

        else:
            text = 'Unknown status {status} for deployment of project *{project}* to environment *{environment}*...'
            message.send(text.format(project=request.project, environment=request.environment, status=event.status))

    if last_status == DeploymentEvent.SUCCEEDED:
        text = 'All done!'
        message.reply(text)
    else:
        text = "Sorry dude, it didn't work out."
        message.reply(text)
