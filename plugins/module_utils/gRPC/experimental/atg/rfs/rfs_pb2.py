# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/atg/rfs/rfs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65xperimental/atg/rfs/rfs.proto\x12\x1d\x63ohesity.experimental.atg.rfs\x1a\x1copen_util/net/protorpc.proto\"\x1d\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1f\n\x0c\x43reateResult\x12\x0f\n\x07success\x18\x01 \x02(\x08\";\n\x0bReadRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x0e\n\x06length\x18\x03 \x02(\x03\"*\n\nReadResult\x12\x0e\n\x06length\x18\x01 \x02(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\":\n\x0cWriteRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\t\"\x1d\n\x0bWriteResult\x12\x0e\n\x06length\x18\x01 \x02(\x03\x32\xc0\x02\n\x03RFS\x12\x65\n\x06\x43reate\x12,.cohesity.experimental.atg.rfs.CreateRequest\x1a+.cohesity.experimental.atg.rfs.CreateResult\"\x00\x12_\n\x04Read\x12*.cohesity.experimental.atg.rfs.ReadRequest\x1a).cohesity.experimental.atg.rfs.ReadResult\"\x00\x12\x62\n\x05Write\x12+.cohesity.experimental.atg.rfs.WriteRequest\x1a*.cohesity.experimental.atg.rfs.WriteResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.atg.rfs.rfs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_RFS']._loaded_options = None
  _globals['_RFS']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEREQUEST']._serialized_start=95
  _globals['_CREATEREQUEST']._serialized_end=124
  _globals['_CREATERESULT']._serialized_start=126
  _globals['_CREATERESULT']._serialized_end=157
  _globals['_READREQUEST']._serialized_start=159
  _globals['_READREQUEST']._serialized_end=218
  _globals['_READRESULT']._serialized_start=220
  _globals['_READRESULT']._serialized_end=262
  _globals['_WRITEREQUEST']._serialized_start=264
  _globals['_WRITEREQUEST']._serialized_end=322
  _globals['_WRITERESULT']._serialized_start=324
  _globals['_WRITERESULT']._serialized_end=353
  _globals['_RFS']._serialized_start=356
  _globals['_RFS']._serialized_end=676
# @@protoc_insertion_point(module_scope)