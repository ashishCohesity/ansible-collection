from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("uuid", "name", "version", "load_balancer_vip", "enode_ip_address_vec")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_VIP_FIELD_NUMBER: _ClassVar[int]
    ENODE_IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    version: str
    load_balancer_vip: str
    enode_ip_address_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., load_balancer_vip: _Optional[str] = ..., enode_ip_address_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ContainerInfo(_message.Message):
    __slots__ = ("id", "name", "uuid", "used_bytes", "created_at", "is_nfs_interface", "is_smb_interface", "supported_protocol_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_NFS_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    IS_SMB_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    uuid: str
    used_bytes: int
    created_at: str
    is_nfs_interface: bool
    is_smb_interface: bool
    supported_protocol_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.NasProtocol.Type]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., used_bytes: _Optional[int] = ..., created_at: _Optional[str] = ..., is_nfs_interface: bool = ..., is_smb_interface: bool = ..., supported_protocol_vec: _Optional[_Iterable[_Union[_enums_pb2.NasProtocol.Type, str]]] = ...) -> None: ...

class ElastifileSnapshotInfo(_message.Message):
    __slots__ = ("id", "name", "uuid", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    uuid: str
    created_at: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "cluster_info", "container_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kContainer: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kContainer: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    cluster_info: ClusterInfo
    container_info: ContainerInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., container_info: _Optional[_Union[ContainerInfo, _Mapping]] = ...) -> None: ...
