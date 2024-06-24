# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/apollo/apollo_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from bridge.apollo import actions_common_pb2 as bridge_dot_apollo_dot_actions__common__pb2
from bridge.snap_tree import snap_tree_pb2 as bridge_dot_snap__tree_dot_snap__tree__pb2
from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"bridge/apollo/apollo_actions.proto\x12\x16\x63ohesity.bridge.apollo\x1a\x1c\x63onfigs/cluster_config.proto\x1a\"bridge/apollo/actions_common.proto\x1a bridge/snap_tree/snap_tree.proto\x1a\x18util/base/op_clock.proto\x1a\x1cutil/base/universal_id.proto\"\x8a\x37\n\x0c\x41polloAction\x12\x17\n\x0bview_box_id\x18\x1f \x01(\x03:\x02-1\x12\x30\n\x15job_start_opclock_vec\x18\x13 \x03(\x0b\x32\x11.cohesity.OpClock\x12\x1c\n\x14high_priority_action\x18\x14 \x01(\x08\x12\x1e\n\x0c\x61lgorithm_id\x18\x15 \x01(\x05:\x08-1000000\x12@\n\tnode_info\x18\x16 \x01(\x0b\x32-.cohesity.bridge.apollo.ApolloAction.NodeInfo\x12\x44\n\x0bping_bridge\x18\x01 \x01(\x0b\x32/.cohesity.bridge.apollo.ApolloAction.PingBridge\x12\x31\n\x08\x66ix_view\x18\x02 \x01(\x0b\x32\x1f.cohesity.bridge.apollo.FixView\x12\x37\n\x0b\x64\x65lete_view\x18\x03 \x01(\x0b\x32\".cohesity.bridge.apollo.DeleteView\x12K\n\x0f\x64\x65lete_view_box\x18\x04 \x01(\x0b\x32\x32.cohesity.bridge.apollo.ApolloAction.DeleteViewBox\x12H\n\rdelete_chunks\x18\x06 \x01(\x0b\x32\x31.cohesity.bridge.apollo.ApolloAction.DeleteChunks\x12P\n\x12\x64\x65lete_scribe_rows\x18\x07 \x03(\x0b\x32\x34.cohesity.bridge.apollo.ApolloAction.DeleteScribeRow\x12N\n\x15\x61\x64just_node_refcounts\x18\x08 \x03(\x0b\x32/.cohesity.bridge.apollo.AdjustNodeRefcountProto\x12\x46\n\x0c\x64\x65\x64up_bricks\x18\t \x01(\x0b\x32\x30.cohesity.bridge.apollo.ApolloAction.DedupBricks\x12Z\n\x17\x66ix_chunk_file_metadata\x18\n \x01(\x0b\x32\x39.cohesity.bridge.apollo.ApolloAction.FixChunkFileMetadata\x12\x64\n\x1c\x64owntier_chunk_file_replicas\x18\x0b \x01(\x0b\x32>.cohesity.bridge.apollo.ApolloAction.DowntierChunkFileReplicas\x12\x66\n\x1drebalance_chunk_file_replicas\x18\x0c \x01(\x0b\x32?.cohesity.bridge.apollo.ApolloAction.RebalanceChunkFileReplicas\x12J\n\x0emigrate_chunks\x18\r \x01(\x0b\x32\x32.cohesity.bridge.apollo.ApolloAction.MigrateChunks\x12J\n\x19\x66ix_snap_fs_entity_handle\x18\x0e \x01(\x0b\x32\'.cohesity.bridge.apollo.FixEntityHandle\x12\x45\n\x14\x66ix_s3_entity_handle\x18& \x01(\x0b\x32\'.cohesity.bridge.apollo.FixEntityHandle\x12H\n\rdelete_bricks\x18\x0f \x01(\x0b\x32\x31.cohesity.bridge.apollo.ApolloAction.DeleteBricks\x12`\n\x1a\x61\x64just_inode_physical_size\x18\x10 \x01(\x0b\x32<.cohesity.bridge.apollo.ApolloAction.AdjustInodePhysicalSize\x12S\n\x13\x64\x65lete_cluster_node\x18\x11 \x01(\x0b\x32\x36.cohesity.bridge.apollo.ApolloAction.DeleteClusterNode\x12\x44\n\x0b\x64\x65lete_disk\x18\x12 \x01(\x0b\x32/.cohesity.bridge.apollo.ApolloAction.DeleteDisk\x12_\n\x19\x64\x65lete_bridge_constituent\x18\x17 \x01(\x0b\x32<.cohesity.bridge.apollo.ApolloAction.DeleteBridgeConstituent\x12\\\n\x18\x64\x65lete_disk_stats_entity\x18\x18 \x01(\x0b\x32:.cohesity.bridge.apollo.ApolloAction.DeleteDiskStatsEntity\x12\\\n\x18\x64\x65lete_node_stats_entity\x18\x19 \x01(\x0b\x32:.cohesity.bridge.apollo.ApolloAction.DeleteNodeStatsEntity\x12\x63\n\x1c\x64\x65lete_view_box_stats_entity\x18\x1a \x01(\x0b\x32=.cohesity.bridge.apollo.ApolloAction.DeleteViewBoxStatsEntity\x12S\n\x1a\x64\x65lete_expired_smb_session\x18\x1b \x01(\x0b\x32/.cohesity.bridge.apollo.DeleteExpiredSmbSession\x12i\n\x1f\x63loud_spill_chunk_file_replicas\x18\x1c \x01(\x0b\x32@.cohesity.bridge.apollo.ApolloAction.CloudSpillChunkFileReplicas\x12G\n\x14\x66ree_blob_byte_range\x18\x1d \x01(\x0b\x32).cohesity.bridge.apollo.FreeBlobByteRange\x12W\n\x17\x64\x65lete_stats_entity_vec\x18\x1e \x03(\x0b\x32\x36.cohesity.bridge.apollo.ApolloAction.DeleteStatsEntity\x12W\n\x15retire_icebox_archive\x18  \x01(\x0b\x32\x38.cohesity.bridge.apollo.ApolloAction.RetireIceboxArchive\x12^\n\x19icebox_fix_chunk_location\x18! \x01(\x0b\x32;.cohesity.bridge.apollo.ApolloAction.IceboxFixChunkLocation\x12\x64\n\'icebox_clean_chunk_location_entries_vec\x18\" \x03(\x0b\x32\x33.cohesity.bridge.apollo.ApolloAction.IceboxRowEntry\x12l\n/icebox_clean_snaptree_node_location_entries_vec\x18# \x03(\x0b\x32\x33.cohesity.bridge.apollo.ApolloAction.IceboxRowEntry\x12u\n8icebox_clean_restored_snaptree_node_location_entries_vec\x18$ \x03(\x0b\x32\x33.cohesity.bridge.apollo.ApolloAction.IceboxRowEntry\x12I\n\x0e\x66ix_view_usage\x18% \x01(\x0b\x32\x31.cohesity.bridge.apollo.ApolloAction.FixViewUsage\x12G\n\x14\x66ix_user_quota_usage\x18* \x01(\x0b\x32).cohesity.bridge.apollo.FixUserQuotaUsage\x12M\n\x17\x64\x65lete_user_quota_usage\x18+ \x01(\x0b\x32,.cohesity.bridge.apollo.DeleteUserQuotaUsage\x12O\n\x11insert_scribe_row\x18, \x01(\x0b\x32\x34.cohesity.bridge.apollo.ApolloAction.InsertScribeRow\x12$\n\x1cv2_action_payload_offset_vec\x18( \x03(\x03\x12\x19\n\x11v2_action_blob_id\x18) \x01(\x03\x1a`\n\x08NodeInfo\x12\x1c\n\x14\x65xpected_alive_nodes\x18\x01 \x03(\x03\x12\x1b\n\x13\x65xpected_down_nodes\x18\x02 \x03(\x03\x12\x19\n\x11preferred_node_id\x18\x03 \x01(\x03\x1a\x0c\n\nPingBridge\x1aU\n\rDeleteViewBox\x12\x13\n\x0bview_box_id\x18\x01 \x02(\x03\x12\x16\n\x0e\x61\x63k_for_apollo\x18\x02 \x01(\x08\x12\x17\n\x0f\x64\x65lete_view_box\x18\x03 \x01(\x08\x1a\xc5\x01\n\x0c\x44\x65leteChunks\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x15\n\rchunk_file_id\x18\x02 \x02(\x03\x12#\n\x1b\x65xpected_chunk_file_version\x18\x03 \x02(\x03\x12%\n\x1dserialized_chunk_id_proto_vec\x18\x04 \x03(\x0c\x12\"\n\x1asnap_tree_leaf_node_id_vec\x18\x05 \x03(\x03\x12\x13\n\x0b\x63hunk_count\x18\x06 \x01(\x05\x1a\x65\n\x0f\x44\x65leteScribeRow\x12\x10\n\x08table_id\x18\x01 \x02(\x05\x12\x0f\n\x07version\x18\x02 \x02(\x03\x12\x17\n\x0finteger_row_key\x18\x03 \x01(\x03\x12\x16\n\x0estring_row_key\x18\x04 \x01(\t\x1ak\n\x0b\x44\x65\x64upBricks\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x14\n\x0c\x62rick_number\x18\x02 \x02(\x03\x12\x12\n\nnum_bricks\x18\x03 \x02(\x05\x12\x17\n\x0f\x61vg_chunk_count\x18\x04 \x01(\x05\x1a}\n\x14\x46ixChunkFileMetadata\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x15\n\rchunk_file_id\x18\x02 \x02(\x03\x12\x1e\n\x16\x66ix_replication_action\x18\x03 \x01(\x08\x12\x13\n\x0b\x63hunk_count\x18\x04 \x01(\x05\x1a\xb3\x01\n\x19\x44owntierChunkFileReplicas\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x15\n\rchunk_file_id\x18\x02 \x02(\x03\x12\x1b\n\x13target_storage_tier\x18\x03 \x02(\t\x12\x16\n\x0escribe_version\x18\x04 \x02(\x03\x12\x1a\n\x12source_replica_vec\x18\x05 \x03(\x03\x12\x13\n\x0b\x63hunk_count\x18\x06 \x01(\x05\x1a\x94\x01\n\x1aRebalanceChunkFileReplicas\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x15\n\rchunk_file_id\x18\x02 \x02(\x03\x12\x17\n\x0ftarget_disk_vec\x18\x03 \x03(\x03\x12\x16\n\x0escribe_version\x18\x04 \x02(\x03\x12\x13\n\x0b\x63hunk_count\x18\x05 \x01(\x05\x1a\xb5\x03\n\rMigrateChunks\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x1b\n\x13target_storage_tier\x18\x02 \x02(\t\x12^\n\x11\x63ompression_level\x18\x03 \x02(\x0e\x32\x43.cohesity.configs.ClusterConfigProto.StoragePolicy.CompressionLevel\x12N\n\x10\x65ncryption_level\x18\x04 \x02(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.EncryptionLevel\x12\x19\n\x11\x63hunk_file_id_vec\x18\x05 \x03(\x03\x12 \n\x12is_reason_compress\x18\x06 \x02(\x08:\x04true\x12J\n\x10migrate_mode_vec\x18\x07 \x03(\x0e\x32\x30.cohesity.bridge.apollo.ApolloAction.MigrateMode\x12\x1e\n\x16may_increase_space_vec\x18\x08 \x03(\x08\x12\x13\n\x0b\x63hunk_count\x18\t \x01(\x05\x1a\xf8\x01\n\x0c\x44\x65leteBricks\x12\x19\n\x11view_snap_tree_id\x18\x01 \x02(\x03\x12\x19\n\x11view_leaf_node_id\x18\x02 \x02(\x03\x12T\n\x16\x65xpected_value_version\x18\x03 \x02(\x0b\x32\x34.cohesity.bridge.snap_tree.SnapTreeValueVersionProto\x12\x19\n\x11\x62lob_snap_tree_id\x18\x04 \x02(\x03\x12\x14\n\x0c\x62rick_number\x18\x05 \x02(\x03\x12\x12\n\nnum_bricks\x18\x06 \x02(\x05\x12\x17\n\x0f\x61vg_chunk_count\x18\x07 \x01(\x05\x1a\xc2\x01\n\x17\x41\x64justInodePhysicalSize\x12\x19\n\x11view_snap_tree_id\x18\x01 \x02(\x03\x12\x19\n\x11view_leaf_node_id\x18\x02 \x02(\x03\x12T\n\x16\x65xpected_value_version\x18\x03 \x02(\x0b\x32\x34.cohesity.bridge.snap_tree.SnapTreeValueVersionProto\x12\x1b\n\x13\x61\x64just_amount_bytes\x18\x04 \x02(\x03\x1a\xd2\x02\n\x11\x44\x65leteClusterNode\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x12$\n\x1c\x64isk_ids_to_mark_for_removal\x18\x02 \x03(\x03\x12\x16\n\x0e\x61\x63k_for_apollo\x18\x03 \x01(\x08\x12\x81\x01\n\x1d\x64\x65lete_from_cluster_partition\x18\x04 \x01(\x0b\x32Z.cohesity.bridge.apollo.ApolloAction.DeleteClusterNode.NodeDeleteFromClusterPartitionState\x12\x1b\n\x13\x64\x65lete_from_cluster\x18\x05 \x01(\x08\x1aM\n#NodeDeleteFromClusterPartitionState\x12&\n\x1e\x64isk_ids_to_clear_from_removal\x18\x01 \x03(\x03\x1aR\n\nDeleteDisk\x12\x0f\n\x07\x64isk_id\x18\x01 \x02(\x03\x12\x16\n\x0e\x61\x63k_for_apollo\x18\x02 \x01(\x08\x12\x1b\n\x13\x64\x65lete_from_cluster\x18\x03 \x01(\x08\x1a\x38\n\x17\x44\x65leteBridgeConstituent\x12\x1d\n\x15\x62ridge_constituent_id\x18\x01 \x02(\x03\x1a(\n\x15\x44\x65leteDiskStatsEntity\x12\x0f\n\x07\x64isk_id\x18\x01 \x02(\x03\x1a(\n\x15\x44\x65leteNodeStatsEntity\x12\x0f\n\x07node_id\x18\x01 \x02(\x03\x1a\x46\n\x18\x44\x65leteViewBoxStatsEntity\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12\x15\n\rview_box_name\x18\x02 \x01(\t\x1a\xd1\x03\n\x1b\x43loudSpillChunkFileReplicas\x12\x19\n\x11\x62lob_snap_tree_id\x18\x01 \x02(\x03\x12\x17\n\x0ftarget_vault_id\x18\x02 \x02(\x03\x12\x63\n\x0b\x63hunk_files\x18\x03 \x03(\x0b\x32N.cohesity.bridge.apollo.ApolloAction.CloudSpillChunkFileReplicas.ChunkFileInfo\x1a\x98\x02\n\rChunkFileInfo\x12\x15\n\rchunk_file_id\x18\x01 \x02(\x03\x12\x16\n\x0escribe_version\x18\x02 \x02(\x03\x12\x66\n\x19\x63urrent_compression_level\x18\x03 \x02(\x0e\x32\x43.cohesity.configs.ClusterConfigProto.StoragePolicy.CompressionLevel\x12V\n\x18\x63urrent_encryption_level\x18\x04 \x02(\x0e\x32\x34.cohesity.configs.ClusterConfigProto.EncryptionLevel\x12\x18\n\x10is_erasure_coded\x18\x05 \x01(\x08\x1a\x39\n\x11\x44\x65leteStatsEntity\x12$\n\x1cserialized_delete_entity_arg\x18\x01 \x01(\x0c\x1a\x46\n\x13RetireIceboxArchive\x12/\n\x0b\x61rchive_uid\x18\x01 \x02(\x0b\x32\x1a.cohesity.UniversalIdProto\x1a\x32\n\x16IceboxFixChunkLocation\x12\x18\n\x10\x63hunk_id_str_vec\x18\x01 \x03(\x0c\x1a\xbf\x01\n\x0eIceboxRowEntry\x12\x0f\n\x07key_str\x18\x01 \x02(\x0c\x12\x11\n\tvalue_str\x18\x02 \x02(\x0c\x12\x0f\n\x07version\x18\x03 \x02(\x03\x12#\n\x1bnum_chunk_locations_deleted\x18\x04 \x01(\x05\x12&\n\x0bopclock_vec\x18\x05 \x03(\x0b\x32\x11.cohesity.OpClock\x12+\n#num_non_ref_chunk_locations_deleted\x18\x06 \x01(\x05\x1a\xb1\x01\n\x0c\x46ixViewUsage\x12\x0f\n\x07view_id\x18\x01 \x02(\x03\x12\x19\n\x11root_snap_tree_id\x18\x02 \x02(\x03\x12\x1a\n\x12user_quota_enabled\x18\x03 \x01(\x08\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\x1a\n\x12mixed_mode_enabled\x18\x05 \x01(\x08\x12\x14\n\x0croot_dir_vec\x18\x06 \x03(\t\x12\x14\n\x0cviewbox_name\x18\x07 \x01(\t\x1aQ\n\x0fInsertScribeRow\x12\x10\n\x08table_id\x18\x01 \x02(\x05\x12\x13\n\x07version\x18\x02 \x01(\x03:\x02-1\x12\x17\n\x0finteger_row_key\x18\x03 \x01(\x03\"I\n\x0bMigrateMode\x12\x0b\n\x07kDefrag\x10\x00\x12\r\n\tkCompress\x10\x01\x12\x10\n\x0ckErasurecode\x10\x02\x12\x0c\n\x08kEncrypt\x10\x03J\x04\x08\x05\x10\x06J\x04\x08-\x10.B!Z\x1f\x62ridge/apollo/apollo_actions.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.apollo.apollo_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\037bridge/apollo/apollo_actions.pb'
  _globals['_APOLLOACTION']._serialized_start=219
  _globals['_APOLLOACTION']._serialized_end=7269
  _globals['_APOLLOACTION_NODEINFO']._serialized_start=3478
  _globals['_APOLLOACTION_NODEINFO']._serialized_end=3574
  _globals['_APOLLOACTION_PINGBRIDGE']._serialized_start=3576
  _globals['_APOLLOACTION_PINGBRIDGE']._serialized_end=3588
  _globals['_APOLLOACTION_DELETEVIEWBOX']._serialized_start=3590
  _globals['_APOLLOACTION_DELETEVIEWBOX']._serialized_end=3675
  _globals['_APOLLOACTION_DELETECHUNKS']._serialized_start=3678
  _globals['_APOLLOACTION_DELETECHUNKS']._serialized_end=3875
  _globals['_APOLLOACTION_DELETESCRIBEROW']._serialized_start=3877
  _globals['_APOLLOACTION_DELETESCRIBEROW']._serialized_end=3978
  _globals['_APOLLOACTION_DEDUPBRICKS']._serialized_start=3980
  _globals['_APOLLOACTION_DEDUPBRICKS']._serialized_end=4087
  _globals['_APOLLOACTION_FIXCHUNKFILEMETADATA']._serialized_start=4089
  _globals['_APOLLOACTION_FIXCHUNKFILEMETADATA']._serialized_end=4214
  _globals['_APOLLOACTION_DOWNTIERCHUNKFILEREPLICAS']._serialized_start=4217
  _globals['_APOLLOACTION_DOWNTIERCHUNKFILEREPLICAS']._serialized_end=4396
  _globals['_APOLLOACTION_REBALANCECHUNKFILEREPLICAS']._serialized_start=4399
  _globals['_APOLLOACTION_REBALANCECHUNKFILEREPLICAS']._serialized_end=4547
  _globals['_APOLLOACTION_MIGRATECHUNKS']._serialized_start=4550
  _globals['_APOLLOACTION_MIGRATECHUNKS']._serialized_end=4987
  _globals['_APOLLOACTION_DELETEBRICKS']._serialized_start=4990
  _globals['_APOLLOACTION_DELETEBRICKS']._serialized_end=5238
  _globals['_APOLLOACTION_ADJUSTINODEPHYSICALSIZE']._serialized_start=5241
  _globals['_APOLLOACTION_ADJUSTINODEPHYSICALSIZE']._serialized_end=5435
  _globals['_APOLLOACTION_DELETECLUSTERNODE']._serialized_start=5438
  _globals['_APOLLOACTION_DELETECLUSTERNODE']._serialized_end=5776
  _globals['_APOLLOACTION_DELETECLUSTERNODE_NODEDELETEFROMCLUSTERPARTITIONSTATE']._serialized_start=5699
  _globals['_APOLLOACTION_DELETECLUSTERNODE_NODEDELETEFROMCLUSTERPARTITIONSTATE']._serialized_end=5776
  _globals['_APOLLOACTION_DELETEDISK']._serialized_start=5778
  _globals['_APOLLOACTION_DELETEDISK']._serialized_end=5860
  _globals['_APOLLOACTION_DELETEBRIDGECONSTITUENT']._serialized_start=5862
  _globals['_APOLLOACTION_DELETEBRIDGECONSTITUENT']._serialized_end=5918
  _globals['_APOLLOACTION_DELETEDISKSTATSENTITY']._serialized_start=5920
  _globals['_APOLLOACTION_DELETEDISKSTATSENTITY']._serialized_end=5960
  _globals['_APOLLOACTION_DELETENODESTATSENTITY']._serialized_start=5962
  _globals['_APOLLOACTION_DELETENODESTATSENTITY']._serialized_end=6002
  _globals['_APOLLOACTION_DELETEVIEWBOXSTATSENTITY']._serialized_start=6004
  _globals['_APOLLOACTION_DELETEVIEWBOXSTATSENTITY']._serialized_end=6074
  _globals['_APOLLOACTION_CLOUDSPILLCHUNKFILEREPLICAS']._serialized_start=6077
  _globals['_APOLLOACTION_CLOUDSPILLCHUNKFILEREPLICAS']._serialized_end=6542
  _globals['_APOLLOACTION_CLOUDSPILLCHUNKFILEREPLICAS_CHUNKFILEINFO']._serialized_start=6262
  _globals['_APOLLOACTION_CLOUDSPILLCHUNKFILEREPLICAS_CHUNKFILEINFO']._serialized_end=6542
  _globals['_APOLLOACTION_DELETESTATSENTITY']._serialized_start=6544
  _globals['_APOLLOACTION_DELETESTATSENTITY']._serialized_end=6601
  _globals['_APOLLOACTION_RETIREICEBOXARCHIVE']._serialized_start=6603
  _globals['_APOLLOACTION_RETIREICEBOXARCHIVE']._serialized_end=6673
  _globals['_APOLLOACTION_ICEBOXFIXCHUNKLOCATION']._serialized_start=6675
  _globals['_APOLLOACTION_ICEBOXFIXCHUNKLOCATION']._serialized_end=6725
  _globals['_APOLLOACTION_ICEBOXROWENTRY']._serialized_start=6728
  _globals['_APOLLOACTION_ICEBOXROWENTRY']._serialized_end=6919
  _globals['_APOLLOACTION_FIXVIEWUSAGE']._serialized_start=6922
  _globals['_APOLLOACTION_FIXVIEWUSAGE']._serialized_end=7099
  _globals['_APOLLOACTION_INSERTSCRIBEROW']._serialized_start=7101
  _globals['_APOLLOACTION_INSERTSCRIBEROW']._serialized_end=7182
  _globals['_APOLLOACTION_MIGRATEMODE']._serialized_start=7184
  _globals['_APOLLOACTION_MIGRATEMODE']._serialized_end=7257
# @@protoc_insertion_point(module_scope)
