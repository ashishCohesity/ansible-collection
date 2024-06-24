from bifrost.base import bifrost_base_pb2 as _bifrost_base_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.view_keeper import list_smb_active_opens_pb2 as _list_smb_active_opens_pb2
from bridge.view_keeper import list_nlm_locks_pb2 as _list_nlm_locks_pb2
from bridge.view_keeper import get_fld_info_result_pb2 as _get_fld_info_result_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from bridge.view_keeper import view_smb_permissions_pb2 as _view_smb_permissions_pb2
from bridge.view_keeper import view_usage_pb2 as _view_usage_pb2
from bridge.stub import rpc_service_pb2 as _rpc_service_pb2
from bridge.snap_fs.stub import rpc_service_pb2 as _rpc_service_pb2_1
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.quota import quota_tree_metadata_pb2 as _quota_tree_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from iris.base import error_pb2 as _error_pb2
from iris.base import tenants_pb2 as _tenants_pb2
from iris.base import liveness_pb2 as _liveness_pb2
from librarian.base import librarian_pb2 as _librarian_pb2
from yoda.audit import cluster_audit_document_pb2 as _cluster_audit_document_pb2
from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from configs.uda import uda_configs_pb2 as _uda_configs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(_message.Message):
    __slots__ = ("error", "error_message")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto.Type
    error_message: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class LookupKeyResult(_message.Message):
    __slots__ = ("status", "key", "data", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    key: str
    data: bytes
    version: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[str] = ..., data: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class UpdateKeyArg(_message.Message):
    __slots__ = ("key", "expected_version", "data")
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    key: str
    expected_version: int
    data: bytes
    def __init__(self, key: _Optional[str] = ..., expected_version: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UpdateKeyResult(_message.Message):
    __slots__ = ("status", "key", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    key: str
    version: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DeleteKeyArg(_message.Message):
    __slots__ = ("key", "expected_version")
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    key: str
    expected_version: int
    def __init__(self, key: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class DeleteKeyResult(_message.Message):
    __slots__ = ("status", "key", "version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    key: str
    version: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., key: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class AllocateIdsResult(_message.Message):
    __slots__ = ("status", "id", "num_ids_allocated")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUM_IDS_ALLOCATED_FIELD_NUMBER: _ClassVar[int]
    status: Status
    id: int
    num_ids_allocated: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., id: _Optional[int] = ..., num_ids_allocated: _Optional[int] = ...) -> None: ...

class WatchClusterConfigArg(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class WatchClusterConfigResult(_message.Message):
    __slots__ = ("status", "version", "config_proto")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    version: int
    config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., version: _Optional[int] = ..., config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class QoS(_message.Message):
    __slots__ = ("qos_mappings",)
    QOS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    qos_mappings: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.QoSMapping]
    def __init__(self, qos_mappings: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping, _Mapping]]] = ...) -> None: ...

class CreateViewArg(_message.Message):
    __slots__ = ("view_name", "view_box_id", "description", "storage_policy_override", "qos", "subnet_vec", "enable_smb_access_based_dir_enumeration", "case_insensitive_entity_names", "quota_policy", "protocol_access_info", "iris_metadata", "s3_bucket_config", "enable_minion", "enable_filer_audit_logging", "inherit_audit_log_from_view", "enable_mixed_mode_permissions", "smb_config", "nfs_config", "file_extension_filter", "file_level_data_lock_config", "tenant_id", "security_mode_config", "antivirus_scan_config", "is_internal", "s3_key_mapping_config", "client_subnet_whitelist_extends_global_whitelist", "view_all_squash_uid", "view_all_squash_gid", "view_root_squash_uid", "view_root_squash_gid", "enable_live_indexing", "nis_netgroup_vec", "client_netgroup_whitelist_extends_global_whitelist", "category", "pin_config", "self_service_snapshot_config", "enable_metadata_accelerator", "s3_folder_support_enabled", "performance_config", "filer_lcm_rules")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    IRIS_METADATA_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FILER_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    INHERIT_AUDIT_LOG_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MIXED_MODE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    FILE_LEVEL_DATA_LOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    S3_KEY_MAPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LIVE_INDEXING_FIELD_NUMBER: _ClassVar[int]
    NIS_NETGROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELF_SERVICE_SNAPSHOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_METADATA_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
    S3_FOLDER_SUPPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILER_LCM_RULES_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    view_box_id: int
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos: QoS
    subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_smb_access_based_dir_enumeration: bool
    case_insensitive_entity_names: bool
    quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    iris_metadata: _view_metadata_pb2.ViewIdMappingProto.IrisMetadata
    s3_bucket_config: _s3_metadata_pb2.S3BucketConfigProto
    enable_minion: bool
    enable_filer_audit_logging: bool
    inherit_audit_log_from_view: bool
    enable_mixed_mode_permissions: bool
    smb_config: _view_smb_permissions_pb2.AliasSmbConfig
    nfs_config: _view_metadata_pb2.ViewIdMappingProto.NfsConfigProto
    file_extension_filter: _view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter
    file_level_data_lock_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    tenant_id: str
    security_mode_config: _view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig
    antivirus_scan_config: _view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig
    is_internal: bool
    s3_key_mapping_config: _s3_metadata_pb2.S3KeyMappingConfigProto
    client_subnet_whitelist_extends_global_whitelist: bool
    view_all_squash_uid: int
    view_all_squash_gid: int
    view_root_squash_uid: int
    view_root_squash_gid: int
    enable_live_indexing: bool
    nis_netgroup_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
    client_netgroup_whitelist_extends_global_whitelist: bool
    category: _view_metadata_pb2.ViewIdMappingProto.ViewCategory
    pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
    self_service_snapshot_config: _view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig
    enable_metadata_accelerator: bool
    s3_folder_support_enabled: bool
    performance_config: _view_metadata_pb2.ViewIdMappingProto.PerformanceConfig
    filer_lcm_rules: _view_metadata_pb2.LifecyclePolicy.LifecycleRules
    def __init__(self, view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos: _Optional[_Union[QoS, _Mapping]] = ..., subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., case_insensitive_entity_names: bool = ..., quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., iris_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.IrisMetadata, _Mapping]] = ..., s3_bucket_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., enable_minion: bool = ..., enable_filer_audit_logging: bool = ..., inherit_audit_log_from_view: bool = ..., enable_mixed_mode_permissions: bool = ..., smb_config: _Optional[_Union[_view_smb_permissions_pb2.AliasSmbConfig, _Mapping]] = ..., nfs_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., file_extension_filter: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., file_level_data_lock_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., tenant_id: _Optional[str] = ..., security_mode_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig, _Mapping]] = ..., antivirus_scan_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig, _Mapping]] = ..., is_internal: bool = ..., s3_key_mapping_config: _Optional[_Union[_s3_metadata_pb2.S3KeyMappingConfigProto, _Mapping]] = ..., client_subnet_whitelist_extends_global_whitelist: bool = ..., view_all_squash_uid: _Optional[int] = ..., view_all_squash_gid: _Optional[int] = ..., view_root_squash_uid: _Optional[int] = ..., view_root_squash_gid: _Optional[int] = ..., enable_live_indexing: bool = ..., nis_netgroup_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., client_netgroup_whitelist_extends_global_whitelist: bool = ..., category: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ViewCategory, str]] = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ..., self_service_snapshot_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig, _Mapping]] = ..., enable_metadata_accelerator: bool = ..., s3_folder_support_enabled: bool = ..., performance_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PerformanceConfig, _Mapping]] = ..., filer_lcm_rules: _Optional[_Union[_view_metadata_pb2.LifecyclePolicy.LifecycleRules, _Mapping]] = ...) -> None: ...

class CreateViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class EditViewArg(_message.Message):
    __slots__ = ("view_name", "description", "storage_policy_override", "qos", "subnet_vec", "enable_smb_access_based_dir_enumeration", "quota_policy", "protocol_access_info", "iris_metadata", "s3_bucket_config", "enable_minion", "enable_filer_audit_logging", "inherit_audit_log_from_view", "worm_lock_expiry_usecs", "enable_mixed_mode_permissions", "smb_config", "nfs_config", "file_extension_filter", "file_level_data_lock_config", "tenant_id", "security_mode_config", "antivirus_scan_config", "client_subnet_whitelist_extends_global_whitelist", "view_all_squash_uid", "view_all_squash_gid", "view_root_squash_uid", "view_root_squash_gid", "nis_netgroup_vec", "client_netgroup_whitelist_extends_global_whitelist", "category", "pin_config", "self_service_snapshot_config", "is_read_only", "enable_metadata_accelerator", "performance_config", "filer_lcm_rules")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    IRIS_METADATA_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FILER_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    INHERIT_AUDIT_LOG_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MIXED_MODE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    FILE_LEVEL_DATA_LOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    NIS_NETGROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELF_SERVICE_SNAPSHOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_METADATA_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILER_LCM_RULES_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos: QoS
    subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_smb_access_based_dir_enumeration: bool
    quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    iris_metadata: _view_metadata_pb2.ViewIdMappingProto.IrisMetadata
    s3_bucket_config: _s3_metadata_pb2.S3BucketConfigProto
    enable_minion: bool
    enable_filer_audit_logging: bool
    inherit_audit_log_from_view: bool
    worm_lock_expiry_usecs: int
    enable_mixed_mode_permissions: bool
    smb_config: _view_smb_permissions_pb2.AliasSmbConfig
    nfs_config: _view_metadata_pb2.ViewIdMappingProto.NfsConfigProto
    file_extension_filter: _view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter
    file_level_data_lock_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    tenant_id: str
    security_mode_config: _view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig
    antivirus_scan_config: _view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig
    client_subnet_whitelist_extends_global_whitelist: bool
    view_all_squash_uid: int
    view_all_squash_gid: int
    view_root_squash_uid: int
    view_root_squash_gid: int
    nis_netgroup_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
    client_netgroup_whitelist_extends_global_whitelist: bool
    category: _view_metadata_pb2.ViewIdMappingProto.ViewCategory
    pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
    self_service_snapshot_config: _view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig
    is_read_only: bool
    enable_metadata_accelerator: bool
    performance_config: _view_metadata_pb2.ViewIdMappingProto.PerformanceConfig
    filer_lcm_rules: _view_metadata_pb2.LifecyclePolicy.LifecycleRules
    def __init__(self, view_name: _Optional[str] = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos: _Optional[_Union[QoS, _Mapping]] = ..., subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., iris_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.IrisMetadata, _Mapping]] = ..., s3_bucket_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., enable_minion: bool = ..., enable_filer_audit_logging: bool = ..., inherit_audit_log_from_view: bool = ..., worm_lock_expiry_usecs: _Optional[int] = ..., enable_mixed_mode_permissions: bool = ..., smb_config: _Optional[_Union[_view_smb_permissions_pb2.AliasSmbConfig, _Mapping]] = ..., nfs_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., file_extension_filter: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., file_level_data_lock_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., tenant_id: _Optional[str] = ..., security_mode_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig, _Mapping]] = ..., antivirus_scan_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig, _Mapping]] = ..., client_subnet_whitelist_extends_global_whitelist: bool = ..., view_all_squash_uid: _Optional[int] = ..., view_all_squash_gid: _Optional[int] = ..., view_root_squash_uid: _Optional[int] = ..., view_root_squash_gid: _Optional[int] = ..., nis_netgroup_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., client_netgroup_whitelist_extends_global_whitelist: bool = ..., category: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ViewCategory, str]] = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ..., self_service_snapshot_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig, _Mapping]] = ..., is_read_only: bool = ..., enable_metadata_accelerator: bool = ..., performance_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PerformanceConfig, _Mapping]] = ..., filer_lcm_rules: _Optional[_Union[_view_metadata_pb2.LifecyclePolicy.LifecycleRules, _Mapping]] = ...) -> None: ...

class EditViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetViewsArg(_message.Message):
    __slots__ = ("view_name_vec", "view_box_id_vec", "max_views", "include_internal_views", "max_view_id", "match_partial_names", "view_count_only", "access_sids", "fetch_smb_permissions", "sort_by_logical_usage", "match_alias_names", "use_tenant_id_as_prefix", "include_views_with_antivirus_enabled_only", "view_id_vec", "include_views_with_data_lock_enabled_only", "include_views_with_audit_log_enabled_only", "include_views_with_audit_log_disabled_only", "summary_only", "view_protection_params", "fetch_view_usage_details", "protocols", "principal_ids", "tenant_ids", "category")
    class ViewProtectionParams(_message.Message):
        __slots__ = ("view_id_vec", "view_external_metadata_object_id_vec", "unprotected_only")
        VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        VIEW_EXTERNAL_METADATA_OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        UNPROTECTED_ONLY_FIELD_NUMBER: _ClassVar[int]
        view_id_vec: _containers.RepeatedScalarFieldContainer[int]
        view_external_metadata_object_id_vec: _containers.RepeatedScalarFieldContainer[int]
        unprotected_only: bool
        def __init__(self, view_id_vec: _Optional[_Iterable[int]] = ..., view_external_metadata_object_id_vec: _Optional[_Iterable[int]] = ..., unprotected_only: bool = ...) -> None: ...
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEWS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERNAL_VIEWS_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_PARTIAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_ONLY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_SIDS_FIELD_NUMBER: _ClassVar[int]
    FETCH_SMB_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_LOGICAL_USAGE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ALIAS_NAMES_FIELD_NUMBER: _ClassVar[int]
    USE_TENANT_ID_AS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIEWS_WITH_ANTIVIRUS_ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIEWS_WITH_DATA_LOCK_ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIEWS_WITH_AUDIT_LOG_ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VIEWS_WITH_AUDIT_LOG_DISABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ONLY_FIELD_NUMBER: _ClassVar[int]
    VIEW_PROTECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FETCH_VIEW_USAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_IDS_FIELD_NUMBER: _ClassVar[int]
    TENANT_IDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    view_box_id_vec: _containers.RepeatedScalarFieldContainer[int]
    max_views: int
    include_internal_views: bool
    max_view_id: int
    match_partial_names: bool
    view_count_only: bool
    access_sids: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    fetch_smb_permissions: bool
    sort_by_logical_usage: bool
    match_alias_names: bool
    use_tenant_id_as_prefix: bool
    include_views_with_antivirus_enabled_only: bool
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    include_views_with_data_lock_enabled_only: bool
    include_views_with_audit_log_enabled_only: bool
    include_views_with_audit_log_disabled_only: bool
    summary_only: bool
    view_protection_params: GetViewsArg.ViewProtectionParams
    fetch_view_usage_details: bool
    protocols: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    principal_ids: _containers.RepeatedScalarFieldContainer[int]
    tenant_ids: _containers.RepeatedScalarFieldContainer[str]
    category: _containers.RepeatedScalarFieldContainer[_view_metadata_pb2.ViewIdMappingProto.ViewCategory]
    def __init__(self, view_name_vec: _Optional[_Iterable[str]] = ..., view_box_id_vec: _Optional[_Iterable[int]] = ..., max_views: _Optional[int] = ..., include_internal_views: bool = ..., max_view_id: _Optional[int] = ..., match_partial_names: bool = ..., view_count_only: bool = ..., access_sids: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., fetch_smb_permissions: bool = ..., sort_by_logical_usage: bool = ..., match_alias_names: bool = ..., use_tenant_id_as_prefix: bool = ..., include_views_with_antivirus_enabled_only: bool = ..., view_id_vec: _Optional[_Iterable[int]] = ..., include_views_with_data_lock_enabled_only: bool = ..., include_views_with_audit_log_enabled_only: bool = ..., include_views_with_audit_log_disabled_only: bool = ..., summary_only: bool = ..., view_protection_params: _Optional[_Union[GetViewsArg.ViewProtectionParams, _Mapping]] = ..., fetch_view_usage_details: bool = ..., protocols: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., principal_ids: _Optional[_Iterable[int]] = ..., tenant_ids: _Optional[_Iterable[str]] = ..., category: _Optional[_Iterable[_Union[_view_metadata_pb2.ViewIdMappingProto.ViewCategory, str]]] = ...) -> None: ...

class GetViewsResult(_message.Message):
    __slots__ = ("status", "view_vec", "last_result", "view_count")
    class View(_message.Message):
        __slots__ = ("name", "id", "view_box_id", "create_time_msecs", "internal", "description", "storage_policy_override", "qos", "subnet_vec", "enable_smb_access_based_dir_enumeration", "case_insensitive_entity_names", "quota_policy", "protocol_access_info", "iris_metadata", "smb_permissions_info", "s3_bucket_config", "worm_lock_expiry_usecs", "enable_minion", "logical_usage_bytes", "enable_filer_audit_logging", "inherit_audit_log_from_view", "alias_vec", "enable_mixed_mode_permissions", "enable_smb_view_discovery", "enable_smb_encryption", "enforce_smb_encryption", "enable_nfs_view_discovery", "share_permissions", "file_extension_filter", "file_level_data_lock_config", "tenant_id", "security_mode_config", "antivirus_scan_config", "target_view_for_data_migration", "client_subnet_whitelist_extends_global_whitelist", "s3_key_mapping_config", "external_metadata", "enable_offline_caching", "view_all_squash_uid", "view_all_squash_gid", "view_root_squash_uid", "view_root_squash_gid", "enable_continuous_availability", "enable_smb_oplock", "enable_live_indexing", "nis_netgroup_vec", "client_netgroup_whitelist_extends_global_whitelist", "category", "enable_nfs_unix_authentication", "enable_nfs_kerberos_authentication", "enable_nfs_kerberos_integrity", "enable_nfs_kerberos_privacy", "is_read_only", "pin_config", "superusers", "self_service_snapshot_config", "snapshot_smb_access_sids", "enable_metadata_accelerator", "view_usage", "s3_folder_support_enabled", "performance_config", "enable_wcc", "filer_lcm_rules")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        QOS_FIELD_NUMBER: _ClassVar[int]
        SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
        CASE_INSENSITIVE_ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
        QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
        IRIS_METADATA_FIELD_NUMBER: _ClassVar[int]
        SMB_PERMISSIONS_INFO_FIELD_NUMBER: _ClassVar[int]
        S3_BUCKET_CONFIG_FIELD_NUMBER: _ClassVar[int]
        WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_MINION_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FILER_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
        INHERIT_AUDIT_LOG_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
        ALIAS_VEC_FIELD_NUMBER: _ClassVar[int]
        ENABLE_MIXED_MODE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SMB_VIEW_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SMB_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        ENFORCE_SMB_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_NFS_VIEW_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
        SHARE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        FILE_EXTENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
        FILE_LEVEL_DATA_LOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        SECURITY_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ANTIVIRUS_SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TARGET_VIEW_FOR_DATA_MIGRATION_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SUBNET_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
        S3_KEY_MAPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
        ENABLE_OFFLINE_CACHING_FIELD_NUMBER: _ClassVar[int]
        VIEW_ALL_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ALL_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ROOT_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
        VIEW_ROOT_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
        ENABLE_CONTINUOUS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SMB_OPLOCK_FIELD_NUMBER: _ClassVar[int]
        ENABLE_LIVE_INDEXING_FIELD_NUMBER: _ClassVar[int]
        NIS_NETGROUP_VEC_FIELD_NUMBER: _ClassVar[int]
        CLIENT_NETGROUP_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_NFS_UNIX_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_NFS_KERBEROS_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_NFS_KERBEROS_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_NFS_KERBEROS_PRIVACY_FIELD_NUMBER: _ClassVar[int]
        IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SUPERUSERS_FIELD_NUMBER: _ClassVar[int]
        SELF_SERVICE_SNAPSHOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_SMB_ACCESS_SIDS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_METADATA_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
        VIEW_USAGE_FIELD_NUMBER: _ClassVar[int]
        S3_FOLDER_SUPPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ENABLE_WCC_FIELD_NUMBER: _ClassVar[int]
        FILER_LCM_RULES_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: int
        view_box_id: int
        create_time_msecs: int
        internal: bool
        description: str
        storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
        qos: QoS
        subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
        enable_smb_access_based_dir_enumeration: bool
        case_insensitive_entity_names: bool
        quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
        protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
        iris_metadata: _view_metadata_pb2.ViewIdMappingProto.IrisMetadata
        smb_permissions_info: _view_smb_permissions_pb2.ViewSmbPermissionsInfo
        s3_bucket_config: _s3_metadata_pb2.S3BucketConfigProto
        worm_lock_expiry_usecs: int
        enable_minion: bool
        logical_usage_bytes: int
        enable_filer_audit_logging: bool
        inherit_audit_log_from_view: bool
        alias_vec: _containers.RepeatedCompositeFieldContainer[ViewAliasInfo]
        enable_mixed_mode_permissions: bool
        enable_smb_view_discovery: bool
        enable_smb_encryption: bool
        enforce_smb_encryption: bool
        enable_nfs_view_discovery: bool
        share_permissions: _containers.RepeatedCompositeFieldContainer[_view_smb_permissions_pb2.SmbPermission]
        file_extension_filter: _view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter
        file_level_data_lock_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
        tenant_id: str
        security_mode_config: _view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig
        antivirus_scan_config: _view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig
        target_view_for_data_migration: bool
        client_subnet_whitelist_extends_global_whitelist: bool
        s3_key_mapping_config: _s3_metadata_pb2.S3KeyMappingConfigProto
        external_metadata: _view_metadata_pb2.ViewIdMappingProto.ExternalMetadata
        enable_offline_caching: bool
        view_all_squash_uid: int
        view_all_squash_gid: int
        view_root_squash_uid: int
        view_root_squash_gid: int
        enable_continuous_availability: bool
        enable_smb_oplock: bool
        enable_live_indexing: bool
        nis_netgroup_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
        client_netgroup_whitelist_extends_global_whitelist: bool
        category: _view_metadata_pb2.ViewIdMappingProto.ViewCategory
        enable_nfs_unix_authentication: bool
        enable_nfs_kerberos_authentication: bool
        enable_nfs_kerberos_integrity: bool
        enable_nfs_kerberos_privacy: bool
        is_read_only: bool
        pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
        superusers: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        self_service_snapshot_config: _view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig
        snapshot_smb_access_sids: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        enable_metadata_accelerator: bool
        view_usage: _view_usage_pb2.ViewUsageProto
        s3_folder_support_enabled: bool
        performance_config: _view_metadata_pb2.ViewIdMappingProto.PerformanceConfig
        enable_wcc: bool
        filer_lcm_rules: _view_metadata_pb2.LifecyclePolicy.LifecycleRules
        def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., create_time_msecs: _Optional[int] = ..., internal: bool = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos: _Optional[_Union[QoS, _Mapping]] = ..., subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., case_insensitive_entity_names: bool = ..., quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., iris_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.IrisMetadata, _Mapping]] = ..., smb_permissions_info: _Optional[_Union[_view_smb_permissions_pb2.ViewSmbPermissionsInfo, _Mapping]] = ..., s3_bucket_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., worm_lock_expiry_usecs: _Optional[int] = ..., enable_minion: bool = ..., logical_usage_bytes: _Optional[int] = ..., enable_filer_audit_logging: bool = ..., inherit_audit_log_from_view: bool = ..., alias_vec: _Optional[_Iterable[_Union[ViewAliasInfo, _Mapping]]] = ..., enable_mixed_mode_permissions: bool = ..., enable_smb_view_discovery: bool = ..., enable_smb_encryption: bool = ..., enforce_smb_encryption: bool = ..., enable_nfs_view_discovery: bool = ..., share_permissions: _Optional[_Iterable[_Union[_view_smb_permissions_pb2.SmbPermission, _Mapping]]] = ..., file_extension_filter: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., file_level_data_lock_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., tenant_id: _Optional[str] = ..., security_mode_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig, _Mapping]] = ..., antivirus_scan_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig, _Mapping]] = ..., target_view_for_data_migration: bool = ..., client_subnet_whitelist_extends_global_whitelist: bool = ..., s3_key_mapping_config: _Optional[_Union[_s3_metadata_pb2.S3KeyMappingConfigProto, _Mapping]] = ..., external_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ExternalMetadata, _Mapping]] = ..., enable_offline_caching: bool = ..., view_all_squash_uid: _Optional[int] = ..., view_all_squash_gid: _Optional[int] = ..., view_root_squash_uid: _Optional[int] = ..., view_root_squash_gid: _Optional[int] = ..., enable_continuous_availability: bool = ..., enable_smb_oplock: bool = ..., enable_live_indexing: bool = ..., nis_netgroup_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., client_netgroup_whitelist_extends_global_whitelist: bool = ..., category: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ViewCategory, str]] = ..., enable_nfs_unix_authentication: bool = ..., enable_nfs_kerberos_authentication: bool = ..., enable_nfs_kerberos_integrity: bool = ..., enable_nfs_kerberos_privacy: bool = ..., is_read_only: bool = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ..., superusers: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., self_service_snapshot_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig, _Mapping]] = ..., snapshot_smb_access_sids: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., enable_metadata_accelerator: bool = ..., view_usage: _Optional[_Union[_view_usage_pb2.ViewUsageProto, _Mapping]] = ..., s3_folder_support_enabled: bool = ..., performance_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PerformanceConfig, _Mapping]] = ..., enable_wcc: bool = ..., filer_lcm_rules: _Optional[_Union[_view_metadata_pb2.LifecyclePolicy.LifecycleRules, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_RESULT_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    view_vec: _containers.RepeatedCompositeFieldContainer[GetViewsResult.View]
    last_result: bool
    view_count: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., view_vec: _Optional[_Iterable[_Union[GetViewsResult.View, _Mapping]]] = ..., last_result: bool = ..., view_count: _Optional[int] = ...) -> None: ...

class CloneViewArg(_message.Message):
    __slots__ = ("src_view_name", "target_view_name", "description", "storage_policy_override", "qos", "subnet_vec", "worm_lock_expiry_usecs", "protocol_access_info", "nis_netgroup_vec", "is_read_only", "owner_sid", "is_internal")
    SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    NIS_NETGROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    OWNER_SID_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    src_view_name: str
    target_view_name: str
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos: QoS
    subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    worm_lock_expiry_usecs: int
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    nis_netgroup_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
    is_read_only: bool
    owner_sid: _cluster_config_pb2.ClusterConfigProto.SID
    is_internal: bool
    def __init__(self, src_view_name: _Optional[str] = ..., target_view_name: _Optional[str] = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos: _Optional[_Union[QoS, _Mapping]] = ..., subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., worm_lock_expiry_usecs: _Optional[int] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., nis_netgroup_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., is_read_only: bool = ..., owner_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., is_internal: bool = ...) -> None: ...

class CloneViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteViewArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class DeleteViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetMetadataCapacityArg(_message.Message):
    __slots__ = ("removed_node_id", "removed_disk_id", "metadata_fault_tolerance", "metadata_fault_tolerance_factor")
    REMOVED_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVED_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FAULT_TOLERANCE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    removed_node_id: int
    removed_disk_id: int
    metadata_fault_tolerance: _cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness
    metadata_fault_tolerance_factor: int
    def __init__(self, removed_node_id: _Optional[int] = ..., removed_disk_id: _Optional[int] = ..., metadata_fault_tolerance: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.FaultToleranceStrictness, _Mapping]] = ..., metadata_fault_tolerance_factor: _Optional[int] = ...) -> None: ...

class GetMetadataCapacityResult(_message.Message):
    __slots__ = ("status", "capacity")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    status: Status
    capacity: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., capacity: _Optional[int] = ...) -> None: ...

class ListInfectedFilesArg(_message.Message):
    __slots__ = ("view_name_vec", "include_quarantined_files", "include_unquarantined_files", "max_entries", "cookie", "file_path", "view_id_vec")
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_QUARANTINED_FILES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNQUARANTINED_FILES_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    include_quarantined_files: bool
    include_unquarantined_files: bool
    max_entries: int
    cookie: str
    file_path: str
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, view_name_vec: _Optional[_Iterable[str]] = ..., include_quarantined_files: bool = ..., include_unquarantined_files: bool = ..., max_entries: _Optional[int] = ..., cookie: _Optional[str] = ..., file_path: _Optional[str] = ..., view_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ListInfectedFilesResult(_message.Message):
    __slots__ = ("infected_files", "status")
    INFECTED_FILES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    infected_files: _rpc_service_pb2.ListInfectedFilesResult
    status: Status
    def __init__(self, infected_files: _Optional[_Union[_rpc_service_pb2.ListInfectedFilesResult, _Mapping]] = ..., status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ModifyInfectedFileStateArg(_message.Message):
    __slots__ = ("modify_arg",)
    MODIFY_ARG_FIELD_NUMBER: _ClassVar[int]
    modify_arg: _rpc_service_pb2.ModifyInfectedFileStateArg
    def __init__(self, modify_arg: _Optional[_Union[_rpc_service_pb2.ModifyInfectedFileStateArg, _Mapping]] = ...) -> None: ...

class ModifyInfectedFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteInfectedFileArg(_message.Message):
    __slots__ = ("delete_arg",)
    DELETE_ARG_FIELD_NUMBER: _ClassVar[int]
    delete_arg: _rpc_service_pb2.DeleteInfectedFileArg
    def __init__(self, delete_arg: _Optional[_Union[_rpc_service_pb2.DeleteInfectedFileArg, _Mapping]] = ...) -> None: ...

class DeleteInfectedFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetIcapConnectionStatusArg(_message.Message):
    __slots__ = ("icap_uri",)
    ICAP_URI_FIELD_NUMBER: _ClassVar[int]
    icap_uri: str
    def __init__(self, icap_uri: _Optional[str] = ...) -> None: ...

class GetIcapConnectionStatusResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class LdapEntryArg(_message.Message):
    __slots__ = ("provider", "ad_domain_name")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    AD_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    provider: _cluster_config_pb2.ClusterConfigProto.LdapConfig.LdapProvider
    ad_domain_name: str
    def __init__(self, provider: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.LdapConfig.LdapProvider, _Mapping]] = ..., ad_domain_name: _Optional[str] = ...) -> None: ...

class LdapEntryResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteLdapArg(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteLdapResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class LdapStatusArg(_message.Message):
    __slots__ = ("id", "tenant_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    tenant_id: str
    def __init__(self, id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class LdapStatusResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ActiveDirectoryEntryArg(_message.Message):
    __slots__ = ("domain_name", "user_name", "password", "machine_accounts", "dns_hostname_vec", "encryption_vec", "ou_name", "workgroup", "overwrite_existing_machine_accounts", "tenant_id_vec", "preferred_dc_vec", "blacklisted_dc_vec", "trusted_domains_disabled", "ldap_id", "nis_domain_name", "network_realm_id", "force_remove", "machine_account_vec", "task_path")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    DNS_HOSTNAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_VEC_FIELD_NUMBER: _ClassVar[int]
    OU_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKGROUP_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_MACHINE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_DOMAINS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    LDAP_ID_FIELD_NUMBER: _ClassVar[int]
    NIS_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_REMOVE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    user_name: str
    password: str
    machine_accounts: _containers.RepeatedScalarFieldContainer[str]
    dns_hostname_vec: _containers.RepeatedScalarFieldContainer[str]
    encryption_vec: _containers.RepeatedScalarFieldContainer[int]
    ou_name: str
    workgroup: str
    overwrite_existing_machine_accounts: bool
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    preferred_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    blacklisted_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    trusted_domains_disabled: bool
    ldap_id: int
    nis_domain_name: str
    network_realm_id: int
    force_remove: bool
    machine_account_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto]
    task_path: str
    def __init__(self, domain_name: _Optional[str] = ..., user_name: _Optional[str] = ..., password: _Optional[str] = ..., machine_accounts: _Optional[_Iterable[str]] = ..., dns_hostname_vec: _Optional[_Iterable[str]] = ..., encryption_vec: _Optional[_Iterable[int]] = ..., ou_name: _Optional[str] = ..., workgroup: _Optional[str] = ..., overwrite_existing_machine_accounts: bool = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., preferred_dc_vec: _Optional[_Iterable[str]] = ..., blacklisted_dc_vec: _Optional[_Iterable[str]] = ..., trusted_domains_disabled: bool = ..., ldap_id: _Optional[int] = ..., nis_domain_name: _Optional[str] = ..., network_realm_id: _Optional[int] = ..., force_remove: bool = ..., machine_account_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto, _Mapping]]] = ..., task_path: _Optional[str] = ...) -> None: ...

class ActiveDirectoryEntryResult(_message.Message):
    __slots__ = ("status", "task_path")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    status: Status
    task_path: str
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., task_path: _Optional[str] = ...) -> None: ...

class ModifyCaPathsArg(_message.Message):
    __slots__ = ("client_fqdn", "cluster_fqdn", "inter_fqdn", "tenant_id_vec", "network_realm_id", "is_add_ca_path")
    CLIENT_FQDN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FQDN_FIELD_NUMBER: _ClassVar[int]
    INTER_FQDN_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_CA_PATH_FIELD_NUMBER: _ClassVar[int]
    client_fqdn: str
    cluster_fqdn: str
    inter_fqdn: str
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    network_realm_id: int
    is_add_ca_path: bool
    def __init__(self, client_fqdn: _Optional[str] = ..., cluster_fqdn: _Optional[str] = ..., inter_fqdn: _Optional[str] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., network_realm_id: _Optional[int] = ..., is_add_ca_path: bool = ...) -> None: ...

class ModifyCaPathsResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class EditPreferredDomainControllersArg(_message.Message):
    __slots__ = ("domain_name", "preferred_dc_vec", "blacklisted_dc_vec", "tenant_id_vec", "network_realm_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    preferred_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    blacklisted_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    network_realm_id: int
    def __init__(self, domain_name: _Optional[str] = ..., preferred_dc_vec: _Optional[_Iterable[str]] = ..., blacklisted_dc_vec: _Optional[_Iterable[str]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., network_realm_id: _Optional[int] = ...) -> None: ...

class EditPreferredDomainControllersResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetCentrifyZonesArg(_message.Message):
    __slots__ = ("ad_domain_name", "tenant_id")
    AD_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ad_domain_name: str
    tenant_id: str
    def __init__(self, ad_domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class CentrifyZone(_message.Message):
    __slots__ = ("zone_name", "distinguished_name", "schema", "zone_description")
    ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ZONE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    zone_name: str
    distinguished_name: str
    schema: _cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema
    zone_description: str
    def __init__(self, zone_name: _Optional[str] = ..., distinguished_name: _Optional[str] = ..., schema: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.IdMappingInfo.CentrifySchema, str]] = ..., zone_description: _Optional[str] = ...) -> None: ...

class GetCentrifyZonesResult(_message.Message):
    __slots__ = ("status", "centrify_zones")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CENTRIFY_ZONES_FIELD_NUMBER: _ClassVar[int]
    status: Status
    centrify_zones: _containers.RepeatedCompositeFieldContainer[CentrifyZone]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., centrify_zones: _Optional[_Iterable[_Union[CentrifyZone, _Mapping]]] = ...) -> None: ...

class GetConnectionsArg(_message.Message):
    __slots__ = ("view_name_vec", "view_id_vec", "max_results", "tenant_id", "client_ip_vec", "node_ip_vec")
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    max_results: int
    tenant_id: str
    client_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_name_vec: _Optional[_Iterable[str]] = ..., view_id_vec: _Optional[_Iterable[int]] = ..., max_results: _Optional[int] = ..., tenant_id: _Optional[str] = ..., client_ip_vec: _Optional[_Iterable[str]] = ..., node_ip_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNfsConnectionsResult(_message.Message):
    __slots__ = ("status", "connection_vec")
    class Connection(_message.Message):
        __slots__ = ("view_name", "view_id", "client_ip", "server_ip", "node_ip", "tenant_id", "mount_path", "uid", "gid", "uptime_usecs")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        GID_FIELD_NUMBER: _ClassVar[int]
        UPTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        view_id: int
        client_ip: str
        server_ip: str
        node_ip: str
        tenant_id: str
        mount_path: str
        uid: int
        gid: int
        uptime_usecs: int
        def __init__(self, view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., client_ip: _Optional[str] = ..., server_ip: _Optional[str] = ..., node_ip: _Optional[str] = ..., tenant_id: _Optional[str] = ..., mount_path: _Optional[str] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., uptime_usecs: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    connection_vec: _containers.RepeatedCompositeFieldContainer[GetNfsConnectionsResult.Connection]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., connection_vec: _Optional[_Iterable[_Union[GetNfsConnectionsResult.Connection, _Mapping]]] = ...) -> None: ...

class GetSmbConnectionsResult(_message.Message):
    __slots__ = ("status", "connection_vec")
    class Connection(_message.Message):
        __slots__ = ("view_name", "view_id", "client_ip", "server_ip", "user_name", "domain_name", "path", "internal_view", "session_id", "node_ip", "token_sid_vec", "tenant_id", "dialect", "uptime_usecs")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        TOKEN_SID_VEC_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        DIALECT_FIELD_NUMBER: _ClassVar[int]
        UPTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        view_id: int
        client_ip: str
        server_ip: str
        user_name: str
        domain_name: str
        path: str
        internal_view: bool
        session_id: int
        node_ip: str
        token_sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        tenant_id: str
        dialect: int
        uptime_usecs: int
        def __init__(self, view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., client_ip: _Optional[str] = ..., server_ip: _Optional[str] = ..., user_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., path: _Optional[str] = ..., internal_view: bool = ..., session_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., token_sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., dialect: _Optional[int] = ..., uptime_usecs: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    connection_vec: _containers.RepeatedCompositeFieldContainer[GetSmbConnectionsResult.Connection]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., connection_vec: _Optional[_Iterable[_Union[GetSmbConnectionsResult.Connection, _Mapping]]] = ...) -> None: ...

class GetClusterConnectionsSummaryArg(_message.Message):
    __slots__ = ("view_name_vec", "view_id_vec", "tenant_id")
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    tenant_id: str
    def __init__(self, view_name_vec: _Optional[_Iterable[str]] = ..., view_id_vec: _Optional[_Iterable[int]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetClusterConnectionsSummaryResult(_message.Message):
    __slots__ = ("status", "connection_summary_vec")
    class ConnectionSummary(_message.Message):
        __slots__ = ("server_ip", "node_ip", "nfs_connection_count", "smb_connection_count")
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        NFS_CONNECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        SMB_CONNECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        server_ip: str
        node_ip: str
        nfs_connection_count: int
        smb_connection_count: int
        def __init__(self, server_ip: _Optional[str] = ..., node_ip: _Optional[str] = ..., nfs_connection_count: _Optional[int] = ..., smb_connection_count: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    connection_summary_vec: _containers.RepeatedCompositeFieldContainer[GetClusterConnectionsSummaryResult.ConnectionSummary]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., connection_summary_vec: _Optional[_Iterable[_Union[GetClusterConnectionsSummaryResult.ConnectionSummary, _Mapping]]] = ...) -> None: ...

class RenameViewArg(_message.Message):
    __slots__ = ("existing_view_name", "new_view_name")
    EXISTING_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    existing_view_name: str
    new_view_name: str
    def __init__(self, existing_view_name: _Optional[str] = ..., new_view_name: _Optional[str] = ...) -> None: ...

class RenameViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class OverwriteViewArg(_message.Message):
    __slots__ = ("source_view_name", "target_view_name")
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    source_view_name: str
    target_view_name: str
    def __init__(self, source_view_name: _Optional[str] = ..., target_view_name: _Optional[str] = ...) -> None: ...

class OverwriteViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class CloneDirectoryArg(_message.Message):
    __slots__ = ("source_dir_path", "dest_parent_dir_path", "dest_dir_name")
    SOURCE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    DEST_PARENT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    DEST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    source_dir_path: str
    dest_parent_dir_path: str
    dest_dir_name: str
    def __init__(self, source_dir_path: _Optional[str] = ..., dest_parent_dir_path: _Optional[str] = ..., dest_dir_name: _Optional[str] = ...) -> None: ...

class CloneDirectoryResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class SetSmbPermissionsViewArg(_message.Message):
    __slots__ = ("view_name", "smb_permissions_info")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SMB_PERMISSIONS_INFO_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    smb_permissions_info: _view_smb_permissions_pb2.ViewSmbPermissionsInfo
    def __init__(self, view_name: _Optional[str] = ..., smb_permissions_info: _Optional[_Union[_view_smb_permissions_pb2.ViewSmbPermissionsInfo, _Mapping]] = ...) -> None: ...

class SetSmbPermissionsViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class WriteClusterAuditLogRecordArg(_message.Message):
    __slots__ = ("audit_doc",)
    AUDIT_DOC_FIELD_NUMBER: _ClassVar[int]
    audit_doc: _cluster_audit_document_pb2.ClusterAuditDocument
    def __init__(self, audit_doc: _Optional[_Union[_cluster_audit_document_pb2.ClusterAuditDocument, _Mapping]] = ...) -> None: ...

class WriteClusterAuditLogRecordResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetActiveOpenSmbFilesArg(_message.Message):
    __slots__ = ("view_name", "file_path", "max_results", "cookie")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    max_results: int
    cookie: str
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., max_results: _Optional[int] = ..., cookie: _Optional[str] = ...) -> None: ...

class GetActiveOpenSmbFilesResult(_message.Message):
    __slots__ = ("status", "file_opens")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILE_OPENS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    file_opens: _list_smb_active_opens_pb2.ListSmbAllActiveOpensResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., file_opens: _Optional[_Union[_list_smb_active_opens_pb2.ListSmbAllActiveOpensResult, _Mapping]] = ...) -> None: ...

class CloseActiveOpenSmbFileArg(_message.Message):
    __slots__ = ("view_name", "file_path", "open_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    open_id: int
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., open_id: _Optional[int] = ...) -> None: ...

class CloseActiveOpenSmbFileResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ViewAlias(_message.Message):
    __slots__ = ("alias_name", "view_name", "view_path", "smb_config", "client_subnet_whitelist", "enable_audit_logging", "overwrite_view_audit_logging")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_VIEW_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    view_name: str
    view_path: str
    smb_config: _view_smb_permissions_pb2.AliasSmbConfig
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_audit_logging: bool
    overwrite_view_audit_logging: bool
    def __init__(self, alias_name: _Optional[str] = ..., view_name: _Optional[str] = ..., view_path: _Optional[str] = ..., smb_config: _Optional[_Union[_view_smb_permissions_pb2.AliasSmbConfig, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_audit_logging: bool = ..., overwrite_view_audit_logging: bool = ...) -> None: ...

class CreateViewAliasResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateViewAliasArg(_message.Message):
    __slots__ = ("alias_name", "smb_config", "client_subnet_whitelist", "enable_audit_logging", "overwrite_view_audit_logging")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_VIEW_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    smb_config: _view_smb_permissions_pb2.AliasSmbConfig
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_audit_logging: bool
    overwrite_view_audit_logging: bool
    def __init__(self, alias_name: _Optional[str] = ..., smb_config: _Optional[_Union[_view_smb_permissions_pb2.AliasSmbConfig, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_audit_logging: bool = ..., overwrite_view_audit_logging: bool = ...) -> None: ...

class UpdateViewAliasResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class DeleteViewAliasArg(_message.Message):
    __slots__ = ("alias_name",)
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    def __init__(self, alias_name: _Optional[str] = ...) -> None: ...

class DeleteViewAliasResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ViewAliasInfo(_message.Message):
    __slots__ = ("alias_name", "view_path", "smb_config", "client_subnet_whitelist", "audit_logging_config")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    view_path: str
    smb_config: _view_smb_permissions_pb2.AliasSmbConfig
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    audit_logging_config: _cluster_config_pb2.ClusterConfigProto.AuditLoggingConfig
    def __init__(self, alias_name: _Optional[str] = ..., view_path: _Optional[str] = ..., smb_config: _Optional[_Union[_view_smb_permissions_pb2.AliasSmbConfig, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., audit_logging_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ...) -> None: ...

class AdSearchArg(_message.Message):
    __slots__ = ("domain", "filter", "attributes", "max_results", "tenant_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    filter: str
    attributes: _containers.RepeatedScalarFieldContainer[str]
    max_results: int
    tenant_id: str
    def __init__(self, domain: _Optional[str] = ..., filter: _Optional[str] = ..., attributes: _Optional[_Iterable[str]] = ..., max_results: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class LdapAttributeValues(_message.Message):
    __slots__ = ("attribute_map",)
    class AttrValue(_message.Message):
        __slots__ = ("value_vec",)
        VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
        value_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, value_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class AttributeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: LdapAttributeValues.AttrValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[LdapAttributeValues.AttrValue, _Mapping]] = ...) -> None: ...
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    attribute_map: _containers.MessageMap[str, LdapAttributeValues.AttrValue]
    def __init__(self, attribute_map: _Optional[_Mapping[str, LdapAttributeValues.AttrValue]] = ...) -> None: ...

class AdSearchResult(_message.Message):
    __slots__ = ("status", "result_vec")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    result_vec: _containers.RepeatedCompositeFieldContainer[LdapAttributeValues]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[LdapAttributeValues, _Mapping]]] = ...) -> None: ...

class GetIrisMasterResult(_message.Message):
    __slots__ = ("status", "master_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MASTER_INFO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    master_info: _liveness_pb2.LivenessProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., master_info: _Optional[_Union[_liveness_pb2.LivenessProto, _Mapping]] = ...) -> None: ...

class WriteColumnArg(_message.Message):
    __slots__ = ("table_name", "key", "version", "column_key", "data")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COLUMN_KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    key: str
    version: int
    column_key: str
    data: bytes
    def __init__(self, table_name: _Optional[str] = ..., key: _Optional[str] = ..., version: _Optional[int] = ..., column_key: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class WriteColumnResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ReadColumnArg(_message.Message):
    __slots__ = ("table_name", "key", "column_key")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_KEY_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    key: str
    column_key: str
    def __init__(self, table_name: _Optional[str] = ..., key: _Optional[str] = ..., column_key: _Optional[str] = ...) -> None: ...

class ReadColumnResult(_message.Message):
    __slots__ = ("status", "version", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: Status
    version: int
    data: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., version: _Optional[int] = ..., data: _Optional[_Iterable[bytes]] = ...) -> None: ...

class UsersQuotaAndUsageForViewResult(_message.Message):
    __slots__ = ("status", "users_quota_and_usage")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USERS_QUOTA_AND_USAGE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    users_quota_and_usage: _rpc_service_pb2.ListUserQuotaResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., users_quota_and_usage: _Optional[_Union[_rpc_service_pb2.ListUserQuotaResult, _Mapping]] = ...) -> None: ...

class UpdateUserQuotaOverridesInViewResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class QuotaAndUsageForUserInAllViewsParams(_message.Message):
    __slots__ = ("user_id", "max_entries", "max_view_id", "view_name_vec")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    user_id: _quota_tree_metadata_pb2.QuotaUID
    max_entries: int
    max_view_id: int
    view_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ..., max_entries: _Optional[int] = ..., max_view_id: _Optional[int] = ..., view_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class QuotaAndUsageForUserInAllViewsResult(_message.Message):
    __slots__ = ("status", "view_quota_and_usage_vec")
    class QuotaAndUsageResult(_message.Message):
        __slots__ = ("view_id", "view_name", "quota_policy", "usage_in_bytes")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
        USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        view_name: str
        quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
        usage_in_bytes: int
        def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., usage_in_bytes: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_QUOTA_AND_USAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    view_quota_and_usage_vec: _containers.RepeatedCompositeFieldContainer[QuotaAndUsageForUserInAllViewsResult.QuotaAndUsageResult]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., view_quota_and_usage_vec: _Optional[_Iterable[_Union[QuotaAndUsageForUserInAllViewsResult.QuotaAndUsageResult, _Mapping]]] = ...) -> None: ...

class UserQuotaSummaryForViewResponse(_message.Message):
    __slots__ = ("status", "user_quota_summary_for_view")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_QUOTA_SUMMARY_FOR_VIEW_FIELD_NUMBER: _ClassVar[int]
    status: Status
    user_quota_summary_for_view: _rpc_service_pb2.GetUserQuotaSummaryForViewResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., user_quota_summary_for_view: _Optional[_Union[_rpc_service_pb2.GetUserQuotaSummaryForViewResult, _Mapping]] = ...) -> None: ...

class UserQuotaSummaryForUserResponse(_message.Message):
    __slots__ = ("status", "view_count", "num_views_above_hard_limit", "num_views_above_alert_threshold")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEWS_ABOVE_HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEWS_ABOVE_ALERT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    status: Status
    view_count: int
    num_views_above_hard_limit: int
    num_views_above_alert_threshold: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., view_count: _Optional[int] = ..., num_views_above_hard_limit: _Optional[int] = ..., num_views_above_alert_threshold: _Optional[int] = ...) -> None: ...

class LibrarianDocumentsResponse(_message.Message):
    __slots__ = ("status", "search_documents_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DOCUMENTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    search_documents_result: _librarian_pb2.GetDocumentsResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., search_documents_result: _Optional[_Union[_librarian_pb2.GetDocumentsResult, _Mapping]] = ...) -> None: ...

class UpdateFileDataLockArg(_message.Message):
    __slots__ = ("view_name", "file_path", "lock_expiry_usecs", "is_privileged")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    lock_expiry_usecs: int
    is_privileged: bool
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., lock_expiry_usecs: _Optional[int] = ..., is_privileged: bool = ...) -> None: ...

class UpdateFileDataLockResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class RestoreViewAliasesArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class RestoreViewAliasesResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetFileDataLockArg(_message.Message):
    __slots__ = ("view_name", "file_path")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class GetFileDataLockResult(_message.Message):
    __slots__ = ("status", "file_lock_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCK_INFO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    file_lock_info: _get_fld_info_result_pb2.FileLevelDataLockResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., file_lock_info: _Optional[_Union[_get_fld_info_result_pb2.FileLevelDataLockResult, _Mapping]] = ...) -> None: ...

class WatchTenantConfigResult(_message.Message):
    __slots__ = ("version", "tenants_proto")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANTS_PROTO_FIELD_NUMBER: _ClassVar[int]
    version: int
    tenants_proto: _tenants_pb2.Tenants
    def __init__(self, version: _Optional[int] = ..., tenants_proto: _Optional[_Union[_tenants_pb2.Tenants, _Mapping]] = ...) -> None: ...

class GetTrustedDomainsArg(_message.Message):
    __slots__ = ("domain", "tenant_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    tenant_id: str
    def __init__(self, domain: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class TriggerTrustedDomainDiscoveryArgs(_message.Message):
    __slots__ = ("primary_domain_fqdn", "task_identifier", "tenant_id")
    PRIMARY_DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    primary_domain_fqdn: str
    task_identifier: str
    tenant_id: str
    def __init__(self, primary_domain_fqdn: _Optional[str] = ..., task_identifier: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class TriggerTrustedDomainDiscoveryResult(_message.Message):
    __slots__ = ("status", "task_identifier")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    status: Status
    task_identifier: str
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., task_identifier: _Optional[str] = ...) -> None: ...

class TrustedDomainDiscoveryStatusArgs(_message.Message):
    __slots__ = ("primary_domain_fqdn", "task_identifier", "tenant_id")
    PRIMARY_DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    primary_domain_fqdn: str
    task_identifier: str
    tenant_id: str
    def __init__(self, primary_domain_fqdn: _Optional[str] = ..., task_identifier: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class TrustedDomainDiscoveryStatusResult(_message.Message):
    __slots__ = ("status", "is_discovery_running")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_DISCOVERY_RUNNING_FIELD_NUMBER: _ClassVar[int]
    status: Status
    is_discovery_running: bool
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., is_discovery_running: bool = ...) -> None: ...

class GetTrustedDomainsResult(_message.Message):
    __slots__ = ("status", "trusted_domain_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_DOMAIN_INFO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    trusted_domain_info: _rpc_service_pb2.GetTrustedDomainsResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., trusted_domain_info: _Optional[_Union[_rpc_service_pb2.GetTrustedDomainsResult, _Mapping]] = ...) -> None: ...

class GetAdInfoFromSidsArg(_message.Message):
    __slots__ = ("sid_vec", "tenant_id")
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    sid_vec: _containers.RepeatedScalarFieldContainer[str]
    tenant_id: str
    def __init__(self, sid_vec: _Optional[_Iterable[str]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetAdInfoFromSidsResult(_message.Message):
    __slots__ = ("status", "get_ad_info_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GET_AD_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    get_ad_info_result: _rpc_service_pb2.GetAdInfoFromSidsResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., get_ad_info_result: _Optional[_Union[_rpc_service_pb2.GetAdInfoFromSidsResult, _Mapping]] = ...) -> None: ...

class AuthenticateUserArg(_message.Message):
    __slots__ = ("domain_name", "username", "password", "tenant_id", "ldap_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    LDAP_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    username: str
    password: str
    tenant_id: str
    ldap_id: int
    def __init__(self, domain_name: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., tenant_id: _Optional[str] = ..., ldap_id: _Optional[int] = ...) -> None: ...

class AuthenticateUserResult(_message.Message):
    __slots__ = ("status", "authenticate_user_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATE_USER_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    authenticate_user_result: _rpc_service_pb2.AuthenticateUserResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., authenticate_user_result: _Optional[_Union[_rpc_service_pb2.AuthenticateUserResult, _Mapping]] = ...) -> None: ...

class GetBifrostServerInfoArg(_message.Message):
    __slots__ = ("tenant_id_vec",)
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenant_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBifrostServerInfoResult(_message.Message):
    __slots__ = ("status", "server_info_vec")
    class ServerInfo(_message.Message):
        __slots__ = ("tenant_id", "constituent_id", "ip_address", "broker_node_id", "broker_constituent_id", "version", "tenant_source_side_ip")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        BROKER_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        BROKER_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        TENANT_SOURCE_SIDE_IP_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        constituent_id: int
        ip_address: str
        broker_node_id: int
        broker_constituent_id: int
        version: str
        tenant_source_side_ip: str
        def __init__(self, tenant_id: _Optional[str] = ..., constituent_id: _Optional[int] = ..., ip_address: _Optional[str] = ..., broker_node_id: _Optional[int] = ..., broker_constituent_id: _Optional[int] = ..., version: _Optional[str] = ..., tenant_source_side_ip: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    server_info_vec: _containers.RepeatedCompositeFieldContainer[GetBifrostServerInfoResult.ServerInfo]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., server_info_vec: _Optional[_Iterable[_Union[GetBifrostServerInfoResult.ServerInfo, _Mapping]]] = ...) -> None: ...

class UpdateBifrostReverseTunnelArg(_message.Message):
    __slots__ = ("bifrost_server_id", "rt_config")
    BIFROST_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    RT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    bifrost_server_id: _bifrost_base_pb2.BifrostServerIdProto
    rt_config: _bifrost_base_pb2.BifrostRtConfigProto
    def __init__(self, bifrost_server_id: _Optional[_Union[_bifrost_base_pb2.BifrostServerIdProto, _Mapping]] = ..., rt_config: _Optional[_Union[_bifrost_base_pb2.BifrostRtConfigProto, _Mapping]] = ...) -> None: ...

class UpdateBifrostReverseTunnelResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetAdUserGroupSidsArg(_message.Message):
    __slots__ = ("sid",)
    SID_FIELD_NUMBER: _ClassVar[int]
    sid: str
    def __init__(self, sid: _Optional[str] = ...) -> None: ...

class GetAdUserGroupSidsResult(_message.Message):
    __slots__ = ("status", "ad_user_group_sids_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AD_USER_GROUP_SIDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    ad_user_group_sids_result: _rpc_service_pb2.GetAdUserGroupSidsResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., ad_user_group_sids_result: _Optional[_Union[_rpc_service_pb2.GetAdUserGroupSidsResult, _Mapping]] = ...) -> None: ...

class ListNlmLocksArg(_message.Message):
    __slots__ = ("view_name", "file_path", "max_results", "cookie")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    max_results: int
    cookie: str
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., max_results: _Optional[int] = ..., cookie: _Optional[str] = ...) -> None: ...

class ListNlmLocksResult(_message.Message):
    __slots__ = ("status", "locks")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCKS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    locks: _list_nlm_locks_pb2.ListNLMLocksResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., locks: _Optional[_Union[_list_nlm_locks_pb2.ListNLMLocksResult, _Mapping]] = ...) -> None: ...

class ClearNlmLocksArg(_message.Message):
    __slots__ = ("view_name", "file_path", "client_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    client_id: str
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class ClearNlmLocksResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class PrepareCrackedFileIndexArg(_message.Message):
    __slots__ = ("prepare_cracked_file_index_arg",)
    PREPARE_CRACKED_FILE_INDEX_ARG_FIELD_NUMBER: _ClassVar[int]
    prepare_cracked_file_index_arg: _yoda_rpc_args_pb2.PrepareCrackedFileIndexArg
    def __init__(self, prepare_cracked_file_index_arg: _Optional[_Union[_yoda_rpc_args_pb2.PrepareCrackedFileIndexArg, _Mapping]] = ...) -> None: ...

class PrepareCrackedFileIndexResult(_message.Message):
    __slots__ = ("status", "prepare_cracked_file_index_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PREPARE_CRACKED_FILE_INDEX_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    prepare_cracked_file_index_result: _yoda_rpc_args_pb2.PrepareCrackedFileIndexResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., prepare_cracked_file_index_result: _Optional[_Union[_yoda_rpc_args_pb2.PrepareCrackedFileIndexResult, _Mapping]] = ...) -> None: ...

class GetCrackedFileIndexArg(_message.Message):
    __slots__ = ("get_cracked_file_index_arg",)
    GET_CRACKED_FILE_INDEX_ARG_FIELD_NUMBER: _ClassVar[int]
    get_cracked_file_index_arg: _yoda_rpc_args_pb2.GetCrackedFileIndexArg
    def __init__(self, get_cracked_file_index_arg: _Optional[_Union[_yoda_rpc_args_pb2.GetCrackedFileIndexArg, _Mapping]] = ...) -> None: ...

class GetCrackedFileIndexResult(_message.Message):
    __slots__ = ("status", "get_cracked_file_index_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GET_CRACKED_FILE_INDEX_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    get_cracked_file_index_result: _yoda_rpc_args_pb2.GetCrackedFileIndexResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., get_cracked_file_index_result: _Optional[_Union[_yoda_rpc_args_pb2.GetCrackedFileIndexResult, _Mapping]] = ...) -> None: ...

class ReleaseCrackedFileIndexArg(_message.Message):
    __slots__ = ("release_cracked_file_index_arg",)
    RELEASE_CRACKED_FILE_INDEX_ARG_FIELD_NUMBER: _ClassVar[int]
    release_cracked_file_index_arg: _yoda_rpc_args_pb2.ReleaseCrackedFileIndexArg
    def __init__(self, release_cracked_file_index_arg: _Optional[_Union[_yoda_rpc_args_pb2.ReleaseCrackedFileIndexArg, _Mapping]] = ...) -> None: ...

class ReleaseCrackedFileIndexResult(_message.Message):
    __slots__ = ("status", "release_cracked_file_index_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CRACKED_FILE_INDEX_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    release_cracked_file_index_result: _yoda_rpc_args_pb2.ReleaseCrackedFileIndexResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., release_cracked_file_index_result: _Optional[_Union[_yoda_rpc_args_pb2.ReleaseCrackedFileIndexResult, _Mapping]] = ...) -> None: ...

class UpdateDirQuotaConfigResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateDirQuotaResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetDirQuotaInfoResult(_message.Message):
    __slots__ = ("status", "quota_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_INFO_FIELD_NUMBER: _ClassVar[int]
    status: Status
    quota_info: _rpc_service_pb2.ListDirQuotaResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., quota_info: _Optional[_Union[_rpc_service_pb2.ListDirQuotaResult, _Mapping]] = ...) -> None: ...

class GetDomainControllersArg(_message.Message):
    __slots__ = ("domain_name", "tenant_id", "network_realm_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    tenant_id: str
    network_realm_id: int
    def __init__(self, domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ...) -> None: ...

class GetDomainControllersResult(_message.Message):
    __slots__ = ("status", "domain_controllers")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTROLLERS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    domain_controllers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., domain_controllers: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDomainControllerStatusArg(_message.Message):
    __slots__ = ("domain_name", "tenant_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    tenant_id: str
    def __init__(self, domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetDomainControllerStatusResult(_message.Message):
    __slots__ = ("status", "domain_controller")
    class ConnectionStatus(_message.Message):
        __slots__ = ("name", "status")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        name: str
        status: _rpc_service_pb2.GetAdDomainControllerStatusResult.DcInfo.DcStatus
        def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[_rpc_service_pb2.GetAdDomainControllerStatusResult.DcInfo.DcStatus, str]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    status: Status
    domain_controller: _containers.RepeatedCompositeFieldContainer[GetDomainControllerStatusResult.ConnectionStatus]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., domain_controller: _Optional[_Iterable[_Union[GetDomainControllerStatusResult.ConnectionStatus, _Mapping]]] = ...) -> None: ...

class CreateOrUpdateKeystoneArg(_message.Message):
    __slots__ = ("create_or_update_arg",)
    CREATE_OR_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    create_or_update_arg: _rpc_service_pb2.ValidateKeystoneConfigArg
    def __init__(self, create_or_update_arg: _Optional[_Union[_rpc_service_pb2.ValidateKeystoneConfigArg, _Mapping]] = ...) -> None: ...

class CreateOrUpdateKeystoneResult(_message.Message):
    __slots__ = ("status", "create_or_update_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_OR_UPDATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    create_or_update_result: _rpc_service_pb2.ValidateKeystoneConfigResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., create_or_update_result: _Optional[_Union[_rpc_service_pb2.ValidateKeystoneConfigResult, _Mapping]] = ...) -> None: ...

class CreateOrUpdateSwiftArg(_message.Message):
    __slots__ = ("create_or_update_arg",)
    CREATE_OR_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    create_or_update_arg: _rpc_service_pb2.ValidateSwiftConfigArg
    def __init__(self, create_or_update_arg: _Optional[_Union[_rpc_service_pb2.ValidateSwiftConfigArg, _Mapping]] = ...) -> None: ...

class CreateOrUpdateSwiftResult(_message.Message):
    __slots__ = ("status", "create_or_update_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_OR_UPDATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: Status
    create_or_update_result: _rpc_service_pb2.ValidateSwiftConfigResult
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., create_or_update_result: _Optional[_Union[_rpc_service_pb2.ValidateSwiftConfigResult, _Mapping]] = ...) -> None: ...

class RegisterSwiftArg(_message.Message):
    __slots__ = ("tenant_id", "keystone")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    keystone: _rpc_service_pb2.ValidateKeystoneConfigArg
    def __init__(self, tenant_id: _Optional[str] = ..., keystone: _Optional[_Union[_rpc_service_pb2.ValidateKeystoneConfigArg, _Mapping]] = ...) -> None: ...

class RegisterSwiftResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UnregisterSwiftArg(_message.Message):
    __slots__ = ("tenant_id", "keystone")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    keystone: _rpc_service_pb2.ValidateKeystoneConfigArg
    def __init__(self, tenant_id: _Optional[str] = ..., keystone: _Optional[_Union[_rpc_service_pb2.ValidateKeystoneConfigArg, _Mapping]] = ...) -> None: ...

class UnregisterSwiftResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class NisProviderEntryArg(_message.Message):
    __slots__ = ("nis_domain_name", "master_server_hostname", "slave_servers_hostname_vec")
    NIS_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    MASTER_SERVER_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SERVERS_HOSTNAME_VEC_FIELD_NUMBER: _ClassVar[int]
    nis_domain_name: str
    master_server_hostname: str
    slave_servers_hostname_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, nis_domain_name: _Optional[str] = ..., master_server_hostname: _Optional[str] = ..., slave_servers_hostname_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class NisProviderEntryResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ClearBridgeCacheArg(_message.Message):
    __slots__ = ("clear_cache_on_all_nodes", "clear_ad_provider_cache", "clear_ldap_provider_cache", "clear_nis_provider_cache", "tenant_id", "clear_s3_abac_cache")
    CLEAR_CACHE_ON_ALL_NODES_FIELD_NUMBER: _ClassVar[int]
    CLEAR_AD_PROVIDER_CACHE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_LDAP_PROVIDER_CACHE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_NIS_PROVIDER_CACHE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLEAR_S3_ABAC_CACHE_FIELD_NUMBER: _ClassVar[int]
    clear_cache_on_all_nodes: bool
    clear_ad_provider_cache: bool
    clear_ldap_provider_cache: bool
    clear_nis_provider_cache: bool
    tenant_id: str
    clear_s3_abac_cache: bool
    def __init__(self, clear_cache_on_all_nodes: bool = ..., clear_ad_provider_cache: bool = ..., clear_ldap_provider_cache: bool = ..., clear_nis_provider_cache: bool = ..., tenant_id: _Optional[str] = ..., clear_s3_abac_cache: bool = ...) -> None: ...

class ClearBridgeCacheResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateLdapBindCredentialsForAdArg(_message.Message):
    __slots__ = ("domain_name", "ldap_bind_user_name", "ldap_bind_user_password", "clear_credentials")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    LDAP_BIND_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    LDAP_BIND_USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLEAR_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    ldap_bind_user_name: str
    ldap_bind_user_password: str
    clear_credentials: bool
    def __init__(self, domain_name: _Optional[str] = ..., ldap_bind_user_name: _Optional[str] = ..., ldap_bind_user_password: _Optional[str] = ..., clear_credentials: bool = ...) -> None: ...

class UpdateLdapBindCredentialsForAdResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class CreateViewTemplateArg(_message.Message):
    __slots__ = ("view_template",)
    VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    view_template: _view_metadata_pb2.Template
    def __init__(self, view_template: _Optional[_Union[_view_metadata_pb2.Template, _Mapping]] = ...) -> None: ...

class CreateViewTemplateResult(_message.Message):
    __slots__ = ("status", "template_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    template_id: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., template_id: _Optional[int] = ...) -> None: ...

class DeleteViewTemplateArg(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class DeleteViewTemplateResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UpdateViewTemplateArg(_message.Message):
    __slots__ = ("version", "view_template")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    version: int
    view_template: _view_metadata_pb2.Template
    def __init__(self, version: _Optional[int] = ..., view_template: _Optional[_Union[_view_metadata_pb2.Template, _Mapping]] = ...) -> None: ...

class UpdateViewTemplateResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class ReadViewTemplateByIdArg(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class ReadViewTemplateByIdResult(_message.Message):
    __slots__ = ("status", "version", "view_template")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    version: int
    view_template: _view_metadata_pb2.Template
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., version: _Optional[int] = ..., view_template: _Optional[_Union[_view_metadata_pb2.Template, _Mapping]] = ...) -> None: ...

class ReadViewTemplatesArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadViewTemplatesResult(_message.Message):
    __slots__ = ("status", "view_template")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    view_template: _containers.RepeatedCompositeFieldContainer[_view_metadata_pb2.Template]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., view_template: _Optional[_Iterable[_Union[_view_metadata_pb2.Template, _Mapping]]] = ...) -> None: ...

class GetBifrostTenantsCapabilitiesArg(_message.Message):
    __slots__ = ("tenant_ids", "include_all_caps_if_no_hyx_connected", "realm_ids")
    TENANT_IDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_CAPS_IF_NO_HYX_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    REALM_IDS_FIELD_NUMBER: _ClassVar[int]
    tenant_ids: _containers.RepeatedScalarFieldContainer[str]
    include_all_caps_if_no_hyx_connected: bool
    realm_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tenant_ids: _Optional[_Iterable[str]] = ..., include_all_caps_if_no_hyx_connected: bool = ..., realm_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetBifrostTenantsCapabilitiesResult(_message.Message):
    __slots__ = ("status", "tenant_capabilities", "all_cluster_capabilities", "realm_capabilities")
    class TenantCapabilities(_message.Message):
        __slots__ = ("tenant_id", "capabilities")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        capabilities: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, tenant_id: _Optional[str] = ..., capabilities: _Optional[_Iterable[str]] = ...) -> None: ...
    class RealmCapabilities(_message.Message):
        __slots__ = ("realm_id", "capabilities")
        REALM_ID_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        realm_id: int
        capabilities: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, realm_id: _Optional[int] = ..., capabilities: _Optional[_Iterable[str]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ALL_CLUSTER_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REALM_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    status: Status
    tenant_capabilities: _containers.RepeatedCompositeFieldContainer[GetBifrostTenantsCapabilitiesResult.TenantCapabilities]
    all_cluster_capabilities: _containers.RepeatedScalarFieldContainer[str]
    realm_capabilities: _containers.RepeatedCompositeFieldContainer[GetBifrostTenantsCapabilitiesResult.RealmCapabilities]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., tenant_capabilities: _Optional[_Iterable[_Union[GetBifrostTenantsCapabilitiesResult.TenantCapabilities, _Mapping]]] = ..., all_cluster_capabilities: _Optional[_Iterable[str]] = ..., realm_capabilities: _Optional[_Iterable[_Union[GetBifrostTenantsCapabilitiesResult.RealmCapabilities, _Mapping]]] = ...) -> None: ...

class LookupPathArg(_message.Message):
    __slots__ = ("path", "qos_context")
    PATH_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    path: str
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    def __init__(self, path: _Optional[str] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ...) -> None: ...

class LookupPathResult(_message.Message):
    __slots__ = ("status", "entity_handle")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    entity_handle: _entity_handle_pb2.EntityHandleProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class CreateFileArg(_message.Message):
    __slots__ = ("dir_eh", "file_name", "ctype", "create_verifier", "mode", "uid", "gid", "size_bytes", "ctime_usecs", "mtime_usecs", "entity_id", "expected_entity_id", "extended_attr", "s3_metadata", "qos_context", "creation_time_usecs", "archived_location", "hdfs_attrs")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CTYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTR_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    HDFS_ATTRS_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    file_name: str
    ctype: _rpc_service_pb2_1.CreateFileArg.CreateType
    create_verifier: int
    mode: int
    uid: int
    gid: int
    size_bytes: int
    ctime_usecs: int
    mtime_usecs: int
    entity_id: int
    expected_entity_id: int
    extended_attr: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    creation_time_usecs: int
    archived_location: _cloud_pb2.ArchivedLocation
    hdfs_attrs: _snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., file_name: _Optional[str] = ..., ctype: _Optional[_Union[_rpc_service_pb2_1.CreateFileArg.CreateType, str]] = ..., create_verifier: _Optional[int] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., size_bytes: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., expected_entity_id: _Optional[int] = ..., extended_attr: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., archived_location: _Optional[_Union[_cloud_pb2.ArchivedLocation, _Mapping]] = ..., hdfs_attrs: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.HdfsAttributes, _Mapping]] = ...) -> None: ...

class CreateFileResult(_message.Message):
    __slots__ = ("status", "entity_handle")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    entity_handle: _entity_handle_pb2.EntityHandleProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class CreateEntityArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "mode", "uid", "gid", "size_bytes", "ctime_usecs", "mtime_usecs", "create_type", "node_info", "dir_info", "link_info", "file_info", "qos_context", "creation_time_usecs", "entity_id", "is_forwarded", "request_id", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_inode_created", "is_retry")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    DIR_INFO_FIELD_NUMBER: _ClassVar[int]
    LINK_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_INODE_CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_RETRY_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    mode: int
    uid: int
    gid: int
    size_bytes: int
    ctime_usecs: int
    mtime_usecs: int
    create_type: _rpc_service_pb2_1.CreateEntityArg.CreateEntityType
    node_info: _rpc_service_pb2_1.CreateEntityArg.MknodInfo
    dir_info: _rpc_service_pb2_1.CreateEntityArg.MkdirInfo
    link_info: _rpc_service_pb2_1.CreateEntityArg.SymlinkInfo
    file_info: _rpc_service_pb2_1.CreateEntityArg.FileInfo
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    creation_time_usecs: int
    entity_id: int
    is_forwarded: bool
    request_id: int
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_inode_created: bool
    is_retry: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., size_bytes: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., create_type: _Optional[_Union[_rpc_service_pb2_1.CreateEntityArg.CreateEntityType, str]] = ..., node_info: _Optional[_Union[_rpc_service_pb2_1.CreateEntityArg.MknodInfo, _Mapping]] = ..., dir_info: _Optional[_Union[_rpc_service_pb2_1.CreateEntityArg.MkdirInfo, _Mapping]] = ..., link_info: _Optional[_Union[_rpc_service_pb2_1.CreateEntityArg.SymlinkInfo, _Mapping]] = ..., file_info: _Optional[_Union[_rpc_service_pb2_1.CreateEntityArg.FileInfo, _Mapping]] = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., creation_time_usecs: _Optional[int] = ..., entity_id: _Optional[int] = ..., is_forwarded: bool = ..., request_id: _Optional[int] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_inode_created: bool = ..., is_retry: bool = ...) -> None: ...

class CreateEntityResult(_message.Message):
    __slots__ = ("status", "entity_handle")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    status: Status
    entity_handle: _entity_handle_pb2.EntityHandleProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class WriteEntityArg(_message.Message):
    __slots__ = ("eh", "offset", "is_optional", "durability", "stats_container", "is_magneto_request", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_blob_ticket_sequencer", "constituent_id", "is_forwarded", "qos_context", "forwarding_enabled", "data", "force_complete_write", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "expect_non_mega_file")
    EH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    DURABILITY_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_BLOB_TICKET_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FORCE_COMPLETE_WRITE_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    EXPECT_NON_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    offset: int
    is_optional: bool
    durability: int
    stats_container: int
    is_magneto_request: bool
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_blob_ticket_sequencer: bool
    constituent_id: int
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    forwarding_enabled: bool
    data: bytes
    force_complete_write: bool
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    expect_non_mega_file: bool
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., offset: _Optional[int] = ..., is_optional: bool = ..., durability: _Optional[int] = ..., stats_container: _Optional[int] = ..., is_magneto_request: bool = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_blob_ticket_sequencer: bool = ..., constituent_id: _Optional[int] = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., forwarding_enabled: bool = ..., data: _Optional[bytes] = ..., force_complete_write: bool = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., expect_non_mega_file: bool = ...) -> None: ...

class WriteEntityResult(_message.Message):
    __slots__ = ("status", "durability", "count", "remote_session_id", "remote_ticket_sequencer_high", "remote_ticket_sequencer_low", "minion_blob_id", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DURABILITY_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    status: Status
    durability: int
    count: int
    remote_session_id: int
    remote_ticket_sequencer_high: int
    remote_ticket_sequencer_low: int
    minion_blob_id: int
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., durability: _Optional[int] = ..., count: _Optional[int] = ..., remote_session_id: _Optional[int] = ..., remote_ticket_sequencer_high: _Optional[int] = ..., remote_ticket_sequencer_low: _Optional[int] = ..., minion_blob_id: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class ReadFileArg(_message.Message):
    __slots__ = ("eh", "is_optional", "offset", "size", "is_forwarded", "qos_context", "forwarding_enabled", "force_complete_read", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low", "disable_dir_prefetch", "expect_non_mega_file")
    EH_FIELD_NUMBER: _ClassVar[int]
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_COMPLETE_READ_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DIR_PREFETCH_FIELD_NUMBER: _ClassVar[int]
    EXPECT_NON_MEGA_FILE_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    is_optional: bool
    offset: int
    size: int
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    forwarding_enabled: bool
    force_complete_read: bool
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    disable_dir_prefetch: bool
    expect_non_mega_file: bool
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., is_optional: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., forwarding_enabled: bool = ..., force_complete_read: bool = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ..., disable_dir_prefetch: bool = ..., expect_non_mega_file: bool = ...) -> None: ...

class ReadFileResult(_message.Message):
    __slots__ = ("status", "eof", "remote_session_id", "remote_ticket_sequencer_high", "remote_ticket_sequencer_low", "data", "minion_blob_id", "pre_pin_expected_ticket_sequencer_high", "pre_pin_expected_ticket_sequencer_low")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    PRE_PIN_EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    status: Status
    eof: bool
    remote_session_id: int
    remote_ticket_sequencer_high: int
    remote_ticket_sequencer_low: int
    data: bytes
    minion_blob_id: int
    pre_pin_expected_ticket_sequencer_high: int
    pre_pin_expected_ticket_sequencer_low: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., eof: bool = ..., remote_session_id: _Optional[int] = ..., remote_ticket_sequencer_high: _Optional[int] = ..., remote_ticket_sequencer_low: _Optional[int] = ..., data: _Optional[bytes] = ..., minion_blob_id: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_high: _Optional[int] = ..., pre_pin_expected_ticket_sequencer_low: _Optional[int] = ...) -> None: ...

class RemoveEntityArg(_message.Message):
    __slots__ = ("dir_eh", "child_name", "expected_entity_id", "is_directory", "is_forwarded", "qos_context", "request_id", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "is_privileged")
    DIR_EH_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    QOS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    dir_eh: _entity_handle_pb2.EntityHandleProto
    child_name: str
    expected_entity_id: int
    is_directory: bool
    is_forwarded: bool
    qos_context: _cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext
    request_id: int
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    is_privileged: bool
    def __init__(self, dir_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., child_name: _Optional[str] = ..., expected_entity_id: _Optional[int] = ..., is_directory: bool = ..., is_forwarded: bool = ..., qos_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping.QoSContext, _Mapping]] = ..., request_id: _Optional[int] = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., is_privileged: bool = ...) -> None: ...

class RemoveEntityResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class CreateHyxConnectorArg(_message.Message):
    __slots__ = ("connector_config", "tenant_id")
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    tenant_id: str
    def __init__(self, connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class CreateHyxConnectorResult(_message.Message):
    __slots__ = ("status", "connector_config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ...) -> None: ...

class UpdateHyxConnectorArg(_message.Message):
    __slots__ = ("connector_config", "tenant_id")
    CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    connector_config: _bifrost_base_pb2.HyxConnectorConfigProto
    tenant_id: str
    def __init__(self, connector_config: _Optional[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class UpdateHyxConnectorResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class GetHyxConnectorsArg(_message.Message):
    __slots__ = ("hyx_connector_id_vec", "realm_id", "tenant_id")
    HYX_CONNECTOR_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    hyx_connector_id_vec: _containers.RepeatedScalarFieldContainer[int]
    realm_id: int
    tenant_id: str
    def __init__(self, hyx_connector_id_vec: _Optional[_Iterable[int]] = ..., realm_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetHyxConnectorsResult(_message.Message):
    __slots__ = ("status", "connector_config_vec")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    connector_config_vec: _containers.RepeatedCompositeFieldContainer[_bifrost_base_pb2.HyxConnectorConfigProto]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., connector_config_vec: _Optional[_Iterable[_Union[_bifrost_base_pb2.HyxConnectorConfigProto, _Mapping]]] = ...) -> None: ...

class DeleteHyxConnectorArg(_message.Message):
    __slots__ = ("hyx_connector_id", "tenant_id")
    HYX_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    hyx_connector_id: int
    tenant_id: str
    def __init__(self, hyx_connector_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class DeleteHyxConnectorResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class CreateNetworkRealmArg(_message.Message):
    __slots__ = ("network_realm",)
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class CreateNetworkRealmResult(_message.Message):
    __slots__ = ("status", "realm_id", "network_realm")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    status: Status
    realm_id: int
    network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., realm_id: _Optional[int] = ..., network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class UpdateNetworkRealmArg(_message.Message):
    __slots__ = ("network_realm",)
    NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class UpdateNetworkRealmResult(_message.Message):
    __slots__ = ("status", "updated_network_realm")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_NETWORK_REALM_FIELD_NUMBER: _ClassVar[int]
    status: Status
    updated_network_realm: _bifrost_base_pb2.NetworkRealm
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., updated_network_realm: _Optional[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]] = ...) -> None: ...

class GetNetworkRealmsArg(_message.Message):
    __slots__ = ("realm_id_vec",)
    REALM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    realm_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, realm_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetNetworkRealmsResult(_message.Message):
    __slots__ = ("status", "network_realm_vec")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_VEC_FIELD_NUMBER: _ClassVar[int]
    status: Status
    network_realm_vec: _containers.RepeatedCompositeFieldContainer[_bifrost_base_pb2.NetworkRealm]
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., network_realm_vec: _Optional[_Iterable[_Union[_bifrost_base_pb2.NetworkRealm, _Mapping]]] = ...) -> None: ...

class DeleteNetworkRealmArg(_message.Message):
    __slots__ = ("realm_id",)
    REALM_ID_FIELD_NUMBER: _ClassVar[int]
    realm_id: int
    def __init__(self, realm_id: _Optional[int] = ...) -> None: ...

class DeleteNetworkRealmResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class KerberosProviderEntryArg(_message.Message):
    __slots__ = ("kerberos_realm_name", "admin_server", "kdc_server_vec", "admin_principal", "password", "host_alias_vec", "ldap_id", "overwrite_host_alias")
    KERBEROS_REALM_NAME_FIELD_NUMBER: _ClassVar[int]
    ADMIN_SERVER_FIELD_NUMBER: _ClassVar[int]
    KDC_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HOST_ALIAS_VEC_FIELD_NUMBER: _ClassVar[int]
    LDAP_ID_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_HOST_ALIAS_FIELD_NUMBER: _ClassVar[int]
    kerberos_realm_name: str
    admin_server: str
    kdc_server_vec: _containers.RepeatedScalarFieldContainer[str]
    admin_principal: str
    password: str
    host_alias_vec: _containers.RepeatedScalarFieldContainer[str]
    ldap_id: int
    overwrite_host_alias: bool
    def __init__(self, kerberos_realm_name: _Optional[str] = ..., admin_server: _Optional[str] = ..., kdc_server_vec: _Optional[_Iterable[str]] = ..., admin_principal: _Optional[str] = ..., password: _Optional[str] = ..., host_alias_vec: _Optional[_Iterable[str]] = ..., ldap_id: _Optional[int] = ..., overwrite_host_alias: bool = ...) -> None: ...

class KerberosProviderEntryResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Status
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ...) -> None: ...

class UDAConnectorConfigResult(_message.Message):
    __slots__ = ("status", "config")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: Status
    config: _uda_configs_pb2.UDAConnectorConfiguration
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., config: _Optional[_Union[_uda_configs_pb2.UDAConnectorConfiguration, _Mapping]] = ...) -> None: ...

class DeleteUDAConnectorConfigArgs(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class S3AbacServerEntryArg(_message.Message):
    __slots__ = ("hostname", "port", "certificate", "key", "ca_certificate_store", "base_path", "is_update_req", "tenant_id", "id")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_STORE_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_UPDATE_REQ_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    port: int
    certificate: str
    key: str
    ca_certificate_store: str
    base_path: str
    is_update_req: bool
    tenant_id: str
    id: int
    def __init__(self, hostname: _Optional[str] = ..., port: _Optional[int] = ..., certificate: _Optional[str] = ..., key: _Optional[str] = ..., ca_certificate_store: _Optional[str] = ..., base_path: _Optional[str] = ..., is_update_req: bool = ..., tenant_id: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class DeleteS3AbacServerArgs(_message.Message):
    __slots__ = ("tenant_id", "hostname", "id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    hostname: str
    id: int
    def __init__(self, tenant_id: _Optional[str] = ..., hostname: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class S3AbacServerResult(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: Status
    id: int
    def __init__(self, status: _Optional[_Union[Status, _Mapping]] = ..., id: _Optional[int] = ...) -> None: ...
