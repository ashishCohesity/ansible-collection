from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: bool
    def __init__(self, error: bool = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("name", "leng", "offset", "send_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LENG_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEND_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    leng: int
    offset: int
    send_id: int
    def __init__(self, name: _Optional[str] = ..., leng: _Optional[int] = ..., offset: _Optional[int] = ..., send_id: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error", "data", "execid", "rcvrid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EXECID_FIELD_NUMBER: _ClassVar[int]
    RCVRID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    data: bytes
    execid: int
    rcvrid: int
    def __init__(self, error: bool = ..., data: _Optional[bytes] = ..., execid: _Optional[int] = ..., rcvrid: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("name", "data", "offset", "send_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEND_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: bytes
    offset: int
    send_id: int
    def __init__(self, name: _Optional[str] = ..., data: _Optional[bytes] = ..., offset: _Optional[int] = ..., send_id: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error", "execid", "rcvrid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECID_FIELD_NUMBER: _ClassVar[int]
    RCVRID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    execid: int
    rcvrid: int
    def __init__(self, error: bool = ..., execid: _Optional[int] = ..., rcvrid: _Optional[int] = ...) -> None: ...
