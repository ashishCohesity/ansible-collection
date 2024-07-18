# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/abhinav_singh/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1experimental/abhinav_singh/rpc/file_service.proto\x12\'cohesity.experimental.abhinav_singh.rpc\x1a\x1copen_util/net/protorpc.proto\"!\n\rCreateRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\" \n\x0e\x43reateResponse\x12\x0e\n\x06status\x18\x01 \x02(\x08\"?\n\x0bReadRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06length\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\"\x1e\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x02(\x08\"0\n\x0cWriteRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"2\n\rWriteResponse\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x32\x96\x03\n\x0b\x46ileService\x12y\n\x08ReadFile\x12\x34.cohesity.experimental.abhinav_singh.rpc.ReadRequest\x1a\x35.cohesity.experimental.abhinav_singh.rpc.ReadResponse\"\x00\x12|\n\tWriteFile\x12\x35.cohesity.experimental.abhinav_singh.rpc.WriteRequest\x1a\x36.cohesity.experimental.abhinav_singh.rpc.WriteResponse\"\x00\x12\x7f\n\nCreateFile\x12\x36.cohesity.experimental.abhinav_singh.rpc.CreateRequest\x1a\x37.cohesity.experimental.abhinav_singh.rpc.CreateResponse\"\x00\x1a\r\x80\xf1\x04\x88\'\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.abhinav_singh.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\210\'\210\361\004\001\220\361\004\002'
  _globals['_CREATEREQUEST']._serialized_start=124
  _globals['_CREATEREQUEST']._serialized_end=157
  _globals['_CREATERESPONSE']._serialized_start=159
  _globals['_CREATERESPONSE']._serialized_end=191
  _globals['_READREQUEST']._serialized_start=193
  _globals['_READREQUEST']._serialized_end=256
  _globals['_READRESPONSE']._serialized_start=258
  _globals['_READRESPONSE']._serialized_end=288
  _globals['_WRITEREQUEST']._serialized_start=290
  _globals['_WRITEREQUEST']._serialized_end=338
  _globals['_WRITERESPONSE']._serialized_start=340
  _globals['_WRITERESPONSE']._serialized_end=390
  _globals['_FILESERVICE']._serialized_start=393
  _globals['_FILESERVICE']._serialized_end=799
# @@protoc_insertion_point(module_scope)