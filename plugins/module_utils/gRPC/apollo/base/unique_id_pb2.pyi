from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UniqueId(_message.Message):
    __slots__ = ("global_id", "local_id")
    GLOBAL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    global_id: int
    local_id: int
    def __init__(self, global_id: _Optional[int] = ..., local_id: _Optional[int] = ...) -> None: ...
