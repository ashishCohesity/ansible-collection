from magneto.agents.windows.o365spo import o365spo_pb2 as _o365spo_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.ms_graph import graph_enums_pb2 as _graph_enums_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.connectors.outlook import outlook_pb2 as _outlook_pb2
from magneto.connectors.outlook import outlook_external_pb2 as _outlook_external_pb2
from magneto.connectors.sharepoint import sharepoint_pb2 as _sharepoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("outlook_snapshot_vec", "one_drive_snapshot_vec", "status", "job_instance_id", "attempt_num", "error", "is_flat_file_structure", "o365_error_proto_deprecated", "o365_error_proto", "is_user_level_entity", "granular_progress_monitor_creation_disabled", "use_magneto_o365_onedrive_v2_subtask", "use_dummy_mailbox_guid", "onedrive_skip_clone_data", "prev_status", "prev_state_start_time", "application_id", "mailbox_start_limited_subtasks", "onedrive_start_limited_subtasks", "application_ids_permit_scaling_enabled", "is_onedrive_incremental_indexing_enabled", "chats_snapshot_info_proto", "chats_backup_allowed")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kPermitGranted: _ClassVar[SnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[SnapshotInfo.Status]
        kBackupFinished: _ClassVar[SnapshotInfo.Status]
        kDriveListFetched: _ClassVar[SnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kPermitGranted: SnapshotInfo.Status
    kProgressMonitorsCreated: SnapshotInfo.Status
    kBackupFinished: SnapshotInfo.Status
    kDriveListFetched: SnapshotInfo.Status
    kPrepareBackupDone: SnapshotInfo.Status
    class OutlookSnapshot(_message.Message):
        __slots__ = ("mailbox_id", "outlook_snapshot_info_proto")
        MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
        OUTLOOK_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        mailbox_id: str
        outlook_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        def __init__(self, mailbox_id: _Optional[str] = ..., outlook_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ...) -> None: ...
    class OneDriveSnapshot(_message.Message):
        __slots__ = ("drive_id", "one_drive_snapshot_info_proto", "drive_type")
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        ONE_DRIVE_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        drive_id: str
        one_drive_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        drive_type: _graph_enums_pb2.DriveType.Type
        def __init__(self, drive_id: _Optional[str] = ..., one_drive_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ...) -> None: ...
    O365_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    o365_snapshot_info: _descriptor.FieldDescriptor
    OUTLOOK_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_FLAT_FILE_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    IS_USER_LEVEL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GRANULAR_PROGRESS_MONITOR_CREATION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    USE_MAGNETO_O365_ONEDRIVE_V2_SUBTASK_FIELD_NUMBER: _ClassVar[int]
    USE_DUMMY_MAILBOX_GUID_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_SKIP_CLONE_DATA_FIELD_NUMBER: _ClassVar[int]
    PREV_STATUS_FIELD_NUMBER: _ClassVar[int]
    PREV_STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_START_LIMITED_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_START_LIMITED_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_PERMIT_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_ONEDRIVE_INCREMENTAL_INDEXING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHATS_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    CHATS_BACKUP_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    outlook_snapshot_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.OutlookSnapshot]
    one_drive_snapshot_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.OneDriveSnapshot]
    status: SnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    error: _error_pb2.ErrorProto
    is_flat_file_structure: bool
    o365_error_proto_deprecated: _o365_error_pb2.O365ErrorProto
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    is_user_level_entity: bool
    granular_progress_monitor_creation_disabled: bool
    use_magneto_o365_onedrive_v2_subtask: bool
    use_dummy_mailbox_guid: bool
    onedrive_skip_clone_data: bool
    prev_status: SnapshotInfo.Status
    prev_state_start_time: int
    application_id: str
    mailbox_start_limited_subtasks: bool
    onedrive_start_limited_subtasks: bool
    application_ids_permit_scaling_enabled: bool
    is_onedrive_incremental_indexing_enabled: bool
    chats_snapshot_info_proto: ChatsSnapshotInfo
    chats_backup_allowed: bool
    def __init__(self, outlook_snapshot_vec: _Optional[_Iterable[_Union[SnapshotInfo.OutlookSnapshot, _Mapping]]] = ..., one_drive_snapshot_vec: _Optional[_Iterable[_Union[SnapshotInfo.OneDriveSnapshot, _Mapping]]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_flat_file_structure: bool = ..., o365_error_proto_deprecated: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., is_user_level_entity: bool = ..., granular_progress_monitor_creation_disabled: bool = ..., use_magneto_o365_onedrive_v2_subtask: bool = ..., use_dummy_mailbox_guid: bool = ..., onedrive_skip_clone_data: bool = ..., prev_status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., prev_state_start_time: _Optional[int] = ..., application_id: _Optional[str] = ..., mailbox_start_limited_subtasks: bool = ..., onedrive_start_limited_subtasks: bool = ..., application_ids_permit_scaling_enabled: bool = ..., is_onedrive_incremental_indexing_enabled: bool = ..., chats_snapshot_info_proto: _Optional[_Union[ChatsSnapshotInfo, _Mapping]] = ..., chats_backup_allowed: bool = ...) -> None: ...

class SharepointSparseConfig(_message.Message):
    __slots__ = ("drive_info_vec", "site_admin_user_vec")
    class DriveInfo(_message.Message):
        __slots__ = ("drive_id", "drive_name", "is_system_drive", "o365_error_proto", "drive_type")
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_SYSTEM_DRIVE_FIELD_NUMBER: _ClassVar[int]
        O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        drive_id: str
        drive_name: str
        is_system_drive: bool
        o365_error_proto: _o365_error_pb2.O365ErrorProto
        drive_type: _graph_enums_pb2.DriveType.Type
        def __init__(self, drive_id: _Optional[str] = ..., drive_name: _Optional[str] = ..., is_system_drive: bool = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ...) -> None: ...
    DRIVE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SITE_ADMIN_USER_VEC_FIELD_NUMBER: _ClassVar[int]
    drive_info_vec: _containers.RepeatedCompositeFieldContainer[SharepointSparseConfig.DriveInfo]
    site_admin_user_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    def __init__(self, drive_info_vec: _Optional[_Iterable[_Union[SharepointSparseConfig.DriveInfo, _Mapping]]] = ..., site_admin_user_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ...) -> None: ...

class SharepointSnapshotInfo(_message.Message):
    __slots__ = ("site_drive_snapshot_vec", "status", "job_instance_id", "attempt_num", "error", "site_list_snapshot_info_proto", "prev_sharepoint_config", "curr_sharepoint_config", "config_file_written", "request_throttled", "template_snapshot_info", "site_not_found", "site_id", "o365_error_proto", "total_bytes_read", "total_bytes_to_transfer", "total_logical_backup_size_in_bytes", "use_magneto_o365_onedrive_v2_subtask", "site_checksum", "sharepoint_data_stats", "file_data_distribution_table", "throttling_time_distribution_table", "prev_status", "prev_state_start_time", "fast_cleanup_enabled", "application_ids_permit_scaling_enabled", "site_template_backup_skipped", "should_backup_sp_lists", "doclib_start_limited_subtasks")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SharepointSnapshotInfo.Status]
        kSiteDriveListFetched: _ClassVar[SharepointSnapshotInfo.Status]
        kPermitGranted: _ClassVar[SharepointSnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[SharepointSnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[SharepointSnapshotInfo.Status]
        kBackupFinished: _ClassVar[SharepointSnapshotInfo.Status]
    kStarted: SharepointSnapshotInfo.Status
    kSiteDriveListFetched: SharepointSnapshotInfo.Status
    kPermitGranted: SharepointSnapshotInfo.Status
    kPrepareBackupDone: SharepointSnapshotInfo.Status
    kProgressMonitorsCreated: SharepointSnapshotInfo.Status
    kBackupFinished: SharepointSnapshotInfo.Status
    class SiteDriveSnapshot(_message.Message):
        __slots__ = ("drive_id", "site_drive_snapshot_info_proto", "trigger_full_backup", "drive_name", "drive_type")
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        SITE_DRIVE_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
        DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
        drive_id: str
        site_drive_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        trigger_full_backup: bool
        drive_name: str
        drive_type: _graph_enums_pb2.DriveType.Type
        def __init__(self, drive_id: _Optional[str] = ..., site_drive_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., trigger_full_backup: bool = ..., drive_name: _Optional[str] = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ...) -> None: ...
    SHAREPOINT_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    sharepoint_snapshot_info: _descriptor.FieldDescriptor
    SITE_DRIVE_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SITE_LIST_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    PREV_SHAREPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CURR_SHAREPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SITE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BACKUP_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    USE_MAGNETO_O365_ONEDRIVE_V2_SUBTASK_FIELD_NUMBER: _ClassVar[int]
    SITE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_DISTRIBUTION_TABLE_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TIME_DISTRIBUTION_TABLE_FIELD_NUMBER: _ClassVar[int]
    PREV_STATUS_FIELD_NUMBER: _ClassVar[int]
    PREV_STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    FAST_CLEANUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_PERMIT_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SITE_TEMPLATE_BACKUP_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BACKUP_SP_LISTS_FIELD_NUMBER: _ClassVar[int]
    DOCLIB_START_LIMITED_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    site_drive_snapshot_vec: _containers.RepeatedCompositeFieldContainer[SharepointSnapshotInfo.SiteDriveSnapshot]
    status: SharepointSnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    error: _error_pb2.ErrorProto
    site_list_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
    prev_sharepoint_config: SharepointSparseConfig
    curr_sharepoint_config: SharepointSparseConfig
    config_file_written: bool
    request_throttled: bool
    template_snapshot_info: SharepointTemplateSnapshotInfo
    site_not_found: bool
    site_id: str
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    total_bytes_read: int
    total_bytes_to_transfer: int
    total_logical_backup_size_in_bytes: int
    use_magneto_o365_onedrive_v2_subtask: bool
    site_checksum: str
    sharepoint_data_stats: _graph_pb2.SharepointDataStats
    file_data_distribution_table: _graph_pb2.DataDistributionTable
    throttling_time_distribution_table: _graph_pb2.ThrottlingErrorTimeDistributionTable
    prev_status: SharepointSnapshotInfo.Status
    prev_state_start_time: int
    fast_cleanup_enabled: bool
    application_ids_permit_scaling_enabled: bool
    site_template_backup_skipped: bool
    should_backup_sp_lists: bool
    doclib_start_limited_subtasks: bool
    def __init__(self, site_drive_snapshot_vec: _Optional[_Iterable[_Union[SharepointSnapshotInfo.SiteDriveSnapshot, _Mapping]]] = ..., status: _Optional[_Union[SharepointSnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., site_list_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., prev_sharepoint_config: _Optional[_Union[SharepointSparseConfig, _Mapping]] = ..., curr_sharepoint_config: _Optional[_Union[SharepointSparseConfig, _Mapping]] = ..., config_file_written: bool = ..., request_throttled: bool = ..., template_snapshot_info: _Optional[_Union[SharepointTemplateSnapshotInfo, _Mapping]] = ..., site_not_found: bool = ..., site_id: _Optional[str] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., total_bytes_read: _Optional[int] = ..., total_bytes_to_transfer: _Optional[int] = ..., total_logical_backup_size_in_bytes: _Optional[int] = ..., use_magneto_o365_onedrive_v2_subtask: bool = ..., site_checksum: _Optional[str] = ..., sharepoint_data_stats: _Optional[_Union[_graph_pb2.SharepointDataStats, _Mapping]] = ..., file_data_distribution_table: _Optional[_Union[_graph_pb2.DataDistributionTable, _Mapping]] = ..., throttling_time_distribution_table: _Optional[_Union[_graph_pb2.ThrottlingErrorTimeDistributionTable, _Mapping]] = ..., prev_status: _Optional[_Union[SharepointSnapshotInfo.Status, str]] = ..., prev_state_start_time: _Optional[int] = ..., fast_cleanup_enabled: bool = ..., application_ids_permit_scaling_enabled: bool = ..., site_template_backup_skipped: bool = ..., should_backup_sp_lists: bool = ..., doclib_start_limited_subtasks: bool = ...) -> None: ...

class PublicFolderChildInfo(_message.Message):
    __slots__ = ("name", "id", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    type: _outlook_external_pb2.FolderType.Type
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ...) -> None: ...

class PublicFolderInfo(_message.Message):
    __slots__ = ("name", "id", "parent_id", "child_info_vec", "full_parent_path", "type", "backup_info", "restore_info", "o365_error_proto_vec")
    class BackupInfo(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RestoreInfo(_message.Message):
        __slots__ = ("restore_arg_idx", "is_root")
        RESTORE_ARG_IDX_FIELD_NUMBER: _ClassVar[int]
        IS_ROOT_FIELD_NUMBER: _ClassVar[int]
        restore_arg_idx: int
        is_root: bool
        def __init__(self, restore_arg_idx: _Optional[int] = ..., is_root: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FULL_PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    parent_id: str
    child_info_vec: _containers.RepeatedCompositeFieldContainer[PublicFolderChildInfo]
    full_parent_path: str
    type: _outlook_external_pb2.FolderType.Type
    backup_info: PublicFolderInfo.BackupInfo
    restore_info: PublicFolderInfo.RestoreInfo
    o365_error_proto_vec: _containers.RepeatedCompositeFieldContainer[_o365_error_pb2.O365ErrorProto]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., parent_id: _Optional[str] = ..., child_info_vec: _Optional[_Iterable[_Union[PublicFolderChildInfo, _Mapping]]] = ..., full_parent_path: _Optional[str] = ..., type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., backup_info: _Optional[_Union[PublicFolderInfo.BackupInfo, _Mapping]] = ..., restore_info: _Optional[_Union[PublicFolderInfo.RestoreInfo, _Mapping]] = ..., o365_error_proto_vec: _Optional[_Iterable[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]]] = ...) -> None: ...

class PublicFolderWorkUnit(_message.Message):
    __slots__ = ("folder_id", "folder_sync_state", "child_cursor_cookie", "work_status")
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    CHILD_CURSOR_COOKIE_FIELD_NUMBER: _ClassVar[int]
    WORK_STATUS_FIELD_NUMBER: _ClassVar[int]
    folder_id: str
    folder_sync_state: str
    child_cursor_cookie: str
    work_status: int
    def __init__(self, folder_id: _Optional[str] = ..., folder_sync_state: _Optional[str] = ..., child_cursor_cookie: _Optional[str] = ..., work_status: _Optional[int] = ...) -> None: ...

class PublicFolderSubTaskScribeInfo(_message.Message):
    __slots__ = ("prev_sync_state", "num_backed_up_items", "size_backed_up_items", "num_created_items", "num_deleted_items", "backup_folder_error", "incremental_file_offset", "incremental_write_error", "all_changes_fetched", "is_first_backup_batch")
    PUBLIC_FOLDER_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    public_folder_sub_task_scribe_info: _descriptor.FieldDescriptor
    PREV_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FOLDER_ERROR_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_WRITE_ERROR_FIELD_NUMBER: _ClassVar[int]
    ALL_CHANGES_FETCHED_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_BACKUP_BATCH_FIELD_NUMBER: _ClassVar[int]
    prev_sync_state: str
    num_backed_up_items: int
    size_backed_up_items: int
    num_created_items: int
    num_deleted_items: int
    backup_folder_error: _error_pb2.ErrorProto
    incremental_file_offset: int
    incremental_write_error: _error_pb2.ErrorProto
    all_changes_fetched: bool
    is_first_backup_batch: bool
    def __init__(self, prev_sync_state: _Optional[str] = ..., num_backed_up_items: _Optional[int] = ..., size_backed_up_items: _Optional[int] = ..., num_created_items: _Optional[int] = ..., num_deleted_items: _Optional[int] = ..., backup_folder_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., incremental_file_offset: _Optional[int] = ..., incremental_write_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., all_changes_fetched: bool = ..., is_first_backup_batch: bool = ...) -> None: ...

class PublicFolderSubTaskInfo(_message.Message):
    __slots__ = ("folder_id", "is_inflated", "replica_id", "parent_folder_id", "sync_state", "content_mailbox_id", "display_name", "child_folder_count", "type", "is_done", "o365_error_proto_vec")
    PUBLIC_FOLDER_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    public_folder_sub_task_info: _descriptor.FieldDescriptor
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_INFLATED_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHILD_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    folder_id: str
    is_inflated: bool
    replica_id: str
    parent_folder_id: str
    sync_state: str
    content_mailbox_id: str
    display_name: str
    child_folder_count: int
    type: _outlook_external_pb2.FolderType.Type
    is_done: bool
    o365_error_proto_vec: _containers.RepeatedCompositeFieldContainer[_o365_error_pb2.O365ErrorProto]
    def __init__(self, folder_id: _Optional[str] = ..., is_inflated: bool = ..., replica_id: _Optional[str] = ..., parent_folder_id: _Optional[str] = ..., sync_state: _Optional[str] = ..., content_mailbox_id: _Optional[str] = ..., display_name: _Optional[str] = ..., child_folder_count: _Optional[int] = ..., type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., is_done: bool = ..., o365_error_proto_vec: _Optional[_Iterable[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]]] = ...) -> None: ...

class PublicFolderSnapshotInfo(_message.Message):
    __slots__ = ("status", "job_instance_id", "attempt_num", "error", "sub_task_vec", "work_unit_vec", "producer_consumer_list_initialized", "mailbox_id", "public_folder_mailbox_id", "hierarchy_db_folder_name", "replica_id", "child_folder_count", "type", "orphaned_directory_vec", "orphaned_directory_deletion_done", "continue_on_error", "should_take_dummy_permit")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[PublicFolderSnapshotInfo.Status]
        kPermitGranted: _ClassVar[PublicFolderSnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[PublicFolderSnapshotInfo.Status]
        kBackupFinished: _ClassVar[PublicFolderSnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[PublicFolderSnapshotInfo.Status]
        kFolderHierarchyFetched: _ClassVar[PublicFolderSnapshotInfo.Status]
    kStarted: PublicFolderSnapshotInfo.Status
    kPermitGranted: PublicFolderSnapshotInfo.Status
    kPrepareBackupDone: PublicFolderSnapshotInfo.Status
    kBackupFinished: PublicFolderSnapshotInfo.Status
    kProgressMonitorsCreated: PublicFolderSnapshotInfo.Status
    kFolderHierarchyFetched: PublicFolderSnapshotInfo.Status
    PUBLIC_FOLDER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    public_folder_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_VEC_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_CONSUMER_LIST_INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_DB_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ORPHANED_DIRECTORY_VEC_FIELD_NUMBER: _ClassVar[int]
    ORPHANED_DIRECTORY_DELETION_DONE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    SHOULD_TAKE_DUMMY_PERMIT_FIELD_NUMBER: _ClassVar[int]
    status: PublicFolderSnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    error: _error_pb2.ErrorProto
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    work_unit_vec: _containers.RepeatedCompositeFieldContainer[PublicFolderWorkUnit]
    producer_consumer_list_initialized: bool
    mailbox_id: str
    public_folder_mailbox_id: str
    hierarchy_db_folder_name: str
    replica_id: str
    child_folder_count: int
    type: _outlook_external_pb2.FolderType.Type
    orphaned_directory_vec: _containers.RepeatedScalarFieldContainer[str]
    orphaned_directory_deletion_done: bool
    continue_on_error: bool
    should_take_dummy_permit: bool
    def __init__(self, status: _Optional[_Union[PublicFolderSnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sub_task_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., work_unit_vec: _Optional[_Iterable[_Union[PublicFolderWorkUnit, _Mapping]]] = ..., producer_consumer_list_initialized: bool = ..., mailbox_id: _Optional[str] = ..., public_folder_mailbox_id: _Optional[str] = ..., hierarchy_db_folder_name: _Optional[str] = ..., replica_id: _Optional[str] = ..., child_folder_count: _Optional[int] = ..., type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., orphaned_directory_vec: _Optional[_Iterable[str]] = ..., orphaned_directory_deletion_done: bool = ..., continue_on_error: bool = ..., should_take_dummy_permit: bool = ...) -> None: ...

class TeamsSparseConfig(_message.Message):
    __slots__ = ("team", "private_channels_index_vec", "is_teams_info_bkp")
    TEAM_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CHANNELS_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_TEAMS_INFO_BKP_FIELD_NUMBER: _ClassVar[int]
    team: _graph_pb2.Team
    private_channels_index_vec: _containers.RepeatedScalarFieldContainer[int]
    is_teams_info_bkp: bool
    def __init__(self, team: _Optional[_Union[_graph_pb2.Team, _Mapping]] = ..., private_channels_index_vec: _Optional[_Iterable[int]] = ..., is_teams_info_bkp: bool = ...) -> None: ...

class TeamsSnapshotInfo(_message.Message):
    __slots__ = ("status", "job_instance_id", "attempt_num", "error", "prev_teams_config", "curr_teams_config", "config_file_written", "o365_group_snapshot", "site_snapshot_vec", "use_magneto_o365_onedrive_v2_subtask", "application_ids_permit_scaling_enabled", "channel_count", "chats_snapshot_info_proto", "chats_backup_allowed", "site_doclib_start_limited_subtasks")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[TeamsSnapshotInfo.Status]
        kBackupFinished: _ClassVar[TeamsSnapshotInfo.Status]
        kTeamChannelsFetched: _ClassVar[TeamsSnapshotInfo.Status]
        kTeamChannelsSitesFetched: _ClassVar[TeamsSnapshotInfo.Status]
        kTeamChannelsInfoFetched: _ClassVar[TeamsSnapshotInfo.Status]
        kPermitGranted: _ClassVar[TeamsSnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[TeamsSnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[TeamsSnapshotInfo.Status]
    kStarted: TeamsSnapshotInfo.Status
    kBackupFinished: TeamsSnapshotInfo.Status
    kTeamChannelsFetched: TeamsSnapshotInfo.Status
    kTeamChannelsSitesFetched: TeamsSnapshotInfo.Status
    kTeamChannelsInfoFetched: TeamsSnapshotInfo.Status
    kPermitGranted: TeamsSnapshotInfo.Status
    kPrepareBackupDone: TeamsSnapshotInfo.Status
    kProgressMonitorsCreated: TeamsSnapshotInfo.Status
    class O365GroupSnapshot(_message.Message):
        __slots__ = ("group_id", "o365_group_snapshot_info_proto")
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        O365_GROUP_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        o365_group_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        def __init__(self, group_id: _Optional[str] = ..., o365_group_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ...) -> None: ...
    class SharepointSnapshot(_message.Message):
        __slots__ = ("site_id", "sharepoint_snapshot_info_proto", "trigger_full_team_site_backup", "channel_name")
        SITE_ID_FIELD_NUMBER: _ClassVar[int]
        SHAREPOINT_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FULL_TEAM_SITE_BACKUP_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        site_id: str
        sharepoint_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        trigger_full_team_site_backup: bool
        channel_name: str
        def __init__(self, site_id: _Optional[str] = ..., sharepoint_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., trigger_full_team_site_backup: bool = ..., channel_name: _Optional[str] = ...) -> None: ...
    TEAMS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    teams_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PREV_TEAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CURR_TEAMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    O365_GROUP_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SITE_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_MAGNETO_O365_ONEDRIVE_V2_SUBTASK_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_PERMIT_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHATS_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    CHATS_BACKUP_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SITE_DOCLIB_START_LIMITED_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    status: TeamsSnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    error: _error_pb2.ErrorProto
    prev_teams_config: TeamsSparseConfig
    curr_teams_config: TeamsSparseConfig
    config_file_written: bool
    o365_group_snapshot: TeamsSnapshotInfo.O365GroupSnapshot
    site_snapshot_vec: _containers.RepeatedCompositeFieldContainer[TeamsSnapshotInfo.SharepointSnapshot]
    use_magneto_o365_onedrive_v2_subtask: bool
    application_ids_permit_scaling_enabled: bool
    channel_count: int
    chats_snapshot_info_proto: ChatsSnapshotInfo
    chats_backup_allowed: bool
    site_doclib_start_limited_subtasks: bool
    def __init__(self, status: _Optional[_Union[TeamsSnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., prev_teams_config: _Optional[_Union[TeamsSparseConfig, _Mapping]] = ..., curr_teams_config: _Optional[_Union[TeamsSparseConfig, _Mapping]] = ..., config_file_written: bool = ..., o365_group_snapshot: _Optional[_Union[TeamsSnapshotInfo.O365GroupSnapshot, _Mapping]] = ..., site_snapshot_vec: _Optional[_Iterable[_Union[TeamsSnapshotInfo.SharepointSnapshot, _Mapping]]] = ..., use_magneto_o365_onedrive_v2_subtask: bool = ..., application_ids_permit_scaling_enabled: bool = ..., channel_count: _Optional[int] = ..., chats_snapshot_info_proto: _Optional[_Union[ChatsSnapshotInfo, _Mapping]] = ..., chats_backup_allowed: bool = ..., site_doclib_start_limited_subtasks: bool = ...) -> None: ...

class SharepointTemplateTaskStats(_message.Message):
    __slots__ = ("skip_reason", "start_time_usecs", "permit_grant_time_usecs", "end_time_usecs", "template_file_size_bytes")
    class SkipReson(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[SharepointTemplateTaskStats.SkipReson]
        kDisabled: _ClassVar[SharepointTemplateTaskStats.SkipReson]
        kNoChecksumAndSystemFilesChanged: _ClassVar[SharepointTemplateTaskStats.SkipReson]
        kPreferredWeekdayConfiguration: _ClassVar[SharepointTemplateTaskStats.SkipReson]
    kNone: SharepointTemplateTaskStats.SkipReson
    kDisabled: SharepointTemplateTaskStats.SkipReson
    kNoChecksumAndSystemFilesChanged: SharepointTemplateTaskStats.SkipReson
    kPreferredWeekdayConfiguration: SharepointTemplateTaskStats.SkipReson
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PERMIT_GRANT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    skip_reason: SharepointTemplateTaskStats.SkipReson
    start_time_usecs: int
    permit_grant_time_usecs: int
    end_time_usecs: int
    template_file_size_bytes: int
    def __init__(self, skip_reason: _Optional[_Union[SharepointTemplateTaskStats.SkipReson, str]] = ..., start_time_usecs: _Optional[int] = ..., permit_grant_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., template_file_size_bytes: _Optional[int] = ...) -> None: ...

class SharepointTemplateSnapshotInfo(_message.Message):
    __slots__ = ("status", "error", "backup_sites_result", "snap_fs_relative_template_path", "mounted_view_path", "parent_site_entity", "site_result", "use_smb_mount", "backup_file_index", "snap_fs_relative_backup_site_result_path", "cancelled", "warnings", "task_stats")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kPermitGranted: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kViewMountDone: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kTemplateSnapshot: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kFetchSnapshot: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kFetchResult: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kSnapshotFetchDone: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kCleanupAgent: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kBackupFinished: _ClassVar[SharepointTemplateSnapshotInfo.Status]
        kCancelTask: _ClassVar[SharepointTemplateSnapshotInfo.Status]
    kStarted: SharepointTemplateSnapshotInfo.Status
    kPermitGranted: SharepointTemplateSnapshotInfo.Status
    kViewMountDone: SharepointTemplateSnapshotInfo.Status
    kTemplateSnapshot: SharepointTemplateSnapshotInfo.Status
    kFetchSnapshot: SharepointTemplateSnapshotInfo.Status
    kFetchResult: SharepointTemplateSnapshotInfo.Status
    kSnapshotFetchDone: SharepointTemplateSnapshotInfo.Status
    kCleanupAgent: SharepointTemplateSnapshotInfo.Status
    kBackupFinished: SharepointTemplateSnapshotInfo.Status
    kCancelTask: SharepointTemplateSnapshotInfo.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SITES_RESULT_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_RELATIVE_TEMPLATE_PATH_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_SITE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    USE_SMB_MOUNT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_RELATIVE_BACKUP_SITE_RESULT_PATH_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    TASK_STATS_FIELD_NUMBER: _ClassVar[int]
    status: SharepointTemplateSnapshotInfo.Status
    error: _error_pb2.ErrorProto
    backup_sites_result: _o365spo_pb2.BackupSiteResult
    snap_fs_relative_template_path: str
    mounted_view_path: str
    parent_site_entity: _entity_pb2.EntityProto
    site_result: _o365spo_pb2.SiteBackupStatus
    use_smb_mount: bool
    backup_file_index: int
    snap_fs_relative_backup_site_result_path: str
    cancelled: bool
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    task_stats: SharepointTemplateTaskStats
    def __init__(self, status: _Optional[_Union[SharepointTemplateSnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_sites_result: _Optional[_Union[_o365spo_pb2.BackupSiteResult, _Mapping]] = ..., snap_fs_relative_template_path: _Optional[str] = ..., mounted_view_path: _Optional[str] = ..., parent_site_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., site_result: _Optional[_Union[_o365spo_pb2.SiteBackupStatus, _Mapping]] = ..., use_smb_mount: bool = ..., backup_file_index: _Optional[int] = ..., snap_fs_relative_backup_site_result_path: _Optional[str] = ..., cancelled: bool = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., task_stats: _Optional[_Union[SharepointTemplateTaskStats, _Mapping]] = ...) -> None: ...

class ChatsSparseConfig(_message.Message):
    __slots__ = ("last_backup_time_msecs", "chat_id_map")
    class ChatIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _graph_pb2.Chat
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_graph_pb2.Chat, _Mapping]] = ...) -> None: ...
    LAST_BACKUP_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    last_backup_time_msecs: int
    chat_id_map: _containers.MessageMap[str, _graph_pb2.Chat]
    def __init__(self, last_backup_time_msecs: _Optional[int] = ..., chat_id_map: _Optional[_Mapping[str, _graph_pb2.Chat]] = ...) -> None: ...

class ChatsSnapshotInfo(_message.Message):
    __slots__ = ("status", "error", "prev_chats_config", "config_file_written", "sub_tasks_vec", "chat_id_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ChatsSnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[ChatsSnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[ChatsSnapshotInfo.Status]
        kBackupFinished: _ClassVar[ChatsSnapshotInfo.Status]
    kStarted: ChatsSnapshotInfo.Status
    kPrepareBackupDone: ChatsSnapshotInfo.Status
    kProgressMonitorsCreated: ChatsSnapshotInfo.Status
    kBackupFinished: ChatsSnapshotInfo.Status
    CHATS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    chats_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PREV_CHATS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    status: ChatsSnapshotInfo.Status
    error: _error_pb2.ErrorProto
    prev_chats_config: ChatsSparseConfig
    config_file_written: bool
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    chat_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[_Union[ChatsSnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., prev_chats_config: _Optional[_Union[ChatsSparseConfig, _Mapping]] = ..., config_file_written: bool = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., chat_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ChatsSubTaskScribeInfo(_message.Message):
    __slots__ = ("last_message_processed_time_millis", "next_link")
    CHATS_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    chats_sub_task_scribe_info: _descriptor.FieldDescriptor
    LAST_MESSAGE_PROCESSED_TIME_MILLIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    last_message_processed_time_millis: int
    next_link: str
    def __init__(self, last_message_processed_time_millis: _Optional[int] = ..., next_link: _Optional[str] = ...) -> None: ...

class O365GroupSparseConfig(_message.Message):
    __slots__ = ("group_info", "group_delta_link", "group_owner_vec", "is_site_backed_up", "group_owner_smtp_address_vec")
    GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_DELTA_LINK_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_SITE_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_SMTP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    group_info: _graph_pb2.Group
    group_delta_link: str
    group_owner_vec: _containers.RepeatedScalarFieldContainer[str]
    is_site_backed_up: bool
    group_owner_smtp_address_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_info: _Optional[_Union[_graph_pb2.Group, _Mapping]] = ..., group_delta_link: _Optional[str] = ..., group_owner_vec: _Optional[_Iterable[str]] = ..., is_site_backed_up: bool = ..., group_owner_smtp_address_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class O365GroupSnapshotInfo(_message.Message):
    __slots__ = ("o365_group_snapshot", "status", "job_instance_id", "attempt_num", "error", "prev_group_config", "curr_group_config", "config_file_written", "o365_error_proto", "include_site_backup", "include_mailbox_backup", "use_magneto_o365_onedrive_v2_subtask", "application_ids_permit_scaling_enabled", "site_doclib_start_limited_subtasks")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[O365GroupSnapshotInfo.Status]
        kGroupSiteFetched: _ClassVar[O365GroupSnapshotInfo.Status]
        kPrepareBackupDone: _ClassVar[O365GroupSnapshotInfo.Status]
        kGroupDeltaFetched: _ClassVar[O365GroupSnapshotInfo.Status]
        kGroupInfoFetched: _ClassVar[O365GroupSnapshotInfo.Status]
        kPermitGranted: _ClassVar[O365GroupSnapshotInfo.Status]
        kProgressMonitorsCreated: _ClassVar[O365GroupSnapshotInfo.Status]
        kBackupFinished: _ClassVar[O365GroupSnapshotInfo.Status]
    kStarted: O365GroupSnapshotInfo.Status
    kGroupSiteFetched: O365GroupSnapshotInfo.Status
    kPrepareBackupDone: O365GroupSnapshotInfo.Status
    kGroupDeltaFetched: O365GroupSnapshotInfo.Status
    kGroupInfoFetched: O365GroupSnapshotInfo.Status
    kPermitGranted: O365GroupSnapshotInfo.Status
    kProgressMonitorsCreated: O365GroupSnapshotInfo.Status
    kBackupFinished: O365GroupSnapshotInfo.Status
    class O365GroupSnapshot(_message.Message):
        __slots__ = ("group_id", "group_mailbox_snapshot_info_proto", "site_id", "sharepoint_snapshot_info_proto", "trigger_full_backup_group", "trigger_full_backup_site", "site_name", "site_url")
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_MAILBOX_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        SITE_ID_FIELD_NUMBER: _ClassVar[int]
        SHAREPOINT_SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FULL_BACKUP_GROUP_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FULL_BACKUP_SITE_FIELD_NUMBER: _ClassVar[int]
        SITE_NAME_FIELD_NUMBER: _ClassVar[int]
        SITE_URL_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        group_mailbox_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        site_id: str
        sharepoint_snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
        trigger_full_backup_group: bool
        trigger_full_backup_site: bool
        site_name: str
        site_url: str
        def __init__(self, group_id: _Optional[str] = ..., group_mailbox_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., site_id: _Optional[str] = ..., sharepoint_snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., trigger_full_backup_group: bool = ..., trigger_full_backup_site: bool = ..., site_name: _Optional[str] = ..., site_url: _Optional[str] = ...) -> None: ...
    O365_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    o365_group_snapshot_info: _descriptor.FieldDescriptor
    O365_GROUP_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PREV_GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CURR_GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SITE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MAILBOX_BACKUP_FIELD_NUMBER: _ClassVar[int]
    USE_MAGNETO_O365_ONEDRIVE_V2_SUBTASK_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_PERMIT_SCALING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SITE_DOCLIB_START_LIMITED_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    o365_group_snapshot: O365GroupSnapshotInfo.O365GroupSnapshot
    status: O365GroupSnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    error: _error_pb2.ErrorProto
    prev_group_config: O365GroupSparseConfig
    curr_group_config: O365GroupSparseConfig
    config_file_written: bool
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    include_site_backup: bool
    include_mailbox_backup: bool
    use_magneto_o365_onedrive_v2_subtask: bool
    application_ids_permit_scaling_enabled: bool
    site_doclib_start_limited_subtasks: bool
    def __init__(self, o365_group_snapshot: _Optional[_Union[O365GroupSnapshotInfo.O365GroupSnapshot, _Mapping]] = ..., status: _Optional[_Union[O365GroupSnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., prev_group_config: _Optional[_Union[O365GroupSparseConfig, _Mapping]] = ..., curr_group_config: _Optional[_Union[O365GroupSparseConfig, _Mapping]] = ..., config_file_written: bool = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., include_site_backup: bool = ..., include_mailbox_backup: bool = ..., use_magneto_o365_onedrive_v2_subtask: bool = ..., application_ids_permit_scaling_enabled: bool = ..., site_doclib_start_limited_subtasks: bool = ...) -> None: ...

class O365AdditionalRunInfo(_message.Message):
    __slots__ = ("view_cloning_enabled", "should_use_flat_file_structure", "base_run_start_time_usecs", "perform_object_specific_cloning")
    O365_ADDITIONAL_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    o365_additional_run_info: _descriptor.FieldDescriptor
    VIEW_CLONING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOULD_USE_FLAT_FILE_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    BASE_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PERFORM_OBJECT_SPECIFIC_CLONING_FIELD_NUMBER: _ClassVar[int]
    view_cloning_enabled: bool
    should_use_flat_file_structure: bool
    base_run_start_time_usecs: int
    perform_object_specific_cloning: bool
    def __init__(self, view_cloning_enabled: bool = ..., should_use_flat_file_structure: bool = ..., base_run_start_time_usecs: _Optional[int] = ..., perform_object_specific_cloning: bool = ...) -> None: ...

class ProgressCBArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProgressCBResult(_message.Message):
    __slots__ = ("cancellation_requested",)
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    cancellation_requested: bool
    def __init__(self, cancellation_requested: bool = ...) -> None: ...

class O365RestoreInfo(_message.Message):
    __slots__ = ("status", "error", "o365_one_drive_restore_info_vec", "entity_root_drive_map", "target_drive_id", "site_view_root_path", "user_view_root_path_vec", "teams_view_root_path", "snap_fs_teams_channel_path", "target_drive_name_id_map", "create_site_info", "template_restore_info", "site_id", "skipped_target_drive_name_id_map", "site_admin_user_vec", "restore_has_multiple_drives_per_user", "lists_restore_info")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[O365RestoreInfo.Status]
        kViewCloned: _ClassVar[O365RestoreInfo.Status]
        kDriveListFetched: _ClassVar[O365RestoreInfo.Status]
        kPermitGranted: _ClassVar[O365RestoreInfo.Status]
        kProgressMonitorsCreated: _ClassVar[O365RestoreInfo.Status]
        kSiteCreated: _ClassVar[O365RestoreInfo.Status]
        kProvisionTemplate: _ClassVar[O365RestoreInfo.Status]
        kTemplateProvisioned: _ClassVar[O365RestoreInfo.Status]
        kViewDeleted: _ClassVar[O365RestoreInfo.Status]
        kSiteInfoFetched: _ClassVar[O365RestoreInfo.Status]
        kRestoreFinished: _ClassVar[O365RestoreInfo.Status]
    kStarted: O365RestoreInfo.Status
    kViewCloned: O365RestoreInfo.Status
    kDriveListFetched: O365RestoreInfo.Status
    kPermitGranted: O365RestoreInfo.Status
    kProgressMonitorsCreated: O365RestoreInfo.Status
    kSiteCreated: O365RestoreInfo.Status
    kProvisionTemplate: O365RestoreInfo.Status
    kTemplateProvisioned: O365RestoreInfo.Status
    kViewDeleted: O365RestoreInfo.Status
    kSiteInfoFetched: O365RestoreInfo.Status
    kRestoreFinished: O365RestoreInfo.Status
    class EntityRootDriveMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class TargetDriveNameIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SkippedTargetDriveNameIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    O365_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    o365_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    O365_ONE_DRIVE_RESTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ROOT_DRIVE_MAP_FIELD_NUMBER: _ClassVar[int]
    TARGET_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_VIEW_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    USER_VIEW_ROOT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    TEAMS_VIEW_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_TEAMS_CHANNEL_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_DRIVE_NAME_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    CREATE_SITE_INFO_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_TARGET_DRIVE_NAME_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    SITE_ADMIN_USER_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_HAS_MULTIPLE_DRIVES_PER_USER_FIELD_NUMBER: _ClassVar[int]
    LISTS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    status: O365RestoreInfo.Status
    error: _error_pb2.ErrorProto
    o365_one_drive_restore_info_vec: _containers.RepeatedCompositeFieldContainer[O365OneDriveRestoreInfo]
    entity_root_drive_map: _containers.ScalarMap[int, str]
    target_drive_id: str
    site_view_root_path: str
    user_view_root_path_vec: _containers.RepeatedScalarFieldContainer[str]
    teams_view_root_path: str
    snap_fs_teams_channel_path: str
    target_drive_name_id_map: _containers.ScalarMap[str, str]
    create_site_info: O365SharepointTemplateRestore
    template_restore_info: O365SharepointTemplateRestore
    site_id: str
    skipped_target_drive_name_id_map: _containers.ScalarMap[str, str]
    site_admin_user_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    restore_has_multiple_drives_per_user: bool
    lists_restore_info: SharepointListsRestoreInfo
    def __init__(self, status: _Optional[_Union[O365RestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., o365_one_drive_restore_info_vec: _Optional[_Iterable[_Union[O365OneDriveRestoreInfo, _Mapping]]] = ..., entity_root_drive_map: _Optional[_Mapping[int, str]] = ..., target_drive_id: _Optional[str] = ..., site_view_root_path: _Optional[str] = ..., user_view_root_path_vec: _Optional[_Iterable[str]] = ..., teams_view_root_path: _Optional[str] = ..., snap_fs_teams_channel_path: _Optional[str] = ..., target_drive_name_id_map: _Optional[_Mapping[str, str]] = ..., create_site_info: _Optional[_Union[O365SharepointTemplateRestore, _Mapping]] = ..., template_restore_info: _Optional[_Union[O365SharepointTemplateRestore, _Mapping]] = ..., site_id: _Optional[str] = ..., skipped_target_drive_name_id_map: _Optional[_Mapping[str, str]] = ..., site_admin_user_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ..., restore_has_multiple_drives_per_user: bool = ..., lists_restore_info: _Optional[_Union[SharepointListsRestoreInfo, _Mapping]] = ...) -> None: ...

class O365OneDriveRestoreInfo(_message.Message):
    __slots__ = ("status", "restore_item_path_vec", "sub_tasks_vec", "error", "last_visited_drive_item_id", "has_more_items", "view_root_path", "snap_fs_drive_path", "drive_id", "target_drive_id", "total_api_call_count", "is_file_structure_flat", "drive_name", "target_folder_path_prefix", "is_system_drive", "site_info", "total_errors_encountered", "errored_file_vec", "drive_type", "entity_index", "phl_folder_prefix", "total_errors_persisted_across_sub_tasks")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[O365OneDriveRestoreInfo.Status]
        kPulseCreated: _ClassVar[O365OneDriveRestoreInfo.Status]
        kSubTasksFinished: _ClassVar[O365OneDriveRestoreInfo.Status]
    kStarted: O365OneDriveRestoreInfo.Status
    kPulseCreated: O365OneDriveRestoreInfo.Status
    kSubTasksFinished: O365OneDriveRestoreInfo.Status
    O365_ONE_DRIVE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    o365_one_drive_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ITEM_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_DRIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_API_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_STRUCTURE_FLAT_FIELD_NUMBER: _ClassVar[int]
    DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FOLDER_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DRIVE_FIELD_NUMBER: _ClassVar[int]
    SITE_INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERRORS_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    ERRORED_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    PHL_FOLDER_PREFIX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERRORS_PERSISTED_ACROSS_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    status: O365OneDriveRestoreInfo.Status
    restore_item_path_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    last_visited_drive_item_id: str
    has_more_items: bool
    view_root_path: str
    snap_fs_drive_path: str
    drive_id: str
    target_drive_id: str
    total_api_call_count: int
    is_file_structure_flat: bool
    drive_name: str
    target_folder_path_prefix: str
    is_system_drive: bool
    site_info: SharepointSiteInfo
    total_errors_encountered: int
    errored_file_vec: _containers.RepeatedCompositeFieldContainer[_graph_pb2.O365ErroredFileInfo]
    drive_type: _graph_enums_pb2.DriveType.Type
    entity_index: int
    phl_folder_prefix: str
    total_errors_persisted_across_sub_tasks: int
    def __init__(self, status: _Optional[_Union[O365OneDriveRestoreInfo.Status, str]] = ..., restore_item_path_vec: _Optional[_Iterable[str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., last_visited_drive_item_id: _Optional[str] = ..., has_more_items: bool = ..., view_root_path: _Optional[str] = ..., snap_fs_drive_path: _Optional[str] = ..., drive_id: _Optional[str] = ..., target_drive_id: _Optional[str] = ..., total_api_call_count: _Optional[int] = ..., is_file_structure_flat: bool = ..., drive_name: _Optional[str] = ..., target_folder_path_prefix: _Optional[str] = ..., is_system_drive: bool = ..., site_info: _Optional[_Union[SharepointSiteInfo, _Mapping]] = ..., total_errors_encountered: _Optional[int] = ..., errored_file_vec: _Optional[_Iterable[_Union[_graph_pb2.O365ErroredFileInfo, _Mapping]]] = ..., drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ..., entity_index: _Optional[int] = ..., phl_folder_prefix: _Optional[str] = ..., total_errors_persisted_across_sub_tasks: _Optional[int] = ...) -> None: ...

class SharepointSiteInfo(_message.Message):
    __slots__ = ("domain_name", "target_web_url", "source_web_url")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    target_web_url: str
    source_web_url: str
    def __init__(self, domain_name: _Optional[str] = ..., target_web_url: _Optional[str] = ..., source_web_url: _Optional[str] = ...) -> None: ...

class O365SharepointTemplateRestore(_message.Message):
    __slots__ = ("status", "error", "snap_fs_relative_template_path", "site_result", "mounted_view_path", "restore_result", "restore_files_info", "use_smb_mount", "cancelled")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[O365SharepointTemplateRestore.Status]
        kCopyTemplate: _ClassVar[O365SharepointTemplateRestore.Status]
        kViewMountDone: _ClassVar[O365SharepointTemplateRestore.Status]
        kRestoreRequested: _ClassVar[O365SharepointTemplateRestore.Status]
        kFetchRestoreStatus: _ClassVar[O365SharepointTemplateRestore.Status]
        kCleanupAgent: _ClassVar[O365SharepointTemplateRestore.Status]
        kRestoreFinished: _ClassVar[O365SharepointTemplateRestore.Status]
        kCancelTask: _ClassVar[O365SharepointTemplateRestore.Status]
    kStarted: O365SharepointTemplateRestore.Status
    kCopyTemplate: O365SharepointTemplateRestore.Status
    kViewMountDone: O365SharepointTemplateRestore.Status
    kRestoreRequested: O365SharepointTemplateRestore.Status
    kFetchRestoreStatus: O365SharepointTemplateRestore.Status
    kCleanupAgent: O365SharepointTemplateRestore.Status
    kRestoreFinished: O365SharepointTemplateRestore.Status
    kCancelTask: O365SharepointTemplateRestore.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAP_FS_RELATIVE_TEMPLATE_PATH_FIELD_NUMBER: _ClassVar[int]
    SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_SMB_MOUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    status: O365SharepointTemplateRestore.Status
    error: _error_pb2.ErrorProto
    snap_fs_relative_template_path: str
    site_result: _o365spo_pb2.SiteBackupStatus
    mounted_view_path: str
    restore_result: _o365spo_pb2.GetRestoreSiteOutputResult.SiteRestoreStatus
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    use_smb_mount: bool
    cancelled: bool
    def __init__(self, status: _Optional[_Union[O365SharepointTemplateRestore.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snap_fs_relative_template_path: _Optional[str] = ..., site_result: _Optional[_Union[_o365spo_pb2.SiteBackupStatus, _Mapping]] = ..., mounted_view_path: _Optional[str] = ..., restore_result: _Optional[_Union[_o365spo_pb2.GetRestoreSiteOutputResult.SiteRestoreStatus, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ..., use_smb_mount: bool = ..., cancelled: bool = ...) -> None: ...

class PublicFolderRestoreSubTaskInfo(_message.Message):
    __slots__ = ("public_folder_info_vec",)
    PUBLIC_FOLDER_RESTORE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    public_folder_restore_sub_task_info: _descriptor.FieldDescriptor
    PUBLIC_FOLDER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    public_folder_info_vec: _containers.RepeatedCompositeFieldContainer[PublicFolderInfo]
    def __init__(self, public_folder_info_vec: _Optional[_Iterable[_Union[PublicFolderInfo, _Mapping]]] = ...) -> None: ...

class PublicFolderRestoreInfo(_message.Message):
    __slots__ = ("status", "sub_task_vec", "folder_idx_to_process", "is_explored", "hierarchy_cookie", "error", "src_entity_name", "finished_sub_task_count", "restore_error", "mailbox_id", "public_folder_mailbox_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[PublicFolderRestoreInfo.Status]
        kViewCloned: _ClassVar[PublicFolderRestoreInfo.Status]
        kSubTasksFinished: _ClassVar[PublicFolderRestoreInfo.Status]
        kViewDeleted: _ClassVar[PublicFolderRestoreInfo.Status]
    kStarted: PublicFolderRestoreInfo.Status
    kViewCloned: PublicFolderRestoreInfo.Status
    kSubTasksFinished: PublicFolderRestoreInfo.Status
    kViewDeleted: PublicFolderRestoreInfo.Status
    PUBLIC_FOLDER_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    public_folder_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_IDX_TO_PROCESS_FIELD_NUMBER: _ClassVar[int]
    IS_EXPLORED_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_COOKIE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SRC_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    FINISHED_SUB_TASK_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    status: PublicFolderRestoreInfo.Status
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    folder_idx_to_process: int
    is_explored: bool
    hierarchy_cookie: str
    error: _error_pb2.ErrorProto
    src_entity_name: str
    finished_sub_task_count: int
    restore_error: _error_pb2.ErrorProto
    mailbox_id: str
    public_folder_mailbox_id: str
    def __init__(self, status: _Optional[_Union[PublicFolderRestoreInfo.Status, str]] = ..., sub_task_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., folder_idx_to_process: _Optional[int] = ..., is_explored: bool = ..., hierarchy_cookie: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., src_entity_name: _Optional[str] = ..., finished_sub_task_count: _Optional[int] = ..., restore_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mailbox_id: _Optional[str] = ..., public_folder_mailbox_id: _Optional[str] = ...) -> None: ...

class PublicFolderRestoreSubTaskScribeInfo(_message.Message):
    __slots__ = ("restore_folder_status_vec",)
    class RestoreFolderStatus(_message.Message):
        __slots__ = ("folder_id", "last_visited_key", "next_index_to_restore", "restore_completed", "content_mailbox_id")
        FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_VISITED_KEY_FIELD_NUMBER: _ClassVar[int]
        NEXT_INDEX_TO_RESTORE_FIELD_NUMBER: _ClassVar[int]
        RESTORE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        CONTENT_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
        folder_id: str
        last_visited_key: str
        next_index_to_restore: int
        restore_completed: bool
        content_mailbox_id: str
        def __init__(self, folder_id: _Optional[str] = ..., last_visited_key: _Optional[str] = ..., next_index_to_restore: _Optional[int] = ..., restore_completed: bool = ..., content_mailbox_id: _Optional[str] = ...) -> None: ...
    PUBLIC_FOLDER_RESTORE_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    public_folder_restore_sub_task_scribe_info: _descriptor.FieldDescriptor
    RESTORE_FOLDER_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_folder_status_vec: _containers.RepeatedCompositeFieldContainer[PublicFolderRestoreSubTaskScribeInfo.RestoreFolderStatus]
    def __init__(self, restore_folder_status_vec: _Optional[_Iterable[_Union[PublicFolderRestoreSubTaskScribeInfo.RestoreFolderStatus, _Mapping]]] = ...) -> None: ...

class OperationInfo(_message.Message):
    __slots__ = ("info_map",)
    class InfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    info_map: _containers.ScalarMap[str, str]
    def __init__(self, info_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TeamsRestoreInfo(_message.Message):
    __slots__ = ("status", "error", "teams_view_root_path", "teams_id", "priv_channels_info_vec", "priv_channels_site_params_vec", "group_restore_info", "new_team_created", "recover_public_channel_files", "should_create_private_channels")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[TeamsRestoreInfo.Status]
        kViewCloned: _ClassVar[TeamsRestoreInfo.Status]
        kPermitGranted: _ClassVar[TeamsRestoreInfo.Status]
        kRestoreFinished: _ClassVar[TeamsRestoreInfo.Status]
        kViewDeleted: _ClassVar[TeamsRestoreInfo.Status]
        kTeamsInfoFetched: _ClassVar[TeamsRestoreInfo.Status]
        kProgressMonitorsCreated: _ClassVar[TeamsRestoreInfo.Status]
    kStarted: TeamsRestoreInfo.Status
    kViewCloned: TeamsRestoreInfo.Status
    kPermitGranted: TeamsRestoreInfo.Status
    kRestoreFinished: TeamsRestoreInfo.Status
    kViewDeleted: TeamsRestoreInfo.Status
    kTeamsInfoFetched: TeamsRestoreInfo.Status
    kProgressMonitorsCreated: TeamsRestoreInfo.Status
    TEAMS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    teams_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEAMS_VIEW_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    PRIV_CHANNELS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIV_CHANNELS_SITE_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    NEW_TEAM_CREATED_FIELD_NUMBER: _ClassVar[int]
    RECOVER_PUBLIC_CHANNEL_FILES_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CREATE_PRIVATE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    status: TeamsRestoreInfo.Status
    error: _error_pb2.ErrorProto
    teams_view_root_path: str
    teams_id: str
    priv_channels_info_vec: _containers.RepeatedCompositeFieldContainer[O365RestoreInfo]
    priv_channels_site_params_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.RestoreSiteParams]
    group_restore_info: GroupRestoreInfo
    new_team_created: bool
    recover_public_channel_files: bool
    should_create_private_channels: bool
    def __init__(self, status: _Optional[_Union[TeamsRestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., teams_view_root_path: _Optional[str] = ..., teams_id: _Optional[str] = ..., priv_channels_info_vec: _Optional[_Iterable[_Union[O365RestoreInfo, _Mapping]]] = ..., priv_channels_site_params_vec: _Optional[_Iterable[_Union[_magneto_pb2.RestoreSiteParams, _Mapping]]] = ..., group_restore_info: _Optional[_Union[GroupRestoreInfo, _Mapping]] = ..., new_team_created: bool = ..., recover_public_channel_files: bool = ..., should_create_private_channels: bool = ...) -> None: ...

class GroupRestoreInfo(_message.Message):
    __slots__ = ("status", "group_view_root_path", "error", "group_config", "group_id", "group_owner", "outlook_restore_info", "outlook_entity_info", "group_smtp_address", "group_site_restore_info", "group_site_params", "include_site_restore", "new_group_created", "group_owner_smtp")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[GroupRestoreInfo.Status]
        kViewCloned: _ClassVar[GroupRestoreInfo.Status]
        kPermitGranted: _ClassVar[GroupRestoreInfo.Status]
        kRestoreFinished: _ClassVar[GroupRestoreInfo.Status]
        kViewDeleted: _ClassVar[GroupRestoreInfo.Status]
        kGroupMetadataRestored: _ClassVar[GroupRestoreInfo.Status]
        kReadGroupConfigDone: _ClassVar[GroupRestoreInfo.Status]
    kStarted: GroupRestoreInfo.Status
    kViewCloned: GroupRestoreInfo.Status
    kPermitGranted: GroupRestoreInfo.Status
    kRestoreFinished: GroupRestoreInfo.Status
    kViewDeleted: GroupRestoreInfo.Status
    kGroupMetadataRestored: GroupRestoreInfo.Status
    kReadGroupConfigDone: GroupRestoreInfo.Status
    GROUP_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    group_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GROUP_VIEW_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SITE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    NEW_GROUP_CREATED_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_SMTP_FIELD_NUMBER: _ClassVar[int]
    status: GroupRestoreInfo.Status
    group_view_root_path: str
    error: _error_pb2.ErrorProto
    group_config: O365GroupSparseConfig
    group_id: str
    group_owner: str
    outlook_restore_info: _outlook_pb2.RestoreInfo
    outlook_entity_info: _magneto_pb2.RestoreInfoProto.RestoreEntity
    group_smtp_address: str
    group_site_restore_info: O365RestoreInfo
    group_site_params: _magneto_pb2.RestoreSiteParams
    include_site_restore: bool
    new_group_created: bool
    group_owner_smtp: str
    def __init__(self, status: _Optional[_Union[GroupRestoreInfo.Status, str]] = ..., group_view_root_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., group_config: _Optional[_Union[O365GroupSparseConfig, _Mapping]] = ..., group_id: _Optional[str] = ..., group_owner: _Optional[str] = ..., outlook_restore_info: _Optional[_Union[_outlook_pb2.RestoreInfo, _Mapping]] = ..., outlook_entity_info: _Optional[_Union[_magneto_pb2.RestoreInfoProto.RestoreEntity, _Mapping]] = ..., group_smtp_address: _Optional[str] = ..., group_site_restore_info: _Optional[_Union[O365RestoreInfo, _Mapping]] = ..., group_site_params: _Optional[_Union[_magneto_pb2.RestoreSiteParams, _Mapping]] = ..., include_site_restore: bool = ..., new_group_created: bool = ..., group_owner_smtp: _Optional[str] = ...) -> None: ...

class O365ErrorDBEntry(_message.Message):
    __slots__ = ("drive_item", "outlook_item", "error_encountered", "o365_error_proto", "timestamp", "action_item")
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
    drive_item: _graph_pb2.DriveItem
    outlook_item: _outlook_pb2.SkippedItemInfo
    error_encountered: _error_pb2.ErrorProto
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    timestamp: int
    action_item: str
    def __init__(self, drive_item: _Optional[_Union[_graph_pb2.DriveItem, _Mapping]] = ..., outlook_item: _Optional[_Union[_outlook_pb2.SkippedItemInfo, _Mapping]] = ..., error_encountered: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., timestamp: _Optional[int] = ..., action_item: _Optional[str] = ...) -> None: ...

class SharepointListsRestoreInfo(_message.Message):
    __slots__ = ("status", "error", "view_root_path", "lists_dir_path", "lists_vec", "current_list_idx", "site_url", "domain_name", "lists_title_suffix", "current_item_key", "eof_items_db", "excluded_lists_id_vec", "num_warnings", "skipped_lists_title_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SharepointListsRestoreInfo.Status]
        kProgressMonitorsCreated: _ClassVar[SharepointListsRestoreInfo.Status]
        kFetchedListsMetadata: _ClassVar[SharepointListsRestoreInfo.Status]
        kListsCreated: _ClassVar[SharepointListsRestoreInfo.Status]
        kListItemsRestored: _ClassVar[SharepointListsRestoreInfo.Status]
    kStarted: SharepointListsRestoreInfo.Status
    kProgressMonitorsCreated: SharepointListsRestoreInfo.Status
    kFetchedListsMetadata: SharepointListsRestoreInfo.Status
    kListsCreated: SharepointListsRestoreInfo.Status
    kListItemsRestored: SharepointListsRestoreInfo.Status
    class ListsMap(_message.Message):
        __slots__ = ("original_id", "original_title", "target_id", "target_url", "target_item_entity_type_full_name")
        ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_TITLE_FIELD_NUMBER: _ClassVar[int]
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_URL_FIELD_NUMBER: _ClassVar[int]
        TARGET_ITEM_ENTITY_TYPE_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        original_id: str
        original_title: str
        target_id: str
        target_url: str
        target_item_entity_type_full_name: str
        def __init__(self, original_id: _Optional[str] = ..., original_title: _Optional[str] = ..., target_id: _Optional[str] = ..., target_url: _Optional[str] = ..., target_item_entity_type_full_name: _Optional[str] = ...) -> None: ...
    SHAREPOINT_LISTS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    sharepoint_lists_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    LISTS_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    LISTS_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIST_IDX_FIELD_NUMBER: _ClassVar[int]
    SITE_URL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    LISTS_TITLE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ITEM_KEY_FIELD_NUMBER: _ClassVar[int]
    EOF_ITEMS_DB_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_LISTS_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_LISTS_TITLE_VEC_FIELD_NUMBER: _ClassVar[int]
    status: SharepointListsRestoreInfo.Status
    error: _error_pb2.ErrorProto
    view_root_path: str
    lists_dir_path: str
    lists_vec: _containers.RepeatedCompositeFieldContainer[SharepointListsRestoreInfo.ListsMap]
    current_list_idx: int
    site_url: str
    domain_name: str
    lists_title_suffix: str
    current_item_key: str
    eof_items_db: bool
    excluded_lists_id_vec: _containers.RepeatedScalarFieldContainer[str]
    num_warnings: int
    skipped_lists_title_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[_Union[SharepointListsRestoreInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_root_path: _Optional[str] = ..., lists_dir_path: _Optional[str] = ..., lists_vec: _Optional[_Iterable[_Union[SharepointListsRestoreInfo.ListsMap, _Mapping]]] = ..., current_list_idx: _Optional[int] = ..., site_url: _Optional[str] = ..., domain_name: _Optional[str] = ..., lists_title_suffix: _Optional[str] = ..., current_item_key: _Optional[str] = ..., eof_items_db: bool = ..., excluded_lists_id_vec: _Optional[_Iterable[str]] = ..., num_warnings: _Optional[int] = ..., skipped_lists_title_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ChatsDownloadInfo(_message.Message):
    __slots__ = ("status", "view_root_path_vec", "view_info", "error", "num_files_created", "zip_ready_time_usecs", "total_size_to_zip_bytes")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ChatsDownloadInfo.Status]
        kViewCloned: _ClassVar[ChatsDownloadInfo.Status]
        kDownloadViewCreated: _ClassVar[ChatsDownloadInfo.Status]
        kDownloadHTMLReady: _ClassVar[ChatsDownloadInfo.Status]
        kClonedViewDeleted: _ClassVar[ChatsDownloadInfo.Status]
        kDownloadZipReady: _ClassVar[ChatsDownloadInfo.Status]
    kStarted: ChatsDownloadInfo.Status
    kViewCloned: ChatsDownloadInfo.Status
    kDownloadViewCreated: ChatsDownloadInfo.Status
    kDownloadHTMLReady: ChatsDownloadInfo.Status
    kClonedViewDeleted: ChatsDownloadInfo.Status
    kDownloadZipReady: ChatsDownloadInfo.Status
    class ChatsDownloadViewInfo(_message.Message):
        __slots__ = ("view_box_id", "view_name", "zip_file_path_in_view", "view_deleted")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        ZIP_FILE_PATH_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
        VIEW_DELETED_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        view_name: str
        zip_file_path_in_view: str
        view_deleted: bool
        def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., zip_file_path_in_view: _Optional[str] = ..., view_deleted: bool = ...) -> None: ...
    CHATS_DOWNLOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    chats_download_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_CREATED_FIELD_NUMBER: _ClassVar[int]
    ZIP_READY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_TO_ZIP_BYTES_FIELD_NUMBER: _ClassVar[int]
    status: ChatsDownloadInfo.Status
    view_root_path_vec: _containers.RepeatedScalarFieldContainer[str]
    view_info: ChatsDownloadInfo.ChatsDownloadViewInfo
    error: _error_pb2.ErrorProto
    num_files_created: int
    zip_ready_time_usecs: int
    total_size_to_zip_bytes: int
    def __init__(self, status: _Optional[_Union[ChatsDownloadInfo.Status, str]] = ..., view_root_path_vec: _Optional[_Iterable[str]] = ..., view_info: _Optional[_Union[ChatsDownloadInfo.ChatsDownloadViewInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., num_files_created: _Optional[int] = ..., zip_ready_time_usecs: _Optional[int] = ..., total_size_to_zip_bytes: _Optional[int] = ...) -> None: ...

class RestoreScribeInfo(_message.Message):
    __slots__ = ("entity_index", "channel_vec_index", "last_processed_key", "offset")
    O365_CHATS_DOWNLOAD_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    o365_chats_download_scribe_info: _descriptor.FieldDescriptor
    ENTITY_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_VEC_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_KEY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    entity_index: int
    channel_vec_index: int
    last_processed_key: str
    offset: int
    def __init__(self, entity_index: _Optional[int] = ..., channel_vec_index: _Optional[int] = ..., last_processed_key: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class AdapterSpecificFlags(_message.Message):
    __slots__ = ("is_rm_sharepoint_powershell_requests_enabled", "is_sharepoint_release_control_path_slot_enabled")
    SHAREPOINT_ADAPTER_FLAGS_FIELD_NUMBER: _ClassVar[int]
    sharepoint_adapter_flags: _descriptor.FieldDescriptor
    IS_RM_SHAREPOINT_POWERSHELL_REQUESTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SHAREPOINT_RELEASE_CONTROL_PATH_SLOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    is_rm_sharepoint_powershell_requests_enabled: bool
    is_sharepoint_release_control_path_slot_enabled: bool
    def __init__(self, is_rm_sharepoint_powershell_requests_enabled: bool = ..., is_sharepoint_release_control_path_slot_enabled: bool = ...) -> None: ...
