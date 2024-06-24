from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class IOParams(_message.Message):
    __slots__ = ("file_name", "num_of_bytes", "offset")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_BYTES_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    num_of_bytes: int
    offset: int
    def __init__(self, file_name: _Optional[str] = ..., num_of_bytes: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("response", "execution_number")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    response: str
    execution_number: int
    def __init__(self, response: _Optional[str] = ..., execution_number: _Optional[int] = ...) -> None: ...
