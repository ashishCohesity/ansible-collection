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

class ScribeEntitySchemaProto(_message.Message):
    __slots__ = ("proto", "old_schema_hash", "metric_id_map")
    class MetricIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    PROTO_FIELD_NUMBER: _ClassVar[int]
    OLD_SCHEMA_HASH_FIELD_NUMBER: _ClassVar[int]
    METRIC_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    proto: _entity_schema_pb2.EntitySchemaProto
    old_schema_hash: str
    metric_id_map: _containers.ScalarMap[str, int]
    def __init__(self, proto: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto, _Mapping]] = ..., old_schema_hash: _Optional[str] = ..., metric_id_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EntityMetaDataProto(_message.Message):
    __slots__ = ("schema_name", "meta", "old_metric_meta_vec", "marked_for_deletion", "created_timestamp_msecs", "last_published_timestamp_msecs")
    class StatsV1MetricMetaDataProto(_message.Message):
        __slots__ = ("metric_name", "rollup_id", "scribe_row_id")
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        ROLLUP_ID_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_ID_FIELD_NUMBER: _ClassVar[int]
        metric_name: str
        rollup_id: RollupIdentifier
        scribe_row_id: int
        def __init__(self, metric_name: _Optional[str] = ..., rollup_id: _Optional[_Union[RollupIdentifier, _Mapping]] = ..., scribe_row_id: _Optional[int] = ...) -> None: ...
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    OLD_METRIC_META_VEC_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_DELETION_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_PUBLISHED_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    meta: _stats_pb2.EntityProto
    old_metric_meta_vec: _containers.RepeatedCompositeFieldContainer[EntityMetaDataProto.StatsV1MetricMetaDataProto]
    marked_for_deletion: bool
    created_timestamp_msecs: int
    last_published_timestamp_msecs: int
    def __init__(self, schema_name: _Optional[str] = ..., meta: _Optional[_Union[_stats_pb2.EntityProto, _Mapping]] = ..., old_metric_meta_vec: _Optional[_Iterable[_Union[EntityMetaDataProto.StatsV1MetricMetaDataProto, _Mapping]]] = ..., marked_for_deletion: bool = ..., created_timestamp_msecs: _Optional[int] = ..., last_published_timestamp_msecs: _Optional[int] = ...) -> None: ...

class StatsContainerProto(_message.Message):
    __slots__ = ("id", "counter_id_vec", "removed", "expiry_time_secs")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    id: int
    counter_id_vec: _containers.RepeatedCompositeFieldContainer[_stats_pb2.CounterIdentifier]
    removed: bool
    expiry_time_secs: int
    def __init__(self, id: _Optional[int] = ..., counter_id_vec: _Optional[_Iterable[_Union[_stats_pb2.CounterIdentifier, _Mapping]]] = ..., removed: bool = ..., expiry_time_secs: _Optional[int] = ...) -> None: ...

class CounterProto(_message.Message):
    __slots__ = ("id", "value", "create_time_series", "removed", "expiry_time_secs", "timeseries_spec", "last_flushed_secs")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    TIMESERIES_SPEC_FIELD_NUMBER: _ClassVar[int]
    LAST_FLUSHED_SECS_FIELD_NUMBER: _ClassVar[int]
    id: _stats_pb2.CounterIdentifier
    value: int
    create_time_series: bool
    removed: bool
    expiry_time_secs: int
    timeseries_spec: _stats_pb2.CounterTimeseriesSpec
    last_flushed_secs: int
    def __init__(self, id: _Optional[_Union[_stats_pb2.CounterIdentifier, _Mapping]] = ..., value: _Optional[int] = ..., create_time_series: bool = ..., removed: bool = ..., expiry_time_secs: _Optional[int] = ..., timeseries_spec: _Optional[_Union[_stats_pb2.CounterTimeseriesSpec, _Mapping]] = ..., last_flushed_secs: _Optional[int] = ...) -> None: ...

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

class AlertPoliciesChangeState(_message.Message):
    __slots__ = ("timestamp_msecs", "server_node_id")
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    SERVER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    timestamp_msecs: int
    server_node_id: int
    def __init__(self, timestamp_msecs: _Optional[int] = ..., server_node_id: _Optional[int] = ...) -> None: ...

class AggregationStateProto(_message.Message):
    __slots__ = ("schema_dag", "last_schema_index")
    SCHEMA_DAG_FIELD_NUMBER: _ClassVar[int]
    LAST_SCHEMA_INDEX_FIELD_NUMBER: _ClassVar[int]
    schema_dag: _containers.RepeatedScalarFieldContainer[str]
    last_schema_index: int
    def __init__(self, schema_dag: _Optional[_Iterable[str]] = ..., last_schema_index: _Optional[int] = ...) -> None: ...

class AggregationTimeSeriesProto(_message.Message):
    __slots__ = ("rolledup_metric_vec", "is_aggregated_entity")
    ROLLEDUP_METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_AGGREGATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    rolledup_metric_vec: _containers.RepeatedCompositeFieldContainer[_stats_pb2.MetricDataBlock]
    is_aggregated_entity: bool
    def __init__(self, rolledup_metric_vec: _Optional[_Iterable[_Union[_stats_pb2.MetricDataBlock, _Mapping]]] = ..., is_aggregated_entity: bool = ...) -> None: ...

class StatsStateProto(_message.Message):
    __slots__ = ("last_aggregation_end_time_msecs", "current_time_msecs")
    LAST_AGGREGATION_END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    last_aggregation_end_time_msecs: int
    current_time_msecs: int
    def __init__(self, last_aggregation_end_time_msecs: _Optional[int] = ..., current_time_msecs: _Optional[int] = ...) -> None: ...

class RollupGranularityProto(_message.Message):
    __slots__ = ("granularity_vec",)
    GRANULARITY_VEC_FIELD_NUMBER: _ClassVar[int]
    granularity_vec: _containers.RepeatedCompositeFieldContainer[_entity_schema_pb2.EntitySchemaProto.Granularity]
    def __init__(self, granularity_vec: _Optional[_Iterable[_Union[_entity_schema_pb2.EntitySchemaProto.Granularity, _Mapping]]] = ...) -> None: ...

class StatsInternalCounter(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class InternalStatsProto(_message.Message):
    __slots__ = ("schema_entity_count", "total_counters", "total_containers")
    class EntityMetricCount(_message.Message):
        __slots__ = ("num_entities", "num_metrics", "descriptive_name")
        NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        NUM_METRICS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        num_entities: int
        num_metrics: int
        descriptive_name: str
        def __init__(self, num_entities: _Optional[int] = ..., num_metrics: _Optional[int] = ..., descriptive_name: _Optional[str] = ...) -> None: ...
    class SchemaEntityCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InternalStatsProto.EntityMetricCount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InternalStatsProto.EntityMetricCount, _Mapping]] = ...) -> None: ...
    SCHEMA_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    schema_entity_count: _containers.MessageMap[str, InternalStatsProto.EntityMetricCount]
    total_counters: int
    total_containers: int
    def __init__(self, schema_entity_count: _Optional[_Mapping[str, InternalStatsProto.EntityMetricCount]] = ..., total_counters: _Optional[int] = ..., total_containers: _Optional[int] = ...) -> None: ...
