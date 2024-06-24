from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("contact_info", "location", "serial_number")
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    contact_info: str
    location: str
    serial_number: str
    def __init__(self, contact_info: _Optional[str] = ..., location: _Optional[str] = ..., serial_number: _Optional[str] = ...) -> None: ...

class DataProtocol(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNfs: _ClassVar[DataProtocol.Type]
        kNfs3: _ClassVar[DataProtocol.Type]
        kNfs4_1: _ClassVar[DataProtocol.Type]
        kCifs: _ClassVar[DataProtocol.Type]
        kIscsi: _ClassVar[DataProtocol.Type]
        kFc: _ClassVar[DataProtocol.Type]
        kFcache: _ClassVar[DataProtocol.Type]
        kHttp: _ClassVar[DataProtocol.Type]
        kNdmp: _ClassVar[DataProtocol.Type]
        kManagement: _ClassVar[DataProtocol.Type]
        kNvme: _ClassVar[DataProtocol.Type]
    kNfs: DataProtocol.Type
    kNfs3: DataProtocol.Type
    kNfs4_1: DataProtocol.Type
    kCifs: DataProtocol.Type
    kIscsi: DataProtocol.Type
    kFc: DataProtocol.Type
    kFcache: DataProtocol.Type
    kHttp: DataProtocol.Type
    kNdmp: DataProtocol.Type
    kManagement: DataProtocol.Type
    kNvme: DataProtocol.Type
    def __init__(self) -> None: ...

class CifsShareInfo(_message.Message):
    __slots__ = ("name", "path", "cifs_server_name", "acl_string_vec")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CIFS_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    ACL_STRING_VEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    cifs_server_name: str
    acl_string_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., cifs_server_name: _Optional[str] = ..., acl_string_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class VserverInfo(_message.Message):
    __slots__ = ("type", "interface_vec", "data_protocol_vec", "root_cifs_share", "volume_info_vec", "nfsv3_enabled", "nfsv41_enabled", "smb_krb5_hostname")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kData: _ClassVar[VserverInfo.Type]
        kAdmin: _ClassVar[VserverInfo.Type]
        kSystem: _ClassVar[VserverInfo.Type]
        kNode: _ClassVar[VserverInfo.Type]
        kUnknown: _ClassVar[VserverInfo.Type]
    kData: VserverInfo.Type
    kAdmin: VserverInfo.Type
    kSystem: VserverInfo.Type
    kNode: VserverInfo.Type
    kUnknown: VserverInfo.Type
    class NetworkInterfaceInfo(_message.Message):
        __slots__ = ("name", "ip_address", "fqdn", "data_protocol_vec", "operational_status", "kerberos_enabled")
        class OperationalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUp: _ClassVar[VserverInfo.NetworkInterfaceInfo.OperationalStatus]
            kDown: _ClassVar[VserverInfo.NetworkInterfaceInfo.OperationalStatus]
        kUp: VserverInfo.NetworkInterfaceInfo.OperationalStatus
        kDown: VserverInfo.NetworkInterfaceInfo.OperationalStatus
        NAME_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        FQDN_FIELD_NUMBER: _ClassVar[int]
        DATA_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
        OPERATIONAL_STATUS_FIELD_NUMBER: _ClassVar[int]
        KERBEROS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        name: str
        ip_address: str
        fqdn: str
        data_protocol_vec: _containers.RepeatedScalarFieldContainer[DataProtocol.Type]
        operational_status: VserverInfo.NetworkInterfaceInfo.OperationalStatus
        kerberos_enabled: bool
        def __init__(self, name: _Optional[str] = ..., ip_address: _Optional[str] = ..., fqdn: _Optional[str] = ..., data_protocol_vec: _Optional[_Iterable[_Union[DataProtocol.Type, str]]] = ..., operational_status: _Optional[_Union[VserverInfo.NetworkInterfaceInfo.OperationalStatus, str]] = ..., kerberos_enabled: bool = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_CIFS_SHARE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NFSV3_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NFSV41_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SMB_KRB5_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    type: VserverInfo.Type
    interface_vec: _containers.RepeatedCompositeFieldContainer[VserverInfo.NetworkInterfaceInfo]
    data_protocol_vec: _containers.RepeatedScalarFieldContainer[DataProtocol.Type]
    root_cifs_share: CifsShareInfo
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[Entity]
    nfsv3_enabled: bool
    nfsv41_enabled: bool
    smb_krb5_hostname: str
    def __init__(self, type: _Optional[_Union[VserverInfo.Type, str]] = ..., interface_vec: _Optional[_Iterable[_Union[VserverInfo.NetworkInterfaceInfo, _Mapping]]] = ..., data_protocol_vec: _Optional[_Iterable[_Union[DataProtocol.Type, str]]] = ..., root_cifs_share: _Optional[_Union[CifsShareInfo, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., nfsv3_enabled: bool = ..., nfsv41_enabled: bool = ..., smb_krb5_hostname: _Optional[str] = ...) -> None: ...

class VolumeInfo(_message.Message):
    __slots__ = ("volume_creation_time", "vserver_name", "aggregate_name", "type", "state", "capacity_bytes", "used_bytes", "junction_path", "export_policy_name", "data_protocol_vec", "cifs_share_info_vec", "extended_style", "security_info", "snapshot_dir_visible", "snapshot_count", "volume_uuid", "qtree_info_map", "snapshot_info_vec", "node_name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReadWrite: _ClassVar[VolumeInfo.Type]
        kLoadSharing: _ClassVar[VolumeInfo.Type]
        kDataProtection: _ClassVar[VolumeInfo.Type]
        kDataCache: _ClassVar[VolumeInfo.Type]
        kTmp: _ClassVar[VolumeInfo.Type]
        kUnknownType: _ClassVar[VolumeInfo.Type]
    kReadWrite: VolumeInfo.Type
    kLoadSharing: VolumeInfo.Type
    kDataProtection: VolumeInfo.Type
    kDataCache: VolumeInfo.Type
    kTmp: VolumeInfo.Type
    kUnknownType: VolumeInfo.Type
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOnline: _ClassVar[VolumeInfo.State]
        kRestricted: _ClassVar[VolumeInfo.State]
        kOffline: _ClassVar[VolumeInfo.State]
        kMixed: _ClassVar[VolumeInfo.State]
        kUnknownState: _ClassVar[VolumeInfo.State]
    kOnline: VolumeInfo.State
    kRestricted: VolumeInfo.State
    kOffline: VolumeInfo.State
    kMixed: VolumeInfo.State
    kUnknownState: VolumeInfo.State
    class ExtendedStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFlexVol: _ClassVar[VolumeInfo.ExtendedStyle]
        kFlexGroup: _ClassVar[VolumeInfo.ExtendedStyle]
    kFlexVol: VolumeInfo.ExtendedStyle
    kFlexGroup: VolumeInfo.ExtendedStyle
    class SecurityInfo(_message.Message):
        __slots__ = ("style", "unix_user_id", "unix_group_id", "unix_permissions")
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnix: _ClassVar[VolumeInfo.SecurityInfo.Style]
            kNtfs: _ClassVar[VolumeInfo.SecurityInfo.Style]
            kMixed: _ClassVar[VolumeInfo.SecurityInfo.Style]
            kUnified: _ClassVar[VolumeInfo.SecurityInfo.Style]
            kUnknown: _ClassVar[VolumeInfo.SecurityInfo.Style]
        kUnix: VolumeInfo.SecurityInfo.Style
        kNtfs: VolumeInfo.SecurityInfo.Style
        kMixed: VolumeInfo.SecurityInfo.Style
        kUnified: VolumeInfo.SecurityInfo.Style
        kUnknown: VolumeInfo.SecurityInfo.Style
        STYLE_FIELD_NUMBER: _ClassVar[int]
        UNIX_USER_ID_FIELD_NUMBER: _ClassVar[int]
        UNIX_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        UNIX_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        style: VolumeInfo.SecurityInfo.Style
        unix_user_id: int
        unix_group_id: int
        unix_permissions: str
        def __init__(self, style: _Optional[_Union[VolumeInfo.SecurityInfo.Style, str]] = ..., unix_user_id: _Optional[int] = ..., unix_group_id: _Optional[int] = ..., unix_permissions: _Optional[str] = ...) -> None: ...
    class QtreeInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SnapshotInfo(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    VOLUME_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    VSERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    JUNCTION_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_PROTOCOL_VEC_FIELD_NUMBER: _ClassVar[int]
    CIFS_SHARE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_STYLE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_UUID_FIELD_NUMBER: _ClassVar[int]
    QTREE_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    volume_creation_time: int
    vserver_name: str
    aggregate_name: str
    type: VolumeInfo.Type
    state: VolumeInfo.State
    capacity_bytes: int
    used_bytes: int
    junction_path: str
    export_policy_name: str
    data_protocol_vec: _containers.RepeatedScalarFieldContainer[DataProtocol.Type]
    cifs_share_info_vec: _containers.RepeatedCompositeFieldContainer[CifsShareInfo]
    extended_style: VolumeInfo.ExtendedStyle
    security_info: VolumeInfo.SecurityInfo
    snapshot_dir_visible: bool
    snapshot_count: int
    volume_uuid: str
    qtree_info_map: _containers.ScalarMap[str, str]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfo.SnapshotInfo]
    node_name: str
    def __init__(self, volume_creation_time: _Optional[int] = ..., vserver_name: _Optional[str] = ..., aggregate_name: _Optional[str] = ..., type: _Optional[_Union[VolumeInfo.Type, str]] = ..., state: _Optional[_Union[VolumeInfo.State, str]] = ..., capacity_bytes: _Optional[int] = ..., used_bytes: _Optional[int] = ..., junction_path: _Optional[str] = ..., export_policy_name: _Optional[str] = ..., data_protocol_vec: _Optional[_Iterable[_Union[DataProtocol.Type, str]]] = ..., cifs_share_info_vec: _Optional[_Iterable[_Union[CifsShareInfo, _Mapping]]] = ..., extended_style: _Optional[_Union[VolumeInfo.ExtendedStyle, str]] = ..., security_info: _Optional[_Union[VolumeInfo.SecurityInfo, _Mapping]] = ..., snapshot_dir_visible: bool = ..., snapshot_count: _Optional[int] = ..., volume_uuid: _Optional[str] = ..., qtree_info_map: _Optional[_Mapping[str, str]] = ..., snapshot_info_vec: _Optional[_Iterable[_Union[VolumeInfo.SnapshotInfo, _Mapping]]] = ..., node_name: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "is_top_level_entity", "cluster_info", "vserver_info", "volume_info", "can_skip_updating_uuids", "vserver_info_vec", "version_tuple", "license_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kVserver: _ClassVar[Entity.Type]
        kVolume: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kVserver: Entity.Type
    kVolume: Entity.Type
    class LicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnapmirrorCloud: _ClassVar[Entity.LicenseType]
    kSnapmirrorCloud: Entity.LicenseType
    class VersionTuple(_message.Message):
        __slots__ = ("generation", "major_version", "minor_version")
        GENERATION_FIELD_NUMBER: _ClassVar[int]
        MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        generation: int
        major_version: int
        minor_version: int
        def __init__(self, generation: _Optional[int] = ..., major_version: _Optional[int] = ..., minor_version: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    IS_TOP_LEVEL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    VSERVER_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    CAN_SKIP_UPDATING_UUIDS_FIELD_NUMBER: _ClassVar[int]
    VSERVER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_TUPLE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_VEC_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    is_top_level_entity: bool
    cluster_info: ClusterInfo
    vserver_info: VserverInfo
    volume_info: VolumeInfo
    can_skip_updating_uuids: bool
    vserver_info_vec: _containers.RepeatedCompositeFieldContainer[VserverInfo]
    version_tuple: Entity.VersionTuple
    license_vec: _containers.RepeatedScalarFieldContainer[Entity.LicenseType]
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., is_top_level_entity: bool = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., vserver_info: _Optional[_Union[VserverInfo, _Mapping]] = ..., volume_info: _Optional[_Union[VolumeInfo, _Mapping]] = ..., can_skip_updating_uuids: bool = ..., vserver_info_vec: _Optional[_Iterable[_Union[VserverInfo, _Mapping]]] = ..., version_tuple: _Optional[_Union[Entity.VersionTuple, _Mapping]] = ..., license_vec: _Optional[_Iterable[_Union[Entity.LicenseType, str]]] = ...) -> None: ...
