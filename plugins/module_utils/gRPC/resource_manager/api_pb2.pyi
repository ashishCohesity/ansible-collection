from resource_manager.base import error_pb2 as _error_pb2
from resource_manager.base import logical_timestamp_pb2 as _logical_timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestorIdProto(_message.Message):
    __slots__ = ("id", "reservation_requestor_id", "parent_requestor_id", "fairness_domain_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    FAIRNESS_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    reservation_requestor_id: str
    parent_requestor_id: str
    fairness_domain_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., reservation_requestor_id: _Optional[str] = ..., parent_requestor_id: _Optional[str] = ..., fairness_domain_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class PriorityProto(_message.Message):
    __slots__ = ("static_priority", "sla_deadline_usecs", "task_start_time_usecs")
    STATIC_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SLA_DEADLINE_USECS_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    static_priority: int
    sla_deadline_usecs: int
    task_start_time_usecs: int
    def __init__(self, static_priority: _Optional[int] = ..., sla_deadline_usecs: _Optional[int] = ..., task_start_time_usecs: _Optional[int] = ...) -> None: ...

class ResourceProviderSpecProto(_message.Message):
    __slots__ = ("id", "resource_map", "attr_map")
    class ResourceMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    class AttrMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MAP_FIELD_NUMBER: _ClassVar[int]
    ATTR_MAP_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource_map: _containers.ScalarMap[str, float]
    attr_map: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., resource_map: _Optional[_Mapping[str, float]] = ..., attr_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ResourceProviderHealthProto(_message.Message):
    __slots__ = ("is_live", "avoid_access")
    IS_LIVE_FIELD_NUMBER: _ClassVar[int]
    AVOID_ACCESS_FIELD_NUMBER: _ClassVar[int]
    is_live: bool
    avoid_access: bool
    def __init__(self, is_live: bool = ..., avoid_access: bool = ...) -> None: ...

class ResourceProviderStatsProto(_message.Message):
    __slots__ = ("resource_type", "slice_vec", "slice_interval_secs")
    class TimeSlice(_message.Message):
        __slots__ = ("weighted_usage", "day_of_the_week_ema_vec")
        WEIGHTED_USAGE_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_THE_WEEK_EMA_VEC_FIELD_NUMBER: _ClassVar[int]
        weighted_usage: float
        day_of_the_week_ema_vec: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, weighted_usage: _Optional[float] = ..., day_of_the_week_ema_vec: _Optional[_Iterable[float]] = ...) -> None: ...
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLICE_VEC_FIELD_NUMBER: _ClassVar[int]
    SLICE_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    slice_vec: _containers.RepeatedCompositeFieldContainer[ResourceProviderStatsProto.TimeSlice]
    slice_interval_secs: int
    def __init__(self, resource_type: _Optional[str] = ..., slice_vec: _Optional[_Iterable[_Union[ResourceProviderStatsProto.TimeSlice, _Mapping]]] = ..., slice_interval_secs: _Optional[int] = ...) -> None: ...

class ResourceRequestSpecProto(_message.Message):
    __slots__ = ("resource_type", "usage_requested", "provider_capacity_multiplier", "is_reservation_request", "provider_attr_map", "root_requestor_max_aggr_usage")
    class ProviderAttrMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USAGE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CAPACITY_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    IS_RESERVATION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ATTR_MAP_FIELD_NUMBER: _ClassVar[int]
    ROOT_REQUESTOR_MAX_AGGR_USAGE_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    usage_requested: float
    provider_capacity_multiplier: float
    is_reservation_request: bool
    provider_attr_map: _containers.ScalarMap[str, str]
    root_requestor_max_aggr_usage: float
    def __init__(self, resource_type: _Optional[str] = ..., usage_requested: _Optional[float] = ..., provider_capacity_multiplier: _Optional[float] = ..., is_reservation_request: bool = ..., provider_attr_map: _Optional[_Mapping[str, str]] = ..., root_requestor_max_aggr_usage: _Optional[float] = ...) -> None: ...

class LockRequestSpecProto(_message.Message):
    __slots__ = ("id", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kShared: _ClassVar[LockRequestSpecProto.Type]
        kExclusive: _ClassVar[LockRequestSpecProto.Type]
    kShared: LockRequestSpecProto.Type
    kExclusive: LockRequestSpecProto.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: LockRequestSpecProto.Type
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[LockRequestSpecProto.Type, str]] = ...) -> None: ...

class ResourceGrant(_message.Message):
    __slots__ = ("resource_type", "provider_id")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    provider_id: str
    def __init__(self, resource_type: _Optional[str] = ..., provider_id: _Optional[str] = ...) -> None: ...

class ResultBaseProto(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AcquireOptions(_message.Message):
    __slots__ = ("timeout_duration_secs", "skip_grant_notification", "defer_missing_provider_error", "reject_duplicate_reservations_across_requests")
    TIMEOUT_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    SKIP_GRANT_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEFER_MISSING_PROVIDER_ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECT_DUPLICATE_RESERVATIONS_ACROSS_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    timeout_duration_secs: int
    skip_grant_notification: bool
    defer_missing_provider_error: bool
    reject_duplicate_reservations_across_requests: bool
    def __init__(self, timeout_duration_secs: _Optional[int] = ..., skip_grant_notification: bool = ..., defer_missing_provider_error: bool = ..., reject_duplicate_reservations_across_requests: bool = ...) -> None: ...

class AcquireArg(_message.Message):
    __slots__ = ("requestor_id", "priority", "resource_request_vec", "lock_request_vec", "attachment", "options", "logical_timestamp")
    REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCK_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    requestor_id: RequestorIdProto
    priority: PriorityProto
    resource_request_vec: _containers.RepeatedCompositeFieldContainer[ResourceRequestSpecProto]
    lock_request_vec: _containers.RepeatedCompositeFieldContainer[LockRequestSpecProto]
    attachment: bytes
    options: AcquireOptions
    logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
    def __init__(self, requestor_id: _Optional[_Union[RequestorIdProto, _Mapping]] = ..., priority: _Optional[_Union[PriorityProto, _Mapping]] = ..., resource_request_vec: _Optional[_Iterable[_Union[ResourceRequestSpecProto, _Mapping]]] = ..., lock_request_vec: _Optional[_Iterable[_Union[LockRequestSpecProto, _Mapping]]] = ..., attachment: _Optional[bytes] = ..., options: _Optional[_Union[AcquireOptions, _Mapping]] = ..., logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ...) -> None: ...

class GrantProto(_message.Message):
    __slots__ = ("error", "requestor_id", "resource_grant_vec", "acquired_lock_id_vec", "attachment")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GRANT_VEC_FIELD_NUMBER: _ClassVar[int]
    ACQUIRED_LOCK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    requestor_id: RequestorIdProto
    resource_grant_vec: _containers.RepeatedCompositeFieldContainer[ResourceGrant]
    acquired_lock_id_vec: _containers.RepeatedScalarFieldContainer[str]
    attachment: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., requestor_id: _Optional[_Union[RequestorIdProto, _Mapping]] = ..., resource_grant_vec: _Optional[_Iterable[_Union[ResourceGrant, _Mapping]]] = ..., acquired_lock_id_vec: _Optional[_Iterable[str]] = ..., attachment: _Optional[bytes] = ...) -> None: ...

class AcquireResult(_message.Message):
    __slots__ = ("base", "grant")
    BASE_FIELD_NUMBER: _ClassVar[int]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    grant: GrantProto
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ..., grant: _Optional[_Union[GrantProto, _Mapping]] = ...) -> None: ...

class ReleaseArg(_message.Message):
    __slots__ = ("requestor_id", "resource_type_vec", "lock_id_vec", "logical_timestamp")
    REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    requestor_id: RequestorIdProto
    resource_type_vec: _containers.RepeatedScalarFieldContainer[str]
    lock_id_vec: _containers.RepeatedScalarFieldContainer[str]
    logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
    def __init__(self, requestor_id: _Optional[_Union[RequestorIdProto, _Mapping]] = ..., resource_type_vec: _Optional[_Iterable[str]] = ..., lock_id_vec: _Optional[_Iterable[str]] = ..., logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ...) -> None: ...

class ReleaseResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ...) -> None: ...

class AddOrUpdateProvidersArg(_message.Message):
    __slots__ = ("add_update_provider_vec", "delete_provider_vec")
    class Provider(_message.Message):
        __slots__ = ("id", "health", "spec")
        ID_FIELD_NUMBER: _ClassVar[int]
        HEALTH_FIELD_NUMBER: _ClassVar[int]
        SPEC_FIELD_NUMBER: _ClassVar[int]
        id: str
        health: ResourceProviderHealthProto
        spec: ResourceProviderSpecProto
        def __init__(self, id: _Optional[str] = ..., health: _Optional[_Union[ResourceProviderHealthProto, _Mapping]] = ..., spec: _Optional[_Union[ResourceProviderSpecProto, _Mapping]] = ...) -> None: ...
    ADD_UPDATE_PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
    add_update_provider_vec: _containers.RepeatedCompositeFieldContainer[AddOrUpdateProvidersArg.Provider]
    delete_provider_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, add_update_provider_vec: _Optional[_Iterable[_Union[AddOrUpdateProvidersArg.Provider, _Mapping]]] = ..., delete_provider_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class AddOrUpdateProvidersResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ...) -> None: ...

class LookupProvidersArg(_message.Message):
    __slots__ = ("provider_id_vec", "attr_map", "include_resource_stats")
    class AttrMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTR_MAP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RESOURCE_STATS_FIELD_NUMBER: _ClassVar[int]
    provider_id_vec: _containers.RepeatedScalarFieldContainer[str]
    attr_map: _containers.ScalarMap[str, str]
    include_resource_stats: bool
    def __init__(self, provider_id_vec: _Optional[_Iterable[str]] = ..., attr_map: _Optional[_Mapping[str, str]] = ..., include_resource_stats: bool = ...) -> None: ...

class LookupProvidersResult(_message.Message):
    __slots__ = ("base", "provider_vec")
    class Provider(_message.Message):
        __slots__ = ("id", "error", "spec", "health", "stats")
        ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        SPEC_FIELD_NUMBER: _ClassVar[int]
        HEALTH_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        id: str
        error: _error_pb2.ErrorProto
        spec: ResourceProviderSpecProto
        health: ResourceProviderHealthProto
        stats: _containers.RepeatedCompositeFieldContainer[ResourceProviderStatsProto]
        def __init__(self, id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., spec: _Optional[_Union[ResourceProviderSpecProto, _Mapping]] = ..., health: _Optional[_Union[ResourceProviderHealthProto, _Mapping]] = ..., stats: _Optional[_Iterable[_Union[ResourceProviderStatsProto, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    provider_vec: _containers.RepeatedCompositeFieldContainer[LookupProvidersResult.Provider]
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ..., provider_vec: _Optional[_Iterable[_Union[LookupProvidersResult.Provider, _Mapping]]] = ...) -> None: ...

class ForceGcArg(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class ForceGcResult(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ...) -> None: ...

class LookupRequestorsArg(_message.Message):
    __slots__ = ("requestor_id_vec", "requestor_id_substring")
    REQUESTOR_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_ID_SUBSTRING_FIELD_NUMBER: _ClassVar[int]
    requestor_id_vec: _containers.RepeatedScalarFieldContainer[str]
    requestor_id_substring: str
    def __init__(self, requestor_id_vec: _Optional[_Iterable[str]] = ..., requestor_id_substring: _Optional[str] = ...) -> None: ...

class LookupRequestorsResult(_message.Message):
    __slots__ = ("base", "requestor_vec")
    class ResourceRequestInfo(_message.Message):
        __slots__ = ("spec", "target_resource_provider_id", "release_timestamp_usecs", "reservation_request_deduped")
        SPEC_FIELD_NUMBER: _ClassVar[int]
        TARGET_RESOURCE_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        RELEASE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_REQUEST_DEDUPED_FIELD_NUMBER: _ClassVar[int]
        spec: ResourceRequestSpecProto
        target_resource_provider_id: str
        release_timestamp_usecs: int
        reservation_request_deduped: bool
        def __init__(self, spec: _Optional[_Union[ResourceRequestSpecProto, _Mapping]] = ..., target_resource_provider_id: _Optional[str] = ..., release_timestamp_usecs: _Optional[int] = ..., reservation_request_deduped: bool = ...) -> None: ...
    class LockRequestInfo(_message.Message):
        __slots__ = ("spec", "release_timestamp_usecs")
        SPEC_FIELD_NUMBER: _ClassVar[int]
        RELEASE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        spec: LockRequestSpecProto
        release_timestamp_usecs: int
        def __init__(self, spec: _Optional[_Union[LockRequestSpecProto, _Mapping]] = ..., release_timestamp_usecs: _Optional[int] = ...) -> None: ...
    class RequestStateInfo(_message.Message):
        __slots__ = ("resource_vec", "lock_vec")
        RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
        LOCK_VEC_FIELD_NUMBER: _ClassVar[int]
        resource_vec: _containers.RepeatedCompositeFieldContainer[LookupRequestorsResult.ResourceRequestInfo]
        lock_vec: _containers.RepeatedCompositeFieldContainer[LookupRequestorsResult.LockRequestInfo]
        def __init__(self, resource_vec: _Optional[_Iterable[_Union[LookupRequestorsResult.ResourceRequestInfo, _Mapping]]] = ..., lock_vec: _Optional[_Iterable[_Union[LookupRequestorsResult.LockRequestInfo, _Mapping]]] = ...) -> None: ...
    class Requestor(_message.Message):
        __slots__ = ("id", "error", "granted_or_released_request_state_vec", "outstanding_request_state")
        ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        GRANTED_OR_RELEASED_REQUEST_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
        OUTSTANDING_REQUEST_STATE_FIELD_NUMBER: _ClassVar[int]
        id: str
        error: _error_pb2.ErrorProto
        granted_or_released_request_state_vec: _containers.RepeatedCompositeFieldContainer[LookupRequestorsResult.RequestStateInfo]
        outstanding_request_state: LookupRequestorsResult.RequestStateInfo
        def __init__(self, id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., granted_or_released_request_state_vec: _Optional[_Iterable[_Union[LookupRequestorsResult.RequestStateInfo, _Mapping]]] = ..., outstanding_request_state: _Optional[_Union[LookupRequestorsResult.RequestStateInfo, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    requestor_vec: _containers.RepeatedCompositeFieldContainer[LookupRequestorsResult.Requestor]
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ..., requestor_vec: _Optional[_Iterable[_Union[LookupRequestorsResult.Requestor, _Mapping]]] = ...) -> None: ...

class SendHeartbeatArg(_message.Message):
    __slots__ = ("heartbeat_request_vec",)
    class HeartbeatRequest(_message.Message):
        __slots__ = ("requestor_id", "heartbeat_timestamp_usecs", "extend_resource_ttl_duration_usecs")
        REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
        HEARTBEAT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        EXTEND_RESOURCE_TTL_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
        requestor_id: str
        heartbeat_timestamp_usecs: int
        extend_resource_ttl_duration_usecs: int
        def __init__(self, requestor_id: _Optional[str] = ..., heartbeat_timestamp_usecs: _Optional[int] = ..., extend_resource_ttl_duration_usecs: _Optional[int] = ...) -> None: ...
    HEARTBEAT_REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    heartbeat_request_vec: _containers.RepeatedCompositeFieldContainer[SendHeartbeatArg.HeartbeatRequest]
    def __init__(self, heartbeat_request_vec: _Optional[_Iterable[_Union[SendHeartbeatArg.HeartbeatRequest, _Mapping]]] = ...) -> None: ...

class SendHeartbeatResult(_message.Message):
    __slots__ = ("base", "heartbeat_result_vec")
    class HeartbeatResult(_message.Message):
        __slots__ = ("requestor_id", "error")
        REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        requestor_id: str
        error: _error_pb2.ErrorProto
        def __init__(self, requestor_id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: ResultBaseProto
    heartbeat_result_vec: _containers.RepeatedCompositeFieldContainer[SendHeartbeatResult.HeartbeatResult]
    def __init__(self, base: _Optional[_Union[ResultBaseProto, _Mapping]] = ..., heartbeat_result_vec: _Optional[_Iterable[_Union[SendHeartbeatResult.HeartbeatResult, _Mapping]]] = ...) -> None: ...
