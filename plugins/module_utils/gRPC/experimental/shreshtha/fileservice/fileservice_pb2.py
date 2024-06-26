# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/shreshtha/fileservice/fileservice.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4experimental/shreshtha/fileservice/fileservice.proto\x12+cohesity.experimental.shreshtha.fileservice\x1a\x1copen_util/net/protorpc.proto\"%\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"Y\n\x12\x43reateFileResponse\x12\x43\n\x02rc\x18\x01 \x01(\x0e\x32\x37.cohesity.experimental.shreshtha.fileservice.ReturnCode\"@\n\x0fReadFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0b\n\x03len\x18\x03 \x01(\x03\"e\n\x10ReadFileResponse\x12\x43\n\x02rc\x18\x01 \x01(\x0e\x32\x37.cohesity.experimental.shreshtha.fileservice.ReturnCode\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"B\n\x10WriteFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"X\n\x11WriteFileResponse\x12\x43\n\x02rc\x18\x01 \x01(\x0e\x32\x37.cohesity.experimental.shreshtha.fileservice.ReturnCode*f\n\nReturnCode\x12\x0b\n\x07Success\x10\x01\x12\x11\n\rAlreadyExists\x10\x02\x12\x10\n\x0c\x44oesNotExist\x10\x03\x12\x14\n\x10PermissionDenied\x10\x04\x12\x10\n\x0cUnknownError\x10\x05\x32\xc5\x03\n\x0b\x46ileService\x12\x8f\x01\n\nCreateFile\x12>.cohesity.experimental.shreshtha.fileservice.CreateFileRequest\x1a?.cohesity.experimental.shreshtha.fileservice.CreateFileResponse\"\x00\x12\x89\x01\n\x08ReadFile\x12<.cohesity.experimental.shreshtha.fileservice.ReadFileRequest\x1a=.cohesity.experimental.shreshtha.fileservice.ReadFileResponse\"\x00\x12\x8c\x01\n\tWriteFile\x12=.cohesity.experimental.shreshtha.fileservice.WriteFileRequest\x1a>.cohesity.experimental.shreshtha.fileservice.WriteFileResponse\"\x00\x1a\t\x80\xf1\x04\xe8\x07\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.shreshtha.fileservice.fileservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\220\361\004\002'
  _globals['_RETURNCODE']._serialized_start=588
  _globals['_RETURNCODE']._serialized_end=690
  _globals['_CREATEFILEREQUEST']._serialized_start=131
  _globals['_CREATEFILEREQUEST']._serialized_end=168
  _globals['_CREATEFILERESPONSE']._serialized_start=170
  _globals['_CREATEFILERESPONSE']._serialized_end=259
  _globals['_READFILEREQUEST']._serialized_start=261
  _globals['_READFILEREQUEST']._serialized_end=325
  _globals['_READFILERESPONSE']._serialized_start=327
  _globals['_READFILERESPONSE']._serialized_end=428
  _globals['_WRITEFILEREQUEST']._serialized_start=430
  _globals['_WRITEFILEREQUEST']._serialized_end=496
  _globals['_WRITEFILERESPONSE']._serialized_start=498
  _globals['_WRITEFILERESPONSE']._serialized_end=586
  _globals['_FILESERVICE']._serialized_start=693
  _globals['_FILESERVICE']._serialized_end=1146
# @@protoc_insertion_point(module_scope)
