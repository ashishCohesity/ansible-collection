from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SystemResourceInfo(_message.Message):
    __slots__ = ("number_of_processors", "total_physical_memory_in_bytes")
    NUMBER_OF_PROCESSORS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_MEMORY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    number_of_processors: int
    total_physical_memory_in_bytes: int
    def __init__(self, number_of_processors: _Optional[int] = ..., total_physical_memory_in_bytes: _Optional[int] = ...) -> None: ...
