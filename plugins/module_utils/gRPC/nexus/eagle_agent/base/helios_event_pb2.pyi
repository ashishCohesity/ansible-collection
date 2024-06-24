from alerts.base import alert_pb2 as _alert_pb2
from alerts.master.stub import master_service_pb2 as _master_service_pb2
from nexus.eagle_agent.base import helios_cluster_base_pb2 as _helios_cluster_base_pb2
from helios.base import helios_cluster_base_pb2 as _helios_cluster_base_pb2_1
from nexus.base import services_gflags_pb2 as _services_gflags_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ("event_uuid", "cluster_identifier", "type", "event_name", "source", "occurrence_timestamp_usecs", "processed_timestamp", "visible_to_user", "alert_instance", "category", "alert_state", "processor", "additional_data", "gflag_instance", "error_details", "node_info", "cluster_name")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAlert: _ClassVar[Event.EventType]
        kNotification: _ClassVar[Event.EventType]
        kClusterSoftwareUpgrade: _ClassVar[Event.EventType]
        kGflags: _ClassVar[Event.EventType]
        kError: _ClassVar[Event.EventType]
    kAlert: Event.EventType
    kNotification: Event.EventType
    kClusterSoftwareUpgrade: Event.EventType
    kGflags: Event.EventType
    kError: Event.EventType
    class EventHostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Event.EventHostType]
        kHelios: _ClassVar[Event.EventHostType]
    kCluster: Event.EventHostType
    kHelios: Event.EventHostType
    class EventCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSystemEvent: _ClassVar[Event.EventCategory]
    kSystemEvent: Event.EventCategory
    EVENT_UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_TO_USER_FIELD_NUMBER: _ClassVar[int]
    ALERT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ALERT_STATE_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    GFLAG_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    event_uuid: str
    cluster_identifier: _helios_cluster_base_pb2_1.ClusterIdentifier
    type: Event.EventType
    event_name: str
    source: Event.EventHostType
    occurrence_timestamp_usecs: int
    processed_timestamp: str
    visible_to_user: bool
    alert_instance: _master_service_pb2.QueryAlertsResult.AlertDetail
    category: Event.EventCategory
    alert_state: _alert_pb2.AlertProto.AlertState
    processor: Event.EventHostType
    additional_data: bytes
    gflag_instance: _services_gflags_pb2.ServicesGflagsProto.ServiceProto.Gflag
    error_details: ErrorDetails
    node_info: str
    cluster_name: str
    def __init__(self, event_uuid: _Optional[str] = ..., cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2_1.ClusterIdentifier, _Mapping]] = ..., type: _Optional[_Union[Event.EventType, str]] = ..., event_name: _Optional[str] = ..., source: _Optional[_Union[Event.EventHostType, str]] = ..., occurrence_timestamp_usecs: _Optional[int] = ..., processed_timestamp: _Optional[str] = ..., visible_to_user: bool = ..., alert_instance: _Optional[_Union[_master_service_pb2.QueryAlertsResult.AlertDetail, _Mapping]] = ..., category: _Optional[_Union[Event.EventCategory, str]] = ..., alert_state: _Optional[_Union[_alert_pb2.AlertProto.AlertState, str]] = ..., processor: _Optional[_Union[Event.EventHostType, str]] = ..., additional_data: _Optional[bytes] = ..., gflag_instance: _Optional[_Union[_services_gflags_pb2.ServicesGflagsProto.ServiceProto.Gflag, _Mapping]] = ..., error_details: _Optional[_Union[ErrorDetails, _Mapping]] = ..., node_info: _Optional[str] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class ErrorDetails(_message.Message):
    __slots__ = ("service_name", "op_name", "object_name", "object", "error_message")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    OP_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    op_name: str
    object_name: str
    object: bytes
    error_message: str
    def __init__(self, service_name: _Optional[str] = ..., op_name: _Optional[str] = ..., object_name: _Optional[str] = ..., object: _Optional[bytes] = ..., error_message: _Optional[str] = ...) -> None: ...

class AuditLogId(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AuditSourceInfo(_message.Message):
    __slots__ = ("cluster_identifier", "user_name", "user_id", "service_name")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _helios_cluster_base_pb2_1.ClusterIdentifier
    user_name: str
    user_id: int
    service_name: str
    def __init__(self, cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2_1.ClusterIdentifier, _Mapping]] = ..., user_name: _Optional[str] = ..., user_id: _Optional[int] = ..., service_name: _Optional[str] = ...) -> None: ...

class AuditLogProto(_message.Message):
    __slots__ = ("audit_log_id", "audit_source_info", "timestamp_usecs", "audit_type", "resource_type", "entity_type_vec", "additional_details")
    class AuditType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[AuditLogProto.AuditType]
        kDeleted: _ClassVar[AuditLogProto.AuditType]
        kUpdated: _ClassVar[AuditLogProto.AuditType]
        kUnregister: _ClassVar[AuditLogProto.AuditType]
        kUpgrade: _ClassVar[AuditLogProto.AuditType]
        kTimeout: _ClassVar[AuditLogProto.AuditType]
        kClusterAuditDocument: _ClassVar[AuditLogProto.AuditType]
        kHeliosAuditDocument: _ClassVar[AuditLogProto.AuditType]
    kCreated: AuditLogProto.AuditType
    kDeleted: AuditLogProto.AuditType
    kUpdated: AuditLogProto.AuditType
    kUnregister: AuditLogProto.AuditType
    kUpgrade: AuditLogProto.AuditType
    kTimeout: AuditLogProto.AuditType
    kClusterAuditDocument: AuditLogProto.AuditType
    kHeliosAuditDocument: AuditLogProto.AuditType
    class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGrpcConn: _ClassVar[AuditLogProto.ResourceType]
        kGrpcPBConn: _ClassVar[AuditLogProto.ResourceType]
        kCluster: _ClassVar[AuditLogProto.ResourceType]
    kGrpcConn: AuditLogProto.ResourceType
    kGrpcPBConn: AuditLogProto.ResourceType
    kCluster: AuditLogProto.ResourceType
    AUDIT_LOG_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIT_SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    audit_log_id: AuditLogId
    audit_source_info: AuditSourceInfo
    timestamp_usecs: int
    audit_type: AuditLogProto.AuditType
    resource_type: AuditLogProto.ResourceType
    entity_type_vec: _containers.RepeatedScalarFieldContainer[str]
    additional_details: str
    def __init__(self, audit_log_id: _Optional[_Union[AuditLogId, _Mapping]] = ..., audit_source_info: _Optional[_Union[AuditSourceInfo, _Mapping]] = ..., timestamp_usecs: _Optional[int] = ..., audit_type: _Optional[_Union[AuditLogProto.AuditType, str]] = ..., resource_type: _Optional[_Union[AuditLogProto.ResourceType, str]] = ..., entity_type_vec: _Optional[_Iterable[str]] = ..., additional_details: _Optional[str] = ...) -> None: ...
