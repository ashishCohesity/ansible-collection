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

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFileReq(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class ReadFileReq(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileReq(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class HelloResult(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...

class CreateFileRes(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class ReadFileRes(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class WriteFileRes(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...
