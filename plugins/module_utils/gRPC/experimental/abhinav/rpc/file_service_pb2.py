# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/abhinav/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+experimental/abhinav/rpc/file_service.proto\x12!cohesity.experimental.abhinav.rpc\x1a\x1copen_util/net/protorpc.proto\">\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ile_num\x18\x01 \x02(\x05\x12\x17\n\x0fmax_file_length\x18\x02 \x02(\x05\"W\n\x10ReadWriteRequest\x12\x10\n\x08\x66ile_num\x18\x01 \x02(\x05\x12\x11\n\tio_op_num\x18\x04 \x02(\x05\x12\x0e\n\x06offset\x18\x05 \x02(\x05\x12\x0e\n\x06length\x18\x06 \x02(\x05\"`\n\x18\x46ileServiceRequestResult\x12\x12\n\nis_success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x32\xa9\x03\n\x0b\x46ileService\x12\x81\x01\n\nCreateFile\x12\x34.cohesity.experimental.abhinav.rpc.CreateFileRequest\x1a;.cohesity.experimental.abhinav.rpc.FileServiceRequestResult\"\x00\x12\x81\x01\n\x0bPerformRead\x12\x33.cohesity.experimental.abhinav.rpc.ReadWriteRequest\x1a;.cohesity.experimental.abhinav.rpc.FileServiceRequestResult\"\x00\x12\x82\x01\n\x0cPerformWrite\x12\x33.cohesity.experimental.abhinav.rpc.ReadWriteRequest\x1a;.cohesity.experimental.abhinav.rpc.FileServiceRequestResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.abhinav.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEREQUEST']._serialized_start=112
  _globals['_CREATEFILEREQUEST']._serialized_end=174
  _globals['_READWRITEREQUEST']._serialized_start=176
  _globals['_READWRITEREQUEST']._serialized_end=263
  _globals['_FILESERVICEREQUESTRESULT']._serialized_start=265
  _globals['_FILESERVICEREQUESTRESULT']._serialized_end=361
  _globals['_FILESERVICE']._serialized_start=364
  _globals['_FILESERVICE']._serialized_end=789
# @@protoc_insertion_point(module_scope)
