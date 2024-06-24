from bridge.base import request_context_pb2 as _request_context_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from bridge.view_keeper import view_smb_permissions_pb2 as _view_smb_permissions_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from configs import service_auth_config_pb2 as _service_auth_config_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmbSecurityInfo(_message.Message):
    __slots__ = ("owner_sid", "aces", "uid", "gid", "mode")
    OWNER_SID_FIELD_NUMBER: _ClassVar[int]
    ACES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    owner_sid: _cluster_config_pb2.ClusterConfigProto.SID
    aces: _containers.RepeatedCompositeFieldContainer[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes.ACE]
    uid: int
    gid: int
    mode: int
    def __init__(self, owner_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., aces: _Optional[_Iterable[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes.ACE, _Mapping]]] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., mode: _Optional[int] = ...) -> None: ...

class LifecyclePolicy(_message.Message):
    __slots__ = ("path_prefix_2_prefix_id", "prefix_id_2_rules", "next_prefix_id")
    class LifecycleRule(_message.Message):
        __slots__ = ("id", "status", "rule_type", "file_mtime_filter", "file_creation_time_filter", "file_atime_filter", "file_size_filter", "file_ext_filter")
        class RuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kAllow: _ClassVar[LifecyclePolicy.LifecycleRule.RuleType]
            kDeny: _ClassVar[LifecyclePolicy.LifecycleRule.RuleType]
        kAllow: LifecyclePolicy.LifecycleRule.RuleType
        kDeny: LifecyclePolicy.LifecycleRule.RuleType
        class TimeFilter(_message.Message):
            __slots__ = ("date_usecs", "days")
            DATE_USECS_FIELD_NUMBER: _ClassVar[int]
            DAYS_FIELD_NUMBER: _ClassVar[int]
            date_usecs: int
            days: int
            def __init__(self, date_usecs: _Optional[int] = ..., days: _Optional[int] = ...) -> None: ...
        class FileSizeFilter(_message.Message):
            __slots__ = ("min_bytes", "max_bytes")
            MIN_BYTES_FIELD_NUMBER: _ClassVar[int]
            MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
            min_bytes: int
            max_bytes: int
            def __init__(self, min_bytes: _Optional[int] = ..., max_bytes: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        RULE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_MTIME_FILTER_FIELD_NUMBER: _ClassVar[int]
        FILE_CREATION_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
        FILE_ATIME_FILTER_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FILTER_FIELD_NUMBER: _ClassVar[int]
        FILE_EXT_FILTER_FIELD_NUMBER: _ClassVar[int]
        id: str
        status: bool
        rule_type: LifecyclePolicy.LifecycleRule.RuleType
        file_mtime_filter: LifecyclePolicy.LifecycleRule.TimeFilter
        file_creation_time_filter: LifecyclePolicy.LifecycleRule.TimeFilter
        file_atime_filter: LifecyclePolicy.LifecycleRule.TimeFilter
        file_size_filter: LifecyclePolicy.LifecycleRule.FileSizeFilter
        file_ext_filter: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., status: bool = ..., rule_type: _Optional[_Union[LifecyclePolicy.LifecycleRule.RuleType, str]] = ..., file_mtime_filter: _Optional[_Union[LifecyclePolicy.LifecycleRule.TimeFilter, _Mapping]] = ..., file_creation_time_filter: _Optional[_Union[LifecyclePolicy.LifecycleRule.TimeFilter, _Mapping]] = ..., file_atime_filter: _Optional[_Union[LifecyclePolicy.LifecycleRule.TimeFilter, _Mapping]] = ..., file_size_filter: _Optional[_Union[LifecyclePolicy.LifecycleRule.FileSizeFilter, _Mapping]] = ..., file_ext_filter: _Optional[_Iterable[str]] = ...) -> None: ...
    class LifecycleRules(_message.Message):
        __slots__ = ("rules",)
        RULES_FIELD_NUMBER: _ClassVar[int]
        rules: _containers.RepeatedCompositeFieldContainer[LifecyclePolicy.LifecycleRule]
        def __init__(self, rules: _Optional[_Iterable[_Union[LifecyclePolicy.LifecycleRule, _Mapping]]] = ...) -> None: ...
    class PathPrefix2PrefixIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class PrefixId2RulesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifecyclePolicy.LifecycleRules
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LifecyclePolicy.LifecycleRules, _Mapping]] = ...) -> None: ...
    PATH_PREFIX_2_PREFIX_ID_FIELD_NUMBER: _ClassVar[int]
    PREFIX_ID_2_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PREFIX_ID_FIELD_NUMBER: _ClassVar[int]
    path_prefix_2_prefix_id: _containers.ScalarMap[str, int]
    prefix_id_2_rules: _containers.MessageMap[int, LifecyclePolicy.LifecycleRules]
    next_prefix_id: int
    def __init__(self, path_prefix_2_prefix_id: _Optional[_Mapping[str, int]] = ..., prefix_id_2_rules: _Optional[_Mapping[int, LifecyclePolicy.LifecycleRules]] = ..., next_prefix_id: _Optional[int] = ...) -> None: ...

class ViewIdMappingProto(_message.Message):
    __slots__ = ("opclock_vec", "view_name", "view_id", "view_box_id", "is_internal", "creation_time_usecs", "root_info", "client_subnet_whitelist", "saved_client_subnet_whitelist", "update_intent", "root_names", "description", "storage_policy_override", "view_qos_principal_map", "view_qos_mapping_vec", "inode_id_floor", "immutable", "view_snap_tree_mapped_keys", "mapped_key_byte_swapped_with_last_byte", "mapped_key_swap_bit_mask", "minion_snap_tree_root_id", "minion_leaf_id", "disable_nfs_access", "view_display_name", "creation_time_2_clone_view_id_map", "src_view_id", "view_quota_policy", "enable_user_quota", "default_user_quota_policy", "quota_snap_tree_id", "usage_quota_snap_tree_id", "dir_quota_snap_tree_id", "enable_smb_access_based_dir_enumeration", "case_insensitive_entity_names", "s3_config", "s3_objects_with_conflicting_path_supported", "s3_key_mapping_config", "object_store_preserve_trailing_slashes", "object_store_preserve_leading_slashes", "protocol_access_info", "iris_metadata", "worm_lock_expiry_usecs", "file_level_data_lock_config", "saved_file_level_data_lock_config", "audit_logging_config", "client_subnet_whitelist_extends_global_whitelist", "mtime_ctime_explicitly_set_only", "enable_minion", "view_alias_map", "saved_view_alias_map", "smb_config", "replication_smb_config", "enable_mixed_mode_permissions", "file_extension_filter", "cache_epoch", "apollo_disable_namespace_fixing", "tenant_id", "nfs_config", "replication_nfs_config", "security_mode_config", "antivirus_scan_config", "antivirus_snap_tree_id", "user_view_tree_id_ceiling", "target_view_for_stubbing", "external_metadata", "latency_alert_params", "bookkeeper_group_id", "view_all_squash_uid", "view_all_squash_gid", "view_root_squash_uid", "view_root_squash_gid", "num_inode_atime_records", "trash_config", "uptier_config", "apollo_disable_orphaned_inodes_deletion", "client_netgroup_whitelist", "client_netgroup_whitelist_extends_global_whitelist", "enable_live_indexing", "performance_config", "pin_config", "language_locale", "category", "is_read_only", "mixed_mode_marker", "snapshot_self_service_config", "archival_info", "snap_fs_accelerator_map", "blur_clone_epoch_id", "service_auth_config", "restrict_access_to_internal", "deprecated_restrict_access_to_internal", "s3object_snap_tree_id", "blur_disabled", "s3_folder_support_enabled", "enable_brick_level_checksum", "snap_fs_dir_layout", "stats_container_id", "saved_immutable", "saved_blur_enabled", "workload_attrs", "workload_type", "bookkeeper_v2_group_id", "enable_small_dedup_chunk_creates", "lcm_policy")
    class ProtocolAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisabled: _ClassVar[ViewIdMappingProto.ProtocolAccess]
        kNonNative: _ClassVar[ViewIdMappingProto.ProtocolAccess]
        kNative: _ClassVar[ViewIdMappingProto.ProtocolAccess]
    kDisabled: ViewIdMappingProto.ProtocolAccess
    kNonNative: ViewIdMappingProto.ProtocolAccess
    kNative: ViewIdMappingProto.ProtocolAccess
    class FileExtensionFilterMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWhitelist: _ClassVar[ViewIdMappingProto.FileExtensionFilterMode]
        kBlacklist: _ClassVar[ViewIdMappingProto.FileExtensionFilterMode]
    kWhitelist: ViewIdMappingProto.FileExtensionFilterMode
    kBlacklist: ViewIdMappingProto.FileExtensionFilterMode
    class SecurityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNativeMode: _ClassVar[ViewIdMappingProto.SecurityMode]
        kUnifiedMode: _ClassVar[ViewIdMappingProto.SecurityMode]
        kNtfsMode: _ClassVar[ViewIdMappingProto.SecurityMode]
    kNativeMode: ViewIdMappingProto.SecurityMode
    kUnifiedMode: ViewIdMappingProto.SecurityMode
    kNtfsMode: ViewIdMappingProto.SecurityMode
    class ViewCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupTarget: _ClassVar[ViewIdMappingProto.ViewCategory]
        kFileServices: _ClassVar[ViewIdMappingProto.ViewCategory]
        kObjectServices: _ClassVar[ViewIdMappingProto.ViewCategory]
        KArchiveServices: _ClassVar[ViewIdMappingProto.ViewCategory]
    kBackupTarget: ViewIdMappingProto.ViewCategory
    kFileServices: ViewIdMappingProto.ViewCategory
    kObjectServices: ViewIdMappingProto.ViewCategory
    KArchiveServices: ViewIdMappingProto.ViewCategory
    class RootInfo(_message.Message):
        __slots__ = ("root_name", "root_inode_id", "root_snap_tree_id", "inconsistent_snaptree")
        ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
        INCONSISTENT_SNAPTREE_FIELD_NUMBER: _ClassVar[int]
        root_name: str
        root_inode_id: int
        root_snap_tree_id: int
        inconsistent_snaptree: bool
        def __init__(self, root_name: _Optional[str] = ..., root_inode_id: _Optional[int] = ..., root_snap_tree_id: _Optional[int] = ..., inconsistent_snaptree: bool = ...) -> None: ...
    class UpdateIntent(_message.Message):
        __slots__ = ("adding_view_name_mapping", "rename_view_mapping", "delete_view_mapping", "add_remove_alias_mapping", "update_view_indices", "sync_child_view_metadata")
        class AddViewNameMapping(_message.Message):
            __slots__ = ("expected_scribe_version", "root_info_provided_by_caller")
            EXPECTED_SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
            ROOT_INFO_PROVIDED_BY_CALLER_FIELD_NUMBER: _ClassVar[int]
            expected_scribe_version: int
            root_info_provided_by_caller: bool
            def __init__(self, expected_scribe_version: _Optional[int] = ..., root_info_provided_by_caller: bool = ...) -> None: ...
        class RenameViewMapping(_message.Message):
            __slots__ = ("old_name", "new_display_name", "expected_new_name_scribe_version")
            OLD_NAME_FIELD_NUMBER: _ClassVar[int]
            NEW_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            EXPECTED_NEW_NAME_SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
            old_name: str
            new_display_name: str
            expected_new_name_scribe_version: int
            def __init__(self, old_name: _Optional[str] = ..., new_display_name: _Optional[str] = ..., expected_new_name_scribe_version: _Optional[int] = ...) -> None: ...
        class DeleteViewMapping(_message.Message):
            __slots__ = ("view_id", "skip_adjusting_node_ref_count")
            VIEW_ID_FIELD_NUMBER: _ClassVar[int]
            SKIP_ADJUSTING_NODE_REF_COUNT_FIELD_NUMBER: _ClassVar[int]
            view_id: int
            skip_adjusting_node_ref_count: bool
            def __init__(self, view_id: _Optional[int] = ..., skip_adjusting_node_ref_count: bool = ...) -> None: ...
        class AddRemoveAliasMapping(_message.Message):
            __slots__ = ("alias_name", "expected_alias_scribe_version", "is_delete")
            ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
            EXPECTED_ALIAS_SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
            IS_DELETE_FIELD_NUMBER: _ClassVar[int]
            alias_name: str
            expected_alias_scribe_version: int
            is_delete: bool
            def __init__(self, alias_name: _Optional[str] = ..., expected_alias_scribe_version: _Optional[int] = ..., is_delete: bool = ...) -> None: ...
        class UpdateViewIndices(_message.Message):
            __slots__ = ("view_index",)
            class ViewIndex(_message.Message):
                __slots__ = ("index_id", "is_delete")
                class IndexId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    kDiscoverableSmbView: _ClassVar[ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId]
                    kDiscoverableNfsView: _ClassVar[ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId]
                    kDiscoverableNfs4View: _ClassVar[ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId]
                kDiscoverableSmbView: ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId
                kDiscoverableNfsView: ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId
                kDiscoverableNfs4View: ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId
                INDEX_ID_FIELD_NUMBER: _ClassVar[int]
                IS_DELETE_FIELD_NUMBER: _ClassVar[int]
                index_id: ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId
                is_delete: bool
                def __init__(self, index_id: _Optional[_Union[ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex.IndexId, str]] = ..., is_delete: bool = ...) -> None: ...
            VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
            view_index: _containers.RepeatedCompositeFieldContainer[ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex]
            def __init__(self, view_index: _Optional[_Iterable[_Union[ViewIdMappingProto.UpdateIntent.UpdateViewIndices.ViewIndex, _Mapping]]] = ...) -> None: ...
        class SynchronizeChildViewMetadata(_message.Message):
            __slots__ = ("child_views",)
            CHILD_VIEWS_FIELD_NUMBER: _ClassVar[int]
            child_views: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, child_views: _Optional[_Iterable[str]] = ...) -> None: ...
        ADDING_VIEW_NAME_MAPPING_FIELD_NUMBER: _ClassVar[int]
        RENAME_VIEW_MAPPING_FIELD_NUMBER: _ClassVar[int]
        DELETE_VIEW_MAPPING_FIELD_NUMBER: _ClassVar[int]
        ADD_REMOVE_ALIAS_MAPPING_FIELD_NUMBER: _ClassVar[int]
        UPDATE_VIEW_INDICES_FIELD_NUMBER: _ClassVar[int]
        SYNC_CHILD_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
        adding_view_name_mapping: ViewIdMappingProto.UpdateIntent.AddViewNameMapping
        rename_view_mapping: ViewIdMappingProto.UpdateIntent.RenameViewMapping
        delete_view_mapping: ViewIdMappingProto.UpdateIntent.DeleteViewMapping
        add_remove_alias_mapping: ViewIdMappingProto.UpdateIntent.AddRemoveAliasMapping
        update_view_indices: ViewIdMappingProto.UpdateIntent.UpdateViewIndices
        sync_child_view_metadata: ViewIdMappingProto.UpdateIntent.SynchronizeChildViewMetadata
        def __init__(self, adding_view_name_mapping: _Optional[_Union[ViewIdMappingProto.UpdateIntent.AddViewNameMapping, _Mapping]] = ..., rename_view_mapping: _Optional[_Union[ViewIdMappingProto.UpdateIntent.RenameViewMapping, _Mapping]] = ..., delete_view_mapping: _Optional[_Union[ViewIdMappingProto.UpdateIntent.DeleteViewMapping, _Mapping]] = ..., add_remove_alias_mapping: _Optional[_Union[ViewIdMappingProto.UpdateIntent.AddRemoveAliasMapping, _Mapping]] = ..., update_view_indices: _Optional[_Union[ViewIdMappingProto.UpdateIntent.UpdateViewIndices, _Mapping]] = ..., sync_child_view_metadata: _Optional[_Union[ViewIdMappingProto.UpdateIntent.SynchronizeChildViewMetadata, _Mapping]] = ...) -> None: ...
    class RootNames(_message.Message):
        __slots__ = ("fs_root_name", "config_root_name", "object_root_name", "internal_root_name")
        FS_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        CONFIG_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        fs_root_name: str
        config_root_name: str
        object_root_name: str
        internal_root_name: str
        def __init__(self, fs_root_name: _Optional[str] = ..., config_root_name: _Optional[str] = ..., object_root_name: _Optional[str] = ..., internal_root_name: _Optional[str] = ...) -> None: ...
    class ViewQosPrincipalMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cluster_config_pb2.ClusterConfigProto.QoSPrincipal
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QoSPrincipal, _Mapping]] = ...) -> None: ...
    class CreationTime2CloneViewIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ProtocolAccessInfo(_message.Message):
        __slots__ = ("nfs_access", "smb_access", "s3_access", "iscsi_access", "swift_access", "nfs4_access")
        NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        SMB_ACCESS_FIELD_NUMBER: _ClassVar[int]
        S3_ACCESS_FIELD_NUMBER: _ClassVar[int]
        ISCSI_ACCESS_FIELD_NUMBER: _ClassVar[int]
        SWIFT_ACCESS_FIELD_NUMBER: _ClassVar[int]
        NFS4_ACCESS_FIELD_NUMBER: _ClassVar[int]
        nfs_access: ViewIdMappingProto.ProtocolAccess
        smb_access: ViewIdMappingProto.ProtocolAccess
        s3_access: ViewIdMappingProto.ProtocolAccess
        iscsi_access: ViewIdMappingProto.ProtocolAccess
        swift_access: ViewIdMappingProto.ProtocolAccess
        nfs4_access: ViewIdMappingProto.ProtocolAccess
        def __init__(self, nfs_access: _Optional[_Union[ViewIdMappingProto.ProtocolAccess, str]] = ..., smb_access: _Optional[_Union[ViewIdMappingProto.ProtocolAccess, str]] = ..., s3_access: _Optional[_Union[ViewIdMappingProto.ProtocolAccess, str]] = ..., iscsi_access: _Optional[_Union[ViewIdMappingProto.ProtocolAccess, str]] = ..., swift_access: _Optional[_Union[ViewIdMappingProto.ProtocolAccess, str]] = ..., nfs4_access: _Optional[_Union[ViewIdMappingProto.ProtocolAccess, str]] = ...) -> None: ...
    class IrisMetadata(_message.Message):
        __slots__ = ("access_sids", "is_locked", "owner_sid", "is_externally_triggered_backup_target", "template_id", "template_name")
        ACCESS_SIDS_FIELD_NUMBER: _ClassVar[int]
        IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
        OWNER_SID_FIELD_NUMBER: _ClassVar[int]
        IS_EXTERNALLY_TRIGGERED_BACKUP_TARGET_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        access_sids: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        is_locked: bool
        owner_sid: _cluster_config_pb2.ClusterConfigProto.SID
        is_externally_triggered_backup_target: bool
        template_id: int
        template_name: str
        def __init__(self, access_sids: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., is_locked: bool = ..., owner_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., is_externally_triggered_backup_target: bool = ..., template_id: _Optional[int] = ..., template_name: _Optional[str] = ...) -> None: ...
    class FileLevelDataLockConfig(_message.Message):
        __slots__ = ("protocol", "auto_lock_duration_usecs", "default_retention_duration_usecs", "min_retention_duration_usecs", "max_retention_duration_usecs", "hold_timestamp_usecs", "mode", "coexisting_lock_mode", "default_retention_duration_years", "ignore_existing_files")
        class ExplicitLockingProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSetReadOnly: _ClassVar[ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingProtocol]
            kSetAtime: _ClassVar[ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingProtocol]
        kSetReadOnly: ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingProtocol
        kSetAtime: ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingProtocol
        class ExplicitLockingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kCompliance: _ClassVar[ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode]
            kEnterprise: _ClassVar[ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode]
        kCompliance: ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode
        kEnterprise: ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        AUTO_LOCK_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
        MIN_RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
        MAX_RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
        HOLD_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        COEXISTING_LOCK_MODE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_RETENTION_DURATION_YEARS_FIELD_NUMBER: _ClassVar[int]
        IGNORE_EXISTING_FILES_FIELD_NUMBER: _ClassVar[int]
        protocol: ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingProtocol
        auto_lock_duration_usecs: int
        default_retention_duration_usecs: int
        min_retention_duration_usecs: int
        max_retention_duration_usecs: int
        hold_timestamp_usecs: int
        mode: ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode
        coexisting_lock_mode: bool
        default_retention_duration_years: int
        ignore_existing_files: bool
        def __init__(self, protocol: _Optional[_Union[ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingProtocol, str]] = ..., auto_lock_duration_usecs: _Optional[int] = ..., default_retention_duration_usecs: _Optional[int] = ..., min_retention_duration_usecs: _Optional[int] = ..., max_retention_duration_usecs: _Optional[int] = ..., hold_timestamp_usecs: _Optional[int] = ..., mode: _Optional[_Union[ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode, str]] = ..., coexisting_lock_mode: bool = ..., default_retention_duration_years: _Optional[int] = ..., ignore_existing_files: bool = ...) -> None: ...
    class SmbConfigProto(_message.Message):
        __slots__ = ("discovery_enabled", "encryption_enabled", "encryption_required", "share_level_acl", "is_share_level_acl_empty", "caching_type", "continuous_availability", "oplock_enabled", "smb_command_timeout_secs", "superusers", "snapshot_acls")
        class OfflineCachingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kManualCaching: _ClassVar[ViewIdMappingProto.SmbConfigProto.OfflineCachingType]
            kAutoCaching: _ClassVar[ViewIdMappingProto.SmbConfigProto.OfflineCachingType]
            kVdoCaching: _ClassVar[ViewIdMappingProto.SmbConfigProto.OfflineCachingType]
            kNoCaching: _ClassVar[ViewIdMappingProto.SmbConfigProto.OfflineCachingType]
        kManualCaching: ViewIdMappingProto.SmbConfigProto.OfflineCachingType
        kAutoCaching: ViewIdMappingProto.SmbConfigProto.OfflineCachingType
        kVdoCaching: ViewIdMappingProto.SmbConfigProto.OfflineCachingType
        kNoCaching: ViewIdMappingProto.SmbConfigProto.OfflineCachingType
        DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        SHARE_LEVEL_ACL_FIELD_NUMBER: _ClassVar[int]
        IS_SHARE_LEVEL_ACL_EMPTY_FIELD_NUMBER: _ClassVar[int]
        CACHING_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTINUOUS_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        OPLOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SMB_COMMAND_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
        SUPERUSERS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ACLS_FIELD_NUMBER: _ClassVar[int]
        discovery_enabled: bool
        encryption_enabled: bool
        encryption_required: bool
        share_level_acl: _containers.RepeatedCompositeFieldContainer[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes.ACE]
        is_share_level_acl_empty: bool
        caching_type: ViewIdMappingProto.SmbConfigProto.OfflineCachingType
        continuous_availability: bool
        oplock_enabled: bool
        smb_command_timeout_secs: int
        superusers: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        snapshot_acls: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        def __init__(self, discovery_enabled: bool = ..., encryption_enabled: bool = ..., encryption_required: bool = ..., share_level_acl: _Optional[_Iterable[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes.ACE, _Mapping]]] = ..., is_share_level_acl_empty: bool = ..., caching_type: _Optional[_Union[ViewIdMappingProto.SmbConfigProto.OfflineCachingType, str]] = ..., continuous_availability: bool = ..., oplock_enabled: bool = ..., smb_command_timeout_secs: _Optional[int] = ..., superusers: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., snapshot_acls: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...
    class ViewAliasMetadata(_message.Message):
        __slots__ = ("alias_display_name", "path", "smb_config", "client_subnet_whitelist", "enable_smb_access_based_dir_enumeration", "audit_logging_config")
        ALIAS_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
        AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        alias_display_name: str
        path: str
        smb_config: ViewIdMappingProto.SmbConfigProto
        client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
        enable_smb_access_based_dir_enumeration: bool
        audit_logging_config: _cluster_config_pb2.ClusterConfigProto.AuditLoggingConfig
        def __init__(self, alias_display_name: _Optional[str] = ..., path: _Optional[str] = ..., smb_config: _Optional[_Union[ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., enable_smb_access_based_dir_enumeration: bool = ..., audit_logging_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ...) -> None: ...
    class ViewAliasMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ViewIdMappingProto.ViewAliasMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ViewIdMappingProto.ViewAliasMetadata, _Mapping]] = ...) -> None: ...
    class SavedViewAliasMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ViewIdMappingProto.ViewAliasMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ViewIdMappingProto.ViewAliasMetadata, _Mapping]] = ...) -> None: ...
    class FileExtensionFilter(_message.Message):
        __slots__ = ("is_enabled", "mode", "file_extensions_map")
        class FileExtensionsMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bool
            def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        FILE_EXTENSIONS_MAP_FIELD_NUMBER: _ClassVar[int]
        is_enabled: bool
        mode: ViewIdMappingProto.FileExtensionFilterMode
        file_extensions_map: _containers.ScalarMap[str, bool]
        def __init__(self, is_enabled: bool = ..., mode: _Optional[_Union[ViewIdMappingProto.FileExtensionFilterMode, str]] = ..., file_extensions_map: _Optional[_Mapping[str, bool]] = ...) -> None: ...
    class NfsConfigProto(_message.Message):
        __slots__ = ("discovery_enabled", "auth_unix_enabled", "rpcsec_gss_none_enabled", "rpcsec_gss_integrity_enabled", "rpcsec_gss_privacy_enabled", "wcc_enable")
        DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        AUTH_UNIX_ENABLED_FIELD_NUMBER: _ClassVar[int]
        RPCSEC_GSS_NONE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        RPCSEC_GSS_INTEGRITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        RPCSEC_GSS_PRIVACY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        WCC_ENABLE_FIELD_NUMBER: _ClassVar[int]
        discovery_enabled: bool
        auth_unix_enabled: bool
        rpcsec_gss_none_enabled: bool
        rpcsec_gss_integrity_enabled: bool
        rpcsec_gss_privacy_enabled: bool
        wcc_enable: bool
        def __init__(self, discovery_enabled: bool = ..., auth_unix_enabled: bool = ..., rpcsec_gss_none_enabled: bool = ..., rpcsec_gss_integrity_enabled: bool = ..., rpcsec_gss_privacy_enabled: bool = ..., wcc_enable: bool = ...) -> None: ...
    class SecurityModeConfig(_message.Message):
        __slots__ = ("security_mode",)
        SECURITY_MODE_FIELD_NUMBER: _ClassVar[int]
        security_mode: ViewIdMappingProto.SecurityMode
        def __init__(self, security_mode: _Optional[_Union[ViewIdMappingProto.SecurityMode, str]] = ...) -> None: ...
    class AntivirusScanConfig(_message.Message):
        __slots__ = ("is_enabled", "scan_on_access", "scan_on_close", "block_access_on_scan_failure", "maximum_scan_file_size", "scan_filter", "scan_timeout_usecs", "antivirus_service_group_id")
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SCAN_ON_ACCESS_FIELD_NUMBER: _ClassVar[int]
        SCAN_ON_CLOSE_FIELD_NUMBER: _ClassVar[int]
        BLOCK_ACCESS_ON_SCAN_FAILURE_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_SCAN_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        SCAN_FILTER_FIELD_NUMBER: _ClassVar[int]
        SCAN_TIMEOUT_USECS_FIELD_NUMBER: _ClassVar[int]
        ANTIVIRUS_SERVICE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        is_enabled: bool
        scan_on_access: bool
        scan_on_close: bool
        block_access_on_scan_failure: bool
        maximum_scan_file_size: int
        scan_filter: ViewIdMappingProto.FileExtensionFilter
        scan_timeout_usecs: int
        antivirus_service_group_id: int
        def __init__(self, is_enabled: bool = ..., scan_on_access: bool = ..., scan_on_close: bool = ..., block_access_on_scan_failure: bool = ..., maximum_scan_file_size: _Optional[int] = ..., scan_filter: _Optional[_Union[ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., scan_timeout_usecs: _Optional[int] = ..., antivirus_service_group_id: _Optional[int] = ...) -> None: ...
    class ExternalMetadata(_message.Message):
        __slots__ = ("magneto_source_view_id", "magneto_source_job_uid", "replication_ancestor_hint", "view_uid", "source_cluster_id", "source_cluster_incarnation", "active_cluster_id", "active_cluster_incarnation", "unplanned_failover_id")
        MAGNETO_SOURCE_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        MAGNETO_SOURCE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
        REPLICATION_ANCESTOR_HINT_FIELD_NUMBER: _ClassVar[int]
        VIEW_UID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CLUSTER_INCARNATION_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_CLUSTER_INCARNATION_FIELD_NUMBER: _ClassVar[int]
        UNPLANNED_FAILOVER_ID_FIELD_NUMBER: _ClassVar[int]
        magneto_source_view_id: str
        magneto_source_job_uid: _universal_id_pb2.UniversalIdProto
        replication_ancestor_hint: _universal_id_pb2.UniversalIdProto
        view_uid: _universal_id_pb2.UniversalIdProto
        source_cluster_id: int
        source_cluster_incarnation: int
        active_cluster_id: int
        active_cluster_incarnation: int
        unplanned_failover_id: _universal_id_pb2.UniversalIdProto
        def __init__(self, magneto_source_view_id: _Optional[str] = ..., magneto_source_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., replication_ancestor_hint: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., view_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., source_cluster_id: _Optional[int] = ..., source_cluster_incarnation: _Optional[int] = ..., active_cluster_id: _Optional[int] = ..., active_cluster_incarnation: _Optional[int] = ..., unplanned_failover_id: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
    class LatencyAlertParams(_message.Message):
        __slots__ = ("write_latency_threshold_msecs", "write_oio_threshold", "read_latency_threshold_msecs", "read_oio_threshold", "latency_window_secs", "meta_alert_params")
        class MetaOpAlertParams(_message.Message):
            __slots__ = ("alert_type", "latency_threshold_msecs", "oio_threshold")
            class MetaAlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kCreateFile: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kMkDir: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kMkNod: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kSymLink: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kRmDir: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kRemoveFile: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kLookupInodeMetaData: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kLookupPath: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kLookupDirectoryEntry: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kLink: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kSetattr: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kReaddir: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kRename: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kCloneBytes: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kCommit: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kDeleteOrphan: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kDeleteGarbage: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kDirQuotaRecursiveWalk: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
                kSnapFsFixer: _ClassVar[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType]
            kCreateFile: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kMkDir: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kMkNod: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kSymLink: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kRmDir: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kRemoveFile: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kLookupInodeMetaData: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kLookupPath: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kLookupDirectoryEntry: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kLink: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kSetattr: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kReaddir: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kRename: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kCloneBytes: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kCommit: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kDeleteOrphan: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kDeleteGarbage: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kDirQuotaRecursiveWalk: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            kSnapFsFixer: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
            LATENCY_THRESHOLD_MSECS_FIELD_NUMBER: _ClassVar[int]
            OIO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            alert_type: ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType
            latency_threshold_msecs: int
            oio_threshold: float
            def __init__(self, alert_type: _Optional[_Union[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams.MetaAlertType, str]] = ..., latency_threshold_msecs: _Optional[int] = ..., oio_threshold: _Optional[float] = ...) -> None: ...
        WRITE_LATENCY_THRESHOLD_MSECS_FIELD_NUMBER: _ClassVar[int]
        WRITE_OIO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        READ_LATENCY_THRESHOLD_MSECS_FIELD_NUMBER: _ClassVar[int]
        READ_OIO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        LATENCY_WINDOW_SECS_FIELD_NUMBER: _ClassVar[int]
        META_ALERT_PARAMS_FIELD_NUMBER: _ClassVar[int]
        write_latency_threshold_msecs: int
        write_oio_threshold: float
        read_latency_threshold_msecs: int
        read_oio_threshold: float
        latency_window_secs: int
        meta_alert_params: _containers.RepeatedCompositeFieldContainer[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams]
        def __init__(self, write_latency_threshold_msecs: _Optional[int] = ..., write_oio_threshold: _Optional[float] = ..., read_latency_threshold_msecs: _Optional[int] = ..., read_oio_threshold: _Optional[float] = ..., latency_window_secs: _Optional[int] = ..., meta_alert_params: _Optional[_Iterable[_Union[ViewIdMappingProto.LatencyAlertParams.MetaOpAlertParams, _Mapping]]] = ...) -> None: ...
    class TrashConfig(_message.Message):
        __slots__ = ("retention_duration_usecs",)
        RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
        retention_duration_usecs: int
        def __init__(self, retention_duration_usecs: _Optional[int] = ...) -> None: ...
    class UptierConfig(_message.Message):
        __slots__ = ("file_select_policy", "num_file_access", "hot_file_window", "file_size_policy", "file_size", "filtering_policy")
        class FileSelectPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kLastAccessed: _ClassVar[ViewIdMappingProto.UptierConfig.FileSelectPolicy]
            kLastModified: _ClassVar[ViewIdMappingProto.UptierConfig.FileSelectPolicy]
        kLastAccessed: ViewIdMappingProto.UptierConfig.FileSelectPolicy
        kLastModified: ViewIdMappingProto.UptierConfig.FileSelectPolicy
        class FileSizePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kGreaterThan: _ClassVar[ViewIdMappingProto.UptierConfig.FileSizePolicy]
            kSmallerThan: _ClassVar[ViewIdMappingProto.UptierConfig.FileSizePolicy]
        kGreaterThan: ViewIdMappingProto.UptierConfig.FileSizePolicy
        kSmallerThan: ViewIdMappingProto.UptierConfig.FileSizePolicy
        class FilteringPolicyProto(_message.Message):
            __slots__ = ("allow_filters", "deny_filters")
            ALLOW_FILTERS_FIELD_NUMBER: _ClassVar[int]
            DENY_FILTERS_FIELD_NUMBER: _ClassVar[int]
            allow_filters: _containers.RepeatedScalarFieldContainer[str]
            deny_filters: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, allow_filters: _Optional[_Iterable[str]] = ..., deny_filters: _Optional[_Iterable[str]] = ...) -> None: ...
        FILE_SELECT_POLICY_FIELD_NUMBER: _ClassVar[int]
        NUM_FILE_ACCESS_FIELD_NUMBER: _ClassVar[int]
        HOT_FILE_WINDOW_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_POLICY_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
        file_select_policy: ViewIdMappingProto.UptierConfig.FileSelectPolicy
        num_file_access: int
        hot_file_window: int
        file_size_policy: ViewIdMappingProto.UptierConfig.FileSizePolicy
        file_size: int
        filtering_policy: ViewIdMappingProto.UptierConfig.FilteringPolicyProto
        def __init__(self, file_select_policy: _Optional[_Union[ViewIdMappingProto.UptierConfig.FileSelectPolicy, str]] = ..., num_file_access: _Optional[int] = ..., hot_file_window: _Optional[int] = ..., file_size_policy: _Optional[_Union[ViewIdMappingProto.UptierConfig.FileSizePolicy, str]] = ..., file_size: _Optional[int] = ..., filtering_policy: _Optional[_Union[ViewIdMappingProto.UptierConfig.FilteringPolicyProto, _Mapping]] = ...) -> None: ...
    class PerformanceConfig(_message.Message):
        __slots__ = ("lexicographic_prefetch",)
        LEXICOGRAPHIC_PREFETCH_FIELD_NUMBER: _ClassVar[int]
        lexicographic_prefetch: bool
        def __init__(self, lexicographic_prefetch: bool = ...) -> None: ...
    class PinConfig(_message.Message):
        __slots__ = ("is_pinned", "pinned_time_secs", "last_update_time_secs")
        IS_PINNED_FIELD_NUMBER: _ClassVar[int]
        PINNED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        is_pinned: bool
        pinned_time_secs: int
        last_update_time_secs: int
        def __init__(self, is_pinned: bool = ..., pinned_time_secs: _Optional[int] = ..., last_update_time_secs: _Optional[int] = ...) -> None: ...
    class SnapshotSelfServiceConfig(_message.Message):
        __slots__ = ("dot_snapshot_enabled", "previous_versions_enabled", "dot_snapshot_smb_enabled", "snapshot_dir_name", "alternate_snapshot_dir_name", "snapshot_acls", "snapshot_deny_acls", "is_snapshot_acl_touched", "dot_snapshot_nfs_enabled", "is_dot_snapshot_nfs_enabled_touched")
        DOT_SNAPSHOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_VERSIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DOT_SNAPSHOT_SMB_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        ALTERNATE_SNAPSHOT_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ACLS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_DENY_ACLS_FIELD_NUMBER: _ClassVar[int]
        IS_SNAPSHOT_ACL_TOUCHED_FIELD_NUMBER: _ClassVar[int]
        DOT_SNAPSHOT_NFS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        IS_DOT_SNAPSHOT_NFS_ENABLED_TOUCHED_FIELD_NUMBER: _ClassVar[int]
        dot_snapshot_enabled: bool
        previous_versions_enabled: bool
        dot_snapshot_smb_enabled: bool
        snapshot_dir_name: str
        alternate_snapshot_dir_name: str
        snapshot_acls: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        snapshot_deny_acls: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
        is_snapshot_acl_touched: bool
        dot_snapshot_nfs_enabled: bool
        is_dot_snapshot_nfs_enabled_touched: bool
        def __init__(self, dot_snapshot_enabled: bool = ..., previous_versions_enabled: bool = ..., dot_snapshot_smb_enabled: bool = ..., snapshot_dir_name: _Optional[str] = ..., alternate_snapshot_dir_name: _Optional[str] = ..., snapshot_acls: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., snapshot_deny_acls: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., is_snapshot_acl_touched: bool = ..., dot_snapshot_nfs_enabled: bool = ..., is_dot_snapshot_nfs_enabled_touched: bool = ...) -> None: ...
    class ArchivalInfo(_message.Message):
        __slots__ = ("cloud_domain_id", "target_tier_type")
        CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        cloud_domain_id: int
        target_tier_type: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType
        def __init__(self, cloud_domain_id: _Optional[int] = ..., target_tier_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierType, _Mapping]] = ...) -> None: ...
    class SnapFsAccelerator(_message.Message):
        __slots__ = ("min_id_2_entities_map",)
        class BlurBlobSet(_message.Message):
            __slots__ = ("blob_vec", "entry_reservation", "max_entity_id")
            BLOB_VEC_FIELD_NUMBER: _ClassVar[int]
            ENTRY_RESERVATION_FIELD_NUMBER: _ClassVar[int]
            MAX_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
            blob_vec: _containers.RepeatedScalarFieldContainer[int]
            entry_reservation: int
            max_entity_id: int
            def __init__(self, blob_vec: _Optional[_Iterable[int]] = ..., entry_reservation: _Optional[int] = ..., max_entity_id: _Optional[int] = ...) -> None: ...
        class MinId2EntitiesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: ViewIdMappingProto.SnapFsAccelerator.BlurBlobSet
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ViewIdMappingProto.SnapFsAccelerator.BlurBlobSet, _Mapping]] = ...) -> None: ...
        MIN_ID_2_ENTITIES_MAP_FIELD_NUMBER: _ClassVar[int]
        min_id_2_entities_map: _containers.MessageMap[int, ViewIdMappingProto.SnapFsAccelerator.BlurBlobSet]
        def __init__(self, min_id_2_entities_map: _Optional[_Mapping[int, ViewIdMappingProto.SnapFsAccelerator.BlurBlobSet]] = ...) -> None: ...
    class SnapFsAcceleratorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ViewIdMappingProto.SnapFsAccelerator
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ViewIdMappingProto.SnapFsAccelerator, _Mapping]] = ...) -> None: ...
    class SnapFSDirectoryLayout(_message.Message):
        __slots__ = ("avg_entries_per_data_fragment", "num_fragments_high_threshold", "max_entries_per_data_fragment")
        AVG_ENTRIES_PER_DATA_FRAGMENT_FIELD_NUMBER: _ClassVar[int]
        NUM_FRAGMENTS_HIGH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        MAX_ENTRIES_PER_DATA_FRAGMENT_FIELD_NUMBER: _ClassVar[int]
        avg_entries_per_data_fragment: int
        num_fragments_high_threshold: int
        max_entries_per_data_fragment: int
        def __init__(self, avg_entries_per_data_fragment: _Optional[int] = ..., num_fragments_high_threshold: _Optional[int] = ..., max_entries_per_data_fragment: _Optional[int] = ...) -> None: ...
    class WorkloadAttributes(_message.Message):
        __slots__ = ("tags_vec",)
        TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
        tags_vec: _containers.RepeatedCompositeFieldContainer[_request_context_pb2.WorkloadTag]
        def __init__(self, tags_vec: _Optional[_Iterable[_Union[_request_context_pb2.WorkloadTag, _Mapping]]] = ...) -> None: ...
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ROOT_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    SAVED_CLIENT_SUBNET_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAMES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    VIEW_QOS_PRINCIPAL_MAP_FIELD_NUMBER: _ClassVar[int]
    VIEW_QOS_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    VIEW_SNAP_TREE_MAPPED_KEYS_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_BYTE_SWAPPED_WITH_LAST_BYTE_FIELD_NUMBER: _ClassVar[int]
    MAPPED_KEY_SWAP_BIT_MASK_FIELD_NUMBER: _ClassVar[int]
    MINION_SNAP_TREE_ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    MINION_LEAF_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NFS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    VIEW_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_2_CLONE_VIEW_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    SRC_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_USER_QUOTA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_USER_QUOTA_POLICY_FIELD_NUMBER: _ClassVar[int]
    QUOTA_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_QUOTA_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    DIR_QUOTA_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMB_ACCESS_BASED_DIR_ENUMERATION_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_ENTITY_NAMES_FIELD_NUMBER: _ClassVar[int]
    S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
    S3_OBJECTS_WITH_CONFLICTING_PATH_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    S3_KEY_MAPPING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_PRESERVE_TRAILING_SLASHES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_PRESERVE_LEADING_SLASHES_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    IRIS_METADATA_FIELD_NUMBER: _ClassVar[int]
    WORM_LOCK_EXPIRY_USECS_FIELD_NUMBER: _ClassVar[int]
    FILE_LEVEL_DATA_LOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SAVED_FILE_LEVEL_DATA_LOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUBNET_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    MTIME_CTIME_EXPLICITLY_SET_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINION_FIELD_NUMBER: _ClassVar[int]
    VIEW_ALIAS_MAP_FIELD_NUMBER: _ClassVar[int]
    SAVED_VIEW_ALIAS_MAP_FIELD_NUMBER: _ClassVar[int]
    SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_SMB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MIXED_MODE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    CACHE_EPOCH_FIELD_NUMBER: _ClassVar[int]
    APOLLO_DISABLE_NAMESPACE_FIXING_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_NFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECURITY_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_SCAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_VIEW_TREE_ID_CEILING_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_FOR_STUBBING_FIELD_NUMBER: _ClassVar[int]
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
    APOLLO_DISABLE_ORPHANED_INODES_DELETION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NETGROUP_WHITELIST_EXTENDS_GLOBAL_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LIVE_INDEXING_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    MIXED_MODE_MARKER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SELF_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_ACCELERATOR_MAP_FIELD_NUMBER: _ClassVar[int]
    BLUR_CLONE_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_ACCESS_TO_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_RESTRICT_ACCESS_TO_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    S3OBJECT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    BLUR_DISABLED_FIELD_NUMBER: _ClassVar[int]
    S3_FOLDER_SUPPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_DIR_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    SAVED_IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    SAVED_BLUR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ATTRS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_V2_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SMALL_DEDUP_CHUNK_CREATES_FIELD_NUMBER: _ClassVar[int]
    LCM_POLICY_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    view_name: str
    view_id: int
    view_box_id: int
    is_internal: bool
    creation_time_usecs: int
    root_info: _containers.RepeatedCompositeFieldContainer[ViewIdMappingProto.RootInfo]
    client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    saved_client_subnet_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    update_intent: ViewIdMappingProto.UpdateIntent
    root_names: ViewIdMappingProto.RootNames
    description: str
    storage_policy_override: _cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride
    view_qos_principal_map: _containers.MessageMap[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]
    view_qos_mapping_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.QoSMapping]
    inode_id_floor: int
    immutable: bool
    view_snap_tree_mapped_keys: bool
    mapped_key_byte_swapped_with_last_byte: int
    mapped_key_swap_bit_mask: int
    minion_snap_tree_root_id: int
    minion_leaf_id: int
    disable_nfs_access: bool
    view_display_name: str
    creation_time_2_clone_view_id_map: _containers.ScalarMap[int, int]
    src_view_id: int
    view_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    enable_user_quota: bool
    default_user_quota_policy: _cluster_config_pb2.ClusterConfigProto.QuotaPolicy
    quota_snap_tree_id: int
    usage_quota_snap_tree_id: int
    dir_quota_snap_tree_id: int
    enable_smb_access_based_dir_enumeration: bool
    case_insensitive_entity_names: bool
    s3_config: _s3_metadata_pb2.S3BucketConfigProto
    s3_objects_with_conflicting_path_supported: bool
    s3_key_mapping_config: _s3_metadata_pb2.S3KeyMappingConfigProto
    object_store_preserve_trailing_slashes: bool
    object_store_preserve_leading_slashes: bool
    protocol_access_info: ViewIdMappingProto.ProtocolAccessInfo
    iris_metadata: ViewIdMappingProto.IrisMetadata
    worm_lock_expiry_usecs: int
    file_level_data_lock_config: ViewIdMappingProto.FileLevelDataLockConfig
    saved_file_level_data_lock_config: ViewIdMappingProto.FileLevelDataLockConfig
    audit_logging_config: _cluster_config_pb2.ClusterConfigProto.AuditLoggingConfig
    client_subnet_whitelist_extends_global_whitelist: bool
    mtime_ctime_explicitly_set_only: bool
    enable_minion: bool
    view_alias_map: _containers.MessageMap[str, ViewIdMappingProto.ViewAliasMetadata]
    saved_view_alias_map: _containers.MessageMap[str, ViewIdMappingProto.ViewAliasMetadata]
    smb_config: ViewIdMappingProto.SmbConfigProto
    replication_smb_config: ViewIdMappingProto.SmbConfigProto
    enable_mixed_mode_permissions: bool
    file_extension_filter: ViewIdMappingProto.FileExtensionFilter
    cache_epoch: int
    apollo_disable_namespace_fixing: bool
    tenant_id: str
    nfs_config: ViewIdMappingProto.NfsConfigProto
    replication_nfs_config: ViewIdMappingProto.NfsConfigProto
    security_mode_config: ViewIdMappingProto.SecurityModeConfig
    antivirus_scan_config: ViewIdMappingProto.AntivirusScanConfig
    antivirus_snap_tree_id: int
    user_view_tree_id_ceiling: int
    target_view_for_stubbing: bool
    external_metadata: ViewIdMappingProto.ExternalMetadata
    latency_alert_params: ViewIdMappingProto.LatencyAlertParams
    bookkeeper_group_id: int
    view_all_squash_uid: int
    view_all_squash_gid: int
    view_root_squash_uid: int
    view_root_squash_gid: int
    num_inode_atime_records: int
    trash_config: ViewIdMappingProto.TrashConfig
    uptier_config: ViewIdMappingProto.UptierConfig
    apollo_disable_orphaned_inodes_deletion: bool
    client_netgroup_whitelist: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.NISNetgroup]
    client_netgroup_whitelist_extends_global_whitelist: bool
    enable_live_indexing: bool
    performance_config: ViewIdMappingProto.PerformanceConfig
    pin_config: ViewIdMappingProto.PinConfig
    language_locale: str
    category: ViewIdMappingProto.ViewCategory
    is_read_only: bool
    mixed_mode_marker: str
    snapshot_self_service_config: ViewIdMappingProto.SnapshotSelfServiceConfig
    archival_info: ViewIdMappingProto.ArchivalInfo
    snap_fs_accelerator_map: _containers.MessageMap[int, ViewIdMappingProto.SnapFsAccelerator]
    blur_clone_epoch_id: int
    service_auth_config: _service_auth_config_pb2.ServiceAuthConfigProto
    restrict_access_to_internal: bool
    deprecated_restrict_access_to_internal: bool
    s3object_snap_tree_id: int
    blur_disabled: bool
    s3_folder_support_enabled: bool
    enable_brick_level_checksum: bool
    snap_fs_dir_layout: ViewIdMappingProto.SnapFSDirectoryLayout
    stats_container_id: int
    saved_immutable: bool
    saved_blur_enabled: bool
    workload_attrs: ViewIdMappingProto.WorkloadAttributes
    workload_type: _request_context_pb2.WorkloadType
    bookkeeper_v2_group_id: str
    enable_small_dedup_chunk_creates: bool
    lcm_policy: LifecyclePolicy
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., is_internal: bool = ..., creation_time_usecs: _Optional[int] = ..., root_info: _Optional[_Iterable[_Union[ViewIdMappingProto.RootInfo, _Mapping]]] = ..., client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., saved_client_subnet_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., update_intent: _Optional[_Union[ViewIdMappingProto.UpdateIntent, _Mapping]] = ..., root_names: _Optional[_Union[ViewIdMappingProto.RootNames, _Mapping]] = ..., description: _Optional[str] = ..., storage_policy_override: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicyOverride, _Mapping]] = ..., view_qos_principal_map: _Optional[_Mapping[int, _cluster_config_pb2.ClusterConfigProto.QoSPrincipal]] = ..., view_qos_mapping_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.QoSMapping, _Mapping]]] = ..., inode_id_floor: _Optional[int] = ..., immutable: bool = ..., view_snap_tree_mapped_keys: bool = ..., mapped_key_byte_swapped_with_last_byte: _Optional[int] = ..., mapped_key_swap_bit_mask: _Optional[int] = ..., minion_snap_tree_root_id: _Optional[int] = ..., minion_leaf_id: _Optional[int] = ..., disable_nfs_access: bool = ..., view_display_name: _Optional[str] = ..., creation_time_2_clone_view_id_map: _Optional[_Mapping[int, int]] = ..., src_view_id: _Optional[int] = ..., view_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., enable_user_quota: bool = ..., default_user_quota_policy: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.QuotaPolicy, _Mapping]] = ..., quota_snap_tree_id: _Optional[int] = ..., usage_quota_snap_tree_id: _Optional[int] = ..., dir_quota_snap_tree_id: _Optional[int] = ..., enable_smb_access_based_dir_enumeration: bool = ..., case_insensitive_entity_names: bool = ..., s3_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., s3_objects_with_conflicting_path_supported: bool = ..., s3_key_mapping_config: _Optional[_Union[_s3_metadata_pb2.S3KeyMappingConfigProto, _Mapping]] = ..., object_store_preserve_trailing_slashes: bool = ..., object_store_preserve_leading_slashes: bool = ..., protocol_access_info: _Optional[_Union[ViewIdMappingProto.ProtocolAccessInfo, _Mapping]] = ..., iris_metadata: _Optional[_Union[ViewIdMappingProto.IrisMetadata, _Mapping]] = ..., worm_lock_expiry_usecs: _Optional[int] = ..., file_level_data_lock_config: _Optional[_Union[ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., saved_file_level_data_lock_config: _Optional[_Union[ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., audit_logging_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.AuditLoggingConfig, _Mapping]] = ..., client_subnet_whitelist_extends_global_whitelist: bool = ..., mtime_ctime_explicitly_set_only: bool = ..., enable_minion: bool = ..., view_alias_map: _Optional[_Mapping[str, ViewIdMappingProto.ViewAliasMetadata]] = ..., saved_view_alias_map: _Optional[_Mapping[str, ViewIdMappingProto.ViewAliasMetadata]] = ..., smb_config: _Optional[_Union[ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., replication_smb_config: _Optional[_Union[ViewIdMappingProto.SmbConfigProto, _Mapping]] = ..., enable_mixed_mode_permissions: bool = ..., file_extension_filter: _Optional[_Union[ViewIdMappingProto.FileExtensionFilter, _Mapping]] = ..., cache_epoch: _Optional[int] = ..., apollo_disable_namespace_fixing: bool = ..., tenant_id: _Optional[str] = ..., nfs_config: _Optional[_Union[ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., replication_nfs_config: _Optional[_Union[ViewIdMappingProto.NfsConfigProto, _Mapping]] = ..., security_mode_config: _Optional[_Union[ViewIdMappingProto.SecurityModeConfig, _Mapping]] = ..., antivirus_scan_config: _Optional[_Union[ViewIdMappingProto.AntivirusScanConfig, _Mapping]] = ..., antivirus_snap_tree_id: _Optional[int] = ..., user_view_tree_id_ceiling: _Optional[int] = ..., target_view_for_stubbing: bool = ..., external_metadata: _Optional[_Union[ViewIdMappingProto.ExternalMetadata, _Mapping]] = ..., latency_alert_params: _Optional[_Union[ViewIdMappingProto.LatencyAlertParams, _Mapping]] = ..., bookkeeper_group_id: _Optional[int] = ..., view_all_squash_uid: _Optional[int] = ..., view_all_squash_gid: _Optional[int] = ..., view_root_squash_uid: _Optional[int] = ..., view_root_squash_gid: _Optional[int] = ..., num_inode_atime_records: _Optional[int] = ..., trash_config: _Optional[_Union[ViewIdMappingProto.TrashConfig, _Mapping]] = ..., uptier_config: _Optional[_Union[ViewIdMappingProto.UptierConfig, _Mapping]] = ..., apollo_disable_orphaned_inodes_deletion: bool = ..., client_netgroup_whitelist: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.NISNetgroup, _Mapping]]] = ..., client_netgroup_whitelist_extends_global_whitelist: bool = ..., enable_live_indexing: bool = ..., performance_config: _Optional[_Union[ViewIdMappingProto.PerformanceConfig, _Mapping]] = ..., pin_config: _Optional[_Union[ViewIdMappingProto.PinConfig, _Mapping]] = ..., language_locale: _Optional[str] = ..., category: _Optional[_Union[ViewIdMappingProto.ViewCategory, str]] = ..., is_read_only: bool = ..., mixed_mode_marker: _Optional[str] = ..., snapshot_self_service_config: _Optional[_Union[ViewIdMappingProto.SnapshotSelfServiceConfig, _Mapping]] = ..., archival_info: _Optional[_Union[ViewIdMappingProto.ArchivalInfo, _Mapping]] = ..., snap_fs_accelerator_map: _Optional[_Mapping[int, ViewIdMappingProto.SnapFsAccelerator]] = ..., blur_clone_epoch_id: _Optional[int] = ..., service_auth_config: _Optional[_Union[_service_auth_config_pb2.ServiceAuthConfigProto, _Mapping]] = ..., restrict_access_to_internal: bool = ..., deprecated_restrict_access_to_internal: bool = ..., s3object_snap_tree_id: _Optional[int] = ..., blur_disabled: bool = ..., s3_folder_support_enabled: bool = ..., enable_brick_level_checksum: bool = ..., snap_fs_dir_layout: _Optional[_Union[ViewIdMappingProto.SnapFSDirectoryLayout, _Mapping]] = ..., stats_container_id: _Optional[int] = ..., saved_immutable: bool = ..., saved_blur_enabled: bool = ..., workload_attrs: _Optional[_Union[ViewIdMappingProto.WorkloadAttributes, _Mapping]] = ..., workload_type: _Optional[_Union[_request_context_pb2.WorkloadType, str]] = ..., bookkeeper_v2_group_id: _Optional[str] = ..., enable_small_dedup_chunk_creates: bool = ..., lcm_policy: _Optional[_Union[LifecyclePolicy, _Mapping]] = ...) -> None: ...

class ViewNameMappingProto(_message.Message):
    __slots__ = ("opclock_vec", "view_id", "is_alias")
    OPCLOCK_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ALIAS_FIELD_NUMBER: _ClassVar[int]
    opclock_vec: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    view_id: int
    is_alias: bool
    def __init__(self, opclock_vec: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ..., view_id: _Optional[int] = ..., is_alias: bool = ...) -> None: ...

class ViewIndicesProto(_message.Message):
    __slots__ = ("next_fragment_id", "view_index_map")
    class ViewIndexMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    NEXT_FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_INDEX_MAP_FIELD_NUMBER: _ClassVar[int]
    next_fragment_id: int
    view_index_map: _containers.ScalarMap[int, bool]
    def __init__(self, next_fragment_id: _Optional[int] = ..., view_index_map: _Optional[_Mapping[int, bool]] = ...) -> None: ...

class Template(_message.Message):
    __slots__ = ("template_id", "name", "view_id_map_proto", "template_type", "properties", "is_default", "default_template_name", "version", "protection_group_id", "smb_permissions_info", "share_permissions_info", "superusers")
    class TemplateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupTarget: _ClassVar[Template.TemplateType]
        kFileService: _ClassVar[Template.TemplateType]
        kObjectService: _ClassVar[Template.TemplateType]
        kCustom: _ClassVar[Template.TemplateType]
    kBackupTarget: Template.TemplateType
    kFileService: Template.TemplateType
    kObjectService: Template.TemplateType
    kCustom: Template.TemplateType
    class DefaultTemplateName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[Template.DefaultTemplateName]
        kBackupGeneral: _ClassVar[Template.DefaultTemplateName]
        kBackupCommvault: _ClassVar[Template.DefaultTemplateName]
        kBackupVeeam: _ClassVar[Template.DefaultTemplateName]
        kFileServiceVideos: _ClassVar[Template.DefaultTemplateName]
        kFileServiceMultimedia: _ClassVar[Template.DefaultTemplateName]
        kFileServiceArchive: _ClassVar[Template.DefaultTemplateName]
        kObjectServiceContainer: _ClassVar[Template.DefaultTemplateName]
        kZDLRA: _ClassVar[Template.DefaultTemplateName]
        kTSM: _ClassVar[Template.DefaultTemplateName]
        kApplicationsDump: _ClassVar[Template.DefaultTemplateName]
        kFileServiceGeneral: _ClassVar[Template.DefaultTemplateName]
        kDigitalArchive: _ClassVar[Template.DefaultTemplateName]
        kObjectServiceGeneral: _ClassVar[Template.DefaultTemplateName]
        kSplunkSmartStore: _ClassVar[Template.DefaultTemplateName]
        kHadoop: _ClassVar[Template.DefaultTemplateName]
        KGeneralArchive: _ClassVar[Template.DefaultTemplateName]
        kSapHana: _ClassVar[Template.DefaultTemplateName]
        kAllTemplates: _ClassVar[Template.DefaultTemplateName]
    kUnknown: Template.DefaultTemplateName
    kBackupGeneral: Template.DefaultTemplateName
    kBackupCommvault: Template.DefaultTemplateName
    kBackupVeeam: Template.DefaultTemplateName
    kFileServiceVideos: Template.DefaultTemplateName
    kFileServiceMultimedia: Template.DefaultTemplateName
    kFileServiceArchive: Template.DefaultTemplateName
    kObjectServiceContainer: Template.DefaultTemplateName
    kZDLRA: Template.DefaultTemplateName
    kTSM: Template.DefaultTemplateName
    kApplicationsDump: Template.DefaultTemplateName
    kFileServiceGeneral: Template.DefaultTemplateName
    kDigitalArchive: Template.DefaultTemplateName
    kObjectServiceGeneral: Template.DefaultTemplateName
    kSplunkSmartStore: Template.DefaultTemplateName
    kHadoop: Template.DefaultTemplateName
    KGeneralArchive: Template.DefaultTemplateName
    kSapHana: Template.DefaultTemplateName
    kAllTemplates: Template.DefaultTemplateName
    class Properties(_message.Message):
        __slots__ = ("should_dedup", "should_compress", "is_externally_triggered_backup_target")
        SHOULD_DEDUP_FIELD_NUMBER: _ClassVar[int]
        SHOULD_COMPRESS_FIELD_NUMBER: _ClassVar[int]
        IS_EXTERNALLY_TRIGGERED_BACKUP_TARGET_FIELD_NUMBER: _ClassVar[int]
        should_dedup: bool
        should_compress: bool
        is_externally_triggered_backup_target: bool
        def __init__(self, should_dedup: bool = ..., should_compress: bool = ..., is_externally_triggered_backup_target: bool = ...) -> None: ...
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_MAP_PROTO_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SMB_PERMISSIONS_INFO_FIELD_NUMBER: _ClassVar[int]
    SHARE_PERMISSIONS_INFO_FIELD_NUMBER: _ClassVar[int]
    SUPERUSERS_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    name: str
    view_id_map_proto: ViewIdMappingProto
    template_type: Template.TemplateType
    properties: Template.Properties
    is_default: bool
    default_template_name: Template.DefaultTemplateName
    version: int
    protection_group_id: str
    smb_permissions_info: _view_smb_permissions_pb2.ViewSmbPermissionsInfo
    share_permissions_info: _containers.RepeatedCompositeFieldContainer[_view_smb_permissions_pb2.SmbPermission]
    superusers: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, template_id: _Optional[int] = ..., name: _Optional[str] = ..., view_id_map_proto: _Optional[_Union[ViewIdMappingProto, _Mapping]] = ..., template_type: _Optional[_Union[Template.TemplateType, str]] = ..., properties: _Optional[_Union[Template.Properties, _Mapping]] = ..., is_default: bool = ..., default_template_name: _Optional[_Union[Template.DefaultTemplateName, str]] = ..., version: _Optional[int] = ..., protection_group_id: _Optional[str] = ..., smb_permissions_info: _Optional[_Union[_view_smb_permissions_pb2.ViewSmbPermissionsInfo, _Mapping]] = ..., share_permissions_info: _Optional[_Iterable[_Union[_view_smb_permissions_pb2.SmbPermission, _Mapping]]] = ..., superusers: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class SnapTreeInfo(_message.Message):
    __slots__ = ("tree_type", "key_type")
    class TreeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kS3ObjectSnapTree: _ClassVar[SnapTreeInfo.TreeType]
        kViewSnapTree: _ClassVar[SnapTreeInfo.TreeType]
        kBlobSnapTree: _ClassVar[SnapTreeInfo.TreeType]
    kS3ObjectSnapTree: SnapTreeInfo.TreeType
    kViewSnapTree: SnapTreeInfo.TreeType
    kBlobSnapTree: SnapTreeInfo.TreeType
    class KeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kKeyStr: _ClassVar[SnapTreeInfo.KeyType]
        kKeyInt: _ClassVar[SnapTreeInfo.KeyType]
    kKeyStr: SnapTreeInfo.KeyType
    kKeyInt: SnapTreeInfo.KeyType
    TREE_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    tree_type: SnapTreeInfo.TreeType
    key_type: SnapTreeInfo.KeyType
    def __init__(self, tree_type: _Optional[_Union[SnapTreeInfo.TreeType, str]] = ..., key_type: _Optional[_Union[SnapTreeInfo.KeyType, str]] = ...) -> None: ...
