from resource_manager import api_pb2 as _api_pb2
from workqueue.base import error_pb2 as _error_pb2
from workqueue.base import workqueue_pb2 as _workqueue_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterWorkerArg(_message.Message):
    __slots__ = ("task_type", "worker_id", "worker_heartbeat_fail_crash_duration_msecs")
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_HEARTBEAT_FAIL_CRASH_DURATION_MSECS_FIELD_NUMBER: _ClassVar[int]
    task_type: _workqueue_pb2.TaskType
    worker_id: _workqueue_pb2.WorkerIncarnationProto
    worker_heartbeat_fail_crash_duration_msecs: int
    def __init__(self, task_type: _Optional[_Union[_workqueue_pb2.TaskType, _Mapping]] = ..., worker_id: _Optional[_Union[_workqueue_pb2.WorkerIncarnationProto, _Mapping]] = ..., worker_heartbeat_fail_crash_duration_msecs: _Optional[int] = ...) -> None: ...

class RegisterWorkerResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchIncarnationIdArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchIncarnationIdResult(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class WorkerToServerHeartbeatArg(_message.Message):
    __slots__ = ("worker_id",)
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    worker_id: _workqueue_pb2.WorkerIncarnationProto
    def __init__(self, worker_id: _Optional[_Union[_workqueue_pb2.WorkerIncarnationProto, _Mapping]] = ...) -> None: ...

class WorkerToServerHeartbeatResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WorkerToServerUpdateArg(_message.Message):
    __slots__ = ("worker_id", "msg_id", "task_status")
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    worker_id: _workqueue_pb2.WorkerIncarnationProto
    msg_id: int
    task_status: _containers.RepeatedCompositeFieldContainer[_workqueue_pb2.TaskStateProto]
    def __init__(self, worker_id: _Optional[_Union[_workqueue_pb2.WorkerIncarnationProto, _Mapping]] = ..., msg_id: _Optional[int] = ..., task_status: _Optional[_Iterable[_Union[_workqueue_pb2.TaskStateProto, _Mapping]]] = ...) -> None: ...

class WorkerToServerUpdateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchUpdateFromServerArg(_message.Message):
    __slots__ = ("worker",)
    WORKER_FIELD_NUMBER: _ClassVar[int]
    worker: _workqueue_pb2.WorkerIncarnationProto
    def __init__(self, worker: _Optional[_Union[_workqueue_pb2.WorkerIncarnationProto, _Mapping]] = ...) -> None: ...

class FetchUpdateFromServerResult(_message.Message):
    __slots__ = ("active_tasks",)
    ACTIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    active_tasks: _containers.RepeatedCompositeFieldContainer[_workqueue_pb2.TaskStateProto]
    def __init__(self, active_tasks: _Optional[_Iterable[_Union[_workqueue_pb2.TaskStateProto, _Mapping]]] = ...) -> None: ...

class CreateTaskGroupArg(_message.Message):
    __slots__ = ("uuid", "max_pending_tasks")
    UUID_FIELD_NUMBER: _ClassVar[int]
    MAX_PENDING_TASKS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    max_pending_tasks: int
    def __init__(self, uuid: _Optional[str] = ..., max_pending_tasks: _Optional[int] = ...) -> None: ...

class CreateTaskGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteTaskGroupArg(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class DeleteTaskGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AddTaskArg(_message.Message):
    __slots__ = ("task_uuid", "parent_task_id", "task_group_uuid", "task_type", "resource_acquisition_arg", "node_affinity", "task_payload_arg")
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ACQUISITION_ARG_FIELD_NUMBER: _ClassVar[int]
    NODE_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    TASK_PAYLOAD_ARG_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    parent_task_id: str
    task_group_uuid: str
    task_type: _workqueue_pb2.TaskType
    resource_acquisition_arg: _api_pb2.AcquireArg
    node_affinity: _workqueue_pb2.NodeAffinityProto
    task_payload_arg: bytes
    def __init__(self, task_uuid: _Optional[str] = ..., parent_task_id: _Optional[str] = ..., task_group_uuid: _Optional[str] = ..., task_type: _Optional[_Union[_workqueue_pb2.TaskType, _Mapping]] = ..., resource_acquisition_arg: _Optional[_Union[_api_pb2.AcquireArg, _Mapping]] = ..., node_affinity: _Optional[_Union[_workqueue_pb2.NodeAffinityProto, _Mapping]] = ..., task_payload_arg: _Optional[bytes] = ...) -> None: ...

class AddTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SubmitTasksArg(_message.Message):
    __slots__ = ("task_args",)
    TASK_ARGS_FIELD_NUMBER: _ClassVar[int]
    task_args: _containers.RepeatedCompositeFieldContainer[AddTaskArg]
    def __init__(self, task_args: _Optional[_Iterable[_Union[AddTaskArg, _Mapping]]] = ...) -> None: ...

class SubmitTasksResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetTaskGroupSummaryArg(_message.Message):
    __slots__ = ("task_group_uuid",)
    TASK_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    task_group_uuid: str
    def __init__(self, task_group_uuid: _Optional[str] = ...) -> None: ...

class GetTaskGroupSummaryResult(_message.Message):
    __slots__ = ("error", "summary")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    summary: _workqueue_pb2.TaskGroupSummaryProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., summary: _Optional[_Union[_workqueue_pb2.TaskGroupSummaryProto, _Mapping]] = ...) -> None: ...

class GetTaskResultArg(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class GetTaskResultResult(_message.Message):
    __slots__ = ("error", "task_uuid", "task_status", "result_payload")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_uuid: str
    task_status: _workqueue_pb2.TaskStatus.Type
    result_payload: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_uuid: _Optional[str] = ..., task_status: _Optional[_Union[_workqueue_pb2.TaskStatus.Type, str]] = ..., result_payload: _Optional[bytes] = ...) -> None: ...

class GetAllTaskResultArg(_message.Message):
    __slots__ = ("task_group_uuid", "start_task_index", "num_tasks")
    TASK_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    START_TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_TASKS_FIELD_NUMBER: _ClassVar[int]
    task_group_uuid: str
    start_task_index: int
    num_tasks: int
    def __init__(self, task_group_uuid: _Optional[str] = ..., start_task_index: _Optional[int] = ..., num_tasks: _Optional[int] = ...) -> None: ...

class GetAllTaskResultResult(_message.Message):
    __slots__ = ("error", "task_results")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_RESULTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_results: _containers.RepeatedCompositeFieldContainer[GetTaskResultResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_results: _Optional[_Iterable[_Union[GetTaskResultResult, _Mapping]]] = ...) -> None: ...

class WaitForTasksArg(_message.Message):
    __slots__ = ("task_id_set",)
    TASK_ID_SET_FIELD_NUMBER: _ClassVar[int]
    task_id_set: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, task_id_set: _Optional[_Iterable[str]] = ...) -> None: ...

class SingleTaskNotification(_message.Message):
    __slots__ = ("finished_task_result",)
    FINISHED_TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    finished_task_result: GetTaskResultResult
    def __init__(self, finished_task_result: _Optional[_Union[GetTaskResultResult, _Mapping]] = ...) -> None: ...

class DestroyFinishedTaskArg(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class DestroyFinishedTaskResult(_message.Message):
    __slots__ = ("error", "all_destroyed_tasks")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ALL_DESTROYED_TASKS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    all_destroyed_tasks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., all_destroyed_tasks: _Optional[_Iterable[str]] = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class CancelTaskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelTaskGroupArg(_message.Message):
    __slots__ = ("task_group_uuid", "cancel_descendant_task_groups")
    TASK_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_DESCENDANT_TASK_GROUPS_FIELD_NUMBER: _ClassVar[int]
    task_group_uuid: str
    cancel_descendant_task_groups: bool
    def __init__(self, task_group_uuid: _Optional[str] = ..., cancel_descendant_task_groups: bool = ...) -> None: ...

class CancelTaskGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RegisterForTaskGroupUpdatesArg(_message.Message):
    __slots__ = ("task_group_uuid", "max_num_failed_tasks", "progress_cb_interval_ms")
    TASK_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_FAILED_TASKS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_CB_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    task_group_uuid: str
    max_num_failed_tasks: int
    progress_cb_interval_ms: int
    def __init__(self, task_group_uuid: _Optional[str] = ..., max_num_failed_tasks: _Optional[int] = ..., progress_cb_interval_ms: _Optional[int] = ...) -> None: ...

class GetTaskCompletionNotificationArg(_message.Message):
    __slots__ = ("wait_for_tasks",)
    WAIT_FOR_TASKS_FIELD_NUMBER: _ClassVar[int]
    wait_for_tasks: WaitForTasksArg
    def __init__(self, wait_for_tasks: _Optional[_Union[WaitForTasksArg, _Mapping]] = ...) -> None: ...

class GetTaskCompletionNotificationResult(_message.Message):
    __slots__ = ("error", "task_notifications")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_notifications: _containers.RepeatedCompositeFieldContainer[SingleTaskNotification]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_notifications: _Optional[_Iterable[_Union[SingleTaskNotification, _Mapping]]] = ...) -> None: ...
