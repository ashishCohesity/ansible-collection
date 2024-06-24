from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.o365 import o365_pb2 as _o365_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareOneDriveBackupUpdateArg(_message.Message):
    __slots__ = ("one_drive_config_file",)
    ONE_DRIVE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    one_drive_config_file: _graph_pb2.OneDriveConfigFile
    def __init__(self, one_drive_config_file: _Optional[_Union[_graph_pb2.OneDriveConfigFile, _Mapping]] = ...) -> None: ...

class SetupInfoUpdateArg(_message.Message):
    __slots__ = ("drive_item_vec_to_backup", "total_drive_data_size", "excluded_drive_item_id_vec", "lookup_error_found", "num_skipped_items_malware", "num_skipped_items_same_ctag", "setup_info_stats", "throttling_table", "incremental_file_offset", "error_db_entry_vec", "num_skipped_permission_items")
    DRIVE_ITEM_VEC_TO_BACKUP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DRIVE_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DRIVE_ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_ERROR_FOUND_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_ITEMS_MALWARE_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_ITEMS_SAME_CTAG_FIELD_NUMBER: _ClassVar[int]
    SETUP_INFO_STATS_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TABLE_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ERROR_DB_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_PERMISSION_ITEMS_FIELD_NUMBER: _ClassVar[int]
    drive_item_vec_to_backup: _containers.RepeatedCompositeFieldContainer[_graph_pb2.DriveItem]
    total_drive_data_size: int
    excluded_drive_item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    lookup_error_found: bool
    num_skipped_items_malware: int
    num_skipped_items_same_ctag: int
    setup_info_stats: _graph_pb2.SetupInfoStats
    throttling_table: _graph_pb2.ThrottlingErrorTimeDistributionTable
    incremental_file_offset: int
    error_db_entry_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.O365ErrorDBEntry]
    num_skipped_permission_items: int
    def __init__(self, drive_item_vec_to_backup: _Optional[_Iterable[_Union[_graph_pb2.DriveItem, _Mapping]]] = ..., total_drive_data_size: _Optional[int] = ..., excluded_drive_item_id_vec: _Optional[_Iterable[str]] = ..., lookup_error_found: bool = ..., num_skipped_items_malware: _Optional[int] = ..., num_skipped_items_same_ctag: _Optional[int] = ..., setup_info_stats: _Optional[_Union[_graph_pb2.SetupInfoStats, _Mapping]] = ..., throttling_table: _Optional[_Union[_graph_pb2.ThrottlingErrorTimeDistributionTable, _Mapping]] = ..., incremental_file_offset: _Optional[int] = ..., error_db_entry_vec: _Optional[_Iterable[_Union[_graph_pb2.O365ErrorDBEntry, _Mapping]]] = ..., num_skipped_permission_items: _Optional[int] = ...) -> None: ...

class BackupFilesUpdateArg(_message.Message):
    __slots__ = ("skipped_item_ids_vec", "request_throttled", "lookup_error_found", "task_stats", "backup_disk_update_arg", "throttling_table", "num_api_calls", "request_timestamp", "dead_time_usecs", "dead_time_timestamp", "total_time_usecs", "total_time_timestamp", "error_db_entry_vec", "mismatched_drive_item_size_vec")
    class TaskStats(_message.Message):
        __slots__ = ("bytes_downloaded", "time_taken_usecs", "errored_item_info", "dead_read_time_usecs")
        class ErroredItemInfo(_message.Message):
            __slots__ = ("drive_item", "error_reason")
            DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
            ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
            drive_item: _graph_pb2.DriveItem
            error_reason: str
            def __init__(self, drive_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., error_reason: _Optional[str] = ...) -> None: ...
        BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
        ERRORED_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
        DEAD_READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        bytes_downloaded: int
        time_taken_usecs: int
        errored_item_info: BackupFilesUpdateArg.TaskStats.ErroredItemInfo
        dead_read_time_usecs: int
        def __init__(self, bytes_downloaded: _Optional[int] = ..., time_taken_usecs: _Optional[int] = ..., errored_item_info: _Optional[_Union[BackupFilesUpdateArg.TaskStats.ErroredItemInfo, _Mapping]] = ..., dead_read_time_usecs: _Optional[int] = ...) -> None: ...
    SKIPPED_ITEM_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUEST_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_ERROR_FOUND_FIELD_NUMBER: _ClassVar[int]
    TASK_STATS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TABLE_FIELD_NUMBER: _ClassVar[int]
    NUM_API_CALLS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_DB_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    MISMATCHED_DRIVE_ITEM_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
    skipped_item_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    request_throttled: bool
    lookup_error_found: bool
    task_stats: _containers.RepeatedCompositeFieldContainer[BackupFilesUpdateArg.TaskStats]
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    throttling_table: _graph_pb2.ThrottlingErrorTimeDistributionTable
    num_api_calls: _containers.RepeatedScalarFieldContainer[int]
    request_timestamp: _containers.RepeatedScalarFieldContainer[int]
    dead_time_usecs: _containers.RepeatedScalarFieldContainer[int]
    dead_time_timestamp: _containers.RepeatedScalarFieldContainer[int]
    total_time_usecs: _containers.RepeatedScalarFieldContainer[int]
    total_time_timestamp: _containers.RepeatedScalarFieldContainer[int]
    error_db_entry_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.O365ErrorDBEntry]
    mismatched_drive_item_size_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.MismatchedDriveItemSize]
    def __init__(self, skipped_item_ids_vec: _Optional[_Iterable[str]] = ..., request_throttled: bool = ..., lookup_error_found: bool = ..., task_stats: _Optional[_Iterable[_Union[BackupFilesUpdateArg.TaskStats, _Mapping]]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., throttling_table: _Optional[_Union[_graph_pb2.ThrottlingErrorTimeDistributionTable, _Mapping]] = ..., num_api_calls: _Optional[_Iterable[int]] = ..., request_timestamp: _Optional[_Iterable[int]] = ..., dead_time_usecs: _Optional[_Iterable[int]] = ..., dead_time_timestamp: _Optional[_Iterable[int]] = ..., total_time_usecs: _Optional[_Iterable[int]] = ..., total_time_timestamp: _Optional[_Iterable[int]] = ..., error_db_entry_vec: _Optional[_Iterable[_Union[_graph_pb2.O365ErrorDBEntry, _Mapping]]] = ..., mismatched_drive_item_size_vec: _Optional[_Iterable[_Union[_graph_pb2.MismatchedDriveItemSize, _Mapping]]] = ...) -> None: ...

class ChunkBackupFilesUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndMetadataSubTaskUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndDataSubTaskUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndBackupUpdateArg(_message.Message):
    __slots__ = ("num_items_deleted", "config_file_written", "is_cleanup_successful")
    NUM_ITEMS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    IS_CLEANUP_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    num_items_deleted: int
    config_file_written: bool
    is_cleanup_successful: bool
    def __init__(self, num_items_deleted: _Optional[int] = ..., config_file_written: bool = ..., is_cleanup_successful: bool = ...) -> None: ...

class ReadDirInfoUpdateArg(_message.Message):
    __slots__ = ("drive_item_vec", "root_dir", "last_visited_drive_item_id", "has_more_items", "is_file_structure_flat")
    DRIVE_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_STRUCTURE_FLAT_FIELD_NUMBER: _ClassVar[int]
    drive_item_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.DriveItem]
    root_dir: str
    last_visited_drive_item_id: str
    has_more_items: bool
    is_file_structure_flat: bool
    def __init__(self, drive_item_vec: _Optional[_Iterable[_Union[_graph_pb2.DriveItem, _Mapping]]] = ..., root_dir: _Optional[str] = ..., last_visited_drive_item_id: _Optional[str] = ..., has_more_items: bool = ..., is_file_structure_flat: bool = ...) -> None: ...

class RestoreFilesUpdateArg(_message.Message):
    __slots__ = ("web_url", "restore_disk_update_arg", "errors_encountered", "errored_file_vec", "o365_error_proto")
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    ERRORED_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    web_url: str
    restore_disk_update_arg: _stub_pb2.RestoreDiskUpdateArg
    errors_encountered: int
    errored_file_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.O365ErroredFileInfo]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, web_url: _Optional[str] = ..., restore_disk_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., errors_encountered: _Optional[int] = ..., errored_file_vec: _Optional[_Iterable[_Union[_graph_pb2.O365ErroredFileInfo, _Mapping]]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class EndRestoreSubTaskUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndRestoreUpdateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OneDriveActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_one_drive_backup_update_arg", "setup_info_update_arg", "backup_files_update_arg", "chunk_backup_files_update_arg", "end_metadata_sub_task_update_arg", "end_data_sub_task_update_arg", "end_backup_update_arg", "read_dir_info_update_arg", "restore_files_update_arg", "end_restore_sub_task_update_arg", "end_restore_update_arg", "operation_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareOneDriveBackupUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kSetupInfoUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kBackupFilesUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kEndMetadataSubTaskUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kEndDataSubTaskUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kChunkBackupFilesUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kReadDirInfoUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kRestoreFilesUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kEndRestoreSubTaskUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[OneDriveActionUpdateArg.Type]
    kPrepareOneDriveBackupUpdate: OneDriveActionUpdateArg.Type
    kSetupInfoUpdate: OneDriveActionUpdateArg.Type
    kBackupFilesUpdate: OneDriveActionUpdateArg.Type
    kEndMetadataSubTaskUpdate: OneDriveActionUpdateArg.Type
    kEndDataSubTaskUpdate: OneDriveActionUpdateArg.Type
    kEndBackupUpdate: OneDriveActionUpdateArg.Type
    kChunkBackupFilesUpdate: OneDriveActionUpdateArg.Type
    kReadDirInfoUpdate: OneDriveActionUpdateArg.Type
    kRestoreFilesUpdate: OneDriveActionUpdateArg.Type
    kEndRestoreSubTaskUpdate: OneDriveActionUpdateArg.Type
    kEndRestoreUpdate: OneDriveActionUpdateArg.Type
    ONE_DRIVE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    one_drive_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_ONE_DRIVE_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BACKUP_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_METADATA_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_DATA_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    READ_DIR_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_RESTORE_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_RESTORE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_INFO_FIELD_NUMBER: _ClassVar[int]
    type: OneDriveActionUpdateArg.Type
    prepare_one_drive_backup_update_arg: PrepareOneDriveBackupUpdateArg
    setup_info_update_arg: SetupInfoUpdateArg
    backup_files_update_arg: BackupFilesUpdateArg
    chunk_backup_files_update_arg: ChunkBackupFilesUpdateArg
    end_metadata_sub_task_update_arg: EndMetadataSubTaskUpdateArg
    end_data_sub_task_update_arg: EndDataSubTaskUpdateArg
    end_backup_update_arg: EndBackupUpdateArg
    read_dir_info_update_arg: ReadDirInfoUpdateArg
    restore_files_update_arg: RestoreFilesUpdateArg
    end_restore_sub_task_update_arg: EndRestoreSubTaskUpdateArg
    end_restore_update_arg: EndRestoreUpdateArg
    operation_info: _o365_pb2.OperationInfo
    def __init__(self, type: _Optional[_Union[OneDriveActionUpdateArg.Type, str]] = ..., prepare_one_drive_backup_update_arg: _Optional[_Union[PrepareOneDriveBackupUpdateArg, _Mapping]] = ..., setup_info_update_arg: _Optional[_Union[SetupInfoUpdateArg, _Mapping]] = ..., backup_files_update_arg: _Optional[_Union[BackupFilesUpdateArg, _Mapping]] = ..., chunk_backup_files_update_arg: _Optional[_Union[ChunkBackupFilesUpdateArg, _Mapping]] = ..., end_metadata_sub_task_update_arg: _Optional[_Union[EndMetadataSubTaskUpdateArg, _Mapping]] = ..., end_data_sub_task_update_arg: _Optional[_Union[EndDataSubTaskUpdateArg, _Mapping]] = ..., end_backup_update_arg: _Optional[_Union[EndBackupUpdateArg, _Mapping]] = ..., read_dir_info_update_arg: _Optional[_Union[ReadDirInfoUpdateArg, _Mapping]] = ..., restore_files_update_arg: _Optional[_Union[RestoreFilesUpdateArg, _Mapping]] = ..., end_restore_sub_task_update_arg: _Optional[_Union[EndRestoreSubTaskUpdateArg, _Mapping]] = ..., end_restore_update_arg: _Optional[_Union[EndRestoreUpdateArg, _Mapping]] = ..., operation_info: _Optional[_Union[_o365_pb2.OperationInfo, _Mapping]] = ...) -> None: ...
