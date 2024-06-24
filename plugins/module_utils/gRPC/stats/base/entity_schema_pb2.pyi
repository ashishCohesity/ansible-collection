from google.protobuf import descriptor_pb2 as _descriptor_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
STATS_MESSAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
stats_message_options: _descriptor.FieldDescriptor

class StatsMessageOptionsProto(_message.Message):
    __slots__ = ("cluster_id_attribute", "cluster_incarnation_id_attribute", "ids_value_type")
    CLUSTER_ID_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    IDS_VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    cluster_id_attribute: str
    cluster_incarnation_id_attribute: str
    ids_value_type: _stats_types_pb2.Value.Type
    def __init__(self, cluster_id_attribute: _Optional[str] = ..., cluster_incarnation_id_attribute: _Optional[str] = ..., ids_value_type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ...) -> None: ...

class EntitySchemaProto(_message.Message):
    __slots__ = ("name", "schema_descriptive_name", "version", "attributes_descriptor", "time_series_descriptor_vec", "schema_help_text", "is_internal_schema", "flush_interval_secs", "largest_flush_interval_secs", "time_to_live_secs", "rollup_granularity_vec", "enable_rollup", "entities_time_to_live_secs")
    class KeyValueDescriptor(_message.Message):
        __slots__ = ("key_name", "value_type")
        KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        key_name: str
        value_type: _stats_types_pb2.Value.Type
        def __init__(self, key_name: _Optional[str] = ..., value_type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ...) -> None: ...
    class AttributesDescriptor(_message.Message):
        __slots__ = ("attribute_vec", "key_attribute_name_index")
        ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        KEY_ATTRIBUTE_NAME_INDEX_FIELD_NUMBER: _ClassVar[int]
        attribute_vec: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto.KeyValueDescriptor]
        key_attribute_name_index: int
        def __init__(self, attribute_vec: _Optional[_Iterable[_Union[EntitySchemaProto.KeyValueDescriptor, _Mapping]]] = ..., key_attribute_name_index: _Optional[int] = ...) -> None: ...
    class TimeSeriesDescriptor(_message.Message):
        __slots__ = ("metric_name", "metric_descriptive_name", "value_type", "metric_unit", "aggregation_descriptor", "raw_metric_publish_interval_hint_secs", "time_to_live_secs", "local_cluster_rollups_vec", "remote_cluster_rollups_vec")
        class MetricUnit(_message.Message):
            __slots__ = ("type",)
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kBytes: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kTimeUsecs: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kTimeMsecs: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kTimeSecs: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kTimeMins: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kCounter: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kTempCentigrade: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kTempFahrenheit: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kRpm: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
                kPercent: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type]
            kBytes: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kTimeUsecs: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kTimeMsecs: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kTimeSecs: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kTimeMins: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kCounter: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kTempCentigrade: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kTempFahrenheit: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kRpm: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            kPercent: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type
            def __init__(self, type: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit.Type, str]] = ...) -> None: ...
        class AggregationFunction(_message.Message):
            __slots__ = ("type",)
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kSum: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type]
                kAverage: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type]
                kCount: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type]
                kMax: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type]
                kMin: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type]
            kSum: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
            kAverage: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
            kCount: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
            kMax: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
            kMin: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type
            def __init__(self, type: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction.Type, str]] = ...) -> None: ...
        class AggregationDescriptor(_message.Message):
            __slots__ = ("source_schema_name", "source_metric_name_vec", "aggregation_interval_sec", "aggregation_function", "rollup_function", "use_latest_data_point", "skip_aggregation_for_missing_source_metrics")
            SOURCE_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
            SOURCE_METRIC_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
            AGGREGATION_INTERVAL_SEC_FIELD_NUMBER: _ClassVar[int]
            AGGREGATION_FUNCTION_FIELD_NUMBER: _ClassVar[int]
            ROLLUP_FUNCTION_FIELD_NUMBER: _ClassVar[int]
            USE_LATEST_DATA_POINT_FIELD_NUMBER: _ClassVar[int]
            SKIP_AGGREGATION_FOR_MISSING_SOURCE_METRICS_FIELD_NUMBER: _ClassVar[int]
            source_schema_name: str
            source_metric_name_vec: _containers.RepeatedScalarFieldContainer[str]
            aggregation_interval_sec: int
            aggregation_function: EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction
            rollup_function: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction
            use_latest_data_point: bool
            skip_aggregation_for_missing_source_metrics: bool
            def __init__(self, source_schema_name: _Optional[str] = ..., source_metric_name_vec: _Optional[_Iterable[str]] = ..., aggregation_interval_sec: _Optional[int] = ..., aggregation_function: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.AggregationFunction, _Mapping]] = ..., rollup_function: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]] = ..., use_latest_data_point: bool = ..., skip_aggregation_for_missing_source_metrics: bool = ...) -> None: ...
        class RollupFunction(_message.Message):
            __slots__ = ("type",)
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kSum: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kAverage: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kCount: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kMax: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kMin: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kMedian: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kPercentile95: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kLatest: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kRate: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
                kRollupFunctionCount: _ClassVar[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type]
            kSum: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kAverage: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kCount: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kMax: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kMin: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kMedian: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kPercentile95: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kLatest: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kRate: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            kRollupFunctionCount: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type
            def __init__(self, type: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction.Type, str]] = ...) -> None: ...
        class Rollups(_message.Message):
            __slots__ = ("rollup_function", "granularity_vec")
            class Granularity(_message.Message):
                __slots__ = ("rollup_interval_secs", "time_to_live_secs")
                ROLLUP_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
                TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
                rollup_interval_secs: int
                time_to_live_secs: int
                def __init__(self, rollup_interval_secs: _Optional[int] = ..., time_to_live_secs: _Optional[int] = ...) -> None: ...
            ROLLUP_FUNCTION_FIELD_NUMBER: _ClassVar[int]
            GRANULARITY_VEC_FIELD_NUMBER: _ClassVar[int]
            rollup_function: EntitySchemaProto.TimeSeriesDescriptor.RollupFunction
            granularity_vec: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto.TimeSeriesDescriptor.Rollups.Granularity]
            def __init__(self, rollup_function: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]] = ..., granularity_vec: _Optional[_Iterable[_Union[EntitySchemaProto.TimeSeriesDescriptor.Rollups.Granularity, _Mapping]]] = ...) -> None: ...
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        METRIC_DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        METRIC_UNIT_FIELD_NUMBER: _ClassVar[int]
        AGGREGATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        RAW_METRIC_PUBLISH_INTERVAL_HINT_SECS_FIELD_NUMBER: _ClassVar[int]
        TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
        LOCAL_CLUSTER_ROLLUPS_VEC_FIELD_NUMBER: _ClassVar[int]
        REMOTE_CLUSTER_ROLLUPS_VEC_FIELD_NUMBER: _ClassVar[int]
        metric_name: str
        metric_descriptive_name: str
        value_type: _stats_types_pb2.Value.Type
        metric_unit: EntitySchemaProto.TimeSeriesDescriptor.MetricUnit
        aggregation_descriptor: EntitySchemaProto.TimeSeriesDescriptor.AggregationDescriptor
        raw_metric_publish_interval_hint_secs: int
        time_to_live_secs: int
        local_cluster_rollups_vec: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto.TimeSeriesDescriptor.Rollups]
        remote_cluster_rollups_vec: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto.TimeSeriesDescriptor.Rollups]
        def __init__(self, metric_name: _Optional[str] = ..., metric_descriptive_name: _Optional[str] = ..., value_type: _Optional[_Union[_stats_types_pb2.Value.Type, str]] = ..., metric_unit: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.MetricUnit, _Mapping]] = ..., aggregation_descriptor: _Optional[_Union[EntitySchemaProto.TimeSeriesDescriptor.AggregationDescriptor, _Mapping]] = ..., raw_metric_publish_interval_hint_secs: _Optional[int] = ..., time_to_live_secs: _Optional[int] = ..., local_cluster_rollups_vec: _Optional[_Iterable[_Union[EntitySchemaProto.TimeSeriesDescriptor.Rollups, _Mapping]]] = ..., remote_cluster_rollups_vec: _Optional[_Iterable[_Union[EntitySchemaProto.TimeSeriesDescriptor.Rollups, _Mapping]]] = ...) -> None: ...
    class Granularity(_message.Message):
        __slots__ = ("rollup_interval_secs", "time_to_live_secs")
        ROLLUP_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
        TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
        rollup_interval_secs: int
        time_to_live_secs: int
        def __init__(self, rollup_interval_secs: _Optional[int] = ..., time_to_live_secs: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_DESCRIPTOR_VEC_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    FLUSH_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    LARGEST_FLUSH_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_GRANULARITY_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ROLLUP_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_TIME_TO_LIVE_SECS_FIELD_NUMBER: _ClassVar[int]
    name: str
    schema_descriptive_name: str
    version: int
    attributes_descriptor: EntitySchemaProto.AttributesDescriptor
    time_series_descriptor_vec: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto.TimeSeriesDescriptor]
    schema_help_text: str
    is_internal_schema: bool
    flush_interval_secs: int
    largest_flush_interval_secs: int
    time_to_live_secs: int
    rollup_granularity_vec: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto.Granularity]
    enable_rollup: bool
    entities_time_to_live_secs: int
    def __init__(self, name: _Optional[str] = ..., schema_descriptive_name: _Optional[str] = ..., version: _Optional[int] = ..., attributes_descriptor: _Optional[_Union[EntitySchemaProto.AttributesDescriptor, _Mapping]] = ..., time_series_descriptor_vec: _Optional[_Iterable[_Union[EntitySchemaProto.TimeSeriesDescriptor, _Mapping]]] = ..., schema_help_text: _Optional[str] = ..., is_internal_schema: bool = ..., flush_interval_secs: _Optional[int] = ..., largest_flush_interval_secs: _Optional[int] = ..., time_to_live_secs: _Optional[int] = ..., rollup_granularity_vec: _Optional[_Iterable[_Union[EntitySchemaProto.Granularity, _Mapping]]] = ..., enable_rollup: bool = ..., entities_time_to_live_secs: _Optional[int] = ...) -> None: ...

class EntitySchemaList(_message.Message):
    __slots__ = ("entity_schema",)
    ENTITY_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    entity_schema: _containers.RepeatedCompositeFieldContainer[EntitySchemaProto]
    def __init__(self, entity_schema: _Optional[_Iterable[_Union[EntitySchemaProto, _Mapping]]] = ...) -> None: ...
