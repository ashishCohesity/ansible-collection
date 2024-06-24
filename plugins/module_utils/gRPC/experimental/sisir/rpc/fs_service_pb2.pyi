from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("pathname",)
    PATHNAME_FIELD_NUMBER: _ClassVar[int]
    pathname: str
    def __init__(self, pathname: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("result", "err_code")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    result: int
    err_code: int
    def __init__(self, result: _Optional[int] = ..., err_code: _Optional[int] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("pathname", "count", "offset")
    PATHNAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    pathname: str
    count: int
    offset: int
    def __init__(self, pathname: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileRangeResponse(_message.Message):
    __slots__ = ("result", "err_code")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    result: int
    err_code: int
    def __init__(self, result: _Optional[int] = ..., err_code: _Optional[int] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("pathname", "count", "offset")
    PATHNAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    pathname: str
    count: int
    offset: int
    def __init__(self, pathname: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileRangeResponse(_message.Message):
    __slots__ = ("result", "err_code")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    result: int
    err_code: int
    def __init__(self, result: _Optional[int] = ..., err_code: _Optional[int] = ...) -> None: ...
