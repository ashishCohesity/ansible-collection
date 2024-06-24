from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BIOS: _ClassVar[FirmwareType]
    UEFI: _ClassVar[FirmwareType]
    UEFI_SECURE_BOOT: _ClassVar[FirmwareType]

class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANY: _ClassVar[Protocol]
    AH: _ClassVar[Protocol]
    DCCP: _ClassVar[Protocol]
    EGP: _ClassVar[Protocol]
    ESP: _ClassVar[Protocol]
    GRE: _ClassVar[Protocol]
    ICMP: _ClassVar[Protocol]
    ICMPV6: _ClassVar[Protocol]
    IGMP: _ClassVar[Protocol]
    IPIP: _ClassVar[Protocol]
    IPV6_ENCAP: _ClassVar[Protocol]
    IPV6_FRAG: _ClassVar[Protocol]
    IPV6_ICMP: _ClassVar[Protocol]
    IPV6_NONXT: _ClassVar[Protocol]
    IPV6_OPTS: _ClassVar[Protocol]
    IPV6_ROUTE: _ClassVar[Protocol]
    OSPF: _ClassVar[Protocol]
    PGM: _ClassVar[Protocol]
    RSVP: _ClassVar[Protocol]
    SCTP: _ClassVar[Protocol]
    TCP: _ClassVar[Protocol]
    UDP: _ClassVar[Protocol]
    UDPLITE: _ClassVar[Protocol]
    VRRP: _ClassVar[Protocol]
BIOS: FirmwareType
UEFI: FirmwareType
UEFI_SECURE_BOOT: FirmwareType
ANY: Protocol
AH: Protocol
DCCP: Protocol
EGP: Protocol
ESP: Protocol
GRE: Protocol
ICMP: Protocol
ICMPV6: Protocol
IGMP: Protocol
IPIP: Protocol
IPV6_ENCAP: Protocol
IPV6_FRAG: Protocol
IPV6_ICMP: Protocol
IPV6_NONXT: Protocol
IPV6_OPTS: Protocol
IPV6_ROUTE: Protocol
OSPF: Protocol
PGM: Protocol
RSVP: Protocol
SCTP: Protocol
TCP: Protocol
UDP: Protocol
UDPLITE: Protocol
VRRP: Protocol

class Event(_message.Message):
    __slots__ = ("id", "metadata", "type", "timestamp", "owner", "request_id", "details")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERNAL: _ClassVar[Event.Type]
    INTERNAL: Event.Type
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    metadata: _containers.ScalarMap[str, str]
    type: Event.Type
    timestamp: int
    owner: str
    request_id: str
    details: bytes
    def __init__(self, id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., type: _Optional[_Union[Event.Type, str]] = ..., timestamp: _Optional[int] = ..., owner: _Optional[str] = ..., request_id: _Optional[str] = ..., details: _Optional[bytes] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("timestamp", "summary", "details", "debug_info")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_INFO_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    summary: str
    details: str
    debug_info: bytes
    def __init__(self, timestamp: _Optional[int] = ..., summary: _Optional[str] = ..., details: _Optional[str] = ..., debug_info: _Optional[bytes] = ...) -> None: ...

class MetadataSelector(_message.Message):
    __slots__ = ("key", "operator", "values")
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        In: _ClassVar[MetadataSelector.Operator]
        NotIn: _ClassVar[MetadataSelector.Operator]
        Exists: _ClassVar[MetadataSelector.Operator]
        DoesNotExist: _ClassVar[MetadataSelector.Operator]
        Lt: _ClassVar[MetadataSelector.Operator]
        Gt: _ClassVar[MetadataSelector.Operator]
    In: MetadataSelector.Operator
    NotIn: MetadataSelector.Operator
    Exists: MetadataSelector.Operator
    DoesNotExist: MetadataSelector.Operator
    Lt: MetadataSelector.Operator
    Gt: MetadataSelector.Operator
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    operator: MetadataSelector.Operator
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., operator: _Optional[_Union[MetadataSelector.Operator, str]] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "hostname", "ip_address", "fqdn", "creation_timestamp", "update_timestamp", "status", "errors")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Host.Status]
        UP: _ClassVar[Host.Status]
        DOWN: _ClassVar[Host.Status]
        MAINTENANCE: _ClassVar[Host.Status]
        ERROR: _ClassVar[Host.Status]
    UNKNOWN: Host.Status
    UP: Host.Status
    DOWN: Host.Status
    MAINTENANCE: Host.Status
    ERROR: Host.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    hostname: str
    ip_address: str
    fqdn: str
    creation_timestamp: int
    update_timestamp: int
    status: Host.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., hostname: _Optional[str] = ..., ip_address: _Optional[str] = ..., fqdn: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., status: _Optional[_Union[Host.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class VMInstanceType(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "vcpus", "memory_in_bytes", "tenant", "custom", "creation_timestamp", "update_timestamp")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VCPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    vcpus: int
    memory_in_bytes: int
    tenant: _containers.RepeatedScalarFieldContainer[str]
    custom: bool
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., vcpus: _Optional[int] = ..., memory_in_bytes: _Optional[int] = ..., tenant: _Optional[_Iterable[str]] = ..., custom: bool = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...

class Keypair(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "type", "public_key", "owner", "creation_timestamp", "update_timestamp", "fingerprint")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SSH: _ClassVar[Keypair.Type]
        X509: _ClassVar[Keypair.Type]
    SSH: Keypair.Type
    X509: Keypair.Type
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    type: Keypair.Type
    public_key: str
    owner: str
    creation_timestamp: int
    update_timestamp: int
    fingerprint: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., type: _Optional[_Union[Keypair.Type, str]] = ..., public_key: _Optional[str] = ..., owner: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., fingerprint: _Optional[str] = ...) -> None: ...

class VMInstance(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "firmware_type", "instance_type", "hostname", "keypairs", "user_data", "block_device_mappings", "network_interfaces", "high_availability", "scheduler_hints", "tenant", "vnc_port", "migration_dst_host", "creation_timestamp", "update_timestamp", "state_progress", "total_storage", "start_timestamp", "stop_timestamp", "host", "state", "errors")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[VMInstance.State]
        CREATING: _ClassVar[VMInstance.State]
        CREATED: _ClassVar[VMInstance.State]
        RUNNING: _ClassVar[VMInstance.State]
        STOPPED: _ClassVar[VMInstance.State]
        PAUSED: _ClassVar[VMInstance.State]
        REMOVING: _ClassVar[VMInstance.State]
        MIGRATING: _ClassVar[VMInstance.State]
        MIGRATED: _ClassVar[VMInstance.State]
        CONVERTING: _ClassVar[VMInstance.State]
        CONVERTED: _ClassVar[VMInstance.State]
        FAILED: _ClassVar[VMInstance.State]
        RESIZING: _ClassVar[VMInstance.State]
        DELETING: _ClassVar[VMInstance.State]
        DELETED: _ClassVar[VMInstance.State]
    UNKNOWN: VMInstance.State
    CREATING: VMInstance.State
    CREATED: VMInstance.State
    RUNNING: VMInstance.State
    STOPPED: VMInstance.State
    PAUSED: VMInstance.State
    REMOVING: VMInstance.State
    MIGRATING: VMInstance.State
    MIGRATED: VMInstance.State
    CONVERTING: VMInstance.State
    CONVERTED: VMInstance.State
    FAILED: VMInstance.State
    RESIZING: VMInstance.State
    DELETING: VMInstance.State
    DELETED: VMInstance.State
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class BlockDeviceMapping(_message.Message):
        __slots__ = ("id", "name", "type", "device_type", "bus_type", "boot_index", "qos")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VOLUME: _ClassVar[VMInstance.BlockDeviceMapping.Type]
            EPHIMERAL: _ClassVar[VMInstance.BlockDeviceMapping.Type]
        VOLUME: VMInstance.BlockDeviceMapping.Type
        EPHIMERAL: VMInstance.BlockDeviceMapping.Type
        class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DISK: _ClassVar[VMInstance.BlockDeviceMapping.DeviceType]
            CDROM: _ClassVar[VMInstance.BlockDeviceMapping.DeviceType]
            FLOPPY: _ClassVar[VMInstance.BlockDeviceMapping.DeviceType]
        DISK: VMInstance.BlockDeviceMapping.DeviceType
        CDROM: VMInstance.BlockDeviceMapping.DeviceType
        FLOPPY: VMInstance.BlockDeviceMapping.DeviceType
        class BusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VIRTIO: _ClassVar[VMInstance.BlockDeviceMapping.BusType]
            IDE: _ClassVar[VMInstance.BlockDeviceMapping.BusType]
            SCSI: _ClassVar[VMInstance.BlockDeviceMapping.BusType]
            FDC: _ClassVar[VMInstance.BlockDeviceMapping.BusType]
        VIRTIO: VMInstance.BlockDeviceMapping.BusType
        IDE: VMInstance.BlockDeviceMapping.BusType
        SCSI: VMInstance.BlockDeviceMapping.BusType
        FDC: VMInstance.BlockDeviceMapping.BusType
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        BUS_TYPE_FIELD_NUMBER: _ClassVar[int]
        BOOT_INDEX_FIELD_NUMBER: _ClassVar[int]
        QOS_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        type: VMInstance.BlockDeviceMapping.Type
        device_type: VMInstance.BlockDeviceMapping.DeviceType
        bus_type: VMInstance.BlockDeviceMapping.BusType
        boot_index: int
        qos: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[VMInstance.BlockDeviceMapping.Type, str]] = ..., device_type: _Optional[_Union[VMInstance.BlockDeviceMapping.DeviceType, str]] = ..., bus_type: _Optional[_Union[VMInstance.BlockDeviceMapping.BusType, str]] = ..., boot_index: _Optional[int] = ..., qos: _Optional[str] = ...) -> None: ...
    class NetworkInterfaceMapping(_message.Message):
        __slots__ = ("name", "port", "vif_type", "qos", "mac_address", "fixed_ip")
        class VifType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            E1000: _ClassVar[VMInstance.NetworkInterfaceMapping.VifType]
            RTL8139: _ClassVar[VMInstance.NetworkInterfaceMapping.VifType]
            VIRTIO: _ClassVar[VMInstance.NetworkInterfaceMapping.VifType]
        E1000: VMInstance.NetworkInterfaceMapping.VifType
        RTL8139: VMInstance.NetworkInterfaceMapping.VifType
        VIRTIO: VMInstance.NetworkInterfaceMapping.VifType
        NAME_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        VIF_TYPE_FIELD_NUMBER: _ClassVar[int]
        QOS_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        FIXED_IP_FIELD_NUMBER: _ClassVar[int]
        name: str
        port: str
        vif_type: VMInstance.NetworkInterfaceMapping.VifType
        qos: str
        mac_address: str
        fixed_ip: str
        def __init__(self, name: _Optional[str] = ..., port: _Optional[str] = ..., vif_type: _Optional[_Union[VMInstance.NetworkInterfaceMapping.VifType, str]] = ..., qos: _Optional[str] = ..., mac_address: _Optional[str] = ..., fixed_ip: _Optional[str] = ...) -> None: ...
    class SchedulerHints(_message.Message):
        __slots__ = ("automatic_start_on_boot", "on_host_maintenance", "affinities", "anti_affinities")
        class OnHostMaintenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MIGRATE: _ClassVar[VMInstance.SchedulerHints.OnHostMaintenance]
            TERMINATE: _ClassVar[VMInstance.SchedulerHints.OnHostMaintenance]
        MIGRATE: VMInstance.SchedulerHints.OnHostMaintenance
        TERMINATE: VMInstance.SchedulerHints.OnHostMaintenance
        class Affinity(_message.Message):
            __slots__ = ("resource_type", "metadata_selectors", "weight", "topology_keys")
            class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                VM_INSTANCE: _ClassVar[VMInstance.SchedulerHints.Affinity.ResourceType]
                HOST: _ClassVar[VMInstance.SchedulerHints.Affinity.ResourceType]
            VM_INSTANCE: VMInstance.SchedulerHints.Affinity.ResourceType
            HOST: VMInstance.SchedulerHints.Affinity.ResourceType
            RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
            METADATA_SELECTORS_FIELD_NUMBER: _ClassVar[int]
            WEIGHT_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_KEYS_FIELD_NUMBER: _ClassVar[int]
            resource_type: VMInstance.SchedulerHints.Affinity.ResourceType
            metadata_selectors: _containers.RepeatedCompositeFieldContainer[MetadataSelector]
            weight: int
            topology_keys: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, resource_type: _Optional[_Union[VMInstance.SchedulerHints.Affinity.ResourceType, str]] = ..., metadata_selectors: _Optional[_Iterable[_Union[MetadataSelector, _Mapping]]] = ..., weight: _Optional[int] = ..., topology_keys: _Optional[_Iterable[str]] = ...) -> None: ...
        class AntiAffinity(_message.Message):
            __slots__ = ("resource_type", "metadata_selectors", "weight", "topology_keys")
            class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                VM_INSTANCE: _ClassVar[VMInstance.SchedulerHints.AntiAffinity.ResourceType]
                HOST: _ClassVar[VMInstance.SchedulerHints.AntiAffinity.ResourceType]
            VM_INSTANCE: VMInstance.SchedulerHints.AntiAffinity.ResourceType
            HOST: VMInstance.SchedulerHints.AntiAffinity.ResourceType
            RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
            METADATA_SELECTORS_FIELD_NUMBER: _ClassVar[int]
            WEIGHT_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_KEYS_FIELD_NUMBER: _ClassVar[int]
            resource_type: VMInstance.SchedulerHints.AntiAffinity.ResourceType
            metadata_selectors: _containers.RepeatedCompositeFieldContainer[MetadataSelector]
            weight: int
            topology_keys: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, resource_type: _Optional[_Union[VMInstance.SchedulerHints.AntiAffinity.ResourceType, str]] = ..., metadata_selectors: _Optional[_Iterable[_Union[MetadataSelector, _Mapping]]] = ..., weight: _Optional[int] = ..., topology_keys: _Optional[_Iterable[str]] = ...) -> None: ...
        AUTOMATIC_START_ON_BOOT_FIELD_NUMBER: _ClassVar[int]
        ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
        AFFINITIES_FIELD_NUMBER: _ClassVar[int]
        ANTI_AFFINITIES_FIELD_NUMBER: _ClassVar[int]
        automatic_start_on_boot: bool
        on_host_maintenance: VMInstance.SchedulerHints.OnHostMaintenance
        affinities: _containers.RepeatedCompositeFieldContainer[VMInstance.SchedulerHints.Affinity]
        anti_affinities: _containers.RepeatedCompositeFieldContainer[VMInstance.SchedulerHints.AntiAffinity]
        def __init__(self, automatic_start_on_boot: bool = ..., on_host_maintenance: _Optional[_Union[VMInstance.SchedulerHints.OnHostMaintenance, str]] = ..., affinities: _Optional[_Iterable[_Union[VMInstance.SchedulerHints.Affinity, _Mapping]]] = ..., anti_affinities: _Optional[_Iterable[_Union[VMInstance.SchedulerHints.AntiAffinity, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    KEYPAIRS_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DEVICE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    HIGH_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_HINTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    VNC_PORT_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_DST_HOST_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    firmware_type: FirmwareType
    instance_type: VMInstanceType
    hostname: str
    keypairs: _containers.RepeatedScalarFieldContainer[str]
    user_data: str
    block_device_mappings: _containers.RepeatedCompositeFieldContainer[VMInstance.BlockDeviceMapping]
    network_interfaces: _containers.RepeatedCompositeFieldContainer[VMInstance.NetworkInterfaceMapping]
    high_availability: bool
    scheduler_hints: VMInstance.SchedulerHints
    tenant: str
    vnc_port: int
    migration_dst_host: str
    creation_timestamp: int
    update_timestamp: int
    state_progress: float
    total_storage: int
    start_timestamp: int
    stop_timestamp: int
    host: str
    state: VMInstance.State
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., firmware_type: _Optional[_Union[FirmwareType, str]] = ..., instance_type: _Optional[_Union[VMInstanceType, _Mapping]] = ..., hostname: _Optional[str] = ..., keypairs: _Optional[_Iterable[str]] = ..., user_data: _Optional[str] = ..., block_device_mappings: _Optional[_Iterable[_Union[VMInstance.BlockDeviceMapping, _Mapping]]] = ..., network_interfaces: _Optional[_Iterable[_Union[VMInstance.NetworkInterfaceMapping, _Mapping]]] = ..., high_availability: bool = ..., scheduler_hints: _Optional[_Union[VMInstance.SchedulerHints, _Mapping]] = ..., tenant: _Optional[str] = ..., vnc_port: _Optional[int] = ..., migration_dst_host: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., state_progress: _Optional[float] = ..., total_storage: _Optional[int] = ..., start_timestamp: _Optional[int] = ..., stop_timestamp: _Optional[int] = ..., host: _Optional[str] = ..., state: _Optional[_Union[VMInstance.State, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "size_in_bytes", "virtual_size_in_bytes", "protected", "checksum", "firmware_type", "source_uri", "min_memory", "location", "container_format", "disk_format", "tenants", "creation_timestamp", "update_timestamp", "status", "errors")
    class ContainerFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BARE: _ClassVar[Image.ContainerFormat]
    BARE: Image.ContainerFormat
    class DiskFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAW: _ClassVar[Image.DiskFormat]
        QCOW2: _ClassVar[Image.DiskFormat]
        VMDK: _ClassVar[Image.DiskFormat]
        VDI: _ClassVar[Image.DiskFormat]
        VHDX: _ClassVar[Image.DiskFormat]
    RAW: Image.DiskFormat
    QCOW2: Image.DiskFormat
    VMDK: Image.DiskFormat
    VDI: Image.DiskFormat
    VHDX: Image.DiskFormat
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Image.Status]
        QUEUED: _ClassVar[Image.Status]
        SAVING: _ClassVar[Image.Status]
        ACTIVE: _ClassVar[Image.Status]
        KILLED: _ClassVar[Image.Status]
        DELETED: _ClassVar[Image.Status]
        PENDING_DELETE: _ClassVar[Image.Status]
        DEACTIVATED: _ClassVar[Image.Status]
        UPLOADING: _ClassVar[Image.Status]
        IMPORTING: _ClassVar[Image.Status]
    UNKNOWN: Image.Status
    QUEUED: Image.Status
    SAVING: Image.Status
    ACTIVE: Image.Status
    KILLED: Image.Status
    DELETED: Image.Status
    PENDING_DELETE: Image.Status
    DEACTIVATED: Image.Status
    UPLOADING: Image.Status
    IMPORTING: Image.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class StorageLocation(_message.Message):
        __slots__ = ("type", "view_name", "path")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ISCSI: _ClassVar[Image.StorageLocation.Type]
            NFS: _ClassVar[Image.StorageLocation.Type]
        ISCSI: Image.StorageLocation.Type
        NFS: Image.StorageLocation.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        type: Image.StorageLocation.Type
        view_name: str
        path: str
        def __init__(self, type: _Optional[_Union[Image.StorageLocation.Type, str]] = ..., view_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    MIN_MEMORY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    size_in_bytes: int
    virtual_size_in_bytes: int
    protected: bool
    checksum: str
    firmware_type: FirmwareType
    source_uri: str
    min_memory: int
    location: Image.StorageLocation
    container_format: Image.ContainerFormat
    disk_format: Image.DiskFormat
    tenants: _containers.RepeatedScalarFieldContainer[str]
    creation_timestamp: int
    update_timestamp: int
    status: Image.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., size_in_bytes: _Optional[int] = ..., virtual_size_in_bytes: _Optional[int] = ..., protected: bool = ..., checksum: _Optional[str] = ..., firmware_type: _Optional[_Union[FirmwareType, str]] = ..., source_uri: _Optional[str] = ..., min_memory: _Optional[int] = ..., location: _Optional[_Union[Image.StorageLocation, _Mapping]] = ..., container_format: _Optional[_Union[Image.ContainerFormat, str]] = ..., disk_format: _Optional[_Union[Image.DiskFormat, str]] = ..., tenants: _Optional[_Iterable[str]] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., status: _Optional[_Union[Image.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "size_in_bytes", "multi_attach_allowed", "source_type", "source_id", "bootable", "firmware_type", "min_memory", "location", "container_format", "disk_format", "delete_on_dettach", "qos", "tenant", "creation_timestamp", "update_timestamp", "attachments", "status", "errors", "checksum")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLANK: _ClassVar[Volume.SourceType]
        IMAGE: _ClassVar[Volume.SourceType]
        VOLUME: _ClassVar[Volume.SourceType]
    BLANK: Volume.SourceType
    IMAGE: Volume.SourceType
    VOLUME: Volume.SourceType
    class ContainerFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BARE: _ClassVar[Volume.ContainerFormat]
    BARE: Volume.ContainerFormat
    class DiskFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RAW: _ClassVar[Volume.DiskFormat]
        QCOW2: _ClassVar[Volume.DiskFormat]
        VMDK: _ClassVar[Volume.DiskFormat]
        VDI: _ClassVar[Volume.DiskFormat]
        VHDX: _ClassVar[Volume.DiskFormat]
    RAW: Volume.DiskFormat
    QCOW2: Volume.DiskFormat
    VMDK: Volume.DiskFormat
    VDI: Volume.DiskFormat
    VHDX: Volume.DiskFormat
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Volume.Status]
        CREATING: _ClassVar[Volume.Status]
        DELETING: _ClassVar[Volume.Status]
        CREATED: _ClassVar[Volume.Status]
        AVAILABLE: _ClassVar[Volume.Status]
        DELETED: _ClassVar[Volume.Status]
        IN_USE: _ClassVar[Volume.Status]
        CREATE_ERROR: _ClassVar[Volume.Status]
        DELETE_ERROR: _ClassVar[Volume.Status]
    UNKNOWN: Volume.Status
    CREATING: Volume.Status
    DELETING: Volume.Status
    CREATED: Volume.Status
    AVAILABLE: Volume.Status
    DELETED: Volume.Status
    IN_USE: Volume.Status
    CREATE_ERROR: Volume.Status
    DELETE_ERROR: Volume.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class StorageLocation(_message.Message):
        __slots__ = ("type", "view_name", "path")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ISCSI: _ClassVar[Volume.StorageLocation.Type]
        ISCSI: Volume.StorageLocation.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        type: Volume.StorageLocation.Type
        view_name: str
        path: str
        def __init__(self, type: _Optional[_Union[Volume.StorageLocation.Type, str]] = ..., view_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...
    class Attachment(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    MULTI_ATTACH_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_MEMORY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_DETTACH_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    size_in_bytes: int
    multi_attach_allowed: bool
    source_type: Volume.SourceType
    source_id: str
    bootable: bool
    firmware_type: FirmwareType
    min_memory: int
    location: Volume.StorageLocation
    container_format: Volume.ContainerFormat
    disk_format: Volume.DiskFormat
    delete_on_dettach: bool
    qos: str
    tenant: str
    creation_timestamp: int
    update_timestamp: int
    attachments: _containers.RepeatedCompositeFieldContainer[Volume.Attachment]
    status: Volume.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    checksum: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., size_in_bytes: _Optional[int] = ..., multi_attach_allowed: bool = ..., source_type: _Optional[_Union[Volume.SourceType, str]] = ..., source_id: _Optional[str] = ..., bootable: bool = ..., firmware_type: _Optional[_Union[FirmwareType, str]] = ..., min_memory: _Optional[int] = ..., location: _Optional[_Union[Volume.StorageLocation, _Mapping]] = ..., container_format: _Optional[_Union[Volume.ContainerFormat, str]] = ..., disk_format: _Optional[_Union[Volume.DiskFormat, str]] = ..., delete_on_dettach: bool = ..., qos: _Optional[str] = ..., tenant: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., attachments: _Optional[_Iterable[_Union[Volume.Attachment, _Mapping]]] = ..., status: _Optional[_Union[Volume.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ..., checksum: _Optional[str] = ...) -> None: ...

class StorageQoS(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "enforcement_type", "read_iops", "write_iops", "both_iops", "read_bps", "write_bps", "both_bps", "tenants", "creation_timestamp", "update_timestamp")
    class EnforcementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[StorageQoS.EnforcementType]
        SERVER: _ClassVar[StorageQoS.EnforcementType]
        CLIENT: _ClassVar[StorageQoS.EnforcementType]
        BOTH: _ClassVar[StorageQoS.EnforcementType]
    NONE: StorageQoS.EnforcementType
    SERVER: StorageQoS.EnforcementType
    CLIENT: StorageQoS.EnforcementType
    BOTH: StorageQoS.EnforcementType
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    READ_IOPS_FIELD_NUMBER: _ClassVar[int]
    WRITE_IOPS_FIELD_NUMBER: _ClassVar[int]
    BOTH_IOPS_FIELD_NUMBER: _ClassVar[int]
    READ_BPS_FIELD_NUMBER: _ClassVar[int]
    WRITE_BPS_FIELD_NUMBER: _ClassVar[int]
    BOTH_BPS_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    enforcement_type: StorageQoS.EnforcementType
    read_iops: int
    write_iops: int
    both_iops: int
    read_bps: int
    write_bps: int
    both_bps: int
    tenants: _containers.RepeatedScalarFieldContainer[str]
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., enforcement_type: _Optional[_Union[StorageQoS.EnforcementType, str]] = ..., read_iops: _Optional[int] = ..., write_iops: _Optional[int] = ..., both_iops: _Optional[int] = ..., read_bps: _Optional[int] = ..., write_bps: _Optional[int] = ..., both_bps: _Optional[int] = ..., tenants: _Optional[_Iterable[str]] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...

class Network(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "type", "provider", "subnets", "mtu", "tenants", "system_defined", "creation_timestamp", "update_timestamp", "status", "errors")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERNAL: _ClassVar[Network.Type]
        EXTERNAL: _ClassVar[Network.Type]
    INTERNAL: Network.Type
    EXTERNAL: Network.Type
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Network.Status]
        ACTIVE: _ClassVar[Network.Status]
        DOWN: _ClassVar[Network.Status]
        BUILD: _ClassVar[Network.Status]
        ERROR: _ClassVar[Network.Status]
    UNKNOWN: Network.Status
    ACTIVE: Network.Status
    DOWN: Network.Status
    BUILD: Network.Status
    ERROR: Network.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Provider(_message.Message):
        __slots__ = ("id", "physical_network", "segments")
        class Segment(_message.Message):
            __slots__ = ("type", "segmentation_id")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FLAT: _ClassVar[Network.Provider.Segment.Type]
                VLAN: _ClassVar[Network.Provider.Segment.Type]
                GRE: _ClassVar[Network.Provider.Segment.Type]
                VXLAN: _ClassVar[Network.Provider.Segment.Type]
                NVGRE: _ClassVar[Network.Provider.Segment.Type]
                STT: _ClassVar[Network.Provider.Segment.Type]
                GENEVE: _ClassVar[Network.Provider.Segment.Type]
            FLAT: Network.Provider.Segment.Type
            VLAN: Network.Provider.Segment.Type
            GRE: Network.Provider.Segment.Type
            VXLAN: Network.Provider.Segment.Type
            NVGRE: Network.Provider.Segment.Type
            STT: Network.Provider.Segment.Type
            GENEVE: Network.Provider.Segment.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            SEGMENTATION_ID_FIELD_NUMBER: _ClassVar[int]
            type: Network.Provider.Segment.Type
            segmentation_id: str
            def __init__(self, type: _Optional[_Union[Network.Provider.Segment.Type, str]] = ..., segmentation_id: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        id: str
        physical_network: str
        segments: _containers.RepeatedCompositeFieldContainer[Network.Provider.Segment]
        def __init__(self, id: _Optional[str] = ..., physical_network: _Optional[str] = ..., segments: _Optional[_Iterable[_Union[Network.Provider.Segment, _Mapping]]] = ...) -> None: ...
    class Subnet(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SUBNETS_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_DEFINED_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    type: Network.Type
    provider: Network.Provider
    subnets: _containers.RepeatedCompositeFieldContainer[Network.Subnet]
    mtu: int
    tenants: _containers.RepeatedScalarFieldContainer[str]
    system_defined: bool
    creation_timestamp: int
    update_timestamp: int
    status: Network.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., type: _Optional[_Union[Network.Type, str]] = ..., provider: _Optional[_Union[Network.Provider, _Mapping]] = ..., subnets: _Optional[_Iterable[_Union[Network.Subnet, _Mapping]]] = ..., mtu: _Optional[int] = ..., tenants: _Optional[_Iterable[str]] = ..., system_defined: bool = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., status: _Optional[_Union[Network.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "network", "type", "cidr", "address_pool", "dhcp", "creation_timestamp", "update_timestamp", "status", "errors")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IPV4: _ClassVar[Subnet.Type]
        IPV6: _ClassVar[Subnet.Type]
    IPV4: Subnet.Type
    IPV6: Subnet.Type
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Subnet.Status]
        ACTIVE: _ClassVar[Subnet.Status]
        DOWN: _ClassVar[Subnet.Status]
        BUILD: _ClassVar[Subnet.Status]
        ERROR: _ClassVar[Subnet.Status]
    UNKNOWN: Subnet.Status
    ACTIVE: Subnet.Status
    DOWN: Subnet.Status
    BUILD: Subnet.Status
    ERROR: Subnet.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Network(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class AddressPoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DHCPConfig(_message.Message):
        __slots__ = ("enabled", "server_ip", "allocation_ranges", "gateway_ip", "dns_nameservers", "extra_dhcp_opts")
        class AllocationRangesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class ExtraDhcpOptsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        ALLOCATION_RANGES_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
        DNS_NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
        EXTRA_DHCP_OPTS_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        server_ip: str
        allocation_ranges: _containers.ScalarMap[str, str]
        gateway_ip: str
        dns_nameservers: _containers.RepeatedScalarFieldContainer[str]
        extra_dhcp_opts: _containers.ScalarMap[str, str]
        def __init__(self, enabled: bool = ..., server_ip: _Optional[str] = ..., allocation_ranges: _Optional[_Mapping[str, str]] = ..., gateway_ip: _Optional[str] = ..., dns_nameservers: _Optional[_Iterable[str]] = ..., extra_dhcp_opts: _Optional[_Mapping[str, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_POOL_FIELD_NUMBER: _ClassVar[int]
    DHCP_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    network: Subnet.Network
    type: Subnet.Type
    cidr: str
    address_pool: _containers.ScalarMap[str, str]
    dhcp: Subnet.DHCPConfig
    creation_timestamp: int
    update_timestamp: int
    status: Subnet.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., network: _Optional[_Union[Subnet.Network, _Mapping]] = ..., type: _Optional[_Union[Subnet.Type, str]] = ..., cidr: _Optional[str] = ..., address_pool: _Optional[_Mapping[str, str]] = ..., dhcp: _Optional[_Union[Subnet.DHCPConfig, _Mapping]] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., status: _Optional[_Union[Subnet.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class Port(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "network", "mac_address", "fixed_ips", "security_groups", "admin_state_up", "extra_dhcp_opts", "port_security_enabled", "allowed_address_pairs", "delete_on_dettach", "tenant", "creation_timestamp", "update_timestamp", "status", "errors", "device_owner_type", "device_owner_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Port.Status]
        ACTIVE: _ClassVar[Port.Status]
        DOWN: _ClassVar[Port.Status]
        BUILD: _ClassVar[Port.Status]
        ERROR: _ClassVar[Port.Status]
    UNKNOWN: Port.Status
    ACTIVE: Port.Status
    DOWN: Port.Status
    BUILD: Port.Status
    ERROR: Port.Status
    class OwnerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VMInstance: _ClassVar[Port.OwnerType]
        Router: _ClassVar[Port.OwnerType]
        LoadBalencer: _ClassVar[Port.OwnerType]
    VMInstance: Port.OwnerType
    Router: Port.OwnerType
    LoadBalencer: Port.OwnerType
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Network(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class FixedIP(_message.Message):
        __slots__ = ("ip_address", "subnet")
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        ip_address: str
        subnet: str
        def __init__(self, ip_address: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...
    class SecurityGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class ExtraDhcpOptsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AddressPairs(_message.Message):
        __slots__ = ("ip_address", "mac_address")
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        ip_address: str
        mac_address: str
        def __init__(self, ip_address: _Optional[str] = ..., mac_address: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FIXED_IPS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_STATE_UP_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DHCP_OPTS_FIELD_NUMBER: _ClassVar[int]
    PORT_SECURITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ADDRESS_PAIRS_FIELD_NUMBER: _ClassVar[int]
    DELETE_ON_DETTACH_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_OWNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    network: Port.Network
    mac_address: str
    fixed_ips: _containers.RepeatedCompositeFieldContainer[Port.FixedIP]
    security_groups: _containers.RepeatedCompositeFieldContainer[Port.SecurityGroup]
    admin_state_up: bool
    extra_dhcp_opts: _containers.ScalarMap[str, str]
    port_security_enabled: bool
    allowed_address_pairs: _containers.RepeatedCompositeFieldContainer[Port.AddressPairs]
    delete_on_dettach: bool
    tenant: str
    creation_timestamp: int
    update_timestamp: int
    status: Port.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    device_owner_type: Port.OwnerType
    device_owner_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., network: _Optional[_Union[Port.Network, _Mapping]] = ..., mac_address: _Optional[str] = ..., fixed_ips: _Optional[_Iterable[_Union[Port.FixedIP, _Mapping]]] = ..., security_groups: _Optional[_Iterable[_Union[Port.SecurityGroup, _Mapping]]] = ..., admin_state_up: bool = ..., extra_dhcp_opts: _Optional[_Mapping[str, str]] = ..., port_security_enabled: bool = ..., allowed_address_pairs: _Optional[_Iterable[_Union[Port.AddressPairs, _Mapping]]] = ..., delete_on_dettach: bool = ..., tenant: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., status: _Optional[_Union[Port.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ..., device_owner_type: _Optional[_Union[Port.OwnerType, str]] = ..., device_owner_id: _Optional[str] = ...) -> None: ...

class NetworkQoS(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "rx_bps", "tx_bps", "both_bps", "tenants", "creation_timestamp", "update_timestamp")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RX_BPS_FIELD_NUMBER: _ClassVar[int]
    TX_BPS_FIELD_NUMBER: _ClassVar[int]
    BOTH_BPS_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    rx_bps: int
    tx_bps: int
    both_bps: int
    tenants: _containers.RepeatedScalarFieldContainer[str]
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., rx_bps: _Optional[int] = ..., tx_bps: _Optional[int] = ..., both_bps: _Optional[int] = ..., tenants: _Optional[_Iterable[str]] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...

class SecurityGroup(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "rules", "tenants", "creation_timestamp", "update_timestamp")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Rule(_message.Message):
        __slots__ = ("id", "direction", "remote_group_id", "ethertype", "protocol", "remote_cidr", "port_range_min", "port_range_max")
        class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INGRESS: _ClassVar[SecurityGroup.Rule.Direction]
            EGRESS: _ClassVar[SecurityGroup.Rule.Direction]
        INGRESS: SecurityGroup.Rule.Direction
        EGRESS: SecurityGroup.Rule.Direction
        class Ethertype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IPV4: _ClassVar[SecurityGroup.Rule.Ethertype]
            IPV6: _ClassVar[SecurityGroup.Rule.Ethertype]
        IPV4: SecurityGroup.Rule.Ethertype
        IPV6: SecurityGroup.Rule.Ethertype
        ID_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        REMOTE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ETHERTYPE_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        REMOTE_CIDR_FIELD_NUMBER: _ClassVar[int]
        PORT_RANGE_MIN_FIELD_NUMBER: _ClassVar[int]
        PORT_RANGE_MAX_FIELD_NUMBER: _ClassVar[int]
        id: str
        direction: SecurityGroup.Rule.Direction
        remote_group_id: str
        ethertype: SecurityGroup.Rule.Ethertype
        protocol: int
        remote_cidr: str
        port_range_min: int
        port_range_max: int
        def __init__(self, id: _Optional[str] = ..., direction: _Optional[_Union[SecurityGroup.Rule.Direction, str]] = ..., remote_group_id: _Optional[str] = ..., ethertype: _Optional[_Union[SecurityGroup.Rule.Ethertype, str]] = ..., protocol: _Optional[int] = ..., remote_cidr: _Optional[str] = ..., port_range_min: _Optional[int] = ..., port_range_max: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    rules: _containers.RepeatedCompositeFieldContainer[SecurityGroup.Rule]
    tenants: _containers.RepeatedScalarFieldContainer[str]
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., rules: _Optional[_Iterable[_Union[SecurityGroup.Rule, _Mapping]]] = ..., tenants: _Optional[_Iterable[str]] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...

class Router(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "external_gateway_info", "ports", "admin_state_up", "tenants", "creation_timestamp", "update_timestamp", "status", "errors")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Router.Status]
        ACTIVE: _ClassVar[Router.Status]
        DOWN: _ClassVar[Router.Status]
        ERROR: _ClassVar[Router.Status]
        PENDING: _ClassVar[Router.Status]
    UNKNOWN: Router.Status
    ACTIVE: Router.Status
    DOWN: Router.Status
    ERROR: Router.Status
    PENDING: Router.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ExternalGatewayInfo(_message.Message):
        __slots__ = ("network", "enable_snat", "external_fixed_ips", "replica_count", "host_metadata_selector")
        class FixedIPs(_message.Message):
            __slots__ = ("ip_address", "subnet")
            IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            SUBNET_FIELD_NUMBER: _ClassVar[int]
            ip_address: str
            subnet: str
            def __init__(self, ip_address: _Optional[str] = ..., subnet: _Optional[str] = ...) -> None: ...
        class HostMetadataSelectorEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SNAT_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_FIXED_IPS_FIELD_NUMBER: _ClassVar[int]
        REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        HOST_METADATA_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        network: str
        enable_snat: bool
        external_fixed_ips: _containers.RepeatedCompositeFieldContainer[Router.ExternalGatewayInfo.FixedIPs]
        replica_count: int
        host_metadata_selector: _containers.ScalarMap[str, str]
        def __init__(self, network: _Optional[str] = ..., enable_snat: bool = ..., external_fixed_ips: _Optional[_Iterable[_Union[Router.ExternalGatewayInfo.FixedIPs, _Mapping]]] = ..., replica_count: _Optional[int] = ..., host_metadata_selector: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class Port(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_GATEWAY_INFO_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_STATE_UP_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    external_gateway_info: Router.ExternalGatewayInfo
    ports: _containers.RepeatedCompositeFieldContainer[Router.Port]
    admin_state_up: bool
    tenants: _containers.RepeatedScalarFieldContainer[str]
    creation_timestamp: int
    update_timestamp: int
    status: Router.Status
    errors: _containers.RepeatedCompositeFieldContainer[Error]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., external_gateway_info: _Optional[_Union[Router.ExternalGatewayInfo, _Mapping]] = ..., ports: _Optional[_Iterable[_Union[Router.Port, _Mapping]]] = ..., admin_state_up: bool = ..., tenants: _Optional[_Iterable[str]] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ..., status: _Optional[_Union[Router.Status, str]] = ..., errors: _Optional[_Iterable[_Union[Error, _Mapping]]] = ...) -> None: ...

class LoadBalencer(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "port", "backend_ports", "tenant", "creation_timestamp", "update_timestamp")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Port(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class BackendPort(_message.Message):
        __slots__ = ("id", "score")
        ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        id: str
        score: int
        def __init__(self, id: _Optional[str] = ..., score: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    BACKEND_PORTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    port: _containers.RepeatedCompositeFieldContainer[LoadBalencer.Port]
    backend_ports: _containers.RepeatedCompositeFieldContainer[LoadBalencer.BackendPort]
    tenant: str
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., port: _Optional[_Iterable[_Union[LoadBalencer.Port, _Mapping]]] = ..., backend_ports: _Optional[_Iterable[_Union[LoadBalencer.BackendPort, _Mapping]]] = ..., tenant: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...

class FloatingIP(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "network", "type", "ip_address", "port", "tenant", "creation_timestamp", "update_timestamp")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IPV4: _ClassVar[FloatingIP.Type]
        IPV6: _ClassVar[FloatingIP.Type]
    IPV4: FloatingIP.Type
    IPV6: FloatingIP.Type
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Network(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    network: FloatingIP.Network
    type: FloatingIP.Type
    ip_address: str
    port: str
    tenant: str
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., network: _Optional[_Union[FloatingIP.Network, _Mapping]] = ..., type: _Optional[_Union[FloatingIP.Type, str]] = ..., ip_address: _Optional[str] = ..., port: _Optional[str] = ..., tenant: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...

class Secret(_message.Message):
    __slots__ = ("id", "name", "description", "metadata", "type", "data", "tenant", "creation_timestamp", "update_timestamp")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GPG_KEY: _ClassVar[Secret.Type]
    GPG_KEY: Secret.Type
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    type: Secret.Type
    data: bytes
    tenant: str
    creation_timestamp: int
    update_timestamp: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., type: _Optional[_Union[Secret.Type, str]] = ..., data: _Optional[bytes] = ..., tenant: _Optional[str] = ..., creation_timestamp: _Optional[int] = ..., update_timestamp: _Optional[int] = ...) -> None: ...
