from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewConfigProto(_message.Message):
    __slots__ = ("constituents", "views", "last_shuffle_start_time_usecs", "last_shuffle_end_time_usecs", "paxos_disabled", "hashing_scheme", "use_multiple_disks_per_node", "is_healing", "cluster_setting", "num_hosting_constituents", "desired_bucket_options", "cleanup_graceful_removal_constituent", "rings", "placement_mode", "desired_setting", "shadow_rings", "space_only_mode_constituents_enabled", "low_mem_usage_setting_tablet_enabled", "last_ssd_rotation_start_time_usecs", "last_ssd_rotation_finish_time_usecs", "current_fault_tolerance", "capturing_row_history_enabled", "scribe_allow_cohesity_wal")
    class PaxosMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLegacyPaxosMode: _ClassVar[ViewConfigProto.PaxosMode]
        kUpgradedFromLegacy: _ClassVar[ViewConfigProto.PaxosMode]
        kNewPaxosMode: _ClassVar[ViewConfigProto.PaxosMode]
    kLegacyPaxosMode: ViewConfigProto.PaxosMode
    kUpgradedFromLegacy: ViewConfigProto.PaxosMode
    kNewPaxosMode: ViewConfigProto.PaxosMode
    class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnappyCompression: _ClassVar[ViewConfigProto.CompressionType]
        kZSTD: _ClassVar[ViewConfigProto.CompressionType]
        kLZ4Compression: _ClassVar[ViewConfigProto.CompressionType]
        kNoCompression: _ClassVar[ViewConfigProto.CompressionType]
    kSnappyCompression: ViewConfigProto.CompressionType
    kZSTD: ViewConfigProto.CompressionType
    kLZ4Compression: ViewConfigProto.CompressionType
    kNoCompression: ViewConfigProto.CompressionType
    class HashingScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAvoidBucketZero: _ClassVar[ViewConfigProto.HashingScheme]
        kStdHash: _ClassVar[ViewConfigProto.HashingScheme]
        kForceBucketZero: _ClassVar[ViewConfigProto.HashingScheme]
        kCityHash: _ClassVar[ViewConfigProto.HashingScheme]
    kAvoidBucketZero: ViewConfigProto.HashingScheme
    kStdHash: ViewConfigProto.HashingScheme
    kForceBucketZero: ViewConfigProto.HashingScheme
    kCityHash: ViewConfigProto.HashingScheme
    class PlacementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHomogenous: _ClassVar[ViewConfigProto.PlacementMode]
        kHeterogenousPerformance: _ClassVar[ViewConfigProto.PlacementMode]
        kHeterogenousSpace: _ClassVar[ViewConfigProto.PlacementMode]
    kHomogenous: ViewConfigProto.PlacementMode
    kHeterogenousPerformance: ViewConfigProto.PlacementMode
    kHeterogenousSpace: ViewConfigProto.PlacementMode
    class Constituent(_message.Message):
        __slots__ = ("id", "node_id", "node_incarnation_id", "disk_id", "node_location", "fake_removed", "operational_status", "max_allowed_load", "avg_primary_replica_size_bytes", "max_capacity_bytes", "usable_capacity_bytes", "product_model", "avg_empty_replica_size_bytes", "max_non_empty_replicas_during_shuffle", "offline_reason_vec", "disk_usage_bytes", "usage_mode", "is_fault_tolerant", "shuffle_state", "perf_factor")
        class OperationalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kOperational: _ClassVar[ViewConfigProto.Constituent.OperationalStatus]
            kAddInProgress: _ClassVar[ViewConfigProto.Constituent.OperationalStatus]
            kGracefulRemoval: _ClassVar[ViewConfigProto.Constituent.OperationalStatus]
            kForceRemoval: _ClassVar[ViewConfigProto.Constituent.OperationalStatus]
            kOffline: _ClassVar[ViewConfigProto.Constituent.OperationalStatus]
        kOperational: ViewConfigProto.Constituent.OperationalStatus
        kAddInProgress: ViewConfigProto.Constituent.OperationalStatus
        kGracefulRemoval: ViewConfigProto.Constituent.OperationalStatus
        kForceRemoval: ViewConfigProto.Constituent.OperationalStatus
        kOffline: ViewConfigProto.Constituent.OperationalStatus
        class OfflineReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDiskOffline: _ClassVar[ViewConfigProto.Constituent.OfflineReason]
            kConstituentNotReachable: _ClassVar[ViewConfigProto.Constituent.OfflineReason]
            kConstituentIsFlaky: _ClassVar[ViewConfigProto.Constituent.OfflineReason]
        kDiskOffline: ViewConfigProto.Constituent.OfflineReason
        kConstituentNotReachable: ViewConfigProto.Constituent.OfflineReason
        kConstituentIsFlaky: ViewConfigProto.Constituent.OfflineReason
        class UsageMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSharedMode: _ClassVar[ViewConfigProto.Constituent.UsageMode]
            kExclusiveMode: _ClassVar[ViewConfigProto.Constituent.UsageMode]
            kSpaceOnlyMode: _ClassVar[ViewConfigProto.Constituent.UsageMode]
            kExclusiveUsedAsSharedMode: _ClassVar[ViewConfigProto.Constituent.UsageMode]
            kSpaceOnlyUsedAsSharedMode: _ClassVar[ViewConfigProto.Constituent.UsageMode]
        kSharedMode: ViewConfigProto.Constituent.UsageMode
        kExclusiveMode: ViewConfigProto.Constituent.UsageMode
        kSpaceOnlyMode: ViewConfigProto.Constituent.UsageMode
        kExclusiveUsedAsSharedMode: ViewConfigProto.Constituent.UsageMode
        kSpaceOnlyUsedAsSharedMode: ViewConfigProto.Constituent.UsageMode
        class NodeLocation(_message.Message):
            __slots__ = ("chassis_id", "rack_id")
            CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
            RACK_ID_FIELD_NUMBER: _ClassVar[int]
            chassis_id: int
            rack_id: int
            def __init__(self, chassis_id: _Optional[int] = ..., rack_id: _Optional[int] = ...) -> None: ...
        class ShuffleState(_message.Message):
            __slots__ = ("num_buckets_at_shuffle_start",)
            NUM_BUCKETS_AT_SHUFFLE_START_FIELD_NUMBER: _ClassVar[int]
            num_buckets_at_shuffle_start: int
            def __init__(self, num_buckets_at_shuffle_start: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        FAKE_REMOVED_FIELD_NUMBER: _ClassVar[int]
        OPERATIONAL_STATUS_FIELD_NUMBER: _ClassVar[int]
        MAX_ALLOWED_LOAD_FIELD_NUMBER: _ClassVar[int]
        AVG_PRIMARY_REPLICA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MAX_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        USABLE_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
        AVG_EMPTY_REPLICA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MAX_NON_EMPTY_REPLICAS_DURING_SHUFFLE_FIELD_NUMBER: _ClassVar[int]
        OFFLINE_REASON_VEC_FIELD_NUMBER: _ClassVar[int]
        DISK_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        USAGE_MODE_FIELD_NUMBER: _ClassVar[int]
        IS_FAULT_TOLERANT_FIELD_NUMBER: _ClassVar[int]
        SHUFFLE_STATE_FIELD_NUMBER: _ClassVar[int]
        PERF_FACTOR_FIELD_NUMBER: _ClassVar[int]
        id: int
        node_id: int
        node_incarnation_id: int
        disk_id: int
        node_location: ViewConfigProto.Constituent.NodeLocation
        fake_removed: bool
        operational_status: ViewConfigProto.Constituent.OperationalStatus
        max_allowed_load: int
        avg_primary_replica_size_bytes: int
        max_capacity_bytes: int
        usable_capacity_bytes: int
        product_model: _cluster_config_pb2.ClusterConfigProto.ProductModel
        avg_empty_replica_size_bytes: int
        max_non_empty_replicas_during_shuffle: int
        offline_reason_vec: _containers.RepeatedScalarFieldContainer[ViewConfigProto.Constituent.OfflineReason]
        disk_usage_bytes: int
        usage_mode: ViewConfigProto.Constituent.UsageMode
        is_fault_tolerant: bool
        shuffle_state: ViewConfigProto.Constituent.ShuffleState
        perf_factor: int
        def __init__(self, id: _Optional[int] = ..., node_id: _Optional[int] = ..., node_incarnation_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., node_location: _Optional[_Union[ViewConfigProto.Constituent.NodeLocation, _Mapping]] = ..., fake_removed: bool = ..., operational_status: _Optional[_Union[ViewConfigProto.Constituent.OperationalStatus, str]] = ..., max_allowed_load: _Optional[int] = ..., avg_primary_replica_size_bytes: _Optional[int] = ..., max_capacity_bytes: _Optional[int] = ..., usable_capacity_bytes: _Optional[int] = ..., product_model: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]] = ..., avg_empty_replica_size_bytes: _Optional[int] = ..., max_non_empty_replicas_during_shuffle: _Optional[int] = ..., offline_reason_vec: _Optional[_Iterable[_Union[ViewConfigProto.Constituent.OfflineReason, str]]] = ..., disk_usage_bytes: _Optional[int] = ..., usage_mode: _Optional[_Union[ViewConfigProto.Constituent.UsageMode, str]] = ..., is_fault_tolerant: bool = ..., shuffle_state: _Optional[_Union[ViewConfigProto.Constituent.ShuffleState, _Mapping]] = ..., perf_factor: _Optional[int] = ...) -> None: ...
    class Replica(_message.Message):
        __slots__ = ("constituent_id", "incarnation", "is_operational", "is_data_corrupted", "pending_compaction_after_migration")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_FIELD_NUMBER: _ClassVar[int]
        IS_OPERATIONAL_FIELD_NUMBER: _ClassVar[int]
        IS_DATA_CORRUPTED_FIELD_NUMBER: _ClassVar[int]
        PENDING_COMPACTION_AFTER_MIGRATION_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        incarnation: int
        is_operational: bool
        is_data_corrupted: bool
        pending_compaction_after_migration: bool
        def __init__(self, constituent_id: _Optional[int] = ..., incarnation: _Optional[int] = ..., is_operational: bool = ..., is_data_corrupted: bool = ..., pending_compaction_after_migration: bool = ...) -> None: ...
    class BucketOptions(_message.Message):
        __slots__ = ("use_dynamic_level_style_compaction", "num_compaction_levels", "table_metadata_version")
        USE_DYNAMIC_LEVEL_STYLE_COMPACTION_FIELD_NUMBER: _ClassVar[int]
        NUM_COMPACTION_LEVELS_FIELD_NUMBER: _ClassVar[int]
        TABLE_METADATA_VERSION_FIELD_NUMBER: _ClassVar[int]
        use_dynamic_level_style_compaction: bool
        num_compaction_levels: int
        table_metadata_version: int
        def __init__(self, use_dynamic_level_style_compaction: bool = ..., num_compaction_levels: _Optional[int] = ..., table_metadata_version: _Optional[int] = ...) -> None: ...
    class ViewRecord(_message.Message):
        __slots__ = ("bucket", "view_version", "current_view", "next_view", "target_view", "move_to_target_view", "num_migrations", "migration_schedule_index", "current_bucket_options", "migration_mode", "migration_stats", "desired_table_metadata_version")
        class MigrationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kRecordTransfer: _ClassVar[ViewConfigProto.ViewRecord.MigrationMode]
            kSstFileTransfer: _ClassVar[ViewConfigProto.ViewRecord.MigrationMode]
        kRecordTransfer: ViewConfigProto.ViewRecord.MigrationMode
        kSstFileTransfer: ViewConfigProto.ViewRecord.MigrationMode
        class MigrationStats(_message.Message):
            __slots__ = ("num_record_transfer_migrations", "num_sst_file_transfer_migrations", "num_sst_file_transfer_restarts")
            NUM_RECORD_TRANSFER_MIGRATIONS_FIELD_NUMBER: _ClassVar[int]
            NUM_SST_FILE_TRANSFER_MIGRATIONS_FIELD_NUMBER: _ClassVar[int]
            NUM_SST_FILE_TRANSFER_RESTARTS_FIELD_NUMBER: _ClassVar[int]
            num_record_transfer_migrations: int
            num_sst_file_transfer_migrations: int
            num_sst_file_transfer_restarts: int
            def __init__(self, num_record_transfer_migrations: _Optional[int] = ..., num_sst_file_transfer_migrations: _Optional[int] = ..., num_sst_file_transfer_restarts: _Optional[int] = ...) -> None: ...
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
        CURRENT_VIEW_FIELD_NUMBER: _ClassVar[int]
        NEXT_VIEW_FIELD_NUMBER: _ClassVar[int]
        TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
        MOVE_TO_TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
        NUM_MIGRATIONS_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_SCHEDULE_INDEX_FIELD_NUMBER: _ClassVar[int]
        CURRENT_BUCKET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_MODE_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_STATS_FIELD_NUMBER: _ClassVar[int]
        DESIRED_TABLE_METADATA_VERSION_FIELD_NUMBER: _ClassVar[int]
        bucket: int
        view_version: int
        current_view: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Replica]
        next_view: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Replica]
        target_view: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Replica]
        move_to_target_view: bool
        num_migrations: int
        migration_schedule_index: int
        current_bucket_options: ViewConfigProto.BucketOptions
        migration_mode: ViewConfigProto.ViewRecord.MigrationMode
        migration_stats: ViewConfigProto.ViewRecord.MigrationStats
        desired_table_metadata_version: int
        def __init__(self, bucket: _Optional[int] = ..., view_version: _Optional[int] = ..., current_view: _Optional[_Iterable[_Union[ViewConfigProto.Replica, _Mapping]]] = ..., next_view: _Optional[_Iterable[_Union[ViewConfigProto.Replica, _Mapping]]] = ..., target_view: _Optional[_Iterable[_Union[ViewConfigProto.Replica, _Mapping]]] = ..., move_to_target_view: bool = ..., num_migrations: _Optional[int] = ..., migration_schedule_index: _Optional[int] = ..., current_bucket_options: _Optional[_Union[ViewConfigProto.BucketOptions, _Mapping]] = ..., migration_mode: _Optional[_Union[ViewConfigProto.ViewRecord.MigrationMode, str]] = ..., migration_stats: _Optional[_Union[ViewConfigProto.ViewRecord.MigrationStats, _Mapping]] = ..., desired_table_metadata_version: _Optional[int] = ...) -> None: ...
    class ClusterSetting(_message.Message):
        __slots__ = ("fault_tolerance", "replication_factor", "replication_factor_at_fake_rf_switch_start", "encryption_enabled", "encryption_block_size", "disaggregated_metadata_disk_enabled")
        FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_FACTOR_AT_FAKE_RF_SWITCH_START_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        DISAGGREGATED_METADATA_DISK_ENABLED_FIELD_NUMBER: _ClassVar[int]
        fault_tolerance: _cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness
        replication_factor: int
        replication_factor_at_fake_rf_switch_start: int
        encryption_enabled: bool
        encryption_block_size: int
        disaggregated_metadata_disk_enabled: bool
        def __init__(self, fault_tolerance: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness, _Mapping]] = ..., replication_factor: _Optional[int] = ..., replication_factor_at_fake_rf_switch_start: _Optional[int] = ..., encryption_enabled: bool = ..., encryption_block_size: _Optional[int] = ..., disaggregated_metadata_disk_enabled: bool = ...) -> None: ...
    class Ring(_message.Message):
        __slots__ = ("members", "ring_base_size_bytes", "capacity_scale_percent", "num_buckets", "standby_constituents_present", "total_standby_constituents", "total_space_only_mode_constituents")
        class ConstituentDomainPair(_message.Message):
            __slots__ = ("constituent_id", "domain_id", "max_capacity_bytes", "product_model", "is_operational")
            CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
            DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
            MAX_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
            PRODUCT_MODEL_FIELD_NUMBER: _ClassVar[int]
            IS_OPERATIONAL_FIELD_NUMBER: _ClassVar[int]
            constituent_id: int
            domain_id: int
            max_capacity_bytes: int
            product_model: _cluster_config_pb2.ClusterConfigProto.ProductModel
            is_operational: bool
            def __init__(self, constituent_id: _Optional[int] = ..., domain_id: _Optional[int] = ..., max_capacity_bytes: _Optional[int] = ..., product_model: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ProductModel, str]] = ..., is_operational: bool = ...) -> None: ...
        MEMBERS_FIELD_NUMBER: _ClassVar[int]
        RING_BASE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_SCALE_PERCENT_FIELD_NUMBER: _ClassVar[int]
        NUM_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        STANDBY_CONSTITUENTS_PRESENT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_STANDBY_CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SPACE_ONLY_MODE_CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
        members: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Ring.ConstituentDomainPair]
        ring_base_size_bytes: int
        capacity_scale_percent: int
        num_buckets: int
        standby_constituents_present: bool
        total_standby_constituents: int
        total_space_only_mode_constituents: int
        def __init__(self, members: _Optional[_Iterable[_Union[ViewConfigProto.Ring.ConstituentDomainPair, _Mapping]]] = ..., ring_base_size_bytes: _Optional[int] = ..., capacity_scale_percent: _Optional[int] = ..., num_buckets: _Optional[int] = ..., standby_constituents_present: bool = ..., total_standby_constituents: _Optional[int] = ..., total_space_only_mode_constituents: _Optional[int] = ...) -> None: ...
    class DesiredSetting(_message.Message):
        __slots__ = ("placement_mode", "fake_bucket_placement_mode_switch_in_progress", "compression_type", "last_test_compression_change_time_usecs")
        PLACEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
        FAKE_BUCKET_PLACEMENT_MODE_SWITCH_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
        LAST_TEST_COMPRESSION_CHANGE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        placement_mode: ViewConfigProto.PlacementMode
        fake_bucket_placement_mode_switch_in_progress: bool
        compression_type: ViewConfigProto.CompressionType
        last_test_compression_change_time_usecs: int
        def __init__(self, placement_mode: _Optional[_Union[ViewConfigProto.PlacementMode, str]] = ..., fake_bucket_placement_mode_switch_in_progress: bool = ..., compression_type: _Optional[_Union[ViewConfigProto.CompressionType, str]] = ..., last_test_compression_change_time_usecs: _Optional[int] = ...) -> None: ...
    CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    LAST_SHUFFLE_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_SHUFFLE_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PAXOS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    HASHING_SCHEME_FIELD_NUMBER: _ClassVar[int]
    USE_MULTIPLE_DISKS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    IS_HEALING_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SETTING_FIELD_NUMBER: _ClassVar[int]
    NUM_HOSTING_CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BUCKET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_GRACEFUL_REMOVAL_CONSTITUENT_FIELD_NUMBER: _ClassVar[int]
    RINGS_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SETTING_FIELD_NUMBER: _ClassVar[int]
    SHADOW_RINGS_FIELD_NUMBER: _ClassVar[int]
    SPACE_ONLY_MODE_CONSTITUENTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOW_MEM_USAGE_SETTING_TABLET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_SSD_ROTATION_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_SSD_ROTATION_FINISH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CAPTURING_ROW_HISTORY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ALLOW_COHESITY_WAL_FIELD_NUMBER: _ClassVar[int]
    constituents: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Constituent]
    views: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.ViewRecord]
    last_shuffle_start_time_usecs: int
    last_shuffle_end_time_usecs: int
    paxos_disabled: bool
    hashing_scheme: ViewConfigProto.HashingScheme
    use_multiple_disks_per_node: bool
    is_healing: bool
    cluster_setting: ViewConfigProto.ClusterSetting
    num_hosting_constituents: int
    desired_bucket_options: ViewConfigProto.BucketOptions
    cleanup_graceful_removal_constituent: bool
    rings: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Ring]
    placement_mode: ViewConfigProto.PlacementMode
    desired_setting: ViewConfigProto.DesiredSetting
    shadow_rings: _containers.RepeatedCompositeFieldContainer[ViewConfigProto.Ring]
    space_only_mode_constituents_enabled: bool
    low_mem_usage_setting_tablet_enabled: bool
    last_ssd_rotation_start_time_usecs: int
    last_ssd_rotation_finish_time_usecs: int
    current_fault_tolerance: _cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness
    capturing_row_history_enabled: bool
    scribe_allow_cohesity_wal: bool
    def __init__(self, constituents: _Optional[_Iterable[_Union[ViewConfigProto.Constituent, _Mapping]]] = ..., views: _Optional[_Iterable[_Union[ViewConfigProto.ViewRecord, _Mapping]]] = ..., last_shuffle_start_time_usecs: _Optional[int] = ..., last_shuffle_end_time_usecs: _Optional[int] = ..., paxos_disabled: bool = ..., hashing_scheme: _Optional[_Union[ViewConfigProto.HashingScheme, str]] = ..., use_multiple_disks_per_node: bool = ..., is_healing: bool = ..., cluster_setting: _Optional[_Union[ViewConfigProto.ClusterSetting, _Mapping]] = ..., num_hosting_constituents: _Optional[int] = ..., desired_bucket_options: _Optional[_Union[ViewConfigProto.BucketOptions, _Mapping]] = ..., cleanup_graceful_removal_constituent: bool = ..., rings: _Optional[_Iterable[_Union[ViewConfigProto.Ring, _Mapping]]] = ..., placement_mode: _Optional[_Union[ViewConfigProto.PlacementMode, str]] = ..., desired_setting: _Optional[_Union[ViewConfigProto.DesiredSetting, _Mapping]] = ..., shadow_rings: _Optional[_Iterable[_Union[ViewConfigProto.Ring, _Mapping]]] = ..., space_only_mode_constituents_enabled: bool = ..., low_mem_usage_setting_tablet_enabled: bool = ..., last_ssd_rotation_start_time_usecs: _Optional[int] = ..., last_ssd_rotation_finish_time_usecs: _Optional[int] = ..., current_fault_tolerance: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness, _Mapping]] = ..., capturing_row_history_enabled: bool = ..., scribe_allow_cohesity_wal: bool = ...) -> None: ...
