from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenResult(_message.Message):
    __slots__ = ("access_token",)
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("reason", "detail")
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    reason: str
    detail: str
    def __init__(self, reason: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class OSInfo(_message.Message):
    __slots__ = ("boot", "type")
    class Boot(_message.Message):
        __slots__ = ("devices",)
        class Devices(_message.Message):
            __slots__ = ("device",)
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            device: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, device: _Optional[_Iterable[str]] = ...) -> None: ...
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: OSInfo.Boot.Devices
        def __init__(self, devices: _Optional[_Union[OSInfo.Boot.Devices, _Mapping]] = ...) -> None: ...
    BOOT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    boot: OSInfo.Boot
    type: str
    def __init__(self, boot: _Optional[_Union[OSInfo.Boot, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...

class VMInfo(_message.Message):
    __slots__ = ("name", "description", "id", "status", "cpu", "memory", "os", "cluster", "vm_template", "host", "custom_emulated_machine", "type", "comment", "memory_policy", "high_availability", "time_zone", "initialization", "total_disk_size")
    class CPU(_message.Message):
        __slots__ = ("topology",)
        class Topology(_message.Message):
            __slots__ = ("sockets", "cores", "threads")
            SOCKETS_FIELD_NUMBER: _ClassVar[int]
            CORES_FIELD_NUMBER: _ClassVar[int]
            THREADS_FIELD_NUMBER: _ClassVar[int]
            sockets: int
            cores: int
            threads: int
            def __init__(self, sockets: _Optional[int] = ..., cores: _Optional[int] = ..., threads: _Optional[int] = ...) -> None: ...
        TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
        topology: VMInfo.CPU.Topology
        def __init__(self, topology: _Optional[_Union[VMInfo.CPU.Topology, _Mapping]] = ...) -> None: ...
    class Template(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Host(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class MemoryPolicy(_message.Message):
        __slots__ = ("guaranteed", "max")
        GUARANTEED_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        guaranteed: int
        max: int
        def __init__(self, guaranteed: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
    class HighAvailability(_message.Message):
        __slots__ = ("enabled", "priority")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        priority: int
        def __init__(self, enabled: bool = ..., priority: _Optional[int] = ...) -> None: ...
    class TimeZone(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Initialization(_message.Message):
        __slots__ = ("configuration",)
        class Configuration(_message.Message):
            __slots__ = ("data",)
            DATA_FIELD_NUMBER: _ClassVar[int]
            data: str
            def __init__(self, data: _Optional[str] = ...) -> None: ...
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        configuration: VMInfo.Initialization.Configuration
        def __init__(self, configuration: _Optional[_Union[VMInfo.Initialization.Configuration, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMULATED_MACHINE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_POLICY_FIELD_NUMBER: _ClassVar[int]
    HIGH_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    id: str
    status: str
    cpu: VMInfo.CPU
    memory: int
    os: OSInfo
    cluster: Cluster
    vm_template: VMInfo.Template
    host: VMInfo.Host
    custom_emulated_machine: str
    type: str
    comment: str
    memory_policy: VMInfo.MemoryPolicy
    high_availability: VMInfo.HighAvailability
    time_zone: VMInfo.TimeZone
    initialization: VMInfo.Initialization
    total_disk_size: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[str] = ..., cpu: _Optional[_Union[VMInfo.CPU, _Mapping]] = ..., memory: _Optional[int] = ..., os: _Optional[_Union[OSInfo, _Mapping]] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., vm_template: _Optional[_Union[VMInfo.Template, _Mapping]] = ..., host: _Optional[_Union[VMInfo.Host, _Mapping]] = ..., custom_emulated_machine: _Optional[str] = ..., type: _Optional[str] = ..., comment: _Optional[str] = ..., memory_policy: _Optional[_Union[VMInfo.MemoryPolicy, _Mapping]] = ..., high_availability: _Optional[_Union[VMInfo.HighAvailability, _Mapping]] = ..., time_zone: _Optional[_Union[VMInfo.TimeZone, _Mapping]] = ..., initialization: _Optional[_Union[VMInfo.Initialization, _Mapping]] = ..., total_disk_size: _Optional[int] = ...) -> None: ...

class HostConfig(_message.Message):
    __slots__ = ("name", "id", "address", "cluster", "spm")
    class SPM(_message.Message):
        __slots__ = ("status",)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: str
        def __init__(self, status: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SPM_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    address: str
    cluster: Cluster
    spm: HostConfig.SPM
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., address: _Optional[str] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., spm: _Optional[_Union[HostConfig.SPM, _Mapping]] = ...) -> None: ...

class HostListResult(_message.Message):
    __slots__ = ("host",)
    HOST_FIELD_NUMBER: _ClassVar[int]
    host: _containers.RepeatedCompositeFieldContainer[HostConfig]
    def __init__(self, host: _Optional[_Iterable[_Union[HostConfig, _Mapping]]] = ...) -> None: ...

class DataCenter(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class VMListResult(_message.Message):
    __slots__ = ("vm",)
    VM_FIELD_NUMBER: _ClassVar[int]
    vm: _containers.RepeatedCompositeFieldContainer[VMInfo]
    def __init__(self, vm: _Optional[_Iterable[_Union[VMInfo, _Mapping]]] = ...) -> None: ...

class NetworkConfig(_message.Message):
    __slots__ = ("name", "id", "description", "data_center")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    description: str
    data_center: DataCenter
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., description: _Optional[str] = ..., data_center: _Optional[_Union[DataCenter, _Mapping]] = ...) -> None: ...

class NetworkListResult(_message.Message):
    __slots__ = ("network",)
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: _containers.RepeatedCompositeFieldContainer[NetworkConfig]
    def __init__(self, network: _Optional[_Iterable[_Union[NetworkConfig, _Mapping]]] = ...) -> None: ...

class ClusterConfig(_message.Message):
    __slots__ = ("name", "id", "data_center")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    data_center: DataCenter
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., data_center: _Optional[_Union[DataCenter, _Mapping]] = ...) -> None: ...

class ClusterListResult(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: _containers.RepeatedCompositeFieldContainer[ClusterConfig]
    def __init__(self, cluster: _Optional[_Iterable[_Union[ClusterConfig, _Mapping]]] = ...) -> None: ...

class MACPool(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class MACPoolsListResult(_message.Message):
    __slots__ = ("mac_pool",)
    MAC_POOL_FIELD_NUMBER: _ClassVar[int]
    mac_pool: _containers.RepeatedCompositeFieldContainer[MACPool]
    def __init__(self, mac_pool: _Optional[_Iterable[_Union[MACPool, _Mapping]]] = ...) -> None: ...

class StorageDomainConfig(_message.Message):
    __slots__ = ("name", "id", "status", "data_centers")
    class DataCenterList(_message.Message):
        __slots__ = ("data_center",)
        class DataCenter(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        DATA_CENTER_FIELD_NUMBER: _ClassVar[int]
        data_center: _containers.RepeatedCompositeFieldContainer[StorageDomainConfig.DataCenterList.DataCenter]
        def __init__(self, data_center: _Optional[_Iterable[_Union[StorageDomainConfig.DataCenterList.DataCenter, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_CENTERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    status: str
    data_centers: StorageDomainConfig.DataCenterList
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[str] = ..., data_centers: _Optional[_Union[StorageDomainConfig.DataCenterList, _Mapping]] = ...) -> None: ...

class StorageDomainListResult(_message.Message):
    __slots__ = ("storage_domain",)
    STORAGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    storage_domain: _containers.RepeatedCompositeFieldContainer[StorageDomainConfig]
    def __init__(self, storage_domain: _Optional[_Iterable[_Union[StorageDomainConfig, _Mapping]]] = ...) -> None: ...

class DataCenterConfig(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DataCenterListResult(_message.Message):
    __slots__ = ("data_center",)
    DATA_CENTER_FIELD_NUMBER: _ClassVar[int]
    data_center: _containers.RepeatedCompositeFieldContainer[DataCenterConfig]
    def __init__(self, data_center: _Optional[_Iterable[_Union[DataCenterConfig, _Mapping]]] = ...) -> None: ...

class VNicProfile(_message.Message):
    __slots__ = ("id", "name", "network")
    class Network(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    network: VNicProfile.Network
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., network: _Optional[_Union[VNicProfile.Network, _Mapping]] = ...) -> None: ...

class VNicProfileList(_message.Message):
    __slots__ = ("vnic_profile",)
    VNIC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    vnic_profile: _containers.RepeatedCompositeFieldContainer[VNicProfile]
    def __init__(self, vnic_profile: _Optional[_Iterable[_Union[VNicProfile, _Mapping]]] = ...) -> None: ...

class VMNicListArg(_message.Message):
    __slots__ = ("vm_id",)
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    def __init__(self, vm_id: _Optional[str] = ...) -> None: ...

class Nic(_message.Message):
    __slots__ = ("name", "id", "mac", "reported_devices", "vnic_profile", "network")
    class Mac(_message.Message):
        __slots__ = ("address",)
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        address: str
        def __init__(self, address: _Optional[str] = ...) -> None: ...
    class Devices(_message.Message):
        __slots__ = ("reported_device",)
        class Device(_message.Message):
            __slots__ = ("ips", "name", "id")
            class IPs(_message.Message):
                __slots__ = ("ip",)
                class IP(_message.Message):
                    __slots__ = ("address", "version")
                    ADDRESS_FIELD_NUMBER: _ClassVar[int]
                    VERSION_FIELD_NUMBER: _ClassVar[int]
                    address: str
                    version: str
                    def __init__(self, address: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
                IP_FIELD_NUMBER: _ClassVar[int]
                ip: _containers.RepeatedCompositeFieldContainer[Nic.Devices.Device.IPs.IP]
                def __init__(self, ip: _Optional[_Iterable[_Union[Nic.Devices.Device.IPs.IP, _Mapping]]] = ...) -> None: ...
            IPS_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            ips: Nic.Devices.Device.IPs
            name: str
            id: str
            def __init__(self, ips: _Optional[_Union[Nic.Devices.Device.IPs, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
        REPORTED_DEVICE_FIELD_NUMBER: _ClassVar[int]
        reported_device: _containers.RepeatedCompositeFieldContainer[Nic.Devices.Device]
        def __init__(self, reported_device: _Optional[_Iterable[_Union[Nic.Devices.Device, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    REPORTED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    VNIC_PROFILE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    mac: Nic.Mac
    reported_devices: Nic.Devices
    vnic_profile: VNicProfile
    network: NetworkConfig
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., mac: _Optional[_Union[Nic.Mac, _Mapping]] = ..., reported_devices: _Optional[_Union[Nic.Devices, _Mapping]] = ..., vnic_profile: _Optional[_Union[VNicProfile, _Mapping]] = ..., network: _Optional[_Union[NetworkConfig, _Mapping]] = ...) -> None: ...

class VMNicListResult(_message.Message):
    __slots__ = ("nic",)
    NIC_FIELD_NUMBER: _ClassVar[int]
    nic: _containers.RepeatedCompositeFieldContainer[Nic]
    def __init__(self, nic: _Optional[_Iterable[_Union[Nic, _Mapping]]] = ...) -> None: ...

class HostNicArg(_message.Message):
    __slots__ = ("host_id",)
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    host_id: str
    def __init__(self, host_id: _Optional[str] = ...) -> None: ...

class HostNicResult(_message.Message):
    __slots__ = ("host_nic",)
    class HostNic(_message.Message):
        __slots__ = ("name", "ip")
        class IP(_message.Message):
            __slots__ = ("address", "gateway", "netmask")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            GATEWAY_FIELD_NUMBER: _ClassVar[int]
            NETMASK_FIELD_NUMBER: _ClassVar[int]
            address: str
            gateway: str
            netmask: str
            def __init__(self, address: _Optional[str] = ..., gateway: _Optional[str] = ..., netmask: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        name: str
        ip: HostNicResult.HostNic.IP
        def __init__(self, name: _Optional[str] = ..., ip: _Optional[_Union[HostNicResult.HostNic.IP, _Mapping]] = ...) -> None: ...
    HOST_NIC_FIELD_NUMBER: _ClassVar[int]
    host_nic: _containers.RepeatedCompositeFieldContainer[HostNicResult.HostNic]
    def __init__(self, host_nic: _Optional[_Iterable[_Union[HostNicResult.HostNic, _Mapping]]] = ...) -> None: ...

class OVirtConfig(_message.Message):
    __slots__ = ("product_info",)
    class ProductInfo(_message.Message):
        __slots__ = ("name", "version")
        class Version(_message.Message):
            __slots__ = ("major_version", "minor_version", "build_version")
            MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
            MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
            BUILD_VERSION_FIELD_NUMBER: _ClassVar[int]
            major_version: str
            minor_version: str
            build_version: str
            def __init__(self, major_version: _Optional[str] = ..., minor_version: _Optional[str] = ..., build_version: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: OVirtConfig.ProductInfo.Version
        def __init__(self, name: _Optional[str] = ..., version: _Optional[_Union[OVirtConfig.ProductInfo.Version, _Mapping]] = ...) -> None: ...
    PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    product_info: OVirtConfig.ProductInfo
    def __init__(self, product_info: _Optional[_Union[OVirtConfig.ProductInfo, _Mapping]] = ...) -> None: ...

class DiskInfoArg(_message.Message):
    __slots__ = ("url_prefix",)
    URL_PREFIX_FIELD_NUMBER: _ClassVar[int]
    url_prefix: str
    def __init__(self, url_prefix: _Optional[str] = ...) -> None: ...

class DiskInfo(_message.Message):
    __slots__ = ("actual_size", "provisioned_size", "name", "id", "format", "read_only", "shareable", "wipe_after_delete", "sparse", "image_id", "storage_domains", "description")
    class StorageDomains(_message.Message):
        __slots__ = ("storage_domain",)
        class StorageDomain(_message.Message):
            __slots__ = ("id", "name")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
        STORAGE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        storage_domain: _containers.RepeatedCompositeFieldContainer[DiskInfo.StorageDomains.StorageDomain]
        def __init__(self, storage_domain: _Optional[_Iterable[_Union[DiskInfo.StorageDomains.StorageDomain, _Mapping]]] = ...) -> None: ...
    ACTUAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    SHAREABLE_FIELD_NUMBER: _ClassVar[int]
    WIPE_AFTER_DELETE_FIELD_NUMBER: _ClassVar[int]
    SPARSE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    actual_size: int
    provisioned_size: int
    name: str
    id: str
    format: str
    read_only: bool
    shareable: bool
    wipe_after_delete: bool
    sparse: bool
    image_id: str
    storage_domains: DiskInfo.StorageDomains
    description: str
    def __init__(self, actual_size: _Optional[int] = ..., provisioned_size: _Optional[int] = ..., name: _Optional[str] = ..., id: _Optional[str] = ..., format: _Optional[str] = ..., read_only: bool = ..., shareable: bool = ..., wipe_after_delete: bool = ..., sparse: bool = ..., image_id: _Optional[str] = ..., storage_domains: _Optional[_Union[DiskInfo.StorageDomains, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class DiskInfoResult(_message.Message):
    __slots__ = ("disk",)
    DISK_FIELD_NUMBER: _ClassVar[int]
    disk: _containers.RepeatedCompositeFieldContainer[DiskInfo]
    def __init__(self, disk: _Optional[_Iterable[_Union[DiskInfo, _Mapping]]] = ...) -> None: ...

class WaitForJobArg(_message.Message):
    __slots__ = ("job_id", "wait_timeout_usecs")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIMEOUT_USECS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    wait_timeout_usecs: int
    def __init__(self, job_id: _Optional[str] = ..., wait_timeout_usecs: _Optional[int] = ...) -> None: ...

class WaitForJobResult(_message.Message):
    __slots__ = ("status", "description", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    description: str
    id: str
    def __init__(self, status: _Optional[str] = ..., description: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class PollEventArg(_message.Message):
    __slots__ = ("correlation_id", "success_code", "failure_code", "timeout_secs")
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CODE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    correlation_id: str
    success_code: int
    failure_code: int
    timeout_secs: int
    def __init__(self, correlation_id: _Optional[str] = ..., success_code: _Optional[int] = ..., failure_code: _Optional[int] = ..., timeout_secs: _Optional[int] = ...) -> None: ...

class PollEventResult(_message.Message):
    __slots__ = ("event",)
    class Event(_message.Message):
        __slots__ = ("correlation_id", "severity", "code", "description")
        CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        correlation_id: str
        severity: str
        code: int
        description: str
        def __init__(self, correlation_id: _Optional[str] = ..., severity: _Optional[str] = ..., code: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _containers.RepeatedCompositeFieldContainer[PollEventResult.Event]
    def __init__(self, event: _Optional[_Iterable[_Union[PollEventResult.Event, _Mapping]]] = ...) -> None: ...

class JobInfo(_message.Message):
    __slots__ = ("status", "job")
    class Job(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    status: str
    job: JobInfo.Job
    def __init__(self, status: _Optional[str] = ..., job: _Optional[_Union[JobInfo.Job, _Mapping]] = ...) -> None: ...

class SnapshotInfoResult(_message.Message):
    __slots__ = ("id", "vm", "description", "snapshot_status", "snapshot_type")
    class VMInfo(_message.Message):
        __slots__ = ("cluster",)
        class ClusterInfo(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: _Optional[str] = ...) -> None: ...
        CLUSTER_FIELD_NUMBER: _ClassVar[int]
        cluster: SnapshotInfoResult.VMInfo.ClusterInfo
        def __init__(self, cluster: _Optional[_Union[SnapshotInfoResult.VMInfo.ClusterInfo, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VM_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATUS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    vm: SnapshotInfoResult.VMInfo
    description: str
    snapshot_status: str
    snapshot_type: str
    def __init__(self, id: _Optional[str] = ..., vm: _Optional[_Union[SnapshotInfoResult.VMInfo, _Mapping]] = ..., description: _Optional[str] = ..., snapshot_status: _Optional[str] = ..., snapshot_type: _Optional[str] = ...) -> None: ...

class SnapshotListArg(_message.Message):
    __slots__ = ("vm_id",)
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    def __init__(self, vm_id: _Optional[str] = ...) -> None: ...

class SnapshotListResult(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: _containers.RepeatedCompositeFieldContainer[SnapshotInfoResult]
    def __init__(self, snapshot: _Optional[_Iterable[_Union[SnapshotInfoResult, _Mapping]]] = ...) -> None: ...

class CreateSnapshotArg(_message.Message):
    __slots__ = ("description", "persist_memorystate")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERSIST_MEMORYSTATE_FIELD_NUMBER: _ClassVar[int]
    description: str
    persist_memorystate: bool
    def __init__(self, description: _Optional[str] = ..., persist_memorystate: bool = ...) -> None: ...

class CreateSnapshotResult(_message.Message):
    __slots__ = ("id", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateVMNicArg(_message.Message):
    __slots__ = ("vm_id", "nic_conf")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    NIC_CONF_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    nic_conf: Nic
    def __init__(self, vm_id: _Optional[str] = ..., nic_conf: _Optional[_Union[Nic, _Mapping]] = ...) -> None: ...

class CreateDiskAttachmentArg(_message.Message):
    __slots__ = ("vm_id", "attachment_conf")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_CONF_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    attachment_conf: DiskAttachmentConf
    def __init__(self, vm_id: _Optional[str] = ..., attachment_conf: _Optional[_Union[DiskAttachmentConf, _Mapping]] = ...) -> None: ...

class DiskAttachmentConf(_message.Message):
    __slots__ = ("bootable", "active", "interface", "read_only", "disk")
    BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    bootable: bool
    active: bool
    interface: str
    read_only: bool
    disk: DiskInfo
    def __init__(self, bootable: bool = ..., active: bool = ..., interface: _Optional[str] = ..., read_only: bool = ..., disk: _Optional[_Union[DiskInfo, _Mapping]] = ...) -> None: ...

class PowerStateArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerStateResult(_message.Message):
    __slots__ = ("fault", "status")
    class Fault(_message.Message):
        __slots__ = ("detail", "reason")
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        detail: str
        reason: str
        def __init__(self, detail: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...
    FAULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    fault: PowerStateResult.Fault
    status: str
    def __init__(self, fault: _Optional[_Union[PowerStateResult.Fault, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class VMDiskListArg(_message.Message):
    __slots__ = ("vm_id", "dc_id")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    DC_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    dc_id: str
    def __init__(self, vm_id: _Optional[str] = ..., dc_id: _Optional[str] = ...) -> None: ...

class DiskAttachmentArg(_message.Message):
    __slots__ = ("vm_id",)
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    def __init__(self, vm_id: _Optional[str] = ...) -> None: ...

class DiskAttachmentResult(_message.Message):
    __slots__ = ("disk_attachment",)
    DISK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    disk_attachment: _containers.RepeatedCompositeFieldContainer[DiskAttachmentConf]
    def __init__(self, disk_attachment: _Optional[_Iterable[_Union[DiskAttachmentConf, _Mapping]]] = ...) -> None: ...
