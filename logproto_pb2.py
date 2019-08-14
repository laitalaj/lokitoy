# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logproto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='logproto.proto',
  package='logproto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0elogproto.proto\x12\x08logproto\x1a\x1fgoogle/protobuf/timestamp.proto\"0\n\x0bPushRequest\x12!\n\x07streams\x18\x01 \x03(\x0b\x32\x10.logproto.Stream\"\x0e\n\x0cPushResponse\"\xb7\x01\n\x0cQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\r\x12)\n\x05start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\tdirection\x18\x05 \x01(\x0e\x32\x13.logproto.Direction\x12\r\n\x05regex\x18\x06 \x01(\t\"2\n\rQueryResponse\x12!\n\x07streams\x18\x01 \x03(\x0b\x32\x10.logproto.Stream\",\n\x0cLabelRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x01(\x08\"\x1f\n\rLabelResponse\x12\x0e\n\x06values\x18\x01 \x03(\t\":\n\x06Stream\x12\x0e\n\x06labels\x18\x01 \x01(\t\x12 \n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x0f.logproto.Entry\"D\n\x05\x45ntry\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04line\x18\x02 \x01(\t*&\n\tDirection\x12\x0b\n\x07\x46ORWARD\x10\x00\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x01\x32\x41\n\x06Pusher\x12\x37\n\x04Push\x12\x15.logproto.PushRequest\x1a\x16.logproto.PushResponse\"\x00\x32\x83\x01\n\x07Querier\x12<\n\x05Query\x12\x16.logproto.QueryRequest\x1a\x17.logproto.QueryResponse\"\x00\x30\x01\x12:\n\x05Label\x12\x16.logproto.LabelRequest\x1a\x17.logproto.LabelResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='logproto.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORWARD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACKWARD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=574,
  serialized_end=612,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
FORWARD = 0
BACKWARD = 1



_PUSHREQUEST = _descriptor.Descriptor(
  name='PushRequest',
  full_name='logproto.PushRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streams', full_name='logproto.PushRequest.streams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=109,
)


_PUSHRESPONSE = _descriptor.Descriptor(
  name='PushResponse',
  full_name='logproto.PushResponse',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=125,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='logproto.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='logproto.QueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='logproto.QueryRequest.limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='logproto.QueryRequest.start', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='logproto.QueryRequest.end', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='logproto.QueryRequest.direction', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regex', full_name='logproto.QueryRequest.regex', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=311,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='logproto.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streams', full_name='logproto.QueryResponse.streams', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=363,
)


_LABELREQUEST = _descriptor.Descriptor(
  name='LabelRequest',
  full_name='logproto.LabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='logproto.LabelRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='logproto.LabelRequest.values', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=409,
)


_LABELRESPONSE = _descriptor.Descriptor(
  name='LabelResponse',
  full_name='logproto.LabelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='logproto.LabelResponse.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=442,
)


_STREAM = _descriptor.Descriptor(
  name='Stream',
  full_name='logproto.Stream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='logproto.Stream.labels', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='logproto.Stream.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=502,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='logproto.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='logproto.Entry.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='logproto.Entry.line', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=572,
)

_PUSHREQUEST.fields_by_name['streams'].message_type = _STREAM
_QUERYREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_QUERYREQUEST.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_QUERYREQUEST.fields_by_name['direction'].enum_type = _DIRECTION
_QUERYRESPONSE.fields_by_name['streams'].message_type = _STREAM
_STREAM.fields_by_name['entries'].message_type = _ENTRY
_ENTRY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['PushRequest'] = _PUSHREQUEST
DESCRIPTOR.message_types_by_name['PushResponse'] = _PUSHRESPONSE
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['LabelRequest'] = _LABELREQUEST
DESCRIPTOR.message_types_by_name['LabelResponse'] = _LABELRESPONSE
DESCRIPTOR.message_types_by_name['Stream'] = _STREAM
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushRequest = _reflection.GeneratedProtocolMessageType('PushRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUSHREQUEST,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.PushRequest)
  ))
_sym_db.RegisterMessage(PushRequest)

PushResponse = _reflection.GeneratedProtocolMessageType('PushResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUSHRESPONSE,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.PushResponse)
  ))
_sym_db.RegisterMessage(PushResponse)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQUEST,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.QueryRequest)
  ))
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

LabelRequest = _reflection.GeneratedProtocolMessageType('LabelRequest', (_message.Message,), dict(
  DESCRIPTOR = _LABELREQUEST,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.LabelRequest)
  ))
_sym_db.RegisterMessage(LabelRequest)

LabelResponse = _reflection.GeneratedProtocolMessageType('LabelResponse', (_message.Message,), dict(
  DESCRIPTOR = _LABELRESPONSE,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.LabelResponse)
  ))
_sym_db.RegisterMessage(LabelResponse)

Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), dict(
  DESCRIPTOR = _STREAM,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.Stream)
  ))
_sym_db.RegisterMessage(Stream)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
  DESCRIPTOR = _ENTRY,
  __module__ = 'logproto_pb2'
  # @@protoc_insertion_point(class_scope:logproto.Entry)
  ))
_sym_db.RegisterMessage(Entry)



_PUSHER = _descriptor.ServiceDescriptor(
  name='Pusher',
  full_name='logproto.Pusher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=614,
  serialized_end=679,
  methods=[
  _descriptor.MethodDescriptor(
    name='Push',
    full_name='logproto.Pusher.Push',
    index=0,
    containing_service=None,
    input_type=_PUSHREQUEST,
    output_type=_PUSHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUSHER)

DESCRIPTOR.services_by_name['Pusher'] = _PUSHER


_QUERIER = _descriptor.ServiceDescriptor(
  name='Querier',
  full_name='logproto.Querier',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=682,
  serialized_end=813,
  methods=[
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='logproto.Querier.Query',
    index=0,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Label',
    full_name='logproto.Querier.Label',
    index=1,
    containing_service=None,
    input_type=_LABELREQUEST,
    output_type=_LABELRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERIER)

DESCRIPTOR.services_by_name['Querier'] = _QUERIER

# @@protoc_insertion_point(module_scope)
