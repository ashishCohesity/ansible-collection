from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileCreateArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class FileCreateResult(_message.Message):
    __slots__ = ("type",)
    class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[FileCreateResult.ResultType]
        kAlreadyExists: _ClassVar[FileCreateResult.ResultType]
        kNoNameProvided: _ClassVar[FileCreateResult.ResultType]
        kUnknownError: _ClassVar[FileCreateResult.ResultType]
    kSuccess: FileCreateResult.ResultType
    kAlreadyExists: FileCreateResult.ResultType
    kNoNameProvided: FileCreateResult.ResultType
    kUnknownError: FileCreateResult.ResultType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: FileCreateResult.ResultType
    def __init__(self, type: _Optional[_Union[FileCreateResult.ResultType, str]] = ...) -> None: ...

class FileReadArg(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class FileReadResult(_message.Message):
    __slots__ = ("type",)
    class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[FileReadResult.ResultType]
        kNoNameProvided: _ClassVar[FileReadResult.ResultType]
        kFileDoesNotExist: _ClassVar[FileReadResult.ResultType]
        kUnknownError: _ClassVar[FileReadResult.ResultType]
    kSuccess: FileReadResult.ResultType
    kNoNameProvided: FileReadResult.ResultType
    kFileDoesNotExist: FileReadResult.ResultType
    kUnknownError: FileReadResult.ResultType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: FileReadResult.ResultType
    def __init__(self, type: _Optional[_Union[FileReadResult.ResultType, str]] = ...) -> None: ...

class FileWriteArg(_message.Message):
    __slots__ = ("file_name", "offset", "len")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    offset: int
    len: int
    def __init__(self, file_name: _Optional[str] = ..., offset: _Optional[int] = ..., len: _Optional[int] = ...) -> None: ...

class FileWriteResult(_message.Message):
    __slots__ = ("type",)
    class ResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[FileWriteResult.ResultType]
        kNoNameProvided: _ClassVar[FileWriteResult.ResultType]
        kFileDoesNotExist: _ClassVar[FileWriteResult.ResultType]
        kUnknownError: _ClassVar[FileWriteResult.ResultType]
    kSuccess: FileWriteResult.ResultType
    kNoNameProvided: FileWriteResult.ResultType
    kFileDoesNotExist: FileWriteResult.ResultType
    kUnknownError: FileWriteResult.ResultType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: FileWriteResult.ResultType
    def __init__(self, type: _Optional[_Union[FileWriteResult.ResultType, str]] = ...) -> None: ...
