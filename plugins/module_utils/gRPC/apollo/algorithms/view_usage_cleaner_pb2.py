# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/algorithms/view_usage_cleaner.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*apollo/algorithms/view_usage_cleaner.proto\x12\x1a\x63ohesity.apollo.algorithms\x1a\x1c\x63onfigs/cluster_config.proto\"f\n ViewUsageCleanerContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x02(\x0b\x32$.cohesity.configs.ClusterConfigProto\".\n\x1bViewUsageCleanerMapKeyProto\x12\x0f\n\x07view_id\x18\x01 \x02(\x03\"~\n\x1dViewUsageCleanerMapValueProto\x12\x15\n\rin_view_usage\x18\x01 \x01(\x08\x12\x18\n\x10in_view_metadata\x18\x02 \x01(\x08\x12\x1a\n\x12scribe_row_version\x18\x03 \x01(\x03\x12\x10\n\x08in_stats\x18\x04 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.algorithms.view_usage_cleaner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VIEWUSAGECLEANERCONTEXTDATAPROTO']._serialized_start=104
  _globals['_VIEWUSAGECLEANERCONTEXTDATAPROTO']._serialized_end=206
  _globals['_VIEWUSAGECLEANERMAPKEYPROTO']._serialized_start=208
  _globals['_VIEWUSAGECLEANERMAPKEYPROTO']._serialized_end=254
  _globals['_VIEWUSAGECLEANERMAPVALUEPROTO']._serialized_start=256
  _globals['_VIEWUSAGECLEANERMAPVALUEPROTO']._serialized_end=382
# @@protoc_insertion_point(module_scope)
