from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleFileServiceErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kErrorSuccess: _ClassVar[SampleFileServiceErrorCode]
    kErrorFileNotFound: _ClassVar[SampleFileServiceErrorCode]
    kErrorInternal: _ClassVar[SampleFileServiceErrorCode]
    kErrorUnknown: _ClassVar[SampleFileServiceErrorCode]
kErrorSuccess: SampleFileServiceErrorCode
kErrorFileNotFound: SampleFileServiceErrorCode
kErrorInternal: SampleFileServiceErrorCode
kErrorUnknown: SampleFileServiceErrorCode

class FileRange(_message.Message):
    __slots__ = ("offset", "length")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: SampleFileServiceErrorCode
    def __init__(self, error: _Optional[_Union[SampleFileServiceErrorCode, str]] = ...) -> None: ...

class ReadFileRangeArg(_message.Message):
    __slots__ = ("file_name", "extent")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    extent: FileRange
    def __init__(self, file_name: _Optional[str] = ..., extent: _Optional[_Union[FileRange, _Mapping]] = ...) -> None: ...

class ReadFileRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: SampleFileServiceErrorCode
    def __init__(self, error: _Optional[_Union[SampleFileServiceErrorCode, str]] = ...) -> None: ...

class WriteFileRangeArg(_message.Message):
    __slots__ = ("file_name", "extent")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    extent: FileRange
    def __init__(self, file_name: _Optional[str] = ..., extent: _Optional[_Union[FileRange, _Mapping]] = ...) -> None: ...

class WriteFileRangeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: SampleFileServiceErrorCode
    def __init__(self, error: _Optional[_Union[SampleFileServiceErrorCode, str]] = ...) -> None: ...

class SampleFileServicePingArg(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SampleFileServicePingResult(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...
