# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experimental/nachiket/coding_exercise/fops.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0experimental/nachiket/coding_exercise/fops.proto\x12.cohesity.experimental.nachiket.coding_exercise\x1a\x1copen_util/net/protorpc.proto\"*\n\rCreateRequest\x12\x19\n\x08\x66ilename\x18\x01 \x02(\t:\x07\x66oo.txt\"-\n\x0b\x43reateReply\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x0e\n\x06\x65rrnum\x18\x02 \x01(\x05\"?\n\x0bReadRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0e\n\x06length\x18\x02 \x02(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\"8\n\tReadReply\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x0b\n\x03\x62uf\x18\x02 \x01(\x0c\x12\x0e\n\x06\x65rrnum\x18\x03 \x01(\x05\"N\n\x0cWriteRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\x12\x0e\n\x06length\x18\x03 \x02(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x05\",\n\nWriteReply\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x0e\n\x06\x65rrnum\x18\x02 \x01(\x05\x32\xbd\x03\n\x0e\x46ileOperations\x12\x8a\x01\n\nCreateFile\x12=.cohesity.experimental.nachiket.coding_exercise.CreateRequest\x1a;.cohesity.experimental.nachiket.coding_exercise.CreateReply\"\x00\x12\x84\x01\n\x08ReadFile\x12;.cohesity.experimental.nachiket.coding_exercise.ReadRequest\x1a\x39.cohesity.experimental.nachiket.coding_exercise.ReadReply\"\x00\x12\x87\x01\n\tWriteFile\x12<.cohesity.experimental.nachiket.coding_exercise.WriteRequest\x1a:.cohesity.experimental.nachiket.coding_exercise.WriteReply\"\x00\x1a\r\x80\xf1\x04\x90N\x88\xf1\x04\x01\x90\xf1\x04\x05\x42\x03\x80\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'experimental.nachiket.coding_exercise.fops_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\200\001\001'
  _globals['_FILEOPERATIONS']._loaded_options = None
  _globals['_FILEOPERATIONS']._serialized_options = b'\200\361\004\220N\210\361\004\001\220\361\004\005'
  _globals['_CREATEREQUEST']._serialized_start=130
  _globals['_CREATEREQUEST']._serialized_end=172
  _globals['_CREATEREPLY']._serialized_start=174
  _globals['_CREATEREPLY']._serialized_end=219
  _globals['_READREQUEST']._serialized_start=221
  _globals['_READREQUEST']._serialized_end=284
  _globals['_READREPLY']._serialized_start=286
  _globals['_READREPLY']._serialized_end=342
  _globals['_WRITEREQUEST']._serialized_start=344
  _globals['_WRITEREQUEST']._serialized_end=422
  _globals['_WRITEREPLY']._serialized_start=424
  _globals['_WRITEREPLY']._serialized_end=468
  _globals['_FILEOPERATIONS']._serialized_start=471
  _globals['_FILEOPERATIONS']._serialized_end=916
# @@protoc_insertion_point(module_scope)
