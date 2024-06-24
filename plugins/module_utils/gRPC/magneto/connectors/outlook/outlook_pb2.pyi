from magneto.agents.windows.stub import exchange_param_pb2 as _exchange_param_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.ms_graph import graph_pb2 as _graph_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.connectors.outlook import outlook_external_pb2 as _outlook_external_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FolderHierarchyChangeType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreate: _ClassVar[FolderHierarchyChangeType.Type]
        kUpdate: _ClassVar[FolderHierarchyChangeType.Type]
        kDelete: _ClassVar[FolderHierarchyChangeType.Type]
    kCreate: FolderHierarchyChangeType.Type
    kUpdate: FolderHierarchyChangeType.Type
    kDelete: FolderHierarchyChangeType.Type
    def __init__(self) -> None: ...

class FolderItemChangeType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreate: _ClassVar[FolderItemChangeType.Type]
        kUpdate: _ClassVar[FolderItemChangeType.Type]
        kDelete: _ClassVar[FolderItemChangeType.Type]
        kReadFlagChange: _ClassVar[FolderItemChangeType.Type]
    kCreate: FolderItemChangeType.Type
    kUpdate: FolderItemChangeType.Type
    kDelete: FolderItemChangeType.Type
    kReadFlagChange: FolderItemChangeType.Type
    def __init__(self) -> None: ...

class FolderRootInfo(_message.Message):
    __slots__ = ("folder_root_type", "sync_state")
    FOLDER_ROOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    folder_root_type: _outlook_external_pb2.FolderRootType.Type
    sync_state: str
    def __init__(self, folder_root_type: _Optional[_Union[_outlook_external_pb2.FolderRootType.Type, str]] = ..., sync_state: _Optional[str] = ...) -> None: ...

class Mailbox(_message.Message):
    __slots__ = ("primary_smtp_address", "guid", "display_name")
    PRIMARY_SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    primary_smtp_address: str
    guid: str
    display_name: str
    def __init__(self, primary_smtp_address: _Optional[str] = ..., guid: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class FileAttachment(_message.Message):
    __slots__ = ("content",)
    FILE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    file_attachment: _descriptor.FieldDescriptor
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class ItemAttachment(_message.Message):
    __slots__ = ("content",)
    ITEM_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    item_attachment: _descriptor.FieldDescriptor
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class ReferenceAttachment(_message.Message):
    __slots__ = ("path", "provider")
    REFERENCE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    reference_attachment: _descriptor.FieldDescriptor
    PATH_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    path: str
    provider: str
    def __init__(self, path: _Optional[str] = ..., provider: _Optional[str] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("item_meta_data", "data", "item_not_found", "externalized", "checksum", "expected_size")
    ITEM_META_DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ITEM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    EXTERNALIZED_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    item_meta_data: _outlook_external_pb2.ItemMetaData
    data: bytes
    item_not_found: bool
    externalized: bool
    checksum: bytes
    expected_size: int
    def __init__(self, item_meta_data: _Optional[_Union[_outlook_external_pb2.ItemMetaData, _Mapping]] = ..., data: _Optional[bytes] = ..., item_not_found: bool = ..., externalized: bool = ..., checksum: _Optional[bytes] = ..., expected_size: _Optional[int] = ...) -> None: ...

class FolderHierarchyChange(_message.Message):
    __slots__ = ("change_type", "folder_id", "folder_change_key", "parent_folder_id", "parent_folder_change_key", "display_name", "folder_type", "is_hidden", "folder_root_type", "total_count", "total_folder_size")
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_CHANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_CHANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FOLDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    change_type: FolderHierarchyChangeType.Type
    folder_id: str
    folder_change_key: str
    parent_folder_id: str
    parent_folder_change_key: str
    display_name: str
    folder_type: _outlook_external_pb2.FolderType.Type
    is_hidden: bool
    folder_root_type: _outlook_external_pb2.FolderRootType.Type
    total_count: int
    total_folder_size: int
    def __init__(self, change_type: _Optional[_Union[FolderHierarchyChangeType.Type, str]] = ..., folder_id: _Optional[str] = ..., folder_change_key: _Optional[str] = ..., parent_folder_id: _Optional[str] = ..., parent_folder_change_key: _Optional[str] = ..., display_name: _Optional[str] = ..., folder_type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., is_hidden: bool = ..., folder_root_type: _Optional[_Union[_outlook_external_pb2.FolderRootType.Type, str]] = ..., total_count: _Optional[int] = ..., total_folder_size: _Optional[int] = ...) -> None: ...

class FolderItemChange(_message.Message):
    __slots__ = ("change_type", "id", "change_key", "size", "skipped_item_info")
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    change_type: FolderItemChangeType.Type
    id: str
    change_key: str
    size: int
    skipped_item_info: SkippedItemInfo
    def __init__(self, change_type: _Optional[_Union[FolderItemChangeType.Type, str]] = ..., id: _Optional[str] = ..., change_key: _Optional[str] = ..., size: _Optional[int] = ..., skipped_item_info: _Optional[_Union[SkippedItemInfo, _Mapping]] = ...) -> None: ...

class SetupFolderInfo(_message.Message):
    __slots__ = ("folder_uuid", "should_delete", "should_recreate")
    FOLDER_UUID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DELETE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RECREATE_FIELD_NUMBER: _ClassVar[int]
    folder_uuid: str
    should_delete: bool
    should_recreate: bool
    def __init__(self, folder_uuid: _Optional[str] = ..., should_delete: bool = ..., should_recreate: bool = ...) -> None: ...

class FolderInfo(_message.Message):
    __slots__ = ("uuid", "parent_uuid", "display_name", "prev_sync_state", "num_create_items", "num_delete_items", "num_total_items", "is_excluded", "folder_type", "folder_key", "is_hidden", "folder_root_type", "is_skipped", "total_folder_size", "previous_snapshot_path_info", "is_failed", "skipped_item_change_vec", "incremental_folder_size", "is_indexed", "is_infinite_loop_detected")
    UUID_FIELD_NUMBER: _ClassVar[int]
    PARENT_UUID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PREV_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FOLDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_PATH_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_FAILED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_ITEM_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FOLDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_INDEXED_FIELD_NUMBER: _ClassVar[int]
    IS_INFINITE_LOOP_DETECTED_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    parent_uuid: str
    display_name: str
    prev_sync_state: str
    num_create_items: int
    num_delete_items: int
    num_total_items: int
    is_excluded: bool
    folder_type: _outlook_external_pb2.FolderType.Type
    folder_key: int
    is_hidden: bool
    folder_root_type: _outlook_external_pb2.FolderRootType.Type
    is_skipped: bool
    total_folder_size: int
    previous_snapshot_path_info: PreviousSnapshotPathInfo
    is_failed: bool
    skipped_item_change_vec: _containers.RepeatedCompositeFieldContainer[FolderItemChange]
    incremental_folder_size: int
    is_indexed: bool
    is_infinite_loop_detected: bool
    def __init__(self, uuid: _Optional[str] = ..., parent_uuid: _Optional[str] = ..., display_name: _Optional[str] = ..., prev_sync_state: _Optional[str] = ..., num_create_items: _Optional[int] = ..., num_delete_items: _Optional[int] = ..., num_total_items: _Optional[int] = ..., is_excluded: bool = ..., folder_type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., folder_key: _Optional[int] = ..., is_hidden: bool = ..., folder_root_type: _Optional[_Union[_outlook_external_pb2.FolderRootType.Type, str]] = ..., is_skipped: bool = ..., total_folder_size: _Optional[int] = ..., previous_snapshot_path_info: _Optional[_Union[PreviousSnapshotPathInfo, _Mapping]] = ..., is_failed: bool = ..., skipped_item_change_vec: _Optional[_Iterable[_Union[FolderItemChange, _Mapping]]] = ..., incremental_folder_size: _Optional[int] = ..., is_indexed: bool = ..., is_infinite_loop_detected: bool = ...) -> None: ...

class SparseMailboxConfig(_message.Message):
    __slots__ = ("folder_info_vec", "folder_root_info_vec", "max_folder_key")
    FOLDER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    folder_info_vec: _containers.RepeatedCompositeFieldContainer[FolderInfo]
    folder_root_info_vec: _containers.RepeatedCompositeFieldContainer[FolderRootInfo]
    max_folder_key: int
    def __init__(self, folder_info_vec: _Optional[_Iterable[_Union[FolderInfo, _Mapping]]] = ..., folder_root_info_vec: _Optional[_Iterable[_Union[FolderRootInfo, _Mapping]]] = ..., max_folder_key: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("status", "job_instance_id", "attempt_num", "sub_tasks_vec", "error", "folder_change_vec", "prev_mailbox_config", "curr_mailbox_config", "folder_hierarchy_sync_state", "max_folder_key", "incremental_fh_change_vec", "folder_root_info_vec", "started_after_62_upgrade", "started_after_63_upgrade", "group_owner_vec", "o365_error_proto", "backup_stat_details", "group_owner_smtp_address_vec", "mailbox_data_stats", "folders_data_distribution_table", "prev_status", "prev_state_start_time", "last_started_sub_task_idx")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kMailboxInfoFetched: _ClassVar[SnapshotInfo.Status]
        kPrepareMailboxFinished: _ClassVar[SnapshotInfo.Status]
        kFolderHierarchyFetched: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFoldersFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
        kCopyFailedFoldersFinished: _ClassVar[SnapshotInfo.Status]
        kGroupOwnersFetched: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kMailboxInfoFetched: SnapshotInfo.Status
    kPrepareMailboxFinished: SnapshotInfo.Status
    kFolderHierarchyFetched: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFoldersFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    kCopyFailedFoldersFinished: SnapshotInfo.Status
    kGroupOwnersFetched: SnapshotInfo.Status
    class BackupStatsDetail(_message.Message):
        __slots__ = ("op_stat_details_vec", "errored_item_info_vec")
        class OpName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kReadFilesOp: _ClassVar[SnapshotInfo.BackupStatsDetail.OpName]
        kReadFilesOp: SnapshotInfo.BackupStatsDetail.OpName
        class OpStatDetails(_message.Message):
            __slots__ = ("op_name", "count", "average_throughput", "rolling_throughput")
            OP_NAME_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            AVERAGE_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
            ROLLING_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
            op_name: SnapshotInfo.BackupStatsDetail.OpName
            count: int
            average_throughput: float
            rolling_throughput: float
            def __init__(self, op_name: _Optional[_Union[SnapshotInfo.BackupStatsDetail.OpName, str]] = ..., count: _Optional[int] = ..., average_throughput: _Optional[float] = ..., rolling_throughput: _Optional[float] = ...) -> None: ...
        class ErroredItemInfo(_message.Message):
            __slots__ = ("error_reason",)
            ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
            error_reason: str
            def __init__(self, error_reason: _Optional[str] = ...) -> None: ...
        OP_STAT_DETAILS_VEC_FIELD_NUMBER: _ClassVar[int]
        ERRORED_ITEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        op_stat_details_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.BackupStatsDetail.OpStatDetails]
        errored_item_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.BackupStatsDetail.ErroredItemInfo]
        def __init__(self, op_stat_details_vec: _Optional[_Iterable[_Union[SnapshotInfo.BackupStatsDetail.OpStatDetails, _Mapping]]] = ..., errored_item_info_vec: _Optional[_Iterable[_Union[SnapshotInfo.BackupStatsDetail.ErroredItemInfo, _Mapping]]] = ...) -> None: ...
    OUTLOOK_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    PREV_MAILBOX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CURR_MAILBOX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FOLDER_HIERARCHY_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    MAX_FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FH_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    STARTED_AFTER_62_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AFTER_63_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STAT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    GROUP_OWNER_SMTP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_DATA_DISTRIBUTION_TABLE_FIELD_NUMBER: _ClassVar[int]
    PREV_STATUS_FIELD_NUMBER: _ClassVar[int]
    PREV_STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_STARTED_SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    status: SnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    folder_change_vec: _containers.RepeatedCompositeFieldContainer[SetupFolderInfo]
    prev_mailbox_config: SparseMailboxConfig
    curr_mailbox_config: SparseMailboxConfig
    folder_hierarchy_sync_state: str
    max_folder_key: int
    incremental_fh_change_vec: _containers.RepeatedCompositeFieldContainer[IncrementalFolderHierarchyChange]
    folder_root_info_vec: _containers.RepeatedCompositeFieldContainer[FolderRootInfo]
    started_after_62_upgrade: bool
    started_after_63_upgrade: bool
    group_owner_vec: _containers.RepeatedScalarFieldContainer[str]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    backup_stat_details: SnapshotInfo.BackupStatsDetail
    group_owner_smtp_address_vec: _containers.RepeatedScalarFieldContainer[str]
    mailbox_data_stats: MailboxDataStats
    folders_data_distribution_table: _graph_pb2.DataDistributionTable
    prev_status: SnapshotInfo.Status
    prev_state_start_time: int
    last_started_sub_task_idx: int
    def __init__(self, status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_change_vec: _Optional[_Iterable[_Union[SetupFolderInfo, _Mapping]]] = ..., prev_mailbox_config: _Optional[_Union[SparseMailboxConfig, _Mapping]] = ..., curr_mailbox_config: _Optional[_Union[SparseMailboxConfig, _Mapping]] = ..., folder_hierarchy_sync_state: _Optional[str] = ..., max_folder_key: _Optional[int] = ..., incremental_fh_change_vec: _Optional[_Iterable[_Union[IncrementalFolderHierarchyChange, _Mapping]]] = ..., folder_root_info_vec: _Optional[_Iterable[_Union[FolderRootInfo, _Mapping]]] = ..., started_after_62_upgrade: bool = ..., started_after_63_upgrade: bool = ..., group_owner_vec: _Optional[_Iterable[str]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., backup_stat_details: _Optional[_Union[SnapshotInfo.BackupStatsDetail, _Mapping]] = ..., group_owner_smtp_address_vec: _Optional[_Iterable[str]] = ..., mailbox_data_stats: _Optional[_Union[MailboxDataStats, _Mapping]] = ..., folders_data_distribution_table: _Optional[_Union[_graph_pb2.DataDistributionTable, _Mapping]] = ..., prev_status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., prev_state_start_time: _Optional[int] = ..., last_started_sub_task_idx: _Optional[int] = ...) -> None: ...

class OutlookSubTaskInfo(_message.Message):
    __slots__ = ("folder_idx", "total_rocksdb_folder_size")
    OUTLOOK_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_sub_task_info: _descriptor.FieldDescriptor
    FOLDER_IDX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROCKSDB_FOLDER_SIZE_FIELD_NUMBER: _ClassVar[int]
    folder_idx: int
    total_rocksdb_folder_size: int
    def __init__(self, folder_idx: _Optional[int] = ..., total_rocksdb_folder_size: _Optional[int] = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ()
    OUTLOOK_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_snapshot_scribe_info: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class OutlookSubTaskScribeInfo(_message.Message):
    __slots__ = ("prev_sync_state", "change_list_info_vec", "num_backed_up_items", "size_backed_up_items", "num_created_items", "num_deleted_items", "backup_folder_error", "snapfs_pending_change_list_vec", "incremental_file_offset", "incremental_write_error", "is_first_backup_batch", "subtask_start_time_usecs", "skipped_item_change_vec", "is_incremental_backup")
    class FolderChangeListInfo(_message.Message):
        __slots__ = ("folder_item_change_vec", "size")
        FOLDER_ITEM_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        folder_item_change_vec: _containers.RepeatedCompositeFieldContainer[FolderItemChange]
        size: int
        def __init__(self, folder_item_change_vec: _Optional[_Iterable[_Union[FolderItemChange, _Mapping]]] = ..., size: _Optional[int] = ...) -> None: ...
    OUTLOOK_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_sub_task_scribe_info: _descriptor.FieldDescriptor
    PREV_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_LIST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FOLDER_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPFS_PENDING_CHANGE_LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_WRITE_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_BACKUP_BATCH_FIELD_NUMBER: _ClassVar[int]
    SUBTASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_ITEM_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_INCREMENTAL_BACKUP_FIELD_NUMBER: _ClassVar[int]
    prev_sync_state: str
    change_list_info_vec: _containers.RepeatedCompositeFieldContainer[OutlookSubTaskScribeInfo.FolderChangeListInfo]
    num_backed_up_items: int
    size_backed_up_items: int
    num_created_items: int
    num_deleted_items: int
    backup_folder_error: _error_pb2.ErrorProto
    snapfs_pending_change_list_vec: _containers.RepeatedCompositeFieldContainer[OutlookSubTaskScribeInfo.FolderChangeListInfo]
    incremental_file_offset: int
    incremental_write_error: _error_pb2.ErrorProto
    is_first_backup_batch: bool
    subtask_start_time_usecs: int
    skipped_item_change_vec: _containers.RepeatedCompositeFieldContainer[FolderItemChange]
    is_incremental_backup: bool
    def __init__(self, prev_sync_state: _Optional[str] = ..., change_list_info_vec: _Optional[_Iterable[_Union[OutlookSubTaskScribeInfo.FolderChangeListInfo, _Mapping]]] = ..., num_backed_up_items: _Optional[int] = ..., size_backed_up_items: _Optional[int] = ..., num_created_items: _Optional[int] = ..., num_deleted_items: _Optional[int] = ..., backup_folder_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapfs_pending_change_list_vec: _Optional[_Iterable[_Union[OutlookSubTaskScribeInfo.FolderChangeListInfo, _Mapping]]] = ..., incremental_file_offset: _Optional[int] = ..., incremental_write_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_first_backup_batch: bool = ..., subtask_start_time_usecs: _Optional[int] = ..., skipped_item_change_vec: _Optional[_Iterable[_Union[FolderItemChange, _Mapping]]] = ..., is_incremental_backup: bool = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("status", "view_root_path_vec", "sub_tasks_vec", "error", "non_email_restore_folder_name_prefix")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.Status]
        kViewCloned: _ClassVar[RestoreInfo.Status]
        kSubTasksFinished: _ClassVar[RestoreInfo.Status]
        kViewDeleted: _ClassVar[RestoreInfo.Status]
    kStarted: RestoreInfo.Status
    kViewCloned: RestoreInfo.Status
    kSubTasksFinished: RestoreInfo.Status
    kViewDeleted: RestoreInfo.Status
    OUTLOOK_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NON_EMAIL_RESTORE_FOLDER_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    status: RestoreInfo.Status
    view_root_path_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    non_email_restore_folder_name_prefix: str
    def __init__(self, status: _Optional[_Union[RestoreInfo.Status, str]] = ..., view_root_path_vec: _Optional[_Iterable[str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., non_email_restore_folder_name_prefix: _Optional[str] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("mail_box_config", "folder_status_vec")
    class FolderStatus(_message.Message):
        __slots__ = ("folder_info", "restore_completed", "sub_task_idx", "source_root_path", "src_relative_path", "src_folder_id", "dest_mailbox_entity", "dest_folder_path_vec", "dest_folder_id", "item_id_vec", "last_restored_key", "next_index_to_restore", "error", "sub_task_completed", "pst_view_dest_folder_path_vec", "dest_folder_path_type_vec", "num_skipped_items")
        FOLDER_INFO_FIELD_NUMBER: _ClassVar[int]
        RESTORE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
        SRC_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        SRC_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        DEST_MAILBOX_ENTITY_FIELD_NUMBER: _ClassVar[int]
        DEST_FOLDER_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        DEST_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        LAST_RESTORED_KEY_FIELD_NUMBER: _ClassVar[int]
        NEXT_INDEX_TO_RESTORE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        PST_VIEW_DEST_FOLDER_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        DEST_FOLDER_PATH_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        NUM_SKIPPED_ITEMS_FIELD_NUMBER: _ClassVar[int]
        folder_info: FolderInfo
        restore_completed: bool
        sub_task_idx: int
        source_root_path: str
        src_relative_path: str
        src_folder_id: str
        dest_mailbox_entity: _o365_pb2.Entity
        dest_folder_path_vec: _containers.RepeatedScalarFieldContainer[str]
        dest_folder_id: str
        item_id_vec: _containers.RepeatedScalarFieldContainer[str]
        last_restored_key: str
        next_index_to_restore: int
        error: _error_pb2.ErrorProto
        sub_task_completed: bool
        pst_view_dest_folder_path_vec: _containers.RepeatedScalarFieldContainer[str]
        dest_folder_path_type_vec: _containers.RepeatedScalarFieldContainer[_outlook_external_pb2.FolderType.Type]
        num_skipped_items: int
        def __init__(self, folder_info: _Optional[_Union[FolderInfo, _Mapping]] = ..., restore_completed: bool = ..., sub_task_idx: _Optional[int] = ..., source_root_path: _Optional[str] = ..., src_relative_path: _Optional[str] = ..., src_folder_id: _Optional[str] = ..., dest_mailbox_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., dest_folder_path_vec: _Optional[_Iterable[str]] = ..., dest_folder_id: _Optional[str] = ..., item_id_vec: _Optional[_Iterable[str]] = ..., last_restored_key: _Optional[str] = ..., next_index_to_restore: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sub_task_completed: bool = ..., pst_view_dest_folder_path_vec: _Optional[_Iterable[str]] = ..., dest_folder_path_type_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderType.Type, str]]] = ..., num_skipped_items: _Optional[int] = ...) -> None: ...
    OUTLOOK_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    outlook_restore_entity_info: _descriptor.FieldDescriptor
    MAIL_BOX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FOLDER_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    mail_box_config: SparseMailboxConfig
    folder_status_vec: _containers.RepeatedCompositeFieldContainer[RestoreEntityInfo.FolderStatus]
    def __init__(self, mail_box_config: _Optional[_Union[SparseMailboxConfig, _Mapping]] = ..., folder_status_vec: _Optional[_Iterable[_Union[RestoreEntityInfo.FolderStatus, _Mapping]]] = ...) -> None: ...

class IncrementalChangesFileHeader(_message.Message):
    __slots__ = ("magic_number", "is_valid", "payload_offset")
    MAGIC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    magic_number: int
    is_valid: int
    payload_offset: int
    def __init__(self, magic_number: _Optional[int] = ..., is_valid: _Optional[int] = ..., payload_offset: _Optional[int] = ...) -> None: ...

class IncrementalFolderHierarchyChange(_message.Message):
    __slots__ = ("folder_key", "display_name", "change_type")
    FOLDER_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    folder_key: int
    display_name: str
    change_type: FolderHierarchyChangeType.Type
    def __init__(self, folder_key: _Optional[int] = ..., display_name: _Optional[str] = ..., change_type: _Optional[_Union[FolderHierarchyChangeType.Type, str]] = ...) -> None: ...

class IncrementalFolderItemChange(_message.Message):
    __slots__ = ("id", "change_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    change_type: FolderItemChangeType.Type
    def __init__(self, id: _Optional[str] = ..., change_type: _Optional[_Union[FolderItemChangeType.Type, str]] = ...) -> None: ...

class PreviousSnapshotPathInfo(_message.Message):
    __slots__ = ("job_id", "job_instance_id", "attempt_num", "view_name")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    job_instance_id: int
    attempt_num: int
    view_name: str
    def __init__(self, job_id: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., view_name: _Optional[str] = ...) -> None: ...

class FolderTraversalType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kShallow: _ClassVar[FolderTraversalType.Type]
        kDeep: _ClassVar[FolderTraversalType.Type]
        kSoftDeleted: _ClassVar[FolderTraversalType.Type]
    kShallow: FolderTraversalType.Type
    kDeep: FolderTraversalType.Type
    kSoftDeleted: FolderTraversalType.Type
    def __init__(self) -> None: ...

class FieldUriType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFolderFolderId: _ClassVar[FieldUriType.Type]
        kFolderDisplayName: _ClassVar[FieldUriType.Type]
        kFolderChildFolderCount: _ClassVar[FieldUriType.Type]
        kFolderFolderClass: _ClassVar[FieldUriType.Type]
        kFolderPermissionSet: _ClassVar[FieldUriType.Type]
        kFolderTotalCount: _ClassVar[FieldUriType.Type]
    kFolderFolderId: FieldUriType.Type
    kFolderDisplayName: FieldUriType.Type
    kFolderChildFolderCount: FieldUriType.Type
    kFolderFolderClass: FieldUriType.Type
    kFolderPermissionSet: FieldUriType.Type
    kFolderTotalCount: FieldUriType.Type
    def __init__(self) -> None: ...

class BaseShapeType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIdOnly: _ClassVar[BaseShapeType.Type]
        kDefault: _ClassVar[BaseShapeType.Type]
        kAllProperties: _ClassVar[BaseShapeType.Type]
    kIdOnly: BaseShapeType.Type
    kDefault: BaseShapeType.Type
    kAllProperties: BaseShapeType.Type
    def __init__(self) -> None: ...

class DistinguishedFolderIdIdType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPublicFoldersRoot: _ClassVar[DistinguishedFolderIdIdType.Type]
        kCalendar: _ClassVar[DistinguishedFolderIdIdType.Type]
        kMsgFolderRoot: _ClassVar[DistinguishedFolderIdIdType.Type]
        kArchiveMsgFolderRoot: _ClassVar[DistinguishedFolderIdIdType.Type]
        kRecoverableItemsRoot: _ClassVar[DistinguishedFolderIdIdType.Type]
        kArchiveRecoverableItemsRoot: _ClassVar[DistinguishedFolderIdIdType.Type]
    kPublicFoldersRoot: DistinguishedFolderIdIdType.Type
    kCalendar: DistinguishedFolderIdIdType.Type
    kMsgFolderRoot: DistinguishedFolderIdIdType.Type
    kArchiveMsgFolderRoot: DistinguishedFolderIdIdType.Type
    kRecoverableItemsRoot: DistinguishedFolderIdIdType.Type
    kArchiveRecoverableItemsRoot: DistinguishedFolderIdIdType.Type
    def __init__(self) -> None: ...

class IndexedPageFolderView(_message.Message):
    __slots__ = ("max_entries_returned", "offset", "base_point")
    class IndexBasePointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBeginning: _ClassVar[IndexedPageFolderView.IndexBasePointType]
        kEnd: _ClassVar[IndexedPageFolderView.IndexBasePointType]
    kBeginning: IndexedPageFolderView.IndexBasePointType
    kEnd: IndexedPageFolderView.IndexBasePointType
    MAX_ENTRIES_RETURNED_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    BASE_POINT_FIELD_NUMBER: _ClassVar[int]
    max_entries_returned: int
    offset: int
    base_point: IndexedPageFolderView.IndexBasePointType
    def __init__(self, max_entries_returned: _Optional[int] = ..., offset: _Optional[int] = ..., base_point: _Optional[_Union[IndexedPageFolderView.IndexBasePointType, str]] = ...) -> None: ...

class DistinguishedFolderId(_message.Message):
    __slots__ = ("id", "change_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    id: DistinguishedFolderIdIdType.Type
    change_key: str
    def __init__(self, id: _Optional[_Union[DistinguishedFolderIdIdType.Type, str]] = ..., change_key: _Optional[str] = ...) -> None: ...

class TargetFolderId(_message.Message):
    __slots__ = ("folder_id", "distinguished_folder_id")
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    folder_id: _outlook_external_pb2.FolderId
    distinguished_folder_id: DistinguishedFolderId
    def __init__(self, folder_id: _Optional[_Union[_outlook_external_pb2.FolderId, _Mapping]] = ..., distinguished_folder_id: _Optional[_Union[DistinguishedFolderId, _Mapping]] = ...) -> None: ...

class Restriction(_message.Message):
    __slots__ = ("is_equal_to",)
    class IsEqualTo(_message.Message):
        __slots__ = ("field_uri_type", "constant")
        FIELD_URI_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONSTANT_FIELD_NUMBER: _ClassVar[int]
        field_uri_type: FieldUriType.Type
        constant: str
        def __init__(self, field_uri_type: _Optional[_Union[FieldUriType.Type, str]] = ..., constant: _Optional[str] = ...) -> None: ...
    IS_EQUAL_TO_FIELD_NUMBER: _ClassVar[int]
    is_equal_to: Restriction.IsEqualTo
    def __init__(self, is_equal_to: _Optional[_Union[Restriction.IsEqualTo, _Mapping]] = ...) -> None: ...

class SetFolderField(_message.Message):
    __slots__ = ("field_uri_type", "folder")
    FIELD_URI_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    field_uri_type: FieldUriType.Type
    folder: _outlook_external_pb2.FolderContentInfo
    def __init__(self, field_uri_type: _Optional[_Union[FieldUriType.Type, str]] = ..., folder: _Optional[_Union[_outlook_external_pb2.FolderContentInfo, _Mapping]] = ...) -> None: ...

class DeleteFolderField(_message.Message):
    __slots__ = ("field_uri_type",)
    FIELD_URI_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_uri_type: FieldUriType.Type
    def __init__(self, field_uri_type: _Optional[_Union[FieldUriType.Type, str]] = ...) -> None: ...

class FolderUpdate(_message.Message):
    __slots__ = ("set_folder_field", "delete_folder_field")
    SET_FOLDER_FIELD_FIELD_NUMBER: _ClassVar[int]
    DELETE_FOLDER_FIELD_FIELD_NUMBER: _ClassVar[int]
    set_folder_field: SetFolderField
    delete_folder_field: DeleteFolderField
    def __init__(self, set_folder_field: _Optional[_Union[SetFolderField, _Mapping]] = ..., delete_folder_field: _Optional[_Union[DeleteFolderField, _Mapping]] = ...) -> None: ...

class FolderChange(_message.Message):
    __slots__ = ("target_folder_id", "folder_update_vec")
    TARGET_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    target_folder_id: TargetFolderId
    folder_update_vec: _containers.RepeatedCompositeFieldContainer[FolderUpdate]
    def __init__(self, target_folder_id: _Optional[_Union[TargetFolderId, _Mapping]] = ..., folder_update_vec: _Optional[_Iterable[_Union[FolderUpdate, _Mapping]]] = ...) -> None: ...

class PstConvertInfo(_message.Message):
    __slots__ = ("status", "view_root_path_vec", "view_info", "pst_convert_result", "error", "sub_tasks_vec", "non_email_restore_folder_name_prefix", "pst_ready_time_usecs", "total_size_to_convert_bytes")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[PstConvertInfo.Status]
        kViewCloned: _ClassVar[PstConvertInfo.Status]
        kPstViewCreated: _ClassVar[PstConvertInfo.Status]
        kPstViewReady: _ClassVar[PstConvertInfo.Status]
        kClonedViewDeleted: _ClassVar[PstConvertInfo.Status]
        kMountPstViewDone: _ClassVar[PstConvertInfo.Status]
        kConversionStarted: _ClassVar[PstConvertInfo.Status]
        kConversionDone: _ClassVar[PstConvertInfo.Status]
        kConversionCancelDone: _ClassVar[PstConvertInfo.Status]
        kPstReady: _ClassVar[PstConvertInfo.Status]
        kZipCreated: _ClassVar[PstConvertInfo.Status]
    kStarted: PstConvertInfo.Status
    kViewCloned: PstConvertInfo.Status
    kPstViewCreated: PstConvertInfo.Status
    kPstViewReady: PstConvertInfo.Status
    kClonedViewDeleted: PstConvertInfo.Status
    kMountPstViewDone: PstConvertInfo.Status
    kConversionStarted: PstConvertInfo.Status
    kConversionDone: PstConvertInfo.Status
    kConversionCancelDone: PstConvertInfo.Status
    kPstReady: PstConvertInfo.Status
    kZipCreated: PstConvertInfo.Status
    class PstConvertViewInfo(_message.Message):
        __slots__ = ("view_box_id", "view_name", "zip_file_path_in_view", "view_deleted", "mounted_view_path", "ews_input_path", "pst_output_path")
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        ZIP_FILE_PATH_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
        VIEW_DELETED_FIELD_NUMBER: _ClassVar[int]
        MOUNTED_VIEW_PATH_FIELD_NUMBER: _ClassVar[int]
        EWS_INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
        PST_OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
        view_box_id: int
        view_name: str
        zip_file_path_in_view: str
        view_deleted: bool
        mounted_view_path: str
        ews_input_path: str
        pst_output_path: str
        def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., zip_file_path_in_view: _Optional[str] = ..., view_deleted: bool = ..., mounted_view_path: _Optional[str] = ..., ews_input_path: _Optional[str] = ..., pst_output_path: _Optional[str] = ...) -> None: ...
    PST_CONVERT_INFO_FIELD_NUMBER: _ClassVar[int]
    pst_convert_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_INFO_FIELD_NUMBER: _ClassVar[int]
    PST_CONVERT_RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    NON_EMAIL_RESTORE_FOLDER_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PST_READY_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_TO_CONVERT_BYTES_FIELD_NUMBER: _ClassVar[int]
    status: PstConvertInfo.Status
    view_root_path_vec: _containers.RepeatedScalarFieldContainer[str]
    view_info: PstConvertInfo.PstConvertViewInfo
    pst_convert_result: _exchange_param_pb2.ConvertEwsToPstStatus
    error: _error_pb2.ErrorProto
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    non_email_restore_folder_name_prefix: str
    pst_ready_time_usecs: int
    total_size_to_convert_bytes: int
    def __init__(self, status: _Optional[_Union[PstConvertInfo.Status, str]] = ..., view_root_path_vec: _Optional[_Iterable[str]] = ..., view_info: _Optional[_Union[PstConvertInfo.PstConvertViewInfo, _Mapping]] = ..., pst_convert_result: _Optional[_Union[_exchange_param_pb2.ConvertEwsToPstStatus, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., non_email_restore_folder_name_prefix: _Optional[str] = ..., pst_ready_time_usecs: _Optional[int] = ..., total_size_to_convert_bytes: _Optional[int] = ...) -> None: ...

class MailboxDataStats(_message.Message):
    __slots__ = ("num_created_items", "num_deleted_items", "num_total_items", "num_created_folders", "num_deleted_folders", "num_updated_folders")
    NUM_CREATED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_UPDATED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    num_created_items: int
    num_deleted_items: int
    num_total_items: int
    num_created_folders: int
    num_deleted_folders: int
    num_updated_folders: int
    def __init__(self, num_created_items: _Optional[int] = ..., num_deleted_items: _Optional[int] = ..., num_total_items: _Optional[int] = ..., num_created_folders: _Optional[int] = ..., num_deleted_folders: _Optional[int] = ..., num_updated_folders: _Optional[int] = ...) -> None: ...

class SkippedItemInfo(_message.Message):
    __slots__ = ("id", "error_encountered", "o365_error_proto", "subject", "folder_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    error_encountered: _error_pb2.ErrorProto
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    subject: str
    folder_path: str
    def __init__(self, id: _Optional[str] = ..., error_encountered: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., subject: _Optional[str] = ..., folder_path: _Optional[str] = ..., **kwargs) -> None: ...
