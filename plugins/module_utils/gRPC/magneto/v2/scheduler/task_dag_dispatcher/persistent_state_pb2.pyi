from magneto.base import error_pb2 as _error_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskSpecProto(_message.Message):
    __slots__ = ("parent_task_uid_vec", "run_uid")
    PARENT_TASK_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    parent_task_uid_vec: _universal_id_pb2.UniversalIdProto
    run_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, parent_task_uid_vec: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class TaskStateProto(_message.Message):
    __slots__ = ("task_uid", "incarnation", "creation_time_usecs", "last_state_change_time_usecs", "end_time_usecs", "defered_start_time_usecs", "pause_reason", "cancel_reason", "final_error", "warring_vec", "spec", "desired_state", "operational_state", "created", "started")
    class PauseCancelReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[TaskStateProto.PauseCancelReason]
        kUser: _ClassVar[TaskStateProto.PauseCancelReason]
        kQuietTime: _ClassVar[TaskStateProto.PauseCancelReason]
        kTimeOut: _ClassVar[TaskStateProto.PauseCancelReason]
    kNone: TaskStateProto.PauseCancelReason
    kUser: TaskStateProto.PauseCancelReason
    kQuietTime: TaskStateProto.PauseCancelReason
    kTimeOut: TaskStateProto.PauseCancelReason
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[TaskStateProto.State]
        kStarted: _ClassVar[TaskStateProto.State]
        kPaused: _ClassVar[TaskStateProto.State]
        kFinished: _ClassVar[TaskStateProto.State]
    kCreated: TaskStateProto.State
    kStarted: TaskStateProto.State
    kPaused: TaskStateProto.State
    kFinished: TaskStateProto.State
    class Created(_message.Message):
        __slots__ = ("pulse_and_counter_created",)
        PULSE_AND_COUNTER_CREATED_FIELD_NUMBER: _ClassVar[int]
        pulse_and_counter_created: bool
        def __init__(self, pulse_and_counter_created: bool = ...) -> None: ...
    class Started(_message.Message):
        __slots__ = ("task_execution_finished", "task_result")
        TASK_EXECUTION_FINISHED_FIELD_NUMBER: _ClassVar[int]
        TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
        task_execution_finished: bool
        task_result: bytes
        def __init__(self, task_execution_finished: bool = ..., task_result: _Optional[bytes] = ...) -> None: ...
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_STATE_CHANGE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEFERED_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PAUSE_REASON_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REASON_FIELD_NUMBER: _ClassVar[int]
    FINAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    WARRING_VEC_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    task_uid: _universal_id_pb2.UniversalIdProto
    incarnation: int
    creation_time_usecs: int
    last_state_change_time_usecs: int
    end_time_usecs: int
    defered_start_time_usecs: int
    pause_reason: TaskStateProto.PauseCancelReason
    cancel_reason: TaskStateProto.PauseCancelReason
    final_error: _error_pb2.ErrorProto
    warring_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    spec: TaskSpecProto
    desired_state: TaskStateProto.State
    operational_state: TaskStateProto.State
    created: TaskStateProto.Created
    started: TaskStateProto.Started
    def __init__(self, task_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., incarnation: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., last_state_change_time_usecs: _Optional[int] = ..., end_time_usecs: _Optional[int] = ..., defered_start_time_usecs: _Optional[int] = ..., pause_reason: _Optional[_Union[TaskStateProto.PauseCancelReason, str]] = ..., cancel_reason: _Optional[_Union[TaskStateProto.PauseCancelReason, str]] = ..., final_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., warring_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., spec: _Optional[_Union[TaskSpecProto, _Mapping]] = ..., desired_state: _Optional[_Union[TaskStateProto.State, str]] = ..., operational_state: _Optional[_Union[TaskStateProto.State, str]] = ..., created: _Optional[_Union[TaskStateProto.Created, _Mapping]] = ..., started: _Optional[_Union[TaskStateProto.Started, _Mapping]] = ...) -> None: ...

class TaskDagDispatcherWALRecordProto(_message.Message):
    __slots__ = ("task_state_proto_vec",)
    TASK_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    task_state_proto_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    def __init__(self, task_state_proto_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ...) -> None: ...
