from groot.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceInfo(_message.Message):
    __slots__ = ("service_id", "service_name", "port", "num_replicas", "cluster_state", "replica_info_vec", "has_master_replica", "epoch_id", "older_replica_info_vec")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReady: _ClassVar[ServiceInfo.State]
        kMigrating: _ClassVar[ServiceInfo.State]
    kReady: ServiceInfo.State
    kMigrating: ServiceInfo.State
    class ReplicaInfo(_message.Message):
        __slots__ = ("node_id", "node_ip", "disk_id", "is_master_replica")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        IS_MASTER_REPLICA_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        node_ip: str
        disk_id: int
        is_master_replica: bool
        def __init__(self, node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., disk_id: _Optional[int] = ..., is_master_replica: bool = ...) -> None: ...
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NUM_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    HAS_MASTER_REPLICA_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    OLDER_REPLICA_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    service_id: int
    service_name: str
    port: int
    num_replicas: int
    cluster_state: ServiceInfo.State
    replica_info_vec: _containers.RepeatedCompositeFieldContainer[ServiceInfo.ReplicaInfo]
    has_master_replica: bool
    epoch_id: int
    older_replica_info_vec: _containers.RepeatedCompositeFieldContainer[ServiceInfo.ReplicaInfo]
    def __init__(self, service_id: _Optional[int] = ..., service_name: _Optional[str] = ..., port: _Optional[int] = ..., num_replicas: _Optional[int] = ..., cluster_state: _Optional[_Union[ServiceInfo.State, str]] = ..., replica_info_vec: _Optional[_Iterable[_Union[ServiceInfo.ReplicaInfo, _Mapping]]] = ..., has_master_replica: bool = ..., epoch_id: _Optional[int] = ..., older_replica_info_vec: _Optional[_Iterable[_Union[ServiceInfo.ReplicaInfo, _Mapping]]] = ...) -> None: ...

class LookupMasterResult(_message.Message):
    __slots__ = ("error", "ip", "port")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    ip: str
    port: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class GetDatabaseInfoResult(_message.Message):
    __slots__ = ("error", "database_info_vec")
    class DatabaseInfo(_message.Message):
        __slots__ = ("node_id", "node_ip", "port", "default_username", "default_password")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_USERNAME_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        node_ip: str
        port: int
        default_username: str
        default_password: str
        def __init__(self, node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., port: _Optional[int] = ..., default_username: _Optional[str] = ..., default_password: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    database_info_vec: _containers.RepeatedCompositeFieldContainer[GetDatabaseInfoResult.DatabaseInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., database_info_vec: _Optional[_Iterable[_Union[GetDatabaseInfoResult.DatabaseInfo, _Mapping]]] = ...) -> None: ...

class TriggerMagnetoFullsyncResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
