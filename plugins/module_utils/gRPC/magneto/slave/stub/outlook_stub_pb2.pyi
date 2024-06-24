from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.connectors.outlook import outlook_pb2 as _outlook_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareMailboxBackupUpdateArg(_message.Message):
    __slots__ = ("mailbox_config",)
    MAILBOX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    mailbox_config: _outlook_pb2.SparseMailboxConfig
    def __init__(self, mailbox_config: _Optional[_Union[_outlook_pb2.SparseMailboxConfig, _Mapping]] = ...) -> None: ...

class CopyFailedFoldersUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetupFoldersUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackupFolderUpdateArg(_message.Message):
    __slots__ = ("item_ids_skipped_from_backup", "sync_state", "all_changes_fetched", "num_create_items", "num_delete_items", "num_backed_up_items", "size_backed_up_items", "incremental_file_offset", "o365_error_proto", "skipped_item_change_vec", "task_stats", "backup_disk_update_arg", "num_api_calls", "request_timestamp", "dead_time_usecs", "dead_time_timestamp", "total_time_usecs", "total_time_timestamp", "fetched_folder_changes_hashes", "fetched_folder_changes_hash_vec")
    class TaskStats(_message.Message):
        __slots__ = ("bytes_downloaded", "time_taken_usecs", "errored_item_info")
        class ErroredItemInfo(_message.Message):
            __slots__ = ("error_reason",)
            ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
            error_reason: str
            def __init__(self, error_reason: _Optional[str] = ...) -> None: ...
        BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
        ERRORED_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
        bytes_downloaded: int
        time_taken_usecs: int
        errored_item_info: BackupFolderUpdateArg.TaskStats.ErroredItemInfo
        def __init__(self, bytes_downloaded: _Optional[int] = ..., time_taken_usecs: _Optional[int] = ..., errored_item_info: _Optional[_Union[BackupFolderUpdateArg.TaskStats.ErroredItemInfo, _Mapping]] = ...) -> None: ...
    ITEM_IDS_SKIPPED_FROM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    ALL_CHANGES_FETCHED_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_ITEM_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_STATS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    NUM_API_CALLS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FETCHED_FOLDER_CHANGES_HASHES_FIELD_NUMBER: _ClassVar[int]
    FETCHED_FOLDER_CHANGES_HASH_VEC_FIELD_NUMBER: _ClassVar[int]
    item_ids_skipped_from_backup: _containers.RepeatedScalarFieldContainer[str]
    sync_state: str
    all_changes_fetched: bool
    num_create_items: int
    num_delete_items: int
    num_backed_up_items: int
    size_backed_up_items: int
    incremental_file_offset: int
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    skipped_item_change_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.FolderItemChange]
    task_stats: _containers.RepeatedCompositeFieldContainer[BackupFolderUpdateArg.TaskStats]
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    num_api_calls: _containers.RepeatedScalarFieldContainer[int]
    request_timestamp: _containers.RepeatedScalarFieldContainer[int]
    dead_time_usecs: _containers.RepeatedScalarFieldContainer[int]
    dead_time_timestamp: _containers.RepeatedScalarFieldContainer[int]
    total_time_usecs: _containers.RepeatedScalarFieldContainer[int]
    total_time_timestamp: _containers.RepeatedScalarFieldContainer[int]
    fetched_folder_changes_hashes: _containers.RepeatedScalarFieldContainer[int]
    fetched_folder_changes_hash_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, item_ids_skipped_from_backup: _Optional[_Iterable[str]] = ..., sync_state: _Optional[str] = ..., all_changes_fetched: bool = ..., num_create_items: _Optional[int] = ..., num_delete_items: _Optional[int] = ..., num_backed_up_items: _Optional[int] = ..., size_backed_up_items: _Optional[int] = ..., incremental_file_offset: _Optional[int] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., skipped_item_change_vec: _Optional[_Iterable[_Union[_outlook_pb2.FolderItemChange, _Mapping]]] = ..., task_stats: _Optional[_Iterable[_Union[BackupFolderUpdateArg.TaskStats, _Mapping]]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., num_api_calls: _Optional[_Iterable[int]] = ..., request_timestamp: _Optional[_Iterable[int]] = ..., dead_time_usecs: _Optional[_Iterable[int]] = ..., dead_time_timestamp: _Optional[_Iterable[int]] = ..., total_time_usecs: _Optional[_Iterable[int]] = ..., total_time_timestamp: _Optional[_Iterable[int]] = ..., fetched_folder_changes_hashes: _Optional[_Iterable[int]] = ..., fetched_folder_changes_hash_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class EndSubTaskUpdateArg(_message.Message):
    __slots__ = ("total_rocksdb_folder_size", "is_rocksdb_validated", "mail_count_in_folder", "is_cleanup_successful")
    TOTAL_ROCKSDB_FOLDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_ROCKSDB_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    MAIL_COUNT_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    total_rocksdb_folder_size: int
    is_rocksdb_validated: bool
    mail_count_in_folder: int
    is_cleanup_successful: bool
    def __init__(self, total_rocksdb_folder_size: _Optional[int] = ..., is_rocksdb_validated: bool = ..., mail_count_in_folder: _Optional[int] = ..., is_cleanup_successful: bool = ...) -> None: ...

class EndBackupUpdateArg(_message.Message):
    __slots__ = ("config_file_written", "is_cleanup_successful", "is_cleanup_on_failure_successful")
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_ON_FAILURE_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    config_file_written: bool
    is_cleanup_successful: bool
    is_cleanup_on_failure_successful: bool
    def __init__(self, config_file_written: bool = ..., is_cleanup_successful: bool = ..., is_cleanup_on_failure_successful: bool = ...) -> None: ...

class MailboxInfoUpdateArg(_message.Message):
    __slots__ = ("mailbox_config_vec",)
    MAILBOX_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    mailbox_config_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.SparseMailboxConfig]
    def __init__(self, mailbox_config_vec: _Optional[_Iterable[_Union[_outlook_pb2.SparseMailboxConfig, _Mapping]]] = ...) -> None: ...

class RestoreItemsUpdateArg(_message.Message):
    __slots__ = ("last_restore_key", "restore_disk_update_arg", "num_skipped_items")
    LAST_RESTORE_KEY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    last_restore_key: str
    restore_disk_update_arg: _stub_pb2.RestoreDiskUpdateArg
    num_skipped_items: int
    def __init__(self, last_restore_key: _Optional[str] = ..., restore_disk_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., num_skipped_items: _Optional[int] = ...) -> None: ...

class OutlookActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_mailbox_backup_update_arg", "setup_folders_update_arg", "backup_folder_update_arg", "end_sub_task_update_arg", "mailbox_info_update_arg", "restore_items_update_arg", "backup_folder_update_arg_vec", "copy_failed_folders_update_arg", "end_backup_update_arg", "operation_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareMailboxBackupUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kSetupFolderUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kBackupFolderUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kMailboxInfoUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kRestoreItemsUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kMultipleBackupFolderUpdate: _ClassVar[OutlookActionUpdateArg.Type]
        kCopyFailedFoldersUpdate: _ClassVar[OutlookActionUpdateArg.Type]
    kPrepareMailboxBackupUpdate: OutlookActionUpdateArg.Type
    kSetupFolderUpdate: OutlookActionUpdateArg.Type
    kBackupFolderUpdate: OutlookActionUpdateArg.Type
    kEndSubTaskUpdate: OutlookActionUpdateArg.Type
    kEndBackupUpdate: OutlookActionUpdateArg.Type
    kMailboxInfoUpdate: OutlookActionUpdateArg.Type
    kRestoreItemsUpdate: OutlookActionUpdateArg.Type
    kMultipleBackupFolderUpdate: OutlookActionUpdateArg.Type
    kCopyFailedFoldersUpdate: OutlookActionUpdateArg.Type
    OUTLOOK_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    outlook_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_MAILBOX_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_FOLDERS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FOLDER_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ITEMS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FOLDER_UPDATE_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_FAILED_FOLDERS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_INFO_FIELD_NUMBER: _ClassVar[int]
    type: OutlookActionUpdateArg.Type
    prepare_mailbox_backup_update_arg: PrepareMailboxBackupUpdateArg
    setup_folders_update_arg: SetupFoldersUpdateArg
    backup_folder_update_arg: BackupFolderUpdateArg
    end_sub_task_update_arg: EndSubTaskUpdateArg
    mailbox_info_update_arg: MailboxInfoUpdateArg
    restore_items_update_arg: RestoreItemsUpdateArg
    backup_folder_update_arg_vec: _containers.RepeatedCompositeFieldContainer[BackupFolderUpdateArg]
    copy_failed_folders_update_arg: CopyFailedFoldersUpdateArg
    end_backup_update_arg: EndBackupUpdateArg
    operation_info: _o365_pb2.OperationInfo
    def __init__(self, type: _Optional[_Union[OutlookActionUpdateArg.Type, str]] = ..., prepare_mailbox_backup_update_arg: _Optional[_Union[PrepareMailboxBackupUpdateArg, _Mapping]] = ..., setup_folders_update_arg: _Optional[_Union[SetupFoldersUpdateArg, _Mapping]] = ..., backup_folder_update_arg: _Optional[_Union[BackupFolderUpdateArg, _Mapping]] = ..., end_sub_task_update_arg: _Optional[_Union[EndSubTaskUpdateArg, _Mapping]] = ..., mailbox_info_update_arg: _Optional[_Union[MailboxInfoUpdateArg, _Mapping]] = ..., restore_items_update_arg: _Optional[_Union[RestoreItemsUpdateArg, _Mapping]] = ..., backup_folder_update_arg_vec: _Optional[_Iterable[_Union[BackupFolderUpdateArg, _Mapping]]] = ..., copy_failed_folders_update_arg: _Optional[_Union[CopyFailedFoldersUpdateArg, _Mapping]] = ..., end_backup_update_arg: _Optional[_Union[EndBackupUpdateArg, _Mapping]] = ..., operation_info: _Optional[_Union[_o365_pb2.OperationInfo, _Mapping]] = ...) -> None: ...
