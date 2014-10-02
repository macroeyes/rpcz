# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpcz.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpcz.proto',
  package='rpcz',
  serialized_pb=_b('\n\nrpcz.proto\x12\x04rpcz\"Y\n\x12rpc_request_header\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x03\x12\x10\n\x08\x64\x65\x61\x64line\x18\x02 \x01(\x05\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\"\xbf\x03\n\x13rpc_response_header\x12\x39\n\x06status\x18\x01 \x01(\x0e\x32%.rpcz.rpc_response_header.status_code:\x02OK\x12\x1c\n\x11\x61pplication_error\x18\x02 \x01(\x05:\x01\x30\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"|\n\x0bstatus_code\x12\x0c\n\x08INACTIVE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x06\n\x02OK\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x15\n\x11\x41PPLICATION_ERROR\x10\x04\x12\x15\n\x11\x44\x45\x41\x44LINE_EXCEEDED\x10\x05\x12\x0e\n\nTERMINATED\x10\x06\"\xc1\x01\n\x16\x61pplication_error_code\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x1b\n\x0eINVALID_HEADER\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fNO_SUCH_SERVICE\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1b\n\x0eNO_SUCH_METHOD\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fINVALID_MESSAGE\x10\xfc\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x16METHOD_NOT_IMPLEMENTED\x10\xfb\xff\xff\xff\xff\xff\xff\xff\xff\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RPC_RESPONSE_HEADER_STATUS_CODE = _descriptor.EnumDescriptor(
  name='status_code',
  full_name='rpcz.rpc_response_header.status_code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_ERROR', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEADLINE_EXCEEDED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TERMINATED', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=239,
  serialized_end=363,
)
_sym_db.RegisterEnumDescriptor(_RPC_RESPONSE_HEADER_STATUS_CODE)

_RPC_RESPONSE_HEADER_APPLICATION_ERROR_CODE = _descriptor.EnumDescriptor(
  name='application_error_code',
  full_name='rpcz.rpc_response_header.application_error_code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_HEADER', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SUCH_SERVICE', index=2, number=-2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_SUCH_METHOD', index=3, number=-3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MESSAGE', index=4, number=-4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='METHOD_NOT_IMPLEMENTED', index=5, number=-5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=366,
  serialized_end=559,
)
_sym_db.RegisterEnumDescriptor(_RPC_RESPONSE_HEADER_APPLICATION_ERROR_CODE)


_RPC_REQUEST_HEADER = _descriptor.Descriptor(
  name='rpc_request_header',
  full_name='rpcz.rpc_request_header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='rpcz.rpc_request_header.event_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='rpcz.rpc_request_header.deadline', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service', full_name='rpcz.rpc_request_header.service', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='rpcz.rpc_request_header.method', index=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=109,
)


_RPC_RESPONSE_HEADER = _descriptor.Descriptor(
  name='rpc_response_header',
  full_name='rpcz.rpc_response_header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='rpcz.rpc_response_header.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='application_error', full_name='rpcz.rpc_response_header.application_error', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='rpcz.rpc_response_header.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RPC_RESPONSE_HEADER_STATUS_CODE,
    _RPC_RESPONSE_HEADER_APPLICATION_ERROR_CODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=559,
)

_RPC_RESPONSE_HEADER.fields_by_name['status'].enum_type = _RPC_RESPONSE_HEADER_STATUS_CODE
_RPC_RESPONSE_HEADER_STATUS_CODE.containing_type = _RPC_RESPONSE_HEADER
_RPC_RESPONSE_HEADER_APPLICATION_ERROR_CODE.containing_type = _RPC_RESPONSE_HEADER
DESCRIPTOR.message_types_by_name['rpc_request_header'] = _RPC_REQUEST_HEADER
DESCRIPTOR.message_types_by_name['rpc_response_header'] = _RPC_RESPONSE_HEADER

rpc_request_header = _reflection.GeneratedProtocolMessageType('rpc_request_header', (_message.Message,), dict(
  DESCRIPTOR = _RPC_REQUEST_HEADER,
  __module__ = 'rpcz_pb2'
  # @@protoc_insertion_point(class_scope:rpcz.rpc_request_header)
  ))
_sym_db.RegisterMessage(rpc_request_header)

rpc_response_header = _reflection.GeneratedProtocolMessageType('rpc_response_header', (_message.Message,), dict(
  DESCRIPTOR = _RPC_RESPONSE_HEADER,
  __module__ = 'rpcz_pb2'
  # @@protoc_insertion_point(class_scope:rpcz.rpc_response_header)
  ))
_sym_db.RegisterMessage(rpc_response_header)


# @@protoc_insertion_point(module_scope)
