# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smurugesan/protobuf-3.6.0/python/google/protobuf/internal/more_extensions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\\experimental/smurugesan/protobuf-3.6.0/python/google/protobuf/internal/more_extensions.proto\x12\x18google.protobuf.internal\"P\n\x0fTopLevelMessage\x12=\n\nsubmessage\x18\x01 \x01(\x0b\x32).google.protobuf.internal.ExtendedMessage\"\x1b\n\x0f\x45xtendedMessage*\x08\x08\x01\x10\x80\x80\x80\x80\x02\"-\n\x0e\x46oreignMessage\x12\x1b\n\x13\x66oreign_message_int\x18\x01 \x01(\x05:I\n\x16optional_int_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x01 \x01(\x05:w\n\x1aoptional_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x02 \x01(\x0b\x32(.google.protobuf.internal.ForeignMessage:I\n\x16repeated_int_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x03 \x03(\x05:w\n\x1arepeated_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x04 \x03(\x0b\x32(.google.protobuf.internal.ForeignMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smurugesan.protobuf_3.6.0.python.google.protobuf.internal.more_extensions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TOPLEVELMESSAGE']._serialized_start=122
  _globals['_TOPLEVELMESSAGE']._serialized_end=202
  _globals['_EXTENDEDMESSAGE']._serialized_start=204
  _globals['_EXTENDEDMESSAGE']._serialized_end=231
  _globals['_FOREIGNMESSAGE']._serialized_start=233
  _globals['_FOREIGNMESSAGE']._serialized_end=278
# @@protoc_insertion_point(module_scope)
