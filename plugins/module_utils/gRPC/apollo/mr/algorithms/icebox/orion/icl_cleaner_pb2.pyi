from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ICLCContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "max_blob_snaptree_level", "invalid_cloud_domain_id_vec", "num_buckets_to_partition", "num_shard_vst_level_multiplier", "action_emitter_num_shards")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOB_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INVALID_CLOUD_DOMAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BUCKETS_TO_PARTITION_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARD_VST_LEVEL_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    ACTION_EMITTER_NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    max_blob_snaptree_level: int
    invalid_cloud_domain_id_vec: _containers.RepeatedScalarFieldContainer[int]
    num_buckets_to_partition: int
    num_shard_vst_level_multiplier: int
    action_emitter_num_shards: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., max_blob_snaptree_level: _Optional[int] = ..., invalid_cloud_domain_id_vec: _Optional[_Iterable[int]] = ..., num_buckets_to_partition: _Optional[int] = ..., num_shard_vst_level_multiplier: _Optional[int] = ..., action_emitter_num_shards: _Optional[int] = ...) -> None: ...

class ICLCKeyProto(_message.Message):
    __slots__ = ("cloud_domain_id", "node_id", "cloud_node_ptr", "bucket_id")
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_domain_id: int
    node_id: int
    cloud_node_ptr: _cloud_pb2.CloudNodePtrProto
    bucket_id: int
    def __init__(self, cloud_domain_id: _Optional[int] = ..., node_id: _Optional[int] = ..., cloud_node_ptr: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ..., bucket_id: _Optional[int] = ...) -> None: ...

class ICLCValueProto(_message.Message):
    __slots__ = ("node_id", "parent_node_id", "chunk_id_vec", "is_chunk_invalid", "is_bst_node_invalid", "is_vst_node_invalid", "view_info", "is_child_invalid", "cloud_domain_id", "key_int", "key_str", "bst_child_info", "vst_child_info")
    class BSTChildInfo(_message.Message):
        __slots__ = ("node_id", "key")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        key: int
        def __init__(self, node_id: _Optional[int] = ..., key: _Optional[int] = ...) -> None: ...
    class VSTChildInfo(_message.Message):
        __slots__ = ("node_id", "key", "blob_snap_tree_id", "bst_child_info")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BST_CHILD_INFO_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        key: int
        blob_snap_tree_id: int
        bst_child_info: ICLCValueProto.BSTChildInfo
        def __init__(self, node_id: _Optional[int] = ..., key: _Optional[int] = ..., blob_snap_tree_id: _Optional[int] = ..., bst_child_info: _Optional[_Union[ICLCValueProto.BSTChildInfo, _Mapping]] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_CHUNK_INVALID_FIELD_NUMBER: _ClassVar[int]
    IS_BST_NODE_INVALID_FIELD_NUMBER: _ClassVar[int]
    IS_VST_NODE_INVALID_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CHILD_INVALID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_INT_FIELD_NUMBER: _ClassVar[int]
    KEY_STR_FIELD_NUMBER: _ClassVar[int]
    BST_CHILD_INFO_FIELD_NUMBER: _ClassVar[int]
    VST_CHILD_INFO_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    parent_node_id: int
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
    is_chunk_invalid: bool
    is_bst_node_invalid: bool
    is_vst_node_invalid: bool
    view_info: _icebox_pb2.InvalidArchivedNodeValueProto.ViewInfo
    is_child_invalid: bool
    cloud_domain_id: int
    key_int: int
    key_str: str
    bst_child_info: ICLCValueProto.BSTChildInfo
    vst_child_info: ICLCValueProto.VSTChildInfo
    def __init__(self, node_id: _Optional[int] = ..., parent_node_id: _Optional[int] = ..., chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., is_chunk_invalid: bool = ..., is_bst_node_invalid: bool = ..., is_vst_node_invalid: bool = ..., view_info: _Optional[_Union[_icebox_pb2.InvalidArchivedNodeValueProto.ViewInfo, _Mapping]] = ..., is_child_invalid: bool = ..., cloud_domain_id: _Optional[int] = ..., key_int: _Optional[int] = ..., key_str: _Optional[str] = ..., bst_child_info: _Optional[_Union[ICLCValueProto.BSTChildInfo, _Mapping]] = ..., vst_child_info: _Optional[_Union[ICLCValueProto.VSTChildInfo, _Mapping]] = ...) -> None: ...
