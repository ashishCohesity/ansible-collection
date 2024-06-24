from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Identifier(_message.Message):
    __slots__ = ("id", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class SnapshotSelector(_message.Message):
    __slots__ = ("pick_method", "snapshot_age_secs", "entity_snapshot_time_msecs_map")
    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LATEST: _ClassVar[SnapshotSelector.Method]
    LATEST: SnapshotSelector.Method
    class EntitySnapshotTimeMsecsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    PICK_METHOD_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_AGE_SECS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SNAPSHOT_TIME_MSECS_MAP_FIELD_NUMBER: _ClassVar[int]
    pick_method: SnapshotSelector.Method
    snapshot_age_secs: int
    entity_snapshot_time_msecs_map: _containers.ScalarMap[str, int]
    def __init__(self, pick_method: _Optional[_Union[SnapshotSelector.Method, str]] = ..., snapshot_age_secs: _Optional[int] = ..., entity_snapshot_time_msecs_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ("identifier", "type", "user", "password", "port", "timeout_secs", "host", "private_key")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSsh: _ClassVar[Connection.Type]
        kWinRm: _ClassVar[Connection.Type]
    kSsh: Connection.Type
    kWinRm: Connection.Type
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    type: Connection.Type
    user: str
    password: str
    port: int
    timeout_secs: int
    host: str
    private_key: bytes
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., type: _Optional[_Union[Connection.Type, str]] = ..., user: _Optional[str] = ..., password: _Optional[str] = ..., port: _Optional[int] = ..., timeout_secs: _Optional[int] = ..., host: _Optional[str] = ..., private_key: _Optional[bytes] = ...) -> None: ...

class VmConfig(_message.Message):
    __slots__ = ("identifier", "script_path")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    script_path: str
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., script_path: _Optional[str] = ...) -> None: ...

class AWSCredentials(_message.Message):
    __slots__ = ("access_key_id", "secret_access_key")
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    access_key_id: str
    secret_access_key: str
    def __init__(self, access_key_id: _Optional[str] = ..., secret_access_key: _Optional[str] = ...) -> None: ...

class AzureCredentials(_message.Message):
    __slots__ = ("subscription_id", "application_id", "application_key", "tenant_id")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    application_id: str
    application_key: str
    tenant_id: str
    def __init__(self, subscription_id: _Optional[str] = ..., application_id: _Optional[str] = ..., application_key: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class VmwareCredentials(_message.Message):
    __slots__ = ("endpoint", "user", "password", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVCenter: _ClassVar[VmwareCredentials.Type]
        kVCloudDirector: _ClassVar[VmwareCredentials.Type]
    kVCenter: VmwareCredentials.Type
    kVCloudDirector: VmwareCredentials.Type
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    user: str
    password: str
    type: VmwareCredentials.Type
    def __init__(self, endpoint: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ..., type: _Optional[_Union[VmwareCredentials.Type, str]] = ...) -> None: ...

class CohesityCredentials(_message.Message):
    __slots__ = ("endpoint", "user", "password", "domain")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    user: str
    password: str
    domain: str
    def __init__(self, endpoint: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class Target(_message.Message):
    __slots__ = ("identifier", "type", "aws_credentials", "azure_credentials", "cohesity_credentials", "vmware_credentials")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAWS: _ClassVar[Target.Type]
        kAzure: _ClassVar[Target.Type]
        kCohesity: _ClassVar[Target.Type]
        kVMware: _ClassVar[Target.Type]
        kView: _ClassVar[Target.Type]
    kAWS: Target.Type
    kAzure: Target.Type
    kCohesity: Target.Type
    kVMware: Target.Type
    kView: Target.Type
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AWS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    COHESITY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    type: Target.Type
    aws_credentials: AWSCredentials
    azure_credentials: AzureCredentials
    cohesity_credentials: CohesityCredentials
    vmware_credentials: VmwareCredentials
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., type: _Optional[_Union[Target.Type, str]] = ..., aws_credentials: _Optional[_Union[AWSCredentials, _Mapping]] = ..., azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]] = ..., cohesity_credentials: _Optional[_Union[CohesityCredentials, _Mapping]] = ..., vmware_credentials: _Optional[_Union[VmwareCredentials, _Mapping]] = ...) -> None: ...

class RemoteCluster(_message.Message):
    __slots__ = ("identifier",)
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    identifier: ClusterIdentifier
    def __init__(self, identifier: _Optional[_Union[ClusterIdentifier, _Mapping]] = ...) -> None: ...

class ClusterIdentifier(_message.Message):
    __slots__ = ("cluster_id", "cluster_incarnation_id", "name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_incarnation_id: int
    name: str
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class AWSProfile(_message.Message):
    __slots__ = ("region", "instance_type", "storage_type", "vpc", "subnet", "security_group")
    REGION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    region: Identifier
    instance_type: Identifier
    storage_type: Identifier
    vpc: Identifier
    subnet: Identifier
    security_group: Identifier
    def __init__(self, region: _Optional[_Union[Identifier, _Mapping]] = ..., instance_type: _Optional[_Union[Identifier, _Mapping]] = ..., storage_type: _Optional[_Union[Identifier, _Mapping]] = ..., vpc: _Optional[_Union[Identifier, _Mapping]] = ..., subnet: _Optional[_Union[Identifier, _Mapping]] = ..., security_group: _Optional[_Union[Identifier, _Mapping]] = ...) -> None: ...

class AzureProfile(_message.Message):
    __slots__ = ("resource_group", "storage_account", "instance_type", "disk_type", "virtual_network", "subnet", "network_security_group")
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    resource_group: Identifier
    storage_account: Identifier
    instance_type: Identifier
    disk_type: Identifier
    virtual_network: Identifier
    subnet: Identifier
    network_security_group: Identifier
    def __init__(self, resource_group: _Optional[_Union[Identifier, _Mapping]] = ..., storage_account: _Optional[_Union[Identifier, _Mapping]] = ..., instance_type: _Optional[_Union[Identifier, _Mapping]] = ..., disk_type: _Optional[_Union[Identifier, _Mapping]] = ..., virtual_network: _Optional[_Union[Identifier, _Mapping]] = ..., subnet: _Optional[_Union[Identifier, _Mapping]] = ..., network_security_group: _Optional[_Union[Identifier, _Mapping]] = ...) -> None: ...

class VmwareProfile(_message.Message):
    __slots__ = ("num_cpus", "memory_bytes", "resource_pool", "vm_folder", "datastore", "network_port_group", "interface_group", "datacenter", "cluster", "datastore_cluster", "vcenter_profile", "vcd_profile")
    NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PORT_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VCENTER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    VCD_PROFILE_FIELD_NUMBER: _ClassVar[int]
    num_cpus: int
    memory_bytes: int
    resource_pool: Identifier
    vm_folder: Identifier
    datastore: Identifier
    network_port_group: Identifier
    interface_group: Identifier
    datacenter: Identifier
    cluster: Identifier
    datastore_cluster: Identifier
    vcenter_profile: VcenterProfile
    vcd_profile: VcloudDirectorProfile
    def __init__(self, num_cpus: _Optional[int] = ..., memory_bytes: _Optional[int] = ..., resource_pool: _Optional[_Union[Identifier, _Mapping]] = ..., vm_folder: _Optional[_Union[Identifier, _Mapping]] = ..., datastore: _Optional[_Union[Identifier, _Mapping]] = ..., network_port_group: _Optional[_Union[Identifier, _Mapping]] = ..., interface_group: _Optional[_Union[Identifier, _Mapping]] = ..., datacenter: _Optional[_Union[Identifier, _Mapping]] = ..., cluster: _Optional[_Union[Identifier, _Mapping]] = ..., datastore_cluster: _Optional[_Union[Identifier, _Mapping]] = ..., vcenter_profile: _Optional[_Union[VcenterProfile, _Mapping]] = ..., vcd_profile: _Optional[_Union[VcloudDirectorProfile, _Mapping]] = ...) -> None: ...

class VcenterProfile(_message.Message):
    __slots__ = ("datacenter", "cluster", "resource_pool", "datastore", "datastore_cluster", "network_port_group")
    DATACENTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PORT_GROUP_FIELD_NUMBER: _ClassVar[int]
    datacenter: Identifier
    cluster: Identifier
    resource_pool: Identifier
    datastore: Identifier
    datastore_cluster: Identifier
    network_port_group: Identifier
    def __init__(self, datacenter: _Optional[_Union[Identifier, _Mapping]] = ..., cluster: _Optional[_Union[Identifier, _Mapping]] = ..., resource_pool: _Optional[_Union[Identifier, _Mapping]] = ..., datastore: _Optional[_Union[Identifier, _Mapping]] = ..., datastore_cluster: _Optional[_Union[Identifier, _Mapping]] = ..., network_port_group: _Optional[_Union[Identifier, _Mapping]] = ...) -> None: ...

class VcloudDirectorProfile(_message.Message):
    __slots__ = ("org", "virtual_datacenter", "storage_profile", "org_network")
    ORG_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DATACENTER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ORG_NETWORK_FIELD_NUMBER: _ClassVar[int]
    org: Identifier
    virtual_datacenter: Identifier
    storage_profile: Identifier
    org_network: Identifier
    def __init__(self, org: _Optional[_Union[Identifier, _Mapping]] = ..., virtual_datacenter: _Optional[_Union[Identifier, _Mapping]] = ..., storage_profile: _Optional[_Union[Identifier, _Mapping]] = ..., org_network: _Optional[_Union[Identifier, _Mapping]] = ...) -> None: ...

class VMsToNICMap(_message.Message):
    __slots__ = ("vm", "nic_vec")
    VM_FIELD_NUMBER: _ClassVar[int]
    NIC_VEC_FIELD_NUMBER: _ClassVar[int]
    vm: Identifier
    nic_vec: _containers.RepeatedCompositeFieldContainer[NICSetting]
    def __init__(self, vm: _Optional[_Union[Identifier, _Mapping]] = ..., nic_vec: _Optional[_Iterable[_Union[NICSetting, _Mapping]]] = ...) -> None: ...

class NICSetting(_message.Message):
    __slots__ = ("ipv4", "gateway", "subnet")
    IPV4_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    ipv4: str
    gateway: str
    subnet: str
    def __init__(self, ipv4: _Optional[str] = ..., gateway: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...

class NetworkMapping(_message.Message):
    __slots__ = ("source_network", "target_network", "gateway", "dns_server_vec", "dns_suffix_vec")
    SOURCE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    TARGET_NETWORK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SUFFIX_VEC_FIELD_NUMBER: _ClassVar[int]
    source_network: str
    target_network: str
    gateway: str
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_suffix_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, source_network: _Optional[str] = ..., target_network: _Optional[str] = ..., gateway: _Optional[str] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., dns_suffix_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CohesityProfile(_message.Message):
    __slots__ = ("num_cpus", "memory_bytes")
    NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    num_cpus: int
    memory_bytes: int
    def __init__(self, num_cpus: _Optional[int] = ..., memory_bytes: _Optional[int] = ...) -> None: ...

class TargetResourceSet(_message.Message):
    __slots__ = ("identifier", "aws_profile", "azure_profile", "cohesity_profile", "vmware_profile", "connection_identifier", "vm_config_identifier", "network_profile_type", "dns_server_vec", "dns_suffix_vec", "vms_nic_map", "network_mapping")
    class NetworkProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDhcp: _ClassVar[TargetResourceSet.NetworkProfileType]
        kPreserveOriginal: _ClassVar[TargetResourceSet.NetworkProfileType]
        kNetworkMapping: _ClassVar[TargetResourceSet.NetworkProfileType]
        kPerVmIps: _ClassVar[TargetResourceSet.NetworkProfileType]
    kDhcp: TargetResourceSet.NetworkProfileType
    kPreserveOriginal: TargetResourceSet.NetworkProfileType
    kNetworkMapping: TargetResourceSet.NetworkProfileType
    kPerVmIps: TargetResourceSet.NetworkProfileType
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    AWS_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AZURE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    COHESITY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PROFILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SUFFIX_VEC_FIELD_NUMBER: _ClassVar[int]
    VMS_NIC_MAP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    aws_profile: AWSProfile
    azure_profile: AzureProfile
    cohesity_profile: CohesityProfile
    vmware_profile: VmwareProfile
    connection_identifier: Identifier
    vm_config_identifier: Identifier
    network_profile_type: TargetResourceSet.NetworkProfileType
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_suffix_vec: _containers.RepeatedScalarFieldContainer[str]
    vms_nic_map: _containers.RepeatedCompositeFieldContainer[VMsToNICMap]
    network_mapping: _containers.RepeatedCompositeFieldContainer[NetworkMapping]
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., aws_profile: _Optional[_Union[AWSProfile, _Mapping]] = ..., azure_profile: _Optional[_Union[AzureProfile, _Mapping]] = ..., cohesity_profile: _Optional[_Union[CohesityProfile, _Mapping]] = ..., vmware_profile: _Optional[_Union[VmwareProfile, _Mapping]] = ..., connection_identifier: _Optional[_Union[Identifier, _Mapping]] = ..., vm_config_identifier: _Optional[_Union[Identifier, _Mapping]] = ..., network_profile_type: _Optional[_Union[TargetResourceSet.NetworkProfileType, str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., dns_suffix_vec: _Optional[_Iterable[str]] = ..., vms_nic_map: _Optional[_Iterable[_Union[VMsToNICMap, _Mapping]]] = ..., network_mapping: _Optional[_Iterable[_Union[NetworkMapping, _Mapping]]] = ...) -> None: ...

class TargetProfile(_message.Message):
    __slots__ = ("identifier", "target_id", "default_target_resource_set", "custom_target_resource_set_vec")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TARGET_RESOURCE_SET_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_RESOURCE_SET_VEC_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    target_id: str
    default_target_resource_set: TargetResourceSet
    custom_target_resource_set_vec: _containers.RepeatedCompositeFieldContainer[TargetResourceSet]
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., target_id: _Optional[str] = ..., default_target_resource_set: _Optional[_Union[TargetResourceSet, _Mapping]] = ..., custom_target_resource_set_vec: _Optional[_Iterable[_Union[TargetResourceSet, _Mapping]]] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("device_name", "type", "size_bytes")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCSI: _ClassVar[Volume.Type]
    SCSI: Volume.Type
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    device_name: str
    type: Volume.Type
    size_bytes: int
    def __init__(self, device_name: _Optional[str] = ..., type: _Optional[_Union[Volume.Type, str]] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class VMProperties(_message.Message):
    __slots__ = ("volume_vec",)
    VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_vec: _containers.RepeatedCompositeFieldContainer[Volume]
    def __init__(self, volume_vec: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("name", "source_identifier", "count", "group_identifier", "target_resource_set_override_vec", "pause_secs", "script_vec", "type", "vm_properties", "primary_resource", "failover_job_uid")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM: _ClassVar[Resource.Type]
    VM: Resource.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_SET_OVERRIDE_VEC_FIELD_NUMBER: _ClassVar[int]
    PAUSE_SECS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_VEC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_JOB_UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_identifier: Identifier
    count: int
    group_identifier: Identifier
    target_resource_set_override_vec: _containers.RepeatedCompositeFieldContainer[Identifier]
    pause_secs: int
    script_vec: _containers.RepeatedCompositeFieldContainer[Identifier]
    type: Resource.Type
    vm_properties: VMProperties
    primary_resource: Resource
    failover_job_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, name: _Optional[str] = ..., source_identifier: _Optional[_Union[Identifier, _Mapping]] = ..., count: _Optional[int] = ..., group_identifier: _Optional[_Union[Identifier, _Mapping]] = ..., target_resource_set_override_vec: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., pause_secs: _Optional[int] = ..., script_vec: _Optional[_Iterable[_Union[Identifier, _Mapping]]] = ..., type: _Optional[_Union[Resource.Type, str]] = ..., vm_properties: _Optional[_Union[VMProperties, _Mapping]] = ..., primary_resource: _Optional[_Union[Resource, _Mapping]] = ..., failover_job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ScriptFile(_message.Message):
    __slots__ = ("name", "content")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: bytes
    def __init__(self, name: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class ScriptArg(_message.Message):
    __slots__ = ("constant", "resource_name", "property_string")
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_STRING_FIELD_NUMBER: _ClassVar[int]
    constant: str
    resource_name: str
    property_string: str
    def __init__(self, constant: _Optional[str] = ..., resource_name: _Optional[str] = ..., property_string: _Optional[str] = ...) -> None: ...

class Script(_message.Message):
    __slots__ = ("identifier", "type", "script_arg_vec", "script_file", "script_command", "destination", "interpreter")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE: _ClassVar[Script.Type]
        LOCAL: _ClassVar[Script.Type]
        REMOTE: _ClassVar[Script.Type]
    FILE: Script.Type
    LOCAL: Script.Type
    REMOTE: Script.Type
    class Interpreter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SHELL: _ClassVar[Script.Interpreter]
        PYTHON: _ClassVar[Script.Interpreter]
    SHELL: Script.Interpreter
    PYTHON: Script.Interpreter
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FILE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_COMMAND_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INTERPRETER_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    type: Script.Type
    script_arg_vec: _containers.RepeatedCompositeFieldContainer[ScriptArg]
    script_file: ScriptFile
    script_command: str
    destination: str
    interpreter: Script.Interpreter
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., type: _Optional[_Union[Script.Type, str]] = ..., script_arg_vec: _Optional[_Iterable[_Union[ScriptArg, _Mapping]]] = ..., script_file: _Optional[_Union[ScriptFile, _Mapping]] = ..., script_command: _Optional[str] = ..., destination: _Optional[str] = ..., interpreter: _Optional[_Union[Script.Interpreter, str]] = ...) -> None: ...

class ScriptResource(_message.Message):
    __slots__ = ("script", "group")
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    script: Script
    group: str
    def __init__(self, script: _Optional[_Union[Script, _Mapping]] = ..., group: _Optional[str] = ...) -> None: ...

class PauseResource(_message.Message):
    __slots__ = ("identifier", "pause_secs", "group")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PAUSE_SECS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    pause_secs: int
    group: str
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., pause_secs: _Optional[int] = ..., group: _Optional[str] = ...) -> None: ...

class DependencyRule(_message.Message):
    __slots__ = ("group", "depends_on_group")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_GROUP_FIELD_NUMBER: _ClassVar[int]
    group: str
    depends_on_group: str
    def __init__(self, group: _Optional[str] = ..., depends_on_group: _Optional[str] = ...) -> None: ...

class AppSpec(_message.Message):
    __slots__ = ("identifier", "resource_vec", "depends_on_vec", "script_vec", "script_resource_vec", "connection_vec", "connection_identifier", "vm_config_vec", "snapshot_selector", "target_vec", "target_profile_vec", "sid", "tenant_id", "status", "pause_resource_vec", "last_run_time_msecs", "last_validated_time_msecs", "validation_status", "replication_source", "replication_targets", "original_identifier", "use_case", "old_target_vec", "old_target_profile_vec", "old_replication_source", "failover_cycle_count", "tag_vec", "is_deleted")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[AppSpec.Status]
        kValidating: _ClassVar[AppSpec.Status]
        kValidated: _ClassVar[AppSpec.Status]
        kValidationFailed: _ClassVar[AppSpec.Status]
        kRunning: _ClassVar[AppSpec.Status]
        kSuccess: _ClassVar[AppSpec.Status]
        kFailed: _ClassVar[AppSpec.Status]
        kFailoverReady: _ClassVar[AppSpec.Status]
        kRunningFailover: _ClassVar[AppSpec.Status]
        kTeardownReady: _ClassVar[AppSpec.Status]
        kRunningTeardown: _ClassVar[AppSpec.Status]
        kFailoverDone: _ClassVar[AppSpec.Status]
        kPreparingForFailback: _ClassVar[AppSpec.Status]
        kFailbackReady: _ClassVar[AppSpec.Status]
        kRunningFailback: _ClassVar[AppSpec.Status]
        kFailoverFailed: _ClassVar[AppSpec.Status]
        kPrepareFailbackFailed: _ClassVar[AppSpec.Status]
        kFailbackFailed: _ClassVar[AppSpec.Status]
        kTeardownFailed: _ClassVar[AppSpec.Status]
    kCreated: AppSpec.Status
    kValidating: AppSpec.Status
    kValidated: AppSpec.Status
    kValidationFailed: AppSpec.Status
    kRunning: AppSpec.Status
    kSuccess: AppSpec.Status
    kFailed: AppSpec.Status
    kFailoverReady: AppSpec.Status
    kRunningFailover: AppSpec.Status
    kTeardownReady: AppSpec.Status
    kRunningTeardown: AppSpec.Status
    kFailoverDone: AppSpec.Status
    kPreparingForFailback: AppSpec.Status
    kFailbackReady: AppSpec.Status
    kRunningFailback: AppSpec.Status
    kFailoverFailed: AppSpec.Status
    kPrepareFailbackFailed: AppSpec.Status
    kFailbackFailed: AppSpec.Status
    kTeardownFailed: AppSpec.Status
    class UseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDR: _ClassVar[AppSpec.UseCase]
        kTestDev: _ClassVar[AppSpec.UseCase]
    kDR: AppSpec.UseCase
    kTestDev: AppSpec.UseCase
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAUSE_RESOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_VALIDATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    USE_CASE_FIELD_NUMBER: _ClassVar[int]
    OLD_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    OLD_TARGET_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    OLD_REPLICATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_CYCLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    identifier: Identifier
    resource_vec: _containers.RepeatedCompositeFieldContainer[Resource]
    depends_on_vec: _containers.RepeatedCompositeFieldContainer[DependencyRule]
    script_vec: _containers.RepeatedCompositeFieldContainer[Script]
    script_resource_vec: _containers.RepeatedCompositeFieldContainer[ScriptResource]
    connection_vec: _containers.RepeatedCompositeFieldContainer[Connection]
    connection_identifier: Identifier
    vm_config_vec: _containers.RepeatedCompositeFieldContainer[VmConfig]
    snapshot_selector: SnapshotSelector
    target_vec: _containers.RepeatedCompositeFieldContainer[Target]
    target_profile_vec: _containers.RepeatedCompositeFieldContainer[TargetProfile]
    sid: str
    tenant_id: str
    status: AppSpec.Status
    pause_resource_vec: _containers.RepeatedCompositeFieldContainer[PauseResource]
    last_run_time_msecs: int
    last_validated_time_msecs: int
    validation_status: AppSpec.Status
    replication_source: RemoteCluster
    replication_targets: _containers.RepeatedCompositeFieldContainer[RemoteCluster]
    original_identifier: Identifier
    use_case: AppSpec.UseCase
    old_target_vec: _containers.RepeatedCompositeFieldContainer[Target]
    old_target_profile_vec: _containers.RepeatedCompositeFieldContainer[TargetProfile]
    old_replication_source: RemoteCluster
    failover_cycle_count: int
    tag_vec: _containers.RepeatedScalarFieldContainer[str]
    is_deleted: bool
    def __init__(self, identifier: _Optional[_Union[Identifier, _Mapping]] = ..., resource_vec: _Optional[_Iterable[_Union[Resource, _Mapping]]] = ..., depends_on_vec: _Optional[_Iterable[_Union[DependencyRule, _Mapping]]] = ..., script_vec: _Optional[_Iterable[_Union[Script, _Mapping]]] = ..., script_resource_vec: _Optional[_Iterable[_Union[ScriptResource, _Mapping]]] = ..., connection_vec: _Optional[_Iterable[_Union[Connection, _Mapping]]] = ..., connection_identifier: _Optional[_Union[Identifier, _Mapping]] = ..., vm_config_vec: _Optional[_Iterable[_Union[VmConfig, _Mapping]]] = ..., snapshot_selector: _Optional[_Union[SnapshotSelector, _Mapping]] = ..., target_vec: _Optional[_Iterable[_Union[Target, _Mapping]]] = ..., target_profile_vec: _Optional[_Iterable[_Union[TargetProfile, _Mapping]]] = ..., sid: _Optional[str] = ..., tenant_id: _Optional[str] = ..., status: _Optional[_Union[AppSpec.Status, str]] = ..., pause_resource_vec: _Optional[_Iterable[_Union[PauseResource, _Mapping]]] = ..., last_run_time_msecs: _Optional[int] = ..., last_validated_time_msecs: _Optional[int] = ..., validation_status: _Optional[_Union[AppSpec.Status, str]] = ..., replication_source: _Optional[_Union[RemoteCluster, _Mapping]] = ..., replication_targets: _Optional[_Iterable[_Union[RemoteCluster, _Mapping]]] = ..., original_identifier: _Optional[_Union[Identifier, _Mapping]] = ..., use_case: _Optional[_Union[AppSpec.UseCase, str]] = ..., old_target_vec: _Optional[_Iterable[_Union[Target, _Mapping]]] = ..., old_target_profile_vec: _Optional[_Iterable[_Union[TargetProfile, _Mapping]]] = ..., old_replication_source: _Optional[_Union[RemoteCluster, _Mapping]] = ..., failover_cycle_count: _Optional[int] = ..., tag_vec: _Optional[_Iterable[str]] = ..., is_deleted: bool = ...) -> None: ...
