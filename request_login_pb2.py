# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_login.proto

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
  name='request_login.proto',
  package='rti',
  serialized_pb=_b('\n\x13request_login.proto\x12\x03rti\"\xba\x03\n\x0cRequestLogin\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x1a\n\x10template_version\x18\xa2\xb0\t \x01(\t\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x0e\n\x04user\x18\xbb\xff\x07 \x01(\t\x12\x12\n\x08password\x18\xd4\xf7\x07 \x01(\t\x12\x12\n\x08\x61pp_name\x18\xd2\xf7\x07 \x01(\t\x12\x15\n\x0b\x61pp_version\x18\xdb\x85\x08 \x01(\t\x12\x15\n\x0bsystem_name\x18\x9c\xb0\t \x01(\t\x12\x34\n\ninfra_type\x18\x95\xb0\t \x01(\x0e\x32\x1e.rti.RequestLogin.SysInfraType\x12\x12\n\x08mac_addr\x18\xec\xe5\x08 \x03(\t\x12\x14\n\nos_version\x18\x95\xe5\x08 \x01(\t\x12\x15\n\x0bos_platform\x18\x94\xe5\x08 \x01(\t\x12\x1b\n\x11\x61ggregated_quotes\x18\xac\xb0\t \x01(\x08\"i\n\x0cSysInfraType\x12\x10\n\x0cTICKER_PLANT\x10\x01\x12\x0f\n\x0bORDER_PLANT\x10\x02\x12\x11\n\rHISTORY_PLANT\x10\x03\x12\r\n\tPNL_PLANT\x10\x04\x12\x14\n\x10REPOSITORY_PLANT\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REQUESTLOGIN_SYSINFRATYPE = _descriptor.EnumDescriptor(
  name='SysInfraType',
  full_name='rti.RequestLogin.SysInfraType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TICKER_PLANT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_PLANT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HISTORY_PLANT', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PNL_PLANT', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPOSITORY_PLANT', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=366,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_REQUESTLOGIN_SYSINFRATYPE)


_REQUESTLOGIN = _descriptor.Descriptor(
  name='RequestLogin',
  full_name='rti.RequestLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.RequestLogin.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='template_version', full_name='rti.RequestLogin.template_version', index=1,
      number=153634, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.RequestLogin.user_msg', index=2,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='rti.RequestLogin.user', index=3,
      number=131003, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='rti.RequestLogin.password', index=4,
      number=130004, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='rti.RequestLogin.app_name', index=5,
      number=130002, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='rti.RequestLogin.app_version', index=6,
      number=131803, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_name', full_name='rti.RequestLogin.system_name', index=7,
      number=153628, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infra_type', full_name='rti.RequestLogin.infra_type', index=8,
      number=153621, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac_addr', full_name='rti.RequestLogin.mac_addr', index=9,
      number=144108, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='os_version', full_name='rti.RequestLogin.os_version', index=10,
      number=144021, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='os_platform', full_name='rti.RequestLogin.os_platform', index=11,
      number=144020, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aggregated_quotes', full_name='rti.RequestLogin.aggregated_quotes', index=12,
      number=153644, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTLOGIN_SYSINFRATYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=471,
)

_REQUESTLOGIN.fields_by_name['infra_type'].enum_type = _REQUESTLOGIN_SYSINFRATYPE
_REQUESTLOGIN_SYSINFRATYPE.containing_type = _REQUESTLOGIN
DESCRIPTOR.message_types_by_name['RequestLogin'] = _REQUESTLOGIN

RequestLogin = _reflection.GeneratedProtocolMessageType('RequestLogin', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTLOGIN,
  __module__ = 'request_login_pb2'
  # @@protoc_insertion_point(class_scope:rti.RequestLogin)
  ))
_sym_db.RegisterMessage(RequestLogin)


# @@protoc_insertion_point(module_scope)
