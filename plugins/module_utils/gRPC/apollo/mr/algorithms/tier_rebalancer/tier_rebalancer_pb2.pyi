from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TierRebalancerContextDataProto(_message.Message):
    __slots__ = ("unbalanced_tier_vec", "tier_shuffle_threshold_pct", "min_tier_shuffle_util_pct", "cluster_config_proto")
    class UnbalancedTier(_message.Message):
        __slots__ = ("name", "rebalance_delay_secs", "disk_vec", "avg_util_pct", "high_disk_util_mode", "disks_exclusive_for_chunk_repo")
        class DiskInfo(_message.Message):
            __slots__ = ("disk_id", "util_pct", "capacity_bytes", "node_id", "chassis_id", "rack_id", "partition_id")
            DISK_ID_FIELD_NUMBER: _ClassVar[int]
            UTIL_PCT_FIELD_NUMBER: _ClassVar[int]
            CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
            NODE_ID_FIELD_NUMBER: _ClassVar[int]
            CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
            RACK_ID_FIELD_NUMBER: _ClassVar[int]
            PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
            disk_id: int
            util_pct: float
            capacity_bytes: int
            node_id: int
            chassis_id: int
            rack_id: int
            partition_id: int
            def __init__(self, disk_id: _Optional[int] = ..., util_pct: _Optional[float] = ..., capacity_bytes: _Optional[int] = ..., node_id: _Optional[int] = ..., chassis_id: _Optional[int] = ..., rack_id: _Optional[int] = ..., partition_id: _Optional[int] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        REBALANCE_DELAY_SECS_FIELD_NUMBER: _ClassVar[int]
        DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        AVG_UTIL_PCT_FIELD_NUMBER: _ClassVar[int]
        HIGH_DISK_UTIL_MODE_FIELD_NUMBER: _ClassVar[int]
        DISKS_EXCLUSIVE_FOR_CHUNK_REPO_FIELD_NUMBER: _ClassVar[int]
        name: str
        rebalance_delay_secs: int
        disk_vec: _containers.RepeatedCompositeFieldContainer[TierRebalancerContextDataProto.UnbalancedTier.DiskInfo]
        avg_util_pct: float
        high_disk_util_mode: bool
        disks_exclusive_for_chunk_repo: bool
        def __init__(self, name: _Optional[str] = ..., rebalance_delay_secs: _Optional[int] = ..., disk_vec: _Optional[_Iterable[_Union[TierRebalancerContextDataProto.UnbalancedTier.DiskInfo, _Mapping]]] = ..., avg_util_pct: _Optional[float] = ..., high_disk_util_mode: bool = ..., disks_exclusive_for_chunk_repo: bool = ...) -> None: ...
    UNBALANCED_TIER_VEC_FIELD_NUMBER: _ClassVar[int]
    TIER_SHUFFLE_THRESHOLD_PCT_FIELD_NUMBER: _ClassVar[int]
    MIN_TIER_SHUFFLE_UTIL_PCT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    unbalanced_tier_vec: _containers.RepeatedCompositeFieldContainer[TierRebalancerContextDataProto.UnbalancedTier]
    tier_shuffle_threshold_pct: int
    min_tier_shuffle_util_pct: int
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, unbalanced_tier_vec: _Optional[_Iterable[_Union[TierRebalancerContextDataProto.UnbalancedTier, _Mapping]]] = ..., tier_shuffle_threshold_pct: _Optional[int] = ..., min_tier_shuffle_util_pct: _Optional[int] = ..., cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class TierRebalancerReducerValueProto(_message.Message):
    __slots__ = ("chunk_file_id", "scribe_row_version", "owner_blob_id", "owner_view_box_id", "chunk_count", "max_replica_failures", "max_entity_failures", "strictness", "morphed_size", "replica_disk_id_vec", "container_id")
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_FAILURES_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTITY_FAILURES_FIELD_NUMBER: _ClassVar[int]
    STRICTNESS_FIELD_NUMBER: _ClassVar[int]
    MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    scribe_row_version: int
    owner_blob_id: int
    owner_view_box_id: int
    chunk_count: int
    max_replica_failures: int
    max_entity_failures: int
    strictness: _cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness.Level
    morphed_size: int
    replica_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    container_id: int
    def __init__(self, chunk_file_id: _Optional[int] = ..., scribe_row_version: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., owner_view_box_id: _Optional[int] = ..., chunk_count: _Optional[int] = ..., max_replica_failures: _Optional[int] = ..., max_entity_failures: _Optional[int] = ..., strictness: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness.Level, str]] = ..., morphed_size: _Optional[int] = ..., replica_disk_id_vec: _Optional[_Iterable[int]] = ..., container_id: _Optional[int] = ...) -> None: ...
