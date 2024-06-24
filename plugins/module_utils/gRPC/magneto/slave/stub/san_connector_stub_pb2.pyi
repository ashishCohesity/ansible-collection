from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SanStartRestoreTaskArg(_message.Message):
    __slots__ = ("snapshot_info_proto_vec",)
    PURE_START_RESTORE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    pure_start_restore_task_arg: _descriptor.FieldDescriptor
    SNAPSHOT_INFO_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_info_proto_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.SnapshotInfoProto]
    def __init__(self, snapshot_info_proto_vec: _Optional[_Iterable[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]]] = ...) -> None: ...
