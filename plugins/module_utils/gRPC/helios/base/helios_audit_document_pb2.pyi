from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosAuditServiceContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDmaas: _ClassVar[HeliosAuditServiceContext]
    kSiteContinuity: _ClassVar[HeliosAuditServiceContext]
    kFortKnox: _ClassVar[HeliosAuditServiceContext]
    kMcm: _ClassVar[HeliosAuditServiceContext]
    kCluster: _ClassVar[HeliosAuditServiceContext]
    kDataGovern: _ClassVar[HeliosAuditServiceContext]
    kSiteContinuity2: _ClassVar[HeliosAuditServiceContext]
kDmaas: HeliosAuditServiceContext
kSiteContinuity: HeliosAuditServiceContext
kFortKnox: HeliosAuditServiceContext
kMcm: HeliosAuditServiceContext
kCluster: HeliosAuditServiceContext
kDataGovern: HeliosAuditServiceContext
kSiteContinuity2: HeliosAuditServiceContext

class AccessAuditDocument(_message.Message):
    __slots__ = ("entity_type", "entity_id", "entity_name", "user_name", "domain_name", "action", "prev_value", "new_value", "change_description", "tenant_id", "original_tenant_id", "ip", "cluster_id", "cluster_incarnation_id", "cluster_name", "tenant_name", "original_tenant_name", "account_id", "service_context")
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
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
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
    cluster_id: str
    cluster_incarnation_id: str
    cluster_name: str
    tenant_name: str
    original_tenant_name: str
    account_id: str
    service_context: HeliosAuditServiceContext
    def __init__(self, entity_type: _Optional[str] = ..., entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., user_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., action: _Optional[str] = ..., prev_value: _Optional[str] = ..., new_value: _Optional[str] = ..., change_description: _Optional[str] = ..., tenant_id: _Optional[str] = ..., original_tenant_id: _Optional[str] = ..., ip: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_incarnation_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., tenant_name: _Optional[str] = ..., original_tenant_name: _Optional[str] = ..., account_id: _Optional[str] = ..., service_context: _Optional[_Union[HeliosAuditServiceContext, str]] = ...) -> None: ...

class HeliosAuditDocument(_message.Message):
    __slots__ = ("timestamp_usecs", "attribute_map", "type", "access_audit_doc")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kClusterAccess: _ClassVar[HeliosAuditDocument.Type]
        kHeliosAccess: _ClassVar[HeliosAuditDocument.Type]
        kServiceAccess: _ClassVar[HeliosAuditDocument.Type]
    kClusterAccess: HeliosAuditDocument.Type
    kHeliosAccess: HeliosAuditDocument.Type
    kServiceAccess: HeliosAuditDocument.Type
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
    ACCESS_AUDIT_DOC_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    attribute_map: _containers.RepeatedCompositeFieldContainer[HeliosAuditDocument.KeyValuePair]
    type: HeliosAuditDocument.Type
    access_audit_doc: AccessAuditDocument
    def __init__(self, timestamp_usecs: _Optional[int] = ..., attribute_map: _Optional[_Iterable[_Union[HeliosAuditDocument.KeyValuePair, _Mapping]]] = ..., type: _Optional[_Union[HeliosAuditDocument.Type, str]] = ..., access_audit_doc: _Optional[_Union[AccessAuditDocument, _Mapping]] = ...) -> None: ...

class HeliosAuditDocumentBatch(_message.Message):
    __slots__ = ("audit_log_list",)
    AUDIT_LOG_LIST_FIELD_NUMBER: _ClassVar[int]
    audit_log_list: _containers.RepeatedCompositeFieldContainer[HeliosAuditDocument]
    def __init__(self, audit_log_list: _Optional[_Iterable[_Union[HeliosAuditDocument, _Mapping]]] = ...) -> None: ...
