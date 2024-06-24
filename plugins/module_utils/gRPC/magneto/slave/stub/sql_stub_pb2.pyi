from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamIOUpdateArg(_message.Message):
    __slots__ = ("task_start_time_usecs", "read_start_time_usecs", "read_end_time_usecs", "write_start_time_usecs", "write_end_time_usecs", "num_bytes_processed", "all_bytes_processed", "force_checkpoint_stream")
    TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    READ_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    ALL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHECKPOINT_STREAM_FIELD_NUMBER: _ClassVar[int]
    task_start_time_usecs: int
    read_start_time_usecs: int
    read_end_time_usecs: int
    write_start_time_usecs: int
    write_end_time_usecs: int
    num_bytes_processed: int
    all_bytes_processed: bool
    force_checkpoint_stream: bool
    def __init__(self, task_start_time_usecs: _Optional[int] = ..., read_start_time_usecs: _Optional[int] = ..., read_end_time_usecs: _Optional[int] = ..., write_start_time_usecs: _Optional[int] = ..., write_end_time_usecs: _Optional[int] = ..., num_bytes_processed: _Optional[int] = ..., all_bytes_processed: bool = ..., force_checkpoint_stream: bool = ...) -> None: ...

class SqlActionUpdateArg(_message.Message):
    __slots__ = ("type", "relative_log_backup_file_path", "read_sql_data_update_arg", "write_sql_data_update_arg", "root_path", "relative_snapshot_dir")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareSqlBackupUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kReadSqlDataUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kEndSqlBackupUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kWriteSqlDataUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kCancelStreamIOUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kPrepareSqlLogReplayUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kEndSqlLogReplayUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kDeleteViewUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kMigrateHostViewUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kPopulateNativeRestoreViewUpdate: _ClassVar[SqlActionUpdateArg.Type]
        kClonePreviousBackupFilesUpdate: _ClassVar[SqlActionUpdateArg.Type]
    kPrepareSqlBackupUpdate: SqlActionUpdateArg.Type
    kReadSqlDataUpdate: SqlActionUpdateArg.Type
    kEndSqlBackupUpdate: SqlActionUpdateArg.Type
    kWriteSqlDataUpdate: SqlActionUpdateArg.Type
    kCancelStreamIOUpdate: SqlActionUpdateArg.Type
    kPrepareSqlLogReplayUpdate: SqlActionUpdateArg.Type
    kEndSqlLogReplayUpdate: SqlActionUpdateArg.Type
    kDeleteViewUpdate: SqlActionUpdateArg.Type
    kMigrateHostViewUpdate: SqlActionUpdateArg.Type
    kPopulateNativeRestoreViewUpdate: SqlActionUpdateArg.Type
    kClonePreviousBackupFilesUpdate: SqlActionUpdateArg.Type
    SQL_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    sql_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_LOG_BACKUP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    READ_SQL_DATA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_SQL_DATA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    type: SqlActionUpdateArg.Type
    relative_log_backup_file_path: str
    read_sql_data_update_arg: StreamIOUpdateArg
    write_sql_data_update_arg: StreamIOUpdateArg
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, type: _Optional[_Union[SqlActionUpdateArg.Type, str]] = ..., relative_log_backup_file_path: _Optional[str] = ..., read_sql_data_update_arg: _Optional[_Union[StreamIOUpdateArg, _Mapping]] = ..., write_sql_data_update_arg: _Optional[_Union[StreamIOUpdateArg, _Mapping]] = ..., root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...
