from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNoError: _ClassVar[ErrorType]
    kFileExists: _ClassVar[ErrorType]
    kCreateError: _ClassVar[ErrorType]
    kFileNotExists: _ClassVar[ErrorType]
    kOther: _ClassVar[ErrorType]
kNoError: ErrorType
kFileExists: ErrorType
kCreateError: ErrorType
kFileNotExists: ErrorType
kOther: ErrorType

class CreateFileReqArg(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class ReadFileReqArg(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileReqArg(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class CreateFileResArg(_message.Message):
    __slots__ = ("error", "errorstr")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORSTR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorType
    errorstr: str
    def __init__(self, error: _Optional[_Union[ErrorType, str]] = ..., errorstr: _Optional[str] = ...) -> None: ...

class ReadFileResArg(_message.Message):
    __slots__ = ("error", "errorstr")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORSTR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorType
    errorstr: str
    def __init__(self, error: _Optional[_Union[ErrorType, str]] = ..., errorstr: _Optional[str] = ...) -> None: ...

class WriteFileResArg(_message.Message):
    __slots__ = ("error", "errorstr")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORSTR_FIELD_NUMBER: _ClassVar[int]
    error: ErrorType
    errorstr: str
    def __init__(self, error: _Optional[_Union[ErrorType, str]] = ..., errorstr: _Optional[str] = ...) -> None: ...
