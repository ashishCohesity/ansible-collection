from stats.base import alert_type_pb2 as _alert_type_pb2
from stats.base import entity_schema_pb2 as _entity_schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertPolicyProto(_message.Message):
    __slots__ = ("alert_type_id", "alert_policy_description", "entity_schema_name", "metric_vec", "critical_threshold", "warning_threshold", "info_threshold", "ascending_order_thresholds", "min_allowed_threshold", "max_allowed_threshold", "duration", "metric_unit", "help_text")
    class Metric(_message.Message):
        __slots__ = ("name", "rollup_function")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROLLUP_FUNCTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        rollup_function: _entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction
        def __init__(self, name: _Optional[str] = ..., rollup_function: _Optional[_Union[_entity_schema_pb2.EntitySchemaProto.TimeSeriesDescriptor.RollupFunction, _Mapping]] = ...) -> None: ...
    class Threshold(_message.Message):
        __slots__ = ("default_threshold", "user_defined_threshold")
        DEFAULT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        USER_DEFINED_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        default_threshold: float
        user_defined_threshold: float
        def __init__(self, default_threshold: _Optional[float] = ..., user_defined_threshold: _Optional[float] = ...) -> None: ...
    class Duration(_message.Message):
        __slots__ = ("default_duration_secs", "user_defined_duration_secs", "min_allowed_duration_secs", "max_allowed_duration_secs")
        DEFAULT_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
        USER_DEFINED_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
        MIN_ALLOWED_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
        MAX_ALLOWED_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
        default_duration_secs: int
        user_defined_duration_secs: int
        min_allowed_duration_secs: int
        max_allowed_duration_secs: int
        def __init__(self, default_duration_secs: _Optional[int] = ..., user_defined_duration_secs: _Optional[int] = ..., min_allowed_duration_secs: _Optional[int] = ..., max_allowed_duration_secs: _Optional[int] = ...) -> None: ...
    ALERT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    WARNING_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    INFO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ASCENDING_ORDER_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    MIN_ALLOWED_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOWED_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    METRIC_UNIT_FIELD_NUMBER: _ClassVar[int]
    HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    alert_type_id: _alert_type_pb2.AlertTypeProto.Id
    alert_policy_description: str
    entity_schema_name: str
    metric_vec: _containers.RepeatedCompositeFieldContainer[AlertPolicyProto.Metric]
    critical_threshold: AlertPolicyProto.Threshold
    warning_threshold: AlertPolicyProto.Threshold
    info_threshold: AlertPolicyProto.Threshold
    ascending_order_thresholds: bool
    min_allowed_threshold: float
    max_allowed_threshold: float
    duration: AlertPolicyProto.Duration
    metric_unit: str
    help_text: str
    def __init__(self, alert_type_id: _Optional[_Union[_alert_type_pb2.AlertTypeProto.Id, str]] = ..., alert_policy_description: _Optional[str] = ..., entity_schema_name: _Optional[str] = ..., metric_vec: _Optional[_Iterable[_Union[AlertPolicyProto.Metric, _Mapping]]] = ..., critical_threshold: _Optional[_Union[AlertPolicyProto.Threshold, _Mapping]] = ..., warning_threshold: _Optional[_Union[AlertPolicyProto.Threshold, _Mapping]] = ..., info_threshold: _Optional[_Union[AlertPolicyProto.Threshold, _Mapping]] = ..., ascending_order_thresholds: bool = ..., min_allowed_threshold: _Optional[float] = ..., max_allowed_threshold: _Optional[float] = ..., duration: _Optional[_Union[AlertPolicyProto.Duration, _Mapping]] = ..., metric_unit: _Optional[str] = ..., help_text: _Optional[str] = ...) -> None: ...

class AlertPoliciesProto(_message.Message):
    __slots__ = ("version", "alert_policy_proto_vec")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICY_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    version: int
    alert_policy_proto_vec: _containers.RepeatedCompositeFieldContainer[AlertPolicyProto]
    def __init__(self, version: _Optional[int] = ..., alert_policy_proto_vec: _Optional[_Iterable[_Union[AlertPolicyProto, _Mapping]]] = ...) -> None: ...
