# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deployment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deployment.proto',
  package='deployment',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x64\x65ployment.proto\x12\ndeployment\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8e\x01\n\x12\x44\x65ploymentArtefact\x12\x11\n\ts3_bucket\x18\x01 \x01(\t\x12\x0e\n\x06s3_key\x18\x02 \x01(\t\x12>\n\x0b\x62undle_type\x18\x03 \x01(\x0e\x32).deployment.DeploymentArtefact.BundleType\"\x15\n\nBundleType\x12\x07\n\x03ZIP\x10\x00\"\x80\x01\n\x11\x44\x65ploymentRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x02 \x01(\t\x12\x30\n\x08\x61rtefact\x18\x03 \x01(\x0b\x32\x1e.deployment.DeploymentArtefact\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"C\n\x1bListDeploymentEventsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x02 \x01(\t\"\xa0\x02\n\x0f\x44\x65ploymentEvent\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x02 \x01(\t\x12\x32\n\x06status\x18\x03 \x01(\x0e\x32\".deployment.DeploymentEvent.Status\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x17\n\x0flifecycle_event\x18\x06 \x01(\t\"Z\n\x06Status\x12\x0b\n\x07\x43REATED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x32\xb6\x01\n\x08\x44\x65ployer\x12H\n\x06\x44\x65ploy\x12\x1d.deployment.DeploymentRequest\x1a\x1b.deployment.DeploymentEvent\"\x00\x30\x01\x12`\n\x14ListDeploymentEvents\x12\'.deployment.ListDeploymentEventsRequest\x1a\x1b.deployment.DeploymentEvent\"\x00\x30\x01\x42\x11\n\x0f\x62ynd.deploymentb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DEPLOYMENTARTEFACT_BUNDLETYPE = _descriptor.EnumDescriptor(
  name='BundleType',
  full_name='deployment.DeploymentArtefact.BundleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZIP', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=187,
  serialized_end=208,
)
_sym_db.RegisterEnumDescriptor(_DEPLOYMENTARTEFACT_BUNDLETYPE)

_DEPLOYMENTEVENT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='deployment.DeploymentEvent.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=609,
  serialized_end=699,
)
_sym_db.RegisterEnumDescriptor(_DEPLOYMENTEVENT_STATUS)


_DEPLOYMENTARTEFACT = _descriptor.Descriptor(
  name='DeploymentArtefact',
  full_name='deployment.DeploymentArtefact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s3_bucket', full_name='deployment.DeploymentArtefact.s3_bucket', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s3_key', full_name='deployment.DeploymentArtefact.s3_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_type', full_name='deployment.DeploymentArtefact.bundle_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEPLOYMENTARTEFACT_BUNDLETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=208,
)


_DEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='DeploymentRequest',
  full_name='deployment.DeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='deployment.DeploymentRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='environment', full_name='deployment.DeploymentRequest.environment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='artefact', full_name='deployment.DeploymentRequest.artefact', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='deployment.DeploymentRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=339,
)


_LISTDEPLOYMENTEVENTSREQUEST = _descriptor.Descriptor(
  name='ListDeploymentEventsRequest',
  full_name='deployment.ListDeploymentEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='deployment.ListDeploymentEventsRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='environment', full_name='deployment.ListDeploymentEventsRequest.environment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=408,
)


_DEPLOYMENTEVENT = _descriptor.Descriptor(
  name='DeploymentEvent',
  full_name='deployment.DeploymentEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='deployment.DeploymentEvent.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='environment', full_name='deployment.DeploymentEvent.environment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='deployment.DeploymentEvent.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='deployment.DeploymentEvent.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='deployment.DeploymentEvent.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lifecycle_event', full_name='deployment.DeploymentEvent.lifecycle_event', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEPLOYMENTEVENT_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=699,
)

_DEPLOYMENTARTEFACT.fields_by_name['bundle_type'].enum_type = _DEPLOYMENTARTEFACT_BUNDLETYPE
_DEPLOYMENTARTEFACT_BUNDLETYPE.containing_type = _DEPLOYMENTARTEFACT
_DEPLOYMENTREQUEST.fields_by_name['artefact'].message_type = _DEPLOYMENTARTEFACT
_DEPLOYMENTEVENT.fields_by_name['status'].enum_type = _DEPLOYMENTEVENT_STATUS
_DEPLOYMENTEVENT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOYMENTEVENT_STATUS.containing_type = _DEPLOYMENTEVENT
DESCRIPTOR.message_types_by_name['DeploymentArtefact'] = _DEPLOYMENTARTEFACT
DESCRIPTOR.message_types_by_name['DeploymentRequest'] = _DEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['ListDeploymentEventsRequest'] = _LISTDEPLOYMENTEVENTSREQUEST
DESCRIPTOR.message_types_by_name['DeploymentEvent'] = _DEPLOYMENTEVENT

DeploymentArtefact = _reflection.GeneratedProtocolMessageType('DeploymentArtefact', (_message.Message,), dict(
  DESCRIPTOR = _DEPLOYMENTARTEFACT,
  __module__ = 'deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.DeploymentArtefact)
  ))
_sym_db.RegisterMessage(DeploymentArtefact)

DeploymentRequest = _reflection.GeneratedProtocolMessageType('DeploymentRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEPLOYMENTREQUEST,
  __module__ = 'deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.DeploymentRequest)
  ))
_sym_db.RegisterMessage(DeploymentRequest)

ListDeploymentEventsRequest = _reflection.GeneratedProtocolMessageType('ListDeploymentEventsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTDEPLOYMENTEVENTSREQUEST,
  __module__ = 'deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.ListDeploymentEventsRequest)
  ))
_sym_db.RegisterMessage(ListDeploymentEventsRequest)

DeploymentEvent = _reflection.GeneratedProtocolMessageType('DeploymentEvent', (_message.Message,), dict(
  DESCRIPTOR = _DEPLOYMENTEVENT,
  __module__ = 'deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.DeploymentEvent)
  ))
_sym_db.RegisterMessage(DeploymentEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\017bynd.deployment'))
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class BetaDeployerServicer(object):
  """The deployer service definition.
  """
  def Deploy(self, request, context):
    """Sends a greeting
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def ListDeploymentEvents(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaDeployerStub(object):
  """The deployer service definition.
  """
  def Deploy(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Sends a greeting
    """
    raise NotImplementedError()
  def ListDeploymentEvents(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_Deployer_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('deployment.Deployer', 'Deploy'): DeploymentRequest.FromString,
    ('deployment.Deployer', 'ListDeploymentEvents'): ListDeploymentEventsRequest.FromString,
  }
  response_serializers = {
    ('deployment.Deployer', 'Deploy'): DeploymentEvent.SerializeToString,
    ('deployment.Deployer', 'ListDeploymentEvents'): DeploymentEvent.SerializeToString,
  }
  method_implementations = {
    ('deployment.Deployer', 'Deploy'): face_utilities.unary_stream_inline(servicer.Deploy),
    ('deployment.Deployer', 'ListDeploymentEvents'): face_utilities.unary_stream_inline(servicer.ListDeploymentEvents),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Deployer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('deployment.Deployer', 'Deploy'): DeploymentRequest.SerializeToString,
    ('deployment.Deployer', 'ListDeploymentEvents'): ListDeploymentEventsRequest.SerializeToString,
  }
  response_deserializers = {
    ('deployment.Deployer', 'Deploy'): DeploymentEvent.FromString,
    ('deployment.Deployer', 'ListDeploymentEvents'): DeploymentEvent.FromString,
  }
  cardinalities = {
    'Deploy': cardinality.Cardinality.UNARY_STREAM,
    'ListDeploymentEvents': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'deployment.Deployer', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
