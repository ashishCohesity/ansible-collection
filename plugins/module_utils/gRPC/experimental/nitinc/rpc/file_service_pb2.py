# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/nitinc/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*experimental/nitinc/rpc/file_service.proto\x12 cohesity.experimental.nitinc.rpc\x1a\x1copen_util/net/protorpc.proto\"\xbe\x01\n\nErrorProto\x12I\n\x04type\x18\x01 \x01(\x0e\x32\x31.cohesity.experimental.nitinc.rpc.ErrorProto.Type:\x08kNoError\x12\x14\n\x0c\x65rror_detail\x18\x02 \x01(\t\"O\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x12\n\x0ekInternalError\x10\x01\x12\x11\n\rkInvalidInput\x10\x02\x12\x12\n\x0ekRetryExceeded\x10\x03\"%\n\x11\x46ileCreateRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"@\n\x0f\x46ileReadRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0b\n\x03len\x18\x03 \x02(\x03\"B\n\x10\x46ileWriteRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\t\"O\n\x10\x46ileCreateResult\x12;\n\x05\x65rror\x18\x01 \x02(\x0b\x32,.cohesity.experimental.nitinc.rpc.ErrorProto\"[\n\x0e\x46ileReadResult\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12;\n\x05\x65rror\x18\x02 \x02(\x0b\x32,.cohesity.experimental.nitinc.rpc.ErrorProto\"[\n\x0f\x46ileWriteResult\x12\x0b\n\x03len\x18\x01 \x01(\x03\x12;\n\x05\x65rror\x18\x02 \x02(\x0b\x32,.cohesity.experimental.nitinc.rpc.ErrorProto2\xfe\x02\n\x0b\x46ileService\x12w\n\nCreateFile\x12\x33.cohesity.experimental.nitinc.rpc.FileCreateRequest\x1a\x32.cohesity.experimental.nitinc.rpc.FileCreateResult\"\x00\x12q\n\x08ReadFile\x12\x31.cohesity.experimental.nitinc.rpc.FileReadRequest\x1a\x30.cohesity.experimental.nitinc.rpc.FileReadResult\"\x00\x12t\n\tWriteFile\x12\x32.cohesity.experimental.nitinc.rpc.FileWriteRequest\x1a\x31.cohesity.experimental.nitinc.rpc.FileWriteResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.nitinc.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_ERRORPROTO']._serialized_start=111
  _globals['_ERRORPROTO']._serialized_end=301
  _globals['_ERRORPROTO_TYPE']._serialized_start=222
  _globals['_ERRORPROTO_TYPE']._serialized_end=301
  _globals['_FILECREATEREQUEST']._serialized_start=303
  _globals['_FILECREATEREQUEST']._serialized_end=340
  _globals['_FILEREADREQUEST']._serialized_start=342
  _globals['_FILEREADREQUEST']._serialized_end=406
  _globals['_FILEWRITEREQUEST']._serialized_start=408
  _globals['_FILEWRITEREQUEST']._serialized_end=474
  _globals['_FILECREATERESULT']._serialized_start=476
  _globals['_FILECREATERESULT']._serialized_end=555
  _globals['_FILEREADRESULT']._serialized_start=557
  _globals['_FILEREADRESULT']._serialized_end=648
  _globals['_FILEWRITERESULT']._serialized_start=650
  _globals['_FILEWRITERESULT']._serialized_end=741
  _globals['_FILESERVICE']._serialized_start=744
  _globals['_FILESERVICE']._serialized_end=1126
# @@protoc_insertion_point(module_scope)
