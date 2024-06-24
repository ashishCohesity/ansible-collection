from bookkeeper.v2.base import bookkeeper_v2_pb2 as _bookkeeper_v2_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bookkeeper.v2.stub import rpc_service_pb2 as _rpc_service_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OSRContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "should_build_pipeline", "max_group_depth", "leaf_group_stats_version", "parent_group_stats_version", "max_view_snaptree_level", "max_blob_snaptree_level", "level0_reducer_num_shards_per_node", "spl_grp_info_vec")
    class SdSpecialGrpInfo(_message.Message):
        __slots__ = ("sd_id", "component_name", "group_id")
        SD_ID_FIELD_NUMBER: _ClassVar[int]
        COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        sd_id: int
        component_name: int
        group_id: str
        def __init__(self, sd_id: _Optional[int] = ..., component_name: _Optional[int] = ..., group_id: _Optional[str] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BUILD_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUP_DEPTH_FIELD_NUMBER: _ClassVar[int]
    LEAF_GROUP_STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOB_SNAPTREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LEVEL0_REDUCER_NUM_SHARDS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    SPL_GRP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    should_build_pipeline: bool
    max_group_depth: int
    leaf_group_stats_version: str
    parent_group_stats_version: str
    max_view_snaptree_level: int
    max_blob_snaptree_level: int
    level0_reducer_num_shards_per_node: int
    spl_grp_info_vec: _containers.RepeatedCompositeFieldContainer[OSRContextDataProto.SdSpecialGrpInfo]
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., should_build_pipeline: bool = ..., max_group_depth: _Optional[int] = ..., leaf_group_stats_version: _Optional[str] = ..., parent_group_stats_version: _Optional[str] = ..., max_view_snaptree_level: _Optional[int] = ..., max_blob_snaptree_level: _Optional[int] = ..., level0_reducer_num_shards_per_node: _Optional[int] = ..., spl_grp_info_vec: _Optional[_Iterable[_Union[OSRContextDataProto.SdSpecialGrpInfo, _Mapping]]] = ...) -> None: ...

class QueryContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "should_build_pipeline", "max_group_depth", "leaf_group_stats_version", "parent_group_stats_version", "query_arg", "result_batch_size")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BUILD_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUP_DEPTH_FIELD_NUMBER: _ClassVar[int]
    LEAF_GROUP_STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_STATS_VERSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_ARG_FIELD_NUMBER: _ClassVar[int]
    RESULT_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    should_build_pipeline: bool
    max_group_depth: int
    leaf_group_stats_version: str
    parent_group_stats_version: str
    query_arg: _bookkeeper_v2_pb2.BkV2PipelineInput
    result_batch_size: int
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., should_build_pipeline: bool = ..., max_group_depth: _Optional[int] = ..., leaf_group_stats_version: _Optional[str] = ..., parent_group_stats_version: _Optional[str] = ..., query_arg: _Optional[_Union[_bookkeeper_v2_pb2.BkV2PipelineInput, _Mapping]] = ..., result_batch_size: _Optional[int] = ...) -> None: ...

class BkprV2StatsAggrValProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OSRKeyProto(_message.Message):
    __slots__ = ("node_id", "bkpr_v2_entity", "view_id", "bk_v2_grp_id", "chunk_id", "blob_id", "brick_number", "storage_domain_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BKPR_V2_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    bkpr_v2_entity: _bookkeeper_v2_pb2.BookkeeperEntityProto
    view_id: int
    bk_v2_grp_id: str
    chunk_id: _blob_store_pb2.ChunkIdProto
    blob_id: int
    brick_number: int
    storage_domain_id: int
    def __init__(self, node_id: _Optional[int] = ..., bkpr_v2_entity: _Optional[_Union[_bookkeeper_v2_pb2.BookkeeperEntityProto, _Mapping]] = ..., view_id: _Optional[int] = ..., bk_v2_grp_id: _Optional[str] = ..., chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., blob_id: _Optional[int] = ..., brick_number: _Optional[int] = ..., storage_domain_id: _Optional[int] = ...) -> None: ...

class QueryKeyProto(_message.Message):
    __slots__ = ("bk_v2_grp_id", "subresult_key")
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    SUBRESULT_KEY_FIELD_NUMBER: _ClassVar[int]
    bk_v2_grp_id: str
    subresult_key: str
    def __init__(self, bk_v2_grp_id: _Optional[str] = ..., subresult_key: _Optional[str] = ...) -> None: ...

class OSRValProto(_message.Message):
    __slots__ = ("child_node_id", "inode_stats", "view_info", "is_present_in_bkpr_v2_groups", "leaf_group_stats", "is_root", "bk_v2_grp_id", "child_grp_id", "parent_group_id_vec", "bk_v2_entity_row_version", "bk_v2_entity_marked_deleted", "bk_v2_entity_deleted_timestamp_usecs", "chunk_stats", "parent_node_id", "blob_info_vec", "bkpr_v2_grp_id_vec", "brick_bytes_logical", "child_key_int", "node_key_int", "minion_brick_bytes_logical", "is_leaf_group", "total_logical_size", "bkpr_v2_entity", "refd_by_num_views", "component_name")
    class InodeStatsInfo(_message.Message):
        __slots__ = ("num_directories", "num_regular_files", "regular_files_usage_bytes", "num_minion_files", "minion_files_usage_bytes", "num_mega_files", "mega_files_usage_bytes", "num_special_inodes", "inode_id")
        NUM_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
        NUM_REGULAR_FILES_FIELD_NUMBER: _ClassVar[int]
        REGULAR_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_MINION_FILES_FIELD_NUMBER: _ClassVar[int]
        MINION_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_MEGA_FILES_FIELD_NUMBER: _ClassVar[int]
        MEGA_FILES_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_SPECIAL_INODES_FIELD_NUMBER: _ClassVar[int]
        INODE_ID_FIELD_NUMBER: _ClassVar[int]
        num_directories: int
        num_regular_files: int
        regular_files_usage_bytes: int
        num_minion_files: int
        minion_files_usage_bytes: int
        num_mega_files: int
        mega_files_usage_bytes: int
        num_special_inodes: int
        inode_id: int
        def __init__(self, num_directories: _Optional[int] = ..., num_regular_files: _Optional[int] = ..., regular_files_usage_bytes: _Optional[int] = ..., num_minion_files: _Optional[int] = ..., minion_files_usage_bytes: _Optional[int] = ..., num_mega_files: _Optional[int] = ..., mega_files_usage_bytes: _Optional[int] = ..., num_special_inodes: _Optional[int] = ..., inode_id: _Optional[int] = ...) -> None: ...
    class ViewInfo(_message.Message):
        __slots__ = ("view_id", "view_name", "storage_domain_id", "is_internal", "root_snaptree_id", "root_inode_id", "root_namespace_name", "is_relevant_namespace")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
        ROOT_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_RELEVANT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        view_name: str
        storage_domain_id: int
        is_internal: bool
        root_snaptree_id: int
        root_inode_id: int
        root_namespace_name: str
        is_relevant_namespace: bool
        def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., storage_domain_id: _Optional[int] = ..., is_internal: bool = ..., root_snaptree_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., root_namespace_name: _Optional[str] = ..., is_relevant_namespace: bool = ...) -> None: ...
    class GroupDetails(_message.Message):
        __slots__ = ("group_metadata_stats", "io_stats", "logical_stats", "physical_stats")
        GROUP_METADATA_STATS_FIELD_NUMBER: _ClassVar[int]
        IO_STATS_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_STATS_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_STATS_FIELD_NUMBER: _ClassVar[int]
        group_metadata_stats: _bookkeeper_v2_pb2.GroupMetadataStats
        io_stats: _bookkeeper_v2_pb2.IOStats
        logical_stats: _bookkeeper_v2_pb2.LogicalStats
        physical_stats: _bookkeeper_v2_pb2.PhysicalStats
        def __init__(self, group_metadata_stats: _Optional[_Union[_bookkeeper_v2_pb2.GroupMetadataStats, _Mapping]] = ..., io_stats: _Optional[_Union[_bookkeeper_v2_pb2.IOStats, _Mapping]] = ..., logical_stats: _Optional[_Union[_bookkeeper_v2_pb2.LogicalStats, _Mapping]] = ..., physical_stats: _Optional[_Union[_bookkeeper_v2_pb2.PhysicalStats, _Mapping]] = ...) -> None: ...
    class ChunkStats(_message.Message):
        __slots__ = ("chunk_logical_bytes", "chunk_morphed_bytes", "chunk_morphed_bytes_cloud", "chunk_physical_bytes_cloud", "chunk_logical_bytes_cloud", "chunk_physical_bytes", "unique_chunk_logical_bytes", "unique_chunk_logical_bytes_cloud", "unique_chunk_morphed_bytes", "unique_chunk_morphed_bytes_cloud", "unique_chunk_physical_bytes_cloud", "unique_chunk_physical_bytes", "storage_domain_id")
        CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_MORPHED_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
        CHUNK_PHYSICAL_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
        CHUNK_LOGICAL_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
        CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_LOGICAL_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_MORPHED_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_PHYSICAL_BYTES_CLOUD_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        chunk_logical_bytes: float
        chunk_morphed_bytes: float
        chunk_morphed_bytes_cloud: float
        chunk_physical_bytes_cloud: float
        chunk_logical_bytes_cloud: float
        chunk_physical_bytes: float
        unique_chunk_logical_bytes: float
        unique_chunk_logical_bytes_cloud: float
        unique_chunk_morphed_bytes: float
        unique_chunk_morphed_bytes_cloud: float
        unique_chunk_physical_bytes_cloud: float
        unique_chunk_physical_bytes: float
        storage_domain_id: int
        def __init__(self, chunk_logical_bytes: _Optional[float] = ..., chunk_morphed_bytes: _Optional[float] = ..., chunk_morphed_bytes_cloud: _Optional[float] = ..., chunk_physical_bytes_cloud: _Optional[float] = ..., chunk_logical_bytes_cloud: _Optional[float] = ..., chunk_physical_bytes: _Optional[float] = ..., unique_chunk_logical_bytes: _Optional[float] = ..., unique_chunk_logical_bytes_cloud: _Optional[float] = ..., unique_chunk_morphed_bytes: _Optional[float] = ..., unique_chunk_morphed_bytes_cloud: _Optional[float] = ..., unique_chunk_physical_bytes_cloud: _Optional[float] = ..., unique_chunk_physical_bytes: _Optional[float] = ..., storage_domain_id: _Optional[int] = ...) -> None: ...
    class BlobInfo(_message.Message):
        __slots__ = ("blob_id", "is_minion", "brick_size", "inode_node_id", "logical_size", "offset", "reserved_size", "inode_id")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        IS_MINION_FIELD_NUMBER: _ClassVar[int]
        BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
        INODE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        RESERVED_SIZE_FIELD_NUMBER: _ClassVar[int]
        INODE_ID_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        is_minion: bool
        brick_size: int
        inode_node_id: int
        logical_size: int
        offset: int
        reserved_size: int
        inode_id: int
        def __init__(self, blob_id: _Optional[int] = ..., is_minion: bool = ..., brick_size: _Optional[int] = ..., inode_node_id: _Optional[int] = ..., logical_size: _Optional[int] = ..., offset: _Optional[int] = ..., reserved_size: _Optional[int] = ..., inode_id: _Optional[int] = ...) -> None: ...
    CHILD_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_STATS_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_PRESENT_IN_BKPR_V2_GROUPS_FIELD_NUMBER: _ClassVar[int]
    LEAF_GROUP_STATS_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_MARKED_DELETED_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_STATS_FIELD_NUMBER: _ClassVar[int]
    PARENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    BKPR_V2_GRP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    CHILD_KEY_INT_FIELD_NUMBER: _ClassVar[int]
    NODE_KEY_INT_FIELD_NUMBER: _ClassVar[int]
    MINION_BRICK_BYTES_LOGICAL_FIELD_NUMBER: _ClassVar[int]
    IS_LEAF_GROUP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BKPR_V2_ENTITY_FIELD_NUMBER: _ClassVar[int]
    REFD_BY_NUM_VIEWS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    child_node_id: int
    inode_stats: OSRValProto.InodeStatsInfo
    view_info: OSRValProto.ViewInfo
    is_present_in_bkpr_v2_groups: bool
    leaf_group_stats: OSRValProto.GroupDetails
    is_root: bool
    bk_v2_grp_id: str
    child_grp_id: str
    parent_group_id_vec: _containers.RepeatedScalarFieldContainer[str]
    bk_v2_entity_row_version: int
    bk_v2_entity_marked_deleted: bool
    bk_v2_entity_deleted_timestamp_usecs: int
    chunk_stats: OSRValProto.ChunkStats
    parent_node_id: int
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[OSRValProto.BlobInfo]
    bkpr_v2_grp_id_vec: _containers.RepeatedScalarFieldContainer[str]
    brick_bytes_logical: int
    child_key_int: int
    node_key_int: int
    minion_brick_bytes_logical: int
    is_leaf_group: bool
    total_logical_size: int
    bkpr_v2_entity: _bookkeeper_v2_pb2.BookkeeperEntityProto
    refd_by_num_views: int
    component_name: str
    def __init__(self, child_node_id: _Optional[int] = ..., inode_stats: _Optional[_Union[OSRValProto.InodeStatsInfo, _Mapping]] = ..., view_info: _Optional[_Union[OSRValProto.ViewInfo, _Mapping]] = ..., is_present_in_bkpr_v2_groups: bool = ..., leaf_group_stats: _Optional[_Union[OSRValProto.GroupDetails, _Mapping]] = ..., is_root: bool = ..., bk_v2_grp_id: _Optional[str] = ..., child_grp_id: _Optional[str] = ..., parent_group_id_vec: _Optional[_Iterable[str]] = ..., bk_v2_entity_row_version: _Optional[int] = ..., bk_v2_entity_marked_deleted: bool = ..., bk_v2_entity_deleted_timestamp_usecs: _Optional[int] = ..., chunk_stats: _Optional[_Union[OSRValProto.ChunkStats, _Mapping]] = ..., parent_node_id: _Optional[int] = ..., blob_info_vec: _Optional[_Iterable[_Union[OSRValProto.BlobInfo, _Mapping]]] = ..., bkpr_v2_grp_id_vec: _Optional[_Iterable[str]] = ..., brick_bytes_logical: _Optional[int] = ..., child_key_int: _Optional[int] = ..., node_key_int: _Optional[int] = ..., minion_brick_bytes_logical: _Optional[int] = ..., is_leaf_group: bool = ..., total_logical_size: _Optional[int] = ..., bkpr_v2_entity: _Optional[_Union[_bookkeeper_v2_pb2.BookkeeperEntityProto, _Mapping]] = ..., refd_by_num_views: _Optional[int] = ..., component_name: _Optional[str] = ...) -> None: ...

class QueryValProto(_message.Message):
    __slots__ = ("is_root", "bk_v2_grp_id", "child_grp_id", "parent_group_id_vec", "group_stats_val", "state", "raise_alert", "in_desired_subtree")
    IS_ROOT_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_GROUP_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_STATS_VAL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RAISE_ALERT_FIELD_NUMBER: _ClassVar[int]
    IN_DESIRED_SUBTREE_FIELD_NUMBER: _ClassVar[int]
    is_root: bool
    bk_v2_grp_id: str
    child_grp_id: str
    parent_group_id_vec: _containers.RepeatedScalarFieldContainer[str]
    group_stats_val: _bookkeeper_v2_pb2.GroupStats
    state: bytes
    raise_alert: bool
    in_desired_subtree: bool
    def __init__(self, is_root: bool = ..., bk_v2_grp_id: _Optional[str] = ..., child_grp_id: _Optional[str] = ..., parent_group_id_vec: _Optional[_Iterable[str]] = ..., group_stats_val: _Optional[_Union[_bookkeeper_v2_pb2.GroupStats, _Mapping]] = ..., state: _Optional[bytes] = ..., raise_alert: bool = ..., in_desired_subtree: bool = ...) -> None: ...

class OSRCleanUpKeyProto(_message.Message):
    __slots__ = ("bk_v2_grp_id",)
    BK_V2_GRP_ID_FIELD_NUMBER: _ClassVar[int]
    bk_v2_grp_id: str
    def __init__(self, bk_v2_grp_id: _Optional[str] = ...) -> None: ...

class OSRCleanUpValProto(_message.Message):
    __slots__ = ("exists_in_bk_v2_grps_tbl", "bk_v2_grp_marked_deleted", "bk_v2_entity_marked_deleted", "bk_v2_entity_deleted_timestamp_usecs", "bkpr_v2_entity", "bk_v2_entity_row_version")
    EXISTS_IN_BK_V2_GRPS_TBL_FIELD_NUMBER: _ClassVar[int]
    BK_V2_GRP_MARKED_DELETED_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_MARKED_DELETED_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_DELETED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    BKPR_V2_ENTITY_FIELD_NUMBER: _ClassVar[int]
    BK_V2_ENTITY_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    exists_in_bk_v2_grps_tbl: bool
    bk_v2_grp_marked_deleted: bool
    bk_v2_entity_marked_deleted: bool
    bk_v2_entity_deleted_timestamp_usecs: int
    bkpr_v2_entity: _bookkeeper_v2_pb2.BookkeeperEntityProto
    bk_v2_entity_row_version: int
    def __init__(self, exists_in_bk_v2_grps_tbl: bool = ..., bk_v2_grp_marked_deleted: bool = ..., bk_v2_entity_marked_deleted: bool = ..., bk_v2_entity_deleted_timestamp_usecs: _Optional[int] = ..., bkpr_v2_entity: _Optional[_Union[_bookkeeper_v2_pb2.BookkeeperEntityProto, _Mapping]] = ..., bk_v2_entity_row_version: _Optional[int] = ...) -> None: ...
