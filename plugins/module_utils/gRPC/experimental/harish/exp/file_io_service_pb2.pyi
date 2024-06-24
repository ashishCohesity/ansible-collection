from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("pathname",)
    PATHNAME_FIELD_NUMBER: _ClassVar[int]
    pathname: str
    def __init__(self, pathname: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("result", "err_code")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    result: int
    err_code: int
    def __init__(self, result: _Optional[int] = ..., err_code: _Optional[int] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("pathname", "count", "offset")
    PATHNAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    pathname: str
    count: int
    offset: int
    def __init__(self, pathname: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("result", "err_code", "data")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    result: int
    err_code: int
    data: bytes
    def __init__(self, result: _Optional[int] = ..., err_code: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("pathname", "count", "offset", "data")
    PATHNAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    pathname: str
    count: int
    offset: int
    data: bytes
    def __init__(self, pathname: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ("result", "err_code")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    result: int
    err_code: int
    def __init__(self, result: _Optional[int] = ..., err_code: _Optional[int] = ...) -> None: ...
