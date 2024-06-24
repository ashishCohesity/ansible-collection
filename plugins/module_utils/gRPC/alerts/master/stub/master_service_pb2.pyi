from alerts.base import alert_pb2 as _alert_pb2
from alerts.base import error_pb2 as _error_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterAlertsArg(_message.Message):
    __slots__ = ("alert_metadata_list",)
    ALERT_METADATA_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_metadata_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertMetadataProto]
    def __init__(self, alert_metadata_list: _Optional[_Iterable[_Union[_alert_pb2.AlertMetadataProto, _Mapping]]] = ...) -> None: ...

class RegisterAlertsResult(_message.Message):
    __slots__ = ("error_list",)
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class SendAlertsArg(_message.Message):
    __slots__ = ("alert_list",)
    ALERT_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertProto]
    def __init__(self, alert_list: _Optional[_Iterable[_Union[_alert_pb2.AlertProto, _Mapping]]] = ...) -> None: ...

class SendAlertsResult(_message.Message):
    __slots__ = ("error_list", "alert_id_list")
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    alert_id_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., alert_id_list: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAlertMetadataArg(_message.Message):
    __slots__ = ("alert_type_list",)
    ALERT_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_type_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, alert_type_list: _Optional[_Iterable[int]] = ...) -> None: ...

class GetAlertMetadataResult(_message.Message):
    __slots__ = ("error_list", "alert_metadata_list")
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_METADATA_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    alert_metadata_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertMetadataProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., alert_metadata_list: _Optional[_Iterable[_Union[_alert_pb2.AlertMetadataProto, _Mapping]]] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class AlertQueryFilter(_message.Message):
    __slots__ = ("alert_id_list", "alert_type_list", "alert_category_list", "time_range", "value_filter", "alert_state_list", "alert_severity_list", "resolution_id_list", "max_alerts", "include_hidden_alerts", "include_alerts_marked_for_support_notification", "tenant_id_list", "all_under_hierarchy", "alert_type_bucket_list", "include_alerts_by_resolved_time", "job_id_list")
    class ValueFilter(_message.Message):
        __slots__ = ("property_name", "value")
        PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        property_name: str
        value: str
        def __init__(self, property_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_CATEGORY_LIST_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FILTER_FIELD_NUMBER: _ClassVar[int]
    ALERT_STATE_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_SEVERITY_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    MAX_ALERTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HIDDEN_ALERTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALERTS_MARKED_FOR_SUPPORT_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ALL_UNDER_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_BUCKET_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALERTS_BY_RESOLVED_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_id_list: _containers.RepeatedScalarFieldContainer[str]
    alert_type_list: _containers.RepeatedScalarFieldContainer[int]
    alert_category_list: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertMetadataProto.AlertCategory]
    time_range: TimeRange
    value_filter: _containers.RepeatedCompositeFieldContainer[AlertQueryFilter.ValueFilter]
    alert_state_list: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertProto.AlertState]
    alert_severity_list: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertProto.Severity]
    resolution_id_list: _containers.RepeatedScalarFieldContainer[int]
    max_alerts: int
    include_hidden_alerts: bool
    include_alerts_marked_for_support_notification: bool
    tenant_id_list: _containers.RepeatedScalarFieldContainer[str]
    all_under_hierarchy: bool
    alert_type_bucket_list: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertMetadataProto.AlertTypeBucket]
    include_alerts_by_resolved_time: bool
    job_id_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, alert_id_list: _Optional[_Iterable[str]] = ..., alert_type_list: _Optional[_Iterable[int]] = ..., alert_category_list: _Optional[_Iterable[_Union[_alert_pb2.AlertMetadataProto.AlertCategory, str]]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., value_filter: _Optional[_Iterable[_Union[AlertQueryFilter.ValueFilter, _Mapping]]] = ..., alert_state_list: _Optional[_Iterable[_Union[_alert_pb2.AlertProto.AlertState, str]]] = ..., alert_severity_list: _Optional[_Iterable[_Union[_alert_pb2.AlertProto.Severity, str]]] = ..., resolution_id_list: _Optional[_Iterable[int]] = ..., max_alerts: _Optional[int] = ..., include_hidden_alerts: bool = ..., include_alerts_marked_for_support_notification: bool = ..., tenant_id_list: _Optional[_Iterable[str]] = ..., all_under_hierarchy: bool = ..., alert_type_bucket_list: _Optional[_Iterable[_Union[_alert_pb2.AlertMetadataProto.AlertTypeBucket, str]]] = ..., include_alerts_by_resolved_time: bool = ..., job_id_list: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryAlertsArg(_message.Message):
    __slots__ = ("query_filter", "language_code")
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    query_filter: AlertQueryFilter
    language_code: str
    def __init__(self, query_filter: _Optional[_Union[AlertQueryFilter, _Mapping]] = ..., language_code: _Optional[str] = ...) -> None: ...

class QueryAlertsResult(_message.Message):
    __slots__ = ("error", "alert_list")
    class AlertDetail(_message.Message):
        __slots__ = ("alert", "alert_id", "alert_code", "first_timestamp_usecs", "latest_timestamp_usecs", "alert_category", "resolution_details", "alert_document", "alert_type_bucket", "hidden_from_user", "resolved_timestamp_usecs")
        ALERT_FIELD_NUMBER: _ClassVar[int]
        ALERT_ID_FIELD_NUMBER: _ClassVar[int]
        ALERT_CODE_FIELD_NUMBER: _ClassVar[int]
        FIRST_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        LATEST_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        ALERT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
        ALERT_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        ALERT_TYPE_BUCKET_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FROM_USER_FIELD_NUMBER: _ClassVar[int]
        RESOLVED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        alert: _alert_pb2.AlertProto
        alert_id: str
        alert_code: str
        first_timestamp_usecs: int
        latest_timestamp_usecs: int
        alert_category: _alert_pb2.AlertMetadataProto.AlertCategory
        resolution_details: _alert_pb2.ResolutionProto
        alert_document: _alert_pb2.AlertDocumentProto
        alert_type_bucket: _alert_pb2.AlertMetadataProto.AlertTypeBucket
        hidden_from_user: bool
        resolved_timestamp_usecs: int
        def __init__(self, alert: _Optional[_Union[_alert_pb2.AlertProto, _Mapping]] = ..., alert_id: _Optional[str] = ..., alert_code: _Optional[str] = ..., first_timestamp_usecs: _Optional[int] = ..., latest_timestamp_usecs: _Optional[int] = ..., alert_category: _Optional[_Union[_alert_pb2.AlertMetadataProto.AlertCategory, str]] = ..., resolution_details: _Optional[_Union[_alert_pb2.ResolutionProto, _Mapping]] = ..., alert_document: _Optional[_Union[_alert_pb2.AlertDocumentProto, _Mapping]] = ..., alert_type_bucket: _Optional[_Union[_alert_pb2.AlertMetadataProto.AlertTypeBucket, str]] = ..., hidden_from_user: bool = ..., resolved_timestamp_usecs: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ALERT_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    alert_list: _containers.RepeatedCompositeFieldContainer[QueryAlertsResult.AlertDetail]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., alert_list: _Optional[_Iterable[_Union[QueryAlertsResult.AlertDetail, _Mapping]]] = ...) -> None: ...

class ResolveAlertsArg(_message.Message):
    __slots__ = ("alert_id_list", "resolution", "resolution_id")
    ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    alert_id_list: _containers.RepeatedScalarFieldContainer[str]
    resolution: _alert_pb2.ResolutionProto
    resolution_id: int
    def __init__(self, alert_id_list: _Optional[_Iterable[str]] = ..., resolution: _Optional[_Union[_alert_pb2.ResolutionProto, _Mapping]] = ..., resolution_id: _Optional[int] = ...) -> None: ...

class ResolveAlertsResult(_message.Message):
    __slots__ = ("error_list", "resolution_id")
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    resolution_id: int
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., resolution_id: _Optional[int] = ...) -> None: ...

class ResolutionQueryFilter(_message.Message):
    __slots__ = ("resolution_id_list", "alert_id_list", "time_range", "max_resolutions", "tenant_id_list", "all_under_hierarchy")
    RESOLUTION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ALL_UNDER_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    resolution_id_list: _containers.RepeatedScalarFieldContainer[int]
    alert_id_list: _containers.RepeatedScalarFieldContainer[str]
    time_range: TimeRange
    max_resolutions: int
    tenant_id_list: _containers.RepeatedScalarFieldContainer[str]
    all_under_hierarchy: bool
    def __init__(self, resolution_id_list: _Optional[_Iterable[int]] = ..., alert_id_list: _Optional[_Iterable[str]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., max_resolutions: _Optional[int] = ..., tenant_id_list: _Optional[_Iterable[str]] = ..., all_under_hierarchy: bool = ...) -> None: ...

class QueryResolutionsArg(_message.Message):
    __slots__ = ("query_filter",)
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    query_filter: ResolutionQueryFilter
    def __init__(self, query_filter: _Optional[_Union[ResolutionQueryFilter, _Mapping]] = ...) -> None: ...

class QueryResolutionsResult(_message.Message):
    __slots__ = ("error", "resolution_list")
    class ResolutionDetail(_message.Message):
        __slots__ = ("resolution", "alert_id_list")
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
        resolution: _alert_pb2.ResolutionProto
        alert_id_list: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, resolution: _Optional[_Union[_alert_pb2.ResolutionProto, _Mapping]] = ..., alert_id_list: _Optional[_Iterable[str]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    resolution_list: _containers.RepeatedCompositeFieldContainer[QueryResolutionsResult.ResolutionDetail]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., resolution_list: _Optional[_Iterable[_Union[QueryResolutionsResult.ResolutionDetail, _Mapping]]] = ...) -> None: ...

class DeleteResolutionsArg(_message.Message):
    __slots__ = ("resolution_id_list",)
    RESOLUTION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    resolution_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, resolution_id_list: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteResolutionsResult(_message.Message):
    __slots__ = ("error_list",)
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class CreateSuppressionsArg(_message.Message):
    __slots__ = ("suppress_list",)
    SUPPRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    suppress_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.SuppressionRuleProto]
    def __init__(self, suppress_list: _Optional[_Iterable[_Union[_alert_pb2.SuppressionRuleProto, _Mapping]]] = ...) -> None: ...

class CreateSuppressionsResult(_message.Message):
    __slots__ = ("error_list", "suppression_id_list")
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    suppression_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., suppression_id_list: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteSuppressionsArg(_message.Message):
    __slots__ = ("suppression_id_list",)
    SUPPRESSION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    suppression_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, suppression_id_list: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteSuppressionsResult(_message.Message):
    __slots__ = ("error_list",)
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class SuppressionQueryFilter(_message.Message):
    __slots__ = ("suppression_id_list", "alert_category_list", "alert_type_list", "alert_severity_list", "time_range", "max_suppressions")
    SUPPRESSION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_CATEGORY_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_SEVERITY_LIST_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAX_SUPPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    suppression_id_list: _containers.RepeatedScalarFieldContainer[int]
    alert_category_list: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertMetadataProto.AlertCategory]
    alert_type_list: _containers.RepeatedScalarFieldContainer[int]
    alert_severity_list: _containers.RepeatedScalarFieldContainer[_alert_pb2.AlertProto.Severity]
    time_range: TimeRange
    max_suppressions: int
    def __init__(self, suppression_id_list: _Optional[_Iterable[int]] = ..., alert_category_list: _Optional[_Iterable[_Union[_alert_pb2.AlertMetadataProto.AlertCategory, str]]] = ..., alert_type_list: _Optional[_Iterable[int]] = ..., alert_severity_list: _Optional[_Iterable[_Union[_alert_pb2.AlertProto.Severity, str]]] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., max_suppressions: _Optional[int] = ...) -> None: ...

class QuerySuppressionsArg(_message.Message):
    __slots__ = ("query_filter",)
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    query_filter: SuppressionQueryFilter
    def __init__(self, query_filter: _Optional[_Union[SuppressionQueryFilter, _Mapping]] = ...) -> None: ...

class QuerySuppressionsResult(_message.Message):
    __slots__ = ("error", "suppression_rules_list")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSION_RULES_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    suppression_rules_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.SuppressionRuleProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., suppression_rules_list: _Optional[_Iterable[_Union[_alert_pb2.SuppressionRuleProto, _Mapping]]] = ...) -> None: ...

class UpdateDedupParamsArg(_message.Message):
    __slots__ = ("dedup_rules_list",)
    DEDUP_RULES_LIST_FIELD_NUMBER: _ClassVar[int]
    dedup_rules_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.DedupRuleProto]
    def __init__(self, dedup_rules_list: _Optional[_Iterable[_Union[_alert_pb2.DedupRuleProto, _Mapping]]] = ...) -> None: ...

class UpdateDedupParamsResult(_message.Message):
    __slots__ = ("error_list",)
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class DedupQueryFilter(_message.Message):
    __slots__ = ("alert_type_list", "max_results")
    ALERT_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    alert_type_list: _containers.RepeatedScalarFieldContainer[int]
    max_results: int
    def __init__(self, alert_type_list: _Optional[_Iterable[int]] = ..., max_results: _Optional[int] = ...) -> None: ...

class QueryDedupParamsArg(_message.Message):
    __slots__ = ("query_filter",)
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    query_filter: DedupQueryFilter
    def __init__(self, query_filter: _Optional[_Union[DedupQueryFilter, _Mapping]] = ...) -> None: ...

class QueryDedupParamsResult(_message.Message):
    __slots__ = ("error", "dedup_rules_list")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RULES_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dedup_rules_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.DedupRuleProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dedup_rules_list: _Optional[_Iterable[_Union[_alert_pb2.DedupRuleProto, _Mapping]]] = ...) -> None: ...

class UpdateDeliveryRulesArg(_message.Message):
    __slots__ = ("delivery_rules_list", "op_type")
    class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdd: _ClassVar[UpdateDeliveryRulesArg.OpType]
        kRemove: _ClassVar[UpdateDeliveryRulesArg.OpType]
        kReplace: _ClassVar[UpdateDeliveryRulesArg.OpType]
    kAdd: UpdateDeliveryRulesArg.OpType
    kRemove: UpdateDeliveryRulesArg.OpType
    kReplace: UpdateDeliveryRulesArg.OpType
    DELIVERY_RULES_LIST_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    delivery_rules_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.DeliveryRuleProto]
    op_type: UpdateDeliveryRulesArg.OpType
    def __init__(self, delivery_rules_list: _Optional[_Iterable[_Union[_alert_pb2.DeliveryRuleProto, _Mapping]]] = ..., op_type: _Optional[_Union[UpdateDeliveryRulesArg.OpType, str]] = ...) -> None: ...

class UpdateDeliveryRulesResult(_message.Message):
    __slots__ = ("error_list",)
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class DeliveryQueryFilter(_message.Message):
    __slots__ = ("max_results", "tenant_id_vec")
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    max_results: int
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, max_results: _Optional[int] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryDeliveryRulesArg(_message.Message):
    __slots__ = ("query_filter",)
    QUERY_FILTER_FIELD_NUMBER: _ClassVar[int]
    query_filter: DeliveryQueryFilter
    def __init__(self, query_filter: _Optional[_Union[DeliveryQueryFilter, _Mapping]] = ...) -> None: ...

class QueryDeliveryRulesResult(_message.Message):
    __slots__ = ("error", "delivery_rules_list")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_RULES_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    delivery_rules_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.DeliveryRuleProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delivery_rules_list: _Optional[_Iterable[_Union[_alert_pb2.DeliveryRuleProto, _Mapping]]] = ...) -> None: ...
