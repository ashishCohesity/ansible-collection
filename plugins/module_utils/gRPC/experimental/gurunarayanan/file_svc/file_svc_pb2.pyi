from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileReq(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFileResp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...

class ReadFileRangeReq(_message.Message):
    __slots__ = ("name", "offset", "len")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileRangeResp(_message.Message):
    __slots__ = ("status", "payload")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    status: int
    payload: bytes
    def __init__(self, status: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeReq(_message.Message):
    __slots__ = ("name", "offset", "len", "payload")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    len: int
    payload: bytes
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class WriteFileRangeResp(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: int
    def __init__(self, status: _Optional[int] = ...) -> None: ...
