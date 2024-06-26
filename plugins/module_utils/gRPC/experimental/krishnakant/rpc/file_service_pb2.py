# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/krishnakant/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/experimental/krishnakant/rpc/file_service.proto\x12%cohesity.experimental.krishnakant.rpc\x1a\x1copen_util/net/protorpc.proto\"\xb0\x01\n\nErrorProto\x12N\n\x04type\x18\x01 \x01(\x0e\x32\x36.cohesity.experimental.krishnakant.rpc.ErrorProto.Type:\x08kNoError\x12\x14\n\x0c\x65rror_string\x18\x02 \x01(\t\"<\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x12\n\x0ekInternalError\x10\x01\x12\x12\n\x0ekRetryExceeded\x10\x02\"\x1e\n\rCreateFileArg\x12\r\n\x05\x66name\x18\x01 \x02(\t\"T\n\x10\x43reateFileResult\x12@\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x31.cohesity.experimental.krishnakant.rpc.ErrorProto\"<\n\x0bReadFileArg\x12\r\n\x05\x66name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x04\x12\x0e\n\x06length\x18\x03 \x02(\x04\"a\n\x0eReadFileResult\x12\r\n\x05seqno\x18\x01 \x01(\x04\x12@\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x31.cohesity.experimental.krishnakant.rpc.ErrorProto\"-\n\x0cWriteFileArg\x12\r\n\x05\x66name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x04\"b\n\x0fWriteFileResult\x12\r\n\x05seqno\x18\x01 \x01(\x04\x12@\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x31.cohesity.experimental.krishnakant.rpc.ErrorProto2\x9a\x03\n\x0b\x46ileService\x12}\n\nCreateFile\x12\x34.cohesity.experimental.krishnakant.rpc.CreateFileArg\x1a\x37.cohesity.experimental.krishnakant.rpc.CreateFileResult\"\x00\x12|\n\rReadFileRange\x12\x32.cohesity.experimental.krishnakant.rpc.ReadFileArg\x1a\x35.cohesity.experimental.krishnakant.rpc.ReadFileResult\"\x00\x12\x7f\n\x0eWriteFileRange\x12\x33.cohesity.experimental.krishnakant.rpc.WriteFileArg\x1a\x36.cohesity.experimental.krishnakant.rpc.WriteFileResult\"\x00\x1a\r\x80\xf1\x04\x88\'\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.krishnakant.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\210\'\210\361\004\001\220\361\004\002'
  _globals['_ERRORPROTO']._serialized_start=121
  _globals['_ERRORPROTO']._serialized_end=297
  _globals['_ERRORPROTO_TYPE']._serialized_start=237
  _globals['_ERRORPROTO_TYPE']._serialized_end=297
  _globals['_CREATEFILEARG']._serialized_start=299
  _globals['_CREATEFILEARG']._serialized_end=329
  _globals['_CREATEFILERESULT']._serialized_start=331
  _globals['_CREATEFILERESULT']._serialized_end=415
  _globals['_READFILEARG']._serialized_start=417
  _globals['_READFILEARG']._serialized_end=477
  _globals['_READFILERESULT']._serialized_start=479
  _globals['_READFILERESULT']._serialized_end=576
  _globals['_WRITEFILEARG']._serialized_start=578
  _globals['_WRITEFILEARG']._serialized_end=623
  _globals['_WRITEFILERESULT']._serialized_start=625
  _globals['_WRITEFILERESULT']._serialized_end=723
  _globals['_FILESERVICE']._serialized_start=726
  _globals['_FILESERVICE']._serialized_end=1136
# @@protoc_insertion_point(module_scope)
