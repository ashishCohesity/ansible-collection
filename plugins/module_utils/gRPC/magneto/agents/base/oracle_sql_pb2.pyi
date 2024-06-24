from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RmanSessionInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("session_id", "session_number", "session_process_id", "client_info", "status", "parent_rman_process_id")
        class SessionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kActive: _ClassVar[RmanSessionInfo.Row.SessionStatus]
            kInactive: _ClassVar[RmanSessionInfo.Row.SessionStatus]
            kKilled: _ClassVar[RmanSessionInfo.Row.SessionStatus]
            kCached: _ClassVar[RmanSessionInfo.Row.SessionStatus]
            kSniped: _ClassVar[RmanSessionInfo.Row.SessionStatus]
        kActive: RmanSessionInfo.Row.SessionStatus
        kInactive: RmanSessionInfo.Row.SessionStatus
        kKilled: RmanSessionInfo.Row.SessionStatus
        kCached: RmanSessionInfo.Row.SessionStatus
        kSniped: RmanSessionInfo.Row.SessionStatus
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SESSION_PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PARENT_RMAN_PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        session_number: int
        session_process_id: int
        client_info: str
        status: RmanSessionInfo.Row.SessionStatus
        parent_rman_process_id: int
        def __init__(self, session_id: _Optional[int] = ..., session_number: _Optional[int] = ..., session_process_id: _Optional[int] = ..., client_info: _Optional[str] = ..., status: _Optional[_Union[RmanSessionInfo.Row.SessionStatus, str]] = ..., parent_rman_process_id: _Optional[int] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[RmanSessionInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[RmanSessionInfo.Row, _Mapping]]] = ...) -> None: ...

class RmanStatusInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("rec_id", "stamp", "parent_rec_id", "parent_stamp", "session_rec_id", "session_stamp", "status")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kRunning: _ClassVar[RmanStatusInfo.Row.Status]
            kRunning_with_warnings: _ClassVar[RmanStatusInfo.Row.Status]
            kRunning_with_error: _ClassVar[RmanStatusInfo.Row.Status]
            kCompleted: _ClassVar[RmanStatusInfo.Row.Status]
            kCompleted_with_warnings: _ClassVar[RmanStatusInfo.Row.Status]
            kCompleted_with_errors: _ClassVar[RmanStatusInfo.Row.Status]
            kFailed: _ClassVar[RmanStatusInfo.Row.Status]
        kRunning: RmanStatusInfo.Row.Status
        kRunning_with_warnings: RmanStatusInfo.Row.Status
        kRunning_with_error: RmanStatusInfo.Row.Status
        kCompleted: RmanStatusInfo.Row.Status
        kCompleted_with_warnings: RmanStatusInfo.Row.Status
        kCompleted_with_errors: RmanStatusInfo.Row.Status
        kFailed: RmanStatusInfo.Row.Status
        REC_ID_FIELD_NUMBER: _ClassVar[int]
        STAMP_FIELD_NUMBER: _ClassVar[int]
        PARENT_REC_ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_STAMP_FIELD_NUMBER: _ClassVar[int]
        SESSION_REC_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_STAMP_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        rec_id: int
        stamp: int
        parent_rec_id: int
        parent_stamp: int
        session_rec_id: int
        session_stamp: int
        status: RmanStatusInfo.Row.Status
        def __init__(self, rec_id: _Optional[int] = ..., stamp: _Optional[int] = ..., parent_rec_id: _Optional[int] = ..., parent_stamp: _Optional[int] = ..., session_rec_id: _Optional[int] = ..., session_stamp: _Optional[int] = ..., status: _Optional[_Union[RmanStatusInfo.Row.Status, str]] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[RmanStatusInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[RmanStatusInfo.Row, _Mapping]]] = ...) -> None: ...

class RedoLogInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("thread_id", "sequence", "reset_logs_change", "reset_logs_time", "first_scn", "first_change_time", "last_scn", "last_change_time", "reset_logs_id", "is_dummy")
        THREAD_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        RESET_LOGS_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RESET_LOGS_TIME_FIELD_NUMBER: _ClassVar[int]
        FIRST_SCN_FIELD_NUMBER: _ClassVar[int]
        FIRST_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_SCN_FIELD_NUMBER: _ClassVar[int]
        LAST_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
        RESET_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
        IS_DUMMY_FIELD_NUMBER: _ClassVar[int]
        thread_id: int
        sequence: int
        reset_logs_change: int
        reset_logs_time: str
        first_scn: int
        first_change_time: str
        last_scn: int
        last_change_time: str
        reset_logs_id: int
        is_dummy: bool
        def __init__(self, thread_id: _Optional[int] = ..., sequence: _Optional[int] = ..., reset_logs_change: _Optional[int] = ..., reset_logs_time: _Optional[str] = ..., first_scn: _Optional[int] = ..., first_change_time: _Optional[str] = ..., last_scn: _Optional[int] = ..., last_change_time: _Optional[str] = ..., reset_logs_id: _Optional[int] = ..., is_dummy: bool = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[RedoLogInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[RedoLogInfo.Row, _Mapping]]] = ...) -> None: ...

class ThreadInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("thread_id", "status")
        class ThreadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kOpen: _ClassVar[ThreadInfo.Row.ThreadStatus]
            kClosed: _ClassVar[ThreadInfo.Row.ThreadStatus]
        kOpen: ThreadInfo.Row.ThreadStatus
        kClosed: ThreadInfo.Row.ThreadStatus
        THREAD_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        thread_id: int
        status: ThreadInfo.Row.ThreadStatus
        def __init__(self, thread_id: _Optional[int] = ..., status: _Optional[_Union[ThreadInfo.Row.ThreadStatus, str]] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[ThreadInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[ThreadInfo.Row, _Mapping]]] = ...) -> None: ...

class ArchiveLogsInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("file_name", "piece_key", "status", "tag", "redo_log_info", "size_bytes")
        class BackupPieceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAvailable: _ClassVar[ArchiveLogsInfo.Row.BackupPieceStatus]
            kDeleted: _ClassVar[ArchiveLogsInfo.Row.BackupPieceStatus]
            kExpired: _ClassVar[ArchiveLogsInfo.Row.BackupPieceStatus]
        kAvailable: ArchiveLogsInfo.Row.BackupPieceStatus
        kDeleted: ArchiveLogsInfo.Row.BackupPieceStatus
        kExpired: ArchiveLogsInfo.Row.BackupPieceStatus
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        PIECE_KEY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        REDO_LOG_INFO_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        piece_key: int
        status: ArchiveLogsInfo.Row.BackupPieceStatus
        tag: str
        redo_log_info: RedoLogInfo
        size_bytes: int
        def __init__(self, file_name: _Optional[str] = ..., piece_key: _Optional[int] = ..., status: _Optional[_Union[ArchiveLogsInfo.Row.BackupPieceStatus, str]] = ..., tag: _Optional[str] = ..., redo_log_info: _Optional[_Union[RedoLogInfo, _Mapping]] = ..., size_bytes: _Optional[int] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[ArchiveLogsInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[ArchiveLogsInfo.Row, _Mapping]]] = ...) -> None: ...

class BackupPieceInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("file_name", "piece_key", "status", "tag", "size_bytes", "is_cloned_for_self_sufficiency")
        class BackupPieceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAvailable: _ClassVar[BackupPieceInfo.Row.BackupPieceStatus]
            kDeleted: _ClassVar[BackupPieceInfo.Row.BackupPieceStatus]
            kExpired: _ClassVar[BackupPieceInfo.Row.BackupPieceStatus]
        kAvailable: BackupPieceInfo.Row.BackupPieceStatus
        kDeleted: BackupPieceInfo.Row.BackupPieceStatus
        kExpired: BackupPieceInfo.Row.BackupPieceStatus
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        PIECE_KEY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_CLONED_FOR_SELF_SUFFICIENCY_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        piece_key: int
        status: BackupPieceInfo.Row.BackupPieceStatus
        tag: str
        size_bytes: int
        is_cloned_for_self_sufficiency: bool
        def __init__(self, file_name: _Optional[str] = ..., piece_key: _Optional[int] = ..., status: _Optional[_Union[BackupPieceInfo.Row.BackupPieceStatus, str]] = ..., tag: _Optional[str] = ..., size_bytes: _Optional[int] = ..., is_cloned_for_self_sufficiency: bool = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[BackupPieceInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[BackupPieceInfo.Row, _Mapping]]] = ...) -> None: ...

class BackupSetInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("bs_key", "controlfile_type", "redo_log_info", "backup_piece_info", "spfile_included")
        BS_KEY_FIELD_NUMBER: _ClassVar[int]
        CONTROLFILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        REDO_LOG_INFO_FIELD_NUMBER: _ClassVar[int]
        BACKUP_PIECE_INFO_FIELD_NUMBER: _ClassVar[int]
        SPFILE_INCLUDED_FIELD_NUMBER: _ClassVar[int]
        bs_key: int
        controlfile_type: int
        redo_log_info: RedoLogInfo
        backup_piece_info: BackupPieceInfo
        spfile_included: bool
        def __init__(self, bs_key: _Optional[int] = ..., controlfile_type: _Optional[int] = ..., redo_log_info: _Optional[_Union[RedoLogInfo, _Mapping]] = ..., backup_piece_info: _Optional[_Union[BackupPieceInfo, _Mapping]] = ..., spfile_included: bool = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[BackupSetInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[BackupSetInfo.Row, _Mapping]]] = ...) -> None: ...

class LogFileInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("file_path", "member_size_mb", "group_number", "thread_number")
        FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        MEMBER_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        GROUP_NUMBER_FIELD_NUMBER: _ClassVar[int]
        THREAD_NUMBER_FIELD_NUMBER: _ClassVar[int]
        file_path: str
        member_size_mb: int
        group_number: int
        thread_number: int
        def __init__(self, file_path: _Optional[str] = ..., member_size_mb: _Optional[int] = ..., group_number: _Optional[int] = ..., thread_number: _Optional[int] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[LogFileInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[LogFileInfo.Row, _Mapping]]] = ...) -> None: ...

class DataFilesInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("file_name", "rec_id", "stamp", "tag", "incremental_level", "reset_logs_change", "reset_logs_time", "checkpoint_change", "checkpoint_time", "absolute_fuzzy_change", "recovery_fuzzy_change", "recovery_fuzzy_time", "online_fuzzy", "backup_fuzzy", "marked_corrupt", "media_corrupt", "logically_corrupt", "status", "blocks", "block_size", "path", "file_status", "file_checkpoint", "con_id", "datafile_number")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAvailable: _ClassVar[DataFilesInfo.Row.Status]
            kDeleted: _ClassVar[DataFilesInfo.Row.Status]
            kUnavailable: _ClassVar[DataFilesInfo.Row.Status]
            kExpired: _ClassVar[DataFilesInfo.Row.Status]
        kAvailable: DataFilesInfo.Row.Status
        kDeleted: DataFilesInfo.Row.Status
        kUnavailable: DataFilesInfo.Row.Status
        kExpired: DataFilesInfo.Row.Status
        class FileStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDisabled: _ClassVar[DataFilesInfo.Row.FileStatus]
            kReadOnly: _ClassVar[DataFilesInfo.Row.FileStatus]
            kReadWrite: _ClassVar[DataFilesInfo.Row.FileStatus]
            kUnknown: _ClassVar[DataFilesInfo.Row.FileStatus]
        kDisabled: DataFilesInfo.Row.FileStatus
        kReadOnly: DataFilesInfo.Row.FileStatus
        kReadWrite: DataFilesInfo.Row.FileStatus
        kUnknown: DataFilesInfo.Row.FileStatus
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        REC_ID_FIELD_NUMBER: _ClassVar[int]
        STAMP_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        RESET_LOGS_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RESET_LOGS_TIME_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_CHANGE_FIELD_NUMBER: _ClassVar[int]
        CHECKPOINT_TIME_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_FUZZY_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RECOVERY_FUZZY_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RECOVERY_FUZZY_TIME_FIELD_NUMBER: _ClassVar[int]
        ONLINE_FUZZY_FIELD_NUMBER: _ClassVar[int]
        BACKUP_FUZZY_FIELD_NUMBER: _ClassVar[int]
        MARKED_CORRUPT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_CORRUPT_FIELD_NUMBER: _ClassVar[int]
        LOGICALLY_CORRUPT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        BLOCKS_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        FILE_STATUS_FIELD_NUMBER: _ClassVar[int]
        FILE_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        CON_ID_FIELD_NUMBER: _ClassVar[int]
        DATAFILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        rec_id: int
        stamp: int
        tag: str
        incremental_level: int
        reset_logs_change: int
        reset_logs_time: str
        checkpoint_change: int
        checkpoint_time: str
        absolute_fuzzy_change: int
        recovery_fuzzy_change: int
        recovery_fuzzy_time: int
        online_fuzzy: bool
        backup_fuzzy: bool
        marked_corrupt: int
        media_corrupt: int
        logically_corrupt: int
        status: DataFilesInfo.Row.Status
        blocks: int
        block_size: int
        path: str
        file_status: DataFilesInfo.Row.FileStatus
        file_checkpoint: int
        con_id: int
        datafile_number: int
        def __init__(self, file_name: _Optional[str] = ..., rec_id: _Optional[int] = ..., stamp: _Optional[int] = ..., tag: _Optional[str] = ..., incremental_level: _Optional[int] = ..., reset_logs_change: _Optional[int] = ..., reset_logs_time: _Optional[str] = ..., checkpoint_change: _Optional[int] = ..., checkpoint_time: _Optional[str] = ..., absolute_fuzzy_change: _Optional[int] = ..., recovery_fuzzy_change: _Optional[int] = ..., recovery_fuzzy_time: _Optional[int] = ..., online_fuzzy: bool = ..., backup_fuzzy: bool = ..., marked_corrupt: _Optional[int] = ..., media_corrupt: _Optional[int] = ..., logically_corrupt: _Optional[int] = ..., status: _Optional[_Union[DataFilesInfo.Row.Status, str]] = ..., blocks: _Optional[int] = ..., block_size: _Optional[int] = ..., path: _Optional[str] = ..., file_status: _Optional[_Union[DataFilesInfo.Row.FileStatus, str]] = ..., file_checkpoint: _Optional[int] = ..., con_id: _Optional[int] = ..., datafile_number: _Optional[int] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[DataFilesInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[DataFilesInfo.Row, _Mapping]]] = ...) -> None: ...

class DatabaseIncarnationInfo(_message.Message):
    __slots__ = ("row_vec",)
    class Row(_message.Message):
        __slots__ = ("reset_log_scn", "incarnation", "reset_log_time", "prior_reset_log_scn", "prior_incarnation", "status", "reset_logs_id")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kOrphan: _ClassVar[DatabaseIncarnationInfo.Row.Status]
            kCurrent: _ClassVar[DatabaseIncarnationInfo.Row.Status]
            kParent: _ClassVar[DatabaseIncarnationInfo.Row.Status]
        kOrphan: DatabaseIncarnationInfo.Row.Status
        kCurrent: DatabaseIncarnationInfo.Row.Status
        kParent: DatabaseIncarnationInfo.Row.Status
        RESET_LOG_SCN_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_FIELD_NUMBER: _ClassVar[int]
        RESET_LOG_TIME_FIELD_NUMBER: _ClassVar[int]
        PRIOR_RESET_LOG_SCN_FIELD_NUMBER: _ClassVar[int]
        PRIOR_INCARNATION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        RESET_LOGS_ID_FIELD_NUMBER: _ClassVar[int]
        reset_log_scn: int
        incarnation: int
        reset_log_time: str
        prior_reset_log_scn: int
        prior_incarnation: int
        status: DatabaseIncarnationInfo.Row.Status
        reset_logs_id: int
        def __init__(self, reset_log_scn: _Optional[int] = ..., incarnation: _Optional[int] = ..., reset_log_time: _Optional[str] = ..., prior_reset_log_scn: _Optional[int] = ..., prior_incarnation: _Optional[int] = ..., status: _Optional[_Union[DatabaseIncarnationInfo.Row.Status, str]] = ..., reset_logs_id: _Optional[int] = ...) -> None: ...
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[DatabaseIncarnationInfo.Row]
    def __init__(self, row_vec: _Optional[_Iterable[_Union[DatabaseIncarnationInfo.Row, _Mapping]]] = ...) -> None: ...

class LongOpProgressInfo(_message.Message):
    __slots__ = ("sofar_bytes", "total_bytes", "incr_sofar_bytes", "incr_total_bytes", "sofar_written_bytes")
    SOFAR_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    INCR_SOFAR_BYTES_FIELD_NUMBER: _ClassVar[int]
    INCR_TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOFAR_WRITTEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    sofar_bytes: int
    total_bytes: int
    incr_sofar_bytes: int
    incr_total_bytes: int
    sofar_written_bytes: int
    def __init__(self, sofar_bytes: _Optional[int] = ..., total_bytes: _Optional[int] = ..., incr_sofar_bytes: _Optional[int] = ..., incr_total_bytes: _Optional[int] = ..., sofar_written_bytes: _Optional[int] = ...) -> None: ...

class BackupSummaryInfo(_message.Message):
    __slots__ = ("start_time", "end_time", "time_taken_secs", "total_read_bytes", "total_write_bytes")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_SECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_READ_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WRITE_BYTES_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    end_time: str
    time_taken_secs: int
    total_read_bytes: int
    total_write_bytes: int
    def __init__(self, start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., time_taken_secs: _Optional[int] = ..., total_read_bytes: _Optional[int] = ..., total_write_bytes: _Optional[int] = ...) -> None: ...
