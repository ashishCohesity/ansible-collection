# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/algorithms/inode_stats/inode_stats.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo.mr.base import histogram_proto_pb2 as apollo_dot_mr_dot_base_dot_histogram__proto__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2apollo/mr/algorithms/inode_stats/inode_stats.proto\x12\x1d\x63ohesity.apollo.mr.algorithms\x1a$apollo/mr/base/histogram_proto.proto\x1a\x1c\x63onfigs/cluster_config.proto\"\xd3\x01\n\x1aInodeStatsContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x01(\x0b\x32$.cohesity.configs.ClusterConfigProto\x12#\n\x17max_view_snaptree_level\x18\x02 \x01(\x05:\x02-1\x12\x15\n\rextension_vec\x18\x03 \x03(\t\x12\x35\n&apollo_mr_enable_apollo_binary_logging\x18\x04 \x01(\x08:\x05\x66\x61lse\"]\n\x12InodeStatsKeyProto\x12\x0f\n\x07node_id\x18\x01 \x01(\x03\x12\x10\n\x08inode_id\x18\x02 \x01(\x03\x12\x0f\n\x07view_id\x18\x03 \x01(\x03\x12\x13\n\x0bview_box_id\x18\x04 \x01(\x03\"\x92\x01\n\x14InodeStatsValueProto\x12\x13\n\x0bview_id_vec\x18\x01 \x03(\x03\x12\x15\n\rchild_node_id\x18\x02 \x01(\x03\x12\x10\n\x08inode_id\x18\x03 \x01(\x03\x12\x14\n\x0clogical_size\x18\x04 \x01(\x03\x12\x11\n\textension\x18\x05 \x01(\t\x12\x13\n\x0bview_box_id\x18\x06 \x01(\x03\";\n\x0eInodeInfoProto\x12\x12\n\nviewbox_id\x18\x01 \x01(\x03\x12\x15\n\rphysical_size\x18\x02 \x01(\x03\"\xb0\x01\n\x18ViewBoxLogicalStatsProto\x12\x1f\n\x17\x63umulative_logical_size\x18\x01 \x01(\x03\x12.\n\x15mega_file_inode_stats\x18\x02 \x01(\x0b\x32\x0f.HistogramProto\x12*\n\x11total_inode_stats\x18\x03 \x01(\x0b\x32\x0f.HistogramProto\x12\x17\n\x0fnum_directories\x18\x04 \x01(\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.algorithms.inode_stats.inode_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INODESTATSCONTEXTDATAPROTO']._serialized_start=154
  _globals['_INODESTATSCONTEXTDATAPROTO']._serialized_end=365
  _globals['_INODESTATSKEYPROTO']._serialized_start=367
  _globals['_INODESTATSKEYPROTO']._serialized_end=460
  _globals['_INODESTATSVALUEPROTO']._serialized_start=463
  _globals['_INODESTATSVALUEPROTO']._serialized_end=609
  _globals['_INODEINFOPROTO']._serialized_start=611
  _globals['_INODEINFOPROTO']._serialized_end=670
  _globals['_VIEWBOXLOGICALSTATSPROTO']._serialized_start=673
  _globals['_VIEWBOXLOGICALSTATSPROTO']._serialized_end=849
# @@protoc_insertion_point(module_scope)
