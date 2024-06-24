from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSuccess: _ClassVar[ErrorCode]
    kAlreadyExists: _ClassVar[ErrorCode]
    kUnknownError: _ClassVar[ErrorCode]
kSuccess: ErrorCode
kAlreadyExists: ErrorCode
kUnknownError: ErrorCode

class CreateFile(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class ReadFile(_message.Message):
    __slots__ = ("filename", "count", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    count: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., count: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("error", "content", "eof")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    content: bytes
    eof: bool
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ..., content: _Optional[bytes] = ..., eof: bool = ...) -> None: ...

class WriteFile(_message.Message):
    __slots__ = ("filename", "offset", "content", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    content: bytes
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., content: _Optional[bytes] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...
