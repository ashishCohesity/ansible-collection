from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditServiceContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDmaas: _ClassVar[AuditServiceContext]
    kSiteContinuity: _ClassVar[AuditServiceContext]
    kFortKnox: _ClassVar[AuditServiceContext]
    kMcm: _ClassVar[AuditServiceContext]
    kCluster: _ClassVar[AuditServiceContext]
    kSiteContinuity2: _ClassVar[AuditServiceContext]
kDmaas: AuditServiceContext
kSiteContinuity: AuditServiceContext
kFortKnox: AuditServiceContext
kMcm: AuditServiceContext
kCluster: AuditServiceContext
kSiteContinuity2: AuditServiceContext

class ClusterAccessAuditDocument(_message.Message):
    __slots__ = ("entity_type", "entity_id", "entity_name", "user_name", "domain_name", "action", "prev_value", "new_value", "change_description", "tenant_id", "original_tenant_id", "ip", "cluster_info", "service_context")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PREV_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    entity_type: str
    entity_id: str
    entity_name: str
    user_name: str
    domain_name: str
    action: str
    prev_value: str
    new_value: str
    change_description: str
    tenant_id: str
    original_tenant_id: str
    ip: str
    cluster_info: str
    service_context: AuditServiceContext
    def __init__(self, entity_type: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., user_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., action: _Optional[str] = ..., prev_value: _Optional[str] = ..., new_value: _Optional[str] = ..., change_description: _Optional[str] = ..., tenant_id: _Optional[str] = ..., original_tenant_id: _Optional[str] = ..., ip: _Optional[str] = ..., cluster_info: _Optional[str] = ..., service_context: _Optional[_Union[AuditServiceContext, str]] = ...) -> None: ...

class ClusterNotificationAuditDocument(_message.Message):
    __slots__ = ("category_type", "category_name", "severity")
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    category_type: str
    category_name: str
    severity: str
    def __init__(self, category_type: _Optional[str] = ..., category_name: _Optional[str] = ..., severity: _Optional[str] = ...) -> None: ...

class ClusterAuditDocument(_message.Message):
    __slots__ = ("timestamp_usecs", "attribute_map", "type", "access_doc", "notification_doc", "elasticsearch_index_name", "elasticsearch_doc_type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAccess: _ClassVar[ClusterAuditDocument.Type]
        kNotification: _ClassVar[ClusterAuditDocument.Type]
        kInternal: _ClassVar[ClusterAuditDocument.Type]
    kAccess: ClusterAuditDocument.Type
    kNotification: ClusterAuditDocument.Type
    kInternal: ClusterAuditDocument.Type
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DOC_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_DOC_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_DOC_TYPE_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    attribute_map: _containers.RepeatedCompositeFieldContainer[ClusterAuditDocument.KeyValuePair]
    type: ClusterAuditDocument.Type
    access_doc: ClusterAccessAuditDocument
    notification_doc: ClusterNotificationAuditDocument
    elasticsearch_index_name: str
    elasticsearch_doc_type: str
    def __init__(self, timestamp_usecs: _Optional[int] = ..., attribute_map: _Optional[_Iterable[_Union[ClusterAuditDocument.KeyValuePair, _Mapping]]] = ..., type: _Optional[_Union[ClusterAuditDocument.Type, str]] = ..., access_doc: _Optional[_Union[ClusterAccessAuditDocument, _Mapping]] = ..., notification_doc: _Optional[_Union[ClusterNotificationAuditDocument, _Mapping]] = ..., elasticsearch_index_name: _Optional[str] = ..., elasticsearch_doc_type: _Optional[str] = ...) -> None: ...

class FormattedClusterAccessAuditDocument(_message.Message):
    __slots__ = ("timestamp", "attribute_map", "entity_type", "entity_id", "entity_name", "user_name", "domain_name", "action", "change_description", "tenant_id", "original_tenant_id", "ip", "cluster_info", "prev_value", "new_value", "service_context")
    class KeyValuePair(_message.Message):
        __slots__ = ("_key", "_value")
        _KEY_FIELD_NUMBER: _ClassVar[int]
        _VALUE_FIELD_NUMBER: _ClassVar[int]
        _key: str
        _value: str
        def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CHANGE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    PREV_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    attribute_map: _containers.RepeatedCompositeFieldContainer[FormattedClusterAccessAuditDocument.KeyValuePair]
    entity_type: str
    entity_id: str
    entity_name: str
    user_name: str
    domain_name: str
    action: str
    change_description: str
    tenant_id: str
    original_tenant_id: str
    ip: str
    cluster_info: str
    prev_value: str
    new_value: str
    service_context: AuditServiceContext
    def __init__(self, timestamp: _Optional[str] = ..., attribute_map: _Optional[_Iterable[_Union[FormattedClusterAccessAuditDocument.KeyValuePair, _Mapping]]] = ..., entity_type: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., user_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., action: _Optional[str] = ..., change_description: _Optional[str] = ..., tenant_id: _Optional[str] = ..., original_tenant_id: _Optional[str] = ..., ip: _Optional[str] = ..., cluster_info: _Optional[str] = ..., prev_value: _Optional[str] = ..., new_value: _Optional[str] = ..., service_context: _Optional[_Union[AuditServiceContext, str]] = ...) -> None: ...
