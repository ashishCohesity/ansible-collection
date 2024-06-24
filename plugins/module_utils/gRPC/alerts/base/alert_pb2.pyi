from google.protobuf import descriptor_pb2 as _descriptor_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmailRecipientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kTo: _ClassVar[EmailRecipientType]
    kCc: _ClassVar[EmailRecipientType]
kTo: EmailRecipientType
kCc: EmailRecipientType

class AlertIdProto(_message.Message):
    __slots__ = ("timestamp_usecs", "id")
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    timestamp_usecs: int
    id: int
    def __init__(self, timestamp_usecs: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class AlertProto(_message.Message):
    __slots__ = ("alert_id", "alert_type", "severity", "property_list", "dedup_timestamps", "dedup_count", "resolution_id", "suppression_id", "cluster_instance_id", "cluster_partition_id", "notification_email_list", "tenant_id_vec", "delivery_target_list", "resolved_timestamp", "resolution_id_string")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCritical: _ClassVar[AlertProto.Severity]
        kWarning: _ClassVar[AlertProto.Severity]
        kInfo: _ClassVar[AlertProto.Severity]
        kSeverityAll: _ClassVar[AlertProto.Severity]
        kNumSeverityLevels: _ClassVar[AlertProto.Severity]
    kCritical: AlertProto.Severity
    kWarning: AlertProto.Severity
    kInfo: AlertProto.Severity
    kSeverityAll: AlertProto.Severity
    kNumSeverityLevels: AlertProto.Severity
    class ReservedResolutionId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDefaultResolutionId: _ClassVar[AlertProto.ReservedResolutionId]
        kNoteResolutionId: _ClassVar[AlertProto.ReservedResolutionId]
    kDefaultResolutionId: AlertProto.ReservedResolutionId
    kNoteResolutionId: AlertProto.ReservedResolutionId
    class AlertState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOpen: _ClassVar[AlertProto.AlertState]
        kResolved: _ClassVar[AlertProto.AlertState]
        kSuppressed: _ClassVar[AlertProto.AlertState]
        kNote: _ClassVar[AlertProto.AlertState]
    kOpen: AlertProto.AlertState
    kResolved: AlertProto.AlertState
    kSuppressed: AlertProto.AlertState
    kNote: AlertProto.AlertState
    class Property(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    DEDUP_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPRESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_EMAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_ID_STRING_FIELD_NUMBER: _ClassVar[int]
    alert_id: AlertIdProto
    alert_type: int
    severity: AlertProto.Severity
    property_list: _containers.RepeatedCompositeFieldContainer[AlertProto.Property]
    dedup_timestamps: _containers.RepeatedScalarFieldContainer[int]
    dedup_count: int
    resolution_id: int
    suppression_id: int
    cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
    cluster_partition_id: int
    notification_email_list: _containers.RepeatedScalarFieldContainer[str]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    delivery_target_list: _containers.RepeatedCompositeFieldContainer[DeliveryRuleProto.DeliveryTarget]
    resolved_timestamp: int
    resolution_id_string: str
    def __init__(self, alert_id: _Optional[_Union[AlertIdProto, _Mapping]] = ..., alert_type: _Optional[int] = ..., severity: _Optional[_Union[AlertProto.Severity, str]] = ..., property_list: _Optional[_Iterable[_Union[AlertProto.Property, _Mapping]]] = ..., dedup_timestamps: _Optional[_Iterable[int]] = ..., dedup_count: _Optional[int] = ..., resolution_id: _Optional[int] = ..., suppression_id: _Optional[int] = ..., cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., notification_email_list: _Optional[_Iterable[str]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., delivery_target_list: _Optional[_Iterable[_Union[DeliveryRuleProto.DeliveryTarget, _Mapping]]] = ..., resolved_timestamp: _Optional[int] = ..., resolution_id_string: _Optional[str] = ...) -> None: ...

class AlertsDataProto(_message.Message):
    __slots__ = ("version", "data_vec")
    class Data(_message.Message):
        __slots__ = ("tenant_id", "notification_email_list", "delivery_rule")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_EMAIL_LIST_FIELD_NUMBER: _ClassVar[int]
        DELIVERY_RULE_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        notification_email_list: _containers.RepeatedScalarFieldContainer[str]
        delivery_rule: DeliveryRuleProto
        def __init__(self, tenant_id: _Optional[str] = ..., notification_email_list: _Optional[_Iterable[str]] = ..., delivery_rule: _Optional[_Union[DeliveryRuleProto, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    version: int
    data_vec: _containers.RepeatedCompositeFieldContainer[AlertsDataProto.Data]
    def __init__(self, version: _Optional[int] = ..., data_vec: _Optional[_Iterable[_Union[AlertsDataProto.Data, _Mapping]]] = ...) -> None: ...

class ResolutionProto(_message.Message):
    __slots__ = ("resolution_id", "resolution_summary", "resolution_details", "timestamp_usecs", "user_id", "tenant_id_list", "resolution_type")
    class ResolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kManualResolved: _ClassVar[ResolutionProto.ResolutionType]
        kAutoResolved: _ClassVar[ResolutionProto.ResolutionType]
    kManualResolved: ResolutionProto.ResolutionType
    kAutoResolved: ResolutionProto.ResolutionType
    RESOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    resolution_id: int
    resolution_summary: bytes
    resolution_details: bytes
    timestamp_usecs: int
    user_id: str
    tenant_id_list: _containers.RepeatedScalarFieldContainer[str]
    resolution_type: ResolutionProto.ResolutionType
    def __init__(self, resolution_id: _Optional[int] = ..., resolution_summary: _Optional[bytes] = ..., resolution_details: _Optional[bytes] = ..., timestamp_usecs: _Optional[int] = ..., user_id: _Optional[str] = ..., tenant_id_list: _Optional[_Iterable[str]] = ..., resolution_type: _Optional[_Union[ResolutionProto.ResolutionType, str]] = ...) -> None: ...

class AlertDocumentProto(_message.Message):
    __slots__ = ("language_code", "alert_name", "alert_description", "alert_cause", "alert_help_text", "alert_255_char_desc")
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ALERT_NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALERT_CAUSE_FIELD_NUMBER: _ClassVar[int]
    ALERT_HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    ALERT_255_CHAR_DESC_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    alert_name: bytes
    alert_description: bytes
    alert_cause: bytes
    alert_help_text: bytes
    alert_255_char_desc: bytes
    def __init__(self, language_code: _Optional[str] = ..., alert_name: _Optional[bytes] = ..., alert_description: _Optional[bytes] = ..., alert_cause: _Optional[bytes] = ..., alert_help_text: _Optional[bytes] = ..., alert_255_char_desc: _Optional[bytes] = ...) -> None: ...

class AlertMetadataProto(_message.Message):
    __slots__ = ("alert_type_id", "version", "category", "property_list", "primary_key_list", "dedup_interval_seconds", "alert_document_list", "snmp_notification", "dedup_until_resolved", "ignore_duplicate_occurrences", "send_support_notification", "hide_alert_from_user", "alert_type_bucket", "info_level_need_resolved", "resolve_alert_type_list", "resolve_confirm_interval_seconds", "recovered_by_alert_type_id", "syslog_notification", "prop_metadata")
    class AlertTypeBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSoftware: _ClassVar[AlertMetadataProto.AlertTypeBucket]
        kHardware: _ClassVar[AlertMetadataProto.AlertTypeBucket]
        kMaintenance: _ClassVar[AlertMetadataProto.AlertTypeBucket]
        kDataService: _ClassVar[AlertMetadataProto.AlertTypeBucket]
        kDeprecatedService: _ClassVar[AlertMetadataProto.AlertTypeBucket]
        kDeprecatedOther: _ClassVar[AlertMetadataProto.AlertTypeBucket]
    kSoftware: AlertMetadataProto.AlertTypeBucket
    kHardware: AlertMetadataProto.AlertTypeBucket
    kMaintenance: AlertMetadataProto.AlertTypeBucket
    kDataService: AlertMetadataProto.AlertTypeBucket
    kDeprecatedService: AlertMetadataProto.AlertTypeBucket
    kDeprecatedOther: AlertMetadataProto.AlertTypeBucket
    class AlertCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisk: _ClassVar[AlertMetadataProto.AlertCategory]
        kNode: _ClassVar[AlertMetadataProto.AlertCategory]
        kCluster: _ClassVar[AlertMetadataProto.AlertCategory]
        kChassis: _ClassVar[AlertMetadataProto.AlertCategory]
        kPowerSupply: _ClassVar[AlertMetadataProto.AlertCategory]
        kCPU: _ClassVar[AlertMetadataProto.AlertCategory]
        kMemory: _ClassVar[AlertMetadataProto.AlertCategory]
        kTemperature: _ClassVar[AlertMetadataProto.AlertCategory]
        kFan: _ClassVar[AlertMetadataProto.AlertCategory]
        kNIC: _ClassVar[AlertMetadataProto.AlertCategory]
        kFirmware: _ClassVar[AlertMetadataProto.AlertCategory]
        kNodeHealth: _ClassVar[AlertMetadataProto.AlertCategory]
        kOperatingSystem: _ClassVar[AlertMetadataProto.AlertCategory]
        kDataPath: _ClassVar[AlertMetadataProto.AlertCategory]
        kMetadata: _ClassVar[AlertMetadataProto.AlertCategory]
        kIndexing: _ClassVar[AlertMetadataProto.AlertCategory]
        kHelios: _ClassVar[AlertMetadataProto.AlertCategory]
        kAppMarketPlace: _ClassVar[AlertMetadataProto.AlertCategory]
        kSystemService: _ClassVar[AlertMetadataProto.AlertCategory]
        kLicense: _ClassVar[AlertMetadataProto.AlertCategory]
        kSecurity: _ClassVar[AlertMetadataProto.AlertCategory]
        kUpgrade: _ClassVar[AlertMetadataProto.AlertCategory]
        kClusterManagement: _ClassVar[AlertMetadataProto.AlertCategory]
        kAuditLog: _ClassVar[AlertMetadataProto.AlertCategory]
        kNetworking: _ClassVar[AlertMetadataProto.AlertCategory]
        kConfiguration: _ClassVar[AlertMetadataProto.AlertCategory]
        kStorageUsage: _ClassVar[AlertMetadataProto.AlertCategory]
        kFaultTolerance: _ClassVar[AlertMetadataProto.AlertCategory]
        kBackupRestore: _ClassVar[AlertMetadataProto.AlertCategory]
        kArchivalRestore: _ClassVar[AlertMetadataProto.AlertCategory]
        kRemoteReplication: _ClassVar[AlertMetadataProto.AlertCategory]
        kQuota: _ClassVar[AlertMetadataProto.AlertCategory]
        kCDP: _ClassVar[AlertMetadataProto.AlertCategory]
        kViewFailover: _ClassVar[AlertMetadataProto.AlertCategory]
        kDisasterRecovery: _ClassVar[AlertMetadataProto.AlertCategory]
        kClusterHealth: _ClassVar[AlertMetadataProto.AlertCategory]
        kEncryption: _ClassVar[AlertMetadataProto.AlertCategory]
        kHeliosProActiveWellness: _ClassVar[AlertMetadataProto.AlertCategory]
        kHeliosAnalyticsJobs: _ClassVar[AlertMetadataProto.AlertCategory]
        kHeliosSignatureJobs: _ClassVar[AlertMetadataProto.AlertCategory]
        kAppsInfra: _ClassVar[AlertMetadataProto.AlertCategory]
        kAntivirus: _ClassVar[AlertMetadataProto.AlertCategory]
        kArchivalCopy: _ClassVar[AlertMetadataProto.AlertCategory]
    kDisk: AlertMetadataProto.AlertCategory
    kNode: AlertMetadataProto.AlertCategory
    kCluster: AlertMetadataProto.AlertCategory
    kChassis: AlertMetadataProto.AlertCategory
    kPowerSupply: AlertMetadataProto.AlertCategory
    kCPU: AlertMetadataProto.AlertCategory
    kMemory: AlertMetadataProto.AlertCategory
    kTemperature: AlertMetadataProto.AlertCategory
    kFan: AlertMetadataProto.AlertCategory
    kNIC: AlertMetadataProto.AlertCategory
    kFirmware: AlertMetadataProto.AlertCategory
    kNodeHealth: AlertMetadataProto.AlertCategory
    kOperatingSystem: AlertMetadataProto.AlertCategory
    kDataPath: AlertMetadataProto.AlertCategory
    kMetadata: AlertMetadataProto.AlertCategory
    kIndexing: AlertMetadataProto.AlertCategory
    kHelios: AlertMetadataProto.AlertCategory
    kAppMarketPlace: AlertMetadataProto.AlertCategory
    kSystemService: AlertMetadataProto.AlertCategory
    kLicense: AlertMetadataProto.AlertCategory
    kSecurity: AlertMetadataProto.AlertCategory
    kUpgrade: AlertMetadataProto.AlertCategory
    kClusterManagement: AlertMetadataProto.AlertCategory
    kAuditLog: AlertMetadataProto.AlertCategory
    kNetworking: AlertMetadataProto.AlertCategory
    kConfiguration: AlertMetadataProto.AlertCategory
    kStorageUsage: AlertMetadataProto.AlertCategory
    kFaultTolerance: AlertMetadataProto.AlertCategory
    kBackupRestore: AlertMetadataProto.AlertCategory
    kArchivalRestore: AlertMetadataProto.AlertCategory
    kRemoteReplication: AlertMetadataProto.AlertCategory
    kQuota: AlertMetadataProto.AlertCategory
    kCDP: AlertMetadataProto.AlertCategory
    kViewFailover: AlertMetadataProto.AlertCategory
    kDisasterRecovery: AlertMetadataProto.AlertCategory
    kClusterHealth: AlertMetadataProto.AlertCategory
    kEncryption: AlertMetadataProto.AlertCategory
    kHeliosProActiveWellness: AlertMetadataProto.AlertCategory
    kHeliosAnalyticsJobs: AlertMetadataProto.AlertCategory
    kHeliosSignatureJobs: AlertMetadataProto.AlertCategory
    kAppsInfra: AlertMetadataProto.AlertCategory
    kAntivirus: AlertMetadataProto.AlertCategory
    kArchivalCopy: AlertMetadataProto.AlertCategory
    class PropertyMetadata(_message.Message):
        __slots__ = ("tag", "property_name", "enum_proto_name")
        TAG_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
        ENUM_PROTO_NAME_FIELD_NUMBER: _ClassVar[int]
        tag: str
        property_name: str
        enum_proto_name: str
        def __init__(self, tag: _Optional[str] = ..., property_name: _Optional[str] = ..., enum_proto_name: _Optional[str] = ...) -> None: ...
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: _descriptor.FieldDescriptor
    ALERT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_LIST_FIELD_NUMBER: _ClassVar[int]
    DEDUP_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALERT_DOCUMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    SNMP_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    DEDUP_UNTIL_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DUPLICATE_OCCURRENCES_FIELD_NUMBER: _ClassVar[int]
    SEND_SUPPORT_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    HIDE_ALERT_FROM_USER_FIELD_NUMBER: _ClassVar[int]
    ALERT_TYPE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    INFO_LEVEL_NEED_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_ALERT_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_CONFIRM_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RECOVERED_BY_ALERT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SYSLOG_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    PROP_METADATA_FIELD_NUMBER: _ClassVar[int]
    alert_type_id: int
    version: int
    category: AlertMetadataProto.AlertCategory
    property_list: _containers.RepeatedScalarFieldContainer[str]
    primary_key_list: _containers.RepeatedScalarFieldContainer[str]
    dedup_interval_seconds: int
    alert_document_list: _containers.RepeatedCompositeFieldContainer[AlertDocumentProto]
    snmp_notification: bool
    dedup_until_resolved: bool
    ignore_duplicate_occurrences: bool
    send_support_notification: bool
    hide_alert_from_user: bool
    alert_type_bucket: AlertMetadataProto.AlertTypeBucket
    info_level_need_resolved: bool
    resolve_alert_type_list: _containers.RepeatedScalarFieldContainer[int]
    resolve_confirm_interval_seconds: int
    recovered_by_alert_type_id: int
    syslog_notification: bool
    prop_metadata: _containers.RepeatedCompositeFieldContainer[AlertMetadataProto.PropertyMetadata]
    def __init__(self, alert_type_id: _Optional[int] = ..., version: _Optional[int] = ..., category: _Optional[_Union[AlertMetadataProto.AlertCategory, str]] = ..., property_list: _Optional[_Iterable[str]] = ..., primary_key_list: _Optional[_Iterable[str]] = ..., dedup_interval_seconds: _Optional[int] = ..., alert_document_list: _Optional[_Iterable[_Union[AlertDocumentProto, _Mapping]]] = ..., snmp_notification: bool = ..., dedup_until_resolved: bool = ..., ignore_duplicate_occurrences: bool = ..., send_support_notification: bool = ..., hide_alert_from_user: bool = ..., alert_type_bucket: _Optional[_Union[AlertMetadataProto.AlertTypeBucket, str]] = ..., info_level_need_resolved: bool = ..., resolve_alert_type_list: _Optional[_Iterable[int]] = ..., resolve_confirm_interval_seconds: _Optional[int] = ..., recovered_by_alert_type_id: _Optional[int] = ..., syslog_notification: bool = ..., prop_metadata: _Optional[_Iterable[_Union[AlertMetadataProto.PropertyMetadata, _Mapping]]] = ...) -> None: ...

class AlertMetadataInputProto(_message.Message):
    __slots__ = ("alert_metadata_list",)
    ALERT_METADATA_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_metadata_list: _containers.RepeatedCompositeFieldContainer[AlertMetadataProto]
    def __init__(self, alert_metadata_list: _Optional[_Iterable[_Union[AlertMetadataProto, _Mapping]]] = ...) -> None: ...

class AlertRuleScope(_message.Message):
    __slots__ = ("alert_type_id_list", "alert_category_list", "alert_severity_list", "property_list", "apply_for_all")
    ALERT_TYPE_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_CATEGORY_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_SEVERITY_LIST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_LIST_FIELD_NUMBER: _ClassVar[int]
    APPLY_FOR_ALL_FIELD_NUMBER: _ClassVar[int]
    alert_type_id_list: _containers.RepeatedScalarFieldContainer[int]
    alert_category_list: _containers.RepeatedScalarFieldContainer[AlertMetadataProto.AlertCategory]
    alert_severity_list: _containers.RepeatedScalarFieldContainer[AlertProto.Severity]
    property_list: _containers.RepeatedCompositeFieldContainer[AlertProto.Property]
    apply_for_all: bool
    def __init__(self, alert_type_id_list: _Optional[_Iterable[int]] = ..., alert_category_list: _Optional[_Iterable[_Union[AlertMetadataProto.AlertCategory, str]]] = ..., alert_severity_list: _Optional[_Iterable[_Union[AlertProto.Severity, str]]] = ..., property_list: _Optional[_Iterable[_Union[AlertProto.Property, _Mapping]]] = ..., apply_for_all: bool = ...) -> None: ...

class ResolutionRuleProto(_message.Message):
    __slots__ = ("resolution_scope", "confirm_interval_seconds")
    RESOLUTION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    resolution_scope: AlertRuleScope
    confirm_interval_seconds: int
    def __init__(self, resolution_scope: _Optional[_Union[AlertRuleScope, _Mapping]] = ..., confirm_interval_seconds: _Optional[int] = ...) -> None: ...

class SuppressionRuleProto(_message.Message):
    __slots__ = ("suppression_scope", "start_time_usecs", "end_time_usecs")
    SUPPRESSION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    suppression_scope: AlertRuleScope
    start_time_usecs: int
    end_time_usecs: int
    def __init__(self, suppression_scope: _Optional[_Union[AlertRuleScope, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ...) -> None: ...

class DedupRuleProto(_message.Message):
    __slots__ = ("dedup_scope", "dedup_interval_seconds", "dedup_until_resolved")
    DEDUP_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_UNTIL_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    dedup_scope: AlertRuleScope
    dedup_interval_seconds: int
    dedup_until_resolved: bool
    def __init__(self, dedup_scope: _Optional[_Union[AlertRuleScope, _Mapping]] = ..., dedup_interval_seconds: _Optional[int] = ..., dedup_until_resolved: bool = ...) -> None: ...

class DeliveryRuleProto(_message.Message):
    __slots__ = ("delivery_scope", "delivery_target_list", "tenant_id", "rule_id", "rule_name")
    class DeliveryTarget(_message.Message):
        __slots__ = ("email_address", "tenant_id", "locale", "external_api_url", "external_api_curl_options", "snmp_notification", "syslog_notification", "email_recipient_type")
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_API_URL_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_API_CURL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        SNMP_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        SYSLOG_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        EMAIL_RECIPIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        email_address: str
        tenant_id: str
        locale: str
        external_api_url: str
        external_api_curl_options: str
        snmp_notification: bool
        syslog_notification: bool
        email_recipient_type: EmailRecipientType
        def __init__(self, email_address: _Optional[str] = ..., tenant_id: _Optional[str] = ..., locale: _Optional[str] = ..., external_api_url: _Optional[str] = ..., external_api_curl_options: _Optional[str] = ..., snmp_notification: bool = ..., syslog_notification: bool = ..., email_recipient_type: _Optional[_Union[EmailRecipientType, str]] = ...) -> None: ...
    DELIVERY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TARGET_LIST_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    delivery_scope: AlertRuleScope
    delivery_target_list: _containers.RepeatedCompositeFieldContainer[DeliveryRuleProto.DeliveryTarget]
    tenant_id: str
    rule_id: int
    rule_name: str
    def __init__(self, delivery_scope: _Optional[_Union[AlertRuleScope, _Mapping]] = ..., delivery_target_list: _Optional[_Iterable[_Union[DeliveryRuleProto.DeliveryTarget, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., rule_id: _Optional[int] = ..., rule_name: _Optional[str] = ...) -> None: ...

class AlertTypeIdReservationProto(_message.Message):
    __slots__ = ("min_alert_type_id", "max_alert_type_id", "nexus_min_type_id", "nexus_max_type_id", "stats_min_type_id", "stats_max_type_id", "apollo_min_type_id", "apollo_max_type_id", "yoda_min_type_id", "yoda_max_type_id", "bridge_min_type_id", "bridge_max_type_id", "magneto_min_type_id", "magneto_max_type_id", "common_min_type_id", "common_max_type_id", "keychain_min_type_id", "keychain_max_type_id", "nexus_sysmon_min_type_id", "nexus_sysmon_max_type_id", "scribe_min_type_id", "scribe_max_type_id", "helios_min_type_id", "helios_max_type_id", "librarian_min_type_id", "librarian_max_type_id", "athena_min_type_id", "athena_max_type_id", "icebox_min_type_id", "icebox_max_type_id", "atom_min_type_id", "atom_max_type_id", "support_toolbox_min_type_id", "support_toolbox_max_type_id")
    MIN_ALERT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_ALERT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXUS_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXUS_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APOLLO_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    YODA_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    YODA_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYCHAIN_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYCHAIN_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXUS_SYSMON_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXUS_SYSMON_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    HELIOS_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    HELIOS_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ATHENA_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ATHENA_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ATOM_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    ATOM_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_TOOLBOX_MIN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_TOOLBOX_MAX_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    min_alert_type_id: int
    max_alert_type_id: int
    nexus_min_type_id: int
    nexus_max_type_id: int
    stats_min_type_id: int
    stats_max_type_id: int
    apollo_min_type_id: int
    apollo_max_type_id: int
    yoda_min_type_id: int
    yoda_max_type_id: int
    bridge_min_type_id: int
    bridge_max_type_id: int
    magneto_min_type_id: int
    magneto_max_type_id: int
    common_min_type_id: int
    common_max_type_id: int
    keychain_min_type_id: int
    keychain_max_type_id: int
    nexus_sysmon_min_type_id: int
    nexus_sysmon_max_type_id: int
    scribe_min_type_id: int
    scribe_max_type_id: int
    helios_min_type_id: int
    helios_max_type_id: int
    librarian_min_type_id: int
    librarian_max_type_id: int
    athena_min_type_id: int
    athena_max_type_id: int
    icebox_min_type_id: int
    icebox_max_type_id: int
    atom_min_type_id: int
    atom_max_type_id: int
    support_toolbox_min_type_id: int
    support_toolbox_max_type_id: int
    def __init__(self, min_alert_type_id: _Optional[int] = ..., max_alert_type_id: _Optional[int] = ..., nexus_min_type_id: _Optional[int] = ..., nexus_max_type_id: _Optional[int] = ..., stats_min_type_id: _Optional[int] = ..., stats_max_type_id: _Optional[int] = ..., apollo_min_type_id: _Optional[int] = ..., apollo_max_type_id: _Optional[int] = ..., yoda_min_type_id: _Optional[int] = ..., yoda_max_type_id: _Optional[int] = ..., bridge_min_type_id: _Optional[int] = ..., bridge_max_type_id: _Optional[int] = ..., magneto_min_type_id: _Optional[int] = ..., magneto_max_type_id: _Optional[int] = ..., common_min_type_id: _Optional[int] = ..., common_max_type_id: _Optional[int] = ..., keychain_min_type_id: _Optional[int] = ..., keychain_max_type_id: _Optional[int] = ..., nexus_sysmon_min_type_id: _Optional[int] = ..., nexus_sysmon_max_type_id: _Optional[int] = ..., scribe_min_type_id: _Optional[int] = ..., scribe_max_type_id: _Optional[int] = ..., helios_min_type_id: _Optional[int] = ..., helios_max_type_id: _Optional[int] = ..., librarian_min_type_id: _Optional[int] = ..., librarian_max_type_id: _Optional[int] = ..., athena_min_type_id: _Optional[int] = ..., athena_max_type_id: _Optional[int] = ..., icebox_min_type_id: _Optional[int] = ..., icebox_max_type_id: _Optional[int] = ..., atom_min_type_id: _Optional[int] = ..., atom_max_type_id: _Optional[int] = ..., support_toolbox_min_type_id: _Optional[int] = ..., support_toolbox_max_type_id: _Optional[int] = ...) -> None: ...

class AlertsConfigProto(_message.Message):
    __slots__ = ("alerts_base_uri", "alerts_master_key", "register_alerts_uri", "send_alerts_uri", "get_alert_metadata_uri", "query_alerts_uri", "resolve_alerts_uri", "query_resolutions_uri", "create_suppressions_uri", "delete_suppressions_uri", "query_suppressions_uri", "update_dedup_params_uri", "query_dedup_params_uri", "update_delivery_rules_uri", "query_delivery_rules_uri", "get_master_info_uri", "delete_resolutions_uri", "ttl_config")
    class TimeToLiveConfigProto(_message.Message):
        __slots__ = ("info_alerts_ttl_secs", "critical_alerts_ttl_secs", "resolutions_ttl_secs")
        INFO_ALERTS_TTL_SECS_FIELD_NUMBER: _ClassVar[int]
        CRITICAL_ALERTS_TTL_SECS_FIELD_NUMBER: _ClassVar[int]
        RESOLUTIONS_TTL_SECS_FIELD_NUMBER: _ClassVar[int]
        info_alerts_ttl_secs: int
        critical_alerts_ttl_secs: int
        resolutions_ttl_secs: int
        def __init__(self, info_alerts_ttl_secs: _Optional[int] = ..., critical_alerts_ttl_secs: _Optional[int] = ..., resolutions_ttl_secs: _Optional[int] = ...) -> None: ...
    ALERTS_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    ALERTS_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    REGISTER_ALERTS_URI_FIELD_NUMBER: _ClassVar[int]
    SEND_ALERTS_URI_FIELD_NUMBER: _ClassVar[int]
    GET_ALERT_METADATA_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_ALERTS_URI_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_ALERTS_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESOLUTIONS_URI_FIELD_NUMBER: _ClassVar[int]
    CREATE_SUPPRESSIONS_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_SUPPRESSIONS_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_SUPPRESSIONS_URI_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DEDUP_PARAMS_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_DEDUP_PARAMS_URI_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DELIVERY_RULES_URI_FIELD_NUMBER: _ClassVar[int]
    QUERY_DELIVERY_RULES_URI_FIELD_NUMBER: _ClassVar[int]
    GET_MASTER_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_RESOLUTIONS_URI_FIELD_NUMBER: _ClassVar[int]
    TTL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    alerts_base_uri: str
    alerts_master_key: str
    register_alerts_uri: str
    send_alerts_uri: str
    get_alert_metadata_uri: str
    query_alerts_uri: str
    resolve_alerts_uri: str
    query_resolutions_uri: str
    create_suppressions_uri: str
    delete_suppressions_uri: str
    query_suppressions_uri: str
    update_dedup_params_uri: str
    query_dedup_params_uri: str
    update_delivery_rules_uri: str
    query_delivery_rules_uri: str
    get_master_info_uri: str
    delete_resolutions_uri: str
    ttl_config: AlertsConfigProto.TimeToLiveConfigProto
    def __init__(self, alerts_base_uri: _Optional[str] = ..., alerts_master_key: _Optional[str] = ..., register_alerts_uri: _Optional[str] = ..., send_alerts_uri: _Optional[str] = ..., get_alert_metadata_uri: _Optional[str] = ..., query_alerts_uri: _Optional[str] = ..., resolve_alerts_uri: _Optional[str] = ..., query_resolutions_uri: _Optional[str] = ..., create_suppressions_uri: _Optional[str] = ..., delete_suppressions_uri: _Optional[str] = ..., query_suppressions_uri: _Optional[str] = ..., update_dedup_params_uri: _Optional[str] = ..., query_dedup_params_uri: _Optional[str] = ..., update_delivery_rules_uri: _Optional[str] = ..., query_delivery_rules_uri: _Optional[str] = ..., get_master_info_uri: _Optional[str] = ..., delete_resolutions_uri: _Optional[str] = ..., ttl_config: _Optional[_Union[AlertsConfigProto.TimeToLiveConfigProto, _Mapping]] = ...) -> None: ...

class AlertProtoList(_message.Message):
    __slots__ = ("alert_list",)
    ALERT_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_list: _containers.RepeatedCompositeFieldContainer[AlertProto]
    def __init__(self, alert_list: _Optional[_Iterable[_Union[AlertProto, _Mapping]]] = ...) -> None: ...
