# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/haoli/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)experimental/haoli/rpc/file_service.proto\x12\x1f\x63ohesity.experimental.haoli.rpc\x1a\x1copen_util/net/protorpc.proto\".\n\x11\x43reateFileRequest\x12\x19\n\x08\x66ilename\x18\x01 \x01(\t:\x07new.txt\"#\n\x12\x43reateFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\"A\n\x0fReadFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\r\n\x05start\x18\x02 \x02(\x03\x12\r\n\x05range\x18\x03 \x02(\x03\"1\n\x10ReadFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0e\n\x06result\x18\x02 \x01(\x0c\"D\n\x10WriteFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\r\n\x05start\x18\x02 \x02(\x03\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\x0c\"\"\n\x11WriteFileResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\"#\n\x0cHelloRequest\x12\x13\n\x04name\x18\x01 \x01(\t:\x05World\"\x1f\n\x0bHelloResult\x12\x10\n\x08greeting\x18\x01 \x01(\t2\xe6\x03\n\x0b\x46ileService\x12\x66\n\x05Greet\x12-.cohesity.experimental.haoli.rpc.HelloRequest\x1a,.cohesity.experimental.haoli.rpc.HelloResult\"\x00\x12w\n\nCreateFile\x12\x32.cohesity.experimental.haoli.rpc.CreateFileRequest\x1a\x33.cohesity.experimental.haoli.rpc.CreateFileResponse\"\x00\x12q\n\x08ReadFile\x12\x30.cohesity.experimental.haoli.rpc.ReadFileRequest\x1a\x31.cohesity.experimental.haoli.rpc.ReadFileResponse\"\x00\x12t\n\tWriteFile\x12\x31.cohesity.experimental.haoli.rpc.WriteFileRequest\x1a\x32.cohesity.experimental.haoli.rpc.WriteFileResponse\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.haoli.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEFILEREQUEST']._serialized_start=108
  _globals['_CREATEFILEREQUEST']._serialized_end=154
  _globals['_CREATEFILERESPONSE']._serialized_start=156
  _globals['_CREATEFILERESPONSE']._serialized_end=191
  _globals['_READFILEREQUEST']._serialized_start=193
  _globals['_READFILEREQUEST']._serialized_end=258
  _globals['_READFILERESPONSE']._serialized_start=260
  _globals['_READFILERESPONSE']._serialized_end=309
  _globals['_WRITEFILEREQUEST']._serialized_start=311
  _globals['_WRITEFILEREQUEST']._serialized_end=379
  _globals['_WRITEFILERESPONSE']._serialized_start=381
  _globals['_WRITEFILERESPONSE']._serialized_end=415
  _globals['_HELLOREQUEST']._serialized_start=417
  _globals['_HELLOREQUEST']._serialized_end=452
  _globals['_HELLORESULT']._serialized_start=454
  _globals['_HELLORESULT']._serialized_end=485
  _globals['_FILESERVICE']._serialized_start=488
  _globals['_FILESERVICE']._serialized_end=974
# @@protoc_insertion_point(module_scope)
