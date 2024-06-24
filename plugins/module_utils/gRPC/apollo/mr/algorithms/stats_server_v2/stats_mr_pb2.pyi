from configs import cluster_config_pb2 as _cluster_config_pb2
from stats.base import alert_policies_pb2 as _alert_policies_pb2
from stats.base import entity_schema_pb2 as _entity_schema_pb2
from stats.base import stats_pb2 as _stats_pb2
from stats.newserver.base import stats_internal_pb2 as _stats_internal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RollupWindow(_message.Message):
    __slots__ = ("start_timestamp_msecs", "time_interval_msecs")
    START_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_MSECS_FIELD_NUMBER: _ClassVar[int]
    start_timestamp_msecs: int
    time_interval_msecs: int
    def __init__(self, start_timestamp_msecs: _Optional[int] = ..., time_interval_msecs: _Optional[int] = ...) -> None: ...

class StatsKeyProto(_message.Message):
    __slots__ = ("schema", "entity_id", "metric", "aggregation_timestamp_msecs", "is_source_entity", "rollup_window", "pipeline")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    schema: str
    entity_id: str
    metric: str
    aggregation_timestamp_msecs: int
    is_source_entity: bool
    rollup_window: RollupWindow
    pipeline: str
    def __init__(self, schema: _Optional[str] = ..., entity_id: _Optional[str] = ..., metric: _Optional[str] = ..., aggregation_timestamp_msecs: _Optional[int] = ..., is_source_entity: bool = ..., rollup_window: _Optional[_Union[RollupWindow, _Mapping]] = ..., pipeline: _Optional[str] = ...) -> None: ...

class StatsEntityMetadataValueProto(_message.Message):
    __slots__ = ("scribe_row_key", "scribe_row_version", "entity_metadata")
    SCRIBE_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    scribe_row_key: str
    scribe_row_version: int
    entity_metadata: _stats_internal_pb2.EntityMetaDataProto
    def __init__(self, scribe_row_key: _Optional[str] = ..., scribe_row_version: _Optional[int] = ..., entity_metadata: _Optional[_Union[_stats_internal_pb2.EntityMetaDataProto, _Mapping]] = ...) -> None: ...

class StatsAggregatorValueProto(_message.Message):
    __slots__ = ("entity_metric_key", "metric_value", "aggregation_table_row_key", "row_key_timestamp", "scribe_row_key_version", "is_aggregated_entity")
    ENTITY_METRIC_KEY_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_TABLE_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_AGGREGATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity_metric_key: StatsKeyProto
    metric_value: _containers.RepeatedCompositeFieldContainer[_stats_pb2.MetricDataBlock]
    aggregation_table_row_key: str
    row_key_timestamp: int
    scribe_row_key_version: int
    is_aggregated_entity: bool
    def __init__(self, entity_metric_key: _Optional[_Union[StatsKeyProto, _Mapping]] = ..., metric_value: _Optional[_Iterable[_Union[_stats_pb2.MetricDataBlock, _Mapping]]] = ..., aggregation_table_row_key: _Optional[str] = ..., row_key_timestamp: _Optional[int] = ..., scribe_row_key_version: _Optional[int] = ..., is_aggregated_entity: bool = ...) -> None: ...

class SchemaProto(_message.Message):
    __slots__ = ("ts_map", "scribe_proto", "dag_level", "is_source_schema")
    class TsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor, _Mapping]] = ...) -> None: ...
    TS_MAP_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_PROTO_FIELD_NUMBER: _ClassVar[int]
    DAG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ts_map: _containers.MessageMap[str, _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor]
    scribe_proto: _stats_internal_pb2.ScribeEntitySchemaProto
    dag_level: int
    is_source_schema: bool
    def __init__(self, ts_map: _Optional[_Mapping[str, _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor]] = ..., scribe_proto: _Optional[_Union[_stats_internal_pb2.ScribeEntitySchemaProto, _Mapping]] = ..., dag_level: _Optional[int] = ..., is_source_schema: bool = ...) -> None: ...

class StatsAggregationContextProto(_message.Message):
    __slots__ = ("cluster_config_proto", "schema_map", "last_aggregation_end_time_msecs", "current_time_msecs", "num_dag_levels", "stats_state_gandalf_version", "policy_registry", "trace_key", "schema_alert_policy_duration")
    class SchemaMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SchemaProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SchemaProto, _Mapping]] = ...) -> None: ...
    class SchemaAlertPolicyDurationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_MAP_FIELD_NUMBER: _ClassVar[int]
    LAST_AGGREGATION_END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    NUM_DAG_LEVELS_FIELD_NUMBER: _ClassVar[int]
    STATS_STATE_GANDALF_VERSION_FIELD_NUMBER: _ClassVar[int]
    POLICY_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    TRACE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_ALERT_POLICY_DURATION_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    schema_map: _containers.MessageMap[str, SchemaProto]
    last_aggregation_end_time_msecs: int
    current_time_msecs: int
    num_dag_levels: int
    stats_state_gandalf_version: int
    policy_registry: _alert_policies_pb2.AlertPoliciesProto
    trace_key: StatsKeyProto
    schema_alert_policy_duration: _containers.ScalarMap[str, int]
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., schema_map: _Optional[_Mapping[str, SchemaProto]] = ..., last_aggregation_end_time_msecs: _Optional[int] = ..., current_time_msecs: _Optional[int] = ..., num_dag_levels: _Optional[int] = ..., stats_state_gandalf_version: _Optional[int] = ..., policy_registry: _Optional[_Union[_alert_policies_pb2.AlertPoliciesProto, _Mapping]] = ..., trace_key: _Optional[_Union[StatsKeyProto, _Mapping]] = ..., schema_alert_policy_duration: _Optional[_Mapping[str, int]] = ...) -> None: ...

class StatsRollupGarbageCollectionValueProto(_message.Message):
    __slots__ = ("scribe_row_key", "scribe_row_version", "timestamp", "marked_for_deletion", "metric_data", "metric_data_map", "counter", "container")
    class MetricDataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stats_internal_pb2.TimeSeriesDataBlockProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stats_internal_pb2.TimeSeriesDataBlockProto, _Mapping]] = ...) -> None: ...
    SCRIBE_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    METRIC_DATA_FIELD_NUMBER: _ClassVar[int]
    METRIC_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    scribe_row_key: str
    scribe_row_version: int
    timestamp: int
    marked_for_deletion: bool
    metric_data: _stats_internal_pb2.TimeSeriesDataBlockProto
    metric_data_map: _containers.MessageMap[int, _stats_internal_pb2.TimeSeriesDataBlockProto]
    counter: _stats_internal_pb2.CounterProto
    container: _stats_internal_pb2.StatsContainerProto
    def __init__(self, scribe_row_key: _Optional[str] = ..., scribe_row_version: _Optional[int] = ..., timestamp: _Optional[int] = ..., marked_for_deletion: bool = ..., metric_data: _Optional[_Union[_stats_internal_pb2.TimeSeriesDataBlockProto, _Mapping]] = ..., metric_data_map: _Optional[_Mapping[int, _stats_internal_pb2.TimeSeriesDataBlockProto]] = ..., counter: _Optional[_Union[_stats_internal_pb2.CounterProto, _Mapping]] = ..., container: _Optional[_Union[_stats_internal_pb2.StatsContainerProto, _Mapping]] = ...) -> None: ...

class StatsRolledUpMetricValueProto(_message.Message):
    __slots__ = ("metric_name", "metric_data", "rolledup_scribe_rows")
    class ScribeRow(_message.Message):
        __slots__ = ("scribe_row_key", "scribe_row_version")
        SCRIBE_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
        scribe_row_key: str
        scribe_row_version: int
        def __init__(self, scribe_row_key: _Optional[str] = ..., scribe_row_version: _Optional[int] = ...) -> None: ...
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_DATA_FIELD_NUMBER: _ClassVar[int]
    ROLLEDUP_SCRIBE_ROWS_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    metric_data: _stats_internal_pb2.TimeSeriesDataBlockProto
    rolledup_scribe_rows: _containers.RepeatedCompositeFieldContainer[StatsRolledUpMetricValueProto.ScribeRow]
    def __init__(self, metric_name: _Optional[str] = ..., metric_data: _Optional[_Union[_stats_internal_pb2.TimeSeriesDataBlockProto, _Mapping]] = ..., rolledup_scribe_rows: _Optional[_Iterable[_Union[StatsRolledUpMetricValueProto.ScribeRow, _Mapping]]] = ...) -> None: ...

class StatsRollupGarbageCollectionContextProto(_message.Message):
    __slots__ = ("cluster_config_proto", "start_timestamp_msecs", "schema_info_map", "global_rollup_granularity", "trace_key")
    class SchemaInfo(_message.Message):
        __slots__ = ("time_to_live_msecs", "schema_proto")
        TIME_TO_LIVE_MSECS_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_PROTO_FIELD_NUMBER: _ClassVar[int]
        time_to_live_msecs: int
        schema_proto: SchemaProto
        def __init__(self, time_to_live_msecs: _Optional[int] = ..., schema_proto: _Optional[_Union[SchemaProto, _Mapping]] = ...) -> None: ...
    class SchemaInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StatsRollupGarbageCollectionContextProto.SchemaInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StatsRollupGarbageCollectionContextProto.SchemaInfo, _Mapping]] = ...) -> None: ...
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ROLLUP_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    TRACE_KEY_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    start_timestamp_msecs: int
    schema_info_map: _containers.MessageMap[str, StatsRollupGarbageCollectionContextProto.SchemaInfo]
    global_rollup_granularity: _stats_internal_pb2.RollupGranularityProto
    trace_key: StatsKeyProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ..., start_timestamp_msecs: _Optional[int] = ..., schema_info_map: _Optional[_Mapping[str, StatsRollupGarbageCollectionContextProto.SchemaInfo]] = ..., global_rollup_granularity: _Optional[_Union[_stats_internal_pb2.RollupGranularityProto, _Mapping]] = ..., trace_key: _Optional[_Union[StatsKeyProto, _Mapping]] = ...) -> None: ...
