from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.storage import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Timespec(_message.Message):
    __slots__ = ("sec", "nsec")
    SEC_FIELD_NUMBER: _ClassVar[int]
    NSEC_FIELD_NUMBER: _ClassVar[int]
    sec: int
    nsec: int
    def __init__(self, sec: _Optional[int] = ..., nsec: _Optional[int] = ...) -> None: ...

class Stat(_message.Message):
    __slots__ = ("dev", "ino", "nlink", "mode", "uid", "gid", "rdev", "size", "blksize", "blocks", "atime", "mtime", "ctime")
    DEV_FIELD_NUMBER: _ClassVar[int]
    INO_FIELD_NUMBER: _ClassVar[int]
    NLINK_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    RDEV_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    BLKSIZE_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    ATIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    dev: int
    ino: int
    nlink: int
    mode: int
    uid: int
    gid: int
    rdev: int
    size: int
    blksize: int
    blocks: int
    atime: Timespec
    mtime: Timespec
    ctime: Timespec
    def __init__(self, dev: _Optional[int] = ..., ino: _Optional[int] = ..., nlink: _Optional[int] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., rdev: _Optional[int] = ..., size: _Optional[int] = ..., blksize: _Optional[int] = ..., blocks: _Optional[int] = ..., atime: _Optional[_Union[Timespec, _Mapping]] = ..., mtime: _Optional[_Union[Timespec, _Mapping]] = ..., ctime: _Optional[_Union[Timespec, _Mapping]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetattrArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class GetattrResult(_message.Message):
    __slots__ = ("error", "stat")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    stat: Stat
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stat: _Optional[_Union[Stat, _Mapping]] = ...) -> None: ...

class ReadlinkArg(_message.Message):
    __slots__ = ("path", "size")
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    path: str
    size: int
    def __init__(self, path: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class ReadlinkResult(_message.Message):
    __slots__ = ("error", "buf")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    buf: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., buf: _Optional[str] = ...) -> None: ...

class MkdirArg(_message.Message):
    __slots__ = ("path", "mode")
    PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    mode: int
    def __init__(self, path: _Optional[str] = ..., mode: _Optional[int] = ...) -> None: ...

class UnlinkArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class RmdirArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class SymlinkArg(_message.Message):
    __slots__ = ("oldpath", "newpath")
    OLDPATH_FIELD_NUMBER: _ClassVar[int]
    NEWPATH_FIELD_NUMBER: _ClassVar[int]
    oldpath: str
    newpath: str
    def __init__(self, oldpath: _Optional[str] = ..., newpath: _Optional[str] = ...) -> None: ...

class RenameArg(_message.Message):
    __slots__ = ("oldpath", "newpath")
    OLDPATH_FIELD_NUMBER: _ClassVar[int]
    NEWPATH_FIELD_NUMBER: _ClassVar[int]
    oldpath: str
    newpath: str
    def __init__(self, oldpath: _Optional[str] = ..., newpath: _Optional[str] = ...) -> None: ...

class LinkArg(_message.Message):
    __slots__ = ("oldpath", "newpath")
    OLDPATH_FIELD_NUMBER: _ClassVar[int]
    NEWPATH_FIELD_NUMBER: _ClassVar[int]
    oldpath: str
    newpath: str
    def __init__(self, oldpath: _Optional[str] = ..., newpath: _Optional[str] = ...) -> None: ...

class ChmodArg(_message.Message):
    __slots__ = ("path", "mode")
    PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    mode: int
    def __init__(self, path: _Optional[str] = ..., mode: _Optional[int] = ...) -> None: ...

class ChownArg(_message.Message):
    __slots__ = ("path", "uid", "gid")
    PATH_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    path: str
    uid: int
    gid: int
    def __init__(self, path: _Optional[str] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ...) -> None: ...

class TruncateArg(_message.Message):
    __slots__ = ("path", "length")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    path: str
    length: int
    def __init__(self, path: _Optional[str] = ..., length: _Optional[int] = ...) -> None: ...

class OpenArg(_message.Message):
    __slots__ = ("path", "flags")
    PATH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    path: str
    flags: int
    def __init__(self, path: _Optional[str] = ..., flags: _Optional[int] = ...) -> None: ...

class ReadArg(_message.Message):
    __slots__ = ("path", "offset", "size")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    size: int
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("error", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteArg(_message.Message):
    __slots__ = ("path", "data", "offset")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    path: str
    data: bytes
    offset: int
    def __init__(self, path: _Optional[str] = ..., data: _Optional[bytes] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("error", "count")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    count: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class ReleaseArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class OpendirArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReaddirArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReaddirResult(_message.Message):
    __slots__ = ("error", "entries_vec")
    class Entry(_message.Message):
        __slots__ = ("name", "stat")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STAT_FIELD_NUMBER: _ClassVar[int]
        name: str
        stat: Stat
        def __init__(self, name: _Optional[str] = ..., stat: _Optional[_Union[Stat, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entries_vec: _containers.RepeatedCompositeFieldContainer[ReaddirResult.Entry]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entries_vec: _Optional[_Iterable[_Union[ReaddirResult.Entry, _Mapping]]] = ...) -> None: ...

class ReleasedirArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class CreateArg(_message.Message):
    __slots__ = ("path", "mode")
    PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    mode: int
    def __init__(self, path: _Optional[str] = ..., mode: _Optional[int] = ...) -> None: ...

class UtimensArg(_message.Message):
    __slots__ = ("path", "atim", "mtim")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ATIM_FIELD_NUMBER: _ClassVar[int]
    MTIM_FIELD_NUMBER: _ClassVar[int]
    path: str
    atim: Timespec
    mtim: Timespec
    def __init__(self, path: _Optional[str] = ..., atim: _Optional[_Union[Timespec, _Mapping]] = ..., mtim: _Optional[_Union[Timespec, _Mapping]] = ...) -> None: ...
