from magneto.v2.scheduler.base import versions_pb2 as _versions_pb2
from magneto.v2.scheduler.task_dag_dispatcher import persistent_state_pb2 as _persistent_state_pb2
from magneto.v2.scheduler.task_dag_generator import persistent_state_pb2 as _persistent_state_pb2_1
from magneto.v2.scheduler.task_executor import persistent_state_pb2 as _persistent_state_pb2_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WALRecordProto(_message.Message):
    __slots__ = ("version", "task_dag_generator_proto_vec", "task_dag_dispatcher_proto_vec", "task_executor_proto_vec")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_DAG_GENERATOR_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_DAG_DISPATCHER_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_EXECUTOR_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    version: _versions_pb2.VersionProto
    task_dag_generator_proto_vec: _containers.RepeatedCompositeFieldContainer[_persistent_state_pb2_1.TaskDagGeneratorWALRecordProto]
    task_dag_dispatcher_proto_vec: _containers.RepeatedCompositeFieldContainer[_persistent_state_pb2.TaskDagDispatcherWALRecordProto]
    task_executor_proto_vec: _containers.RepeatedCompositeFieldContainer[_persistent_state_pb2_1_1.TaskExecutorWALRecordProto]
    def __init__(self, version: _Optional[_Union[_versions_pb2.VersionProto, _Mapping]] = ..., task_dag_generator_proto_vec: _Optional[_Iterable[_Union[_persistent_state_pb2_1.TaskDagGeneratorWALRecordProto, _Mapping]]] = ..., task_dag_dispatcher_proto_vec: _Optional[_Iterable[_Union[_persistent_state_pb2.TaskDagDispatcherWALRecordProto, _Mapping]]] = ..., task_executor_proto_vec: _Optional[_Iterable[_Union[_persistent_state_pb2_1_1.TaskExecutorWALRecordProto, _Mapping]]] = ...) -> None: ...
