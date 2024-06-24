from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupTaskDagSpecProto(_message.Message):
    __slots__ = ("run_uid", "node_vec", "root_node_idx")
    class Node(_message.Message):
        __slots__ = ("snapshot_node_uid", "child_index_vec")
        SNAPSHOT_NODE_UID_FIELD_NUMBER: _ClassVar[int]
        CHILD_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
        snapshot_node_uid: _universal_id_pb2.UniversalIdProto
        child_index_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, snapshot_node_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., child_index_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_IDX_FIELD_NUMBER: _ClassVar[int]
    run_uid: _universal_id_pb2.UniversalIdProto
    node_vec: _containers.RepeatedCompositeFieldContainer[BackupTaskDagSpecProto.Node]
    root_node_idx: int
    def __init__(self, run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., node_vec: _Optional[_Iterable[_Union[BackupTaskDagSpecProto.Node, _Mapping]]] = ..., root_node_idx: _Optional[int] = ...) -> None: ...
