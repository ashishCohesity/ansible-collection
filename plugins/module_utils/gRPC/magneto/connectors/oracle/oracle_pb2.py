# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/connectors/oracle/oracle.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.agents.base import oracle_sql_pb2 as magneto_dot_agents_dot_base_dot_oracle__sql__pb2
from magneto.api.common import oracle_pb2 as magneto_dot_api_dot_common_dot_oracle__pb2
from magneto.base.entities import oracle_pb2 as magneto_dot_base_dot_entities_dot_oracle__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import env_params_pb2 as magneto_dot_base_dot_env__params__pb2
from magneto.base import error_pb2 as magneto_dot_base_dot_error__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.base import sub_task_pb2 as magneto_dot_base_dot_sub__task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&magneto/connectors/oracle/oracle.proto\x12\x17\x63ohesity.magneto.oracle\x1a\x1fmagneto/agents/base/agent.proto\x1a$magneto/agents/base/oracle_sql.proto\x1a\x1fmagneto/api/common/oracle.proto\x1a\"magneto/base/entities/oracle.proto\x1a\x18magneto/base/enums.proto\x1a\x1dmagneto/base/env_params.proto\x1a\x18magneto/base/error.proto\x1a\x1amagneto/base/magneto.proto\x1a\x1bmagneto/base/sub_task.proto\"\x81\n\n\x12\x44\x61tabaseBackupInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x13\n\x0bunique_name\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x62_name\x18\x11 \x01(\t\x12=\n\x0e\x64\x62_entity_info\x18\x03 \x01(\x0b\x32%.cohesity.magneto.oracle.DBEntityInfo\x12\x30\n\nskip_error\x18\x04 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12+\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x19\n\x11perform_l0_backup\x18\x06 \x01(\x08\x12\x46\n\x0f\x62\x61\x63kup_set_info\x18\r \x01(\x0b\x32-.cohesity.magneto.agents.oracle.BackupSetInfo\x12\x46\n\x0f\x64\x61ta_files_info\x18\x08 \x01(\x0b\x32-.cohesity.magneto.agents.oracle.DataFilesInfo\x12O\n\x18previous_data_files_info\x18\x10 \x01(\x0b\x32-.cohesity.magneto.agents.oracle.DataFilesInfo\x12\x19\n\rmax_fuzzy_scn\x18\x12 \x01(\x03:\x02-1\x12\x1e\n\x12min_checkpoint_scn\x18\x13 \x01(\x03:\x02-1\x12\x1f\n\x13max_checkpoint_time\x18\x16 \x01(\x03:\x02-1\x12T\n\x13\x64\x62_incarnation_info\x18\t \x01(\x0b\x32\x37.cohesity.magneto.agents.oracle.DatabaseIncarnationInfo\x12\x42\n\rlog_file_info\x18\x0c \x01(\x0b\x32+.cohesity.magneto.agents.oracle.LogFileInfo\x12\x1b\n\x13timezone_difference\x18\n \x01(\x03\x12\x19\n\x11\x63\x61talog_performed\x18\x0b \x01(\x08\x12\x17\n\x0frelative_db_dir\x18\x0e \x01(\t\x12\x18\n\x10\x62\x61\x63kup_view_name\x18\x0f \x01(\t\x12Q\n\x10rman_backup_type\x18\x14 \x01(\x0e\x32+.cohesity.magneto.OracleRmanBackupType.Type:\nkImageCopy\x12\x1b\n\x13is_backup_validated\x18\x15 \x01(\x08\x12\x1a\n\x12is_self_sufficient\x18\x17 \x01(\x08\x12R\n\x19self_sufficiency_log_info\x18\x18 \x01(\x0b\x32/.cohesity.magneto.oracle.SelfSufficiencyLogInfo\x12\'\n\x18is_log_filler_clone_done\x18\x19 \x01(\x08:\x05\x66\x61lse\x12?\n\x0bthread_info\x18\x1a \x01(\x0b\x32*.cohesity.magneto.agents.oracle.ThreadInfo\x12\x17\n\x0frac_config_file\x18\x1b \x01(\t\x12Y\n\x1c\x64\x65precated_archive_logs_info\x18\x07 \x01(\x0b\x32/.cohesity.magneto.agents.oracle.ArchiveLogsInfoB\x02\x18\x01\"\xe7\x02\n\x10VerificationInfo\x12\x46\n\x11\x64\x61tabase_info_vec\x18\x01 \x03(\x0b\x32+.cohesity.magneto.oracle.DatabaseBackupInfo\x12:\n\x14query_oracle_warning\x18\x02 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x19\n\x11query_oracle_info\x18\x03 \x01(\t\x12>\n\x0chost_summary\x18\x04 \x01(\x0b\x32(.cohesity.magneto.agents.HostInfoSummary2t\n\x18oracle_verification_info\x12\'.cohesity.magneto.VerificationInfoProto\x18\x65 \x01(\x0b\x32).cohesity.magneto.oracle.VerificationInfo\"\x81\x02\n\nEntityInfo\x12\x0f\n\x07host_id\x18\x01 \x01(\x03\x12\x11\n\tview_name\x18\x02 \x01(\t\x12\x13\n\x07view_id\x18\x03 \x01(\x03:\x02-1\x12K\n\x11\x64\x61tabase_info_vec\x18\x04 \x03(\x0b\x32\x30.cohesity.magneto.oracle.EntityInfo.DatabaseInfo\x12\x1f\n\x17whitelisted_host_ip_vec\x18\x05 \x03(\t\x12\x14\n\x0cview_fs_path\x18\x06 \x01(\t\x1a\x36\n\x0c\x44\x61tabaseInfo\x12\r\n\x05\x64\x62_id\x18\x01 \x01(\t\x12\x17\n\x0frelative_db_dir\x18\x02 \x01(\t\";\n\x11OracleDBHostsInfo\x12\x13\n\x0bip_addr_vec\x18\x01 \x03(\t\x12\x11\n\tindex_vec\x18\x02 \x03(\x05\"@\n\x13OracleHostMountInfo\x12\x18\n\x10mount_points_vec\x18\x01 \x03(\t\x12\x0f\n\x07num_cpu\x18\x02 \x01(\x05\"\xc1\x0c\n\x0cSnapshotInfo\x12<\n\x06status\x18\x01 \x01(\x0e\x32,.cohesity.magneto.oracle.SnapshotInfo.Status\x12M\n\x11\x64\x61tabase_info_vec\x18\x02 \x03(\x0b\x32\x32.cohesity.magneto.oracle.SnapshotInfo.DatabaseInfo\x12\x17\n\x0fjob_instance_id\x18\x03 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x04 \x01(\x05\x12\x41\n\x14previous_entity_info\x18\x05 \x01(\x0b\x32#.cohesity.magneto.oracle.EntityInfo\x12@\n\x13\x63urrent_entity_info\x18\x06 \x01(\x0b\x32#.cohesity.magneto.oracle.EntityInfo\x12\x19\n\x11\x62\x61\x63kup_job_db_vec\x18\x07 \x03(\t\x12\x1d\n\x15\x62\x61\x63kup_all_dbs_in_job\x18\x08 \x01(\x08\x12\x1d\n\x15\x62\x61\x63kup_all_dbs_in_run\x18\t \x01(\x08\x12\x18\n\x10mount_points_vec\x18\n \x03(\t\x12\x34\n\rsub_tasks_vec\x18\x0b \x03(\x0b\x32\x1d.cohesity.magneto.SubTaskInfo\x12+\n\x05\x65rror\x18\x0c \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x1d\n\x0e\x64iscovery_done\x18\x0e \x01(\x08:\x05\x66\x61lse\x12]\n\x16host_to_mount_info_map\x18\x0f \x03(\x0b\x32=.cohesity.magneto.oracle.SnapshotInfo.HostToMountInfoMapEntry\x12Y\n\x14\x64\x62_to_hosts_info_map\x18\x10 \x03(\x0b\x32;.cohesity.magneto.oracle.SnapshotInfo.DbToHostsInfoMapEntry\x12\x18\n\x10lock_db_entities\x18\x11 \x01(\x08\x12#\n\x1bparallel_log_backup_enabled\x18\x12 \x01(\x08\x12#\n\x14\x64\x62\x63onfig_in_liveview\x18\x13 \x01(\x08:\x05\x66\x61lse\x12\x18\n\x0chost_ip_addr\x18\r \x01(\tB\x02\x18\x01\x1a\xa3\x01\n\x0c\x44\x61tabaseInfo\x12H\n\x13\x63urrent_backup_info\x18\x01 \x01(\x0b\x32+.cohesity.magneto.oracle.DatabaseBackupInfo\x12I\n\x14previous_backup_info\x18\x02 \x01(\x0b\x32+.cohesity.magneto.oracle.DatabaseBackupInfo\x1ag\n\x17HostToMountInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.cohesity.magneto.oracle.OracleHostMountInfo:\x02\x38\x01\x1a\x63\n\x15\x44\x62ToHostsInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.cohesity.magneto.oracle.OracleDBHostsInfo:\x02\x38\x01\"\xe5\x01\n\x06Status\x12\x0c\n\x08kStarted\x10\x00\x12\x10\n\x0ckViewCreated\x10\x01\x12\x12\n\x0ekDbsDiscovered\x10\x02\x12\x16\n\x12kSetupDirsFinished\x10\x03\x12\x10\n\x0ckViewMounted\x10\x04\x12\x13\n\x0fkSubTaskCreated\x10\x05\x12\x15\n\x11kDataFileCopyDone\x10\t\x12\x16\n\x12kLogGapInfoFetched\x10\n\x12\x15\n\x11kSubTasksFinished\x10\x06\x12\x0f\n\x0bkViewCloned\x10\x07\x12\x11\n\rkFilesDeleted\x10\x08\x32h\n\x14oracle_snapshot_info\x12#.cohesity.magneto.SnapshotInfoProto\x18n \x01(\x0b\x32%.cohesity.magneto.oracle.SnapshotInfo\"\xff\x01\n\x11OracleSubTaskInfo\x12\x18\n\x0c\x64\x61tabase_idx\x18\x01 \x01(\x05:\x02-1\x12\x16\n\x0epermit_granted\x18\x02 \x01(\x08\x12\x18\n\x10start_time_usecs\x18\x03 \x01(\x03\x12\x16\n\x0e\x65nd_time_usecs\x18\x04 \x01(\x03\x12\x1d\n\x15progress_monitor_path\x18\x05 \x01(\t2g\n\x14oracle_sub_task_info\x12\x1d.cohesity.magneto.SubTaskInfo\x18l \x01(\x0b\x32*.cohesity.magneto.oracle.OracleSubTaskInfo\"\xd2\x01\n\x17OracleAdditionalRunInfo\x12<\n\x0f\x65ntity_info_vec\x18\x01 \x03(\x0b\x32#.cohesity.magneto.oracle.EntityInfo2y\n\x1aoracle_additional_run_info\x12#.cohesity.magneto.AdditionalRunInfo\x18\x64 \x01(\x0b\x32\x30.cohesity.magneto.oracle.OracleAdditionalRunInfo\"T\n\nDBMetaInfo\x12\x15\n\tfirst_scn\x18\x01 \x01(\x03:\x02-1\x12\x14\n\x08last_scn\x18\x02 \x01(\x03:\x02-1\x12\x19\n\rreset_logs_id\x18\x03 \x01(\x03:\x02-1\"\xb0\x03\n\x13\x44\x61tabaseRestoreInfo\x12\x43\n\x0e\x64\x62_backup_info\x18\x01 \x01(\x0b\x32+.cohesity.magneto.oracle.DatabaseBackupInfo\x12\x18\n\x10\x62\x61\x63kup_view_name\x18\x02 \x01(\t\x12\x15\n\rbackup_run_id\x18\x08 \x01(\x03\x12\x15\n\rrelative_path\x18\x03 \x01(\t\x12?\n\x0b\x62\x61\x63kup_type\x18\x04 \x01(\x0e\x32*.cohesity.magneto.ScheduledBackupType.Type\x12\x12\n\nclone_done\x18\x05 \x01(\x08\x12\x14\n\x0c\x63\x61talog_done\x18\x06 \x01(\x08\x12\x16\n\x0euncatalog_done\x18\x07 \x01(\x08\x12>\n\x11run_meta_info_vec\x18\t \x03(\x0b\x32#.cohesity.magneto.oracle.DBMetaInfo\x12\x15\n\rcopy_datafile\x18\n \x01(\x08\x12\x18\n\x10\x63opy_controlfile\x18\x0b \x01(\x08\x12\x18\n\x10\x64\x62_reset_logs_id\x18\x0c \x01(\x03\"\x99\x16\n\x0bRestoreInfo\x12Q\n\x12restore_task_state\x18\x01 \x01(\x0e\x32\x35.cohesity.magneto.oracle.RestoreInfo.RestoreTaskState\x12\x14\n\x0crestore_time\x18\x02 \x01(\t\x12\x1b\n\x13timezone_difference\x18\x03 \x01(\x03\x12i\n\x19\x61lternate_location_params\x18\x05 \x01(\x0b\x32\x46.cohesity.magneto.RestoreOracleAppObjectParams.AlternateLocationParams\x12I\n\x13\x64\x62_restore_info_vec\x18\x06 \x03(\x0b\x32,.cohesity.magneto.oracle.DatabaseRestoreInfo\x12+\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12\x14\n\x0cno_open_mode\x18\x0c \x01(\x08\x12\x15\n\rbackup_job_id\x18\r \x01(\x03\x12N\n\x17\x64\x65stroy_clone_task_info\x18\x0e \x01(\x0b\x32-.cohesity.magneto.oracle.DestroyCloneTaskInfo\x12T\n\x17migrate_clone_task_info\x18\x1b \x01(\x0b\x32\x33.cohesity.magneto.oracle.MigrateOracleCloneTaskInfo\x12#\n\x14is_migration_subtask\x18\x1c \x01(\x08:\x05\x66\x61lse\x12\x41\n\x12\x63loned_db_info_vec\x18\x18 \x03(\x0b\x32%.cohesity.magneto.oracle.ClonedDBInfo\x12\x1d\n\x15restore_proto_version\x18\x0f \x01(\x03\x12\\\n\x16host_to_mount_info_map\x18\x10 \x03(\x0b\x32<.cohesity.magneto.oracle.RestoreInfo.HostToMountInfoMapEntry\x12X\n\x14\x64\x62_to_hosts_info_map\x18\x11 \x03(\x0b\x32:.cohesity.magneto.oracle.RestoreInfo.DbToHostsInfoMapEntry\x12\x42\n\x14oracle_target_params\x18\x12 \x01(\x0b\x32$.cohesity.magneto.OracleSourceParams\x12\x62\n\x19\x63loned_data_file_info_map\x18\x14 \x03(\x0b\x32?.cohesity.magneto.oracle.RestoreInfo.ClonedDataFileInfoMapEntry\x12N\n oracle_clone_app_view_params_vec\x18\x15 \x03(\x0b\x32$.cohesity.magneto.CloneAppViewParams\x12\x18\n\x10lock_db_entities\x18\x16 \x01(\x08\x12#\n\x1boracle_restore_to_same_host\x18\x17 \x01(\x08\x12Z\n\x15shell_environment_vec\x18\x19 \x03(\x0b\x32;.cohesity.magneto.RestoreOracleAppObjectParams.KeyValuePair\x12\x44\n\x15granular_restore_info\x18\x1a \x01(\x0b\x32%.cohesity.magneto.GranularRestoreInfo\x12 \n\x18granular_clone_completed\x18\x1d \x01(\x08\x12\x16\n\x0eskip_clone_nid\x18\x1e \x01(\x08\x12!\n\x19roll_forward_log_path_vec\x18\x1f \x03(\t\x12!\n\x19\x61ttempt_complete_recovery\x18  \x01(\x08\x12\x1f\n\x17roll_forward_time_msecs\x18# \x01(\x03\x12O\n\x1foracle_archive_log_restore_info\x18! \x01(\x0b\x32&.cohesity.magneto.OracleArchiveLogInfo\x12\x13\n\x0brestore_scn\x18\" \x01(\x03\x12W\n\x1foracle_recovery_validation_info\x18$ \x01(\x0b\x32..cohesity.magneto.OracleRecoveryValidationInfo\x12P\n\x1crestore_spfile_or_pfile_info\x18% \x01(\x0b\x32*.cohesity.magneto.RestoreSpfileOrPfileInfo\x12\x1b\n\x13use_scn_for_restore\x18& \x01(\x08\x12\x1b\n\x13stop_active_passive\x18\' \x01(\x08\x12\x61\n\x1fsame_config_ir_recovery_options\x18( \x01(\x0b\x32\x38.cohesity.magneto.api.oracle.SameConfigIrRecoveryOptions\x12\x16\n\x0erestore_as_rac\x18) \x01(\x08\x12\x1a\n\x0eincarnation_id\x18\x04 \x01(\x05\x42\x02\x18\x01\x12\x1c\n\x10mount_points_vec\x18\x07 \x03(\tB\x02\x18\x01\x12\x18\n\x0c\x63ontrol_file\x18\t \x01(\tB\x02\x18\x01\x12&\n\x1a\x63ontrol_file_backup_run_id\x18\n \x01(\x03\x42\x02\x18\x01\x12\x18\n\x0chost_ip_addr\x18\x0b \x01(\tB\x02\x18\x01\x12\x19\n\rcatalog_index\x18\x13 \x01(\x05\x42\x02\x18\x01\x1ag\n\x17HostToMountInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.cohesity.magneto.oracle.OracleHostMountInfo:\x02\x38\x01\x1a\x63\n\x15\x44\x62ToHostsInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.cohesity.magneto.oracle.OracleDBHostsInfo:\x02\x38\x01\x1a<\n\x1a\x43lonedDataFileInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xaa\x02\n\x10RestoreTaskState\x12\x0c\n\x08kStarted\x10\x01\x12\x16\n\x12kBackupFilesCloned\x10\x02\x12\x10\n\x0ckViewMounted\x10\x03\x12\x1e\n\x1akRestorePrecheckInProgress\x10\x0c\x12\x18\n\x14kControlFileRestored\x10\t\x12\x10\n\x0ckCatalogDone\x10\x04\x12\x12\n\x0ekRestoreDBDone\x10\x05\x12\x19\n\x15kPostAltRestoreDBDone\x10\x0b\x12\x12\n\x0ekUnCatalogDone\x10\x06\x12\x12\n\x0ekViewUnmounted\x10\x07\x12\x16\n\x12kRestoreLogsCopied\x10\r\x12\r\n\tkFinished\x10\x08\x12\x14\n\x10kDBConfigFetched\x10\n2e\n\x13oracle_restore_info\x12\".cohesity.magneto.RestoreInfoProto\x18n \x01(\x0b\x32$.cohesity.magneto.oracle.RestoreInfo\"\xdc\x01\n\x0c\x43lonedDBInfo\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x62_sid\x18\x02 \x01(\t\x12\x13\n\x0boracle_home\x18\x03 \x01(\t\x12=\n\x0e\x64\x62_entity_info\x18\x06 \x01(\x0b\x32%.cohesity.magneto.oracle.DBEntityInfo\x12\x0c\n\x04uuid\x18\x07 \x01(\t\x12\x1c\n\x14\x64ropped_successfully\x18\x04 \x01(\x08\x12+\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\"\xbb\x04\n\x14\x44\x65stroyCloneTaskInfo\x12\x17\n\x0fhost_identifier\x18\x01 \x01(\t\x12\x1d\n\x15mountpoint_identifier\x18\x02 \x01(\t\x12\x1a\n\x12mountpoint_basedir\x18\x07 \x01(\t\x12\x11\n\tview_name\x18\x03 \x01(\t\x12Z\n\x12\x64\x65stroy_task_state\x18\x04 \x01(\x0e\x32>.cohesity.magneto.oracle.DestroyCloneTaskInfo.DestroyTaskState\x12\x41\n\x12\x63loned_db_info_vec\x18\x05 \x03(\x0b\x32%.cohesity.magneto.oracle.ClonedDBInfo\x12$\n\x1cview_mount_subdir_identifier\x18\x06 \x01(\t\x12#\n\x1bremote_host_identifiers_vec\x18\x08 \x03(\t\"F\n\x10\x44\x65stroyTaskState\x12\x0c\n\x08kStarted\x10\x01\x12\x10\n\x0ckDropDBsDone\x10\x02\x12\x12\n\x0ekViewUnmounted\x10\x03\x32\x89\x01\n\"oracle_destroy_clone_app_task_info\x12..cohesity.magneto.DestroyCloneAppTaskInfoProto\x18\x65 \x01(\x0b\x32-.cohesity.magneto.oracle.DestroyCloneTaskInfo\"\xe2\x02\n\x1aMigrateOracleCloneTaskInfo\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x12k\n\x18migrate_clone_task_state\x18\x02 \x01(\x0e\x32I.cohesity.magneto.oracle.MigrateOracleCloneTaskInfo.MigrateCloneTaskState\x12H\n\x14migrate_clone_params\x18\x03 \x01(\x0b\x32*.cohesity.magneto.MigrateOracleCloneParams\"`\n\x15MigrateCloneTaskState\x12\x0c\n\x08kStarted\x10\x01\x12\x11\n\rkPrecheckDone\x10\x02\x12\x12\n\x0ekDBMigrateDone\x10\x03\x12\x12\n\x0ekViewUnmounted\x10\x04\"\x9a\x02\n\x16SelfSufficiencyLogInfo\x12Z\n\x13\x63lone_logs_info_vec\x18\x01 \x03(\x0b\x32=.cohesity.magneto.oracle.SelfSufficiencyLogInfo.CloneLogsInfo\x12\x1c\n\x14\x61rchivelog_base_time\x18\x02 \x01(\t\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.cohesity.magneto.ErrorProto\x1aY\n\rCloneLogsInfo\x12\x11\n\tview_name\x18\x01 \x01(\t\x12\x17\n\x0frelative_db_dir\x18\x02 \x01(\t\x12\x1c\n\x14run_start_time_usecs\x18\x03 \x01(\x03\x42%Z#magneto/connectors/oracle/oracle.pb')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.connectors.oracle.oracle_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#magneto/connectors/oracle/oracle.pb'
  _globals['_DATABASEBACKUPINFO'].fields_by_name['deprecated_archive_logs_info']._loaded_options = None
  _globals['_DATABASEBACKUPINFO'].fields_by_name['deprecated_archive_logs_info']._serialized_options = b'\030\001'
  _globals['_SNAPSHOTINFO_HOSTTOMOUNTINFOMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_HOSTTOMOUNTINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO_DBTOHOSTSINFOMAPENTRY']._loaded_options = None
  _globals['_SNAPSHOTINFO_DBTOHOSTSINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_SNAPSHOTINFO'].fields_by_name['host_ip_addr']._loaded_options = None
  _globals['_SNAPSHOTINFO'].fields_by_name['host_ip_addr']._serialized_options = b'\030\001'
  _globals['_RESTOREINFO_HOSTTOMOUNTINFOMAPENTRY']._loaded_options = None
  _globals['_RESTOREINFO_HOSTTOMOUNTINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREINFO_DBTOHOSTSINFOMAPENTRY']._loaded_options = None
  _globals['_RESTOREINFO_DBTOHOSTSINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREINFO_CLONEDDATAFILEINFOMAPENTRY']._loaded_options = None
  _globals['_RESTOREINFO_CLONEDDATAFILEINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_RESTOREINFO'].fields_by_name['incarnation_id']._loaded_options = None
  _globals['_RESTOREINFO'].fields_by_name['incarnation_id']._serialized_options = b'\030\001'
  _globals['_RESTOREINFO'].fields_by_name['mount_points_vec']._loaded_options = None
  _globals['_RESTOREINFO'].fields_by_name['mount_points_vec']._serialized_options = b'\030\001'
  _globals['_RESTOREINFO'].fields_by_name['control_file']._loaded_options = None
  _globals['_RESTOREINFO'].fields_by_name['control_file']._serialized_options = b'\030\001'
  _globals['_RESTOREINFO'].fields_by_name['control_file_backup_run_id']._loaded_options = None
  _globals['_RESTOREINFO'].fields_by_name['control_file_backup_run_id']._serialized_options = b'\030\001'
  _globals['_RESTOREINFO'].fields_by_name['host_ip_addr']._loaded_options = None
  _globals['_RESTOREINFO'].fields_by_name['host_ip_addr']._serialized_options = b'\030\001'
  _globals['_RESTOREINFO'].fields_by_name['catalog_index']._loaded_options = None
  _globals['_RESTOREINFO'].fields_by_name['catalog_index']._serialized_options = b'\030\001'
  _globals['_DATABASEBACKUPINFO']._serialized_start=348
  _globals['_DATABASEBACKUPINFO']._serialized_end=1629
  _globals['_VERIFICATIONINFO']._serialized_start=1632
  _globals['_VERIFICATIONINFO']._serialized_end=1991
  _globals['_ENTITYINFO']._serialized_start=1994
  _globals['_ENTITYINFO']._serialized_end=2251
  _globals['_ENTITYINFO_DATABASEINFO']._serialized_start=2197
  _globals['_ENTITYINFO_DATABASEINFO']._serialized_end=2251
  _globals['_ORACLEDBHOSTSINFO']._serialized_start=2253
  _globals['_ORACLEDBHOSTSINFO']._serialized_end=2312
  _globals['_ORACLEHOSTMOUNTINFO']._serialized_start=2314
  _globals['_ORACLEHOSTMOUNTINFO']._serialized_end=2378
  _globals['_SNAPSHOTINFO']._serialized_start=2381
  _globals['_SNAPSHOTINFO']._serialized_end=3982
  _globals['_SNAPSHOTINFO_DATABASEINFO']._serialized_start=3275
  _globals['_SNAPSHOTINFO_DATABASEINFO']._serialized_end=3438
  _globals['_SNAPSHOTINFO_HOSTTOMOUNTINFOMAPENTRY']._serialized_start=3440
  _globals['_SNAPSHOTINFO_HOSTTOMOUNTINFOMAPENTRY']._serialized_end=3543
  _globals['_SNAPSHOTINFO_DBTOHOSTSINFOMAPENTRY']._serialized_start=3545
  _globals['_SNAPSHOTINFO_DBTOHOSTSINFOMAPENTRY']._serialized_end=3644
  _globals['_SNAPSHOTINFO_STATUS']._serialized_start=3647
  _globals['_SNAPSHOTINFO_STATUS']._serialized_end=3876
  _globals['_ORACLESUBTASKINFO']._serialized_start=3985
  _globals['_ORACLESUBTASKINFO']._serialized_end=4240
  _globals['_ORACLEADDITIONALRUNINFO']._serialized_start=4243
  _globals['_ORACLEADDITIONALRUNINFO']._serialized_end=4453
  _globals['_DBMETAINFO']._serialized_start=4455
  _globals['_DBMETAINFO']._serialized_end=4539
  _globals['_DATABASERESTOREINFO']._serialized_start=4542
  _globals['_DATABASERESTOREINFO']._serialized_end=4974
  _globals['_RESTOREINFO']._serialized_start=4977
  _globals['_RESTOREINFO']._serialized_end=7818
  _globals['_RESTOREINFO_HOSTTOMOUNTINFOMAPENTRY']._serialized_start=3440
  _globals['_RESTOREINFO_HOSTTOMOUNTINFOMAPENTRY']._serialized_end=3543
  _globals['_RESTOREINFO_DBTOHOSTSINFOMAPENTRY']._serialized_start=3545
  _globals['_RESTOREINFO_DBTOHOSTSINFOMAPENTRY']._serialized_end=3644
  _globals['_RESTOREINFO_CLONEDDATAFILEINFOMAPENTRY']._serialized_start=7354
  _globals['_RESTOREINFO_CLONEDDATAFILEINFOMAPENTRY']._serialized_end=7414
  _globals['_RESTOREINFO_RESTORETASKSTATE']._serialized_start=7417
  _globals['_RESTOREINFO_RESTORETASKSTATE']._serialized_end=7715
  _globals['_CLONEDDBINFO']._serialized_start=7821
  _globals['_CLONEDDBINFO']._serialized_end=8041
  _globals['_DESTROYCLONETASKINFO']._serialized_start=8044
  _globals['_DESTROYCLONETASKINFO']._serialized_end=8615
  _globals['_DESTROYCLONETASKINFO_DESTROYTASKSTATE']._serialized_start=8405
  _globals['_DESTROYCLONETASKINFO_DESTROYTASKSTATE']._serialized_end=8475
  _globals['_MIGRATEORACLECLONETASKINFO']._serialized_start=8618
  _globals['_MIGRATEORACLECLONETASKINFO']._serialized_end=8972
  _globals['_MIGRATEORACLECLONETASKINFO_MIGRATECLONETASKSTATE']._serialized_start=8876
  _globals['_MIGRATEORACLECLONETASKINFO_MIGRATECLONETASKSTATE']._serialized_end=8972
  _globals['_SELFSUFFICIENCYLOGINFO']._serialized_start=8975
  _globals['_SELFSUFFICIENCYLOGINFO']._serialized_end=9257
  _globals['_SELFSUFFICIENCYLOGINFO_CLONELOGSINFO']._serialized_start=9168
  _globals['_SELFSUFFICIENCYLOGINFO_CLONELOGSINFO']._serialized_end=9257
# @@protoc_insertion_point(module_scope)
