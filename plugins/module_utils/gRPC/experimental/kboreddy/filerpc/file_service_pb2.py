# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/kboreddy/filerpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0experimental/kboreddy/filerpc/file_service.proto\x12&cohesity.experimental.kboreddy.filerpc\x1a\x1copen_util/net/protorpc.proto\"&\n\x11\x43reateFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"[\n\x10\x43reateFileResult\x12G\n\x0breturn_code\x18\x01 \x01(\x0e\x32\x32.cohesity.experimental.kboreddy.filerpc.ReturnCode\"H\n\x0fReadFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x12\n\x06offset\x18\x02 \x01(\x03:\x02-1\x12\x0e\n\x06length\x18\x03 \x01(\x03\"Y\n\x0eReadFileResult\x12G\n\x0breturn_code\x18\x01 \x01(\x0e\x32\x32.cohesity.experimental.kboreddy.filerpc.ReturnCode\"I\n\x10WriteFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x12\n\x06offset\x18\x02 \x01(\x03:\x02-1\x12\x0e\n\x06length\x18\x03 \x01(\x03\"Z\n\x0fWriteFileResult\x12G\n\x0breturn_code\x18\x01 \x01(\x0e\x32\x32.cohesity.experimental.kboreddy.filerpc.ReturnCode*g\n\nReturnCode\x12\x0c\n\x08kSuccess\x10\x01\x12\x12\n\x0ekAlreadyExists\x10\x02\x12\x11\n\rkDoesNotExist\x10\x03\x12\x11\n\rkAccessDenied\x10\x04\x12\x11\n\rkUnknownError\x10\x05\x32\xb0\x03\n\x0b\x46ileService\x12\x83\x01\n\nCreateFile\x12\x39.cohesity.experimental.kboreddy.filerpc.CreateFileRequest\x1a\x38.cohesity.experimental.kboreddy.filerpc.CreateFileResult\"\x00\x12\x82\x01\n\rReadFileRange\x12\x37.cohesity.experimental.kboreddy.filerpc.ReadFileRequest\x1a\x36.cohesity.experimental.kboreddy.filerpc.ReadFileResult\"\x00\x12\x85\x01\n\x0eWriteFileRange\x12\x38.cohesity.experimental.kboreddy.filerpc.WriteFileRequest\x1a\x37.cohesity.experimental.kboreddy.filerpc.WriteFileResult\"\x00\x1a\x0e\x80\xf1\x04\xe0\xd4\x03\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.kboreddy.filerpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\340\324\003\210\361\004\001\220\361\004\002'
  _globals['_RETURNCODE']._serialized_start=587
  _globals['_RETURNCODE']._serialized_end=690
  _globals['_CREATEFILEREQUEST']._serialized_start=122
  _globals['_CREATEFILEREQUEST']._serialized_end=160
  _globals['_CREATEFILERESULT']._serialized_start=162
  _globals['_CREATEFILERESULT']._serialized_end=253
  _globals['_READFILEREQUEST']._serialized_start=255
  _globals['_READFILEREQUEST']._serialized_end=327
  _globals['_READFILERESULT']._serialized_start=329
  _globals['_READFILERESULT']._serialized_end=418
  _globals['_WRITEFILEREQUEST']._serialized_start=420
  _globals['_WRITEFILEREQUEST']._serialized_end=493
  _globals['_WRITEFILERESULT']._serialized_start=495
  _globals['_WRITEFILERESULT']._serialized_end=585
  _globals['_FILESERVICE']._serialized_start=693
  _globals['_FILESERVICE']._serialized_end=1125
# @@protoc_insertion_point(module_scope)