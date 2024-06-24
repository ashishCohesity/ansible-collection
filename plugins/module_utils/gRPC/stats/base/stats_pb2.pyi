from stats.base import alert_type_pb2 as _alert_type_pb2
from stats.base import alert_policies_pb2 as _alert_policies_pb2
from stats.base import entity_schema_pb2 as _entity_schema_pb2
from stats.base import error_pb2 as _error_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricDataPoint(_message.Message):
    __slots__ = ("timestamp_msecs", "data", "rollup_function")
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    timestamp_msecs: int
    data: _stats_types_pb2.Value.Data
    rollup_function: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
    def __init__(self, timestamp_msecs: _Optional[int] = ..., data: _Optional[_Union[_stats_types_pb2.Value.Data, _Mapping]] = ..., rollup_function: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type, str]] = ...) -> None: ...

class MetricValue(_message.Message):
    __slots__ = ("metric_name", "timestamp_msecs", "value")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    timestamp_msecs: int
    value: _stats_types_pb2.Value
    def __init__(self, metric_name: _Optional[str] = ..., timestamp_msecs: _Optional[int] = ..., value: _Optional[_Union[_stats_types_pb2.Value, _Mapping]] = ...) -> None: ...

class MetricDataBlock(_message.Message):
    __slots__ = ("metric_name", "type", "data_point_vec")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    type: _stats_types_pb2.Value.Type
    data_point_vec: _containers.RepeatedCompositeFieldContainer[MetricDataPoint]
    def __init__(self, metric_name: _Optional[str] = ..., type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ..., data_point_vec: _Optional[_Iterable[_Union[MetricDataPoint, _Mapping]]] = ...) -> None: ...

class EntityIdentifier(_message.Message):
    __slots__ = ("cluster_instance_identifier", "entity_id")
    CLUSTER_INSTANCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_instance_identifier: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    entity_id: _stats_types_pb2.Value
    def __init__(self, cluster_instance_identifier: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., entity_id: _Optional[_Union[_stats_types_pb2.Value, _Mapping]] = ...) -> None: ...

class EntityProto(_message.Message):
    __slots__ = ("entity_id", "attribute_vec", "aggregate_metric_source_vec", "latest_metric_vec")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRIC_SOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    LATEST_METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: EntityIdentifier
    attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    aggregate_metric_source_vec: _containers.RepeatedCompositeFieldContainer[AggregateMetricSourceProto]
    latest_metric_vec: _containers.RepeatedCompositeFieldContainer[MetricValue]
    def __init__(self, entity_id: _Optional[_Union[EntityIdentifier, _Mapping]] = ..., attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., aggregate_metric_source_vec: _Optional[_Iterable[_Union[AggregateMetricSourceProto, _Mapping]]] = ..., latest_metric_vec: _Optional[_Iterable[_Union[MetricValue, _Mapping]]] = ...) -> None: ...

class GetMasterArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMasterResult(_message.Message):
    __slots__ = ("error", "master_info")
    class MasterInfo(_message.Message):
        __slots__ = ("id", "ip", "port")
        ID_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        id: int
        ip: str
        port: int
        def __init__(self, id: _Optional[int] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MASTER_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    master_info: GetMasterResult.MasterInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., master_info: _Optional[_Union[GetMasterResult.MasterInfo, _Mapping]] = ...) -> None: ...

class CreateOrUpdateEntitySchemaArg(_message.Message):
    __slots__ = ("entity_schema",)
    ENTITY_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    entity_schema: _entity_schema_pb2.EntitySchemaProto
    def __init__(self, entity_schema: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto, _Mapping]] = ...) -> None: ...

class CreateOrUpdateEntitySchemaResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetEntitiesSchemaArg(_message.Message):
    __slots__ = ("schema_name_vec", "include_internal_schemas", "priority_request")
    SCHEMA_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERNAL_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    schema_name_vec: _containers.RepeatedScalarFieldContainer[str]
    include_internal_schemas: bool
    priority_request: bool
    def __init__(self, schema_name_vec: _Optional[_Iterable[str]] = ..., include_internal_schemas: bool = ..., priority_request: bool = ...) -> None: ...

class GetEntitiesSchemaResult(_message.Message):
    __slots__ = ("error", "entity_schema_proto_vec", "deprecated_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SCHEMA_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_schema_proto_vec: _containers.RepeatedCompositeFieldContainer[_entity_schema_pb2.EntitySchemaProto]
    deprecated_version: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_schema_proto_vec: _Optional[_Iterable[_Union[_entity_schema_pb2.EntitySchemaProto, _Mapping]]] = ..., deprecated_version: _Optional[int] = ...) -> None: ...

class AggregateMetricSourceProto(_message.Message):
    __slots__ = ("metric_name", "source_entity_id_vec", "source_metric_name_vec", "all_source_entities")
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_METRIC_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_SOURCE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    source_entity_id_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.Value]
    source_metric_name_vec: _containers.RepeatedScalarFieldContainer[str]
    all_source_entities: bool
    def __init__(self, metric_name: _Optional[str] = ..., source_entity_id_vec: _Optional[_Iterable[_Union[_stats_types_pb2.Value, _Mapping]]] = ..., source_metric_name_vec: _Optional[_Iterable[str]] = ..., all_source_entities: bool = ...) -> None: ...

class AddOrUpdateEntityArg(_message.Message):
    __slots__ = ("schema_name", "entity_attribute_vec", "aggregate_metric_source_vec", "entity_identifier")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_METRIC_SOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    aggregate_metric_source_vec: _containers.RepeatedCompositeFieldContainer[AggregateMetricSourceProto]
    entity_identifier: EntityIdentifier
    def __init__(self, schema_name: _Optional[str] = ..., entity_attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., aggregate_metric_source_vec: _Optional[_Iterable[_Union[AggregateMetricSourceProto, _Mapping]]] = ..., entity_identifier: _Optional[_Union[EntityIdentifier, _Mapping]] = ...) -> None: ...

class AddOrUpdateEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddEntityStatsArg(_message.Message):
    __slots__ = ("schema_name", "entity_identifier", "metric_data_block", "make_durable", "update_entity_publish_timestamp")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    METRIC_DATA_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MAKE_DURABLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ENTITY_PUBLISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_identifier: EntityIdentifier
    metric_data_block: MetricDataBlock
    make_durable: bool
    update_entity_publish_timestamp: bool
    def __init__(self, schema_name: _Optional[str] = ..., entity_identifier: _Optional[_Union[EntityIdentifier, _Mapping]] = ..., metric_data_block: _Optional[_Union[MetricDataBlock, _Mapping]] = ..., make_durable: bool = ..., update_entity_publish_timestamp: bool = ...) -> None: ...

class AddEntityStatsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddEntitiesStatsArg(_message.Message):
    __slots__ = ("schema_name", "entity_stats_vec", "make_durable", "update_entity_publish_timestamp")
    class EntityStats(_message.Message):
        __slots__ = ("entity_identifier", "metric_data_block_vec")
        ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        METRIC_DATA_BLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_identifier: EntityIdentifier
        metric_data_block_vec: _containers.RepeatedCompositeFieldContainer[MetricDataBlock]
        def __init__(self, entity_identifier: _Optional[_Union[EntityIdentifier, _Mapping]] = ..., metric_data_block_vec: _Optional[_Iterable[_Union[MetricDataBlock, _Mapping]]] = ...) -> None: ...
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    MAKE_DURABLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ENTITY_PUBLISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_stats_vec: _containers.RepeatedCompositeFieldContainer[AddEntitiesStatsArg.EntityStats]
    make_durable: bool
    update_entity_publish_timestamp: bool
    def __init__(self, schema_name: _Optional[str] = ..., entity_stats_vec: _Optional[_Iterable[_Union[AddEntitiesStatsArg.EntityStats, _Mapping]]] = ..., make_durable: bool = ..., update_entity_publish_timestamp: bool = ...) -> None: ...

class AddEntitiesStatsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetEntitiesArg(_message.Message):
    __slots__ = ("schema_name", "max_entities", "cluster_instance_identifier", "filter_criteria", "ordered_by", "exclude_entity_attributes", "exclude_aggregate_metric_sources", "next_cursor", "metric_name_vec", "priority_request", "skip_cache", "entity_prefix")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FILTER_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ORDERED_BY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_ENTITY_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_AGGREGATE_METRIC_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    max_entities: int
    cluster_instance_identifier: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    filter_criteria: str
    ordered_by: str
    exclude_entity_attributes: bool
    exclude_aggregate_metric_sources: bool
    next_cursor: str
    metric_name_vec: _containers.RepeatedScalarFieldContainer[str]
    priority_request: bool
    skip_cache: bool
    entity_prefix: str
    def __init__(self, schema_name: _Optional[str] = ..., max_entities: _Optional[int] = ..., cluster_instance_identifier: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., filter_criteria: _Optional[str] = ..., ordered_by: _Optional[str] = ..., exclude_entity_attributes: bool = ..., exclude_aggregate_metric_sources: bool = ..., next_cursor: _Optional[str] = ..., metric_name_vec: _Optional[_Iterable[str]] = ..., priority_request: bool = ..., skip_cache: bool = ..., entity_prefix: _Optional[str] = ...) -> None: ...

class GetEntitiesResult(_message.Message):
    __slots__ = ("error", "entity_vec", "next_cursor")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[EntityProto]
    next_cursor: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[EntityProto, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class GetEntitiesByIdArg(_message.Message):
    __slots__ = ("schema_name", "entity_identifier_vec", "exclude_entity_attributes", "exclude_aggregate_metric_sources", "metric_name_vec", "priority_request", "skip_cache")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDENTIFIER_VEC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_ENTITY_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_AGGREGATE_METRIC_SOURCES_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SKIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_identifier_vec: _containers.RepeatedCompositeFieldContainer[EntityIdentifier]
    exclude_entity_attributes: bool
    exclude_aggregate_metric_sources: bool
    metric_name_vec: _containers.RepeatedScalarFieldContainer[str]
    priority_request: bool
    skip_cache: bool
    def __init__(self, schema_name: _Optional[str] = ..., entity_identifier_vec: _Optional[_Iterable[_Union[EntityIdentifier, _Mapping]]] = ..., exclude_entity_attributes: bool = ..., exclude_aggregate_metric_sources: bool = ..., metric_name_vec: _Optional[_Iterable[str]] = ..., priority_request: bool = ..., skip_cache: bool = ...) -> None: ...

class GetEntitiesByIdResult(_message.Message):
    __slots__ = ("error", "entity_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[EntityProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[EntityProto, _Mapping]]] = ...) -> None: ...

class DeleteEntityArg(_message.Message):
    __slots__ = ("schema_name", "entity_identifier")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_identifier: EntityIdentifier
    def __init__(self, schema_name: _Optional[str] = ..., entity_identifier: _Optional[_Union[EntityIdentifier, _Mapping]] = ...) -> None: ...

class DeleteEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteClusterInstanceArg(_message.Message):
    __slots__ = ("cluster_instance_identifier",)
    CLUSTER_INSTANCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    cluster_instance_identifier: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    def __init__(self, cluster_instance_identifier: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ...) -> None: ...

class DeleteClusterInstanceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetTimeSeriesStatsArg(_message.Message):
    __slots__ = ("schema_name", "entity_identifier", "metric_name", "start_time_msecs", "end_time_msecs", "rollup_function", "rollup_interval_secs", "metric_name_vec", "skip_shard_check", "priority_request", "rollup_function_vec", "rollup_interval_secs_vec", "pro_rate_data_points", "show_growth_change")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_SHARD_CHECK_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FUNCTION_VEC_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_INTERVAL_SECS_VEC_FIELD_NUMBER: _ClassVar[int]
    PRO_RATE_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_GROWTH_CHANGE_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_identifier: EntityIdentifier
    metric_name: str
    start_time_msecs: int
    end_time_msecs: int
    rollup_function: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction
    rollup_interval_secs: int
    metric_name_vec: _containers.RepeatedScalarFieldContainer[str]
    skip_shard_check: bool
    priority_request: bool
    rollup_function_vec: _containers.RepeatedCompositeFieldContainer[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction]
    rollup_interval_secs_vec: _containers.RepeatedScalarFieldContainer[int]
    pro_rate_data_points: bool
    show_growth_change: bool
    def __init__(self, schema_name: _Optional[str] = ..., entity_identifier: _Optional[_Union[EntityIdentifier, _Mapping]] = ..., metric_name: _Optional[str] = ..., start_time_msecs: _Optional[int] = ..., end_time_msecs: _Optional[int] = ..., rollup_function: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]] = ..., rollup_interval_secs: _Optional[int] = ..., metric_name_vec: _Optional[_Iterable[str]] = ..., skip_shard_check: bool = ..., priority_request: bool = ..., rollup_function_vec: _Optional[_Iterable[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]]] = ..., rollup_interval_secs_vec: _Optional[_Iterable[int]] = ..., pro_rate_data_points: bool = ..., show_growth_change: bool = ...) -> None: ...

class GetTimeSeriesStatsResult(_message.Message):
    __slots__ = ("error", "metric_data_block", "fetched_all_stats", "metric_data_block_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METRIC_DATA_BLOCK_FIELD_NUMBER: _ClassVar[int]
    FETCHED_ALL_STATS_FIELD_NUMBER: _ClassVar[int]
    METRIC_DATA_BLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    metric_data_block: MetricDataBlock
    fetched_all_stats: bool
    metric_data_block_vec: _containers.RepeatedCompositeFieldContainer[MetricDataBlock]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., metric_data_block: _Optional[_Union[MetricDataBlock, _Mapping]] = ..., fetched_all_stats: bool = ..., metric_data_block_vec: _Optional[_Iterable[_Union[MetricDataBlock, _Mapping]]] = ...) -> None: ...

class CounterNamespace(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMagneto: _ClassVar[CounterNamespace.Type]
        kIris: _ClassVar[CounterNamespace.Type]
        kBridge: _ClassVar[CounterNamespace.Type]
        kIcebox: _ClassVar[CounterNamespace.Type]
        kMax: _ClassVar[CounterNamespace.Type]
    kMagneto: CounterNamespace.Type
    kIris: CounterNamespace.Type
    kBridge: CounterNamespace.Type
    kIcebox: CounterNamespace.Type
    kMax: CounterNamespace.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: CounterNamespace.Type
    def __init__(self, type: _Optional[_Union[CounterNamespace.Type, str]] = ...) -> None: ...

class CounterIdentifier(_message.Message):
    __slots__ = ("ns", "name")
    NS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ns: CounterNamespace
    name: str
    def __init__(self, ns: _Optional[_Union[CounterNamespace, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class Counter(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: CounterIdentifier
    value: int
    def __init__(self, id: _Optional[_Union[CounterIdentifier, _Mapping]] = ..., value: _Optional[int] = ...) -> None: ...

class CounterTimeseriesSpec(_message.Message):
    __slots__ = ("schema_name", "entity_id", "metric_name")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_id: EntityIdentifier
    metric_name: str
    def __init__(self, schema_name: _Optional[str] = ..., entity_id: _Optional[_Union[EntityIdentifier, _Mapping]] = ..., metric_name: _Optional[str] = ...) -> None: ...

class CreateCountersArg(_message.Message):
    __slots__ = ("counter_spec_vec",)
    class CounterSpec(_message.Message):
        __slots__ = ("counter_id", "create_time_series", "ignore_if_exists", "initial_value", "timeseries_spec")
        COUNTER_ID_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
        IGNORE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
        INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
        TIMESERIES_SPEC_FIELD_NUMBER: _ClassVar[int]
        counter_id: CounterIdentifier
        create_time_series: bool
        ignore_if_exists: bool
        initial_value: int
        timeseries_spec: CounterTimeseriesSpec
        def __init__(self, counter_id: _Optional[_Union[CounterIdentifier, _Mapping]] = ..., create_time_series: bool = ..., ignore_if_exists: bool = ..., initial_value: _Optional[int] = ..., timeseries_spec: _Optional[_Union[CounterTimeseriesSpec, _Mapping]] = ...) -> None: ...
    COUNTER_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    counter_spec_vec: _containers.RepeatedCompositeFieldContainer[CreateCountersArg.CounterSpec]
    def __init__(self, counter_spec_vec: _Optional[_Iterable[_Union[CreateCountersArg.CounterSpec, _Mapping]]] = ...) -> None: ...

class CreateCountersResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetCountersArg(_message.Message):
    __slots__ = ("counter_id_vec", "counter_ns", "max_counters", "cursor")
    COUNTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    COUNTER_NS_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    counter_id_vec: _containers.RepeatedCompositeFieldContainer[CounterIdentifier]
    counter_ns: CounterNamespace
    max_counters: int
    cursor: bytes
    def __init__(self, counter_id_vec: _Optional[_Iterable[_Union[CounterIdentifier, _Mapping]]] = ..., counter_ns: _Optional[_Union[CounterNamespace, _Mapping]] = ..., max_counters: _Optional[int] = ..., cursor: _Optional[bytes] = ...) -> None: ...

class GetCountersResult(_message.Message):
    __slots__ = ("error", "counter_vec", "next_cursor")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COUNTER_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    counter_vec: _containers.RepeatedCompositeFieldContainer[Counter]
    next_cursor: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., counter_vec: _Optional[_Iterable[_Union[Counter, _Mapping]]] = ..., next_cursor: _Optional[bytes] = ...) -> None: ...

class UpdateCountersArg(_message.Message):
    __slots__ = ("update_counter_vec",)
    class UpdateCounter(_message.Message):
        __slots__ = ("counter_id", "value", "increment_counter", "create_if_absent")
        COUNTER_ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        INCREMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
        CREATE_IF_ABSENT_FIELD_NUMBER: _ClassVar[int]
        counter_id: CounterIdentifier
        value: int
        increment_counter: bool
        create_if_absent: bool
        def __init__(self, counter_id: _Optional[_Union[CounterIdentifier, _Mapping]] = ..., value: _Optional[int] = ..., increment_counter: bool = ..., create_if_absent: bool = ...) -> None: ...
    UPDATE_COUNTER_VEC_FIELD_NUMBER: _ClassVar[int]
    update_counter_vec: _containers.RepeatedCompositeFieldContainer[UpdateCountersArg.UpdateCounter]
    def __init__(self, update_counter_vec: _Optional[_Iterable[_Union[UpdateCountersArg.UpdateCounter, _Mapping]]] = ...) -> None: ...

class UpdateCountersResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteCountersArg(_message.Message):
    __slots__ = ("counter_id_vec",)
    COUNTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    counter_id_vec: _containers.RepeatedCompositeFieldContainer[CounterIdentifier]
    def __init__(self, counter_id_vec: _Optional[_Iterable[_Union[CounterIdentifier, _Mapping]]] = ...) -> None: ...

class DeleteCountersResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateStatsContainersArg(_message.Message):
    __slots__ = ("container_spec_vec",)
    class ContainerSpec(_message.Message):
        __slots__ = ("counter_id_vec", "time_to_live_secs", "container_id")
        COUNTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
        counter_id_vec: _containers.RepeatedCompositeFieldContainer[CounterIdentifier]
        time_to_live_secs: int
        container_id: int
        def __init__(self, counter_id_vec: _Optional[_Iterable[_Union[CounterIdentifier, _Mapping]]] = ..., time_to_live_secs: _Optional[int] = ..., container_id: _Optional[int] = ...) -> None: ...
    CONTAINER_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    container_spec_vec: _containers.RepeatedCompositeFieldContainer[CreateStatsContainersArg.ContainerSpec]
    def __init__(self, container_spec_vec: _Optional[_Iterable[_Union[CreateStatsContainersArg.ContainerSpec, _Mapping]]] = ...) -> None: ...

class CreateStatsContainersResult(_message.Message):
    __slots__ = ("error", "id_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetStatsContainersArg(_message.Message):
    __slots__ = ("id_vec", "max_stats_containers", "cursor")
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_STATS_CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id_vec: _containers.RepeatedScalarFieldContainer[int]
    max_stats_containers: int
    cursor: str
    def __init__(self, id_vec: _Optional[_Iterable[int]] = ..., max_stats_containers: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class GetStatsContainersResult(_message.Message):
    __slots__ = ("error", "stats_container_vec", "next_cursor")
    class StatsContainer(_message.Message):
        __slots__ = ("id", "counter_vec")
        ID_FIELD_NUMBER: _ClassVar[int]
        COUNTER_VEC_FIELD_NUMBER: _ClassVar[int]
        id: int
        counter_vec: _containers.RepeatedCompositeFieldContainer[Counter]
        def __init__(self, id: _Optional[int] = ..., counter_vec: _Optional[_Iterable[_Union[Counter, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    stats_container_vec: _containers.RepeatedCompositeFieldContainer[GetStatsContainersResult.StatsContainer]
    next_cursor: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., stats_container_vec: _Optional[_Iterable[_Union[GetStatsContainersResult.StatsContainer, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class UpdateStatsContainersArg(_message.Message):
    __slots__ = ("update_stats_container_vec",)
    class UpdateStatsContainer(_message.Message):
        __slots__ = ("id", "value", "increment_counters")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        INCREMENT_COUNTERS_FIELD_NUMBER: _ClassVar[int]
        id: int
        value: int
        increment_counters: bool
        def __init__(self, id: _Optional[int] = ..., value: _Optional[int] = ..., increment_counters: bool = ...) -> None: ...
    UPDATE_STATS_CONTAINER_VEC_FIELD_NUMBER: _ClassVar[int]
    update_stats_container_vec: _containers.RepeatedCompositeFieldContainer[UpdateStatsContainersArg.UpdateStatsContainer]
    def __init__(self, update_stats_container_vec: _Optional[_Iterable[_Union[UpdateStatsContainersArg.UpdateStatsContainer, _Mapping]]] = ...) -> None: ...

class UpdateStatsContainersResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteStatsContainersArg(_message.Message):
    __slots__ = ("id_vec",)
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteStatsContainersResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetAlertPoliciesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAlertPoliciesResult(_message.Message):
    __slots__ = ("error", "alert_policies")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICIES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    alert_policies: _alert_policies_pb2.AlertPoliciesProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., alert_policies: _Optional[_Union[_alert_policies_pb2.AlertPoliciesProto, _Mapping]] = ...) -> None: ...

class UpdateAlertPoliciesArg(_message.Message):
    __slots__ = ("reset_all_policies_to_default", "update_alert_policy_vec")
    class UpdateAlertPolicy(_message.Message):
        __slots__ = ("alert_type_id", "critical_threshold_value", "warning_threshold_value", "info_threshold_value", "duration_secs")
        ALERT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        CRITICAL_THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
        WARNING_THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
        INFO_THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
        DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
        alert_type_id: _alert_type_pb2.AlertTypeProto.Id
        critical_threshold_value: float
        warning_threshold_value: float
        info_threshold_value: float
        duration_secs: float
        def __init__(self, alert_type_id: _Optional[_Union[_alert_type_pb2.AlertTypeProto.Id, str]] = ..., critical_threshold_value: _Optional[float] = ..., warning_threshold_value: _Optional[float] = ..., info_threshold_value: _Optional[float] = ..., duration_secs: _Optional[float] = ...) -> None: ...
    RESET_ALL_POLICIES_TO_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ALERT_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    reset_all_policies_to_default: bool
    update_alert_policy_vec: _containers.RepeatedCompositeFieldContainer[UpdateAlertPoliciesArg.UpdateAlertPolicy]
    def __init__(self, reset_all_policies_to_default: bool = ..., update_alert_policy_vec: _Optional[_Iterable[_Union[UpdateAlertPoliciesArg.UpdateAlertPolicy, _Mapping]]] = ...) -> None: ...

class UpdateAlertPoliciesResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetEntityMetadataArg(_message.Message):
    __slots__ = ("schema_name", "entity_identifier")
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    schema_name: str
    entity_identifier: EntityIdentifier
    def __init__(self, schema_name: _Optional[str] = ..., entity_identifier: _Optional[_Union[EntityIdentifier, _Mapping]] = ...) -> None: ...

class GetEntityMetadataResult(_message.Message):
    __slots__ = ("error", "entity_removal_state", "metric_metadata_vec")
    class MetricMetadata(_message.Message):
        __slots__ = ("metric_name", "rollup_function", "rollup_interval_secs", "scribe_row_id", "data_block_location_vec")
        class DataBlockLocation(_message.Message):
            __slots__ = ("start_time_msecs", "scribe_row_id")
            START_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
            SCRIBE_ROW_ID_FIELD_NUMBER: _ClassVar[int]
            start_time_msecs: int
            scribe_row_id: int
            def __init__(self, start_time_msecs: _Optional[int] = ..., scribe_row_id: _Optional[int] = ...) -> None: ...
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        ROLLUP_FUNCTION_FIELD_NUMBER: _ClassVar[int]
        ROLLUP_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
        SCRIBE_ROW_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_BLOCK_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
        metric_name: str
        rollup_function: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction
        rollup_interval_secs: int
        scribe_row_id: int
        data_block_location_vec: _containers.RepeatedCompositeFieldContainer[GetEntityMetadataResult.MetricMetadata.DataBlockLocation]
        def __init__(self, metric_name: _Optional[str] = ..., rollup_function: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]] = ..., rollup_interval_secs: _Optional[int] = ..., scribe_row_id: _Optional[int] = ..., data_block_location_vec: _Optional[_Iterable[_Union[GetEntityMetadataResult.MetricMetadata.DataBlockLocation, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_REMOVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    METRIC_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_removal_state: str
    metric_metadata_vec: _containers.RepeatedCompositeFieldContainer[GetEntityMetadataResult.MetricMetadata]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_removal_state: _Optional[str] = ..., metric_metadata_vec: _Optional[_Iterable[_Union[GetEntityMetadataResult.MetricMetadata, _Mapping]]] = ...) -> None: ...

class StatsMigrationState(_message.Message):
    __slots__ = ("migration_completed", "cutover_epoch_timestamps_usecs")
    MIGRATION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CUTOVER_EPOCH_TIMESTAMPS_USECS_FIELD_NUMBER: _ClassVar[int]
    migration_completed: bool
    cutover_epoch_timestamps_usecs: int
    def __init__(self, migration_completed: bool = ..., cutover_epoch_timestamps_usecs: _Optional[int] = ...) -> None: ...

class StatsConfigProto(_message.Message):
    __slots__ = ("stats_master_key", "base_url", "get_master_absolute_url", "create_or_update_entity_schema_relative_url", "get_entities_schema_relative_url", "add_or_update_entity_relative_url", "get_entities_relative_url", "get_entities_by_id_relative_url", "delete_entity_relative_url", "add_entity_stats_relative_url", "get_entity_stats_relative_url", "get_alert_policies_relative_url", "update_alert_policies_relative_url", "create_counters_relative_url", "get_counters_relative_url", "update_counters_relative_url", "delete_counters_relative_url", "get_stats_containers_relative_url", "update_stats_containers_relative_url", "create_task_relative_url", "report_tasks_progress_relative_url", "get_tasks_relative_url", "print_counters_relative_url", "migrate_state_key", "add_entities_stats_relative_url", "stats_aggregation_state_key", "stats_global_rollup_granularity_key")
    STATS_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_MASTER_ABSOLUTE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_OR_UPDATE_ENTITY_SCHEMA_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITIES_SCHEMA_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_ENTITY_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITIES_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITIES_BY_ID_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTITY_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    ADD_ENTITY_STATS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_STATS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_ALERT_POLICIES_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ALERT_POLICIES_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_COUNTERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_COUNTERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_COUNTERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_COUNTERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_STATS_CONTAINERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STATS_CONTAINERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TASK_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    REPORT_TASKS_PROGRESS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_TASKS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    PRINT_COUNTERS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_STATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ADD_ENTITIES_STATS_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    STATS_AGGREGATION_STATE_KEY_FIELD_NUMBER: _ClassVar[int]
    STATS_GLOBAL_ROLLUP_GRANULARITY_KEY_FIELD_NUMBER: _ClassVar[int]
    stats_master_key: str
    base_url: str
    get_master_absolute_url: str
    create_or_update_entity_schema_relative_url: str
    get_entities_schema_relative_url: str
    add_or_update_entity_relative_url: str
    get_entities_relative_url: str
    get_entities_by_id_relative_url: str
    delete_entity_relative_url: str
    add_entity_stats_relative_url: str
    get_entity_stats_relative_url: str
    get_alert_policies_relative_url: str
    update_alert_policies_relative_url: str
    create_counters_relative_url: str
    get_counters_relative_url: str
    update_counters_relative_url: str
    delete_counters_relative_url: str
    get_stats_containers_relative_url: str
    update_stats_containers_relative_url: str
    create_task_relative_url: str
    report_tasks_progress_relative_url: str
    get_tasks_relative_url: str
    print_counters_relative_url: str
    migrate_state_key: str
    add_entities_stats_relative_url: str
    stats_aggregation_state_key: str
    stats_global_rollup_granularity_key: str
    def __init__(self, stats_master_key: _Optional[str] = ..., base_url: _Optional[str] = ..., get_master_absolute_url: _Optional[str] = ..., create_or_update_entity_schema_relative_url: _Optional[str] = ..., get_entities_schema_relative_url: _Optional[str] = ..., add_or_update_entity_relative_url: _Optional[str] = ..., get_entities_relative_url: _Optional[str] = ..., get_entities_by_id_relative_url: _Optional[str] = ..., delete_entity_relative_url: _Optional[str] = ..., add_entity_stats_relative_url: _Optional[str] = ..., get_entity_stats_relative_url: _Optional[str] = ..., get_alert_policies_relative_url: _Optional[str] = ..., update_alert_policies_relative_url: _Optional[str] = ..., create_counters_relative_url: _Optional[str] = ..., get_counters_relative_url: _Optional[str] = ..., update_counters_relative_url: _Optional[str] = ..., delete_counters_relative_url: _Optional[str] = ..., get_stats_containers_relative_url: _Optional[str] = ..., update_stats_containers_relative_url: _Optional[str] = ..., create_task_relative_url: _Optional[str] = ..., report_tasks_progress_relative_url: _Optional[str] = ..., get_tasks_relative_url: _Optional[str] = ..., print_counters_relative_url: _Optional[str] = ..., migrate_state_key: _Optional[str] = ..., add_entities_stats_relative_url: _Optional[str] = ..., stats_aggregation_state_key: _Optional[str] = ..., stats_global_rollup_granularity_key: _Optional[str] = ...) -> None: ...
