from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.stub import rpc_common_args_pb2 as _rpc_common_args_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1
from magneto.connectors.file import file_pb2 as _file_pb2
from magneto.connectors.vmware import vmware_common_args_pb2 as _vmware_common_args_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StubType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoStub: _ClassVar[StubType.Type]
        kProxy: _ClassVar[StubType.Type]
        kSmbProxy: _ClassVar[StubType.Type]
        kMixedMode: _ClassVar[StubType.Type]
        kHybrid: _ClassVar[StubType.Type]
        kNfsProxy: _ClassVar[StubType.Type]
    kNoStub: StubType.Type
    kProxy: StubType.Type
    kSmbProxy: StubType.Type
    kMixedMode: StubType.Type
    kHybrid: StubType.Type
    kNfsProxy: StubType.Type
    def __init__(self) -> None: ...

class DiffEntity(_message.Message):
    __slots__ = ("prev_metadata", "curr_metadata", "hardlink_path", "keep_existing_snapfs_entity", "only_setattr", "rename_path", "is_renamed_to_existing_path")
    PREV_METADATA_FIELD_NUMBER: _ClassVar[int]
    CURR_METADATA_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_PATH_FIELD_NUMBER: _ClassVar[int]
    KEEP_EXISTING_SNAPFS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ONLY_SETATTR_FIELD_NUMBER: _ClassVar[int]
    RENAME_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_RENAMED_TO_EXISTING_PATH_FIELD_NUMBER: _ClassVar[int]
    prev_metadata: _directory_walker_pb2.EntityMetadata
    curr_metadata: _directory_walker_pb2.EntityMetadata
    hardlink_path: str
    keep_existing_snapfs_entity: bool
    only_setattr: bool
    rename_path: str
    is_renamed_to_existing_path: bool
    def __init__(self, prev_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., curr_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., hardlink_path: _Optional[str] = ..., keep_existing_snapfs_entity: bool = ..., only_setattr: bool = ..., rename_path: _Optional[str] = ..., is_renamed_to_existing_path: bool = ...) -> None: ...

class WorkUnit(_message.Message):
    __slots__ = ("diff_entity", "offset", "size", "is_multi_part", "set_attributes", "rename_entity", "clean_up", "move_entity", "stub_entity", "purge_all_file_handles_on_finalize")
    DIFF_ENTITY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_PART_FIELD_NUMBER: _ClassVar[int]
    SET_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RENAME_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CLEAN_UP_FIELD_NUMBER: _ClassVar[int]
    MOVE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    STUB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PURGE_ALL_FILE_HANDLES_ON_FINALIZE_FIELD_NUMBER: _ClassVar[int]
    diff_entity: DiffEntity
    offset: int
    size: int
    is_multi_part: bool
    set_attributes: bool
    rename_entity: bool
    clean_up: bool
    move_entity: bool
    stub_entity: bool
    purge_all_file_handles_on_finalize: bool
    def __init__(self, diff_entity: _Optional[_Union[DiffEntity, _Mapping]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., is_multi_part: bool = ..., set_attributes: bool = ..., rename_entity: bool = ..., clean_up: bool = ..., move_entity: bool = ..., stub_entity: bool = ..., purge_all_file_handles_on_finalize: bool = ...) -> None: ...

class BackupFileArg(_message.Message):
    __slots__ = ("type", "job_id", "job_instance_id", "attempt_num", "view_box_id", "view_box_name", "previous_view_name", "view_name", "fld_config", "is_file_data_lock_set", "view_id", "qos_principal_name", "stats_container_id", "backup_work_unit_vec", "prev_checkpoint_file_name", "uses_source_snapshot", "continue_on_error", "host_entity_id", "uses_remote_nas", "uses_smb_proxy", "connector_params", "use_case_insensitive_view", "server_snapshot_info", "remote_nas_info_map", "backup_type", "mount_username", "mount_password", "mount_encrypted_password", "mount_domain_name", "cifs_relative_path", "skip_tmp_dir_deletion", "num_tmp_dirs_per_level", "entities_in_config_to_delete", "perform_dedup_read", "min_dedup_chunk_size", "max_dedup_chunk_size", "non_dedup_chunk_size", "is_stubbing_target_view", "is_internal_view", "is_stubbing_task", "nfs_mount_path_for_stubbing", "primary_domain_name", "view_tenant_id", "migrate_without_stub", "need_checksum_verification", "hardlink_inodes_to_cleanup_map", "min_mega_file_size_mb", "sub_file_size", "uptier_config", "remote_server", "remote_path", "is_source_initiated_backup", "s3_config", "is_direct_archive_enabled", "entity_id", "kubernetes_volume_path", "enable_blur", "enable_brick_level_checksum", "smb_krb5_hostname")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupFileArg.ActionType]
        kBackupWorkUnits: _ClassVar[BackupFileArg.ActionType]
        kEndSubTask: _ClassVar[BackupFileArg.ActionType]
        kEndBackup: _ClassVar[BackupFileArg.ActionType]
        kStubbingWorkUnits: _ClassVar[BackupFileArg.ActionType]
    kPrepareBackup: BackupFileArg.ActionType
    kBackupWorkUnits: BackupFileArg.ActionType
    kEndSubTask: BackupFileArg.ActionType
    kEndBackup: BackupFileArg.ActionType
    kStubbingWorkUnits: BackupFileArg.ActionType
    class RemoteNasInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _file_pb2.RemoteNasInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_file_pb2.RemoteNasInfo, _Mapping]] = ...) -> None: ...
    class HardlinkInodesToCleanupMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_DATA_LOCK_SET_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    QOS_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    STATS_CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WORK_UNIT_VEC_FIELD_NUMBER: _ClassVar[int]
    PREV_CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    USES_SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    USES_REMOTE_NAS_FIELD_NUMBER: _ClassVar[int]
    USES_SMB_PROXY_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_CASE_INSENSITIVE_VIEW_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_USERNAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOUNT_ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CIFS_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    SKIP_TMP_DIR_DELETION_FIELD_NUMBER: _ClassVar[int]
    NUM_TMP_DIRS_PER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_IN_CONFIG_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_DEDUP_READ_FIELD_NUMBER: _ClassVar[int]
    MIN_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NON_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_STUBBING_TARGET_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_STUBBING_TASK_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_PATH_FOR_STUBBING_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_WITHOUT_STUB_FIELD_NUMBER: _ClassVar[int]
    NEED_CHECKSUM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_INODES_TO_CLEANUP_MAP_FIELD_NUMBER: _ClassVar[int]
    MIN_MEGA_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    UPTIER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_INITIATED_BACKUP_FIELD_NUMBER: _ClassVar[int]
    S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BLUR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_BRICK_LEVEL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    SMB_KRB5_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    type: BackupFileArg.ActionType
    job_id: int
    job_instance_id: int
    attempt_num: int
    view_box_id: int
    view_box_name: str
    previous_view_name: str
    view_name: str
    fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    is_file_data_lock_set: bool
    view_id: int
    qos_principal_name: str
    stats_container_id: int
    backup_work_unit_vec: _containers.RepeatedCompositeFieldContainer[WorkUnit]
    prev_checkpoint_file_name: str
    uses_source_snapshot: bool
    continue_on_error: bool
    host_entity_id: int
    uses_remote_nas: bool
    uses_smb_proxy: bool
    connector_params: _magneto_pb2.ConnectorParams
    use_case_insensitive_view: bool
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    remote_nas_info_map: _containers.MessageMap[int, _file_pb2.RemoteNasInfo]
    backup_type: _enums_pb2.NasProtocol.Type
    mount_username: str
    mount_password: str
    mount_encrypted_password: bytes
    mount_domain_name: str
    cifs_relative_path: str
    skip_tmp_dir_deletion: bool
    num_tmp_dirs_per_level: int
    entities_in_config_to_delete: _containers.RepeatedCompositeFieldContainer[_directory_walker_pb2.EntityMetadata]
    perform_dedup_read: bool
    min_dedup_chunk_size: int
    max_dedup_chunk_size: int
    non_dedup_chunk_size: int
    is_stubbing_target_view: bool
    is_internal_view: bool
    is_stubbing_task: bool
    nfs_mount_path_for_stubbing: str
    primary_domain_name: str
    view_tenant_id: str
    migrate_without_stub: bool
    need_checksum_verification: bool
    hardlink_inodes_to_cleanup_map: _containers.ScalarMap[int, bool]
    min_mega_file_size_mb: int
    sub_file_size: int
    uptier_config: _env_params_pb2_1.FileUptieringParams
    remote_server: str
    remote_path: str
    is_source_initiated_backup: bool
    s3_config: _s3_metadata_pb2.S3BucketConfigProto
    is_direct_archive_enabled: bool
    entity_id: int
    kubernetes_volume_path: str
    enable_blur: bool
    enable_brick_level_checksum: bool
    smb_krb5_hostname: str
    def __init__(self, type: _Optional[_Union[BackupFileArg.ActionType, str]] = ..., job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_box_name: _Optional[str] = ..., previous_view_name: _Optional[str] = ..., view_name: _Optional[str] = ..., fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., is_file_data_lock_set: bool = ..., view_id: _Optional[int] = ..., qos_principal_name: _Optional[str] = ..., stats_container_id: _Optional[int] = ..., backup_work_unit_vec: _Optional[_Iterable[_Union[WorkUnit, _Mapping]]] = ..., prev_checkpoint_file_name: _Optional[str] = ..., uses_source_snapshot: bool = ..., continue_on_error: bool = ..., host_entity_id: _Optional[int] = ..., uses_remote_nas: bool = ..., uses_smb_proxy: bool = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., use_case_insensitive_view: bool = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., remote_nas_info_map: _Optional[_Mapping[int, _file_pb2.RemoteNasInfo]] = ..., backup_type: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., mount_username: _Optional[str] = ..., mount_password: _Optional[str] = ..., mount_encrypted_password: _Optional[bytes] = ..., mount_domain_name: _Optional[str] = ..., cifs_relative_path: _Optional[str] = ..., skip_tmp_dir_deletion: bool = ..., num_tmp_dirs_per_level: _Optional[int] = ..., entities_in_config_to_delete: _Optional[_Iterable[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]]] = ..., perform_dedup_read: bool = ..., min_dedup_chunk_size: _Optional[int] = ..., max_dedup_chunk_size: _Optional[int] = ..., non_dedup_chunk_size: _Optional[int] = ..., is_stubbing_target_view: bool = ..., is_internal_view: bool = ..., is_stubbing_task: bool = ..., nfs_mount_path_for_stubbing: _Optional[str] = ..., primary_domain_name: _Optional[str] = ..., view_tenant_id: _Optional[str] = ..., migrate_without_stub: bool = ..., need_checksum_verification: bool = ..., hardlink_inodes_to_cleanup_map: _Optional[_Mapping[int, bool]] = ..., min_mega_file_size_mb: _Optional[int] = ..., sub_file_size: _Optional[int] = ..., uptier_config: _Optional[_Union[_env_params_pb2_1.FileUptieringParams, _Mapping]] = ..., remote_server: _Optional[str] = ..., remote_path: _Optional[str] = ..., is_source_initiated_backup: bool = ..., s3_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., is_direct_archive_enabled: bool = ..., entity_id: _Optional[int] = ..., kubernetes_volume_path: _Optional[str] = ..., enable_blur: bool = ..., enable_brick_level_checksum: bool = ..., smb_krb5_hostname: _Optional[str] = ...) -> None: ...

class RestoreFileArg(_message.Message):
    __slots__ = ("type", "restore_preferences", "view_box_id", "view_box_name", "src_view_name", "view_id", "view_flr_params", "restore_work_unit_vec", "host_entity_id", "uses_remote_nas", "nas_uptier_restore", "nas_uptier_symlink_prefix", "uses_smb_proxy", "uses_locally_mounted_virtual_disk", "disable_local_umount", "volume_info", "is_flr_test_enabled", "connector_params", "root_dirs", "use_task_id_as_key", "guest_operation_params", "vmware_params", "backup_type", "remote_nas_info_map", "remote_server", "remote_path", "restore_type", "mount_username", "mount_encrypted_password", "mount_domain_name", "directory_name_security_style_map", "curr_root_dir", "is_using_bifrost", "mount_password", "fleet_storage_proxy_ip_address", "entity_id", "smb_krb5_hostname", "mount_point_vec", "restore_from_archived_snapshot")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRestoreWorkUnits: _ClassVar[RestoreFileArg.ActionType]
        kEndSubTask: _ClassVar[RestoreFileArg.ActionType]
        kEndRestore: _ClassVar[RestoreFileArg.ActionType]
    kRestoreWorkUnits: RestoreFileArg.ActionType
    kEndSubTask: RestoreFileArg.ActionType
    kEndRestore: RestoreFileArg.ActionType
    class ViewFLRParams(_message.Message):
        __slots__ = ("should_clone_file", "dst_view_id", "dst_view_name", "dst_view_box_name")
        SHOULD_CLONE_FILE_FIELD_NUMBER: _ClassVar[int]
        DST_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        DST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        DST_VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
        should_clone_file: bool
        dst_view_id: int
        dst_view_name: str
        dst_view_box_name: str
        def __init__(self, should_clone_file: bool = ..., dst_view_id: _Optional[int] = ..., dst_view_name: _Optional[str] = ..., dst_view_box_name: _Optional[str] = ...) -> None: ...
    class VMwareParams(_message.Message):
        __slots__ = ("host_name",)
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        host_name: str
        def __init__(self, host_name: _Optional[str] = ...) -> None: ...
    class RemoteNasInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _file_pb2.RemoteNasInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_file_pb2.RemoteNasInfo, _Mapping]] = ...) -> None: ...
    class DirectoryNameSecurityStyleMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FLR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_WORK_UNIT_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    USES_REMOTE_NAS_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_RESTORE_FIELD_NUMBER: _ClassVar[int]
    NAS_UPTIER_SYMLINK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    USES_SMB_PROXY_FIELD_NUMBER: _ClassVar[int]
    USES_LOCALLY_MOUNTED_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    DISABLE_LOCAL_UMOUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_FLR_TEST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ROOT_DIRS_FIELD_NUMBER: _ClassVar[int]
    USE_TASK_ID_AS_KEY_FIELD_NUMBER: _ClassVar[int]
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_USERNAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOUNT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_NAME_SECURITY_STYLE_MAP_FIELD_NUMBER: _ClassVar[int]
    CURR_ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    IS_USING_BIFROST_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    FLEET_STORAGE_PROXY_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    SMB_KRB5_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FROM_ARCHIVED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    type: RestoreFileArg.ActionType
    restore_preferences: _magneto_pb2.RestoreFilesPreferences
    view_box_id: int
    view_box_name: str
    src_view_name: str
    view_id: int
    view_flr_params: RestoreFileArg.ViewFLRParams
    restore_work_unit_vec: _containers.RepeatedCompositeFieldContainer[WorkUnit]
    host_entity_id: int
    uses_remote_nas: bool
    nas_uptier_restore: bool
    nas_uptier_symlink_prefix: str
    uses_smb_proxy: bool
    uses_locally_mounted_virtual_disk: bool
    disable_local_umount: bool
    volume_info: _volume_info_pb2.VolumeInfo
    is_flr_test_enabled: bool
    connector_params: _magneto_pb2.ConnectorParams
    root_dirs: _containers.RepeatedScalarFieldContainer[str]
    use_task_id_as_key: bool
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    vmware_params: RestoreFileArg.VMwareParams
    backup_type: _enums_pb2.Environment.Type
    remote_nas_info_map: _containers.MessageMap[int, _file_pb2.RemoteNasInfo]
    remote_server: str
    remote_path: str
    restore_type: _enums_pb2.NasProtocol.Type
    mount_username: str
    mount_encrypted_password: bytes
    mount_domain_name: str
    directory_name_security_style_map: _containers.ScalarMap[str, str]
    curr_root_dir: str
    is_using_bifrost: bool
    mount_password: bytes
    fleet_storage_proxy_ip_address: str
    entity_id: int
    smb_krb5_hostname: str
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    restore_from_archived_snapshot: bool
    def __init__(self, type: _Optional[_Union[RestoreFileArg.ActionType, str]] = ..., restore_preferences: _Optional[_Union[_magneto_pb2.RestoreFilesPreferences, _Mapping]] = ..., view_box_id: _Optional[int] = ..., view_box_name: _Optional[str] = ..., src_view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., view_flr_params: _Optional[_Union[RestoreFileArg.ViewFLRParams, _Mapping]] = ..., restore_work_unit_vec: _Optional[_Iterable[_Union[WorkUnit, _Mapping]]] = ..., host_entity_id: _Optional[int] = ..., uses_remote_nas: bool = ..., nas_uptier_restore: bool = ..., nas_uptier_symlink_prefix: _Optional[str] = ..., uses_smb_proxy: bool = ..., uses_locally_mounted_virtual_disk: bool = ..., disable_local_umount: bool = ..., volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., is_flr_test_enabled: bool = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., root_dirs: _Optional[_Iterable[str]] = ..., use_task_id_as_key: bool = ..., guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., vmware_params: _Optional[_Union[RestoreFileArg.VMwareParams, _Mapping]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., remote_nas_info_map: _Optional[_Mapping[int, _file_pb2.RemoteNasInfo]] = ..., remote_server: _Optional[str] = ..., remote_path: _Optional[str] = ..., restore_type: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., mount_username: _Optional[str] = ..., mount_encrypted_password: _Optional[bytes] = ..., mount_domain_name: _Optional[str] = ..., directory_name_security_style_map: _Optional[_Mapping[str, str]] = ..., curr_root_dir: _Optional[str] = ..., is_using_bifrost: bool = ..., mount_password: _Optional[bytes] = ..., fleet_storage_proxy_ip_address: _Optional[str] = ..., entity_id: _Optional[int] = ..., smb_krb5_hostname: _Optional[str] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., restore_from_archived_snapshot: bool = ...) -> None: ...

class FileActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_file_arg", "restore_file_arg", "cancel_task_arg", "num_of_parallel_threads", "cancel_sub_task", "cluster_id", "cluster_incarnation_id", "is_using_bifrost", "encryption_enabled", "stub_type", "kdc")
    FILE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    file_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILE_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_PARALLEL_THREADS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_USING_BIFROST_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    KDC_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_file_arg: BackupFileArg
    restore_file_arg: RestoreFileArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    num_of_parallel_threads: int
    cancel_sub_task: bool
    cluster_id: int
    cluster_incarnation_id: int
    is_using_bifrost: bool
    encryption_enabled: bool
    stub_type: StubType.Type
    kdc: str
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_file_arg: _Optional[_Union[BackupFileArg, _Mapping]] = ..., restore_file_arg: _Optional[_Union[RestoreFileArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ..., num_of_parallel_threads: _Optional[int] = ..., cancel_sub_task: bool = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., is_using_bifrost: bool = ..., encryption_enabled: bool = ..., stub_type: _Optional[_Union[StubType.Type, str]] = ..., kdc: _Optional[str] = ...) -> None: ...

class FileBridgeActionUpdateArg(_message.Message):
    __slots__ = ("work_unit_idx", "entity_key")
    FILE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    file_action_update_arg: _descriptor.FieldDescriptor
    WORK_UNIT_IDX_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    work_unit_idx: int
    entity_key: str
    def __init__(self, work_unit_idx: _Optional[int] = ..., entity_key: _Optional[str] = ...) -> None: ...
