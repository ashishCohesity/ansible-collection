from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AthenaUnmountProto(_message.Message):
    __slots__ = ("unmountdir", "poduid")
    UNMOUNTDIR_FIELD_NUMBER: _ClassVar[int]
    PODUID_FIELD_NUMBER: _ClassVar[int]
    unmountdir: str
    poduid: str
    def __init__(self, unmountdir: _Optional[str] = ..., poduid: _Optional[str] = ...) -> None: ...
