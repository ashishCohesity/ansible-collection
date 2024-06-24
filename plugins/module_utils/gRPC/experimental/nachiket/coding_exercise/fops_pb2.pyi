from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateReply(_message.Message):
    __slots__ = ("status", "errnum")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRNUM_FIELD_NUMBER: _ClassVar[int]
    status: bool
    errnum: int
    def __init__(self, status: bool = ..., errnum: _Optional[int] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("filename", "length", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    length: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadReply(_message.Message):
    __slots__ = ("status", "buf", "errnum")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    ERRNUM_FIELD_NUMBER: _ClassVar[int]
    status: bool
    buf: bytes
    errnum: int
    def __init__(self, status: bool = ..., buf: _Optional[bytes] = ..., errnum: _Optional[int] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("filename", "data", "length", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    data: bytes
    length: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., data: _Optional[bytes] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteReply(_message.Message):
    __slots__ = ("status", "errnum")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRNUM_FIELD_NUMBER: _ClassVar[int]
    status: bool
    errnum: int
    def __init__(self, status: bool = ..., errnum: _Optional[int] = ...) -> None: ...
