# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/smidth/sfs/server/stub/sfs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-experimental/smidth/sfs/server/stub/sfs.proto\x12\x18\x63ohesity.sfs.server.stub\x1a\x1copen_util/net/protorpc.proto\"\"\n\rCreateFileArg\x12\x11\n\tfile_name\x18\x01 \x02(\t\"\x12\n\x10\x43reateFileResult2x\n\nRpcService\x12\x63\n\nCreateFile\x12\'.cohesity.sfs.server.stub.CreateFileArg\x1a*.cohesity.sfs.server.stub.CreateFileResult\"\x00\x1a\x05\x80\xf1\x04\x90NB\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.smidth.sfs.server.stub.sfs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_RPCSERVICE']._loaded_options = None
  _globals['_RPCSERVICE']._serialized_options = b'\200\361\004\220N'
  _globals['_CREATEFILEARG']._serialized_start=105
  _globals['_CREATEFILEARG']._serialized_end=139
  _globals['_CREATEFILERESULT']._serialized_start=141
  _globals['_CREATEFILERESULT']._serialized_end=159
  _globals['_RPCSERVICE']._serialized_start=161
  _globals['_RPCSERVICE']._serialized_end=281
# @@protoc_insertion_point(module_scope)
