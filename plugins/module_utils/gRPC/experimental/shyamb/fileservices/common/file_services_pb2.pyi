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

class CreateFileArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error_num", "err_str")
    ERROR_NUM_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    error_num: ErrorType
    err_str: str
    def __init__(self, error_num: _Optional[_Union[ErrorType, str]] = ..., err_str: _Optional[str] = ...) -> None: ...

class ReadFileArg(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("error_num", "err_str")
    ERROR_NUM_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    error_num: ErrorType
    err_str: str
    def __init__(self, error_num: _Optional[_Union[ErrorType, str]] = ..., err_str: _Optional[str] = ...) -> None: ...

class WriteFileArg(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("error_num", "err_str")
    ERROR_NUM_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    error_num: ErrorType
    err_str: str
    def __init__(self, error_num: _Optional[_Union[ErrorType, str]] = ..., err_str: _Optional[str] = ...) -> None: ...
