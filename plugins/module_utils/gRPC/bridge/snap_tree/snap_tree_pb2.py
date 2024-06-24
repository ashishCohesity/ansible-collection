# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/snap_tree/snap_tree.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.base import cloud_pb2 as bridge_dot_base_dot_cloud__pb2
from util.base import cluster_instance_identifier_pb2 as util_dot_base_dot_cluster__instance__identifier__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n bridge/snap_tree/snap_tree.proto\x12\x19\x63ohesity.bridge.snap_tree\x1a\x17\x62ridge/base/cloud.proto\x1a+util/base/cluster_instance_identifier.proto\x1a\x18util/base/op_clock.proto\"B\n\x19SnapTreeValueVersionProto\x12\x16\n\x0e\x63reation_epoch\x18\x01 \x02(\x03\x12\r\n\x05\x63ount\x18\x02 \x02(\x03\"\xf2\x0b\n\x11SnapTreeNodeProto\x12\x0f\n\x07tree_id\x18\x01 \x02(\x03\x12\x0f\n\x07node_id\x18\x02 \x02(\x03\x12\x10\n\x08refcount\x18\x03 \x02(\x05\x12\x12\n\nis_deduped\x18\x0b \x01(\x08\x12H\n\troot_info\x18\x04 \x01(\x0b\x32\x35.cohesity.bridge.snap_tree.SnapTreeNodeProto.RootInfo\x12S\n\x11key_child_ptr_vec\x18\x05 \x03(\x0b\x32\x38.cohesity.bridge.snap_tree.SnapTreeNodeProto.KeyChildPtr\x12\x1b\n\x13leaf_level_distance\x18\x06 \x02(\x05\x12K\n\rvalue_version\x18\x07 \x01(\x0b\x32\x34.cohesity.bridge.snap_tree.SnapTreeValueVersionProto\x12&\n\x0bopclock_vec\x18\x08 \x03(\x0b\x32\x11.cohesity.OpClock\x12\x65\n\x1a\x61rchived_node_location_vec\x18\t \x03(\x0b\x32\x41.cohesity.bridge.snap_tree.SnapTreeNodeProto.ArchivedNodeLocation\x12%\n\x1dstub_node_restore_in_progress\x18\n \x01(\x08\x12\x1f\n\x13parent_node_tree_id\x18\x0c \x01(\x03:\x02-1\x12\x1f\n\x13parent_node_node_id\x18\r \x01(\x03:\x02-1\x1a\xa0\x01\n\x08RootInfo\x12\x15\n\nmin_degree\x18\x01 \x01(\x05:\x01\x38\x12\x12\n\nmax_degree\x18\x02 \x01(\x05\x12\x13\n\x0bmulti_homed\x18\x03 \x01(\x08\x12\x1a\n\x12\x64ynamic_max_degree\x18\x04 \x01(\x08\x12\x11\n\timmutable\x18\x05 \x01(\x08\x12%\n\x1dmin_degree_constraint_relaxed\x18\x06 \x01(\x08\x1a\xb1\x01\n\x0bKeyChildPtr\x12\x0f\n\x07key_int\x18\x01 \x01(\x03\x12\x0f\n\x07key_str\x18\x04 \x01(\x0c\x12\x19\n\x11\x63hild_ptr_tree_id\x18\x02 \x01(\x03\x12\x19\n\x11\x63hild_ptr_node_id\x18\x03 \x01(\x03\x12\x44\n\x18\x63hild_ptr_cloud_location\x18\x06 \x01(\x0b\x32\".cohesity.bridge.CloudNodePtrProtoJ\x04\x08\x05\x10\x06\x1a\x8c\x04\n\x14\x41rchivedNodeLocation\x12\x12\n\narchive_id\x18\x01 \x01(\x03\x12\x11\n\tentity_id\x18\x07 \x01(\x03\x12\x1b\n\x0f\x62\x61se_archive_id\x18\x02 \x01(\x03:\x02-1\x12\x11\n\tobject_id\x18\x03 \x01(\x03\x12\x37\n\ncluster_id\x18\x04 \x01(\x0b\x32#.cohesity.ClusterInstanceIdentifier\x12\x1c\n\x14segment_start_offset\x18\x05 \x01(\x03\x12\x13\n\x0bnode_offset\x18\x06 \x01(\x05\x12\x11\n\tdomain_id\x18\t \x01(\x03\x12:\n\x0e\x63loud_location\x18\n \x01(\x0b\x32\".cohesity.bridge.CloudNodePtrProto\x12#\n\x1bmax_bst_leaf_level_distance\x18\x0b \x01(\x05\x12#\n\x1bsub_tree_logical_size_bytes\x18\r \x01(\x03\x12\x12\n\nviewbox_id\x18\x0e \x01(\x03\x12\x34\n(minimum_subtree_retention_timestamp_secs\x18\x0f \x01(\x03:\x02-1\x12\x1f\n\x17sha256_summary_checksum\x18\x10 \x01(\x0cJ\x04\x08\x08\x10\tJ\x04\x08\x0c\x10\rR!sub_tree_brick_logical_size_bytesJ\x04\x08\x0e\x10\x0fR(minimum_subtree_retention_timestamp_secs\"\xcc\x02\n\x1cSnapTreeTraversalCookieProto\x12Z\n\ncookie_map\x18\x01 \x03(\x0b\x32\x46.cohesity.bridge.snap_tree.SnapTreeTraversalCookieProto.CookieMapEntry\x1aW\n\rSubTreeCookie\x12\x0f\n\x07key_int\x18\x01 \x01(\x03\x12\x0f\n\x07key_str\x18\x02 \x01(\t\x12$\n\x15is_sub_tree_traversed\x18\x03 \x01(\x08:\x05\x66\x61lse\x1aw\n\x0e\x43ookieMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12T\n\x05value\x18\x02 \x01(\x0b\x32\x45.cohesity.bridge.snap_tree.SnapTreeTraversalCookieProto.SubTreeCookie:\x02\x38\x01\"F\n\x14SnapTreeKeyOperation\".\n\x04Type\x12\n\n\x06kAdded\x10\x01\x12\x0c\n\x08kUpdated\x10\x02\x12\x0c\n\x08kRemoved\x10\x03\"\x83\x08\n\x14SnapTreeUpdateReason\x12Q\n\x0cmodifying_op\x18\x01 \x01(\x0e\x32;.cohesity.bridge.snap_tree.SnapTreeUpdateReason.ModifyingOp\x12\x46\n\x06reason\x18\x02 \x01(\x0e\x32\x36.cohesity.bridge.snap_tree.SnapTreeUpdateReason.Reason\x12\x10\n\x08refcount\x18\x03 \x01(\x05\x12I\n\x08\x66ix_type\x18\x04 \x01(\x0e\x32\x37.cohesity.bridge.snap_tree.SnapTreeUpdateReason.FixType\"\x8d\x03\n\x0bModifyingOp\x12\x19\n\x15kAdjustNodeRefcountOp\x10\x00\x12\x16\n\x12kBatchUpdateNanoOp\x10\x01\x12\x0c\n\x08kCloneOp\x10\x02\x12\x1a\n\x16kCreateStubNodesNanoOp\x10\x03\x12\x0e\n\nkCreatorOp\x10\x04\x12\x12\n\x0ekDeduplicateOp\x10\x05\x12\x14\n\x10kNodeFixerNanoOp\x10\x06\x12\x18\n\x14kOverwriteSnapTreeOp\x10\x07\x12\x1d\n\x19kRestoreStubNodeContentOp\x10\x08\x12\x15\n\x11kShadowCopyNanoOp\x10\t\x12\x10\n\x0ckTouchNodeOp\x10\n\x12\x15\n\x11kUpdateLeafNodeOp\x10\x0b\x12!\n\x1dkUpdateNodeArchivedLocationOp\x10\x0c\x12\r\n\tkUpdateOp\x10\x0e\x12\x15\n\x11kUpdateSnapTreeOp\x10\x0f\x12%\n!kUpdateStubNodeRestoreStateNanoOp\x10\x10\"\xfc\x01\n\x06Reason\x12\x0f\n\x0bkCreateRoot\x10\x00\x12\x0f\n\x0bkCreateNode\x10\x01\x12\x0f\n\x0bkDeleteNode\x10\x02\x12\x0f\n\x0bkUpdateRoot\x10\x03\x12\x0f\n\x0bkUpdateNode\x10\x04\x12\x11\n\rkUpdateParent\x10\x05\x12\x12\n\x0ekUpdateSrcRoot\x10\x06\x12\x13\n\x0fkUpdateDestRoot\x10\x07\x12\x14\n\x10kUpdateLeafToAdd\x10\x08\x12\x0f\n\x0bkCreateLeaf\x10\t\x12\x1a\n\x16kUpdateParentToAddLeaf\x10\n\x12\x1e\n\x1akUpdateParentToDeleteChild\x10\x0b\"d\n\x07\x46ixType\x12\t\n\x05kNone\x10\x00\x12\n\n\x06kSplit\x10\x01\x12\r\n\tkLeftJoin\x10\x02\x12\x0e\n\nkRightJoin\x10\x03\x12\x10\n\x0ckLeftShuffle\x10\x04\x12\x11\n\rkRightShuffle\x10\x05\x42\x1f\n\x1d\x63om.cohesity.bridge.snap_tree')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.snap_tree.snap_tree_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.cohesity.bridge.snap_tree'
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO_COOKIEMAPENTRY']._loaded_options = None
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO_COOKIEMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPTREEVALUEVERSIONPROTO']._serialized_start=159
  _globals['_SNAPTREEVALUEVERSIONPROTO']._serialized_end=225
  _globals['_SNAPTREENODEPROTO']._serialized_start=228
  _globals['_SNAPTREENODEPROTO']._serialized_end=1750
  _globals['_SNAPTREENODEPROTO_ROOTINFO']._serialized_start=835
  _globals['_SNAPTREENODEPROTO_ROOTINFO']._serialized_end=995
  _globals['_SNAPTREENODEPROTO_KEYCHILDPTR']._serialized_start=998
  _globals['_SNAPTREENODEPROTO_KEYCHILDPTR']._serialized_end=1175
  _globals['_SNAPTREENODEPROTO_ARCHIVEDNODELOCATION']._serialized_start=1178
  _globals['_SNAPTREENODEPROTO_ARCHIVEDNODELOCATION']._serialized_end=1702
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO']._serialized_start=1753
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO']._serialized_end=2085
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO_SUBTREECOOKIE']._serialized_start=1877
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO_SUBTREECOOKIE']._serialized_end=1964
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO_COOKIEMAPENTRY']._serialized_start=1966
  _globals['_SNAPTREETRAVERSALCOOKIEPROTO_COOKIEMAPENTRY']._serialized_end=2085
  _globals['_SNAPTREEKEYOPERATION']._serialized_start=2087
  _globals['_SNAPTREEKEYOPERATION']._serialized_end=2157
  _globals['_SNAPTREEKEYOPERATION_TYPE']._serialized_start=2111
  _globals['_SNAPTREEKEYOPERATION_TYPE']._serialized_end=2157
  _globals['_SNAPTREEUPDATEREASON']._serialized_start=2160
  _globals['_SNAPTREEUPDATEREASON']._serialized_end=3187
  _globals['_SNAPTREEUPDATEREASON_MODIFYINGOP']._serialized_start=2433
  _globals['_SNAPTREEUPDATEREASON_MODIFYINGOP']._serialized_end=2830
  _globals['_SNAPTREEUPDATEREASON_REASON']._serialized_start=2833
  _globals['_SNAPTREEUPDATEREASON_REASON']._serialized_end=3085
  _globals['_SNAPTREEUPDATEREASON_FIXTYPE']._serialized_start=3087
  _globals['_SNAPTREEUPDATEREASON_FIXTYPE']._serialized_end=3187
# @@protoc_insertion_point(module_scope)
