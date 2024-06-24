from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MorphBricksContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_blob_snap_tree_level", "view_box_with_dedup_found")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOB_SNAP_TREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_WITH_DEDUP_FOUND_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_blob_snap_tree_level: int
    view_box_with_dedup_found: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_blob_snap_tree_level: _Optional[int] = ..., view_box_with_dedup_found: bool = ...) -> None: ...

class BlobSnapTreeLeafLevelMapValueProto(_message.Message):
    __slots__ = ("node_id", "brick_num", "view_box_id", "chunk_count", "can_dedup_in_isolation", "brick_size")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUM_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    CAN_DEDUP_IN_ISOLATION_FIELD_NUMBER: _ClassVar[int]
    BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    brick_num: int
    view_box_id: int
    chunk_count: int
    can_dedup_in_isolation: bool
    brick_size: int
    def __init__(self, node_id: _Optional[int] = ..., brick_num: _Optional[int] = ..., view_box_id: _Optional[int] = ..., chunk_count: _Optional[int] = ..., can_dedup_in_isolation: bool = ..., brick_size: _Optional[int] = ...) -> None: ...

class BlobSnapTreeInternalNodeMapValueProto(_message.Message):
    __slots__ = ("brick_info", "parent_node_id", "opclock_vec")
    BRICK_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    brick_info: BlobSnapTreeLeafLevelMapValueProto
    parent_node_id: int
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, brick_info: _Optional[_Union[BlobSnapTreeLeafLevelMapValueProto, _Mapping]] = ..., parent_node_id: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...
