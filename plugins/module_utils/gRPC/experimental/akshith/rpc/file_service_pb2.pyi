from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileArg(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class ReadFileArg(_message.Message):
    __slots__ = ("filename", "offset", "length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("status", "sequence_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    status: bool
    sequence_id: int
    def __init__(self, status: bool = ..., sequence_id: _Optional[int] = ...) -> None: ...

class WriteFileArg(_message.Message):
    __slots__ = ("filename", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("status", "sequence_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    status: bool
    sequence_id: int
    def __init__(self, status: bool = ..., sequence_id: _Optional[int] = ...) -> None: ...
