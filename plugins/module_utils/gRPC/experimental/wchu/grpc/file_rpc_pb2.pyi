from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Success: _ClassVar[Result]
    FileAlreadyExists: _ClassVar[Result]
    FileDoesNotExist: _ClassVar[Result]
    PermissionDenied: _ClassVar[Result]
    FileSystemError: _ClassVar[Result]
    InvalidOffset: _ClassVar[Result]
    BadRequest: _ClassVar[Result]
Success: Result
FileAlreadyExists: Result
FileDoesNotExist: Result
PermissionDenied: Result
FileSystemError: Result
InvalidOffset: Result
BadRequest: Result

class FileCreationReq(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class FileCreationResp(_message.Message):
    __slots__ = ("name", "result")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    result: Result
    def __init__(self, name: _Optional[str] = ..., result: _Optional[_Union[Result, str]] = ...) -> None: ...

class WriteFileRangeReq(_message.Message):
    __slots__ = ("name", "offset", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    data: bytes
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeResp(_message.Message):
    __slots__ = ("name", "offset", "size", "result")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    size: int
    result: Result
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., result: _Optional[_Union[Result, str]] = ...) -> None: ...

class ReadFileRangeReq(_message.Message):
    __slots__ = ("name", "offset", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    size: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ReadFileRangeResp(_message.Message):
    __slots__ = ("name", "offset", "size", "result", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    size: int
    result: Result
    data: bytes
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., result: _Optional[_Union[Result, str]] = ..., data: _Optional[bytes] = ...) -> None: ...
