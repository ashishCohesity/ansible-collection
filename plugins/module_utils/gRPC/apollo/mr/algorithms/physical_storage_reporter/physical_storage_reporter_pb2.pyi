from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from bookkeeper.base import bookkeeper_pb2 as _bookkeeper_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PhysicalStorageReporterContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "max_view_snaptree_level", "max_blob_snaptree_level", "max_group_depth", "should_build_pipeline", "group_id_vec", "group_config_vec", "sd_spl_grp_map", "relevant_nmspce_grp_idx", "non_relevant_nmspce_grp_idx", "all_nmspce_grp_idx", "pst_level0_reducer_num_shards_per_node", "pst_minion_brick_reducer_num_shards_per_node", "pst_minion_blob_reducer_num_shards_per_node")
    class StorageDomainSpecialGroup(_message.Message):
        __slots__ = ("storage_domain_id", "storage_domain_name", "entity_name")
        STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        storage_domain_id: int
        storage_domain_name: str
        entity_name: str
        def __init__(self, storage_domain_id: _Optional[int] = ..., storage_domain_name: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...
    class SdSplGrpMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PhysicalStorageReporterContextDataProto.StorageDomainSpecialGroup
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PhysicalStorageReporterContextDataProto.StorageDomainSpecialGroup, _Mapping]] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOB_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUP_DEPTH_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BUILD_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    SD_SPL_GRP_MAP_FIELD_NUMBER: _ClassVar[int]
    RELEVANT_NMSPCE_GRP_IDX_FIELD_NUMBER: _ClassVar[int]
    NON_RELEVANT_NMSPCE_GRP_IDX_FIELD_NUMBER: _ClassVar[int]
    ALL_NMSPCE_GRP_IDX_FIELD_NUMBER: _ClassVar[int]
    PST_LEVEL0_REDUCER_NUM_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    PST_MINION_BRICK_REDUCER_NUM_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    PST_MINION_BLOB_REDUCER_NUM_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    max_view_snaptree_level: int
    max_blob_snaptree_level: int
    max_group_depth: int
    should_build_pipeline: bool
    group_id_vec: _containers.RepeatedScalarFieldContainer[int]
    group_config_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_pb2.GroupConfigProto]
    sd_spl_grp_map: _containers.MessageMap[int, PhysicalStorageReporterContextDataProto.StorageDomainSpecialGroup]
    relevant_nmspce_grp_idx: int
    non_relevant_nmspce_grp_idx: int
    all_nmspce_grp_idx: int
    pst_level0_reducer_num_shards_per_node: int
    pst_minion_brick_reducer_num_shards_per_node: int
    pst_minion_blob_reducer_num_shards_per_node: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., max_view_snaptree_level: _Optional[int] = ..., max_blob_snaptree_level: _Optional[int] = ..., max_group_depth: _Optional[int] = ..., should_build_pipeline: bool = ..., group_id_vec: _Optional[_Iterable[int]] = ..., group_config_vec: _Optional[_Iterable[_Union[_bookkeeper_pb2.GroupConfigProto, _Mapping]]] = ..., sd_spl_grp_map: _Optional[_Mapping[int, PhysicalStorageReporterContextDataProto.StorageDomainSpecialGroup]] = ..., relevant_nmspce_grp_idx: _Optional[int] = ..., non_relevant_nmspce_grp_idx: _Optional[int] = ..., all_nmspce_grp_idx: _Optional[int] = ..., pst_level0_reducer_num_shards_per_node: _Optional[int] = ..., pst_minion_brick_reducer_num_shards_per_node: _Optional[int] = ..., pst_minion_blob_reducer_num_shards_per_node: _Optional[int] = ...) -> None: ...

class PhysicalStorageReporterKeyProto(_message.Message):
    __slots__ = ("node_id", "offset", "id_vec", "group_config_vec", "blob_id", "brick_number", "brick_node_id", "index_vec", "bucket_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BRICK_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    offset: int
    id_vec: _containers.RepeatedScalarFieldContainer[int]
    group_config_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_pb2.GroupConfigProto]
    blob_id: int
    brick_number: int
    brick_node_id: int
    index_vec: _containers.RepeatedScalarFieldContainer[int]
    bucket_id: int
    def __init__(self, node_id: _Optional[int] = ..., offset: _Optional[int] = ..., id_vec: _Optional[_Iterable[int]] = ..., group_config_vec: _Optional[_Iterable[_Union[_bookkeeper_pb2.GroupConfigProto, _Mapping]]] = ..., blob_id: _Optional[int] = ..., brick_number: _Optional[int] = ..., brick_node_id: _Optional[int] = ..., index_vec: _Optional[_Iterable[int]] = ..., bucket_id: _Optional[int] = ...) -> None: ...

class PhysicalStorageReporterValueProto(_message.Message):
    __slots__ = ("child_node_id", "offset", "brick_size", "reserved_size", "chunk_id_vec", "chunk_logical_bytes", "chunk_morphed_bytes", "chunk_morphed_bytes_cloud", "chunk_physical_bytes_cloud", "chunk_physical_bytes", "brick_bytes_logical", "id_vec", "obj_proto", "root_snaptree_id", "num_directories", "num_regular_files", "regular_files_usage_bytes", "num_minion_files", "minion_files_usage_bytes", "num_mega_files", "mega_files_usage_bytes", "stats_present", "scribe_row_version", "group_config_vec", "is_unique_chunk", "logical_size", "blob_info_vec", "refd_by_inode", "brick_number", "brick_node_id", "inode_node_id", "unique_chunk_logical_bytes", "unique_chunk_physical_bytes", "unique_chunk_morphed_bytes", "unique_chunk_physical_bytes_cloud", "unique_chunk_morphed_bytes_cloud", "index_vec", "storage_domain_id", "view_name", "is_internal", "is_relevant_namespace")
    class BlobInfo(_message.Message):
        __slots__ = ("blob_id", "is_minion")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        IS_MINION_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        is_minion: bool
        def __init__(self, blob_id: _Optional[int] = ..., is_minion: bool = ...) -> None: ...
    CHILD_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CHUNK_MORPHED_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
    CHUNK_PHYSICAL_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
    CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJ_PROTO_FIELD_NUMBER: _ClassVar[int]
    ROOT_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    NUM_REGULAR_FILES_FIELD_NUMBER: _ClassVar[int]
    REGULAR_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_MINION_FILES_FIELD_NUMBER: _ClassVar[int]
    MINION_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_MEGA_FILES_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATS_PRESENT_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    GROUP_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_UNIQUE_CHUNK_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REFD_BY_INODE_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BRICK_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CHUNK_PHYSICAL_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CHUNK_MORPHED_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
    INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    IS_RELEVANT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    child_node_id: int
    offset: int
    brick_size: int
    reserved_size: int
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
    chunk_logical_bytes: int
    chunk_morphed_bytes: int
    chunk_morphed_bytes_cloud: int
    chunk_physical_bytes_cloud: int
    chunk_physical_bytes: int
    brick_bytes_logical: int
    id_vec: _containers.RepeatedScalarFieldContainer[int]
    obj_proto: _bookkeeper_pb2.ObjectProto
    root_snaptree_id: int
    num_directories: int
    num_regular_files: int
    regular_files_usage_bytes: int
    num_minion_files: int
    minion_files_usage_bytes: int
    num_mega_files: int
    mega_files_usage_bytes: int
    stats_present: bool
    scribe_row_version: int
    group_config_vec: _containers.RepeatedCompositeFieldContainer[_bookkeeper_pb2.GroupConfigProto]
    is_unique_chunk: bool
    logical_size: int
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[PhysicalStorageReporterValueProto.BlobInfo]
    refd_by_inode: bool
    brick_number: int
    brick_node_id: int
    inode_node_id: int
    unique_chunk_logical_bytes: int
    unique_chunk_physical_bytes: int
    unique_chunk_morphed_bytes: int
    unique_chunk_physical_bytes_cloud: int
    unique_chunk_morphed_bytes_cloud: int
    index_vec: _containers.RepeatedScalarFieldContainer[int]
    storage_domain_id: int
    view_name: str
    is_internal: bool
    is_relevant_namespace: bool
    def __init__(self, child_node_id: _Optional[int] = ..., offset: _Optional[int] = ..., brick_size: _Optional[int] = ..., reserved_size: _Optional[int] = ..., chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., chunk_logical_bytes: _Optional[int] = ..., chunk_morphed_bytes: _Optional[int] = ..., chunk_morphed_bytes_cloud: _Optional[int] = ..., chunk_physical_bytes_cloud: _Optional[int] = ..., chunk_physical_bytes: _Optional[int] = ..., brick_bytes_logical: _Optional[int] = ..., id_vec: _Optional[_Iterable[int]] = ..., obj_proto: _Optional[_Union[_bookkeeper_pb2.ObjectProto, _Mapping]] = ..., root_snaptree_id: _Optional[int] = ..., num_directories: _Optional[int] = ..., num_regular_files: _Optional[int] = ..., regular_files_usage_bytes: _Optional[int] = ..., num_minion_files: _Optional[int] = ..., minion_files_usage_bytes: _Optional[int] = ..., num_mega_files: _Optional[int] = ..., mega_files_usage_bytes: _Optional[int] = ..., stats_present: bool = ..., scribe_row_version: _Optional[int] = ..., group_config_vec: _Optional[_Iterable[_Union[_bookkeeper_pb2.GroupConfigProto, _Mapping]]] = ..., is_unique_chunk: bool = ..., logical_size: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[PhysicalStorageReporterValueProto.BlobInfo, _Mapping]]] = ..., refd_by_inode: bool = ..., brick_number: _Optional[int] = ..., brick_node_id: _Optional[int] = ..., inode_node_id: _Optional[int] = ..., unique_chunk_logical_bytes: _Optional[int] = ..., unique_chunk_physical_bytes: _Optional[int] = ..., unique_chunk_morphed_bytes: _Optional[int] = ..., unique_chunk_physical_bytes_cloud: _Optional[int] = ..., unique_chunk_morphed_bytes_cloud: _Optional[int] = ..., index_vec: _Optional[_Iterable[int]] = ..., storage_domain_id: _Optional[int] = ..., view_name: _Optional[str] = ..., is_internal: bool = ..., is_relevant_namespace: bool = ...) -> None: ...
