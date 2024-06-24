from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorMessage(_message.Message):
    __slots__ = ("message", "reason")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    message: str
    reason: str
    def __init__(self, message: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("code", "message", "message_list", "kind", "api_version", "state")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    message_list: _containers.RepeatedCompositeFieldContainer[ErrorMessage]
    kind: str
    api_version: str
    state: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., message_list: _Optional[_Iterable[_Union[ErrorMessage, _Mapping]]] = ..., kind: _Optional[str] = ..., api_version: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class ListArg(_message.Message):
    __slots__ = ("kind", "api_version")
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str
    def __init__(self, kind: _Optional[str] = ..., api_version: _Optional[str] = ...) -> None: ...

class DeviceProperties(_message.Message):
    __slots__ = ("device_type", "disk_address")
    class DiskAddress(_message.Message):
        __slots__ = ("adapter_type", "device_index")
        ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
        adapter_type: str
        device_index: int
        def __init__(self, adapter_type: _Optional[str] = ..., device_index: _Optional[int] = ...) -> None: ...
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    device_type: str
    disk_address: DeviceProperties.DiskAddress
    def __init__(self, device_type: _Optional[str] = ..., disk_address: _Optional[_Union[DeviceProperties.DiskAddress, _Mapping]] = ...) -> None: ...

class Disk(_message.Message):
    __slots__ = ("device_properties", "disk_size_mib", "data_source_reference", "disk_size_bytes", "uuid")
    class Reference(_message.Message):
        __slots__ = ("kind", "name", "uuid")
        KIND_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        kind: str
        name: str
        uuid: str
        def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...
    DEVICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_MIB_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    device_properties: DeviceProperties
    disk_size_mib: int
    data_source_reference: Disk.Reference
    disk_size_bytes: int
    uuid: str
    def __init__(self, device_properties: _Optional[_Union[DeviceProperties, _Mapping]] = ..., disk_size_mib: _Optional[int] = ..., data_source_reference: _Optional[_Union[Disk.Reference, _Mapping]] = ..., disk_size_bytes: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...

class HostReference(_message.Message):
    __slots__ = ("kind", "uuid")
    KIND_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    kind: str
    uuid: str
    def __init__(self, kind: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class VMNic(_message.Message):
    __slots__ = ("nic_type", "mac_address")
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    nic_type: str
    mac_address: str
    def __init__(self, nic_type: _Optional[str] = ..., mac_address: _Optional[str] = ...) -> None: ...

class VMResources(_message.Message):
    __slots__ = ("disk_list", "memory_size_mib", "hypervisor_type", "host_reference", "num_sockets", "num_vcpus_per_socket", "nic_list", "guest_tools")
    DISK_LIST_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_MIB_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    NUM_SOCKETS_FIELD_NUMBER: _ClassVar[int]
    NUM_VCPUS_PER_SOCKET_FIELD_NUMBER: _ClassVar[int]
    NIC_LIST_FIELD_NUMBER: _ClassVar[int]
    GUEST_TOOLS_FIELD_NUMBER: _ClassVar[int]
    disk_list: _containers.RepeatedCompositeFieldContainer[Disk]
    memory_size_mib: int
    hypervisor_type: str
    host_reference: HostReference
    num_sockets: int
    num_vcpus_per_socket: int
    nic_list: _containers.RepeatedCompositeFieldContainer[VMNic]
    guest_tools: GuestToolsInfo
    def __init__(self, disk_list: _Optional[_Iterable[_Union[Disk, _Mapping]]] = ..., memory_size_mib: _Optional[int] = ..., hypervisor_type: _Optional[str] = ..., host_reference: _Optional[_Union[HostReference, _Mapping]] = ..., num_sockets: _Optional[int] = ..., num_vcpus_per_socket: _Optional[int] = ..., nic_list: _Optional[_Iterable[_Union[VMNic, _Mapping]]] = ..., guest_tools: _Optional[_Union[GuestToolsInfo, _Mapping]] = ...) -> None: ...

class VMStatus(_message.Message):
    __slots__ = ("state", "name", "resources", "message_list")
    STATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    state: str
    name: str
    resources: VMResources
    message_list: _containers.RepeatedCompositeFieldContainer[ErrorMessage]
    def __init__(self, state: _Optional[str] = ..., name: _Optional[str] = ..., resources: _Optional[_Union[VMResources, _Mapping]] = ..., message_list: _Optional[_Iterable[_Union[ErrorMessage, _Mapping]]] = ...) -> None: ...

class EntityMetadata(_message.Message):
    __slots__ = ("uuid", "name", "kind", "entity_version", "spec_version")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPEC_VERSION_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    kind: str
    entity_version: int
    spec_version: int
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ..., entity_version: _Optional[int] = ..., spec_version: _Optional[int] = ...) -> None: ...

class GuestToolsInfo(_message.Message):
    __slots__ = ("nutanix_guest_tools",)
    class NGTInfo(_message.Message):
        __slots__ = ("available_version", "ngt_state", "iso_mount_state", "state", "version", "enabled_capability_list", "guest_os_version", "is_reachable")
        AVAILABLE_VERSION_FIELD_NUMBER: _ClassVar[int]
        NGT_STATE_FIELD_NUMBER: _ClassVar[int]
        ISO_MOUNT_STATE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ENABLED_CAPABILITY_LIST_FIELD_NUMBER: _ClassVar[int]
        GUEST_OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_REACHABLE_FIELD_NUMBER: _ClassVar[int]
        available_version: str
        ngt_state: str
        iso_mount_state: str
        state: str
        version: str
        enabled_capability_list: _containers.RepeatedScalarFieldContainer[str]
        guest_os_version: str
        is_reachable: bool
        def __init__(self, available_version: _Optional[str] = ..., ngt_state: _Optional[str] = ..., iso_mount_state: _Optional[str] = ..., state: _Optional[str] = ..., version: _Optional[str] = ..., enabled_capability_list: _Optional[_Iterable[str]] = ..., guest_os_version: _Optional[str] = ..., is_reachable: bool = ...) -> None: ...
    NUTANIX_GUEST_TOOLS_FIELD_NUMBER: _ClassVar[int]
    nutanix_guest_tools: GuestToolsInfo.NGTInfo
    def __init__(self, nutanix_guest_tools: _Optional[_Union[GuestToolsInfo.NGTInfo, _Mapping]] = ...) -> None: ...

class VMEntity(_message.Message):
    __slots__ = ("metadata", "status")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    metadata: EntityMetadata
    status: VMStatus
    def __init__(self, metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[VMStatus, _Mapping]] = ...) -> None: ...

class ListMetadata(_message.Message):
    __slots__ = ("total_matches", "kind", "length", "offset")
    TOTAL_MATCHES_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    total_matches: int
    kind: str
    length: int
    offset: int
    def __init__(self, total_matches: _Optional[int] = ..., kind: _Optional[str] = ..., length: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class VMListArg(_message.Message):
    __slots__ = ("filter", "kind", "sort_order", "offset", "length", "sort_attribute")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SORT_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    filter: str
    kind: str
    sort_order: str
    offset: int
    length: int
    sort_attribute: str
    def __init__(self, filter: _Optional[str] = ..., kind: _Optional[str] = ..., sort_order: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., sort_attribute: _Optional[str] = ...) -> None: ...

class VMListResult(_message.Message):
    __slots__ = ("api_version", "metadata", "entities")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: ListMetadata
    entities: _containers.RepeatedCompositeFieldContainer[VMEntity]
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[VMEntity, _Mapping]]] = ...) -> None: ...

class VMInfoResult(_message.Message):
    __slots__ = ("api_version", "metadata", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    status: VMStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[VMStatus, _Mapping]] = ...) -> None: ...

class SnapshotSourceResource(_message.Message):
    __slots__ = ("entity_uuid",)
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    entity_uuid: str
    def __init__(self, entity_uuid: _Optional[str] = ...) -> None: ...

class SnapshotFile(_message.Message):
    __slots__ = ("file_path", "snapshot_file_path")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    snapshot_file_path: str
    def __init__(self, file_path: _Optional[str] = ..., snapshot_file_path: _Optional[str] = ...) -> None: ...

class SnapshotStatus(_message.Message):
    __slots__ = ("name", "state", "snapshot_type", "expiration_time_msecs", "resources", "snapshot_file_list")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: str
    snapshot_type: str
    expiration_time_msecs: int
    resources: SnapshotSourceResource
    snapshot_file_list: _containers.RepeatedCompositeFieldContainer[SnapshotFile]
    def __init__(self, name: _Optional[str] = ..., state: _Optional[str] = ..., snapshot_type: _Optional[str] = ..., expiration_time_msecs: _Optional[int] = ..., resources: _Optional[_Union[SnapshotSourceResource, _Mapping]] = ..., snapshot_file_list: _Optional[_Iterable[_Union[SnapshotFile, _Mapping]]] = ...) -> None: ...

class SnapshotInfoResult(_message.Message):
    __slots__ = ("api_version", "metadata", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    status: SnapshotStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[SnapshotStatus, _Mapping]] = ...) -> None: ...

class CreateSnapshotArg(_message.Message):
    __slots__ = ("api_version", "metadata", "spec")
    class Specification(_message.Message):
        __slots__ = ("name", "snapshot_type", "expiration_time_msecs", "resources")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        name: str
        snapshot_type: str
        expiration_time_msecs: int
        resources: SnapshotSourceResource
        def __init__(self, name: _Optional[str] = ..., snapshot_type: _Optional[str] = ..., expiration_time_msecs: _Optional[int] = ..., resources: _Optional[_Union[SnapshotSourceResource, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    spec: CreateSnapshotArg.Specification
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., spec: _Optional[_Union[CreateSnapshotArg.Specification, _Mapping]] = ...) -> None: ...

class CreateSnapshotResult(_message.Message):
    __slots__ = ("api_version", "metadata", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    status: SnapshotStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[SnapshotStatus, _Mapping]] = ...) -> None: ...

class ExternalRepoResource(_message.Message):
    __slots__ = ("nfs_configuration",)
    class NfsConfiguration(_message.Message):
        __slots__ = ("access_mode", "exported_directory", "server_address_list")
        class ServerAddress(_message.Message):
            __slots__ = ("ip",)
            IP_FIELD_NUMBER: _ClassVar[int]
            ip: str
            def __init__(self, ip: _Optional[str] = ...) -> None: ...
        ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
        EXPORTED_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        SERVER_ADDRESS_LIST_FIELD_NUMBER: _ClassVar[int]
        access_mode: str
        exported_directory: str
        server_address_list: _containers.RepeatedCompositeFieldContainer[ExternalRepoResource.NfsConfiguration.ServerAddress]
        def __init__(self, access_mode: _Optional[str] = ..., exported_directory: _Optional[str] = ..., server_address_list: _Optional[_Iterable[_Union[ExternalRepoResource.NfsConfiguration.ServerAddress, _Mapping]]] = ...) -> None: ...
    NFS_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    nfs_configuration: ExternalRepoResource.NfsConfiguration
    def __init__(self, nfs_configuration: _Optional[_Union[ExternalRepoResource.NfsConfiguration, _Mapping]] = ...) -> None: ...

class ExternalRepoStatus(_message.Message):
    __slots__ = ("name", "state", "resources")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: str
    resources: ExternalRepoResource
    def __init__(self, name: _Optional[str] = ..., state: _Optional[str] = ..., resources: _Optional[_Union[ExternalRepoResource, _Mapping]] = ...) -> None: ...

class CreateExternalRepoArg(_message.Message):
    __slots__ = ("spec", "metadata")
    class Specification(_message.Message):
        __slots__ = ("name", "resources")
        NAME_FIELD_NUMBER: _ClassVar[int]
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        name: str
        resources: ExternalRepoResource
        def __init__(self, name: _Optional[str] = ..., resources: _Optional[_Union[ExternalRepoResource, _Mapping]] = ...) -> None: ...
    SPEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    spec: CreateExternalRepoArg.Specification
    metadata: EntityMetadata
    def __init__(self, spec: _Optional[_Union[CreateExternalRepoArg.Specification, _Mapping]] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ...) -> None: ...

class CreateExternalRepoResult(_message.Message):
    __slots__ = ("api_version", "metadata", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    status: ExternalRepoStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[ExternalRepoStatus, _Mapping]] = ...) -> None: ...

class ExternalRepoInfoResult(_message.Message):
    __slots__ = ("api_version", "metadata", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    status: ExternalRepoStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[ExternalRepoStatus, _Mapping]] = ...) -> None: ...

class CreateIdempotenceIdentifierArg(_message.Message):
    __slots__ = ("client_identifier", "count")
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    client_identifier: str
    count: int
    def __init__(self, client_identifier: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CreateIdempotenceIdentifierResult(_message.Message):
    __slots__ = ("client_identifier", "count", "uuid_vec")
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    client_identifier: str
    count: int
    uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_identifier: _Optional[str] = ..., count: _Optional[int] = ..., uuid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ChangeRegionArg(_message.Message):
    __slots__ = ("end_offset", "snapshot_file_path", "start_offset", "reference_snapshot_file_path")
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SNAPSHOT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    end_offset: int
    snapshot_file_path: str
    start_offset: int
    reference_snapshot_file_path: str
    def __init__(self, end_offset: _Optional[int] = ..., snapshot_file_path: _Optional[str] = ..., start_offset: _Optional[int] = ..., reference_snapshot_file_path: _Optional[str] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ("length", "type", "offset")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    type: str
    offset: int
    def __init__(self, length: _Optional[int] = ..., type: _Optional[str] = ..., offset: _Optional[int] = ...) -> None: ...

class ChangeRegionResult(_message.Message):
    __slots__ = ("region_list", "file_size", "next_offset")
    REGION_LIST_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    region_list: _containers.RepeatedCompositeFieldContainer[Region]
    file_size: int
    next_offset: int
    def __init__(self, region_list: _Optional[_Iterable[_Union[Region, _Mapping]]] = ..., file_size: _Optional[int] = ..., next_offset: _Optional[int] = ...) -> None: ...

class ClusterConfigMetadata(_message.Message):
    __slots__ = ("uuid", "name", "kind")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    kind: str
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class ClusterSpec(_message.Message):
    __slots__ = ("name", "resources")
    class Resources(_message.Message):
        __slots__ = ("network",)
        class Network(_message.Message):
            __slots__ = ("external_ip", "external_data_services_ip")
            EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
            EXTERNAL_DATA_SERVICES_IP_FIELD_NUMBER: _ClassVar[int]
            external_ip: str
            external_data_services_ip: str
            def __init__(self, external_ip: _Optional[str] = ..., external_data_services_ip: _Optional[str] = ...) -> None: ...
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        network: ClusterSpec.Resources.Network
        def __init__(self, network: _Optional[_Union[ClusterSpec.Resources.Network, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    resources: ClusterSpec.Resources
    def __init__(self, name: _Optional[str] = ..., resources: _Optional[_Union[ClusterSpec.Resources, _Mapping]] = ...) -> None: ...

class ClusterStatus(_message.Message):
    __slots__ = ("state", "resources", "name")
    class Resources(_message.Message):
        __slots__ = ("config", "nodes")
        class Config(_message.Message):
            __slots__ = ("build",)
            class Build(_message.Message):
                __slots__ = ("version", "full_version", "is_long_term_support")
                VERSION_FIELD_NUMBER: _ClassVar[int]
                FULL_VERSION_FIELD_NUMBER: _ClassVar[int]
                IS_LONG_TERM_SUPPORT_FIELD_NUMBER: _ClassVar[int]
                version: str
                full_version: str
                is_long_term_support: bool
                def __init__(self, version: _Optional[str] = ..., full_version: _Optional[str] = ..., is_long_term_support: bool = ...) -> None: ...
            BUILD_FIELD_NUMBER: _ClassVar[int]
            build: ClusterStatus.Resources.Config.Build
            def __init__(self, build: _Optional[_Union[ClusterStatus.Resources.Config.Build, _Mapping]] = ...) -> None: ...
        class Nodes(_message.Message):
            __slots__ = ("hypervisor_server_list",)
            class HypervisorServerInfo(_message.Message):
                __slots__ = ("ip", "version", "type")
                IP_FIELD_NUMBER: _ClassVar[int]
                VERSION_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                ip: str
                version: str
                type: str
                def __init__(self, ip: _Optional[str] = ..., version: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
            HYPERVISOR_SERVER_LIST_FIELD_NUMBER: _ClassVar[int]
            hypervisor_server_list: _containers.RepeatedCompositeFieldContainer[ClusterStatus.Resources.Nodes.HypervisorServerInfo]
            def __init__(self, hypervisor_server_list: _Optional[_Iterable[_Union[ClusterStatus.Resources.Nodes.HypervisorServerInfo, _Mapping]]] = ...) -> None: ...
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        NODES_FIELD_NUMBER: _ClassVar[int]
        config: ClusterStatus.Resources.Config
        nodes: ClusterStatus.Resources.Nodes
        def __init__(self, config: _Optional[_Union[ClusterStatus.Resources.Config, _Mapping]] = ..., nodes: _Optional[_Union[ClusterStatus.Resources.Nodes, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    state: str
    resources: ClusterStatus.Resources
    name: str
    def __init__(self, state: _Optional[str] = ..., resources: _Optional[_Union[ClusterStatus.Resources, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class ClusterConfig(_message.Message):
    __slots__ = ("api_version", "metadata", "spec", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: ClusterConfigMetadata
    spec: ClusterSpec
    status: ClusterStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[ClusterConfigMetadata, _Mapping]] = ..., spec: _Optional[_Union[ClusterSpec, _Mapping]] = ..., status: _Optional[_Union[ClusterStatus, _Mapping]] = ...) -> None: ...

class SubnetEntity(_message.Message):
    __slots__ = ("status", "metadata", "spec")
    class Status(_message.Message):
        __slots__ = ("state", "name", "message_list")
        STATE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        state: str
        name: str
        message_list: _containers.RepeatedCompositeFieldContainer[ErrorMessage]
        def __init__(self, state: _Optional[str] = ..., name: _Optional[str] = ..., message_list: _Optional[_Iterable[_Union[ErrorMessage, _Mapping]]] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("uuid",)
        UUID_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        def __init__(self, uuid: _Optional[str] = ...) -> None: ...
    class Spec(_message.Message):
        __slots__ = ("resources",)
        class Resources(_message.Message):
            __slots__ = ("ip_config",)
            class IPConfig(_message.Message):
                __slots__ = ("default_gateway", "subnet_ip")
                DEFAULT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
                SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
                default_gateway: str
                subnet_ip: str
                def __init__(self, default_gateway: _Optional[str] = ..., subnet_ip: _Optional[str] = ...) -> None: ...
            IP_CONFIG_FIELD_NUMBER: _ClassVar[int]
            ip_config: SubnetEntity.Spec.Resources.IPConfig
            def __init__(self, ip_config: _Optional[_Union[SubnetEntity.Spec.Resources.IPConfig, _Mapping]] = ...) -> None: ...
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        resources: SubnetEntity.Spec.Resources
        def __init__(self, resources: _Optional[_Union[SubnetEntity.Spec.Resources, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    status: SubnetEntity.Status
    metadata: SubnetEntity.Metadata
    spec: SubnetEntity.Spec
    def __init__(self, status: _Optional[_Union[SubnetEntity.Status, _Mapping]] = ..., metadata: _Optional[_Union[SubnetEntity.Metadata, _Mapping]] = ..., spec: _Optional[_Union[SubnetEntity.Spec, _Mapping]] = ...) -> None: ...

class NetworkListResult(_message.Message):
    __slots__ = ("api_version", "entities", "metadata")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    entities: _containers.RepeatedCompositeFieldContainer[SubnetEntity]
    metadata: ListMetadata
    def __init__(self, api_version: _Optional[str] = ..., entities: _Optional[_Iterable[_Union[SubnetEntity, _Mapping]]] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ...) -> None: ...

class ExternalRepoListArg(_message.Message):
    __slots__ = ("kind",)
    KIND_FIELD_NUMBER: _ClassVar[int]
    kind: str
    def __init__(self, kind: _Optional[str] = ...) -> None: ...

class ExternalRepoListResult(_message.Message):
    __slots__ = ("api_version", "metadata")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: ListMetadata
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ...) -> None: ...

class DeleteExternalRepoResult(_message.Message):
    __slots__ = ("status",)
    class Status(_message.Message):
        __slots__ = ("execution_context",)
        class ExecutionContext(_message.Message):
            __slots__ = ("task_uuid",)
            TASK_UUID_FIELD_NUMBER: _ClassVar[int]
            task_uuid: str
            def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...
        EXECUTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        execution_context: DeleteExternalRepoResult.Status.ExecutionContext
        def __init__(self, execution_context: _Optional[_Union[DeleteExternalRepoResult.Status.ExecutionContext, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: DeleteExternalRepoResult.Status
    def __init__(self, status: _Optional[_Union[DeleteExternalRepoResult.Status, _Mapping]] = ...) -> None: ...

class BackgroundMigrationPolicy(_message.Message):
    __slots__ = ("background_migration_suspended", "background_migration_enabled")
    BACKGROUND_MIGRATION_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MIGRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    background_migration_suspended: bool
    background_migration_enabled: bool
    def __init__(self, background_migration_suspended: bool = ..., background_migration_enabled: bool = ...) -> None: ...

class DatasourceResource(_message.Message):
    __slots__ = ("external_repository_uuid", "datasource_url", "container_uuid", "datasource_size", "task_uuid", "storage_migration_policy", "datasource_usage_mode")
    class StorageMigrationPolicy(_message.Message):
        __slots__ = ("background_migration_policy",)
        BACKGROUND_MIGRATION_POLICY_FIELD_NUMBER: _ClassVar[int]
        background_migration_policy: BackgroundMigrationPolicy
        def __init__(self, background_migration_policy: _Optional[_Union[BackgroundMigrationPolicy, _Mapping]] = ...) -> None: ...
    EXTERNAL_REPOSITORY_UUID_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_MIGRATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_USAGE_MODE_FIELD_NUMBER: _ClassVar[int]
    external_repository_uuid: str
    datasource_url: str
    container_uuid: str
    datasource_size: int
    task_uuid: str
    storage_migration_policy: DatasourceResource.StorageMigrationPolicy
    datasource_usage_mode: str
    def __init__(self, external_repository_uuid: _Optional[str] = ..., datasource_url: _Optional[str] = ..., container_uuid: _Optional[str] = ..., datasource_size: _Optional[int] = ..., task_uuid: _Optional[str] = ..., storage_migration_policy: _Optional[_Union[DatasourceResource.StorageMigrationPolicy, _Mapping]] = ..., datasource_usage_mode: _Optional[str] = ...) -> None: ...

class DatasourceStatus(_message.Message):
    __slots__ = ("state", "resources")
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    state: str
    resources: DatasourceResource
    def __init__(self, state: _Optional[str] = ..., resources: _Optional[_Union[DatasourceResource, _Mapping]] = ...) -> None: ...

class GetDatasourceInfoResult(_message.Message):
    __slots__ = ("api_version", "metadata", "status")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: EntityMetadata
    status: DatasourceStatus
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[EntityMetadata, _Mapping]] = ..., status: _Optional[_Union[DatasourceStatus, _Mapping]] = ...) -> None: ...

class StorageConfigMetadata(_message.Message):
    __slots__ = ("uuid", "spec_version", "kind")
    UUID_FIELD_NUMBER: _ClassVar[int]
    SPEC_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    spec_version: int
    kind: str
    def __init__(self, uuid: _Optional[str] = ..., spec_version: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class ConfigureStorageMigrationArg(_message.Message):
    __slots__ = ("api_version", "metadata", "spec")
    class Specification(_message.Message):
        __slots__ = ("resources",)
        class Resources(_message.Message):
            __slots__ = ("background_migration_policy",)
            BACKGROUND_MIGRATION_POLICY_FIELD_NUMBER: _ClassVar[int]
            background_migration_policy: BackgroundMigrationPolicy
            def __init__(self, background_migration_policy: _Optional[_Union[BackgroundMigrationPolicy, _Mapping]] = ...) -> None: ...
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        resources: ConfigureStorageMigrationArg.Specification.Resources
        def __init__(self, resources: _Optional[_Union[ConfigureStorageMigrationArg.Specification.Resources, _Mapping]] = ...) -> None: ...
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    api_version: str
    metadata: StorageConfigMetadata
    spec: ConfigureStorageMigrationArg.Specification
    def __init__(self, api_version: _Optional[str] = ..., metadata: _Optional[_Union[StorageConfigMetadata, _Mapping]] = ..., spec: _Optional[_Union[ConfigureStorageMigrationArg.Specification, _Mapping]] = ...) -> None: ...

class ConfigureStorageMigrationResult(_message.Message):
    __slots__ = ("status", "spec", "api_version", "metadata")
    class ConfigureStorageMigrationStatus(_message.Message):
        __slots__ = ("state",)
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: str
        def __init__(self, state: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    status: ConfigureStorageMigrationResult.ConfigureStorageMigrationStatus
    spec: ConfigureStorageMigrationArg.Specification
    api_version: str
    metadata: StorageConfigMetadata
    def __init__(self, status: _Optional[_Union[ConfigureStorageMigrationResult.ConfigureStorageMigrationStatus, _Mapping]] = ..., spec: _Optional[_Union[ConfigureStorageMigrationArg.Specification, _Mapping]] = ..., api_version: _Optional[str] = ..., metadata: _Optional[_Union[StorageConfigMetadata, _Mapping]] = ...) -> None: ...

class WaitForTaskFinishArg(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class WaitForTaskFinishResult(_message.Message):
    __slots__ = ("status", "entity_reference_list", "start_time_usecs", "creation_time_usecs", "completion_time_usecs", "progress_message", "percentage_complete", "api_version", "task_uuid", "logical_timestamp", "error_detail", "error_code")
    class EntityReference(_message.Message):
        __slots__ = ("kind", "uuid")
        KIND_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        kind: str
        uuid: str
        def __init__(self, kind: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_REFERENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    status: str
    entity_reference_list: _containers.RepeatedCompositeFieldContainer[WaitForTaskFinishResult.EntityReference]
    start_time_usecs: int
    creation_time_usecs: int
    completion_time_usecs: int
    progress_message: str
    percentage_complete: int
    api_version: str
    task_uuid: str
    logical_timestamp: int
    error_detail: str
    error_code: str
    def __init__(self, status: _Optional[str] = ..., entity_reference_list: _Optional[_Iterable[_Union[WaitForTaskFinishResult.EntityReference, _Mapping]]] = ..., start_time_usecs: _Optional[int] = ..., creation_time_usecs: _Optional[int] = ..., completion_time_usecs: _Optional[int] = ..., progress_message: _Optional[str] = ..., percentage_complete: _Optional[int] = ..., api_version: _Optional[str] = ..., task_uuid: _Optional[str] = ..., logical_timestamp: _Optional[int] = ..., error_detail: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
