# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/shubham/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+experimental/shubham/rpc/file_service.proto\x12!cohesity.experimental.shubham.rpc\x1a\x1copen_util/net/protorpc.proto\"%\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"#\n\x12\x43reateFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\"C\n\x0fReadFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\"4\n\x10ReadFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"D\n\x10WriteFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\"5\n\x11WriteFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x32\x8c\x03\n\rMyFileService\x12{\n\nCreateFile\x12\x34.cohesity.experimental.shubham.rpc.CreateFileRequest\x1a\x35.cohesity.experimental.shubham.rpc.CreateFileResponse\"\x00\x12u\n\x08ReadFile\x12\x32.cohesity.experimental.shubham.rpc.ReadFileRequest\x1a\x33.cohesity.experimental.shubham.rpc.ReadFileResponse\"\x00\x12x\n\tWriteFile\x12\x33.cohesity.experimental.shubham.rpc.WriteFileRequest\x1a\x34.cohesity.experimental.shubham.rpc.WriteFileResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.shubham.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_MYFILESERVICE']._loaded_options = None
  _globals['_MYFILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEREQUEST']._serialized_start=112
  _globals['_CREATEFILEREQUEST']._serialized_end=149
  _globals['_CREATEFILERESPONSE']._serialized_start=151
  _globals['_CREATEFILERESPONSE']._serialized_end=186
  _globals['_READFILEREQUEST']._serialized_start=188
  _globals['_READFILEREQUEST']._serialized_end=255
  _globals['_READFILERESPONSE']._serialized_start=257
  _globals['_READFILERESPONSE']._serialized_end=309
  _globals['_WRITEFILEREQUEST']._serialized_start=311
  _globals['_WRITEFILEREQUEST']._serialized_end=379
  _globals['_WRITEFILERESPONSE']._serialized_start=381
  _globals['_WRITEFILERESPONSE']._serialized_end=434
  _globals['_MYFILESERVICE']._serialized_start=437
  _globals['_MYFILESERVICE']._serialized_end=833
# @@protoc_insertion_point(module_scope)
