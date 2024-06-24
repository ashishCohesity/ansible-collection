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
    __slots__ = ("name", "len", "offset", "send_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEND_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    len: int
    offset: int
    send_id: int
    def __init__(self, name: _Optional[str] = ..., len: _Optional[int] = ..., offset: _Optional[int] = ..., send_id: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error", "data", "exec_id", "rcv_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    RCV_ID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    data: bytes
    exec_id: int
    rcv_id: int
    def __init__(self, error: bool = ..., data: _Optional[bytes] = ..., exec_id: _Optional[int] = ..., rcv_id: _Optional[int] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("name", "content", "offset", "send_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEND_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: bytes
    offset: int
    send_id: int
    def __init__(self, name: _Optional[str] = ..., content: _Optional[bytes] = ..., offset: _Optional[int] = ..., send_id: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error", "exec_id", "rcv_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    RCV_ID_FIELD_NUMBER: _ClassVar[int]
    error: bool
    exec_id: int
    rcv_id: int
    def __init__(self, error: bool = ..., exec_id: _Optional[int] = ..., rcv_id: _Optional[int] = ...) -> None: ...
