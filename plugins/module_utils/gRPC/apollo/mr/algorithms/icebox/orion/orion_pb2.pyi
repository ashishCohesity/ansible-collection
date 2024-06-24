from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from bridge.view_keeper import view_usage_pb2 as _view_usage_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudDomainNodePtrProto(_message.Message):
    __slots__ = ("domain_id", "cloud_node_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    cloud_node_id: _cloud_pb2.CloudNodePtrProto
    def __init__(self, domain_id: _Optional[int] = ..., cloud_node_id: _Optional[_Union[_cloud_pb2.CloudNodePtrProto, _Mapping]] = ...) -> None: ...

class CloudDomainNodePtrVec(_message.Message):
    __slots__ = ("ptr_vec",)
    PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    ptr_vec: _containers.RepeatedCompositeFieldContainer[CloudDomainNodePtrProto]
    def __init__(self, ptr_vec: _Optional[_Iterable[_Union[CloudDomainNodePtrProto, _Mapping]]] = ...) -> None: ...

class OrionHealerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "apollo_mr_enable_orion_healer_algos", "domain_id_vec", "max_view_snap_tree_height", "max_blob_snap_tree_height", "view_box_name", "view_name", "fs_name", "cluster_id", "list_from_vault", "approx_per_shard_cm_table_cleanup_size_kb", "apollo_mr_orion_enable_chunk_metadata_cleaner", "apollo_mr_orion_enable_ccfm_fixer", "domain_to_epoch_id_map", "apollo_mr_orion_enable_cloud_domain_gc", "apollo_mr_orion_enable_cloud_domain_tiering", "apollo_mr_orion_ccfm_double_scan_to_validate", "apollo_mr_orion_skip_csr_gc_for_domain_ids", "apollo_mr_orion_skip_ccr_gc_for_domain_ids", "apollo_mr_orion_validate_cloud_chunk_files", "apollo_mr_orion_gc_validate_dangling_minion_bricks", "apollo_mr_orion_gc_cache_refs_to_cloud_chunks", "apollo_mr_orion_gc_add_scan_order", "apollo_mr_orion_gc_enable_worm_domains")
    class DomainToEpochIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_ORION_HEALER_ALGOS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_SNAP_TREE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOB_SNAP_TREE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_FROM_VAULT_FIELD_NUMBER: _ClassVar[int]
    APPROX_PER_SHARD_CM_TABLE_CLEANUP_SIZE_KB_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_ENABLE_CHUNK_METADATA_CLEANER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_ENABLE_CCFM_FIXER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TO_EPOCH_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_ENABLE_CLOUD_DOMAIN_GC_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_ENABLE_CLOUD_DOMAIN_TIERING_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_CCFM_DOUBLE_SCAN_TO_VALIDATE_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_SKIP_CSR_GC_FOR_DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_SKIP_CCR_GC_FOR_DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_VALIDATE_CLOUD_CHUNK_FILES_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_GC_VALIDATE_DANGLING_MINION_BRICKS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_GC_CACHE_REFS_TO_CLOUD_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_GC_ADD_SCAN_ORDER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ORION_GC_ENABLE_WORM_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    apollo_mr_enable_orion_healer_algos: bool
    domain_id_vec: _containers.RepeatedScalarFieldContainer[int]
    max_view_snap_tree_height: int
    max_blob_snap_tree_height: int
    view_box_name: str
    view_name: str
    fs_name: str
    cluster_id: int
    list_from_vault: bool
    approx_per_shard_cm_table_cleanup_size_kb: int
    apollo_mr_orion_enable_chunk_metadata_cleaner: bool
    apollo_mr_orion_enable_ccfm_fixer: bool
    domain_to_epoch_id_map: _containers.ScalarMap[int, int]
    apollo_mr_orion_enable_cloud_domain_gc: bool
    apollo_mr_orion_enable_cloud_domain_tiering: bool
    apollo_mr_orion_ccfm_double_scan_to_validate: bool
    apollo_mr_orion_skip_csr_gc_for_domain_ids: str
    apollo_mr_orion_skip_ccr_gc_for_domain_ids: str
    apollo_mr_orion_validate_cloud_chunk_files: bool
    apollo_mr_orion_gc_validate_dangling_minion_bricks: bool
    apollo_mr_orion_gc_cache_refs_to_cloud_chunks: bool
    apollo_mr_orion_gc_add_scan_order: bool
    apollo_mr_orion_gc_enable_worm_domains: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., apollo_mr_enable_orion_healer_algos: bool = ..., domain_id_vec: _Optional[_Iterable[int]] = ..., max_view_snap_tree_height: _Optional[int] = ..., max_blob_snap_tree_height: _Optional[int] = ..., view_box_name: _Optional[str] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., cluster_id: _Optional[int] = ..., list_from_vault: bool = ..., approx_per_shard_cm_table_cleanup_size_kb: _Optional[int] = ..., apollo_mr_orion_enable_chunk_metadata_cleaner: bool = ..., apollo_mr_orion_enable_ccfm_fixer: bool = ..., domain_to_epoch_id_map: _Optional[_Mapping[int, int]] = ..., apollo_mr_orion_enable_cloud_domain_gc: bool = ..., apollo_mr_orion_enable_cloud_domain_tiering: bool = ..., apollo_mr_orion_ccfm_double_scan_to_validate: bool = ..., apollo_mr_orion_skip_csr_gc_for_domain_ids: _Optional[str] = ..., apollo_mr_orion_skip_ccr_gc_for_domain_ids: _Optional[str] = ..., apollo_mr_orion_validate_cloud_chunk_files: bool = ..., apollo_mr_orion_gc_validate_dangling_minion_bricks: bool = ..., apollo_mr_orion_gc_cache_refs_to_cloud_chunks: bool = ..., apollo_mr_orion_gc_add_scan_order: bool = ..., apollo_mr_orion_gc_enable_worm_domains: bool = ...) -> None: ...

class OrionHealerVaultSourceProto(_message.Message):
    __slots__ = ("node", "vst_value", "brick_meta", "s3object_st_value", "cloud_object_id", "epoch_id", "tree_type")
    NODE_FIELD_NUMBER: _ClassVar[int]
    VST_VALUE_FIELD_NUMBER: _ClassVar[int]
    BRICK_META_FIELD_NUMBER: _ClassVar[int]
    S3OBJECT_ST_VALUE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    node: _snap_tree_pb2.SnapTreeNodeProto
    vst_value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
    brick_meta: _blob_store_pb2.BrickMetadataProto
    s3object_st_value: _s3_metadata_pb2.S3ObjectSnapTreeValueProto
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    epoch_id: int
    tree_type: _icebox_pb2.IceboxSnapTreeType
    def __init__(self, node: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ..., vst_value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ..., brick_meta: _Optional[_Union[_blob_store_pb2.BrickMetadataProto, _Mapping]] = ..., s3object_st_value: _Optional[_Union[_s3_metadata_pb2.S3ObjectSnapTreeValueProto, _Mapping]] = ..., cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., epoch_id: _Optional[int] = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ...) -> None: ...

class OrionHealerKeyProto(_message.Message):
    __slots__ = ("cloud_node_ptr", "snap_tree_node_id", "cloud_object_id", "cloud_domain_id", "is_csr_object", "is_validate_action")
    CLOUD_NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CSR_OBJECT_FIELD_NUMBER: _ClassVar[int]
    IS_VALIDATE_ACTION_FIELD_NUMBER: _ClassVar[int]
    cloud_node_ptr: CloudDomainNodePtrProto
    snap_tree_node_id: int
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    cloud_domain_id: int
    is_csr_object: bool
    is_validate_action: bool
    def __init__(self, cloud_node_ptr: _Optional[_Union[CloudDomainNodePtrProto, _Mapping]] = ..., snap_tree_node_id: _Optional[int] = ..., cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., is_csr_object: bool = ..., is_validate_action: bool = ...) -> None: ...

class OrionHealerValueProto(_message.Message):
    __slots__ = ("num_references", "cloud_child_node_ptr_vec", "cloud_object_id", "live_node_ptr_vec", "live_cloud_chunk_id_vec", "chunk_count", "node_count", "extension_stats_map", "scribe_row_version", "epoch_id", "parent_epoch_id", "utility_score", "latest_expiry_time_days", "is_leaf_node", "is_root_node", "referred_local_nodes_vec", "dead_local_nodes_vec", "brick_meta", "last_touch_secs", "num_cm_rows", "delete_cloud_object_id_vec", "chunk_meta", "chunk_id_vec", "proto_size_bytes", "brick_meta_reference", "cm_table_entry_expected", "cm_table_entry_present", "validate_local_nodes_vec", "all_cloud_chunk_id_vec", "skip_ccfm_chunk_count_validation", "post_scan_scribe_row_version", "cm_referred_cloud_chunk_id_vec", "brick_referred_cloud_chunk_id_vec", "cm_unlikely_to_dedup", "tier_type", "current_tier_rank", "do_not_partial_gc", "do_not_lcm", "is_forwarded_from_prev_level_reducer", "found_in_vault", "tree_type", "num_scribe_references", "validate_ccr_object", "last_file_existence_validation_secs", "last_chunk_existence_validation_secs", "last_chunk_data_validation_secs", "validate_cloud_chunk_checksum", "is_minion_brick_node", "not_found_in_vault", "cloud_parent_node_ptr_vec", "in_archive_tier", "worm_params", "worm_retention_extendability_info", "cloud_object_size")
    class ExtensionStatsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _view_usage_pb2.ViewUsageProto.ExtensionStatsProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_view_usage_pb2.ViewUsageProto.ExtensionStatsProto, _Mapping]] = ...) -> None: ...
    NUM_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHILD_NODE_PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_NODE_PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    LIVE_CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_STATS_MAP_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    UTILITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    LATEST_EXPIRY_TIME_DAYS_FIELD_NUMBER: _ClassVar[int]
    IS_LEAF_NODE_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_NODE_FIELD_NUMBER: _ClassVar[int]
    REFERRED_LOCAL_NODES_VEC_FIELD_NUMBER: _ClassVar[int]
    DEAD_LOCAL_NODES_VEC_FIELD_NUMBER: _ClassVar[int]
    BRICK_META_FIELD_NUMBER: _ClassVar[int]
    LAST_TOUCH_SECS_FIELD_NUMBER: _ClassVar[int]
    NUM_CM_ROWS_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLOUD_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_META_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PROTO_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BRICK_META_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CM_TABLE_ENTRY_EXPECTED_FIELD_NUMBER: _ClassVar[int]
    CM_TABLE_ENTRY_PRESENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_LOCAL_NODES_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_CCFM_CHUNK_COUNT_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    CM_REFERRED_CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BRICK_REFERRED_CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CM_UNLIKELY_TO_DEDUP_FIELD_NUMBER: _ClassVar[int]
    TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIER_RANK_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_PARTIAL_GC_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_LCM_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FROM_PREV_LEVEL_REDUCER_FIELD_NUMBER: _ClassVar[int]
    FOUND_IN_VAULT_FIELD_NUMBER: _ClassVar[int]
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_SCRIBE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_CCR_OBJECT_FIELD_NUMBER: _ClassVar[int]
    LAST_FILE_EXISTENCE_VALIDATION_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHUNK_EXISTENCE_VALIDATION_SECS_FIELD_NUMBER: _ClassVar[int]
    LAST_CHUNK_DATA_VALIDATION_SECS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_CLOUD_CHUNK_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    IS_MINION_BRICK_NODE_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_IN_VAULT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PARENT_NODE_PTR_VEC_FIELD_NUMBER: _ClassVar[int]
    IN_ARCHIVE_TIER_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_EXTENDABILITY_INFO_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    num_references: int
    cloud_child_node_ptr_vec: CloudDomainNodePtrVec
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    live_node_ptr_vec: CloudDomainNodePtrVec
    live_cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
    chunk_count: int
    node_count: int
    extension_stats_map: _containers.MessageMap[str, _view_usage_pb2.ViewUsageProto.ExtensionStatsProto]
    scribe_row_version: int
    epoch_id: int
    parent_epoch_id: int
    utility_score: int
    latest_expiry_time_days: int
    is_leaf_node: bool
    is_root_node: bool
    referred_local_nodes_vec: _containers.RepeatedScalarFieldContainer[int]
    dead_local_nodes_vec: _containers.RepeatedScalarFieldContainer[int]
    brick_meta: _blob_store_pb2.BrickMetadataProto
    last_touch_secs: int
    num_cm_rows: int
    delete_cloud_object_id_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.CloudObjectIdProto]
    chunk_meta: _blob_store_pb2.ChunkMetadataProto
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
    proto_size_bytes: int
    brick_meta_reference: bool
    cm_table_entry_expected: bool
    cm_table_entry_present: bool
    validate_local_nodes_vec: _containers.RepeatedScalarFieldContainer[int]
    all_cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
    skip_ccfm_chunk_count_validation: bool
    post_scan_scribe_row_version: int
    cm_referred_cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
    brick_referred_cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
    cm_unlikely_to_dedup: bool
    tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
    current_tier_rank: int
    do_not_partial_gc: bool
    do_not_lcm: bool
    is_forwarded_from_prev_level_reducer: bool
    found_in_vault: bool
    tree_type: _icebox_pb2.IceboxSnapTreeType
    num_scribe_references: int
    validate_ccr_object: bool
    last_file_existence_validation_secs: int
    last_chunk_existence_validation_secs: int
    last_chunk_data_validation_secs: int
    validate_cloud_chunk_checksum: bool
    is_minion_brick_node: bool
    not_found_in_vault: bool
    cloud_parent_node_ptr_vec: CloudDomainNodePtrVec
    in_archive_tier: bool
    worm_params: _worm_pb2.WORMParams
    worm_retention_extendability_info: _worm_pb2.WORMRetentionExtendabilityInfo
    cloud_object_size: int
    def __init__(self, num_references: _Optional[int] = ..., cloud_child_node_ptr_vec: _Optional[_Union[CloudDomainNodePtrVec, _Mapping]] = ..., cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., live_node_ptr_vec: _Optional[_Union[CloudDomainNodePtrVec, _Mapping]] = ..., live_cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., chunk_count: _Optional[int] = ..., node_count: _Optional[int] = ..., extension_stats_map: _Optional[_Mapping[str, _view_usage_pb2.ViewUsageProto.ExtensionStatsProto]] = ..., scribe_row_version: _Optional[int] = ..., epoch_id: _Optional[int] = ..., parent_epoch_id: _Optional[int] = ..., utility_score: _Optional[int] = ..., latest_expiry_time_days: _Optional[int] = ..., is_leaf_node: bool = ..., is_root_node: bool = ..., referred_local_nodes_vec: _Optional[_Iterable[int]] = ..., dead_local_nodes_vec: _Optional[_Iterable[int]] = ..., brick_meta: _Optional[_Union[_blob_store_pb2.BrickMetadataProto, _Mapping]] = ..., last_touch_secs: _Optional[int] = ..., num_cm_rows: _Optional[int] = ..., delete_cloud_object_id_vec: _Optional[_Iterable[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]]] = ..., chunk_meta: _Optional[_Union[_blob_store_pb2.ChunkMetadataProto, _Mapping]] = ..., chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., proto_size_bytes: _Optional[int] = ..., brick_meta_reference: bool = ..., cm_table_entry_expected: bool = ..., cm_table_entry_present: bool = ..., validate_local_nodes_vec: _Optional[_Iterable[int]] = ..., all_cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., skip_ccfm_chunk_count_validation: bool = ..., post_scan_scribe_row_version: _Optional[int] = ..., cm_referred_cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., brick_referred_cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., cm_unlikely_to_dedup: bool = ..., tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., current_tier_rank: _Optional[int] = ..., do_not_partial_gc: bool = ..., do_not_lcm: bool = ..., is_forwarded_from_prev_level_reducer: bool = ..., found_in_vault: bool = ..., tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., num_scribe_references: _Optional[int] = ..., validate_ccr_object: bool = ..., last_file_existence_validation_secs: _Optional[int] = ..., last_chunk_existence_validation_secs: _Optional[int] = ..., last_chunk_data_validation_secs: _Optional[int] = ..., validate_cloud_chunk_checksum: bool = ..., is_minion_brick_node: bool = ..., not_found_in_vault: bool = ..., cloud_parent_node_ptr_vec: _Optional[_Union[CloudDomainNodePtrVec, _Mapping]] = ..., in_archive_tier: bool = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ..., worm_retention_extendability_info: _Optional[_Union[_worm_pb2.WORMRetentionExtendabilityInfo, _Mapping]] = ..., cloud_object_size: _Optional[int] = ...) -> None: ...
