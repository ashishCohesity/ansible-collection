# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo/mr/algorithms/view_snaptree_fixer/view_snaptree_fixer.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from bridge.snap_tree import snap_tree_pb2 as bridge_dot_snap__tree_dot_snap__tree__pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as bridge_dot_snap__fs_dot_snap__fs__metadata__pb2
from bridge.view_keeper import view_metadata_pb2 as bridge_dot_view__keeper_dot_view__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBapollo/mr/algorithms/view_snaptree_fixer/view_snaptree_fixer.proto\x12\x1d\x63ohesity.apollo.mr.algorithms\x1a\x1c\x63onfigs/cluster_config.proto\x1a bridge/snap_tree/snap_tree.proto\x1a%bridge/snap_fs/snap_fs_metadata.proto\x1a&bridge/view_keeper/view_metadata.proto\"\x81\x03\n!ViewSnapTreeFixerContextDataProto\x12\x42\n\x14\x63luster_config_proto\x18\x01 \x01(\x0b\x32$.cohesity.configs.ClusterConfigProto\x12#\n\x17max_view_snaptree_level\x18\x02 \x01(\x05:\x02-1\x12\x1f\n\x17\x65nable_orphan_entity_gc\x18\x03 \x01(\x08\x12&\n\x1e\x65nable_lazy_directory_deletion\x18\x04 \x01(\x08\x12\"\n\x1a\x65nable_s3lc_fixer_pipeline\x18\x05 \x01(\x08\x12\x1d\n\x11s3lc_inode_bucket\x18\x06 \x01(\x03:\x02\x33\x32\x12\x33\n+enable_delete_orphan_s3_inodes_with_intents\x18\x07 \x01(\x08\x12\x32\n*create_separate_scanner_for_each_vst_level\x18\x08 \x01(\x08\"\x82\x02\n\x1bViewSnapTreeIntentFixerInfo\x12\x16\n\x0esnap_fs_intent\x18\x01 \x01(\x08\x12\x11\n\ts3_intent\x18\x02 \x01(\x08\x12^\n\x11snap_fs_intent_id\x18\x03 \x01(\x0b\x32\x43.cohesity.apollo.mr.algorithms.ViewSnapTreeIntentFixerInfo.IntentId\x12\x1d\n\x15s3_empty_dir_deletion\x18\x04 \x01(\x08\x1a\x39\n\x08IntentId\x12\x16\n\x0eintent_id_high\x18\x01 \x01(\x04\x12\x15\n\rintent_id_low\x18\x02 \x01(\x04\"@\n\x0c\x45ntityGCInfo\x12\x16\n\x0eowner_inode_id\x18\x01 \x01(\x03\x12\x18\n\x10is_data_fragment\x18\x02 \x01(\x08\"\x88\x01\n\x0f\x41syncDeleteInfo\x12K\n\rvalue_version\x18\x01 \x01(\x0b\x32\x34.cohesity.bridge.snap_tree.SnapTreeValueVersionProto\x12\x16\n\x0eowner_inode_id\x18\x05 \x01(\x03J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"\xe7\x06\n\x16ViewSnapTreeFixerProto\x12\x11\n\tentity_id\x18\x01 \x01(\x03\x12\x0f\n\x07node_id\x18\x02 \x01(\x03\x12S\n\x0f\x66ix_intent_info\x18\x03 \x01(\x0b\x32:.cohesity.apollo.mr.algorithms.ViewSnapTreeIntentFixerInfo\x12@\n\x0b\x65ntity_info\x18\x04 \x01(\x0b\x32+.cohesity.apollo.mr.algorithms.EntityGCInfo\x12\x16\n\x0eparent_node_id\x18\x05 \x01(\x03\x12\x0f\n\x07view_id\x18\x06 \x01(\x03\x12\x15\n\rroot_inode_id\x18\x07 \x01(\x03\x12!\n\x19namespace_fixing_disabled\x18\t \x01(\x08\x12)\n!orphan_entities_deletion_disabled\x18\n \x01(\x08\x12\x16\n\x0eop_in_progress\x18\x08 \x01(\x08\x12\x1b\n\x13value_version_count\x18\x0b \x01(\x03\x12 \n\x18view_creation_time_usecs\x18\x0c \x01(\x03\x12I\n\x11\x61sync_delete_info\x18\r \x01(\x0b\x32..cohesity.apollo.mr.algorithms.AsyncDeleteInfo\x12\"\n\x1anum_garbage_data_fragments\x18\x0e \x01(\x03\x12/\n\'num_garbage_dir_embedded_data_fragments\x18\x0f \x01(\x03\x12\x18\n\x10is_root_inode_id\x18\x10 \x01(\x03\x12$\n\x1cmapped_from_view_usage_table\x18\x11 \x01(\x08\x12\x1b\n\x13num_orphan_entities\x18\x16 \x01(\x03\x12\x1c\n\x14num_orphan_fragments\x18\x17 \x01(\x03\x12\x13\n\x0bis_internal\x18\x18 \x01(\x03\x12\x1f\n\x17update_view_usage_table\x18\x19 \x01(\x08\x12*\n\"is_s3_view_with_empty_dir_deletion\x18\x1a \x01(\x08\x12\x18\n\x10publish_gc_stats\x18\x1b \x01(\x08J\x04\x08\x12\x10\x13J\x04\x08\x13\x10\x14J\x04\x08\x14\x10\x15J\x04\x08\x15\x10\x16\"U\n\x18S3LifeCycleFixerKeyProto\x12\x0f\n\x07view_id\x18\x01 \x01(\x03\x12\x17\n\x0finode_bucket_id\x18\x02 \x01(\x03\x12\x0f\n\x07node_id\x18\x03 \x01(\x03\"\xd4\x01\n\x1aS3LifeCycleFixerValueProto\x12\x13\n\x0bview_id_vec\x18\x01 \x03(\x03\x12\x19\n\x11\x63hild_node_id_vec\x18\x02 \x03(\x03\x12\x43\n\x0einode_metadata\x18\x03 \x01(\x0b\x32+.cohesity.bridge.snap_fs.InodeMetadataProto\x12\x41\n\x0fview_id_mapping\x18\x04 \x01(\x0b\x32(.cohesity.bridge.view.ViewIdMappingProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apollo.mr.algorithms.view_snaptree_fixer.view_snaptree_fixer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VIEWSNAPTREEFIXERCONTEXTDATAPROTO']._serialized_start=245
  _globals['_VIEWSNAPTREEFIXERCONTEXTDATAPROTO']._serialized_end=630
  _globals['_VIEWSNAPTREEINTENTFIXERINFO']._serialized_start=633
  _globals['_VIEWSNAPTREEINTENTFIXERINFO']._serialized_end=891
  _globals['_VIEWSNAPTREEINTENTFIXERINFO_INTENTID']._serialized_start=834
  _globals['_VIEWSNAPTREEINTENTFIXERINFO_INTENTID']._serialized_end=891
  _globals['_ENTITYGCINFO']._serialized_start=893
  _globals['_ENTITYGCINFO']._serialized_end=957
  _globals['_ASYNCDELETEINFO']._serialized_start=960
  _globals['_ASYNCDELETEINFO']._serialized_end=1096
  _globals['_VIEWSNAPTREEFIXERPROTO']._serialized_start=1099
  _globals['_VIEWSNAPTREEFIXERPROTO']._serialized_end=1970
  _globals['_S3LIFECYCLEFIXERKEYPROTO']._serialized_start=1972
  _globals['_S3LIFECYCLEFIXERKEYPROTO']._serialized_end=2057
  _globals['_S3LIFECYCLEFIXERVALUEPROTO']._serialized_start=2060
  _globals['_S3LIFECYCLEFIXERVALUEPROTO']._serialized_end=2272
# @@protoc_insertion_point(module_scope)
