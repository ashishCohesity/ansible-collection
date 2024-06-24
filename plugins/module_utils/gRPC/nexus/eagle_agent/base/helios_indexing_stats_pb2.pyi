from yoda.base import yoda_pb2 as _yoda_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IndexingStatsBatch(_message.Message):
    __slots__ = ("indexing_stats_vec",)
    INDEXING_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    indexing_stats_vec: _containers.RepeatedCompositeFieldContainer[_yoda_pb2.IndexingMetadataStats]
    def __init__(self, indexing_stats_vec: _Optional[_Iterable[_Union[_yoda_pb2.IndexingMetadataStats, _Mapping]]] = ...) -> None: ...
