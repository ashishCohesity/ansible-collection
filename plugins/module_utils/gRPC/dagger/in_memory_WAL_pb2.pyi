from dagger import dagger_pb2 as _dagger_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskStateProto(_message.Message):
    __slots__ = ("type", "task_id", "parent_id", "arg_bytes", "state_machine_bytes", "children", "cancellation_requested")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    ARG_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATE_MACHINE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    type: int
    task_id: _dagger_pb2.TaskId
    parent_id: _dagger_pb2.TaskId
    arg_bytes: bytes
    state_machine_bytes: bytes
    children: _containers.RepeatedCompositeFieldContainer[_dagger_pb2.TaskId]
    cancellation_requested: bool
    def __init__(self, type: _Optional[int] = ..., task_id: _Optional[_Union[_dagger_pb2.TaskId, _Mapping]] = ..., parent_id: _Optional[_Union[_dagger_pb2.TaskId, _Mapping]] = ..., arg_bytes: _Optional[bytes] = ..., state_machine_bytes: _Optional[bytes] = ..., children: _Optional[_Iterable[_Union[_dagger_pb2.TaskId, _Mapping]]] = ..., cancellation_requested: bool = ...) -> None: ...

class WALRecordProto(_message.Message):
    __slots__ = ("task_local_id_generator", "task_state_vec", "finished_task_state_vec", "add_or_update_task_vec", "set_finished_task_state_vec", "delete_task_vec")
    TASK_LOCAL_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    FINISHED_TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    SET_FINISHED_TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    task_local_id_generator: int
    task_state_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    finished_task_state_vec: _containers.RepeatedCompositeFieldContainer[_dagger_pb2.FinishedTaskStateProto]
    add_or_update_task_vec: _containers.RepeatedCompositeFieldContainer[TaskStateProto]
    set_finished_task_state_vec: _containers.RepeatedCompositeFieldContainer[_dagger_pb2.FinishedTaskStateProto]
    delete_task_vec: _containers.RepeatedCompositeFieldContainer[_dagger_pb2.TaskId]
    def __init__(self, task_local_id_generator: _Optional[int] = ..., task_state_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ..., finished_task_state_vec: _Optional[_Iterable[_Union[_dagger_pb2.FinishedTaskStateProto, _Mapping]]] = ..., add_or_update_task_vec: _Optional[_Iterable[_Union[TaskStateProto, _Mapping]]] = ..., set_finished_task_state_vec: _Optional[_Iterable[_Union[_dagger_pb2.FinishedTaskStateProto, _Mapping]]] = ..., delete_task_vec: _Optional[_Iterable[_Union[_dagger_pb2.TaskId, _Mapping]]] = ...) -> None: ...
