# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gandalf/server/peer_info.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egandalf/server/peer_info.proto\x12\x17\x63ohesity.gandalf.server\"o\n\rPeerInfoProto\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x12\x13\n\x0bip_addr_str\x18\x02 \x02(\t\x12\x0c\n\x04port\x18\x03 \x02(\x05\x12*\n\x12liveness_namespace\x18\x04 \x01(\t:\x0egandalf_server')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gandalf.server.peer_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PEERINFOPROTO']._serialized_start=59
  _globals['_PEERINFOPROTO']._serialized_end=170
# @@protoc_insertion_point(module_scope)
