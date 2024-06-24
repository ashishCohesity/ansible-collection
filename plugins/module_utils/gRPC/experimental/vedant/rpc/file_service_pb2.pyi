from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileIORequest(_message.Message):
    __slots__ = ("type", "file_index", "offset", "length")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFileCreate: _ClassVar[FileIORequest.RequestType]
        kFileRead: _ClassVar[FileIORequest.RequestType]
        kFileWrite: _ClassVar[FileIORequest.RequestType]
    kFileCreate: FileIORequest.RequestType
    kFileRead: FileIORequest.RequestType
    kFileWrite: FileIORequest.RequestType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_INDEX_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    type: FileIORequest.RequestType
    file_index: int
    offset: int
    length: int
    def __init__(self, type: _Optional[_Union[FileIORequest.RequestType, str]] = ..., file_index: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class FileIOResult(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...
