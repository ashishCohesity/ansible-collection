from stats.base import alert_policies_pb2 as _alert_policies_pb2
from stats.base import entity_schema_pb2 as _entity_schema_pb2
from stats.base import stats_pb2 as _stats_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RollupIdentifier(_message.Message):
    __slots__ = ("rollup_func", "rollup_interval_secs")
    ROLLUP_FUNC_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    rollup_func: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction
    rollup_interval_secs: int
    def __init__(self, rollup_func: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]] = ..., rollup_interval_secs: _Optional[int] = ...) -> None: ...

class TimeSeriesDataBlockProto(_message.Message):
    __slots__ = ("type", "data_point_vec")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    type: _stats_types_pb2.Value.Type
    data_point_vec: _containers.RepeatedCompositeFieldContainer[_stats_pb2.MetricDataPoint]
    def __init__(self, type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ..., data_point_vec: _Optional[_Iterable[_Union[_stats_pb2.MetricDataPoint, _Mapping]]] = ...) -> None: ...

class TimeSeriesMetaDataProto(_message.Message):
    __slots__ = ("entity_id", "metric_name", "rollup_id", "data_block_location_vec")
    class DataBlockLocation(_message.Message):
        __slots__ = ("start_time_msecs", "scribe_row_id")
        START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_ID_FIELD_NUMBER: _ClassVar[int]
        start_time_msecs: int
        scribe_row_id: int
        def __init__(self, start_time_msecs: _Optional[int] = ..., scribe_row_id: _Optional[int] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_BLOCK_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: _stats_pb2.EntityIdentifier
    metric_name: str
    rollup_id: RollupIdentifier
    data_block_location_vec: _containers.RepeatedCompositeFieldContainer[TimeSeriesMetaDataProto.DataBlockLocation]
    def __init__(self, entity_id: _Optional[_Union[_stats_pb2.EntityIdentifier, _Mapping]] = ..., metric_name: _Optional[str] = ..., rollup_id: _Optional[_Union[RollupIdentifier, _Mapping]] = ..., data_block_location_vec: _Optional[_Iterable[_Union[TimeSeriesMetaDataProto.DataBlockLocation, _Mapping]]] = ...) -> None: ...

class OldStatsContainerProto(_message.Message):
    __slots__ = ("id", "counter_id_vec", "expiry_time_usecs", "removed")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    id: int
    counter_id_vec: _containers.RepeatedCompositeFieldContainer[_stats_pb2.CounterIdentifier]
    expiry_time_usecs: int
    removed: bool
    def __init__(self, id: _Optional[int] = ..., counter_id_vec: _Optional[_Iterable[_Union[_stats_pb2.CounterIdentifier, _Mapping]]] = ..., expiry_time_usecs: _Optional[int] = ..., removed: bool = ...) -> None: ...

class CounterProto(_message.Message):
    __slots__ = ("id", "value", "create_time_series", "removed", "timeseries_spec")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    TIMESERIES_SPEC_FIELD_NUMBER: _ClassVar[int]
    id: _stats_pb2.CounterIdentifier
    value: int
    create_time_series: bool
    removed: bool
    timeseries_spec: _stats_pb2.CounterTimeseriesSpec
    def __init__(self, id: _Optional[_Union[_stats_pb2.CounterIdentifier, _Mapping]] = ..., value: _Optional[int] = ..., create_time_series: bool = ..., removed: bool = ..., timeseries_spec: _Optional[_Union[_stats_pb2.CounterTimeseriesSpec, _Mapping]] = ...) -> None: ...

class RemovalState(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDontRemove: _ClassVar[RemovalState.Status]
        kMarkedForRemoval: _ClassVar[RemovalState.Status]
        kOkToRemove: _ClassVar[RemovalState.Status]
    kDontRemove: RemovalState.Status
    kMarkedForRemoval: RemovalState.Status
    kOkToRemove: RemovalState.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: RemovalState.Status
    def __init__(self, status: _Optional[_Union[RemovalState.Status, str]] = ...) -> None: ...

class MigrationState(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMigrationNotStarted: _ClassVar[MigrationState.Status]
        kMigrationInProgress: _ClassVar[MigrationState.Status]
        kMigrationCompleted: _ClassVar[MigrationState.Status]
    kMigrationNotStarted: MigrationState.Status
    kMigrationInProgress: MigrationState.Status
    kMigrationCompleted: MigrationState.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: MigrationState.Status
    def __init__(self, status: _Optional[_Union[MigrationState.Status, str]] = ...) -> None: ...

class NewStatsMigrationState(_message.Message):
    __slots__ = ("migration_start_time_msecs", "entity_migrate_last_schema", "entity_migrate_last_id", "counter_migrate_last_id", "container_migrate_last_id", "num_schemas_migrated", "num_entities_migrated", "num_counters_migrated", "num_containers_migrated", "counters_pending_migration", "containers_pending_migration", "schemas_pending_migration", "migration_stage", "migration_blackout_window", "entities_pending_migration")
    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[NewStatsMigrationState.Stage]
        kSchema: _ClassVar[NewStatsMigrationState.Stage]
        kEntity: _ClassVar[NewStatsMigrationState.Stage]
        kCounter: _ClassVar[NewStatsMigrationState.Stage]
        kContainer: _ClassVar[NewStatsMigrationState.Stage]
        kMigrationDone: _ClassVar[NewStatsMigrationState.Stage]
    kNone: NewStatsMigrationState.Stage
    kSchema: NewStatsMigrationState.Stage
    kEntity: NewStatsMigrationState.Stage
    kCounter: NewStatsMigrationState.Stage
    kContainer: NewStatsMigrationState.Stage
    kMigrationDone: NewStatsMigrationState.Stage
    MIGRATION_START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MIGRATE_LAST_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MIGRATE_LAST_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_MIGRATE_LAST_ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_MIGRATE_LAST_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_SCHEMAS_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTITIES_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    NUM_COUNTERS_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    NUM_CONTAINERS_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_PENDING_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_PENDING_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_PENDING_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_STAGE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_BLACKOUT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_PENDING_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    migration_start_time_msecs: int
    entity_migrate_last_schema: str
    entity_migrate_last_id: _stats_types_pb2.Value
    counter_migrate_last_id: _stats_pb2.CounterIdentifier
    container_migrate_last_id: int
    num_schemas_migrated: int
    num_entities_migrated: int
    num_counters_migrated: int
    num_containers_migrated: int
    counters_pending_migration: _containers.RepeatedCompositeFieldContainer[_stats_pb2.CounterIdentifier]
    containers_pending_migration: _containers.RepeatedScalarFieldContainer[int]
    schemas_pending_migration: bool
    migration_stage: NewStatsMigrationState.Stage
    migration_blackout_window: bool
    entities_pending_migration: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, migration_start_time_msecs: _Optional[int] = ..., entity_migrate_last_schema: _Optional[str] = ..., entity_migrate_last_id: _Optional[_Union[_stats_types_pb2.Value, _Mapping]] = ..., counter_migrate_last_id: _Optional[_Union[_stats_pb2.CounterIdentifier, _Mapping]] = ..., container_migrate_last_id: _Optional[int] = ..., num_schemas_migrated: _Optional[int] = ..., num_entities_migrated: _Optional[int] = ..., num_counters_migrated: _Optional[int] = ..., num_containers_migrated: _Optional[int] = ..., counters_pending_migration: _Optional[_Iterable[_Union[_stats_pb2.CounterIdentifier, _Mapping]]] = ..., containers_pending_migration: _Optional[_Iterable[int]] = ..., schemas_pending_migration: bool = ..., migration_stage: _Optional[_Union[NewStatsMigrationState.Stage, str]] = ..., migration_blackout_window: bool = ..., entities_pending_migration: _Optional[_Iterable[str]] = ...) -> None: ...

class StaleEntitiesState(_message.Message):
    __slots__ = ("delete_stale_entities_gflag",)
    DELETE_STALE_ENTITIES_GFLAG_FIELD_NUMBER: _ClassVar[int]
    delete_stale_entities_gflag: bool
    def __init__(self, delete_stale_entities_gflag: bool = ...) -> None: ...

class PersistentStateProto(_message.Message):
    __slots__ = ("schema_vec", "entity_data_vec", "stats_container_vec", "counter_vec", "alert_policies", "record_persist_time_usecs", "counters_containers_migration_state", "newstats_migration_state", "stale_entities_state")
    class EntityData(_message.Message):
        __slots__ = ("entity_id", "entity_arg", "removal_state", "metric_meta_data_vec")
        class MetricMetaDataProto(_message.Message):
            __slots__ = ("metric_name", "rollup_id", "scribe_row_id")
            METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
            ROLLUP_ID_FIELD_NUMBER: _ClassVar[int]
            SCRIBE_ROW_ID_FIELD_NUMBER: _ClassVar[int]
            metric_name: str
            rollup_id: RollupIdentifier
            scribe_row_id: int
            def __init__(self, metric_name: _Optional[str] = ..., rollup_id: _Optional[_Union[RollupIdentifier, _Mapping]] = ..., scribe_row_id: _Optional[int] = ...) -> None: ...
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
        REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
        METRIC_META_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_id: _stats_pb2.EntityIdentifier
        entity_arg: _stats_pb2.AddOrUpdateEntityArg
        removal_state: RemovalState
        metric_meta_data_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.EntityData.MetricMetaDataProto]
        def __init__(self, entity_id: _Optional[_Union[_stats_pb2.EntityIdentifier, _Mapping]] = ..., entity_arg: _Optional[_Union[_stats_pb2.AddOrUpdateEntityArg, _Mapping]] = ..., removal_state: _Optional[_Union[RemovalState, _Mapping]] = ..., metric_meta_data_vec: _Optional[_Iterable[_Union[PersistentStateProto.EntityData.MetricMetaDataProto, _Mapping]]] = ...) -> None: ...
    SCHEMA_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_VEC_FIELD_NUMBER: _ClassVar[int]
    COUNTER_VEC_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICIES_FIELD_NUMBER: _ClassVar[int]
    RECORD_PERSIST_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_CONTAINERS_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    NEWSTATS_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    STALE_ENTITIES_STATE_FIELD_NUMBER: _ClassVar[int]
    schema_vec: _containers.RepeatedCompositeFieldContainer[_entity_schema_pb2.EntitySchemaProto]
    entity_data_vec: _containers.RepeatedCompositeFieldContainer[PersistentStateProto.EntityData]
    stats_container_vec: _containers.RepeatedCompositeFieldContainer[OldStatsContainerProto]
    counter_vec: _containers.RepeatedCompositeFieldContainer[CounterProto]
    alert_policies: _alert_policies_pb2.AlertPoliciesProto
    record_persist_time_usecs: int
    counters_containers_migration_state: MigrationState
    newstats_migration_state: NewStatsMigrationState
    stale_entities_state: StaleEntitiesState
    def __init__(self, schema_vec: _Optional[_Iterable[_Union[_entity_schema_pb2.EntitySchemaProto, _Mapping]]] = ..., entity_data_vec: _Optional[_Iterable[_Union[PersistentStateProto.EntityData, _Mapping]]] = ..., stats_container_vec: _Optional[_Iterable[_Union[OldStatsContainerProto, _Mapping]]] = ..., counter_vec: _Optional[_Iterable[_Union[CounterProto, _Mapping]]] = ..., alert_policies: _Optional[_Union[_alert_policies_pb2.AlertPoliciesProto, _Mapping]] = ..., record_persist_time_usecs: _Optional[int] = ..., counters_containers_migration_state: _Optional[_Union[MigrationState, _Mapping]] = ..., newstats_migration_state: _Optional[_Union[NewStatsMigrationState, _Mapping]] = ..., stale_entities_state: _Optional[_Union[StaleEntitiesState, _Mapping]] = ...) -> None: ...
