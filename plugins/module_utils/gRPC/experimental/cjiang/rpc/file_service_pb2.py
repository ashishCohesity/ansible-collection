# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/cjiang/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*experimental/cjiang/rpc/file_service.proto\x12\x1c\x63ohesity.experimental.cjiang\x1a\x1copen_util/net/protorpc.proto\"\x1d\n\rCreateFileReq\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x10ReadFileRangeReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\"?\n\x11WriteFileRangeReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\x0c\"#\n\x10\x43reateFileResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\"4\n\x13ReadFileRangeResult\x12\x0c\n\x04text\x18\x01 \x01(\x0c\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\'\n\x14WriteFileRangeResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xf8\x02\n\x0b\x46ileService\x12k\n\nCreateFile\x12+.cohesity.experimental.cjiang.CreateFileReq\x1a..cohesity.experimental.cjiang.CreateFileResult\"\x00\x12t\n\rReadFileRange\x12..cohesity.experimental.cjiang.ReadFileRangeReq\x1a\x31.cohesity.experimental.cjiang.ReadFileRangeResult\"\x00\x12w\n\x0eWriteFileRange\x12/.cohesity.experimental.cjiang.WriteFileRangeReq\x1a\x32.cohesity.experimental.cjiang.WriteFileRangeResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.cjiang.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEREQ']._serialized_start=106
  _globals['_CREATEFILEREQ']._serialized_end=135
  _globals['_READFILERANGEREQ']._serialized_start=137
  _globals['_READFILERANGEREQ']._serialized_end=201
  _globals['_WRITEFILERANGEREQ']._serialized_start=203
  _globals['_WRITEFILERANGEREQ']._serialized_end=266
  _globals['_CREATEFILERESULT']._serialized_start=268
  _globals['_CREATEFILERESULT']._serialized_end=303
  _globals['_READFILERANGERESULT']._serialized_start=305
  _globals['_READFILERANGERESULT']._serialized_end=357
  _globals['_WRITEFILERANGERESULT']._serialized_start=359
  _globals['_WRITEFILERANGERESULT']._serialized_end=398
  _globals['_FILESERVICE']._serialized_start=401
  _globals['_FILESERVICE']._serialized_end=777
# @@protoc_insertion_point(module_scope)
