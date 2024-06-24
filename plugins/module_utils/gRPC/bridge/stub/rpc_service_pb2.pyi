from apollo.mr.base import api_version_pb2 as _api_version_pb2
from bridge.apollo import actions_v2_pb2 as _actions_v2_pb2
from bridge.apollo import apollo_actions_pb2 as _apollo_actions_pb2
from bridge.base import error_pb2 as _error_pb2
from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.icebox.base import icebox_pb2 as _icebox_pb2
from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from bridge.quota import quota_tree_metadata_pb2 as _quota_tree_metadata_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.smb_portal import smb_portal_metadata_pb2 as _smb_portal_metadata_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.stats import bridge_stats_config_pb2 as _bridge_stats_config_pb2
from bridge.stub import rpc_common_args_pb2 as _rpc_common_args_pb2
from bridge.view_keeper import list_smb_active_opens_pb2 as _list_smb_active_opens_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from bridge.view_keeper import view_usage_pb2 as _view_usage_pb2
from bridge.virus_scanner import antivirus_scan_metadata_pb2 as _antivirus_scan_metadata_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from configs import service_auth_config_pb2 as _service_auth_config_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateViewArg(_message.Message):
    __slots__ = ("view_name", "view_box_id", "is_internal", "description", "storage_policy_override", "qos_mappings", "qos_principals", "disable_nfs_access", "client_subnet_whitelist", "enable_smb_access_based_dir_enumeration", "case_insensitive_entity_names", "view_quota_policy", "protocol_access_info", "iris_metadata", "s3_bucket_config", "client_subnet_whitelist_extends_global_whitelist", "mtime_ctime_explicitly_set_only", "enable_minion", "enable_audit_logging", "inherit_audit_log_from_view", "smb_config", "replication_smb_config", "node_id_floor", "view_snap_tree_mapped_keys", "mapped_key_byte_swapped_with_last_byte", "mapped_key_swap_bit_mask", "root_info_vec", "file_extension_filter", "is_immutable", "enable_user_quota", "default_user_quota_policy", "fld_config", "saved_fld_config", "tenant_id", "nfs_config", "replication_nfs_config", "security_mode_config", "user_view_tree_id_ceiling", "antivirus_scan_config", "apollo_disable_namespace_fixing", "create_view_for_stubbing", "external_metadata", "latency_alert_params", "s3_objects_with_conflicting_path_supported", "s3_key_mapping_config", "view_all_squash_uid", "view_all_squash_gid", "view_root_squash_uid", "view_root_squash_gid", "num_inode_atime_records", "trash_config", "uptier_config", "apollo_disable_orphaned_inodes_deletion", "client_netgroup_whitelist", "client_netgroup_whitelist_extends_global_whitelist", "enable_live_indexing", "pin_config", "add_inode_id_floor", "language_locale", "category", "snapshot_self_service_config", "restrict_access_to_internal", "archival_info", "enable_blur", "service_auth_config", "enable_brick_level_checksum", "performance_config", "s3_folder_support_enabled", "stats_container_id", "worm_lock_expiry_usecs", "saved_immutable", "is_magneto_v2_view", "workload_attrs", "saved_client_subnet_whitelist", "s3object_snap_tree_id", "workload_type", "enable_small_dedup_chunk_creates", "lcm_rules")
    class QosPrincipalsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ...) -> None: ...
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    VIEW_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    IRIS_METADATA_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    MTIME_CTIME_EXPLICITLY_SET_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    INHERIT_AUDIT_LOG_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_MAPPED_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_BYTE_SWAPPED_WITH_LAST_BYTE_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_SWAP_BIT_MASK_FIELD_NUMBER: _ClassVar[int]
    ROOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_USER_QUOTA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_USER_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SAVED_FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USER_VIEW_TREE_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    APOLLO_DISABLE_NAMESPACE_FIXING_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FOR_STUBBING_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    LATENCY_ALERT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_OBJECTS_WITH_CONFLICTING_PATH_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_KEY_MAPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    NUM_INODE_ATIME_RECORDS_FIELD_NUMBER: _ClassVar[int]
    TRASH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPTIER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    APOLLO_DISABLE_ORPHANED_INODES_DELETION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LIVE_INDEXING_FIELD_NUMBER: _ClassVar[int]
    PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADD_INODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SELF_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_ACCESS_TO_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BLUR_FIELD_NUMBER: _ClassVar[int]
    SERVICE_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    S3_FOLDER_SUPPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    SAVED_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNETO_V2_VIEW_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ATTRS_FIELD_NUMBER: _ClassVar[int]
    SAVED_CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    S3OBJECT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMALL_DEDUP_CHUNK_CREATES_FIELD_NUMBER: _ClassVar[int]
    LCM_RULES_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    view_box_id: int
    is_internal: bool
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos_mappings: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.QoSMapping]
    qos_principals: _containers.MessageMap[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]
    disable_nfs_access: bool
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_smb_access_based_dir_enumeration: bool
    case_insensitive_entity_names: bool
    view_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    iris_metadata: _view_metadata_pb2.ViewIdMappingProto.IrisMetadata
    s3_bucket_config: _s3_metadata_pb2.S3BucketConfigProto
    client_subnet_whitelist_extends_global_whitelist: bool
    mtime_ctime_explicitly_set_only: bool
    enable_minion: bool
    enable_audit_logging: bool
    inherit_audit_log_from_view: bool
    smb_config: _view_metadata_pb2.ViewIdMappingProto.SmbConfigProto
    replication_smb_config: _view_metadata_pb2.ViewIdMappingProto.SmbConfigProto
    node_id_floor: int
    view_snap_tree_mapped_keys: bool
    mapped_key_byte_swapped_with_last_byte: int
    mapped_key_swap_bit_mask: int
    root_info_vec: _containers.RepeatedCompositeFieldContainer[_view_metadata_pb2.ViewIdMappingProto.RootInfo]
    file_extension_filter: _view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter
    is_immutable: bool
    enable_user_quota: bool
    default_user_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    saved_fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    tenant_id: str
    nfs_config: _view_metadata_pb2.ViewIdMappingProto.NfsConfigProto
    replication_nfs_config: _view_metadata_pb2.ViewIdMappingProto.NfsConfigProto
    security_mode_config: _view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig
    user_view_tree_id_ceiling: int
    antivirus_scan_config: _view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig
    apollo_disable_namespace_fixing: bool
    create_view_for_stubbing: bool
    external_metadata: _view_metadata_pb2.ViewIdMappingProto.ExternalMetadata
    latency_alert_params: _view_metadata_pb2.ViewIdMappingProto.LatencyAlertParams
    s3_objects_with_conflicting_path_supported: bool
    s3_key_mapping_config: _s3_metadata_pb2.S3KeyMappingConfigProto
    view_all_squash_uid: int
    view_all_squash_gid: int
    view_root_squash_uid: int
    view_root_squash_gid: int
    num_inode_atime_records: int
    trash_config: _view_metadata_pb2.ViewIdMappingProto.TrashConfig
    uptier_config: _view_metadata_pb2.ViewIdMappingProto.UptierConfig
    apollo_disable_orphaned_inodes_deletion: bool
    client_netgroup_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
    client_netgroup_whitelist_extends_global_whitelist: bool
    enable_live_indexing: bool
    pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
    add_inode_id_floor: bool
    language_locale: str
    category: _view_metadata_pb2.ViewIdMappingProto.ViewCategory
    snapshot_self_service_config: _view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig
    restrict_access_to_internal: bool
    archival_info: _view_metadata_pb2.ViewIdMappingProto.ArchivalInfo
    enable_blur: bool
    service_auth_config: _service_auth_config_pb2.ServiceAuthConfigProto
    enable_brick_level_checksum: bool
    performance_config: _view_metadata_pb2.ViewIdMappingProto.PerformanceConfig
    s3_folder_support_enabled: bool
    stats_container_id: int
    worm_lock_expiry_usecs: int
    saved_immutable: bool
    is_magneto_v2_view: bool
    workload_attrs: _view_metadata_pb2.ViewIdMappingProto.WorkloadAttributes
    saved_client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    s3object_snap_tree_id: int
    workload_type: _request_context_pb2.WorkloadType
    enable_small_dedup_chunk_creates: bool
    lcm_rules: _view_metadata_pb2.LifecyclePolicy.LifecycleRules
    def __init__(self, view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., is_internal: bool = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos_mappings: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping, _Mapping]]] = ..., qos_principals: _Optional[_Mapping[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]] = ..., disable_nfs_access: bool = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., case_insensitive_entity_names: bool = ..., view_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., iris_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.IrisMetadata, _Mapping]] = ..., s3_bucket_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., client_subnet_whitelist_extends_global_whitelist: bool = ..., mtime_ctime_explicitly_set_only: bool = ..., enable_minion: bool = ..., enable_audit_logging: bool = ..., inherit_audit_log_from_view: bool = ..., smb_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., replication_smb_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., node_id_floor: _Optional[int] = ..., view_snap_tree_mapped_keys: bool = ..., mapped_key_byte_swapped_with_last_byte: _Optional[int] = ..., mapped_key_swap_bit_mask: _Optional[int] = ..., root_info_vec: _Optional[_Iterable[_Union[_view_metadata_pb2.ViewIdMappingProto.RootInfo, _Mapping]]] = ..., file_extension_filter: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., is_immutable: bool = ..., enable_user_quota: bool = ..., default_user_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., saved_fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., tenant_id: _Optional[str] = ..., nfs_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., replication_nfs_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., security_mode_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig, _Mapping]] = ..., user_view_tree_id_ceiling: _Optional[int] = ..., antivirus_scan_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig, _Mapping]] = ..., apollo_disable_namespace_fixing: bool = ..., create_view_for_stubbing: bool = ..., external_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ExternalMetadata, _Mapping]] = ..., latency_alert_params: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.LatencyAlertParams, _Mapping]] = ..., s3_objects_with_conflicting_path_supported: bool = ..., s3_key_mapping_config: _Optional[_Union[_s3_metadata_pb2.S3KeyMappingConfigProto, _Mapping]] = ..., view_all_squash_uid: _Optional[int] = ..., view_all_squash_gid: _Optional[int] = ..., view_root_squash_uid: _Optional[int] = ..., view_root_squash_gid: _Optional[int] = ..., num_inode_atime_records: _Optional[int] = ..., trash_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.TrashConfig, _Mapping]] = ..., uptier_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.UptierConfig, _Mapping]] = ..., apollo_disable_orphaned_inodes_deletion: bool = ..., client_netgroup_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., client_netgroup_whitelist_extends_global_whitelist: bool = ..., enable_live_indexing: bool = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ..., add_inode_id_floor: bool = ..., language_locale: _Optional[str] = ..., category: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ViewCategory, str]] = ..., snapshot_self_service_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig, _Mapping]] = ..., restrict_access_to_internal: bool = ..., archival_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ArchivalInfo, _Mapping]] = ..., enable_blur: bool = ..., service_auth_config: _Optional[_Union[_service_auth_config_pb2.ServiceAuthConfigProto, _Mapping]] = ..., enable_brick_level_checksum: bool = ..., performance_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PerformanceConfig, _Mapping]] = ..., s3_folder_support_enabled: bool = ..., stats_container_id: _Optional[int] = ..., worm_lock_expiry_usecs: _Optional[int] = ..., saved_immutable: bool = ..., is_magneto_v2_view: bool = ..., workload_attrs: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.WorkloadAttributes, _Mapping]] = ..., saved_client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., s3object_snap_tree_id: _Optional[int] = ..., workload_type: _Optional[_Union[_request_context_pb2.WorkloadType, str]] = ..., enable_small_dedup_chunk_creates: bool = ..., lcm_rules: _Optional[_Union[_view_metadata_pb2.LifecyclePolicy.LifecycleRules, _Mapping]] = ...) -> None: ...

class CreateViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteViewArg(_message.Message):
    __slots__ = ("view_name", "view_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    view_id: int
    def __init__(self, view_name: _Optional[str] = ..., view_id: _Optional[int] = ...) -> None: ...

class DeleteViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloneViewArg(_message.Message):
    __slots__ = ("src_view_name", "target_view_name", "is_internal", "description", "storage_policy_override", "qos_mappings", "qos_principals", "target_view_immutable", "disable_nfs_access", "protocol_access_info", "s3_bucket_config", "client_subnet_whitelist", "add_inode_id_floor_target_view", "add_inode_id_floor_src_view", "worm_lock_expiry_usecs", "enable_audit_logging", "inherit_audit_log_from_view", "mtime_ctime_explicitly_set_only", "apollo_disable_namespace_fixing", "change_user_view_tree_id_ceiling", "make_two_clones_of_snap_tree", "apollo_disable_orphaned_inodes_deletion", "is_read_only", "external_metadata", "archival_info", "service_auth_config", "clone_service_auth_config", "restrict_access_to_internal", "enable_brick_level_checksum", "owner_sid", "pin_config", "enable_obj_store_access", "stats_container_id", "clone_stats_container_id", "workload_attrs", "workload_type", "enable_small_dedup_chunk_creates")
    class QosPrincipalsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ...) -> None: ...
    SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ADD_INODE_ID_FLOOR_TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
    ADD_INODE_ID_FLOOR_SRC_VIEW_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    INHERIT_AUDIT_LOG_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
    MTIME_CTIME_EXPLICITLY_SET_ONLY_FIELD_NUMBER: _ClassVar[int]
    APOLLO_DISABLE_NAMESPACE_FIXING_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_VIEW_TREE_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    MAKE_TWO_CLONES_OF_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    APOLLO_DISABLE_ORPHANED_INODES_DELETION_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLONE_SERVICE_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_ACCESS_TO_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    OWNER_SID_FIELD_NUMBER: _ClassVar[int]
    PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OBJ_STORE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CLONE_STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ATTRS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMALL_DEDUP_CHUNK_CREATES_FIELD_NUMBER: _ClassVar[int]
    src_view_name: str
    target_view_name: str
    is_internal: bool
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos_mappings: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.QoSMapping]
    qos_principals: _containers.MessageMap[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]
    target_view_immutable: bool
    disable_nfs_access: bool
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    s3_bucket_config: _s3_metadata_pb2.S3BucketConfigProto
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    add_inode_id_floor_target_view: bool
    add_inode_id_floor_src_view: bool
    worm_lock_expiry_usecs: int
    enable_audit_logging: bool
    inherit_audit_log_from_view: bool
    mtime_ctime_explicitly_set_only: bool
    apollo_disable_namespace_fixing: bool
    change_user_view_tree_id_ceiling: bool
    make_two_clones_of_snap_tree: bool
    apollo_disable_orphaned_inodes_deletion: bool
    is_read_only: bool
    external_metadata: _view_metadata_pb2.ViewIdMappingProto.ExternalMetadata
    archival_info: _view_metadata_pb2.ViewIdMappingProto.ArchivalInfo
    service_auth_config: _service_auth_config_pb2.ServiceAuthConfigProto
    clone_service_auth_config: bool
    restrict_access_to_internal: bool
    enable_brick_level_checksum: bool
    owner_sid: _cluster_config_pb2.ClusterConfigProto.SID
    pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
    enable_obj_store_access: bool
    stats_container_id: int
    clone_stats_container_id: bool
    workload_attrs: _view_metadata_pb2.ViewIdMappingProto.WorkloadAttributes
    workload_type: _request_context_pb2.WorkloadType
    enable_small_dedup_chunk_creates: bool
    def __init__(self, src_view_name: _Optional[str] = ..., target_view_name: _Optional[str] = ..., is_internal: bool = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos_mappings: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping, _Mapping]]] = ..., qos_principals: _Optional[_Mapping[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]] = ..., target_view_immutable: bool = ..., disable_nfs_access: bool = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., s3_bucket_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., add_inode_id_floor_target_view: bool = ..., add_inode_id_floor_src_view: bool = ..., worm_lock_expiry_usecs: _Optional[int] = ..., enable_audit_logging: bool = ..., inherit_audit_log_from_view: bool = ..., mtime_ctime_explicitly_set_only: bool = ..., apollo_disable_namespace_fixing: bool = ..., change_user_view_tree_id_ceiling: bool = ..., make_two_clones_of_snap_tree: bool = ..., apollo_disable_orphaned_inodes_deletion: bool = ..., is_read_only: bool = ..., external_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ExternalMetadata, _Mapping]] = ..., archival_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ArchivalInfo, _Mapping]] = ..., service_auth_config: _Optional[_Union[_service_auth_config_pb2.ServiceAuthConfigProto, _Mapping]] = ..., clone_service_auth_config: bool = ..., restrict_access_to_internal: bool = ..., enable_brick_level_checksum: bool = ..., owner_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ..., enable_obj_store_access: bool = ..., stats_container_id: _Optional[int] = ..., clone_stats_container_id: bool = ..., workload_attrs: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.WorkloadAttributes, _Mapping]] = ..., workload_type: _Optional[_Union[_request_context_pb2.WorkloadType, str]] = ..., enable_small_dedup_chunk_creates: bool = ...) -> None: ...

class CloneViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloneDirArg(_message.Message):
    __slots__ = ("src_dir_path", "target_parent_dir_path", "target_dir_name", "mode", "uid", "gid", "is_recursive", "is_non_atomic_clone")
    SRC_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARENT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    IS_RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    IS_NON_ATOMIC_CLONE_FIELD_NUMBER: _ClassVar[int]
    src_dir_path: str
    target_parent_dir_path: str
    target_dir_name: str
    mode: int
    uid: int
    gid: int
    is_recursive: bool
    is_non_atomic_clone: bool
    def __init__(self, src_dir_path: _Optional[str] = ..., target_parent_dir_path: _Optional[str] = ..., target_dir_name: _Optional[str] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., is_recursive: bool = ..., is_non_atomic_clone: bool = ...) -> None: ...

class CloneDirResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloneBytesArg(_message.Message):
    __slots__ = ("src_file_path", "src_offset", "dst_file_path", "dst_offset", "count")
    SRC_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SRC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DST_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    src_file_path: str
    src_offset: int
    dst_file_path: str
    dst_offset: int
    count: int
    def __init__(self, src_file_path: _Optional[str] = ..., src_offset: _Optional[int] = ..., dst_file_path: _Optional[str] = ..., dst_offset: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class CloneBytesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModifyViewArg(_message.Message):
    __slots__ = ("view_name", "client_subnet_whitelist", "cleanup_client_subnet_whitelist", "description", "storage_policy_override", "qos_mappings", "modify_qos_mappings", "qos_principals", "modify_qos_principals", "disable_nfs_access", "enable_smb_access_based_dir_enumeration", "view_quota_policy", "inherit_view_quota_policy_from_viewbox", "protocol_access_info", "iris_metadata", "s3_bucket_config", "enable_minion", "enable_audit_logging", "inherit_audit_log_from_view", "worm_lock_expiry_usecs", "client_subnet_whitelist_extends_global_whitelist", "smb_config", "file_extension_filter", "mtime_ctime_explicitly_set_only", "fld_config", "saved_fld_config", "tenant_id", "nfs_config", "security_mode_config", "antivirus_scan_config", "stubbing_target", "external_metadata", "latency_alert_params", "bookkeeper_group_id", "view_all_squash_uid", "view_all_squash_gid", "view_root_squash_uid", "view_root_squash_gid", "num_inode_atime_records", "trash_config", "uptier_config", "set_view_immutable", "client_netgroup_whitelist", "cleanup_client_netgroup_whitelist", "client_netgroup_whitelist_extends_global_whitelist", "pin_config", "change_user_view_tree_id_ceiling", "language_locale", "category", "snapshot_self_service_config", "restrict_access_to_internal", "is_read_only", "service_auth_config", "enable_brick_level_checksum", "performance_config", "enable_blur", "stats_container_id", "workload_attrs", "workload_type", "root_name_2_inconsistent_snaptree_map", "bookkeeper_v2_group_id", "enable_apollo_namespace_fixing", "enable_small_dedup_chunk_creates", "lcm_rules")
    class QosPrincipalsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ...) -> None: ...
    class RootName2InconsistentSnaptreeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    QOS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    MODIFY_QOS_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    MODIFY_QOS_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    VIEW_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    INHERIT_VIEW_QUOTA_POLICY_FROM_VIEWBOX_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    IRIS_METADATA_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    INHERIT_AUDIT_LOG_FROM_VIEW_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    MTIME_CTIME_EXPLICITLY_SET_ONLY_FIELD_NUMBER: _ClassVar[int]
    FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SAVED_FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STUBBING_TARGET_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    LATENCY_ALERT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALL_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_UID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_SQUASH_GID_FIELD_NUMBER: _ClassVar[int]
    NUM_INODE_ATIME_RECORDS_FIELD_NUMBER: _ClassVar[int]
    TRASH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPTIER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SET_VIEW_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_CLIENT_NETGROUP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_VIEW_TREE_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SELF_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_ACCESS_TO_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BLUR_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ATTRS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAME_2_INCONSISTENT_SNAPTREE_MAP_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_APOLLO_NAMESPACE_FIXING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMALL_DEDUP_CHUNK_CREATES_FIELD_NUMBER: _ClassVar[int]
    LCM_RULES_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    cleanup_client_subnet_whitelist: bool
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    qos_mappings: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.QoSMapping]
    modify_qos_mappings: bool
    qos_principals: _containers.MessageMap[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]
    modify_qos_principals: bool
    disable_nfs_access: bool
    enable_smb_access_based_dir_enumeration: bool
    view_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    inherit_view_quota_policy_from_viewbox: bool
    protocol_access_info: _view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo
    iris_metadata: _view_metadata_pb2.ViewIdMappingProto.IrisMetadata
    s3_bucket_config: _s3_metadata_pb2.S3BucketConfigProto
    enable_minion: bool
    enable_audit_logging: bool
    inherit_audit_log_from_view: bool
    worm_lock_expiry_usecs: int
    client_subnet_whitelist_extends_global_whitelist: bool
    smb_config: _view_metadata_pb2.ViewIdMappingProto.SmbConfigProto
    file_extension_filter: _view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter
    mtime_ctime_explicitly_set_only: bool
    fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    saved_fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    tenant_id: str
    nfs_config: _view_metadata_pb2.ViewIdMappingProto.NfsConfigProto
    security_mode_config: _view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig
    antivirus_scan_config: _view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig
    stubbing_target: bool
    external_metadata: _view_metadata_pb2.ViewIdMappingProto.ExternalMetadata
    latency_alert_params: _view_metadata_pb2.ViewIdMappingProto.LatencyAlertParams
    bookkeeper_group_id: int
    view_all_squash_uid: int
    view_all_squash_gid: int
    view_root_squash_uid: int
    view_root_squash_gid: int
    num_inode_atime_records: int
    trash_config: _view_metadata_pb2.ViewIdMappingProto.TrashConfig
    uptier_config: _view_metadata_pb2.ViewIdMappingProto.UptierConfig
    set_view_immutable: bool
    client_netgroup_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
    cleanup_client_netgroup_whitelist: bool
    client_netgroup_whitelist_extends_global_whitelist: bool
    pin_config: _view_metadata_pb2.ViewIdMappingProto.PinConfig
    change_user_view_tree_id_ceiling: bool
    language_locale: str
    category: _view_metadata_pb2.ViewIdMappingProto.ViewCategory
    snapshot_self_service_config: _view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig
    restrict_access_to_internal: bool
    is_read_only: bool
    service_auth_config: _service_auth_config_pb2.ServiceAuthConfigProto
    enable_brick_level_checksum: bool
    performance_config: _view_metadata_pb2.ViewIdMappingProto.PerformanceConfig
    enable_blur: bool
    stats_container_id: int
    workload_attrs: _view_metadata_pb2.ViewIdMappingProto.WorkloadAttributes
    workload_type: _request_context_pb2.WorkloadType
    root_name_2_inconsistent_snaptree_map: _containers.ScalarMap[str, bool]
    bookkeeper_v2_group_id: str
    enable_apollo_namespace_fixing: bool
    enable_small_dedup_chunk_creates: bool
    lcm_rules: _view_metadata_pb2.LifecyclePolicy.LifecycleRules
    def __init__(self, view_name: _Optional[str] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., cleanup_client_subnet_whitelist: bool = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., qos_mappings: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping, _Mapping]]] = ..., modify_qos_mappings: bool = ..., qos_principals: _Optional[_Mapping[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]] = ..., modify_qos_principals: bool = ..., disable_nfs_access: bool = ..., enable_smb_access_based_dir_enumeration: bool = ..., view_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., inherit_view_quota_policy_from_viewbox: bool = ..., protocol_access_info: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., iris_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.IrisMetadata, _Mapping]] = ..., s3_bucket_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., enable_minion: bool = ..., enable_audit_logging: bool = ..., inherit_audit_log_from_view: bool = ..., worm_lock_expiry_usecs: _Optional[int] = ..., client_subnet_whitelist_extends_global_whitelist: bool = ..., smb_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., file_extension_filter: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., mtime_ctime_explicitly_set_only: bool = ..., fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., saved_fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., tenant_id: _Optional[str] = ..., nfs_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., security_mode_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SecurityModeConfig, _Mapping]] = ..., antivirus_scan_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.AntivirusScanConfig, _Mapping]] = ..., stubbing_target: bool = ..., external_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ExternalMetadata, _Mapping]] = ..., latency_alert_params: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.LatencyAlertParams, _Mapping]] = ..., bookkeeper_group_id: _Optional[int] = ..., view_all_squash_uid: _Optional[int] = ..., view_all_squash_gid: _Optional[int] = ..., view_root_squash_uid: _Optional[int] = ..., view_root_squash_gid: _Optional[int] = ..., num_inode_atime_records: _Optional[int] = ..., trash_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.TrashConfig, _Mapping]] = ..., uptier_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.UptierConfig, _Mapping]] = ..., set_view_immutable: bool = ..., client_netgroup_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., cleanup_client_netgroup_whitelist: bool = ..., client_netgroup_whitelist_extends_global_whitelist: bool = ..., pin_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PinConfig, _Mapping]] = ..., change_user_view_tree_id_ceiling: bool = ..., language_locale: _Optional[str] = ..., category: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.ViewCategory, str]] = ..., snapshot_self_service_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SnapshotSelfServiceConfig, _Mapping]] = ..., restrict_access_to_internal: bool = ..., is_read_only: bool = ..., service_auth_config: _Optional[_Union[_service_auth_config_pb2.ServiceAuthConfigProto, _Mapping]] = ..., enable_brick_level_checksum: bool = ..., performance_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.PerformanceConfig, _Mapping]] = ..., enable_blur: bool = ..., stats_container_id: _Optional[int] = ..., workload_attrs: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.WorkloadAttributes, _Mapping]] = ..., workload_type: _Optional[_Union[_request_context_pb2.WorkloadType, str]] = ..., root_name_2_inconsistent_snaptree_map: _Optional[_Mapping[str, bool]] = ..., bookkeeper_v2_group_id: _Optional[str] = ..., enable_apollo_namespace_fixing: bool = ..., enable_small_dedup_chunk_creates: bool = ..., lcm_rules: _Optional[_Union[_view_metadata_pb2.LifecyclePolicy.LifecycleRules, _Mapping]] = ...) -> None: ...

class ModifyViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddPrefixArg(_message.Message):
    __slots__ = ("view_name", "prefix_map")
    class PrefixMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_MAP_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    prefix_map: _containers.ScalarMap[str, str]
    def __init__(self, view_name: _Optional[str] = ..., prefix_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AddPrefixResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePrefixArg(_message.Message):
    __slots__ = ("view_name", "prefix_map")
    class PrefixMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_MAP_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    prefix_map: _containers.ScalarMap[str, str]
    def __init__(self, view_name: _Optional[str] = ..., prefix_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeletePrefixResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RenameViewArg(_message.Message):
    __slots__ = ("existing_view_name", "new_view_name")
    EXISTING_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    existing_view_name: str
    new_view_name: str
    def __init__(self, existing_view_name: _Optional[str] = ..., new_view_name: _Optional[str] = ...) -> None: ...

class RenameViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddViewAliasArg(_message.Message):
    __slots__ = ("alias_name", "view_name", "view_path", "smb_config", "client_subnet_whitelist", "enable_smb_access_based_dir_enumeration", "enable_audit_logging", "overwrite_view_audit_logging")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_VIEW_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    view_name: str
    view_path: str
    smb_config: _view_metadata_pb2.ViewIdMappingProto.SmbConfigProto
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_smb_access_based_dir_enumeration: bool
    enable_audit_logging: bool
    overwrite_view_audit_logging: bool
    def __init__(self, alias_name: _Optional[str] = ..., view_name: _Optional[str] = ..., view_path: _Optional[str] = ..., smb_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., enable_audit_logging: bool = ..., overwrite_view_audit_logging: bool = ...) -> None: ...

class AddViewAliasResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModifyViewAliasArg(_message.Message):
    __slots__ = ("alias_name", "smb_config", "client_subnet_whitelist", "enable_smb_access_based_dir_enumeration", "enable_audit_logging", "overwrite_view_audit_logging")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_VIEW_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    smb_config: _view_metadata_pb2.ViewIdMappingProto.SmbConfigProto
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    enable_smb_access_based_dir_enumeration: bool
    enable_audit_logging: bool
    overwrite_view_audit_logging: bool
    def __init__(self, alias_name: _Optional[str] = ..., smb_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., enable_audit_logging: bool = ..., overwrite_view_audit_logging: bool = ...) -> None: ...

class ModifyViewAliasResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveViewAliasArg(_message.Message):
    __slots__ = ("alias_name",)
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    def __init__(self, alias_name: _Optional[str] = ...) -> None: ...

class RemoveViewAliasResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetViewInodeIdFloorArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class SetViewInodeIdFloorResult(_message.Message):
    __slots__ = ("inode_id_floor",)
    INODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    inode_id_floor: int
    def __init__(self, inode_id_floor: _Optional[int] = ...) -> None: ...

class FlushMetadataJournalArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class FlushMetadataJournalResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OverwriteViewArg(_message.Message):
    __slots__ = ("src_view_name", "target_view_name")
    SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    src_view_name: str
    target_view_name: str
    def __init__(self, src_view_name: _Optional[str] = ..., target_view_name: _Optional[str] = ...) -> None: ...

class OverwriteViewResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetViewIdMappingArg(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class GetViewIdMappingResult(_message.Message):
    __slots__ = ("mapping",)
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    mapping: _view_metadata_pb2.ViewIdMappingProto
    def __init__(self, mapping: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ...) -> None: ...

class GetViewNameMappingArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class GetViewNameMappingResult(_message.Message):
    __slots__ = ("mapping",)
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    mapping: _view_metadata_pb2.ViewNameMappingProto
    def __init__(self, mapping: _Optional[_Union[_view_metadata_pb2.ViewNameMappingProto, _Mapping]] = ...) -> None: ...

class RestoreViewAliasesArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class RestoreViewAliasesResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExecuteApolloActionArg(_message.Message):
    __slots__ = ("action", "api_version")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    action: _apollo_actions_pb2.ApolloAction
    api_version: _api_version_pb2.APIVersion
    def __init__(self, action: _Optional[_Union[_apollo_actions_pb2.ApolloAction, _Mapping]] = ..., api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ...) -> None: ...

class ExecuteApolloActionResult(_message.Message):
    __slots__ = ("ip_deprecated", "port_deprecated", "constituent_id_deprecated", "session_id", "entities_executed", "entities_rejected", "action_vec", "defrag_action_raised", "defrag_error", "action_result")
    IP_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    PORT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_REJECTED_FIELD_NUMBER: _ClassVar[int]
    ACTION_VEC_FIELD_NUMBER: _ClassVar[int]
    DEFRAG_ACTION_RAISED_FIELD_NUMBER: _ClassVar[int]
    DEFRAG_ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ip_deprecated: str
    port_deprecated: int
    constituent_id_deprecated: int
    session_id: int
    entities_executed: int
    entities_rejected: int
    action_vec: _containers.RepeatedCompositeFieldContainer[_apollo_actions_pb2.ApolloAction]
    defrag_action_raised: bool
    defrag_error: _error_pb2.ErrorProto
    action_result: _actions_v2_pb2.ActionResultProto
    def __init__(self, ip_deprecated: _Optional[str] = ..., port_deprecated: _Optional[int] = ..., constituent_id_deprecated: _Optional[int] = ..., session_id: _Optional[int] = ..., entities_executed: _Optional[int] = ..., entities_rejected: _Optional[int] = ..., action_vec: _Optional[_Iterable[_Union[_apollo_actions_pb2.ApolloAction, _Mapping]]] = ..., defrag_action_raised: bool = ..., defrag_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., action_result: _Optional[_Union[_actions_v2_pb2.ActionResultProto, _Mapping]] = ...) -> None: ...

class ExecuteApolloActionV2Arg(_message.Message):
    __slots__ = ("api_version", "action_sink_id", "action_id", "priority")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTION_SINK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    action_sink_id: str
    action_id: int
    priority: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., action_sink_id: _Optional[str] = ..., action_id: _Optional[int] = ..., priority: _Optional[int] = ...) -> None: ...

class ExecuteApolloActionV2Result(_message.Message):
    __slots__ = ("action_result",)
    ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_result: _actions_v2_pb2.ActionResultProto
    def __init__(self, action_result: _Optional[_Union[_actions_v2_pb2.ActionResultProto, _Mapping]] = ...) -> None: ...

class QueryApolloActionArg(_message.Message):
    __slots__ = ("api_version", "action_sink_id", "action_id")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTION_SINK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    api_version: _api_version_pb2.APIVersion
    action_sink_id: str
    action_id: int
    def __init__(self, api_version: _Optional[_Union[_api_version_pb2.APIVersion, _Mapping]] = ..., action_sink_id: _Optional[str] = ..., action_id: _Optional[int] = ...) -> None: ...

class QueryApolloActionResult(_message.Message):
    __slots__ = ("action_result",)
    ACTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_result: _actions_v2_pb2.ActionResultProto
    def __init__(self, action_result: _Optional[_Union[_actions_v2_pb2.ActionResultProto, _Mapping]] = ...) -> None: ...

class ListNfsConnectionsArg(_message.Message):
    __slots__ = ("view_id", "max_results", "tenant_id", "client_ip")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    view_id: _containers.RepeatedScalarFieldContainer[int]
    max_results: int
    tenant_id: str
    client_ip: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_id: _Optional[_Iterable[int]] = ..., max_results: _Optional[int] = ..., tenant_id: _Optional[str] = ..., client_ip: _Optional[_Iterable[str]] = ...) -> None: ...

class ListNfsConnectionsResult(_message.Message):
    __slots__ = ("connections",)
    class NfsConnection(_message.Message):
        __slots__ = ("client_ip", "server_ip", "view_id", "node_ip", "tenant_id", "mount_path", "uid", "gid", "uptime_usecs")
        CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        GID_FIELD_NUMBER: _ClassVar[int]
        UPTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        client_ip: str
        server_ip: str
        view_id: int
        node_ip: str
        tenant_id: str
        mount_path: str
        uid: int
        gid: int
        uptime_usecs: int
        def __init__(self, client_ip: _Optional[str] = ..., server_ip: _Optional[str] = ..., view_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., tenant_id: _Optional[str] = ..., mount_path: _Optional[str] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., uptime_usecs: _Optional[int] = ...) -> None: ...
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[ListNfsConnectionsResult.NfsConnection]
    def __init__(self, connections: _Optional[_Iterable[_Union[ListNfsConnectionsResult.NfsConnection, _Mapping]]] = ...) -> None: ...

class NodeConnectionsSummaryArg(_message.Message):
    __slots__ = ("tenant_id", "include_internal_connection")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INTERNAL_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    include_internal_connection: bool
    def __init__(self, tenant_id: _Optional[str] = ..., include_internal_connection: bool = ...) -> None: ...

class NodeConnectionsSummaryResult(_message.Message):
    __slots__ = ("node_connections_summary",)
    class NodeConnectionsSummary(_message.Message):
        __slots__ = ("node_ip", "server_ip_to_nfs_connection_count_map", "server_ip_to_smb_connection_count_map", "nfs_connection_count", "smb_connection_count")
        class ServerIpToNfsConnectionCountMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        class ServerIpToSmbConnectionCountMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_TO_NFS_CONNECTION_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_TO_SMB_CONNECTION_COUNT_MAP_FIELD_NUMBER: _ClassVar[int]
        NFS_CONNECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        SMB_CONNECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        node_ip: str
        server_ip_to_nfs_connection_count_map: _containers.ScalarMap[str, int]
        server_ip_to_smb_connection_count_map: _containers.ScalarMap[str, int]
        nfs_connection_count: int
        smb_connection_count: int
        def __init__(self, node_ip: _Optional[str] = ..., server_ip_to_nfs_connection_count_map: _Optional[_Mapping[str, int]] = ..., server_ip_to_smb_connection_count_map: _Optional[_Mapping[str, int]] = ..., nfs_connection_count: _Optional[int] = ..., smb_connection_count: _Optional[int] = ...) -> None: ...
    NODE_CONNECTIONS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    node_connections_summary: NodeConnectionsSummaryResult.NodeConnectionsSummary
    def __init__(self, node_connections_summary: _Optional[_Union[NodeConnectionsSummaryResult.NodeConnectionsSummary, _Mapping]] = ...) -> None: ...

class ClusterUsageInfo(_message.Message):
    __slots__ = ("disk_usage_info", "node_info")
    class Metric(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: _bridge_stats_config_pb2.BridgeStatsConfigProto.Metric
        value: int
        def __init__(self, id: _Optional[_Union[_bridge_stats_config_pb2.BridgeStatsConfigProto.Metric, str]] = ..., value: _Optional[int] = ...) -> None: ...
    class DiskUsageInfo(_message.Message):
        __slots__ = ("disk_id", "session_id", "sequence_id", "metric_vec")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
        METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_id: int
        session_id: int
        sequence_id: int
        metric_vec: _containers.RepeatedCompositeFieldContainer[ClusterUsageInfo.Metric]
        def __init__(self, disk_id: _Optional[int] = ..., session_id: _Optional[int] = ..., sequence_id: _Optional[int] = ..., metric_vec: _Optional[_Iterable[_Union[ClusterUsageInfo.Metric, _Mapping]]] = ...) -> None: ...
    class NodeInfo(_message.Message):
        __slots__ = ("node_id", "session_id", "sequence_id", "metric_vec")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
        METRIC_VEC_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        session_id: int
        sequence_id: int
        metric_vec: _containers.RepeatedCompositeFieldContainer[ClusterUsageInfo.Metric]
        def __init__(self, node_id: _Optional[int] = ..., session_id: _Optional[int] = ..., sequence_id: _Optional[int] = ..., metric_vec: _Optional[_Iterable[_Union[ClusterUsageInfo.Metric, _Mapping]]] = ...) -> None: ...
    DISK_USAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_FIELD_NUMBER: _ClassVar[int]
    disk_usage_info: _containers.RepeatedCompositeFieldContainer[ClusterUsageInfo.DiskUsageInfo]
    node_info: _containers.RepeatedCompositeFieldContainer[ClusterUsageInfo.NodeInfo]
    def __init__(self, disk_usage_info: _Optional[_Iterable[_Union[ClusterUsageInfo.DiskUsageInfo, _Mapping]]] = ..., node_info: _Optional[_Iterable[_Union[ClusterUsageInfo.NodeInfo, _Mapping]]] = ...) -> None: ...

class ClusterUsageStatsArg(_message.Message):
    __slots__ = ("cluster_usage_info",)
    CLUSTER_USAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    cluster_usage_info: ClusterUsageInfo
    def __init__(self, cluster_usage_info: _Optional[_Union[ClusterUsageInfo, _Mapping]] = ...) -> None: ...

class ClusterUsageStatsResult(_message.Message):
    __slots__ = ("cluster_usage_info",)
    CLUSTER_USAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    cluster_usage_info: ClusterUsageInfo
    def __init__(self, cluster_usage_info: _Optional[_Union[ClusterUsageInfo, _Mapping]] = ...) -> None: ...

class SetViewSmbSecurityInfoArg(_message.Message):
    __slots__ = ("view_name", "smb_security_info", "root_name")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SMB_SECURITY_INFO_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    smb_security_info: _view_metadata_pb2.SmbSecurityInfo
    root_name: str
    def __init__(self, view_name: _Optional[str] = ..., smb_security_info: _Optional[_Union[_view_metadata_pb2.SmbSecurityInfo, _Mapping]] = ..., root_name: _Optional[str] = ...) -> None: ...

class SetViewSmbSecurityInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetViewSmbSecurityInfoArg(_message.Message):
    __slots__ = ("view_name", "root_name")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    root_name: str
    def __init__(self, view_name: _Optional[str] = ..., root_name: _Optional[str] = ...) -> None: ...

class GetViewSmbSecurityInfoResult(_message.Message):
    __slots__ = ("smb_security_info",)
    SMB_SECURITY_INFO_FIELD_NUMBER: _ClassVar[int]
    smb_security_info: _view_metadata_pb2.SmbSecurityInfo
    def __init__(self, smb_security_info: _Optional[_Union[_view_metadata_pb2.SmbSecurityInfo, _Mapping]] = ...) -> None: ...

class ForceClearNLMLocksArg(_message.Message):
    __slots__ = ("client_id", "view_name", "file_path")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    view_name: str
    file_path: str
    def __init__(self, client_id: _Optional[str] = ..., view_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class ForceClearNLMLocksResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ForceCloseSmbOpenArg(_message.Message):
    __slots__ = ("view_name", "file_path", "open_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    open_id: int
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., open_id: _Optional[int] = ...) -> None: ...

class ForceCloseSmbOpenResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchLdapArg(_message.Message):
    __slots__ = ("domain_name", "search_base", "search_scope", "search_filter", "max_results", "attributes_vec", "tenant_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_BASE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    search_base: str
    search_scope: int
    search_filter: str
    max_results: int
    attributes_vec: _containers.RepeatedScalarFieldContainer[str]
    tenant_id: str
    def __init__(self, domain_name: _Optional[str] = ..., search_base: _Optional[str] = ..., search_scope: _Optional[int] = ..., search_filter: _Optional[str] = ..., max_results: _Optional[int] = ..., attributes_vec: _Optional[_Iterable[str]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class SearchLdapResult(_message.Message):
    __slots__ = ("result_vec",)
    class LdapResult(_message.Message):
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
            value: SearchLdapResult.LdapResult.AttrValue
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SearchLdapResult.LdapResult.AttrValue, _Mapping]] = ...) -> None: ...
        ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
        attribute_map: _containers.MessageMap[str, SearchLdapResult.LdapResult.AttrValue]
        def __init__(self, attribute_map: _Optional[_Mapping[str, SearchLdapResult.LdapResult.AttrValue]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[SearchLdapResult.LdapResult]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[SearchLdapResult.LdapResult, _Mapping]]] = ...) -> None: ...

class SearchNamesInDomainArg(_message.Message):
    __slots__ = ("search_input", "domain_name", "tenant_id")
    SEARCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    search_input: str
    domain_name: str
    tenant_id: str
    def __init__(self, search_input: _Optional[str] = ..., domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class SearchNamesInDomainResult(_message.Message):
    __slots__ = ("search_results",)
    class SearchResult(_message.Message):
        __slots__ = ("sid", "display_name", "principal_name", "account_name", "domain_name")
        SID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        display_name: str
        principal_name: str
        account_name: str
        domain_name: str
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., display_name: _Optional[str] = ..., principal_name: _Optional[str] = ..., account_name: _Optional[str] = ..., domain_name: _Optional[str] = ...) -> None: ...
    SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    search_results: _containers.RepeatedCompositeFieldContainer[SearchNamesInDomainResult.SearchResult]
    def __init__(self, search_results: _Optional[_Iterable[_Union[SearchNamesInDomainResult.SearchResult, _Mapping]]] = ...) -> None: ...

class InodeInfoArg(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class InodeInfoResult(_message.Message):
    __slots__ = ("inode_metadata",)
    INODE_METADATA_FIELD_NUMBER: _ClassVar[int]
    inode_metadata: _snap_fs_metadata_pb2.InodeMetadataProto
    def __init__(self, inode_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto, _Mapping]] = ...) -> None: ...

class GetViewUsageArg(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class GetViewUsageResult(_message.Message):
    __slots__ = ("view_usage",)
    VIEW_USAGE_FIELD_NUMBER: _ClassVar[int]
    view_usage: int
    def __init__(self, view_usage: _Optional[int] = ...) -> None: ...

class GetViewUsageDetailsArg(_message.Message):
    __slots__ = ("view_id",)
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    def __init__(self, view_id: _Optional[int] = ...) -> None: ...

class GetViewUsageDetailsResult(_message.Message):
    __slots__ = ("view_usage_details",)
    VIEW_USAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    view_usage_details: _view_usage_pb2.ViewUsageProto
    def __init__(self, view_usage_details: _Optional[_Union[_view_usage_pb2.ViewUsageProto, _Mapping]] = ...) -> None: ...

class ListUserQuotaArg(_message.Message):
    __slots__ = ("view_name", "include_usage", "user_id", "max_entries", "cookie", "list_users_to_be_alerted", "include_usage_version", "enable_user_id_conversion", "user_id_vec")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    LIST_USERS_TO_BE_ALERTED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_USER_ID_CONVERSION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    include_usage: bool
    user_id: _quota_tree_metadata_pb2.QuotaUID
    max_entries: int
    cookie: bytes
    list_users_to_be_alerted: bool
    include_usage_version: bool
    enable_user_id_conversion: bool
    user_id_vec: _containers.RepeatedCompositeFieldContainer[_quota_tree_metadata_pb2.QuotaUID]
    def __init__(self, view_name: _Optional[str] = ..., include_usage: bool = ..., user_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ..., max_entries: _Optional[int] = ..., cookie: _Optional[bytes] = ..., list_users_to_be_alerted: bool = ..., include_usage_version: bool = ..., enable_user_id_conversion: bool = ..., user_id_vec: _Optional[_Iterable[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]]] = ...) -> None: ...

class ListUserQuotaResult(_message.Message):
    __slots__ = ("is_user_quota_enabled", "default_user_quota_policy", "result_vec", "next_scan_cookie")
    class UserQuotaResult(_message.Message):
        __slots__ = ("user_unix_id", "user_sid", "user_email", "user_name", "user_quota_override", "usage_in_bytes", "usage_version")
        USER_UNIX_ID_FIELD_NUMBER: _ClassVar[int]
        USER_SID_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_QUOTA_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        USAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
        user_unix_id: int
        user_sid: _cluster_config_pb2.ClusterConfigProto.SID
        user_email: str
        user_name: str
        user_quota_override: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
        usage_in_bytes: int
        usage_version: _snap_tree_pb2.SnapTreeValueVersionProto
        def __init__(self, user_unix_id: _Optional[int] = ..., user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., user_email: _Optional[str] = ..., user_name: _Optional[str] = ..., user_quota_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., usage_in_bytes: _Optional[int] = ..., usage_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ...) -> None: ...
    IS_USER_QUOTA_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_USER_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    is_user_quota_enabled: bool
    default_user_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    result_vec: _containers.RepeatedCompositeFieldContainer[ListUserQuotaResult.UserQuotaResult]
    next_scan_cookie: bytes
    def __init__(self, is_user_quota_enabled: bool = ..., default_user_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[ListUserQuotaResult.UserQuotaResult, _Mapping]]] = ..., next_scan_cookie: _Optional[bytes] = ...) -> None: ...

class UpdateUserQuotaArg(_message.Message):
    __slots__ = ("view_name", "enable_user_quota", "inherit_default_policy_from_viewbox", "default_policy", "override_vec", "clear_existing_overrides")
    class UserQuotaOverride(_message.Message):
        __slots__ = ("user_id", "user_quota_policy_override")
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_QUOTA_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        user_id: _quota_tree_metadata_pb2.QuotaUID
        user_quota_policy_override: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
        def __init__(self, user_id: _Optional[_Union[_quota_tree_metadata_pb2.QuotaUID, _Mapping]] = ..., user_quota_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ...) -> None: ...
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_USER_QUOTA_FIELD_NUMBER: _ClassVar[int]
    INHERIT_DEFAULT_POLICY_FROM_VIEWBOX_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POLICY_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    enable_user_quota: bool
    inherit_default_policy_from_viewbox: bool
    default_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    override_vec: _containers.RepeatedCompositeFieldContainer[UpdateUserQuotaArg.UserQuotaOverride]
    clear_existing_overrides: bool
    def __init__(self, view_name: _Optional[str] = ..., enable_user_quota: bool = ..., inherit_default_policy_from_viewbox: bool = ..., default_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., override_vec: _Optional[_Iterable[_Union[UpdateUserQuotaArg.UserQuotaOverride, _Mapping]]] = ..., clear_existing_overrides: bool = ...) -> None: ...

class UpdateUserQuotaResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserQuotaSummaryForViewArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class GetUserQuotaSummaryForViewResult(_message.Message):
    __slots__ = ("total_num_users", "num_users_above_hard_limit", "num_users_above_alert_threshold", "default_quota_policy")
    TOTAL_NUM_USERS_FIELD_NUMBER: _ClassVar[int]
    NUM_USERS_ABOVE_HARD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NUM_USERS_ABOVE_ALERT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    total_num_users: int
    num_users_above_hard_limit: int
    num_users_above_alert_threshold: int
    default_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    def __init__(self, total_num_users: _Optional[int] = ..., num_users_above_hard_limit: _Optional[int] = ..., num_users_above_alert_threshold: _Optional[int] = ..., default_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ...) -> None: ...

class BackupUserQuotaDataArg(_message.Message):
    __slots__ = ("view_name", "backup_unique_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    backup_unique_id: int
    def __init__(self, view_name: _Optional[str] = ..., backup_unique_id: _Optional[int] = ...) -> None: ...

class BackupUserQuotaDataResult(_message.Message):
    __slots__ = ("backup_dir_name",)
    BACKUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    backup_dir_name: str
    def __init__(self, backup_dir_name: _Optional[str] = ...) -> None: ...

class RestoreUserQuotaDataArg(_message.Message):
    __slots__ = ("view_name", "backup_unique_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    backup_unique_id: int
    def __init__(self, view_name: _Optional[str] = ..., backup_unique_id: _Optional[int] = ...) -> None: ...

class RestoreUserQuotaDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateFileLevelDataLockArg(_message.Message):
    __slots__ = ("view_name", "file_path", "lock_expiry_usecs", "is_privileged", "mode", "legal_hold_enabled")
    class ExplicitLockingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCompliance: _ClassVar[UpdateFileLevelDataLockArg.ExplicitLockingMode]
        kEnterprise: _ClassVar[UpdateFileLevelDataLockArg.ExplicitLockingMode]
    kCompliance: UpdateFileLevelDataLockArg.ExplicitLockingMode
    kEnterprise: UpdateFileLevelDataLockArg.ExplicitLockingMode
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    file_path: str
    lock_expiry_usecs: int
    is_privileged: bool
    mode: UpdateFileLevelDataLockArg.ExplicitLockingMode
    legal_hold_enabled: bool
    def __init__(self, view_name: _Optional[str] = ..., file_path: _Optional[str] = ..., lock_expiry_usecs: _Optional[int] = ..., is_privileged: bool = ..., mode: _Optional[_Union[UpdateFileLevelDataLockArg.ExplicitLockingMode, str]] = ..., legal_hold_enabled: bool = ...) -> None: ...

class UpdateFileLevelDataLockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTrustedDomainsArg(_message.Message):
    __slots__ = ("domain_name", "tenant_id", "only_get_active")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ONLY_GET_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    tenant_id: str
    only_get_active: bool
    def __init__(self, domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., only_get_active: bool = ...) -> None: ...

class GetTrustedDomainsResult(_message.Message):
    __slots__ = ("trusted_domain_vec",)
    TRUSTED_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
    trusted_domain_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, trusted_domain_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPrimaryDomainArg(_message.Message):
    __slots__ = ("domain_name", "tenant_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    tenant_id: str
    def __init__(self, domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetPrimaryDomainResult(_message.Message):
    __slots__ = ("primary_domain",)
    PRIMARY_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    primary_domain: str
    def __init__(self, primary_domain: _Optional[str] = ...) -> None: ...

class GetAdInfoFromSidsArg(_message.Message):
    __slots__ = ("sid_vec", "tenant_id")
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    tenant_id: str
    def __init__(self, sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetAdInfoFromSidsResult(_message.Message):
    __slots__ = ("result_vec",)
    class AdInfo(_message.Message):
        __slots__ = ("sid", "display_name", "account_name", "domain_name", "object_class")
        class ObjectClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[GetAdInfoFromSidsResult.AdInfo.ObjectClass]
            kUser: _ClassVar[GetAdInfoFromSidsResult.AdInfo.ObjectClass]
            kGroup: _ClassVar[GetAdInfoFromSidsResult.AdInfo.ObjectClass]
            kComputer: _ClassVar[GetAdInfoFromSidsResult.AdInfo.ObjectClass]
        kUnknown: GetAdInfoFromSidsResult.AdInfo.ObjectClass
        kUser: GetAdInfoFromSidsResult.AdInfo.ObjectClass
        kGroup: GetAdInfoFromSidsResult.AdInfo.ObjectClass
        kComputer: GetAdInfoFromSidsResult.AdInfo.ObjectClass
        SID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        display_name: str
        account_name: str
        domain_name: str
        object_class: GetAdInfoFromSidsResult.AdInfo.ObjectClass
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., display_name: _Optional[str] = ..., account_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., object_class: _Optional[_Union[GetAdInfoFromSidsResult.AdInfo.ObjectClass, str]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[GetAdInfoFromSidsResult.AdInfo]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[GetAdInfoFromSidsResult.AdInfo, _Mapping]]] = ...) -> None: ...

class AuthenticateUserArg(_message.Message):
    __slots__ = ("domain_name", "ldap_provider_id", "user_name", "user_password", "exclude_group_membership_cache", "tenant_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_GROUP_MEMBERSHIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    ldap_provider_id: int
    user_name: str
    user_password: str
    exclude_group_membership_cache: bool
    tenant_id: str
    def __init__(self, domain_name: _Optional[str] = ..., ldap_provider_id: _Optional[int] = ..., user_name: _Optional[str] = ..., user_password: _Optional[str] = ..., exclude_group_membership_cache: bool = ..., tenant_id: _Optional[str] = ...) -> None: ...

class AuthenticateUserResult(_message.Message):
    __slots__ = ("user_sid", "group_sid_vec")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SID_VEC_FIELD_NUMBER: _ClassVar[int]
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    group_sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., group_sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class GetAdUserGroupSidsArg(_message.Message):
    __slots__ = ("user_sid", "exclude_group_membership_cache", "tenant_id")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_GROUP_MEMBERSHIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    exclude_group_membership_cache: bool
    tenant_id: str
    def __init__(self, user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., exclude_group_membership_cache: bool = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetAdUserGroupSidsResult(_message.Message):
    __slots__ = ("group_sid_vec",)
    GROUP_SID_VEC_FIELD_NUMBER: _ClassVar[int]
    group_sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, group_sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class ValidateLdapProviderConfigArg(_message.Message):
    __slots__ = ("ldap_provider_id", "tenant_id")
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ldap_provider_id: int
    tenant_id: str
    def __init__(self, ldap_provider_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class ValidateLdapProviderConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloneToLUNArg(_message.Message):
    __slots__ = ("src_file_path", "dest_view_name")
    SRC_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DEST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    src_file_path: str
    dest_view_name: str
    def __init__(self, src_file_path: _Optional[str] = ..., dest_view_name: _Optional[str] = ...) -> None: ...

class CloneToLUNResult(_message.Message):
    __slots__ = ("target_name", "lun", "error")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    lun: int
    error: _error_pb2.ErrorProto
    def __init__(self, target_name: _Optional[str] = ..., lun: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateLUNArg(_message.Message):
    __slots__ = ("target_name", "file_size_in_bytes", "subfile_size_in_mb")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    SUBFILE_SIZE_IN_MB_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    file_size_in_bytes: int
    subfile_size_in_mb: int
    def __init__(self, target_name: _Optional[str] = ..., file_size_in_bytes: _Optional[int] = ..., subfile_size_in_mb: _Optional[int] = ...) -> None: ...

class CreateLUNResult(_message.Message):
    __slots__ = ("lun", "error")
    LUN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    lun: int
    error: _error_pb2.ErrorProto
    def __init__(self, lun: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetTargetLUNsArg(_message.Message):
    __slots__ = ("target_name",)
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    def __init__(self, target_name: _Optional[str] = ...) -> None: ...

class GetTargetLUNsResult(_message.Message):
    __slots__ = ("lun_vec",)
    LUN_VEC_FIELD_NUMBER: _ClassVar[int]
    lun_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, lun_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class RemoveLUNArg(_message.Message):
    __slots__ = ("target_name", "lun")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    lun: int
    def __init__(self, target_name: _Optional[str] = ..., lun: _Optional[int] = ...) -> None: ...

class RemoveLUNResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateLUNSizeArg(_message.Message):
    __slots__ = ("target_name", "lun", "file_size_in_bytes")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    lun: int
    file_size_in_bytes: int
    def __init__(self, target_name: _Optional[str] = ..., lun: _Optional[int] = ..., file_size_in_bytes: _Optional[int] = ...) -> None: ...

class UpdateLUNSizeResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateTargetArg(_message.Message):
    __slots__ = ("storage_domain", "view_name")
    STORAGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    storage_domain: str
    view_name: str
    def __init__(self, storage_domain: _Optional[str] = ..., view_name: _Optional[str] = ...) -> None: ...

class CreateTargetResult(_message.Message):
    __slots__ = ("target_name", "error")
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    target_name: str
    error: _error_pb2.ErrorProto
    def __init__(self, target_name: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteTargetArg(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    def __init__(self, view_name: _Optional[str] = ...) -> None: ...

class DeleteTargetResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshTargetsArg(_message.Message):
    __slots__ = ("notify_peers",)
    NOTIFY_PEERS_FIELD_NUMBER: _ClassVar[int]
    notify_peers: bool
    def __init__(self, notify_peers: bool = ...) -> None: ...

class RefreshTargetsResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetBridgeCapacityArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBridgeCapacityResult(_message.Message):
    __slots__ = ("bridge_capacity_info_vec",)
    class BridgeCapacityInfo(_message.Message):
        __slots__ = ("constituent_id", "session_id", "sequence_number", "blob_store_io_capacity", "blob_store_metadata_capacity")
        class LoadCapacityInfo(_message.Message):
            __slots__ = ("queue_capacity", "queue_load")
            QUEUE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
            QUEUE_LOAD_FIELD_NUMBER: _ClassVar[int]
            queue_capacity: int
            queue_load: int
            def __init__(self, queue_capacity: _Optional[int] = ..., queue_load: _Optional[int] = ...) -> None: ...
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        BLOB_STORE_IO_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        BLOB_STORE_METADATA_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        session_id: int
        sequence_number: int
        blob_store_io_capacity: GetBridgeCapacityResult.BridgeCapacityInfo.LoadCapacityInfo
        blob_store_metadata_capacity: GetBridgeCapacityResult.BridgeCapacityInfo.LoadCapacityInfo
        def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., sequence_number: _Optional[int] = ..., blob_store_io_capacity: _Optional[_Union[GetBridgeCapacityResult.BridgeCapacityInfo.LoadCapacityInfo, _Mapping]] = ..., blob_store_metadata_capacity: _Optional[_Union[GetBridgeCapacityResult.BridgeCapacityInfo.LoadCapacityInfo, _Mapping]] = ...) -> None: ...
    BRIDGE_CAPACITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    bridge_capacity_info_vec: _containers.RepeatedCompositeFieldContainer[GetBridgeCapacityResult.BridgeCapacityInfo]
    def __init__(self, bridge_capacity_info_vec: _Optional[_Iterable[_Union[GetBridgeCapacityResult.BridgeCapacityInfo, _Mapping]]] = ...) -> None: ...

class ListInfectedFilesArg(_message.Message):
    __slots__ = ("view_id", "include_quarantined_files", "include_unquarantined_files", "max_entries", "cookie", "file_path")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_QUARANTINED_FILES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNQUARANTINED_FILES_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    include_quarantined_files: bool
    include_unquarantined_files: bool
    max_entries: int
    cookie: bytes
    file_path: str
    def __init__(self, view_id: _Optional[int] = ..., include_quarantined_files: bool = ..., include_unquarantined_files: bool = ..., max_entries: _Optional[int] = ..., cookie: _Optional[bytes] = ..., file_path: _Optional[str] = ...) -> None: ...

class ListInfectedFilesResult(_message.Message):
    __slots__ = ("result_vec", "next_scan_cookie")
    class InfectedFileResult(_message.Message):
        __slots__ = ("view_id", "view_name", "root_inode_id", "entity_id", "remediation_state", "infection_info", "scan_timestamp_usecs", "mtime_usecs", "service_icap_tag")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        REMEDIATION_STATE_FIELD_NUMBER: _ClassVar[int]
        INFECTION_INFO_FIELD_NUMBER: _ClassVar[int]
        SCAN_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ICAP_TAG_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        view_name: str
        root_inode_id: int
        entity_id: int
        remediation_state: _snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata.Remediation
        infection_info: _antivirus_scan_metadata_pb2.AntivirusSnapTreeValueProto
        scan_timestamp_usecs: int
        mtime_usecs: int
        service_icap_tag: str
        def __init__(self, view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., remediation_state: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata.Remediation, str]] = ..., infection_info: _Optional[_Union[_antivirus_scan_metadata_pb2.AntivirusSnapTreeValueProto, _Mapping]] = ..., scan_timestamp_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., service_icap_tag: _Optional[str] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[ListInfectedFilesResult.InfectedFileResult]
    next_scan_cookie: bytes
    def __init__(self, result_vec: _Optional[_Iterable[_Union[ListInfectedFilesResult.InfectedFileResult, _Mapping]]] = ..., next_scan_cookie: _Optional[bytes] = ...) -> None: ...

class ModifyInfectedFileStateArg(_message.Message):
    __slots__ = ("view_id", "root_inode_id", "entity_id", "remediation_state", "username", "domain_name", "user_sid")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_STATE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    root_inode_id: int
    entity_id: int
    remediation_state: _snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata.Remediation
    username: str
    domain_name: str
    user_sid: str
    def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., remediation_state: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata.Remediation, str]] = ..., username: _Optional[str] = ..., domain_name: _Optional[str] = ..., user_sid: _Optional[str] = ...) -> None: ...

class ModifyInfectedFileStateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteInfectedFileArg(_message.Message):
    __slots__ = ("view_id", "root_inode_id", "entity_id", "username", "domain_name", "user_sid")
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    view_id: int
    root_inode_id: int
    entity_id: int
    username: str
    domain_name: str
    user_sid: str
    def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., username: _Optional[str] = ..., domain_name: _Optional[str] = ..., user_sid: _Optional[str] = ...) -> None: ...

class DeleteInfectedFileResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckICAPServerConnectionArg(_message.Message):
    __slots__ = ("service_uri",)
    SERVICE_URI_FIELD_NUMBER: _ClassVar[int]
    service_uri: str
    def __init__(self, service_uri: _Optional[str] = ...) -> None: ...

class CheckICAPServerConnectionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DirQuotaPolicy(_message.Message):
    __slots__ = ("path", "policy", "usage_bytes", "dir_walk_pending")
    PATH_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DIR_WALK_PENDING_FIELD_NUMBER: _ClassVar[int]
    path: str
    policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    usage_bytes: int
    dir_walk_pending: bool
    def __init__(self, path: _Optional[str] = ..., policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., usage_bytes: _Optional[int] = ..., dir_walk_pending: bool = ...) -> None: ...

class DirQuotaConfig(_message.Message):
    __slots__ = ("view_name", "enabled")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    enabled: bool
    def __init__(self, view_name: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class DirQuotaConfigArg(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: DirQuotaConfig
    def __init__(self, config: _Optional[_Union[DirQuotaConfig, _Mapping]] = ...) -> None: ...

class DirQuotaConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateDirQuotaArg(_message.Message):
    __slots__ = ("view_name", "quota", "disable_dir_quota", "view_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DIR_QUOTA_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    quota: DirQuotaPolicy
    disable_dir_quota: bool
    view_id: int
    def __init__(self, view_name: _Optional[str] = ..., quota: _Optional[_Union[DirQuotaPolicy, _Mapping]] = ..., disable_dir_quota: bool = ..., view_id: _Optional[int] = ...) -> None: ...

class UpdateDirQuotaResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDirQuotaArg(_message.Message):
    __slots__ = ("view_name", "max_entries", "cookie", "list_dirs_to_be_alerted", "show_deleted_entries", "dir_path", "view_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    LIST_DIRS_TO_BE_ALERTED_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    max_entries: int
    cookie: int
    list_dirs_to_be_alerted: bool
    show_deleted_entries: bool
    dir_path: str
    view_id: int
    def __init__(self, view_name: _Optional[str] = ..., max_entries: _Optional[int] = ..., cookie: _Optional[int] = ..., list_dirs_to_be_alerted: bool = ..., show_deleted_entries: bool = ..., dir_path: _Optional[str] = ..., view_id: _Optional[int] = ...) -> None: ...

class ListDirQuotaResult(_message.Message):
    __slots__ = ("config", "quotas", "next_scan_cookie")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUOTAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    config: DirQuotaConfig
    quotas: _containers.RepeatedCompositeFieldContainer[DirQuotaPolicy]
    next_scan_cookie: int
    def __init__(self, config: _Optional[_Union[DirQuotaConfig, _Mapping]] = ..., quotas: _Optional[_Iterable[_Union[DirQuotaPolicy, _Mapping]]] = ..., next_scan_cookie: _Optional[int] = ...) -> None: ...

class BackupDirQuotaDataArg(_message.Message):
    __slots__ = ("view_name", "backup_unique_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    backup_unique_id: int
    def __init__(self, view_name: _Optional[str] = ..., backup_unique_id: _Optional[int] = ...) -> None: ...

class BackupDirQuotaDataResult(_message.Message):
    __slots__ = ("backup_dir_name",)
    BACKUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    backup_dir_name: str
    def __init__(self, backup_dir_name: _Optional[str] = ...) -> None: ...

class RestoreDirQuotaDataArg(_message.Message):
    __slots__ = ("view_name", "backup_unique_id")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    backup_unique_id: int
    def __init__(self, view_name: _Optional[str] = ..., backup_unique_id: _Optional[int] = ...) -> None: ...

class RestoreDirQuotaDataResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearAccessProviderCacheArg(_message.Message):
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

class ClearAccessProviderCacheResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateKeystoneConfigArg(_message.Message):
    __slots__ = ("auth_url", "www_authenticate_uri", "service_user", "project_scope", "domain_scope", "keystone_config_id", "name")
    class KeystoneUser(_message.Message):
        __slots__ = ("domain_name", "username", "password")
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        username: str
        password: str
        def __init__(self, domain_name: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
    class ProjectScope(_message.Message):
        __slots__ = ("domain_name", "project_name")
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        project_name: str
        def __init__(self, domain_name: _Optional[str] = ..., project_name: _Optional[str] = ...) -> None: ...
    class DomainScope(_message.Message):
        __slots__ = ("domain_name",)
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        def __init__(self, domain_name: _Optional[str] = ...) -> None: ...
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    WWW_AUTHENTICATE_URI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_USER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_SCOPE_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    auth_url: str
    www_authenticate_uri: str
    service_user: ValidateKeystoneConfigArg.KeystoneUser
    project_scope: ValidateKeystoneConfigArg.ProjectScope
    domain_scope: ValidateKeystoneConfigArg.DomainScope
    keystone_config_id: int
    name: str
    def __init__(self, auth_url: _Optional[str] = ..., www_authenticate_uri: _Optional[str] = ..., service_user: _Optional[_Union[ValidateKeystoneConfigArg.KeystoneUser, _Mapping]] = ..., project_scope: _Optional[_Union[ValidateKeystoneConfigArg.ProjectScope, _Mapping]] = ..., domain_scope: _Optional[_Union[ValidateKeystoneConfigArg.DomainScope, _Mapping]] = ..., keystone_config_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class ValidateKeystoneConfigResult(_message.Message):
    __slots__ = ("keystone_config_id",)
    KEYSTONE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    keystone_config_id: int
    def __init__(self, keystone_config_id: _Optional[int] = ...) -> None: ...

class ValidateSwiftConfigArg(_message.Message):
    __slots__ = ("tenant_id", "keystone_config_id", "operator_roles")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ROLES_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    keystone_config_id: int
    operator_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tenant_id: _Optional[str] = ..., keystone_config_id: _Optional[int] = ..., operator_roles: _Optional[_Iterable[str]] = ...) -> None: ...

class ValidateSwiftConfigResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmbActiveOpensArg(_message.Message):
    __slots__ = ("view_name", "entity_name")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: str
    entity_name: str
    def __init__(self, view_name: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...

class RegisterSwiftServiceArg(_message.Message):
    __slots__ = ("tenant_id", "keystone_user")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_USER_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    keystone_user: ValidateKeystoneConfigArg
    def __init__(self, tenant_id: _Optional[str] = ..., keystone_user: _Optional[_Union[ValidateKeystoneConfigArg, _Mapping]] = ...) -> None: ...

class RegisterSwiftServiceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnregisterSwiftServiceArg(_message.Message):
    __slots__ = ("tenant_id", "keystone_user")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    KEYSTONE_USER_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    keystone_user: ValidateKeystoneConfigArg
    def __init__(self, tenant_id: _Optional[str] = ..., keystone_user: _Optional[_Union[ValidateKeystoneConfigArg, _Mapping]] = ...) -> None: ...

class UnregisterSwiftServiceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateViewTemplateArg(_message.Message):
    __slots__ = ("view_template",)
    VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    view_template: _view_metadata_pb2.Template
    def __init__(self, view_template: _Optional[_Union[_view_metadata_pb2.Template, _Mapping]] = ...) -> None: ...

class CreateViewTemplateResult(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class DeleteViewTemplateArg(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class DeleteViewTemplateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModifyViewTemplateArg(_message.Message):
    __slots__ = ("version", "view_template")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VIEW_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    version: int
    view_template: _view_metadata_pb2.Template
    def __init__(self, version: _Optional[int] = ..., view_template: _Optional[_Union[_view_metadata_pb2.Template, _Mapping]] = ...) -> None: ...

class ModifyViewTemplateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadViewTemplateArg(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    def __init__(self, template_id: _Optional[int] = ...) -> None: ...

class ReadViewTemplateResult(_message.Message):
    __slots__ = ("version", "result_template")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESULT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    version: int
    result_template: _view_metadata_pb2.Template
    def __init__(self, version: _Optional[int] = ..., result_template: _Optional[_Union[_view_metadata_pb2.Template, _Mapping]] = ...) -> None: ...

class FetchAllViewTemplateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchAllViewTemplateResult(_message.Message):
    __slots__ = ("result_template",)
    RESULT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    result_template: _containers.RepeatedCompositeFieldContainer[_view_metadata_pb2.Template]
    def __init__(self, result_template: _Optional[_Iterable[_Union[_view_metadata_pb2.Template, _Mapping]]] = ...) -> None: ...

class MarkSnapTreeAsImmutableArg(_message.Message):
    __slots__ = ("snap_tree_id", "snap_tree_type", "is_view_snap_tree")
    SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAP_TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    snap_tree_id: int
    snap_tree_type: _icebox_pb2.IceboxSnapTreeType
    is_view_snap_tree: bool
    def __init__(self, snap_tree_id: _Optional[int] = ..., snap_tree_type: _Optional[_Union[_icebox_pb2.IceboxSnapTreeType, str]] = ..., is_view_snap_tree: bool = ...) -> None: ...

class MarkSnapTreeAsImmutableResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MarkSnapTreeAsMutableArg(_message.Message):
    __slots__ = ("snap_tree_id", "is_view_snap_tree")
    SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_SNAP_TREE_FIELD_NUMBER: _ClassVar[int]
    snap_tree_id: int
    is_view_snap_tree: bool
    def __init__(self, snap_tree_id: _Optional[int] = ..., is_view_snap_tree: bool = ...) -> None: ...

class MarkSnapTreeAsMutableResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchSessionStateForEntityAccessArg(_message.Message):
    __slots__ = ("username", "domain_name", "client_ip", "session_id")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    username: str
    domain_name: str
    client_ip: str
    session_id: int
    def __init__(self, username: _Optional[str] = ..., domain_name: _Optional[str] = ..., client_ip: _Optional[str] = ..., session_id: _Optional[int] = ...) -> None: ...

class FetchSessionStateForEntityAccessResult(_message.Message):
    __slots__ = ("token", "uid", "gid", "secondary_gid")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_GID_FIELD_NUMBER: _ClassVar[int]
    token: _smb_portal_metadata_pb2.SmbSessionMetadataProto.Token
    uid: int
    gid: int
    secondary_gid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, token: _Optional[_Union[_smb_portal_metadata_pb2.SmbSessionMetadataProto.Token, _Mapping]] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., secondary_gid: _Optional[_Iterable[int]] = ...) -> None: ...

class LookupSidsArg(_message.Message):
    __slots__ = ("domain_name", "sid_vec", "tenant_id")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    sid_vec: _containers.RepeatedScalarFieldContainer[str]
    tenant_id: str
    def __init__(self, domain_name: _Optional[str] = ..., sid_vec: _Optional[_Iterable[str]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class LookupSidsResult(_message.Message):
    __slots__ = ("user_id_vec",)
    class UserId(_message.Message):
        __slots__ = ("username", "domain")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        username: str
        domain: str
        def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...
    USER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    user_id_vec: _containers.RepeatedCompositeFieldContainer[LookupSidsResult.UserId]
    def __init__(self, user_id_vec: _Optional[_Iterable[_Union[LookupSidsResult.UserId, _Mapping]]] = ...) -> None: ...

class TriggerManualTrustDiscoveryArg(_message.Message):
    __slots__ = ("primary_domain_fqdn", "task_identifier", "tenant_id")
    PRIMARY_DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    primary_domain_fqdn: str
    task_identifier: str
    tenant_id: str
    def __init__(self, primary_domain_fqdn: _Optional[str] = ..., task_identifier: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class TriggerManualTrustDiscoveryResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsManualTrustDiscoveryRunnningArg(_message.Message):
    __slots__ = ("primary_domain_fqdn", "task_identifier", "tenant_id")
    PRIMARY_DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    primary_domain_fqdn: str
    task_identifier: str
    tenant_id: str
    def __init__(self, primary_domain_fqdn: _Optional[str] = ..., task_identifier: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class IsManualTrustDiscoveryRunnningResult(_message.Message):
    __slots__ = ("is_running",)
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    is_running: bool
    def __init__(self, is_running: bool = ...) -> None: ...

class GetAdDomainControllerStatusArg(_message.Message):
    __slots__ = ("domain_fqdn", "tenant_id")
    DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_fqdn: str
    tenant_id: str
    def __init__(self, domain_fqdn: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetAdDomainControllerStatusResult(_message.Message):
    __slots__ = ("dc_info_vec",)
    class DcInfo(_message.Message):
        __slots__ = ("dc_fqdn", "dc_status")
        class DcStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kReachable: _ClassVar[GetAdDomainControllerStatusResult.DcInfo.DcStatus]
            kIncompatible: _ClassVar[GetAdDomainControllerStatusResult.DcInfo.DcStatus]
            kFlapping: _ClassVar[GetAdDomainControllerStatusResult.DcInfo.DcStatus]
            kClockSkew: _ClassVar[GetAdDomainControllerStatusResult.DcInfo.DcStatus]
        kReachable: GetAdDomainControllerStatusResult.DcInfo.DcStatus
        kIncompatible: GetAdDomainControllerStatusResult.DcInfo.DcStatus
        kFlapping: GetAdDomainControllerStatusResult.DcInfo.DcStatus
        kClockSkew: GetAdDomainControllerStatusResult.DcInfo.DcStatus
        DC_FQDN_FIELD_NUMBER: _ClassVar[int]
        DC_STATUS_FIELD_NUMBER: _ClassVar[int]
        dc_fqdn: str
        dc_status: GetAdDomainControllerStatusResult.DcInfo.DcStatus
        def __init__(self, dc_fqdn: _Optional[str] = ..., dc_status: _Optional[_Union[GetAdDomainControllerStatusResult.DcInfo.DcStatus, str]] = ...) -> None: ...
    DC_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    dc_info_vec: _containers.RepeatedCompositeFieldContainer[GetAdDomainControllerStatusResult.DcInfo]
    def __init__(self, dc_info_vec: _Optional[_Iterable[_Union[GetAdDomainControllerStatusResult.DcInfo, _Mapping]]] = ...) -> None: ...

class GetDomainControllersArg(_message.Message):
    __slots__ = ("domain_fqdn", "tenant_id", "network_realm_id")
    DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    domain_fqdn: str
    tenant_id: str
    network_realm_id: int
    def __init__(self, domain_fqdn: _Optional[str] = ..., tenant_id: _Optional[str] = ..., network_realm_id: _Optional[int] = ...) -> None: ...

class GetDomainControllersResult(_message.Message):
    __slots__ = ("domain_controllers_vec",)
    DOMAIN_CONTROLLERS_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_controllers_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain_controllers_vec: _Optional[_Iterable[str]] = ...) -> None: ...
