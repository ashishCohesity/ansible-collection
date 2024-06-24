from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base.entities import agent_pb2 as _agent_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VMwareToolsVersionStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsCurrent: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsNeedUpgrade: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsNotInstalled: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsUnmanaged: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsBlacklisted: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsSupportedNew: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsSupportedOld: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsTooNew: _ClassVar[VMwareToolsVersionStatus.Type]
        kGuestToolsTooOld: _ClassVar[VMwareToolsVersionStatus.Type]
    kUnknown: VMwareToolsVersionStatus.Type
    kGuestToolsCurrent: VMwareToolsVersionStatus.Type
    kGuestToolsNeedUpgrade: VMwareToolsVersionStatus.Type
    kGuestToolsNotInstalled: VMwareToolsVersionStatus.Type
    kGuestToolsUnmanaged: VMwareToolsVersionStatus.Type
    kGuestToolsBlacklisted: VMwareToolsVersionStatus.Type
    kGuestToolsSupportedNew: VMwareToolsVersionStatus.Type
    kGuestToolsSupportedOld: VMwareToolsVersionStatus.Type
    kGuestToolsTooNew: VMwareToolsVersionStatus.Type
    kGuestToolsTooOld: VMwareToolsVersionStatus.Type
    def __init__(self) -> None: ...

class VMwareToolsRunningStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[VMwareToolsRunningStatus.Type]
        kGuestToolsExecutingScripts: _ClassVar[VMwareToolsRunningStatus.Type]
        kGuestToolsNotRunning: _ClassVar[VMwareToolsRunningStatus.Type]
        kGuestToolsRunning: _ClassVar[VMwareToolsRunningStatus.Type]
    kUnknown: VMwareToolsRunningStatus.Type
    kGuestToolsExecutingScripts: VMwareToolsRunningStatus.Type
    kGuestToolsNotRunning: VMwareToolsRunningStatus.Type
    kGuestToolsRunning: VMwareToolsRunningStatus.Type
    def __init__(self) -> None: ...

class VirtualDiskMode(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[VirtualDiskMode.Type]
        kAppend: _ClassVar[VirtualDiskMode.Type]
        kNonPersistent: _ClassVar[VirtualDiskMode.Type]
        kPersistent: _ClassVar[VirtualDiskMode.Type]
        kIndependentNonPersistent: _ClassVar[VirtualDiskMode.Type]
        kIndependentPersistent: _ClassVar[VirtualDiskMode.Type]
        kUndoable: _ClassVar[VirtualDiskMode.Type]
    kUnknown: VirtualDiskMode.Type
    kAppend: VirtualDiskMode.Type
    kNonPersistent: VirtualDiskMode.Type
    kPersistent: VirtualDiskMode.Type
    kIndependentNonPersistent: VirtualDiskMode.Type
    kIndependentPersistent: VirtualDiskMode.Type
    kUndoable: VirtualDiskMode.Type
    def __init__(self) -> None: ...

class FolderType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[FolderType.Type]
        kVMFolder: _ClassVar[FolderType.Type]
        kHostFolder: _ClassVar[FolderType.Type]
        kDatastoreFolder: _ClassVar[FolderType.Type]
        kNetworkFolder: _ClassVar[FolderType.Type]
        kRootFolder: _ClassVar[FolderType.Type]
    kUnknown: FolderType.Type
    kVMFolder: FolderType.Type
    kHostFolder: FolderType.Type
    kDatastoreFolder: FolderType.Type
    kNetworkFolder: FolderType.Type
    kRootFolder: FolderType.Type
    def __init__(self) -> None: ...

class TagAttributes(_message.Message):
    __slots__ = ("entity_id", "uuid", "name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    uuid: str
    name: str
    def __init__(self, entity_id: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CustomAttribute(_message.Message):
    __slots__ = ("name", "value", "type", "key")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    type: str
    key: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ..., key: _Optional[int] = ...) -> None: ...

class VirtualDiskInfo(_message.Message):
    __slots__ = ("unit_number", "controller_bus_number", "file_name", "controller_type", "logical_size_bytes", "uuid")
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    unit_number: int
    controller_bus_number: int
    file_name: str
    controller_type: str
    logical_size_bytes: int
    uuid: str
    def __init__(self, unit_number: _Optional[int] = ..., controller_bus_number: _Optional[int] = ..., file_name: _Optional[str] = ..., controller_type: _Optional[str] = ..., logical_size_bytes: _Optional[int] = ..., uuid: _Optional[str] = ...) -> None: ...

class DatastoreInfo(_message.Message):
    __slots__ = ("capacity", "free_space", "datacenter_name", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHealthy: _ClassVar[DatastoreInfo.Status]
        kUnHealthy: _ClassVar[DatastoreInfo.Status]
    kHealthy: DatastoreInfo.Status
    kUnHealthy: DatastoreInfo.Status
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FREE_SPACE_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    capacity: int
    free_space: int
    datacenter_name: str
    status: DatastoreInfo.Status
    def __init__(self, capacity: _Optional[int] = ..., free_space: _Optional[int] = ..., datacenter_name: _Optional[str] = ..., status: _Optional[_Union[DatastoreInfo.Status, str]] = ...) -> None: ...

class VCDAttributes(_message.Message):
    __slots__ = ("vcd_uuid", "vcenter_id", "vcenter_name", "resource_pool_moref", "resgrp_entity_id", "vcenter_endpoint", "is_vapp_auto_generated", "is_standalone_vm", "provider_vdc_uuid", "provider_vdc_name", "parent_vdc_uuid", "storage_profile_uuid", "vcd_resource_pool_moref", "is_vapp_template", "catalog_id", "catalog_item_uuid")
    VCD_UUID_FIELD_NUMBER: _ClassVar[int]
    VCENTER_ID_FIELD_NUMBER: _ClassVar[int]
    VCENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    RESGRP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VCENTER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    IS_VAPP_AUTO_GENERATED_FIELD_NUMBER: _ClassVar[int]
    IS_STANDALONE_VM_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VDC_UUID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VDC_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_VDC_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_UUID_FIELD_NUMBER: _ClassVar[int]
    VCD_RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    IS_VAPP_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    vcd_uuid: str
    vcenter_id: str
    vcenter_name: str
    resource_pool_moref: str
    resgrp_entity_id: int
    vcenter_endpoint: str
    is_vapp_auto_generated: bool
    is_standalone_vm: bool
    provider_vdc_uuid: str
    provider_vdc_name: str
    parent_vdc_uuid: str
    storage_profile_uuid: str
    vcd_resource_pool_moref: _vmware_common_pb2.MORef
    is_vapp_template: bool
    catalog_id: str
    catalog_item_uuid: str
    def __init__(self, vcd_uuid: _Optional[str] = ..., vcenter_id: _Optional[str] = ..., vcenter_name: _Optional[str] = ..., resource_pool_moref: _Optional[str] = ..., resgrp_entity_id: _Optional[int] = ..., vcenter_endpoint: _Optional[str] = ..., is_vapp_auto_generated: bool = ..., is_standalone_vm: bool = ..., provider_vdc_uuid: _Optional[str] = ..., provider_vdc_name: _Optional[str] = ..., parent_vdc_uuid: _Optional[str] = ..., storage_profile_uuid: _Optional[str] = ..., vcd_resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., is_vapp_template: bool = ..., catalog_id: _Optional[str] = ..., catalog_item_uuid: _Optional[str] = ...) -> None: ...

class StorageProfile(_message.Message):
    __slots__ = ("vcd_uuid", "name", "is_default")
    VCD_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    vcd_uuid: str
    name: str
    is_default: bool
    def __init__(self, vcd_uuid: _Optional[str] = ..., name: _Optional[str] = ..., is_default: bool = ...) -> None: ...

class VCDCatalog(_message.Message):
    __slots__ = ("vcd_uuid", "name")
    VCD_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    vcd_uuid: str
    name: str
    def __init__(self, vcd_uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class VMLinkingInfo(_message.Message):
    __slots__ = ("is_migrated", "previous_vm_parent_source_id", "previous_vm_entity_id", "migrated_time_usecs")
    IS_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VM_PARENT_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VM_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    is_migrated: bool
    previous_vm_parent_source_id: int
    previous_vm_entity_id: int
    migrated_time_usecs: int
    def __init__(self, is_migrated: bool = ..., previous_vm_parent_source_id: _Optional[int] = ..., previous_vm_entity_id: _Optional[int] = ..., migrated_time_usecs: _Optional[int] = ...) -> None: ...

class IoFilterStoragePolicyProperties(_message.Message):
    __slots__ = ("cohesity_id", "cohesity_cluster_endpoint", "heartbeat_interval_secs", "vcenter_uuid")
    COHESITY_ID_FIELD_NUMBER: _ClassVar[int]
    COHESITY_CLUSTER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    VCENTER_UUID_FIELD_NUMBER: _ClassVar[int]
    cohesity_id: str
    cohesity_cluster_endpoint: str
    heartbeat_interval_secs: int
    vcenter_uuid: str
    def __init__(self, cohesity_id: _Optional[str] = ..., cohesity_cluster_endpoint: _Optional[str] = ..., heartbeat_interval_secs: _Optional[int] = ..., vcenter_uuid: _Optional[str] = ...) -> None: ...

class IOFilterState(_message.Message):
    __slots__ = ("upgradability", "version", "filter_status", "io_filter_properties")
    class FilterStatus(_message.Message):
        __slots__ = ("state", "error")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFilterInstalled: _ClassVar[IOFilterState.FilterStatus.State]
            kInstallFilterInProgress: _ClassVar[IOFilterState.FilterStatus.State]
            kUninstallFilterInProgress: _ClassVar[IOFilterState.FilterStatus.State]
            kUpgradeFilterInProgress: _ClassVar[IOFilterState.FilterStatus.State]
            kUninstallFilterFailed: _ClassVar[IOFilterState.FilterStatus.State]
            kUpgradeFilterFailed: _ClassVar[IOFilterState.FilterStatus.State]
            kUpgradeAccepted: _ClassVar[IOFilterState.FilterStatus.State]
            kUninstallAccepted: _ClassVar[IOFilterState.FilterStatus.State]
            kInstallAccepted: _ClassVar[IOFilterState.FilterStatus.State]
        kFilterInstalled: IOFilterState.FilterStatus.State
        kInstallFilterInProgress: IOFilterState.FilterStatus.State
        kUninstallFilterInProgress: IOFilterState.FilterStatus.State
        kUpgradeFilterInProgress: IOFilterState.FilterStatus.State
        kUninstallFilterFailed: IOFilterState.FilterStatus.State
        kUpgradeFilterFailed: IOFilterState.FilterStatus.State
        kUpgradeAccepted: IOFilterState.FilterStatus.State
        kUninstallAccepted: IOFilterState.FilterStatus.State
        kInstallAccepted: IOFilterState.FilterStatus.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        state: IOFilterState.FilterStatus.State
        error: _error_pb2.ErrorProto
        def __init__(self, state: _Optional[_Union[IOFilterState.FilterStatus.State, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    UPGRADABILITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    IO_FILTER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    upgradability: _common_pb2.Upgradability.State
    version: str
    filter_status: IOFilterState.FilterStatus
    io_filter_properties: IoFilterStoragePolicyProperties
    def __init__(self, upgradability: _Optional[_Union[_common_pb2.Upgradability.State, str]] = ..., version: _Optional[str] = ..., filter_status: _Optional[_Union[IOFilterState.FilterStatus, _Mapping]] = ..., io_filter_properties: _Optional[_Union[IoFilterStoragePolicyProperties, _Mapping]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "is_vmc_env", "uuid", "moref", "vm_bios_uuid", "vm_bios_uuid_secondary", "vcd_attributes", "parent_vapp_uuid", "name", "connection_state", "vmware_tools_status", "folder_type", "host_type", "tag_attributes_vec", "uses_persistent_agent", "agent_status_vec", "agent_entity_id", "virtual_disk_info", "datastore_info", "vcenter_static_id", "is_vm_template", "system_resource_info", "parent_vcenter_uuid", "version", "guest_full_name", "custom_attributes_vec", "esxi_host_name", "ip_addr_vec", "storage_profile_vec", "data_transfer_ip", "org_vdc_network_vec", "filter_state", "aggregate_guest_disk_space_used", "vcd_catalog_vec", "vmware_custom_attributes_map", "front_end_size_info", "use_vm_bios_uuid", "vm_linking_info", "api_version", "logical_size_in_bytes", "last_tag_refresh_usecs", "is_saas_connector", "inventory_path")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVCenter: _ClassVar[Entity.Type]
        kStandaloneHost: _ClassVar[Entity.Type]
        kFolder: _ClassVar[Entity.Type]
        kDatacenter: _ClassVar[Entity.Type]
        kComputeResource: _ClassVar[Entity.Type]
        kClusterComputeResource: _ClassVar[Entity.Type]
        kResourcePool: _ClassVar[Entity.Type]
        kDatastore: _ClassVar[Entity.Type]
        kHostSystem: _ClassVar[Entity.Type]
        kVirtualMachine: _ClassVar[Entity.Type]
        kVirtualApp: _ClassVar[Entity.Type]
        kStoragePod: _ClassVar[Entity.Type]
        kNetwork: _ClassVar[Entity.Type]
        kDistributedVirtualPortgroup: _ClassVar[Entity.Type]
        kTagCategory: _ClassVar[Entity.Type]
        kTag: _ClassVar[Entity.Type]
        kOpaqueNetwork: _ClassVar[Entity.Type]
        kvCloudDirector: _ClassVar[Entity.Type]
        kOrganization: _ClassVar[Entity.Type]
        kVirtualDatacenter: _ClassVar[Entity.Type]
        kCatalog: _ClassVar[Entity.Type]
        kOrgMetadata: _ClassVar[Entity.Type]
        kStoragePolicy: _ClassVar[Entity.Type]
        kVirtualDisk: _ClassVar[Entity.Type]
        kvAppTemplate: _ClassVar[Entity.Type]
        kDummyResource: _ClassVar[Entity.Type]
        kUnknown: _ClassVar[Entity.Type]
    kVCenter: Entity.Type
    kStandaloneHost: Entity.Type
    kFolder: Entity.Type
    kDatacenter: Entity.Type
    kComputeResource: Entity.Type
    kClusterComputeResource: Entity.Type
    kResourcePool: Entity.Type
    kDatastore: Entity.Type
    kHostSystem: Entity.Type
    kVirtualMachine: Entity.Type
    kVirtualApp: Entity.Type
    kStoragePod: Entity.Type
    kNetwork: Entity.Type
    kDistributedVirtualPortgroup: Entity.Type
    kTagCategory: Entity.Type
    kTag: Entity.Type
    kOpaqueNetwork: Entity.Type
    kvCloudDirector: Entity.Type
    kOrganization: Entity.Type
    kVirtualDatacenter: Entity.Type
    kCatalog: Entity.Type
    kOrgMetadata: Entity.Type
    kStoragePolicy: Entity.Type
    kVirtualDisk: Entity.Type
    kvAppTemplate: Entity.Type
    kDummyResource: Entity.Type
    kUnknown: Entity.Type
    class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kConnected: _ClassVar[Entity.ConnectionState]
        kDisconnected: _ClassVar[Entity.ConnectionState]
        kInaccessible: _ClassVar[Entity.ConnectionState]
        kInvalid: _ClassVar[Entity.ConnectionState]
        kOrphaned: _ClassVar[Entity.ConnectionState]
        kNotResponding: _ClassVar[Entity.ConnectionState]
    kConnected: Entity.ConnectionState
    kDisconnected: Entity.ConnectionState
    kInaccessible: Entity.ConnectionState
    kInvalid: Entity.ConnectionState
    kOrphaned: Entity.ConnectionState
    kNotResponding: Entity.ConnectionState
    class VmwareCustomAttributesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CustomAttribute
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CustomAttribute, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_VMC_ENV_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_BIOS_UUID_SECONDARY_FIELD_NUMBER: _ClassVar[int]
    VCD_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PARENT_VAPP_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_TOOLS_STATUS_FIELD_NUMBER: _ClassVar[int]
    FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    USES_PERSISTENT_AGENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    VCENTER_STATIC_ID_FIELD_NUMBER: _ClassVar[int]
    IS_VM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    PARENT_VCENTER_UUID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GUEST_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    ESXI_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_IP_FIELD_NUMBER: _ClassVar[int]
    ORG_VDC_NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    FILTER_STATE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_GUEST_DISK_SPACE_USED_FIELD_NUMBER: _ClassVar[int]
    VCD_CATALOG_VEC_FIELD_NUMBER: _ClassVar[int]
    VMWARE_CUSTOM_ATTRIBUTES_MAP_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_VM_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_LINKING_INFO_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_TAG_REFRESH_USECS_FIELD_NUMBER: _ClassVar[int]
    IS_SAAS_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    is_vmc_env: bool
    uuid: str
    moref: _vmware_common_pb2.MORef
    vm_bios_uuid: str
    vm_bios_uuid_secondary: str
    vcd_attributes: VCDAttributes
    parent_vapp_uuid: str
    name: str
    connection_state: Entity.ConnectionState
    vmware_tools_status: VMwareToolsRunningStatus.Type
    folder_type: FolderType.Type
    host_type: _enums_pb2.HostEnv.Type
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[TagAttributes]
    uses_persistent_agent: bool
    agent_status_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.HostAgentStatus]
    agent_entity_id: int
    virtual_disk_info: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo]
    datastore_info: DatastoreInfo
    vcenter_static_id: int
    is_vm_template: bool
    system_resource_info: _common_pb2.SystemResourceInfo
    parent_vcenter_uuid: str
    version: str
    guest_full_name: str
    custom_attributes_vec: _containers.RepeatedCompositeFieldContainer[CustomAttribute]
    esxi_host_name: str
    ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
    storage_profile_vec: _containers.RepeatedCompositeFieldContainer[StorageProfile]
    data_transfer_ip: str
    org_vdc_network_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2.OrgVDCNetwork]
    filter_state: IOFilterState
    aggregate_guest_disk_space_used: int
    vcd_catalog_vec: _containers.RepeatedCompositeFieldContainer[VCDCatalog]
    vmware_custom_attributes_map: _containers.MessageMap[int, CustomAttribute]
    front_end_size_info: _stats_pb2.SizeInfo
    use_vm_bios_uuid: bool
    vm_linking_info: VMLinkingInfo
    api_version: str
    logical_size_in_bytes: int
    last_tag_refresh_usecs: int
    is_saas_connector: bool
    inventory_path: str
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., is_vmc_env: bool = ..., uuid: _Optional[str] = ..., moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_bios_uuid: _Optional[str] = ..., vm_bios_uuid_secondary: _Optional[str] = ..., vcd_attributes: _Optional[_Union[VCDAttributes, _Mapping]] = ..., parent_vapp_uuid: _Optional[str] = ..., name: _Optional[str] = ..., connection_state: _Optional[_Union[Entity.ConnectionState, str]] = ..., vmware_tools_status: _Optional[_Union[VMwareToolsRunningStatus.Type, str]] = ..., folder_type: _Optional[_Union[FolderType.Type, str]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[TagAttributes, _Mapping]]] = ..., uses_persistent_agent: bool = ..., agent_status_vec: _Optional[_Iterable[_Union[_agent_pb2.HostAgentStatus, _Mapping]]] = ..., agent_entity_id: _Optional[int] = ..., virtual_disk_info: _Optional[_Iterable[_Union[VirtualDiskInfo, _Mapping]]] = ..., datastore_info: _Optional[_Union[DatastoreInfo, _Mapping]] = ..., vcenter_static_id: _Optional[int] = ..., is_vm_template: bool = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ..., parent_vcenter_uuid: _Optional[str] = ..., version: _Optional[str] = ..., guest_full_name: _Optional[str] = ..., custom_attributes_vec: _Optional[_Iterable[_Union[CustomAttribute, _Mapping]]] = ..., esxi_host_name: _Optional[str] = ..., ip_addr_vec: _Optional[_Iterable[str]] = ..., storage_profile_vec: _Optional[_Iterable[_Union[StorageProfile, _Mapping]]] = ..., data_transfer_ip: _Optional[str] = ..., org_vdc_network_vec: _Optional[_Iterable[_Union[_common_pb2.OrgVDCNetwork, _Mapping]]] = ..., filter_state: _Optional[_Union[IOFilterState, _Mapping]] = ..., aggregate_guest_disk_space_used: _Optional[int] = ..., vcd_catalog_vec: _Optional[_Iterable[_Union[VCDCatalog, _Mapping]]] = ..., vmware_custom_attributes_map: _Optional[_Mapping[int, CustomAttribute]] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ..., use_vm_bios_uuid: bool = ..., vm_linking_info: _Optional[_Union[VMLinkingInfo, _Mapping]] = ..., api_version: _Optional[str] = ..., logical_size_in_bytes: _Optional[int] = ..., last_tag_refresh_usecs: _Optional[int] = ..., is_saas_connector: bool = ..., inventory_path: _Optional[str] = ...) -> None: ...
