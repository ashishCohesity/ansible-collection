from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("id", "primary_server", "ces_addresses", "node_info_vec", "use_path_entity_hash_comparator")
    class NodeInfo(_message.Message):
        __slots__ = ("name", "ip_address", "operational_status")
        class OperationalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUp: _ClassVar[ClusterInfo.NodeInfo.OperationalStatus]
            kDown: _ClassVar[ClusterInfo.NodeInfo.OperationalStatus]
        kUp: ClusterInfo.NodeInfo.OperationalStatus
        kDown: ClusterInfo.NodeInfo.OperationalStatus
        NAME_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        OPERATIONAL_STATUS_FIELD_NUMBER: _ClassVar[int]
        name: str
        ip_address: str
        operational_status: ClusterInfo.NodeInfo.OperationalStatus
        def __init__(self, name: _Optional[str] = ..., ip_address: _Optional[str] = ..., operational_status: _Optional[_Union[ClusterInfo.NodeInfo.OperationalStatus, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SERVER_FIELD_NUMBER: _ClassVar[int]
    CES_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    NODE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_PATH_ENTITY_HASH_COMPARATOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    primary_server: str
    ces_addresses: _containers.RepeatedScalarFieldContainer[str]
    node_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterInfo.NodeInfo]
    use_path_entity_hash_comparator: bool
    def __init__(self, id: _Optional[int] = ..., primary_server: _Optional[str] = ..., ces_addresses: _Optional[_Iterable[str]] = ..., node_info_vec: _Optional[_Iterable[_Union[ClusterInfo.NodeInfo, _Mapping]]] = ..., use_path_entity_hash_comparator: bool = ...) -> None: ...

class FilesystemInfo(_message.Message):
    __slots__ = ("id", "path", "capacity_bytes", "used_bytes")
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: str
    capacity_bytes: int
    used_bytes: int
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ..., capacity_bytes: _Optional[int] = ..., used_bytes: _Optional[int] = ...) -> None: ...

class FilesetInfo(_message.Message):
    __slots__ = ("id", "path", "filesystem_name", "supported_protocol_vec", "is_independent_fileset", "fsid", "use_fsid_as_hash_comparator", "use_path_entity_hash_comparator")
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_INDEPENDENT_FILESET_FIELD_NUMBER: _ClassVar[int]
    FSID_FIELD_NUMBER: _ClassVar[int]
    USE_FSID_AS_HASH_COMPARATOR_FIELD_NUMBER: _ClassVar[int]
    USE_PATH_ENTITY_HASH_COMPARATOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    path: str
    filesystem_name: str
    supported_protocol_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.NasProtocol.Type]
    is_independent_fileset: bool
    fsid: str
    use_fsid_as_hash_comparator: bool
    use_path_entity_hash_comparator: bool
    def __init__(self, id: _Optional[int] = ..., path: _Optional[str] = ..., filesystem_name: _Optional[str] = ..., supported_protocol_vec: _Optional[_Iterable[_Union[_enums_pb2.NasProtocol.Type, str]]] = ..., is_independent_fileset: bool = ..., fsid: _Optional[str] = ..., use_fsid_as_hash_comparator: bool = ..., use_path_entity_hash_comparator: bool = ...) -> None: ...

class FilesetSnapshotInfo(_message.Message):
    __slots__ = ("snap_id", "snapshot_name", "filesystem_name", "fileset_name", "created")
    SNAP_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_NAME_FIELD_NUMBER: _ClassVar[int]
    FILESET_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    snap_id: int
    snapshot_name: str
    filesystem_name: str
    fileset_name: str
    created: str
    def __init__(self, snap_id: _Optional[int] = ..., snapshot_name: _Optional[str] = ..., filesystem_name: _Optional[str] = ..., fileset_name: _Optional[str] = ..., created: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "cluster_info", "filesystem_info", "fileset_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kFilesystem: _ClassVar[Entity.Type]
        kFileset: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kFilesystem: Entity.Type
    kFileset: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    FILESET_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    cluster_info: ClusterInfo
    filesystem_info: FilesystemInfo
    fileset_info: FilesetInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., filesystem_info: _Optional[_Union[FilesystemInfo, _Mapping]] = ..., fileset_info: _Optional[_Union[FilesetInfo, _Mapping]] = ...) -> None: ...
