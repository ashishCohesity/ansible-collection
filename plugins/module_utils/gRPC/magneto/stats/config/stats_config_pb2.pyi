from stats.base import entity_schema_pb2 as _entity_schema_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatsConfigProto(_message.Message):
    __slots__ = ("metric_type", "metric", "entity_schema_config")
    class MetricType(_message.Message):
        __slots__ = ("name", "value_type", "unit_type", "aggr_func_type", "rollup_func_type", "incremental", "publish_and_reset", "track_bandwidth")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        UNIT_TYPE_FIELD_NUMBER: _ClassVar[int]
        AGGR_FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
        ROLLUP_FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
        PUBLISH_AND_RESET_FIELD_NUMBER: _ClassVar[int]
        TRACK_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
        name: str
        value_type: _stats_types_pb2.Value.Type
        unit_type: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
        aggr_func_type: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
        rollup_func_type: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
        incremental: bool
        publish_and_reset: bool
        track_bandwidth: bool
        def __init__(self, name: _Optional[str] = ..., value_type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ..., unit_type: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type, str]] = ..., aggr_func_type: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type, str]] = ..., rollup_func_type: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type, str]] = ..., incremental: bool = ..., publish_and_reset: bool = ..., track_bandwidth: bool = ...) -> None: ...
    class Metric(_message.Message):
        __slots__ = ("name", "type", "descriptive_name")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str
        descriptive_name: str
        def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., descriptive_name: _Optional[str] = ...) -> None: ...
    class EntitySchemaConfig(_message.Message):
        __slots__ = ("schema_name", "schema_descriptive_name", "schema_version", "id_attr", "id_attr_type", "name_attr", "time_to_live_secs", "metric_name", "aggregation_metric")
        class AggregationMetric(_message.Message):
            __slots__ = ("source_schema_name", "metric_name", "aggregation_interval_sec_multiplier", "use_latest_data_point")
            SOURCE_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
            METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
            AGGREGATION_INTERVAL_SEC_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
            USE_LATEST_DATA_POINT_FIELD_NUMBER: _ClassVar[int]
            source_schema_name: str
            metric_name: str
            aggregation_interval_sec_multiplier: int
            use_latest_data_point: bool
            def __init__(self, source_schema_name: _Optional[str] = ..., metric_name: _Optional[str] = ..., aggregation_interval_sec_multiplier: _Optional[int] = ..., use_latest_data_point: bool = ...) -> None: ...
        SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_FIELD_NUMBER: _ClassVar[int]
        ID_ATTR_TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_ATTR_FIELD_NUMBER: _ClassVar[int]
        TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        AGGREGATION_METRIC_FIELD_NUMBER: _ClassVar[int]
        schema_name: str
        schema_descriptive_name: str
        schema_version: int
        id_attr: str
        id_attr_type: _stats_types_pb2.Value.Type
        name_attr: str
        time_to_live_secs: int
        metric_name: _containers.RepeatedScalarFieldContainer[str]
        aggregation_metric: _containers.RepeatedCompositeFieldContainer[StatsConfigProto.EntitySchemaConfig.AggregationMetric]
        def __init__(self, schema_name: _Optional[str] = ..., schema_descriptive_name: _Optional[str] = ..., schema_version: _Optional[int] = ..., id_attr: _Optional[str] = ..., id_attr_type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ..., name_attr: _Optional[str] = ..., time_to_live_secs: _Optional[int] = ..., metric_name: _Optional[_Iterable[str]] = ..., aggregation_metric: _Optional[_Iterable[_Union[StatsConfigProto.EntitySchemaConfig.AggregationMetric, _Mapping]]] = ...) -> None: ...
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SCHEMA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metric_type: _containers.RepeatedCompositeFieldContainer[StatsConfigProto.MetricType]
    metric: _containers.RepeatedCompositeFieldContainer[StatsConfigProto.Metric]
    entity_schema_config: _containers.RepeatedCompositeFieldContainer[StatsConfigProto.EntitySchemaConfig]
    def __init__(self, metric_type: _Optional[_Iterable[_Union[StatsConfigProto.MetricType, _Mapping]]] = ..., metric: _Optional[_Iterable[_Union[StatsConfigProto.Metric, _Mapping]]] = ..., entity_schema_config: _Optional[_Iterable[_Union[StatsConfigProto.EntitySchemaConfig, _Mapping]]] = ...) -> None: ...
