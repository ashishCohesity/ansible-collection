from magneto.connectors.san import san_pb2 as _san_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorContext(_message.Message):
    __slots__ = ("msg", "ctx", "severity", "text")
    MSG_FIELD_NUMBER: _ClassVar[int]
    CTX_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    msg: str
    ctx: str
    severity: str
    text: str
    def __init__(self, msg: _Optional[str] = ..., ctx: _Optional[str] = ..., severity: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class ErrorContextVec(_message.Message):
    __slots__ = ("error_ctx_vec", "messages")
    ERROR_CTX_VEC_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    error_ctx_vec: _containers.RepeatedCompositeFieldContainer[ErrorContext]
    messages: _containers.RepeatedCompositeFieldContainer[ErrorContext]
    def __init__(self, error_ctx_vec: _Optional[_Iterable[_Union[ErrorContext, _Mapping]]] = ..., messages: _Optional[_Iterable[_Union[ErrorContext, _Mapping]]] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("created", "name", "serial", "size", "source", "id", "online", "online_snaps", "iqn", "parent_id", "parent_name", "availability_group_name", "raw_response", "storage_pool_id", "storage_pool_name", "is_secured", "provisioning", "compression", "deduplication", "availability_group_id")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SNAPS_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RAW_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SECURED_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    created: str
    name: str
    serial: str
    size: int
    source: str
    id: str
    online: bool
    online_snaps: _containers.RepeatedCompositeFieldContainer[Volume]
    iqn: str
    parent_id: str
    parent_name: str
    availability_group_name: str
    raw_response: bytes
    storage_pool_id: str
    storage_pool_name: str
    is_secured: bool
    provisioning: _san_pb2.Provisioning.Type
    compression: _san_pb2.Compression.Type
    deduplication: _san_pb2.Deduplication.Type
    availability_group_id: str
    def __init__(self, created: _Optional[str] = ..., name: _Optional[str] = ..., serial: _Optional[str] = ..., size: _Optional[int] = ..., source: _Optional[str] = ..., id: _Optional[str] = ..., online: bool = ..., online_snaps: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., iqn: _Optional[str] = ..., parent_id: _Optional[str] = ..., parent_name: _Optional[str] = ..., availability_group_name: _Optional[str] = ..., raw_response: _Optional[bytes] = ..., storage_pool_id: _Optional[str] = ..., storage_pool_name: _Optional[str] = ..., is_secured: bool = ..., provisioning: _Optional[_Union[_san_pb2.Provisioning.Type, str]] = ..., compression: _Optional[_Union[_san_pb2.Compression.Type, str]] = ..., deduplication: _Optional[_Union[_san_pb2.Deduplication.Type, str]] = ..., availability_group_id: _Optional[str] = ...) -> None: ...

class ProtectionGroup(_message.Message):
    __slots__ = ("name", "volumes", "source", "created")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    volumes: _containers.RepeatedScalarFieldContainer[str]
    source: str
    created: str
    def __init__(self, name: _Optional[str] = ..., volumes: _Optional[_Iterable[str]] = ..., source: _Optional[str] = ..., created: _Optional[str] = ...) -> None: ...

class VolumeSpaceInfo(_message.Message):
    __slots__ = ("total", "name", "snapshots", "volumes")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    total: int
    name: str
    snapshots: int
    volumes: int
    def __init__(self, total: _Optional[int] = ..., name: _Optional[str] = ..., snapshots: _Optional[int] = ..., volumes: _Optional[int] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("hgroup", "hgroup_id", "id", "ip_address", "name", "iqn", "wwn")
    HGROUP_FIELD_NUMBER: _ClassVar[int]
    HGROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    WWN_FIELD_NUMBER: _ClassVar[int]
    hgroup: str
    hgroup_id: str
    id: str
    ip_address: str
    name: str
    iqn: _containers.RepeatedScalarFieldContainer[str]
    wwn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hgroup: _Optional[str] = ..., hgroup_id: _Optional[str] = ..., id: _Optional[str] = ..., ip_address: _Optional[str] = ..., name: _Optional[str] = ..., iqn: _Optional[_Iterable[str]] = ..., wwn: _Optional[_Iterable[str]] = ...) -> None: ...

class VolumeHostConnection(_message.Message):
    __slots__ = ("host", "lun", "name", "size")
    HOST_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    host: str
    lun: int
    name: str
    size: int
    def __init__(self, host: _Optional[str] = ..., lun: _Optional[int] = ..., name: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class VolumeHGroupConnection(_message.Message):
    __slots__ = ("hgroup", "host", "lun", "name", "size_bytes")
    HGROUP_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    hgroup: str
    host: str
    lun: int
    name: str
    size_bytes: int
    def __init__(self, hgroup: _Optional[str] = ..., host: _Optional[str] = ..., lun: _Optional[int] = ..., name: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class HostVolumeConnection(_message.Message):
    __slots__ = ("hgroup", "lun", "name", "vol")
    HGROUP_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_FIELD_NUMBER: _ClassVar[int]
    hgroup: str
    lun: int
    name: str
    vol: str
    def __init__(self, hgroup: _Optional[str] = ..., lun: _Optional[int] = ..., name: _Optional[str] = ..., vol: _Optional[str] = ...) -> None: ...

class HGroupVolumeConnection(_message.Message):
    __slots__ = ("lun", "name", "vol")
    LUN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_FIELD_NUMBER: _ClassVar[int]
    lun: int
    name: str
    vol: str
    def __init__(self, lun: _Optional[int] = ..., name: _Optional[str] = ..., vol: _Optional[str] = ...) -> None: ...

class VolumeArea(_message.Message):
    __slots__ = ("offset", "length", "startRow", "endRow")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    STARTROW_FIELD_NUMBER: _ClassVar[int]
    ENDROW_FIELD_NUMBER: _ClassVar[int]
    offset: int
    length: int
    startRow: int
    endRow: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ..., startRow: _Optional[int] = ..., endRow: _Optional[int] = ...) -> None: ...

class Port(_message.Message):
    __slots__ = ("name", "portal", "iqn", "wwn")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORTAL_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    WWN_FIELD_NUMBER: _ClassVar[int]
    name: str
    portal: str
    iqn: str
    wwn: str
    def __init__(self, name: _Optional[str] = ..., portal: _Optional[str] = ..., iqn: _Optional[str] = ..., wwn: _Optional[str] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TokenRequest(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class TokenResponse(_message.Message):
    __slots__ = ("api_token",)
    API_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_token: str
    def __init__(self, api_token: _Optional[str] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("api_token",)
    API_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_token: str
    def __init__(self, api_token: _Optional[str] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class GetArrayResponse(_message.Message):
    __slots__ = ("array_name", "id", "revision", "version")
    ARRAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    array_name: str
    id: str
    revision: str
    version: str
    def __init__(self, array_name: _Optional[str] = ..., id: _Optional[str] = ..., revision: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GetPortResponse(_message.Message):
    __slots__ = ("port_vec",)
    PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    port_vec: _containers.RepeatedCompositeFieldContainer[Port]
    def __init__(self, port_vec: _Optional[_Iterable[_Union[Port, _Mapping]]] = ...) -> None: ...

class GetVolumesResponse(_message.Message):
    __slots__ = ("volume_vec",)
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_vec: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, volume_vec: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class GetVolumesSpaceResponse(_message.Message):
    __slots__ = ("volume_space_info_vec",)
    VOLUME_SPACE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_space_info_vec: _containers.RepeatedCompositeFieldContainer[VolumeSpaceInfo]
    def __init__(self, volume_space_info_vec: _Optional[_Iterable[_Union[VolumeSpaceInfo, _Mapping]]] = ...) -> None: ...

class GetVolumeHostsResponse(_message.Message):
    __slots__ = ("volume_host_connection_vec",)
    VOLUME_HOST_CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_host_connection_vec: _containers.RepeatedCompositeFieldContainer[VolumeHostConnection]
    def __init__(self, volume_host_connection_vec: _Optional[_Iterable[_Union[VolumeHostConnection, _Mapping]]] = ...) -> None: ...

class GetVolumeHGroupsResponse(_message.Message):
    __slots__ = ("volume_hgroup_connection_vec",)
    VOLUME_HGROUP_CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_hgroup_connection_vec: _containers.RepeatedCompositeFieldContainer[VolumeHGroupConnection]
    def __init__(self, volume_hgroup_connection_vec: _Optional[_Iterable[_Union[VolumeHGroupConnection, _Mapping]]] = ...) -> None: ...

class GetHostsResponse(_message.Message):
    __slots__ = ("host_vec",)
    HOST_VEC_FIELD_NUMBER: _ClassVar[int]
    host_vec: _containers.RepeatedCompositeFieldContainer[Host]
    def __init__(self, host_vec: _Optional[_Iterable[_Union[Host, _Mapping]]] = ...) -> None: ...

class GetHostResponse(_message.Message):
    __slots__ = ("name", "hgroup", "iqn", "wwn")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HGROUP_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    WWN_FIELD_NUMBER: _ClassVar[int]
    name: str
    hgroup: str
    iqn: _containers.RepeatedScalarFieldContainer[str]
    wwn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., hgroup: _Optional[str] = ..., iqn: _Optional[_Iterable[str]] = ..., wwn: _Optional[_Iterable[str]] = ...) -> None: ...

class AddHostRequest(_message.Message):
    __slots__ = ("iqnlist", "wwnlist")
    IQNLIST_FIELD_NUMBER: _ClassVar[int]
    WWNLIST_FIELD_NUMBER: _ClassVar[int]
    iqnlist: _containers.RepeatedScalarFieldContainer[str]
    wwnlist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, iqnlist: _Optional[_Iterable[str]] = ..., wwnlist: _Optional[_Iterable[str]] = ...) -> None: ...

class AddHostResponse(_message.Message):
    __slots__ = ("name", "iqn")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    name: str
    iqn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., iqn: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateHostRequest(_message.Message):
    __slots__ = ("iqnlist", "remiqnlist", "wwnlist", "remwwnlist")
    IQNLIST_FIELD_NUMBER: _ClassVar[int]
    REMIQNLIST_FIELD_NUMBER: _ClassVar[int]
    WWNLIST_FIELD_NUMBER: _ClassVar[int]
    REMWWNLIST_FIELD_NUMBER: _ClassVar[int]
    iqnlist: _containers.RepeatedScalarFieldContainer[str]
    remiqnlist: _containers.RepeatedScalarFieldContainer[str]
    wwnlist: _containers.RepeatedScalarFieldContainer[str]
    remwwnlist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, iqnlist: _Optional[_Iterable[str]] = ..., remiqnlist: _Optional[_Iterable[str]] = ..., wwnlist: _Optional[_Iterable[str]] = ..., remwwnlist: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateHostResponse(_message.Message):
    __slots__ = ("name", "iqn")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IQN_FIELD_NUMBER: _ClassVar[int]
    name: str
    iqn: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., iqn: _Optional[_Iterable[str]] = ...) -> None: ...

class GetHostVolumesResponse(_message.Message):
    __slots__ = ("host_volume_connection_vec",)
    HOST_VOLUME_CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    host_volume_connection_vec: _containers.RepeatedCompositeFieldContainer[HostVolumeConnection]
    def __init__(self, host_volume_connection_vec: _Optional[_Iterable[_Union[HostVolumeConnection, _Mapping]]] = ...) -> None: ...

class UpdateHostConnectionRequest(_message.Message):
    __slots__ = ("lun",)
    LUN_FIELD_NUMBER: _ClassVar[int]
    lun: int
    def __init__(self, lun: _Optional[int] = ...) -> None: ...

class UpdateHostConnectionResponse(_message.Message):
    __slots__ = ("lun", "name", "vol")
    LUN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_FIELD_NUMBER: _ClassVar[int]
    lun: int
    name: str
    vol: str
    def __init__(self, lun: _Optional[int] = ..., name: _Optional[str] = ..., vol: _Optional[str] = ...) -> None: ...

class GetHGroupVolumesResponse(_message.Message):
    __slots__ = ("hgroup_volume_connection_vec",)
    HGROUP_VOLUME_CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    hgroup_volume_connection_vec: _containers.RepeatedCompositeFieldContainer[HGroupVolumeConnection]
    def __init__(self, hgroup_volume_connection_vec: _Optional[_Iterable[_Union[HGroupVolumeConnection, _Mapping]]] = ...) -> None: ...

class UpdateHGroupConnectionRequest(_message.Message):
    __slots__ = ("lun",)
    LUN_FIELD_NUMBER: _ClassVar[int]
    lun: int
    def __init__(self, lun: _Optional[int] = ...) -> None: ...

class UpdateHGroupConnectionResponse(_message.Message):
    __slots__ = ("lun", "name", "vol")
    LUN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOL_FIELD_NUMBER: _ClassVar[int]
    lun: int
    name: str
    vol: str
    def __init__(self, lun: _Optional[int] = ..., name: _Optional[str] = ..., vol: _Optional[str] = ...) -> None: ...

class CreateSnapshotsRequest(_message.Message):
    __slots__ = ("snap", "source", "suffix")
    SNAP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    snap: bool
    source: _containers.RepeatedScalarFieldContainer[str]
    suffix: str
    def __init__(self, snap: bool = ..., source: _Optional[_Iterable[str]] = ..., suffix: _Optional[str] = ...) -> None: ...

class CreateSnapshotsResponse(_message.Message):
    __slots__ = ("snapshot_vec",)
    SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_vec: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, snapshot_vec: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateVolumeRequest(_message.Message):
    __slots__ = ("overwrite", "size", "source")
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    overwrite: bool
    size: int
    source: str
    def __init__(self, overwrite: bool = ..., size: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...

class GetVolumeAreasResponse(_message.Message):
    __slots__ = ("volume_area_vec",)
    VOLUME_AREA_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_area_vec: _containers.RepeatedCompositeFieldContainer[VolumeArea]
    def __init__(self, volume_area_vec: _Optional[_Iterable[_Union[VolumeArea, _Mapping]]] = ...) -> None: ...

class GetDNSResponse(_message.Message):
    __slots__ = ("domain", "nameservers")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    nameservers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain: _Optional[str] = ..., nameservers: _Optional[_Iterable[str]] = ...) -> None: ...

class GetProtectionGroupsResponse(_message.Message):
    __slots__ = ("protection_group_vec",)
    PROTECTION_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    protection_group_vec: _containers.RepeatedCompositeFieldContainer[ProtectionGroup]
    def __init__(self, protection_group_vec: _Optional[_Iterable[_Union[ProtectionGroup, _Mapping]]] = ...) -> None: ...

class CreateProtectionGroupSnapshotRequest(_message.Message):
    __slots__ = ("snap", "source", "suffix")
    SNAP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    snap: bool
    source: _containers.RepeatedScalarFieldContainer[str]
    suffix: str
    def __init__(self, snap: bool = ..., source: _Optional[_Iterable[str]] = ..., suffix: _Optional[str] = ...) -> None: ...

class CreateProtectionGroupSnapshotResponse(_message.Message):
    __slots__ = ("protection_group_snapshot_vec",)
    PROTECTION_GROUP_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    protection_group_snapshot_vec: _containers.RepeatedCompositeFieldContainer[ProtectionGroup]
    def __init__(self, protection_group_snapshot_vec: _Optional[_Iterable[_Union[ProtectionGroup, _Mapping]]] = ...) -> None: ...

class LookupProtectionGroupSnapshotResponse(_message.Message):
    __slots__ = ("protection_group_snapshot_vec",)
    PROTECTION_GROUP_SNAPSHOT_VEC_FIELD_NUMBER: _ClassVar[int]
    protection_group_snapshot_vec: _containers.RepeatedCompositeFieldContainer[ProtectionGroup]
    def __init__(self, protection_group_snapshot_vec: _Optional[_Iterable[_Union[ProtectionGroup, _Mapping]]] = ...) -> None: ...

class DeleteProtectionGroupSnapshotResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateProtectionGroupRequest(_message.Message):
    __slots__ = ("vollist",)
    VOLLIST_FIELD_NUMBER: _ClassVar[int]
    vollist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vollist: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateProtectionGroupRequest(_message.Message):
    __slots__ = ("addvollist", "remvollist", "vollist")
    ADDVOLLIST_FIELD_NUMBER: _ClassVar[int]
    REMVOLLIST_FIELD_NUMBER: _ClassVar[int]
    VOLLIST_FIELD_NUMBER: _ClassVar[int]
    addvollist: _containers.RepeatedScalarFieldContainer[str]
    remvollist: _containers.RepeatedScalarFieldContainer[str]
    vollist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, addvollist: _Optional[_Iterable[str]] = ..., remvollist: _Optional[_Iterable[str]] = ..., vollist: _Optional[_Iterable[str]] = ...) -> None: ...
