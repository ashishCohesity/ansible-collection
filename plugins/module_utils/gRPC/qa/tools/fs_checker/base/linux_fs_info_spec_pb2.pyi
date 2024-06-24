from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LinuxFsInfoMsg(_message.Message):
    __slots__ = ("path", "is_dir", "checksum", "timestamp", "uid", "gid", "permissions", "size")
    PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DIR_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    path: str
    is_dir: bool
    checksum: str
    timestamp: str
    uid: str
    gid: str
    permissions: str
    size: int
    def __init__(self, path: _Optional[str] = ..., is_dir: bool = ..., checksum: _Optional[str] = ..., timestamp: _Optional[str] = ..., uid: _Optional[str] = ..., gid: _Optional[str] = ..., permissions: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...
