from librarian.base import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateIntent(_message.Message):
    __slots__ = ("source", "destinations", "update_type", "state", "num_new_buckets", "arrival_usecs", "update_intent_id", "new_bucket_incarnation_id", "new_index_incarnation_id", "sub_intents", "blacklisted_disks", "blacklisted_nodes", "new_nodes", "fault_tolerance_factor", "overloaded_nodes", "state_detail", "domain_awareness_change", "restore_lost_replicas")
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoChanges: _ClassVar[UpdateIntent.UpdateType]
        kDeleteReplica: _ClassVar[UpdateIntent.UpdateType]
        kSyncReplica: _ClassVar[UpdateIntent.UpdateType]
        kMigrateKeys: _ClassVar[UpdateIntent.UpdateType]
        kShuffleBuckets: _ClassVar[UpdateIntent.UpdateType]
        kDeleteIndex: _ClassVar[UpdateIntent.UpdateType]
        kMarkReplicaReadOnly: _ClassVar[UpdateIntent.UpdateType]
        kMarkReplicaReadWrite: _ClassVar[UpdateIntent.UpdateType]
        kAddReplica: _ClassVar[UpdateIntent.UpdateType]
        kReplicate: _ClassVar[UpdateIntent.UpdateType]
    kNoChanges: UpdateIntent.UpdateType
    kDeleteReplica: UpdateIntent.UpdateType
    kSyncReplica: UpdateIntent.UpdateType
    kMigrateKeys: UpdateIntent.UpdateType
    kShuffleBuckets: UpdateIntent.UpdateType
    kDeleteIndex: UpdateIntent.UpdateType
    kMarkReplicaReadOnly: UpdateIntent.UpdateType
    kMarkReplicaReadWrite: UpdateIntent.UpdateType
    kAddReplica: UpdateIntent.UpdateType
    kReplicate: UpdateIntent.UpdateType
    class UpdateState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[UpdateIntent.UpdateState]
        kStarted: _ClassVar[UpdateIntent.UpdateState]
        kDone: _ClassVar[UpdateIntent.UpdateState]
        kNotAborted: _ClassVar[UpdateIntent.UpdateState]
        kAborted: _ClassVar[UpdateIntent.UpdateState]
        kSlaveError: _ClassVar[UpdateIntent.UpdateState]
        kReadOnly: _ClassVar[UpdateIntent.UpdateState]
        kCopyStarted: _ClassVar[UpdateIntent.UpdateState]
        kCopyDone: _ClassVar[UpdateIntent.UpdateState]
        kCopyNotStarted: _ClassVar[UpdateIntent.UpdateState]
        kShuffleCopyNotStarted: _ClassVar[UpdateIntent.UpdateState]
        kShuffleCopyStarted: _ClassVar[UpdateIntent.UpdateState]
        kShuffleCopyDone: _ClassVar[UpdateIntent.UpdateState]
    kNotStarted: UpdateIntent.UpdateState
    kStarted: UpdateIntent.UpdateState
    kDone: UpdateIntent.UpdateState
    kNotAborted: UpdateIntent.UpdateState
    kAborted: UpdateIntent.UpdateState
    kSlaveError: UpdateIntent.UpdateState
    kReadOnly: UpdateIntent.UpdateState
    kCopyStarted: UpdateIntent.UpdateState
    kCopyDone: UpdateIntent.UpdateState
    kCopyNotStarted: UpdateIntent.UpdateState
    kShuffleCopyNotStarted: UpdateIntent.UpdateState
    kShuffleCopyStarted: UpdateIntent.UpdateState
    kShuffleCopyDone: UpdateIntent.UpdateState
    class DataItem(_message.Message):
        __slots__ = ("disk_id", "bucket_id", "incarnation_id")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        bucket_id: int
        incarnation_id: int
        def __init__(self, disk_id: _Optional[int] = ..., bucket_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
    class BlacklistedDisks(_message.Message):
        __slots__ = ("disk_id", "is_offline")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        is_offline: bool
        def __init__(self, disk_id: _Optional[int] = ..., is_offline: bool = ...) -> None: ...
    class BlacklistedNodes(_message.Message):
        __slots__ = ("node_id", "is_offline")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        is_offline: bool
        def __init__(self, node_id: _Optional[int] = ..., is_offline: bool = ...) -> None: ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_NEW_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    ARRIVAL_USECS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_INTENTS_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_DISKS_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_NODES_FIELD_NUMBER: _ClassVar[int]
    NEW_NODES_FIELD_NUMBER: _ClassVar[int]
    FAULT_TOLERANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    OVERLOADED_NODES_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_AWARENESS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_LOST_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    source: UpdateIntent.DataItem
    destinations: _containers.RepeatedCompositeFieldContainer[UpdateIntent.DataItem]
    update_type: UpdateIntent.UpdateType
    state: UpdateIntent.UpdateState
    num_new_buckets: int
    arrival_usecs: int
    update_intent_id: int
    new_bucket_incarnation_id: int
    new_index_incarnation_id: int
    sub_intents: _containers.RepeatedCompositeFieldContainer[UpdateIntent]
    blacklisted_disks: _containers.RepeatedCompositeFieldContainer[UpdateIntent.BlacklistedDisks]
    blacklisted_nodes: _containers.RepeatedCompositeFieldContainer[UpdateIntent.BlacklistedNodes]
    new_nodes: _containers.RepeatedScalarFieldContainer[int]
    fault_tolerance_factor: int
    overloaded_nodes: _containers.RepeatedScalarFieldContainer[int]
    state_detail: str
    domain_awareness_change: bool
    restore_lost_replicas: bool
    def __init__(self, source: _Optional[_Union[UpdateIntent.DataItem, _Mapping]] = ..., destinations: _Optional[_Iterable[_Union[UpdateIntent.DataItem, _Mapping]]] = ..., update_type: _Optional[_Union[UpdateIntent.UpdateType, str]] = ..., state: _Optional[_Union[UpdateIntent.UpdateState, str]] = ..., num_new_buckets: _Optional[int] = ..., arrival_usecs: _Optional[int] = ..., update_intent_id: _Optional[int] = ..., new_bucket_incarnation_id: _Optional[int] = ..., new_index_incarnation_id: _Optional[int] = ..., sub_intents: _Optional[_Iterable[_Union[UpdateIntent, _Mapping]]] = ..., blacklisted_disks: _Optional[_Iterable[_Union[UpdateIntent.BlacklistedDisks, _Mapping]]] = ..., blacklisted_nodes: _Optional[_Iterable[_Union[UpdateIntent.BlacklistedNodes, _Mapping]]] = ..., new_nodes: _Optional[_Iterable[int]] = ..., fault_tolerance_factor: _Optional[int] = ..., overloaded_nodes: _Optional[_Iterable[int]] = ..., state_detail: _Optional[str] = ..., domain_awareness_change: bool = ..., restore_lost_replicas: bool = ...) -> None: ...

class WalRecord(_message.Message):
    __slots__ = ("index_info_vec",)
    INDEX_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    index_info_vec: _containers.RepeatedCompositeFieldContainer[MasterIndexInfo]
    def __init__(self, index_info_vec: _Optional[_Iterable[_Union[MasterIndexInfo, _Mapping]]] = ...) -> None: ...

class MasterIndexInfo(_message.Message):
    __slots__ = ("index", "update_intent_vec", "rebalancing_state", "num_buckets_mismatch_time_usecs", "num_overloaded_nodes_time_usecs", "previous_migration_stats")
    class RebalancingState(_message.Message):
        __slots__ = ("new_bucket_vec", "blacklisted_bucket_vec")
        NEW_BUCKET_VEC_FIELD_NUMBER: _ClassVar[int]
        BLACKLISTED_BUCKET_VEC_FIELD_NUMBER: _ClassVar[int]
        new_bucket_vec: _containers.RepeatedCompositeFieldContainer[_config_pb2.IndexInfo.BucketInfo]
        blacklisted_bucket_vec: _containers.RepeatedCompositeFieldContainer[_config_pb2.IndexInfo.BucketInfo]
        def __init__(self, new_bucket_vec: _Optional[_Iterable[_Union[_config_pb2.IndexInfo.BucketInfo, _Mapping]]] = ..., blacklisted_bucket_vec: _Optional[_Iterable[_Union[_config_pb2.IndexInfo.BucketInfo, _Mapping]]] = ...) -> None: ...
    class MigrationStats(_message.Message):
        __slots__ = ("update_intent_id", "final_state", "update_type", "arrival_usecs", "finished_usecs", "detail")
        UPDATE_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
        FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        ARRIVAL_USECS_FIELD_NUMBER: _ClassVar[int]
        FINISHED_USECS_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        update_intent_id: int
        final_state: UpdateIntent.UpdateState
        update_type: UpdateIntent.UpdateType
        arrival_usecs: int
        finished_usecs: int
        detail: str
        def __init__(self, update_intent_id: _Optional[int] = ..., final_state: _Optional[_Union[UpdateIntent.UpdateState, str]] = ..., update_type: _Optional[_Union[UpdateIntent.UpdateType, str]] = ..., arrival_usecs: _Optional[int] = ..., finished_usecs: _Optional[int] = ..., detail: _Optional[str] = ...) -> None: ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_VEC_FIELD_NUMBER: _ClassVar[int]
    REBALANCING_STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_BUCKETS_MISMATCH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_OVERLOADED_NODES_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_MIGRATION_STATS_FIELD_NUMBER: _ClassVar[int]
    index: _config_pb2.IndexInfo
    update_intent_vec: _containers.RepeatedCompositeFieldContainer[UpdateIntent]
    rebalancing_state: MasterIndexInfo.RebalancingState
    num_buckets_mismatch_time_usecs: int
    num_overloaded_nodes_time_usecs: int
    previous_migration_stats: _containers.RepeatedCompositeFieldContainer[MasterIndexInfo.MigrationStats]
    def __init__(self, index: _Optional[_Union[_config_pb2.IndexInfo, _Mapping]] = ..., update_intent_vec: _Optional[_Iterable[_Union[UpdateIntent, _Mapping]]] = ..., rebalancing_state: _Optional[_Union[MasterIndexInfo.RebalancingState, _Mapping]] = ..., num_buckets_mismatch_time_usecs: _Optional[int] = ..., num_overloaded_nodes_time_usecs: _Optional[int] = ..., previous_migration_stats: _Optional[_Iterable[_Union[MasterIndexInfo.MigrationStats, _Mapping]]] = ...) -> None: ...

class CloudIndexMigrationState(_message.Message):
    __slots__ = ("index_name", "update_intent_id", "bucket_instance_metadata_map")
    class BucketInstanceMetadata(_message.Message):
        __slots__ = ("read_only", "replication_in_progress", "shuffle_keys_cookie", "prune_keys_cookie", "pruning_completed")
        READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        SHUFFLE_KEYS_COOKIE_FIELD_NUMBER: _ClassVar[int]
        PRUNE_KEYS_COOKIE_FIELD_NUMBER: _ClassVar[int]
        PRUNING_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        read_only: bool
        replication_in_progress: bool
        shuffle_keys_cookie: bytes
        prune_keys_cookie: bytes
        pruning_completed: bool
        def __init__(self, read_only: bool = ..., replication_in_progress: bool = ..., shuffle_keys_cookie: _Optional[bytes] = ..., prune_keys_cookie: _Optional[bytes] = ..., pruning_completed: bool = ...) -> None: ...
    class BucketInstanceMetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CloudIndexMigrationState.BucketInstanceMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CloudIndexMigrationState.BucketInstanceMetadata, _Mapping]] = ...) -> None: ...
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INSTANCE_METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    update_intent_id: int
    bucket_instance_metadata_map: _containers.MessageMap[str, CloudIndexMigrationState.BucketInstanceMetadata]
    def __init__(self, index_name: _Optional[str] = ..., update_intent_id: _Optional[int] = ..., bucket_instance_metadata_map: _Optional[_Mapping[str, CloudIndexMigrationState.BucketInstanceMetadata]] = ...) -> None: ...
