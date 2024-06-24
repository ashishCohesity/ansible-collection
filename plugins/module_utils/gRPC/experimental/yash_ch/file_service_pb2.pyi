from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateResult(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: int
    def __init__(self, response: _Optional[int] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("filename", "offset", "read_length")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    READ_LENGTH_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    read_length: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., read_length: _Optional[int] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("buffer", "seqno", "response")
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    buffer: str
    seqno: int
    response: int
    def __init__(self, buffer: _Optional[str] = ..., seqno: _Optional[int] = ..., response: _Optional[int] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ("filename", "offset", "buffer")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    buffer: str
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., buffer: _Optional[str] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("response", "seqno", "length_written")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    LENGTH_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    response: int
    seqno: int
    length_written: int
    def __init__(self, response: _Optional[int] = ..., seqno: _Optional[int] = ..., length_written: _Optional[int] = ...) -> None: ...
