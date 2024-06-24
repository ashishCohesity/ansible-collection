from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CrashTesterWALProto(_message.Message):
    __slots__ = ("key", "checksum")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    key: int
    checksum: int
    def __init__(self, key: _Optional[int] = ..., checksum: _Optional[int] = ...) -> None: ...
