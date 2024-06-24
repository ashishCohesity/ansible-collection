from helios.base import helios_cluster_base_pb2 as _helios_cluster_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterTenantInfo(_message.Message):
    __slots__ = ("cluster_identifier", "tenantInfo")
    class TenantInfo(_message.Message):
        __slots__ = ("name", "description", "tenantId", "createdTimeMsecs", "lastUpdatedTimeMsecs", "active", "deleted", "bifrostEnabled", "clusterHostname", "clusterIps")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TENANTID_FIELD_NUMBER: _ClassVar[int]
        CREATEDTIMEMSECS_FIELD_NUMBER: _ClassVar[int]
        LASTUPDATEDTIMEMSECS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        BIFROSTENABLED_FIELD_NUMBER: _ClassVar[int]
        CLUSTERHOSTNAME_FIELD_NUMBER: _ClassVar[int]
        CLUSTERIPS_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        tenantId: str
        createdTimeMsecs: int
        lastUpdatedTimeMsecs: int
        active: bool
        deleted: bool
        bifrostEnabled: bool
        clusterHostname: str
        clusterIps: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., tenantId: _Optional[str] = ..., createdTimeMsecs: _Optional[int] = ..., lastUpdatedTimeMsecs: _Optional[int] = ..., active: bool = ..., deleted: bool = ..., bifrostEnabled: bool = ..., clusterHostname: _Optional[str] = ..., clusterIps: _Optional[_Iterable[str]] = ...) -> None: ...
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TENANTINFO_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _helios_cluster_base_pb2.ClusterIdentifier
    tenantInfo: _containers.RepeatedCompositeFieldContainer[ClusterTenantInfo.TenantInfo]
    def __init__(self, cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2.ClusterIdentifier, _Mapping]] = ..., tenantInfo: _Optional[_Iterable[_Union[ClusterTenantInfo.TenantInfo, _Mapping]]] = ...) -> None: ...
