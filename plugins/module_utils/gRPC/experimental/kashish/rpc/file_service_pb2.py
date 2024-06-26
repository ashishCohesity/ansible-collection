# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/kashish/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+experimental/kashish/rpc/file_service.proto\x12!cohesity.experimental.kashish.rpc\x1a\x1copen_util/net/protorpc.proto\"#\n\x0cHelloRequest\x12\x13\n\x04name\x18\x01 \x01(\t:\x05World\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t\"!\n\rCreateFileReq\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"Q\n\x12\x43reateFileResponse\x12;\n\x05\x65rror\x18\x01 \x01(\x0e\x32,.cohesity.experimental.kashish.rpc.ErrorCode\"E\n\x0bReadFileReq\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x14\n\x06length\x18\x03 \x01(\x03:\x04\x31\x30\x32\x34\"j\n\x10ReadFileResponse\x12;\n\x05\x65rror\x18\x01 \x01(\x0e\x32,.cohesity.experimental.kashish.rpc.ErrorCode\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03\x65of\x18\x03 \x01(\x08\"A\n\x0cWriteFileReq\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"P\n\x11WriteFileResponse\x12;\n\x05\x65rror\x18\x01 \x01(\x0e\x32,.cohesity.experimental.kashish.rpc.ErrorCode*@\n\tErrorCode\x12\x0c\n\x08kSuccess\x10\x01\x12\x12\n\x0ekAlreadyExists\x10\x02\x12\x11\n\rkUnknownError\x10\x03\x32\xec\x03\n\x0b\x46ileService\x12l\n\x05Greet\x12/.cohesity.experimental.kashish.rpc.HelloRequest\x1a\x30.cohesity.experimental.kashish.rpc.HelloResponse\"\x00\x12w\n\nCreateFile\x12\x30.cohesity.experimental.kashish.rpc.CreateFileReq\x1a\x35.cohesity.experimental.kashish.rpc.CreateFileResponse\"\x00\x12q\n\x08ReadFile\x12..cohesity.experimental.kashish.rpc.ReadFileReq\x1a\x33.cohesity.experimental.kashish.rpc.ReadFileResponse\"\x00\x12t\n\tWriteFile\x12/.cohesity.experimental.kashish.rpc.WriteFileReq\x1a\x34.cohesity.experimental.kashish.rpc.WriteFileResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.kashish.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_ERRORCODE']._serialized_start=630
  _globals['_ERRORCODE']._serialized_end=694
  _globals['_HELLOREQUEST']._serialized_start=112
  _globals['_HELLOREQUEST']._serialized_end=147
  _globals['_HELLORESPONSE']._serialized_start=149
  _globals['_HELLORESPONSE']._serialized_end=182
  _globals['_CREATEFILEREQ']._serialized_start=184
  _globals['_CREATEFILEREQ']._serialized_end=217
  _globals['_CREATEFILERESPONSE']._serialized_start=219
  _globals['_CREATEFILERESPONSE']._serialized_end=300
  _globals['_READFILEREQ']._serialized_start=302
  _globals['_READFILEREQ']._serialized_end=371
  _globals['_READFILERESPONSE']._serialized_start=373
  _globals['_READFILERESPONSE']._serialized_end=479
  _globals['_WRITEFILEREQ']._serialized_start=481
  _globals['_WRITEFILEREQ']._serialized_end=546
  _globals['_WRITEFILERESPONSE']._serialized_start=548
  _globals['_WRITEFILERESPONSE']._serialized_end=628
  _globals['_FILESERVICE']._serialized_start=697
  _globals['_FILESERVICE']._serialized_end=1189
# @@protoc_insertion_point(module_scope)
