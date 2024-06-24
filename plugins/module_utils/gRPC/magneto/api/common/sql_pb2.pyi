from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AAGBackupPreference(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrimaryReplicaOnly: _ClassVar[AAGBackupPreference.Type]
        kSecondaryReplicaOnly: _ClassVar[AAGBackupPreference.Type]
        kPreferSecondaryReplica: _ClassVar[AAGBackupPreference.Type]
        kAnyReplica: _ClassVar[AAGBackupPreference.Type]
    kPrimaryReplicaOnly: AAGBackupPreference.Type
    kSecondaryReplicaOnly: AAGBackupPreference.Type
    kPreferSecondaryReplica: AAGBackupPreference.Type
    kAnyReplica: AAGBackupPreference.Type
    def __init__(self) -> None: ...

class EnvBackupParamsProto(_message.Message):
    __slots__ = ("user_db_preference_type", "backup_system_dbs", "use_aag_preferences_from_sql_server", "aag_backup_preference_type", "backup_database_volumes_only", "full_backup_type", "is_copy_only_full", "is_copy_only_log", "enable_checksum", "continue_after_error", "num_dbs_per_batch", "num_streams", "with_clause", "log_backup_num_streams", "log_backup_with_clause", "enable_incremental_backup_after_restart", "advanced_settings")
    class UserDatabaseBackupPreferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupAllDatabases: _ClassVar[EnvBackupParamsProto.UserDatabaseBackupPreferenceType]
        kBackupAllExceptAAGDatabases: _ClassVar[EnvBackupParamsProto.UserDatabaseBackupPreferenceType]
        kBackupOnlyAAGDatabases: _ClassVar[EnvBackupParamsProto.UserDatabaseBackupPreferenceType]
    kBackupAllDatabases: EnvBackupParamsProto.UserDatabaseBackupPreferenceType
    kBackupAllExceptAAGDatabases: EnvBackupParamsProto.UserDatabaseBackupPreferenceType
    kBackupOnlyAAGDatabases: EnvBackupParamsProto.UserDatabaseBackupPreferenceType
    class FullBackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSqlVSSVolume: _ClassVar[EnvBackupParamsProto.FullBackupType]
        kSqlVSSFile: _ClassVar[EnvBackupParamsProto.FullBackupType]
        kSqlNative: _ClassVar[EnvBackupParamsProto.FullBackupType]
    kSqlVSSVolume: EnvBackupParamsProto.FullBackupType
    kSqlVSSFile: EnvBackupParamsProto.FullBackupType
    kSqlNative: EnvBackupParamsProto.FullBackupType
    USER_DB_PREFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SYSTEM_DBS_FIELD_NUMBER: _ClassVar[int]
    USE_AAG_PREFERENCES_FROM_SQL_SERVER_FIELD_NUMBER: _ClassVar[int]
    AAG_BACKUP_PREFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DATABASE_VOLUMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_ONLY_FULL_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_ONLY_LOG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_DBS_PER_BATCH_FIELD_NUMBER: _ClassVar[int]
    NUM_STREAMS_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_NUM_STREAMS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INCREMENTAL_BACKUP_AFTER_RESTART_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    user_db_preference_type: EnvBackupParamsProto.UserDatabaseBackupPreferenceType
    backup_system_dbs: bool
    use_aag_preferences_from_sql_server: bool
    aag_backup_preference_type: AAGBackupPreference.Type
    backup_database_volumes_only: bool
    full_backup_type: EnvBackupParamsProto.FullBackupType
    is_copy_only_full: bool
    is_copy_only_log: bool
    enable_checksum: bool
    continue_after_error: bool
    num_dbs_per_batch: int
    num_streams: int
    with_clause: str
    log_backup_num_streams: int
    log_backup_with_clause: str
    enable_incremental_backup_after_restart: bool
    advanced_settings: AdvancedSettings
    def __init__(self, user_db_preference_type: _Optional[_Union[EnvBackupParamsProto.UserDatabaseBackupPreferenceType, str]] = ..., backup_system_dbs: bool = ..., use_aag_preferences_from_sql_server: bool = ..., aag_backup_preference_type: _Optional[_Union[AAGBackupPreference.Type, str]] = ..., backup_database_volumes_only: bool = ..., full_backup_type: _Optional[_Union[EnvBackupParamsProto.FullBackupType, str]] = ..., is_copy_only_full: bool = ..., is_copy_only_log: bool = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., num_dbs_per_batch: _Optional[int] = ..., num_streams: _Optional[int] = ..., with_clause: _Optional[str] = ..., log_backup_num_streams: _Optional[int] = ..., log_backup_with_clause: _Optional[str] = ..., enable_incremental_backup_after_restart: bool = ..., advanced_settings: _Optional[_Union[AdvancedSettings, _Mapping]] = ...) -> None: ...

class AdvancedSettings(_message.Message):
    __slots__ = ("missing_db_backup_status", "report_all_non_autoprotect_db_errors", "offline_restoring_db_backup_status", "cloned_db_backup_status", "db_backup_if_not_online_status", "read_only_db_backup_status")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kError: _ClassVar[AdvancedSettings.ErrorType]
        kWarn: _ClassVar[AdvancedSettings.ErrorType]
        kIgnore: _ClassVar[AdvancedSettings.ErrorType]
    kError: AdvancedSettings.ErrorType
    kWarn: AdvancedSettings.ErrorType
    kIgnore: AdvancedSettings.ErrorType
    MISSING_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_ALL_NON_AUTOPROTECT_DB_ERRORS_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_RESTORING_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    CLONED_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    DB_BACKUP_IF_NOT_ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_DB_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    missing_db_backup_status: AdvancedSettings.ErrorType
    report_all_non_autoprotect_db_errors: AdvancedSettings.ErrorType
    offline_restoring_db_backup_status: AdvancedSettings.ErrorType
    cloned_db_backup_status: AdvancedSettings.ErrorType
    db_backup_if_not_online_status: AdvancedSettings.ErrorType
    read_only_db_backup_status: AdvancedSettings.ErrorType
    def __init__(self, missing_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., report_all_non_autoprotect_db_errors: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., offline_restoring_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., cloned_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., db_backup_if_not_online_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ..., read_only_db_backup_status: _Optional[_Union[AdvancedSettings.ErrorType, str]] = ...) -> None: ...
