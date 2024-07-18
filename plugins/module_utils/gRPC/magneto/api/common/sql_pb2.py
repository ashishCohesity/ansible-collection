# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: magneto/api/common/sql.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cmagneto/api/common/sql.proto\x12\x18\x63ohesity.magneto.api.sql\"\x7f\n\x13\x41\x41GBackupPreference\"h\n\x04Type\x12\x17\n\x13kPrimaryReplicaOnly\x10\x00\x12\x19\n\x15kSecondaryReplicaOnly\x10\x01\x12\x1b\n\x17kPreferSecondaryReplica\x10\x02\x12\x0f\n\x0bkAnyReplica\x10\x03\"\x9c\x08\n\x14\x45nvBackupParamsProto\x12\x85\x01\n\x17user_db_preference_type\x18\x01 \x01(\x0e\x32O.cohesity.magneto.api.sql.EnvBackupParamsProto.UserDatabaseBackupPreferenceType:\x13kBackupAllDatabases\x12\x1f\n\x11\x62\x61\x63kup_system_dbs\x18\x02 \x01(\x08:\x04true\x12\x31\n#use_aag_preferences_from_sql_server\x18\x03 \x01(\x08:\x04true\x12V\n\x1a\x61\x61g_backup_preference_type\x18\x04 \x01(\x0e\x32\x32.cohesity.magneto.api.sql.AAGBackupPreference.Type\x12+\n\x1c\x62\x61\x63kup_database_volumes_only\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x66\n\x10\x66ull_backup_type\x18\x06 \x01(\x0e\x32=.cohesity.magneto.api.sql.EnvBackupParamsProto.FullBackupType:\rkSqlVSSVolume\x12\x19\n\x11is_copy_only_full\x18\x07 \x01(\x08\x12\x18\n\x10is_copy_only_log\x18\x08 \x01(\x08\x12\x17\n\x0f\x65nable_checksum\x18\t \x01(\x08\x12\x1c\n\x14\x63ontinue_after_error\x18\n \x01(\x08\x12\x1d\n\x11num_dbs_per_batch\x18\x0b \x01(\x05:\x02-1\x12\x17\n\x0bnum_streams\x18\x0c \x01(\x05:\x02-1\x12\x13\n\x0bwith_clause\x18\r \x01(\t\x12\"\n\x16log_backup_num_streams\x18\x0f \x01(\x05:\x02-1\x12\x1e\n\x16log_backup_with_clause\x18\x10 \x01(\t\x12\x35\n\'enable_incremental_backup_after_restart\x18\x0e \x01(\x08:\x04true\x12\x45\n\x11\x61\x64vanced_settings\x18\x11 \x01(\x0b\x32*.cohesity.magneto.api.sql.AdvancedSettings\"z\n UserDatabaseBackupPreferenceType\x12\x17\n\x13kBackupAllDatabases\x10\x00\x12 \n\x1ckBackupAllExceptAAGDatabases\x10\x01\x12\x1b\n\x17kBackupOnlyAAGDatabases\x10\x02\"D\n\x0e\x46ullBackupType\x12\x11\n\rkSqlVSSVolume\x10\x00\x12\x0f\n\x0bkSqlVSSFile\x10\x01\x12\x0e\n\nkSqlNative\x10\x02\"\xa3\x05\n\x10\x41\x64vancedSettings\x12^\n\x18missing_db_backup_status\x18\x01 \x01(\x0e\x32\x34.cohesity.magneto.api.sql.AdvancedSettings.ErrorType:\x06kError\x12j\n$report_all_non_autoprotect_db_errors\x18\x02 \x01(\x0e\x32\x34.cohesity.magneto.api.sql.AdvancedSettings.ErrorType:\x06kError\x12h\n\"offline_restoring_db_backup_status\x18\x03 \x01(\x0e\x32\x34.cohesity.magneto.api.sql.AdvancedSettings.ErrorType:\x06kError\x12^\n\x17\x63loned_db_backup_status\x18\x04 \x01(\x0e\x32\x34.cohesity.magneto.api.sql.AdvancedSettings.ErrorType:\x07kIgnore\x12\x65\n\x1e\x64\x62_backup_if_not_online_status\x18\x05 \x01(\x0e\x32\x34.cohesity.magneto.api.sql.AdvancedSettings.ErrorType:\x07kIgnore\x12\x61\n\x1aread_only_db_backup_status\x18\x06 \x01(\x0e\x32\x34.cohesity.magneto.api.sql.AdvancedSettings.ErrorType:\x07kIgnore\"/\n\tErrorType\x12\n\n\x06kError\x10\x00\x12\t\n\x05kWarn\x10\x01\x12\x0b\n\x07kIgnore\x10\x02\x42\x1aZ\x18\x63ohesity/magneto/api/sql')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'magneto.api.common.sql_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030cohesity/magneto/api/sql'
  _globals['_AAGBACKUPPREFERENCE']._serialized_start=58
  _globals['_AAGBACKUPPREFERENCE']._serialized_end=185
  _globals['_AAGBACKUPPREFERENCE_TYPE']._serialized_start=81
  _globals['_AAGBACKUPPREFERENCE_TYPE']._serialized_end=185
  _globals['_ENVBACKUPPARAMSPROTO']._serialized_start=188
  _globals['_ENVBACKUPPARAMSPROTO']._serialized_end=1240
  _globals['_ENVBACKUPPARAMSPROTO_USERDATABASEBACKUPPREFERENCETYPE']._serialized_start=1048
  _globals['_ENVBACKUPPARAMSPROTO_USERDATABASEBACKUPPREFERENCETYPE']._serialized_end=1170
  _globals['_ENVBACKUPPARAMSPROTO_FULLBACKUPTYPE']._serialized_start=1172
  _globals['_ENVBACKUPPARAMSPROTO_FULLBACKUPTYPE']._serialized_end=1240
  _globals['_ADVANCEDSETTINGS']._serialized_start=1243
  _globals['_ADVANCEDSETTINGS']._serialized_end=1918
  _globals['_ADVANCEDSETTINGS_ERRORTYPE']._serialized_start=1871
  _globals['_ADVANCEDSETTINGS_ERRORTYPE']._serialized_end=1918
# @@protoc_insertion_point(module_scope)