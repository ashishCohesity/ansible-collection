# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pubsub/base/error.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17pubsub/base/error.proto\x12\x0f\x63ohesity.pubsub\"\xed\x02\n\nErrorProto\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32 .cohesity.pubsub.ErrorProto.Type:\x08kNoError\x12\x11\n\terror_msg\x18\x02 \x01(\t\"\x91\x02\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x13\n\x0fkTransportError\x10\x01\x12\x0c\n\x08kTimeout\x10\x02\x12\n\n\x06kRetry\x10\x03\x12\x0e\n\nkNotLeader\x10\x04\x12\x0c\n\x08kInvalid\x10\x05\x12\x0f\n\x0bkParseError\x10\x07\x12\x17\n\x13kServiceUnavailable\x10\x08\x12\x11\n\rkAccessDenied\x10\t\x12\x0c\n\x08kCorrupt\x10\x0b\x12\r\n\tkNotFound\x10\x0c\x12\x11\n\rkShardFailure\x10\r\x12\x0c\n\x08kFsError\x10\x0e\x12\x0c\n\x08kIOError\x10\x0f\x12\x11\n\rkUnknownError\x10\x10\x12\x12\n\x0ekConsumerError\x10\x11\x42+\n\x13\x63om.cohesity.pubsubZ\x14pubsub/base/error.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pubsub.base.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.cohesity.pubsubZ\024pubsub/base/error.pb'
  _globals['_ERRORPROTO']._serialized_start=45
  _globals['_ERRORPROTO']._serialized_end=410
  _globals['_ERRORPROTO_TYPE']._serialized_start=137
  _globals['_ERRORPROTO_TYPE']._serialized_end=410
# @@protoc_insertion_point(module_scope)
