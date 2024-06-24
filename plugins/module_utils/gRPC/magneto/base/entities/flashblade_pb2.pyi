from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkInterface(_message.Message):
    __slots__ = ("name", "ip_address", "vlan_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    ip_address: str
    vlan_id: int
    def __init__(self, name: _Optional[str] = ..., ip_address: _Optional[str] = ..., vlan_id: _Optional[int] = ...) -> None: ...

class ArrayInfo(_message.Message):
    __slots__ = ("id", "version", "revision", "data_network_interface_vec", "logical_capacity_bytes", "physical_space_used_bytes")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    DATA_NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SPACE_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: str
    revision: str
    data_network_interface_vec: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    logical_capacity_bytes: int
    physical_space_used_bytes: int
    def __init__(self, id: _Optional[str] = ..., version: _Optional[str] = ..., revision: _Optional[str] = ..., data_network_interface_vec: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]] = ..., logical_capacity_bytes: _Optional[int] = ..., physical_space_used_bytes: _Optional[int] = ...) -> None: ...

class NfsInfo(_message.Message):
    __slots__ = ("export_rules",)
    EXPORT_RULES_FIELD_NUMBER: _ClassVar[int]
    export_rules: str
    def __init__(self, export_rules: _Optional[str] = ...) -> None: ...

class FileSystemInfo(_message.Message):
    __slots__ = ("creation_time_msecs", "supported_protocol_vec", "nfs_info", "snapshot_dir_enabled", "logical_capacity_bytes", "total_physical_usage_in_bytes", "unique_usage_in_bytes", "logical_usage_in_bytes")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNfs: _ClassVar[FileSystemInfo.Protocol]
        kCifs2: _ClassVar[FileSystemInfo.Protocol]
        kHttp: _ClassVar[FileSystemInfo.Protocol]
    kNfs: FileSystemInfo.Protocol
    kCifs2: FileSystemInfo.Protocol
    kHttp: FileSystemInfo.Protocol
    CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
    NFS_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_USAGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    creation_time_msecs: int
    supported_protocol_vec: _containers.RepeatedScalarFieldContainer[FileSystemInfo.Protocol]
    nfs_info: NfsInfo
    snapshot_dir_enabled: bool
    logical_capacity_bytes: int
    total_physical_usage_in_bytes: int
    unique_usage_in_bytes: int
    logical_usage_in_bytes: int
    def __init__(self, creation_time_msecs: _Optional[int] = ..., supported_protocol_vec: _Optional[_Iterable[_Union[FileSystemInfo.Protocol, str]]] = ..., nfs_info: _Optional[_Union[NfsInfo, _Mapping]] = ..., snapshot_dir_enabled: bool = ..., logical_capacity_bytes: _Optional[int] = ..., total_physical_usage_in_bytes: _Optional[int] = ..., unique_usage_in_bytes: _Optional[int] = ..., logical_usage_in_bytes: _Optional[int] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "array_info", "file_system_info", "smb_krb5_hostname")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStorageArray: _ClassVar[Entity.Type]
        kFileSystem: _ClassVar[Entity.Type]
    kStorageArray: Entity.Type
    kFileSystem: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARRAY_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    SMB_KRB5_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    array_info: ArrayInfo
    file_system_info: FileSystemInfo
    smb_krb5_hostname: str
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., array_info: _Optional[_Union[ArrayInfo, _Mapping]] = ..., file_system_info: _Optional[_Union[FileSystemInfo, _Mapping]] = ..., smb_krb5_hostname: _Optional[str] = ...) -> None: ...
