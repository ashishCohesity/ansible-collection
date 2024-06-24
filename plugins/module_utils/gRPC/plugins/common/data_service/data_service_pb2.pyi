from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataServiceOpenRequest(_message.Message):
    __slots__ = ("path", "mode")
    class FileOpenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        READ: _ClassVar[DataServiceOpenRequest.FileOpenMode]
        WRITE: _ClassVar[DataServiceOpenRequest.FileOpenMode]
    READ: DataServiceOpenRequest.FileOpenMode
    WRITE: DataServiceOpenRequest.FileOpenMode
    PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    path: str
    mode: DataServiceOpenRequest.FileOpenMode
    def __init__(self, path: _Optional[str] = ..., mode: _Optional[_Union[DataServiceOpenRequest.FileOpenMode, str]] = ...) -> None: ...

class DataServiceCloseRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class DataServiceReadRequest(_message.Message):
    __slots__ = ("path", "offset", "length")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    length: int
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class DataServiceWriteRequest(_message.Message):
    __slots__ = ("path", "data", "offset")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    path: str
    data: bytes
    offset: int
    def __init__(self, path: _Optional[str] = ..., data: _Optional[bytes] = ..., offset: _Optional[int] = ...) -> None: ...

class DataServiceReadResponse(_message.Message):
    __slots__ = ("bytesRead", "data")
    BYTESREAD_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    bytesRead: int
    data: bytes
    def __init__(self, bytesRead: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class DataServiceOpenResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class DataServiceCloseResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class DataServiceWriteResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...
