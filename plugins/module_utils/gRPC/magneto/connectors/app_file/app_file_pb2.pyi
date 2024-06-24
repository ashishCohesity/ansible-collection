from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.windows.base import file_attrs_pb2 as _file_attrs_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppFileInfoBase(_message.Message):
    __slots__ = ("uuid", "filepath", "snapshot_device_filepath", "capacity", "file_attributes", "encoded_filename")
    UUID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    filepath: str
    snapshot_device_filepath: str
    capacity: int
    file_attributes: _file_attrs_pb2.FileAttributes
    encoded_filename: str
    def __init__(self, uuid: _Optional[str] = ..., filepath: _Optional[str] = ..., snapshot_device_filepath: _Optional[str] = ..., capacity: _Optional[int] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ..., encoded_filename: _Optional[str] = ...) -> None: ...

class AppFile(_message.Message):
    __slots__ = ("key", "base", "delta_type", "delta_info", "last_position_backed_up", "total_bytes_read_from_source", "disk_area_start_offset", "query_disk_error", "should_skip_fetch_cbt")
    APP_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_info: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    SHOULD_SKIP_FETCH_CBT_FIELD_NUMBER: _ClassVar[int]
    key: int
    base: AppFileInfoBase
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    last_position_backed_up: int
    total_bytes_read_from_source: int
    disk_area_start_offset: int
    query_disk_error: _error_pb2.ErrorProto
    should_skip_fetch_cbt: bool
    def __init__(self, key: _Optional[int] = ..., base: _Optional[_Union[AppFileInfoBase, _Mapping]] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., disk_area_start_offset: _Optional[int] = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., should_skip_fetch_cbt: bool = ...) -> None: ...

class AppFileGroupInfo(_message.Message):
    __slots__ = ("group_dir_name", "file_info_vec", "sub_file_size_mb", "prev_snapshot_root_path", "relative_prev_snapshot_dir", "prev_snapshot_set_id", "first_sub_task_start_time_usecs", "last_sub_task_end_time_usecs", "batch_index", "public_status", "error", "total_logical_bytes", "total_bytes_read_from_source", "prev_group_dir_name", "is_small_files_group")
    class FileInfo(_message.Message):
        __slots__ = ("current_app_file", "prev_app_file", "should_delete", "should_skip", "subtask_unnecessary")
        CURRENT_APP_FILE_FIELD_NUMBER: _ClassVar[int]
        PREV_APP_FILE_FIELD_NUMBER: _ClassVar[int]
        SHOULD_DELETE_FIELD_NUMBER: _ClassVar[int]
        SHOULD_SKIP_FIELD_NUMBER: _ClassVar[int]
        SUBTASK_UNNECESSARY_FIELD_NUMBER: _ClassVar[int]
        current_app_file: AppFile
        prev_app_file: AppFile
        should_delete: bool
        should_skip: bool
        subtask_unnecessary: bool
        def __init__(self, current_app_file: _Optional[_Union[AppFile, _Mapping]] = ..., prev_app_file: _Optional[_Union[AppFile, _Mapping]] = ..., should_delete: bool = ..., should_skip: bool = ..., subtask_unnecessary: bool = ...) -> None: ...
    GROUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    PREV_SNAPSHOT_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PREV_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    PREV_SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_SUB_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_SUB_TASK_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    BATCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PREV_GROUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SMALL_FILES_GROUP_FIELD_NUMBER: _ClassVar[int]
    group_dir_name: str
    file_info_vec: _containers.RepeatedCompositeFieldContainer[AppFileGroupInfo.FileInfo]
    sub_file_size_mb: int
    prev_snapshot_root_path: str
    relative_prev_snapshot_dir: str
    prev_snapshot_set_id: bytes
    first_sub_task_start_time_usecs: int
    last_sub_task_end_time_usecs: int
    batch_index: int
    public_status: _enums_pb2.PublicTaskStatus.Type
    error: _error_pb2.ErrorProto
    total_logical_bytes: int
    total_bytes_read_from_source: int
    prev_group_dir_name: str
    is_small_files_group: bool
    def __init__(self, group_dir_name: _Optional[str] = ..., file_info_vec: _Optional[_Iterable[_Union[AppFileGroupInfo.FileInfo, _Mapping]]] = ..., sub_file_size_mb: _Optional[int] = ..., prev_snapshot_root_path: _Optional[str] = ..., relative_prev_snapshot_dir: _Optional[str] = ..., prev_snapshot_set_id: _Optional[bytes] = ..., first_sub_task_start_time_usecs: _Optional[int] = ..., last_sub_task_end_time_usecs: _Optional[int] = ..., batch_index: _Optional[int] = ..., public_status: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_logical_bytes: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., prev_group_dir_name: _Optional[str] = ..., is_small_files_group: bool = ...) -> None: ...

class BatchStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[BatchStatus.Type]
        kPrepareHostForSnapshotDone: _ClassVar[BatchStatus.Type]
        kSnapshotTaken: _ClassVar[BatchStatus.Type]
        kQueryChangedAreasDone: _ClassVar[BatchStatus.Type]
        kSubTasksCreated: _ClassVar[BatchStatus.Type]
        kSetupFilesFinished: _ClassVar[BatchStatus.Type]
        kSubTasksFinished: _ClassVar[BatchStatus.Type]
        kEndBackupFinished: _ClassVar[BatchStatus.Type]
    kStarted: BatchStatus.Type
    kPrepareHostForSnapshotDone: BatchStatus.Type
    kSnapshotTaken: BatchStatus.Type
    kQueryChangedAreasDone: BatchStatus.Type
    kSubTasksCreated: BatchStatus.Type
    kSetupFilesFinished: BatchStatus.Type
    kSubTasksFinished: BatchStatus.Type
    kEndBackupFinished: BatchStatus.Type
    def __init__(self) -> None: ...

class BatchInfo(_message.Message):
    __slots__ = ("status", "error", "server_snapshot_info_file_name", "server_snapshot_info", "server_snapshot_serialized_fetch_info", "snapshot_deletion_pending", "app_file_group_info_vec", "is_common_host_dir_cloned_under_app_file_groups", "sub_tasks_vec", "sub_tasks_id_start", "take_snapshot_error", "fetch_snapshot_metadata_error", "notify_backup_complete_error", "end_backup_error", "delete_snapshot_error", "next_file_key", "sub_task_group_vec")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_SERIALIZED_FETCH_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_PENDING_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_HOST_DIR_CLONED_UNDER_APP_FILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_ID_START_FIELD_NUMBER: _ClassVar[int]
    TAKE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    FETCH_SNAPSHOT_METADATA_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_ERROR_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELETE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    NEXT_FILE_KEY_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    status: BatchStatus.Type
    error: _error_pb2.ErrorProto
    server_snapshot_info_file_name: str
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    server_snapshot_serialized_fetch_info: _agent_pb2.ServerSnapshotSerializedFetchInfo
    snapshot_deletion_pending: bool
    app_file_group_info_vec: _containers.RepeatedCompositeFieldContainer[AppFileGroupInfo]
    is_common_host_dir_cloned_under_app_file_groups: bool
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    sub_tasks_id_start: int
    take_snapshot_error: _error_pb2.ErrorProto
    fetch_snapshot_metadata_error: _error_pb2.ErrorProto
    notify_backup_complete_error: _error_pb2.ErrorProto
    end_backup_error: _error_pb2.ErrorProto
    delete_snapshot_error: _error_pb2.ErrorProto
    next_file_key: int
    sub_task_group_vec: _containers.RepeatedCompositeFieldContainer[SubTaskGroup]
    def __init__(self, status: _Optional[_Union[BatchStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., server_snapshot_info_file_name: _Optional[str] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., server_snapshot_serialized_fetch_info: _Optional[_Union[_agent_pb2.ServerSnapshotSerializedFetchInfo, _Mapping]] = ..., snapshot_deletion_pending: bool = ..., app_file_group_info_vec: _Optional[_Iterable[_Union[AppFileGroupInfo, _Mapping]]] = ..., is_common_host_dir_cloned_under_app_file_groups: bool = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., sub_tasks_id_start: _Optional[int] = ..., take_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fetch_snapshot_metadata_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., notify_backup_complete_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., end_backup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delete_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., next_file_key: _Optional[int] = ..., sub_task_group_vec: _Optional[_Iterable[_Union[SubTaskGroup, _Mapping]]] = ...) -> None: ...

class SubTaskGroup(_message.Message):
    __slots__ = ("sub_task_idx_vec", "primary_sub_task", "current_sub_task_idx")
    SUB_TASK_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SUB_TASK_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    sub_task_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    primary_sub_task: _sub_task_pb2.SubTaskInfo
    current_sub_task_idx: int
    def __init__(self, sub_task_idx_vec: _Optional[_Iterable[int]] = ..., primary_sub_task: _Optional[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]] = ..., current_sub_task_idx: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("status", "error", "app_user_messages", "job_instance_id", "attempt_num", "server_snapshot_info", "server_snapshot_info_file_name", "common_host_dir_name", "server_snapshot_serialized_fetch_info", "host_summary", "agent_info", "app_file_group_info_vec", "is_common_host_dir_cloned_under_app_file_groups", "sub_tasks_vec", "take_snapshot_error", "fetch_snapshot_metadata_error", "notify_backup_complete_error", "end_backup_error", "snapshot_deletion_pending", "delete_snapshot_error", "abort_snapshot_error", "batch_info_vec", "current_batch_index", "is_source_side_dedup_enabled")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kPrepareHostForSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kSnapshotTaken: _ClassVar[SnapshotInfo.Status]
        kQueryChangedAreasDone: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kPrepareHostForSnapshotDone: SnapshotInfo.Status
    kSnapshotTaken: SnapshotInfo.Status
    kQueryChangedAreasDone: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    APP_FILE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMON_HOST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_SERIALIZED_FETCH_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_HOST_DIR_CLONED_UNDER_APP_FILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    TAKE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    FETCH_SNAPSHOT_METADATA_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_ERROR_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_PENDING_FIELD_NUMBER: _ClassVar[int]
    DELETE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    ABORT_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    BATCH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BATCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_SIDE_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    status: SnapshotInfo.Status
    error: _error_pb2.ErrorProto
    app_user_messages: _magneto_pb2.UserMessageProto
    job_instance_id: int
    attempt_num: int
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    server_snapshot_info_file_name: str
    common_host_dir_name: str
    server_snapshot_serialized_fetch_info: _agent_pb2.ServerSnapshotSerializedFetchInfo
    host_summary: _agent_pb2.SnapshotHostInfoSummary
    agent_info: _agent_pb2.AgentInfoProto
    app_file_group_info_vec: _containers.RepeatedCompositeFieldContainer[AppFileGroupInfo]
    is_common_host_dir_cloned_under_app_file_groups: bool
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    take_snapshot_error: _error_pb2.ErrorProto
    fetch_snapshot_metadata_error: _error_pb2.ErrorProto
    notify_backup_complete_error: _error_pb2.ErrorProto
    end_backup_error: _error_pb2.ErrorProto
    snapshot_deletion_pending: bool
    delete_snapshot_error: _error_pb2.ErrorProto
    abort_snapshot_error: _error_pb2.ErrorProto
    batch_info_vec: _containers.RepeatedCompositeFieldContainer[BatchInfo]
    current_batch_index: int
    is_source_side_dedup_enabled: bool
    def __init__(self, status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., server_snapshot_info_file_name: _Optional[str] = ..., common_host_dir_name: _Optional[str] = ..., server_snapshot_serialized_fetch_info: _Optional[_Union[_agent_pb2.ServerSnapshotSerializedFetchInfo, _Mapping]] = ..., host_summary: _Optional[_Union[_agent_pb2.SnapshotHostInfoSummary, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., app_file_group_info_vec: _Optional[_Iterable[_Union[AppFileGroupInfo, _Mapping]]] = ..., is_common_host_dir_cloned_under_app_file_groups: bool = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., take_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fetch_snapshot_metadata_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., notify_backup_complete_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., end_backup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_pending: bool = ..., delete_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., abort_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., batch_info_vec: _Optional[_Iterable[_Union[BatchInfo, _Mapping]]] = ..., current_batch_index: _Optional[int] = ..., is_source_side_dedup_enabled: bool = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ("app_file_vec",)
    APP_FILE_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_snapshot_scribe_info: _descriptor.FieldDescriptor
    APP_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    app_file_vec: _containers.RepeatedCompositeFieldContainer[AppFile]
    def __init__(self, app_file_vec: _Optional[_Iterable[_Union[AppFile, _Mapping]]] = ...) -> None: ...
