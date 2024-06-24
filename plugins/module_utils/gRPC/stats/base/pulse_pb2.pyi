from stats.base import stats_types_pb2 as _stats_types_pb2
from stats.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskPrefix(_message.Message):
    __slots__ = ("add_node_task_prefix", "remove_node_task_prefix", "bridge_task_prefix", "scribe_task_prefix", "apollo_task_prefix", "magneto_backup_task_prefix", "magneto_clone_task_prefix", "magneto_recover_task_prefix", "magneto_restore_files_task_prefix", "magneto_restore_sql_task_prefix", "magneto_clone_view_task_prefix", "magneto_mount_volumes_task_prefix", "magneto_recover_san_volume_task_prefix", "magneto_recover_convert_and_deploy_task_prefix", "magneto_mount_nas_volume_task_prefix", "magneto_recover_volumes_task_prefix", "magneto_deploy_vms_task_prefix", "magneto_download_files_task_prefix", "magneto_recover_disks_task_prefix", "magneto_agents_upgrade_task_prefix", "nexus_task_prefix", "icebox_task_prefix", "yoda_indexing_prefix", "iris_task_prefix", "magneto_registration_task_prefix", "magneto_clone_protection_job_view_task_prefix", "magneto_recover_san_group_task_prefix")
    ADD_NODE_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REMOVE_NODE_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    APOLLO_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_BACKUP_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CLONE_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RECOVER_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RESTORE_FILES_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RESTORE_SQL_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CLONE_VIEW_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_MOUNT_VOLUMES_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RECOVER_SAN_VOLUME_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RECOVER_CONVERT_AND_DEPLOY_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_MOUNT_NAS_VOLUME_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RECOVER_VOLUMES_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_DEPLOY_VMS_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_DOWNLOAD_FILES_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RECOVER_DISKS_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_AGENTS_UPGRADE_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NEXUS_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ICEBOX_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    YODA_INDEXING_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IRIS_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_REGISTRATION_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_CLONE_PROTECTION_JOB_VIEW_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_RECOVER_SAN_GROUP_TASK_PREFIX_FIELD_NUMBER: _ClassVar[int]
    add_node_task_prefix: str
    remove_node_task_prefix: str
    bridge_task_prefix: str
    scribe_task_prefix: str
    apollo_task_prefix: str
    magneto_backup_task_prefix: str
    magneto_clone_task_prefix: str
    magneto_recover_task_prefix: str
    magneto_restore_files_task_prefix: str
    magneto_restore_sql_task_prefix: str
    magneto_clone_view_task_prefix: str
    magneto_mount_volumes_task_prefix: str
    magneto_recover_san_volume_task_prefix: str
    magneto_recover_convert_and_deploy_task_prefix: str
    magneto_mount_nas_volume_task_prefix: str
    magneto_recover_volumes_task_prefix: str
    magneto_deploy_vms_task_prefix: str
    magneto_download_files_task_prefix: str
    magneto_recover_disks_task_prefix: str
    magneto_agents_upgrade_task_prefix: str
    nexus_task_prefix: str
    icebox_task_prefix: str
    yoda_indexing_prefix: str
    iris_task_prefix: str
    magneto_registration_task_prefix: str
    magneto_clone_protection_job_view_task_prefix: str
    magneto_recover_san_group_task_prefix: str
    def __init__(self, add_node_task_prefix: _Optional[str] = ..., remove_node_task_prefix: _Optional[str] = ..., bridge_task_prefix: _Optional[str] = ..., scribe_task_prefix: _Optional[str] = ..., apollo_task_prefix: _Optional[str] = ..., magneto_backup_task_prefix: _Optional[str] = ..., magneto_clone_task_prefix: _Optional[str] = ..., magneto_recover_task_prefix: _Optional[str] = ..., magneto_restore_files_task_prefix: _Optional[str] = ..., magneto_restore_sql_task_prefix: _Optional[str] = ..., magneto_clone_view_task_prefix: _Optional[str] = ..., magneto_mount_volumes_task_prefix: _Optional[str] = ..., magneto_recover_san_volume_task_prefix: _Optional[str] = ..., magneto_recover_convert_and_deploy_task_prefix: _Optional[str] = ..., magneto_mount_nas_volume_task_prefix: _Optional[str] = ..., magneto_recover_volumes_task_prefix: _Optional[str] = ..., magneto_deploy_vms_task_prefix: _Optional[str] = ..., magneto_download_files_task_prefix: _Optional[str] = ..., magneto_recover_disks_task_prefix: _Optional[str] = ..., magneto_agents_upgrade_task_prefix: _Optional[str] = ..., nexus_task_prefix: _Optional[str] = ..., icebox_task_prefix: _Optional[str] = ..., yoda_indexing_prefix: _Optional[str] = ..., iris_task_prefix: _Optional[str] = ..., magneto_registration_task_prefix: _Optional[str] = ..., magneto_clone_protection_job_view_task_prefix: _Optional[str] = ..., magneto_recover_san_group_task_prefix: _Optional[str] = ...) -> None: ...

class EventLogsDirStructure(_message.Message):
    __slots__ = ("split_level", "split_width", "split_depth", "reverse_and_split")
    SPLIT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SPLIT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SPLIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    REVERSE_AND_SPLIT_FIELD_NUMBER: _ClassVar[int]
    split_level: int
    split_width: int
    split_depth: int
    reverse_and_split: bool
    def __init__(self, split_level: _Optional[int] = ..., split_width: _Optional[int] = ..., split_depth: _Optional[int] = ..., reverse_and_split: bool = ...) -> None: ...

class CreateTaskArg(_message.Message):
    __slots__ = ("task", "logs_dir_structure")
    class Task(_message.Message):
        __slots__ = ("task_path", "weight", "hung_task_timeout_secs", "attribute_vec", "disable_implicit_finish", "sub_task_vec")
        TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        HUNG_TASK_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        DISABLE_IMPLICIT_FINISH_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
        task_path: str
        weight: int
        hung_task_timeout_secs: int
        attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
        disable_implicit_finish: bool
        sub_task_vec: _containers.RepeatedCompositeFieldContainer[CreateTaskArg.Task]
        def __init__(self, task_path: _Optional[str] = ..., weight: _Optional[int] = ..., hung_task_timeout_secs: _Optional[int] = ..., attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., disable_implicit_finish: bool = ..., sub_task_vec: _Optional[_Iterable[_Union[CreateTaskArg.Task, _Mapping]]] = ...) -> None: ...
    TASK_FIELD_NUMBER: _ClassVar[int]
    LOGS_DIR_STRUCTURE_FIELD_NUMBER: _ClassVar[int]
    task: CreateTaskArg.Task
    logs_dir_structure: EventLogsDirStructure
    def __init__(self, task: _Optional[_Union[CreateTaskArg.Task, _Mapping]] = ..., logs_dir_structure: _Optional[_Union[EventLogsDirStructure, _Mapping]] = ...) -> None: ...

class CreateTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class TaskEvent(_message.Message):
    __slots__ = ("event_msg", "timestamp_secs", "owner_percent_finished", "owner_remaining_work_count")
    EVENT_MSG_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    OWNER_PERCENT_FINISHED_FIELD_NUMBER: _ClassVar[int]
    OWNER_REMAINING_WORK_COUNT_FIELD_NUMBER: _ClassVar[int]
    event_msg: str
    timestamp_secs: int
    owner_percent_finished: float
    owner_remaining_work_count: int
    def __init__(self, event_msg: _Optional[str] = ..., timestamp_secs: _Optional[int] = ..., owner_percent_finished: _Optional[float] = ..., owner_remaining_work_count: _Optional[int] = ...) -> None: ...

class ReportTaskProgressArg(_message.Message):
    __slots__ = ("task_vec",)
    class Task(_message.Message):
        __slots__ = ("task_path", "finished_ok", "finished_with_errors", "is_cancelled", "error_msg", "event_vec", "attribute_vec", "delete_previous_attributes", "percent_finished", "remaining_work_count", "completed_work_count", "unknown_remaining_work")
        TASK_PATH_FIELD_NUMBER: _ClassVar[int]
        FINISHED_OK_FIELD_NUMBER: _ClassVar[int]
        FINISHED_WITH_ERRORS_FIELD_NUMBER: _ClassVar[int]
        IS_CANCELLED_FIELD_NUMBER: _ClassVar[int]
        ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
        EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        DELETE_PREVIOUS_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        PERCENT_FINISHED_FIELD_NUMBER: _ClassVar[int]
        REMAINING_WORK_COUNT_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_WORK_COUNT_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_REMAINING_WORK_FIELD_NUMBER: _ClassVar[int]
        task_path: str
        finished_ok: bool
        finished_with_errors: bool
        is_cancelled: bool
        error_msg: str
        event_vec: _containers.RepeatedCompositeFieldContainer[TaskEvent]
        attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
        delete_previous_attributes: bool
        percent_finished: float
        remaining_work_count: int
        completed_work_count: int
        unknown_remaining_work: bool
        def __init__(self, task_path: _Optional[str] = ..., finished_ok: bool = ..., finished_with_errors: bool = ..., is_cancelled: bool = ..., error_msg: _Optional[str] = ..., event_vec: _Optional[_Iterable[_Union[TaskEvent, _Mapping]]] = ..., attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., delete_previous_attributes: bool = ..., percent_finished: _Optional[float] = ..., remaining_work_count: _Optional[int] = ..., completed_work_count: _Optional[int] = ..., unknown_remaining_work: bool = ...) -> None: ...
    TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    task_vec: _containers.RepeatedCompositeFieldContainer[ReportTaskProgressArg.Task]
    def __init__(self, task_vec: _Optional[_Iterable[_Union[ReportTaskProgressArg.Task, _Mapping]]] = ...) -> None: ...

class ReportTaskProgressResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class TaskStatus(_message.Message):
    __slots__ = ("type", "error_msg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kActive: _ClassVar[TaskStatus.Type]
        kFinished: _ClassVar[TaskStatus.Type]
        kFinishedWithError: _ClassVar[TaskStatus.Type]
        kCancelled: _ClassVar[TaskStatus.Type]
        kFinishedGarbageCollected: _ClassVar[TaskStatus.Type]
    kActive: TaskStatus.Type
    kFinished: TaskStatus.Type
    kFinishedWithError: TaskStatus.Type
    kCancelled: TaskStatus.Type
    kFinishedGarbageCollected: TaskStatus.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    type: TaskStatus.Type
    error_msg: str
    def __init__(self, type: _Optional[_Union[TaskStatus.Type, str]] = ..., error_msg: _Optional[str] = ...) -> None: ...

class TaskProgress(_message.Message):
    __slots__ = ("status", "start_time_secs", "end_time_secs", "percent_finished", "approx_percent_unknown_work", "last_update_time_secs", "expected_end_time_secs", "expected_time_remaining_secs", "event_vec", "attribute_vec", "expected_total_work_count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FINISHED_FIELD_NUMBER: _ClassVar[int]
    APPROX_PERCENT_UNKNOWN_WORK_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TIME_REMAINING_SECS_FIELD_NUMBER: _ClassVar[int]
    EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TOTAL_WORK_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: TaskStatus
    start_time_secs: int
    end_time_secs: int
    percent_finished: float
    approx_percent_unknown_work: float
    last_update_time_secs: int
    expected_end_time_secs: int
    expected_time_remaining_secs: int
    event_vec: _containers.RepeatedCompositeFieldContainer[TaskEvent]
    attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    expected_total_work_count: int
    def __init__(self, status: _Optional[_Union[TaskStatus, _Mapping]] = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., percent_finished: _Optional[float] = ..., approx_percent_unknown_work: _Optional[float] = ..., last_update_time_secs: _Optional[int] = ..., expected_end_time_secs: _Optional[int] = ..., expected_time_remaining_secs: _Optional[int] = ..., event_vec: _Optional[_Iterable[_Union[TaskEvent, _Mapping]]] = ..., attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., expected_total_work_count: _Optional[int] = ...) -> None: ...

class GetTasksArg(_message.Message):
    __slots__ = ("task_path_vec", "include_finished_tasks", "start_time_secs", "end_time_secs", "max_tasks", "exclude_sub_tasks", "attribute_vec", "include_event_logs", "fetch_logs_max_level")
    TASK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FINISHED_TASKS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    MAX_TASKS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SUB_TASKS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EVENT_LOGS_FIELD_NUMBER: _ClassVar[int]
    FETCH_LOGS_MAX_LEVEL_FIELD_NUMBER: _ClassVar[int]
    task_path_vec: _containers.RepeatedScalarFieldContainer[str]
    include_finished_tasks: bool
    start_time_secs: int
    end_time_secs: int
    max_tasks: int
    exclude_sub_tasks: bool
    attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    include_event_logs: bool
    fetch_logs_max_level: int
    def __init__(self, task_path_vec: _Optional[_Iterable[str]] = ..., include_finished_tasks: bool = ..., start_time_secs: _Optional[int] = ..., end_time_secs: _Optional[int] = ..., max_tasks: _Optional[int] = ..., exclude_sub_tasks: bool = ..., attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., include_event_logs: bool = ..., fetch_logs_max_level: _Optional[int] = ...) -> None: ...

class GetTasksResult(_message.Message):
    __slots__ = ("error", "result_group_vec")
    class ResultGroup(_message.Message):
        __slots__ = ("task_vec",)
        class Task(_message.Message):
            __slots__ = ("task_path", "progress", "sub_task_vec")
            TASK_PATH_FIELD_NUMBER: _ClassVar[int]
            PROGRESS_FIELD_NUMBER: _ClassVar[int]
            SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
            task_path: str
            progress: TaskProgress
            sub_task_vec: _containers.RepeatedCompositeFieldContainer[GetTasksResult.ResultGroup.Task]
            def __init__(self, task_path: _Optional[str] = ..., progress: _Optional[_Union[TaskProgress, _Mapping]] = ..., sub_task_vec: _Optional[_Iterable[_Union[GetTasksResult.ResultGroup.Task, _Mapping]]] = ...) -> None: ...
        TASK_VEC_FIELD_NUMBER: _ClassVar[int]
        task_vec: _containers.RepeatedCompositeFieldContainer[GetTasksResult.ResultGroup.Task]
        def __init__(self, task_vec: _Optional[_Iterable[_Union[GetTasksResult.ResultGroup.Task, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    result_group_vec: _containers.RepeatedCompositeFieldContainer[GetTasksResult.ResultGroup]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., result_group_vec: _Optional[_Iterable[_Union[GetTasksResult.ResultGroup, _Mapping]]] = ...) -> None: ...
