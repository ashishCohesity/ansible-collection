# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/stub/rpc_common_args.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.base import error_pb2 as bridge_dot_base_dot_error__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!bridge/stub/rpc_common_args.proto\x12\x14\x63ohesity.bridge.stub\x1a\x17\x62ridge/base/error.proto\x1a\x18util/base/op_clock.proto\"\x98\x01\n\x15\x42ridgeActionUpdateArg\x12#\n\x08op_clock\x18\x01 \x01(\x0b\x32\x11.cohesity.OpClock\x12\x0f\n\x07task_id\x18\x02 \x01(\x03\x12\x13\n\x0bsub_task_id\x18\x03 \x01(\x03\x12*\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x1b.cohesity.bridge.ErrorProto*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x1a\n\x18\x42ridgeActionUpdateResult')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.stub.rpc_common_args_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BRIDGEACTIONUPDATEARG']._serialized_start=111
  _globals['_BRIDGEACTIONUPDATEARG']._serialized_end=263
  _globals['_BRIDGEACTIONUPDATERESULT']._serialized_start=265
  _globals['_BRIDGEACTIONUPDATERESULT']._serialized_end=291
# @@protoc_insertion_point(module_scope)