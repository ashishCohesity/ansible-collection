# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/aniket/protorpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/experimental/aniket/protorpc/file_service.proto\x12%cohesity.experimental.aniket.protorpc\x1a\x1copen_util/net/protorpc.proto\"#\n\x0cHelloRequest\x12\x13\n\x04name\x18\x01 \x01(\t:\x05World\"\x1f\n\x0bHelloResult\x12\x10\n\x08greeting\x18\x01 \x01(\t\"\xb1\x01\n\nErrorProto\x12N\n\x04type\x18\x01 \x01(\x0e\x32\x36.cohesity.experimental.aniket.protorpc.ErrorProto.Type:\x08kNoError\"S\n\x04Type\x12\x0c\n\x08kNoError\x10\x00\x12\x14\n\x10kFileCreateError\x10\x01\x12\x12\n\x0ekFileReadError\x10\x02\x12\x13\n\x0fkFileWriteError\x10\x03\"!\n\x11\x46ileCreateRequest\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"D\n\x14\x46ileReadRangeRequest\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\"V\n\x15\x46ileWriteRangeRequest\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0e\n\x06length\x18\x03 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\"T\n\x10\x46ileCreateResult\x12@\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x31.cohesity.experimental.aniket.protorpc.ErrorProto\"v\n\x13\x46ileReadRangeResult\x12@\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x31.cohesity.experimental.aniket.protorpc.ErrorProto\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x08\x12\x10\n\x08\x64\x61taread\x18\x03 \x01(\x0c\"X\n\x14\x46ileWriteRangeResult\x12@\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x31.cohesity.experimental.aniket.protorpc.ErrorProto2\xb1\x04\n\x0b\x46ileService\x12r\n\x05Greet\x12\x33.cohesity.experimental.aniket.protorpc.HelloRequest\x1a\x32.cohesity.experimental.aniket.protorpc.HelloResult\"\x00\x12\x81\x01\n\nFileCreate\x12\x38.cohesity.experimental.aniket.protorpc.FileCreateRequest\x1a\x37.cohesity.experimental.aniket.protorpc.FileCreateResult\"\x00\x12\x8a\x01\n\rFileReadRange\x12;.cohesity.experimental.aniket.protorpc.FileReadRangeRequest\x1a:.cohesity.experimental.aniket.protorpc.FileReadRangeResult\"\x00\x12\x8d\x01\n\x0e\x46ileWriteRange\x12<.cohesity.experimental.aniket.protorpc.FileWriteRangeRequest\x1a;.cohesity.experimental.aniket.protorpc.FileWriteRangeResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.aniket.protorpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_HELLOREQUEST']._serialized_start=120
  _globals['_HELLOREQUEST']._serialized_end=155
  _globals['_HELLORESULT']._serialized_start=157
  _globals['_HELLORESULT']._serialized_end=188
  _globals['_ERRORPROTO']._serialized_start=191
  _globals['_ERRORPROTO']._serialized_end=368
  _globals['_ERRORPROTO_TYPE']._serialized_start=285
  _globals['_ERRORPROTO_TYPE']._serialized_end=368
  _globals['_FILECREATEREQUEST']._serialized_start=370
  _globals['_FILECREATEREQUEST']._serialized_end=403
  _globals['_FILEREADRANGEREQUEST']._serialized_start=405
  _globals['_FILEREADRANGEREQUEST']._serialized_end=473
  _globals['_FILEWRITERANGEREQUEST']._serialized_start=475
  _globals['_FILEWRITERANGEREQUEST']._serialized_end=561
  _globals['_FILECREATERESULT']._serialized_start=563
  _globals['_FILECREATERESULT']._serialized_end=647
  _globals['_FILEREADRANGERESULT']._serialized_start=649
  _globals['_FILEREADRANGERESULT']._serialized_end=767
  _globals['_FILEWRITERANGERESULT']._serialized_start=769
  _globals['_FILEWRITERANGERESULT']._serialized_end=857
  _globals['_FILESERVICE']._serialized_start=860
  _globals['_FILESERVICE']._serialized_end=1421
# @@protoc_insertion_point(module_scope)