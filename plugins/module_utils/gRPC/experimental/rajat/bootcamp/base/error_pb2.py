# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/rajat/bootcamp/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,experimental/rajat/bootcamp/base/error.proto\x12)cohesity.experimental.rajat.bootcamp.base\x1a\x1copen_util/net/protorpc.proto\"\xb3\x02\n\nErrorProto\x12X\n\nerror_type\x18\x01 \x01(\x0e\x32:.cohesity.experimental.rajat.bootcamp.base.ErrorProto.Type:\x08kNoError\x12\x13\n\terror_msg\x18\x02 \x01(\t:\x00\"\xb5\x01\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\r\n\tkFileOpen\x10\x01\x12\x0f\n\x0bkFileCreate\x10\x02\x12\x11\n\rkFileNotFound\x10\x03\x12\x0f\n\x0bkFileExists\x10\x04\x12\r\n\tkFileRead\x10\x05\x12\x0e\n\nkFileWrite\x10\x06\x12\x12\n\x0ekFileWriteLess\x10\x07\x12\n\n\x06kRetry\x10\x08\x12\x0c\n\x08kTimeout\x10\t\x12\x0e\n\nkTransport\x10\n')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.rajat.bootcamp.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ERRORPROTO']._serialized_start=122
  _globals['_ERRORPROTO']._serialized_end=429
  _globals['_ERRORPROTO_TYPE']._serialized_start=248
  _globals['_ERRORPROTO_TYPE']._serialized_end=429
# @@protoc_insertion_point(module_scope)