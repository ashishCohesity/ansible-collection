# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/algorithms/chunk_file_fixer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(apollo/algorithms/chunk_file_fixer.proto\x12\x1a\x63ohesity.apollo.algorithms\x1a\x1c\x63onfigs/cluster_config.proto\"~\n\x1e\x43hunkFileFixerContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x02(\x0b\x32$.cohesity.configs.ClusterConfigProto\x12\x18\n\x10num_constituents\x18\x02 \x02(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.algorithms.chunk_file_fixer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHUNKFILEFIXERCONTEXTDATAPROTO']._serialized_start=102
  _globals['_CHUNKFILEFIXERCONTEXTDATAPROTO']._serialized_end=228
# @@protoc_insertion_point(module_scope)