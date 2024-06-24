# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/file/file.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.view_keeper import view_metadata_pb2 as bridge_dot_view__keeper_dot_view__metadata__pb2
from bridge.s3_portal.base import s3_metadata_pb2 as bridge_dot_s3__portal_dot_base_dot_s3__metadata__pb2
from bridge.snap_fs import entity_handle_pb2 as bridge_dot_snap__fs_dot_entity__handle__pb2
from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import sub_task_pb2 as magneto_dot_base_dot_sub__task__pb2
from util.base import universal_id_pb2 as util_dot_base_dot_universal__id__pb2
from magneto.directory_walker import directory_walker_pb2 as magneto_dot_directory__walker_dot_directory__walker__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"magneto/connectors/file/file.proto\x12\x15\x63ohesity.magneto.file\x1a&bridge/view_keeper/view_metadata.proto\x1a\'bridge/s3_portal/base/s3_metadata.proto\x1a\"bridge/snap_fs/entity_handle.proto\x1a\x1fmagneto/agents/base/agent.proto\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/enums.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1bmagneto/base/sub_task.proto\x1a\x1cutil/base/universal_id.proto\x1a/magneto/directory_walker/directory_walker.proto\"\x87*\n\x0cSnapshotInfo\x12\x17\n\x0fjob_instance_id\x18\x01 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x02 \x01(\x05\x12\x11\n\ttask_name\x18\x03 \x01(\t\x12\x0f\n\x07task_id\x18, \x01(\x03\x12\x32\n&uses_parallel_diff_streamer_deprecated\x18. \x01(\x08\x42\x02\x18\x01\x12\"\n\x14uses_source_snapshot\x18\x18 \x01(\x08:\x04true\x12I\n\x14server_snapshot_info\x18* \x01(\x0b\x32+.cohesity.magneto.agents.ServerSnapshotInfo\x12\x1d\n\x0fuses_remote_nas\x18\x1c \x01(\x08:\x04true\x12\x19\n\x11\x63ontinue_on_error\x18# \x01(\x08\x12$\n\x1cuses_smb_proxy_for_file_data\x18$ \x01(\x08\x12\x18\n\x10\x63\x61se_insensitive\x18% \x01(\x08\x12R\n\x0etraversal_type\x18\x39 \x01(\x0e\x32/.cohesity.storage.dir_walker.TraversalType.Type:\tkPreOrder\x12^\n\x12sibling_order_type\x18: \x01(\x0e\x32\x32.cohesity.storage.dir_walker.SiblingOrderType.Type:\x0ekLexicographic\x12#\n\x1b\x64ir_walker_case_insensitive\x18\x63 \x01(\x08\x12O\n\x15prev_dir_walker_stats\x18S \x01(\x0b\x32\x30.cohesity.storage.dir_walker.DirWalkerStatsProto\x12O\n\x15\x63urr_dir_walker_stats\x18T \x01(\x0b\x32\x30.cohesity.storage.dir_walker.DirWalkerStatsProto\x12 \n\x18\x66orce_usec_ts_resolution\x18& \x01(\x08\x12;\n\x0f\x62\x61\x63kup_type_vec\x18\x19 \x03(\x0e\x32\".cohesity.magneto.NasProtocol.Type\x12@\n\x14\x62\x61\x63kup_data_protocol\x18Q \x01(\x0e\x32\".cohesity.magneto.NasProtocol.Type\x12V\n\x13remote_nas_info_map\x18\x31 \x03(\x0b\x32\x39.cohesity.magneto.file.SnapshotInfo.RemoteNasInfoMapEntry\x12\x14\n\x0clogical_size\x18\n \x01(\x03\x12\x16\n\x0emountpoint_dir\x18\x0b \x01(\t\x12\x1a\n\x12\x63ifs_relative_path\x18\x1a \x01(\t\x12\x19\n\x11nfs_relative_path\x18W \x01(\t\x12%\n\x1dpossible_orphans_rocksdb_name\x18> \x01(\t\x12#\n\x1brename_checkpoint_file_name\x18? \x01(\t\x12\x1e\n\x16kubernetes_volume_path\x18Z \x01(\t\x12\x11\n\troot_dirs\x18\x1f \x03(\t\x12\x1c\n\x14\x63heckpoint_file_name\x18\x06 \x01(\t\x12$\n\x1cskipped_checkpoint_file_name\x18\x36 \x01(\t\x12-\n%can_use_error_aware_checkpoint_keeper\x18\x37 \x01(\x08\x12\'\n\x1fuses_custom_rocks_db_comparator\x18\x38 \x01(\x08\x12:\n\x06status\x18\x07 \x01(\x0e\x32*.cohesity.magneto.file.SnapshotInfo.Status\x12\x33\n\x0csub_task_vec\x18\x08 \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12 \n\x18max_concurrent_sub_tasks\x18\r \x01(\x04\x12 \n\x18max_work_unit_bytes_size\x18\x0e \x01(\x03\x12+\n\x05\x65rror\x18\x0f \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x44\n\terror_map\x18\x1d \x03(\x0b\x32\x31.cohesity.magneto.file.SnapshotInfo.ErrorMapEntry\x12\x19\n\x11total_error_count\x18\x1e \x01(\x05\x12!\n\x19\x64iff_streamer_error_count\x18; \x01(\x05\x12\x1d\n\x15sub_task_errors_count\x18< \x01(\x05\x12+\n#non_ignorable_sub_task_errors_count\x18[ \x01(\x05\x12\'\n\x1f\x61\x64\x64itional_entities_to_skip_vec\x18\x1b \x03(\t\x12>\n\x18unmount_remote_nas_error\x18\x10 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x45\n\x1funmount_previous_snapshot_error\x18\x11 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12@\n\x1a\x64isconnect_nodes_error_vec\x18\x13 \x03(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12?\n\x19\x64\x65lete_src_snapshot_error\x18\x14 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x37\n\x11\x64\x65lete_view_error\x18\x15 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x39\n\x13\x64iff_streamer_error\x18\x16 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x41\n\x1b\x64iff_streamer_cleanup_error\x18\x17 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x42\n\x1cnotify_backup_complete_error\x18R \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12$\n\x15use_hardlink_sub_task\x18\" \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x16num_tmp_dirs_per_level\x18\' \x01(\x05\x12(\n is_sub_task_scribe_state_generic\x18( \x01(\x08\x12P\n\x12snap_change_status\x18) \x01(\x0b\x32\x34.cohesity.magneto.file.SnapshotInfo.SnapChangeStatus\x12#\n\x14is_snapshot_retained\x18+ \x01(\x08:\x05\x66\x61lse\x12\x19\n\x11total_split_count\x18/ \x01(\r\x12(\n\x19is_direct_archive_enabled\x18\x33 \x01(\x08:\x05\x66\x61lse\x12\x33\n\x0f\x61rchive_job_uid\x18\x34 \x01(\x0b\x32\x1a.cohesity.UniversalIdProto\x12q\n!directory_name_security_style_map\x18\x35 \x03(\x0b\x32\x46.cohesity.magneto.file.SnapshotInfo.DirectoryNameSecurityStyleMapEntry\x12 \n\x18min_mega_file_size_bytes\x18@ \x01(\x03\x12\x1b\n\x13sub_file_size_bytes\x18\x41 \x01(\x03\x12\x30\n(incomplete_hardlink_group_info_file_name\x18\x42 \x01(\t\x12#\n\x1blazy_smb_acls_fetch_enabled\x18\x43 \x01(\x08\x12\'\n\x1fmagneto_enable_mega_file_backup\x18\x44 \x01(\x08\x12(\n\x19symlink_follow_nas_target\x18\x45 \x01(\x08:\x05\x66\x61lse\x12`\n\x18\x66\x61iled_megafile_path_map\x18\x46 \x03(\x0b\x32>.cohesity.magneto.file.SnapshotInfo.FailedMegafilePathMapEntry\x12\x1a\n\x12\x66orce_snap_fs_walk\x18G \x01(\x08\x12T\n\nfld_config\x18H \x01(\x0b\x32@.cohesity.bridge.view.ViewIdMappingProto.FileLevelDataLockConfig\x12\x1f\n\x17snap_change_num_entries\x18I \x01(\x03\x12\x37\n/uses_custom_rocks_db_comparator_for_snap_change\x18J \x01(\x08\x12\x33\n+use_non_batching_complete_checkpoint_keeper\x18K \x01(\x08\x12H\n\x17uptier_job_restore_info\x18L \x01(\x0b\x32\'.cohesity.magneto.file.RestoreFilesInfo\x12Z\n\x1esource_initiated_backup_status\x18M \x01(\x0b\x32\x32.cohesity.magneto.file.SourceInitiatedBackupStatus\x12)\n\x1ais_source_initiated_backup\x18N \x01(\x08:\x05\x66\x61lse\x12:\n\ts3_config\x18O \x01(\x0b\x32\'.cohesity.bridge.s3.S3BucketConfigProto\x12\x1f\n\x17\x61ggregated_tiered_bytes\x18P \x01(\x03\x12%\n\x1dsnap_change_info_rocksdb_name\x18U \x01(\t\x12(\n snap_change_info_cache_file_name\x18V \x01(\t\x12#\n\x1bsnap_master_path_table_name\x18\\ \x01(\t\x12$\n\x1csnap_master_inode_table_name\x18] \x01(\t\x12\x16\n\x0elive_view_name\x18_ \x01(\t\x12\x19\n\rremote_server\x18\x04 \x01(\tB\x02\x18\x01\x12\x1b\n\x0fremote_nas_path\x18\x05 \x01(\tB\x02\x18\x01\x12\x1d\n\x11remote_mount_path\x18\x30 \x01(\tB\x02\x18\x01\x12k\n\x1ehardlink_inodes_to_cleanup_map\x18\x32 \x03(\x0b\x32\x43.cohesity.magneto.file.SnapshotInfo.HardlinkInodesToCleanupMapEntry\x12\"\n\x13\x66ull_directory_walk\x18X \x01(\x08:\x05\x66\x61lse\x12>\n\x0findexing_policy\x18^ \x01(\x0b\x32%.cohesity.magneto.IndexingPolicyProto\x1a]\n\x15RemoteNasInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.cohesity.magneto.file.RemoteNasInfo:\x02\x38\x01\x1aM\n\rErrorMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto:\x02\x38\x01\x1a\xea\x02\n\x10SnapChangeStatus\x12S\n\x05state\x18\x01 \x01(\x0e\x32\x44.cohesity.magneto.file.SnapshotInfo.SnapChangeStatus.SnapChangeState\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12#\n\x1bprevious_errors_finish_line\x18\x03 \x01(\t\x12!\n\x19use_compressed_cache_file\x18\x04 \x01(\x08\"\x8b\x01\n\x0fSnapChangeState\x12\x0c\n\x08kStarted\x10\x00\x12\x17\n\x13kPreviousErrorsDone\x10\x01\x12\x15\n\x11kIngestionStarted\x10\x02\x12\x12\n\x0ekIngestionDone\x10\x03\x12\x10\n\x0ckPassTwoDone\x10\x04\x12\x14\n\x10kMoveSubTaskDone\x10\x05\x1a\x44\n\"DirectoryNameSecurityStyleMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1a\x46\x61iledMegafilePathMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x41\n\x1fHardlinkInodesToCleanupMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\x93\x02\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x11\n\rkViewPrepared\x10\x01\x12\x15\n\x11kSourceConfigured\x10\x0b\x12\x17\n\x13kSrcSnapshotCreated\x10\x02\x12\x13\n\x0fkNodesConnected\x10\x03\x12\x15\n\x11kSubTasksFinished\x10\x04\x12\x16\n\x12kBridgeBackupEnded\x10\x05\x12\x16\n\x12kNodesDisconnected\x10\x06\x12\x17\n\x13kSrcSnapshotDeleted\x10\x07\x12\x13\n\x0fkBackupFinished\x10\x08\x12\x13\n\x0fkLiveViewCloned\x10\t\x12\x19\n\x15kNotifyBackupComplete\x10\n*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x32\x64\n\x12\x66ile_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18i \x01(\x0b\x32#.cohesity.magneto.file.SnapshotInfoJ\x04\x08\t\x10\nJ\x04\x08\x0c\x10\rJ\x04\x08\x12\x10\x13J\x04\x08 \x10!J\x04\x08!\x10\"J\x04\x08=\x10>\"\x83\x03\n\x1bSourceInitiatedBackupStatus\x12\x64\n\x14\x64\x61ta_movement_status\x18\x01 \x01(\x0e\x32\x39.cohesity.magneto.file.SourceInitiatedBackupStatus.Status:\x0bkNotStarted\x12\x39\n\x13\x64\x61ta_movement_error\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12l\n\x1csnap_change_ingestion_status\x18\x03 \x01(\x0e\x32\x39.cohesity.magneto.file.SourceInitiatedBackupStatus.Status:\x0bkNotStarted\"U\n\x06Status\x12\x0f\n\x0bkNotStarted\x10\x00\x12\x0f\n\x0bkInProgress\x10\x01\x12\r\n\tkFinished\x10\x02\x12\x0c\n\x08kAborted\x10\x03\x12\x0c\n\x08kErrored\x10\x04\"C\n\rRemoteNasInfo\x12\x19\n\x11remote_server_vec\x18\x01 \x03(\t\x12\x17\n\x0fremote_nas_path\x18\x02 \x01(\t\"\xa3\x01\n\x1bIncompleteHardlinkGroupInfo\x12S\n\tinode_map\x18\x01 \x03(\x0b\x32@.cohesity.magneto.file.IncompleteHardlinkGroupInfo.InodeMapEntry\x1a/\n\rInodeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\x91\x01\n\x0b\x45ntityRange\x12\x41\n\x0cstart_entity\x18\x01 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12?\n\nend_entity\x18\x02 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\"\xa3\x01\n\x11UptierEntityRange\x12G\n\x13start_entity_handle\x18\x01 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\x12\x45\n\x11\x65nd_entity_handle\x18\x02 \x01(\x0b\x32*.cohesity.bridge.snap_fs.EntityHandleProto\"\xe1\x01\n\rEntitiesStats\x12\x16\n\x0etotal_entities\x18\x01 \x01(\x03\x12 \n\x18total_logical_size_bytes\x18\x02 \x01(\x03\x12\x1e\n\x16total_changed_entities\x18\x03 \x01(\x03\x12\x1e\n\x16total_skipped_entities\x18\x04 \x01(\x03\x12\x1b\n\x13total_bytes_to_read\x18\x05 \x01(\x03\x12\x18\n\x10total_bytes_read\x18\x06 \x01(\x03\x12\x1f\n\x17total_changed_hardlinks\x18\x07 \x01(\x03\"\x9d\t\n\x0f\x46ileSubTaskInfo\x12\x31\n\x05range\x18\n \x01(\x0b\x32\".cohesity.magneto.file.EntityRange\x12>\n\x0cuptier_range\x18% \x01(\x0b\x32(.cohesity.magneto.file.UptierEntityRange\x12Y\n\x13remote_nas_info_map\x18\x1d \x03(\x0b\x32<.cohesity.magneto.file.FileSubTaskInfo.RemoteNasInfoMapEntry\x12>\n\x18\x64\x65lete_scribe_info_error\x18\x08 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x19\n\x11total_error_count\x18\x0b \x01(\x05\x12\x18\n\x10is_move_sub_task\x18\x10 \x01(\x08\x12\x1c\n\x14is_hardlink_sub_task\x18\x0c \x01(\x08\x12\x1c\n\x14is_finished_sub_task\x18\x0e \x01(\x08\x12\x1a\n\x12\x65ntities_processed\x18\r \x01(\x05\x12\x14\n\x0c\x62ytes_tiered\x18  \x01(\x03\x12\x1c\n\x14is_set_attr_sub_task\x18\x0f \x01(\x08\x12$\n\x1cis_migrated_orphans_sub_task\x18\x1e \x01(\x08\x12#\n\x17num_of_parallel_threads\x18\x11 \x01(\x05:\x02-1\x12 \n\x18max_allowed_active_packs\x18\x12 \x01(\r\x12S\n\rsub_task_type\x18\" \x01(\x0e\x32\x32.cohesity.magneto.file.FileSubTaskInfo.SubTaskType:\x08kRegular\x12\x1e\n\x16write_sub_task_idx_vec\x18# \x03(\x03\x12!\n\x19\x66inalize_sub_task_idx_vec\x18$ \x03(\x03\x12\x19\n\rremote_server\x18\x04 \x01(\tB\x02\x18\x01\x12\x15\n\rskip_finalize\x18\x13 \x01(\x08\x12&\n\x1e\x66leet_storage_proxy_ip_address\x18\x1f \x01(\t\x12\'\n\x1ftotal_non_ignorable_error_count\x18! \x01(\x05\x1a]\n\x15RemoteNasInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.cohesity.magneto.file.RemoteNasInfo:\x02\x38\x01\"C\n\x0bSubTaskType\x12\x0c\n\x08kRegular\x10\x00\x12\x0b\n\x07kCreate\x10\x01\x12\n\n\x06kWrite\x10\x02\x12\r\n\tkFinalize\x10\x03*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x32\x61\n\x12\x66ile_sub_task_info\x12\x1d.cohesity.magneto.SubTaskInfo\x18\x65 \x01(\x0b\x32&.cohesity.magneto.file.FileSubTaskInfoJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\t\x10\n\"\x80\x0c\n\x15\x46ileSubTaskScribeInfo\x12\x1b\n\x0f\x66inish_line_idx\x18\x01 \x01(\x05:\x02-1\x12R\n\x0chole_idx_map\x18\x02 \x03(\x0b\x32<.cohesity.magneto.file.FileSubTaskScribeInfo.HoleIdxMapEntry\x12^\n\x15\x66inish_line_work_unit\x18\x03 \x01(\x0b\x32?.cohesity.magneto.file.FileSubTaskScribeInfo.FinishLineWorkUnit\x12T\n\rhole_info_map\x18\x04 \x03(\x0b\x32=.cohesity.magneto.file.FileSubTaskScribeInfo.HoleInfoMapEntry\x12\x19\n\x11\x62ytes_transferred\x18\x05 \x01(\x03\x12\x12\n\nbytes_read\x18\x06 \x01(\x03\x12\x1a\n\x12\x65ntities_processed\x18\n \x01(\x05\x12\x14\n\x0c\x62ytes_tiered\x18\x0c \x01(\x03\x12\x1a\n\x12num_attributes_set\x18\x08 \x01(\x03\x12M\n\terror_map\x18\x07 \x03(\x0b\x32:.cohesity.magneto.file.FileSubTaskScribeInfo.ErrorMapEntry\x12\x19\n\x11total_error_count\x18\t \x01(\x05\x12^\n\x12\x63leanup_entity_map\x18\x0b \x03(\x0b\x32\x42.cohesity.magneto.file.FileSubTaskScribeInfo.CleanupEntityMapEntry\x12\'\n\x1ftotal_non_ignorable_error_count\x18\x0e \x01(\x05\x1a\x31\n\x0fHoleIdxMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x86\x01\n\x12\x46inishLineWorkUnit\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x44\n\x04type\x18\x04 \x01(\x0e\x32\x36.cohesity.storage.dir_walker.EntityMetadata.EntityType\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04size\x18\x03 \x01(\x03\x1a\xfd\x01\n\x08HoleInfo\x12=\n\x08metadata\x18\x01 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12\x61\n\x0foffset_size_map\x18\x02 \x03(\x0b\x32H.cohesity.magneto.file.FileSubTaskScribeInfo.HoleInfo.OffsetSizeMapEntry\x12\x19\n\nholes_done\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a\x34\n\x12OffsetSizeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1ai\n\x10HoleInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x44\n\x05value\x18\x02 \x01(\x0b\x32\x35.cohesity.magneto.file.FileSubTaskScribeInfo.HoleInfo:\x02\x38\x01\x1aM\n\rErrorMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto:\x02\x38\x01\x1a\x64\n\x15\x43leanupEntityMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata:\x02\x38\x01\x32t\n\x19\x66ile_sub_task_scribe_info\x12#.cohesity.magneto.SubTaskScribeInfo\x18\x65 \x01(\x0b\x32,.cohesity.magneto.file.FileSubTaskScribeInfo\"\xa4\x02\n\x0bRestoreInfo\x12\x39\n\x06status\x18\x01 \x01(\x0e\x32).cohesity.magneto.file.RestoreInfo.Status\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"J\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x18\n\x14kCloneVolumeFinished\x10\x01\x12\x18\n\x14kMountVolumeFinished\x10\x02\x32\x61\n\x11\x66ile_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18h \x01(\x0b\x32\".cohesity.magneto.file.RestoreInfo\"\xf7\x06\n\x15RestoreFileCheckpoint\x12I\n\x0c\x65ntities_vec\x18\x01 \x03(\x0b\x32\x33.cohesity.magneto.file.RestoreFileCheckpoint.Entity\x12\x45\n\x10last_diff_entity\x18\x02 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12H\n\x13last_ignored_entity\x18\x03 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12P\n\x13parent_entities_vec\x18\x04 \x03(\x0b\x32\x33.cohesity.magneto.file.RestoreFileCheckpoint.Entity\x12V\n\x19restore_attr_entities_vec\x18\x05 \x03(\x0b\x32\x33.cohesity.magneto.file.RestoreFileCheckpoint.Entity\x12 \n\x14restore_dirs_vec_idx\x18\x06 \x01(\x03:\x02-1\x12!\n\x15restore_files_vec_idx\x18\x07 \x01(\x03:\x02-1\x12&\n\x1eroot_entity_start_sub_task_idx\x18\x08 \x01(\x03\x1a\xea\x02\n\x06\x45ntity\x12\x41\n\x0csrc_metadata\x18\x01 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12\x41\n\x0c\x64st_metadata\x18\x02 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12\x13\n\x0b\x66ile_handle\x18\x03 \x01(\x0c\x12\x0e\n\x06offset\x18\x04 \x01(\x03\x12\x0b\n\x03\x65of\x18\x05 \x01(\x08\x12\x15\n\rshould_commit\x18\x06 \x01(\x08\x12J\n\x06status\x18\x07 \x01(\x0e\x32:.cohesity.magneto.file.RestoreFileCheckpoint.Entity.Status\"E\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x0c\n\x08kCreated\x10\x01\x12\x0f\n\x0bkDataSynced\x10\x02\x12\x0e\n\nkFinalized\x10\x03\"\xcd\x13\n\x10RestoreFilesInfo\x12>\n\x06status\x18\x01 \x01(\x0e\x32..cohesity.magneto.file.RestoreFilesInfo.Status\x12\x10\n\x08\x64irs_vec\x18\x04 \x03(\t\x12\x11\n\tfiles_vec\x18\x05 \x03(\t\x12@\n\ncheckpoint\x18\x06 \x01(\x0b\x32,.cohesity.magneto.file.RestoreFileCheckpoint\x12H\n\terror_map\x18\x07 \x03(\x0b\x32\x35.cohesity.magneto.file.RestoreFilesInfo.ErrorMapEntry\x12\x19\n\x11total_error_count\x18\x08 \x01(\x05\x12\x34\n\rsub_tasks_vec\x18\t \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12 \n\x18max_concurrent_sub_tasks\x18\x12 \x01(\x04\x12+\n\x05\x65rror\x18\n \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x19\n\x11\x62\x61se_dirs_created\x18\x0b \x01(\x08\x12\x32\n\x0bhost_entity\x18\x0c \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x1d\n\x0fuses_remote_nas\x18\x14 \x01(\x08:\x04true\x12)\n\x1bis_file_based_backup_source\x18\x1d \x01(\x08:\x04true\x12\x38\n\x0crestore_type\x18\x15 \x01(\x0e\x32\".cohesity.magneto.NasProtocol.Type\x12\x17\n\x0froot_dir_prefix\x18\r \x01(\t\x12>\n\x18unmount_remote_nas_error\x18\x0e \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12 \n\x14restore_dirs_vec_idx\x18\x0f \x01(\x03:\x02-1\x12!\n\x15restore_files_vec_idx\x18\x10 \x01(\x03:\x02-1\x12&\n\x1eroot_entity_start_sub_task_idx\x18\x11 \x01(\x03\x12 \n\x18max_work_unit_bytes_size\x18\x13 \x01(\x03\x12\x1d\n\x15set_attr_pass_started\x18\x16 \x01(\x08\x12\x33\n\'root_entity_first_set_attr_sub_task_idx\x18\x17 \x01(\x03:\x02-1\x12>\n\x18\x64\x65lete_scribe_info_error\x18\x18 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x42\n\x11target_agent_info\x18\x19 \x01(\x0b\x32\'.cohesity.magneto.agents.AgentInfoProto\x12\x1c\n\x14target_agent_ip_addr\x18\x1a \x01(\t\x12\x16\n\x0enas_mountpoint\x18\x1b \x01(\t\x12[\n\x13\x64isk_mountpoint_map\x18\x1c \x03(\x0b\x32>.cohesity.magneto.file.RestoreFilesInfo.DiskMountpointMapEntry\x12*\n\x1bis_local_storage_proxy_used\x18# \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0bis_view_flr\x18% \x01(\x08:\x05\x66\x61lse\x12Z\n\x13remote_nas_info_map\x18\x1e \x03(\x0b\x32=.cohesity.magneto.file.RestoreFilesInfo.RemoteNasInfoMapEntry\x12(\n magneto_enable_mega_file_restore\x18  \x01(\x08\x12(\n restore_min_mega_file_size_bytes\x18$ \x01(\x03\x12h\n\x1a\x66\x61iled_megafile_entity_map\x18! \x03(\x0b\x32\x44.cohesity.magneto.file.RestoreFilesInfo.FailedMegafileEntityMapEntry\x12K\n\rvmware_params\x18\" \x01(\x0b\x32\x34.cohesity.magneto.file.RestoreFilesInfo.VMwareParams\x12&\n\x1euse_entity_id_for_uptier_range\x18& \x01(\x08\x12\x19\n\rremote_server\x18\x02 \x01(\tB\x02\x18\x01\x12\x1b\n\x0fremote_nas_path\x18\x03 \x01(\tB\x02\x18\x01\x1aM\n\rErrorMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto:\x02\x38\x01\x1a\x38\n\x16\x44iskMountpointMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a]\n\x15RemoteNasInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.cohesity.magneto.file.RemoteNasInfo:\x02\x38\x01\x1a>\n\x1c\x46\x61iledMegafileEntityMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a!\n\x0cVMwareParams\x12\x11\n\thost_name\x18\x01 \x01(\t\"\xa9\x02\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x16\n\x12kPreProcessingDone\x10\t\x12\x0f\n\x0bkViewCloned\x10\x01\x12\x13\n\x0fkNodesConnected\x10\x02\x12\x0f\n\x0bkNasMounted\x10\x03\x12\x1c\n\x18kLocalVirtualDiskMounted\x10\n\x12\x15\n\x11kSubTasksFinished\x10\x04\x12\x17\n\x13kBridgeRestoreEnded\x10\x08\x12\x11\n\rkNasUnmounted\x10\x05\x12\x1e\n\x1akLocalVirtualDiskUnmounted\x10\x0b\x12\x16\n\x12kNodesDisconnected\x10\x06\x12\x10\n\x0ckViewDeleted\x10\x07\x12\x17\n\x13kPostProcessingDone\x10\x0c*\x08\x08\x64\x10\x80\x80\x80\x80\x02\x32l\n\x12restore_files_info\x12\'.cohesity.magneto.RestoreFilesInfoProto\x18\x66 \x01(\x0b\x32\'.cohesity.magneto.file.RestoreFilesInfoJ\x04\x08\x1f\x10 \"y\n\rDirectoryInfo\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\x96\x03\n\x11RestoreScribeInfo\x12U\n\x0f\x66inish_line_row\x18\x01 \x01(\x0b\x32<.cohesity.magneto.file.RestoreScribeInfo.FinishLineScribeRow\x12X\n\x11setattr_holes_map\x18\x02 \x03(\x0b\x32=.cohesity.magneto.file.RestoreScribeInfo.SetattrHolesMapEntry\x1a\"\n\x13\x46inishLineScribeRow\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x1a\x36\n\x14SetattrHolesMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x32t\n\x18\x66ile_restore_scribe_info\x12(.cohesity.magneto.RestoreScribeInfoProto\x18\x64 \x01(\x0b\x32(.cohesity.magneto.file.RestoreScribeInfo\"\xbf\x01\n\x12SnapshotScribeInfo\x12\x30\n\nerror_list\x18\x02 \x03(\x0b\x32\x1c.cohesity.magneto.ErrorProto2w\n\x19\x66ile_snapshot_scribe_info\x12).cohesity.magneto.SnapshotScribeInfoProto\x18h \x01(\x0b\x32).cohesity.magneto.file.SnapshotScribeInfo\"\xa3\x02\n\x10\x43hangeEntryProto\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x42\n\rprev_metadata\x18\x02 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12\x42\n\rcurr_metadata\x18\x03 \x01(\x0b\x32+.cohesity.storage.dir_walker.EntityMetadata\x12\x18\n\x10is_prev_move_src\x18\x04 \x01(\x08\x12\x18\n\x10is_curr_move_dst\x18\x05 \x01(\x08\x12\x16\n\x0eis_error_entry\x18\x07 \x01(\x08\x12\x1d\n\x0eis_del_bit_set\x18\x08 \x01(\x08:\x05\x66\x61lse*\x08\x08\x64\x10\x80\x80\x80\x80\x02J\x04\x08\x06\x10\x07\"\xf2\x06\n\x18SnapChangeInfoCacheProto\x12\x65\n\x14\x63hanged_hardlink_map\x18\x01 \x03(\x0b\x32G.cohesity.magneto.file.SnapChangeInfoCacheProto.ChangedHardlinkMapEntry\x12\x61\n\x12hardlink_group_map\x18\x02 \x03(\x0b\x32\x45.cohesity.magneto.file.SnapChangeInfoCacheProto.HardlinkGroupMapEntry\x12T\n\x12move_operation_vec\x18\x03 \x03(\x0b\x32\x38.cohesity.magneto.file.SnapChangeInfoCacheProto.MoveInfo\x12\x1c\n\x14pass_two_finish_line\x18\x04 \x01(\t\x12\x1a\n\x12num_change_entries\x18\x05 \x01(\x03\x12+\n#curr_num_snap_change_entries_phase1\x18\x06 \x01(\x03\x12%\n\x1dtotal_num_snap_change_entries\x18\x07 \x01(\x03\x1a\x39\n\x17\x43hangedHardlinkMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1aq\n\x11HardlinkGroupInfo\x12\x15\n\rexisting_path\x18\x01 \x01(\t\x12\x15\n\rnum_new_links\x18\x02 \x01(\r\x12\x15\n\rnum_all_links\x18\x03 \x01(\r\x12\x17\n\x0f\x66irst_path_seen\x18\x04 \x01(\t\x1az\n\x15HardlinkGroupMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12P\n\x05value\x18\x02 \x01(\x0b\x32\x41.cohesity.magneto.file.SnapChangeInfoCacheProto.HardlinkGroupInfo:\x02\x38\x01\x1at\n\x08MoveInfo\x12\x10\n\x08src_path\x18\x01 \x01(\t\x12\x10\n\x08\x64st_path\x18\x02 \x01(\t\x12\x44\n\x04type\x18\x03 \x01(\x0e\x32\x36.cohesity.storage.dir_walker.EntityMetadata.EntityType*\x08\x08\x64\x10\x80\x80\x80\x80\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.file.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SNAPSHOTINFO_REMOTENASINFOMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_REMOTENASINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO_ERRORMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_ERRORMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO_DIRECTORYNAMESECURITYSTYLEMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_DIRECTORYNAMESECURITYSTYLEMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO_FAILEDMEGAFILEPATHMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_FAILEDMEGAFILEPATHMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO_HARDLINKINODESTOCLEANUPMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_HARDLINKINODESTOCLEANUPMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO'].fields_by_name['uses_parallel_diff_streamer_deprecated']._loaded_options = None
  _globals['_SNAPSHOTINFO'].fields_by_name['uses_parallel_diff_streamer_deprecated']._serialized_options = b'\030\001'
  _globals['_SNAPSHOTINFO'].fields_by_name['remote_server']._loaded_options = None
  _globals['_SNAPSHOTINFO'].fields_by_name['remote_server']._serialized_options = b'\030\001'
  _globals['_SNAPSHOTINFO'].fields_by_name['remote_nas_path']._loaded_options = None
  _globals['_SNAPSHOTINFO'].fields_by_name['remote_nas_path']._serialized_options = b'\030\001'
  _globals['_SNAPSHOTINFO'].fields_by_name['remote_mount_path']._loaded_options = None
  _globals['_SNAPSHOTINFO'].fields_by_name['remote_mount_path']._serialized_options = b'\030\001'
  _globals['_INCOMPLETEHARDLINKGROUPINFO_INODEMAPENTRY']._loaded_options = None
  _globals['_INCOMPLETEHARDLINKGROUPINFO_INODEMAPENTRY']._serialized_options = b'8\001'
  _globals['_FILESUBTASKINFO_REMOTENASINFOMAPENTRY']._loaded_options = None
  _globals['_FILESUBTASKINFO_REMOTENASINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_FILESUBTASKINFO'].fields_by_name['remote_server']._loaded_options = None
  _globals['_FILESUBTASKINFO'].fields_by_name['remote_server']._serialized_options = b'\030\001'
  _globals['_FILESUBTASKSCRIBEINFO_HOLEIDXMAPENTRY']._loaded_options = None
  _globals['_FILESUBTASKSCRIBEINFO_HOLEIDXMAPENTRY']._serialized_options = b'8\001'
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFO_OFFSETSIZEMAPENTRY']._loaded_options = None
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFO_OFFSETSIZEMAPENTRY']._serialized_options = b'8\001'
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFOMAPENTRY']._loaded_options = None
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_FILESUBTASKSCRIBEINFO_ERRORMAPENTRY']._loaded_options = None
  _globals['_FILESUBTASKSCRIBEINFO_ERRORMAPENTRY']._serialized_options = b'8\001'
  _globals['_FILESUBTASKSCRIBEINFO_CLEANUPENTITYMAPENTRY']._loaded_options = None
  _globals['_FILESUBTASKSCRIBEINFO_CLEANUPENTITYMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREFILESINFO_ERRORMAPENTRY']._loaded_options = None
  _globals['_RESTOREFILESINFO_ERRORMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREFILESINFO_DISKMOUNTPOINTMAPENTRY']._loaded_options = None
  _globals['_RESTOREFILESINFO_DISKMOUNTPOINTMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREFILESINFO_REMOTENASINFOMAPENTRY']._loaded_options = None
  _globals['_RESTOREFILESINFO_REMOTENASINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREFILESINFO_FAILEDMEGAFILEENTITYMAPENTRY']._loaded_options = None
  _globals['_RESTOREFILESINFO_FAILEDMEGAFILEENTITYMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREFILESINFO'].fields_by_name['remote_server']._loaded_options = None
  _globals['_RESTOREFILESINFO'].fields_by_name['remote_server']._serialized_options = b'\030\001'
  _globals['_RESTOREFILESINFO'].fields_by_name['remote_nas_path']._loaded_options = None
  _globals['_RESTOREFILESINFO'].fields_by_name['remote_nas_path']._serialized_options = b'\030\001'
  _globals['_RESTORESCRIBEINFO_SETATTRHOLESMAPENTRY']._loaded_options = None
  _globals['_RESTORESCRIBEINFO_SETATTRHOLESMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPCHANGEINFOCACHEPROTO_CHANGEDHARDLINKMAPENTRY']._loaded_options = None
  _globals['_SNAPCHANGEINFOCACHEPROTO_CHANGEDHARDLINKMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPCHANGEINFOCACHEPROTO_HARDLINKGROUPMAPENTRY']._loaded_options = None
  _globals['_SNAPCHANGEINFOCACHEPROTO_HARDLINKGROUPMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO']._serialized_start=427
  _globals['_SNAPSHOTINFO']._serialized_end=5810
  _globals['_SNAPSHOTINFO_REMOTENASINFOMAPENTRY']._serialized_start=4648
  _globals['_SNAPSHOTINFO_REMOTENASINFOMAPENTRY']._serialized_end=4741
  _globals['_SNAPSHOTINFO_ERRORMAPENTRY']._serialized_start=4743
  _globals['_SNAPSHOTINFO_ERRORMAPENTRY']._serialized_end=4820
  _globals['_SNAPSHOTINFO_SNAPCHANGESTATUS']._serialized_start=4823
  _globals['_SNAPSHOTINFO_SNAPCHANGESTATUS']._serialized_end=5185
  _globals['_SNAPSHOTINFO_SNAPCHANGESTATUS_SNAPCHANGESTATE']._serialized_start=5046
  _globals['_SNAPSHOTINFO_SNAPCHANGESTATUS_SNAPCHANGESTATE']._serialized_end=5185
  _globals['_SNAPSHOTINFO_DIRECTORYNAMESECURITYSTYLEMAPENTRY']._serialized_start=5187
  _globals['_SNAPSHOTINFO_DIRECTORYNAMESECURITYSTYLEMAPENTRY']._serialized_end=5255
  _globals['_SNAPSHOTINFO_FAILEDMEGAFILEPATHMAPENTRY']._serialized_start=5257
  _globals['_SNAPSHOTINFO_FAILEDMEGAFILEPATHMAPENTRY']._serialized_end=5317
  _globals['_SNAPSHOTINFO_HARDLINKINODESTOCLEANUPMAPENTRY']._serialized_start=5319
  _globals['_SNAPSHOTINFO_HARDLINKINODESTOCLEANUPMAPENTRY']._serialized_end=5384
  _globals['_SNAPSHOTINFO_STATUS']._serialized_start=5387
  _globals['_SNAPSHOTINFO_STATUS']._serialized_end=5662
  _globals['_SOURCEINITIATEDBACKUPSTATUS']._serialized_start=5813
  _globals['_SOURCEINITIATEDBACKUPSTATUS']._serialized_end=6200
  _globals['_SOURCEINITIATEDBACKUPSTATUS_STATUS']._serialized_start=6115
  _globals['_SOURCEINITIATEDBACKUPSTATUS_STATUS']._serialized_end=6200
  _globals['_REMOTENASINFO']._serialized_start=6202
  _globals['_REMOTENASINFO']._serialized_end=6269
  _globals['_INCOMPLETEHARDLINKGROUPINFO']._serialized_start=6272
  _globals['_INCOMPLETEHARDLINKGROUPINFO']._serialized_end=6435
  _globals['_INCOMPLETEHARDLINKGROUPINFO_INODEMAPENTRY']._serialized_start=6388
  _globals['_INCOMPLETEHARDLINKGROUPINFO_INODEMAPENTRY']._serialized_end=6435
  _globals['_ENTITYRANGE']._serialized_start=6438
  _globals['_ENTITYRANGE']._serialized_end=6583
  _globals['_UPTIERENTITYRANGE']._serialized_start=6586
  _globals['_UPTIERENTITYRANGE']._serialized_end=6749
  _globals['_ENTITIESSTATS']._serialized_start=6752
  _globals['_ENTITIESSTATS']._serialized_end=6977
  _globals['_FILESUBTASKINFO']._serialized_start=6980
  _globals['_FILESUBTASKINFO']._serialized_end=8161
  _globals['_FILESUBTASKINFO_REMOTENASINFOMAPENTRY']._serialized_start=4648
  _globals['_FILESUBTASKINFO_REMOTENASINFOMAPENTRY']._serialized_end=4741
  _globals['_FILESUBTASKINFO_SUBTASKTYPE']._serialized_start=7949
  _globals['_FILESUBTASKINFO_SUBTASKTYPE']._serialized_end=8016
  _globals['_FILESUBTASKSCRIBEINFO']._serialized_start=8164
  _globals['_FILESUBTASKSCRIBEINFO']._serialized_end=9700
  _globals['_FILESUBTASKSCRIBEINFO_HOLEIDXMAPENTRY']._serialized_start=8852
  _globals['_FILESUBTASKSCRIBEINFO_HOLEIDXMAPENTRY']._serialized_end=8901
  _globals['_FILESUBTASKSCRIBEINFO_FINISHLINEWORKUNIT']._serialized_start=8904
  _globals['_FILESUBTASKSCRIBEINFO_FINISHLINEWORKUNIT']._serialized_end=9038
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFO']._serialized_start=9041
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFO']._serialized_end=9294
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFO_OFFSETSIZEMAPENTRY']._serialized_start=9242
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFO_OFFSETSIZEMAPENTRY']._serialized_end=9294
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFOMAPENTRY']._serialized_start=9296
  _globals['_FILESUBTASKSCRIBEINFO_HOLEINFOMAPENTRY']._serialized_end=9401
  _globals['_FILESUBTASKSCRIBEINFO_ERRORMAPENTRY']._serialized_start=4743
  _globals['_FILESUBTASKSCRIBEINFO_ERRORMAPENTRY']._serialized_end=4820
  _globals['_FILESUBTASKSCRIBEINFO_CLEANUPENTITYMAPENTRY']._serialized_start=9482
  _globals['_FILESUBTASKSCRIBEINFO_CLEANUPENTITYMAPENTRY']._serialized_end=9582
  _globals['_RESTOREINFO']._serialized_start=9703
  _globals['_RESTOREINFO']._serialized_end=9995
  _globals['_RESTOREINFO_STATUS']._serialized_start=9822
  _globals['_RESTOREINFO_STATUS']._serialized_end=9896
  _globals['_RESTOREFILECHECKPOINT']._serialized_start=9998
  _globals['_RESTOREFILECHECKPOINT']._serialized_end=10885
  _globals['_RESTOREFILECHECKPOINT_ENTITY']._serialized_start=10523
  _globals['_RESTOREFILECHECKPOINT_ENTITY']._serialized_end=10885
  _globals['_RESTOREFILECHECKPOINT_ENTITY_STATUS']._serialized_start=10816
  _globals['_RESTOREFILECHECKPOINT_ENTITY_STATUS']._serialized_end=10885
  _globals['_RESTOREFILESINFO']._serialized_start=10888
  _globals['_RESTOREFILESINFO']._serialized_end=13397
  _globals['_RESTOREFILESINFO_ERRORMAPENTRY']._serialized_start=4743
  _globals['_RESTOREFILESINFO_ERRORMAPENTRY']._serialized_end=4820
  _globals['_RESTOREFILESINFO_DISKMOUNTPOINTMAPENTRY']._serialized_start=12721
  _globals['_RESTOREFILESINFO_DISKMOUNTPOINTMAPENTRY']._serialized_end=12777
  _globals['_RESTOREFILESINFO_REMOTENASINFOMAPENTRY']._serialized_start=4648
  _globals['_RESTOREFILESINFO_REMOTENASINFOMAPENTRY']._serialized_end=4741
  _globals['_RESTOREFILESINFO_FAILEDMEGAFILEENTITYMAPENTRY']._serialized_start=12874
  _globals['_RESTOREFILESINFO_FAILEDMEGAFILEENTITYMAPENTRY']._serialized_end=12936
  _globals['_RESTOREFILESINFO_VMWAREPARAMS']._serialized_start=12938
  _globals['_RESTOREFILESINFO_VMWAREPARAMS']._serialized_end=12971
  _globals['_RESTOREFILESINFO_STATUS']._serialized_start=12974
  _globals['_RESTOREFILESINFO_STATUS']._serialized_end=13271
  _globals['_DIRECTORYINFO']._serialized_start=13399
  _globals['_DIRECTORYINFO']._serialized_end=13520
  _globals['_RESTORESCRIBEINFO']._serialized_start=13523
  _globals['_RESTORESCRIBEINFO']._serialized_end=13929
  _globals['_RESTORESCRIBEINFO_FINISHLINESCRIBEROW']._serialized_start=13721
  _globals['_RESTORESCRIBEINFO_FINISHLINESCRIBEROW']._serialized_end=13755
  _globals['_RESTORESCRIBEINFO_SETATTRHOLESMAPENTRY']._serialized_start=13757
  _globals['_RESTORESCRIBEINFO_SETATTRHOLESMAPENTRY']._serialized_end=13811
  _globals['_SNAPSHOTSCRIBEINFO']._serialized_start=13932
  _globals['_SNAPSHOTSCRIBEINFO']._serialized_end=14123
  _globals['_CHANGEENTRYPROTO']._serialized_start=14126
  _globals['_CHANGEENTRYPROTO']._serialized_end=14417
  _globals['_SNAPCHANGEINFOCACHEPROTO']._serialized_start=14420
  _globals['_SNAPCHANGEINFOCACHEPROTO']._serialized_end=15302
  _globals['_SNAPCHANGEINFOCACHEPROTO_CHANGEDHARDLINKMAPENTRY']._serialized_start=14878
  _globals['_SNAPCHANGEINFOCACHEPROTO_CHANGEDHARDLINKMAPENTRY']._serialized_end=14935
  _globals['_SNAPCHANGEINFOCACHEPROTO_HARDLINKGROUPINFO']._serialized_start=14937
  _globals['_SNAPCHANGEINFOCACHEPROTO_HARDLINKGROUPINFO']._serialized_end=15050
  _globals['_SNAPCHANGEINFOCACHEPROTO_HARDLINKGROUPMAPENTRY']._serialized_start=15052
  _globals['_SNAPCHANGEINFOCACHEPROTO_HARDLINKGROUPMAPENTRY']._serialized_end=15174
  _globals['_SNAPCHANGEINFOCACHEPROTO_MOVEINFO']._serialized_start=15176
  _globals['_SNAPCHANGEINFOCACHEPROTO_MOVEINFO']._serialized_end=15292
# @@protoc_insertion_point(module_scope)
