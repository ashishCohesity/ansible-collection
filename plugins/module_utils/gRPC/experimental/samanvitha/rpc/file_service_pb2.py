# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/samanvitha/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.experimental/samanvitha/rpc/file_service.proto\x12$cohesity.experimental.samanvitha.rpc\x1a\x1copen_util/net/protorpc.proto\"\xcc\x01\n\x05\x45rror\x12I\n\nerror_type\x18\x01 \x02(\x0e\x32\x35.cohesity.experimental.samanvitha.rpc.Error.ErrorType\x12\x15\n\rerror_message\x18\x02 \x01(\t\"a\n\tErrorType\x12\x0c\n\x08kNoError\x10\x01\x12\x11\n\rkFileNotFound\x10\x02\x12\x12\n\x0ekAlreadyExists\x10\x03\x12\x11\n\rkUnknownError\x10\x04\x12\x0c\n\x08kInvalid\x10\x05\"&\n\x11\x43reateFileRequest\x12\x11\n\tfile_name\x18\x01 \x02(\t\"N\n\x10\x43reateFileResult\x12:\n\x05\x65rror\x18\x01 \x02(\x0b\x32+.cohesity.experimental.samanvitha.rpc.Error\"I\n\x14ReadFileRangeRequest\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x0e\n\x06length\x18\x03 \x02(\x03\"_\n\x13ReadFileRangeResult\x12:\n\x05\x65rror\x18\x01 \x02(\x0b\x32+.cohesity.experimental.samanvitha.rpc.Error\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"H\n\x15WriteFileRangeRequest\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"R\n\x14WriteFileRangeResult\x12:\n\x05\x65rror\x18\x01 \x02(\x0b\x32+.cohesity.experimental.samanvitha.rpc.Error2\xc6\x03\n\x0b\x46ileService\x12\x84\x01\n\nCreateFile\x12\x37.cohesity.experimental.samanvitha.rpc.CreateFileRequest\x1a\x36.cohesity.experimental.samanvitha.rpc.CreateFileResult\"\x05\x80\xe2\t\xd0\x0f\x12\x8d\x01\n\rReadFileRange\x12:.cohesity.experimental.samanvitha.rpc.ReadFileRangeRequest\x1a\x39.cohesity.experimental.samanvitha.rpc.ReadFileRangeResult\"\x05\x80\xe2\t\xd0\x0f\x12\x90\x01\n\x0eWriteFileRange\x12;.cohesity.experimental.samanvitha.rpc.WriteFileRangeRequest\x1a:.cohesity.experimental.samanvitha.rpc.WriteFileRangeResult\"\x05\x80\xe2\t\xd0\x0f\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.samanvitha.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_FILESERVICE'].methods_by_name['CreateFile']._loaded_options = None
  _globals['_FILESERVICE'].methods_by_name['CreateFile']._serialized_options = b'\200\342\t\320\017'
  _globals['_FILESERVICE'].methods_by_name['ReadFileRange']._loaded_options = None
  _globals['_FILESERVICE'].methods_by_name['ReadFileRange']._serialized_options = b'\200\342\t\320\017'
  _globals['_FILESERVICE'].methods_by_name['WriteFileRange']._loaded_options = None
  _globals['_FILESERVICE'].methods_by_name['WriteFileRange']._serialized_options = b'\200\342\t\320\017'
  _globals['_ERROR']._serialized_start=119
  _globals['_ERROR']._serialized_end=323
  _globals['_ERROR_ERRORTYPE']._serialized_start=226
  _globals['_ERROR_ERRORTYPE']._serialized_end=323
  _globals['_CREATEFILEREQUEST']._serialized_start=325
  _globals['_CREATEFILEREQUEST']._serialized_end=363
  _globals['_CREATEFILERESULT']._serialized_start=365
  _globals['_CREATEFILERESULT']._serialized_end=443
  _globals['_READFILERANGEREQUEST']._serialized_start=445
  _globals['_READFILERANGEREQUEST']._serialized_end=518
  _globals['_READFILERANGERESULT']._serialized_start=520
  _globals['_READFILERANGERESULT']._serialized_end=615
  _globals['_WRITEFILERANGEREQUEST']._serialized_start=617
  _globals['_WRITEFILERANGEREQUEST']._serialized_end=689
  _globals['_WRITEFILERANGERESULT']._serialized_start=691
  _globals['_WRITEFILERANGERESULT']._serialized_end=773
  _globals['_FILESERVICE']._serialized_start=776
  _globals['_FILESERVICE']._serialized_end=1230
# @@protoc_insertion_point(module_scope)
