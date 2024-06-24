from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FullCFM(_message.Message):
    __slots__ = ("master_column", "chunk_vec", "chunk_group_vec", "scribe_version")
    class ChunkInfo(_message.Message):
        __slots__ = ("chunk_id", "chunk_column")
        CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
        chunk_id: _blob_store_pb2.ChunkIdProto
        chunk_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkColumn
        def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., chunk_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ...) -> None: ...
    class ChunkGroupInfo(_message.Message):
        __slots__ = ("chunk_group_id", "chunk_group_column")
        CHUNK_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_GROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
        chunk_group_id: int
        chunk_group_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn
        def __init__(self, chunk_group_id: _Optional[int] = ..., chunk_group_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ...) -> None: ...
    MASTER_COLUMN_FIELD_NUMBER: _ClassVar[int]
    CHUNK_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    master_column: _blob_store_pb2.ChunkFileMetadataProto.MasterColumn
    chunk_vec: _containers.RepeatedCompositeFieldContainer[FullCFM.ChunkInfo]
    chunk_group_vec: _containers.RepeatedCompositeFieldContainer[FullCFM.ChunkGroupInfo]
    scribe_version: int
    def __init__(self, master_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.MasterColumn, _Mapping]] = ..., chunk_vec: _Optional[_Iterable[_Union[FullCFM.ChunkInfo, _Mapping]]] = ..., chunk_group_vec: _Optional[_Iterable[_Union[FullCFM.ChunkGroupInfo, _Mapping]]] = ..., scribe_version: _Optional[int] = ...) -> None: ...
