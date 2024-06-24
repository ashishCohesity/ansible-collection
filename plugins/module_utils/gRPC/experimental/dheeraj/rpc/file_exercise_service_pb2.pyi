from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileExerciseRequest(_message.Message):
    __slots__ = ("type", "file", "length", "offset", "data")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        READ: _ClassVar[FileExerciseRequest.Type]
        WRITE: _ClassVar[FileExerciseRequest.Type]
        CREATE: _ClassVar[FileExerciseRequest.Type]
    READ: FileExerciseRequest.Type
    WRITE: FileExerciseRequest.Type
    CREATE: FileExerciseRequest.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: FileExerciseRequest.Type
    file: str
    length: int
    offset: int
    data: str
    def __init__(self, type: _Optional[_Union[FileExerciseRequest.Type, str]] = ..., file: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ..., data: _Optional[str] = ...) -> None: ...

class FileExerciseResult(_message.Message):
    __slots__ = ("success", "timestamp", "result")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    timestamp: int
    result: str
    def __init__(self, success: bool = ..., timestamp: _Optional[int] = ..., result: _Optional[str] = ...) -> None: ...
