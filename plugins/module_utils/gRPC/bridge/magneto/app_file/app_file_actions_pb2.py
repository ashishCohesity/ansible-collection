# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/app_file/app_file_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from configs import cluster_config_pb2 as configs_dot_cluster__config__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2
from magneto.connectors.app_file import app_file_pb2 as magneto_dot_connectors_dot_app__file_dot_app__file__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.bridge/magneto/app_file/app_file_actions.proto\x12 cohesity.bridge.magneto.app_file\x1a)bridge/magneto/base/magneto_actions.proto\x1a\x1c\x63onfigs/cluster_config.proto\x1a\x19magneto/base/entity.proto\x1a\x1amagneto/base/magneto.proto\x1a*magneto/connectors/app_file/app_file.proto\"\xa6\x05\n\x11\x42\x61\x63kupAppFilesArg\x12\x34\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32&.cohesity.bridge.magneto.BackupBaseArg\x12\x46\n\x04type\x18\x02 \x01(\x0e\x32\x38.cohesity.bridge.magneto.app_file.BackupAppFilesArg.Type\x12\x32\n\x0broot_entity\x18\x03 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x34\n\rsource_entity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12L\n\x17\x61pp_file_group_info_vec\x18\x05 \x03(\x0b\x32+.cohesity.magneto.app_file.AppFileGroupInfo\x12\x1c\n\x14\x63ommon_host_dir_name\x18\x06 \x01(\t\x12!\n\x12perform_dedup_read\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x14min_dedup_chunk_size\x18\x08 \x01(\x05\x12\x1c\n\x14max_dedup_chunk_size\x18\t \x01(\x05\x12\x1c\n\x14non_dedup_chunk_size\x18\n \x01(\x05\x12\x16\n\ncluster_id\x18\x0c \x01(\x03:\x02-1\x12\"\n\x16\x63luster_incarnation_id\x18\r \x01(\x03:\x02-1\x12&\n\x18\x65nable_file_handle_cache\x18\x0e \x01(\x08:\x04true\"\\\n\x04Type\x12\x12\n\x0ekPrepareBackup\x10\x01\x12\x0f\n\x0bkSetupFiles\x10\x02\x12\x0f\n\x0bkBackupFile\x10\x03\x12\x0e\n\nkCloseFile\x10\x04\x12\x0e\n\nkEndBackup\x10\x05\"\xfc\x05\n\x12RestoreAppFilesArg\x12G\n\x04type\x18\x01 \x01(\x0e\x32\x39.cohesity.bridge.magneto.app_file.RestoreAppFilesArg.Type\x12u\n\x1f\x61pp_file_group_restore_info_vec\x18\x02 \x03(\x0b\x32L.cohesity.bridge.magneto.app_file.RestoreAppFilesArg.AppFileGroupRestoreInfo\x12\x13\n\x0bview_box_id\x18\x03 \x01(\x03\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\x13\n\x0b\x63reate_view\x18\x05 \x01(\x08\x12\x18\n\x10is_internal_view\x18\x06 \x01(\x08\x12\x13\n\x0bpath_prefix\x18\x07 \x01(\t\x12&\n\x1eview_whitelist_ip_addr_str_vec\x18\x08 \x03(\t\x12Q\n\x1cview_whitelist_ip_ranges_vec\x18\r \x03(\x0b\x32+.cohesity.configs.ClusterConfigProto.Subnet\x12\x1c\n\x14use_non_atomic_clone\x18\x0e \x01(\x08\x1a\xef\x01\n\x17\x41ppFileGroupRestoreInfo\x12\x11\n\tview_name\x18\x01 \x01(\t\x12\"\n\x1asnapshot_relative_dir_path\x18\x02 \x01(\t\x12\x16\n\x0egroup_dir_name\x18\x03 \x01(\t\x12(\n\x1a\x63reate_directory_per_group\x18\x05 \x01(\x08:\x04true\x12\x34\n\rsource_entity\x18\x04 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12%\n\x1d\x64\x65lete_file_relative_path_vec\x18\x06 \x03(\t\"/\n\x04Type\x12\x12\n\x0ekCloneAppFiles\x10\x01\x12\x13\n\x0fkDeleteAppFiles\x10\x02\"\xa5\x03\n\x10\x41ppFileActionArg\x12\x13\n\x07task_id\x18\x01 \x01(\x03:\x02-1\x12\x17\n\x0bsub_task_id\x18\x02 \x01(\x03:\x02-1\x12Q\n\x14\x62\x61\x63kup_app_files_arg\x18\x03 \x01(\x0b\x32\x33.cohesity.bridge.magneto.app_file.BackupAppFilesArg\x12S\n\x15restore_app_files_arg\x18\x04 \x01(\x0b\x32\x34.cohesity.bridge.magneto.app_file.RestoreAppFilesArg\x12?\n\x0f\x63\x61ncel_task_arg\x18\x05 \x01(\x0b\x32&.cohesity.bridge.magneto.CancelTaskArg2z\n\x13\x61pp_file_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18q \x01(\x0b\x32\x32.cohesity.bridge.magneto.app_file.AppFileActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.app_file.app_file_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BACKUPAPPFILESARG']._serialized_start=257
  _globals['_BACKUPAPPFILESARG']._serialized_end=935
  _globals['_BACKUPAPPFILESARG_TYPE']._serialized_start=843
  _globals['_BACKUPAPPFILESARG_TYPE']._serialized_end=935
  _globals['_RESTOREAPPFILESARG']._serialized_start=938
  _globals['_RESTOREAPPFILESARG']._serialized_end=1702
  _globals['_RESTOREAPPFILESARG_APPFILEGROUPRESTOREINFO']._serialized_start=1414
  _globals['_RESTOREAPPFILESARG_APPFILEGROUPRESTOREINFO']._serialized_end=1653
  _globals['_RESTOREAPPFILESARG_TYPE']._serialized_start=1655
  _globals['_RESTOREAPPFILESARG_TYPE']._serialized_end=1702
  _globals['_APPFILEACTIONARG']._serialized_start=1705
  _globals['_APPFILEACTIONARG']._serialized_end=2126
# @@protoc_insertion_point(module_scope)
