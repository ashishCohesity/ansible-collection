# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/deepansh/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,experimental/deepansh/rpc/file_service.proto\x12\"cohesity.experimental.deepansh.rpc\x1a\x1copen_util/net/protorpc.proto\"\x1d\n\rCreateFileArg\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x12\n\x10\x43reateFileResult\"8\n\x0bReadFileArg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0b\n\x03len\x18\x03 \x01(\x03\"\x10\n\x0eReadFileResult\"9\n\x0cWriteFileArg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0b\n\x03len\x18\x03 \x01(\x03\"&\n\x0fWriteFileResult\x12\x13\n\x0bservice_num\x18\x01 \x01(\x03\x32\xfe\x02\n\x0b\x46ileService\x12w\n\nCreateFile\x12\x31.cohesity.experimental.deepansh.rpc.CreateFileArg\x1a\x34.cohesity.experimental.deepansh.rpc.CreateFileResult\"\x00\x12q\n\x08ReadFile\x12/.cohesity.experimental.deepansh.rpc.ReadFileArg\x1a\x32.cohesity.experimental.deepansh.rpc.ReadFileResult\"\x00\x12t\n\tWriteFile\x12\x30.cohesity.experimental.deepansh.rpc.WriteFileArg\x1a\x33.cohesity.experimental.deepansh.rpc.WriteFileResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.deepansh.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEARG']._serialized_start=114
  _globals['_CREATEFILEARG']._serialized_end=143
  _globals['_CREATEFILERESULT']._serialized_start=145
  _globals['_CREATEFILERESULT']._serialized_end=163
  _globals['_READFILEARG']._serialized_start=165
  _globals['_READFILEARG']._serialized_end=221
  _globals['_READFILERESULT']._serialized_start=223
  _globals['_READFILERESULT']._serialized_end=239
  _globals['_WRITEFILEARG']._serialized_start=241
  _globals['_WRITEFILEARG']._serialized_end=298
  _globals['_WRITEFILERESULT']._serialized_start=300
  _globals['_WRITEFILERESULT']._serialized_end=338
  _globals['_FILESERVICE']._serialized_start=341
  _globals['_FILESERVICE']._serialized_end=723
# @@protoc_insertion_point(module_scope)