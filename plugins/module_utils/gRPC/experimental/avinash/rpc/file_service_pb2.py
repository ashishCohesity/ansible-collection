# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/avinash/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+experimental/avinash/rpc/file_service.proto\x12!cohesity.experimental.avinash.rpc\x1a\x1copen_util/net/protorpc.proto\"U\n\x12\x46ileServiceRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x11\n\x06offset\x18\x02 \x01(\x03:\x01\x30\x12\x0b\n\x03len\x18\x03 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\xd2\x01\n\x13\x46ileServiceResponse\x12^\n\nerror_type\x18\x01 \x01(\x0e\x32@.cohesity.experimental.avinash.rpc.FileServiceResponse.ErrorType:\x08kNoError\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03\x65of\x18\x03 \x01(\x08\"@\n\tErrorType\x12\x0c\n\x08kNoError\x10\x00\x12\x12\n\x0ekAlreadyExists\x10\x01\x12\x11\n\rkUnknownError\x10\x02\x32\xa2\x03\n\x0b\x46ileService\x12}\n\nCreateFile\x12\x35.cohesity.experimental.avinash.rpc.FileServiceRequest\x1a\x36.cohesity.experimental.avinash.rpc.FileServiceResponse\"\x00\x12\x80\x01\n\rReadFileRange\x12\x35.cohesity.experimental.avinash.rpc.FileServiceRequest\x1a\x36.cohesity.experimental.avinash.rpc.FileServiceResponse\"\x00\x12\x81\x01\n\x0eWriteFileRange\x12\x35.cohesity.experimental.avinash.rpc.FileServiceRequest\x1a\x36.cohesity.experimental.avinash.rpc.FileServiceResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.avinash.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_FILESERVICEREQUEST']._serialized_start=112
  _globals['_FILESERVICEREQUEST']._serialized_end=197
  _globals['_FILESERVICERESPONSE']._serialized_start=200
  _globals['_FILESERVICERESPONSE']._serialized_end=410
  _globals['_FILESERVICERESPONSE_ERRORTYPE']._serialized_start=346
  _globals['_FILESERVICERESPONSE_ERRORTYPE']._serialized_end=410
  _globals['_FILESERVICE']._serialized_start=413
  _globals['_FILESERVICE']._serialized_end=831
# @@protoc_insertion_point(module_scope)