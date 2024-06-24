from apollo.mr.base import histogram_proto_pb2 as _histogram_proto_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SummarizedChunkStatsProto(_message.Message):
    __slots__ = ("chunk_count", "chunk_bytes_logical", "chunk_bytes_morphed", "chunk_bytes_physical", "logical_size_histogram", "chunk_bytes_morphed_local")
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_MORPHED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_MORPHED_LOCAL_FIELD_NUMBER: _ClassVar[int]
    chunk_count: int
    chunk_bytes_logical: int
    chunk_bytes_morphed: int
    chunk_bytes_physical: int
    logical_size_histogram: _histogram_proto_pb2.HistogramProto
    chunk_bytes_morphed_local: int
    def __init__(self, chunk_count: _Optional[int] = ..., chunk_bytes_logical: _Optional[int] = ..., chunk_bytes_morphed: _Optional[int] = ..., chunk_bytes_physical: _Optional[int] = ..., logical_size_histogram: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ..., chunk_bytes_morphed_local: _Optional[int] = ...) -> None: ...
