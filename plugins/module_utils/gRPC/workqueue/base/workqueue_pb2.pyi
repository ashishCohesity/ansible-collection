from workqueue.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskType(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TaskType.Type]
        kNumberGeneratorTest: _ClassVar[TaskType.Type]
        kO365BackupTask: _ClassVar[TaskType.Type]
        kO365RecoveryTask: _ClassVar[TaskType.Type]
        kGenericBackupTask: _ClassVar[TaskType.Type]
    kUnknown: TaskType.Type
    kNumberGeneratorTest: TaskType.Type
    kO365BackupTask: TaskType.Type
    kO365RecoveryTask: TaskType.Type
    kGenericBackupTask: TaskType.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: TaskType.Type
    def __init__(self, type: _Optional[_Union[TaskType.Type, str]] = ...) -> None: ...

class TaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TaskStatus.Type]
        kInitializing: _ClassVar[TaskStatus.Type]
        kWaitingForResources: _ClassVar[TaskStatus.Type]
        kWaitingForWorkerAssignment: _ClassVar[TaskStatus.Type]
        kRunning: _ClassVar[TaskStatus.Type]
        kWaitingForCancellation: _ClassVar[TaskStatus.Type]
        kFinished: _ClassVar[TaskStatus.Type]
    kUnknown: TaskStatus.Type
    kInitializing: TaskStatus.Type
    kWaitingForResources: TaskStatus.Type
    kWaitingForWorkerAssignment: TaskStatus.Type
    kRunning: TaskStatus.Type
    kWaitingForCancellation: TaskStatus.Type
    kFinished: TaskStatus.Type
    def __init__(self) -> None: ...

class PodNodeAffinityProto(_message.Message):
    __slots__ = ("pod_name", "node_affinity_label")
    POD_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_AFFINITY_LABEL_FIELD_NUMBER: _ClassVar[int]
    pod_name: str
    node_affinity_label: str
    def __init__(self, pod_name: _Optional[str] = ..., node_affinity_label: _Optional[str] = ...) -> None: ...

class NodeAffinityProto(_message.Message):
    __slots__ = ("node_affinity_label", "pod_node_affinity")
    NODE_AFFINITY_LABEL_FIELD_NUMBER: _ClassVar[int]
    POD_NODE_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    node_affinity_label: str
    pod_node_affinity: _containers.RepeatedCompositeFieldContainer[PodNodeAffinityProto]
    def __init__(self, node_affinity_label: _Optional[str] = ..., pod_node_affinity: _Optional[_Iterable[_Union[PodNodeAffinityProto, _Mapping]]] = ...) -> None: ...

class TaskGroupSummaryProto(_message.Message):
    __slots__ = ("task_status_count_vec",)
    class TaskStatusCount(_message.Message):
        __slots__ = ("task_status", "num_tasks")
        TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
        NUM_TASKS_FIELD_NUMBER: _ClassVar[int]
        task_status: TaskStatus.Type
        num_tasks: int
        def __init__(self, task_status: _Optional[_Union[TaskStatus.Type, str]] = ..., num_tasks: _Optional[int] = ...) -> None: ...
    TASK_STATUS_COUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    task_status_count_vec: _containers.RepeatedCompositeFieldContainer[TaskGroupSummaryProto.TaskStatusCount]
    def __init__(self, task_status_count_vec: _Optional[_Iterable[_Union[TaskGroupSummaryProto.TaskStatusCount, _Mapping]]] = ...) -> None: ...

class WorkerIncarnationProto(_message.Message):
    __slots__ = ("id", "incarnation_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    incarnation_id: int
    def __init__(self, id: _Optional[str] = ..., incarnation_id: _Optional[int] = ...) -> None: ...

class TaskStateProto(_message.Message):
    __slots__ = ("task_id", "parent_task_id", "type", "status", "assigned_worker_id", "error")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    parent_task_id: str
    type: TaskType
    status: TaskStatus.Type
    assigned_worker_id: WorkerIncarnationProto
    error: _error_pb2.ErrorProto
    def __init__(self, task_id: _Optional[str] = ..., parent_task_id: _Optional[str] = ..., type: _Optional[_Union[TaskType, _Mapping]] = ..., status: _Optional[_Union[TaskStatus.Type, str]] = ..., assigned_worker_id: _Optional[_Union[WorkerIncarnationProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class WorkerStateProto(_message.Message):
    __slots__ = ("worker_id", "idle_worker_expiry_duration_at_server_msecs", "capacity")
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    IDLE_WORKER_EXPIRY_DURATION_AT_SERVER_MSECS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    worker_id: WorkerIncarnationProto
    idle_worker_expiry_duration_at_server_msecs: int
    capacity: int
    def __init__(self, worker_id: _Optional[_Union[WorkerIncarnationProto, _Mapping]] = ..., idle_worker_expiry_duration_at_server_msecs: _Optional[int] = ..., capacity: _Optional[int] = ...) -> None: ...

class WorkqueueServerConfigProto(_message.Message):
    __slots__ = ("gandalf_master_key",)
    GANDALF_MASTER_KEY_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_key: str
    def __init__(self, gandalf_master_key: _Optional[str] = ...) -> None: ...
