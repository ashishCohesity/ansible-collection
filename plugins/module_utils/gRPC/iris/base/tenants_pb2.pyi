from configs import cluster_config_pb2 as _cluster_config_pb2
from iris.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tenant(_message.Message):
    __slots__ = ("tenant_id", "name", "description", "parent_tenant_id", "active", "created_time_msecs", "last_updated_time_msecs", "preferences", "subscribe_to_alert_emails", "deleted", "deleted_time_msecs", "deletion_info_vec", "finished_tenant_migrations", "active_tenant_migration", "object_deletion_required", "certificate_version", "bifrost_enabled", "deletion_finished", "cluster_hostname", "cluster_ip_vec", "ip_whitelist_vec", "reverse_tunnel_private_key", "reverse_tunnel_public_key", "reverse_tunnel_key_version", "realm_ids_vec", "default_realm_id_for_hyx_tenant", "bifrost_cert", "bifrost_cert_priv_key_encrypted", "internal_bifrost_enabled", "is_managed_on_helios", "is_tenant_migration_in_progress", "is_gcm_enabled", "deny_embedded_agent_cert")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARENT_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TO_ALERT_EMAILS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DELETION_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TENANT_MIGRATIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TENANT_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DELETION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BIFROST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DELETION_FINISHED_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    IP_WHITELIST_VEC_FIELD_NUMBER: _ClassVar[int]
    REVERSE_TUNNEL_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    REVERSE_TUNNEL_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    REVERSE_TUNNEL_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    REALM_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REALM_ID_FOR_HYX_TENANT_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CERT_FIELD_NUMBER: _ClassVar[int]
    BIFROST_CERT_PRIV_KEY_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_BIFROST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_MANAGED_ON_HELIOS_FIELD_NUMBER: _ClassVar[int]
    IS_TENANT_MIGRATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_GCM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DENY_EMBEDDED_AGENT_CERT_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    name: str
    description: str
    parent_tenant_id: str
    active: bool
    created_time_msecs: int
    last_updated_time_msecs: int
    preferences: TenantPreferences
    subscribe_to_alert_emails: bool
    deleted: bool
    deleted_time_msecs: int
    deletion_info_vec: _containers.RepeatedCompositeFieldContainer[TenantDeletionInfo]
    finished_tenant_migrations: _containers.RepeatedCompositeFieldContainer[TenantMigrationStatus]
    active_tenant_migration: TenantMigrationStatus
    object_deletion_required: bool
    certificate_version: int
    bifrost_enabled: bool
    deletion_finished: bool
    cluster_hostname: str
    cluster_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    ip_whitelist_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    reverse_tunnel_private_key: bytes
    reverse_tunnel_public_key: bytes
    reverse_tunnel_key_version: int
    realm_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    default_realm_id_for_hyx_tenant: int
    bifrost_cert: str
    bifrost_cert_priv_key_encrypted: bytes
    internal_bifrost_enabled: bool
    is_managed_on_helios: bool
    is_tenant_migration_in_progress: bool
    is_gcm_enabled: bool
    deny_embedded_agent_cert: bool
    def __init__(self, tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., parent_tenant_id: _Optional[str] = ..., active: bool = ..., created_time_msecs: _Optional[int] = ..., last_updated_time_msecs: _Optional[int] = ..., preferences: _Optional[_Union[TenantPreferences, _Mapping]] = ..., subscribe_to_alert_emails: bool = ..., deleted: bool = ..., deleted_time_msecs: _Optional[int] = ..., deletion_info_vec: _Optional[_Iterable[_Union[TenantDeletionInfo, _Mapping]]] = ..., finished_tenant_migrations: _Optional[_Iterable[_Union[TenantMigrationStatus, _Mapping]]] = ..., active_tenant_migration: _Optional[_Union[TenantMigrationStatus, _Mapping]] = ..., object_deletion_required: bool = ..., certificate_version: _Optional[int] = ..., bifrost_enabled: bool = ..., deletion_finished: bool = ..., cluster_hostname: _Optional[str] = ..., cluster_ip_vec: _Optional[_Iterable[str]] = ..., ip_whitelist_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., reverse_tunnel_private_key: _Optional[bytes] = ..., reverse_tunnel_public_key: _Optional[bytes] = ..., reverse_tunnel_key_version: _Optional[int] = ..., realm_ids_vec: _Optional[_Iterable[int]] = ..., default_realm_id_for_hyx_tenant: _Optional[int] = ..., bifrost_cert: _Optional[str] = ..., bifrost_cert_priv_key_encrypted: _Optional[bytes] = ..., internal_bifrost_enabled: bool = ..., is_managed_on_helios: bool = ..., is_tenant_migration_in_progress: bool = ..., is_gcm_enabled: bool = ..., deny_embedded_agent_cert: bool = ...) -> None: ...

class TenantDeletionInfo(_message.Message):
    __slots__ = ("category", "state", "started_at_time_msecs", "finished_at_time_msecs", "processed_at_node", "retry_count")
    class ObjectCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ProtectionJobs: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Views: _ClassVar[TenantDeletionInfo.ObjectCategory]
        ProtectionSources: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Users: _ClassVar[TenantDeletionInfo.ObjectCategory]
        ProtectionPolicies: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Groups: _ClassVar[TenantDeletionInfo.ObjectCategory]
        ActiveDirectories: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Ldap: _ClassVar[TenantDeletionInfo.ObjectCategory]
        RecoveryTask: _ClassVar[TenantDeletionInfo.ObjectCategory]
        RemoteClusters: _ClassVar[TenantDeletionInfo.ObjectCategory]
        StorageDomains: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Alerts: _ClassVar[TenantDeletionInfo.ObjectCategory]
        ReportingSchedules: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Idps: _ClassVar[TenantDeletionInfo.ObjectCategory]
        Swift: _ClassVar[TenantDeletionInfo.ObjectCategory]
        ExternalTargets: _ClassVar[TenantDeletionInfo.ObjectCategory]
        HyxConnectors: _ClassVar[TenantDeletionInfo.ObjectCategory]
        HyxRealms: _ClassVar[TenantDeletionInfo.ObjectCategory]
    ProtectionJobs: TenantDeletionInfo.ObjectCategory
    Views: TenantDeletionInfo.ObjectCategory
    ProtectionSources: TenantDeletionInfo.ObjectCategory
    Users: TenantDeletionInfo.ObjectCategory
    ProtectionPolicies: TenantDeletionInfo.ObjectCategory
    Groups: TenantDeletionInfo.ObjectCategory
    ActiveDirectories: TenantDeletionInfo.ObjectCategory
    Ldap: TenantDeletionInfo.ObjectCategory
    RecoveryTask: TenantDeletionInfo.ObjectCategory
    RemoteClusters: TenantDeletionInfo.ObjectCategory
    StorageDomains: TenantDeletionInfo.ObjectCategory
    Alerts: TenantDeletionInfo.ObjectCategory
    ReportingSchedules: TenantDeletionInfo.ObjectCategory
    Idps: TenantDeletionInfo.ObjectCategory
    Swift: TenantDeletionInfo.ObjectCategory
    ExternalTargets: TenantDeletionInfo.ObjectCategory
    HyxConnectors: TenantDeletionInfo.ObjectCategory
    HyxRealms: TenantDeletionInfo.ObjectCategory
    class CompletionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NotStarted: _ClassVar[TenantDeletionInfo.CompletionState]
        InProgress: _ClassVar[TenantDeletionInfo.CompletionState]
        Finished: _ClassVar[TenantDeletionInfo.CompletionState]
        Skipped: _ClassVar[TenantDeletionInfo.CompletionState]
        Waiting: _ClassVar[TenantDeletionInfo.CompletionState]
    NotStarted: TenantDeletionInfo.CompletionState
    InProgress: TenantDeletionInfo.CompletionState
    Finished: TenantDeletionInfo.CompletionState
    Skipped: TenantDeletionInfo.CompletionState
    Waiting: TenantDeletionInfo.CompletionState
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_AT_NODE_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    category: TenantDeletionInfo.ObjectCategory
    state: TenantDeletionInfo.CompletionState
    started_at_time_msecs: int
    finished_at_time_msecs: int
    processed_at_node: str
    retry_count: int
    def __init__(self, category: _Optional[_Union[TenantDeletionInfo.ObjectCategory, str]] = ..., state: _Optional[_Union[TenantDeletionInfo.CompletionState, str]] = ..., started_at_time_msecs: _Optional[int] = ..., finished_at_time_msecs: _Optional[int] = ..., processed_at_node: _Optional[str] = ..., retry_count: _Optional[int] = ...) -> None: ...

class Tenants(_message.Message):
    __slots__ = ("version", "tenant_vec", "next_available_id")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    version: int
    tenant_vec: _containers.RepeatedCompositeFieldContainer[Tenant]
    next_available_id: int
    def __init__(self, version: _Optional[int] = ..., tenant_vec: _Optional[_Iterable[_Union[Tenant, _Mapping]]] = ..., next_available_id: _Optional[int] = ...) -> None: ...

class TenantPreferences(_message.Message):
    __slots__ = ("allow_impersonation_by_parent", "copy_ancestors_in_alert_emails")
    ALLOW_IMPERSONATION_BY_PARENT_FIELD_NUMBER: _ClassVar[int]
    COPY_ANCESTORS_IN_ALERT_EMAILS_FIELD_NUMBER: _ClassVar[int]
    allow_impersonation_by_parent: bool
    copy_ancestors_in_alert_emails: bool
    def __init__(self, allow_impersonation_by_parent: bool = ..., copy_ancestors_in_alert_emails: bool = ...) -> None: ...

class TenantMigrationActionStatus(_message.Message):
    __slots__ = ("action_type", "action_incarnation_id", "status", "error_type", "error_message")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[TenantMigrationActionStatus.Status]
        kFinished: _ClassVar[TenantMigrationActionStatus.Status]
        kCancelled: _ClassVar[TenantMigrationActionStatus.Status]
    kStarted: TenantMigrationActionStatus.Status
    kFinished: TenantMigrationActionStatus.Status
    kCancelled: TenantMigrationActionStatus.Status
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    action_type: _cluster_config_pb2.TenantMigrationInfo.Action
    action_incarnation_id: int
    status: TenantMigrationActionStatus.Status
    error_type: _error_pb2.ErrorProto.Type
    error_message: str
    def __init__(self, action_type: _Optional[_Union[_cluster_config_pb2.TenantMigrationInfo.Action, str]] = ..., action_incarnation_id: _Optional[int] = ..., status: _Optional[_Union[TenantMigrationActionStatus.Status, str]] = ..., error_type: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class TenantMigrationServiceStatus(_message.Message):
    __slots__ = ("service_type", "finished_actions", "active_actions")
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FINISHED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    service_type: _cluster_config_pb2.TenantMigrationInfo.Service
    finished_actions: _containers.RepeatedCompositeFieldContainer[TenantMigrationActionStatus]
    active_actions: _containers.RepeatedCompositeFieldContainer[TenantMigrationActionStatus]
    def __init__(self, service_type: _Optional[_Union[_cluster_config_pb2.TenantMigrationInfo.Service, str]] = ..., finished_actions: _Optional[_Iterable[_Union[TenantMigrationActionStatus, _Mapping]]] = ..., active_actions: _Optional[_Iterable[_Union[TenantMigrationActionStatus, _Mapping]]] = ...) -> None: ...

class TenantMigrationStatus(_message.Message):
    __slots__ = ("migration_uuid", "tenant_id", "start_time_usecs", "end_time_usecs", "error_type", "error_message", "services")
    MIGRATION_UUID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    migration_uuid: str
    tenant_id: str
    start_time_usecs: int
    end_time_usecs: int
    error_type: _error_pb2.ErrorProto.Type
    error_message: str
    services: _containers.RepeatedCompositeFieldContainer[TenantMigrationServiceStatus]
    def __init__(self, migration_uuid: _Optional[str] = ..., tenant_id: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., error_type: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ..., services: _Optional[_Iterable[_Union[TenantMigrationServiceStatus, _Mapping]]] = ...) -> None: ...
