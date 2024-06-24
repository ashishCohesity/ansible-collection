# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scribe/newscribe/stub/stub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from util.base import op_clock_pb2 as util_dot_base_dot_op__clock__pb2
from open_util.net import protorpc_pb2 as open__util_dot_net_dot_protorpc__pb2
from scribe.base import scribe_pb2 as scribe_dot_base_dot_scribe__pb2
from scribe.newscribe.server import data_format_pb2 as scribe_dot_newscribe_dot_server_dot_data__format__pb2
from scribe.newscribe.stub import server_error_pb2 as scribe_dot_newscribe_dot_stub_dot_server__error__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from scribe.newscribe.base import liveness_pb2 as scribe_dot_newscribe_dot_base_dot_liveness__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n scribe/newscribe/stub/stub.proto\x12\x1b\x63ohesity.scribe.server.stub\x1a\x18util/base/op_clock.proto\x1a\x1copen_util/net/protorpc.proto\x1a\x18scribe/base/scribe.proto\x1a)scribe/newscribe/server/data_format.proto\x1a(scribe/newscribe/stub/server_error.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a$scribe/newscribe/base/liveness.proto\"W\n\nRpcContext\x12\x12\n\x06\x62ucket\x18\x01 \x02(\x05:\x02-1\x12\x11\n\x05table\x18\x02 \x02(\x05:\x02-1\x12\"\n\x16sender_timestamp_usecs\x18\x03 \x01(\x03:\x02-1\"k\n\x0eVersionContext\x12\x18\n\x0cview_version\x18\x01 \x01(\x03:\x02-1\x12\x1c\n\x10table_md_version\x18\x02 \x01(\x03:\x02-1\x12!\n\x15leader_lock_sequencer\x18\x03 \x01(\x03:\x02-1\"\x8a\x06\n\x08WriteArg\x12<\n\x0brpc_context\x18\x01 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12<\n\x06params\x18\x03 \x02(\x0b\x32,.cohesity.scribe.server.stub.WriteArg.Params\x12$\n\x1c\x61rg_creation_timestamp_msecs\x18\x04 \x01(\x03\x12$\n\x15maybe_dump_mem_traces\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rhistory_write\x18\x07 \x01(\x08:\x05\x66\x61lse\x1a\xd1\x03\n\x06Params\x12(\n\x06update\x18\x01 \x02(\x0b\x32\x18.cohesity.scribe.RowData\x12\x13\n\x07version\x18\x02 \x01(\x03:\x02-2\x12\x32\n\tsequencer\x18\x03 \x01(\x0b\x32\x1f.cohesity.scribe.SequencerProto\x12\'\n\x0cop_clock_vec\x18\x04 \x03(\x0b\x32\x11.cohesity.OpClock\x12;\n\x11scribe_qos_params\x18\x05 \x01(\x0b\x32 .cohesity.scribe.ScribeQoSParams\x12!\n\x19writer_writes_unique_data\x18\x06 \x01(\x08\x12/\n\x14\x65xpected_opclock_vec\x18\x07 \x03(\x0b\x32\x11.cohesity.OpClock\x12:\n\x13\x65xisting_column_vec\x18\x08 \x03(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12\x14\n\x0cpayload_size\x18\t \x01(\x03\x12\x16\n\x0epayload_offset\x18\n \x01(\x03\x12 \n\x18\x63lear_existing_sequencer\x18\x0b \x01(\x08\x12\x0e\n\x06reason\x18\x0c \x01(\x0c\"\r\n\x0bWriteResult\"\x80\x02\n\x0c\x42ulkWriteArg\x12<\n\x0brpc_context\x18\x01 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12\x46\n\x10write_params_vec\x18\x03 \x03(\x0b\x32,.cohesity.scribe.server.stub.WriteArg.Params\x12$\n\x1c\x61rg_creation_timestamp_msecs\x18\x04 \x01(\x03\"~\n\x12KeyServerErrorPair\x12*\n\x03key\x18\x01 \x02(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12<\n\x05\x65rror\x18\x02 \x02(\x0e\x32-.cohesity.scribe.server.ServerErrorProto.Type\"Y\n\x0f\x42ulkWriteResult\x12\x46\n\rkey_error_vec\x18\x01 \x03(\x0b\x32/.cohesity.scribe.server.stub.KeyServerErrorPair\"\xcf\x03\n\x17\x42ulkWriteTransactionArg\x12V\n\x0e\x62ucket_arg_vec\x18\x01 \x03(\x0b\x32>.cohesity.scribe.server.stub.BulkWriteTransactionArg.BucketArg\x12]\n\x10\x62ulk_rpc_context\x18\x02 \x01(\x0b\x32\x43.cohesity.scribe.server.stub.BulkWriteTransactionArg.BulkRpcContext\x1a\xb0\x01\n\tBucketArg\x12\x15\n\tbucket_id\x18\x01 \x02(\x05:\x02-1\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12\x46\n\x10write_params_vec\x18\x03 \x03(\x0b\x32,.cohesity.scribe.server.stub.WriteArg.Params\x1aJ\n\x0e\x42ulkRpcContext\x12\x14\n\x08table_id\x18\x01 \x02(\x05:\x02-1\x12\"\n\x16sender_timestamp_usecs\x18\x02 \x01(\x03:\x02-1\"\x83\x02\n\x18\x42ulkWriteForMigrationArg\x12<\n\x0brpc_context\x18\x01 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12=\n\x07records\x18\x03 \x03(\x0b\x32,.cohesity.scribe.server.stub.WriteArg.Params\x12$\n\x1c\x61rg_creation_timestamp_msecs\x18\x04 \x01(\x03\"`\n\x1b\x42ulkWriteForMigrationResult\x12\x1d\n\x15num_records_persisted\x18\x01 \x01(\x03\x12\"\n\x1anum_rocksdb_rows_persisted\x18\x02 \x01(\x03\"\xf0\x04\n\x07ReadArg\x12<\n\x0brpc_context\x18\x01 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12*\n\x03key\x18\x03 \x02(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12;\n\x06params\x18\x04 \x02(\x0b\x32+.cohesity.scribe.server.stub.ReadArg.Params\x12$\n\x1c\x61rg_creation_timestamp_msecs\x18\x05 \x01(\x03\x12$\n\x15maybe_dump_mem_traces\x18\x06 \x01(\x08:\x05\x66\x61lse\x1a\xab\x02\n\x06Params\x12.\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12\x32\n\tsequencer\x18\x02 \x01(\x0b\x32\x1f.cohesity.scribe.SequencerProto\x12*\n\x0fop_clock_to_add\x18\x03 \x01(\x0b\x32\x11.cohesity.OpClock\x12\x1f\n\x10\x63reate_tombstone\x18\x04 \x01(\x08:\x05\x66\x61lse\x12;\n\x11scribe_qos_params\x18\x05 \x01(\x0b\x32 .cohesity.scribe.ScribeQoSParams\x12\x11\n\tlist_only\x18\x06 \x01(\x08\x12 \n\x18\x63lear_existing_sequencer\x18\x07 \x01(\x08\"9\n\nReadResult\x12+\n\x03row\x18\x01 \x01(\x0b\x32\x1e.cohesity.scribe.ReadRowResult\"\x9e\x06\n\x0cRangeScanArg\x12,\n\trow_range\x18\x01 \x01(\x0b\x32\x19.cohesity.scribe.RowRange\x12<\n\x0brpc_context\x18\x02 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x03 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12@\n\x06params\x18\x04 \x02(\x0b\x32\x30.cohesity.scribe.server.stub.RangeScanArg.Params\x12-\n\x06\x63ookie\x18\x05 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12\x1d\n\x15sender_constituent_id\x18\x06 \x01(\x03\x12&\n\x1eresponse_size_limit_hint_bytes\x18\x07 \x01(\x03\x12\x1d\n\x15maybe_dump_mem_traces\x18\x08 \x01(\x08\x12\x1f\n\x17response_num_rows_limit\x18\t \x01(\x05\x12\x1f\n\x17is_throttled_range_scan\x18\n \x01(\x08\x12\x1e\n\x12\x62ucket_incarnation\x18\x0b \x01(\x03:\x02-1\x1a\xa2\x02\n\x06Params\x12.\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12R\n\x16range_scan_consistency\x18\x03 \x01(\x0e\x32%.cohesity.scribe.RangeScanConsistency:\x0bkConsistent\x12\x37\n+range_scan_row_payload_size_threshold_bytes\x18\x04 \x01(\x05:\x02-1\x12\x15\n\tis_sorted\x18\x05 \x01(\x08\x42\x02\x18\x01\x12)\n\x1d\x63\x61pacity_per_column_per_batch\x18\x06 \x01(\x05:\x02-1\x12\x13\n\x0b\x63lient_name\x18\x07 \x01(\tJ\x04\x08\x01\x10\x02\"\x80\x02\n\x0fRangeScanResult\x12,\n\x04rows\x18\x01 \x03(\x0b\x32\x1e.cohesity.scribe.ReadRowResult\x12\x36\n\x0funresolved_rows\x18\x02 \x03(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12(\n\x1amay_have_inconsistent_rows\x18\x03 \x01(\x08:\x04true\x12=\n\x16range_scan_next_cookie\x18\x04 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12\x1e\n\x12\x62ucket_incarnation\x18\x05 \x01(\x03:\x02-1\"\xe1\x01\n\x0eHistoryReadArg\x12,\n\trow_range\x18\x01 \x01(\x0b\x32\x19.cohesity.scribe.RowRange\x12\x42\n\x06params\x18\x02 \x02(\x0b\x32\x32.cohesity.scribe.server.stub.HistoryReadArg.Params\x12#\n\x17response_num_rows_limit\x18\x03 \x01(\x05:\x02-1\x1a\x38\n\x06Params\x12.\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\"\xc1\x01\n\x0fGetDebugInfoArg\x12<\n\x0brpc_context\x18\x01 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12*\n\x03key\x18\x03 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\"\x9f\x02\n\x12GetDebugInfoResult\x12\x12\n\ndebug_info\x18\x01 \x01(\x0c\x12*\n\x03key\x18\x02 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12U\n\x10replica_info_vec\x18\x03 \x03(\x0b\x32;.cohesity.scribe.server.stub.GetDebugInfoResult.ReplicaInfo\x12\x0e\n\x06\x62ucket\x18\x04 \x01(\x05\x12\r\n\x05table\x18\x05 \x01(\x05\x1aS\n\x0bReplicaInfo\x12\x16\n\x0e\x63onstituent_id\x18\x01 \x01(\x03\x12,\n\x06row_md\x18\x02 \x01(\x0b\x32\x1c.cohesity.scribe.ScribeRowMD\"G\n\x18GetConstituentForKeysArg\x12+\n\x04keys\x18\x01 \x03(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\"r\n\x11\x43onstituentForKey\x12*\n\x03key\x18\x01 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12\x1a\n\x0e\x63onstituent_id\x18\x02 \x01(\x03:\x02-1\x12\x15\n\tbucket_id\x18\x03 \x01(\x05:\x02-1\"]\n\x1bGetConstituentForKeysResult\x12>\n\x06result\x18\x01 \x03(\x0b\x32..cohesity.scribe.server.stub.ConstituentForKey\"\x9d\x01\n\x17GetTableInfoInBucketArg\x12<\n\x0brpc_context\x18\x01 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x02 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\"?\n\x1aGetTableInfoInBucketResult\x12!\n\x19\x61pproximate_size_in_bytes\x18\x01 \x01(\x03\"$\n\x0e\x44\x65leteTableArg\x12\x12\n\ntable_name\x18\x01 \x02(\x0c\"\x13\n\x11\x44\x65leteTableResult\"\xfc\x01\n\x18ShuffleBucketsForTestArg\x12W\n\x0cshuffle_type\x18\x01 \x01(\x0e\x32\x41.cohesity.scribe.server.stub.ShuffleBucketsForTestArg.ShuffleType\"\x86\x01\n\x0bShuffleType\x12\x18\n\x14kFakeGracefulRemoval\x10\x00\x12\x15\n\x11kFakeForceRemoval\x10\x01\x12\x15\n\x11kReshuffleBuckets\x10\x02\x12\x11\n\rkFakeRFSwitch\x10\x03\x12\x1c\n\x18kFakePlacementModeSwitch\x10\x04\"\x1d\n\x1bShuffleBucketsForTestResult\"\xf9\x01\n\x15GetClusterCapacityArg\x12$\n\x15\x66orce_homogenous_mode\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x0fremoved_node_id\x18\x02 \x01(\x03\x12\x17\n\x0fremoved_disk_id\x18\x03 \x01(\x03\x12_\n\x18metadata_fault_tolerance\x18\x04 \x01(\x0b\x32=.cohesity.configs.ClusterConfigProto.FaultToleranceStrictness\x12\'\n\x1fmetadata_fault_tolerance_factor\x18\x05 \x01(\x03\":\n\x18GetClusterCapacityResult\x12\x1e\n\x16\x63luster_capacity_bytes\x18\x01 \x02(\x03\"$\n\x12GetBucketLeaderArg\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\x05\"\xc5\x01\n\x15GetBucketLeaderResult\x12\x1a\n\x0e\x63onstituent_id\x18\x01 \x01(\x03:\x02-1\x12\x1a\n\x0elock_sequencer\x18\x02 \x01(\x03:\x02-1\x12\x16\n\nip_address\x18\x03 \x01(\tB\x02\x18\x01\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12N\n\x15network_interface_vec\x18\x05 \x03(\x0b\x32/.cohesity.scribe.LivenessProto.NetworkInterface\"A\n\x15GetShuffleProgressArg\x12\x13\n\x0b\x64isk_id_vec\x18\x01 \x03(\x03\x12\x13\n\x0bnode_id_vec\x18\x02 \x03(\x03\"\xce\x03\n\x18GetShuffleProgressResult\x12\x64\n\x15\x64isk_shuffle_stat_vec\x18\x01 \x03(\x0b\x32\x45.cohesity.scribe.server.stub.GetShuffleProgressResult.DiskShuffleStat\x12\x14\n\x0cis_shuffling\x18\x02 \x01(\x08\x12 \n\x18shuffle_start_time_usecs\x18\x03 \x01(\x03\x1a\x93\x02\n\x0f\x44iskShuffleStat\x12\x0f\n\x07\x64isk_id\x18\x01 \x01(\x03\x12\x16\n\x0e\x63onstituent_id\x18\x02 \x01(\x03\x12\x0f\n\x07node_id\x18\x03 \x01(\x03\x12$\n\x1cnum_buckets_at_shuffle_start\x18\x04 \x01(\x05\x12\x1e\n\x16num_buckets_hosted_now\x18\x05 \x01(\x05\x12Z\n\x05\x65rror\x18\x06 \x01(\x0e\x32K.cohesity.scribe.server.stub.GetShuffleProgressResult.DiskShuffleStat.Error\"$\n\x05\x45rror\x12\x0c\n\x08kNoError\x10\x00\x12\r\n\tkNotFound\x10\x01\"\xea\x02\n\x0e\x44\x65leteRangeArg\x12,\n\trow_range\x18\x01 \x01(\x0b\x32\x19.cohesity.scribe.RowRange\x12<\n\x0brpc_context\x18\x02 \x02(\x0b\x32\'.cohesity.scribe.server.stub.RpcContext\x12\x44\n\x0fversion_context\x18\x03 \x02(\x0b\x32+.cohesity.scribe.server.stub.VersionContext\x12\x1d\n\x15sender_constituent_id\x18\x04 \x01(\x03\x12\x1d\n\x15maybe_dump_mem_traces\x18\x05 \x01(\x08\x12-\n\x06\x63ookie\x18\x06 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey\x12$\n\x1c\x61rg_creation_timestamp_msecs\x18\x07 \x01(\x03\x12\x13\n\x0b\x63lient_name\x18\x08 \x01(\t\"R\n\x11\x44\x65leteRangeResult\x12=\n\x16range_scan_next_cookie\x18\x01 \x01(\x0b\x32\x1d.cohesity.scribe.RowColumnKey2\xa5\t\n\nRpcService\x12W\n\x04Read\x12$.cohesity.scribe.server.stub.ReadArg\x1a\'.cohesity.scribe.server.stub.ReadResult\"\x00\x12l\n\tRangeScan\x12).cohesity.scribe.server.stub.RangeScanArg\x1a,.cohesity.scribe.server.stub.RangeScanResult\"\x06\x80\xe2\t\xa0\x9c\x01\x12Z\n\x05Write\x12%.cohesity.scribe.server.stub.WriteArg\x1a(.cohesity.scribe.server.stub.WriteResult\"\x00\x12\x66\n\tBulkWrite\x12).cohesity.scribe.server.stub.BulkWriteArg\x1a,.cohesity.scribe.server.stub.BulkWriteResult\"\x00\x12|\n\x14\x42ulkWriteTransaction\x12\x34.cohesity.scribe.server.stub.BulkWriteTransactionArg\x1a,.cohesity.scribe.server.stub.BulkWriteResult\"\x00\x12}\n\x15WriteTransactionBatch\x12\x34.cohesity.scribe.server.stub.BulkWriteTransactionArg\x1a,.cohesity.scribe.server.stub.BulkWriteResult\"\x00\x12r\n\x0b\x44\x65leteRange\x12+.cohesity.scribe.server.stub.DeleteRangeArg\x1a..cohesity.scribe.server.stub.DeleteRangeResult\"\x06\x80\xe2\t\xa0\x9c\x01\x12\x90\x01\n\x15\x42ulkWriteForMigration\x12\x35.cohesity.scribe.server.stub.BulkWriteForMigrationArg\x1a\x38.cohesity.scribe.server.stub.BulkWriteForMigrationResult\"\x06\x80\xe2\t\xb0\xea\x01\x12o\n\x0cGetDebugInfo\x12,.cohesity.scribe.server.stub.GetDebugInfoArg\x1a/.cohesity.scribe.server.stub.GetDebugInfoResult\"\x00\x12\x87\x01\n\x14GetTableInfoInBucket\x12\x34.cohesity.scribe.server.stub.GetTableInfoInBucketArg\x1a\x37.cohesity.scribe.server.stub.GetTableInfoInBucketResult\"\x00\x1a\r\x80\xf1\x04\x88\'\x88\xf1\x04\x00\x90\xf1\x04\x00\x32\x9e\x05\n\x10MasterRpcService\x12l\n\x0b\x44\x65leteTable\x12+.cohesity.scribe.server.stub.DeleteTableArg\x1a..cohesity.scribe.server.stub.DeleteTableResult\"\x00\x12x\n\x0fGetBucketLeader\x12/.cohesity.scribe.server.stub.GetBucketLeaderArg\x1a\x32.cohesity.scribe.server.stub.GetBucketLeaderResult\"\x00\x12\x8a\x01\n\x15ShuffleBucketsForTest\x12\x35.cohesity.scribe.server.stub.ShuffleBucketsForTestArg\x1a\x38.cohesity.scribe.server.stub.ShuffleBucketsForTestResult\"\x00\x12\x81\x01\n\x12GetClusterCapacity\x12\x32.cohesity.scribe.server.stub.GetClusterCapacityArg\x1a\x35.cohesity.scribe.server.stub.GetClusterCapacityResult\"\x00\x12\x81\x01\n\x12GetShuffleProgress\x12\x32.cohesity.scribe.server.stub.GetShuffleProgressArg\x1a\x35.cohesity.scribe.server.stub.GetShuffleProgressResult\"\x00\x1a\r\x80\xf1\x04\x88\'\x88\xf1\x04\x00\x90\xf1\x04\x00\x42\x08H\x01\x80\x01\x01\xf8\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scribe.newscribe.stub.stub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\200\001\001\370\001\001'
  _globals['_RANGESCANARG_PARAMS'].fields_by_name['is_sorted']._loaded_options = None
  _globals['_RANGESCANARG_PARAMS'].fields_by_name['is_sorted']._serialized_options = b'\030\001'
  _globals['_GETBUCKETLEADERRESULT'].fields_by_name['ip_address']._loaded_options = None
  _globals['_GETBUCKETLEADERRESULT'].fields_by_name['ip_address']._serialized_options = b'\030\001'
  _globals['_RPCSERVICE']._loaded_options = None
  _globals['_RPCSERVICE']._serialized_options = b'\200\361\004\210\'\210\361\004\000\220\361\004\000'
  _globals['_RPCSERVICE'].methods_by_name['RangeScan']._loaded_options = None
  _globals['_RPCSERVICE'].methods_by_name['RangeScan']._serialized_options = b'\200\342\t\240\234\001'
  _globals['_RPCSERVICE'].methods_by_name['DeleteRange']._loaded_options = None
  _globals['_RPCSERVICE'].methods_by_name['DeleteRange']._serialized_options = b'\200\342\t\240\234\001'
  _globals['_RPCSERVICE'].methods_by_name['BulkWriteForMigration']._loaded_options = None
  _globals['_RPCSERVICE'].methods_by_name['BulkWriteForMigration']._serialized_options = b'\200\342\t\260\352\001'
  _globals['_MASTERRPCSERVICE']._loaded_options = None
  _globals['_MASTERRPCSERVICE']._serialized_options = b'\200\361\004\210\'\210\361\004\000\220\361\004\000'
  _globals['_RPCCONTEXT']._serialized_start=300
  _globals['_RPCCONTEXT']._serialized_end=387
  _globals['_VERSIONCONTEXT']._serialized_start=389
  _globals['_VERSIONCONTEXT']._serialized_end=496
  _globals['_WRITEARG']._serialized_start=499
  _globals['_WRITEARG']._serialized_end=1277
  _globals['_WRITEARG_PARAMS']._serialized_start=812
  _globals['_WRITEARG_PARAMS']._serialized_end=1277
  _globals['_WRITERESULT']._serialized_start=1279
  _globals['_WRITERESULT']._serialized_end=1292
  _globals['_BULKWRITEARG']._serialized_start=1295
  _globals['_BULKWRITEARG']._serialized_end=1551
  _globals['_KEYSERVERERRORPAIR']._serialized_start=1553
  _globals['_KEYSERVERERRORPAIR']._serialized_end=1679
  _globals['_BULKWRITERESULT']._serialized_start=1681
  _globals['_BULKWRITERESULT']._serialized_end=1770
  _globals['_BULKWRITETRANSACTIONARG']._serialized_start=1773
  _globals['_BULKWRITETRANSACTIONARG']._serialized_end=2236
  _globals['_BULKWRITETRANSACTIONARG_BUCKETARG']._serialized_start=1984
  _globals['_BULKWRITETRANSACTIONARG_BUCKETARG']._serialized_end=2160
  _globals['_BULKWRITETRANSACTIONARG_BULKRPCCONTEXT']._serialized_start=2162
  _globals['_BULKWRITETRANSACTIONARG_BULKRPCCONTEXT']._serialized_end=2236
  _globals['_BULKWRITEFORMIGRATIONARG']._serialized_start=2239
  _globals['_BULKWRITEFORMIGRATIONARG']._serialized_end=2498
  _globals['_BULKWRITEFORMIGRATIONRESULT']._serialized_start=2500
  _globals['_BULKWRITEFORMIGRATIONRESULT']._serialized_end=2596
  _globals['_READARG']._serialized_start=2599
  _globals['_READARG']._serialized_end=3223
  _globals['_READARG_PARAMS']._serialized_start=2924
  _globals['_READARG_PARAMS']._serialized_end=3223
  _globals['_READRESULT']._serialized_start=3225
  _globals['_READRESULT']._serialized_end=3282
  _globals['_RANGESCANARG']._serialized_start=3285
  _globals['_RANGESCANARG']._serialized_end=4083
  _globals['_RANGESCANARG_PARAMS']._serialized_start=3793
  _globals['_RANGESCANARG_PARAMS']._serialized_end=4083
  _globals['_RANGESCANRESULT']._serialized_start=4086
  _globals['_RANGESCANRESULT']._serialized_end=4342
  _globals['_HISTORYREADARG']._serialized_start=4345
  _globals['_HISTORYREADARG']._serialized_end=4570
  _globals['_HISTORYREADARG_PARAMS']._serialized_start=2924
  _globals['_HISTORYREADARG_PARAMS']._serialized_end=2980
  _globals['_GETDEBUGINFOARG']._serialized_start=4573
  _globals['_GETDEBUGINFOARG']._serialized_end=4766
  _globals['_GETDEBUGINFORESULT']._serialized_start=4769
  _globals['_GETDEBUGINFORESULT']._serialized_end=5056
  _globals['_GETDEBUGINFORESULT_REPLICAINFO']._serialized_start=4973
  _globals['_GETDEBUGINFORESULT_REPLICAINFO']._serialized_end=5056
  _globals['_GETCONSTITUENTFORKEYSARG']._serialized_start=5058
  _globals['_GETCONSTITUENTFORKEYSARG']._serialized_end=5129
  _globals['_CONSTITUENTFORKEY']._serialized_start=5131
  _globals['_CONSTITUENTFORKEY']._serialized_end=5245
  _globals['_GETCONSTITUENTFORKEYSRESULT']._serialized_start=5247
  _globals['_GETCONSTITUENTFORKEYSRESULT']._serialized_end=5340
  _globals['_GETTABLEINFOINBUCKETARG']._serialized_start=5343
  _globals['_GETTABLEINFOINBUCKETARG']._serialized_end=5500
  _globals['_GETTABLEINFOINBUCKETRESULT']._serialized_start=5502
  _globals['_GETTABLEINFOINBUCKETRESULT']._serialized_end=5565
  _globals['_DELETETABLEARG']._serialized_start=5567
  _globals['_DELETETABLEARG']._serialized_end=5603
  _globals['_DELETETABLERESULT']._serialized_start=5605
  _globals['_DELETETABLERESULT']._serialized_end=5624
  _globals['_SHUFFLEBUCKETSFORTESTARG']._serialized_start=5627
  _globals['_SHUFFLEBUCKETSFORTESTARG']._serialized_end=5879
  _globals['_SHUFFLEBUCKETSFORTESTARG_SHUFFLETYPE']._serialized_start=5745
  _globals['_SHUFFLEBUCKETSFORTESTARG_SHUFFLETYPE']._serialized_end=5879
  _globals['_SHUFFLEBUCKETSFORTESTRESULT']._serialized_start=5881
  _globals['_SHUFFLEBUCKETSFORTESTRESULT']._serialized_end=5910
  _globals['_GETCLUSTERCAPACITYARG']._serialized_start=5913
  _globals['_GETCLUSTERCAPACITYARG']._serialized_end=6162
  _globals['_GETCLUSTERCAPACITYRESULT']._serialized_start=6164
  _globals['_GETCLUSTERCAPACITYRESULT']._serialized_end=6222
  _globals['_GETBUCKETLEADERARG']._serialized_start=6224
  _globals['_GETBUCKETLEADERARG']._serialized_end=6260
  _globals['_GETBUCKETLEADERRESULT']._serialized_start=6263
  _globals['_GETBUCKETLEADERRESULT']._serialized_end=6460
  _globals['_GETSHUFFLEPROGRESSARG']._serialized_start=6462
  _globals['_GETSHUFFLEPROGRESSARG']._serialized_end=6527
  _globals['_GETSHUFFLEPROGRESSRESULT']._serialized_start=6530
  _globals['_GETSHUFFLEPROGRESSRESULT']._serialized_end=6992
  _globals['_GETSHUFFLEPROGRESSRESULT_DISKSHUFFLESTAT']._serialized_start=6717
  _globals['_GETSHUFFLEPROGRESSRESULT_DISKSHUFFLESTAT']._serialized_end=6992
  _globals['_GETSHUFFLEPROGRESSRESULT_DISKSHUFFLESTAT_ERROR']._serialized_start=6956
  _globals['_GETSHUFFLEPROGRESSRESULT_DISKSHUFFLESTAT_ERROR']._serialized_end=6992
  _globals['_DELETERANGEARG']._serialized_start=6995
  _globals['_DELETERANGEARG']._serialized_end=7357
  _globals['_DELETERANGERESULT']._serialized_start=7359
  _globals['_DELETERANGERESULT']._serialized_end=7441
  _globals['_RPCSERVICE']._serialized_start=7444
  _globals['_RPCSERVICE']._serialized_end=8633
  _globals['_MASTERRPCSERVICE']._serialized_start=8636
  _globals['_MASTERRPCSERVICE']._serialized_end=9306
# @@protoc_insertion_point(module_scope)
