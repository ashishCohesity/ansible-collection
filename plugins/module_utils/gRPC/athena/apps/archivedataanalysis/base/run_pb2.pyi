from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Run(_message.Message):
    __slots__ = ("id", "job_uid", "status", "start_time_msecs", "end_time_msecs", "findings_table_name", "status_message")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInProgress: _ClassVar[Run.Status]
        kCompleted: _ClassVar[Run.Status]
        kFailed: _ClassVar[Run.Status]
    kInProgress: Run.Status
    kCompleted: Run.Status
    kFailed: Run.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    job_uid: str
    status: Run.Status
    start_time_msecs: int
    end_time_msecs: int
    findings_table_name: str
    status_message: str
    def __init__(self, id: _Optional[int] = ..., job_uid: _Optional[str] = ..., status: _Optional[_Union[Run.Status, str]] = ..., start_time_msecs: _Optional[int] = ..., end_time_msecs: _Optional[int] = ..., findings_table_name: _Optional[str] = ..., status_message: _Optional[str] = ...) -> None: ...
