# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bridge/magneto/sql/sql_actions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bridge.magneto.base import magneto_actions_pb2 as bridge_dot_magneto_dot_base_dot_magneto__actions__pb2
from magneto.base.entities import sql_pb2 as magneto_dot_base_dot_entities_dot_sql__pb2
from magneto.base import entity_pb2 as magneto_dot_base_dot_entity__pb2
from magneto.base import enums_pb2 as magneto_dot_base_dot_enums__pb2
from magneto.base import magneto_pb2 as magneto_dot_base_dot_magneto__pb2
try:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto_dot_base_dot_env__params__pb2
except AttributeError:
  magneto_dot_base_dot_env__params__pb2 = magneto_dot_base_dot_magneto__pb2.magneto.base.env_params_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$bridge/magneto/sql/sql_actions.proto\x12\x1b\x63ohesity.bridge.magneto.sql\x1a)bridge/magneto/base/magneto_actions.proto\x1a\x1fmagneto/base/entities/sql.proto\x1a\x19magneto/base/entity.proto\x1a\x18magneto/base/enums.proto\x1a\x1amagneto/base/magneto.proto\"}\n\tAgentInfo\x12;\n\x10\x63onnector_params\x18\x01 \x01(\x0b\x32!.cohesity.magneto.ConnectorParams\x12\x15\n\ragent_version\x18\x02 \x01(\x03\x12\x1c\n\x14\x61gent_incarnation_id\x18\x03 \x01(\x03\"V\n\x0eStreamIOParams\x12\x11\n\tstream_id\x18\x01 \x01(\x03\x12\x15\n\rstream_offset\x18\x02 \x01(\x03\x12\x1a\n\x12stream_data_length\x18\x03 \x01(\x03\"\xdc\x01\n\x12MigrateHostViewArg\x12\x12\n\x06job_id\x18\x01 \x01(\x03:\x02-1\x12\x1b\n\x0fjob_instance_id\x18\x02 \x01(\x03:\x02-1\x12\x17\n\x0b\x61ttempt_num\x18\x03 \x01(\x05:\x02-1\x12\x13\n\x0bview_box_id\x18\x04 \x01(\x03\x12\x18\n\x10source_view_name\x18\x05 \x01(\t\x12\x16\n\x0e\x64\x65st_view_name\x18\x06 \x01(\t\x12\x19\n\x11\x64\x65st_snapshot_dir\x18\x07 \x01(\t\x12\x1a\n\x12qos_principal_name\x18\x08 \x01(\t\"\xc2\x01\n\x1cPopulateNativeRestoreViewArg\x12\x13\n\x0bview_box_id\x18\x01 \x01(\x03\x12\x15\n\rsrc_view_name\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x65st_view_name\x18\x03 \x01(\t\x12\x18\n\x10src_snapshot_dir\x18\x04 \x01(\t\x12\x1c\n\x14\x62\x61\x63kup_file_name_vec\x18\x05 \x03(\t\x12&\n\x1eview_whitelist_ip_addr_str_vec\x18\x06 \x03(\t\"\xc2\x01\n\x1b\x43lonePreviousBackupFilesArg\x12\x12\n\x06job_id\x18\x01 \x01(\x03:\x02-1\x12\x1b\n\x0fjob_instance_id\x18\x02 \x01(\x03:\x02-1\x12\x11\n\troot_path\x18\x03 \x01(\t\x12\x1d\n\x15relative_snapshot_dir\x18\x04 \x01(\t\x12\"\n\x1arelative_prev_snapshot_dir\x18\x05 \x01(\t\x12\x1c\n\x14\x62\x61\x63kup_file_name_vec\x18\x06 \x03(\t\"\xa9\x05\n\x0fSqlLogBackupArg\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.cohesity.bridge.magneto.sql.SqlLogBackupArg.Type\x12\x30\n\x0b\x64\x61tabase_id\x18\x02 \x01(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x13\n\x0bview_box_id\x18\x03 \x01(\x03\x12\x11\n\tview_name\x18\x0c \x01(\t\x12\x1a\n\x12qos_principal_name\x18\r \x01(\t\x12\x0e\n\x06job_id\x18\x04 \x01(\x03\x12\x17\n\x0fjob_instance_id\x18\x05 \x01(\x03\x12\x13\n\x0b\x61ttempt_num\x18\x06 \x01(\x05\x12\x32\n\x0broot_entity\x18\x07 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x34\n\rsource_entity\x18\x08 \x01(\x0b\x32\x1d.cohesity.magneto.EntityProto\x12\x11\n\tfile_name\x18\t \x01(\t\x12>\n\tio_params\x18\n \x01(\x0b\x32+.cohesity.bridge.magneto.sql.StreamIOParams\x12\x1e\n\x12stats_container_id\x18\x0b \x01(\x03:\x02-1\x12\x11\n\troot_path\x18\x0e \x01(\t\x12\x1d\n\x15relative_snapshot_dir\x18\x0f \x01(\t\x12\x15\n\rdatabase_name\x18\x10 \x01(\t\x12\x16\n\ncluster_id\x18\x11 \x01(\x03:\x02-1\x12\"\n\x16\x63luster_incarnation_id\x18\x12 \x01(\x03:\x02-1\"?\n\x04Type\x12\x15\n\x11kPrepareLogBackup\x10\x01\x12\r\n\tkReadData\x10\x02\x12\x11\n\rkEndLogBackup\x10\x03\"Q\n\x0fWriteSqlDataArg\x12>\n\tio_params\x18\x01 \x01(\x0b\x32+.cohesity.bridge.magneto.sql.StreamIOParams\"*\n\x11\x43\x61ncelStreamIOArg\x12\x15\n\rstream_id_vec\x18\x01 \x03(\x03\"\x9a\x04\n\x0fSqlLogReplayArg\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.cohesity.bridge.magneto.sql.SqlLogReplayArg.Type\x12\x44\n\x0fsource_env_type\x18\x07 \x01(\x0e\x32\".cohesity.magneto.Environment.Type:\x07kVMware\x12\x30\n\x0b\x64\x61tabase_id\x18\x02 \x01(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x13\n\x0bview_box_id\x18\x03 \x01(\x03\x12\x11\n\tview_name\x18\x04 \x01(\t\x12\x18\n\x10source_view_name\x18\x08 \x01(\t\x12\x11\n\tfile_path\x18\x05 \x01(\t\x12\x17\n\x0ftarget_dir_name\x18\t \x01(\t\x12>\n\tio_params\x18\x06 \x01(\x0b\x32+.cohesity.bridge.magneto.sql.StreamIOParams\x12\x11\n\troot_path\x18\n \x01(\t\x12\x16\n\ncluster_id\x18\x0b \x01(\x03:\x02-1\x12\"\n\x16\x63luster_incarnation_id\x18\x0c \x01(\x03:\x02-1\"Q\n\x04Type\x12\x15\n\x11kPrepareLogReplay\x10\x01\x12\x0e\n\nkWriteData\x10\x02\x12\x11\n\rkEndLogReplay\x10\x03\x12\x0f\n\x0bkDeleteView\x10\x04\"\x8d\x06\n\x0cSqlActionArg\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12:\n\nagent_info\x18\x02 \x01(\x0b\x32&.cohesity.bridge.magneto.sql.AgentInfo\x12H\n\x12sql_log_backup_arg\x18\x03 \x01(\x0b\x32,.cohesity.bridge.magneto.sql.SqlLogBackupArg\x12H\n\x12write_sql_data_arg\x18\x04 \x01(\x0b\x32,.cohesity.bridge.magneto.sql.WriteSqlDataArg\x12L\n\x14\x63\x61ncel_stream_io_arg\x18\x05 \x01(\x0b\x32..cohesity.bridge.magneto.sql.CancelStreamIOArg\x12H\n\x12sql_log_replay_arg\x18\x06 \x01(\x0b\x32,.cohesity.bridge.magneto.sql.SqlLogReplayArg\x12N\n\x15migrate_host_view_arg\x18\x07 \x01(\x0b\x32/.cohesity.bridge.magneto.sql.MigrateHostViewArg\x12\x63\n populate_native_restore_view_arg\x18\x08 \x01(\x0b\x32\x39.cohesity.bridge.magneto.sql.PopulateNativeRestoreViewArg\x12\x61\n\x1f\x63lone_previous_backup_files_arg\x18\t \x01(\x0b\x32\x38.cohesity.bridge.magneto.sql.ClonePreviousBackupFilesArg2l\n\x0esql_action_arg\x12).cohesity.bridge.magneto.ExecuteActionArg\x18\x65 \x01(\x0b\x32).cohesity.bridge.magneto.sql.SqlActionArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bridge.magneto.sql.sql_actions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AGENTINFO']._serialized_start=226
  _globals['_AGENTINFO']._serialized_end=351
  _globals['_STREAMIOPARAMS']._serialized_start=353
  _globals['_STREAMIOPARAMS']._serialized_end=439
  _globals['_MIGRATEHOSTVIEWARG']._serialized_start=442
  _globals['_MIGRATEHOSTVIEWARG']._serialized_end=662
  _globals['_POPULATENATIVERESTOREVIEWARG']._serialized_start=665
  _globals['_POPULATENATIVERESTOREVIEWARG']._serialized_end=859
  _globals['_CLONEPREVIOUSBACKUPFILESARG']._serialized_start=862
  _globals['_CLONEPREVIOUSBACKUPFILESARG']._serialized_end=1056
  _globals['_SQLLOGBACKUPARG']._serialized_start=1059
  _globals['_SQLLOGBACKUPARG']._serialized_end=1740
  _globals['_SQLLOGBACKUPARG_TYPE']._serialized_start=1677
  _globals['_SQLLOGBACKUPARG_TYPE']._serialized_end=1740
  _globals['_WRITESQLDATAARG']._serialized_start=1742
  _globals['_WRITESQLDATAARG']._serialized_end=1823
  _globals['_CANCELSTREAMIOARG']._serialized_start=1825
  _globals['_CANCELSTREAMIOARG']._serialized_end=1867
  _globals['_SQLLOGREPLAYARG']._serialized_start=1870
  _globals['_SQLLOGREPLAYARG']._serialized_end=2408
  _globals['_SQLLOGREPLAYARG_TYPE']._serialized_start=2327
  _globals['_SQLLOGREPLAYARG_TYPE']._serialized_end=2408
  _globals['_SQLACTIONARG']._serialized_start=2411
  _globals['_SQLACTIONARG']._serialized_end=3192
# @@protoc_insertion_point(module_scope)
