from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicySpecProto(_message.Message):
    __slots__ = ("id", "time_period_secs", "backup_start_time_secs")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    id: str
    time_period_secs: int
    backup_start_time_secs: int
    def __init__(self, id: _Optional[str] = ..., time_period_secs: _Optional[int] = ..., backup_start_time_secs: _Optional[int] = ...) -> None: ...

class EntitySpecProto(_message.Message):
    __slots__ = ("name", "type", "env", "tenant_id", "logical_size", "data_source_entity_name", "policy_id", "sla_duration_secs", "priority", "daily_change_rate_mean", "daily_change_rate_stddev", "num_data_read_slots", "max_read_bytes_per_sec", "max_write_bytes_per_sec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLeaf: _ClassVar[EntitySpecProto.Type]
        kDataSource: _ClassVar[EntitySpecProto.Type]
    kLeaf: EntitySpecProto.Type
    kDataSource: EntitySpecProto.Type
    class Environment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[EntitySpecProto.Environment]
        kVMware: _ClassVar[EntitySpecProto.Environment]
        kO365: _ClassVar[EntitySpecProto.Environment]
        kNAS: _ClassVar[EntitySpecProto.Environment]
    kInvalid: EntitySpecProto.Environment
    kVMware: EntitySpecProto.Environment
    kO365: EntitySpecProto.Environment
    kNAS: EntitySpecProto.Environment
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SLA_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DAILY_CHANGE_RATE_MEAN_FIELD_NUMBER: _ClassVar[int]
    DAILY_CHANGE_RATE_STDDEV_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_READ_SLOTS_FIELD_NUMBER: _ClassVar[int]
    MAX_READ_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    MAX_WRITE_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: EntitySpecProto.Type
    env: EntitySpecProto.Environment
    tenant_id: str
    logical_size: int
    data_source_entity_name: str
    policy_id: str
    sla_duration_secs: int
    priority: int
    daily_change_rate_mean: float
    daily_change_rate_stddev: float
    num_data_read_slots: int
    max_read_bytes_per_sec: int
    max_write_bytes_per_sec: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[EntitySpecProto.Type, str]] = ..., env: _Optional[_Union[EntitySpecProto.Environment, str]] = ..., tenant_id: _Optional[str] = ..., logical_size: _Optional[int] = ..., data_source_entity_name: _Optional[str] = ..., policy_id: _Optional[str] = ..., sla_duration_secs: _Optional[int] = ..., priority: _Optional[int] = ..., daily_change_rate_mean: _Optional[float] = ..., daily_change_rate_stddev: _Optional[float] = ..., num_data_read_slots: _Optional[int] = ..., max_read_bytes_per_sec: _Optional[int] = ..., max_write_bytes_per_sec: _Optional[int] = ...) -> None: ...

class ClusterSpecProto(_message.Message):
    __slots__ = ("cluster_id", "num_nodes", "policy_vec", "entity_vec", "num_tenants")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_TENANTS_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    num_nodes: int
    policy_vec: _containers.RepeatedCompositeFieldContainer[PolicySpecProto]
    entity_vec: _containers.RepeatedCompositeFieldContainer[EntitySpecProto]
    num_tenants: int
    def __init__(self, cluster_id: _Optional[str] = ..., num_nodes: _Optional[int] = ..., policy_vec: _Optional[_Iterable[_Union[PolicySpecProto, _Mapping]]] = ..., entity_vec: _Optional[_Iterable[_Union[EntitySpecProto, _Mapping]]] = ..., num_tenants: _Optional[int] = ...) -> None: ...
