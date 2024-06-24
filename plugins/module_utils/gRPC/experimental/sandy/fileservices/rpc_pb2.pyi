from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSuccess: _ClassVar[ErrorCode]
    kUnknownError: _ClassVar[ErrorCode]
    rwSuccess: _ClassVar[ErrorCode]
    rwUnknownError: _ClassVar[ErrorCode]
kSuccess: ErrorCode
kUnknownError: ErrorCode
rwSuccess: ErrorCode
rwUnknownError: ErrorCode

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
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFile(_message.Message):
    __slots__ = ("data", "filename", "offset", "len")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    data: str
    filename: str
    offset: int
    len: int
    def __init__(self, data: _Optional[str] = ..., filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("error", "errormsg", "data")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    errormsg: str
    data: str
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ..., errormsg: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("error", "errormsg")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    error: ErrorCode
    errormsg: str
    def __init__(self, error: _Optional[_Union[ErrorCode, str]] = ..., errormsg: _Optional[str] = ...) -> None: ...
