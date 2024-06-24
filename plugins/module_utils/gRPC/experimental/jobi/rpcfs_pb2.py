# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/jobi/rpcfs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x65xperimental/jobi/rpcfs.proto\x12 cohesity.experimental.jobi.rpcfs\x1a\x1copen_util/net/protorpc.proto\x1a\x18util/base/op_clock.proto\"\x1d\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1f\n\x0c\x43reateResult\x12\x0f\n\x07success\x18\x01 \x02(\x08\"9\n\x0bReadRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x04\x12\x0c\n\x04size\x18\x03 \x02(\x04\"+\n\nReadResult\x12\r\n\x05\x65rror\x18\x01 \x02(\x05\x12\x0e\n\x06length\x18\x02 \x02(\x03\"<\n\x0cWriteRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06offset\x18\x02 \x02(\x04\x12\x0e\n\x06length\x18\x03 \x02(\x03\",\n\x0bWriteResult\x12\r\n\x05\x65rror\x18\x01 \x02(\x05\x12\x0e\n\x06length\x18\x02 \x02(\x03\x32\xd4\x02\n\x05RPCFS\x12k\n\x06\x43reate\x12/.cohesity.experimental.jobi.rpcfs.CreateRequest\x1a..cohesity.experimental.jobi.rpcfs.CreateResult\"\x00\x12\x65\n\x04Read\x12-.cohesity.experimental.jobi.rpcfs.ReadRequest\x1a,.cohesity.experimental.jobi.rpcfs.ReadResult\"\x00\x12h\n\x05Write\x12..cohesity.experimental.jobi.rpcfs.WriteRequest\x1a-.cohesity.experimental.jobi.rpcfs.WriteResult\"\x00\x1a\r\x80\xf1\x04\xe8\x07\x88\xf1\x04\x01\x90\xf1\x04\x02\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.jobi.rpcfs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_RPCFS']._loaded_options = None
  _globals['_RPCFS']._serialized_options = b'\200\361\004\350\007\210\361\004\001\220\361\004\002'
  _globals['_CREATEREQUEST']._serialized_start=123
  _globals['_CREATEREQUEST']._serialized_end=152
  _globals['_CREATERESULT']._serialized_start=154
  _globals['_CREATERESULT']._serialized_end=185
  _globals['_READREQUEST']._serialized_start=187
  _globals['_READREQUEST']._serialized_end=244
  _globals['_READRESULT']._serialized_start=246
  _globals['_READRESULT']._serialized_end=289
  _globals['_WRITEREQUEST']._serialized_start=291
  _globals['_WRITEREQUEST']._serialized_end=351
  _globals['_WRITERESULT']._serialized_start=353
  _globals['_WRITERESULT']._serialized_end=397
  _globals['_RPCFS']._serialized_start=400
  _globals['_RPCFS']._serialized_end=740
# @@protoc_insertion_point(module_scope)
