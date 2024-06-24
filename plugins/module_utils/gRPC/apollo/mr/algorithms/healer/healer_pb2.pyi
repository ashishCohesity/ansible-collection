from apollo.mr.algorithms.inode_stats.utils import utils_pb2 as _utils_pb2
from apollo.mr.algorithms.utils import universal_id_set_pb2 as _universal_id_set_pb2
from apollo.mr.base import action_pb2 as _action_pb2
from bridge.base import apollo_actions_base_pb2 as _apollo_actions_base_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "enable_refcount_fixer_for_quota_trees", "apollo_mr_enable_blob_metadata_fixer", "apollo_mr_enable_chunk_file_metadata_fixer", "apollo_mr_enable_chunk_file_access_cleaner", "apollo_mr_enable_minion_blob_garbage_collector", "apollo_mr_enable_blob_root_delete_action_verification", "apollo_mr_enable_view_metadata_fixer", "apollo_mr_enable_view_box_deleter", "deletable_view_boxes", "apollo_mr_enable_view_usage_cleaner", "apollo_mr_enable_defunct_chunk_cleaner", "apollo_mr_enable_refcount_fixer_for_antivirus_trees", "apollo_mr_healer_run_blob_metadata_fixer_in_debug_mode", "apollo_mr_enable_archived_node_locations_cleaner", "icebox_clean_snap_tree_nodes_info", "apollo_mr_healer_delete_stale_chunk_mapping", "apollo_mr_enable_view_snap_tree_root_delete_verification", "num_scribe_buckets", "apollo_mr_enable_blur_scan", "apollo_mr_enable_s3object_snap_tree_cleaner", "apollo_mr_enable_apollo_binary_logging", "apollo_mr_enable_chunk_metadata_scan", "apollo_mr_enable_refcount_fixer_for_dir_quota_trees")
    class ViewBoxDeletionInfo(_message.Message):
        __slots__ = ("view_box_id", "opclock_vec")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
        def __init__(self, view_box_id: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...
    class IceboxSnapTreeCleaningInfo(_message.Message):
        __slots__ = ("in_use_archives", "latest_full_archives")
        IN_USE_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
        LATEST_FULL_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
        in_use_archives: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
        latest_full_archives: _containers.RepeatedCompositeFieldContainer[_universal_id_set_pb2.UniversalIdSetProto]
        def __init__(self, in_use_archives: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ..., latest_full_archives: _Optional[_Iterable[_Union[_universal_id_set_pb2.UniversalIdSetProto, _Mapping]]] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REFCOUNT_FIXER_FOR_QUOTA_TREES_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_BLOB_METADATA_FIXER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_CHUNK_FILE_METADATA_FIXER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_CHUNK_FILE_ACCESS_CLEANER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_MINION_BLOB_GARBAGE_COLLECTOR_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_BLOB_ROOT_DELETE_ACTION_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_VIEW_METADATA_FIXER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_VIEW_BOX_DELETER_FIELD_NUMBER: _ClassVar[int]
    DELETABLE_VIEW_BOXES_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_VIEW_USAGE_CLEANER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_DEFUNCT_CHUNK_CLEANER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_REFCOUNT_FIXER_FOR_ANTIVIRUS_TREES_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_HEALER_RUN_BLOB_METADATA_FIXER_IN_DEBUG_MODE_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_ARCHIVED_NODE_LOCATIONS_CLEANER_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_CLEAN_SNAP_TREE_NODES_INFO_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_HEALER_DELETE_STALE_CHUNK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_VIEW_SNAP_TREE_ROOT_DELETE_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    NUM_SCRIBE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_BLUR_SCAN_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_S3OBJECT_SNAP_TREE_CLEANER_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_APOLLO_BINARY_LOGGING_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_CHUNK_METADATA_SCAN_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MR_ENABLE_REFCOUNT_FIXER_FOR_DIR_QUOTA_TREES_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    enable_refcount_fixer_for_quota_trees: bool
    apollo_mr_enable_blob_metadata_fixer: bool
    apollo_mr_enable_chunk_file_metadata_fixer: bool
    apollo_mr_enable_chunk_file_access_cleaner: bool
    apollo_mr_enable_minion_blob_garbage_collector: bool
    apollo_mr_enable_blob_root_delete_action_verification: bool
    apollo_mr_enable_view_metadata_fixer: bool
    apollo_mr_enable_view_box_deleter: bool
    deletable_view_boxes: _containers.RepeatedCompositeFieldContainer[HealerContextDataProto.ViewBoxDeletionInfo]
    apollo_mr_enable_view_usage_cleaner: bool
    apollo_mr_enable_defunct_chunk_cleaner: bool
    apollo_mr_enable_refcount_fixer_for_antivirus_trees: bool
    apollo_mr_healer_run_blob_metadata_fixer_in_debug_mode: bool
    apollo_mr_enable_archived_node_locations_cleaner: bool
    icebox_clean_snap_tree_nodes_info: HealerContextDataProto.IceboxSnapTreeCleaningInfo
    apollo_mr_healer_delete_stale_chunk_mapping: bool
    apollo_mr_enable_view_snap_tree_root_delete_verification: bool
    num_scribe_buckets: int
    apollo_mr_enable_blur_scan: bool
    apollo_mr_enable_s3object_snap_tree_cleaner: bool
    apollo_mr_enable_apollo_binary_logging: bool
    apollo_mr_enable_chunk_metadata_scan: bool
    apollo_mr_enable_refcount_fixer_for_dir_quota_trees: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., enable_refcount_fixer_for_quota_trees: bool = ..., apollo_mr_enable_blob_metadata_fixer: bool = ..., apollo_mr_enable_chunk_file_metadata_fixer: bool = ..., apollo_mr_enable_chunk_file_access_cleaner: bool = ..., apollo_mr_enable_minion_blob_garbage_collector: bool = ..., apollo_mr_enable_blob_root_delete_action_verification: bool = ..., apollo_mr_enable_view_metadata_fixer: bool = ..., apollo_mr_enable_view_box_deleter: bool = ..., deletable_view_boxes: _Optional[_Iterable[_Union[HealerContextDataProto.ViewBoxDeletionInfo, _Mapping]]] = ..., apollo_mr_enable_view_usage_cleaner: bool = ..., apollo_mr_enable_defunct_chunk_cleaner: bool = ..., apollo_mr_enable_refcount_fixer_for_antivirus_trees: bool = ..., apollo_mr_healer_run_blob_metadata_fixer_in_debug_mode: bool = ..., apollo_mr_enable_archived_node_locations_cleaner: bool = ..., icebox_clean_snap_tree_nodes_info: _Optional[_Union[HealerContextDataProto.IceboxSnapTreeCleaningInfo, _Mapping]] = ..., apollo_mr_healer_delete_stale_chunk_mapping: bool = ..., apollo_mr_enable_view_snap_tree_root_delete_verification: bool = ..., num_scribe_buckets: _Optional[int] = ..., apollo_mr_enable_blur_scan: bool = ..., apollo_mr_enable_s3object_snap_tree_cleaner: bool = ..., apollo_mr_enable_apollo_binary_logging: bool = ..., apollo_mr_enable_chunk_metadata_scan: bool = ..., apollo_mr_enable_refcount_fixer_for_dir_quota_trees: bool = ...) -> None: ...

class ChunkFileActionInfoProto(_message.Message):
    __slots__ = ("version", "owner_blob_id", "chunk_count", "chunk_file_physical_bytes", "view_box_id", "has_brick_owned_chunks", "chunk_physical_bytes", "num_data_stripes", "num_coded_stripes", "has_dedup_chunks", "actual_chunk_file_physical_bytes", "morphed_size_hint", "is_container_chunk_file")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_BRICK_OWNED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
    NUM_CODED_STRIPES_FIELD_NUMBER: _ClassVar[int]
    HAS_DEDUP_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_CHUNK_FILE_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    MORPHED_SIZE_HINT_FIELD_NUMBER: _ClassVar[int]
    IS_CONTAINER_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    version: int
    owner_blob_id: int
    chunk_count: int
    chunk_file_physical_bytes: int
    view_box_id: int
    has_brick_owned_chunks: bool
    chunk_physical_bytes: int
    num_data_stripes: int
    num_coded_stripes: int
    has_dedup_chunks: bool
    actual_chunk_file_physical_bytes: int
    morphed_size_hint: int
    is_container_chunk_file: bool
    def __init__(self, version: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., chunk_count: _Optional[int] = ..., chunk_file_physical_bytes: _Optional[int] = ..., view_box_id: _Optional[int] = ..., has_brick_owned_chunks: bool = ..., chunk_physical_bytes: _Optional[int] = ..., num_data_stripes: _Optional[int] = ..., num_coded_stripes: _Optional[int] = ..., has_dedup_chunks: bool = ..., actual_chunk_file_physical_bytes: _Optional[int] = ..., morphed_size_hint: _Optional[int] = ..., is_container_chunk_file: bool = ...) -> None: ...

class ChunkRefCountMapValueProto(_message.Message):
    __slots__ = ("op_in_progress", "chunk_file_metadata_info", "brick_info", "chunk_metadata_info")
    class BrickInfo(_message.Message):
        __slots__ = ("chunk_file_id", "brick_snap_tree_node_id", "skip_dangling_stale_defunct_chunk_checks", "row_version")
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        BRICK_SNAP_TREE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        SKIP_DANGLING_STALE_DEFUNCT_CHUNK_CHECKS_FIELD_NUMBER: _ClassVar[int]
        ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        chunk_file_id: int
        brick_snap_tree_node_id: int
        skip_dangling_stale_defunct_chunk_checks: bool
        row_version: int
        def __init__(self, chunk_file_id: _Optional[int] = ..., brick_snap_tree_node_id: _Optional[int] = ..., skip_dangling_stale_defunct_chunk_checks: bool = ..., row_version: _Optional[int] = ...) -> None: ...
    class ChunkFileMetadataInfo(_message.Message):
        __slots__ = ("chunk_file_id", "intent_pending", "chunk_morphed_bytes")
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        INTENT_PENDING_FIELD_NUMBER: _ClassVar[int]
        CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        chunk_file_id: int
        intent_pending: bool
        chunk_morphed_bytes: int
        def __init__(self, chunk_file_id: _Optional[int] = ..., intent_pending: bool = ..., chunk_morphed_bytes: _Optional[int] = ...) -> None: ...
    class ChunkMetadataInfo(_message.Message):
        __slots__ = ("chunk_file_id", "row_version", "skip_dangling_stale_defunct_chunk_checks")
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        SKIP_DANGLING_STALE_DEFUNCT_CHUNK_CHECKS_FIELD_NUMBER: _ClassVar[int]
        chunk_file_id: int
        row_version: int
        skip_dangling_stale_defunct_chunk_checks: bool
        def __init__(self, chunk_file_id: _Optional[int] = ..., row_version: _Optional[int] = ..., skip_dangling_stale_defunct_chunk_checks: bool = ...) -> None: ...
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    BRICK_INFO_FIELD_NUMBER: _ClassVar[int]
    CHUNK_METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    op_in_progress: bool
    chunk_file_metadata_info: ChunkRefCountMapValueProto.ChunkFileMetadataInfo
    brick_info: ChunkRefCountMapValueProto.BrickInfo
    chunk_metadata_info: ChunkRefCountMapValueProto.ChunkMetadataInfo
    def __init__(self, op_in_progress: bool = ..., chunk_file_metadata_info: _Optional[_Union[ChunkRefCountMapValueProto.ChunkFileMetadataInfo, _Mapping]] = ..., brick_info: _Optional[_Union[ChunkRefCountMapValueProto.BrickInfo, _Mapping]] = ..., chunk_metadata_info: _Optional[_Union[ChunkRefCountMapValueProto.ChunkMetadataInfo, _Mapping]] = ...) -> None: ...

class ChunkFileMapValueProto(_message.Message):
    __slots__ = ("chunk_file_action_info", "delete_chunk_info", "migrate_info", "should_downtier_on_migrate", "imbalance_info")
    class ChunkInfo(_message.Message):
        __slots__ = ("chunk_id", "chunk_morphed_bytes")
        CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        chunk_id: _blob_store_pb2.ChunkIdProto
        chunk_morphed_bytes: int
        def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., chunk_morphed_bytes: _Optional[int] = ...) -> None: ...
    class MigrateInfo(_message.Message):
        __slots__ = ("chunk_logical_bytes", "target_tier", "compress_file", "encode_file", "defrag_file", "force_encode", "encode_to_container", "compression_level", "encryption_level", "highest_tier", "disk_id_vec")
        CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIER_FIELD_NUMBER: _ClassVar[int]
        COMPRESS_FILE_FIELD_NUMBER: _ClassVar[int]
        ENCODE_FILE_FIELD_NUMBER: _ClassVar[int]
        DEFRAG_FILE_FIELD_NUMBER: _ClassVar[int]
        FORCE_ENCODE_FIELD_NUMBER: _ClassVar[int]
        ENCODE_TO_CONTAINER_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        HIGHEST_TIER_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        chunk_logical_bytes: int
        target_tier: str
        compress_file: bool
        encode_file: bool
        defrag_file: bool
        force_encode: bool
        encode_to_container: bool
        compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
        encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
        highest_tier: str
        disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, chunk_logical_bytes: _Optional[int] = ..., target_tier: _Optional[str] = ..., compress_file: bool = ..., encode_file: bool = ..., defrag_file: bool = ..., force_encode: bool = ..., encode_to_container: bool = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., highest_tier: _Optional[str] = ..., disk_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class ImbalanceInfo(_message.Message):
        __slots__ = ("imbalance_pct", "imbalance_bytes")
        IMBALANCE_PCT_FIELD_NUMBER: _ClassVar[int]
        IMBALANCE_BYTES_FIELD_NUMBER: _ClassVar[int]
        imbalance_pct: int
        imbalance_bytes: int
        def __init__(self, imbalance_pct: _Optional[int] = ..., imbalance_bytes: _Optional[int] = ...) -> None: ...
    CHUNK_FILE_ACTION_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_CHUNK_INFO_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DOWNTIER_ON_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    IMBALANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    chunk_file_action_info: ChunkFileActionInfoProto
    delete_chunk_info: ChunkFileMapValueProto.ChunkInfo
    migrate_info: ChunkFileMapValueProto.MigrateInfo
    should_downtier_on_migrate: bool
    imbalance_info: ChunkFileMapValueProto.ImbalanceInfo
    def __init__(self, chunk_file_action_info: _Optional[_Union[ChunkFileActionInfoProto, _Mapping]] = ..., delete_chunk_info: _Optional[_Union[ChunkFileMapValueProto.ChunkInfo, _Mapping]] = ..., migrate_info: _Optional[_Union[ChunkFileMapValueProto.MigrateInfo, _Mapping]] = ..., should_downtier_on_migrate: bool = ..., imbalance_info: _Optional[_Union[ChunkFileMapValueProto.ImbalanceInfo, _Mapping]] = ...) -> None: ...

class SnapTreeRefCountMapValueProto(_message.Message):
    __slots__ = ("node_info", "op_in_progress", "update_intent_present", "child_ref_info")
    class NodeInfo(_message.Message):
        __slots__ = ("is_root", "stored_refcount", "tree_id", "snap_tree_name", "version")
        IS_ROOT_FIELD_NUMBER: _ClassVar[int]
        STORED_REFCOUNT_FIELD_NUMBER: _ClassVar[int]
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        is_root: bool
        stored_refcount: int
        tree_id: int
        snap_tree_name: _apollo_actions_base_pb2.SnapTreeName
        version: int
        def __init__(self, is_root: bool = ..., stored_refcount: _Optional[int] = ..., tree_id: _Optional[int] = ..., snap_tree_name: _Optional[_Union[_apollo_actions_base_pb2.SnapTreeName, str]] = ..., version: _Optional[int] = ...) -> None: ...
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
    CHILD_REF_INFO_FIELD_NUMBER: _ClassVar[int]
    node_info: SnapTreeRefCountMapValueProto.NodeInfo
    op_in_progress: bool
    update_intent_present: bool
    child_ref_info: _action_pb2.SnapTreeChildReferenceInfoProto
    def __init__(self, node_info: _Optional[_Union[SnapTreeRefCountMapValueProto.NodeInfo, _Mapping]] = ..., op_in_progress: bool = ..., update_intent_present: bool = ..., child_ref_info: _Optional[_Union[_action_pb2.SnapTreeChildReferenceInfoProto, _Mapping]] = ...) -> None: ...

class BlobMetadataFixerMapValueProto(_message.Message):
    __slots__ = ("op_in_progress", "is_referenced", "view_box_id", "scribe_row_version", "exists_in_blob_metadata", "is_blob_snap_tree_root_ref", "is_blob_snap_tree_leaf_ref", "is_chunk_file_ref", "extra_debug_info")
    class ExtraDebugInfo(_message.Message):
        __slots__ = ("master_column", "chunk_file_id", "chunk_file_scribe_row_version", "snap_tree_node", "snap_tree_node_version", "brick_metadata", "blob_metadata")
        MASTER_COLUMN_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_NODE_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
        BRICK_METADATA_FIELD_NUMBER: _ClassVar[int]
        BLOB_METADATA_FIELD_NUMBER: _ClassVar[int]
        master_column: _blob_store_pb2.ChunkFileMetadataProto.MasterColumn
        chunk_file_id: int
        chunk_file_scribe_row_version: int
        snap_tree_node: _snap_tree_pb2.SnapTreeNodeProto
        snap_tree_node_version: int
        brick_metadata: _blob_store_pb2.BrickMetadataProto
        blob_metadata: _blob_store_pb2.BlobMetadataProto
        def __init__(self, master_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.MasterColumn, _Mapping]] = ..., chunk_file_id: _Optional[int] = ..., chunk_file_scribe_row_version: _Optional[int] = ..., snap_tree_node: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ..., snap_tree_node_version: _Optional[int] = ..., brick_metadata: _Optional[_Union[_blob_store_pb2.BrickMetadataProto, _Mapping]] = ..., blob_metadata: _Optional[_Union[_blob_store_pb2.BlobMetadataProto, _Mapping]] = ...) -> None: ...
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCED_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXISTS_IN_BLOB_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_BLOB_SNAP_TREE_ROOT_REF_FIELD_NUMBER: _ClassVar[int]
    IS_BLOB_SNAP_TREE_LEAF_REF_FIELD_NUMBER: _ClassVar[int]
    IS_CHUNK_FILE_REF_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    op_in_progress: bool
    is_referenced: bool
    view_box_id: int
    scribe_row_version: int
    exists_in_blob_metadata: bool
    is_blob_snap_tree_root_ref: bool
    is_blob_snap_tree_leaf_ref: bool
    is_chunk_file_ref: bool
    extra_debug_info: BlobMetadataFixerMapValueProto.ExtraDebugInfo
    def __init__(self, op_in_progress: bool = ..., is_referenced: bool = ..., view_box_id: _Optional[int] = ..., scribe_row_version: _Optional[int] = ..., exists_in_blob_metadata: bool = ..., is_blob_snap_tree_root_ref: bool = ..., is_blob_snap_tree_leaf_ref: bool = ..., is_chunk_file_ref: bool = ..., extra_debug_info: _Optional[_Union[BlobMetadataFixerMapValueProto.ExtraDebugInfo, _Mapping]] = ...) -> None: ...

class ChunkFileMetadataFixerMapValueProto(_message.Message):
    __slots__ = ("op_in_progress", "is_referenced", "scribe_row_version", "intent_pending", "blob_id", "view_box_id", "chunk_count", "chunk_file_opclock_vec", "chunk_file_container_id")
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_REFERENCED_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    INTENT_PENDING_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    op_in_progress: bool
    is_referenced: bool
    scribe_row_version: int
    intent_pending: bool
    blob_id: int
    view_box_id: int
    chunk_count: int
    chunk_file_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    chunk_file_container_id: int
    def __init__(self, op_in_progress: bool = ..., is_referenced: bool = ..., scribe_row_version: _Optional[int] = ..., intent_pending: bool = ..., blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., chunk_count: _Optional[int] = ..., chunk_file_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., chunk_file_container_id: _Optional[int] = ...) -> None: ...

class ChunkFileAccessCleanerMapValueProto(_message.Message):
    __slots__ = ("in_chunk_file_metadata_table", "scribe_row_version")
    IN_CHUNK_FILE_METADATA_TABLE_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    in_chunk_file_metadata_table: bool
    scribe_row_version: int
    def __init__(self, in_chunk_file_metadata_table: bool = ..., scribe_row_version: _Optional[int] = ...) -> None: ...

class ViewboxChunkStatsMapValueProto(_message.Message):
    __slots__ = ("non_dedup_chunk_stats", "dedup_chunk_stats")
    NON_DEDUP_CHUNK_STATS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_CHUNK_STATS_FIELD_NUMBER: _ClassVar[int]
    non_dedup_chunk_stats: _utils_pb2.SummarizedChunkStatsProto
    dedup_chunk_stats: _utils_pb2.SummarizedChunkStatsProto
    def __init__(self, non_dedup_chunk_stats: _Optional[_Union[_utils_pb2.SummarizedChunkStatsProto, _Mapping]] = ..., dedup_chunk_stats: _Optional[_Union[_utils_pb2.SummarizedChunkStatsProto, _Mapping]] = ...) -> None: ...

class MinionBlobGCMapValueProto(_message.Message):
    __slots__ = ("used_range", "referenced_range", "is_minion_blob", "view_box_id", "brick_info")
    class Range(_message.Message):
        __slots__ = ("offset", "count")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        offset: int
        count: int
        def __init__(self, offset: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    class BrickInfo(_message.Message):
        __slots__ = ("brick_number", "brick_value_version")
        BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        BRICK_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        brick_number: int
        brick_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        def __init__(self, brick_number: _Optional[int] = ..., brick_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...
    USED_RANGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_RANGE_FIELD_NUMBER: _ClassVar[int]
    IS_MINION_BLOB_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_INFO_FIELD_NUMBER: _ClassVar[int]
    used_range: MinionBlobGCMapValueProto.Range
    referenced_range: MinionBlobGCMapValueProto.Range
    is_minion_blob: bool
    view_box_id: int
    brick_info: MinionBlobGCMapValueProto.BrickInfo
    def __init__(self, used_range: _Optional[_Union[MinionBlobGCMapValueProto.Range, _Mapping]] = ..., referenced_range: _Optional[_Union[MinionBlobGCMapValueProto.Range, _Mapping]] = ..., is_minion_blob: bool = ..., view_box_id: _Optional[int] = ..., brick_info: _Optional[_Union[MinionBlobGCMapValueProto.BrickInfo, _Mapping]] = ...) -> None: ...

class ViewMetadataFixerInfoProto(_message.Message):
    __slots__ = ("op_in_progress", "view_name_info", "view_id_info")
    class ViewNameInfo(_message.Message):
        __slots__ = ("view_name",)
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        view_name: bytes
        def __init__(self, view_name: _Optional[bytes] = ...) -> None: ...
    class ViewIdInfo(_message.Message):
        __slots__ = ("view_box_id", "update_intent_present")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        update_intent_present: bool
        def __init__(self, view_box_id: _Optional[int] = ..., update_intent_present: bool = ...) -> None: ...
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_INFO_FIELD_NUMBER: _ClassVar[int]
    op_in_progress: bool
    view_name_info: ViewMetadataFixerInfoProto.ViewNameInfo
    view_id_info: ViewMetadataFixerInfoProto.ViewIdInfo
    def __init__(self, op_in_progress: bool = ..., view_name_info: _Optional[_Union[ViewMetadataFixerInfoProto.ViewNameInfo, _Mapping]] = ..., view_id_info: _Optional[_Union[ViewMetadataFixerInfoProto.ViewIdInfo, _Mapping]] = ...) -> None: ...

class ViewUsageCleanerProto(_message.Message):
    __slots__ = ("is_present_in_view_metadata", "scribe_row_version")
    IS_PRESENT_IN_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    is_present_in_view_metadata: bool
    scribe_row_version: int
    def __init__(self, is_present_in_view_metadata: bool = ..., scribe_row_version: _Optional[int] = ...) -> None: ...

class DeleteBlobSnapTreeRootValueProto(_message.Message):
    __slots__ = ("is_referenced", "view_snaptree_node_version", "view_snaptree_node_proto", "view_snaptree_value")
    IS_REFERENCED_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAPTREE_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAPTREE_NODE_PROTO_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAPTREE_VALUE_FIELD_NUMBER: _ClassVar[int]
    is_referenced: bool
    view_snaptree_node_version: int
    view_snaptree_node_proto: _snap_tree_pb2.SnapTreeNodeProto
    view_snaptree_value: _snap_fs_metadata_pb2.ViewSnapTreeValueProto
    def __init__(self, is_referenced: bool = ..., view_snaptree_node_version: _Optional[int] = ..., view_snaptree_node_proto: _Optional[_Union[_snap_tree_pb2.SnapTreeNodeProto, _Mapping]] = ..., view_snaptree_value: _Optional[_Union[_snap_fs_metadata_pb2.ViewSnapTreeValueProto, _Mapping]] = ...) -> None: ...

class DeleteViewSnapTreeRootValueProto(_message.Message):
    __slots__ = ("view_id", "row_version", "op_in_progress")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    row_version: int
    op_in_progress: bool
    def __init__(self, view_id: _Optional[int] = ..., row_version: _Optional[int] = ..., op_in_progress: bool = ...) -> None: ...

class ChunkFileActionKeyProto(_message.Message):
    __slots__ = ("owner_blob_id", "view_box_id", "count_or_percent")
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_OR_PERCENT_FIELD_NUMBER: _ClassVar[int]
    owner_blob_id: int
    view_box_id: int
    count_or_percent: int
    def __init__(self, owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., count_or_percent: _Optional[int] = ...) -> None: ...

class ChunkFileActionGrouperKeyProto(_message.Message):
    __slots__ = ("utility_bucket", "owner_blob_id", "view_box_id")
    UTILITY_BUCKET_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    utility_bucket: int
    owner_blob_id: int
    view_box_id: int
    def __init__(self, utility_bucket: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ...) -> None: ...
