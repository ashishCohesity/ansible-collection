from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskId(_message.Message):
    __slots__ = ("gandalf_session_id", "local_id", "name")
    GANDALF_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gandalf_session_id: int
    local_id: int
    name: str
    def __init__(self, gandalf_session_id: _Optional[int] = ..., local_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class FinishedTaskStateProto(_message.Message):
    __slots__ = ("task_id", "type", "arg_bytes", "result_bytes", "cancelled")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ARG_BYTES_FIELD_NUMBER: _ClassVar[int]
    RESULT_BYTES_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    task_id: TaskId
    type: int
    arg_bytes: bytes
    result_bytes: bytes
    cancelled: bool
    def __init__(self, task_id: _Optional[_Union[TaskId, _Mapping]] = ..., type: _Optional[int] = ..., arg_bytes: _Optional[bytes] = ..., result_bytes: _Optional[bytes] = ..., cancelled: bool = ...) -> None: ...
