from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChecksumLogProto(_message.Message):
    __slots__ = ("id", "file_identifier", "is_forwarded", "chunk_vec", "error", "request_type")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRead: _ClassVar[ChecksumLogProto.RequestType]
        kWrite: _ClassVar[ChecksumLogProto.RequestType]
    kRead: ChecksumLogProto.RequestType
    kWrite: ChecksumLogProto.RequestType
    class Chunk(_message.Message):
        __slots__ = ("offset", "length", "checksum", "sample_data")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_DATA_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        checksum: int
        sample_data: bytes
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., checksum: _Optional[int] = ..., sample_data: _Optional[bytes] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    file_identifier: str
    is_forwarded: bool
    chunk_vec: _containers.RepeatedCompositeFieldContainer[ChecksumLogProto.Chunk]
    error: int
    request_type: ChecksumLogProto.RequestType
    def __init__(self, id: _Optional[int] = ..., file_identifier: _Optional[str] = ..., is_forwarded: bool = ..., chunk_vec: _Optional[_Iterable[_Union[ChecksumLogProto.Chunk, _Mapping]]] = ..., error: _Optional[int] = ..., request_type: _Optional[_Union[ChecksumLogProto.RequestType, str]] = ...) -> None: ...
