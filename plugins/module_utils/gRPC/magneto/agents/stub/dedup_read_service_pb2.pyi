from bridge.snap_fs import dedup_range_pb2 as _dedup_range_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadSliceDedupArg(_message.Message):
    __slots__ = ("header", "volume_dev_path", "read_from_volume_device", "guid", "data_region", "missing_dedup_range", "chunking_args", "volume_type", "volume_size_bytes")
    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnapshot: _ClassVar[ReadSliceDedupArg.VolumeType]
        kAttachedDisk: _ClassVar[ReadSliceDedupArg.VolumeType]
    kSnapshot: ReadSliceDedupArg.VolumeType
    kAttachedDisk: ReadSliceDedupArg.VolumeType
    class DataRegion(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    class ChunkingArgs(_message.Message):
        __slots__ = ("min_dedup_chunk_size", "max_dedup_chunk_size", "non_dedup_chunk_size")
        MIN_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        NON_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        min_dedup_chunk_size: int
        max_dedup_chunk_size: int
        non_dedup_chunk_size: int
        def __init__(self, min_dedup_chunk_size: _Optional[int] = ..., max_dedup_chunk_size: _Optional[int] = ..., non_dedup_chunk_size: _Optional[int] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    READ_FROM_VOLUME_DEVICE_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    DATA_REGION_FIELD_NUMBER: _ClassVar[int]
    MISSING_DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    CHUNKING_ARGS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    volume_dev_path: str
    read_from_volume_device: bool
    guid: bytes
    data_region: ReadSliceDedupArg.DataRegion
    missing_dedup_range: _dedup_range_pb2.DedupRange
    chunking_args: ReadSliceDedupArg.ChunkingArgs
    volume_type: ReadSliceDedupArg.VolumeType
    volume_size_bytes: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., volume_dev_path: _Optional[str] = ..., read_from_volume_device: bool = ..., guid: _Optional[bytes] = ..., data_region: _Optional[_Union[ReadSliceDedupArg.DataRegion, _Mapping]] = ..., missing_dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., chunking_args: _Optional[_Union[ReadSliceDedupArg.ChunkingArgs, _Mapping]] = ..., volume_type: _Optional[_Union[ReadSliceDedupArg.VolumeType, str]] = ..., volume_size_bytes: _Optional[int] = ...) -> None: ...

class ReadSliceDedupResult(_message.Message):
    __slots__ = ("error", "dedup_range", "data", "eof", "io_latency_usecs", "dedup_compute_time_usecs", "num_cache_hits", "num_cache_misses")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    IO_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_COMPUTE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    NUM_CACHE_MISSES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dedup_range: _dedup_range_pb2.DedupRange
    data: bytes
    eof: bool
    io_latency_usecs: int
    dedup_compute_time_usecs: int
    num_cache_hits: int
    num_cache_misses: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dedup_range: _Optional[_Union[_dedup_range_pb2.DedupRange, _Mapping]] = ..., data: _Optional[bytes] = ..., eof: bool = ..., io_latency_usecs: _Optional[int] = ..., dedup_compute_time_usecs: _Optional[int] = ..., num_cache_hits: _Optional[int] = ..., num_cache_misses: _Optional[int] = ...) -> None: ...
