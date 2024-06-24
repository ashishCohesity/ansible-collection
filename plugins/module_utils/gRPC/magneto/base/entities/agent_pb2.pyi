from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Properties(_message.Message):
    __slots__ = ("status", "agent_sw_version_str", "upgradability", "upgrade_status", "upgrade_error", "cbmr_info", "host_type", "linux_pkg_type", "agent_type", "machine_identifier", "machine_uuid", "vol_cbt_info", "file_cbt_info", "solaris_pkg_type")
    class UpgradeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIdle: _ClassVar[Properties.UpgradeStatus]
        kAccepted: _ClassVar[Properties.UpgradeStatus]
        kStarted: _ClassVar[Properties.UpgradeStatus]
        kFinished: _ClassVar[Properties.UpgradeStatus]
        kScheduled: _ClassVar[Properties.UpgradeStatus]
    kIdle: Properties.UpgradeStatus
    kAccepted: Properties.UpgradeStatus
    kStarted: Properties.UpgradeStatus
    kFinished: Properties.UpgradeStatus
    kScheduled: Properties.UpgradeStatus
    class Upgradability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpgradable: _ClassVar[Properties.Upgradability]
        kCurrent: _ClassVar[Properties.Upgradability]
        kUnknown: _ClassVar[Properties.Upgradability]
        kNonUpgradableInvalidVersion: _ClassVar[Properties.Upgradability]
        kNonUpgradableAgentIsNewer: _ClassVar[Properties.Upgradability]
        kNonUpgradableAgentIsOld: _ClassVar[Properties.Upgradability]
    kUpgradable: Properties.Upgradability
    kCurrent: Properties.Upgradability
    kUnknown: Properties.Upgradability
    kNonUpgradableInvalidVersion: Properties.Upgradability
    kNonUpgradableAgentIsNewer: Properties.Upgradability
    kNonUpgradableAgentIsOld: Properties.Upgradability
    class Status(_message.Message):
        __slots__ = ("type", "detail_msg")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[Properties.Status.Type]
            kUnreachable: _ClassVar[Properties.Status.Type]
            kHealthy: _ClassVar[Properties.Status.Type]
            kDegraded: _ClassVar[Properties.Status.Type]
            kUnHealthy: _ClassVar[Properties.Status.Type]
        kUnknown: Properties.Status.Type
        kUnreachable: Properties.Status.Type
        kHealthy: Properties.Status.Type
        kDegraded: Properties.Status.Type
        kUnHealthy: Properties.Status.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DETAIL_MSG_FIELD_NUMBER: _ClassVar[int]
        type: Properties.Status.Type
        detail_msg: str
        def __init__(self, type: _Optional[_Union[Properties.Status.Type, str]] = ..., detail_msg: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AGENT_SW_VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    UPGRADABILITY_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_ERROR_FIELD_NUMBER: _ClassVar[int]
    CBMR_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    LINUX_PKG_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MACHINE_UUID_FIELD_NUMBER: _ClassVar[int]
    VOL_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_CBT_INFO_FIELD_NUMBER: _ClassVar[int]
    SOLARIS_PKG_TYPE_FIELD_NUMBER: _ClassVar[int]
    status: Properties.Status
    agent_sw_version_str: str
    upgradability: Properties.Upgradability
    upgrade_status: Properties.UpgradeStatus
    upgrade_error: _error_pb2.ErrorProto
    cbmr_info: _agent_pb2.CBMRInfo
    host_type: _enums_pb2.HostEnv.Type
    linux_pkg_type: _agent_pb2.AgentInfoProto.LinuxAgentPackageType
    agent_type: _agent_pb2.AgentInfoProto.AgentType
    machine_identifier: str
    machine_uuid: str
    vol_cbt_info: _agent_pb2.CbtInfo
    file_cbt_info: _agent_pb2.CbtInfo
    solaris_pkg_type: _agent_pb2.AgentInfoProto.SolarisAgentPackageType
    def __init__(self, status: _Optional[_Union[Properties.Status, _Mapping]] = ..., agent_sw_version_str: _Optional[str] = ..., upgradability: _Optional[_Union[Properties.Upgradability, str]] = ..., upgrade_status: _Optional[_Union[Properties.UpgradeStatus, str]] = ..., upgrade_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cbmr_info: _Optional[_Union[_agent_pb2.CBMRInfo, _Mapping]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., linux_pkg_type: _Optional[_Union[_agent_pb2.AgentInfoProto.LinuxAgentPackageType, str]] = ..., agent_type: _Optional[_Union[_agent_pb2.AgentInfoProto.AgentType, str]] = ..., machine_identifier: _Optional[str] = ..., machine_uuid: _Optional[str] = ..., vol_cbt_info: _Optional[_Union[_agent_pb2.CbtInfo, _Mapping]] = ..., file_cbt_info: _Optional[_Union[_agent_pb2.CbtInfo, _Mapping]] = ..., solaris_pkg_type: _Optional[_Union[_agent_pb2.AgentInfoProto.SolarisAgentPackageType, str]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "agent_uid", "name", "host_type", "properties", "owner_entity_id_vec", "installer_uri", "linux_installer_args", "windows_installer_args", "aix_installer_args", "refresh_error", "supported_features", "config_scribe_key", "config_file_timestamp", "agent_cert_info", "solaris_installer_args", "hpux_installer_args", "agent_port")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGroup: _ClassVar[Entity.Type]
        kHost: _ClassVar[Entity.Type]
    kGroup: Entity.Type
    kHost: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTALLER_URI_FIELD_NUMBER: _ClassVar[int]
    LINUX_INSTALLER_ARGS_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_INSTALLER_ARGS_FIELD_NUMBER: _ClassVar[int]
    AIX_INSTALLER_ARGS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_ERROR_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SCRIBE_KEY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AGENT_CERT_INFO_FIELD_NUMBER: _ClassVar[int]
    SOLARIS_INSTALLER_ARGS_FIELD_NUMBER: _ClassVar[int]
    HPUX_INSTALLER_ARGS_FIELD_NUMBER: _ClassVar[int]
    AGENT_PORT_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    agent_uid: _universal_id_pb2.UniversalIdProto
    name: str
    host_type: _enums_pb2.HostEnv.Type
    properties: Properties
    owner_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    installer_uri: str
    linux_installer_args: str
    windows_installer_args: str
    aix_installer_args: str
    refresh_error: _error_pb2.ErrorProto
    supported_features: _containers.RepeatedScalarFieldContainer[str]
    config_scribe_key: str
    config_file_timestamp: int
    agent_cert_info: _agent_pb2.AgentCertificateInformation
    solaris_installer_args: str
    hpux_installer_args: str
    agent_port: int
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., properties: _Optional[_Union[Properties, _Mapping]] = ..., owner_entity_id_vec: _Optional[_Iterable[int]] = ..., installer_uri: _Optional[str] = ..., linux_installer_args: _Optional[str] = ..., windows_installer_args: _Optional[str] = ..., aix_installer_args: _Optional[str] = ..., refresh_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., supported_features: _Optional[_Iterable[str]] = ..., config_scribe_key: _Optional[str] = ..., config_file_timestamp: _Optional[int] = ..., agent_cert_info: _Optional[_Union[_agent_pb2.AgentCertificateInformation, _Mapping]] = ..., solaris_installer_args: _Optional[str] = ..., hpux_installer_args: _Optional[str] = ..., agent_port: _Optional[int] = ...) -> None: ...

class HostAgentStatus(_message.Message):
    __slots__ = ("id", "display_name", "properties", "verification_status", "verification_error", "refresh_error", "source_side_dedup_enabled", "oracle_multi_node_multi_channel_supported")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    REFRESH_ERROR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIDE_DEDUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ORACLE_MULTI_NODE_MULTI_CHANNEL_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    id: int
    display_name: str
    properties: Properties
    verification_status: _enums_pb2.VerificationStatus.Type
    verification_error: _error_pb2.ErrorProto
    refresh_error: _error_pb2.ErrorProto
    source_side_dedup_enabled: bool
    oracle_multi_node_multi_channel_supported: bool
    def __init__(self, id: _Optional[int] = ..., display_name: _Optional[str] = ..., properties: _Optional[_Union[Properties, _Mapping]] = ..., verification_status: _Optional[_Union[_enums_pb2.VerificationStatus.Type, str]] = ..., verification_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., refresh_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., source_side_dedup_enabled: bool = ..., oracle_multi_node_multi_channel_supported: bool = ...) -> None: ...
