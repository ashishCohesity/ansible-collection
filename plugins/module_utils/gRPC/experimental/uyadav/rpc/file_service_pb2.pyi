from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: bool
    def __init__(self, error: bool = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("name", "len", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    len: int
    offset: int
    def __init__(self, name: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error_msg", "data")
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error_msg: str
    data: bytes
    def __init__(self, error_msg: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("name", "content", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: bytes
    offset: int
    def __init__(self, name: _Optional[str] = ..., content: _Optional[bytes] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error_msg", "size_of_bytes")
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    SIZE_OF_BYTES_FIELD_NUMBER: _ClassVar[int]
    error_msg: str
    size_of_bytes: int
    def __init__(self, error_msg: _Optional[str] = ..., size_of_bytes: _Optional[int] = ...) -> None: ...
