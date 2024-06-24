from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PingPongRequest(_message.Message):
    __slots__ = ("ping",)
    PING_FIELD_NUMBER: _ClassVar[int]
    ping: str
    def __init__(self, ping: _Optional[str] = ...) -> None: ...

class PingPongResponse(_message.Message):
    __slots__ = ("pong",)
    PONG_FIELD_NUMBER: _ClassVar[int]
    pong: str
    def __init__(self, pong: _Optional[str] = ...) -> None: ...

class OpenFileRequest(_message.Message):
    __slots__ = ("path", "flags", "mode")
    PATH_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    flags: int
    mode: int
    def __init__(self, path: _Optional[str] = ..., flags: _Optional[int] = ..., mode: _Optional[int] = ...) -> None: ...

class OpenFileResponse(_message.Message):
    __slots__ = ("fd",)
    FD_FIELD_NUMBER: _ClassVar[int]
    fd: int
    def __init__(self, fd: _Optional[int] = ...) -> None: ...

class CloseFileRequest(_message.Message):
    __slots__ = ("fd",)
    FD_FIELD_NUMBER: _ClassVar[int]
    fd: int
    def __init__(self, fd: _Optional[int] = ...) -> None: ...

class CloseFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("fd", "buf", "count", "offset")
    FD_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    fd: int
    buf: str
    count: int
    offset: int
    def __init__(self, fd: _Optional[int] = ..., buf: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("size",)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("fd", "buf", "count", "offset")
    FD_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    fd: int
    buf: str
    count: int
    offset: int
    def __init__(self, fd: _Optional[int] = ..., buf: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("size",)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...
