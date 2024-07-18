# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/devershi/file_service/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5experimental/devershi/file_service/file_service.proto\x12\"experimental.devershi.file_service\x1a\x1copen_util/net/protorpc.proto\"&\n\x11\x43reateFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"M\n\x14ReadFileBlockRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x12\n\nblock_size\x18\x03 \x01(\x03\"H\n\x15WriteFileBlockRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"\xaf\x01\n\x0e\x46ileOpResponse\x12?\n\x08\x65rr_code\x18\x01 \x01(\x0e\x32-.experimental.devershi.file_service.ErrorType\x12;\n\x07op_type\x18\x02 \x01(\x0e\x32*.experimental.devershi.file_service.OpType\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x11\n\terror_msg\x18\x04 \x01(\t*\x9f\x01\n\tErrorType\x12\x10\n\x0ckUnowknError\x10\x00\x12\x12\n\x0ekInternalError\x10\x01\x12\x14\n\x10kOutOfRangeError\x10\x02\x12\x18\n\x14kInvalidRequestError\x10\x03\x12\x0c\n\x08kNoError\x10\x04\x12\x16\n\x12kFileAlreadyExists\x10\x05\x12\x16\n\x12kFileDoesNotExists\x10\x06*<\n\x06OpType\x12\x0e\n\nkUnknownOp\x10\x00\x12\t\n\x05kRead\x10\x01\x12\x0b\n\x07kCreate\x10\x02\x12\n\n\x06kWrite\x10\x03\x32\x9c\x03\n\x0b\x46ileService\x12y\n\nCreateFile\x12\x35.experimental.devershi.file_service.CreateFileRequest\x1a\x32.experimental.devershi.file_service.FileOpResponse\"\x00\x12\x7f\n\rReadFileBlock\x12\x38.experimental.devershi.file_service.ReadFileBlockRequest\x1a\x32.experimental.devershi.file_service.FileOpResponse\"\x00\x12\x81\x01\n\x0eWriteFileBlock\x12\x39.experimental.devershi.file_service.WriteFileBlockRequest\x1a\x32.experimental.devershi.file_service.FileOpResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.devershi.file_service.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_ERRORTYPE']._serialized_start=495
  _globals['_ERRORTYPE']._serialized_end=654
  _globals['_OPTYPE']._serialized_start=656
  _globals['_OPTYPE']._serialized_end=716
  _globals['_CREATEFILEREQUEST']._serialized_start=123
  _globals['_CREATEFILEREQUEST']._serialized_end=161
  _globals['_READFILEBLOCKREQUEST']._serialized_start=163
  _globals['_READFILEBLOCKREQUEST']._serialized_end=240
  _globals['_WRITEFILEBLOCKREQUEST']._serialized_start=242
  _globals['_WRITEFILEBLOCKREQUEST']._serialized_end=314
  _globals['_FILEOPRESPONSE']._serialized_start=317
  _globals['_FILEOPRESPONSE']._serialized_end=492
  _globals['_FILESERVICE']._serialized_start=719
  _globals['_FILESERVICE']._serialized_end=1131
# @@protoc_insertion_point(module_scope)