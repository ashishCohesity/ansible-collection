# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/aabhas/rpc/file_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*experimental/aabhas/rpc/file_service.proto\x12 cohesity.experimental.aabhas.rpc\x1a\x1copen_util/net/protorpc.proto\"\x1d\n\tCreateMsg\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"\x1e\n\x0c\x43reateStatus\x12\x0e\n\x06status\x18\x01 \x01(\x08\";\n\x07ReadMsg\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06length\x18\x02 \x01(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\"\x1c\n\nReadStatus\x12\x0e\n\x06status\x18\x01 \x01(\x08\",\n\x08WriteMsg\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x05\"\x1d\n\x0bWriteStatus\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32\xda\x02\n\x0b\x46ileService\x12k\n\nCreateFile\x12+.cohesity.experimental.aabhas.rpc.CreateMsg\x1a..cohesity.experimental.aabhas.rpc.CreateStatus\"\x00\x12\x65\n\x08ReadFile\x12).cohesity.experimental.aabhas.rpc.ReadMsg\x1a,.cohesity.experimental.aabhas.rpc.ReadStatus\"\x00\x12h\n\tWriteFile\x12*.cohesity.experimental.aabhas.rpc.WriteMsg\x1a-.cohesity.experimental.aabhas.rpc.WriteStatus\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.aabhas.rpc.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILESERVICE']._loaded_options = None
  _globals['_FILESERVICE']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEMSG']._serialized_start=110
  _globals['_CREATEMSG']._serialized_end=139
  _globals['_CREATESTATUS']._serialized_start=141
  _globals['_CREATESTATUS']._serialized_end=171
  _globals['_READMSG']._serialized_start=173
  _globals['_READMSG']._serialized_end=232
  _globals['_READSTATUS']._serialized_start=234
  _globals['_READSTATUS']._serialized_end=262
  _globals['_WRITEMSG']._serialized_start=264
  _globals['_WRITEMSG']._serialized_end=308
  _globals['_WRITESTATUS']._serialized_start=310
  _globals['_WRITESTATUS']._serialized_end=339
  _globals['_FILESERVICE']._serialized_start=342
  _globals['_FILESERVICE']._serialized_end=688
# @@protoc_insertion_point(module_scope)
