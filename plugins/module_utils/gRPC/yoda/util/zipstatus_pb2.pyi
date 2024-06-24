from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ZipStatus(_message.Message):
    __slots__ = ("state", "entry_count", "source_bytes_added", "metadata", "volume_name")
    class ZipState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrestart: _ClassVar[ZipStatus.ZipState]
        kStart: _ClassVar[ZipStatus.ZipState]
        kPrecommit: _ClassVar[ZipStatus.ZipState]
        kCommit: _ClassVar[ZipStatus.ZipState]
    kPrestart: ZipStatus.ZipState
    kStart: ZipStatus.ZipState
    kPrecommit: ZipStatus.ZipState
    kCommit: ZipStatus.ZipState
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BYTES_ADDED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    state: ZipStatus.ZipState
    entry_count: int
    source_bytes_added: int
    metadata: _directory_walker_pb2.EntityMetadata
    volume_name: str
    def __init__(self, state: _Optional[_Union[ZipStatus.ZipState, str]] = ..., entry_count: _Optional[int] = ..., source_bytes_added: _Optional[int] = ..., metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., volume_name: _Optional[str] = ...) -> None: ...
