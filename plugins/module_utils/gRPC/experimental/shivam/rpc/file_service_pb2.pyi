from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileRequest(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: File
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ...) -> None: ...

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

class ReadFileRangeRequest(_message.Message):
    __slots__ = ("file", "offset", "len")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file: File
    offset: int
    len: int
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class ReadFileRangeResponse(_message.Message):
    __slots__ = ("error", "error_msg")
    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ReadFileRangeResponse.Error]
        kInvalidArgs: _ClassVar[ReadFileRangeResponse.Error]
        kUnableToOpen: _ClassVar[ReadFileRangeResponse.Error]
        kUnableToRead: _ClassVar[ReadFileRangeResponse.Error]
        kEOF: _ClassVar[ReadFileRangeResponse.Error]
    kNoError: ReadFileRangeResponse.Error
    kInvalidArgs: ReadFileRangeResponse.Error
    kUnableToOpen: ReadFileRangeResponse.Error
    kUnableToRead: ReadFileRangeResponse.Error
    kEOF: ReadFileRangeResponse.Error
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error: ReadFileRangeResponse.Error
    error_msg: str
    def __init__(self, error: _Optional[_Union[ReadFileRangeResponse.Error, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class WriteFileRangeRequest(_message.Message):
    __slots__ = ("file", "offset", "len")
    FILE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file: File
    offset: int
    len: int
    def __init__(self, file: _Optional[_Union[File, _Mapping]] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class WriteFileRangeResponse(_message.Message):
    __slots__ = ("error", "error_msg")
    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[WriteFileRangeResponse.Error]
        kInvalidArgs: _ClassVar[WriteFileRangeResponse.Error]
        kInvalidPayload: _ClassVar[WriteFileRangeResponse.Error]
        kUnableToOpen: _ClassVar[WriteFileRangeResponse.Error]
        kUnableToWrite: _ClassVar[WriteFileRangeResponse.Error]
    kNoError: WriteFileRangeResponse.Error
    kInvalidArgs: WriteFileRangeResponse.Error
    kInvalidPayload: WriteFileRangeResponse.Error
    kUnableToOpen: WriteFileRangeResponse.Error
    kUnableToWrite: WriteFileRangeResponse.Error
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error: WriteFileRangeResponse.Error
    error_msg: str
    def __init__(self, error: _Optional[_Union[WriteFileRangeResponse.Error, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...
