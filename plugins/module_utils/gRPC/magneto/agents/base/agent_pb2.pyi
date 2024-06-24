from magneto.base import common_pb2 as _common_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.base import enums_pb2 as _enums_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterNetworkingInfo(_message.Message):
    __slots__ = ("resource_vec",)
    class Endpoint(_message.Message):
        __slots__ = ("fqdn", "ipv4addr", "ipv6addr", "subnet_ip4addr", "is_preferred_endpoint", "preferred_address")
        FQDN_FIELD_NUMBER: _ClassVar[int]
        IPV4ADDR_FIELD_NUMBER: _ClassVar[int]
        IPV6ADDR_FIELD_NUMBER: _ClassVar[int]
        SUBNET_IP4ADDR_FIELD_NUMBER: _ClassVar[int]
        IS_PREFERRED_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        PREFERRED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        fqdn: str
        ipv4addr: str
        ipv6addr: str
        subnet_ip4addr: str
        is_preferred_endpoint: bool
        preferred_address: str
        def __init__(self, fqdn: _Optional[str] = ..., ipv4addr: _Optional[str] = ..., ipv6addr: _Optional[str] = ..., subnet_ip4addr: _Optional[str] = ..., is_preferred_endpoint: bool = ..., preferred_address: _Optional[str] = ...) -> None: ...
    class Resource(_message.Message):
        __slots__ = ("type", "endpoint_vec", "is_native", "id", "name", "instance_name")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kServer: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kCluster: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kSQL: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kOracleRAC: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kAD: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kOracleAP: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kExchange: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kSqlAAG: _ClassVar[ClusterNetworkingInfo.Resource.Type]
            kRole: _ClassVar[ClusterNetworkingInfo.Resource.Type]
        kServer: ClusterNetworkingInfo.Resource.Type
        kCluster: ClusterNetworkingInfo.Resource.Type
        kSQL: ClusterNetworkingInfo.Resource.Type
        kOracleRAC: ClusterNetworkingInfo.Resource.Type
        kAD: ClusterNetworkingInfo.Resource.Type
        kOracleAP: ClusterNetworkingInfo.Resource.Type
        kExchange: ClusterNetworkingInfo.Resource.Type
        kSqlAAG: ClusterNetworkingInfo.Resource.Type
        kRole: ClusterNetworkingInfo.Resource.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_NATIVE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
        type: ClusterNetworkingInfo.Resource.Type
        endpoint_vec: _containers.RepeatedCompositeFieldContainer[ClusterNetworkingInfo.Endpoint]
        is_native: bool
        id: str
        name: str
        instance_name: str
        def __init__(self, type: _Optional[_Union[ClusterNetworkingInfo.Resource.Type, str]] = ..., endpoint_vec: _Optional[_Iterable[_Union[ClusterNetworkingInfo.Endpoint, _Mapping]]] = ..., is_native: bool = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., instance_name: _Optional[str] = ...) -> None: ...
    RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    resource_vec: _containers.RepeatedCompositeFieldContainer[ClusterNetworkingInfo.Resource]
    def __init__(self, resource_vec: _Optional[_Iterable[_Union[ClusterNetworkingInfo.Resource, _Mapping]]] = ...) -> None: ...

class CBMRInfo(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class AgentInfoProto(_message.Message):
    __slots__ = ("source_entity_id", "host_type", "agent_id", "api_version", "incarnation_id", "cluster_id", "cluster_incarnation_id", "cluster_name", "dedup_read_supported", "ip_addr_str_vec", "agent_sw_version_str", "os_version", "os_name", "vhdx_supported", "state", "pid", "last_successful_agent_start_method", "agent_uid", "supported_features", "cluster_net_info", "cbmr_info", "linux_agent_pkg_type", "agent_type", "hostname", "registered_cluster_vec", "allow_multiple_cohesity_clusters", "ipaddr_to_subnet_id_vec", "agent_version", "subcomponent_vec", "vcs_version", "machine_identifier", "machine_uuid", "is_persistent_agent", "user_account", "cbmr_version", "temp_folder", "task_id", "host_capability", "agent_cert_info", "solaris_agent_pkg_type", "agent_port")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUninstalled: _ClassVar[AgentInfoProto.State]
        kInstalling: _ClassVar[AgentInfoProto.State]
        kInstalled: _ClassVar[AgentInfoProto.State]
        kHealthy: _ClassVar[AgentInfoProto.State]
        kUnhealthy: _ClassVar[AgentInfoProto.State]
    kUninstalled: AgentInfoProto.State
    kInstalling: AgentInfoProto.State
    kInstalled: AgentInfoProto.State
    kHealthy: AgentInfoProto.State
    kUnhealthy: AgentInfoProto.State
    class AgentStartMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVSphere: _ClassVar[AgentInfoProto.AgentStartMethod]
        kRemoteCommand: _ClassVar[AgentInfoProto.AgentStartMethod]
    kVSphere: AgentInfoProto.AgentStartMethod
    kRemoteCommand: AgentInfoProto.AgentStartMethod
    class LinuxAgentPackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kScript: _ClassVar[AgentInfoProto.LinuxAgentPackageType]
        kRPM: _ClassVar[AgentInfoProto.LinuxAgentPackageType]
        kSuseRPM: _ClassVar[AgentInfoProto.LinuxAgentPackageType]
        kDEB: _ClassVar[AgentInfoProto.LinuxAgentPackageType]
        kPowerPCRPM: _ClassVar[AgentInfoProto.LinuxAgentPackageType]
    kScript: AgentInfoProto.LinuxAgentPackageType
    kRPM: AgentInfoProto.LinuxAgentPackageType
    kSuseRPM: AgentInfoProto.LinuxAgentPackageType
    kDEB: AgentInfoProto.LinuxAgentPackageType
    kPowerPCRPM: AgentInfoProto.LinuxAgentPackageType
    class AgentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCpp: _ClassVar[AgentInfoProto.AgentType]
        kGo: _ClassVar[AgentInfoProto.AgentType]
        kJava: _ClassVar[AgentInfoProto.AgentType]
        kLegacy: _ClassVar[AgentInfoProto.AgentType]
    kCpp: AgentInfoProto.AgentType
    kGo: AgentInfoProto.AgentType
    kJava: AgentInfoProto.AgentType
    kLegacy: AgentInfoProto.AgentType
    class MultipleClusterRegistrationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnset: _ClassVar[AgentInfoProto.MultipleClusterRegistrationPolicy]
        kAllow: _ClassVar[AgentInfoProto.MultipleClusterRegistrationPolicy]
        kDisallow: _ClassVar[AgentInfoProto.MultipleClusterRegistrationPolicy]
    kUnset: AgentInfoProto.MultipleClusterRegistrationPolicy
    kAllow: AgentInfoProto.MultipleClusterRegistrationPolicy
    kDisallow: AgentInfoProto.MultipleClusterRegistrationPolicy
    class SolarisAgentPackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AgentInfoProto.SolarisAgentPackageType]
        kSolaris10x86: _ClassVar[AgentInfoProto.SolarisAgentPackageType]
        kSolaris10Sparc: _ClassVar[AgentInfoProto.SolarisAgentPackageType]
        kSolaris11x86: _ClassVar[AgentInfoProto.SolarisAgentPackageType]
        kSolaris11Sparc: _ClassVar[AgentInfoProto.SolarisAgentPackageType]
    kUnknown: AgentInfoProto.SolarisAgentPackageType
    kSolaris10x86: AgentInfoProto.SolarisAgentPackageType
    kSolaris10Sparc: AgentInfoProto.SolarisAgentPackageType
    kSolaris11x86: AgentInfoProto.SolarisAgentPackageType
    kSolaris11Sparc: AgentInfoProto.SolarisAgentPackageType
    class RegisteredCluster(_message.Message):
        __slots__ = ("cluster_id", "cluster_incarnation_id", "cluster_name")
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        cluster_id: int
        cluster_incarnation_id: int
        cluster_name: str
        def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ...) -> None: ...
    class IPAddrToSubnetId(_message.Message):
        __slots__ = ("ip_addr", "subnet_id")
        IP_ADDR_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        ip_addr: str
        subnet_id: str
        def __init__(self, ip_addr: _Optional[str] = ..., subnet_id: _Optional[str] = ...) -> None: ...
    class InstalledSubcomponent(_message.Message):
        __slots__ = ("subcomponent", "name", "version")
        class InstalledSubcomponentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kWindowsVolumeCBT: _ClassVar[AgentInfoProto.InstalledSubcomponent.InstalledSubcomponentType]
            kWindowsFileCBT: _ClassVar[AgentInfoProto.InstalledSubcomponent.InstalledSubcomponentType]
        kWindowsVolumeCBT: AgentInfoProto.InstalledSubcomponent.InstalledSubcomponentType
        kWindowsFileCBT: AgentInfoProto.InstalledSubcomponent.InstalledSubcomponentType
        class Version(_message.Message):
            __slots__ = ("major_ver", "minor_ver", "revision_num", "build_ver")
            MAJOR_VER_FIELD_NUMBER: _ClassVar[int]
            MINOR_VER_FIELD_NUMBER: _ClassVar[int]
            REVISION_NUM_FIELD_NUMBER: _ClassVar[int]
            BUILD_VER_FIELD_NUMBER: _ClassVar[int]
            major_ver: int
            minor_ver: int
            revision_num: int
            build_ver: int
            def __init__(self, major_ver: _Optional[int] = ..., minor_ver: _Optional[int] = ..., revision_num: _Optional[int] = ..., build_ver: _Optional[int] = ...) -> None: ...
        SUBCOMPONENT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        subcomponent: AgentInfoProto.InstalledSubcomponent.InstalledSubcomponentType
        name: str
        version: AgentInfoProto.InstalledSubcomponent.Version
        def __init__(self, subcomponent: _Optional[_Union[AgentInfoProto.InstalledSubcomponent.InstalledSubcomponentType, str]] = ..., name: _Optional[str] = ..., version: _Optional[_Union[AgentInfoProto.InstalledSubcomponent.Version, _Mapping]] = ...) -> None: ...
    class AgentUser(_message.Message):
        __slots__ = ("account", "sid")
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        SID_FIELD_NUMBER: _ClassVar[int]
        account: str
        sid: str
        def __init__(self, account: _Optional[str] = ..., sid: _Optional[str] = ...) -> None: ...
    SOURCE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEDUP_READ_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_SW_VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_NAME_FIELD_NUMBER: _ClassVar[int]
    VHDX_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_AGENT_START_METHOD_FIELD_NUMBER: _ClassVar[int]
    AGENT_UID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NET_INFO_FIELD_NUMBER: _ClassVar[int]
    CBMR_INFO_FIELD_NUMBER: _ClassVar[int]
    LINUX_AGENT_PKG_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULTIPLE_COHESITY_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    IPADDR_TO_SUBNET_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBCOMPONENT_VEC_FIELD_NUMBER: _ClassVar[int]
    VCS_VERSION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MACHINE_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_PERSISTENT_AGENT_FIELD_NUMBER: _ClassVar[int]
    USER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CBMR_VERSION_FIELD_NUMBER: _ClassVar[int]
    TEMP_FOLDER_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    AGENT_CERT_INFO_FIELD_NUMBER: _ClassVar[int]
    SOLARIS_AGENT_PKG_TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_PORT_FIELD_NUMBER: _ClassVar[int]
    source_entity_id: int
    host_type: _enums_pb2.HostEnv.Type
    agent_id: int
    api_version: int
    incarnation_id: int
    cluster_id: int
    cluster_incarnation_id: int
    cluster_name: str
    dedup_read_supported: bool
    ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    agent_sw_version_str: str
    os_version: str
    os_name: str
    vhdx_supported: bool
    state: AgentInfoProto.State
    pid: int
    last_successful_agent_start_method: AgentInfoProto.AgentStartMethod
    agent_uid: _universal_id_pb2.UniversalIdProto
    supported_features: _containers.RepeatedScalarFieldContainer[str]
    cluster_net_info: ClusterNetworkingInfo
    cbmr_info: CBMRInfo
    linux_agent_pkg_type: AgentInfoProto.LinuxAgentPackageType
    agent_type: AgentInfoProto.AgentType
    hostname: str
    registered_cluster_vec: _containers.RepeatedCompositeFieldContainer[AgentInfoProto.RegisteredCluster]
    allow_multiple_cohesity_clusters: AgentInfoProto.MultipleClusterRegistrationPolicy
    ipaddr_to_subnet_id_vec: _containers.RepeatedCompositeFieldContainer[AgentInfoProto.IPAddrToSubnetId]
    agent_version: int
    subcomponent_vec: _containers.RepeatedCompositeFieldContainer[AgentInfoProto.InstalledSubcomponent]
    vcs_version: str
    machine_identifier: str
    machine_uuid: str
    is_persistent_agent: bool
    user_account: AgentInfoProto.AgentUser
    cbmr_version: str
    temp_folder: str
    task_id: int
    host_capability: int
    agent_cert_info: AgentCertificateInformation
    solaris_agent_pkg_type: AgentInfoProto.SolarisAgentPackageType
    agent_port: int
    def __init__(self, source_entity_id: _Optional[int] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., agent_id: _Optional[int] = ..., api_version: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., dedup_read_supported: bool = ..., ip_addr_str_vec: _Optional[_Iterable[str]] = ..., agent_sw_version_str: _Optional[str] = ..., os_version: _Optional[str] = ..., os_name: _Optional[str] = ..., vhdx_supported: bool = ..., state: _Optional[_Union[AgentInfoProto.State, str]] = ..., pid: _Optional[int] = ..., last_successful_agent_start_method: _Optional[_Union[AgentInfoProto.AgentStartMethod, str]] = ..., agent_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., supported_features: _Optional[_Iterable[str]] = ..., cluster_net_info: _Optional[_Union[ClusterNetworkingInfo, _Mapping]] = ..., cbmr_info: _Optional[_Union[CBMRInfo, _Mapping]] = ..., linux_agent_pkg_type: _Optional[_Union[AgentInfoProto.LinuxAgentPackageType, str]] = ..., agent_type: _Optional[_Union[AgentInfoProto.AgentType, str]] = ..., hostname: _Optional[str] = ..., registered_cluster_vec: _Optional[_Iterable[_Union[AgentInfoProto.RegisteredCluster, _Mapping]]] = ..., allow_multiple_cohesity_clusters: _Optional[_Union[AgentInfoProto.MultipleClusterRegistrationPolicy, str]] = ..., ipaddr_to_subnet_id_vec: _Optional[_Iterable[_Union[AgentInfoProto.IPAddrToSubnetId, _Mapping]]] = ..., agent_version: _Optional[int] = ..., subcomponent_vec: _Optional[_Iterable[_Union[AgentInfoProto.InstalledSubcomponent, _Mapping]]] = ..., vcs_version: _Optional[str] = ..., machine_identifier: _Optional[str] = ..., machine_uuid: _Optional[str] = ..., is_persistent_agent: bool = ..., user_account: _Optional[_Union[AgentInfoProto.AgentUser, _Mapping]] = ..., cbmr_version: _Optional[str] = ..., temp_folder: _Optional[str] = ..., task_id: _Optional[int] = ..., host_capability: _Optional[int] = ..., agent_cert_info: _Optional[_Union[AgentCertificateInformation, _Mapping]] = ..., solaris_agent_pkg_type: _Optional[_Union[AgentInfoProto.SolarisAgentPackageType, str]] = ..., agent_port: _Optional[int] = ...) -> None: ...

class AgentCertificateInformation(_message.Message):
    __slots__ = ("expiry_time_epoch", "cert_type", "cipher_type", "cipher_str")
    class CertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AgentCertificateInformation.CertType]
        kNoCert: _ClassVar[AgentCertificateInformation.CertType]
        kEmbedded: _ClassVar[AgentCertificateInformation.CertType]
        kCohesityCert: _ClassVar[AgentCertificateInformation.CertType]
        kThirdPartyCert: _ClassVar[AgentCertificateInformation.CertType]
    kUnknown: AgentCertificateInformation.CertType
    kNoCert: AgentCertificateInformation.CertType
    kEmbedded: AgentCertificateInformation.CertType
    kCohesityCert: AgentCertificateInformation.CertType
    kThirdPartyCert: AgentCertificateInformation.CertType
    class CipherTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CIPHER: _ClassVar[AgentCertificateInformation.CipherTypeEnum]
        ECDHE_ECDSA_AES128_GCM_SHA256: _ClassVar[AgentCertificateInformation.CipherTypeEnum]
        ECDHE_ECDSA_AES256_GCM_SHA384: _ClassVar[AgentCertificateInformation.CipherTypeEnum]
        ECDHE_RSA_AES128_GCM_SHA256: _ClassVar[AgentCertificateInformation.CipherTypeEnum]
        ECDHE_RSA_AES256_GCM_SHA384: _ClassVar[AgentCertificateInformation.CipherTypeEnum]
    UNKNOWN_CIPHER: AgentCertificateInformation.CipherTypeEnum
    ECDHE_ECDSA_AES128_GCM_SHA256: AgentCertificateInformation.CipherTypeEnum
    ECDHE_ECDSA_AES256_GCM_SHA384: AgentCertificateInformation.CipherTypeEnum
    ECDHE_RSA_AES128_GCM_SHA256: AgentCertificateInformation.CipherTypeEnum
    ECDHE_RSA_AES256_GCM_SHA384: AgentCertificateInformation.CipherTypeEnum
    EXPIRY_TIME_EPOCH_FIELD_NUMBER: _ClassVar[int]
    CERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CIPHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CIPHER_STR_FIELD_NUMBER: _ClassVar[int]
    expiry_time_epoch: int
    cert_type: AgentCertificateInformation.CertType
    cipher_type: AgentCertificateInformation.CipherTypeEnum
    cipher_str: str
    def __init__(self, expiry_time_epoch: _Optional[int] = ..., cert_type: _Optional[_Union[AgentCertificateInformation.CertType, str]] = ..., cipher_type: _Optional[_Union[AgentCertificateInformation.CipherTypeEnum, str]] = ..., cipher_str: _Optional[str] = ...) -> None: ...

class VolumeInfoProto(_message.Message):
    __slots__ = ("path", "volume_guid", "volume_label", "serial_number", "device_number", "partition_number", "target_id", "logical_unit_number", "controller_number", "logical_size_bytes", "used_size_bytes", "logical_sector_size_bytes", "mount_point_vec", "file_backup_supported", "extended_attributes_supported", "mount_type", "is_boot_volume", "is_shared_volume", "is_smb_volume", "is_read_only", "is_cohesity_mount_volume", "volume_count", "is_refs_volume")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LABEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_BACKUP_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    MOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_BOOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    IS_SHARED_VOLUME_FIELD_NUMBER: _ClassVar[int]
    IS_SMB_VOLUME_FIELD_NUMBER: _ClassVar[int]
    IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    IS_COHESITY_MOUNT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_REFS_VOLUME_FIELD_NUMBER: _ClassVar[int]
    path: str
    volume_guid: bytes
    volume_label: str
    serial_number: str
    device_number: int
    partition_number: int
    target_id: int
    logical_unit_number: int
    controller_number: int
    logical_size_bytes: int
    used_size_bytes: int
    logical_sector_size_bytes: int
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    file_backup_supported: bool
    extended_attributes_supported: bool
    mount_type: str
    is_boot_volume: bool
    is_shared_volume: bool
    is_smb_volume: bool
    is_read_only: bool
    is_cohesity_mount_volume: bool
    volume_count: int
    is_refs_volume: bool
    def __init__(self, path: _Optional[str] = ..., volume_guid: _Optional[bytes] = ..., volume_label: _Optional[str] = ..., serial_number: _Optional[str] = ..., device_number: _Optional[int] = ..., partition_number: _Optional[int] = ..., target_id: _Optional[int] = ..., logical_unit_number: _Optional[int] = ..., controller_number: _Optional[int] = ..., logical_size_bytes: _Optional[int] = ..., used_size_bytes: _Optional[int] = ..., logical_sector_size_bytes: _Optional[int] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., file_backup_supported: bool = ..., extended_attributes_supported: bool = ..., mount_type: _Optional[str] = ..., is_boot_volume: bool = ..., is_shared_volume: bool = ..., is_smb_volume: bool = ..., is_read_only: bool = ..., is_cohesity_mount_volume: bool = ..., volume_count: _Optional[int] = ..., is_refs_volume: bool = ...) -> None: ...

class VolumeInfoSummaryProto(_message.Message):
    __slots__ = ("volume_guid", "mount_point_vec", "logical_size_bytes", "used_size_bytes")
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    volume_guid: bytes
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    logical_size_bytes: int
    used_size_bytes: int
    def __init__(self, volume_guid: _Optional[bytes] = ..., mount_point_vec: _Optional[_Iterable[str]] = ..., logical_size_bytes: _Optional[int] = ..., used_size_bytes: _Optional[int] = ...) -> None: ...

class VolumeSnapshotInfoProto(_message.Message):
    __slots__ = ("volume_guid", "volume_label", "serial_number", "device_number", "partition_number", "snapshot_set_id", "snapshot_id", "snapshot_device_path", "logical_size_bytes", "logical_sector_size_bytes", "used_size_bytes", "snapshot_time_micro_seconds", "delta_type", "delta_info", "full_backup_reason", "cbt_error", "mount_point_vec")
    Extensions: _python_message._ExtensionDict
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LABEL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_MICRO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_REASON_FIELD_NUMBER: _ClassVar[int]
    CBT_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_guid: bytes
    volume_label: str
    serial_number: str
    device_number: int
    partition_number: int
    snapshot_set_id: bytes
    snapshot_id: bytes
    snapshot_device_path: str
    logical_size_bytes: int
    logical_sector_size_bytes: int
    used_size_bytes: int
    snapshot_time_micro_seconds: int
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    full_backup_reason: str
    cbt_error: _error_pb2.ErrorProto
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, volume_guid: _Optional[bytes] = ..., volume_label: _Optional[str] = ..., serial_number: _Optional[str] = ..., device_number: _Optional[int] = ..., partition_number: _Optional[int] = ..., snapshot_set_id: _Optional[bytes] = ..., snapshot_id: _Optional[bytes] = ..., snapshot_device_path: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., logical_sector_size_bytes: _Optional[int] = ..., used_size_bytes: _Optional[int] = ..., snapshot_time_micro_seconds: _Optional[int] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., full_backup_reason: _Optional[str] = ..., cbt_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mount_point_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class AppFileInfo(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class ServerSnapshotInfo(_message.Message):
    __slots__ = ("snapshot_set_id", "snapshot_info_vec", "app_file_info")
    Extensions: _python_message._ExtensionDict
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_set_id: bytes
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[VolumeSnapshotInfoProto]
    app_file_info: AppFileInfo
    def __init__(self, snapshot_set_id: _Optional[bytes] = ..., snapshot_info_vec: _Optional[_Iterable[_Union[VolumeSnapshotInfoProto, _Mapping]]] = ..., app_file_info: _Optional[_Union[AppFileInfo, _Mapping]] = ...) -> None: ...

class MountVolumeInfo(_message.Message):
    __slots__ = ("volume_guid", "virtual_disk_mount_point", "virtual_disk_path")
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    volume_guid: str
    virtual_disk_mount_point: str
    virtual_disk_path: str
    def __init__(self, volume_guid: _Optional[str] = ..., virtual_disk_mount_point: _Optional[str] = ..., virtual_disk_path: _Optional[str] = ...) -> None: ...

class GFlagSetting(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ServiceState(_message.Message):
    __slots__ = ("name", "display_name", "state", "start", "logon_user")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRunning: _ClassVar[ServiceState.State]
        kStopped: _ClassVar[ServiceState.State]
        kPaused: _ClassVar[ServiceState.State]
        kUnknown: _ClassVar[ServiceState.State]
    kRunning: ServiceState.State
    kStopped: ServiceState.State
    kPaused: ServiceState.State
    kUnknown: ServiceState.State
    class StartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAuto: _ClassVar[ServiceState.StartType]
        kBoot: _ClassVar[ServiceState.StartType]
        kDemand: _ClassVar[ServiceState.StartType]
        kDisabled: _ClassVar[ServiceState.StartType]
        kSystem: _ClassVar[ServiceState.StartType]
        kUnrecognized: _ClassVar[ServiceState.StartType]
    kAuto: ServiceState.StartType
    kBoot: ServiceState.StartType
    kDemand: ServiceState.StartType
    kDisabled: ServiceState.StartType
    kSystem: ServiceState.StartType
    kUnrecognized: ServiceState.StartType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    LOGON_USER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: ServiceState.State
    start: ServiceState.StartType
    logon_user: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., state: _Optional[_Union[ServiceState.State, str]] = ..., start: _Optional[_Union[ServiceState.StartType, str]] = ..., logon_user: _Optional[str] = ...) -> None: ...

class HostInfo(_message.Message):
    __slots__ = ("volume_info_vec", "server_snapshot_info_vec", "service_state_vec", "process_memory_usage_mb", "process_memory_usage_hwm_mb", "system_resource_info")
    Extensions: _python_message._ExtensionDict
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    PROCESS_MEMORY_USAGE_MB_FIELD_NUMBER: _ClassVar[int]
    PROCESS_MEMORY_USAGE_HWM_MB_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfoProto]
    server_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[ServerSnapshotInfo]
    service_state_vec: _containers.RepeatedCompositeFieldContainer[ServiceState]
    process_memory_usage_mb: int
    process_memory_usage_hwm_mb: int
    system_resource_info: _common_pb2.SystemResourceInfo
    def __init__(self, volume_info_vec: _Optional[_Iterable[_Union[VolumeInfoProto, _Mapping]]] = ..., server_snapshot_info_vec: _Optional[_Iterable[_Union[ServerSnapshotInfo, _Mapping]]] = ..., service_state_vec: _Optional[_Iterable[_Union[ServiceState, _Mapping]]] = ..., process_memory_usage_mb: _Optional[int] = ..., process_memory_usage_hwm_mb: _Optional[int] = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ...) -> None: ...

class HostInfoSummary(_message.Message):
    __slots__ = ("volume_info_summary_vec", "num_snapshots")
    Extensions: _python_message._ExtensionDict
    VOLUME_INFO_SUMMARY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    volume_info_summary_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfoSummaryProto]
    num_snapshots: int
    def __init__(self, volume_info_summary_vec: _Optional[_Iterable[_Union[VolumeInfoSummaryProto, _Mapping]]] = ..., num_snapshots: _Optional[int] = ...) -> None: ...

class SnapshotHostInfoSummary(_message.Message):
    __slots__ = ("summary_before_snapshot_is_taken", "summary_before_snapshot_is_deleted", "summary_after_snapshot_is_deleted")
    SUMMARY_BEFORE_SNAPSHOT_IS_TAKEN_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_BEFORE_SNAPSHOT_IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_AFTER_SNAPSHOT_IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    summary_before_snapshot_is_taken: HostInfoSummary
    summary_before_snapshot_is_deleted: HostInfoSummary
    summary_after_snapshot_is_deleted: HostInfoSummary
    def __init__(self, summary_before_snapshot_is_taken: _Optional[_Union[HostInfoSummary, _Mapping]] = ..., summary_before_snapshot_is_deleted: _Optional[_Union[HostInfoSummary, _Mapping]] = ..., summary_after_snapshot_is_deleted: _Optional[_Union[HostInfoSummary, _Mapping]] = ...) -> None: ...

class ServerSnapshotSerializedFetchInfo(_message.Message):
    __slots__ = ("server_snapshot_info_size", "server_snapshot_info_is_compressed", "server_snapshot_info_saved_successfully")
    SERVER_SNAPSHOT_INFO_SIZE_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_SAVED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    server_snapshot_info_size: int
    server_snapshot_info_is_compressed: bool
    server_snapshot_info_saved_successfully: bool
    def __init__(self, server_snapshot_info_size: _Optional[int] = ..., server_snapshot_info_is_compressed: bool = ..., server_snapshot_info_saved_successfully: bool = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ("start_offset", "size")
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    start_offset: int
    size: int
    def __init__(self, start_offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ApplyChangedAreasBatch(_message.Message):
    __slots__ = ("file_range", "changed_area_vec", "mounted_source_snapshot_file_full_path", "target_local_file_full_path", "error")
    class ChangedArea(_message.Message):
        __slots__ = ("range", "state", "error")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNotStarted: _ClassVar[ApplyChangedAreasBatch.ChangedArea.State]
            kPending: _ClassVar[ApplyChangedAreasBatch.ChangedArea.State]
            kDone: _ClassVar[ApplyChangedAreasBatch.ChangedArea.State]
        kNotStarted: ApplyChangedAreasBatch.ChangedArea.State
        kPending: ApplyChangedAreasBatch.ChangedArea.State
        kDone: ApplyChangedAreasBatch.ChangedArea.State
        RANGE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        range: Range
        state: ApplyChangedAreasBatch.ChangedArea.State
        error: _error_pb2.ErrorProto
        def __init__(self, range: _Optional[_Union[Range, _Mapping]] = ..., state: _Optional[_Union[ApplyChangedAreasBatch.ChangedArea.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    FILE_RANGE_FIELD_NUMBER: _ClassVar[int]
    CHANGED_AREA_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_SOURCE_SNAPSHOT_FILE_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_LOCAL_FILE_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    file_range: Range
    changed_area_vec: _containers.RepeatedCompositeFieldContainer[ApplyChangedAreasBatch.ChangedArea]
    mounted_source_snapshot_file_full_path: str
    target_local_file_full_path: str
    error: _error_pb2.ErrorProto
    def __init__(self, file_range: _Optional[_Union[Range, _Mapping]] = ..., changed_area_vec: _Optional[_Iterable[_Union[ApplyChangedAreasBatch.ChangedArea, _Mapping]]] = ..., mounted_source_snapshot_file_full_path: _Optional[str] = ..., target_local_file_full_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class HostSettingsCheck(_message.Message):
    __slots__ = ("check_type", "params")
    class CheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIsAgentPortAccessible: _ClassVar[HostSettingsCheck.CheckType]
        kIsAgentRunning: _ClassVar[HostSettingsCheck.CheckType]
        kIsSQLWriterRunning: _ClassVar[HostSettingsCheck.CheckType]
        kAreSQLInstancesRunning: _ClassVar[HostSettingsCheck.CheckType]
        kCheckServiceLoginsConfig: _ClassVar[HostSettingsCheck.CheckType]
        kCheckSQLFCIVIP: _ClassVar[HostSettingsCheck.CheckType]
        kCheckSQLDiskSpace: _ClassVar[HostSettingsCheck.CheckType]
    kIsAgentPortAccessible: HostSettingsCheck.CheckType
    kIsAgentRunning: HostSettingsCheck.CheckType
    kIsSQLWriterRunning: HostSettingsCheck.CheckType
    kAreSQLInstancesRunning: HostSettingsCheck.CheckType
    kCheckServiceLoginsConfig: HostSettingsCheck.CheckType
    kCheckSQLFCIVIP: HostSettingsCheck.CheckType
    kCheckSQLDiskSpace: HostSettingsCheck.CheckType
    CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    check_type: HostSettingsCheck.CheckType
    params: HostSettingsCheckParams
    def __init__(self, check_type: _Optional[_Union[HostSettingsCheck.CheckType, str]] = ..., params: _Optional[_Union[HostSettingsCheckParams, _Mapping]] = ...) -> None: ...

class HostSettingsCheckParams(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class IsAgentPortAccessibleParams(_message.Message):
    __slots__ = ("agent_port",)
    IS_AGENT_PORT_ACCESSIBLE_PARAM_FIELD_NUMBER: _ClassVar[int]
    is_agent_port_accessible_param: _descriptor.FieldDescriptor
    AGENT_PORT_FIELD_NUMBER: _ClassVar[int]
    agent_port: int
    def __init__(self, agent_port: _Optional[int] = ...) -> None: ...

class CheckServiceLoginsConfigParams(_message.Message):
    __slots__ = ("included_sql_instances_vec",)
    CHECK_SERVICE_LOGINS_CONFIG_PARAMS_FIELD_NUMBER: _ClassVar[int]
    check_service_logins_config_params: _descriptor.FieldDescriptor
    INCLUDED_SQL_INSTANCES_VEC_FIELD_NUMBER: _ClassVar[int]
    included_sql_instances_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, included_sql_instances_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckSQLFCIVIPParams(_message.Message):
    __slots__ = ("registered_sql_fci_vip",)
    CHECK_SQL_FCI_VIP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    check_sql_fci_vip_params: _descriptor.FieldDescriptor
    REGISTERED_SQL_FCI_VIP_FIELD_NUMBER: _ClassVar[int]
    registered_sql_fci_vip: str
    def __init__(self, registered_sql_fci_vip: _Optional[str] = ...) -> None: ...

class HostSettingsCheckResult(_message.Message):
    __slots__ = ("host_settings_check", "result_type", "user_message", "env_type", "info_messages_vec")
    Extensions: _python_message._ExtensionDict
    class CheckResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPass: _ClassVar[HostSettingsCheckResult.CheckResultType]
        kFail: _ClassVar[HostSettingsCheckResult.CheckResultType]
        kWarning: _ClassVar[HostSettingsCheckResult.CheckResultType]
    kPass: HostSettingsCheckResult.CheckResultType
    kFail: HostSettingsCheckResult.CheckResultType
    kWarning: HostSettingsCheckResult.CheckResultType
    HOST_SETTINGS_CHECK_FIELD_NUMBER: _ClassVar[int]
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
    INFO_MESSAGES_VEC_FIELD_NUMBER: _ClassVar[int]
    host_settings_check: HostSettingsCheck
    result_type: HostSettingsCheckResult.CheckResultType
    user_message: str
    env_type: _enums_pb2.Environment.Type
    info_messages_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, host_settings_check: _Optional[_Union[HostSettingsCheck, _Mapping]] = ..., result_type: _Optional[_Union[HostSettingsCheckResult.CheckResultType, str]] = ..., user_message: _Optional[str] = ..., env_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., info_messages_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CheckServiceLoginsConfigResultData(_message.Message):
    __slots__ = ("service_logons_map", "sql_instance_sysadmins_map")
    class ServiceLogonsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SysadminList(_message.Message):
        __slots__ = ("sysadmins_vec",)
        SYSADMINS_VEC_FIELD_NUMBER: _ClassVar[int]
        sysadmins_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, sysadmins_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class SqlInstanceSysadminsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CheckServiceLoginsConfigResultData.SysadminList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CheckServiceLoginsConfigResultData.SysadminList, _Mapping]] = ...) -> None: ...
    CHECK_SERVICE_LOGINS_CONFIG_RESULT_DATA_FIELD_NUMBER: _ClassVar[int]
    check_service_logins_config_result_data: _descriptor.FieldDescriptor
    SERVICE_LOGONS_MAP_FIELD_NUMBER: _ClassVar[int]
    SQL_INSTANCE_SYSADMINS_MAP_FIELD_NUMBER: _ClassVar[int]
    service_logons_map: _containers.ScalarMap[str, str]
    sql_instance_sysadmins_map: _containers.MessageMap[str, CheckServiceLoginsConfigResultData.SysadminList]
    def __init__(self, service_logons_map: _Optional[_Mapping[str, str]] = ..., sql_instance_sysadmins_map: _Optional[_Mapping[str, CheckServiceLoginsConfigResultData.SysadminList]] = ...) -> None: ...

class CbtInfo(_message.Message):
    __slots__ = ("is_installed", "service_state", "file_version", "reboot_status")
    class RebootStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRebooted: _ClassVar[CbtInfo.RebootStatus]
        kNeedsReboot: _ClassVar[CbtInfo.RebootStatus]
        kInternalError: _ClassVar[CbtInfo.RebootStatus]
    kRebooted: CbtInfo.RebootStatus
    kNeedsReboot: CbtInfo.RebootStatus
    kInternalError: CbtInfo.RebootStatus
    IS_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
    REBOOT_STATUS_FIELD_NUMBER: _ClassVar[int]
    is_installed: bool
    service_state: ServiceState
    file_version: AgentInfoProto.InstalledSubcomponent.Version
    reboot_status: CbtInfo.RebootStatus
    def __init__(self, is_installed: bool = ..., service_state: _Optional[_Union[ServiceState, _Mapping]] = ..., file_version: _Optional[_Union[AgentInfoProto.InstalledSubcomponent.Version, _Mapping]] = ..., reboot_status: _Optional[_Union[CbtInfo.RebootStatus, str]] = ...) -> None: ...

class RpcStats(_message.Message):
    __slots__ = ("cluster_start_time_usecs", "cluster_end_time_usecs", "agent_start_time_usecs", "agent_end_time_usecs")
    CLUSTER_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    AGENT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    AGENT_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    cluster_start_time_usecs: int
    cluster_end_time_usecs: int
    agent_start_time_usecs: int
    agent_end_time_usecs: int
    def __init__(self, cluster_start_time_usecs: _Optional[int] = ..., cluster_end_time_usecs: _Optional[int] = ..., agent_start_time_usecs: _Optional[int] = ..., agent_end_time_usecs: _Optional[int] = ...) -> None: ...
