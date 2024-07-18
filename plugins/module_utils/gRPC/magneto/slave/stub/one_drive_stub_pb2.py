# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/slave/stub/one_drive_stub.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.slave.stub import stub_pb2 as magneto_dot_slave_dot_stub_dot_stub__pb2
from magneto.connectors.ms_graph import graph_pb2 as magneto_dot_connectors_dot_ms__graph_dot_graph__pb2
from magneto.connectors.o365 import o365_pb2 as magneto_dot_connectors_dot_o365_dot_o365__pb2
from magneto.slave.stub import bridge_updates_pb2 as magneto_dot_slave_dot_stub_dot_bridge__updates__pb2
from magneto.connectors.o365 import o365_error_pb2 as magneto_dot_connectors_dot_o365_dot_o365__error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'magneto/slave/stub/one_drive_stub.proto\x12%cohesity.magneto.slave.stub.one_drive\x1a\x1dmagneto/slave/stub/stub.proto\x1a\'magneto/connectors/ms_graph/graph.proto\x1a\"magneto/connectors/o365/o365.proto\x1a\'magneto/slave/stub/bridge_updates.proto\x1a(magneto/connectors/o365/o365_error.proto\"m\n\x1ePrepareOneDriveBackupUpdateArg\x12K\n\x15one_drive_config_file\x18\x01 \x01(\x0b\x32,.cohesity.magneto.MSGraph.OneDriveConfigFile\"\xb6\x04\n\x12SetupInfoUpdateArg\x12\x45\n\x18\x64rive_item_vec_to_backup\x18\x01 \x03(\x0b\x32#.cohesity.magneto.MSGraph.DriveItem\x12\x1d\n\x15total_drive_data_size\x18\x02 \x01(\x03\x12\"\n\x1a\x65xcluded_drive_item_id_vec\x18\x03 \x03(\t\x12!\n\x12lookup_error_found\x18\x04 \x01(\x08:\x05\x66\x61lse\x12!\n\x19num_skipped_items_malware\x18\x05 \x01(\x03\x12#\n\x1bnum_skipped_items_same_ctag\x18\n \x01(\x03\x12\x42\n\x10setup_info_stats\x18\x06 \x01(\x0b\x32(.cohesity.magneto.MSGraph.SetupInfoStats\x12X\n\x10throttling_table\x18\x07 \x01(\x0b\x32>.cohesity.magneto.MSGraph.ThrottlingErrorTimeDistributionTable\x12\x1f\n\x17incremental_file_offset\x18\x08 \x01(\x03\x12\x46\n\x12\x65rror_db_entry_vec\x18\t \x03(\x0b\x32*.cohesity.magneto.MSGraph.O365ErrorDBEntry\x12$\n\x1cnum_skipped_permission_items\x18\x0b \x01(\x03\"\xf0\x07\n\x14\x42\x61\x63kupFilesUpdateArg\x12\x1c\n\x14skipped_item_ids_vec\x18\x01 \x03(\t\x12\x19\n\x11request_throttled\x18\x02 \x01(\x08\x12!\n\x12lookup_error_found\x18\x03 \x01(\x08:\x05\x66\x61lse\x12Y\n\ntask_stats\x18\x04 \x03(\x0b\x32\x45.cohesity.magneto.slave.stub.one_drive.BackupFilesUpdateArg.TaskStats\x12P\n\x16\x62\x61\x63kup_disk_update_arg\x18\x05 \x01(\x0b\x32\x30.cohesity.magneto.slave.stub.BackupDiskUpdateArg\x12X\n\x10throttling_table\x18\x06 \x01(\x0b\x32>.cohesity.magneto.MSGraph.ThrottlingErrorTimeDistributionTable\x12\x15\n\rnum_api_calls\x18\r \x03(\x03\x12\x19\n\x11request_timestamp\x18\x07 \x03(\x03\x12\x17\n\x0f\x64\x65\x61\x64_time_usecs\x18\x08 \x03(\x03\x12\x1b\n\x13\x64\x65\x61\x64_time_timestamp\x18\t \x03(\x03\x12\x18\n\x10total_time_usecs\x18\n \x03(\x03\x12\x1c\n\x14total_time_timestamp\x18\x0b \x03(\x03\x12\x46\n\x12\x65rror_db_entry_vec\x18\x0c \x03(\x0b\x32*.cohesity.magneto.MSGraph.O365ErrorDBEntry\x12Y\n\x1emismatched_drive_item_size_vec\x18\x0e \x03(\x0b\x32\x31.cohesity.magneto.MSGraph.MismatchedDriveItemSize\x1a\xb1\x02\n\tTaskStats\x12\x18\n\x10\x62ytes_downloaded\x18\x01 \x01(\x03\x12\x18\n\x10time_taken_usecs\x18\x02 \x01(\x03\x12p\n\x11\x65rrored_item_info\x18\x03 \x01(\x0b\x32U.cohesity.magneto.slave.stub.one_drive.BackupFilesUpdateArg.TaskStats.ErroredItemInfo\x12\x1c\n\x14\x64\x65\x61\x64_read_time_usecs\x18\x04 \x01(\x03\x1a`\n\x0f\x45rroredItemInfo\x12\x37\n\ndrive_item\x18\x01 \x01(\x0b\x32#.cohesity.magneto.MSGraph.DriveItem\x12\x14\n\x0c\x65rror_reason\x18\x02 \x01(\t\"\x1b\n\x19\x43hunkBackupFilesUpdateArg\"\x1d\n\x1b\x45ndMetadataSubTaskUpdateArg\"\x19\n\x17\x45ndDataSubTaskUpdateArg\"k\n\x12\x45ndBackupUpdateArg\x12\x19\n\x11num_items_deleted\x18\x01 \x01(\x03\x12\x1b\n\x13\x63onfig_file_written\x18\x02 \x01(\x08\x12\x1d\n\x15is_cleanup_successful\x18\x03 \x01(\x08\"\xc1\x01\n\x14ReadDirInfoUpdateArg\x12;\n\x0e\x64rive_item_vec\x18\x01 \x03(\x0b\x32#.cohesity.magneto.MSGraph.DriveItem\x12\x10\n\x08root_dir\x18\x02 \x01(\t\x12\"\n\x1alast_visited_drive_item_id\x18\x03 \x01(\t\x12\x16\n\x0ehas_more_items\x18\x04 \x01(\x08\x12\x1e\n\x16is_file_structure_flat\x18\x05 \x01(\x08\"\xa2\x02\n\x15RestoreFilesUpdateArg\x12\x0f\n\x07web_url\x18\x01 \x01(\t\x12R\n\x17restore_disk_update_arg\x18\x02 \x01(\x0b\x32\x31.cohesity.magneto.slave.stub.RestoreDiskUpdateArg\x12\x1a\n\x12\x65rrors_encountered\x18\x03 \x01(\x03\x12G\n\x10\x65rrored_file_vec\x18\x04 \x03(\x0b\x32-.cohesity.magneto.MSGraph.O365ErroredFileInfo\x12?\n\x10o365_error_proto\x18\x05 \x01(\x0b\x32%.cohesity.magneto.o365.O365ErrorProto\"\x1c\n\x1a\x45ndRestoreSubTaskUpdateArg\"\x15\n\x13\x45ndRestoreUpdateArg\"\xc0\r\n\x17OneDriveActionUpdateArg\x12Q\n\x04type\x18\x01 \x01(\x0e\x32\x43.cohesity.magneto.slave.stub.one_drive.OneDriveActionUpdateArg.Type\x12r\n#prepare_one_drive_backup_update_arg\x18\x02 \x01(\x0b\x32\x45.cohesity.magneto.slave.stub.one_drive.PrepareOneDriveBackupUpdateArg\x12X\n\x15setup_info_update_arg\x18\x03 \x01(\x0b\x32\x39.cohesity.magneto.slave.stub.one_drive.SetupInfoUpdateArg\x12\\\n\x17\x62\x61\x63kup_files_update_arg\x18\x04 \x01(\x0b\x32;.cohesity.magneto.slave.stub.one_drive.BackupFilesUpdateArg\x12g\n\x1d\x63hunk_backup_files_update_arg\x18\r \x01(\x0b\x32@.cohesity.magneto.slave.stub.one_drive.ChunkBackupFilesUpdateArg\x12l\n end_metadata_sub_task_update_arg\x18\x06 \x01(\x0b\x32\x42.cohesity.magneto.slave.stub.one_drive.EndMetadataSubTaskUpdateArg\x12\x64\n\x1c\x65nd_data_sub_task_update_arg\x18\x07 \x01(\x0b\x32>.cohesity.magneto.slave.stub.one_drive.EndDataSubTaskUpdateArg\x12X\n\x15\x65nd_backup_update_arg\x18\x08 \x01(\x0b\x32\x39.cohesity.magneto.slave.stub.one_drive.EndBackupUpdateArg\x12]\n\x18read_dir_info_update_arg\x18\t \x01(\x0b\x32;.cohesity.magneto.slave.stub.one_drive.ReadDirInfoUpdateArg\x12^\n\x18restore_files_update_arg\x18\n \x01(\x0b\x32<.cohesity.magneto.slave.stub.one_drive.RestoreFilesUpdateArg\x12j\n\x1f\x65nd_restore_sub_task_update_arg\x18\x0b \x01(\x0b\x32\x41.cohesity.magneto.slave.stub.one_drive.EndRestoreSubTaskUpdateArg\x12Z\n\x16\x65nd_restore_update_arg\x18\x0c \x01(\x0b\x32:.cohesity.magneto.slave.stub.one_drive.EndRestoreUpdateArg\x12<\n\x0eoperation_info\x18\x0e \x01(\x0b\x32$.cohesity.magneto.o365.OperationInfo\"\xaf\x02\n\x04Type\x12 \n\x1ckPrepareOneDriveBackupUpdate\x10\x01\x12\x14\n\x10kSetupInfoUpdate\x10\x02\x12\x16\n\x12kBackupFilesUpdate\x10\x03\x12\x1d\n\x19kEndMetadataSubTaskUpdate\x10\x05\x12\x19\n\x15kEndDataSubTaskUpdate\x10\x06\x12\x14\n\x10kEndBackupUpdate\x10\x07\x12\x1b\n\x17kChunkBackupFilesUpdate\x10\x0c\x12\x16\n\x12kReadDirInfoUpdate\x10\x08\x12\x17\n\x13kRestoreFilesUpdate\x10\t\x12\x1c\n\x18kEndRestoreSubTaskUpdate\x10\n\x12\x15\n\x11kEndRestoreUpdate\x10\x0b\"\x04\x08\x04\x10\x04\x32\x91\x01\n\x1bone_drive_action_update_arg\x12,.cohesity.magneto.slave.stub.ActionUpdateArg\x18u \x01(\x0b\x32>.cohesity.magneto.slave.stub.one_drive.OneDriveActionUpdateArgJ\x04\x08\x05\x10\x06')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.slave.stub.one_drive_stub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREPAREONEDRIVEBACKUPUPDATEARG']._serialized_start=273
  _globals['_PREPAREONEDRIVEBACKUPUPDATEARG']._serialized_end=382
  _globals['_SETUPINFOUPDATEARG']._serialized_start=385
  _globals['_SETUPINFOUPDATEARG']._serialized_end=951
  _globals['_BACKUPFILESUPDATEARG']._serialized_start=954
  _globals['_BACKUPFILESUPDATEARG']._serialized_end=1962
  _globals['_BACKUPFILESUPDATEARG_TASKSTATS']._serialized_start=1657
  _globals['_BACKUPFILESUPDATEARG_TASKSTATS']._serialized_end=1962
  _globals['_BACKUPFILESUPDATEARG_TASKSTATS_ERROREDITEMINFO']._serialized_start=1866
  _globals['_BACKUPFILESUPDATEARG_TASKSTATS_ERROREDITEMINFO']._serialized_end=1962
  _globals['_CHUNKBACKUPFILESUPDATEARG']._serialized_start=1964
  _globals['_CHUNKBACKUPFILESUPDATEARG']._serialized_end=1991
  _globals['_ENDMETADATASUBTASKUPDATEARG']._serialized_start=1993
  _globals['_ENDMETADATASUBTASKUPDATEARG']._serialized_end=2022
  _globals['_ENDDATASUBTASKUPDATEARG']._serialized_start=2024
  _globals['_ENDDATASUBTASKUPDATEARG']._serialized_end=2049
  _globals['_ENDBACKUPUPDATEARG']._serialized_start=2051
  _globals['_ENDBACKUPUPDATEARG']._serialized_end=2158
  _globals['_READDIRINFOUPDATEARG']._serialized_start=2161
  _globals['_READDIRINFOUPDATEARG']._serialized_end=2354
  _globals['_RESTOREFILESUPDATEARG']._serialized_start=2357
  _globals['_RESTOREFILESUPDATEARG']._serialized_end=2647
  _globals['_ENDRESTORESUBTASKUPDATEARG']._serialized_start=2649
  _globals['_ENDRESTORESUBTASKUPDATEARG']._serialized_end=2677
  _globals['_ENDRESTOREUPDATEARG']._serialized_start=2679
  _globals['_ENDRESTOREUPDATEARG']._serialized_end=2700
  _globals['_ONEDRIVEACTIONUPDATEARG']._serialized_start=2703
  _globals['_ONEDRIVEACTIONUPDATEARG']._serialized_end=4431
  _globals['_ONEDRIVEACTIONUPDATEARG_TYPE']._serialized_start=3974
  _globals['_ONEDRIVEACTIONUPDATEARG_TYPE']._serialized_end=4277
# @@protoc_insertion_point(module_scope)