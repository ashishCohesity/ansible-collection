from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileCreationRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class FileCreationResult(_message.Message):
    __slots__ = ("response", "status_code")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    response: str
    status_code: int
    def __init__(self, response: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...

class ReadWriteRangeRequest(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadWriteRangeResult(_message.Message):
    __slots__ = ("response", "status_code")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    response: str
    status_code: int
    def __init__(self, response: _Optional[str] = ..., status_code: _Optional[int] = ...) -> None: ...
