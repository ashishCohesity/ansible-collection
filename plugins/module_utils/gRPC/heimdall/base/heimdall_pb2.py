# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heimdall/base/heimdall.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from heimdall.base import error_pb2 as heimdall_dot_base_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cheimdall/base/heimdall.proto\x12\x16\x63ohesity.heimdall.base\x1a\x19heimdall/base/error.proto\"\\\n\x12LookupMasterResult\x12,\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.cohesity.heimdall.ErrorProto\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'heimdall.base.heimdall_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOOKUPMASTERRESULT']._serialized_start=83
  _globals['_LOOKUPMASTERRESULT']._serialized_end=175
# @@protoc_insertion_point(module_scope)
