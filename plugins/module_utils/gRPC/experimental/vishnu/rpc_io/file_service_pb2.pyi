from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("outcome",)
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    outcome: bool
    def __init__(self, outcome: bool = ...) -> None: ...

class WriteToFileRequest(_message.Message):
    __slots__ = ("filename", "writesize", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    WRITESIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    writesize: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., writesize: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class WriteToFileResponse(_message.Message):
    __slots__ = ("exists", "success")
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    success: bool
    def __init__(self, exists: bool = ..., success: bool = ...) -> None: ...

class ReadFromFileRequest(_message.Message):
    __slots__ = ("filename", "readsize", "offset")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    READSIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filename: str
    readsize: int
    offset: int
    def __init__(self, filename: _Optional[str] = ..., readsize: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ReadFromFileResponse(_message.Message):
    __slots__ = ("exists", "success")
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    success: bool
    def __init__(self, exists: bool = ..., success: bool = ...) -> None: ...
