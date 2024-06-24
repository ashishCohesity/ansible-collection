from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from bridge.cloud_chunk_repository import cloud_chunk_repository_pb2 as _cloud_chunk_repository_pb2
from bridge.vault.base import worm_pb2 as _worm_pb2
from cohesion.dataplane_object_manager import dataplane_object_pb2 as _dataplane_object_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShuffleChunkFileArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "chunk_file_id", "target_storage_tier", "prefered_node_id", "disk_id_vec", "reason", "target_vault_id", "num_replicas_in_target_tier", "scribe_version", "chunk_count", "source_replica_disk_id", "priority", "is_optional")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
    PREFERED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TARGET_VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_REPLICAS_IN_TARGET_TIER_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    chunk_file_id: int
    target_storage_tier: str
    prefered_node_id: int
    disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    reason: _blob_store_pb2.MorphParams.Reason
    target_vault_id: int
    num_replicas_in_target_tier: int
    scribe_version: int
    chunk_count: int
    source_replica_disk_id: int
    priority: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal.Priority
    is_optional: bool
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., chunk_file_id: _Optional[int] = ..., target_storage_tier: _Optional[str] = ..., prefered_node_id: _Optional[int] = ..., disk_id_vec: _Optional[_Iterable[int]] = ..., reason: _Optional[_Union[_blob_store_pb2.MorphParams.Reason, str]] = ..., target_vault_id: _Optional[int] = ..., num_replicas_in_target_tier: _Optional[int] = ..., scribe_version: _Optional[int] = ..., chunk_count: _Optional[int] = ..., source_replica_disk_id: _Optional[int] = ..., priority: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal.Priority, str]] = ..., is_optional: bool = ...) -> None: ...

class ShuffleChunkFileResult(_message.Message):
    __slots__ = ("remote_session_id", "chunk_file_max_pin_secs")
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_MAX_PIN_SECS_FIELD_NUMBER: _ClassVar[int]
    remote_session_id: int
    chunk_file_max_pin_secs: int
    def __init__(self, remote_session_id: _Optional[int] = ..., chunk_file_max_pin_secs: _Optional[int] = ...) -> None: ...

class MigrateChunksArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "src_chunk_file_id", "clevel", "elevel", "target_storage_tier", "prefered_node_id", "reason", "disable_erasure_coding", "use_reserve_capacity", "is_optional")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CLEVEL_FIELD_NUMBER: _ClassVar[int]
    ELEVEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_STORAGE_TIER_FIELD_NUMBER: _ClassVar[int]
    PREFERED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ERASURE_CODING_FIELD_NUMBER: _ClassVar[int]
    USE_RESERVE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    src_chunk_file_id: int
    clevel: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    elevel: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    target_storage_tier: str
    prefered_node_id: int
    reason: _blob_store_pb2.MorphParams.Reason
    disable_erasure_coding: bool
    use_reserve_capacity: bool
    is_optional: bool
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., src_chunk_file_id: _Optional[int] = ..., clevel: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., elevel: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., target_storage_tier: _Optional[str] = ..., prefered_node_id: _Optional[int] = ..., reason: _Optional[_Union[_blob_store_pb2.MorphParams.Reason, str]] = ..., disable_erasure_coding: bool = ..., use_reserve_capacity: bool = ..., is_optional: bool = ...) -> None: ...

class MigrateChunksResult(_message.Message):
    __slots__ = ("remote_session_id",)
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    remote_session_id: int
    def __init__(self, remote_session_id: _Optional[int] = ...) -> None: ...

class BrickExtents(_message.Message):
    __slots__ = ("extent_vec",)
    EXTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    extent_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.BrickMetadataProto.Extent]
    def __init__(self, extent_vec: _Optional[_Iterable[_Union[_blob_store_pb2.BrickMetadataProto.Extent, _Mapping]]] = ...) -> None: ...

class CloneExtentsArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "offset", "count", "fail_if_journal_has_overlapping_range")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FAIL_IF_JOURNAL_HAS_OVERLAPPING_RANGE_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    offset: int
    count: int
    fail_if_journal_has_overlapping_range: bool
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., offset: _Optional[int] = ..., count: _Optional[int] = ..., fail_if_journal_has_overlapping_range: bool = ...) -> None: ...

class CloneExtentsResult(_message.Message):
    __slots__ = ("brick_map",)
    class BrickMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BrickExtents
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BrickExtents, _Mapping]] = ...) -> None: ...
    BRICK_MAP_FIELD_NUMBER: _ClassVar[int]
    brick_map: _containers.MessageMap[int, BrickExtents]
    def __init__(self, brick_map: _Optional[_Mapping[int, BrickExtents]] = ...) -> None: ...

class WriteExtentsArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "offset", "brick_map", "chunk_reference_held")
    class BrickMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BrickExtents
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BrickExtents, _Mapping]] = ...) -> None: ...
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BRICK_MAP_FIELD_NUMBER: _ClassVar[int]
    CHUNK_REFERENCE_HELD_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    offset: int
    brick_map: _containers.MessageMap[int, BrickExtents]
    chunk_reference_held: bool
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., offset: _Optional[int] = ..., brick_map: _Optional[_Mapping[int, BrickExtents]] = ..., chunk_reference_held: bool = ...) -> None: ...

class WriteExtentsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InvalidateDataJournalByteRangeArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "offset", "length")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    offset: int
    length: int
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class InvalidateDataJournalByteRangeResult(_message.Message):
    __slots__ = ("invalidated_ranges", "non_empty_ranges")
    class Range(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    INVALIDATED_RANGES_FIELD_NUMBER: _ClassVar[int]
    NON_EMPTY_RANGES_FIELD_NUMBER: _ClassVar[int]
    invalidated_ranges: _containers.RepeatedCompositeFieldContainer[InvalidateDataJournalByteRangeResult.Range]
    non_empty_ranges: _containers.RepeatedCompositeFieldContainer[InvalidateDataJournalByteRangeResult.Range]
    def __init__(self, invalidated_ranges: _Optional[_Iterable[_Union[InvalidateDataJournalByteRangeResult.Range, _Mapping]]] = ..., non_empty_ranges: _Optional[_Iterable[_Union[InvalidateDataJournalByteRangeResult.Range, _Mapping]]] = ...) -> None: ...

class ReadCloudChunkFileInfoArg(_message.Message):
    __slots__ = ("cloud_object_id", "version", "metadata_only")
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    version: int
    metadata_only: bool
    def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., version: _Optional[int] = ..., metadata_only: bool = ...) -> None: ...

class ReadCloudChunkFileInfoResult(_message.Message):
    __slots__ = ("cloud_chunk_file_metadata_proto", "cloud_chunk_file_enc_metadata_proto")
    CLOUD_CHUNK_FILE_METADATA_PROTO_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_ENC_METADATA_PROTO_FIELD_NUMBER: _ClassVar[int]
    cloud_chunk_file_metadata_proto: _cloud_chunk_repository_pb2.CloudChunkFileMetadataProto
    cloud_chunk_file_enc_metadata_proto: _cloud_chunk_repository_pb2.CloudChunkFileEncryptionMetadataProto
    def __init__(self, cloud_chunk_file_metadata_proto: _Optional[_Union[_cloud_chunk_repository_pb2.CloudChunkFileMetadataProto, _Mapping]] = ..., cloud_chunk_file_enc_metadata_proto: _Optional[_Union[_cloud_chunk_repository_pb2.CloudChunkFileEncryptionMetadataProto, _Mapping]] = ...) -> None: ...

class DowntierChunkInfo(_message.Message):
    __slots__ = ("chunk_id", "blob_snap_tree_leaf_node_id", "blob_snap_tree_id")
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_id: _blob_store_pb2.ChunkIdProto
    blob_snap_tree_leaf_node_id: int
    blob_snap_tree_id: int
    def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., blob_snap_tree_leaf_node_id: _Optional[int] = ..., blob_snap_tree_id: _Optional[int] = ...) -> None: ...

class DowntierChunksToCloudArg(_message.Message):
    __slots__ = ("chunk_info_vec", "chunk_file_id_vec", "force_flush", "delete_local_chunks", "cloud_domain_id", "view_box_id", "request_context", "downtier_chunk_file", "worm_params")
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_FLUSH_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOCAL_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    WORM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[DowntierChunkInfo]
    chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    force_flush: bool
    delete_local_chunks: bool
    cloud_domain_id: int
    view_box_id: int
    request_context: _request_context_pb2.RequestContextProto
    downtier_chunk_file: bool
    worm_params: _worm_pb2.WORMParams
    def __init__(self, chunk_info_vec: _Optional[_Iterable[_Union[DowntierChunkInfo, _Mapping]]] = ..., chunk_file_id_vec: _Optional[_Iterable[int]] = ..., force_flush: bool = ..., delete_local_chunks: bool = ..., cloud_domain_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., downtier_chunk_file: bool = ..., worm_params: _Optional[_Union[_worm_pb2.WORMParams, _Mapping]] = ...) -> None: ...

class DowntierChunksToCloudResult(_message.Message):
    __slots__ = ("chunk_location_info_vec", "skipped_chunk_info_vec", "downtier_stats", "rearchived_chunks", "minimum_retention_timestamp_secs")
    class ChunkLocationInfo(_message.Message):
        __slots__ = ("chunk_id", "chunk_file_id", "cloud_chunk_info_vec")
        class CloudChunkInfo(_message.Message):
            __slots__ = ("cloud_object_id", "cloud_chunk_id")
            CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
            CLOUD_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
            cloud_object_id: _cloud_pb2.CloudObjectIdProto
            cloud_chunk_id: _blob_store_pb2.CloudChunkIdProto
            def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., cloud_chunk_id: _Optional[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]] = ...) -> None: ...
        CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        CLOUD_CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        chunk_id: _blob_store_pb2.ChunkIdProto
        chunk_file_id: int
        cloud_chunk_info_vec: _containers.RepeatedCompositeFieldContainer[DowntierChunksToCloudResult.ChunkLocationInfo.CloudChunkInfo]
        def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., chunk_file_id: _Optional[int] = ..., cloud_chunk_info_vec: _Optional[_Iterable[_Union[DowntierChunksToCloudResult.ChunkLocationInfo.CloudChunkInfo, _Mapping]]] = ...) -> None: ...
    class DowntierChunksToCloudStats(_message.Message):
        __slots__ = ("logical_downtiered_bytes", "physical_downtiered_bytes", "num_chunks_rearchived", "num_cloud_chunk_files_worm_retention_extended", "num_bytes_rearchived")
        LOGICAL_DOWNTIERED_BYTES_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_DOWNTIERED_BYTES_FIELD_NUMBER: _ClassVar[int]
        NUM_CHUNKS_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
        NUM_CLOUD_CHUNK_FILES_WORM_RETENTION_EXTENDED_FIELD_NUMBER: _ClassVar[int]
        NUM_BYTES_REARCHIVED_FIELD_NUMBER: _ClassVar[int]
        logical_downtiered_bytes: int
        physical_downtiered_bytes: int
        num_chunks_rearchived: int
        num_cloud_chunk_files_worm_retention_extended: int
        num_bytes_rearchived: int
        def __init__(self, logical_downtiered_bytes: _Optional[int] = ..., physical_downtiered_bytes: _Optional[int] = ..., num_chunks_rearchived: _Optional[int] = ..., num_cloud_chunk_files_worm_retention_extended: _Optional[int] = ..., num_bytes_rearchived: _Optional[int] = ...) -> None: ...
    CHUNK_LOCATION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DOWNTIER_STATS_FIELD_NUMBER: _ClassVar[int]
    REARCHIVED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    chunk_location_info_vec: _containers.RepeatedCompositeFieldContainer[DowntierChunksToCloudResult.ChunkLocationInfo]
    skipped_chunk_info_vec: _containers.RepeatedCompositeFieldContainer[DowntierChunkInfo]
    downtier_stats: DowntierChunksToCloudResult.DowntierChunksToCloudStats
    rearchived_chunks: bool
    minimum_retention_timestamp_secs: int
    def __init__(self, chunk_location_info_vec: _Optional[_Iterable[_Union[DowntierChunksToCloudResult.ChunkLocationInfo, _Mapping]]] = ..., skipped_chunk_info_vec: _Optional[_Iterable[_Union[DowntierChunkInfo, _Mapping]]] = ..., downtier_stats: _Optional[_Union[DowntierChunksToCloudResult.DowntierChunksToCloudStats, _Mapping]] = ..., rearchived_chunks: bool = ..., minimum_retention_timestamp_secs: _Optional[int] = ...) -> None: ...

class FlushDataJournalArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "offset", "count", "is_optional", "request_context")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    offset: int
    count: int
    is_optional: bool
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., offset: _Optional[int] = ..., count: _Optional[int] = ..., is_optional: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class FlushDataJournalResult(_message.Message):
    __slots__ = ("remote_session_id",)
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    remote_session_id: int
    def __init__(self, remote_session_id: _Optional[int] = ...) -> None: ...

class GetChunkFileDowntierOwnerInfoArg(_message.Message):
    __slots__ = ("chunk_id_vec", "chunk_file_id_vec", "allow_cache_lookup", "request_context")
    CHUNK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CACHE_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    chunk_id_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.ChunkIdProto]
    chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
    allow_cache_lookup: bool
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, chunk_id_vec: _Optional[_Iterable[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]]] = ..., chunk_file_id_vec: _Optional[_Iterable[int]] = ..., allow_cache_lookup: bool = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class GetChunkFileDowntierOwnerInfoResult(_message.Message):
    __slots__ = ("chunk_id_2_chunk_file_id_map_entry_vec", "chunk_file_id_2_session_id_map_entry_vec")
    class ChunkId2ChunkFileIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: _blob_store_pb2.ChunkIdProto
        value: int
        def __init__(self, key: _Optional[_Union[_blob_store_pb2.ChunkIdProto, _Mapping]] = ..., value: _Optional[int] = ...) -> None: ...
    class ChunkFileId2SessionIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CHUNK_ID_2_CHUNK_FILE_ID_MAP_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_2_SESSION_ID_MAP_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    chunk_id_2_chunk_file_id_map_entry_vec: _containers.RepeatedCompositeFieldContainer[GetChunkFileDowntierOwnerInfoResult.ChunkId2ChunkFileIdMapEntry]
    chunk_file_id_2_session_id_map_entry_vec: _containers.RepeatedCompositeFieldContainer[GetChunkFileDowntierOwnerInfoResult.ChunkFileId2SessionIdMapEntry]
    def __init__(self, chunk_id_2_chunk_file_id_map_entry_vec: _Optional[_Iterable[_Union[GetChunkFileDowntierOwnerInfoResult.ChunkId2ChunkFileIdMapEntry, _Mapping]]] = ..., chunk_file_id_2_session_id_map_entry_vec: _Optional[_Iterable[_Union[GetChunkFileDowntierOwnerInfoResult.ChunkFileId2SessionIdMapEntry, _Mapping]]] = ...) -> None: ...

class LookupBlobSnapTreeBrickSizeArg(_message.Message):
    __slots__ = ("blob_snap_tree_id",)
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    def __init__(self, blob_snap_tree_id: _Optional[int] = ...) -> None: ...

class LookupBlobSnapTreeBrickSizeResult(_message.Message):
    __slots__ = ("brick_size",)
    BRICK_SIZE_FIELD_NUMBER: _ClassVar[int]
    brick_size: int
    def __init__(self, brick_size: _Optional[int] = ...) -> None: ...

class RestoreStubBrickDataArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "offset", "data", "request_context")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    offset: int
    data: bytes
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class RestoreStubBrickDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UptierArg(_message.Message):
    __slots__ = ("cloud_object_id", "epoch_id", "target_tier_type", "request_context", "retention_msecs")
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MSECS_FIELD_NUMBER: _ClassVar[int]
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    epoch_id: int
    target_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
    request_context: _request_context_pb2.RequestContextProto
    retention_msecs: int
    def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., epoch_id: _Optional[int] = ..., target_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ..., retention_msecs: _Optional[int] = ...) -> None: ...

class UptierResult(_message.Message):
    __slots__ = ("uptier_status", "expiry_time")
    UPTIER_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    uptier_status: bool
    expiry_time: int
    def __init__(self, uptier_status: bool = ..., expiry_time: _Optional[int] = ...) -> None: ...

class CopyBricksToDataPlaneObjectArg(_message.Message):
    __slots__ = ("blob_snap_tree_id", "brick_info_vec", "object_params", "request_context")
    class CopyBrickInfoProto(_message.Message):
        __slots__ = ("brick_key", "blob_snap_tree_leaf_node_id")
        BRICK_KEY_FIELD_NUMBER: _ClassVar[int]
        BLOB_SNAP_TREE_LEAF_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        brick_key: int
        blob_snap_tree_leaf_node_id: int
        def __init__(self, brick_key: _Optional[int] = ..., blob_snap_tree_leaf_node_id: _Optional[int] = ...) -> None: ...
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    BRICK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    brick_info_vec: _containers.RepeatedCompositeFieldContainer[CopyBricksToDataPlaneObjectArg.CopyBrickInfoProto]
    object_params: _dataplane_object_pb2.ObjectParamsProto
    request_context: _request_context_pb2.RequestContextProto
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., brick_info_vec: _Optional[_Iterable[_Union[CopyBricksToDataPlaneObjectArg.CopyBrickInfoProto, _Mapping]]] = ..., object_params: _Optional[_Union[_dataplane_object_pb2.ObjectParamsProto, _Mapping]] = ..., request_context: _Optional[_Union[_request_context_pb2.RequestContextProto, _Mapping]] = ...) -> None: ...

class CopyBricksToDataPlaneObjectResult(_message.Message):
    __slots__ = ("brick_sha256_vec",)
    BRICK_SHA256_VEC_FIELD_NUMBER: _ClassVar[int]
    brick_sha256_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, brick_sha256_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...
