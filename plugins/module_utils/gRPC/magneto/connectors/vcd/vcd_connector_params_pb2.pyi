from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VcdItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kVcdItemVM: _ClassVar[VcdItemType]
    kVcdItemVApp: _ClassVar[VcdItemType]
    kVcdItemVAppTemplate: _ClassVar[VcdItemType]
kVcdItemVM: VcdItemType
kVcdItemVApp: VcdItemType
kVcdItemVAppTemplate: VcdItemType

class NewVCDConnectorContextArg(_message.Message):
    __slots__ = ("connector_params", "instance_id")
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    connector_params: _magneto_pb2.ConnectorParams
    instance_id: int
    def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., instance_id: _Optional[int] = ...) -> None: ...

class NewVCDConnectorContextResult(_message.Message):
    __slots__ = ("unique_id", "server_type")
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    unique_id: str
    server_type: _vmware_pb2.Entity.Type
    def __init__(self, unique_id: _Optional[str] = ..., server_type: _Optional[_Union[_vmware_pb2.Entity.Type, str]] = ...) -> None: ...

class VCDConnectorContextProto(_message.Message):
    __slots__ = ("endpoint", "id", "unique_id", "version", "instance_id", "connector_params")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    id: int
    unique_id: str
    version: int
    instance_id: int
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, endpoint: _Optional[str] = ..., id: _Optional[int] = ..., unique_id: _Optional[str] = ..., version: _Optional[int] = ..., instance_id: _Optional[int] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class MORefStringEntityProtoMap(_message.Message):
    __slots__ = ("moref_entity_proto_map",)
    class MorefEntityProtoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _entity_pb2.EntityProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    MOREF_ENTITY_PROTO_MAP_FIELD_NUMBER: _ClassVar[int]
    moref_entity_proto_map: _containers.MessageMap[str, _entity_pb2.EntityProto]
    def __init__(self, moref_entity_proto_map: _Optional[_Mapping[str, _entity_pb2.EntityProto]] = ...) -> None: ...

class QueryVCDHierarchyArg(_message.Message):
    __slots__ = ("vcd_entity_hierarchy", "vcenter_moref_entity_proto_map", "vcenter", "moref_vec", "entity_proto_vec")
    class VcenterMorefEntityProtoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MORefStringEntityProtoMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MORefStringEntityProtoMap, _Mapping]] = ...) -> None: ...
    VCD_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    VCENTER_MOREF_ENTITY_PROTO_MAP_FIELD_NUMBER: _ClassVar[int]
    VCENTER_FIELD_NUMBER: _ClassVar[int]
    MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    vcd_entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    vcenter_moref_entity_proto_map: _containers.MessageMap[str, MORefStringEntityProtoMap]
    vcenter: _containers.RepeatedScalarFieldContainer[str]
    moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    entity_proto_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, vcd_entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., vcenter_moref_entity_proto_map: _Optional[_Mapping[str, MORefStringEntityProtoMap]] = ..., vcenter: _Optional[_Iterable[str]] = ..., moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., entity_proto_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class QueryVCDHierarchyResult(_message.Message):
    __slots__ = ("vms_missing_from_vcenter", "vcenter_vm_moref_entity_proto_map", "vms_in_incosistent_state", "queried_vcd_entity_hierarchy")
    class VcenterVmMorefEntityProtoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MORefStringEntityProtoMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MORefStringEntityProtoMap, _Mapping]] = ...) -> None: ...
    VMS_MISSING_FROM_VCENTER_FIELD_NUMBER: _ClassVar[int]
    VCENTER_VM_MOREF_ENTITY_PROTO_MAP_FIELD_NUMBER: _ClassVar[int]
    VMS_IN_INCOSISTENT_STATE_FIELD_NUMBER: _ClassVar[int]
    QUERIED_VCD_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    vms_missing_from_vcenter: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    vcenter_vm_moref_entity_proto_map: _containers.MessageMap[str, MORefStringEntityProtoMap]
    vms_in_incosistent_state: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    queried_vcd_entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, vms_missing_from_vcenter: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., vcenter_vm_moref_entity_proto_map: _Optional[_Mapping[str, MORefStringEntityProtoMap]] = ..., vms_in_incosistent_state: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., queried_vcd_entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class ListVCentersArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListVCentersResult(_message.Message):
    __slots__ = ("vcenter_info_vec",)
    class VCenterInfo(_message.Message):
        __slots__ = ("vcenter_name", "vcenter_endpoint", "vcenter_id")
        VCENTER_NAME_FIELD_NUMBER: _ClassVar[int]
        VCENTER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        VCENTER_ID_FIELD_NUMBER: _ClassVar[int]
        vcenter_name: str
        vcenter_endpoint: str
        vcenter_id: str
        def __init__(self, vcenter_name: _Optional[str] = ..., vcenter_endpoint: _Optional[str] = ..., vcenter_id: _Optional[str] = ...) -> None: ...
    VCENTER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vcenter_info_vec: _containers.RepeatedCompositeFieldContainer[ListVCentersResult.VCenterInfo]
    def __init__(self, vcenter_info_vec: _Optional[_Iterable[_Union[ListVCentersResult.VCenterInfo, _Mapping]]] = ...) -> None: ...

class FetchVAppInfoArg(_message.Message):
    __slots__ = ("vapp",)
    VAPP_FIELD_NUMBER: _ClassVar[int]
    vapp: str
    def __init__(self, vapp: _Optional[str] = ...) -> None: ...

class FetchVAppInfoResult(_message.Message):
    __slots__ = ("vapp_xml_str", "id", "name", "href", "in_maintenance_mode", "deployed", "vdc_id", "children", "vapp_network_xml_str", "warnings")
    class ChildrenEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VAPP_XML_STR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HREF_FIELD_NUMBER: _ClassVar[int]
    IN_MAINTENANCE_MODE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_FIELD_NUMBER: _ClassVar[int]
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    VAPP_NETWORK_XML_STR_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    vapp_xml_str: str
    id: str
    name: str
    href: str
    in_maintenance_mode: bool
    deployed: bool
    vdc_id: str
    children: _containers.ScalarMap[str, str]
    vapp_network_xml_str: str
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, vapp_xml_str: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., href: _Optional[str] = ..., in_maintenance_mode: bool = ..., deployed: bool = ..., vdc_id: _Optional[str] = ..., children: _Optional[_Mapping[str, str]] = ..., vapp_network_xml_str: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class GetVcdOrgInfoArg(_message.Message):
    __slots__ = ("org",)
    ORG_FIELD_NUMBER: _ClassVar[int]
    org: str
    def __init__(self, org: _Optional[str] = ...) -> None: ...

class GetVcdOrgInfoResult(_message.Message):
    __slots__ = ("org_id", "vcd_host")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    VCD_HOST_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    vcd_host: str
    def __init__(self, org_id: _Optional[str] = ..., vcd_host: _Optional[str] = ...) -> None: ...

class GetVCDVersionInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVCDVersionInfoResult(_message.Message):
    __slots__ = ("vcd_version",)
    VCD_VERSION_FIELD_NUMBER: _ClassVar[int]
    vcd_version: str
    def __init__(self, vcd_version: _Optional[str] = ...) -> None: ...

class GetUrlArg(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetUrlResult(_message.Message):
    __slots__ = ("xml_data",)
    XML_DATA_FIELD_NUMBER: _ClassVar[int]
    xml_data: str
    def __init__(self, xml_data: _Optional[str] = ...) -> None: ...

class ModifyVAppAttributeArg(_message.Message):
    __slots__ = ("vapp", "vapp_attr", "vapp_attr_val")
    class VAppAttribute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMaintenanceMode: _ClassVar[ModifyVAppAttributeArg.VAppAttribute]
    kMaintenanceMode: ModifyVAppAttributeArg.VAppAttribute
    class VAppAttributeVal(_message.Message):
        __slots__ = ("enter_maintenance_mode",)
        ENTER_MAINTENANCE_MODE_FIELD_NUMBER: _ClassVar[int]
        enter_maintenance_mode: bool
        def __init__(self, enter_maintenance_mode: bool = ...) -> None: ...
    VAPP_FIELD_NUMBER: _ClassVar[int]
    VAPP_ATTR_FIELD_NUMBER: _ClassVar[int]
    VAPP_ATTR_VAL_FIELD_NUMBER: _ClassVar[int]
    vapp: str
    vapp_attr: ModifyVAppAttributeArg.VAppAttribute
    vapp_attr_val: ModifyVAppAttributeArg.VAppAttributeVal
    def __init__(self, vapp: _Optional[str] = ..., vapp_attr: _Optional[_Union[ModifyVAppAttributeArg.VAppAttribute, str]] = ..., vapp_attr_val: _Optional[_Union[ModifyVAppAttributeArg.VAppAttributeVal, _Mapping]] = ...) -> None: ...

class ModifyVAppAttributeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VcdItem(_message.Message):
    __slots__ = ("item_type", "item_id", "item_name")
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    item_type: VcdItemType
    item_id: str
    item_name: str
    def __init__(self, item_type: _Optional[_Union[VcdItemType, str]] = ..., item_id: _Optional[str] = ..., item_name: _Optional[str] = ...) -> None: ...

class DiskSettings(_message.Message):
    __slots__ = ("size_mb", "unit_number", "bus_number", "adapter_type", "thin_provisioned")
    SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    THIN_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
    size_mb: int
    unit_number: int
    bus_number: int
    adapter_type: str
    thin_provisioned: bool
    def __init__(self, size_mb: _Optional[int] = ..., unit_number: _Optional[int] = ..., bus_number: _Optional[int] = ..., adapter_type: _Optional[str] = ..., thin_provisioned: bool = ...) -> None: ...

class DiskSection(_message.Message):
    __slots__ = ("disk_settings",)
    DISK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    disk_settings: _containers.RepeatedCompositeFieldContainer[DiskSettings]
    def __init__(self, disk_settings: _Optional[_Iterable[_Union[DiskSettings, _Mapping]]] = ...) -> None: ...

class VmSpecSection(_message.Message):
    __slots__ = ("os_type", "num_cpus", "num_cores_per_socket", "cpu_resource_mhz", "memory_resource_mb", "disk_section", "hardware_version", "virtual_cpu_type")
    class VirtualCpuType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM64: _ClassVar[VmSpecSection.VirtualCpuType]
        VM32: _ClassVar[VmSpecSection.VirtualCpuType]
    VM64: VmSpecSection.VirtualCpuType
    VM32: VmSpecSection.VirtualCpuType
    class ComputeResourceType(_message.Message):
        __slots__ = ("Configured",)
        CONFIGURED_FIELD_NUMBER: _ClassVar[int]
        Configured: int
        def __init__(self, Configured: _Optional[int] = ...) -> None: ...
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_CPUS_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_PER_SOCKET_FIELD_NUMBER: _ClassVar[int]
    CPU_RESOURCE_MHZ_FIELD_NUMBER: _ClassVar[int]
    MEMORY_RESOURCE_MB_FIELD_NUMBER: _ClassVar[int]
    DISK_SECTION_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    os_type: str
    num_cpus: int
    num_cores_per_socket: int
    cpu_resource_mhz: VmSpecSection.ComputeResourceType
    memory_resource_mb: VmSpecSection.ComputeResourceType
    disk_section: DiskSection
    hardware_version: str
    virtual_cpu_type: VmSpecSection.VirtualCpuType
    def __init__(self, os_type: _Optional[str] = ..., num_cpus: _Optional[int] = ..., num_cores_per_socket: _Optional[int] = ..., cpu_resource_mhz: _Optional[_Union[VmSpecSection.ComputeResourceType, _Mapping]] = ..., memory_resource_mb: _Optional[_Union[VmSpecSection.ComputeResourceType, _Mapping]] = ..., disk_section: _Optional[_Union[DiskSection, _Mapping]] = ..., hardware_version: _Optional[str] = ..., virtual_cpu_type: _Optional[_Union[VmSpecSection.VirtualCpuType, str]] = ...) -> None: ...

class CreateVm(_message.Message):
    __slots__ = ("name", "vm_spec_section", "storage_profile")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_SPEC_SECTION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_spec_section: VmSpecSection
    storage_profile: str
    def __init__(self, name: _Optional[str] = ..., vm_spec_section: _Optional[_Union[VmSpecSection, _Mapping]] = ..., storage_profile: _Optional[str] = ...) -> None: ...

class CreateVcdVmArg(_message.Message):
    __slots__ = ("vdc_id", "create_vm", "xml_vm_config")
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_VM_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    vdc_id: str
    create_vm: CreateVm
    xml_vm_config: str
    def __init__(self, vdc_id: _Optional[str] = ..., create_vm: _Optional[_Union[CreateVm, _Mapping]] = ..., xml_vm_config: _Optional[str] = ...) -> None: ...

class CreateVcdVmResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateVAppArg(_message.Message):
    __slots__ = ("vapp_name", "vdc_id", "vapp_xml_str", "sourced_items", "vapp_network_xml_str", "network_uuid_vec", "should_attach_network", "attach_internal_networks")
    VAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    VAPP_XML_STR_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    VAPP_NETWORK_XML_STR_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ATTACH_NETWORK_FIELD_NUMBER: _ClassVar[int]
    ATTACH_INTERNAL_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    vapp_name: str
    vdc_id: str
    vapp_xml_str: str
    sourced_items: _containers.RepeatedCompositeFieldContainer[VcdItem]
    vapp_network_xml_str: str
    network_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    should_attach_network: bool
    attach_internal_networks: bool
    def __init__(self, vapp_name: _Optional[str] = ..., vdc_id: _Optional[str] = ..., vapp_xml_str: _Optional[str] = ..., sourced_items: _Optional[_Iterable[_Union[VcdItem, _Mapping]]] = ..., vapp_network_xml_str: _Optional[str] = ..., network_uuid_vec: _Optional[_Iterable[str]] = ..., should_attach_network: bool = ..., attach_internal_networks: bool = ...) -> None: ...

class CreateVAppResult(_message.Message):
    __slots__ = ("resp_vapp_xml_str", "created_vapp_name", "created_vapp_id", "warnings")
    RESP_VAPP_XML_STR_FIELD_NUMBER: _ClassVar[int]
    CREATED_VAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_VAPP_ID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    resp_vapp_xml_str: str
    created_vapp_name: str
    created_vapp_id: str
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, resp_vapp_xml_str: _Optional[str] = ..., created_vapp_name: _Optional[str] = ..., created_vapp_id: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class ReConfigureVAppArg(_message.Message):
    __slots__ = ("vapp_id", "add_items", "remove_items")
    VAPP_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_ITEMS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    vapp_id: str
    add_items: _containers.RepeatedCompositeFieldContainer[VcdItem]
    remove_items: _containers.RepeatedCompositeFieldContainer[VcdItem]
    def __init__(self, vapp_id: _Optional[str] = ..., add_items: _Optional[_Iterable[_Union[VcdItem, _Mapping]]] = ..., remove_items: _Optional[_Iterable[_Union[VcdItem, _Mapping]]] = ...) -> None: ...

class ReConfigureVAppResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImportedDiskType(_message.Message):
    __slots__ = ("vdc_storage_profile", "instance_id")
    VDC_STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    vdc_storage_profile: str
    instance_id: str
    def __init__(self, vdc_storage_profile: _Optional[str] = ..., instance_id: _Optional[str] = ...) -> None: ...

class ImportVmIntoVAppArg(_message.Message):
    __slots__ = ("vapp_id", "sourced_item_href", "sourced_item_moref", "sourced_item_name", "item_description", "vdc_storage_profile", "source_vc_server_id", "source_move", "storage_profile_uuid", "storage_profile_name", "imported_disk_type")
    VAPP_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEM_HREF_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VDC_STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VC_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MOVE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    vapp_id: str
    sourced_item_href: str
    sourced_item_moref: str
    sourced_item_name: str
    item_description: str
    vdc_storage_profile: str
    source_vc_server_id: str
    source_move: bool
    storage_profile_uuid: str
    storage_profile_name: str
    imported_disk_type: _containers.RepeatedCompositeFieldContainer[ImportedDiskType]
    def __init__(self, vapp_id: _Optional[str] = ..., sourced_item_href: _Optional[str] = ..., sourced_item_moref: _Optional[str] = ..., sourced_item_name: _Optional[str] = ..., item_description: _Optional[str] = ..., vdc_storage_profile: _Optional[str] = ..., source_vc_server_id: _Optional[str] = ..., source_move: bool = ..., storage_profile_uuid: _Optional[str] = ..., storage_profile_name: _Optional[str] = ..., imported_disk_type: _Optional[_Iterable[_Union[ImportedDiskType, _Mapping]]] = ...) -> None: ...

class ImportVmIntoVAppResult(_message.Message):
    __slots__ = ("vm_id",)
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    def __init__(self, vm_id: _Optional[str] = ...) -> None: ...

class ImportVmAsVAppArg(_message.Message):
    __slots__ = ("vdc_id", "vapp_name", "vm_moref", "vm_name", "vdc_storage_profile", "source_vc_server_id", "source_move", "is_standalone")
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    VAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VDC_STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VC_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MOVE_FIELD_NUMBER: _ClassVar[int]
    IS_STANDALONE_FIELD_NUMBER: _ClassVar[int]
    vdc_id: str
    vapp_name: str
    vm_moref: str
    vm_name: str
    vdc_storage_profile: str
    source_vc_server_id: str
    source_move: bool
    is_standalone: bool
    def __init__(self, vdc_id: _Optional[str] = ..., vapp_name: _Optional[str] = ..., vm_moref: _Optional[str] = ..., vm_name: _Optional[str] = ..., vdc_storage_profile: _Optional[str] = ..., source_vc_server_id: _Optional[str] = ..., source_move: bool = ..., is_standalone: bool = ...) -> None: ...

class ImportVmAsVAppResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WaitForVcdTaskArg(_message.Message):
    __slots__ = ("task_to_monitor_id", "idle_timeout_seconds", "poll_interval_seconds")
    TASK_TO_MONITOR_ID_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    POLL_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    task_to_monitor_id: str
    idle_timeout_seconds: int
    poll_interval_seconds: int
    def __init__(self, task_to_monitor_id: _Optional[str] = ..., idle_timeout_seconds: _Optional[int] = ..., poll_interval_seconds: _Optional[int] = ...) -> None: ...

class WaitForVcdTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshVcenterInVCDArg(_message.Message):
    __slots__ = ("vcenter_id",)
    VCENTER_ID_FIELD_NUMBER: _ClassVar[int]
    vcenter_id: str
    def __init__(self, vcenter_id: _Optional[str] = ...) -> None: ...

class RefreshVcenterInVCDResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DestroyVCDObjectArg(_message.Message):
    __slots__ = ("vcd_object_id", "is_object_vapp")
    VCD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_VAPP_FIELD_NUMBER: _ClassVar[int]
    vcd_object_id: str
    is_object_vapp: bool
    def __init__(self, vcd_object_id: _Optional[str] = ..., is_object_vapp: bool = ...) -> None: ...

class DestroyVCDObjectResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerOnOffVCDVMArg(_message.Message):
    __slots__ = ("vcd_object_id", "power_on", "is_object_vapp")
    VCD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_VAPP_FIELD_NUMBER: _ClassVar[int]
    vcd_object_id: str
    power_on: bool
    is_object_vapp: bool
    def __init__(self, vcd_object_id: _Optional[str] = ..., power_on: bool = ..., is_object_vapp: bool = ...) -> None: ...

class PowerOnOffVCDVMResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchAllDatastoresForStorageProfileArg(_message.Message):
    __slots__ = ("parent_vcenter_uuid", "storage_profile_name", "pvdc_uuid", "include_cohesity_datastores")
    PARENT_VCENTER_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PVDC_UUID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_COHESITY_DATASTORES_FIELD_NUMBER: _ClassVar[int]
    parent_vcenter_uuid: str
    storage_profile_name: str
    pvdc_uuid: str
    include_cohesity_datastores: bool
    def __init__(self, parent_vcenter_uuid: _Optional[str] = ..., storage_profile_name: _Optional[str] = ..., pvdc_uuid: _Optional[str] = ..., include_cohesity_datastores: bool = ...) -> None: ...

class FetchAllDatastoresForStorageProfileResult(_message.Message):
    __slots__ = ("datastores_moref_vec",)
    DATASTORES_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    datastores_moref_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, datastores_moref_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchCompatibleDatastoresForVDCArg(_message.Message):
    __slots__ = ("pvdc_uuid",)
    PVDC_UUID_FIELD_NUMBER: _ClassVar[int]
    pvdc_uuid: str
    def __init__(self, pvdc_uuid: _Optional[str] = ...) -> None: ...

class FetchCompatibleDatastoresForVDCResult(_message.Message):
    __slots__ = ("datastores_moref_vec",)
    DATASTORES_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    datastores_moref_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, datastores_moref_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RefreshStoragePoliciesOnVCDArg(_message.Message):
    __slots__ = ("vc_id",)
    VC_ID_FIELD_NUMBER: _ClassVar[int]
    vc_id: str
    def __init__(self, vc_id: _Optional[str] = ...) -> None: ...

class RefreshStoragePoliciesOnVCDResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImportAsStandaloneVmArg(_message.Message):
    __slots__ = ("vdc_id", "sourced_item_href", "sourced_item_moref", "sourced_item_name", "item_description", "vdc_storage_profile", "source_vc_server_id", "source_move", "storage_profile_uuid", "storage_profile_name", "imported_disk_type")
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEM_HREF_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    SOURCED_ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VDC_STORAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VC_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MOVE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    vdc_id: str
    sourced_item_href: str
    sourced_item_moref: str
    sourced_item_name: str
    item_description: str
    vdc_storage_profile: str
    source_vc_server_id: str
    source_move: bool
    storage_profile_uuid: str
    storage_profile_name: str
    imported_disk_type: _containers.RepeatedCompositeFieldContainer[ImportedDiskType]
    def __init__(self, vdc_id: _Optional[str] = ..., sourced_item_href: _Optional[str] = ..., sourced_item_moref: _Optional[str] = ..., sourced_item_name: _Optional[str] = ..., item_description: _Optional[str] = ..., vdc_storage_profile: _Optional[str] = ..., source_vc_server_id: _Optional[str] = ..., source_move: bool = ..., storage_profile_uuid: _Optional[str] = ..., storage_profile_name: _Optional[str] = ..., imported_disk_type: _Optional[_Iterable[_Union[ImportedDiskType, _Mapping]]] = ...) -> None: ...

class ImportAsStandaloneVmResult(_message.Message):
    __slots__ = ("vm_id",)
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    def __init__(self, vm_id: _Optional[str] = ...) -> None: ...

class FetchOrgVDCNetworkArg(_message.Message):
    __slots__ = ("vm_uuid",)
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ...) -> None: ...

class FetchOrgVDCNetworkResult(_message.Message):
    __slots__ = ("primary_network_connection_index", "network_vec")
    PRIMARY_NETWORK_CONNECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    primary_network_connection_index: int
    network_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VMOrgVDCNetwork]
    def __init__(self, primary_network_connection_index: _Optional[int] = ..., network_vec: _Optional[_Iterable[_Union[_magneto_pb2.VMOrgVDCNetwork, _Mapping]]] = ...) -> None: ...

class ReconfigureVcdVmArg(_message.Message):
    __slots__ = ("vm_id", "vm_name", "attach_org_vdc_networks", "primary_network_connection_index", "org_vdc_network_vec")
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACH_ORG_VDC_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_NETWORK_CONNECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    ORG_VDC_NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_id: str
    vm_name: str
    attach_org_vdc_networks: bool
    primary_network_connection_index: int
    org_vdc_network_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VMOrgVDCNetwork]
    def __init__(self, vm_id: _Optional[str] = ..., vm_name: _Optional[str] = ..., attach_org_vdc_networks: bool = ..., primary_network_connection_index: _Optional[int] = ..., org_vdc_network_vec: _Optional[_Iterable[_Union[_magneto_pb2.VMOrgVDCNetwork, _Mapping]]] = ...) -> None: ...

class ReconfigureVcdVmResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CaptureVappAsTemplateArg(_message.Message):
    __slots__ = ("vapp_id", "vdc_id", "vapp_name", "vapp_template_name", "catalog_id")
    VAPP_ID_FIELD_NUMBER: _ClassVar[int]
    VDC_ID_FIELD_NUMBER: _ClassVar[int]
    VAPP_NAME_FIELD_NUMBER: _ClassVar[int]
    VAPP_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    vapp_id: str
    vdc_id: str
    vapp_name: str
    vapp_template_name: str
    catalog_id: str
    def __init__(self, vapp_id: _Optional[str] = ..., vdc_id: _Optional[str] = ..., vapp_name: _Optional[str] = ..., vapp_template_name: _Optional[str] = ..., catalog_id: _Optional[str] = ...) -> None: ...

class CaptureVappAsTemplateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchVAppNetworkArg(_message.Message):
    __slots__ = ("vapp_uuid",)
    VAPP_UUID_FIELD_NUMBER: _ClassVar[int]
    vapp_uuid: str
    def __init__(self, vapp_uuid: _Optional[str] = ...) -> None: ...

class FetchVAppNetworkResult(_message.Message):
    __slots__ = ("vapp_network_xml",)
    VAPP_NETWORK_XML_FIELD_NUMBER: _ClassVar[int]
    vapp_network_xml: str
    def __init__(self, vapp_network_xml: _Optional[str] = ...) -> None: ...

class RemoveStoragePolicyArg(_message.Message):
    __slots__ = ("pvdc_uuid", "vdc_uuid", "storage_profile_name", "storage_profile_pvdc_uuid", "storage_profile_vdc_uuid")
    PVDC_UUID_FIELD_NUMBER: _ClassVar[int]
    VDC_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_PVDC_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_VDC_UUID_FIELD_NUMBER: _ClassVar[int]
    pvdc_uuid: str
    vdc_uuid: str
    storage_profile_name: str
    storage_profile_pvdc_uuid: str
    storage_profile_vdc_uuid: str
    def __init__(self, pvdc_uuid: _Optional[str] = ..., vdc_uuid: _Optional[str] = ..., storage_profile_name: _Optional[str] = ..., storage_profile_pvdc_uuid: _Optional[str] = ..., storage_profile_vdc_uuid: _Optional[str] = ...) -> None: ...

class RemoveStoragePolicyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
