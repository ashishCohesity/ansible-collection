from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileAuditProto(_message.Message):
    __slots__ = ("op_type", "blob_id", "chunk_file_state_vec", "destination_chunk_file_id_vec", "opclock", "start_usecs")
    class ChunkFileOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[ChunkFileAuditProto.ChunkFileOpType]
        kDeleteChunks: _ClassVar[ChunkFileAuditProto.ChunkFileOpType]
        kMigrateChunks: _ClassVar[ChunkFileAuditProto.ChunkFileOpType]
        kWriteChunks: _ClassVar[ChunkFileAuditProto.ChunkFileOpType]
        kDowntierChunksToCloud: _ClassVar[ChunkFileAuditProto.ChunkFileOpType]
        kFixDeleteChunks: _ClassVar[ChunkFileAuditProto.ChunkFileOpType]
    kUnknown: ChunkFileAuditProto.ChunkFileOpType
    kDeleteChunks: ChunkFileAuditProto.ChunkFileOpType
    kMigrateChunks: ChunkFileAuditProto.ChunkFileOpType
    kWriteChunks: ChunkFileAuditProto.ChunkFileOpType
    kDowntierChunksToCloud: ChunkFileAuditProto.ChunkFileOpType
    kFixDeleteChunks: ChunkFileAuditProto.ChunkFileOpType
    class NonDedupChunkDetails(_message.Message):
        __slots__ = ("chunk_id", "snap_tree_leaf_node_id")
        CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        chunk_id: _blob_store_pb2.ChunkIdProto
        snap_tree_leaf_node_id: int
        def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., snap_tree_leaf_node_id: _Optional[int] = ...) -> None: ...
    class ChunkFileState(_message.Message):
        __slots__ = ("chunk_file_id", "error", "ndd_chunk_details_vec")
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        NDD_CHUNK_DETAILS_VEC_FIELD_NUMBER: _ClassVar[int]
        chunk_file_id: int
        error: int
        ndd_chunk_details_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileAuditProto.NonDedupChunkDetails]
        def __init__(self, chunk_file_id: _Optional[int] = ..., error: _Optional[int] = ..., ndd_chunk_details_vec: _Optional[_Iterable[_Union[ChunkFileAuditProto.NonDedupChunkDetails, _Mapping]]] = ...) -> None: ...
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_FIELD_NUMBER: _ClassVar[int]
    START_USECS_FIELD_NUMBER: _ClassVar[int]
    op_type: ChunkFileAuditProto.ChunkFileOpType
    blob_id: int
    chunk_file_state_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileAuditProto.ChunkFileState]
    destination_chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    opclock: _op_clock_pb2.OpClock
    start_usecs: int
    def __init__(self, op_type: _Optional[_Union[ChunkFileAuditProto.ChunkFileOpType, str]] = ..., blob_id: _Optional[int] = ..., chunk_file_state_vec: _Optional[_Iterable[_Union[ChunkFileAuditProto.ChunkFileState, _Mapping]]] = ..., destination_chunk_file_id_vec: _Optional[_Iterable[int]] = ..., opclock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., start_usecs: _Optional[int] = ...) -> None: ...
