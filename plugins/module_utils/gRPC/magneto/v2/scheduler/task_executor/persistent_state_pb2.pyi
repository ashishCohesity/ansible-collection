from magneto.base import error_pb2 as _error_pb2
from magneto.v2.scheduler.task_executor import external_pb2 as _external_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskBaseProto(_message.Message):
    __slots__ = ("start_time_usecs", "end_time_usecs", "error_vec", "warning_vec")
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
    start_time_usecs: int
    end_time_usecs: int
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    warning_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, start_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., warning_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BackupTaskStateProto(_message.Message):
    __slots__ = ("batch_identifier", "backup_task_spec", "task_base", "desired_state", "operational_state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[BackupTaskStateProto.State]
        kStarted: _ClassVar[BackupTaskStateProto.State]
        kPaused: _ClassVar[BackupTaskStateProto.State]
        kExecuted: _ClassVar[BackupTaskStateProto.State]
        kPostProcessed: _ClassVar[BackupTaskStateProto.State]
        kFinished: _ClassVar[BackupTaskStateProto.State]
    kCreated: BackupTaskStateProto.State
    kStarted: BackupTaskStateProto.State
    kPaused: BackupTaskStateProto.State
    kExecuted: BackupTaskStateProto.State
    kPostProcessed: BackupTaskStateProto.State
    kFinished: BackupTaskStateProto.State
    BATCH_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_SPEC_FIELD_NUMBER: _ClassVar[int]
    TASK_BASE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    batch_identifier: int
    backup_task_spec: _external_pb2.BackupTaskSpecProto
    task_base: TaskBaseProto
    desired_state: BackupTaskStateProto.State
    operational_state: BackupTaskStateProto.State
    def __init__(self, batch_identifier: _Optional[int] = ..., backup_task_spec: _Optional[_Union[_external_pb2.BackupTaskSpecProto, _Mapping]] = ..., task_base: _Optional[_Union[TaskBaseProto, _Mapping]] = ..., desired_state: _Optional[_Union[BackupTaskStateProto.State, str]] = ..., operational_state: _Optional[_Union[BackupTaskStateProto.State, str]] = ...) -> None: ...

class TaskExecutorWALRecordProto(_message.Message):
    __slots__ = ("backup_task_state_vec",)
    BACKUP_TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_task_state_vec: _containers.RepeatedCompositeFieldContainer[BackupTaskStateProto]
    def __init__(self, backup_task_state_vec: _Optional[_Iterable[_Union[BackupTaskStateProto, _Mapping]]] = ...) -> None: ...
