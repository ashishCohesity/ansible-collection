# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/anmol/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)experimental/anmol/rpc/file_service.proto\x12\x1f\x63ohesity.experimental.anmol.rpc\x1a\x1copen_util/net/protorpc.proto\"\xdd\x01\n\x05\x45rror\x12H\n\x04type\x18\x01 \x01(\x0e\x32\x30.cohesity.experimental.anmol.rpc.Error.ErrorType:\x08kNoError\x12\x11\n\terror_msg\x18\x02 \x01(\t\"w\n\tErrorType\x12\x11\n\rkAlreadyExist\x10\x01\x12\x0c\n\x08kSuccess\x10\x02\x12\x11\n\rkUnknownError\x10\x03\x12\x14\n\x10kBadRequestError\x10\x04\x12\x0c\n\x08kNoError\x10\x05\x12\x12\n\x0ekInvalidParams\x10\x06\"#\n\x0cHelloRequest\x12\x13\n\x04name\x18\x01 \x01(\t:\x05World\"+\n\rCreateFileReq\x12\x1a\n\x08\x66ilename\x18\x01 \x01(\t:\x08new_file\"<\n\x0bReadFileReq\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0b\n\x03len\x18\x03 \x01(\x03\"=\n\x0cWriteFileReq\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0b\n\x03len\x18\x03 \x01(\x03\"\x1f\n\x0bHelloResult\x12\x10\n\x08greeting\x18\x01 \x01(\t\"F\n\rCreateFileRes\x12\x35\n\x05\x65rror\x18\x01 \x01(\x0b\x32&.cohesity.experimental.anmol.rpc.Error\"D\n\x0bReadFileRes\x12\x35\n\x05\x65rror\x18\x01 \x01(\x0b\x32&.cohesity.experimental.anmol.rpc.Error\"E\n\x0cWriteFileRes\x12\x35\n\x05\x65rror\x18\x01 \x01(\x0b\x32&.cohesity.experimental.anmol.rpc.Error2\xcb\x03\n\x0b\x46ileService\x12\x66\n\x05Greet\x12-.cohesity.experimental.anmol.rpc.HelloRequest\x1a,.cohesity.experimental.anmol.rpc.HelloResult\"\x00\x12n\n\nCreateFile\x12..cohesity.experimental.anmol.rpc.CreateFileReq\x1a..cohesity.experimental.anmol.rpc.CreateFileRes\"\x00\x12h\n\x08ReadFile\x12,.cohesity.experimental.anmol.rpc.ReadFileReq\x1a,.cohesity.experimental.anmol.rpc.ReadFileRes\"\x00\x12k\n\tWriteFile\x12-.cohesity.experimental.anmol.rpc.WriteFileReq\x1a-.cohesity.experimental.anmol.rpc.WriteFileRes\"\x00\x1a\r\x80\xf1\x04\xb8\x17\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.anmol.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\270\027\210\361\004\001\220\361\004\002'
  _globals['_ERROR']._serialized_start=109
  _globals['_ERROR']._serialized_end=330
  _globals['_ERROR_ERRORTYPE']._serialized_start=211
  _globals['_ERROR_ERRORTYPE']._serialized_end=330
  _globals['_HELLOREQUEST']._serialized_start=332
  _globals['_HELLOREQUEST']._serialized_end=367
  _globals['_CREATEFILEREQ']._serialized_start=369
  _globals['_CREATEFILEREQ']._serialized_end=412
  _globals['_READFILEREQ']._serialized_start=414
  _globals['_READFILEREQ']._serialized_end=474
  _globals['_WRITEFILEREQ']._serialized_start=476
  _globals['_WRITEFILEREQ']._serialized_end=537
  _globals['_HELLORESULT']._serialized_start=539
  _globals['_HELLORESULT']._serialized_end=570
  _globals['_CREATEFILERES']._serialized_start=572
  _globals['_CREATEFILERES']._serialized_end=642
  _globals['_READFILERES']._serialized_start=644
  _globals['_READFILERES']._serialized_end=712
  _globals['_WRITEFILERES']._serialized_start=714
  _globals['_WRITEFILERES']._serialized_end=783
  _globals['_FILESERVICE']._serialized_start=786
  _globals['_FILESERVICE']._serialized_end=1245
# @@protoc_insertion_point(module_scope)
