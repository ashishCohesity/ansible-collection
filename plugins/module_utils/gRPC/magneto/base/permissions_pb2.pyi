from configs import cluster_config_pb2 as _cluster_config_pb2
from stats.base import stats_types_pb2 as _stats_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityPermissionInfo(_message.Message):
    __slots__ = ("entity_id", "permissions", "tenant_id", "is_inferred", "registering_tenant_id", "is_registered_by_sp", "last_modification_time_usecs")
    class Permission(_message.Message):
        __slots__ = ("sid",)
        SID_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_INFERRED_FIELD_NUMBER: _ClassVar[int]
    REGISTERING_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_BY_SP_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    permissions: _containers.RepeatedCompositeFieldContainer[EntityPermissionInfo.Permission]
    tenant_id: str
    is_inferred: bool
    registering_tenant_id: str
    is_registered_by_sp: bool
    last_modification_time_usecs: int
    def __init__(self, entity_id: _Optional[int] = ..., permissions: _Optional[_Iterable[_Union[EntityPermissionInfo.Permission, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., is_inferred: bool = ..., registering_tenant_id: _Optional[str] = ..., is_registered_by_sp: bool = ..., last_modification_time_usecs: _Optional[int] = ...) -> None: ...

class UserInformation(_message.Message):
    __slots__ = ("pulse_attribute_vec", "sid_vec", "tenant_id_vec", "include_subtenant_objects")
    PULSE_ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SUBTENANT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    pulse_attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    include_subtenant_objects: bool
    def __init__(self, pulse_attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., include_subtenant_objects: bool = ...) -> None: ...
