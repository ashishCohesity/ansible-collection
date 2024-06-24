# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/sandy/fileservices/rpc.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)experimental/sandy/fileservices/rpc.proto\x12\x1f\x63ohesity.experimental.sandy.rpc\x1a\x1copen_util/net/protorpc.proto\"\x1e\n\nCreateFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"M\n\x10\x43reateFileResult\x12\x39\n\x05\x65rror\x18\x01 \x01(\x0e\x32*.cohesity.experimental.sandy.rpc.ErrorCode\"9\n\x08ReadFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x0b\n\x03len\x18\x03 \x01(\x05\"H\n\tWriteFile\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x0b\n\x03len\x18\x04 \x01(\x05\"k\n\x0eReadFileResult\x12\x39\n\x05\x65rror\x18\x01 \x01(\x0e\x32*.cohesity.experimental.sandy.rpc.ErrorCode\x12\x10\n\x08\x65rrormsg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"^\n\x0fWriteFileResult\x12\x39\n\x05\x65rror\x18\x01 \x01(\x0e\x32*.cohesity.experimental.sandy.rpc.ErrorCode\x12\x10\n\x08\x65rrormsg\x18\x02 \x01(\t*O\n\tErrorCode\x12\x0c\n\x08kSuccess\x10\x01\x12\x11\n\rkUnknownError\x10\x02\x12\r\n\trwSuccess\x10\x03\x12\x12\n\x0erwUnknownError\x10\x04\x32\xd7\x02\n\x0b\x46ileService\x12j\n\x06\x43reate\x12+.cohesity.experimental.sandy.rpc.CreateFile\x1a\x31.cohesity.experimental.sandy.rpc.CreateFileResult\"\x00\x12\x64\n\x04Read\x12).cohesity.experimental.sandy.rpc.ReadFile\x1a/.cohesity.experimental.sandy.rpc.ReadFileResult\"\x00\x12g\n\x05Write\x12*.cohesity.experimental.sandy.rpc.WriteFile\x1a\x30.cohesity.experimental.sandy.rpc.WriteFileResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x00\x90\xf1\x04\x03\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.sandy.fileservices.rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\000\220\361\004\003'
  _globals['_ERRORCODE']._serialized_start=557
  _globals['_ERRORCODE']._serialized_end=636
  _globals['_CREATEFILE']._serialized_start=108
  _globals['_CREATEFILE']._serialized_end=138
  _globals['_CREATEFILERESULT']._serialized_start=140
  _globals['_CREATEFILERESULT']._serialized_end=217
  _globals['_READFILE']._serialized_start=219
  _globals['_READFILE']._serialized_end=276
  _globals['_WRITEFILE']._serialized_start=278
  _globals['_WRITEFILE']._serialized_end=350
  _globals['_READFILERESULT']._serialized_start=352
  _globals['_READFILERESULT']._serialized_end=459
  _globals['_WRITEFILERESULT']._serialized_start=461
  _globals['_WRITEFILERESULT']._serialized_end=555
  _globals['_FILESERVICE']._serialized_start=639
  _globals['_FILESERVICE']._serialized_end=982
# @@protoc_insertion_point(module_scope)
