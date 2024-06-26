# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/algorithms/snap_tree_dedup/snap_tree_dedup.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.blob_store import blob_store_pb2 as bridge_dot_blob__store_dot_blob__store__pb2
from bridge.snap_tree import snap_tree_pb2 as bridge_dot_snap__tree_dot_snap__tree__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:apollo/mr/algorithms/snap_tree_dedup/snap_tree_dedup.proto\x12\x1d\x63ohesity.apollo.mr.algorithms\x1a\"bridge/blob_store/blob_store.proto\x1a bridge/snap_tree/snap_tree.proto\x1a\x1c\x63onfigs/cluster_config.proto\"\x96\x03\n\x1dSnapTreeDedupContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x01(\x0b\x32$.cohesity.configs.ClusterConfigProto\x12\x38\n-apollo_mr_snap_tree_dedup_minimum_nodes_count\x18\x02 \x01(\x05:\x01\x32\x12;\n-apollo_mr_snap_tree_dedup_maximum_nodes_count\x18\x03 \x01(\x05:\x04\x31\x30\x32\x34\x12\x42\n4apollo_mr_snap_tree_dedup_maximum_parent_nodes_count\x18\x04 \x01(\x05:\x04\x31\x30\x32\x34\x12:\n2snap_tree_dedup_action_emitter_num_shards_per_node\x18\x05 \x01(\x03\x12:\n2snap_tree_dedup_parent_reducer_num_shards_per_node\x18\x06 \x01(\x03\"\xcf\x01\n\x10SnapTreeDedupKey\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12\x14\n\x0c\x62rick_number\x18\x02 \x01(\x03\x12\x43\n\nextent_vec\x18\x03 \x03(\x0b\x32/.cohesity.bridge.blob.BrickMetadataProto.Extent\x12K\n\rvalue_version\x18\x04 \x01(\x0b\x32\x34.cohesity.bridge.snap_tree.SnapTreeValueVersionProto\"y\n\x08NodeInfo\x12\x0f\n\x07tree_id\x18\x01 \x01(\x03\x12\x0f\n\x07node_id\x18\x02 \x01(\x03\x12K\n\rvalue_version\x18\x03 \x01(\x0b\x32\x34.cohesity.bridge.snap_tree.SnapTreeValueVersionProto\"\xa1\x01\n\x1fSnapTreeDedupParentReducerProto\x12:\n\tnode_info\x18\x01 \x01(\x0b\x32\'.cohesity.apollo.mr.algorithms.NodeInfo\x12\x42\n\tdedup_key\x18\x02 \x01(\x0b\x32/.cohesity.apollo.mr.algorithms.SnapTreeDedupKey\"\x92\x01\n\x12SnapTreeDedupValue\x12@\n\x0fparent_info_vec\x18\x01 \x03(\x0b\x32\'.cohesity.apollo.mr.algorithms.NodeInfo\x12:\n\tnode_info\x18\x02 \x01(\x0b\x32\'.cohesity.apollo.mr.algorithms.NodeInfo')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.algorithms.snap_tree_dedup.snap_tree_dedup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SNAPTREEDEDUPCONTEXTDATAPROTO']._serialized_start=194
  _globals['_SNAPTREEDEDUPCONTEXTDATAPROTO']._serialized_end=600
  _globals['_SNAPTREEDEDUPKEY']._serialized_start=603
  _globals['_SNAPTREEDEDUPKEY']._serialized_end=810
  _globals['_NODEINFO']._serialized_start=812
  _globals['_NODEINFO']._serialized_end=933
  _globals['_SNAPTREEDEDUPPARENTREDUCERPROTO']._serialized_start=936
  _globals['_SNAPTREEDEDUPPARENTREDUCERPROTO']._serialized_end=1097
  _globals['_SNAPTREEDEDUPVALUE']._serialized_start=1100
  _globals['_SNAPTREEDEDUPVALUE']._serialized_end=1246
# @@protoc_insertion_point(module_scope)
