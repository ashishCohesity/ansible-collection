from configs import cluster_config_pb2 as _cluster_config_pb2
from bridge.apollo import actions_common_pb2 as _actions_common_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApolloAction(_message.Message):
    __slots__ = ("view_box_id", "job_start_opclock_vec", "high_priority_action", "algorithm_id", "node_info", "ping_bridge", "fix_view", "delete_view", "delete_view_box", "delete_chunks", "delete_scribe_rows", "adjust_node_refcounts", "dedup_bricks", "fix_chunk_file_metadata", "downtier_chunk_file_replicas", "rebalance_chunk_file_replicas", "migrate_chunks", "fix_snap_fs_entity_handle", "fix_s3_entity_handle", "delete_bricks", "adjust_inode_physical_size", "delete_cluster_node", "delete_disk", "delete_bridge_constituent", "delete_disk_stats_entity", "delete_node_stats_entity", "delete_view_box_stats_entity", "delete_expired_smb_session", "cloud_spill_chunk_file_replicas", "free_blob_byte_range", "delete_stats_entity_vec", "retire_icebox_archive", "icebox_fix_chunk_location", "icebox_clean_chunk_location_entries_vec", "icebox_clean_snaptree_node_location_entries_vec", "icebox_clean_restored_snaptree_node_location_entries_vec", "fix_view_usage", "fix_user_quota_usage", "delete_user_quota_usage", "insert_scribe_row", "v2_action_payload_offset_vec", "v2_action_blob_id")
    class MigrateMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDefrag: _ClassVar[ApolloAction.MigrateMode]
        kCompress: _ClassVar[ApolloAction.MigrateMode]
        kErasurecode: _ClassVar[ApolloAction.MigrateMode]
        kEncrypt: _ClassVar[ApolloAction.MigrateMode]
    kDefrag: ApolloAction.MigrateMode
    kCompress: ApolloAction.MigrateMode
    kErasurecode: ApolloAction.MigrateMode
    kEncrypt: ApolloAction.MigrateMode
    class NodeInfo(_message.Message):
        __slots__ = ("expected_alive_nodes", "expected_down_nodes", "preferred_node_id")
        EXPECTED_ALIVE_NODES_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_DOWN_NODES_FIELD_NUMBER: _ClassVar[int]
        PREFERRED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        expected_alive_nodes: _containers.RepeatedScalarFieldContainer[int]
        expected_down_nodes: _containers.RepeatedScalarFieldContainer[int]
        preferred_node_id: int
        def __init__(self, expected_alive_nodes: _Optional[_Iterable[int]] = ..., expected_down_nodes: _Optional[_Iterable[int]] = ..., preferred_node_id: _Optional[int] = ...) -> None: ...
    class PingBridge(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class DeleteViewBox(_message.Message):
        __slots__ = ("view_box_id", "ack_for_apollo", "delete_view_box")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        ACK_FOR_APOLLO_FIELD_NUMBER: _ClassVar[int]
        DELETE_VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        ack_for_apollo: bool
        delete_view_box: bool
        def __init__(self, view_box_id: _Optional[int] = ..., ack_for_apollo: bool = ..., delete_view_box: bool = ...) -> None: ...
    class DeleteChunks(_message.Message):
        __slots__ = ("blob_snap_tree_id", "chunk_file_id", "expected_chunk_file_version", "serialized_chunk_id_proto_vec", "snap_tree_leaf_node_id_vec", "chunk_count")
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_CHUNK_FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
        SERIALIZED_CHUNK_ID_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_LEAF_NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        chunk_file_id: int
        expected_chunk_file_version: int
        serialized_chunk_id_proto_vec: _containers.RepeatedScalarFieldContainer[bytes]
        snap_tree_leaf_node_id_vec: _containers.RepeatedScalarFieldContainer[int]
        chunk_count: int
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., expected_chunk_file_version: _Optional[int] = ..., serialized_chunk_id_proto_vec: _Optional[_Iterable[bytes]] = ..., snap_tree_leaf_node_id_vec: _Optional[_Iterable[int]] = ..., chunk_count: _Optional[int] = ...) -> None: ...
    class DeleteScribeRow(_message.Message):
        __slots__ = ("table_id", "version", "integer_row_key", "string_row_key")
        TABLE_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        INTEGER_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        STRING_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        table_id: int
        version: int
        integer_row_key: int
        string_row_key: str
        def __init__(self, table_id: _Optional[int] = ..., version: _Optional[int] = ..., integer_row_key: _Optional[int] = ..., string_row_key: _Optional[str] = ...) -> None: ...
    class DedupBricks(_message.Message):
        __slots__ = ("blob_snap_tree_id", "brick_number", "num_bricks", "avg_chunk_count")
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NUM_BRICKS_FIELD_NUMBER: _ClassVar[int]
        AVG_CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        brick_number: int
        num_bricks: int
        avg_chunk_count: int
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., brick_number: _Optional[int] = ..., num_bricks: _Optional[int] = ..., avg_chunk_count: _Optional[int] = ...) -> None: ...
    class FixChunkFileMetadata(_message.Message):
        __slots__ = ("blob_snap_tree_id", "chunk_file_id", "fix_replication_action", "chunk_count")
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        FIX_REPLICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        chunk_file_id: int
        fix_replication_action: bool
        chunk_count: int
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., fix_replication_action: bool = ..., chunk_count: _Optional[int] = ...) -> None: ...
    class DowntierChunkFileReplicas(_message.Message):
        __slots__ = ("blob_snap_tree_id", "chunk_file_id", "target_storage_tier", "scribe_version", "source_replica_vec", "chunk_count")
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        SOURCE_REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        chunk_file_id: int
        target_storage_tier: str
        scribe_version: int
        source_replica_vec: _containers.RepeatedScalarFieldContainer[int]
        chunk_count: int
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., target_storage_tier: _Optional[str] = ..., scribe_version: _Optional[int] = ..., source_replica_vec: _Optional[_Iterable[int]] = ..., chunk_count: _Optional[int] = ...) -> None: ...
    class RebalanceChunkFileReplicas(_message.Message):
        __slots__ = ("blob_snap_tree_id", "chunk_file_id", "target_disk_vec", "scribe_version", "chunk_count")
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        chunk_file_id: int
        target_disk_vec: _containers.RepeatedScalarFieldContainer[int]
        scribe_version: int
        chunk_count: int
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., target_disk_vec: _Optional[_Iterable[int]] = ..., scribe_version: _Optional[int] = ..., chunk_count: _Optional[int] = ...) -> None: ...
    class MigrateChunks(_message.Message):
        __slots__ = ("blob_snap_tree_id", "target_storage_tier", "compression_level", "encryption_level", "chunk_file_id_vec", "is_reason_compress", "migrate_mode_vec", "may_increase_space_vec", "chunk_count")
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_REASON_COMPRESS_FIELD_NUMBER: _ClassVar[int]
        MIGRATE_MODE_VEC_FIELD_NUMBER: _ClassVar[int]
        MAY_INCREASE_SPACE_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        target_storage_tier: str
        compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
        encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
        chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
        is_reason_compress: bool
        migrate_mode_vec: _containers.RepeatedScalarFieldContainer[ApolloAction.MigrateMode]
        may_increase_space_vec: _containers.RepeatedScalarFieldContainer[bool]
        chunk_count: int
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., target_storage_tier: _Optional[str] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., chunk_file_id_vec: _Optional[_Iterable[int]] = ..., is_reason_compress: bool = ..., migrate_mode_vec: _Optional[_Iterable[_Union[ApolloAction.MigrateMode, str]]] = ..., may_increase_space_vec: _Optional[_Iterable[bool]] = ..., chunk_count: _Optional[int] = ...) -> None: ...
    class DeleteBricks(_message.Message):
        __slots__ = ("view_snap_tree_id", "view_leaf_node_id", "expected_value_version", "blob_snap_tree_id", "brick_number", "num_bricks", "avg_chunk_count")
        VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NUM_BRICKS_FIELD_NUMBER: _ClassVar[int]
        AVG_CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        view_snap_tree_id: int
        view_leaf_node_id: int
        expected_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        blob_snap_tree_id: int
        brick_number: int
        num_bricks: int
        avg_chunk_count: int
        def __init__(self, view_snap_tree_id: _Optional[int] = ..., view_leaf_node_id: _Optional[int] = ..., expected_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., blob_snap_tree_id: _Optional[int] = ..., brick_number: _Optional[int] = ..., num_bricks: _Optional[int] = ..., avg_chunk_count: _Optional[int] = ...) -> None: ...
    class AdjustInodePhysicalSize(_message.Message):
        __slots__ = ("view_snap_tree_id", "view_leaf_node_id", "expected_value_version", "adjust_amount_bytes")
        VIEW_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        ADJUST_AMOUNT_BYTES_FIELD_NUMBER: _ClassVar[int]
        view_snap_tree_id: int
        view_leaf_node_id: int
        expected_value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        adjust_amount_bytes: int
        def __init__(self, view_snap_tree_id: _Optional[int] = ..., view_leaf_node_id: _Optional[int] = ..., expected_value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., adjust_amount_bytes: _Optional[int] = ...) -> None: ...
    class DeleteClusterNode(_message.Message):
        __slots__ = ("node_id", "disk_ids_to_mark_for_removal", "ack_for_apollo", "delete_from_cluster_partition", "delete_from_cluster")
        class NodeDeleteFromClusterPartitionState(_message.Message):
            __slots__ = ("disk_ids_to_clear_from_removal",)
            DISK_IDS_TO_CLEAR_FROM_REMOVAL_FIELD_NUMBER: _ClassVar[int]
            disk_ids_to_clear_from_removal: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, disk_ids_to_clear_from_removal: _Optional[_Iterable[int]] = ...) -> None: ...
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_IDS_TO_MARK_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
        ACK_FOR_APOLLO_FIELD_NUMBER: _ClassVar[int]
        DELETE_FROM_CLUSTER_PARTITION_FIELD_NUMBER: _ClassVar[int]
        DELETE_FROM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        disk_ids_to_mark_for_removal: _containers.RepeatedScalarFieldContainer[int]
        ack_for_apollo: bool
        delete_from_cluster_partition: ApolloAction.DeleteClusterNode.NodeDeleteFromClusterPartitionState
        delete_from_cluster: bool
        def __init__(self, node_id: _Optional[int] = ..., disk_ids_to_mark_for_removal: _Optional[_Iterable[int]] = ..., ack_for_apollo: bool = ..., delete_from_cluster_partition: _Optional[_Union[ApolloAction.DeleteClusterNode.NodeDeleteFromClusterPartitionState, _Mapping]] = ..., delete_from_cluster: bool = ...) -> None: ...
    class DeleteDisk(_message.Message):
        __slots__ = ("disk_id", "ack_for_apollo", "delete_from_cluster")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        ACK_FOR_APOLLO_FIELD_NUMBER: _ClassVar[int]
        DELETE_FROM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        ack_for_apollo: bool
        delete_from_cluster: bool
        def __init__(self, disk_id: _Optional[int] = ..., ack_for_apollo: bool = ..., delete_from_cluster: bool = ...) -> None: ...
    class DeleteBridgeConstituent(_message.Message):
        __slots__ = ("bridge_constituent_id",)
        BRIDGE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        bridge_constituent_id: int
        def __init__(self, bridge_constituent_id: _Optional[int] = ...) -> None: ...
    class DeleteDiskStatsEntity(_message.Message):
        __slots__ = ("disk_id",)
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        def __init__(self, disk_id: _Optional[int] = ...) -> None: ...
    class DeleteNodeStatsEntity(_message.Message):
        __slots__ = ("node_id",)
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        def __init__(self, node_id: _Optional[int] = ...) -> None: ...
    class DeleteViewBoxStatsEntity(_message.Message):
        __slots__ = ("view_box_id", "view_box_name")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        view_box_name: str
        def __init__(self, view_box_id: _Optional[int] = ..., view_box_name: _Optional[str] = ...) -> None: ...
    class CloudSpillChunkFileReplicas(_message.Message):
        __slots__ = ("blob_snap_tree_id", "target_vault_id", "chunk_files")
        class ChunkFileInfo(_message.Message):
            __slots__ = ("chunk_file_id", "scribe_version", "current_compression_level", "current_encryption_level", "is_erasure_coded")
            CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
            SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
            CURRENT_COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
            CURRENT_ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
            IS_ERASURE_CODED_FIELD_NUMBER: _ClassVar[int]
            chunk_file_id: int
            scribe_version: int
            current_compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
            current_encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
            is_erasure_coded: bool
            def __init__(self, chunk_file_id: _Optional[int] = ..., scribe_version: _Optional[int] = ..., current_compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., current_encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., is_erasure_coded: bool = ...) -> None: ...
        BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILES_FIELD_NUMBER: _ClassVar[int]
        blob_snap_tree_id: int
        target_vault_id: int
        chunk_files: _containers.RepeatedCompositeFieldContainer[ApolloAction.CloudSpillChunkFileReplicas.ChunkFileInfo]
        def __init__(self, blob_snap_tree_id: _Optional[int] = ..., target_vault_id: _Optional[int] = ..., chunk_files: _Optional[_Iterable[_Union[ApolloAction.CloudSpillChunkFileReplicas.ChunkFileInfo, _Mapping]]] = ...) -> None: ...
    class DeleteStatsEntity(_message.Message):
        __slots__ = ("serialized_delete_entity_arg",)
        SERIALIZED_DELETE_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
        serialized_delete_entity_arg: bytes
        def __init__(self, serialized_delete_entity_arg: _Optional[bytes] = ...) -> None: ...
    class RetireIceboxArchive(_message.Message):
        __slots__ = ("archive_uid",)
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class IceboxFixChunkLocation(_message.Message):
        __slots__ = ("chunk_id_str_vec",)
        CHUNK_ID_STR_VEC_FIELD_NUMBER: _ClassVar[int]
        chunk_id_str_vec: _containers.RepeatedScalarFieldContainer[bytes]
        def __init__(self, chunk_id_str_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...
    class IceboxRowEntry(_message.Message):
        __slots__ = ("key_str", "value_str", "version", "num_chunk_locations_deleted", "opclock_vec", "num_non_ref_chunk_locations_deleted")
        KEY_STR_FIELD_NUMBER: _ClassVar[int]
        VALUE_STR_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NUM_CHUNK_LOCATIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
        OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        NUM_NON_REF_CHUNK_LOCATIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
        key_str: bytes
        value_str: bytes
        version: int
        num_chunk_locations_deleted: int
        opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
        num_non_ref_chunk_locations_deleted: int
        def __init__(self, key_str: _Optional[bytes] = ..., value_str: _Optional[bytes] = ..., version: _Optional[int] = ..., num_chunk_locations_deleted: _Optional[int] = ..., opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., num_non_ref_chunk_locations_deleted: _Optional[int] = ...) -> None: ...
    class FixViewUsage(_message.Message):
        __slots__ = ("view_id", "root_snap_tree_id", "user_quota_enabled", "view_name", "mixed_mode_enabled", "root_dir_vec", "viewbox_name")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        USER_QUOTA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        MIXED_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ROOT_DIR_VEC_FIELD_NUMBER: _ClassVar[int]
        VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_snap_tree_id: int
        user_quota_enabled: bool
        view_name: str
        mixed_mode_enabled: bool
        root_dir_vec: _containers.RepeatedScalarFieldContainer[str]
        viewbox_name: str
        def __init__(self, view_id: _Optional[int] = ..., root_snap_tree_id: _Optional[int] = ..., user_quota_enabled: bool = ..., view_name: _Optional[str] = ..., mixed_mode_enabled: bool = ..., root_dir_vec: _Optional[_Iterable[str]] = ..., viewbox_name: _Optional[str] = ...) -> None: ...
    class InsertScribeRow(_message.Message):
        __slots__ = ("table_id", "version", "integer_row_key")
        TABLE_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        INTEGER_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        table_id: int
        version: int
        integer_row_key: int
        def __init__(self, table_id: _Optional[int] = ..., version: _Optional[int] = ..., integer_row_key: _Optional[int] = ...) -> None: ...
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_START_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRIORITY_ACTION_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    PING_BRIDGE_FIELD_NUMBER: _ClassVar[int]
    FIX_VIEW_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
    DELETE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    DELETE_SCRIBE_ROWS_FIELD_NUMBER: _ClassVar[int]
    ADJUST_NODE_REFCOUNTS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_BRICKS_FIELD_NUMBER: _ClassVar[int]
    FIX_CHUNK_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_CHUNK_FILE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_CHUNK_FILE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    FIX_SNAP_FS_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FIX_S3_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DELETE_BRICKS_FIELD_NUMBER: _ClassVar[int]
    ADJUST_INODE_PHYSICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLUSTER_NODE_FIELD_NUMBER: _ClassVar[int]
    DELETE_DISK_FIELD_NUMBER: _ClassVar[int]
    DELETE_BRIDGE_CONSTITUENT_FIELD_NUMBER: _ClassVar[int]
    DELETE_DISK_STATS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DELETE_NODE_STATS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_BOX_STATS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DELETE_EXPIRED_SMB_SESSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPILL_CHUNK_FILE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    FREE_BLOB_BYTE_RANGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_STATS_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    RETIRE_ICEBOX_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_FIX_CHUNK_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_CLEAN_CHUNK_LOCATION_ENTRIES_VEC_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_CLEAN_SNAPTREE_NODE_LOCATION_ENTRIES_VEC_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_CLEAN_RESTORED_SNAPTREE_NODE_LOCATION_ENTRIES_VEC_FIELD_NUMBER: _ClassVar[int]
    FIX_VIEW_USAGE_FIELD_NUMBER: _ClassVar[int]
    FIX_USER_QUOTA_USAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_USER_QUOTA_USAGE_FIELD_NUMBER: _ClassVar[int]
    INSERT_SCRIBE_ROW_FIELD_NUMBER: _ClassVar[int]
    V2_ACTION_PAYLOAD_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
    V2_ACTION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    job_start_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    high_priority_action: bool
    algorithm_id: int
    node_info: ApolloAction.NodeInfo
    ping_bridge: ApolloAction.PingBridge
    fix_view: _actions_common_pb2.FixView
    delete_view: _actions_common_pb2.DeleteView
    delete_view_box: ApolloAction.DeleteViewBox
    delete_chunks: ApolloAction.DeleteChunks
    delete_scribe_rows: _containers.RepeatedCompositeFieldContainer[ApolloAction.DeleteScribeRow]
    adjust_node_refcounts: _containers.RepeatedCompositeFieldContainer[_actions_common_pb2.AdjustNodeRefcountProto]
    dedup_bricks: ApolloAction.DedupBricks
    fix_chunk_file_metadata: ApolloAction.FixChunkFileMetadata
    downtier_chunk_file_replicas: ApolloAction.DowntierChunkFileReplicas
    rebalance_chunk_file_replicas: ApolloAction.RebalanceChunkFileReplicas
    migrate_chunks: ApolloAction.MigrateChunks
    fix_snap_fs_entity_handle: _actions_common_pb2.FixEntityHandle
    fix_s3_entity_handle: _actions_common_pb2.FixEntityHandle
    delete_bricks: ApolloAction.DeleteBricks
    adjust_inode_physical_size: ApolloAction.AdjustInodePhysicalSize
    delete_cluster_node: ApolloAction.DeleteClusterNode
    delete_disk: ApolloAction.DeleteDisk
    delete_bridge_constituent: ApolloAction.DeleteBridgeConstituent
    delete_disk_stats_entity: ApolloAction.DeleteDiskStatsEntity
    delete_node_stats_entity: ApolloAction.DeleteNodeStatsEntity
    delete_view_box_stats_entity: ApolloAction.DeleteViewBoxStatsEntity
    delete_expired_smb_session: _actions_common_pb2.DeleteExpiredSmbSession
    cloud_spill_chunk_file_replicas: ApolloAction.CloudSpillChunkFileReplicas
    free_blob_byte_range: _actions_common_pb2.FreeBlobByteRange
    delete_stats_entity_vec: _containers.RepeatedCompositeFieldContainer[ApolloAction.DeleteStatsEntity]
    retire_icebox_archive: ApolloAction.RetireIceboxArchive
    icebox_fix_chunk_location: ApolloAction.IceboxFixChunkLocation
    icebox_clean_chunk_location_entries_vec: _containers.RepeatedCompositeFieldContainer[ApolloAction.IceboxRowEntry]
    icebox_clean_snaptree_node_location_entries_vec: _containers.RepeatedCompositeFieldContainer[ApolloAction.IceboxRowEntry]
    icebox_clean_restored_snaptree_node_location_entries_vec: _containers.RepeatedCompositeFieldContainer[ApolloAction.IceboxRowEntry]
    fix_view_usage: ApolloAction.FixViewUsage
    fix_user_quota_usage: _actions_common_pb2.FixUserQuotaUsage
    delete_user_quota_usage: _actions_common_pb2.DeleteUserQuotaUsage
    insert_scribe_row: ApolloAction.InsertScribeRow
    v2_action_payload_offset_vec: _containers.RepeatedScalarFieldContainer[int]
    v2_action_blob_id: int
    def __init__(self, view_box_id: _Optional[int] = ..., job_start_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., high_priority_action: bool = ..., algorithm_id: _Optional[int] = ..., node_info: _Optional[_Union[ApolloAction.NodeInfo, _Mapping]] = ..., ping_bridge: _Optional[_Union[ApolloAction.PingBridge, _Mapping]] = ..., fix_view: _Optional[_Union[_actions_common_pb2.FixView, _Mapping]] = ..., delete_view: _Optional[_Union[_actions_common_pb2.DeleteView, _Mapping]] = ..., delete_view_box: _Optional[_Union[ApolloAction.DeleteViewBox, _Mapping]] = ..., delete_chunks: _Optional[_Union[ApolloAction.DeleteChunks, _Mapping]] = ..., delete_scribe_rows: _Optional[_Iterable[_Union[ApolloAction.DeleteScribeRow, _Mapping]]] = ..., adjust_node_refcounts: _Optional[_Iterable[_Union[_actions_common_pb2.AdjustNodeRefcountProto, _Mapping]]] = ..., dedup_bricks: _Optional[_Union[ApolloAction.DedupBricks, _Mapping]] = ..., fix_chunk_file_metadata: _Optional[_Union[ApolloAction.FixChunkFileMetadata, _Mapping]] = ..., downtier_chunk_file_replicas: _Optional[_Union[ApolloAction.DowntierChunkFileReplicas, _Mapping]] = ..., rebalance_chunk_file_replicas: _Optional[_Union[ApolloAction.RebalanceChunkFileReplicas, _Mapping]] = ..., migrate_chunks: _Optional[_Union[ApolloAction.MigrateChunks, _Mapping]] = ..., fix_snap_fs_entity_handle: _Optional[_Union[_actions_common_pb2.FixEntityHandle, _Mapping]] = ..., fix_s3_entity_handle: _Optional[_Union[_actions_common_pb2.FixEntityHandle, _Mapping]] = ..., delete_bricks: _Optional[_Union[ApolloAction.DeleteBricks, _Mapping]] = ..., adjust_inode_physical_size: _Optional[_Union[ApolloAction.AdjustInodePhysicalSize, _Mapping]] = ..., delete_cluster_node: _Optional[_Union[ApolloAction.DeleteClusterNode, _Mapping]] = ..., delete_disk: _Optional[_Union[ApolloAction.DeleteDisk, _Mapping]] = ..., delete_bridge_constituent: _Optional[_Union[ApolloAction.DeleteBridgeConstituent, _Mapping]] = ..., delete_disk_stats_entity: _Optional[_Union[ApolloAction.DeleteDiskStatsEntity, _Mapping]] = ..., delete_node_stats_entity: _Optional[_Union[ApolloAction.DeleteNodeStatsEntity, _Mapping]] = ..., delete_view_box_stats_entity: _Optional[_Union[ApolloAction.DeleteViewBoxStatsEntity, _Mapping]] = ..., delete_expired_smb_session: _Optional[_Union[_actions_common_pb2.DeleteExpiredSmbSession, _Mapping]] = ..., cloud_spill_chunk_file_replicas: _Optional[_Union[ApolloAction.CloudSpillChunkFileReplicas, _Mapping]] = ..., free_blob_byte_range: _Optional[_Union[_actions_common_pb2.FreeBlobByteRange, _Mapping]] = ..., delete_stats_entity_vec: _Optional[_Iterable[_Union[ApolloAction.DeleteStatsEntity, _Mapping]]] = ..., retire_icebox_archive: _Optional[_Union[ApolloAction.RetireIceboxArchive, _Mapping]] = ..., icebox_fix_chunk_location: _Optional[_Union[ApolloAction.IceboxFixChunkLocation, _Mapping]] = ..., icebox_clean_chunk_location_entries_vec: _Optional[_Iterable[_Union[ApolloAction.IceboxRowEntry, _Mapping]]] = ..., icebox_clean_snaptree_node_location_entries_vec: _Optional[_Iterable[_Union[ApolloAction.IceboxRowEntry, _Mapping]]] = ..., icebox_clean_restored_snaptree_node_location_entries_vec: _Optional[_Iterable[_Union[ApolloAction.IceboxRowEntry, _Mapping]]] = ..., fix_view_usage: _Optional[_Union[ApolloAction.FixViewUsage, _Mapping]] = ..., fix_user_quota_usage: _Optional[_Union[_actions_common_pb2.FixUserQuotaUsage, _Mapping]] = ..., delete_user_quota_usage: _Optional[_Union[_actions_common_pb2.DeleteUserQuotaUsage, _Mapping]] = ..., insert_scribe_row: _Optional[_Union[ApolloAction.InsertScribeRow, _Mapping]] = ..., v2_action_payload_offset_vec: _Optional[_Iterable[int]] = ..., v2_action_blob_id: _Optional[int] = ...) -> None: ...
