from magneto.base import error_pb2 as _error_pb2
from magneto.v2.scheduler.task_dag_generator import external_pb2 as _external_pb2
from magneto.v2.adapters import facade_for_scheduler_pb2 as _facade_for_scheduler_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupEventTransientStateProto(_message.Message):
    __slots__ = ("create_snapshot_nodes",)
    class CreateSnapshotNodes(_message.Message):
        __slots__ = ("dag_index", "dag_node_index")
        DAG_INDEX_FIELD_NUMBER: _ClassVar[int]
        DAG_NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
        dag_index: int
        dag_node_index: int
        def __init__(self, dag_index: _Optional[int] = ..., dag_node_index: _Optional[int] = ...) -> None: ...
    CREATE_SNAPSHOT_NODES_FIELD_NUMBER: _ClassVar[int]
    create_snapshot_nodes: BackupEventTransientStateProto.CreateSnapshotNodes
    def __init__(self, create_snapshot_nodes: _Optional[_Union[BackupEventTransientStateProto.CreateSnapshotNodes, _Mapping]] = ...) -> None: ...

class ScheduledBackupEventStateProto(_message.Message):
    __slots__ = ("event_spec_proto", "state", "last_modification_usec", "error", "run_uid", "enumerate_objects_result", "backup_plan_result", "transient_state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPreProcess: _ClassVar[ScheduledBackupEventStateProto.State]
        kAnalyze: _ClassVar[ScheduledBackupEventStateProto.State]
        kGenerateDag: _ClassVar[ScheduledBackupEventStateProto.State]
        kUpdateMDS: _ClassVar[ScheduledBackupEventStateProto.State]
        kDispatch: _ClassVar[ScheduledBackupEventStateProto.State]
        kFinish: _ClassVar[ScheduledBackupEventStateProto.State]
    kPreProcess: ScheduledBackupEventStateProto.State
    kAnalyze: ScheduledBackupEventStateProto.State
    kGenerateDag: ScheduledBackupEventStateProto.State
    kUpdateMDS: ScheduledBackupEventStateProto.State
    kDispatch: ScheduledBackupEventStateProto.State
    kFinish: ScheduledBackupEventStateProto.State
    EVENT_SPEC_PROTO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_USEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RUN_UID_FIELD_NUMBER: _ClassVar[int]
    ENUMERATE_OBJECTS_RESULT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSIENT_STATE_FIELD_NUMBER: _ClassVar[int]
    event_spec_proto: _external_pb2.ScheduledBackupEventSpecProto
    state: ScheduledBackupEventStateProto.State
    last_modification_usec: int
    error: _error_pb2.ErrorProto
    run_uid: _universal_id_pb2.UniversalIdProto
    enumerate_objects_result: _facade_for_scheduler_pb2.EnumerateObjectsToBackupResult
    backup_plan_result: _facade_for_scheduler_pb2.ConstructBackupPlanResult
    transient_state: BackupEventTransientStateProto
    def __init__(self, event_spec_proto: _Optional[_Union[_external_pb2.ScheduledBackupEventSpecProto, _Mapping]] = ..., state: _Optional[_Union[ScheduledBackupEventStateProto.State, str]] = ..., last_modification_usec: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., run_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., enumerate_objects_result: _Optional[_Union[_facade_for_scheduler_pb2.EnumerateObjectsToBackupResult, _Mapping]] = ..., backup_plan_result: _Optional[_Union[_facade_for_scheduler_pb2.ConstructBackupPlanResult, _Mapping]] = ..., transient_state: _Optional[_Union[BackupEventTransientStateProto, _Mapping]] = ...) -> None: ...

class TaskDagGeneratorWALRecordProto(_message.Message):
    __slots__ = ("event_state_proto_vec",)
    EVENT_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    event_state_proto_vec: _containers.RepeatedCompositeFieldContainer[ScheduledBackupEventStateProto]
    def __init__(self, event_state_proto_vec: _Optional[_Iterable[_Union[ScheduledBackupEventStateProto, _Mapping]]] = ...) -> None: ...
