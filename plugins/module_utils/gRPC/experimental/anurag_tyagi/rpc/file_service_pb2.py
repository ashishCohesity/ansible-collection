# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/anurag_tyagi/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0experimental/anurag_tyagi/rpc/file_service.proto\x12&cohesity.experimental.anurag_tyagi.rpc\x1a\x1copen_util/net/protorpc.proto\"!\n\x11\x43reateFileRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x12\x43reateFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\"M\n\x0fReadFileRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03len\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0f\n\x07send_id\x18\x04 \x01(\x05\"P\n\x10ReadFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0f\n\x07\x65xec_id\x18\x03 \x01(\x05\x12\x0e\n\x06rcv_id\x18\x04 \x01(\x05\"R\n\x10WriteFileRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0f\n\x07send_id\x18\x04 \x01(\x05\"C\n\x11WriteFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07\x65xec_id\x18\x02 \x01(\x05\x12\x0e\n\x06rcv_id\x18\x03 \x01(\x05\x32\xaa\x03\n\x0b\x46ileService\x12\x85\x01\n\nCreateFile\x12\x39.cohesity.experimental.anurag_tyagi.rpc.CreateFileRequest\x1a:.cohesity.experimental.anurag_tyagi.rpc.CreateFileResponse\"\x00\x12\x7f\n\x08ReadFile\x12\x37.cohesity.experimental.anurag_tyagi.rpc.ReadFileRequest\x1a\x38.cohesity.experimental.anurag_tyagi.rpc.ReadFileResponse\"\x00\x12\x82\x01\n\tWriteFile\x12\x38.cohesity.experimental.anurag_tyagi.rpc.WriteFileRequest\x1a\x39.cohesity.experimental.anurag_tyagi.rpc.WriteFileResponse\"\x00\x1a\r\x80\xf1\x04\xd8\x36\x88\xf1\x04\x01\x90\xf1\x04\x05\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.anurag_tyagi.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\3306\210\361\004\001\220\361\004\005'
  _globals['_CREATEFILEREQUEST']._serialized_start=122
  _globals['_CREATEFILEREQUEST']._serialized_end=155
  _globals['_CREATEFILERESPONSE']._serialized_start=157
  _globals['_CREATEFILERESPONSE']._serialized_end=192
  _globals['_READFILEREQUEST']._serialized_start=194
  _globals['_READFILEREQUEST']._serialized_end=271
  _globals['_READFILERESPONSE']._serialized_start=273
  _globals['_READFILERESPONSE']._serialized_end=353
  _globals['_WRITEFILEREQUEST']._serialized_start=355
  _globals['_WRITEFILEREQUEST']._serialized_end=437
  _globals['_WRITEFILERESPONSE']._serialized_start=439
  _globals['_WRITEFILERESPONSE']._serialized_end=506
  _globals['_FILESERVICE']._serialized_start=509
  _globals['_FILESERVICE']._serialized_end=935
# @@protoc_insertion_point(module_scope)
