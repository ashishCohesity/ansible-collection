from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorProto(_message.Message):
    __slots__ = ("code", "error_detail")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[ErrorProto.Code]
        kInvalidArgument: _ClassVar[ErrorProto.Code]
        kReadError: _ClassVar[ErrorProto.Code]
        kWriteError: _ClassVar[ErrorProto.Code]
    kNoError: ErrorProto.Code
    kInvalidArgument: ErrorProto.Code
    kReadError: ErrorProto.Code
    kWriteError: ErrorProto.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    code: ErrorProto.Code
    error_detail: str
    def __init__(self, code: _Optional[_Union[ErrorProto.Code, str]] = ..., error_detail: _Optional[str] = ...) -> None: ...

class ListFilesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFilesRet(_message.Message):
    __slots__ = ("error", "file_names")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_NAMES_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    file_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ..., file_names: _Optional[_Iterable[str]] = ...) -> None: ...

class RangeSpec(_message.Message):
    __slots__ = ("offset", "size")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("file_name", "write_range")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    WRITE_RANGE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    write_range: RangeSpec
    def __init__(self, file_name: _Optional[str] = ..., write_range: _Optional[_Union[RangeSpec, _Mapping]] = ...) -> None: ...

class CreateFileRet(_message.Message):
    __slots__ = ("error", "timestamp", "bytes_written")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    timestamp: int
    bytes_written: int
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ..., timestamp: _Optional[int] = ..., bytes_written: _Optional[int] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("file_name", "read_range", "timestamp")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    READ_RANGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    read_range: RangeSpec
    timestamp: int
    def __init__(self, file_name: _Optional[str] = ..., read_range: _Optional[_Union[RangeSpec, _Mapping]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ReadFileRangeRet(_message.Message):
    __slots__ = ("error", "timestamp", "bytes_read")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    timestamp: int
    bytes_read: int
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ..., timestamp: _Optional[int] = ..., bytes_read: _Optional[int] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("file_name", "write_range")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    WRITE_RANGE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    write_range: RangeSpec
    def __init__(self, file_name: _Optional[str] = ..., write_range: _Optional[_Union[RangeSpec, _Mapping]] = ...) -> None: ...

class WriteFileRangeRet(_message.Message):
    __slots__ = ("error", "timestamp", "bytes_written")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BYTES_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    error: ErrorProto
    timestamp: int
    bytes_written: int
    def __init__(self, error: _Optional[_Union[ErrorProto, _Mapping]] = ..., timestamp: _Optional[int] = ..., bytes_written: _Optional[int] = ...) -> None: ...
