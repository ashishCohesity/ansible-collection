from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileCreateRequest(_message.Message):
    __slots__ = ("file_name", "file_extension")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_extension: str
    def __init__(self, file_name: _Optional[str] = ..., file_extension: _Optional[str] = ...) -> None: ...

class FileCreateResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class FileWriteRequest(_message.Message):
    __slots__ = ("file_name", "offset", "data_to_write", "write_mode")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_TO_WRITE_FIELD_NUMBER: _ClassVar[int]
    WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    data_to_write: bytes
    write_mode: str
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., data_to_write: _Optional[bytes] = ..., write_mode: _Optional[str] = ...) -> None: ...

class FileWriteResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class FileReadRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileReadResult(_message.Message):
    __slots__ = ("status", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: bool
    data: bytes
    def __init__(self, status: bool = ..., data: _Optional[bytes] = ...) -> None: ...
