# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/eugene/file/fileservice.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*experimental/eugene/file/fileservice.proto\x12!cohesity.experimental.eugene.file\x1a\x1copen_util/net/protorpc.proto\"%\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"!\n\x10\x43reateFileResult\x12\r\n\x05\x65rror\x18\x01 \x02(\r\"J\n\x15WriteFileRangeRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x11\n\x06offset\x18\x03 \x01(\r:\x01\x30\"<\n\x14WriteFileRangeResult\x12\r\n\x05\x65rror\x18\x01 \x02(\r\x12\x15\n\rbytes_written\x18\x02 \x02(\x05\"J\n\x14ReadFileRangeRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x02(\r\x12\x11\n\x06offset\x18\x03 \x01(\r:\x01\x30\"F\n\x13ReadFileRangeResult\x12\r\n\x05\x65rror\x18\x01 \x02(\r\x12\x12\n\nbytes_read\x18\x02 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x32\xa4\x03\n\x0b\x46ileService\x12y\n\nCreateFile\x12\x34.cohesity.experimental.eugene.file.CreateFileRequest\x1a\x33.cohesity.experimental.eugene.file.CreateFileResult\"\x00\x12\x85\x01\n\x0eWriteFileRange\x12\x38.cohesity.experimental.eugene.file.WriteFileRangeRequest\x1a\x37.cohesity.experimental.eugene.file.WriteFileRangeResult\"\x00\x12\x82\x01\n\rReadFileRange\x12\x37.cohesity.experimental.eugene.file.ReadFileRangeRequest\x1a\x36.cohesity.experimental.eugene.file.ReadFileRangeResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.eugene.file.fileservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEREQUEST']._serialized_start=111
  _globals['_CREATEFILEREQUEST']._serialized_end=148
  _globals['_CREATEFILERESULT']._serialized_start=150
  _globals['_CREATEFILERESULT']._serialized_end=183
  _globals['_WRITEFILERANGEREQUEST']._serialized_start=185
  _globals['_WRITEFILERANGEREQUEST']._serialized_end=259
  _globals['_WRITEFILERANGERESULT']._serialized_start=261
  _globals['_WRITEFILERANGERESULT']._serialized_end=321
  _globals['_READFILERANGEREQUEST']._serialized_start=323
  _globals['_READFILERANGEREQUEST']._serialized_end=397
  _globals['_READFILERANGERESULT']._serialized_start=399
  _globals['_READFILERANGERESULT']._serialized_end=469
  _globals['_FILESERVICE']._serialized_start=472
  _globals['_FILESERVICE']._serialized_end=892
# @@protoc_insertion_point(module_scope)
