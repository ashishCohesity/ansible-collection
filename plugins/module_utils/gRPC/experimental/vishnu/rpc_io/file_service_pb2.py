# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/vishnu/rpc_io/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-experimental/vishnu/rpc_io/file_service.proto\x12#cohesity.experimental.vishnu.rpc_io\x1a\x1copen_util/net/protorpc.proto\"%\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"%\n\x12\x43reateFileResponse\x12\x0f\n\x07outcome\x18\x01 \x01(\x08\"I\n\x12WriteToFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x11\n\twritesize\x18\x02 \x02(\x05\x12\x0e\n\x06offset\x18\x03 \x02(\x05\"6\n\x13WriteToFileResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x12\x0f\n\x07success\x18\x02 \x01(\x08\"I\n\x13ReadFromFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x10\n\x08readsize\x18\x02 \x02(\x05\x12\x0e\n\x06offset\x18\x03 \x02(\x05\"7\n\x14ReadFromFileResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x12\x0f\n\x07success\x18\x02 \x01(\x08\x32\xaa\x03\n\x0b\x46ileService\x12\x7f\n\nCreateFile\x12\x36.cohesity.experimental.vishnu.rpc_io.CreateFileRequest\x1a\x37.cohesity.experimental.vishnu.rpc_io.CreateFileResponse\"\x00\x12\x82\x01\n\x0bWriteToFile\x12\x37.cohesity.experimental.vishnu.rpc_io.WriteToFileRequest\x1a\x38.cohesity.experimental.vishnu.rpc_io.WriteToFileResponse\"\x00\x12\x85\x01\n\x0cReadFromFile\x12\x38.cohesity.experimental.vishnu.rpc_io.ReadFromFileRequest\x1a\x39.cohesity.experimental.vishnu.rpc_io.ReadFromFileResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.vishnu.rpc_io.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEREQUEST']._serialized_start=116
  _globals['_CREATEFILEREQUEST']._serialized_end=153
  _globals['_CREATEFILERESPONSE']._serialized_start=155
  _globals['_CREATEFILERESPONSE']._serialized_end=192
  _globals['_WRITETOFILEREQUEST']._serialized_start=194
  _globals['_WRITETOFILEREQUEST']._serialized_end=267
  _globals['_WRITETOFILERESPONSE']._serialized_start=269
  _globals['_WRITETOFILERESPONSE']._serialized_end=323
  _globals['_READFROMFILEREQUEST']._serialized_start=325
  _globals['_READFROMFILEREQUEST']._serialized_end=398
  _globals['_READFROMFILERESPONSE']._serialized_start=400
  _globals['_READFROMFILERESPONSE']._serialized_end=455
  _globals['_FILESERVICE']._serialized_start=458
  _globals['_FILESERVICE']._serialized_end=884
# @@protoc_insertion_point(module_scope)
