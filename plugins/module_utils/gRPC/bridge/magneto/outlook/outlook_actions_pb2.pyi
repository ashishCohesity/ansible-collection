from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.connectors.outlook import outlook_param_pb2 as _outlook_param_pb2
from magneto.connectors.outlook import outlook_pb2 as _outlook_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareBackupInfo(_message.Message):
    __slots__ = ("skip_directory_cloning",)
    SKIP_DIRECTORY_CLONING_FIELD_NUMBER: _ClassVar[int]
    skip_directory_cloning: bool
    def __init__(self, skip_directory_cloning: bool = ...) -> None: ...

class PrepareOutlookBackupInfo(_message.Message):
    __slots__ = ("view_cloning_enabled", "should_recursively_clone_dir", "delete_entire_mailbox_dir", "dir_to_be_renamed", "first_time_view_clone")
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECURSIVELY_CLONE_DIR_FIELD_NUMBER: _ClassVar[int]
    DELETE_ENTIRE_MAILBOX_DIR_FIELD_NUMBER: _ClassVar[int]
    DIR_TO_BE_RENAMED_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIME_VIEW_CLONE_FIELD_NUMBER: _ClassVar[int]
    view_cloning_enabled: bool
    should_recursively_clone_dir: bool
    delete_entire_mailbox_dir: bool
    dir_to_be_renamed: str
    first_time_view_clone: bool
    def __init__(self, view_cloning_enabled: bool = ..., should_recursively_clone_dir: bool = ..., delete_entire_mailbox_dir: bool = ..., dir_to_be_renamed: _Optional[str] = ..., first_time_view_clone: bool = ...) -> None: ...

class CopyFailedFoldersInfo(_message.Message):
    __slots__ = ("failed_folders_vec",)
    class FolderInfo(_message.Message):
        __slots__ = ("full_snapshot_path", "folder_uuid")
        FULL_SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
        FOLDER_UUID_FIELD_NUMBER: _ClassVar[int]
        full_snapshot_path: str
        folder_uuid: str
        def __init__(self, full_snapshot_path: _Optional[str] = ..., folder_uuid: _Optional[str] = ...) -> None: ...
    FAILED_FOLDERS_VEC_FIELD_NUMBER: _ClassVar[int]
    failed_folders_vec: _containers.RepeatedCompositeFieldContainer[CopyFailedFoldersInfo.FolderInfo]
    def __init__(self, failed_folders_vec: _Optional[_Iterable[_Union[CopyFailedFoldersInfo.FolderInfo, _Mapping]]] = ...) -> None: ...

class SetupInfo(_message.Message):
    __slots__ = ("folder_info_vec", "incremental_fh_change_vec", "is_incremental_backup")
    FOLDER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FH_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    folder_info_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.SetupFolderInfo]
    incremental_fh_change_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.IncrementalFolderHierarchyChange]
    is_incremental_backup: bool
    def __init__(self, folder_info_vec: _Optional[_Iterable[_Union[_outlook_pb2.SetupFolderInfo, _Mapping]]] = ..., incremental_fh_change_vec: _Optional[_Iterable[_Union[_outlook_pb2.IncrementalFolderHierarchyChange, _Mapping]]] = ..., is_incremental_backup: bool = ...) -> None: ...

class BackupInfo(_message.Message):
    __slots__ = ("mailbox_id", "folder_id", "change_vec", "item_metadata_presence_vec", "item_body_presence_vec", "flush_after_backup", "sync_state", "already_fetched_folder_changes_result", "is_incremental_backup", "incremental_file_offset", "is_first_backup_batch", "group_owner", "public_folder_info")
    class PublicFolderInfo(_message.Message):
        __slots__ = ("public_folder_mailbox", "public_folder_mailbox_id")
        PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_FOLDER_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
        public_folder_mailbox: str
        public_folder_mailbox_id: str
        def __init__(self, public_folder_mailbox: _Optional[str] = ..., public_folder_mailbox_id: _Optional[str] = ...) -> None: ...
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    ITEM_METADATA_PRESENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    ITEM_BODY_PRESENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    FLUSH_AFTER_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    ALREADY_FETCHED_FOLDER_CHANGES_RESULT_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_BACKUP_BATCH_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_INFO_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    folder_id: str
    change_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.FolderItemChange]
    item_metadata_presence_vec: _containers.RepeatedScalarFieldContainer[bool]
    item_body_presence_vec: _containers.RepeatedScalarFieldContainer[bool]
    flush_after_backup: bool
    sync_state: str
    already_fetched_folder_changes_result: _outlook_param_pb2.GetFolderChangesResult
    is_incremental_backup: bool
    incremental_file_offset: int
    is_first_backup_batch: bool
    group_owner: str
    public_folder_info: BackupInfo.PublicFolderInfo
    def __init__(self, mailbox_id: _Optional[str] = ..., folder_id: _Optional[str] = ..., change_vec: _Optional[_Iterable[_Union[_outlook_pb2.FolderItemChange, _Mapping]]] = ..., item_metadata_presence_vec: _Optional[_Iterable[bool]] = ..., item_body_presence_vec: _Optional[_Iterable[bool]] = ..., flush_after_backup: bool = ..., sync_state: _Optional[str] = ..., already_fetched_folder_changes_result: _Optional[_Union[_outlook_param_pb2.GetFolderChangesResult, _Mapping]] = ..., is_incremental_backup: bool = ..., incremental_file_offset: _Optional[int] = ..., is_first_backup_batch: bool = ..., group_owner: _Optional[str] = ..., public_folder_info: _Optional[_Union[BackupInfo.PublicFolderInfo, _Mapping]] = ...) -> None: ...

class EndSubTaskInfo(_message.Message):
    __slots__ = ("folder_id", "relative_path", "calculate_sub_task_stat", "perform_rocksdb_validation", "is_public_folder", "write_folder_content_info", "mailbox_id", "sync_state", "cleanup_on_failure", "requires_end_externalization")
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    CALCULATE_SUB_TASK_STAT_FIELD_NUMBER: _ClassVar[int]
    PERFORM_ROCKSDB_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FOLDER_FIELD_NUMBER: _ClassVar[int]
    WRITE_FOLDER_CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_END_EXTERNALIZATION_FIELD_NUMBER: _ClassVar[int]
    folder_id: str
    relative_path: str
    calculate_sub_task_stat: bool
    perform_rocksdb_validation: bool
    is_public_folder: bool
    write_folder_content_info: bool
    mailbox_id: str
    sync_state: str
    cleanup_on_failure: bool
    requires_end_externalization: bool
    def __init__(self, folder_id: _Optional[str] = ..., relative_path: _Optional[str] = ..., calculate_sub_task_stat: bool = ..., perform_rocksdb_validation: bool = ..., is_public_folder: bool = ..., write_folder_content_info: bool = ..., mailbox_id: _Optional[str] = ..., sync_state: _Optional[str] = ..., cleanup_on_failure: bool = ..., requires_end_externalization: bool = ...) -> None: ...

class EndBackupInfo(_message.Message):
    __slots__ = ("force_write_config_file", "remove_failed_attempt_dirs", "cleanup_on_failure")
    FORCE_WRITE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FAILED_ATTEMPT_DIRS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    force_write_config_file: bool
    remove_failed_attempt_dirs: bool
    cleanup_on_failure: bool
    def __init__(self, force_write_config_file: bool = ..., remove_failed_attempt_dirs: bool = ..., cleanup_on_failure: bool = ...) -> None: ...

class BackupOutlookArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "mailbox_entity", "setup_info", "backup_info", "end_subtask_info", "mailbox_config", "write_config_file", "prepare_backup_info", "prepare_outlook_backup_info", "is_sent_from_o365_mailbox_op", "backup_info_vec", "copy_failed_folders_info", "end_backup_info", "outlook_config_absent", "record_error_in_db")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupOutlookArg.Type]
        kSetupFolders: _ClassVar[BackupOutlookArg.Type]
        kBackupItems: _ClassVar[BackupOutlookArg.Type]
        kEndSubTask: _ClassVar[BackupOutlookArg.Type]
        kEndBackup: _ClassVar[BackupOutlookArg.Type]
        kFetchBackupItems: _ClassVar[BackupOutlookArg.Type]
        kEnhancedFetchBackupItems: _ClassVar[BackupOutlookArg.Type]
        kCopyFailedFolders: _ClassVar[BackupOutlookArg.Type]
    kPrepareBackup: BackupOutlookArg.Type
    kSetupFolders: BackupOutlookArg.Type
    kBackupItems: BackupOutlookArg.Type
    kEndSubTask: BackupOutlookArg.Type
    kEndBackup: BackupOutlookArg.Type
    kFetchBackupItems: BackupOutlookArg.Type
    kEnhancedFetchBackupItems: BackupOutlookArg.Type
    kCopyFailedFolders: BackupOutlookArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SETUP_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    END_SUBTASK_INFO_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    PREPARE_OUTLOOK_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_SENT_FROM_O365_MAILBOX_OP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_FAILED_FOLDERS_INFO_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_CONFIG_ABSENT_FIELD_NUMBER: _ClassVar[int]
    RECORD_ERROR_IN_DB_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupOutlookArg.Type
    root_entity: _o365_pb2.Entity
    mailbox_entity: _o365_pb2.Entity
    setup_info: SetupInfo
    backup_info: BackupInfo
    end_subtask_info: EndSubTaskInfo
    mailbox_config: _outlook_pb2.SparseMailboxConfig
    write_config_file: bool
    prepare_backup_info: PrepareBackupInfo
    prepare_outlook_backup_info: PrepareOutlookBackupInfo
    is_sent_from_o365_mailbox_op: bool
    backup_info_vec: _containers.RepeatedCompositeFieldContainer[BackupInfo]
    copy_failed_folders_info: CopyFailedFoldersInfo
    end_backup_info: EndBackupInfo
    outlook_config_absent: bool
    record_error_in_db: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupOutlookArg.Type, str]] = ..., root_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., mailbox_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., setup_info: _Optional[_Union[SetupInfo, _Mapping]] = ..., backup_info: _Optional[_Union[BackupInfo, _Mapping]] = ..., end_subtask_info: _Optional[_Union[EndSubTaskInfo, _Mapping]] = ..., mailbox_config: _Optional[_Union[_outlook_pb2.SparseMailboxConfig, _Mapping]] = ..., write_config_file: bool = ..., prepare_backup_info: _Optional[_Union[PrepareBackupInfo, _Mapping]] = ..., prepare_outlook_backup_info: _Optional[_Union[PrepareOutlookBackupInfo, _Mapping]] = ..., is_sent_from_o365_mailbox_op: bool = ..., backup_info_vec: _Optional[_Iterable[_Union[BackupInfo, _Mapping]]] = ..., copy_failed_folders_info: _Optional[_Union[CopyFailedFoldersInfo, _Mapping]] = ..., end_backup_info: _Optional[_Union[EndBackupInfo, _Mapping]] = ..., outlook_config_absent: bool = ..., record_error_in_db: bool = ...) -> None: ...

class MailboxInfo(_message.Message):
    __slots__ = ("src_relative_path", "mailbox_entity")
    SRC_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ENTITY_FIELD_NUMBER: _ClassVar[int]
    src_relative_path: str
    mailbox_entity: _o365_pb2.Entity
    def __init__(self, src_relative_path: _Optional[str] = ..., mailbox_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("src_relative_path", "src_mailbox_entity", "src_folder_id", "item_id_vec", "last_restore_key", "dest_mailbox_entity", "dest_folder_id", "view_box_id", "src_root_path", "mailbox_id", "public_folder_mailbox", "copy_to_pst_view", "full_folder_path_on_pst_view", "folder_path", "continue_on_error", "group_smtp_address")
    SRC_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    SRC_MAILBOX_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SRC_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_RESTORE_KEY_FIELD_NUMBER: _ClassVar[int]
    DEST_MAILBOX_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DEST_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    SRC_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    COPY_TO_PST_VIEW_FIELD_NUMBER: _ClassVar[int]
    FULL_FOLDER_PATH_ON_PST_VIEW_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    GROUP_SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    src_relative_path: str
    src_mailbox_entity: _o365_pb2.Entity
    src_folder_id: str
    item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    last_restore_key: str
    dest_mailbox_entity: _o365_pb2.Entity
    dest_folder_id: str
    view_box_id: int
    src_root_path: str
    mailbox_id: str
    public_folder_mailbox: str
    copy_to_pst_view: bool
    full_folder_path_on_pst_view: str
    folder_path: str
    continue_on_error: bool
    group_smtp_address: str
    def __init__(self, src_relative_path: _Optional[str] = ..., src_mailbox_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., src_folder_id: _Optional[str] = ..., item_id_vec: _Optional[_Iterable[str]] = ..., last_restore_key: _Optional[str] = ..., dest_mailbox_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., dest_folder_id: _Optional[str] = ..., view_box_id: _Optional[int] = ..., src_root_path: _Optional[str] = ..., mailbox_id: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., copy_to_pst_view: bool = ..., full_folder_path_on_pst_view: _Optional[str] = ..., folder_path: _Optional[str] = ..., continue_on_error: bool = ..., group_smtp_address: _Optional[str] = ...) -> None: ...

class RestoreOutlookArg(_message.Message):
    __slots__ = ("base", "type", "src_root_path_vec", "mailbox_info_vec", "restore_info", "end_subtask_info", "is_alt_restore")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetMailboxInfo: _ClassVar[RestoreOutlookArg.Type]
        kRestoreItems: _ClassVar[RestoreOutlookArg.Type]
        kEndSubTask: _ClassVar[RestoreOutlookArg.Type]
        kEndRestore: _ClassVar[RestoreOutlookArg.Type]
    kGetMailboxInfo: RestoreOutlookArg.Type
    kRestoreItems: RestoreOutlookArg.Type
    kEndSubTask: RestoreOutlookArg.Type
    kEndRestore: RestoreOutlookArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_ROOT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    END_SUBTASK_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_ALT_RESTORE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreOutlookArg.Type
    src_root_path_vec: _containers.RepeatedScalarFieldContainer[str]
    mailbox_info_vec: _containers.RepeatedCompositeFieldContainer[MailboxInfo]
    restore_info: RestoreInfo
    end_subtask_info: EndSubTaskInfo
    is_alt_restore: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreOutlookArg.Type, str]] = ..., src_root_path_vec: _Optional[_Iterable[str]] = ..., mailbox_info_vec: _Optional[_Iterable[_Union[MailboxInfo, _Mapping]]] = ..., restore_info: _Optional[_Union[RestoreInfo, _Mapping]] = ..., end_subtask_info: _Optional[_Union[EndSubTaskInfo, _Mapping]] = ..., is_alt_restore: bool = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("folder_id", "wait_for_cancellation", "dead_slave_constituent_id", "dead_slave_incarnation_id")
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEAD_SLAVE_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    folder_id: str
    wait_for_cancellation: bool
    dead_slave_constituent_id: int
    dead_slave_incarnation_id: int
    def __init__(self, folder_id: _Optional[str] = ..., wait_for_cancellation: bool = ..., dead_slave_constituent_id: _Optional[int] = ..., dead_slave_incarnation_id: _Optional[int] = ...) -> None: ...

class OutlookActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_outlook_arg", "restore_outlook_arg", "cancel_task_arg", "operation_info")
    OUTLOOK_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    outlook_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_OUTLOOK_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OUTLOOK_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_INFO_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_outlook_arg: BackupOutlookArg
    restore_outlook_arg: RestoreOutlookArg
    cancel_task_arg: CancelTaskArg
    operation_info: _o365_pb2_1.OperationInfo
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_outlook_arg: _Optional[_Union[BackupOutlookArg, _Mapping]] = ..., restore_outlook_arg: _Optional[_Union[RestoreOutlookArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[CancelTaskArg, _Mapping]] = ..., operation_info: _Optional[_Union[_o365_pb2_1.OperationInfo, _Mapping]] = ...) -> None: ...
