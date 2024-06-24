from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubTaskInfo(_message.Message):
    __slots__ = ("sub_task_idx", "version", "disk_key", "start_pos", "end_pos", "bytes_transferred", "total_bytes_to_transfer", "last_pos_transferred", "bytes_read", "constituent_id", "bifrost_constituent_id", "bifrost_session_id", "status", "error", "skip_transfer", "scribe_table_row", "scribe_table_column", "transport_mode", "reacquire_permit", "total_read_time_usecs", "is_zero_fill_sub_task", "should_skip_permit_on_source_entities")
    Extensions: _python_message._ExtensionDict
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SubTaskInfo.Status]
        kRestarting: _ClassVar[SubTaskInfo.Status]
        kFinishing: _ClassVar[SubTaskInfo.Status]
        kFinished: _ClassVar[SubTaskInfo.Status]
        kCancelled: _ClassVar[SubTaskInfo.Status]
    kStarted: SubTaskInfo.Status
    kRestarting: SubTaskInfo.Status
    kFinishing: SubTaskInfo.Status
    kFinished: SubTaskInfo.Status
    kCancelled: SubTaskInfo.Status
    SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DISK_KEY_FIELD_NUMBER: _ClassVar[int]
    START_POS_FIELD_NUMBER: _ClassVar[int]
    END_POS_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    LAST_POS_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    BIFROST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SKIP_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_ROW_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TABLE_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    REACQUIRE_PERMIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_ZERO_FILL_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    SHOULD_SKIP_PERMIT_ON_SOURCE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    sub_task_idx: int
    version: int
    disk_key: int
    start_pos: int
    end_pos: int
    bytes_transferred: int
    total_bytes_to_transfer: int
    last_pos_transferred: int
    bytes_read: int
    constituent_id: int
    bifrost_constituent_id: int
    bifrost_session_id: int
    status: SubTaskInfo.Status
    error: _error_pb2.ErrorProto
    skip_transfer: bool
    scribe_table_row: str
    scribe_table_column: str
    transport_mode: str
    reacquire_permit: bool
    total_read_time_usecs: int
    is_zero_fill_sub_task: bool
    should_skip_permit_on_source_entities: bool
    def __init__(self, sub_task_idx: _Optional[int] = ..., version: _Optional[int] = ..., disk_key: _Optional[int] = ..., start_pos: _Optional[int] = ..., end_pos: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., total_bytes_to_transfer: _Optional[int] = ..., last_pos_transferred: _Optional[int] = ..., bytes_read: _Optional[int] = ..., constituent_id: _Optional[int] = ..., bifrost_constituent_id: _Optional[int] = ..., bifrost_session_id: _Optional[int] = ..., status: _Optional[_Union[SubTaskInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., skip_transfer: bool = ..., scribe_table_row: _Optional[str] = ..., scribe_table_column: _Optional[str] = ..., transport_mode: _Optional[str] = ..., reacquire_permit: bool = ..., total_read_time_usecs: _Optional[int] = ..., is_zero_fill_sub_task: bool = ..., should_skip_permit_on_source_entities: bool = ...) -> None: ...

class SubTaskScribeInfo(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...
