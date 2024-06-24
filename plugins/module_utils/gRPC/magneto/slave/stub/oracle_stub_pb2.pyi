from bridge.base import error_pb2 as _error_pb2
from magneto.base import error_pb2 as _error_pb2_1
from magneto.connectors.oracle import oracle_pb2 as _oracle_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupDBsUpdateArg(_message.Message):
    __slots__ = ("create_dirs_error", "delete_files_error", "delete_dirs_error", "populate_db_config_error", "db_config_info_vec", "num_ongoing_tasks")
    CREATE_DIRS_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILES_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_DIRS_ERROR_FIELD_NUMBER: _ClassVar[int]
    POPULATE_DB_CONFIG_ERROR_FIELD_NUMBER: _ClassVar[int]
    DB_CONFIG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_ONGOING_TASKS_FIELD_NUMBER: _ClassVar[int]
    create_dirs_error: _error_pb2.ErrorProto
    delete_files_error: _error_pb2.ErrorProto
    delete_dirs_error: _error_pb2.ErrorProto
    populate_db_config_error: _error_pb2.ErrorProto
    db_config_info_vec: _containers.RepeatedCompositeFieldContainer[_oracle_pb2.DatabaseBackupInfo]
    num_ongoing_tasks: int
    def __init__(self, create_dirs_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_files_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_dirs_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., populate_db_config_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., db_config_info_vec: _Optional[_Iterable[_Union[_oracle_pb2.DatabaseBackupInfo, _Mapping]]] = ..., num_ongoing_tasks: _Optional[int] = ...) -> None: ...

class RestoreDBUpdateArg(_message.Message):
    __slots__ = ("clone_files_error", "cloned_data_file_info_map")
    class ClonedDataFileInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLONE_FILES_ERROR_FIELD_NUMBER: _ClassVar[int]
    CLONED_DATA_FILE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    clone_files_error: _error_pb2.ErrorProto
    cloned_data_file_info_map: _containers.ScalarMap[str, str]
    def __init__(self, clone_files_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cloned_data_file_info_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DBConfigUpdateArg(_message.Message):
    __slots__ = ("db_config_info_vec",)
    DB_CONFIG_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    db_config_info_vec: _containers.RepeatedCompositeFieldContainer[_oracle_pb2.DatabaseBackupInfo]
    def __init__(self, db_config_info_vec: _Optional[_Iterable[_Union[_oracle_pb2.DatabaseBackupInfo, _Mapping]]] = ...) -> None: ...

class PrepareArchiveViewUpdateArg(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class OracleActionUpdateArg(_message.Message):
    __slots__ = ("backup_dbs_update_arg", "restore_db_update_arg", "type", "db_config_update_arg", "prepare_archive_view_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupUpdate: _ClassVar[OracleActionUpdateArg.Type]
        kDBConfigUpdate: _ClassVar[OracleActionUpdateArg.Type]
        kRestoreDBUpdate: _ClassVar[OracleActionUpdateArg.Type]
        kPrepareArchiveViewUpdate: _ClassVar[OracleActionUpdateArg.Type]
    kBackupUpdate: OracleActionUpdateArg.Type
    kDBConfigUpdate: OracleActionUpdateArg.Type
    kRestoreDBUpdate: OracleActionUpdateArg.Type
    kPrepareArchiveViewUpdate: OracleActionUpdateArg.Type
    ORACLE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    oracle_action_update_arg: _descriptor.FieldDescriptor
    BACKUP_DBS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DB_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DB_CONFIG_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    PREPARE_ARCHIVE_VIEW_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    backup_dbs_update_arg: BackupDBsUpdateArg
    restore_db_update_arg: RestoreDBUpdateArg
    type: OracleActionUpdateArg.Type
    db_config_update_arg: DBConfigUpdateArg
    prepare_archive_view_update_arg: PrepareArchiveViewUpdateArg
    def __init__(self, backup_dbs_update_arg: _Optional[_Union[BackupDBsUpdateArg, _Mapping]] = ..., restore_db_update_arg: _Optional[_Union[RestoreDBUpdateArg, _Mapping]] = ..., type: _Optional[_Union[OracleActionUpdateArg.Type, str]] = ..., db_config_update_arg: _Optional[_Union[DBConfigUpdateArg, _Mapping]] = ..., prepare_archive_view_update_arg: _Optional[_Union[PrepareArchiveViewUpdateArg, _Mapping]] = ...) -> None: ...

class NotifyOracleSlaveTaskArg(_message.Message):
    __slots__ = ("self_sufficiency_log_info_map", "error")
    class SelfSufficiencyLogInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _oracle_pb2.SelfSufficiencyLogInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_oracle_pb2.SelfSufficiencyLogInfo, _Mapping]] = ...) -> None: ...
    UPDATE_ORACLE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    update_oracle_task_arg: _descriptor.FieldDescriptor
    SELF_SUFFICIENCY_LOG_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    self_sufficiency_log_info_map: _containers.MessageMap[str, _oracle_pb2.SelfSufficiencyLogInfo]
    error: _error_pb2_1.ErrorProto
    def __init__(self, self_sufficiency_log_info_map: _Optional[_Mapping[str, _oracle_pb2.SelfSufficiencyLogInfo]] = ..., error: _Optional[_Union[_error_pb2_1.ErrorProto, _Mapping]] = ...) -> None: ...
