from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "task_name", "task_id", "uses_parallel_diff_streamer_deprecated", "uses_source_snapshot", "server_snapshot_info", "uses_remote_nas", "continue_on_error", "uses_smb_proxy_for_file_data", "case_insensitive", "traversal_type", "sibling_order_type", "dir_walker_case_insensitive", "prev_dir_walker_stats", "curr_dir_walker_stats", "force_usec_ts_resolution", "backup_type_vec", "backup_data_protocol", "remote_nas_info_map", "logical_size", "mountpoint_dir", "cifs_relative_path", "nfs_relative_path", "possible_orphans_rocksdb_name", "rename_checkpoint_file_name", "kubernetes_volume_path", "root_dirs", "checkpoint_file_name", "skipped_checkpoint_file_name", "can_use_error_aware_checkpoint_keeper", "uses_custom_rocks_db_comparator", "status", "sub_task_vec", "max_concurrent_sub_tasks", "max_work_unit_bytes_size", "error", "error_map", "total_error_count", "diff_streamer_error_count", "sub_task_errors_count", "non_ignorable_sub_task_errors_count", "additional_entities_to_skip_vec", "unmount_remote_nas_error", "unmount_previous_snapshot_error", "disconnect_nodes_error_vec", "delete_src_snapshot_error", "delete_view_error", "diff_streamer_error", "diff_streamer_cleanup_error", "notify_backup_complete_error", "use_hardlink_sub_task", "num_tmp_dirs_per_level", "is_sub_task_scribe_state_generic", "snap_change_status", "is_snapshot_retained", "total_split_count", "is_direct_archive_enabled", "archive_job_uid", "directory_name_security_style_map", "min_mega_file_size_bytes", "sub_file_size_bytes", "incomplete_hardlink_group_info_file_name", "lazy_smb_acls_fetch_enabled", "magneto_enable_mega_file_backup", "symlink_follow_nas_target", "failed_megafile_path_map", "force_snap_fs_walk", "fld_config", "snap_change_num_entries", "uses_custom_rocks_db_comparator_for_snap_change", "use_non_batching_complete_checkpoint_keeper", "uptier_job_restore_info", "source_initiated_backup_status", "is_source_initiated_backup", "s3_config", "aggregated_tiered_bytes", "snap_change_info_rocksdb_name", "snap_change_info_cache_file_name", "snap_master_path_table_name", "snap_master_inode_table_name", "live_view_name", "remote_server", "remote_nas_path", "remote_mount_path", "hardlink_inodes_to_cleanup_map", "full_directory_walk", "indexing_policy")
    Extensions: _python_message._ExtensionDict
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kViewPrepared: _ClassVar[SnapshotInfo.Status]
        kSourceConfigured: _ClassVar[SnapshotInfo.Status]
        kSrcSnapshotCreated: _ClassVar[SnapshotInfo.Status]
        kNodesConnected: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kBridgeBackupEnded: _ClassVar[SnapshotInfo.Status]
        kNodesDisconnected: _ClassVar[SnapshotInfo.Status]
        kSrcSnapshotDeleted: _ClassVar[SnapshotInfo.Status]
        kBackupFinished: _ClassVar[SnapshotInfo.Status]
        kLiveViewCloned: _ClassVar[SnapshotInfo.Status]
        kNotifyBackupComplete: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kViewPrepared: SnapshotInfo.Status
    kSourceConfigured: SnapshotInfo.Status
    kSrcSnapshotCreated: SnapshotInfo.Status
    kNodesConnected: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kBridgeBackupEnded: SnapshotInfo.Status
    kNodesDisconnected: SnapshotInfo.Status
    kSrcSnapshotDeleted: SnapshotInfo.Status
    kBackupFinished: SnapshotInfo.Status
    kLiveViewCloned: SnapshotInfo.Status
    kNotifyBackupComplete: SnapshotInfo.Status
    class RemoteNasInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RemoteNasInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RemoteNasInfo, _Mapping]] = ...) -> None: ...
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class SnapChangeStatus(_message.Message):
        __slots__ = ("state", "error", "previous_errors_finish_line", "use_compressed_cache_file")
        class SnapChangeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[SnapshotInfo.SnapChangeStatus.SnapChangeState]
            kPreviousErrorsDone: _ClassVar[SnapshotInfo.SnapChangeStatus.SnapChangeState]
            kIngestionStarted: _ClassVar[SnapshotInfo.SnapChangeStatus.SnapChangeState]
            kIngestionDone: _ClassVar[SnapshotInfo.SnapChangeStatus.SnapChangeState]
            kPassTwoDone: _ClassVar[SnapshotInfo.SnapChangeStatus.SnapChangeState]
            kMoveSubTaskDone: _ClassVar[SnapshotInfo.SnapChangeStatus.SnapChangeState]
        kStarted: SnapshotInfo.SnapChangeStatus.SnapChangeState
        kPreviousErrorsDone: SnapshotInfo.SnapChangeStatus.SnapChangeState
        kIngestionStarted: SnapshotInfo.SnapChangeStatus.SnapChangeState
        kIngestionDone: SnapshotInfo.SnapChangeStatus.SnapChangeState
        kPassTwoDone: SnapshotInfo.SnapChangeStatus.SnapChangeState
        kMoveSubTaskDone: SnapshotInfo.SnapChangeStatus.SnapChangeState
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_ERRORS_FINISH_LINE_FIELD_NUMBER: _ClassVar[int]
        USE_COMPRESSED_CACHE_FILE_FIELD_NUMBER: _ClassVar[int]
        state: SnapshotInfo.SnapChangeStatus.SnapChangeState
        error: _error_pb2.ErrorProto
        previous_errors_finish_line: str
        use_compressed_cache_file: bool
        def __init__(self, state: _Optional[_Union[SnapshotInfo.SnapChangeStatus.SnapChangeState, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., previous_errors_finish_line: _Optional[str] = ..., use_compressed_cache_file: bool = ...) -> None: ...
    class DirectoryNameSecurityStyleMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class FailedMegafilePathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class HardlinkInodesToCleanupMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    FILE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    file_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    USES_PARALLEL_DIFF_STREAMER_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    USES_SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    USES_REMOTE_NAS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    USES_SMB_PROXY_FOR_FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
    TRAVERSAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIBLING_ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIR_WALKER_CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
    PREV_DIR_WALKER_STATS_FIELD_NUMBER: _ClassVar[int]
    CURR_DIR_WALKER_STATS_FIELD_NUMBER: _ClassVar[int]
    FORCE_USEC_TS_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DATA_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINT_DIR_FIELD_NUMBER: _ClassVar[int]
    CIFS_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    NFS_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_ORPHANS_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
    RENAME_CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
    ROOT_DIRS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_CHECKPOINT_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_USE_ERROR_AWARE_CHECKPOINT_KEEPER_FIELD_NUMBER: _ClassVar[int]
    USES_CUSTOM_ROCKS_DB_COMPARATOR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    MAX_WORK_UNIT_BYTES_SIZE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIFF_STREAMER_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    NON_IGNORABLE_SUB_TASK_ERRORS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENTITIES_TO_SKIP_VEC_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_REMOTE_NAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_PREVIOUS_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_NODES_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_SRC_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_ERROR_FIELD_NUMBER: _ClassVar[int]
    DIFF_STREAMER_ERROR_FIELD_NUMBER: _ClassVar[int]
    DIFF_STREAMER_CLEANUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_ERROR_FIELD_NUMBER: _ClassVar[int]
    USE_HARDLINK_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    NUM_TMP_DIRS_PER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_SUB_TASK_SCRIBE_STATE_GENERIC_FIELD_NUMBER: _ClassVar[int]
    SNAP_CHANGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_SNAPSHOT_RETAINED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SPLIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECT_ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_NAME_SECURITY_STYLE_MAP_FIELD_NUMBER: _ClassVar[int]
    MIN_MEGA_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_HARDLINK_GROUP_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LAZY_SMB_ACLS_FETCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ENABLE_MEGA_FILE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_FOLLOW_NAS_TARGET_FIELD_NUMBER: _ClassVar[int]
    FAILED_MEGAFILE_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    FORCE_SNAP_FS_WALK_FIELD_NUMBER: _ClassVar[int]
    FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SNAP_CHANGE_NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    USES_CUSTOM_ROCKS_DB_COMPARATOR_FOR_SNAP_CHANGE_FIELD_NUMBER: _ClassVar[int]
    USE_NON_BATCHING_COMPLETE_CHECKPOINT_KEEPER_FIELD_NUMBER: _ClassVar[int]
    UPTIER_JOB_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INITIATED_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_INITIATED_BACKUP_FIELD_NUMBER: _ClassVar[int]
    S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_TIERED_BYTES_FIELD_NUMBER: _ClassVar[int]
    SNAP_CHANGE_INFO_ROCKSDB_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAP_CHANGE_INFO_CACHE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAP_MASTER_PATH_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAP_MASTER_INODE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_INODES_TO_CLEANUP_MAP_FIELD_NUMBER: _ClassVar[int]
    FULL_DIRECTORY_WALK_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    task_name: str
    task_id: int
    uses_parallel_diff_streamer_deprecated: bool
    uses_source_snapshot: bool
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    uses_remote_nas: bool
    continue_on_error: bool
    uses_smb_proxy_for_file_data: bool
    case_insensitive: bool
    traversal_type: _directory_walker_pb2.TraversalType.Type
    sibling_order_type: _directory_walker_pb2.SiblingOrderType.Type
    dir_walker_case_insensitive: bool
    prev_dir_walker_stats: _directory_walker_pb2.DirWalkerStatsProto
    curr_dir_walker_stats: _directory_walker_pb2.DirWalkerStatsProto
    force_usec_ts_resolution: bool
    backup_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.NasProtocol.Type]
    backup_data_protocol: _enums_pb2.NasProtocol.Type
    remote_nas_info_map: _containers.MessageMap[int, RemoteNasInfo]
    logical_size: int
    mountpoint_dir: str
    cifs_relative_path: str
    nfs_relative_path: str
    possible_orphans_rocksdb_name: str
    rename_checkpoint_file_name: str
    kubernetes_volume_path: str
    root_dirs: _containers.RepeatedScalarFieldContainer[str]
    checkpoint_file_name: str
    skipped_checkpoint_file_name: str
    can_use_error_aware_checkpoint_keeper: bool
    uses_custom_rocks_db_comparator: bool
    status: SnapshotInfo.Status
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    max_concurrent_sub_tasks: int
    max_work_unit_bytes_size: int
    error: _error_pb2.ErrorProto
    error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    total_error_count: int
    diff_streamer_error_count: int
    sub_task_errors_count: int
    non_ignorable_sub_task_errors_count: int
    additional_entities_to_skip_vec: _containers.RepeatedScalarFieldContainer[str]
    unmount_remote_nas_error: _error_pb2.ErrorProto
    unmount_previous_snapshot_error: _error_pb2.ErrorProto
    disconnect_nodes_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    delete_src_snapshot_error: _error_pb2.ErrorProto
    delete_view_error: _error_pb2.ErrorProto
    diff_streamer_error: _error_pb2.ErrorProto
    diff_streamer_cleanup_error: _error_pb2.ErrorProto
    notify_backup_complete_error: _error_pb2.ErrorProto
    use_hardlink_sub_task: bool
    num_tmp_dirs_per_level: int
    is_sub_task_scribe_state_generic: bool
    snap_change_status: SnapshotInfo.SnapChangeStatus
    is_snapshot_retained: bool
    total_split_count: int
    is_direct_archive_enabled: bool
    archive_job_uid: _universal_id_pb2.UniversalIdProto
    directory_name_security_style_map: _containers.ScalarMap[str, str]
    min_mega_file_size_bytes: int
    sub_file_size_bytes: int
    incomplete_hardlink_group_info_file_name: str
    lazy_smb_acls_fetch_enabled: bool
    magneto_enable_mega_file_backup: bool
    symlink_follow_nas_target: bool
    failed_megafile_path_map: _containers.ScalarMap[str, bool]
    force_snap_fs_walk: bool
    fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    snap_change_num_entries: int
    uses_custom_rocks_db_comparator_for_snap_change: bool
    use_non_batching_complete_checkpoint_keeper: bool
    uptier_job_restore_info: RestoreFilesInfo
    source_initiated_backup_status: SourceInitiatedBackupStatus
    is_source_initiated_backup: bool
    s3_config: _s3_metadata_pb2.S3BucketConfigProto
    aggregated_tiered_bytes: int
    snap_change_info_rocksdb_name: str
    snap_change_info_cache_file_name: str
    snap_master_path_table_name: str
    snap_master_inode_table_name: str
    live_view_name: str
    remote_server: str
    remote_nas_path: str
    remote_mount_path: str
    hardlink_inodes_to_cleanup_map: _containers.ScalarMap[int, bool]
    full_directory_walk: bool
    indexing_policy: _env_params_pb2.IndexingPolicyProto
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., task_name: _Optional[str] = ..., task_id: _Optional[int] = ..., uses_parallel_diff_streamer_deprecated: bool = ..., uses_source_snapshot: bool = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., uses_remote_nas: bool = ..., continue_on_error: bool = ..., uses_smb_proxy_for_file_data: bool = ..., case_insensitive: bool = ..., traversal_type: _Optional[_Union[_directory_walker_pb2.TraversalType.Type, str]] = ..., sibling_order_type: _Optional[_Union[_directory_walker_pb2.SiblingOrderType.Type, str]] = ..., dir_walker_case_insensitive: bool = ..., prev_dir_walker_stats: _Optional[_Union[_directory_walker_pb2.DirWalkerStatsProto, _Mapping]] = ..., curr_dir_walker_stats: _Optional[_Union[_directory_walker_pb2.DirWalkerStatsProto, _Mapping]] = ..., force_usec_ts_resolution: bool = ..., backup_type_vec: _Optional[_Iterable[_Union[_enums_pb2.NasProtocol.Type, str]]] = ..., backup_data_protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., remote_nas_info_map: _Optional[_Mapping[int, RemoteNasInfo]] = ..., logical_size: _Optional[int] = ..., mountpoint_dir: _Optional[str] = ..., cifs_relative_path: _Optional[str] = ..., nfs_relative_path: _Optional[str] = ..., possible_orphans_rocksdb_name: _Optional[str] = ..., rename_checkpoint_file_name: _Optional[str] = ..., kubernetes_volume_path: _Optional[str] = ..., root_dirs: _Optional[_Iterable[str]] = ..., checkpoint_file_name: _Optional[str] = ..., skipped_checkpoint_file_name: _Optional[str] = ..., can_use_error_aware_checkpoint_keeper: bool = ..., uses_custom_rocks_db_comparator: bool = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., sub_task_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., max_concurrent_sub_tasks: _Optional[int] = ..., max_work_unit_bytes_size: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., total_error_count: _Optional[int] = ..., diff_streamer_error_count: _Optional[int] = ..., sub_task_errors_count: _Optional[int] = ..., non_ignorable_sub_task_errors_count: _Optional[int] = ..., additional_entities_to_skip_vec: _Optional[_Iterable[str]] = ..., unmount_remote_nas_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., unmount_previous_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., disconnect_nodes_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., delete_src_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_view_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., diff_streamer_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., diff_streamer_cleanup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., notify_backup_complete_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., use_hardlink_sub_task: bool = ..., num_tmp_dirs_per_level: _Optional[int] = ..., is_sub_task_scribe_state_generic: bool = ..., snap_change_status: _Optional[_Union[SnapshotInfo.SnapChangeStatus, _Mapping]] = ..., is_snapshot_retained: bool = ..., total_split_count: _Optional[int] = ..., is_direct_archive_enabled: bool = ..., archive_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., directory_name_security_style_map: _Optional[_Mapping[str, str]] = ..., min_mega_file_size_bytes: _Optional[int] = ..., sub_file_size_bytes: _Optional[int] = ..., incomplete_hardlink_group_info_file_name: _Optional[str] = ..., lazy_smb_acls_fetch_enabled: bool = ..., magneto_enable_mega_file_backup: bool = ..., symlink_follow_nas_target: bool = ..., failed_megafile_path_map: _Optional[_Mapping[str, bool]] = ..., force_snap_fs_walk: bool = ..., fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., snap_change_num_entries: _Optional[int] = ..., uses_custom_rocks_db_comparator_for_snap_change: bool = ..., use_non_batching_complete_checkpoint_keeper: bool = ..., uptier_job_restore_info: _Optional[_Union[RestoreFilesInfo, _Mapping]] = ..., source_initiated_backup_status: _Optional[_Union[SourceInitiatedBackupStatus, _Mapping]] = ..., is_source_initiated_backup: bool = ..., s3_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., aggregated_tiered_bytes: _Optional[int] = ..., snap_change_info_rocksdb_name: _Optional[str] = ..., snap_change_info_cache_file_name: _Optional[str] = ..., snap_master_path_table_name: _Optional[str] = ..., snap_master_inode_table_name: _Optional[str] = ..., live_view_name: _Optional[str] = ..., remote_server: _Optional[str] = ..., remote_nas_path: _Optional[str] = ..., remote_mount_path: _Optional[str] = ..., hardlink_inodes_to_cleanup_map: _Optional[_Mapping[int, bool]] = ..., full_directory_walk: bool = ..., indexing_policy: _Optional[_Union[_env_params_pb2.IndexingPolicyProto, _Mapping]] = ...) -> None: ...

class SourceInitiatedBackupStatus(_message.Message):
    __slots__ = ("data_movement_status", "data_movement_error", "snap_change_ingestion_status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[SourceInitiatedBackupStatus.Status]
        kInProgress: _ClassVar[SourceInitiatedBackupStatus.Status]
        kFinished: _ClassVar[SourceInitiatedBackupStatus.Status]
        kAborted: _ClassVar[SourceInitiatedBackupStatus.Status]
        kErrored: _ClassVar[SourceInitiatedBackupStatus.Status]
    kNotStarted: SourceInitiatedBackupStatus.Status
    kInProgress: SourceInitiatedBackupStatus.Status
    kFinished: SourceInitiatedBackupStatus.Status
    kAborted: SourceInitiatedBackupStatus.Status
    kErrored: SourceInitiatedBackupStatus.Status
    DATA_MOVEMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_MOVEMENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAP_CHANGE_INGESTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    data_movement_status: SourceInitiatedBackupStatus.Status
    data_movement_error: _error_pb2.ErrorProto
    snap_change_ingestion_status: SourceInitiatedBackupStatus.Status
    def __init__(self, data_movement_status: _Optional[_Union[SourceInitiatedBackupStatus.Status, str]] = ..., data_movement_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snap_change_ingestion_status: _Optional[_Union[SourceInitiatedBackupStatus.Status, str]] = ...) -> None: ...

class RemoteNasInfo(_message.Message):
    __slots__ = ("remote_server_vec", "remote_nas_path")
    REMOTE_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    remote_server_vec: _containers.RepeatedScalarFieldContainer[str]
    remote_nas_path: str
    def __init__(self, remote_server_vec: _Optional[_Iterable[str]] = ..., remote_nas_path: _Optional[str] = ...) -> None: ...

class IncompleteHardlinkGroupInfo(_message.Message):
    __slots__ = ("inode_map",)
    class InodeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    INODE_MAP_FIELD_NUMBER: _ClassVar[int]
    inode_map: _containers.ScalarMap[int, bool]
    def __init__(self, inode_map: _Optional[_Mapping[int, bool]] = ...) -> None: ...

class EntityRange(_message.Message):
    __slots__ = ("start_entity", "end_entity")
    START_ENTITY_FIELD_NUMBER: _ClassVar[int]
    END_ENTITY_FIELD_NUMBER: _ClassVar[int]
    start_entity: _directory_walker_pb2.EntityMetadata
    end_entity: _directory_walker_pb2.EntityMetadata
    def __init__(self, start_entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., end_entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ...) -> None: ...

class UptierEntityRange(_message.Message):
    __slots__ = ("start_entity_handle", "end_entity_handle")
    START_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    END_ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    start_entity_handle: _entity_handle_pb2.EntityHandleProto
    end_entity_handle: _entity_handle_pb2.EntityHandleProto
    def __init__(self, start_entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., end_entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ...) -> None: ...

class EntitiesStats(_message.Message):
    __slots__ = ("total_entities", "total_logical_size_bytes", "total_changed_entities", "total_skipped_entities", "total_bytes_to_read", "total_bytes_read", "total_changed_hardlinks")
    TOTAL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHANGED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SKIPPED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_READ_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHANGED_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
    total_entities: int
    total_logical_size_bytes: int
    total_changed_entities: int
    total_skipped_entities: int
    total_bytes_to_read: int
    total_bytes_read: int
    total_changed_hardlinks: int
    def __init__(self, total_entities: _Optional[int] = ..., total_logical_size_bytes: _Optional[int] = ..., total_changed_entities: _Optional[int] = ..., total_skipped_entities: _Optional[int] = ..., total_bytes_to_read: _Optional[int] = ..., total_bytes_read: _Optional[int] = ..., total_changed_hardlinks: _Optional[int] = ...) -> None: ...

class FileSubTaskInfo(_message.Message):
    __slots__ = ("range", "uptier_range", "remote_nas_info_map", "delete_scribe_info_error", "total_error_count", "is_move_sub_task", "is_hardlink_sub_task", "is_finished_sub_task", "entities_processed", "bytes_tiered", "is_set_attr_sub_task", "is_migrated_orphans_sub_task", "num_of_parallel_threads", "max_allowed_active_packs", "sub_task_type", "write_sub_task_idx_vec", "finalize_sub_task_idx_vec", "remote_server", "skip_finalize", "fleet_storage_proxy_ip_address", "total_non_ignorable_error_count")
    Extensions: _python_message._ExtensionDict
    class SubTaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[FileSubTaskInfo.SubTaskType]
        kCreate: _ClassVar[FileSubTaskInfo.SubTaskType]
        kWrite: _ClassVar[FileSubTaskInfo.SubTaskType]
        kFinalize: _ClassVar[FileSubTaskInfo.SubTaskType]
    kRegular: FileSubTaskInfo.SubTaskType
    kCreate: FileSubTaskInfo.SubTaskType
    kWrite: FileSubTaskInfo.SubTaskType
    kFinalize: FileSubTaskInfo.SubTaskType
    class RemoteNasInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RemoteNasInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RemoteNasInfo, _Mapping]] = ...) -> None: ...
    FILE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    file_sub_task_info: _descriptor.FieldDescriptor
    RANGE_FIELD_NUMBER: _ClassVar[int]
    UPTIER_RANGE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    DELETE_SCRIBE_INFO_ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_MOVE_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    IS_HARDLINK_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TIERED_FIELD_NUMBER: _ClassVar[int]
    IS_SET_ATTR_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATED_ORPHANS_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_PARALLEL_THREADS_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOWED_ACTIVE_PACKS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    WRITE_SUB_TASK_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_SUB_TASK_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    SKIP_FINALIZE_FIELD_NUMBER: _ClassVar[int]
    FLEET_STORAGE_PROXY_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NON_IGNORABLE_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    range: EntityRange
    uptier_range: UptierEntityRange
    remote_nas_info_map: _containers.MessageMap[int, RemoteNasInfo]
    delete_scribe_info_error: _error_pb2.ErrorProto
    total_error_count: int
    is_move_sub_task: bool
    is_hardlink_sub_task: bool
    is_finished_sub_task: bool
    entities_processed: int
    bytes_tiered: int
    is_set_attr_sub_task: bool
    is_migrated_orphans_sub_task: bool
    num_of_parallel_threads: int
    max_allowed_active_packs: int
    sub_task_type: FileSubTaskInfo.SubTaskType
    write_sub_task_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    finalize_sub_task_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    remote_server: str
    skip_finalize: bool
    fleet_storage_proxy_ip_address: str
    total_non_ignorable_error_count: int
    def __init__(self, range: _Optional[_Union[EntityRange, _Mapping]] = ..., uptier_range: _Optional[_Union[UptierEntityRange, _Mapping]] = ..., remote_nas_info_map: _Optional[_Mapping[int, RemoteNasInfo]] = ..., delete_scribe_info_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_error_count: _Optional[int] = ..., is_move_sub_task: bool = ..., is_hardlink_sub_task: bool = ..., is_finished_sub_task: bool = ..., entities_processed: _Optional[int] = ..., bytes_tiered: _Optional[int] = ..., is_set_attr_sub_task: bool = ..., is_migrated_orphans_sub_task: bool = ..., num_of_parallel_threads: _Optional[int] = ..., max_allowed_active_packs: _Optional[int] = ..., sub_task_type: _Optional[_Union[FileSubTaskInfo.SubTaskType, str]] = ..., write_sub_task_idx_vec: _Optional[_Iterable[int]] = ..., finalize_sub_task_idx_vec: _Optional[_Iterable[int]] = ..., remote_server: _Optional[str] = ..., skip_finalize: bool = ..., fleet_storage_proxy_ip_address: _Optional[str] = ..., total_non_ignorable_error_count: _Optional[int] = ...) -> None: ...

class FileSubTaskScribeInfo(_message.Message):
    __slots__ = ("finish_line_idx", "hole_idx_map", "finish_line_work_unit", "hole_info_map", "bytes_transferred", "bytes_read", "entities_processed", "bytes_tiered", "num_attributes_set", "error_map", "total_error_count", "cleanup_entity_map", "total_non_ignorable_error_count")
    class HoleIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class FinishLineWorkUnit(_message.Message):
        __slots__ = ("path", "type", "offset", "size")
        PATH_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        path: str
        type: _directory_walker_pb2.EntityMetadata.EntityType
        offset: int
        size: int
        def __init__(self, path: _Optional[str] = ..., type: _Optional[_Union[_directory_walker_pb2.EntityMetadata.EntityType, str]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
    class HoleInfo(_message.Message):
        __slots__ = ("metadata", "offset_size_map", "holes_done")
        class OffsetSizeMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int
            def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
        METADATA_FIELD_NUMBER: _ClassVar[int]
        OFFSET_SIZE_MAP_FIELD_NUMBER: _ClassVar[int]
        HOLES_DONE_FIELD_NUMBER: _ClassVar[int]
        metadata: _directory_walker_pb2.EntityMetadata
        offset_size_map: _containers.ScalarMap[int, int]
        holes_done: bool
        def __init__(self, metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., offset_size_map: _Optional[_Mapping[int, int]] = ..., holes_done: bool = ...) -> None: ...
    class HoleInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FileSubTaskScribeInfo.HoleInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FileSubTaskScribeInfo.HoleInfo, _Mapping]] = ...) -> None: ...
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class CleanupEntityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _directory_walker_pb2.EntityMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ...) -> None: ...
    FILE_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    file_sub_task_scribe_info: _descriptor.FieldDescriptor
    FINISH_LINE_IDX_FIELD_NUMBER: _ClassVar[int]
    HOLE_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    FINISH_LINE_WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    HOLE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TIERED_FIELD_NUMBER: _ClassVar[int]
    NUM_ATTRIBUTES_SET_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ENTITY_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NON_IGNORABLE_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    finish_line_idx: int
    hole_idx_map: _containers.ScalarMap[int, bool]
    finish_line_work_unit: FileSubTaskScribeInfo.FinishLineWorkUnit
    hole_info_map: _containers.MessageMap[str, FileSubTaskScribeInfo.HoleInfo]
    bytes_transferred: int
    bytes_read: int
    entities_processed: int
    bytes_tiered: int
    num_attributes_set: int
    error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    total_error_count: int
    cleanup_entity_map: _containers.MessageMap[str, _directory_walker_pb2.EntityMetadata]
    total_non_ignorable_error_count: int
    def __init__(self, finish_line_idx: _Optional[int] = ..., hole_idx_map: _Optional[_Mapping[int, bool]] = ..., finish_line_work_unit: _Optional[_Union[FileSubTaskScribeInfo.FinishLineWorkUnit, _Mapping]] = ..., hole_info_map: _Optional[_Mapping[str, FileSubTaskScribeInfo.HoleInfo]] = ..., bytes_transferred: _Optional[int] = ..., bytes_read: _Optional[int] = ..., entities_processed: _Optional[int] = ..., bytes_tiered: _Optional[int] = ..., num_attributes_set: _Optional[int] = ..., error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., total_error_count: _Optional[int] = ..., cleanup_entity_map: _Optional[_Mapping[str, _directory_walker_pb2.EntityMetadata]] = ..., total_non_ignorable_error_count: _Optional[int] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.Status]
        kCloneVolumeFinished: _ClassVar[RestoreInfo.Status]
        kMountVolumeFinished: _ClassVar[RestoreInfo.Status]
    kStarted: RestoreInfo.Status
    kCloneVolumeFinished: RestoreInfo.Status
    kMountVolumeFinished: RestoreInfo.Status
    FILE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    file_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: RestoreInfo.Status
    error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[RestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreFileCheckpoint(_message.Message):
    __slots__ = ("entities_vec", "last_diff_entity", "last_ignored_entity", "parent_entities_vec", "restore_attr_entities_vec", "restore_dirs_vec_idx", "restore_files_vec_idx", "root_entity_start_sub_task_idx")
    class Entity(_message.Message):
        __slots__ = ("src_metadata", "dst_metadata", "file_handle", "offset", "eof", "should_commit", "status")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[RestoreFileCheckpoint.Entity.Status]
            kCreated: _ClassVar[RestoreFileCheckpoint.Entity.Status]
            kDataSynced: _ClassVar[RestoreFileCheckpoint.Entity.Status]
            kFinalized: _ClassVar[RestoreFileCheckpoint.Entity.Status]
        kStarted: RestoreFileCheckpoint.Entity.Status
        kCreated: RestoreFileCheckpoint.Entity.Status
        kDataSynced: RestoreFileCheckpoint.Entity.Status
        kFinalized: RestoreFileCheckpoint.Entity.Status
        SRC_METADATA_FIELD_NUMBER: _ClassVar[int]
        DST_METADATA_FIELD_NUMBER: _ClassVar[int]
        FILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        EOF_FIELD_NUMBER: _ClassVar[int]
        SHOULD_COMMIT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        src_metadata: _directory_walker_pb2.EntityMetadata
        dst_metadata: _directory_walker_pb2.EntityMetadata
        file_handle: bytes
        offset: int
        eof: bool
        should_commit: bool
        status: RestoreFileCheckpoint.Entity.Status
        def __init__(self, src_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., dst_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., file_handle: _Optional[bytes] = ..., offset: _Optional[int] = ..., eof: bool = ..., should_commit: bool = ..., status: _Optional[_Union[RestoreFileCheckpoint.Entity.Status, str]] = ...) -> None: ...
    ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_DIFF_ENTITY_FIELD_NUMBER: _ClassVar[int]
    LAST_IGNORED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ATTR_ENTITIES_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DIRS_VEC_IDX_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_VEC_IDX_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_START_SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    entities_vec: _containers.RepeatedCompositeFieldContainer[RestoreFileCheckpoint.Entity]
    last_diff_entity: _directory_walker_pb2.EntityMetadata
    last_ignored_entity: _directory_walker_pb2.EntityMetadata
    parent_entities_vec: _containers.RepeatedCompositeFieldContainer[RestoreFileCheckpoint.Entity]
    restore_attr_entities_vec: _containers.RepeatedCompositeFieldContainer[RestoreFileCheckpoint.Entity]
    restore_dirs_vec_idx: int
    restore_files_vec_idx: int
    root_entity_start_sub_task_idx: int
    def __init__(self, entities_vec: _Optional[_Iterable[_Union[RestoreFileCheckpoint.Entity, _Mapping]]] = ..., last_diff_entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., last_ignored_entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., parent_entities_vec: _Optional[_Iterable[_Union[RestoreFileCheckpoint.Entity, _Mapping]]] = ..., restore_attr_entities_vec: _Optional[_Iterable[_Union[RestoreFileCheckpoint.Entity, _Mapping]]] = ..., restore_dirs_vec_idx: _Optional[int] = ..., restore_files_vec_idx: _Optional[int] = ..., root_entity_start_sub_task_idx: _Optional[int] = ...) -> None: ...

class RestoreFilesInfo(_message.Message):
    __slots__ = ("status", "dirs_vec", "files_vec", "checkpoint", "error_map", "total_error_count", "sub_tasks_vec", "max_concurrent_sub_tasks", "error", "base_dirs_created", "host_entity", "uses_remote_nas", "is_file_based_backup_source", "restore_type", "root_dir_prefix", "unmount_remote_nas_error", "restore_dirs_vec_idx", "restore_files_vec_idx", "root_entity_start_sub_task_idx", "max_work_unit_bytes_size", "set_attr_pass_started", "root_entity_first_set_attr_sub_task_idx", "delete_scribe_info_error", "target_agent_info", "target_agent_ip_addr", "nas_mountpoint", "disk_mountpoint_map", "is_local_storage_proxy_used", "is_view_flr", "remote_nas_info_map", "magneto_enable_mega_file_restore", "restore_min_mega_file_size_bytes", "failed_megafile_entity_map", "vmware_params", "use_entity_id_for_uptier_range", "remote_server", "remote_nas_path")
    Extensions: _python_message._ExtensionDict
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreFilesInfo.Status]
        kPreProcessingDone: _ClassVar[RestoreFilesInfo.Status]
        kViewCloned: _ClassVar[RestoreFilesInfo.Status]
        kNodesConnected: _ClassVar[RestoreFilesInfo.Status]
        kNasMounted: _ClassVar[RestoreFilesInfo.Status]
        kLocalVirtualDiskMounted: _ClassVar[RestoreFilesInfo.Status]
        kSubTasksFinished: _ClassVar[RestoreFilesInfo.Status]
        kBridgeRestoreEnded: _ClassVar[RestoreFilesInfo.Status]
        kNasUnmounted: _ClassVar[RestoreFilesInfo.Status]
        kLocalVirtualDiskUnmounted: _ClassVar[RestoreFilesInfo.Status]
        kNodesDisconnected: _ClassVar[RestoreFilesInfo.Status]
        kViewDeleted: _ClassVar[RestoreFilesInfo.Status]
        kPostProcessingDone: _ClassVar[RestoreFilesInfo.Status]
    kStarted: RestoreFilesInfo.Status
    kPreProcessingDone: RestoreFilesInfo.Status
    kViewCloned: RestoreFilesInfo.Status
    kNodesConnected: RestoreFilesInfo.Status
    kNasMounted: RestoreFilesInfo.Status
    kLocalVirtualDiskMounted: RestoreFilesInfo.Status
    kSubTasksFinished: RestoreFilesInfo.Status
    kBridgeRestoreEnded: RestoreFilesInfo.Status
    kNasUnmounted: RestoreFilesInfo.Status
    kLocalVirtualDiskUnmounted: RestoreFilesInfo.Status
    kNodesDisconnected: RestoreFilesInfo.Status
    kViewDeleted: RestoreFilesInfo.Status
    kPostProcessingDone: RestoreFilesInfo.Status
    class ErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class DiskMountpointMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RemoteNasInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RemoteNasInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RemoteNasInfo, _Mapping]] = ...) -> None: ...
    class FailedMegafileEntityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class VMwareParams(_message.Message):
        __slots__ = ("host_name",)
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        host_name: str
        def __init__(self, host_name: _Optional[str] = ...) -> None: ...
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_files_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DIRS_VEC_FIELD_NUMBER: _ClassVar[int]
    FILES_VEC_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BASE_DIRS_CREATED_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    USES_REMOTE_NAS_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_BASED_BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_DIR_PREFIX_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_REMOTE_NAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DIRS_VEC_IDX_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_VEC_IDX_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_START_SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    MAX_WORK_UNIT_BYTES_SIZE_FIELD_NUMBER: _ClassVar[int]
    SET_ATTR_PASS_STARTED_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIRST_SET_ATTR_SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    DELETE_SCRIBE_INFO_ERROR_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    NAS_MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    DISK_MOUNTPOINT_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_STORAGE_PROXY_USED_FIELD_NUMBER: _ClassVar[int]
    IS_VIEW_FLR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_ENABLE_MEGA_FILE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_MIN_MEGA_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FAILED_MEGAFILE_ENTITY_MAP_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_ENTITY_ID_FOR_UPTIER_RANGE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SERVER_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    status: RestoreFilesInfo.Status
    dirs_vec: _containers.RepeatedScalarFieldContainer[str]
    files_vec: _containers.RepeatedScalarFieldContainer[str]
    checkpoint: RestoreFileCheckpoint
    error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    total_error_count: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    max_concurrent_sub_tasks: int
    error: _error_pb2.ErrorProto
    base_dirs_created: bool
    host_entity: _entity_pb2.EntityProto
    uses_remote_nas: bool
    is_file_based_backup_source: bool
    restore_type: _enums_pb2.NasProtocol.Type
    root_dir_prefix: str
    unmount_remote_nas_error: _error_pb2.ErrorProto
    restore_dirs_vec_idx: int
    restore_files_vec_idx: int
    root_entity_start_sub_task_idx: int
    max_work_unit_bytes_size: int
    set_attr_pass_started: bool
    root_entity_first_set_attr_sub_task_idx: int
    delete_scribe_info_error: _error_pb2.ErrorProto
    target_agent_info: _agent_pb2.AgentInfoProto
    target_agent_ip_addr: str
    nas_mountpoint: str
    disk_mountpoint_map: _containers.ScalarMap[str, str]
    is_local_storage_proxy_used: bool
    is_view_flr: bool
    remote_nas_info_map: _containers.MessageMap[int, RemoteNasInfo]
    magneto_enable_mega_file_restore: bool
    restore_min_mega_file_size_bytes: int
    failed_megafile_entity_map: _containers.ScalarMap[str, bool]
    vmware_params: RestoreFilesInfo.VMwareParams
    use_entity_id_for_uptier_range: bool
    remote_server: str
    remote_nas_path: str
    def __init__(self, status: _Optional[_Union[RestoreFilesInfo.Status, str]] = ..., dirs_vec: _Optional[_Iterable[str]] = ..., files_vec: _Optional[_Iterable[str]] = ..., checkpoint: _Optional[_Union[RestoreFileCheckpoint, _Mapping]] = ..., error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., total_error_count: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., max_concurrent_sub_tasks: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., base_dirs_created: bool = ..., host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., uses_remote_nas: bool = ..., is_file_based_backup_source: bool = ..., restore_type: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., root_dir_prefix: _Optional[str] = ..., unmount_remote_nas_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_dirs_vec_idx: _Optional[int] = ..., restore_files_vec_idx: _Optional[int] = ..., root_entity_start_sub_task_idx: _Optional[int] = ..., max_work_unit_bytes_size: _Optional[int] = ..., set_attr_pass_started: bool = ..., root_entity_first_set_attr_sub_task_idx: _Optional[int] = ..., delete_scribe_info_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., target_agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., target_agent_ip_addr: _Optional[str] = ..., nas_mountpoint: _Optional[str] = ..., disk_mountpoint_map: _Optional[_Mapping[str, str]] = ..., is_local_storage_proxy_used: bool = ..., is_view_flr: bool = ..., remote_nas_info_map: _Optional[_Mapping[int, RemoteNasInfo]] = ..., magneto_enable_mega_file_restore: bool = ..., restore_min_mega_file_size_bytes: _Optional[int] = ..., failed_megafile_entity_map: _Optional[_Mapping[str, bool]] = ..., vmware_params: _Optional[_Union[RestoreFilesInfo.VMwareParams, _Mapping]] = ..., use_entity_id_for_uptier_range: bool = ..., remote_server: _Optional[str] = ..., remote_nas_path: _Optional[str] = ...) -> None: ...

class DirectoryInfo(_message.Message):
    __slots__ = ("entity", "error")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entity: _directory_walker_pb2.EntityMetadata
    error: _error_pb2.ErrorProto
    def __init__(self, entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreScribeInfo(_message.Message):
    __slots__ = ("finish_line_row", "setattr_holes_map")
    class FinishLineScribeRow(_message.Message):
        __slots__ = ("key",)
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: bytes
        def __init__(self, key: _Optional[bytes] = ...) -> None: ...
    class SetattrHolesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    FILE_RESTORE_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    file_restore_scribe_info: _descriptor.FieldDescriptor
    FINISH_LINE_ROW_FIELD_NUMBER: _ClassVar[int]
    SETATTR_HOLES_MAP_FIELD_NUMBER: _ClassVar[int]
    finish_line_row: RestoreScribeInfo.FinishLineScribeRow
    setattr_holes_map: _containers.ScalarMap[str, bool]
    def __init__(self, finish_line_row: _Optional[_Union[RestoreScribeInfo.FinishLineScribeRow, _Mapping]] = ..., setattr_holes_map: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ("error_list",)
    FILE_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    file_snapshot_scribe_info: _descriptor.FieldDescriptor
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class ChangeEntryProto(_message.Message):
    __slots__ = ("path", "prev_metadata", "curr_metadata", "is_prev_move_src", "is_curr_move_dst", "is_error_entry", "is_del_bit_set")
    Extensions: _python_message._ExtensionDict
    PATH_FIELD_NUMBER: _ClassVar[int]
    PREV_METADATA_FIELD_NUMBER: _ClassVar[int]
    CURR_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_PREV_MOVE_SRC_FIELD_NUMBER: _ClassVar[int]
    IS_CURR_MOVE_DST_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_ENTRY_FIELD_NUMBER: _ClassVar[int]
    IS_DEL_BIT_SET_FIELD_NUMBER: _ClassVar[int]
    path: str
    prev_metadata: _directory_walker_pb2.EntityMetadata
    curr_metadata: _directory_walker_pb2.EntityMetadata
    is_prev_move_src: bool
    is_curr_move_dst: bool
    is_error_entry: bool
    is_del_bit_set: bool
    def __init__(self, path: _Optional[str] = ..., prev_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., curr_metadata: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., is_prev_move_src: bool = ..., is_curr_move_dst: bool = ..., is_error_entry: bool = ..., is_del_bit_set: bool = ...) -> None: ...

class SnapChangeInfoCacheProto(_message.Message):
    __slots__ = ("changed_hardlink_map", "hardlink_group_map", "move_operation_vec", "pass_two_finish_line", "num_change_entries", "curr_num_snap_change_entries_phase1", "total_num_snap_change_entries")
    Extensions: _python_message._ExtensionDict
    class ChangedHardlinkMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class HardlinkGroupInfo(_message.Message):
        __slots__ = ("existing_path", "num_new_links", "num_all_links", "first_path_seen")
        EXISTING_PATH_FIELD_NUMBER: _ClassVar[int]
        NUM_NEW_LINKS_FIELD_NUMBER: _ClassVar[int]
        NUM_ALL_LINKS_FIELD_NUMBER: _ClassVar[int]
        FIRST_PATH_SEEN_FIELD_NUMBER: _ClassVar[int]
        existing_path: str
        num_new_links: int
        num_all_links: int
        first_path_seen: str
        def __init__(self, existing_path: _Optional[str] = ..., num_new_links: _Optional[int] = ..., num_all_links: _Optional[int] = ..., first_path_seen: _Optional[str] = ...) -> None: ...
    class HardlinkGroupMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SnapChangeInfoCacheProto.HardlinkGroupInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SnapChangeInfoCacheProto.HardlinkGroupInfo, _Mapping]] = ...) -> None: ...
    class MoveInfo(_message.Message):
        __slots__ = ("src_path", "dst_path", "type")
        SRC_PATH_FIELD_NUMBER: _ClassVar[int]
        DST_PATH_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        src_path: str
        dst_path: str
        type: _directory_walker_pb2.EntityMetadata.EntityType
        def __init__(self, src_path: _Optional[str] = ..., dst_path: _Optional[str] = ..., type: _Optional[_Union[_directory_walker_pb2.EntityMetadata.EntityType, str]] = ...) -> None: ...
    CHANGED_HARDLINK_MAP_FIELD_NUMBER: _ClassVar[int]
    HARDLINK_GROUP_MAP_FIELD_NUMBER: _ClassVar[int]
    MOVE_OPERATION_VEC_FIELD_NUMBER: _ClassVar[int]
    PASS_TWO_FINISH_LINE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHANGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    CURR_NUM_SNAP_CHANGE_ENTRIES_PHASE1_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_SNAP_CHANGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    changed_hardlink_map: _containers.ScalarMap[str, bool]
    hardlink_group_map: _containers.MessageMap[int, SnapChangeInfoCacheProto.HardlinkGroupInfo]
    move_operation_vec: _containers.RepeatedCompositeFieldContainer[SnapChangeInfoCacheProto.MoveInfo]
    pass_two_finish_line: str
    num_change_entries: int
    curr_num_snap_change_entries_phase1: int
    total_num_snap_change_entries: int
    def __init__(self, changed_hardlink_map: _Optional[_Mapping[str, bool]] = ..., hardlink_group_map: _Optional[_Mapping[int, SnapChangeInfoCacheProto.HardlinkGroupInfo]] = ..., move_operation_vec: _Optional[_Iterable[_Union[SnapChangeInfoCacheProto.MoveInfo, _Mapping]]] = ..., pass_two_finish_line: _Optional[str] = ..., num_change_entries: _Optional[int] = ..., curr_num_snap_change_entries_phase1: _Optional[int] = ..., total_num_snap_change_entries: _Optional[int] = ...) -> None: ...
