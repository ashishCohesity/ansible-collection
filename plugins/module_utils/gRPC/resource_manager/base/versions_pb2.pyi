from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VersionProto(_message.Message):
    __slots__ = ("wal_version", "api_version")
    WAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    wal_version: int
    api_version: int
    def __init__(self, wal_version: _Optional[int] = ..., api_version: _Optional[int] = ...) -> None: ...
