# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/outlook/outlook_actions.proto
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
from magneto.connectors.outlook import outlook_param_pb2 as magneto_dot_connectors_dot_outlook_dot_outlook__param__pb2
from magneto.connectors.outlook import outlook_pb2 as magneto_dot_connectors_dot_outlook_dot_outlook__pb2
from magneto.connectors.o365 import o365_pb2 as magneto_dot_connectors_dot_o365_dot_o365__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,bridge/magneto/outlook/outlook_actions.proto\x12\x1f\x63ohesity.bridge.magneto.outlook\x1a)bridge/magneto/base/magneto_actions.proto\x1a magneto/base/entities/o365.proto\x1a.magneto/connectors/outlook/outlook_param.proto\x1a(magneto/connectors/outlook/outlook.proto\x1a\"magneto/connectors/o365/o365.proto\"3\n\x11PrepareBackupInfo\x12\x1e\n\x16skip_directory_cloning\x18\x01 \x01(\x08\"\xbb\x01\n\x18PrepareOutlookBackupInfo\x12\x1c\n\x14view_cloning_enabled\x18\x01 \x01(\x08\x12$\n\x1cshould_recursively_clone_dir\x18\x02 \x01(\x08\x12!\n\x19\x64\x65lete_entire_mailbox_dir\x18\x03 \x01(\x08\x12\x19\n\x11\x64ir_to_be_renamed\x18\x04 \x01(\t\x12\x1d\n\x15\x66irst_time_view_clone\x18\x05 \x01(\x08\"\xb5\x01\n\x15\x43opyFailedFoldersInfo\x12]\n\x12\x66\x61iled_folders_vec\x18\x01 \x03(\x0b\x32\x41.cohesity.bridge.magneto.outlook.CopyFailedFoldersInfo.FolderInfo\x1a=\n\nFolderInfo\x12\x1a\n\x12\x66ull_snapshot_path\x18\x01 \x01(\t\x12\x13\n\x0b\x66older_uuid\x18\x02 \x01(\t\"\xcd\x01\n\tSetupInfo\x12\x42\n\x0f\x66older_info_vec\x18\x01 \x03(\x0b\x32).cohesity.magneto.outlook.SetupFolderInfo\x12]\n\x19incremental_fh_change_vec\x18\x02 \x03(\x0b\x32:.cohesity.magneto.outlook.IncrementalFolderHierarchyChange\x12\x1d\n\x15is_incremental_backup\x18\x03 \x01(\x08\"\xf1\x04\n\nBackupInfo\x12\x12\n\nmailbox_id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12>\n\nchange_vec\x18\x03 \x03(\x0b\x32*.cohesity.magneto.outlook.FolderItemChange\x12\"\n\x1aitem_metadata_presence_vec\x18\x04 \x03(\x08\x12\x1e\n\x16item_body_presence_vec\x18\x05 \x03(\x08\x12\x1a\n\x12\x66lush_after_backup\x18\x06 \x01(\x08\x12\x12\n\nsync_state\x18\x07 \x01(\t\x12_\n%already_fetched_folder_changes_result\x18\x08 \x01(\x0b\x32\x30.cohesity.magneto.outlook.GetFolderChangesResult\x12\x1d\n\x15is_incremental_backup\x18\t \x01(\x08\x12\x1f\n\x17incremental_file_offset\x18\n \x01(\x03\x12\x1d\n\x15is_first_backup_batch\x18\x0b \x01(\x08\x12\x13\n\x0bgroup_owner\x18\x0c \x01(\t\x12X\n\x12public_folder_info\x18\x0e \x01(\x0b\x32<.cohesity.bridge.magneto.outlook.BackupInfo.PublicFolderInfo\x1aS\n\x10PublicFolderInfo\x12\x1d\n\x15public_folder_mailbox\x18\x01 \x01(\t\x12 \n\x18public_folder_mailbox_id\x18\x02 \x01(\tJ\x04\x08\r\x10\x0e\"\xac\x02\n\x0e\x45ndSubTaskInfo\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x15\n\rrelative_path\x18\x02 \x01(\t\x12\x1f\n\x17\x63\x61lculate_sub_task_stat\x18\x03 \x01(\x08\x12\"\n\x1aperform_rocksdb_validation\x18\x04 \x01(\x08\x12\x18\n\x10is_public_folder\x18\x05 \x01(\x08\x12!\n\x19write_folder_content_info\x18\x06 \x01(\x08\x12\x12\n\nmailbox_id\x18\x07 \x01(\t\x12\x12\n\nsync_state\x18\x08 \x01(\t\x12\x1a\n\x12\x63leanup_on_failure\x18\t \x01(\x08\x12*\n\x1crequires_end_externalization\x18\n \x01(\x08:\x04true\"p\n\rEndBackupInfo\x12\x1f\n\x17\x66orce_write_config_file\x18\x01 \x01(\x08\x12\"\n\x1aremove_failed_attempt_dirs\x18\x02 \x01(\x08\x12\x1a\n\x12\x63leanup_on_failure\x18\x03 \x01(\x08\"\xda\t\n\x10\x42\x61\x63kupOutlookArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12\x44\n\x04type\x18\x02 \x01(\x0e\x32\x36.cohesity.bridge.magneto.outlook.BackupOutlookArg.Type\x12\x32\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12\x35\n\x0emailbox_entity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12>\n\nsetup_info\x18\x05 \x01(\x0b\x32*.cohesity.bridge.magneto.outlook.SetupInfo\x12@\n\x0b\x62\x61\x63kup_info\x18\x06 \x01(\x0b\x32+.cohesity.bridge.magneto.outlook.BackupInfo\x12I\n\x10\x65nd_subtask_info\x18\x07 \x01(\x0b\x32/.cohesity.bridge.magneto.outlook.EndSubTaskInfo\x12\x45\n\x0emailbox_config\x18\x08 \x01(\x0b\x32-.cohesity.magneto.outlook.SparseMailboxConfig\x12\x1f\n\x11write_config_file\x18\t \x01(\x08:\x04true\x12O\n\x13prepare_backup_info\x18\n \x01(\x0b\x32\x32.cohesity.bridge.magneto.outlook.PrepareBackupInfo\x12^\n\x1bprepare_outlook_backup_info\x18\x0b \x01(\x0b\x32\x39.cohesity.bridge.magneto.outlook.PrepareOutlookBackupInfo\x12$\n\x1cis_sent_from_o365_mailbox_op\x18\x0c \x01(\x08\x12\x44\n\x0f\x62\x61\x63kup_info_vec\x18\r \x03(\x0b\x32+.cohesity.bridge.magneto.outlook.BackupInfo\x12X\n\x18\x63opy_failed_folders_info\x18\x0e \x01(\x0b\x32\x36.cohesity.bridge.magneto.outlook.CopyFailedFoldersInfo\x12G\n\x0f\x65nd_backup_info\x18\x0f \x01(\x0b\x32..cohesity.bridge.magneto.outlook.EndBackupInfo\x12\x1d\n\x15outlook_config_absent\x18\x10 \x01(\x08\x12\x1a\n\x12record_error_in_db\x18\x11 \x01(\x08\"\xae\x01\n\x04Type\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x11\n\rkSetupFolders\x10\x02\x12\x10\n\x0ckBackupItems\x10\x03\x12\x0f\n\x0bkEndSubTask\x10\x04\x12\x0e\n\nkEndBackup\x10\x05\x12\x15\n\x11kFetchBackupItems\x10\x06\x12\x1d\n\x19kEnhancedFetchBackupItems\x10\x07\x12\x16\n\x12kCopyFailedFolders\x10\x08\"_\n\x0bMailboxInfo\x12\x19\n\x11src_relative_path\x18\x01 \x01(\t\x12\x35\n\x0emailbox_entity\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\"\xe8\x03\n\x0bRestoreInfo\x12\x19\n\x11src_relative_path\x18\x01 \x01(\t\x12\x39\n\x12src_mailbox_entity\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12\x15\n\rsrc_folder_id\x18\x03 \x01(\t\x12\x13\n\x0bitem_id_vec\x18\x04 \x03(\t\x12\x18\n\x10last_restore_key\x18\x05 \x01(\t\x12:\n\x13\x64\x65st_mailbox_entity\x18\x06 \x01(\x0b\x32\x1d.cohesity.magneto.o365.Entity\x12\x16\n\x0e\x64\x65st_folder_id\x18\x07 \x01(\t\x12\x13\n\x0bview_box_id\x18\x08 \x01(\x03\x12\x15\n\rsrc_root_path\x18\t \x01(\t\x12\x12\n\nmailbox_id\x18\n \x01(\t\x12\x1d\n\x15public_folder_mailbox\x18\x0b \x01(\t\x12\x18\n\x10\x63opy_to_pst_view\x18\x0c \x01(\x08\x12$\n\x1c\x66ull_folder_path_on_pst_view\x18\r \x01(\t\x12\x13\n\x0b\x66older_path\x18\x0e \x01(\t\x12\x19\n\x11\x63ontinue_on_error\x18\x0f \x01(\x08\x12\x1a\n\x12group_smtp_address\x18\x10 \x01(\t\"\xed\x03\n\x11RestoreOutlookArg\x12\x35\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\'.cohesity.bridge.magneto.RestoreBaseArg\x12\x45\n\x04type\x18\x02 \x01(\x0e\x32\x37.cohesity.bridge.magneto.outlook.RestoreOutlookArg.Type\x12\x19\n\x11src_root_path_vec\x18\x03 \x03(\t\x12\x46\n\x10mailbox_info_vec\x18\x04 \x03(\x0b\x32,.cohesity.bridge.magneto.outlook.MailboxInfo\x12\x42\n\x0crestore_info\x18\x05 \x01(\x0b\x32,.cohesity.bridge.magneto.outlook.RestoreInfo\x12I\n\x10\x65nd_subtask_info\x18\x06 \x01(\x0b\x32/.cohesity.bridge.magneto.outlook.EndSubTaskInfo\x12\x16\n\x0eis_alt_restore\x18\x07 \x01(\x08\"P\n\x04Type\x12\x13\n\x0fkGetMailboxInfo\x10\x01\x12\x11\n\rkRestoreItems\x10\x02\x12\x0f\n\x0bkEndSubTask\x10\x03\x12\x0f\n\x0bkEndRestore\x10\x04\"\x87\x01\n\rCancelTaskArg\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x1d\n\x15wait_for_cancellation\x18\x03 \x01(\x08\x12!\n\x19\x64\x65\x61\x64_slave_constituent_id\x18\x04 \x01(\x03\x12!\n\x19\x64\x65\x61\x64_slave_incarnation_id\x18\x05 \x01(\x03\"\xdd\x03\n\x10OutlookActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12M\n\x12\x62\x61\x63kup_outlook_arg\x18\x03 \x01(\x0b\x32\x31.cohesity.bridge.magneto.outlook.BackupOutlookArg\x12O\n\x13restore_outlook_arg\x18\x04 \x01(\x0b\x32\x32.cohesity.bridge.magneto.outlook.RestoreOutlookArg\x12G\n\x0f\x63\x61ncel_task_arg\x18\x05 \x01(\x0b\x32..cohesity.bridge.magneto.outlook.CancelTaskArg\x12<\n\x0eoperation_info\x18\x06 \x01(\x0b\x32$.cohesity.magneto.o365.OperationInfo2x\n\x12outlook_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18s \x01(\x0b\x32\x31.cohesity.bridge.magneto.outlook.OutlookActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.outlook.outlook_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREPAREBACKUPINFO']._serialized_start=284
  _globals['_PREPAREBACKUPINFO']._serialized_end=335
  _globals['_PREPAREOUTLOOKBACKUPINFO']._serialized_start=338
  _globals['_PREPAREOUTLOOKBACKUPINFO']._serialized_end=525
  _globals['_COPYFAILEDFOLDERSINFO']._serialized_start=528
  _globals['_COPYFAILEDFOLDERSINFO']._serialized_end=709
  _globals['_COPYFAILEDFOLDERSINFO_FOLDERINFO']._serialized_start=648
  _globals['_COPYFAILEDFOLDERSINFO_FOLDERINFO']._serialized_end=709
  _globals['_SETUPINFO']._serialized_start=712
  _globals['_SETUPINFO']._serialized_end=917
  _globals['_BACKUPINFO']._serialized_start=920
  _globals['_BACKUPINFO']._serialized_end=1545
  _globals['_BACKUPINFO_PUBLICFOLDERINFO']._serialized_start=1456
  _globals['_BACKUPINFO_PUBLICFOLDERINFO']._serialized_end=1539
  _globals['_ENDSUBTASKINFO']._serialized_start=1548
  _globals['_ENDSUBTASKINFO']._serialized_end=1848
  _globals['_ENDBACKUPINFO']._serialized_start=1850
  _globals['_ENDBACKUPINFO']._serialized_end=1962
  _globals['_BACKUPOUTLOOKARG']._serialized_start=1965
  _globals['_BACKUPOUTLOOKARG']._serialized_end=3207
  _globals['_BACKUPOUTLOOKARG_TYPE']._serialized_start=3033
  _globals['_BACKUPOUTLOOKARG_TYPE']._serialized_end=3207
  _globals['_MAILBOXINFO']._serialized_start=3209
  _globals['_MAILBOXINFO']._serialized_end=3304
  _globals['_RESTOREINFO']._serialized_start=3307
  _globals['_RESTOREINFO']._serialized_end=3795
  _globals['_RESTOREOUTLOOKARG']._serialized_start=3798
  _globals['_RESTOREOUTLOOKARG']._serialized_end=4291
  _globals['_RESTOREOUTLOOKARG_TYPE']._serialized_start=4211
  _globals['_RESTOREOUTLOOKARG_TYPE']._serialized_end=4291
  _globals['_CANCELTASKARG']._serialized_start=4294
  _globals['_CANCELTASKARG']._serialized_end=4429
  _globals['_OUTLOOKACTIONARG']._serialized_start=4432
  _globals['_OUTLOOKACTIONARG']._serialized_end=4909
# @@protoc_insertion_point(module_scope)
