# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/madrox/master_state.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bridge/madrox/master_state.proto\x12\x16\x63ohesity.bridge.madrox\"\x9e\x01\n\x16RemoteClusterInfoProto\x12\x19\n\x11remote_cluster_id\x18\x01 \x02(\x03\x12%\n\x1dremote_cluster_incarnation_id\x18\x02 \x02(\x03\x12\x1d\n\x15last_heard_time_usecs\x18\x03 \x01(\x03\x12#\n\x1b\x65ncrypt_handshake_supported\x18\x04 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.madrox.master_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMOTECLUSTERINFOPROTO']._serialized_start=61
  _globals['_REMOTECLUSTERINFOPROTO']._serialized_end=219
# @@protoc_insertion_point(module_scope)