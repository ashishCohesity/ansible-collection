from magnus.api.v1 import public_vmware_data_pb2 as _public_vmware_data_pb2
from magnus.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagnusServerConfigProto(_message.Message):
    __slots__ = ("gandalf_owner_key",)
    GANDALF_OWNER_KEY_FIELD_NUMBER: _ClassVar[int]
    gandalf_owner_key: str
    def __init__(self, gandalf_owner_key: _Optional[str] = ...) -> None: ...

class Environment(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMware: _ClassVar[Environment.Type]
    kVMware: Environment.Type
    def __init__(self) -> None: ...

class TaskType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TaskType.Type]
        kVMwareVMTask: _ClassVar[TaskType.Type]
        kVMwareDatastoreTask: _ClassVar[TaskType.Type]
    kUnknown: TaskType.Type
    kVMwareVMTask: TaskType.Type
    kVMwareDatastoreTask: TaskType.Type
    def __init__(self) -> None: ...

class TaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TaskStatus.Type]
        kAccepted: _ClassVar[TaskStatus.Type]
        kScheduled: _ClassVar[TaskStatus.Type]
        kRunning: _ClassVar[TaskStatus.Type]
        kFinished: _ClassVar[TaskStatus.Type]
    kUnknown: TaskStatus.Type
    kAccepted: TaskStatus.Type
    kScheduled: TaskStatus.Type
    kRunning: TaskStatus.Type
    kFinished: TaskStatus.Type
    def __init__(self) -> None: ...

class TaskBase(_message.Message):
    __slots__ = ("task_id", "env", "type", "status", "error", "assigned_actor", "start_time_usecs", "end_time_usecs", "is_garbage_collected")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ACTOR_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_GARBAGE_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    env: Environment.Type
    type: TaskType.Type
    status: TaskStatus.Type
    error: _error_pb2.ErrorProto
    assigned_actor: ActorIncarnationProto
    start_time_usecs: int
    end_time_usecs: int
    is_garbage_collected: bool
    def __init__(self, task_id: _Optional[str] = ..., env: _Optional[_Union[Environment.Type, str]] = ..., type: _Optional[_Union[TaskType.Type, str]] = ..., status: _Optional[_Union[TaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., assigned_actor: _Optional[_Union[ActorIncarnationProto, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., is_garbage_collected: bool = ...) -> None: ...

class TaskStateProto(_message.Message):
    __slots__ = ("base", "vmware_vm_task", "vmware_datastore_task")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_VM_TASK_FIELD_NUMBER: _ClassVar[int]
    VMWARE_DATASTORE_TASK_FIELD_NUMBER: _ClassVar[int]
    base: TaskBase
    vmware_vm_task: VMwareVMPersistedTask
    vmware_datastore_task: VMwareDatastorePersistedTask
    def __init__(self, base: _Optional[_Union[TaskBase, _Mapping]] = ..., vmware_vm_task: _Optional[_Union[VMwareVMPersistedTask, _Mapping]] = ..., vmware_datastore_task: _Optional[_Union[VMwareDatastorePersistedTask, _Mapping]] = ...) -> None: ...

class ActorIncarnationProto(_message.Message):
    __slots__ = ("actor_id", "incarnation_id")
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    incarnation_id: int
    def __init__(self, actor_id: _Optional[str] = ..., incarnation_id: _Optional[int] = ...) -> None: ...

class VMwareDatastorePersistedTask(_message.Message):
    __slots__ = ("request", "result")
    class Result(_message.Message):
        __slots__ = ("mount_nas_datastore_result",)
        MOUNT_NAS_DATASTORE_RESULT_FIELD_NUMBER: _ClassVar[int]
        mount_nas_datastore_result: _public_vmware_data_pb2.MountVMwareNasDatastoreResult
        def __init__(self, mount_nas_datastore_result: _Optional[_Union[_public_vmware_data_pb2.MountVMwareNasDatastoreResult, _Mapping]] = ...) -> None: ...
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    request: _public_vmware_data_pb2.VMwareDatastoreActionArg
    result: VMwareDatastorePersistedTask.Result
    def __init__(self, request: _Optional[_Union[_public_vmware_data_pb2.VMwareDatastoreActionArg, _Mapping]] = ..., result: _Optional[_Union[VMwareDatastorePersistedTask.Result, _Mapping]] = ...) -> None: ...

class VMwareVMPersistedTask(_message.Message):
    __slots__ = ("request", "result")
    class Result(_message.Message):
        __slots__ = ("create_result", "relocate_result", "run_program_result")
        CREATE_RESULT_FIELD_NUMBER: _ClassVar[int]
        RELOCATE_RESULT_FIELD_NUMBER: _ClassVar[int]
        RUN_PROGRAM_RESULT_FIELD_NUMBER: _ClassVar[int]
        create_result: _public_vmware_data_pb2.CreateVMwareVMResult
        relocate_result: _public_vmware_data_pb2.RelocateVMwareVMResult
        run_program_result: _public_vmware_data_pb2.RunProgramVMwareVMResult
        def __init__(self, create_result: _Optional[_Union[_public_vmware_data_pb2.CreateVMwareVMResult, _Mapping]] = ..., relocate_result: _Optional[_Union[_public_vmware_data_pb2.RelocateVMwareVMResult, _Mapping]] = ..., run_program_result: _Optional[_Union[_public_vmware_data_pb2.RunProgramVMwareVMResult, _Mapping]] = ...) -> None: ...
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    request: _public_vmware_data_pb2.VMwareVMActionArg
    result: VMwareVMPersistedTask.Result
    def __init__(self, request: _Optional[_Union[_public_vmware_data_pb2.VMwareVMActionArg, _Mapping]] = ..., result: _Optional[_Union[VMwareVMPersistedTask.Result, _Mapping]] = ...) -> None: ...

class ActorStateProto(_message.Message):
    __slots__ = ("actor", "idle_actor_expiry_duration_at_server_msecs", "capacity", "is_expired", "last_received_msg_id")
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    IDLE_ACTOR_EXPIRY_DURATION_AT_SERVER_MSECS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    LAST_RECEIVED_MSG_ID_FIELD_NUMBER: _ClassVar[int]
    actor: ActorIncarnationProto
    idle_actor_expiry_duration_at_server_msecs: int
    capacity: int
    is_expired: bool
    last_received_msg_id: int
    def __init__(self, actor: _Optional[_Union[ActorIncarnationProto, _Mapping]] = ..., idle_actor_expiry_duration_at_server_msecs: _Optional[int] = ..., capacity: _Optional[int] = ..., is_expired: bool = ..., last_received_msg_id: _Optional[int] = ...) -> None: ...

class IncarnationProto(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ServerPersistenceProto(_message.Message):
    __slots__ = ("task_vec", "actor_vec", "incarnation_vec")
    TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    ACTOR_VEC_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_VEC_FIELD_NUMBER: _ClassVar[int]
    task_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    actor_vec: _containers.RepeatedCompositeFieldContainer[ActorStateProto]
    incarnation_vec: _containers.RepeatedCompositeFieldContainer[IncarnationProto]
    def __init__(self, task_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ..., actor_vec: _Optional[_Iterable[_Union[ActorStateProto, _Mapping]]] = ..., incarnation_vec: _Optional[_Iterable[_Union[IncarnationProto, _Mapping]]] = ...) -> None: ...
