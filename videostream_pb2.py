# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: videostream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11videostream.proto\"\x15\n\x05\x46rame\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x16\n\x06Result\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32+\n\x0bVideoStream\x12\x1c\n\x05Infer\x12\x06.Frame\x1a\x07.Result(\x01\x30\x01\x62\x06proto3')



_FRAME = DESCRIPTOR.message_types_by_name['Frame']
_RESULT = DESCRIPTOR.message_types_by_name['Result']
Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), {
  'DESCRIPTOR' : _FRAME,
  '__module__' : 'videostream_pb2'
  # @@protoc_insertion_point(class_scope:Frame)
  })
_sym_db.RegisterMessage(Frame)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'videostream_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  })
_sym_db.RegisterMessage(Result)

_VIDEOSTREAM = DESCRIPTOR.services_by_name['VideoStream']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FRAME._serialized_start=21
  _FRAME._serialized_end=42
  _RESULT._serialized_start=44
  _RESULT._serialized_end=66
  _VIDEOSTREAM._serialized_start=68
  _VIDEOSTREAM._serialized_end=111
# @@protoc_insertion_point(module_scope)