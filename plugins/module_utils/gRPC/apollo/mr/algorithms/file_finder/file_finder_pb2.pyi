from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileFinderContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "max_blob_snaptree_level", "blob_info_vec", "chunk_id_vec", "view_snaptree_node_id_vec", "log_inodes_with_inconsistent_size", "cloud_object_id_vec", "mangeled_brick_range_vec", "inode_key_range_vec", "blob_snaptree_range_info_vec", "blob_snaptree_node_id_vec", "num_shard_per_vst_level_multiplier", "action_emitter_num_shards")
    class BlobRangeInfo(_message.Message):
        __slots__ = ("blob_id", "blob_offset", "range_size")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
        RANGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        blob_offset: int
        range_size: int
        def __init__(self, blob_id: _Optional[int] = ..., blob_offset: _Optional[int] = ..., range_size: _Optional[int] = ...) -> None: ...
    class MangledBrickRange(_message.Message):
        __slots__ = ("blob_id", "start", "end")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        start: int
        end: int
        def __init__(self, blob_id: _Optional[int] = ..., start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
    class InodeKeyRangeInfo(_message.Message):
        __slots__ = ("start_val", "end_val")
        START_VAL_FIELD_NUMBER: _ClassVar[int]
        END_VAL_FIELD_NUMBER: _ClassVar[int]
        start_val: int
        end_val: int
        def __init__(self, start_val: _Optional[int] = ..., end_val: _Optional[int] = ...) -> None: ...
    class BlobSnapTreeRangeInfo(_message.Message):
        __slots__ = ("start", "end", "scribe_bucket_id")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        start: int
        end: int
        scribe_bucket_id: int
        def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., scribe_bucket_id: _Optional[int] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOB_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAPTREE_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    LOG_INODES_WITH_INCONSISTENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MANGELED_BRICK_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    INODE_KEY_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAPTREE_RANGE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAPTREE_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARD_PER_VST_LEVEL_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    ACTION_EMITTER_NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    max_blob_snaptree_level: int
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[FileFinderContextDataProto.BlobRangeInfo]
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
    view_snaptree_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    log_inodes_with_inconsistent_size: bool
    cloud_object_id_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.CloudObjectIdProto]
    mangeled_brick_range_vec: _containers.RepeatedCompositeFieldContainer[FileFinderContextDataProto.MangledBrickRange]
    inode_key_range_vec: _containers.RepeatedCompositeFieldContainer[FileFinderContextDataProto.InodeKeyRangeInfo]
    blob_snaptree_range_info_vec: _containers.RepeatedCompositeFieldContainer[FileFinderContextDataProto.BlobSnapTreeRangeInfo]
    blob_snaptree_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    num_shard_per_vst_level_multiplier: int
    action_emitter_num_shards: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., max_blob_snaptree_level: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[FileFinderContextDataProto.BlobRangeInfo, _Mapping]]] = ..., chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., view_snaptree_node_id_vec: _Optional[_Iterable[int]] = ..., log_inodes_with_inconsistent_size: bool = ..., cloud_object_id_vec: _Optional[_Iterable[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]]] = ..., mangeled_brick_range_vec: _Optional[_Iterable[_Union[FileFinderContextDataProto.MangledBrickRange, _Mapping]]] = ..., inode_key_range_vec: _Optional[_Iterable[_Union[FileFinderContextDataProto.InodeKeyRangeInfo, _Mapping]]] = ..., blob_snaptree_range_info_vec: _Optional[_Iterable[_Union[FileFinderContextDataProto.BlobSnapTreeRangeInfo, _Mapping]]] = ..., blob_snaptree_node_id_vec: _Optional[_Iterable[int]] = ..., num_shard_per_vst_level_multiplier: _Optional[int] = ..., action_emitter_num_shards: _Optional[int] = ...) -> None: ...

class FileFinderKeyProto(_message.Message):
    __slots__ = ("node_id", "chunk_id", "offset", "inode_id_bucket")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    chunk_id: _blob_store_pb2.ChunkIdProto
    offset: int
    inode_id_bucket: int
    def __init__(self, node_id: _Optional[int] = ..., chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., offset: _Optional[int] = ..., inode_id_bucket: _Optional[int] = ...) -> None: ...

class FileFinderValueProto(_message.Message):
    __slots__ = ("node_id", "view_info", "parent_node_id", "blob_info_vec")
    class ViewInfo(_message.Message):
        __slots__ = ("view_id", "root_inode_id", "root_inode_path")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_inode_id: int
        root_inode_path: str
        def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., root_inode_path: _Optional[str] = ...) -> None: ...
    class BlobInfo(_message.Message):
        __slots__ = ("blob_id", "inode_info_vec", "chunk_info_vec")
        class InodeInfo(_message.Message):
            __slots__ = ("inode_id", "offset_vec")
            INODE_ID_FIELD_NUMBER: _ClassVar[int]
            OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
            inode_id: int
            offset_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, inode_id: _Optional[int] = ..., offset_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        class ChunkInfo(_message.Message):
            __slots__ = ("chunk_id", "offset_vec", "selected_from_cm_table")
            CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
            OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
            SELECTED_FROM_CM_TABLE_FIELD_NUMBER: _ClassVar[int]
            chunk_id: _blob_store_pb2.ChunkIdProto
            offset_vec: _containers.RepeatedScalarFieldContainer[int]
            selected_from_cm_table: bool
            def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., offset_vec: _Optional[_Iterable[int]] = ..., selected_from_cm_table: bool = ...) -> None: ...
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        INODE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        inode_info_vec: _containers.RepeatedCompositeFieldContainer[FileFinderValueProto.BlobInfo.InodeInfo]
        chunk_info_vec: _containers.RepeatedCompositeFieldContainer[FileFinderValueProto.BlobInfo.ChunkInfo]
        def __init__(self, blob_id: _Optional[int] = ..., inode_info_vec: _Optional[_Iterable[_Union[FileFinderValueProto.BlobInfo.InodeInfo, _Mapping]]] = ..., chunk_info_vec: _Optional[_Iterable[_Union[FileFinderValueProto.BlobInfo.ChunkInfo, _Mapping]]] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    view_info: FileFinderValueProto.ViewInfo
    parent_node_id: int
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[FileFinderValueProto.BlobInfo]
    def __init__(self, node_id: _Optional[int] = ..., view_info: _Optional[_Union[FileFinderValueProto.ViewInfo, _Mapping]] = ..., parent_node_id: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[FileFinderValueProto.BlobInfo, _Mapping]]] = ...) -> None: ...

class VSTNFinderKeyProto(_message.Message):
    __slots__ = ("node_id", "id_bucket")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    id_bucket: int
    def __init__(self, node_id: _Optional[int] = ..., id_bucket: _Optional[int] = ...) -> None: ...

class VSTNFinderValueProto(_message.Message):
    __slots__ = ("node_id", "parent_node_id", "view_info", "inode_id", "missing_entry_name_vec", "missing_fragment_id_vec")
    class ViewInfo(_message.Message):
        __slots__ = ("view_id", "root_inode_id", "storage_domain_name", "view_name", "namespace_name", "root_inode_path")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_inode_id: int
        storage_domain_name: str
        view_name: str
        namespace_name: str
        root_inode_path: str
        def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., storage_domain_name: _Optional[str] = ..., view_name: _Optional[str] = ..., namespace_name: _Optional[str] = ..., root_inode_path: _Optional[str] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    MISSING_ENTRY_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    MISSING_FRAGMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    parent_node_id: int
    view_info: VSTNFinderValueProto.ViewInfo
    inode_id: int
    missing_entry_name_vec: _containers.RepeatedScalarFieldContainer[str]
    missing_fragment_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, node_id: _Optional[int] = ..., parent_node_id: _Optional[int] = ..., view_info: _Optional[_Union[VSTNFinderValueProto.ViewInfo, _Mapping]] = ..., inode_id: _Optional[int] = ..., missing_entry_name_vec: _Optional[_Iterable[str]] = ..., missing_fragment_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class BSTFinderKeyProto(_message.Message):
    __slots__ = ("node_id", "blob_id", "inode_id_bucket")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_BUCKET_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    blob_id: int
    inode_id_bucket: int
    def __init__(self, node_id: _Optional[int] = ..., blob_id: _Optional[int] = ..., inode_id_bucket: _Optional[int] = ...) -> None: ...

class BSTFinderValProto(_message.Message):
    __slots__ = ("view_info", "parent_node_id", "node_id", "inode_id", "blob_snap_tree_node_id_vec")
    class ViewInfo(_message.Message):
        __slots__ = ("view_id", "root_inode_id", "root_inode_path")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_PATH_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_inode_id: int
        root_inode_path: str
        def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., root_inode_path: _Optional[str] = ...) -> None: ...
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    view_info: BSTFinderValProto.ViewInfo
    parent_node_id: int
    node_id: int
    inode_id: int
    blob_snap_tree_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, view_info: _Optional[_Union[BSTFinderValProto.ViewInfo, _Mapping]] = ..., parent_node_id: _Optional[int] = ..., node_id: _Optional[int] = ..., inode_id: _Optional[int] = ..., blob_snap_tree_node_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
