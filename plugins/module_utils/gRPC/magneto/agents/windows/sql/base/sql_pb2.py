# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/agents/windows/sql/base/sql.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from magneto.agents.base import agent_pb2 as magneto_dot_agents_dot_base_dot_agent__pb2
from magneto.agents.base import error_pb2 as magneto_dot_agents_dot_base_dot_error__pb2
from magneto.agents.stub import agent_param_pb2 as magneto_dot_agents_dot_stub_dot_agent__param__pb2
from magneto.agents.windows.base import vss_pb2 as magneto_dot_agents_dot_windows_dot_base_dot_vss__pb2
from magneto.base.entities import sql_pb2 as magneto_dot_base_dot_entities_dot_sql__pb2
from magneto.connectors.sql import sql_pb2 as magneto_dot_connectors_dot_sql_dot_sql__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)magneto/agents/windows/sql/base/sql.proto\x12#cohesity.magneto.agents.windows.sql\x1a\x1fmagneto/agents/base/agent.proto\x1a\x1fmagneto/agents/base/error.proto\x1a%magneto/agents/stub/agent_param.proto\x1a%magneto/agents/windows/base/vss.proto\x1a\x1fmagneto/base/entities/sql.proto\x1a magneto/connectors/sql/sql.proto\".\n\x08\x41uthType\"\"\n\x04Type\x12\x0c\n\x08kAdBased\x10\x00\x12\x0c\n\x08kDbBased\x10\x01\"\xcc\x08\n\x0fSQLDatabaseInfo\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x15\n\rinstance_name\x18\x02 \x01(\x0c\x12\x15\n\rdatabase_name\x18\x03 \x01(\x0c\x12\x46\n\x16\x62\x61\x63kupset_row_info_vec\x18\x04 \x03(\x0b\x32&.cohesity.magneto.sql.BackupSetRowInfo\x12@\n\x0erecovery_model\x18\x06 \x01(\x0e\x32(.cohesity.magneto.sql.RecoveryModel.Type\x12:\n\x05state\x18\x07 \x01(\x0e\x32+.cohesity.magneto.sql.SQLDatabaseState.Type\x12\x19\n\x11state_description\x18\x08 \x01(\t\x12#\n\x1bis_available_for_vss_backup\x18\t \x01(\x08\x12\x16\n\x0eldf_size_bytes\x18\n \x01(\x03\x12\x18\n\x10total_size_bytes\x18\x0b \x01(\x03\x12\x13\n\x0b\x63reate_date\x18\x0c \x01(\t\x12;\n\x08\x66ile_vec\x18\r \x03(\x0b\x32).cohesity.magneto.sql.SQLDatabaseFileInfo\x12;\n\x0e\x66ile_vec_error\x18\x0f \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x12\x1d\n\x15vdi_snapshot_metadata\x18\x0e \x01(\x0c\x12N\n\x18\x64\x61tabase_recovery_status\x18\x10 \x01(\x0b\x32,.cohesity.magneto.sql.DatabaseRecoveryStatus\x12\x16\n\x0e\x64\x61tabase_owner\x18\x11 \x01(\t\x12K\n\x13\x66ile_group_info_vec\x18\x12 \x03(\x0b\x32..cohesity.magneto.sql.SQLDatabaseFileGroupInfo\x12\x1b\n\x13\x63ompatibility_level\x18\x13 \x01(\x03\x12\x11\n\tread_only\x18\x14 \x01(\x08\x12\x1a\n\x12is_database_cloned\x18\x15 \x01(\x08\x12\x17\n\x0fis_fci_database\x18\x16 \x01(\x08\x12%\n\x1dhas_files_on_external_storage\x18\x17 \x01(\x08\x12\x18\n\x10usage_size_bytes\x18\x18 \x01(\x03\x12\x45\n\tauth_type\x18\x19 \x01(\x0e\x32\x32.cohesity.magneto.agents.windows.sql.AuthType.Type\x12\x10\n\x08username\x18\x1a \x01(\t\x12\x10\n\x08password\x18\x1b \x01(\t\x12\x1a\n\x12\x65ncrypted_password\x18\x1c \x01(\x0c\x12\x14\n\x0cis_encrypted\x18\x1d \x01(\x08J\x04\x08\x05\x10\x06\"\xb5\x02\n\x13\x44\x61tabaseRestoreSpec\x12+\n\x06sql_id\x18\x01 \x01(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x15\n\rinstance_name\x18\x02 \x01(\t\x12\x15\n\rdatabase_name\x18\x03 \x01(\t\x12 \n\x18resolve_db_name_conflict\x18\x08 \x01(\x08\x12)\n!grant_full_control_to_these_users\x18\x04 \x03(\t\x12\x18\n\x10use_vdi_snapshot\x18\x05 \x01(\x08\x12\x15\n\rwith_recovery\x18\x06 \x01(\x08\x12\x14\n\x0cno_file_copy\x18\x07 \x01(\x08\x12\x10\n\x08keep_cdc\x18\t \x01(\x08\x12\x1d\n\x0eis_pit_restore\x18\n \x01(\x08:\x05\x66\x61lse\"\xfe\x01\n\x1cSQLFileCopyInstructionFilter\x12?\n\x10\x64\x62_file_type_vec\x18\x01 \x03(\x0e\x32%.cohesity.magneto.sql.DBFileType.Type2\x9c\x01\n\x18\x64\x62_file_copy_instruction\x12\x37.cohesity.magneto.agents.windows.VSSFileCopyInstruction\x18\x64 \x01(\x0b\x32\x41.cohesity.magneto.agents.windows.sql.SQLFileCopyInstructionFilter\"\xea\x03\n\rRestorePolicy\x12Q\n\x0c\x64\x61tabase_vec\x18\x01 \x03(\x0b\x32;.cohesity.magneto.agents.windows.sql.RestorePolicy.Database\x12#\n\x1b\x61ll_databases_with_recovery\x18\x02 \x01(\x08\x12\x1d\n\x11\x61ttach_deprecated\x18\x03 \x01(\x08\x42\x02\x18\x01\x12\x18\n\x0cvdi_snapshot\x18\x05 \x01(\x08\x42\x02\x18\x01\x1a\xa7\x02\n\x08\x44\x61tabase\x12O\n\rdatabase_spec\x18\x01 \x01(\x0b\x32\x38.cohesity.magneto.agents.windows.sql.DatabaseRestoreSpec\x12U\n\x14\x63opy_instruction_vec\x18\x02 \x03(\x0b\x32\x37.cohesity.magneto.agents.windows.VSSFileCopyInstruction\x12\x19\n\rwith_recovery\x18\x03 \x01(\x08\x42\x02\x18\x01\x12X\n\x1b\x64\x62_restore_overwrite_policy\x18\x04 \x01(\x0e\x32\x33.cohesity.magneto.sql.DBRestoreOverwritePolicy.Type\"\xb9\x03\n\x15SQLVSSRestoreProgress\x12Y\n\x0c\x64\x61tabase_vec\x18\x03 \x03(\x0b\x32\x43.cohesity.magneto.agents.windows.sql.SQLVSSRestoreProgress.Database\x12\x10\n\x08\x66inished\x18\x04 \x01(\x08\x12:\n\rrestore_error\x18\x05 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\x1a\xf6\x01\n\x08\x44\x61tabase\x12+\n\x06sql_id\x18\x01 \x01(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x15\n\rdatabase_name\x18\x07 \x01(\t\x12\x34\n\x0foriginal_sql_id\x18\x08 \x01(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x11\n\tnum_files\x18\x02 \x01(\x05\x12\x1b\n\x13num_files_processed\x18\x03 \x01(\x05\x12\x11\n\tnum_bytes\x18\x04 \x01(\x03\x12\x1b\n\x13num_bytes_processed\x18\x05 \x01(\x03\x12\x10\n\x08\x66inished\x18\x06 \x01(\x08\"\x95\x01\n\tSQLParams\x12 \n\x11populate_sql_info\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x34\n\x0f\x64\x61tabase_id_vec\x18\x02 \x03(\x0b\x32\x1b.cohesity.magneto.sql.SqlId\x12\x16\n\x0etrack_file_cbt\x18\x03 \x01(\x08\x12\x18\n\x10use_vdi_snapshot\x18\x04 \x01(\x08\"\xa7\x02\n\rVSSBackupInfo\x12I\n\x0b\x64\x62_info_vec\x18\x01 \x03(\x0b\x32\x34.cohesity.magneto.agents.windows.sql.SQLDatabaseInfo\x12?\n\x10sql_instance_vec\x18\x02 \x03(\x0b\x32%.cohesity.magneto.sql.SQLInstanceInfo2\x89\x01\n\x0fvss_backup_info\x12<.cohesity.magneto.agents.windows.VSSSnapshotSetMetadataProto\x18\x64 \x01(\x0b\x32\x32.cohesity.magneto.agents.windows.sql.VSSBackupInfo\"t\n\rAAGInfoResult\x12/\n\x08\x61\x61g_info\x18\x01 \x01(\x0b\x32\x1d.cohesity.magneto.sql.AAGInfo\x12\x32\n\x05\x65rror\x18\x02 \x01(\x0b\x32#.cohesity.magneto.agents.ErrorProto\"~\n\x1aSQLFileInfoFromVSSSnapshot\x12\x15\n\rfull_filepath\x18\x01 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x02 \x01(\x0c\x12\x15\n\rsnapshot_path\x18\x03 \x01(\t\x12 \n\x18snapshot_file_size_bytes\x18\x04 \x01(\x03\"\x81\x04\n\x0eSQLAppFileInfo\x12X\n\x16xxx_db_info_deprecated\x18\x01 \x03(\x0b\x32\x34.cohesity.magneto.agents.windows.sql.SQLDatabaseInfoB\x02\x18\x01\x12]\n\x0c\x64\x61tabase_vec\x18\x03 \x03(\x0b\x32G.cohesity.magneto.agents.windows.sql.SQLAppFileInfo.DatabaseAppFileInfo\x1a\xbd\x01\n\x13\x44\x61tabaseAppFileInfo\x12\x45\n\x07\x64\x62_info\x18\x01 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.sql.SQLDatabaseInfo\x12_\n\x16\x66ile_snapshot_info_vec\x18\x02 \x03(\x0b\x32?.cohesity.magneto.agents.windows.sql.SQLFileInfoFromVSSSnapshot2p\n\rapp_file_info\x12$.cohesity.magneto.agents.AppFileInfo\x18\x64 \x01(\x0b\x32\x33.cohesity.magneto.agents.windows.sql.SQLAppFileInfoJ\x04\x08\x02\x10\x03\"\x80\x02\n\x0fSQLTopologyNode\x12?\n\x10sql_instance_vec\x18\x01 \x03(\x0b\x32%.cohesity.magneto.sql.SQLInstanceInfo\x12/\n\x08\x61\x61g_info\x18\x02 \x01(\x0b\x32\x1d.cohesity.magneto.sql.AAGInfo2{\n\x11sql_topology_node\x12*.cohesity.magneto.agents.stub.TopologyNode\x18\x64 \x01(\x0b\x32\x34.cohesity.magneto.agents.windows.sql.SQLTopologyNode\"\xdc\x01\n\x11GetSQLTopologyArg\x12\x19\n\x11include_databases\x18\x01 \x01(\x08\x12$\n\x15\x61llow_fqdn_generation\x18\x02 \x01(\x08:\x05\x66\x61lse2\x85\x01\n\x14get_sql_topology_arg\x12/.cohesity.magneto.agents.stub.GetAppTopologyArg\x18\x64 \x01(\x0b\x32\x36.cohesity.magneto.agents.windows.sql.GetSQLTopologyArg')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.agents.windows.sql.base.sql_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_RESTOREPOLICY_DATABASE'].fields_by_name['with_recovery']._loaded_options = None
  _globals['_RESTOREPOLICY_DATABASE'].fields_by_name['with_recovery']._serialized_options = b'\030\001'
  _globals['_RESTOREPOLICY'].fields_by_name['attach_deprecated']._loaded_options = None
  _globals['_RESTOREPOLICY'].fields_by_name['attach_deprecated']._serialized_options = b'\030\001'
  _globals['_RESTOREPOLICY'].fields_by_name['vdi_snapshot']._loaded_options = None
  _globals['_RESTOREPOLICY'].fields_by_name['vdi_snapshot']._serialized_options = b'\030\001'
  _globals['_SQLAPPFILEINFO'].fields_by_name['xxx_db_info_deprecated']._loaded_options = None
  _globals['_SQLAPPFILEINFO'].fields_by_name['xxx_db_info_deprecated']._serialized_options = b'\030\001'
  _globals['_AUTHTYPE']._serialized_start=293
  _globals['_AUTHTYPE']._serialized_end=339
  _globals['_AUTHTYPE_TYPE']._serialized_start=305
  _globals['_AUTHTYPE_TYPE']._serialized_end=339
  _globals['_SQLDATABASEINFO']._serialized_start=342
  _globals['_SQLDATABASEINFO']._serialized_end=1442
  _globals['_DATABASERESTORESPEC']._serialized_start=1445
  _globals['_DATABASERESTORESPEC']._serialized_end=1754
  _globals['_SQLFILECOPYINSTRUCTIONFILTER']._serialized_start=1757
  _globals['_SQLFILECOPYINSTRUCTIONFILTER']._serialized_end=2011
  _globals['_RESTOREPOLICY']._serialized_start=2014
  _globals['_RESTOREPOLICY']._serialized_end=2504
  _globals['_RESTOREPOLICY_DATABASE']._serialized_start=2209
  _globals['_RESTOREPOLICY_DATABASE']._serialized_end=2504
  _globals['_SQLVSSRESTOREPROGRESS']._serialized_start=2507
  _globals['_SQLVSSRESTOREPROGRESS']._serialized_end=2948
  _globals['_SQLVSSRESTOREPROGRESS_DATABASE']._serialized_start=2702
  _globals['_SQLVSSRESTOREPROGRESS_DATABASE']._serialized_end=2948
  _globals['_SQLPARAMS']._serialized_start=2951
  _globals['_SQLPARAMS']._serialized_end=3100
  _globals['_VSSBACKUPINFO']._serialized_start=3103
  _globals['_VSSBACKUPINFO']._serialized_end=3398
  _globals['_AAGINFORESULT']._serialized_start=3400
  _globals['_AAGINFORESULT']._serialized_end=3516
  _globals['_SQLFILEINFOFROMVSSSNAPSHOT']._serialized_start=3518
  _globals['_SQLFILEINFOFROMVSSSNAPSHOT']._serialized_end=3644
  _globals['_SQLAPPFILEINFO']._serialized_start=3647
  _globals['_SQLAPPFILEINFO']._serialized_end=4160
  _globals['_SQLAPPFILEINFO_DATABASEAPPFILEINFO']._serialized_start=3851
  _globals['_SQLAPPFILEINFO_DATABASEAPPFILEINFO']._serialized_end=4040
  _globals['_SQLTOPOLOGYNODE']._serialized_start=4163
  _globals['_SQLTOPOLOGYNODE']._serialized_end=4419
  _globals['_GETSQLTOPOLOGYARG']._serialized_start=4422
  _globals['_GETSQLTOPOLOGYARG']._serialized_end=4642
# @@protoc_insertion_point(module_scope)
