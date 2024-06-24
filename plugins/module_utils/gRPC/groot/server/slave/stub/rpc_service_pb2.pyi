from groot.base import error_pb2 as _error_pb2
from groot.base import groot_pb2 as _groot_pb2
from groot.server.master import wal_entry_pb2 as _wal_entry_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateServiceInfoArg(_message.Message):
    __slots__ = ("service_id", "epoch_id", "constituent_id", "session_id", "state", "is_replica", "master_replica_info", "replica_disk_id")
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IS_REPLICA_FIELD_NUMBER: _ClassVar[int]
    MASTER_REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: int
    epoch_id: int
    constituent_id: int
    session_id: int
    state: _groot_pb2.ServiceInfo.State
    is_replica: bool
    master_replica_info: _groot_pb2.ServiceInfo.ReplicaInfo
    replica_disk_id: int
    def __init__(self, service_id: _Optional[int] = ..., epoch_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., state: _Optional[_Union[_groot_pb2.ServiceInfo.State, str]] = ..., is_replica: bool = ..., master_replica_info: _Optional[_Union[_groot_pb2.ServiceInfo.ReplicaInfo, _Mapping]] = ..., replica_disk_id: _Optional[int] = ...) -> None: ...

class UpdateServiceInfoResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class StartMigrationArg(_message.Message):
    __slots__ = ("task_id", "service_id", "constituent_id", "session_id", "task_type", "source_node_id", "source_disk_id", "is_fresh_start")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FRESH_START_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    service_id: int
    constituent_id: int
    session_id: int
    task_type: _wal_entry_pb2.MigrationTask.TaskType
    source_node_id: int
    source_disk_id: int
    is_fresh_start: bool
    def __init__(self, task_id: _Optional[int] = ..., service_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., task_type: _Optional[_Union[_wal_entry_pb2.MigrationTask.TaskType, str]] = ..., source_node_id: _Optional[int] = ..., source_disk_id: _Optional[int] = ..., is_fresh_start: bool = ...) -> None: ...

class StartMigrationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CancelMigrationArg(_message.Message):
    __slots__ = ("task_id", "service_id", "constituent_id", "session_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    service_id: int
    constituent_id: int
    session_id: int
    def __init__(self, task_id: _Optional[int] = ..., service_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ...) -> None: ...

class CancelMigrationResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class QueryMigrationTasksArg(_message.Message):
    __slots__ = ("service_id",)
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: int
    def __init__(self, service_id: _Optional[int] = ...) -> None: ...

class QueryMigrationTasksResult(_message.Message):
    __slots__ = ("slave_session_id", "taskid_vec")
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASKID_VEC_FIELD_NUMBER: _ClassVar[int]
    slave_session_id: int
    taskid_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, slave_session_id: _Optional[int] = ..., taskid_vec: _Optional[_Iterable[int]] = ...) -> None: ...
