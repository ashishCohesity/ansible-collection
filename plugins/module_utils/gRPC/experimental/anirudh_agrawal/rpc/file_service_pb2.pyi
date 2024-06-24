from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(_message.Message):
    __slots__ = ("code", "error_detail")
    class StatusCodes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[Status.StatusCodes]
        kWriteFailed: _ClassVar[Status.StatusCodes]
        kReadFailed: _ClassVar[Status.StatusCodes]
        kReadInvalidRange: _ClassVar[Status.StatusCodes]
        kCannotOpenFile: _ClassVar[Status.StatusCodes]
    kNoError: Status.StatusCodes
    kWriteFailed: Status.StatusCodes
    kReadFailed: Status.StatusCodes
    kReadInvalidRange: Status.StatusCodes
    kCannotOpenFile: Status.StatusCodes
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    code: Status.StatusCodes
    error_detail: str
    def __init__(self, code: _Optional[_Union[Status.StatusCodes, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "len")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("status", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: Status
    data: str
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., data: _Optional[str] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("filename", "offset", "len", "data")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    len: int
    data: str
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("status", "len")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    status: Status
    len: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., len: _Optional[int] = ...) -> None: ...
