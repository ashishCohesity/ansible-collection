# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configs/user_tunings.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63onfigs/user_tunings.proto\x12\x10\x63ohesity.configs\"\x9f\x1c\n\x0fUserTuningProto\x12\x43\n\x04mode\x18\x01 \x01(\x0e\x32&.cohesity.configs.UserTuningProto.Mode:\rkApolloNoMode\x12?\n\x05state\x18\x02 \x01(\x0e\x32(.cohesity.configs.UserTuningProto.Status:\x06kUnSet\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x1c\n\x10start_time_usecs\x18\x04 \x01(\x03:\x02-1\x12\x1a\n\x0e\x65nd_time_usecs\x18\x05 \x01(\x03:\x02-1\x12;\n\ngflags_vec\x18\x06 \x03(\x0b\x32\'.cohesity.configs.UserTuningProto.Gflag\x12\xc3\x07\n\x1c\x64\x65\x66\x61ult_apollo_common_gflags\x18\x07 \x01(\t:\x9c\x07[{\"name\":\"apollo_cluster_storage_usage_high_pct_threshold\",\"service_name\":\"kApollo\"},{\"name\":\"apollo_cluster_storage_usage_critical_pct_threshold\",\"service_name\":\"kApollo\"},{\"name\":\"apollo_mr_master_job_action_exec_time_min_pct\",\"service_name\":\"kApollo\",\"target_value\":\"99\"},{\"name\":\"apollo_mr_pipelines_to_run\",\"service_name\":\"kApollo\",\"target_value\":\"Healer,Healer_FastSnapTree,TierRebalancer,ReplicationFixer,ChunkFileCloudSpiller,SnapTreeDedup,MorphBricks,ViewSnapTreeFixer,StatsAggregation,StatsRollupGarbageCollection\"},{\"name\":\"apollo_mr_stats_aggregation_run_interval_secs\",\"service_name\":\"kApollo\",\"target_value\":\"3600\"},{\"name\":\"apollo_mr_stats_garbage_collection_run_interval_secs\",\"service_name\":\"kApollo\",\"target_value\":\"86400\"},{\"name\":\"bridge_apollo_action_admctl_threshold\",\"service_name\":\"kBridge\"},{\"name\":\"bridge_background_usage_num_chunk_files_to_process\",\"service_name\":\"kBridge\",\"target_value\":\"100\"}]\x12\x83\x05\n\x1e\x64\x65\x66\x61ult_apollo_chunk_gc_gflags\x18\x08 \x01(\t:\xda\x04[{\"name\":\"apollo_mr_healer_urgency\",\"service_name\":\"kApollo\",\"target_value\":\"10\"},{\"name\":\"apollo_mr_master_job_cancellation_duration_secs\",\"service_name\":\"kApollo\",\"target_value\":\"259200\"},{\"name\":\"apollo_mr_healer_fast_snaptree_max_duration_secs\",\"service_name\":\"kApollo\",\"target_value\":\"259200\"},{\"name\":\"apollo_mr_healer_max_duration_secs\",\"service_name\":\"kApollo\",\"target_value\":\"259200\"},{\"name\":\"apollo_mr_replication_fixer_run_interval_secs\",\"service_name\":\"kApollo\",\"target_value\":\"14400\"},{\"name\":\"apollo_mr_tier_rebalancer_run_interval_secs\",\"service_name\":\"kApollo\",\"target_value\":\"43200\"}]\x12\xa8\x05\n default_apollo_metadata_gc_glags\x18\t \x01(\t:\xfd\x04[{\"name\":\"apollo_mr_snap_tree_dedup_action_emitter_num_shards_per_node\",\"service_name\":\"kApollo\",\"target_value\":\"5\"},{\"name\":\"apollo_mr_snap_tree_dedup_parent_reducer_num_shards_per_node\",\"service_name\":\"kApollo\",\"target_value\":\"250\"},{\"name\":\"apollo_mr_healer_fast_snaptree_run_interval_secs\",\"service_name\":\"kApollo\",\"target_value\":\"0\"},{\"name\":\"apollo_mr_snap_tree_dedup_run_interval_secs\",\"service_name\":\"kApollo\",\"target_value\":\"0\"},{\"name\":\"bridge_admctl_snaptree_maintenance_threshold\",\"service_name\":\"kBridge\"},{\"name\":\"bridge_apollo_action_admctl_max_queued_snaptree_cloudspill\",\"service_name\":\"kBridge\",\"target_value\":\"10240\"}]\x12\xa7\x01\n2default_apollo_aggressive_node_disk_removal_gflags\x18\n \x01(\t:k[{\"name\":\"apollo_mr_replication_fixer_max_duration_secs\",\"service_name\":\"kApollo\",\"target_value\":\"345600\"}]\x12\x85\x02\n0default_apollo_aggressive_tier_rebalancer_gflags\x18\x0b \x01(\t:\xca\x01[{\"name\":\"apollo_mr_tier_rebalancer_max_duration_secs\",\"service_name\":\"kApollo\",\"target_value\":\"345600\"},{\"name\":\"apollo_mr_tier_rebalancer_action_priority\",\"service_name\":\"kApollo\",\"target_value\":\"2\"}]\x12\xfb\x01\n#default_apollo_aggressive_ec_gflags\x18\x0c \x01(\t:\xcd\x01[{\"name\":\"apollo_mr_healer_migrate_actions_per_node\",\"service_name\":\"kApollo\",\"target_value\":\"2000000\"},{\"name\":\"apollo_mr_min_ec_migrate_action_replica_bytes\",\"service_name\":\"kApollo\",\"target_value\":\"0\"}]\x1a\x65\n\x05Gflag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x11\n\told_value\x18\x03 \x01(\t\x12\x12\n\nold_reason\x18\x04 \x01(\t\x12\x11\n\tnew_value\x18\x05 \x01(\t\"\xbc\x01\n\x04Mode\x12\x11\n\rkApolloNoMode\x10\x00\x12\x1c\n\x18kApolloChunkGCAggressive\x10\x01\x12\x1f\n\x1bkApolloMetadataGCAggressive\x10\x02\x12$\n kApolloNodeDiskRemovalAggressive\x10\x03\x12#\n\x1fkApolloTierRebalancerAggressive\x10\x04\x12\x17\n\x13kApolloECAggressive\x10\x05\"2\n\x06Status\x12\n\n\x06kUnSet\x10\x00\x12\x12\n\x0ekSetInProgress\x10\x01\x12\x08\n\x04kSet\x10\x02\x42\x12Z\x10\x63ohesity/configs')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'configs.user_tunings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\020cohesity/configs'
  _globals['_USERTUNINGPROTO']._serialized_start=49
  _globals['_USERTUNINGPROTO']._serialized_end=3664
  _globals['_USERTUNINGPROTO_GFLAG']._serialized_start=3320
  _globals['_USERTUNINGPROTO_GFLAG']._serialized_end=3421
  _globals['_USERTUNINGPROTO_MODE']._serialized_start=3424
  _globals['_USERTUNINGPROTO_MODE']._serialized_end=3612
  _globals['_USERTUNINGPROTO_STATUS']._serialized_start=3614
  _globals['_USERTUNINGPROTO_STATUS']._serialized_end=3664
# @@protoc_insertion_point(module_scope)
