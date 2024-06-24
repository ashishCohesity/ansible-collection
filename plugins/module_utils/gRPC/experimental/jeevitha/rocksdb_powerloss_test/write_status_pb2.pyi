from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteStatus(_message.Message):
    __slots__ = ("last_synced_key",)
    LAST_SYNCED_KEY_FIELD_NUMBER: _ClassVar[int]
    last_synced_key: int
    def __init__(self, last_synced_key: _Optional[int] = ...) -> None: ...
