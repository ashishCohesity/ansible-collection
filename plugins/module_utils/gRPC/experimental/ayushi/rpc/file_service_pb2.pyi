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

class HandShakeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HandShakeResponse(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error", "eof")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    eof: bool
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ..., eof: bool = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("filename", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("timestamp", "error")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    error: ErrorCode
    def __init__(self, timestamp: _Optional[int] = ..., error: _Optional[_Union[ErrorCode, str]] = ...) -> None: ...
