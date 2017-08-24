# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ddzproto.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ddzproto.proto',
  package='DDZProto',
  serialized_pb='\n\x0e\x64\x64zproto.proto\x12\x08\x44\x44ZProto\"x\n\nDDZMessage\x12\"\n\x07request\x18\x01 \x01(\x0b\x32\x11.DDZProto.Request\x12$\n\x08response\x18\x02 \x01(\x0b\x32\x12.DDZProto.Response\x12 \n\x06notify\x18\x03 \x01(\x0b\x32\x10.DDZProto.Notify\"#\n\x07Request\x12\x0e\n\x06serial\x18\x01 \x01(\r*\x08\x08\n\x10\x80\x80\x80\x80\x02\"p\n\x08Response\x12\x0e\n\x06serial\x18\x01 \x01(\r\x12&\n\terrorCode\x18\x02 \x02(\x0e\x32\x13.DDZProto.ErrorCode\x12\x14\n\x0c\x65rrorMessage\x18\x03 \x01(\t\x12\x0c\n\x04\x63oin\x18\x04 \x01(\x01*\x08\x08\n\x10\x80\x80\x80\x80\x02\"\x12\n\x06Notify*\x08\x08\n\x10\x80\x80\x80\x80\x02\"\x17\n\x0b\x41uthRequest*\x08\x08\n\x10\x80\x80\x80\x80\x02\"\x18\n\x0c\x41uthResponse*\x08\x08\n\x10\x80\x80\x80\x80\x02\"9\n\x10UserLoginRequest\x12\x13\n\x0b\x61\x63\x63ountName\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x11UserLoginResponse\x12\r\n\x05token\x18\x02 \x01(\t*\xa5\x01\n\tErrorCode\x12\r\n\tE_Success\x10\x00\x12\r\n\tE_Unknown\x10\x01\x12\x0e\n\nE_WrongUrl\x10\x02\x12\x13\n\x0f\x45_NotSupportXHR\x10\x03\x12\x17\n\x11\x45_AccountNotExist\x10\x81\x80\x04\x12\x16\n\x10\x45_MoneyNotEnough\x10\x81\x80\x08\x12\x14\n\x0e\x45_TokenInvalid\x10\x81\x80\x0c\x12\x0e\n\x08\x45_Others\x10\x81\x80\x10:=\n\x0b\x61uthRequest\x12\x11.DDZProto.Request\x18\x0b \x01(\x0b\x32\x15.DDZProto.AuthRequest:@\n\x0c\x61uthResponse\x12\x12.DDZProto.Response\x18\x0b \x01(\x0b\x32\x16.DDZProto.AuthResponse:D\n\tuserLogin\x12\x15.DDZProto.AuthRequest\x18\r \x01(\x0b\x32\x1a.DDZProto.UserLoginRequest:N\n\x11userLoginResponse\x12\x16.DDZProto.AuthResponse\x18\r \x01(\x0b\x32\x1b.DDZProto.UserLoginResponse')

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='DDZProto.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='E_Success', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_Unknown', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_WrongUrl', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_NotSupportXHR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_AccountNotExist', index=4, number=65537,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_MoneyNotEnough', index=5, number=131073,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_TokenInvalid', index=6, number=196609,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_Others', index=7, number=262145,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=468,
  serialized_end=633,
)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
E_Success = 0
E_Unknown = 1
E_WrongUrl = 2
E_NotSupportXHR = 3
E_AccountNotExist = 65537
E_MoneyNotEnough = 131073
E_TokenInvalid = 196609
E_Others = 262145

AUTHREQUEST_FIELD_NUMBER = 11
authRequest = _descriptor.FieldDescriptor(
  name='authRequest', full_name='DDZProto.authRequest', index=0,
  number=11, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
AUTHRESPONSE_FIELD_NUMBER = 11
authResponse = _descriptor.FieldDescriptor(
  name='authResponse', full_name='DDZProto.authResponse', index=1,
  number=11, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
USERLOGIN_FIELD_NUMBER = 13
userLogin = _descriptor.FieldDescriptor(
  name='userLogin', full_name='DDZProto.userLogin', index=2,
  number=13, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
USERLOGINRESPONSE_FIELD_NUMBER = 13
userLoginResponse = _descriptor.FieldDescriptor(
  name='userLoginResponse', full_name='DDZProto.userLoginResponse', index=3,
  number=13, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_DDZMESSAGE = _descriptor.Descriptor(
  name='DDZMessage',
  full_name='DDZProto.DDZMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='DDZProto.DDZMessage.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='DDZProto.DDZMessage.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notify', full_name='DDZProto.DDZMessage.notify', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=28,
  serialized_end=148,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='DDZProto.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial', full_name='DDZProto.Request.serial', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  is_extendable=True,
  extension_ranges=[(10, 536870912), ],
  serialized_start=150,
  serialized_end=185,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='DDZProto.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serial', full_name='DDZProto.Response.serial', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='DDZProto.Response.errorCode', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='DDZProto.Response.errorMessage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coin', full_name='DDZProto.Response.coin', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
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
  is_extendable=True,
  extension_ranges=[(10, 536870912), ],
  serialized_start=187,
  serialized_end=299,
)


_NOTIFY = _descriptor.Descriptor(
  name='Notify',
  full_name='DDZProto.Notify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10, 536870912), ],
  serialized_start=301,
  serialized_end=319,
)


_AUTHREQUEST = _descriptor.Descriptor(
  name='AuthRequest',
  full_name='DDZProto.AuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10, 536870912), ],
  serialized_start=321,
  serialized_end=344,
)


_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='DDZProto.AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(10, 536870912), ],
  serialized_start=346,
  serialized_end=370,
)


_USERLOGINREQUEST = _descriptor.Descriptor(
  name='UserLoginRequest',
  full_name='DDZProto.UserLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountName', full_name='DDZProto.UserLoginRequest.accountName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='DDZProto.UserLoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=372,
  serialized_end=429,
)


_USERLOGINRESPONSE = _descriptor.Descriptor(
  name='UserLoginResponse',
  full_name='DDZProto.UserLoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='DDZProto.UserLoginResponse.token', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=431,
  serialized_end=465,
)

_DDZMESSAGE.fields_by_name['request'].message_type = _REQUEST
_DDZMESSAGE.fields_by_name['response'].message_type = _RESPONSE
_DDZMESSAGE.fields_by_name['notify'].message_type = _NOTIFY
_RESPONSE.fields_by_name['errorCode'].enum_type = _ERRORCODE
DESCRIPTOR.message_types_by_name['DDZMessage'] = _DDZMESSAGE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Notify'] = _NOTIFY
DESCRIPTOR.message_types_by_name['AuthRequest'] = _AUTHREQUEST
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
DESCRIPTOR.message_types_by_name['UserLoginRequest'] = _USERLOGINREQUEST
DESCRIPTOR.message_types_by_name['UserLoginResponse'] = _USERLOGINRESPONSE

class DDZMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DDZMESSAGE

  # @@protoc_insertion_point(class_scope:DDZProto.DDZMessage)

class Request(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUEST

  # @@protoc_insertion_point(class_scope:DDZProto.Request)

class Response(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE

  # @@protoc_insertion_point(class_scope:DDZProto.Response)

class Notify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NOTIFY

  # @@protoc_insertion_point(class_scope:DDZProto.Notify)

class AuthRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHREQUEST

  # @@protoc_insertion_point(class_scope:DDZProto.AuthRequest)

class AuthResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHRESPONSE

  # @@protoc_insertion_point(class_scope:DDZProto.AuthResponse)

class UserLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERLOGINREQUEST

  # @@protoc_insertion_point(class_scope:DDZProto.UserLoginRequest)

class UserLoginResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERLOGINRESPONSE

  # @@protoc_insertion_point(class_scope:DDZProto.UserLoginResponse)

authRequest.message_type = _AUTHREQUEST
Request.RegisterExtension(authRequest)
authResponse.message_type = _AUTHRESPONSE
Response.RegisterExtension(authResponse)
userLogin.message_type = _USERLOGINREQUEST
AuthRequest.RegisterExtension(userLogin)
userLoginResponse.message_type = _USERLOGINRESPONSE
AuthResponse.RegisterExtension(userLoginResponse)

# @@protoc_insertion_point(module_scope)