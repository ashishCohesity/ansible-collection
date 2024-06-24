from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapTreeDedupContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "apollo_mr_snap_tree_dedup_minimum_nodes_count", "apollo_mr_snap_tree_dedup_maximum_nodes_count", "apollo_mr_snap_tree_dedup_maximum_parent_nodes_count", "snap_tree_dedup_action_emitter_num_shards_per_node", "snap_tree_dedup_parent_reducer_num_shards_per_node")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_SNAP_TREE_DEDUP_MINIMUM_NODES_COUNT_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_SNAP_TREE_DEDUP_MAXIMUM_NODES_COUNT_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_SNAP_TREE_DEDUP_MAXIMUM_PARENT_NODES_COUNT_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_DEDUP_ACTION_EMITTER_NUM_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_DEDUP_PARENT_REDUCER_NUM_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    apollo_mr_snap_tree_dedup_minimum_nodes_count: int
    apollo_mr_snap_tree_dedup_maximum_nodes_count: int
    apollo_mr_snap_tree_dedup_maximum_parent_nodes_count: int
    snap_tree_dedup_action_emitter_num_shards_per_node: int
    snap_tree_dedup_parent_reducer_num_shards_per_node: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., apollo_mr_snap_tree_dedup_minimum_nodes_count: _Optional[int] = ..., apollo_mr_snap_tree_dedup_maximum_nodes_count: _Optional[int] = ..., apollo_mr_snap_tree_dedup_maximum_parent_nodes_count: _Optional[int] = ..., snap_tree_dedup_action_emitter_num_shards_per_node: _Optional[int] = ..., snap_tree_dedup_parent_reducer_num_shards_per_node: _Optional[int] = ...) -> None: ...

class SnapTreeDedupKey(_message.Message):
    __slots__ = ("view_box_id", "brick_number", "extent_vec", "value_version")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    brick_number: int
    extent_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.BrickMetadataProto.Extent]
    value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    def __init__(self, view_box_id: _Optional[int] = ..., brick_number: _Optional[int] = ..., extent_vec: _Optional[_Iterable[_Union[_blob_store_pb2.BrickMetadataProto.Extent, _Mapping]]] = ..., value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("tree_id", "node_id", "value_version")
    TREE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    tree_id: int
    node_id: int
    value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    def __init__(self, tree_id: _Optional[int] = ..., node_id: _Optional[int] = ..., value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...

class SnapTreeDedupParentReducerProto(_message.Message):
    __slots__ = ("node_info", "dedup_key")
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    DEDUP_KEY_FIELD_NUMBER: _ClassVar[int]
    node_info: NodeInfo
    dedup_key: SnapTreeDedupKey
    def __init__(self, node_info: _Optional[_Union[NodeInfo, _Mapping]] = ..., dedup_key: _Optional[_Union[SnapTreeDedupKey, _Mapping]] = ...) -> None: ...

class SnapTreeDedupValue(_message.Message):
    __slots__ = ("parent_info_vec", "node_info")
    PARENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    parent_info_vec: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    node_info: NodeInfo
    def __init__(self, parent_info_vec: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ..., node_info: _Optional[_Union[NodeInfo, _Mapping]] = ...) -> None: ...
