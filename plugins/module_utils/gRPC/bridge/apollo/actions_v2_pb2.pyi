from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.apollo import actions_common_pb2 as _actions_common_pb2
from bridge.base import apollo_actions_base_pb2 as _apollo_actions_base_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileActionProto(_message.Message):
    __slots__ = ("chunk_file_id_vec", "owner_blob_id", "view_box_id", "delete_chunks_info_vec", "migrate_info", "migrate_chunk_file_info_vec", "fix_chunk_file_info", "shuffle_chunk_file_replicas", "cloud_spill_chunk_file_info_vec", "is_any_disk_on_cloud", "update_chunk_file_list_pin_secs_info")
    class DeleteChunksInfo(_message.Message):
        __slots__ = ("expected_chunk_file_version", "chunk_id_vec", "chunk_size_vec", "all_chunks_deleted", "chunk_file_physical_bytes", "migrate_live_chunks_on_cas_error")
        EXPECTED_CHUNK_FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        CHUNK_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
        ALL_CHUNKS_DELETED_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        MIGRATE_LIVE_CHUNKS_ON_CAS_ERROR_FIELD_NUMBER: _ClassVar[int]
        expected_chunk_file_version: int
        chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
        chunk_size_vec: _containers.RepeatedScalarFieldContainer[int]
        all_chunks_deleted: bool
        chunk_file_physical_bytes: int
        migrate_live_chunks_on_cas_error: bool
        def __init__(self, expected_chunk_file_version: _Optional[int] = ..., chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., chunk_size_vec: _Optional[_Iterable[int]] = ..., all_chunks_deleted: bool = ..., chunk_file_physical_bytes: _Optional[int] = ..., migrate_live_chunks_on_cas_error: bool = ...) -> None: ...
    class MigrateInfo(_message.Message):
        __slots__ = ("reason", "target_tier", "compression_level", "encryption_level", "may_increase_space", "force_encode", "encode_to_container", "data_stripe_disk_id_vec", "coded_stripe_disk_id_vec")
        REASON_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIER_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        MAY_INCREASE_SPACE_FIELD_NUMBER: _ClassVar[int]
        FORCE_ENCODE_FIELD_NUMBER: _ClassVar[int]
        ENCODE_TO_CONTAINER_FIELD_NUMBER: _ClassVar[int]
        DATA_STRIPE_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        CODED_STRIPE_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        reason: _blob_store_pb2.MorphParams.Reason
        target_tier: str
        compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
        encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
        may_increase_space: bool
        force_encode: bool
        encode_to_container: bool
        data_stripe_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
        coded_stripe_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, reason: _Optional[_Union[_blob_store_pb2.MorphParams.Reason, str]] = ..., target_tier: _Optional[str] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., may_increase_space: bool = ..., force_encode: bool = ..., encode_to_container: bool = ..., data_stripe_disk_id_vec: _Optional[_Iterable[int]] = ..., coded_stripe_disk_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class MigrateChunkFileInfo(_message.Message):
        __slots__ = ("chunk_count", "garbage_physical_bytes", "compress_file", "encode_file", "desired_num_data_stripes", "desired_num_coded_stripes", "chunk_physical_bytes", "has_brick_owned_chunks", "disk_id_vec", "container_ec_enabled_in_view_box", "replica_count")
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        GARBAGE_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        COMPRESS_FILE_FIELD_NUMBER: _ClassVar[int]
        ENCODE_FILE_FIELD_NUMBER: _ClassVar[int]
        DESIRED_NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
        DESIRED_NUM_CODED_STRIPES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        HAS_BRICK_OWNED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_EC_ENABLED_IN_VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
        REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        chunk_count: int
        garbage_physical_bytes: int
        compress_file: bool
        encode_file: bool
        desired_num_data_stripes: int
        desired_num_coded_stripes: int
        chunk_physical_bytes: int
        has_brick_owned_chunks: bool
        disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
        container_ec_enabled_in_view_box: bool
        replica_count: int
        def __init__(self, chunk_count: _Optional[int] = ..., garbage_physical_bytes: _Optional[int] = ..., compress_file: bool = ..., encode_file: bool = ..., desired_num_data_stripes: _Optional[int] = ..., desired_num_coded_stripes: _Optional[int] = ..., chunk_physical_bytes: _Optional[int] = ..., has_brick_owned_chunks: bool = ..., disk_id_vec: _Optional[_Iterable[int]] = ..., container_ec_enabled_in_view_box: bool = ..., replica_count: _Optional[int] = ...) -> None: ...
    class FixChunkFileInfo(_message.Message):
        __slots__ = ("fix_replication_action", "chunk_count", "fix_to_current_fault_tolerance", "expected_down_nodes", "is_optional", "salvage_chunk_file")
        FIX_REPLICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        FIX_TO_CURRENT_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_DOWN_NODES_FIELD_NUMBER: _ClassVar[int]
        IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
        SALVAGE_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
        fix_replication_action: bool
        chunk_count: int
        fix_to_current_fault_tolerance: bool
        expected_down_nodes: _containers.RepeatedScalarFieldContainer[int]
        is_optional: bool
        salvage_chunk_file: bool
        def __init__(self, fix_replication_action: bool = ..., chunk_count: _Optional[int] = ..., fix_to_current_fault_tolerance: bool = ..., expected_down_nodes: _Optional[_Iterable[int]] = ..., is_optional: bool = ..., salvage_chunk_file: bool = ...) -> None: ...
    class ShuffleChunkFileReplicas(_message.Message):
        __slots__ = ("target_disk_vec", "scribe_version", "chunk_count", "chunk_morphed_bytes")
        TARGET_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        CHUNK_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
        target_disk_vec: _containers.RepeatedScalarFieldContainer[int]
        scribe_version: int
        chunk_count: int
        chunk_morphed_bytes: int
        def __init__(self, target_disk_vec: _Optional[_Iterable[int]] = ..., scribe_version: _Optional[int] = ..., chunk_count: _Optional[int] = ..., chunk_morphed_bytes: _Optional[int] = ...) -> None: ...
    class CloudSpillChunkFileInfo(_message.Message):
        __slots__ = ("scribe_version", "current_compression_level", "current_encryption_level", "is_erasure_coded", "morphed_size", "target_vault_id", "previous_tier_name")
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        CURRENT_COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        CURRENT_ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        IS_ERASURE_CODED_FIELD_NUMBER: _ClassVar[int]
        MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        TARGET_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_TIER_NAME_FIELD_NUMBER: _ClassVar[int]
        scribe_version: int
        current_compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
        current_encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
        is_erasure_coded: bool
        morphed_size: int
        target_vault_id: int
        previous_tier_name: str
        def __init__(self, scribe_version: _Optional[int] = ..., current_compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., current_encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., is_erasure_coded: bool = ..., morphed_size: _Optional[int] = ..., target_vault_id: _Optional[int] = ..., previous_tier_name: _Optional[str] = ...) -> None: ...
    class UpdateChunkFileListPinSecsInfo(_message.Message):
        __slots__ = ("disk_id", "chunk_file_vec")
        class ChunkFileEntry(_message.Message):
            __slots__ = ("chunk_file_id", "max_pin_secs")
            CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
            MAX_PIN_SECS_FIELD_NUMBER: _ClassVar[int]
            chunk_file_id: int
            max_pin_secs: int
            def __init__(self, chunk_file_id: _Optional[int] = ..., max_pin_secs: _Optional[int] = ...) -> None: ...
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        chunk_file_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileActionProto.UpdateChunkFileListPinSecsInfo.ChunkFileEntry]
        def __init__(self, disk_id: _Optional[int] = ..., chunk_file_vec: _Optional[_Iterable[_Union[ChunkFileActionProto.UpdateChunkFileListPinSecsInfo.ChunkFileEntry, _Mapping]]] = ...) -> None: ...
    CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DELETE_CHUNKS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_INFO_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_CHUNK_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FIX_CHUNK_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_CHUNK_FILE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPILL_CHUNK_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_ANY_DISK_ON_CLOUD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CHUNK_FILE_LIST_PIN_SECS_INFO_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    owner_blob_id: int
    view_box_id: int
    delete_chunks_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileActionProto.DeleteChunksInfo]
    migrate_info: ChunkFileActionProto.MigrateInfo
    migrate_chunk_file_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileActionProto.MigrateChunkFileInfo]
    fix_chunk_file_info: ChunkFileActionProto.FixChunkFileInfo
    shuffle_chunk_file_replicas: ChunkFileActionProto.ShuffleChunkFileReplicas
    cloud_spill_chunk_file_info_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileActionProto.CloudSpillChunkFileInfo]
    is_any_disk_on_cloud: bool
    update_chunk_file_list_pin_secs_info: ChunkFileActionProto.UpdateChunkFileListPinSecsInfo
    def __init__(self, chunk_file_id_vec: _Optional[_Iterable[int]] = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., delete_chunks_info_vec: _Optional[_Iterable[_Union[ChunkFileActionProto.DeleteChunksInfo, _Mapping]]] = ..., migrate_info: _Optional[_Union[ChunkFileActionProto.MigrateInfo, _Mapping]] = ..., migrate_chunk_file_info_vec: _Optional[_Iterable[_Union[ChunkFileActionProto.MigrateChunkFileInfo, _Mapping]]] = ..., fix_chunk_file_info: _Optional[_Union[ChunkFileActionProto.FixChunkFileInfo, _Mapping]] = ..., shuffle_chunk_file_replicas: _Optional[_Union[ChunkFileActionProto.ShuffleChunkFileReplicas, _Mapping]] = ..., cloud_spill_chunk_file_info_vec: _Optional[_Iterable[_Union[ChunkFileActionProto.CloudSpillChunkFileInfo, _Mapping]]] = ..., is_any_disk_on_cloud: bool = ..., update_chunk_file_list_pin_secs_info: _Optional[_Union[ChunkFileActionProto.UpdateChunkFileListPinSecsInfo, _Mapping]] = ...) -> None: ...

class DedupNodeInfo(_message.Message):
    __slots__ = ("node_info", "parent_info_vec")
    class NodeInfo(_message.Message):
        __slots__ = ("tree_id", "node_id", "value_version")
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
        tree_id: int
        node_id: int
        value_version: _snap_tree_pb2.SnapTreeValueVersionProto
        def __init__(self, tree_id: _Optional[int] = ..., node_id: _Optional[int] = ..., value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    node_info: DedupNodeInfo.NodeInfo
    parent_info_vec: _containers.RepeatedCompositeFieldContainer[DedupNodeInfo.NodeInfo]
    def __init__(self, node_info: _Optional[_Union[DedupNodeInfo.NodeInfo, _Mapping]] = ..., parent_info_vec: _Optional[_Iterable[_Union[DedupNodeInfo.NodeInfo, _Mapping]]] = ...) -> None: ...

class SnapTreeDedupAction(_message.Message):
    __slots__ = ("canonical_node", "dedup_nodes")
    CANONICAL_NODE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_NODES_FIELD_NUMBER: _ClassVar[int]
    canonical_node: DedupNodeInfo
    dedup_nodes: _containers.RepeatedCompositeFieldContainer[DedupNodeInfo]
    def __init__(self, canonical_node: _Optional[_Union[DedupNodeInfo, _Mapping]] = ..., dedup_nodes: _Optional[_Iterable[_Union[DedupNodeInfo, _Mapping]]] = ...) -> None: ...

class ConvertToMegachunkAction(_message.Message):
    __slots__ = ("blob_position_vec", "dedup_chunk_vec")
    class BlobPositionInfo(_message.Message):
        __slots__ = ("blob_id", "blob_offset")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
        blob_id: int
        blob_offset: int
        def __init__(self, blob_id: _Optional[int] = ..., blob_offset: _Optional[int] = ...) -> None: ...
    class DedupChunkInfo(_message.Message):
        __slots__ = ("sha1", "length")
        SHA1_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        sha1: bytes
        length: int
        def __init__(self, sha1: _Optional[bytes] = ..., length: _Optional[int] = ...) -> None: ...
    BLOB_POSITION_VEC_FIELD_NUMBER: _ClassVar[int]
    DEDUP_CHUNK_VEC_FIELD_NUMBER: _ClassVar[int]
    blob_position_vec: _containers.RepeatedCompositeFieldContainer[ConvertToMegachunkAction.BlobPositionInfo]
    dedup_chunk_vec: _containers.RepeatedCompositeFieldContainer[ConvertToMegachunkAction.DedupChunkInfo]
    def __init__(self, blob_position_vec: _Optional[_Iterable[_Union[ConvertToMegachunkAction.BlobPositionInfo, _Mapping]]] = ..., dedup_chunk_vec: _Optional[_Iterable[_Union[ConvertToMegachunkAction.DedupChunkInfo, _Mapping]]] = ...) -> None: ...

class AdjustNodeRefcountResultProto(_message.Message):
    __slots__ = ("num_deleted", "error_map", "snap_tree_name", "num_refcount_incremented")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_REFCOUNT_INCREMENTED_FIELD_NUMBER: _ClassVar[int]
    num_deleted: int
    error_map: _containers.ScalarMap[int, int]
    snap_tree_name: _apollo_actions_base_pb2.SnapTreeName
    num_refcount_incremented: int
    def __init__(self, num_deleted: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ..., snap_tree_name: _Optional[_Union[_apollo_actions_base_pb2.SnapTreeName, str]] = ..., num_refcount_incremented: _Optional[int] = ...) -> None: ...

class ChunkFileActionResultProto(_message.Message):
    __slots__ = ("num_chunks_deleted", "chunk_deleted_bytes_morphed", "chunk_delete_error_map", "num_files_migrated", "reclaimed_bytes_physical", "encode_count_map", "num_files_compressed", "migrate_error_map", "num_files_deleted", "fix_chunk_file_error_type", "migrated_bytes_physical", "shuffle_chunk_file_replicas_error_type", "rebalanced_bytes_morphed", "cloud_spill_chunk_file_replicas_error_type", "num_chunk_files_cloud_spilled", "chunk_file_cloud_spilled_morphed_bytes", "update_chunk_file_list_pin_secs_error_type", "num_chunk_file_list_pin_secs_updated", "num_chunk_files_encoded_to_container", "num_containers_created", "encode_to_container_error_type", "num_garbage_chunks_migrated", "num_garbage_chunks_with_migrate_errors", "num_chunk_files_with_cas_error", "num_chunks_migrated_due_to_cas_error", "num_bytes_migrated_due_to_cas_error")
    class ChunkDeleteErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class EncodeCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class MigrateErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_CHUNKS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DELETED_BYTES_MORPHED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DELETE_ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    RECLAIMED_BYTES_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    ENCODE_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    FIX_CHUNK_FILE_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIGRATED_BYTES_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_CHUNK_FILE_REPLICAS_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    REBALANCED_BYTES_MORPHED_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPILL_CHUNK_FILE_REPLICAS_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_CLOUD_SPILLED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_CLOUD_SPILLED_MORPHED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CHUNK_FILE_LIST_PIN_SECS_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILE_LIST_PIN_SECS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_ENCODED_TO_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    NUM_CONTAINERS_CREATED_FIELD_NUMBER: _ClassVar[int]
    ENCODE_TO_CONTAINER_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_GARBAGE_CHUNKS_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    NUM_GARBAGE_CHUNKS_WITH_MIGRATE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_WITH_CAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNKS_MIGRATED_DUE_TO_CAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_MIGRATED_DUE_TO_CAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    num_chunks_deleted: int
    chunk_deleted_bytes_morphed: int
    chunk_delete_error_map: _containers.ScalarMap[int, int]
    num_files_migrated: int
    reclaimed_bytes_physical: int
    encode_count_map: _containers.ScalarMap[str, int]
    num_files_compressed: int
    migrate_error_map: _containers.ScalarMap[int, int]
    num_files_deleted: int
    fix_chunk_file_error_type: int
    migrated_bytes_physical: int
    shuffle_chunk_file_replicas_error_type: int
    rebalanced_bytes_morphed: int
    cloud_spill_chunk_file_replicas_error_type: int
    num_chunk_files_cloud_spilled: int
    chunk_file_cloud_spilled_morphed_bytes: int
    update_chunk_file_list_pin_secs_error_type: int
    num_chunk_file_list_pin_secs_updated: int
    num_chunk_files_encoded_to_container: int
    num_containers_created: int
    encode_to_container_error_type: int
    num_garbage_chunks_migrated: int
    num_garbage_chunks_with_migrate_errors: int
    num_chunk_files_with_cas_error: int
    num_chunks_migrated_due_to_cas_error: int
    num_bytes_migrated_due_to_cas_error: int
    def __init__(self, num_chunks_deleted: _Optional[int] = ..., chunk_deleted_bytes_morphed: _Optional[int] = ..., chunk_delete_error_map: _Optional[_Mapping[int, int]] = ..., num_files_migrated: _Optional[int] = ..., reclaimed_bytes_physical: _Optional[int] = ..., encode_count_map: _Optional[_Mapping[str, int]] = ..., num_files_compressed: _Optional[int] = ..., migrate_error_map: _Optional[_Mapping[int, int]] = ..., num_files_deleted: _Optional[int] = ..., fix_chunk_file_error_type: _Optional[int] = ..., migrated_bytes_physical: _Optional[int] = ..., shuffle_chunk_file_replicas_error_type: _Optional[int] = ..., rebalanced_bytes_morphed: _Optional[int] = ..., cloud_spill_chunk_file_replicas_error_type: _Optional[int] = ..., num_chunk_files_cloud_spilled: _Optional[int] = ..., chunk_file_cloud_spilled_morphed_bytes: _Optional[int] = ..., update_chunk_file_list_pin_secs_error_type: _Optional[int] = ..., num_chunk_file_list_pin_secs_updated: _Optional[int] = ..., num_chunk_files_encoded_to_container: _Optional[int] = ..., num_containers_created: _Optional[int] = ..., encode_to_container_error_type: _Optional[int] = ..., num_garbage_chunks_migrated: _Optional[int] = ..., num_garbage_chunks_with_migrate_errors: _Optional[int] = ..., num_chunk_files_with_cas_error: _Optional[int] = ..., num_chunks_migrated_due_to_cas_error: _Optional[int] = ..., num_bytes_migrated_due_to_cas_error: _Optional[int] = ...) -> None: ...

class FreeBlobByteRangeActionResultProto(_message.Message):
    __slots__ = ("free_blob_byte_range_error_type", "num_blob_bytes_freed")
    FREE_BLOB_BYTE_RANGE_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_BLOB_BYTES_FREED_FIELD_NUMBER: _ClassVar[int]
    free_blob_byte_range_error_type: int
    num_blob_bytes_freed: int
    def __init__(self, free_blob_byte_range_error_type: _Optional[int] = ..., num_blob_bytes_freed: _Optional[int] = ...) -> None: ...

class DeleteExpiredSmbSessionActionResultProto(_message.Message):
    __slots__ = ("error_count_map", "num_entities_executed")
    class ErrorCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTITIES_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    error_count_map: _containers.ScalarMap[int, int]
    num_entities_executed: int
    def __init__(self, error_count_map: _Optional[_Mapping[int, int]] = ..., num_entities_executed: _Optional[int] = ...) -> None: ...

class IceboxFixChunkLocation(_message.Message):
    __slots__ = ("chunk_id_vec",)
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_icebox_pb2.IceboxChunkIdProto]
    def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[_icebox_pb2.IceboxChunkIdProto, _Mapping]]] = ...) -> None: ...

class IceboxFixChunkLocationActionResultProto(_message.Message):
    __slots__ = ("error_count_map", "num_chunk_locations_fixed")
    class ErrorCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_LOCATIONS_FIXED_FIELD_NUMBER: _ClassVar[int]
    error_count_map: _containers.ScalarMap[int, int]
    num_chunk_locations_fixed: int
    def __init__(self, error_count_map: _Optional[_Mapping[int, int]] = ..., num_chunk_locations_fixed: _Optional[int] = ...) -> None: ...

class DeleteViewActionResultProto(_message.Message):
    __slots__ = ("delete_view_error_type",)
    DELETE_VIEW_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    delete_view_error_type: int
    def __init__(self, delete_view_error_type: _Optional[int] = ...) -> None: ...

class IceboxRetireArchive(_message.Message):
    __slots__ = ("archive_uid", "job_start_opclock_vec")
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_START_OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    job_start_opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_start_opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class IceboxRetireArchiveActionResultProto(_message.Message):
    __slots__ = ("retire_archive_error_type",)
    RETIRE_ARCHIVE_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    retire_archive_error_type: int
    def __init__(self, retire_archive_error_type: _Optional[int] = ...) -> None: ...

class IceboxDirectArchiveFilesGC(_message.Message):
    __slots__ = ("job_uid", "output_dir_names", "output_view_name", "inode_metadata_vec", "output_view_box_name", "fs_name")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DIR_NAMES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INODE_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    job_uid: _universal_id_pb2.UniversalIdProto
    output_dir_names: _containers.RepeatedScalarFieldContainer[str]
    output_view_name: str
    inode_metadata_vec: _containers.RepeatedCompositeFieldContainer[_snap_fs_metadata_pb2.InodeMetadataProto]
    output_view_box_name: str
    fs_name: str
    def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., output_dir_names: _Optional[_Iterable[str]] = ..., output_view_name: _Optional[str] = ..., inode_metadata_vec: _Optional[_Iterable[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]]] = ..., output_view_box_name: _Optional[str] = ..., fs_name: _Optional[str] = ...) -> None: ...

class IceboxDirectArchiveFilesGCActionResultProto(_message.Message):
    __slots__ = ("job_uid_completed_error_type", "num_files_gc_done", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    JOB_UID_COMPLETED_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_GC_DONE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    job_uid_completed_error_type: int
    num_files_gc_done: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, job_uid_completed_error_type: _Optional[int] = ..., num_files_gc_done: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class CloudObjectGCAction(_message.Message):
    __slots__ = ("delete_info_vec",)
    class CloudObjectInfo(_message.Message):
        __slots__ = ("cloud_object_id", "dead_object_local_id_vec", "live_cloud_chunk_id_vec", "scribe_version", "latest_expiration_time")
        CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        DEAD_OBJECT_LOCAL_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        LIVE_CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        LATEST_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
        cloud_object_id: _cloud_pb2.CloudObjectIdProto
        dead_object_local_id_vec: _containers.RepeatedScalarFieldContainer[int]
        live_cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
        scribe_version: int
        latest_expiration_time: int
        def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., dead_object_local_id_vec: _Optional[_Iterable[int]] = ..., live_cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., scribe_version: _Optional[int] = ..., latest_expiration_time: _Optional[int] = ...) -> None: ...
    DELETE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    delete_info_vec: _containers.RepeatedCompositeFieldContainer[CloudObjectGCAction.CloudObjectInfo]
    def __init__(self, delete_info_vec: _Optional[_Iterable[_Union[CloudObjectGCAction.CloudObjectInfo, _Mapping]]] = ...) -> None: ...

class CloudObjectGCActionResultProto(_message.Message):
    __slots__ = ("num_cloud_nodes_deleted", "num_cloud_chunks_deleted", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_CLOUD_NODES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_CLOUD_CHUNKS_DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_cloud_nodes_deleted: int
    num_cloud_chunks_deleted: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_cloud_nodes_deleted: _Optional[int] = ..., num_cloud_chunks_deleted: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FixCloudChunkFilesAction(_message.Message):
    __slots__ = ("cloud_chunk_file_id_vec",)
    CLOUD_CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    cloud_chunk_file_id_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.CloudObjectIdProto]
    def __init__(self, cloud_chunk_file_id_vec: _Optional[_Iterable[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]]] = ...) -> None: ...

class FixCloudChunkFilesActionResultProto(_message.Message):
    __slots__ = ("num_cloud_chunk_files_fixed", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_CLOUD_CHUNK_FILES_FIXED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_cloud_chunk_files_fixed: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_cloud_chunk_files_fixed: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class LCMCloudChunkFilesAction(_message.Message):
    __slots__ = ("lcm_info_vec",)
    class LCMInfo(_message.Message):
        __slots__ = ("cloud_chunk_file_id", "scribe_row_version", "target_tier_type")
        CLOUD_CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        cloud_chunk_file_id: _cloud_pb2.CloudObjectIdProto
        scribe_row_version: int
        target_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
        def __init__(self, cloud_chunk_file_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., scribe_row_version: _Optional[int] = ..., target_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ...) -> None: ...
    LCM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    lcm_info_vec: _containers.RepeatedCompositeFieldContainer[LCMCloudChunkFilesAction.LCMInfo]
    def __init__(self, lcm_info_vec: _Optional[_Iterable[_Union[LCMCloudChunkFilesAction.LCMInfo, _Mapping]]] = ...) -> None: ...

class LCMCloudChunkFilesActionResultProto(_message.Message):
    __slots__ = ("num_cloud_chunk_files_lcmed", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_CLOUD_CHUNK_FILES_LCMED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_cloud_chunk_files_lcmed: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_cloud_chunk_files_lcmed: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class IceboxDeleteStubViewsAction(_message.Message):
    __slots__ = ("delete_stub_view_info_vec",)
    class DeleteStubViewInfo(_message.Message):
        __slots__ = ("archive_uid", "entity_id", "stub_view_id", "scribe_version", "viewbox_id")
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        STUB_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        entity_id: int
        stub_view_id: int
        scribe_version: int
        viewbox_id: int
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., entity_id: _Optional[int] = ..., stub_view_id: _Optional[int] = ..., scribe_version: _Optional[int] = ..., viewbox_id: _Optional[int] = ...) -> None: ...
    DELETE_STUB_VIEW_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    delete_stub_view_info_vec: _containers.RepeatedCompositeFieldContainer[IceboxDeleteStubViewsAction.DeleteStubViewInfo]
    def __init__(self, delete_stub_view_info_vec: _Optional[_Iterable[_Union[IceboxDeleteStubViewsAction.DeleteStubViewInfo, _Mapping]]] = ...) -> None: ...

class IceboxDeleteStubViewsActionResultProto(_message.Message):
    __slots__ = ("num_stub_views_deleted", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_STUB_VIEWS_DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_stub_views_deleted: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_stub_views_deleted: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class IceboxCleanSnapTreeNodes(_message.Message):
    __slots__ = ("node_vec", "archive_id_vec")
    class SnapTreeNodeIdSetProto(_message.Message):
        __slots__ = ("tree_id", "snap_tree_name", "node_id_vec")
        TREE_ID_FIELD_NUMBER: _ClassVar[int]
        SNAP_TREE_NAME_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        tree_id: int
        snap_tree_name: _apollo_actions_base_pb2.SnapTreeName
        node_id_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, tree_id: _Optional[int] = ..., snap_tree_name: _Optional[_Union[_apollo_actions_base_pb2.SnapTreeName, str]] = ..., node_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    node_vec: _containers.RepeatedCompositeFieldContainer[IceboxCleanSnapTreeNodes.SnapTreeNodeIdSetProto]
    archive_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, node_vec: _Optional[_Iterable[_Union[IceboxCleanSnapTreeNodes.SnapTreeNodeIdSetProto, _Mapping]]] = ..., archive_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class IceboxCleanSnapTreeNodesResultProto(_message.Message):
    __slots__ = ("num_nodes_cleaned", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_NODES_CLEANED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_nodes_cleaned: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_nodes_cleaned: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class AsyncEntityDeleteResultProto(_message.Message):
    __slots__ = ("num_garbage_fragments_deleted", "num_files_deleted", "num_megafiles_deleted", "num_file_fragments_deleted", "num_directories_deleted", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_GARBAGE_FRAGMENTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_MEGAFILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_FILE_FRAGMENTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_garbage_fragments_deleted: int
    num_files_deleted: int
    num_megafiles_deleted: int
    num_file_fragments_deleted: int
    num_directories_deleted: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_garbage_fragments_deleted: _Optional[int] = ..., num_files_deleted: _Optional[int] = ..., num_megafiles_deleted: _Optional[int] = ..., num_file_fragments_deleted: _Optional[int] = ..., num_directories_deleted: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class SnapTreeDedupActionResultProto(_message.Message):
    __slots__ = ("snap_tree_dedup_action_error_type", "num_nodes_deduped")
    SNAP_TREE_DEDUP_ACTION_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_NODES_DEDUPED_FIELD_NUMBER: _ClassVar[int]
    snap_tree_dedup_action_error_type: int
    num_nodes_deduped: int
    def __init__(self, snap_tree_dedup_action_error_type: _Optional[int] = ..., num_nodes_deduped: _Optional[int] = ...) -> None: ...

class ConvertToMegachunkActionResultProto(_message.Message):
    __slots__ = ("convert_to_megachunk_action_error_type", "num_megachunk_occurrance_deduped", "num_chunks_in_megachunk")
    CONVERT_TO_MEGACHUNK_ACTION_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_MEGACHUNK_OCCURRANCE_DEDUPED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNKS_IN_MEGACHUNK_FIELD_NUMBER: _ClassVar[int]
    convert_to_megachunk_action_error_type: int
    num_megachunk_occurrance_deduped: int
    num_chunks_in_megachunk: int
    def __init__(self, convert_to_megachunk_action_error_type: _Optional[int] = ..., num_megachunk_occurrance_deduped: _Optional[int] = ..., num_chunks_in_megachunk: _Optional[int] = ...) -> None: ...

class FixUserQuotaUsageActionResultProto(_message.Message):
    __slots__ = ("num_user_entries_fixed", "num_user_entries_failed_to_fix")
    NUM_USER_ENTRIES_FIXED_FIELD_NUMBER: _ClassVar[int]
    NUM_USER_ENTRIES_FAILED_TO_FIX_FIELD_NUMBER: _ClassVar[int]
    num_user_entries_fixed: int
    num_user_entries_failed_to_fix: int
    def __init__(self, num_user_entries_fixed: _Optional[int] = ..., num_user_entries_failed_to_fix: _Optional[int] = ...) -> None: ...

class DeleteUserQuotaUsageActionResultProto(_message.Message):
    __slots__ = ("num_user_entries_deleted", "num_user_entries_failed_to_delete")
    NUM_USER_ENTRIES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_USER_ENTRIES_FAILED_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    num_user_entries_deleted: int
    num_user_entries_failed_to_delete: int
    def __init__(self, num_user_entries_deleted: _Optional[int] = ..., num_user_entries_failed_to_delete: _Optional[int] = ...) -> None: ...

class Nfs4CleanupActionResultProto(_message.Message):
    __slots__ = ("cleaned_objects_count", "error_count")
    CLEANED_OBJECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    cleaned_objects_count: int
    error_count: int
    def __init__(self, cleaned_objects_count: _Optional[int] = ..., error_count: _Optional[int] = ...) -> None: ...

class FixDirQuota(_message.Message):
    __slots__ = ("view_id", "dir_entry_vec", "dir_quota_snaptree_id")
    class FixDirQuotaEntry(_message.Message):
        __slots__ = ("dir_quota_id", "usage_in_bytes", "expected_version", "is_walk_pending", "is_tombstone")
        DIR_QUOTA_ID_FIELD_NUMBER: _ClassVar[int]
        USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_WALK_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_TOMBSTONE_FIELD_NUMBER: _ClassVar[int]
        dir_quota_id: int
        usage_in_bytes: int
        expected_version: _snap_tree_pb2.SnapTreeValueVersionProto
        is_walk_pending: bool
        is_tombstone: bool
        def __init__(self, dir_quota_id: _Optional[int] = ..., usage_in_bytes: _Optional[int] = ..., expected_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., is_walk_pending: bool = ..., is_tombstone: bool = ...) -> None: ...
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_SNAPTREE_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    dir_entry_vec: _containers.RepeatedCompositeFieldContainer[FixDirQuota.FixDirQuotaEntry]
    dir_quota_snaptree_id: int
    def __init__(self, view_id: _Optional[int] = ..., dir_entry_vec: _Optional[_Iterable[_Union[FixDirQuota.FixDirQuotaEntry, _Mapping]]] = ..., dir_quota_snaptree_id: _Optional[int] = ...) -> None: ...

class FixDirQuotaActionResultProto(_message.Message):
    __slots__ = ("num_dir_entries_fixed", "num_dir_entries_failed_to_fix")
    NUM_DIR_ENTRIES_FIXED_FIELD_NUMBER: _ClassVar[int]
    NUM_DIR_ENTRIES_FAILED_TO_FIX_FIELD_NUMBER: _ClassVar[int]
    num_dir_entries_fixed: int
    num_dir_entries_failed_to_fix: int
    def __init__(self, num_dir_entries_fixed: _Optional[int] = ..., num_dir_entries_failed_to_fix: _Optional[int] = ...) -> None: ...

class ShadowCopySetContextCleanup(_message.Message):
    __slots__ = ("context_entry_vec",)
    class ShadowCopySetContextCleanupEntry(_message.Message):
        __slots__ = ("client_ip",)
        CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
        client_ip: str
        def __init__(self, client_ip: _Optional[str] = ...) -> None: ...
    CONTEXT_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    context_entry_vec: _containers.RepeatedCompositeFieldContainer[ShadowCopySetContextCleanup.ShadowCopySetContextCleanupEntry]
    def __init__(self, context_entry_vec: _Optional[_Iterable[_Union[ShadowCopySetContextCleanup.ShadowCopySetContextCleanupEntry, _Mapping]]] = ...) -> None: ...

class ShadowCopySetContextCleanupActionResultProto(_message.Message):
    __slots__ = ("error_count_map", "num_contexts_cleaned")
    class ErrorCountMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_CONTEXTS_CLEANED_FIELD_NUMBER: _ClassVar[int]
    error_count_map: _containers.ScalarMap[int, int]
    num_contexts_cleaned: int
    def __init__(self, error_count_map: _Optional[_Mapping[int, int]] = ..., num_contexts_cleaned: _Optional[int] = ...) -> None: ...

class GarbageCollectOrphanEntity(_message.Message):
    __slots__ = ("eh", "owner_inode_id")
    EH_FIELD_NUMBER: _ClassVar[int]
    OWNER_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    owner_inode_id: int
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., owner_inode_id: _Optional[int] = ...) -> None: ...

class GarbageCollectOrphanEntityActionResultProto(_message.Message):
    __slots__ = ("error_type",)
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    error_type: int
    def __init__(self, error_type: _Optional[int] = ...) -> None: ...

class FixEntityHandleActionResultProto(_message.Message):
    __slots__ = ("fix_entity_error_type",)
    FIX_ENTITY_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    fix_entity_error_type: int
    def __init__(self, fix_entity_error_type: _Optional[int] = ...) -> None: ...

class NFSv4CleanupAction(_message.Message):
    __slots__ = ("client_id_vec",)
    CLIENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    client_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, client_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class AsyncEntityDeleteAction(_message.Message):
    __slots__ = ("eh", "value_version", "owner_inode_id")
    EH_FIELD_NUMBER: _ClassVar[int]
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    OWNER_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    owner_inode_id: int
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., owner_inode_id: _Optional[int] = ...) -> None: ...

class DedupBricksAction(_message.Message):
    __slots__ = ("blob_snap_tree_id", "brick_number", "num_bricks", "total_chunk_count")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NUM_BRICKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    brick_number: int
    num_bricks: int
    total_chunk_count: int
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., brick_number: _Optional[int] = ..., num_bricks: _Optional[int] = ..., total_chunk_count: _Optional[int] = ...) -> None: ...

class DedupBricksActionResultProto(_message.Message):
    __slots__ = ("num_bricks_deduped", "dedup_bricks_error_type")
    NUM_BRICKS_DEDUPED_FIELD_NUMBER: _ClassVar[int]
    DEDUP_BRICKS_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    num_bricks_deduped: int
    dedup_bricks_error_type: int
    def __init__(self, num_bricks_deduped: _Optional[int] = ..., dedup_bricks_error_type: _Optional[int] = ...) -> None: ...

class ChunkFileContainerAction(_message.Message):
    __slots__ = ("container_id", "owner_blob_id", "fix_container_info", "delete_container")
    class FixContainerInfo(_message.Message):
        __slots__ = ("fix_replication_action", "total_chunk_count", "expected_down_nodes")
        FIX_REPLICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_DOWN_NODES_FIELD_NUMBER: _ClassVar[int]
        fix_replication_action: bool
        total_chunk_count: int
        expected_down_nodes: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, fix_replication_action: bool = ..., total_chunk_count: _Optional[int] = ..., expected_down_nodes: _Optional[_Iterable[int]] = ...) -> None: ...
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    FIX_CONTAINER_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    container_id: int
    owner_blob_id: int
    fix_container_info: ChunkFileContainerAction.FixContainerInfo
    delete_container: bool
    def __init__(self, container_id: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., fix_container_info: _Optional[_Union[ChunkFileContainerAction.FixContainerInfo, _Mapping]] = ..., delete_container: bool = ...) -> None: ...

class ChunkFileContainerActionResultProto(_message.Message):
    __slots__ = ("num_containers_fixed", "fix_container_error_type", "num_containers_deleted", "delete_container_error_type")
    NUM_CONTAINERS_FIXED_FIELD_NUMBER: _ClassVar[int]
    FIX_CONTAINER_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_CONTAINERS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETE_CONTAINER_ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    num_containers_fixed: int
    fix_container_error_type: int
    num_containers_deleted: int
    delete_container_error_type: int
    def __init__(self, num_containers_fixed: _Optional[int] = ..., fix_container_error_type: _Optional[int] = ..., num_containers_deleted: _Optional[int] = ..., delete_container_error_type: _Optional[int] = ...) -> None: ...

class S3LifecycleExpirationSet(_message.Message):
    __slots__ = ("current_version_expiration", "noncurrent_version_expiration", "abort_incomplete_multipart_upload")
    CURRENT_VERSION_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    NONCURRENT_VERSION_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ABORT_INCOMPLETE_MULTIPART_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    current_version_expiration: bool
    noncurrent_version_expiration: bool
    abort_incomplete_multipart_upload: bool
    def __init__(self, current_version_expiration: bool = ..., noncurrent_version_expiration: bool = ..., abort_incomplete_multipart_upload: bool = ...) -> None: ...

class S3LifecycleExpiration(_message.Message):
    __slots__ = ("config_version_id", "object_name", "expiration_set")
    CONFIG_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_SET_FIELD_NUMBER: _ClassVar[int]
    config_version_id: int
    object_name: str
    expiration_set: S3LifecycleExpirationSet
    def __init__(self, config_version_id: _Optional[int] = ..., object_name: _Optional[str] = ..., expiration_set: _Optional[_Union[S3LifecycleExpirationSet, _Mapping]] = ...) -> None: ...

class S3CompositeActionProto(_message.Message):
    __slots__ = ("entity_handle", "fix_s3_intent", "fix_creation_ts_vec", "s3_lifecycle_expiration", "s3_empty_dir_deletion")
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FIX_S3_INTENT_FIELD_NUMBER: _ClassVar[int]
    FIX_CREATION_TS_VEC_FIELD_NUMBER: _ClassVar[int]
    S3_LIFECYCLE_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    S3_EMPTY_DIR_DELETION_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _actions_common_pb2.FixEntityHandle
    fix_s3_intent: bool
    fix_creation_ts_vec: bool
    s3_lifecycle_expiration: S3LifecycleExpiration
    s3_empty_dir_deletion: bool
    def __init__(self, entity_handle: _Optional[_Union[_actions_common_pb2.FixEntityHandle, _Mapping]] = ..., fix_s3_intent: bool = ..., fix_creation_ts_vec: bool = ..., s3_lifecycle_expiration: _Optional[_Union[S3LifecycleExpiration, _Mapping]] = ..., s3_empty_dir_deletion: bool = ...) -> None: ...

class CloudChunkFileValidateActionProto(_message.Message):
    __slots__ = ("validate_info_vec",)
    class ValidateInfo(_message.Message):
        __slots__ = ("cloud_object_id", "scribe_version", "live_cloud_chunk_id_vec", "validate_cloud_chunk_checksum")
        CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        LIVE_CLOUD_CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        VALIDATE_CLOUD_CHUNK_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        cloud_object_id: _cloud_pb2.CloudObjectIdProto
        scribe_version: int
        live_cloud_chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkIdProto]
        validate_cloud_chunk_checksum: bool
        def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., scribe_version: _Optional[int] = ..., live_cloud_chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]]] = ..., validate_cloud_chunk_checksum: bool = ...) -> None: ...
    VALIDATE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    validate_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileValidateActionProto.ValidateInfo]
    def __init__(self, validate_info_vec: _Optional[_Iterable[_Union[CloudChunkFileValidateActionProto.ValidateInfo, _Mapping]]] = ...) -> None: ...

class FilerLifecycleActionProto(_message.Message):
    __slots__ = ("entity_id", "view_id", "root_inode_id", "inode_type", "parent_inode_id", "entity_names")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    view_id: int
    root_inode_id: int
    inode_type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
    parent_inode_id: int
    entity_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entity_id: _Optional[int] = ..., view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., inode_type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ..., parent_inode_id: _Optional[int] = ..., entity_names: _Optional[_Iterable[str]] = ...) -> None: ...

class S3IntentFixingResult(_message.Message):
    __slots__ = ("error_map",)
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FixingCreationTimestampVecResult(_message.Message):
    __slots__ = ("error_map",)
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class LifecycleExecutationResult(_message.Message):
    __slots__ = ("error_map", "num_s3_entities_deleted", "logical_bytes_deleted", "num_object_versions_deleted", "logical_bytes_object_versions_deleted", "num_incomplete_multipart_uploads_aborted", "logical_bytes_incomplete_multipart_uploads_aborted")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_S3_ENTITIES_DELETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_OBJECT_VERSIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_OBJECT_VERSIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_INCOMPLETE_MULTIPART_UPLOADS_ABORTED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_BYTES_INCOMPLETE_MULTIPART_UPLOADS_ABORTED_FIELD_NUMBER: _ClassVar[int]
    error_map: _containers.ScalarMap[int, int]
    num_s3_entities_deleted: int
    logical_bytes_deleted: int
    num_object_versions_deleted: int
    logical_bytes_object_versions_deleted: int
    num_incomplete_multipart_uploads_aborted: int
    logical_bytes_incomplete_multipart_uploads_aborted: int
    def __init__(self, error_map: _Optional[_Mapping[int, int]] = ..., num_s3_entities_deleted: _Optional[int] = ..., logical_bytes_deleted: _Optional[int] = ..., num_object_versions_deleted: _Optional[int] = ..., logical_bytes_object_versions_deleted: _Optional[int] = ..., num_incomplete_multipart_uploads_aborted: _Optional[int] = ..., logical_bytes_incomplete_multipart_uploads_aborted: _Optional[int] = ...) -> None: ...

class S3CompositeActionResultProto(_message.Message):
    __slots__ = ("s3_intent_fixing_result", "fix_creation_ts_vec_result", "lifecycle_result")
    S3_INTENT_FIXING_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIX_CREATION_TS_VEC_RESULT_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_RESULT_FIELD_NUMBER: _ClassVar[int]
    s3_intent_fixing_result: S3IntentFixingResult
    fix_creation_ts_vec_result: FixingCreationTimestampVecResult
    lifecycle_result: LifecycleExecutationResult
    def __init__(self, s3_intent_fixing_result: _Optional[_Union[S3IntentFixingResult, _Mapping]] = ..., fix_creation_ts_vec_result: _Optional[_Union[FixingCreationTimestampVecResult, _Mapping]] = ..., lifecycle_result: _Optional[_Union[LifecycleExecutationResult, _Mapping]] = ...) -> None: ...

class CloudChunkFileValidationActionResultProto(_message.Message):
    __slots__ = ("error_map", "num_cloud_chunks_validated", "num_missing_cloud_chunks", "num_corrupt_cloud_chunks")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    NUM_CLOUD_CHUNKS_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    NUM_MISSING_CLOUD_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    NUM_CORRUPT_CLOUD_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    error_map: _containers.ScalarMap[int, int]
    num_cloud_chunks_validated: int
    num_missing_cloud_chunks: int
    num_corrupt_cloud_chunks: int
    def __init__(self, error_map: _Optional[_Mapping[int, int]] = ..., num_cloud_chunks_validated: _Optional[int] = ..., num_missing_cloud_chunks: _Optional[int] = ..., num_corrupt_cloud_chunks: _Optional[int] = ...) -> None: ...

class ArchiveMetadataGCAction(_message.Message):
    __slots__ = ("archive_metadata_info_vec",)
    class ArchiveMetadataInfo(_message.Message):
        __slots__ = ("archive_uid", "scribe_version")
        ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
        archive_uid: _universal_id_pb2.UniversalIdProto
        scribe_version: int
        def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., scribe_version: _Optional[int] = ...) -> None: ...
    ARCHIVE_METADATA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_metadata_info_vec: _containers.RepeatedCompositeFieldContainer[ArchiveMetadataGCAction.ArchiveMetadataInfo]
    def __init__(self, archive_metadata_info_vec: _Optional[_Iterable[_Union[ArchiveMetadataGCAction.ArchiveMetadataInfo, _Mapping]]] = ...) -> None: ...

class ArchiveMetadataGCActionResultProto(_message.Message):
    __slots__ = ("num_archive_metadata_deleted", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_ARCHIVE_METADATA_DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_archive_metadata_deleted: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_archive_metadata_deleted: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DowntierUptieredCloudChunkFilesAction(_message.Message):
    __slots__ = ("downtier_ccfm_info_vec",)
    class DowntierCCFMInfo(_message.Message):
        __slots__ = ("cloud_chunk_file_id", "scribe_row_version", "target_tier_type")
        CLOUD_CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        cloud_chunk_file_id: _cloud_pb2.CloudObjectIdProto
        scribe_row_version: int
        target_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
        def __init__(self, cloud_chunk_file_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., scribe_row_version: _Optional[int] = ..., target_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ...) -> None: ...
    DOWNTIER_CCFM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    downtier_ccfm_info_vec: _containers.RepeatedCompositeFieldContainer[DowntierUptieredCloudChunkFilesAction.DowntierCCFMInfo]
    def __init__(self, downtier_ccfm_info_vec: _Optional[_Iterable[_Union[DowntierUptieredCloudChunkFilesAction.DowntierCCFMInfo, _Mapping]]] = ...) -> None: ...

class DowntierUptieredCloudChunkFilesActionResultProto(_message.Message):
    __slots__ = ("num_uptiered_ccf_downtiered", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_UPTIERED_CCF_DOWNTIERED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_uptiered_ccf_downtiered: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_uptiered_ccf_downtiered: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FilerLifecycleActionResultProto(_message.Message):
    __slots__ = ("num_files_deleted", "num_of_bytes_removed", "num_directories_removed", "error_map")
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NUM_FILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_BYTES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    NUM_DIRECTORIES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    num_files_deleted: int
    num_of_bytes_removed: int
    num_directories_removed: int
    error_map: _containers.ScalarMap[int, int]
    def __init__(self, num_files_deleted: _Optional[int] = ..., num_of_bytes_removed: _Optional[int] = ..., num_directories_removed: _Optional[int] = ..., error_map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class ActionProto(_message.Message):
    __slots__ = ("type", "adjust_node_refcount_vec", "chunk_file_action", "free_blob_byte_range_action", "snap_tree_dedup_action", "fix_user_quota_usage_action", "delete_user_quota_usage_action", "delete_expired_smb_session_action", "delete_view_action", "fix_view_metadata_action", "fix_entity_handle_action", "icebox_fix_chunk_location_action", "icebox_retire_archive_action", "fix_dir_quota_action", "garbage_collect_orphan_entity_action", "shadow_copy_set_context_cleanup_action", "icebox_direct_archive_files_gc_action", "nfs4_cleanup_action", "icebox_clean_snap_tree_nodes_action", "async_entity_delete_action", "dedup_bricks_action", "qos_component", "convert_to_megachunk_action", "cloud_object_gc_action", "fix_cloud_chunk_files_action", "icebox_delete_stub_views_action", "orion_lcm_cloud_chunk_files_action", "chunk_file_container_action", "s3_composite_action", "cloud_chunk_file_validation_action", "archive_metadata_gc_action", "downtier_uptiered_cloud_chunk_files_action", "filer_lifecycle_action")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnaptreeRefcount: _ClassVar[ActionProto.Type]
        kChunkFileAction: _ClassVar[ActionProto.Type]
        kFreeBlobByteRangeAction: _ClassVar[ActionProto.Type]
        kSnapTreeDedupAction: _ClassVar[ActionProto.Type]
        kFixUserQuotaUsageAction: _ClassVar[ActionProto.Type]
        kDeleteUserQuotaUsageAction: _ClassVar[ActionProto.Type]
        kDeleteExpiredSmbSessionAction: _ClassVar[ActionProto.Type]
        kDeleteViewAction: _ClassVar[ActionProto.Type]
        kFixViewMetadataAction: _ClassVar[ActionProto.Type]
        kFixEntityHandleAction: _ClassVar[ActionProto.Type]
        kIceboxFixChunkLocationAction: _ClassVar[ActionProto.Type]
        kIceboxRetireArchiveAction: _ClassVar[ActionProto.Type]
        kFixDirQuotaAction: _ClassVar[ActionProto.Type]
        kGarbageCollectOrphanEntityAction: _ClassVar[ActionProto.Type]
        kShadowCopySetContextCleanupAction: _ClassVar[ActionProto.Type]
        kIceboxDirectArchiveFilesGCAction: _ClassVar[ActionProto.Type]
        kNFSv4CleanupAction: _ClassVar[ActionProto.Type]
        kIceboxCleanSnapTreeNodesAction: _ClassVar[ActionProto.Type]
        kAsyncEntityDeleteAction: _ClassVar[ActionProto.Type]
        kDedupBricksAction: _ClassVar[ActionProto.Type]
        kConvertToMegachunkAction: _ClassVar[ActionProto.Type]
        kDeleteCloudChunksAction: _ClassVar[ActionProto.Type]
        kDeleteCloudNodesAction: _ClassVar[ActionProto.Type]
        kFixCloudChunkFilesAction: _ClassVar[ActionProto.Type]
        kIceboxDeleteStubViewsAction: _ClassVar[ActionProto.Type]
        kLCMCloudChunkFilesAction: _ClassVar[ActionProto.Type]
        kChunkFileContainerAction: _ClassVar[ActionProto.Type]
        kS3CompositeAction: _ClassVar[ActionProto.Type]
        kCloudChunkFileValidationAction: _ClassVar[ActionProto.Type]
        kArchiveMetadataGCAction: _ClassVar[ActionProto.Type]
        kDowntierUptieredCloudChunkFilesAction: _ClassVar[ActionProto.Type]
        kFilerLifecycleAction: _ClassVar[ActionProto.Type]
    kSnaptreeRefcount: ActionProto.Type
    kChunkFileAction: ActionProto.Type
    kFreeBlobByteRangeAction: ActionProto.Type
    kSnapTreeDedupAction: ActionProto.Type
    kFixUserQuotaUsageAction: ActionProto.Type
    kDeleteUserQuotaUsageAction: ActionProto.Type
    kDeleteExpiredSmbSessionAction: ActionProto.Type
    kDeleteViewAction: ActionProto.Type
    kFixViewMetadataAction: ActionProto.Type
    kFixEntityHandleAction: ActionProto.Type
    kIceboxFixChunkLocationAction: ActionProto.Type
    kIceboxRetireArchiveAction: ActionProto.Type
    kFixDirQuotaAction: ActionProto.Type
    kGarbageCollectOrphanEntityAction: ActionProto.Type
    kShadowCopySetContextCleanupAction: ActionProto.Type
    kIceboxDirectArchiveFilesGCAction: ActionProto.Type
    kNFSv4CleanupAction: ActionProto.Type
    kIceboxCleanSnapTreeNodesAction: ActionProto.Type
    kAsyncEntityDeleteAction: ActionProto.Type
    kDedupBricksAction: ActionProto.Type
    kConvertToMegachunkAction: ActionProto.Type
    kDeleteCloudChunksAction: ActionProto.Type
    kDeleteCloudNodesAction: ActionProto.Type
    kFixCloudChunkFilesAction: ActionProto.Type
    kIceboxDeleteStubViewsAction: ActionProto.Type
    kLCMCloudChunkFilesAction: ActionProto.Type
    kChunkFileContainerAction: ActionProto.Type
    kS3CompositeAction: ActionProto.Type
    kCloudChunkFileValidationAction: ActionProto.Type
    kArchiveMetadataGCAction: ActionProto.Type
    kDowntierUptieredCloudChunkFilesAction: ActionProto.Type
    kFilerLifecycleAction: ActionProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADJUST_NODE_REFCOUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ACTION_FIELD_NUMBER: _ClassVar[int]
    FREE_BLOB_BYTE_RANGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_DEDUP_ACTION_FIELD_NUMBER: _ClassVar[int]
    FIX_USER_QUOTA_USAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_USER_QUOTA_USAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_EXPIRED_SMB_SESSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_ACTION_FIELD_NUMBER: _ClassVar[int]
    FIX_VIEW_METADATA_ACTION_FIELD_NUMBER: _ClassVar[int]
    FIX_ENTITY_HANDLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_FIX_CHUNK_LOCATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_RETIRE_ARCHIVE_ACTION_FIELD_NUMBER: _ClassVar[int]
    FIX_DIR_QUOTA_ACTION_FIELD_NUMBER: _ClassVar[int]
    GARBAGE_COLLECT_ORPHAN_ENTITY_ACTION_FIELD_NUMBER: _ClassVar[int]
    SHADOW_COPY_SET_CONTEXT_CLEANUP_ACTION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_DIRECT_ARCHIVE_FILES_GC_ACTION_FIELD_NUMBER: _ClassVar[int]
    NFS4_CLEANUP_ACTION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_CLEAN_SNAP_TREE_NODES_ACTION_FIELD_NUMBER: _ClassVar[int]
    ASYNC_ENTITY_DELETE_ACTION_FIELD_NUMBER: _ClassVar[int]
    DEDUP_BRICKS_ACTION_FIELD_NUMBER: _ClassVar[int]
    QOS_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TO_MEGACHUNK_ACTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_GC_ACTION_FIELD_NUMBER: _ClassVar[int]
    FIX_CLOUD_CHUNK_FILES_ACTION_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_DELETE_STUB_VIEWS_ACTION_FIELD_NUMBER: _ClassVar[int]
    ORION_LCM_CLOUD_CHUNK_FILES_ACTION_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_CONTAINER_ACTION_FIELD_NUMBER: _ClassVar[int]
    S3_COMPOSITE_ACTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_VALIDATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_GC_ACTION_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_UPTIERED_CLOUD_CHUNK_FILES_ACTION_FIELD_NUMBER: _ClassVar[int]
    FILER_LIFECYCLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    type: ActionProto.Type
    adjust_node_refcount_vec: _containers.RepeatedCompositeFieldContainer[_actions_common_pb2.AdjustNodeRefcountProto]
    chunk_file_action: ChunkFileActionProto
    free_blob_byte_range_action: _actions_common_pb2.FreeBlobByteRange
    snap_tree_dedup_action: SnapTreeDedupAction
    fix_user_quota_usage_action: _actions_common_pb2.FixUserQuotaUsage
    delete_user_quota_usage_action: _actions_common_pb2.DeleteUserQuotaUsage
    delete_expired_smb_session_action: _actions_common_pb2.DeleteExpiredSmbSession
    delete_view_action: _actions_common_pb2.DeleteView
    fix_view_metadata_action: _actions_common_pb2.FixView
    fix_entity_handle_action: _actions_common_pb2.FixEntityHandle
    icebox_fix_chunk_location_action: IceboxFixChunkLocation
    icebox_retire_archive_action: IceboxRetireArchive
    fix_dir_quota_action: FixDirQuota
    garbage_collect_orphan_entity_action: GarbageCollectOrphanEntity
    shadow_copy_set_context_cleanup_action: ShadowCopySetContextCleanup
    icebox_direct_archive_files_gc_action: IceboxDirectArchiveFilesGC
    nfs4_cleanup_action: NFSv4CleanupAction
    icebox_clean_snap_tree_nodes_action: IceboxCleanSnapTreeNodes
    async_entity_delete_action: AsyncEntityDeleteAction
    dedup_bricks_action: DedupBricksAction
    qos_component: _cluster_config_pb2.ClusterConfigProto.Component.QoSComponent
    convert_to_megachunk_action: ConvertToMegachunkAction
    cloud_object_gc_action: CloudObjectGCAction
    fix_cloud_chunk_files_action: FixCloudChunkFilesAction
    icebox_delete_stub_views_action: IceboxDeleteStubViewsAction
    orion_lcm_cloud_chunk_files_action: LCMCloudChunkFilesAction
    chunk_file_container_action: ChunkFileContainerAction
    s3_composite_action: S3CompositeActionProto
    cloud_chunk_file_validation_action: CloudChunkFileValidateActionProto
    archive_metadata_gc_action: ArchiveMetadataGCAction
    downtier_uptiered_cloud_chunk_files_action: DowntierUptieredCloudChunkFilesAction
    filer_lifecycle_action: FilerLifecycleActionProto
    def __init__(self, type: _Optional[_Union[ActionProto.Type, str]] = ..., adjust_node_refcount_vec: _Optional[_Iterable[_Union[_actions_common_pb2.AdjustNodeRefcountProto, _Mapping]]] = ..., chunk_file_action: _Optional[_Union[ChunkFileActionProto, _Mapping]] = ..., free_blob_byte_range_action: _Optional[_Union[_actions_common_pb2.FreeBlobByteRange, _Mapping]] = ..., snap_tree_dedup_action: _Optional[_Union[SnapTreeDedupAction, _Mapping]] = ..., fix_user_quota_usage_action: _Optional[_Union[_actions_common_pb2.FixUserQuotaUsage, _Mapping]] = ..., delete_user_quota_usage_action: _Optional[_Union[_actions_common_pb2.DeleteUserQuotaUsage, _Mapping]] = ..., delete_expired_smb_session_action: _Optional[_Union[_actions_common_pb2.DeleteExpiredSmbSession, _Mapping]] = ..., delete_view_action: _Optional[_Union[_actions_common_pb2.DeleteView, _Mapping]] = ..., fix_view_metadata_action: _Optional[_Union[_actions_common_pb2.FixView, _Mapping]] = ..., fix_entity_handle_action: _Optional[_Union[_actions_common_pb2.FixEntityHandle, _Mapping]] = ..., icebox_fix_chunk_location_action: _Optional[_Union[IceboxFixChunkLocation, _Mapping]] = ..., icebox_retire_archive_action: _Optional[_Union[IceboxRetireArchive, _Mapping]] = ..., fix_dir_quota_action: _Optional[_Union[FixDirQuota, _Mapping]] = ..., garbage_collect_orphan_entity_action: _Optional[_Union[GarbageCollectOrphanEntity, _Mapping]] = ..., shadow_copy_set_context_cleanup_action: _Optional[_Union[ShadowCopySetContextCleanup, _Mapping]] = ..., icebox_direct_archive_files_gc_action: _Optional[_Union[IceboxDirectArchiveFilesGC, _Mapping]] = ..., nfs4_cleanup_action: _Optional[_Union[NFSv4CleanupAction, _Mapping]] = ..., icebox_clean_snap_tree_nodes_action: _Optional[_Union[IceboxCleanSnapTreeNodes, _Mapping]] = ..., async_entity_delete_action: _Optional[_Union[AsyncEntityDeleteAction, _Mapping]] = ..., dedup_bricks_action: _Optional[_Union[DedupBricksAction, _Mapping]] = ..., qos_component: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Component.QoSComponent, str]] = ..., convert_to_megachunk_action: _Optional[_Union[ConvertToMegachunkAction, _Mapping]] = ..., cloud_object_gc_action: _Optional[_Union[CloudObjectGCAction, _Mapping]] = ..., fix_cloud_chunk_files_action: _Optional[_Union[FixCloudChunkFilesAction, _Mapping]] = ..., icebox_delete_stub_views_action: _Optional[_Union[IceboxDeleteStubViewsAction, _Mapping]] = ..., orion_lcm_cloud_chunk_files_action: _Optional[_Union[LCMCloudChunkFilesAction, _Mapping]] = ..., chunk_file_container_action: _Optional[_Union[ChunkFileContainerAction, _Mapping]] = ..., s3_composite_action: _Optional[_Union[S3CompositeActionProto, _Mapping]] = ..., cloud_chunk_file_validation_action: _Optional[_Union[CloudChunkFileValidateActionProto, _Mapping]] = ..., archive_metadata_gc_action: _Optional[_Union[ArchiveMetadataGCAction, _Mapping]] = ..., downtier_uptiered_cloud_chunk_files_action: _Optional[_Union[DowntierUptieredCloudChunkFilesAction, _Mapping]] = ..., filer_lifecycle_action: _Optional[_Union[FilerLifecycleActionProto, _Mapping]] = ...) -> None: ...

class ActionResultProto(_message.Message):
    __slots__ = ("action_completed", "blob_owner_session_id", "adjust_node_refcount_result", "chunk_file_action_result", "free_blob_byte_range_action_result", "snap_tree_dedup_action_result", "fix_user_quota_usage_action_result", "delete_user_quota_usage_action_result", "delete_expired_smb_session_action_result", "delete_view_action_result", "fix_entity_handle_action_result", "icebox_fix_chunk_location_action_result", "icebox_retire_archive_action_result", "fix_dir_quota_action_result", "garbage_collect_orphan_entity_action_result", "shadow_copy_set_context_cleanup_action_result", "icebox_direct_archive_files_gc_action_result", "nfs4_cleanup_action_result", "icebox_clean_snap_tree_nodes_action_result", "async_entity_delete_action_result", "dedup_bricks_action_result", "convert_to_megachunk_action_result", "cloud_object_gc_action_result", "fix_cloud_chunk_files_action_result", "icebox_delete_stub_views_action_result", "orion_lcm_cloud_chunk_files_action_result", "chunk_file_container_action_result", "s3_composite_action_result", "cloud_chunk_file_validation_action_result", "archive_metadata_gc_action_result", "downtier_uptiered_cloud_chunk_files_action_result", "filer_lifecycle_action_result")
    ACTION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    BLOB_OWNER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ADJUST_NODE_REFCOUNT_RESULT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FREE_BLOB_BYTE_RANGE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_DEDUP_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIX_USER_QUOTA_USAGE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_USER_QUOTA_USAGE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_EXPIRED_SMB_SESSION_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIX_ENTITY_HANDLE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_FIX_CHUNK_LOCATION_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_RETIRE_ARCHIVE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIX_DIR_QUOTA_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    GARBAGE_COLLECT_ORPHAN_ENTITY_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    SHADOW_COPY_SET_CONTEXT_CLEANUP_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_DIRECT_ARCHIVE_FILES_GC_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    NFS4_CLEANUP_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_CLEAN_SNAP_TREE_NODES_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ASYNC_ENTITY_DELETE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DEDUP_BRICKS_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TO_MEGACHUNK_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_GC_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIX_CLOUD_CHUNK_FILES_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_DELETE_STUB_VIEWS_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ORION_LCM_CLOUD_CHUNK_FILES_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_CONTAINER_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    S3_COMPOSITE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_VALIDATION_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_METADATA_GC_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_UPTIERED_CLOUD_CHUNK_FILES_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FILER_LIFECYCLE_ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_completed: bool
    blob_owner_session_id: int
    adjust_node_refcount_result: AdjustNodeRefcountResultProto
    chunk_file_action_result: ChunkFileActionResultProto
    free_blob_byte_range_action_result: FreeBlobByteRangeActionResultProto
    snap_tree_dedup_action_result: SnapTreeDedupActionResultProto
    fix_user_quota_usage_action_result: FixUserQuotaUsageActionResultProto
    delete_user_quota_usage_action_result: DeleteUserQuotaUsageActionResultProto
    delete_expired_smb_session_action_result: DeleteExpiredSmbSessionActionResultProto
    delete_view_action_result: DeleteViewActionResultProto
    fix_entity_handle_action_result: FixEntityHandleActionResultProto
    icebox_fix_chunk_location_action_result: IceboxFixChunkLocationActionResultProto
    icebox_retire_archive_action_result: IceboxRetireArchiveActionResultProto
    fix_dir_quota_action_result: FixDirQuotaActionResultProto
    garbage_collect_orphan_entity_action_result: GarbageCollectOrphanEntityActionResultProto
    shadow_copy_set_context_cleanup_action_result: ShadowCopySetContextCleanupActionResultProto
    icebox_direct_archive_files_gc_action_result: IceboxDirectArchiveFilesGCActionResultProto
    nfs4_cleanup_action_result: Nfs4CleanupActionResultProto
    icebox_clean_snap_tree_nodes_action_result: IceboxCleanSnapTreeNodesResultProto
    async_entity_delete_action_result: AsyncEntityDeleteResultProto
    dedup_bricks_action_result: DedupBricksActionResultProto
    convert_to_megachunk_action_result: ConvertToMegachunkActionResultProto
    cloud_object_gc_action_result: CloudObjectGCActionResultProto
    fix_cloud_chunk_files_action_result: FixCloudChunkFilesActionResultProto
    icebox_delete_stub_views_action_result: IceboxDeleteStubViewsActionResultProto
    orion_lcm_cloud_chunk_files_action_result: LCMCloudChunkFilesActionResultProto
    chunk_file_container_action_result: ChunkFileContainerActionResultProto
    s3_composite_action_result: S3CompositeActionResultProto
    cloud_chunk_file_validation_action_result: CloudChunkFileValidationActionResultProto
    archive_metadata_gc_action_result: ArchiveMetadataGCActionResultProto
    downtier_uptiered_cloud_chunk_files_action_result: DowntierUptieredCloudChunkFilesActionResultProto
    filer_lifecycle_action_result: FilerLifecycleActionResultProto
    def __init__(self, action_completed: bool = ..., blob_owner_session_id: _Optional[int] = ..., adjust_node_refcount_result: _Optional[_Union[AdjustNodeRefcountResultProto, _Mapping]] = ..., chunk_file_action_result: _Optional[_Union[ChunkFileActionResultProto, _Mapping]] = ..., free_blob_byte_range_action_result: _Optional[_Union[FreeBlobByteRangeActionResultProto, _Mapping]] = ..., snap_tree_dedup_action_result: _Optional[_Union[SnapTreeDedupActionResultProto, _Mapping]] = ..., fix_user_quota_usage_action_result: _Optional[_Union[FixUserQuotaUsageActionResultProto, _Mapping]] = ..., delete_user_quota_usage_action_result: _Optional[_Union[DeleteUserQuotaUsageActionResultProto, _Mapping]] = ..., delete_expired_smb_session_action_result: _Optional[_Union[DeleteExpiredSmbSessionActionResultProto, _Mapping]] = ..., delete_view_action_result: _Optional[_Union[DeleteViewActionResultProto, _Mapping]] = ..., fix_entity_handle_action_result: _Optional[_Union[FixEntityHandleActionResultProto, _Mapping]] = ..., icebox_fix_chunk_location_action_result: _Optional[_Union[IceboxFixChunkLocationActionResultProto, _Mapping]] = ..., icebox_retire_archive_action_result: _Optional[_Union[IceboxRetireArchiveActionResultProto, _Mapping]] = ..., fix_dir_quota_action_result: _Optional[_Union[FixDirQuotaActionResultProto, _Mapping]] = ..., garbage_collect_orphan_entity_action_result: _Optional[_Union[GarbageCollectOrphanEntityActionResultProto, _Mapping]] = ..., shadow_copy_set_context_cleanup_action_result: _Optional[_Union[ShadowCopySetContextCleanupActionResultProto, _Mapping]] = ..., icebox_direct_archive_files_gc_action_result: _Optional[_Union[IceboxDirectArchiveFilesGCActionResultProto, _Mapping]] = ..., nfs4_cleanup_action_result: _Optional[_Union[Nfs4CleanupActionResultProto, _Mapping]] = ..., icebox_clean_snap_tree_nodes_action_result: _Optional[_Union[IceboxCleanSnapTreeNodesResultProto, _Mapping]] = ..., async_entity_delete_action_result: _Optional[_Union[AsyncEntityDeleteResultProto, _Mapping]] = ..., dedup_bricks_action_result: _Optional[_Union[DedupBricksActionResultProto, _Mapping]] = ..., convert_to_megachunk_action_result: _Optional[_Union[ConvertToMegachunkActionResultProto, _Mapping]] = ..., cloud_object_gc_action_result: _Optional[_Union[CloudObjectGCActionResultProto, _Mapping]] = ..., fix_cloud_chunk_files_action_result: _Optional[_Union[FixCloudChunkFilesActionResultProto, _Mapping]] = ..., icebox_delete_stub_views_action_result: _Optional[_Union[IceboxDeleteStubViewsActionResultProto, _Mapping]] = ..., orion_lcm_cloud_chunk_files_action_result: _Optional[_Union[LCMCloudChunkFilesActionResultProto, _Mapping]] = ..., chunk_file_container_action_result: _Optional[_Union[ChunkFileContainerActionResultProto, _Mapping]] = ..., s3_composite_action_result: _Optional[_Union[S3CompositeActionResultProto, _Mapping]] = ..., cloud_chunk_file_validation_action_result: _Optional[_Union[CloudChunkFileValidationActionResultProto, _Mapping]] = ..., archive_metadata_gc_action_result: _Optional[_Union[ArchiveMetadataGCActionResultProto, _Mapping]] = ..., downtier_uptiered_cloud_chunk_files_action_result: _Optional[_Union[DowntierUptieredCloudChunkFilesActionResultProto, _Mapping]] = ..., filer_lifecycle_action_result: _Optional[_Union[FilerLifecycleActionResultProto, _Mapping]] = ...) -> None: ...
