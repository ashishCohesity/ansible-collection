from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("error", "error_msg")
    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[CreateFileResponse.Error]
        kInvalidArgs: _ClassVar[CreateFileResponse.Error]
        kUnableToCreate: _ClassVar[CreateFileResponse.Error]
    kNoError: CreateFileResponse.Error
    kInvalidArgs: CreateFileResponse.Error
    kUnableToCreate: CreateFileResponse.Error
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error: CreateFileResponse.Error
    error_msg: str
    def __init__(self, error: _Optional[_Union[CreateFileResponse.Error, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class ReadFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class ReadFileResponse(_message.Message):
    __slots__ = ("error", "error_msg")
    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ReadFileResponse.Error]
        kInvalidArgs: _ClassVar[ReadFileResponse.Error]
        kUnableToOpen: _ClassVar[ReadFileResponse.Error]
        kUnableToRead: _ClassVar[ReadFileResponse.Error]
        kEOFReached: _ClassVar[ReadFileResponse.Error]
    kNoError: ReadFileResponse.Error
    kInvalidArgs: ReadFileResponse.Error
    kUnableToOpen: ReadFileResponse.Error
    kUnableToRead: ReadFileResponse.Error
    kEOFReached: ReadFileResponse.Error
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error: ReadFileResponse.Error
    error_msg: str
    def __init__(self, error: _Optional[_Union[ReadFileResponse.Error, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class WriteFileRequest(_message.Message):
    __slots__ = ("file_name", "offset", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    length: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class WriteFileResponse(_message.Message):
    __slots__ = ("error", "error_msg")
    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[WriteFileResponse.Error]
        kInvalidArgs: _ClassVar[WriteFileResponse.Error]
        kUnableToOpen: _ClassVar[WriteFileResponse.Error]
        kUnableToWrite: _ClassVar[WriteFileResponse.Error]
    kNoError: WriteFileResponse.Error
    kInvalidArgs: WriteFileResponse.Error
    kUnableToOpen: WriteFileResponse.Error
    kUnableToWrite: WriteFileResponse.Error
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error: WriteFileResponse.Error
    error_msg: str
    def __init__(self, error: _Optional[_Union[WriteFileResponse.Error, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
