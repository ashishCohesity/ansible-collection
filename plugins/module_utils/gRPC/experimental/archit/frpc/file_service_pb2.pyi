from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("fname",)
    FNAME_FIELD_NUMBER: _ClassVar[int]
    fname: str
    def __init__(self, fname: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: bool
    def __init__(self, error: bool = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("fname", "offset", "len")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    len: int
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error", "response", "server_exec_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SERVER_EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    response: bytes
    server_exec_id: int
    def __init__(self, error: bool = ..., response: _Optional[bytes] = ..., server_exec_id: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("fname", "offset", "content")
    FNAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    fname: str
    offset: int
    content: bytes
    def __init__(self, fname: _Optional[str] = ..., offset: _Optional[int] = ..., content: _Optional[bytes] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error", "response", "server_exec_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SERVER_EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    response: bytes
    server_exec_id: int
    def __init__(self, error: bool = ..., response: _Optional[bytes] = ..., server_exec_id: _Optional[int] = ...) -> None: ...
