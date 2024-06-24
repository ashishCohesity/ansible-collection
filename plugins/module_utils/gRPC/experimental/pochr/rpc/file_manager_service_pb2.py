# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/pochr/rpc/file_manager_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1experimental/pochr/rpc/file_manager_service.proto\x12\x1f\x63ohesity.experimental.pochr.rpc\x1a\x1copen_util/net/protorpc.proto\"\xb3\x01\n\rClientRequest\x12\x41\n\x04type\x18\x01 \x01(\x0e\x32\x33.cohesity.experimental.pochr.rpc.ClientRequest.Type\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x11\n\x06offset\x18\x03 \x01(\x03:\x01\x30\x12\x11\n\x06length\x18\x04 \x01(\x03:\x01\x30\"\'\n\x04Type\x12\n\n\x06\x43REATE\x10\x00\x12\x08\n\x04READ\x10\x01\x12\t\n\x05WRITE\x10\x02\"\xfb\x01\n\x0eServerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x17\n\x0bsequence_id\x18\x03 \x01(\x03:\x02-1\x12M\n\nerror_type\x18\x04 \x01(\x0e\x32\x39.cohesity.experimental.pochr.rpc.ServerResponse.ErrorType\"b\n\tErrorType\x12\x0c\n\x08kNoError\x10\x00\x12\x0c\n\x08kInvalid\x10\x01\x12\x0f\n\x0bkWriteError\x10\x02\x12\x15\n\x11kPermissionDenied\x10\x03\x12\x11\n\rkFileNotFound\x10\x04\x32\x90\x01\n\x12\x46ileManagerService\x12k\n\x06IOtask\x12..cohesity.experimental.pochr.rpc.ClientRequest\x1a/.cohesity.experimental.pochr.rpc.ServerResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.pochr.rpc.file_manager_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILEMANAGERSERVICE']._loaded_options = None
  _globals['_FILEMANAGERSERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CLIENTREQUEST']._serialized_start=117
  _globals['_CLIENTREQUEST']._serialized_end=296
  _globals['_CLIENTREQUEST_TYPE']._serialized_start=257
  _globals['_CLIENTREQUEST_TYPE']._serialized_end=296
  _globals['_SERVERRESPONSE']._serialized_start=299
  _globals['_SERVERRESPONSE']._serialized_end=550
  _globals['_SERVERRESPONSE_ERRORTYPE']._serialized_start=452
  _globals['_SERVERRESPONSE_ERRORTYPE']._serialized_end=550
  _globals['_FILEMANAGERSERVICE']._serialized_start=553
  _globals['_FILEMANAGERSERVICE']._serialized_end=697
# @@protoc_insertion_point(module_scope)
