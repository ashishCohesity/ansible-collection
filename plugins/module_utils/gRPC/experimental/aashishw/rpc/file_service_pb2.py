# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/aashishw/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,experimental/aashishw/rpc/file_service.proto\x12\"cohesity.experimental.aashishw.rpc\x1a\x1copen_util/net/protorpc.proto\"\x1d\n\rCreateRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\" \n\x0e\x43reateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"8\n\x0bReadRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x0b\n\x03len\x18\x03 \x01(\x05\"\x1e\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"9\n\x0cWriteRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x0b\n\x03len\x18\x03 \x01(\x05\"\x1f\n\rWriteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\x82\x03\n\x0b\x46ileService\x12u\n\nCreateFile\x12\x31.cohesity.experimental.aashishw.rpc.CreateRequest\x1a\x32.cohesity.experimental.aashishw.rpc.CreateResponse\"\x00\x12t\n\rReadFileRange\x12/.cohesity.experimental.aashishw.rpc.ReadRequest\x1a\x30.cohesity.experimental.aashishw.rpc.ReadResponse\"\x00\x12w\n\x0eWriteFileRange\x12\x30.cohesity.experimental.aashishw.rpc.WriteRequest\x1a\x31.cohesity.experimental.aashishw.rpc.WriteResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.aashishw.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEREQUEST']._serialized_start=114
  _globals['_CREATEREQUEST']._serialized_end=143
  _globals['_CREATERESPONSE']._serialized_start=145
  _globals['_CREATERESPONSE']._serialized_end=177
  _globals['_READREQUEST']._serialized_start=179
  _globals['_READREQUEST']._serialized_end=235
  _globals['_READRESPONSE']._serialized_start=237
  _globals['_READRESPONSE']._serialized_end=267
  _globals['_WRITEREQUEST']._serialized_start=269
  _globals['_WRITEREQUEST']._serialized_end=326
  _globals['_WRITERESPONSE']._serialized_start=328
  _globals['_WRITERESPONSE']._serialized_end=359
  _globals['_FILESERVICE']._serialized_start=362
  _globals['_FILESERVICE']._serialized_end=748
# @@protoc_insertion_point(module_scope)
