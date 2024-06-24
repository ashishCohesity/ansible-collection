from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base import error_pb2 as _error_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumerateObjectsToBackupArg(_message.Message):
    __slots__ = ("base", "protected_source_uid_vec")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_SOURCE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    protected_source_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., protected_source_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...

class EnumerateObjectsToBackupResult(_message.Message):
    __slots__ = ("base", "result_vec")
    class Result(_message.Message):
        __slots__ = ("protected_source_uid", "error", "object_uid_vec")
        PROTECTED_SOURCE_UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        protected_source_uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        def __init__(self, protected_source_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    result_vec: _containers.RepeatedCompositeFieldContainer[EnumerateObjectsToBackupResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., result_vec: _Optional[_Iterable[_Union[EnumerateObjectsToBackupResult.Result, _Mapping]]] = ...) -> None: ...

class ConstructBackupPlanArg(_message.Message):
    __slots__ = ("base", "run_uid", "protected_source_vec")
    class ProtectedSource(_message.Message):
        __slots__ = ("uid", "object_uid_vec")
        UID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        uid: _universal_id_pb2.UniversalIdProto
        object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_SOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ArgumentBase
    run_uid: _universal_id_pb2.UniversalIdProto
    protected_source_vec: _containers.RepeatedCompositeFieldContainer[ConstructBackupPlanArg.ProtectedSource]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ArgumentBase, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., protected_source_vec: _Optional[_Iterable[_Union[ConstructBackupPlanArg.ProtectedSource, _Mapping]]] = ...) -> None: ...

class BackupTaskDagProto(_message.Message):
    __slots__ = ("node_vec", "root_node_vec")
    class Node(_message.Message):
        __slots__ = ("serialized_task_arg", "object_uid_vec", "child_index_vec")
        SERIALIZED_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
        OBJECT_UID_VEC_FIELD_NUMBER: _ClassVar[int]
        CHILD_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
        serialized_task_arg: bytes
        object_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
        child_index_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, serialized_task_arg: _Optional[bytes] = ..., object_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., child_index_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class RootNode(_message.Message):
        __slots__ = ("root_node_index",)
        ROOT_NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
        root_node_index: int
        def __init__(self, root_node_index: _Optional[int] = ...) -> None: ...
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    node_vec: _containers.RepeatedCompositeFieldContainer[BackupTaskDagProto.Node]
    root_node_vec: _containers.RepeatedCompositeFieldContainer[BackupTaskDagProto.RootNode]
    def __init__(self, node_vec: _Optional[_Iterable[_Union[BackupTaskDagProto.Node, _Mapping]]] = ..., root_node_vec: _Optional[_Iterable[_Union[BackupTaskDagProto.RootNode, _Mapping]]] = ...) -> None: ...

class ConstructBackupPlanResult(_message.Message):
    __slots__ = ("base", "in_progress", "result_vec")
    class Result(_message.Message):
        __slots__ = ("run_uid", "uid", "error", "task_dag")
        RUN_UID_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        TASK_DAG_FIELD_NUMBER: _ClassVar[int]
        run_uid: _universal_id_pb2.UniversalIdProto
        uid: _universal_id_pb2.UniversalIdProto
        error: _error_pb2.ErrorProto
        task_dag: BackupTaskDagProto
        def __init__(self, run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_dag: _Optional[_Union[BackupTaskDagProto, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_external_base_pb2.ResultBase
    in_progress: bool
    result_vec: _containers.RepeatedCompositeFieldContainer[ConstructBackupPlanResult.Result]
    def __init__(self, base: _Optional[_Union[_magneto_external_base_pb2.ResultBase, _Mapping]] = ..., in_progress: bool = ..., result_vec: _Optional[_Iterable[_Union[ConstructBackupPlanResult.Result, _Mapping]]] = ...) -> None: ...
