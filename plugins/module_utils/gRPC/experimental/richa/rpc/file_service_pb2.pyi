from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("type", "error_msg")
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAlreadyExist: _ClassVar[Error.ErrorType]
        kSuccess: _ClassVar[Error.ErrorType]
        kUnknownError: _ClassVar[Error.ErrorType]
        kBadRequestError: _ClassVar[Error.ErrorType]
        kNoError: _ClassVar[Error.ErrorType]
        kInvalidParams: _ClassVar[Error.ErrorType]
    kAlreadyExist: Error.ErrorType
    kSuccess: Error.ErrorType
    kUnknownError: Error.ErrorType
    kBadRequestError: Error.ErrorType
    kNoError: Error.ErrorType
    kInvalidParams: Error.ErrorType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: Error.ErrorType
    error_msg: str
    def __init__(self, type: _Optional[_Union[Error.ErrorType, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class CreateArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("file_name", "len", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    len: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("content", "error")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    error: Error
    def __init__(self, content: _Optional[bytes] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("content", "offset", "file_name")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    offset: int
    file_name: str
    def __init__(self, content: _Optional[bytes] = ..., offset: _Optional[int] = ..., file_name: _Optional[str] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
