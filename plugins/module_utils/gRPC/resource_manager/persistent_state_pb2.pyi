from resource_manager import api_pb2 as _api_pb2
from resource_manager.base import logical_timestamp_pb2 as _logical_timestamp_pb2
from resource_manager.base import versions_pb2 as _versions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceRequestStateProto(_message.Message):
    __slots__ = ("spec", "target_resource_provider_id", "quantity_granted_from_reserved_pool", "quantity_granted", "release_timestamp_usecs", "reservation_request_deduped")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_GRANTED_FROM_RESERVED_POOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_GRANTED_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_REQUEST_DEDUPED_FIELD_NUMBER: _ClassVar[int]
    spec: _api_pb2.ResourceRequestSpecProto
    target_resource_provider_id: str
    quantity_granted_from_reserved_pool: float
    quantity_granted: float
    release_timestamp_usecs: int
    reservation_request_deduped: bool
    def __init__(self, spec: _Optional[_Union[_api_pb2.ResourceRequestSpecProto, _Mapping]] = ..., target_resource_provider_id: _Optional[str] = ..., quantity_granted_from_reserved_pool: _Optional[float] = ..., quantity_granted: _Optional[float] = ..., release_timestamp_usecs: _Optional[int] = ..., reservation_request_deduped: bool = ...) -> None: ...

class LockRequestStateProto(_message.Message):
    __slots__ = ("spec", "release_timestamp_usecs")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    spec: _api_pb2.LockRequestSpecProto
    release_timestamp_usecs: int
    def __init__(self, spec: _Optional[_Union[_api_pb2.LockRequestSpecProto, _Mapping]] = ..., release_timestamp_usecs: _Optional[int] = ...) -> None: ...

class RequestStateProto(_message.Message):
    __slots__ = ("resource_vec", "lock_vec", "priority", "requestor_id", "options", "attachment", "received_timestamp_usecs", "granted_timestamp_usecs", "grant_notified", "timedout_timestamp_usecs", "cancelled_timestamp_usecs", "latest_logical_timestamp", "timed_out_DEPRECATED", "cancelled_DEPRECATED")
    RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    LOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    GRANT_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    TIMEDOUT_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LATEST_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMED_OUT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    resource_vec: _containers.RepeatedCompositeFieldContainer[ResourceRequestStateProto]
    lock_vec: _containers.RepeatedCompositeFieldContainer[LockRequestStateProto]
    priority: _api_pb2.PriorityProto
    requestor_id: _api_pb2.RequestorIdProto
    options: _api_pb2.AcquireOptions
    attachment: bytes
    received_timestamp_usecs: int
    granted_timestamp_usecs: int
    grant_notified: bool
    timedout_timestamp_usecs: int
    cancelled_timestamp_usecs: int
    latest_logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
    timed_out_DEPRECATED: bool
    cancelled_DEPRECATED: bool
    def __init__(self, resource_vec: _Optional[_Iterable[_Union[ResourceRequestStateProto, _Mapping]]] = ..., lock_vec: _Optional[_Iterable[_Union[LockRequestStateProto, _Mapping]]] = ..., priority: _Optional[_Union[_api_pb2.PriorityProto, _Mapping]] = ..., requestor_id: _Optional[_Union[_api_pb2.RequestorIdProto, _Mapping]] = ..., options: _Optional[_Union[_api_pb2.AcquireOptions, _Mapping]] = ..., attachment: _Optional[bytes] = ..., received_timestamp_usecs: _Optional[int] = ..., granted_timestamp_usecs: _Optional[int] = ..., grant_notified: bool = ..., timedout_timestamp_usecs: _Optional[int] = ..., cancelled_timestamp_usecs: _Optional[int] = ..., latest_logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ..., timed_out_DEPRECATED: bool = ..., cancelled_DEPRECATED: bool = ...) -> None: ...

class ResourceProviderStateProto(_message.Message):
    __slots__ = ("spec", "health")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    spec: _api_pb2.ResourceProviderSpecProto
    health: _api_pb2.ResourceProviderHealthProto
    def __init__(self, spec: _Optional[_Union[_api_pb2.ResourceProviderSpecProto, _Mapping]] = ..., health: _Optional[_Union[_api_pb2.ResourceProviderHealthProto, _Mapping]] = ...) -> None: ...

class ResourceManagerWALRecordProto(_message.Message):
    __slots__ = ("api_version", "persistent_state_proto_vec", "provider_vec", "remove_provider_id_vec", "provider_health_update_vec", "request_vec", "release_info", "ignored_delta_record_limit")
    class ProviderHealthUpdateProto(_message.Message):
        __slots__ = ("id", "health")
        ID_FIELD_NUMBER: _ClassVar[int]
        HEALTH_FIELD_NUMBER: _ClassVar[int]
        id: str
        health: _api_pb2.ResourceProviderHealthProto
        def __init__(self, id: _Optional[str] = ..., health: _Optional[_Union[_api_pb2.ResourceProviderHealthProto, _Mapping]] = ...) -> None: ...
    class ReleaseInfoProto(_message.Message):
        __slots__ = ("requestor_id", "resource_type_vec", "lock_id_vec", "release_timestamp_usecs", "cancel_outstanding_request", "logical_timestamp")
        REQUESTOR_ID_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        LOCK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        RELEASE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        CANCEL_OUTSTANDING_REQUEST_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        requestor_id: _api_pb2.RequestorIdProto
        resource_type_vec: _containers.RepeatedScalarFieldContainer[str]
        lock_id_vec: _containers.RepeatedScalarFieldContainer[str]
        release_timestamp_usecs: int
        cancel_outstanding_request: bool
        logical_timestamp: _logical_timestamp_pb2.LogicalTimestamp
        def __init__(self, requestor_id: _Optional[_Union[_api_pb2.RequestorIdProto, _Mapping]] = ..., resource_type_vec: _Optional[_Iterable[str]] = ..., lock_id_vec: _Optional[_Iterable[str]] = ..., release_timestamp_usecs: _Optional[int] = ..., cancel_outstanding_request: bool = ..., logical_timestamp: _Optional[_Union[_logical_timestamp_pb2.LogicalTimestamp, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PROVIDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_HEALTH_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    RELEASE_INFO_FIELD_NUMBER: _ClassVar[int]
    IGNORED_DELTA_RECORD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    api_version: _versions_pb2.VersionProto
    persistent_state_proto_vec: _containers.RepeatedCompositeFieldContainer[ResourceManagerWALRecordProto]
    provider_vec: _containers.RepeatedCompositeFieldContainer[ResourceProviderStateProto]
    remove_provider_id_vec: _containers.RepeatedScalarFieldContainer[str]
    provider_health_update_vec: _containers.RepeatedCompositeFieldContainer[ResourceManagerWALRecordProto.ProviderHealthUpdateProto]
    request_vec: _containers.RepeatedCompositeFieldContainer[RequestStateProto]
    release_info: ResourceManagerWALRecordProto.ReleaseInfoProto
    ignored_delta_record_limit: int
    def __init__(self, api_version: _Optional[_Union[_versions_pb2.VersionProto, _Mapping]] = ..., persistent_state_proto_vec: _Optional[_Iterable[_Union[ResourceManagerWALRecordProto, _Mapping]]] = ..., provider_vec: _Optional[_Iterable[_Union[ResourceProviderStateProto, _Mapping]]] = ..., remove_provider_id_vec: _Optional[_Iterable[str]] = ..., provider_health_update_vec: _Optional[_Iterable[_Union[ResourceManagerWALRecordProto.ProviderHealthUpdateProto, _Mapping]]] = ..., request_vec: _Optional[_Iterable[_Union[RequestStateProto, _Mapping]]] = ..., release_info: _Optional[_Union[ResourceManagerWALRecordProto.ReleaseInfoProto, _Mapping]] = ..., ignored_delta_record_limit: _Optional[int] = ...) -> None: ...
