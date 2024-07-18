# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/one_drive/one_drive_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base.entities import o365_pb2 as magneto_dot_base_dot_entities_dot_o365__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.connectors.ms_graph import graph_pb2 as magneto_dot_connectors_dot_ms__graph_dot_graph__pb2
from magneto.connectors.o365 import o365_pb2 as magneto_dot_connectors_dot_o365_dot_o365__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0bridge/magneto/one_drive/one_drive_actions.proto\x12!cohesity.bridge.magneto.one_drive\x1a)bridge/magneto/base/magneto_actions.proto\x1a magneto/base/entities/o365.proto\x1a\x18magneto/base/enums.proto\x1a\'magneto/connectors/ms_graph/graph.proto\x1a\"magneto/connectors/o365/o365.proto\"b\n\x11PrepareBackupInfo\x12\x1e\n\x16skip_directory_cloning\x18\x01 \x01(\x08\x12\x10\n\x08\x64rive_id\x18\x02 \x01(\t\x12\x1b\n\x13\x63reate_rocks_db_dir\x18\x03 \x01(\x08\"\xd6\x04\n\tSetupInfo\x12\x42\n\x15\x64rive_item_change_vec\x18\x01 \x03(\x0b\x32#.cohesity.magneto.MSGraph.DriveItem\x12\x14\n\x0c\x64\x65ny_filters\x18\x02 \x03(\t\x12\x10\n\x08\x64rive_id\x18\x03 \x01(\t\x12\x1c\n\x14\x64\x65ny_filters_changed\x18\x04 \x01(\x08\x12\"\n\x1a\x65xcluded_drive_item_id_vec\x18\x05 \x03(\t\x12$\n\x1csend_error_on_move_operation\x18\x06 \x01(\x08\x12\x1d\n\x15\x63lose_rocks_db_handle\x18\x07 \x01(\x08\x12\'\n\x19\x63reate_files_during_setup\x18\x08 \x01(\x08:\x04true\x12\"\n\x1ashould_trigger_full_backup\x18\t \x01(\x08\x12!\n\x19skip_fetching_permissions\x18\n \x01(\x08\x12*\n\"skip_storing_inherited_permissions\x18\x0b \x01(\x08\x12\x1d\n\x15is_incremental_backup\x18\x0c \x01(\x08\x12\x1f\n\x17incremental_file_offset\x18\r \x01(\x03\x12!\n\x19is_first_setup_info_batch\x18\x0e \x01(\x08\x12\x1d\n\x15\x66\x65tch_all_permissions\x18\x0f \x01(\x08\x12\x1d\n\x15should_recon_metadata\x18\x10 \x01(\x08\x12\x19\n\x11should_recon_data\x18\x11 \x01(\x08\"\xc6\x01\n\x0f\x42\x61\x63kupFilesInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x64rive_id\x18\x02 \x01(\t\x12\x37\n\ndrive_item\x18\x03 \x01(\x0b\x32#.cohesity.magneto.MSGraph.DriveItem\x12\x0e\n\x06offset\x18\x04 \x01(\x03\x12\x0e\n\x06length\x18\x05 \x01(\x03\x12\x1c\n\x14\x63heck_file_integrity\x18\x06 \x01(\x08\x12\x19\n\x11\x63reate_file_first\x18\x07 \x01(\x08\"\x82\x01\n\x14\x43hunkBackupFilesInfo\x12Q\n\x15\x62\x61\x63kup_files_info_vec\x18\x01 \x03(\x0b\x32\x32.cohesity.bridge.magneto.one_drive.BackupFilesInfo\x12\x17\n\x0fstart_index_vec\x18\x02 \x03(\x03\"7\n\x12\x45ndDataSubTaskInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x64rive_id\x18\x02 \x01(\t\";\n\x16\x45ndMetadataSubTaskInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x64rive_id\x18\x02 \x01(\t\"\x9a\x04\n\rEndBackupInfo\x12\x46\n\x10one_drive_config\x18\x01 \x01(\x0b\x32,.cohesity.magneto.MSGraph.OneDriveConfigFile\x12\x1f\n\x11write_config_file\x18\x02 \x01(\x08:\x04true\x12\x10\n\x08\x64rive_id\x18\x03 \x01(\t\x12\x1b\n\x13\x64\x65leted_item_id_vec\x18\x04 \x03(\t\x12!\n\x19\x63onfirm_config_file_write\x18\x05 \x01(\x08\x12\x1a\n\x12\x63leanup_on_failure\x18\x06 \x01(\x08\x12\x14\n\x0cis_new_drive\x18\x07 \x01(\x08\x12\"\n\x1aremove_failed_attempt_dirs\x18\x08 \x01(\x08\x12,\n$fix_parent_linkage_for_deleted_items\x18\t \x01(\x08\x12\x1f\n\x17\x66\x61st_cleanup_on_failure\x18\n \x01(\x08\x12*\n\"finalize_incremental_indexing_file\x18\x0b \x01(\x08\x12\"\n\x1ashould_delete_old_error_db\x18\x0c \x01(\x08\x12Y\n\x1emismatched_drive_item_size_vec\x18\r \x03(\x0b\x32\x31.cohesity.magneto.MSGraph.MismatchedDriveItemSize\"\xf5\t\n\x11\x42\x61\x63kupOneDriveArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12G\n\x04type\x18\x02 \x01(\x0e\x32\x39.cohesity.bridge.magneto.one_drive.BackupOneDriveArg.Type\x12\x32\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12\x32\n\x0buser_entity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12Q\n\x13prepare_backup_info\x18\x05 \x01(\x0b\x32\x34.cohesity.bridge.magneto.one_drive.PrepareBackupInfo\x12@\n\nsetup_info\x18\x06 \x01(\x0b\x32,.cohesity.bridge.magneto.one_drive.SetupInfo\x12M\n\x11\x62\x61\x63kup_files_info\x18\x07 \x03(\x0b\x32\x32.cohesity.bridge.magneto.one_drive.BackupFilesInfo\x12X\n\x17\x63hunk_backup_files_info\x18\x0e \x01(\x0b\x32\x37.cohesity.bridge.magneto.one_drive.ChunkBackupFilesInfo\x12I\n\x0f\x65nd_backup_info\x18\t \x01(\x0b\x32\x30.cohesity.bridge.magneto.one_drive.EndBackupInfo\x12U\n\x16\x65nd_data_sub_task_info\x18\n \x01(\x0b\x32\x35.cohesity.bridge.magneto.one_drive.EndDataSubTaskInfo\x12]\n\x1a\x65nd_metadata_sub_task_info\x18\x0b \x01(\x0b\x32\x39.cohesity.bridge.magneto.one_drive.EndMetadataSubTaskInfo\x12J\n\x10one_drive_config\x18\x0c \x01(\x0b\x32,.cohesity.magneto.MSGraph.OneDriveConfigFileB\x02\x18\x01\x12\x1d\n\x11write_config_file\x18\r \x01(\x08\x42\x02\x18\x01\x12 \n\x18one_drive_config_present\x18\x0f \x01(\x08\x12(\n throttling_time_bins_size_string\x18\x10 \x01(\t\x12\x1a\n\x12record_error_in_db\x18\x11 \x01(\x08\x12?\n\x0b\x62\x61\x63kup_type\x18\x12 \x01(\x0e\x32*.cohesity.magneto.ScheduledBackupType.Type\"\x9f\x01\n\x04Type\x12\x1a\n\x16kPrepareOneDriveBackup\x10\x01\x12\x0e\n\nkSetupInfo\x10\x02\x12\x10\n\x0ckBackupFiles\x10\x03\x12\x0e\n\nkEndBackup\x10\x05\x12\x13\n\x0fkEndDataSubTask\x10\x06\x12\x17\n\x13kEndMetadataSubTask\x10\x07\x12\x15\n\x11kChunkBackupFiles\x10\x08\"\x04\x08\x04\x10\x04J\x04\x08\x08\x10\t\"\x8a\x01\n\x0bReadDirInfo\x12\x10\n\x08\x64ir_path\x18\x01 \x01(\t\x12\"\n\x1alast_visited_drive_item_id\x18\x02 \x01(\t\x12*\n\"num_drive_items_to_read_in_rocksdb\x18\x03 \x01(\x03\x12\x19\n\x11relative_dir_path\x18\x04 \x01(\t\"\x9b\x04\n\x10RestoreFilesInfo\x12\x1f\n\x17\x66ull_parent_folder_path\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x1b\n\x13is_full_file_upload\x18\x03 \x01(\x08\x12\x0f\n\x07web_url\x18\x04 \x01(\t\x12\x0e\n\x06offset\x18\x05 \x01(\x03\x12\x0e\n\x06length\x18\x06 \x01(\x03\x12\x13\n\x0btarget_path\x18\x08 \x01(\t\x12\x1a\n\x12snapfs_prefix_path\x18\t \x01(\t\x12\x1e\n\x16total_full_file_length\x18\n \x01(\x03\x12\x10\n\x08\x64rive_id\x18\x0b \x01(\t\x12\x15\n\rsrc_root_path\x18\x0c \x01(\t\x12\x11\n\tis_folder\x18\r \x01(\x08\x12\"\n\x1ashould_permissions_restore\x18\x0e \x01(\x08\x12\x45\n\x16restore_permission_vec\x18\x0f \x03(\x0b\x32%.cohesity.magneto.MSGraph.Permissions\x12\x15\n\rdrive_item_id\x18\x10 \x01(\t\x12\x1e\n\x16restored_drive_item_id\x18\x11 \x01(\t\x12#\n\x1b\x64rive_item_relative_web_url\x18\x12 \x01(\t\x12\x11\n\tupload_id\x18\x13 \x01(\t\x12\x1e\n\x16\x64\x65ny_permission_id_vec\x18\x14 \x03(\t\"\x17\n\x15\x45ndRestoreSubTaskInfo\"\x10\n\x0e\x45ndRestoreInfo\"\xf7\x05\n\x12RestoreOneDriveArg\x12\x35\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12H\n\x04type\x18\x02 \x01(\x0e\x32:.cohesity.bridge.magneto.one_drive.RestoreOneDriveArg.Type\x12\x15\n\rsrc_root_path\x18\x03 \x01(\t\x12\x45\n\rread_dir_info\x18\x05 \x01(\x0b\x32..cohesity.bridge.magneto.one_drive.ReadDirInfo\x12O\n\x12restore_files_info\x18\x06 \x03(\x0b\x32\x33.cohesity.bridge.magneto.one_drive.RestoreFilesInfo\x12Z\n\x18\x65nd_restore_subtask_info\x18\x07 \x01(\x0b\x32\x38.cohesity.bridge.magneto.one_drive.EndRestoreSubTaskInfo\x12K\n\x10\x65nd_restore_info\x18\x08 \x01(\x0b\x32\x31.cohesity.bridge.magneto.one_drive.EndRestoreInfo\x12$\n\x1crelative_drive_snapshot_path\x18\t \x01(\t\x12\x1b\n\x13target_site_web_url\x18\n \x01(\t\x12\x1e\n\x16sharepoint_domain_name\x18\x0b \x01(\t\x12\x17\n\x0fis_system_drive\x18\x0c \x01(\x08\x12\x1b\n\x13source_site_web_url\x18\r \x01(\t\x12\x19\n\x11\x63ontinue_on_error\x18\x0e \x01(\x08\"T\n\x04Type\x12\x10\n\x0ckReadDirInfo\x10\x01\x12\x11\n\rkRestoreFiles\x10\x02\x12\x16\n\x12kEndRestoreSubTask\x10\x03\x12\x0f\n\x0bkEndRestore\x10\x04\"t\n\rCancelTaskArg\x12\x1d\n\x15wait_for_cancellation\x18\x01 \x01(\x08\x12!\n\x19\x64\x65\x61\x64_slave_constituent_id\x18\x02 \x01(\x03\x12!\n\x19\x64\x65\x61\x64_slave_incarnation_id\x18\x03 \x01(\x03\"\xed\x04\n\x11OneDriveActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12\x10\n\x08\x64rive_id\x18\x08 \x01(\t\x12R\n\x14\x62\x61\x63kup_one_drive_arg\x18\x03 \x01(\x0b\x32\x34.cohesity.bridge.magneto.one_drive.BackupOneDriveArg\x12T\n\x15restore_one_drive_arg\x18\x04 \x01(\x0b\x32\x35.cohesity.bridge.magneto.one_drive.RestoreOneDriveArg\x12M\n\x07version\x18\x05 \x01(\x0e\x32<.cohesity.bridge.magneto.one_drive.OneDriveActionArg.Version\x12I\n\x0f\x63\x61ncel_task_arg\x18\x06 \x01(\x0b\x32\x30.cohesity.bridge.magneto.one_drive.CancelTaskArg\x12<\n\x0eoperation_info\x18\x07 \x01(\x0b\x32$.cohesity.magneto.o365.OperationInfo\"\x1b\n\x07Version\x12\x07\n\x03kV0\x10\x00\x12\x07\n\x03kV1\x10\x01\x32}\n\x14one_drive_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18u \x01(\x0b\x32\x34.cohesity.bridge.magneto.one_drive.OneDriveActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.one_drive.one_drive_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BACKUPONEDRIVEARG'].fields_by_name['one_drive_config']._loaded_options = None
  _globals['_BACKUPONEDRIVEARG'].fields_by_name['one_drive_config']._serialized_options = b'\030\001'
  _globals['_BACKUPONEDRIVEARG'].fields_by_name['write_config_file']._loaded_options = None
  _globals['_BACKUPONEDRIVEARG'].fields_by_name['write_config_file']._serialized_options = b'\030\001'
  _globals['_PREPAREBACKUPINFO']._serialized_start=267
  _globals['_PREPAREBACKUPINFO']._serialized_end=365
  _globals['_SETUPINFO']._serialized_start=368
  _globals['_SETUPINFO']._serialized_end=966
  _globals['_BACKUPFILESINFO']._serialized_start=969
  _globals['_BACKUPFILESINFO']._serialized_end=1167
  _globals['_CHUNKBACKUPFILESINFO']._serialized_start=1170
  _globals['_CHUNKBACKUPFILESINFO']._serialized_end=1300
  _globals['_ENDDATASUBTASKINFO']._serialized_start=1302
  _globals['_ENDDATASUBTASKINFO']._serialized_end=1357
  _globals['_ENDMETADATASUBTASKINFO']._serialized_start=1359
  _globals['_ENDMETADATASUBTASKINFO']._serialized_end=1418
  _globals['_ENDBACKUPINFO']._serialized_start=1421
  _globals['_ENDBACKUPINFO']._serialized_end=1959
  _globals['_BACKUPONEDRIVEARG']._serialized_start=1962
  _globals['_BACKUPONEDRIVEARG']._serialized_end=3231
  _globals['_BACKUPONEDRIVEARG_TYPE']._serialized_start=3066
  _globals['_BACKUPONEDRIVEARG_TYPE']._serialized_end=3225
  _globals['_READDIRINFO']._serialized_start=3234
  _globals['_READDIRINFO']._serialized_end=3372
  _globals['_RESTOREFILESINFO']._serialized_start=3375
  _globals['_RESTOREFILESINFO']._serialized_end=3914
  _globals['_ENDRESTORESUBTASKINFO']._serialized_start=3916
  _globals['_ENDRESTORESUBTASKINFO']._serialized_end=3939
  _globals['_ENDRESTOREINFO']._serialized_start=3941
  _globals['_ENDRESTOREINFO']._serialized_end=3957
  _globals['_RESTOREONEDRIVEARG']._serialized_start=3960
  _globals['_RESTOREONEDRIVEARG']._serialized_end=4719
  _globals['_RESTOREONEDRIVEARG_TYPE']._serialized_start=4635
  _globals['_RESTOREONEDRIVEARG_TYPE']._serialized_end=4719
  _globals['_CANCELTASKARG']._serialized_start=4721
  _globals['_CANCELTASKARG']._serialized_end=4837
  _globals['_ONEDRIVEACTIONARG']._serialized_start=4840
  _globals['_ONEDRIVEACTIONARG']._serialized_end=5461
  _globals['_ONEDRIVEACTIONARG_VERSION']._serialized_start=5307
  _globals['_ONEDRIVEACTIONARG_VERSION']._serialized_end=5334
# @@protoc_insertion_point(module_scope)