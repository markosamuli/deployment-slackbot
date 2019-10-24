# deployment-slackbot

## Archived

This repository is no longer maintained, so please use any of the code at your
own discretion.

## Description

This is sandbox project for playing with [lins05/slackbot] Python Slack chat bot.

The `ukko.plugins.deployment` plugin integrates with [deployment-server]
using [gRPC](http://www.grpc.io/) to trigger application deployments from Slack
channels.

[Protocol Buffers] (proto3) `.proto` language files can be found in the
`deployment-server` repository.

[lins05/slackbot]: https://github.com/lins05/slackbot
[deployment-server]:https://github.com/markosamuli/deployment-server
[gRPC]: http://www.grpc.io/
[Protocol Buffers]: https://developers.google.com/protocol-buffers/docs/overview

## Requirements

Install Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

Create `slackbot_settings.py` configuration file.

### Bot configuration

Configure bot:

```python
API_TOKEN = "<Slack API token>"
ERRORS_TO = "bots"
BOT_EMOJI = ":robot_face:"
```

### Plugins

Load plugins from Python packages:

```python
PLUGINS = [
    'ukko.plugins',
]
```

[Ukko] is is the god of the sky in Finnish mythology. Use any name you want
for your bot when configuring it.

[Ukko]: https://en.wikipedia.org/wiki/Ukko

### Deployment

The `ukko.plugins.deployment` plugin expects the following configuration to work.

```python
DEPLOYMENT_CHANNELS = {}
DEPLOYMENT_PROJECTS = {}
```

Max runtime for a deployment:

```python
DEPLOYMENT_TIMEOUT_SECONDS = 60 * 30
```

Configure default projects for Slack channels:

```python
DEPLOYMENT_CHANNELS['ABCDEFGH'] = {
  'projects': [
    'project-name'
  ]
}
```

Configure project settings:

```python
DEPLOYMENT_PROJECTS['project-name'] = {
    'build_filename': 'build.zip',
    's3_bucket': 'project-name-artefacts',
    'deployer': {
        'host': '127.0.0.1',
        'port': '50000',
    },
    'channels': [
        'ABCDEFGH'
    ],
    'environments': {
        'dev': {
            'default_branch': 'dev',
        },
        'uat': {}
    }
}
```

## Run the bot

```bash
python run.py
```

## Talk to the bot

* `<project name>` matches `[a-z0-9\-]+`
* `<environment>` matches `[a-z]+`
* `<branch>` matches `[a-z0-9\-_/]+`

### Register a project

This is a naive command to associate a project to a channel. All state data is
stored in the application memory so this will be lost if you restart the bot.
Just use the configuration file instead.

```text
@ukko: register project <project-name>
```

### Deploy the default project

If there is only one project associated with a channel, you can omit the 
project name.

If an environment has a default branch to deploy from, you can trigger
deployment by the environment name only:

```text
@ukko: deploy to <environment>
```

Some some environments you need to specific a branch as well:

```text
@ukko: deploy to <environment> from <branch>
```

### Deploy a specific project

These follow the same pattern as the examples above, just add project name to
the beginning. You'll need to do this if a channel has multiple projects 
associated.

Deploy a project to an environment:

```text
@ukko: deploy <project name> to <environment>
```

Deploy a project to an environment from a specific branch.

```text
@ukko: deploy <project name> to <environment> from <branch>
```

## License

* [MIT License](LICENSE)

## Author

* [@markosamuli](https://github.com/markosamuli)
