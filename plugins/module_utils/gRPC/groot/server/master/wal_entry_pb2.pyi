from groot.base import groot_pb2 as _groot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MigrationTask(_message.Message):
    __slots__ = ("task_id", "service_id", "source_node_id", "source_disk_id", "destination_node_id", "destination_disk_id", "task_type", "status")
    class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdd: _ClassVar[MigrationTask.TaskType]
        kDelete: _ClassVar[MigrationTask.TaskType]
    kAdd: MigrationTask.TaskType
    kDelete: MigrationTask.TaskType
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIncomplete: _ClassVar[MigrationTask.Status]
        kDone: _ClassVar[MigrationTask.Status]
        kCancelled: _ClassVar[MigrationTask.Status]
    kIncomplete: MigrationTask.Status
    kDone: MigrationTask.Status
    kCancelled: MigrationTask.Status
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    service_id: int
    source_node_id: int
    source_disk_id: int
    destination_node_id: int
    destination_disk_id: int
    task_type: MigrationTask.TaskType
    status: MigrationTask.Status
    def __init__(self, task_id: _Optional[int] = ..., service_id: _Optional[int] = ..., source_node_id: _Optional[int] = ..., source_disk_id: _Optional[int] = ..., destination_node_id: _Optional[int] = ..., destination_disk_id: _Optional[int] = ..., task_type: _Optional[_Union[MigrationTask.TaskType, str]] = ..., status: _Optional[_Union[MigrationTask.Status, str]] = ...) -> None: ...

class WALEntry(_message.Message):
    __slots__ = ("service_state_vec", "service_update_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpdateIntentLogged: _ClassVar[WALEntry.Status]
        kSlaveEpochUpdated: _ClassVar[WALEntry.Status]
        kMigrationComplete: _ClassVar[WALEntry.Status]
        kServiceEnabled: _ClassVar[WALEntry.Status]
    kUpdateIntentLogged: WALEntry.Status
    kSlaveEpochUpdated: WALEntry.Status
    kMigrationComplete: WALEntry.Status
    kServiceEnabled: WALEntry.Status
    class ServiceState(_message.Message):
        __slots__ = ("service_info", "migration_task_vec", "status")
        SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        service_info: _groot_pb2.ServiceInfo
        migration_task_vec: _containers.RepeatedCompositeFieldContainer[MigrationTask]
        status: WALEntry.Status
        def __init__(self, service_info: _Optional[_Union[_groot_pb2.ServiceInfo, _Mapping]] = ..., migration_task_vec: _Optional[_Iterable[_Union[MigrationTask, _Mapping]]] = ..., status: _Optional[_Union[WALEntry.Status, str]] = ...) -> None: ...
    class ServiceUpdate(_message.Message):
        __slots__ = ("service_id", "epoch_update_intent", "migration_task_vec", "replica_info_vec", "older_replica_info_vec", "status")
        class EpochUpdateIntent(_message.Message):
            __slots__ = ("current_epoch_id", "new_epoch_id")
            CURRENT_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
            NEW_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
            current_epoch_id: int
            new_epoch_id: int
            def __init__(self, current_epoch_id: _Optional[int] = ..., new_epoch_id: _Optional[int] = ...) -> None: ...
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        EPOCH_UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
        REPLICA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        OLDER_REPLICA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        service_id: int
        epoch_update_intent: WALEntry.ServiceUpdate.EpochUpdateIntent
        migration_task_vec: _containers.RepeatedCompositeFieldContainer[MigrationTask]
        replica_info_vec: _containers.RepeatedCompositeFieldContainer[_groot_pb2.ServiceInfo.ReplicaInfo]
        older_replica_info_vec: _containers.RepeatedCompositeFieldContainer[_groot_pb2.ServiceInfo.ReplicaInfo]
        status: WALEntry.Status
        def __init__(self, service_id: _Optional[int] = ..., epoch_update_intent: _Optional[_Union[WALEntry.ServiceUpdate.EpochUpdateIntent, _Mapping]] = ..., migration_task_vec: _Optional[_Iterable[_Union[MigrationTask, _Mapping]]] = ..., replica_info_vec: _Optional[_Iterable[_Union[_groot_pb2.ServiceInfo.ReplicaInfo, _Mapping]]] = ..., older_replica_info_vec: _Optional[_Iterable[_Union[_groot_pb2.ServiceInfo.ReplicaInfo, _Mapping]]] = ..., status: _Optional[_Union[WALEntry.Status, str]] = ...) -> None: ...
    SERVICE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    service_state_vec: _containers.RepeatedCompositeFieldContainer[WALEntry.ServiceState]
    service_update_vec: _containers.RepeatedCompositeFieldContainer[WALEntry.ServiceUpdate]
    def __init__(self, service_state_vec: _Optional[_Iterable[_Union[WALEntry.ServiceState, _Mapping]]] = ..., service_update_vec: _Optional[_Iterable[_Union[WALEntry.ServiceUpdate, _Mapping]]] = ...) -> None: ...
