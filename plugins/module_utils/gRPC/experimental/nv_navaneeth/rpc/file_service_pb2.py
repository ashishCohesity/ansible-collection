# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/nv_navaneeth/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0experimental/nv_navaneeth/rpc/file_service.proto\x12&cohesity.experimental.nv_navaneeth.rpc\x1a\x1copen_util/net/protorpc.proto\"\"\n\rCreateFileArg\x12\x11\n\tfile_name\x18\x01 \x02(\t\"7\n\x10\x43reateFileResult\x12\x12\n\nis_success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rr_str\x18\x02 \x01(\t\"E\n\x10ReadFileRangeArg\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x0e\n\x06length\x18\x03 \x02(\x03\"P\n\x13ReadFileRangeResult\x12\x12\n\nis_success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rr_str\x18\x02 \x01(\t\x12\x14\n\x0csequence_num\x18\x03 \x01(\x03\"6\n\x11WriteFileRangeArg\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\"l\n\x14WriteFileRangeResult\x12\x12\n\nis_success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rr_str\x18\x02 \x01(\t\x12\x19\n\x11num_bytes_written\x18\x03 \x01(\x03\x12\x14\n\x0csequence_num\x18\x04 \x01(\x03\x32\xae\x03\n\x0b\x46ileService\x12\x7f\n\nCreateFile\x12\x35.cohesity.experimental.nv_navaneeth.rpc.CreateFileArg\x1a\x38.cohesity.experimental.nv_navaneeth.rpc.CreateFileResult\"\x00\x12\x88\x01\n\rReadFileRange\x12\x38.cohesity.experimental.nv_navaneeth.rpc.ReadFileRangeArg\x1a;.cohesity.experimental.nv_navaneeth.rpc.ReadFileRangeResult\"\x00\x12\x8b\x01\n\x0eWriteFileRange\x12\x39.cohesity.experimental.nv_navaneeth.rpc.WriteFileRangeArg\x1a<.cohesity.experimental.nv_navaneeth.rpc.WriteFileRangeResult\"\x00\x1a\x05\x80\xf1\x04\xf4\x03\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.nv_navaneeth.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\364\003'
  _globals['_CREATEFILEARG']._serialized_start=122
  _globals['_CREATEFILEARG']._serialized_end=156
  _globals['_CREATEFILERESULT']._serialized_start=158
  _globals['_CREATEFILERESULT']._serialized_end=213
  _globals['_READFILERANGEARG']._serialized_start=215
  _globals['_READFILERANGEARG']._serialized_end=284
  _globals['_READFILERANGERESULT']._serialized_start=286
  _globals['_READFILERANGERESULT']._serialized_end=366
  _globals['_WRITEFILERANGEARG']._serialized_start=368
  _globals['_WRITEFILERANGEARG']._serialized_end=422
  _globals['_WRITEFILERANGERESULT']._serialized_start=424
  _globals['_WRITEFILERANGERESULT']._serialized_end=532
  _globals['_FILESERVICE']._serialized_start=535
  _globals['_FILESERVICE']._serialized_end=965
# @@protoc_insertion_point(module_scope)
