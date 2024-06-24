from apollo.mr.algorithms.inode_stats.utils import utils_pb2 as _utils_pb2
from apollo.mr.base import histogram_proto_pb2 as _histogram_proto_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SummarizedChunkFileStatsProto(_message.Message):
    __slots__ = ("num_chunk_files", "total_chunk_file_bytes", "histogram", "num_chunks", "num_containers")
    NUM_CHUNK_FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHUNK_FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    NUM_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    num_chunk_files: int
    total_chunk_file_bytes: int
    histogram: _histogram_proto_pb2.HistogramProto
    num_chunks: int
    num_containers: int
    def __init__(self, num_chunk_files: _Optional[int] = ..., total_chunk_file_bytes: _Optional[int] = ..., histogram: _Optional[_Union[_histogram_proto_pb2.HistogramProto, _Mapping]] = ..., num_chunks: _Optional[int] = ..., num_containers: _Optional[int] = ...) -> None: ...

class ResiliencyDomainProto(_message.Message):
    __slots__ = ("type", "id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DataUnavailable: _ClassVar[ResiliencyDomainProto.Type]
        UnderReplicated: _ClassVar[ResiliencyDomainProto.Type]
        NeedsHealing: _ClassVar[ResiliencyDomainProto.Type]
        Disk: _ClassVar[ResiliencyDomainProto.Type]
        Node: _ClassVar[ResiliencyDomainProto.Type]
        Chassis: _ClassVar[ResiliencyDomainProto.Type]
        Rack: _ClassVar[ResiliencyDomainProto.Type]
        NeedsNodeDispersal: _ClassVar[ResiliencyDomainProto.Type]
        NeedsChassisDispersal: _ClassVar[ResiliencyDomainProto.Type]
        NeedsRackDispersal: _ClassVar[ResiliencyDomainProto.Type]
        NeedsHealingUserInitiated: _ClassVar[ResiliencyDomainProto.Type]
        NeedsHealingSoftwareInitiated: _ClassVar[ResiliencyDomainProto.Type]
        NeedsHealingUnhealthyReplica: _ClassVar[ResiliencyDomainProto.Type]
    DataUnavailable: ResiliencyDomainProto.Type
    UnderReplicated: ResiliencyDomainProto.Type
    NeedsHealing: ResiliencyDomainProto.Type
    Disk: ResiliencyDomainProto.Type
    Node: ResiliencyDomainProto.Type
    Chassis: ResiliencyDomainProto.Type
    Rack: ResiliencyDomainProto.Type
    NeedsNodeDispersal: ResiliencyDomainProto.Type
    NeedsChassisDispersal: ResiliencyDomainProto.Type
    NeedsRackDispersal: ResiliencyDomainProto.Type
    NeedsHealingUserInitiated: ResiliencyDomainProto.Type
    NeedsHealingSoftwareInitiated: ResiliencyDomainProto.Type
    NeedsHealingUnhealthyReplica: ResiliencyDomainProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: ResiliencyDomainProto.Type
    id: int
    def __init__(self, type: _Optional[_Union[ResiliencyDomainProto.Type, str]] = ..., id: _Optional[int] = ...) -> None: ...

class ChunkFileEncodingProto(_message.Message):
    __slots__ = ("replication_factor", "num_data_stripes", "num_coded_stripes", "container_chunk_file")
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
    NUM_CODED_STRIPES_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    replication_factor: int
    num_data_stripes: int
    num_coded_stripes: int
    container_chunk_file: bool
    def __init__(self, replication_factor: _Optional[int] = ..., num_data_stripes: _Optional[int] = ..., num_coded_stripes: _Optional[int] = ..., container_chunk_file: bool = ...) -> None: ...

class SummarizedResiliencyStatsProto(_message.Message):
    __slots__ = ("remaining_tolerance_map", "remaining_tolerance_container_map", "encoding_stats_vec", "unsafe_to_ack_disk_removal")
    class RemainingToleranceMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SummarizedChunkFileStatsProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SummarizedChunkFileStatsProto, _Mapping]] = ...) -> None: ...
    class RemainingToleranceContainerMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SummarizedChunkFileStatsProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SummarizedChunkFileStatsProto, _Mapping]] = ...) -> None: ...
    class EncodingStats(_message.Message):
        __slots__ = ("encoding", "stats")
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        encoding: ChunkFileEncodingProto
        stats: SummarizedChunkFileStatsProto
        def __init__(self, encoding: _Optional[_Union[ChunkFileEncodingProto, _Mapping]] = ..., stats: _Optional[_Union[SummarizedChunkFileStatsProto, _Mapping]] = ...) -> None: ...
    REMAINING_TOLERANCE_MAP_FIELD_NUMBER: _ClassVar[int]
    REMAINING_TOLERANCE_CONTAINER_MAP_FIELD_NUMBER: _ClassVar[int]
    ENCODING_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    UNSAFE_TO_ACK_DISK_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    remaining_tolerance_map: _containers.MessageMap[int, SummarizedChunkFileStatsProto]
    remaining_tolerance_container_map: _containers.MessageMap[int, SummarizedChunkFileStatsProto]
    encoding_stats_vec: _containers.RepeatedCompositeFieldContainer[SummarizedResiliencyStatsProto.EncodingStats]
    unsafe_to_ack_disk_removal: bool
    def __init__(self, remaining_tolerance_map: _Optional[_Mapping[int, SummarizedChunkFileStatsProto]] = ..., remaining_tolerance_container_map: _Optional[_Mapping[int, SummarizedChunkFileStatsProto]] = ..., encoding_stats_vec: _Optional[_Iterable[_Union[SummarizedResiliencyStatsProto.EncodingStats, _Mapping]]] = ..., unsafe_to_ack_disk_removal: bool = ...) -> None: ...

class ChunkFileAttributesProto(_message.Message):
    __slots__ = ("compression", "encryption", "cloud_tier", "update_intent", "container_chunk_file")
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TIER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
    compression: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    encryption: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    cloud_tier: bool
    update_intent: bool
    container_chunk_file: bool
    def __init__(self, compression: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., cloud_tier: bool = ..., update_intent: bool = ..., container_chunk_file: bool = ...) -> None: ...

class ViewboxTierStatsMapValueProto(_message.Message):
    __slots__ = ("encoding_vec", "encoding_stats_vec", "attribute_vec", "attribute_stats_vec", "summarized_chunk_stats", "summarized_container_chunk_stats", "encryption_mode_vec", "encryption_mode_stats_vec")
    ENCODING_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCODING_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZED_CHUNK_STATS_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZED_CONTAINER_CHUNK_STATS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    encoding_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileEncodingProto]
    encoding_stats_vec: _containers.RepeatedCompositeFieldContainer[SummarizedChunkFileStatsProto]
    attribute_vec: _containers.RepeatedCompositeFieldContainer[ChunkFileAttributesProto]
    attribute_stats_vec: _containers.RepeatedCompositeFieldContainer[SummarizedChunkFileStatsProto]
    summarized_chunk_stats: _utils_pb2.SummarizedChunkStatsProto
    summarized_container_chunk_stats: _utils_pb2.SummarizedChunkStatsProto
    encryption_mode_vec: _containers.RepeatedScalarFieldContainer[_aes_encryptor_pb2.AESEncryptorMode]
    encryption_mode_stats_vec: _containers.RepeatedCompositeFieldContainer[SummarizedChunkFileStatsProto]
    def __init__(self, encoding_vec: _Optional[_Iterable[_Union[ChunkFileEncodingProto, _Mapping]]] = ..., encoding_stats_vec: _Optional[_Iterable[_Union[SummarizedChunkFileStatsProto, _Mapping]]] = ..., attribute_vec: _Optional[_Iterable[_Union[ChunkFileAttributesProto, _Mapping]]] = ..., attribute_stats_vec: _Optional[_Iterable[_Union[SummarizedChunkFileStatsProto, _Mapping]]] = ..., summarized_chunk_stats: _Optional[_Union[_utils_pb2.SummarizedChunkStatsProto, _Mapping]] = ..., summarized_container_chunk_stats: _Optional[_Union[_utils_pb2.SummarizedChunkStatsProto, _Mapping]] = ..., encryption_mode_vec: _Optional[_Iterable[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]]] = ..., encryption_mode_stats_vec: _Optional[_Iterable[_Union[SummarizedChunkFileStatsProto, _Mapping]]] = ...) -> None: ...

class ReplicationFixerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto", "stats_reporter_mode", "speedup_disk_removal_for_empty_chunk_files", "disk_ids_to_ack_vec", "num_shards", "num_scribe_buckets", "defrag_container_mode", "skip_defrag_container_mode", "enable_paranoid_range_scan_mode")
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    STATS_REPORTER_MODE_FIELD_NUMBER: _ClassVar[int]
    SPEEDUP_DISK_REMOVAL_FOR_EMPTY_CHUNK_FILES_FIELD_NUMBER: _ClassVar[int]
    DISK_IDS_TO_ACK_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    NUM_SCRIBE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    DEFRAG_CONTAINER_MODE_FIELD_NUMBER: _ClassVar[int]
    SKIP_DEFRAG_CONTAINER_MODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PARANOID_RANGE_SCAN_MODE_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    stats_reporter_mode: bool
    speedup_disk_removal_for_empty_chunk_files: bool
    disk_ids_to_ack_vec: _containers.RepeatedScalarFieldContainer[int]
    num_shards: int
    num_scribe_buckets: int
    defrag_container_mode: bool
    skip_defrag_container_mode: bool
    enable_paranoid_range_scan_mode: bool
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., stats_reporter_mode: bool = ..., speedup_disk_removal_for_empty_chunk_files: bool = ..., disk_ids_to_ack_vec: _Optional[_Iterable[int]] = ..., num_shards: _Optional[int] = ..., num_scribe_buckets: _Optional[int] = ..., defrag_container_mode: bool = ..., skip_defrag_container_mode: bool = ..., enable_paranoid_range_scan_mode: bool = ...) -> None: ...

class ContainerReplicationFixerReducerValueProto(_message.Message):
    __slots__ = ("container_info", "chunk_file_info")
    class ContainerInfo(_message.Message):
        __slots__ = ("view_box_id", "chunk_file_id_vec", "update_intent", "op_in_progress", "ec_info")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
        OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        EC_INFO_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        chunk_file_id_vec: _containers.RepeatedScalarFieldContainer[int]
        update_intent: _blob_store_pb2.ChunkFileContainerMetadataProto.UpdateIntent
        op_in_progress: bool
        ec_info: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.ECInfo
        def __init__(self, view_box_id: _Optional[int] = ..., chunk_file_id_vec: _Optional[_Iterable[int]] = ..., update_intent: _Optional[_Union[_blob_store_pb2.ChunkFileContainerMetadataProto.UpdateIntent, _Mapping]] = ..., op_in_progress: bool = ..., ec_info: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.ECInfo, _Mapping]] = ...) -> None: ...
    class ChunkFileInfo(_message.Message):
        __slots__ = ("chunk_file_id", "owner_blob_id", "view_box_id", "replica", "intent_pending", "op_in_progress", "is_any_disk_on_cloud", "chunk_count", "scribe_row_version", "chunk_file_physical_bytes", "chunk_physical_bytes", "chunk_logical_bytes", "has_brick_owned_chunks", "target_tier", "is_coded_chunk_file")
        CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        REPLICA_FIELD_NUMBER: _ClassVar[int]
        INTENT_PENDING_FIELD_NUMBER: _ClassVar[int]
        OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        IS_ANY_DISK_ON_CLOUD_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FILE_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        CHUNK_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        HAS_BRICK_OWNED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIER_FIELD_NUMBER: _ClassVar[int]
        IS_CODED_CHUNK_FILE_FIELD_NUMBER: _ClassVar[int]
        chunk_file_id: int
        owner_blob_id: int
        view_box_id: int
        replica: _blob_store_pb2.ChunkFileMetadataProto.Replica
        intent_pending: bool
        op_in_progress: bool
        is_any_disk_on_cloud: bool
        chunk_count: int
        scribe_row_version: int
        chunk_file_physical_bytes: int
        chunk_physical_bytes: int
        chunk_logical_bytes: int
        has_brick_owned_chunks: bool
        target_tier: str
        is_coded_chunk_file: bool
        def __init__(self, chunk_file_id: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., replica: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.Replica, _Mapping]] = ..., intent_pending: bool = ..., op_in_progress: bool = ..., is_any_disk_on_cloud: bool = ..., chunk_count: _Optional[int] = ..., scribe_row_version: _Optional[int] = ..., chunk_file_physical_bytes: _Optional[int] = ..., chunk_physical_bytes: _Optional[int] = ..., chunk_logical_bytes: _Optional[int] = ..., has_brick_owned_chunks: bool = ..., target_tier: _Optional[str] = ..., is_coded_chunk_file: bool = ...) -> None: ...
    CONTAINER_INFO_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    container_info: ContainerReplicationFixerReducerValueProto.ContainerInfo
    chunk_file_info: ContainerReplicationFixerReducerValueProto.ChunkFileInfo
    def __init__(self, container_info: _Optional[_Union[ContainerReplicationFixerReducerValueProto.ContainerInfo, _Mapping]] = ..., chunk_file_info: _Optional[_Union[ContainerReplicationFixerReducerValueProto.ChunkFileInfo, _Mapping]] = ...) -> None: ...

class ContainerReplicationFixerContainerInfoReducerProto(_message.Message):
    __slots__ = ("view_box_id", "chunk_file_info_vec", "update_intent", "op_in_progress", "ec_info")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    OP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    EC_INFO_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    chunk_file_info_vec: _containers.RepeatedCompositeFieldContainer[ContainerReplicationFixerReducerValueProto.ChunkFileInfo]
    update_intent: _blob_store_pb2.ChunkFileContainerMetadataProto.UpdateIntent
    op_in_progress: bool
    ec_info: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.ECInfo
    def __init__(self, view_box_id: _Optional[int] = ..., chunk_file_info_vec: _Optional[_Iterable[_Union[ContainerReplicationFixerReducerValueProto.ChunkFileInfo, _Mapping]]] = ..., update_intent: _Optional[_Union[_blob_store_pb2.ChunkFileContainerMetadataProto.UpdateIntent, _Mapping]] = ..., op_in_progress: bool = ..., ec_info: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.ECInfo, _Mapping]] = ...) -> None: ...

class ContainerReplicationFixerMapperKeyProto(_message.Message):
    __slots__ = ("reducer_key", "view_box_id")
    REDUCER_KEY_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    reducer_key: int
    view_box_id: int
    def __init__(self, reducer_key: _Optional[int] = ..., view_box_id: _Optional[int] = ...) -> None: ...

class ChunkFileStatsReporterMapValueProto(_message.Message):
    __slots__ = ("time_to_last_access_secs", "view_box_id", "tier_name")
    TIME_TO_LAST_ACCESS_SECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_NAME_FIELD_NUMBER: _ClassVar[int]
    time_to_last_access_secs: int
    view_box_id: int
    tier_name: str
    def __init__(self, time_to_last_access_secs: _Optional[int] = ..., view_box_id: _Optional[int] = ..., tier_name: _Optional[str] = ...) -> None: ...

class ChunkFileStatsReporterHistogramReducerKeyProto(_message.Message):
    __slots__ = ("view_box_id", "tier_name")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_NAME_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    tier_name: str
    def __init__(self, view_box_id: _Optional[int] = ..., tier_name: _Optional[str] = ...) -> None: ...

class ChunkFileStatsReporterHistogramReducerValueProto(_message.Message):
    __slots__ = ("time_to_last_access_secs", "tier_name", "num_chunk_files_without_last_access_time")
    TIME_TO_LAST_ACCESS_SECS_FIELD_NUMBER: _ClassVar[int]
    TIER_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_WITHOUT_LAST_ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    time_to_last_access_secs: int
    tier_name: str
    num_chunk_files_without_last_access_time: int
    def __init__(self, time_to_last_access_secs: _Optional[int] = ..., tier_name: _Optional[str] = ..., num_chunk_files_without_last_access_time: _Optional[int] = ...) -> None: ...
