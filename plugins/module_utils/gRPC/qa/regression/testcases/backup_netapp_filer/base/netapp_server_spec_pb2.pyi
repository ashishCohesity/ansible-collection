from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VserverSpec(_message.Message):
    __slots__ = ("name", "root_volume_name", "aggregate", "protocol")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    name: str
    root_volume_name: str
    aggregate: str
    protocol: str
    def __init__(self, name: _Optional[str] = ..., root_volume_name: _Optional[str] = ..., aggregate: _Optional[str] = ..., protocol: _Optional[str] = ...) -> None: ...

class NetworkSpec(_message.Message):
    __slots__ = ("ip_address", "netmask", "vserver_name", "lif", "role", "protocol", "home_node", "port", "force_subnet", "nfsaccess", "nfsv3")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    VSERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    LIF_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HOME_NODE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    FORCE_SUBNET_FIELD_NUMBER: _ClassVar[int]
    NFSACCESS_FIELD_NUMBER: _ClassVar[int]
    NFSV3_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    netmask: str
    vserver_name: str
    lif: str
    role: str
    protocol: str
    home_node: str
    port: str
    force_subnet: str
    nfsaccess: str
    nfsv3: str
    def __init__(self, ip_address: _Optional[str] = ..., netmask: _Optional[str] = ..., vserver_name: _Optional[str] = ..., lif: _Optional[str] = ..., role: _Optional[str] = ..., protocol: _Optional[str] = ..., home_node: _Optional[str] = ..., port: _Optional[str] = ..., force_subnet: _Optional[str] = ..., nfsaccess: _Optional[str] = ..., nfsv3: _Optional[str] = ...) -> None: ...

class ExportPolicySpec(_message.Message):
    __slots__ = ("vserver_name", "policy_name", "client_match", "protocol", "ro_rule", "rw_rule", "superuser")
    VSERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MATCH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    RO_RULE_FIELD_NUMBER: _ClassVar[int]
    RW_RULE_FIELD_NUMBER: _ClassVar[int]
    SUPERUSER_FIELD_NUMBER: _ClassVar[int]
    vserver_name: str
    policy_name: str
    client_match: str
    protocol: str
    ro_rule: str
    rw_rule: str
    superuser: str
    def __init__(self, vserver_name: _Optional[str] = ..., policy_name: _Optional[str] = ..., client_match: _Optional[str] = ..., protocol: _Optional[str] = ..., ro_rule: _Optional[str] = ..., rw_rule: _Optional[str] = ..., superuser: _Optional[str] = ...) -> None: ...

class VolumeSpec(_message.Message):
    __slots__ = ("volume_name", "junction_path", "size", "aggregate", "state", "type", "foreground", "shutdown_force", "policy", "vserver_name", "netapp_vol_mount")
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    JUNCTION_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FOREGROUND_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_FORCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    VSERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    NETAPP_VOL_MOUNT_FIELD_NUMBER: _ClassVar[int]
    volume_name: str
    junction_path: str
    size: str
    aggregate: str
    state: str
    type: str
    foreground: str
    shutdown_force: str
    policy: str
    vserver_name: str
    netapp_vol_mount: str
    def __init__(self, volume_name: _Optional[str] = ..., junction_path: _Optional[str] = ..., size: _Optional[str] = ..., aggregate: _Optional[str] = ..., state: _Optional[str] = ..., type: _Optional[str] = ..., foreground: _Optional[str] = ..., shutdown_force: _Optional[str] = ..., policy: _Optional[str] = ..., vserver_name: _Optional[str] = ..., netapp_vol_mount: _Optional[str] = ...) -> None: ...

class SvmSpec(_message.Message):
    __slots__ = ("vserver_vec", "network_vec", "export_policy_vec", "volume_vec")
    VSERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    vserver_vec: _containers.RepeatedCompositeFieldContainer[VserverSpec]
    network_vec: _containers.RepeatedCompositeFieldContainer[NetworkSpec]
    export_policy_vec: _containers.RepeatedCompositeFieldContainer[ExportPolicySpec]
    volume_vec: _containers.RepeatedCompositeFieldContainer[VolumeSpec]
    def __init__(self, vserver_vec: _Optional[_Iterable[_Union[VserverSpec, _Mapping]]] = ..., network_vec: _Optional[_Iterable[_Union[NetworkSpec, _Mapping]]] = ..., export_policy_vec: _Optional[_Iterable[_Union[ExportPolicySpec, _Mapping]]] = ..., volume_vec: _Optional[_Iterable[_Union[VolumeSpec, _Mapping]]] = ...) -> None: ...

class NetappServerSpec(_message.Message):
    __slots__ = ("svm_vec",)
    SVM_VEC_FIELD_NUMBER: _ClassVar[int]
    svm_vec: _containers.RepeatedCompositeFieldContainer[SvmSpec]
    def __init__(self, svm_vec: _Optional[_Iterable[_Union[SvmSpec, _Mapping]]] = ...) -> None: ...
