# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/emal/chunkservice/chunkservice.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1experimental/emal/chunkservice/chunkservice.proto\x12\x0c\x63hunkservice\"&\n\x11\x43reateFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"T\n\x15WriteFileRangeRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"E\n\x14ReadFileRangeRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x04\"0\n\x08Response\x12$\n\x06result\x18\x01 \x01(\x0e\x32\x14.chunkservice.Result\"B\n\x0cReadResponse\x12$\n\x06result\x18\x01 \x01(\x0e\x32\x14.chunkservice.Result\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t*H\n\x06Result\x12\x0e\n\nOP_SUCCESS\x10\x00\x12\r\n\tOP_FAILED\x10\x01\x12\r\n\tOP_EXISTS\x10\x02\x12\x10\n\x0cOP_NOT_FOUND\x10\x03\x32\xfb\x01\n\x0c\x43hunkService\x12G\n\nCreateFile\x12\x1f.chunkservice.CreateFileRequest\x1a\x16.chunkservice.Response\"\x00\x12O\n\x0eWriteFileRange\x12#.chunkservice.WriteFileRangeRequest\x1a\x16.chunkservice.Response\"\x00\x12Q\n\rReadFileRange\x12\".chunkservice.ReadFileRangeRequest\x1a\x1a.chunkservice.ReadResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.emal.chunkservice.chunkservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RESULT']._serialized_start=382
  _globals['_RESULT']._serialized_end=454
  _globals['_CREATEFILEREQUEST']._serialized_start=67
  _globals['_CREATEFILEREQUEST']._serialized_end=105
  _globals['_WRITEFILERANGEREQUEST']._serialized_start=107
  _globals['_WRITEFILERANGEREQUEST']._serialized_end=191
  _globals['_READFILERANGEREQUEST']._serialized_start=193
  _globals['_READFILERANGEREQUEST']._serialized_end=262
  _globals['_RESPONSE']._serialized_start=264
  _globals['_RESPONSE']._serialized_end=312
  _globals['_READRESPONSE']._serialized_start=314
  _globals['_READRESPONSE']._serialized_end=380
  _globals['_CHUNKSERVICE']._serialized_start=457
  _globals['_CHUNKSERVICE']._serialized_end=708
# @@protoc_insertion_point(module_scope)
