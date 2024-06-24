from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.storage import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GreetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GreetResult(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateResult(_message.Message):
    __slots__ = ("status", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: bool
    error: _error_pb2.ErrorProto
    def __init__(self, status: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("name", "length", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    length: int
    offset: int
    def __init__(self, name: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("r_bytes", "buf", "error")
    R_BYTES_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    r_bytes: int
    buf: str
    error: _error_pb2.ErrorProto
    def __init__(self, r_bytes: _Optional[int] = ..., buf: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("name", "buf", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUF_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    buf: str
    offset: int
    def __init__(self, name: _Optional[str] = ..., buf: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("w_bytes", "w_seqnum", "error")
    W_BYTES_FIELD_NUMBER: _ClassVar[int]
    W_SEQNUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    w_bytes: int
    w_seqnum: int
    error: _error_pb2.ErrorProto
    def __init__(self, w_bytes: _Optional[int] = ..., w_seqnum: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
