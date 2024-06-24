from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: str
    def __init__(self, file: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file", "offset", "length")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file: str
    offset: int
    length: int
    def __init__(self, file: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileResult(_message.Message):
    __slots__ = ("status", "order_no")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_NO_FIELD_NUMBER: _ClassVar[int]
    status: bool
    order_no: int
    def __init__(self, status: bool = ..., order_no: _Optional[int] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file", "offset", "length")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file: str
    offset: int
    length: int
    def __init__(self, file: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("status", "order_no")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_NO_FIELD_NUMBER: _ClassVar[int]
    status: bool
    order_no: int
    def __init__(self, status: bool = ..., order_no: _Optional[int] = ...) -> None: ...
