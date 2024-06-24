from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompressionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCompressionNone: _ClassVar[CompressionLevel]
    kCompressionLow: _ClassVar[CompressionLevel]
    kCompressionHigh: _ClassVar[CompressionLevel]
    kCompressionSnappy: _ClassVar[CompressionLevel]
    kCompressionGZip: _ClassVar[CompressionLevel]
    kCompressionLZ4: _ClassVar[CompressionLevel]
    kCompressionZSTDLow: _ClassVar[CompressionLevel]
    kCompressionZSTDHigh: _ClassVar[CompressionLevel]
kCompressionNone: CompressionLevel
kCompressionLow: CompressionLevel
kCompressionHigh: CompressionLevel
kCompressionSnappy: CompressionLevel
kCompressionGZip: CompressionLevel
kCompressionLZ4: CompressionLevel
kCompressionZSTDLow: CompressionLevel
kCompressionZSTDHigh: CompressionLevel

class ByteRange(_message.Message):
    __slots__ = ("logical_offset", "write_offset", "write_length", "adler32_cksum", "block_offset", "logical_length", "compression_level", "compressed_length")
    LOGICAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WRITE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WRITE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ADLER32_CKSUM_FIELD_NUMBER: _ClassVar[int]
    BLOCK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_LENGTH_FIELD_NUMBER: _ClassVar[int]
    logical_offset: int
    write_offset: int
    write_length: int
    adler32_cksum: int
    block_offset: int
    logical_length: int
    compression_level: CompressionLevel
    compressed_length: int
    def __init__(self, logical_offset: _Optional[int] = ..., write_offset: _Optional[int] = ..., write_length: _Optional[int] = ..., adler32_cksum: _Optional[int] = ..., block_offset: _Optional[int] = ..., logical_length: _Optional[int] = ..., compression_level: _Optional[_Union[CompressionLevel, str]] = ..., compressed_length: _Optional[int] = ...) -> None: ...

class FlushData(_message.Message):
    __slots__ = ("epoch_id", "sequence_id", "blob_offset", "write_length", "flush_finish_usecs")
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
    WRITE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    FLUSH_FINISH_USECS_FIELD_NUMBER: _ClassVar[int]
    epoch_id: int
    sequence_id: int
    blob_offset: int
    write_length: int
    flush_finish_usecs: int
    def __init__(self, epoch_id: _Optional[int] = ..., sequence_id: _Optional[int] = ..., blob_offset: _Optional[int] = ..., write_length: _Optional[int] = ..., flush_finish_usecs: _Optional[int] = ...) -> None: ...

class MetadataRecord(_message.Message):
    __slots__ = ("sequence_id", "writes", "max_committed_sequence_id", "flushes", "is_random", "stats_container_id", "write_issue_usecs", "qos_principal_id", "view_id")
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    WRITES_FIELD_NUMBER: _ClassVar[int]
    MAX_COMMITTED_SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    FLUSHES_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    WRITE_ISSUE_USECS_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    sequence_id: int
    writes: _containers.RepeatedCompositeFieldContainer[ByteRange]
    max_committed_sequence_id: int
    flushes: _containers.RepeatedCompositeFieldContainer[FlushData]
    is_random: bool
    stats_container_id: int
    write_issue_usecs: int
    qos_principal_id: int
    view_id: int
    def __init__(self, sequence_id: _Optional[int] = ..., writes: _Optional[_Iterable[_Union[ByteRange, _Mapping]]] = ..., max_committed_sequence_id: _Optional[int] = ..., flushes: _Optional[_Iterable[_Union[FlushData, _Mapping]]] = ..., is_random: bool = ..., stats_container_id: _Optional[int] = ..., write_issue_usecs: _Optional[int] = ..., qos_principal_id: _Optional[int] = ..., view_id: _Optional[int] = ...) -> None: ...
