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

class CreateFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

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
    __slots__ = ("error", "content", "eof")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    content: bytes
    eof: bool
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ..., content: _Optional[bytes] = ..., eof: bool = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("name", "content", "offset", "len")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: bytes
    offset: int
    len: int
    def __init__(self, name: _Optional[str] = ..., content: _Optional[bytes] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error", "check_sum")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHECK_SUM_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    check_sum: str
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ..., check_sum: _Optional[str] = ...) -> None: ...
