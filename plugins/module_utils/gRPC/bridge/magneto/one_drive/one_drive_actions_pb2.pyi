from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareBackupInfo(_message.Message):
    __slots__ = ("skip_directory_cloning", "drive_id", "create_rocks_db_dir")
    SKIP_DIRECTORY_CLONING_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ROCKS_DB_DIR_FIELD_NUMBER: _ClassVar[int]
    skip_directory_cloning: bool
    drive_id: str
    create_rocks_db_dir: bool
    def __init__(self, skip_directory_cloning: bool = ..., drive_id: _Optional[str] = ..., create_rocks_db_dir: bool = ...) -> None: ...

class SetupInfo(_message.Message):
    __slots__ = ("drive_item_change_vec", "deny_filters", "drive_id", "deny_filters_changed", "excluded_drive_item_id_vec", "send_error_on_move_operation", "close_rocks_db_handle", "create_files_during_setup", "should_trigger_full_backup", "skip_fetching_permissions", "skip_storing_inherited_permissions", "is_incremental_backup", "incremental_file_offset", "is_first_setup_info_batch", "fetch_all_permissions", "should_recon_metadata", "should_recon_data")
    DRIVE_ITEM_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    DENY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DENY_FILTERS_CHANGED_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DRIVE_ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SEND_ERROR_ON_MOVE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    CLOSE_ROCKS_DB_HANDLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_FILES_DURING_SETUP_FIELD_NUMBER: _ClassVar[int]
    SHOULD_TRIGGER_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SKIP_FETCHING_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SKIP_STORING_INHERITED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_SETUP_INFO_BATCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_ALL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECON_METADATA_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECON_DATA_FIELD_NUMBER: _ClassVar[int]
    drive_item_change_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.DriveItem]
    deny_filters: _containers.RepeatedScalarFieldContainer[str]
    drive_id: str
    deny_filters_changed: bool
    excluded_drive_item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    send_error_on_move_operation: bool
    close_rocks_db_handle: bool
    create_files_during_setup: bool
    should_trigger_full_backup: bool
    skip_fetching_permissions: bool
    skip_storing_inherited_permissions: bool
    is_incremental_backup: bool
    incremental_file_offset: int
    is_first_setup_info_batch: bool
    fetch_all_permissions: bool
    should_recon_metadata: bool
    should_recon_data: bool
    def __init__(self, drive_item_change_vec: _Optional[_Iterable[_Union[_graph_pb2.DriveItem, _Mapping]]] = ..., deny_filters: _Optional[_Iterable[str]] = ..., drive_id: _Optional[str] = ..., deny_filters_changed: bool = ..., excluded_drive_item_id_vec: _Optional[_Iterable[str]] = ..., send_error_on_move_operation: bool = ..., close_rocks_db_handle: bool = ..., create_files_during_setup: bool = ..., should_trigger_full_backup: bool = ..., skip_fetching_permissions: bool = ..., skip_storing_inherited_permissions: bool = ..., is_incremental_backup: bool = ..., incremental_file_offset: _Optional[int] = ..., is_first_setup_info_batch: bool = ..., fetch_all_permissions: bool = ..., should_recon_metadata: bool = ..., should_recon_data: bool = ...) -> None: ...

class BackupFilesInfo(_message.Message):
    __slots__ = ("user_id", "drive_id", "drive_item", "offset", "length", "check_file_integrity", "create_file_first")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CHECK_FILE_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    CREATE_FILE_FIRST_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    drive_id: str
    drive_item: _graph_pb2.DriveItem
    offset: int
    length: int
    check_file_integrity: bool
    create_file_first: bool
    def __init__(self, user_id: _Optional[str] = ..., drive_id: _Optional[str] = ..., drive_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., check_file_integrity: bool = ..., create_file_first: bool = ...) -> None: ...

class ChunkBackupFilesInfo(_message.Message):
    __slots__ = ("backup_files_info_vec", "start_index_vec")
    BACKUP_FILES_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_files_info_vec: _containers.RepeatedCompositeFieldContainer[BackupFilesInfo]
    start_index_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, backup_files_info_vec: _Optional[_Iterable[_Union[BackupFilesInfo, _Mapping]]] = ..., start_index_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class EndDataSubTaskInfo(_message.Message):
    __slots__ = ("user_id", "drive_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    drive_id: str
    def __init__(self, user_id: _Optional[str] = ..., drive_id: _Optional[str] = ...) -> None: ...

class EndMetadataSubTaskInfo(_message.Message):
    __slots__ = ("user_id", "drive_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    drive_id: str
    def __init__(self, user_id: _Optional[str] = ..., drive_id: _Optional[str] = ...) -> None: ...

class EndBackupInfo(_message.Message):
    __slots__ = ("one_drive_config", "write_config_file", "drive_id", "deleted_item_id_vec", "confirm_config_file_write", "cleanup_on_failure", "is_new_drive", "remove_failed_attempt_dirs", "fix_parent_linkage_for_deleted_items", "fast_cleanup_on_failure", "finalize_incremental_indexing_file", "should_delete_old_error_db", "mismatched_drive_item_size_vec")
    ONE_DRIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_CONFIG_FILE_WRITE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_DRIVE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FAILED_ATTEMPT_DIRS_FIELD_NUMBER: _ClassVar[int]
    FIX_PARENT_LINKAGE_FOR_DELETED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    FAST_CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_INCREMENTAL_INDEXING_FILE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DELETE_OLD_ERROR_DB_FIELD_NUMBER: _ClassVar[int]
    MISMATCHED_DRIVE_ITEM_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
    one_drive_config: _graph_pb2.OneDriveConfigFile
    write_config_file: bool
    drive_id: str
    deleted_item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    confirm_config_file_write: bool
    cleanup_on_failure: bool
    is_new_drive: bool
    remove_failed_attempt_dirs: bool
    fix_parent_linkage_for_deleted_items: bool
    fast_cleanup_on_failure: bool
    finalize_incremental_indexing_file: bool
    should_delete_old_error_db: bool
    mismatched_drive_item_size_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.MismatchedDriveItemSize]
    def __init__(self, one_drive_config: _Optional[_Union[_graph_pb2.OneDriveConfigFile, _Mapping]] = ..., write_config_file: bool = ..., drive_id: _Optional[str] = ..., deleted_item_id_vec: _Optional[_Iterable[str]] = ..., confirm_config_file_write: bool = ..., cleanup_on_failure: bool = ..., is_new_drive: bool = ..., remove_failed_attempt_dirs: bool = ..., fix_parent_linkage_for_deleted_items: bool = ..., fast_cleanup_on_failure: bool = ..., finalize_incremental_indexing_file: bool = ..., should_delete_old_error_db: bool = ..., mismatched_drive_item_size_vec: _Optional[_Iterable[_Union[_graph_pb2.MismatchedDriveItemSize, _Mapping]]] = ...) -> None: ...

class BackupOneDriveArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "user_entity", "prepare_backup_info", "setup_info", "backup_files_info", "chunk_backup_files_info", "end_backup_info", "end_data_sub_task_info", "end_metadata_sub_task_info", "one_drive_config", "write_config_file", "one_drive_config_present", "throttling_time_bins_size_string", "record_error_in_db", "backup_type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareOneDriveBackup: _ClassVar[BackupOneDriveArg.Type]
        kSetupInfo: _ClassVar[BackupOneDriveArg.Type]
        kBackupFiles: _ClassVar[BackupOneDriveArg.Type]
        kEndBackup: _ClassVar[BackupOneDriveArg.Type]
        kEndDataSubTask: _ClassVar[BackupOneDriveArg.Type]
        kEndMetadataSubTask: _ClassVar[BackupOneDriveArg.Type]
        kChunkBackupFiles: _ClassVar[BackupOneDriveArg.Type]
    kPrepareOneDriveBackup: BackupOneDriveArg.Type
    kSetupInfo: BackupOneDriveArg.Type
    kBackupFiles: BackupOneDriveArg.Type
    kEndBackup: BackupOneDriveArg.Type
    kEndDataSubTask: BackupOneDriveArg.Type
    kEndMetadataSubTask: BackupOneDriveArg.Type
    kChunkBackupFiles: BackupOneDriveArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    USER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PREPARE_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    SETUP_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BACKUP_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    END_DATA_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    END_METADATA_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_CONFIG_PRESENT_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TIME_BINS_SIZE_STRING_FIELD_NUMBER: _ClassVar[int]
    RECORD_ERROR_IN_DB_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupOneDriveArg.Type
    root_entity: _o365_pb2.Entity
    user_entity: _o365_pb2.Entity
    prepare_backup_info: PrepareBackupInfo
    setup_info: SetupInfo
    backup_files_info: _containers.RepeatedCompositeFieldContainer[BackupFilesInfo]
    chunk_backup_files_info: ChunkBackupFilesInfo
    end_backup_info: EndBackupInfo
    end_data_sub_task_info: EndDataSubTaskInfo
    end_metadata_sub_task_info: EndMetadataSubTaskInfo
    one_drive_config: _graph_pb2.OneDriveConfigFile
    write_config_file: bool
    one_drive_config_present: bool
    throttling_time_bins_size_string: str
    record_error_in_db: bool
    backup_type: _enums_pb2.ScheduledBackupType.Type
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupOneDriveArg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., user_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., prepare_backup_info: _Optional[_Union[PrepareBackupInfo, _Mapping]] = ..., setup_info: _Optional[_Union[SetupInfo, _Mapping]] = ..., backup_files_info: _Optional[_Iterable[_Union[BackupFilesInfo, _Mapping]]] = ..., chunk_backup_files_info: _Optional[_Union[ChunkBackupFilesInfo, _Mapping]] = ..., end_backup_info: _Optional[_Union[EndBackupInfo, _Mapping]] = ..., end_data_sub_task_info: _Optional[_Union[EndDataSubTaskInfo, _Mapping]] = ..., end_metadata_sub_task_info: _Optional[_Union[EndMetadataSubTaskInfo, _Mapping]] = ..., one_drive_config: _Optional[_Union[_graph_pb2.OneDriveConfigFile, _Mapping]] = ..., write_config_file: bool = ..., one_drive_config_present: bool = ..., throttling_time_bins_size_string: _Optional[str] = ..., record_error_in_db: bool = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ...) -> None: ...

class ReadDirInfo(_message.Message):
    __slots__ = ("dir_path", "last_visited_drive_item_id", "num_drive_items_to_read_in_rocksdb", "relative_dir_path")
    DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_DRIVE_ITEMS_TO_READ_IN_ROCKSDB_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    dir_path: str
    last_visited_drive_item_id: str
    num_drive_items_to_read_in_rocksdb: int
    relative_dir_path: str
    def __init__(self, dir_path: _Optional[str] = ..., last_visited_drive_item_id: _Optional[str] = ..., num_drive_items_to_read_in_rocksdb: _Optional[int] = ..., relative_dir_path: _Optional[str] = ...) -> None: ...

class RestoreFilesInfo(_message.Message):
    __slots__ = ("full_parent_folder_path", "file_name", "is_full_file_upload", "web_url", "offset", "length", "target_path", "snapfs_prefix_path", "total_full_file_length", "drive_id", "src_root_path", "is_folder", "should_permissions_restore", "restore_permission_vec", "drive_item_id", "restored_drive_item_id", "drive_item_relative_web_url", "upload_id", "deny_permission_id_vec")
    FULL_PARENT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_FILE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPFS_PREFIX_PATH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FULL_FILE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    SHOULD_PERMISSIONS_RESTORE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORED_DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_RELATIVE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    DENY_PERMISSION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    full_parent_folder_path: str
    file_name: str
    is_full_file_upload: bool
    web_url: str
    offset: int
    length: int
    target_path: str
    snapfs_prefix_path: str
    total_full_file_length: int
    drive_id: str
    src_root_path: str
    is_folder: bool
    should_permissions_restore: bool
    restore_permission_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.Permissions]
    drive_item_id: str
    restored_drive_item_id: str
    drive_item_relative_web_url: str
    upload_id: str
    deny_permission_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, full_parent_folder_path: _Optional[str] = ..., file_name: _Optional[str] = ..., is_full_file_upload: bool = ..., web_url: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., target_path: _Optional[str] = ..., snapfs_prefix_path: _Optional[str] = ..., total_full_file_length: _Optional[int] = ..., drive_id: _Optional[str] = ..., src_root_path: _Optional[str] = ..., is_folder: bool = ..., should_permissions_restore: bool = ..., restore_permission_vec: _Optional[_Iterable[_Union[_graph_pb2.Permissions, _Mapping]]] = ..., drive_item_id: _Optional[str] = ..., restored_drive_item_id: _Optional[str] = ..., drive_item_relative_web_url: _Optional[str] = ..., upload_id: _Optional[str] = ..., deny_permission_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class EndRestoreSubTaskInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndRestoreInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreOneDriveArg(_message.Message):
    __slots__ = ("base", "type", "src_root_path", "read_dir_info", "restore_files_info", "end_restore_subtask_info", "end_restore_info", "relative_drive_snapshot_path", "target_site_web_url", "sharepoint_domain_name", "is_system_drive", "source_site_web_url", "continue_on_error")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadDirInfo: _ClassVar[RestoreOneDriveArg.Type]
        kRestoreFiles: _ClassVar[RestoreOneDriveArg.Type]
        kEndRestoreSubTask: _ClassVar[RestoreOneDriveArg.Type]
        kEndRestore: _ClassVar[RestoreOneDriveArg.Type]
    kReadDirInfo: RestoreOneDriveArg.Type
    kRestoreFiles: RestoreOneDriveArg.Type
    kEndRestoreSubTask: RestoreOneDriveArg.Type
    kEndRestore: RestoreOneDriveArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    READ_DIR_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    END_RESTORE_SUBTASK_INFO_FIELD_NUMBER: _ClassVar[int]
    END_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DRIVE_SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_SITE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SITE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreOneDriveArg.Type
    src_root_path: str
    read_dir_info: ReadDirInfo
    restore_files_info: _containers.RepeatedCompositeFieldContainer[RestoreFilesInfo]
    end_restore_subtask_info: EndRestoreSubTaskInfo
    end_restore_info: EndRestoreInfo
    relative_drive_snapshot_path: str
    target_site_web_url: str
    sharepoint_domain_name: str
    is_system_drive: bool
    source_site_web_url: str
    continue_on_error: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreOneDriveArg.Type, str]] = ..., src_root_path: _Optional[str] = ..., read_dir_info: _Optional[_Union[ReadDirInfo, _Mapping]] = ..., restore_files_info: _Optional[_Iterable[_Union[RestoreFilesInfo, _Mapping]]] = ..., end_restore_subtask_info: _Optional[_Union[EndRestoreSubTaskInfo, _Mapping]] = ..., end_restore_info: _Optional[_Union[EndRestoreInfo, _Mapping]] = ..., relative_drive_snapshot_path: _Optional[str] = ..., target_site_web_url: _Optional[str] = ..., sharepoint_domain_name: _Optional[str] = ..., is_system_drive: bool = ..., source_site_web_url: _Optional[str] = ..., continue_on_error: bool = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("wait_for_cancellation", "dead_slave_constituent_id", "dead_slave_incarnation_id")
    WAIT_FOR_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    wait_for_cancellation: bool
    dead_slave_constituent_id: int
    dead_slave_incarnation_id: int
    def __init__(self, wait_for_cancellation: bool = ..., dead_slave_constituent_id: _Optional[int] = ..., dead_slave_incarnation_id: _Optional[int] = ...) -> None: ...

class OneDriveActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "drive_id", "backup_one_drive_arg", "restore_one_drive_arg", "version", "cancel_task_arg", "operation_info")
    class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kV0: _ClassVar[OneDriveActionArg.Version]
        kV1: _ClassVar[OneDriveActionArg.Version]
    kV0: OneDriveActionArg.Version
    kV1: OneDriveActionArg.Version
    ONE_DRIVE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    one_drive_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ONE_DRIVE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ONE_DRIVE_ARG_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_INFO_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    drive_id: str
    backup_one_drive_arg: BackupOneDriveArg
    restore_one_drive_arg: RestoreOneDriveArg
    version: OneDriveActionArg.Version
    cancel_task_arg: CancelTaskArg
    operation_info: _o365_pb2_1.OperationInfo
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., drive_id: _Optional[str] = ..., backup_one_drive_arg: _Optional[_Union[BackupOneDriveArg, _Mapping]] = ..., restore_one_drive_arg: _Optional[_Union[RestoreOneDriveArg, _Mapping]] = ..., version: _Optional[_Union[OneDriveActionArg.Version, str]] = ..., cancel_task_arg: _Optional[_Union[CancelTaskArg, _Mapping]] = ..., operation_info: _Optional[_Union[_o365_pb2_1.OperationInfo, _Mapping]] = ...) -> None: ...
