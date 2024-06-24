from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MorphBricksContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class MorphBricksMapKeyProto(_message.Message):
    __slots__ = ("blob_snap_tree_id",)
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    def __init__(self, blob_snap_tree_id: _Optional[int] = ...) -> None: ...

class MorphBricksMapValueProto(_message.Message):
    __slots__ = ("brick_number", "can_dedup_in_isolation", "blob_root_info", "view_box_id", "chunk_count")
    class BlobRootInfo(_message.Message):
        __slots__ = ("stored_refcount", "expected_scribe_version")
        STORED_REFCOUNT_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        stored_refcount: int
        expected_scribe_version: int
        def __init__(self, stored_refcount: _Optional[int] = ..., expected_scribe_version: _Optional[int] = ...) -> None: ...
    BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CAN_DEDUP_IN_ISOLATION_FIELD_NUMBER: _ClassVar[int]
    BLOB_ROOT_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    brick_number: int
    can_dedup_in_isolation: bool
    blob_root_info: MorphBricksMapValueProto.BlobRootInfo
    view_box_id: int
    chunk_count: int
    def __init__(self, brick_number: _Optional[int] = ..., can_dedup_in_isolation: bool = ..., blob_root_info: _Optional[_Union[MorphBricksMapValueProto.BlobRootInfo, _Mapping]] = ..., view_box_id: _Optional[int] = ..., chunk_count: _Optional[int] = ...) -> None: ...

class BlobDedupableBrickRanges(_message.Message):
    __slots__ = ("brick_range_vec", "view_box_id")
    class BrickRange(_message.Message):
        __slots__ = ("start_brick_number", "num_bricks", "avg_chunk_count")
        START_BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NUM_BRICKS_FIELD_NUMBER: _ClassVar[int]
        AVG_CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        start_brick_number: int
        num_bricks: int
        avg_chunk_count: int
        def __init__(self, start_brick_number: _Optional[int] = ..., num_bricks: _Optional[int] = ..., avg_chunk_count: _Optional[int] = ...) -> None: ...
    BRICK_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    brick_range_vec: _containers.RepeatedCompositeFieldContainer[BlobDedupableBrickRanges.BrickRange]
    view_box_id: int
    def __init__(self, brick_range_vec: _Optional[_Iterable[_Union[BlobDedupableBrickRanges.BrickRange, _Mapping]]] = ..., view_box_id: _Optional[int] = ...) -> None: ...
