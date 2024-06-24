from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WinFsInfoMsg(_message.Message):
    __slots__ = ("path", "isDir", "acl", "time", "hash")
    class Timestamp(_message.Message):
        __slots__ = ("creationTime", "lastAccessTime", "lastWriteTime")
        CREATIONTIME_FIELD_NUMBER: _ClassVar[int]
        LASTACCESSTIME_FIELD_NUMBER: _ClassVar[int]
        LASTWRITETIME_FIELD_NUMBER: _ClassVar[int]
        creationTime: bytes
        lastAccessTime: bytes
        lastWriteTime: bytes
        def __init__(self, creationTime: _Optional[bytes] = ..., lastAccessTime: _Optional[bytes] = ..., lastWriteTime: _Optional[bytes] = ...) -> None: ...
    class Acl(_message.Message):
        __slots__ = ("owner", "groups", "access", "sddl")
        OWNER_FIELD_NUMBER: _ClassVar[int]
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        ACCESS_FIELD_NUMBER: _ClassVar[int]
        SDDL_FIELD_NUMBER: _ClassVar[int]
        owner: bytes
        groups: bytes
        access: bytes
        sddl: bytes
        def __init__(self, owner: _Optional[bytes] = ..., groups: _Optional[bytes] = ..., access: _Optional[bytes] = ..., sddl: _Optional[bytes] = ...) -> None: ...
    PATH_FIELD_NUMBER: _ClassVar[int]
    ISDIR_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    path: str
    isDir: bool
    acl: WinFsInfoMsg.Acl
    time: WinFsInfoMsg.Timestamp
    hash: bytes
    def __init__(self, path: _Optional[str] = ..., isDir: bool = ..., acl: _Optional[_Union[WinFsInfoMsg.Acl, _Mapping]] = ..., time: _Optional[_Union[WinFsInfoMsg.Timestamp, _Mapping]] = ..., hash: _Optional[bytes] = ...) -> None: ...
