# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: open_util/qa/test/fork_helper_test.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(open_util/qa/test/fork_helper_test.proto\x12\x10\x63ohesity.qa.test\x1a\x1copen_util/net/protorpc.proto\"\x1c\n\x0b\x44ummyRpcArg\x12\r\n\x05value\x18\x01 \x02(\x05\"\x1f\n\x0e\x44ummyRpcResult\x12\r\n\x05value\x18\x01 \x02(\x05\x32g\n\x11\x46orkHelperTestSvc\x12K\n\x08\x44ummyRpc\x12\x1d.cohesity.qa.test.DummyRpcArg\x1a .cohesity.qa.test.DummyRpcResult\x1a\x05\x80\xf1\x04\xe8\x07\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'open_util.qa.test.fork_helper_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FORKHELPERTESTSVC']._loaded_options = None
  _globals['_FORKHELPERTESTSVC']._serialized_options = b'\200\361\004\350\007'
  _globals['_DUMMYRPCARG']._serialized_start=92
  _globals['_DUMMYRPCARG']._serialized_end=120
  _globals['_DUMMYRPCRESULT']._serialized_start=122
  _globals['_DUMMYRPCRESULT']._serialized_end=153
  _globals['_FORKHELPERTESTSVC']._serialized_start=155
  _globals['_FORKHELPERTESTSVC']._serialized_end=258
# @@protoc_insertion_point(module_scope)
