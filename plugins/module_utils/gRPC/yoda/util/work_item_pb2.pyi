from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorkItem(_message.Message):
    __slots__ = ("DEPRECATED_partition_id", "id", "arrival_usecs", "failure_count", "partition_id")
    Extensions: _python_message._ExtensionDict
    DEPRECATED_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_USECS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_partition_id: int
    id: int
    arrival_usecs: int
    failure_count: int
    partition_id: str
    def __init__(self, DEPRECATED_partition_id: _Optional[int] = ..., id: _Optional[int] = ..., arrival_usecs: _Optional[int] = ..., failure_count: _Optional[int] = ..., partition_id: _Optional[str] = ...) -> None: ...
