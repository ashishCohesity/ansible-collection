from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import nas_pb2 as _nas_pb2
from magneto.base import san_pb2 as _san_pb2
from magneto.connectors.vmware import vmware_pb2 as _vmware_pb2_1
from magneto.connectors.vmware import vmware_common_args_pb2 as _vmware_common_args_pb2
from magneto.connectors.vmware import vmware_pbm_pb2 as _vmware_pbm_pb2
from magneto.connectors.vmware import vsphere_pb2 as _vsphere_pb2
from magneto.v2.adapters import facade_for_entity_manager_pb2 as _facade_for_entity_manager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskProvisionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kThickProvisionLazyZeroed: _ClassVar[DiskProvisionType]
    kThickProvisionEagerlyZeroed: _ClassVar[DiskProvisionType]
    kThinProvision: _ClassVar[DiskProvisionType]
kThickProvisionLazyZeroed: DiskProvisionType
kThickProvisionEagerlyZeroed: DiskProvisionType
kThinProvision: DiskProvisionType

class NewConnectorContextArg(_message.Message):
    __slots__ = ("connector_params", "instance_id")
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    connector_params: _magneto_pb2.ConnectorParams
    instance_id: int
    def __init__(self, connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., instance_id: _Optional[int] = ...) -> None: ...

class NewConnectorContextResult(_message.Message):
    __slots__ = ("unique_id", "server_type")
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    unique_id: str
    server_type: _vmware_pb2.Entity.Type
    def __init__(self, unique_id: _Optional[str] = ..., server_type: _Optional[_Union[_vmware_pb2.Entity.Type, str]] = ...) -> None: ...

class VMwareConnectorContextProto(_message.Message):
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

class BaseParamsProto(_message.Message):
    __slots__ = ("connector_context", "task_id", "max_retry_count", "retry_interval_msecs")
    CONNECTOR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRY_INTERVAL_MSECS_FIELD_NUMBER: _ClassVar[int]
    connector_context: VMwareConnectorContextProto
    task_id: int
    max_retry_count: int
    retry_interval_msecs: int
    def __init__(self, connector_context: _Optional[_Union[VMwareConnectorContextProto, _Mapping]] = ..., task_id: _Optional[int] = ..., max_retry_count: _Optional[int] = ..., retry_interval_msecs: _Optional[int] = ...) -> None: ...

class QueryEntityHierarchyArg(_message.Message):
    __slots__ = ("root_moref", "include_unsupported_vms", "populate_vm_bios_uuid", "query_vm_tag_hierarchy", "ignore_query_vm_tag_hierarchy_error", "vcenter_static_id", "preferred_subnet_vec", "populate_dag_hierarchy", "max_objects_to_retrieve_per_request")
    ROOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNSUPPORTED_VMS_FIELD_NUMBER: _ClassVar[int]
    POPULATE_VM_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    QUERY_VM_TAG_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    IGNORE_QUERY_VM_TAG_HIERARCHY_ERROR_FIELD_NUMBER: _ClassVar[int]
    VCENTER_STATIC_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
    POPULATE_DAG_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECTS_TO_RETRIEVE_PER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    root_moref: _vmware_common_pb2.MORef
    include_unsupported_vms: bool
    populate_vm_bios_uuid: bool
    query_vm_tag_hierarchy: bool
    ignore_query_vm_tag_hierarchy_error: bool
    vcenter_static_id: int
    preferred_subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    populate_dag_hierarchy: bool
    max_objects_to_retrieve_per_request: int
    def __init__(self, root_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., include_unsupported_vms: bool = ..., populate_vm_bios_uuid: bool = ..., query_vm_tag_hierarchy: bool = ..., ignore_query_vm_tag_hierarchy_error: bool = ..., vcenter_static_id: _Optional[int] = ..., preferred_subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., populate_dag_hierarchy: bool = ..., max_objects_to_retrieve_per_request: _Optional[int] = ...) -> None: ...

class QueryEntityHierarchyResult(_message.Message):
    __slots__ = ("queried_entity_hierarchy", "query_vm_tag_hierarchy_error", "moref_vec", "entity_proto_vec", "is_vmc_env", "dag_entity_hierarchy_result", "pk_to_entity_map")
    class PkToEntityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _vmware_pb2.Entity
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ...) -> None: ...
    QUERIED_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    QUERY_VM_TAG_HIERARCHY_ERROR_FIELD_NUMBER: _ClassVar[int]
    MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_VMC_ENV_FIELD_NUMBER: _ClassVar[int]
    DAG_ENTITY_HIERARCHY_RESULT_FIELD_NUMBER: _ClassVar[int]
    PK_TO_ENTITY_MAP_FIELD_NUMBER: _ClassVar[int]
    queried_entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    query_vm_tag_hierarchy_error: _error_pb2.ErrorProto
    moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    entity_proto_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    is_vmc_env: bool
    dag_entity_hierarchy_result: _facade_for_entity_manager_pb2.FetchEntityHierarchyDAGResult
    pk_to_entity_map: _containers.MessageMap[str, _vmware_pb2.Entity]
    def __init__(self, queried_entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., query_vm_tag_hierarchy_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., entity_proto_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., is_vmc_env: bool = ..., dag_entity_hierarchy_result: _Optional[_Union[_facade_for_entity_manager_pb2.FetchEntityHierarchyDAGResult, _Mapping]] = ..., pk_to_entity_map: _Optional[_Mapping[str, _vmware_pb2.Entity]] = ...) -> None: ...

class FetchServiceInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchServiceInfoResult(_message.Message):
    __slots__ = ("name", "uuid", "api_type", "api_version", "is_supported", "tag_apis_available", "full_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    API_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    TAG_APIS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    api_type: str
    api_version: str
    is_supported: bool
    tag_apis_available: bool
    full_name: str
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., api_type: _Optional[str] = ..., api_version: _Optional[str] = ..., is_supported: bool = ..., tag_apis_available: bool = ..., full_name: _Optional[str] = ...) -> None: ...

class LocateVMArg(_message.Message):
    __slots__ = ("vm_moref", "vm_uuid", "root_moref", "fetch_vm_datastores", "fetch_xml_vm_config", "fetch_vmx_file", "datacenter_name", "vmware_disk_exclusion_info", "fetch_tags_info", "fetch_custom_attributes_info", "vmware_custom_attributes_map", "keep_xml_vm_config_backup_consistent", "ignore_populate_disks_error")
    class VmwareCustomAttributesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _vmware_pb2.CustomAttribute
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_vmware_pb2.CustomAttribute, _Mapping]] = ...) -> None: ...
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    ROOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    FETCH_VM_DATASTORES_FIELD_NUMBER: _ClassVar[int]
    FETCH_XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FETCH_VMX_FILE_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    VMWARE_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    FETCH_TAGS_INFO_FIELD_NUMBER: _ClassVar[int]
    FETCH_CUSTOM_ATTRIBUTES_INFO_FIELD_NUMBER: _ClassVar[int]
    VMWARE_CUSTOM_ATTRIBUTES_MAP_FIELD_NUMBER: _ClassVar[int]
    KEEP_XML_VM_CONFIG_BACKUP_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_POPULATE_DISKS_ERROR_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    vm_uuid: str
    root_moref: _vmware_common_pb2.MORef
    fetch_vm_datastores: bool
    fetch_xml_vm_config: bool
    fetch_vmx_file: bool
    datacenter_name: str
    vmware_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.VMwareDiskExclusionProto]
    fetch_tags_info: bool
    fetch_custom_attributes_info: bool
    vmware_custom_attributes_map: _containers.MessageMap[int, _vmware_pb2.CustomAttribute]
    keep_xml_vm_config_backup_consistent: bool
    ignore_populate_disks_error: bool
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_uuid: _Optional[str] = ..., root_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., fetch_vm_datastores: bool = ..., fetch_xml_vm_config: bool = ..., fetch_vmx_file: bool = ..., datacenter_name: _Optional[str] = ..., vmware_disk_exclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.VMwareDiskExclusionProto, _Mapping]]] = ..., fetch_tags_info: bool = ..., fetch_custom_attributes_info: bool = ..., vmware_custom_attributes_map: _Optional[_Mapping[int, _vmware_pb2.CustomAttribute]] = ..., keep_xml_vm_config_backup_consistent: bool = ..., ignore_populate_disks_error: bool = ...) -> None: ...

class LocateVMResult(_message.Message):
    __slots__ = ("vm_name", "vm_moref", "vm_uuid", "vm_folder_moref", "vm_vapp_moref", "resource_pool_moref", "host_moref", "host_name", "file_info_list", "virtual_disk_datastore_morefs", "datastore_infos", "change_tracking_enabled", "total_primary_physical_size_bytes", "total_primary_logical_size_bytes", "is_ft_enabled", "is_template", "xml_vm_config", "vmx_file_data", "power_state", "connection_state", "vmware_tools_info", "nic_ip_addr_vec", "consolidation_required", "guest_os_info", "sparse_vm_config", "tag_info_result", "tag_error", "system_resource_info", "version", "custom_attributes_info_result", "vm_nic_vec", "search_domain_vec", "dns_server_vec", "domain_name", "ipv4_gateway", "guest_host_name", "ds_url_pairs", "aggregate_guest_disk_space_used", "is_saas_connector")
    class FileInfo(_message.Message):
        __slots__ = ("name", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str
        def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    class DatastoreInfo(_message.Message):
        __slots__ = ("name", "moref")
        NAME_FIELD_NUMBER: _ClassVar[int]
        MOREF_FIELD_NUMBER: _ClassVar[int]
        name: str
        moref: _vmware_common_pb2.MORef
        def __init__(self, name: _Optional[str] = ..., moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    class FileData(_message.Message):
        __slots__ = ("file_name", "path", "data", "error")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        path: str
        data: bytes
        error: _error_pb2.ErrorProto
        def __init__(self, file_name: _Optional[str] = ..., path: _Optional[str] = ..., data: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class VMwareToolsInfo(_message.Message):
        __slots__ = ("version_status", "running_status")
        VERSION_STATUS_FIELD_NUMBER: _ClassVar[int]
        RUNNING_STATUS_FIELD_NUMBER: _ClassVar[int]
        version_status: _vmware_pb2.VMwareToolsVersionStatus.Type
        running_status: _vmware_pb2.VMwareToolsRunningStatus.Type
        def __init__(self, version_status: _Optional[_Union[_vmware_pb2.VMwareToolsVersionStatus.Type, str]] = ..., running_status: _Optional[_Union[_vmware_pb2.VMwareToolsRunningStatus.Type, str]] = ...) -> None: ...
    class GuestOSInfo(_message.Message):
        __slots__ = ("host_env_type", "os_name", "os_id")
        HOST_ENV_TYPE_FIELD_NUMBER: _ClassVar[int]
        OS_NAME_FIELD_NUMBER: _ClassVar[int]
        OS_ID_FIELD_NUMBER: _ClassVar[int]
        host_env_type: _enums_pb2.HostEnv.Type
        os_name: str
        os_id: str
        def __init__(self, host_env_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., os_name: _Optional[str] = ..., os_id: _Optional[str] = ...) -> None: ...
    class TagInfo(_message.Message):
        __slots__ = ("tag_identifier", "tag_name")
        TAG_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        TAG_NAME_FIELD_NUMBER: _ClassVar[int]
        tag_identifier: str
        tag_name: str
        def __init__(self, tag_identifier: _Optional[str] = ..., tag_name: _Optional[str] = ...) -> None: ...
    class CustomAttributesInfo(_message.Message):
        __slots__ = ("name", "value", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        type: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
    class DsUrlPairsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_VAPP_MOREF_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_DATASTORE_MOREFS_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRIMARY_PHYSICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRIMARY_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_FT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VMX_FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_TOOLS_INFO_FIELD_NUMBER: _ClassVar[int]
    NIC_IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_INFO_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TAG_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    TAG_ERROR_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    VM_NIC_VEC_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    IPV4_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    GUEST_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    DS_URL_PAIRS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_GUEST_DISK_SPACE_USED_FIELD_NUMBER: _ClassVar[int]
    IS_SAAS_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    vm_moref: _vmware_common_pb2.MORef
    vm_uuid: str
    vm_folder_moref: _vmware_common_pb2.MORef
    vm_vapp_moref: _vmware_common_pb2.MORef
    resource_pool_moref: _vmware_common_pb2.MORef
    host_moref: _vmware_common_pb2.MORef
    host_name: str
    file_info_list: _containers.RepeatedCompositeFieldContainer[LocateVMResult.FileInfo]
    virtual_disk_datastore_morefs: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    datastore_infos: _containers.RepeatedCompositeFieldContainer[LocateVMResult.DatastoreInfo]
    change_tracking_enabled: bool
    total_primary_physical_size_bytes: int
    total_primary_logical_size_bytes: int
    is_ft_enabled: bool
    is_template: bool
    xml_vm_config: str
    vmx_file_data: LocateVMResult.FileData
    power_state: _vmware_pb2_1.VirtualMachinePowerState
    connection_state: _vmware_pb2.Entity.ConnectionState
    vmware_tools_info: LocateVMResult.VMwareToolsInfo
    nic_ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
    consolidation_required: bool
    guest_os_info: LocateVMResult.GuestOSInfo
    sparse_vm_config: _vmware_pb2_1.SparseVMConfig
    tag_info_result: _containers.RepeatedCompositeFieldContainer[LocateVMResult.TagInfo]
    tag_error: _error_pb2.ErrorProto
    system_resource_info: _common_pb2.SystemResourceInfo
    version: str
    custom_attributes_info_result: _containers.RepeatedCompositeFieldContainer[LocateVMResult.CustomAttributesInfo]
    vm_nic_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.NICSetting]
    search_domain_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name: str
    ipv4_gateway: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.DeviceGatewayMap]
    guest_host_name: str
    ds_url_pairs: _containers.ScalarMap[str, str]
    aggregate_guest_disk_space_used: int
    is_saas_connector: bool
    def __init__(self, vm_name: _Optional[str] = ..., vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_uuid: _Optional[str] = ..., vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_vapp_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_name: _Optional[str] = ..., file_info_list: _Optional[_Iterable[_Union[LocateVMResult.FileInfo, _Mapping]]] = ..., virtual_disk_datastore_morefs: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., datastore_infos: _Optional[_Iterable[_Union[LocateVMResult.DatastoreInfo, _Mapping]]] = ..., change_tracking_enabled: bool = ..., total_primary_physical_size_bytes: _Optional[int] = ..., total_primary_logical_size_bytes: _Optional[int] = ..., is_ft_enabled: bool = ..., is_template: bool = ..., xml_vm_config: _Optional[str] = ..., vmx_file_data: _Optional[_Union[LocateVMResult.FileData, _Mapping]] = ..., power_state: _Optional[_Union[_vmware_pb2_1.VirtualMachinePowerState, str]] = ..., connection_state: _Optional[_Union[_vmware_pb2.Entity.ConnectionState, str]] = ..., vmware_tools_info: _Optional[_Union[LocateVMResult.VMwareToolsInfo, _Mapping]] = ..., nic_ip_addr_vec: _Optional[_Iterable[str]] = ..., consolidation_required: bool = ..., guest_os_info: _Optional[_Union[LocateVMResult.GuestOSInfo, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[_vmware_pb2_1.SparseVMConfig, _Mapping]] = ..., tag_info_result: _Optional[_Iterable[_Union[LocateVMResult.TagInfo, _Mapping]]] = ..., tag_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., system_resource_info: _Optional[_Union[_common_pb2.SystemResourceInfo, _Mapping]] = ..., version: _Optional[str] = ..., custom_attributes_info_result: _Optional[_Iterable[_Union[LocateVMResult.CustomAttributesInfo, _Mapping]]] = ..., vm_nic_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.NICSetting, _Mapping]]] = ..., search_domain_vec: _Optional[_Iterable[str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name: _Optional[str] = ..., ipv4_gateway: _Optional[_Iterable[_Union[_vmware_pb2_1.DeviceGatewayMap, _Mapping]]] = ..., guest_host_name: _Optional[str] = ..., ds_url_pairs: _Optional[_Mapping[str, str]] = ..., aggregate_guest_disk_space_used: _Optional[int] = ..., is_saas_connector: bool = ...) -> None: ...

class CreateSnapshotArg(_message.Message):
    __slots__ = ("vm_moref", "snapshot_name", "snapshot_description", "enable_change_tracking", "quiesce", "allow_crash_consistent_snapshot")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHANGE_TRACKING_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CRASH_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    snapshot_name: str
    snapshot_description: str
    enable_change_tracking: bool
    quiesce: bool
    allow_crash_consistent_snapshot: bool
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_name: _Optional[str] = ..., snapshot_description: _Optional[str] = ..., enable_change_tracking: bool = ..., quiesce: bool = ..., allow_crash_consistent_snapshot: bool = ...) -> None: ...

class CreateSnapshotResult(_message.Message):
    __slots__ = ("snapshot_moref", "snapshot_id", "snapshot_create_time_secs")
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    snapshot_moref: _vmware_common_pb2.MORef
    snapshot_id: int
    snapshot_create_time_secs: int
    def __init__(self, snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_id: _Optional[int] = ..., snapshot_create_time_secs: _Optional[int] = ...) -> None: ...

class FetchSnapshotInfoArg(_message.Message):
    __slots__ = ("snapshot_moref", "vmware_disk_exclusion_info")
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    VMWARE_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_moref: _vmware_common_pb2.MORef
    vmware_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.VMwareDiskExclusionProto]
    def __init__(self, snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vmware_disk_exclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.VMwareDiskExclusionProto, _Mapping]]] = ...) -> None: ...

class FetchSnapshotInfoResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: _vmware_pb2_1.SnapshotInfo
    def __init__(self, snapshot_info: _Optional[_Union[_vmware_pb2_1.SnapshotInfo, _Mapping]] = ...) -> None: ...

class QueryDiskArg(_message.Message):
    __slots__ = ("vm_moref", "snapshot_moref", "disk_key", "start_offset", "capacity", "previous_change_id", "max_disk_areas")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    DISK_KEY_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_AREAS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    snapshot_moref: _vmware_common_pb2.MORef
    disk_key: int
    start_offset: int
    capacity: int
    previous_change_id: str
    max_disk_areas: int
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disk_key: _Optional[int] = ..., start_offset: _Optional[int] = ..., capacity: _Optional[int] = ..., previous_change_id: _Optional[str] = ..., max_disk_areas: _Optional[int] = ...) -> None: ...

class QueryDiskResult(_message.Message):
    __slots__ = ("disk_areas", "query_disk_error")
    DISK_AREAS_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    disk_areas: _disk_pb2.DiskAreaListProto
    query_disk_error: _error_pb2.ErrorProto
    def __init__(self, disk_areas: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchHostsArg(_message.Message):
    __slots__ = ("host_moref", "resource_pool_moref", "fetch_iqn")
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    FETCH_IQN_FIELD_NUMBER: _ClassVar[int]
    host_moref: _vmware_common_pb2.MORef
    resource_pool_moref: _vmware_common_pb2.MORef
    fetch_iqn: bool
    def __init__(self, host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., fetch_iqn: bool = ...) -> None: ...

class FetchHostsResult(_message.Message):
    __slots__ = ("host_infos", "datastore_info_vec")
    class HostInfo(_message.Message):
        __slots__ = ("moref", "datastore_system_moref", "host_storage_system_moref", "datastore_morefs", "ip_addr_vec", "host_iqn")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        HOST_STORAGE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_MOREFS_FIELD_NUMBER: _ClassVar[int]
        IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
        HOST_IQN_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        datastore_system_moref: _vmware_common_pb2.MORef
        host_storage_system_moref: _vmware_common_pb2.MORef
        datastore_morefs: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
        ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
        host_iqn: str
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_storage_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_morefs: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., ip_addr_vec: _Optional[_Iterable[str]] = ..., host_iqn: _Optional[str] = ...) -> None: ...
    class DatastoreInfo(_message.Message):
        __slots__ = ("moref", "name", "url", "datastore_type", "vmfs_datastore_info", "remote_host", "remote_path", "nas_datastore_info")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
        VMFS_DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
        REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
        REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
        NAS_DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        name: str
        url: str
        datastore_type: _vmware_pb2_1.DatastoreType.Type
        vmfs_datastore_info: _vmware_pb2_1.VmfsDatastoreInfo
        remote_host: str
        remote_path: str
        nas_datastore_info: _vmware_pb2_1.NasDatastoreInfo
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., name: _Optional[str] = ..., url: _Optional[str] = ..., datastore_type: _Optional[_Union[_vmware_pb2_1.DatastoreType.Type, str]] = ..., vmfs_datastore_info: _Optional[_Union[_vmware_pb2_1.VmfsDatastoreInfo, _Mapping]] = ..., remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., nas_datastore_info: _Optional[_Union[_vmware_pb2_1.NasDatastoreInfo, _Mapping]] = ...) -> None: ...
    HOST_INFOS_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    host_infos: _containers.RepeatedCompositeFieldContainer[FetchHostsResult.HostInfo]
    datastore_info_vec: _containers.RepeatedCompositeFieldContainer[FetchHostsResult.DatastoreInfo]
    def __init__(self, host_infos: _Optional[_Iterable[_Union[FetchHostsResult.HostInfo, _Mapping]]] = ..., datastore_info_vec: _Optional[_Iterable[_Union[FetchHostsResult.DatastoreInfo, _Mapping]]] = ...) -> None: ...

class FindChildArg(_message.Message):
    __slots__ = ("parent_moref", "child_name")
    PARENT_MOREF_FIELD_NUMBER: _ClassVar[int]
    CHILD_NAME_FIELD_NUMBER: _ClassVar[int]
    parent_moref: _vmware_common_pb2.MORef
    child_name: str
    def __init__(self, parent_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., child_name: _Optional[str] = ...) -> None: ...

class FindChildResult(_message.Message):
    __slots__ = ("child_moref",)
    CHILD_MOREF_FIELD_NUMBER: _ClassVar[int]
    child_moref: _vmware_common_pb2.MORef
    def __init__(self, child_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class MountDatastoreArg(_message.Message):
    __slots__ = ("remote_host", "remote_path", "nas_path", "datastore_name", "datastore_system_moref", "host_moref")
    REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    remote_host: str
    remote_path: str
    nas_path: _nas_pb2.NasPathProto
    datastore_name: str
    datastore_system_moref: _vmware_common_pb2.MORef
    host_moref: _vmware_common_pb2.MORef
    def __init__(self, remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., nas_path: _Optional[_Union[_nas_pb2.NasPathProto, _Mapping]] = ..., datastore_name: _Optional[str] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class MountDatastoreResult(_message.Message):
    __slots__ = ("mounted_datastore_moref",)
    MOUNTED_DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    mounted_datastore_moref: _vmware_common_pb2.MORef
    def __init__(self, mounted_datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class UnmountDatastoreArg(_message.Message):
    __slots__ = ("datastore_system_moref", "datastore_moref", "disable_sio")
    DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SIO_FIELD_NUMBER: _ClassVar[int]
    datastore_system_moref: _vmware_common_pb2.MORef
    datastore_moref: _vmware_common_pb2.MORef
    disable_sio: bool
    def __init__(self, datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disable_sio: bool = ...) -> None: ...

class UnmountDatastoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MountDatastoreOnRSPoolArg(_message.Message):
    __slots__ = ("remote_host", "remote_path", "nas_path", "datastore_name", "num_hosts_to_mount_datastore", "mounted_datastore_moref", "hosts_without_datastore_list", "host_info_list", "resource_pool_moref", "host_moref_vec")
    REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_HOSTS_TO_MOUNT_DATASTORE_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOSTS_WITHOUT_DATASTORE_LIST_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    remote_host: str
    remote_path: str
    nas_path: _nas_pb2.NasPathProto
    datastore_name: str
    num_hosts_to_mount_datastore: int
    mounted_datastore_moref: _vmware_common_pb2.MORef
    hosts_without_datastore_list: _containers.RepeatedCompositeFieldContainer[FetchHostsResult.HostInfo]
    host_info_list: _containers.RepeatedCompositeFieldContainer[MountDatastoreOnRSPoolResult.HostInfo]
    resource_pool_moref: _vmware_common_pb2.MORef
    host_moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    def __init__(self, remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., nas_path: _Optional[_Union[_nas_pb2.NasPathProto, _Mapping]] = ..., datastore_name: _Optional[str] = ..., num_hosts_to_mount_datastore: _Optional[int] = ..., mounted_datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., hosts_without_datastore_list: _Optional[_Iterable[_Union[FetchHostsResult.HostInfo, _Mapping]]] = ..., host_info_list: _Optional[_Iterable[_Union[MountDatastoreOnRSPoolResult.HostInfo, _Mapping]]] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ...) -> None: ...

class MountDatastoreOnRSPoolResult(_message.Message):
    __slots__ = ("datastore_name", "host_info_list", "mounted_datastore_moref")
    class HostInfo(_message.Message):
        __slots__ = ("moref", "datastore_system_moref")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        datastore_system_moref: _vmware_common_pb2.MORef
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    datastore_name: str
    host_info_list: _containers.RepeatedCompositeFieldContainer[MountDatastoreOnRSPoolResult.HostInfo]
    mounted_datastore_moref: _vmware_common_pb2.MORef
    def __init__(self, datastore_name: _Optional[str] = ..., host_info_list: _Optional[_Iterable[_Union[MountDatastoreOnRSPoolResult.HostInfo, _Mapping]]] = ..., mounted_datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class UnmountDatastoreFromDCArg(_message.Message):
    __slots__ = ("datastore_moref", "datastore_system_moref_list")
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_SYSTEM_MOREF_LIST_FIELD_NUMBER: _ClassVar[int]
    datastore_moref: _vmware_common_pb2.MORef
    datastore_system_moref_list: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    def __init__(self, datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref_list: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ...) -> None: ...

class UnmountDatastoreFromDCResult(_message.Message):
    __slots__ = ("num_hosts_succeeded", "num_hosts_failed")
    NUM_HOSTS_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    NUM_HOSTS_FAILED_FIELD_NUMBER: _ClassVar[int]
    num_hosts_succeeded: int
    num_hosts_failed: int
    def __init__(self, num_hosts_succeeded: _Optional[int] = ..., num_hosts_failed: _Optional[int] = ...) -> None: ...

class MountLunCopyArg(_message.Message):
    __slots__ = ("serial_number", "datastore_system_moref", "host_storage_system_moref", "host_system_moref", "host_name")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_STORAGE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    datastore_system_moref: _vmware_common_pb2.MORef
    host_storage_system_moref: _vmware_common_pb2.MORef
    host_system_moref: _vmware_common_pb2.MORef
    host_name: str
    def __init__(self, serial_number: _Optional[str] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_storage_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_name: _Optional[str] = ...) -> None: ...

class MountLunCopyResult(_message.Message):
    __slots__ = ("mounted_datastore_moref",)
    MOUNTED_DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    mounted_datastore_moref: _vmware_common_pb2.MORef
    def __init__(self, mounted_datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class MountLunCopyOnRSPoolArg(_message.Message):
    __slots__ = ("serial_number", "datastore_name", "resource_pool_moref", "num_hosts_to_mount_datastore", "rescan_all_hbas", "host_moref_vec")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    NUM_HOSTS_TO_MOUNT_DATASTORE_FIELD_NUMBER: _ClassVar[int]
    RESCAN_ALL_HBAS_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    datastore_name: str
    resource_pool_moref: _vmware_common_pb2.MORef
    num_hosts_to_mount_datastore: int
    rescan_all_hbas: bool
    host_moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    def __init__(self, serial_number: _Optional[str] = ..., datastore_name: _Optional[str] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., num_hosts_to_mount_datastore: _Optional[int] = ..., rescan_all_hbas: bool = ..., host_moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ...) -> None: ...

class MountLunCopyOnRSPoolResult(_message.Message):
    __slots__ = ("datastore_name", "host_info_list", "mounted_datastore_moref")
    class HostInfo(_message.Message):
        __slots__ = ("moref", "datastore_system_moref")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        datastore_system_moref: _vmware_common_pb2.MORef
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    datastore_name: str
    host_info_list: _containers.RepeatedCompositeFieldContainer[MountLunCopyOnRSPoolResult.HostInfo]
    mounted_datastore_moref: _vmware_common_pb2.MORef
    def __init__(self, datastore_name: _Optional[str] = ..., host_info_list: _Optional[_Iterable[_Union[MountLunCopyOnRSPoolResult.HostInfo, _Mapping]]] = ..., mounted_datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class LocateDatastoreArg(_message.Message):
    __slots__ = ("datastore_moref",)
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    datastore_moref: _vmware_common_pb2.MORef
    def __init__(self, datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class LocateDatastoreResult(_message.Message):
    __slots__ = ("datastore_name", "host_info_list", "vm_entity_list", "parent_folder_moref", "datastore_type", "vmfs_datastore_info", "nas_datastore_info", "free_space", "capacity", "url", "is_top_level_directory_create_supported", "accessible")
    class HostInfo(_message.Message):
        __slots__ = ("moref", "datastore_system_moref", "storage_system_moref")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        STORAGE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        datastore_system_moref: _vmware_common_pb2.MORef
        storage_system_moref: _vmware_common_pb2.MORef
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., storage_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_LIST_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VMFS_DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    NAS_DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    FREE_SPACE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    IS_TOP_LEVEL_DIRECTORY_CREATE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBLE_FIELD_NUMBER: _ClassVar[int]
    datastore_name: str
    host_info_list: _containers.RepeatedCompositeFieldContainer[LocateDatastoreResult.HostInfo]
    vm_entity_list: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.Entity]
    parent_folder_moref: _vmware_common_pb2.MORef
    datastore_type: _vmware_pb2_1.DatastoreType.Type
    vmfs_datastore_info: _vmware_pb2_1.VmfsDatastoreInfo
    nas_datastore_info: _vmware_pb2_1.NasDatastoreInfo
    free_space: int
    capacity: int
    url: str
    is_top_level_directory_create_supported: bool
    accessible: bool
    def __init__(self, datastore_name: _Optional[str] = ..., host_info_list: _Optional[_Iterable[_Union[LocateDatastoreResult.HostInfo, _Mapping]]] = ..., vm_entity_list: _Optional[_Iterable[_Union[_vmware_pb2.Entity, _Mapping]]] = ..., parent_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_type: _Optional[_Union[_vmware_pb2_1.DatastoreType.Type, str]] = ..., vmfs_datastore_info: _Optional[_Union[_vmware_pb2_1.VmfsDatastoreInfo, _Mapping]] = ..., nas_datastore_info: _Optional[_Union[_vmware_pb2_1.NasDatastoreInfo, _Mapping]] = ..., free_space: _Optional[int] = ..., capacity: _Optional[int] = ..., url: _Optional[str] = ..., is_top_level_directory_create_supported: bool = ..., accessible: bool = ...) -> None: ...

class RemoveVMFSDatastoreArg(_message.Message):
    __slots__ = ("datastore_system_moref", "storage_system_moref", "datastore_moref", "vmfs_datastore_info", "disable_sio", "request_type")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnmountVMFS: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
        kRemoveDatastore: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
        kDetachLUN: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
        kUnspecified: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
        kRescanHBA: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
        kDeleteVMFS: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
        kDeleteLunState: _ClassVar[RemoveVMFSDatastoreArg.RequestType]
    kUnmountVMFS: RemoveVMFSDatastoreArg.RequestType
    kRemoveDatastore: RemoveVMFSDatastoreArg.RequestType
    kDetachLUN: RemoveVMFSDatastoreArg.RequestType
    kUnspecified: RemoveVMFSDatastoreArg.RequestType
    kRescanHBA: RemoveVMFSDatastoreArg.RequestType
    kDeleteVMFS: RemoveVMFSDatastoreArg.RequestType
    kDeleteLunState: RemoveVMFSDatastoreArg.RequestType
    DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    VMFS_DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SIO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    datastore_system_moref: _vmware_common_pb2.MORef
    storage_system_moref: _vmware_common_pb2.MORef
    datastore_moref: _vmware_common_pb2.MORef
    vmfs_datastore_info: _vmware_pb2_1.VmfsDatastoreInfo
    disable_sio: bool
    request_type: RemoveVMFSDatastoreArg.RequestType
    def __init__(self, datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., storage_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vmfs_datastore_info: _Optional[_Union[_vmware_pb2_1.VmfsDatastoreInfo, _Mapping]] = ..., disable_sio: bool = ..., request_type: _Optional[_Union[RemoveVMFSDatastoreArg.RequestType, str]] = ...) -> None: ...

class RemoveVMFSDatastoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveVMFSDatastoreFromDCArg(_message.Message):
    __slots__ = ("datastore_moref", "remove_inactive_datastore_only_once")
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    REMOVE_INACTIVE_DATASTORE_ONLY_ONCE_FIELD_NUMBER: _ClassVar[int]
    datastore_moref: _vmware_common_pb2.MORef
    remove_inactive_datastore_only_once: bool
    def __init__(self, datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., remove_inactive_datastore_only_once: bool = ...) -> None: ...

class RemoveVMFSDatastoreFromDCResult(_message.Message):
    __slots__ = ("num_hosts_succeeded", "num_hosts_failed")
    NUM_HOSTS_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    NUM_HOSTS_FAILED_FIELD_NUMBER: _ClassVar[int]
    num_hosts_succeeded: int
    num_hosts_failed: int
    def __init__(self, num_hosts_succeeded: _Optional[int] = ..., num_hosts_failed: _Optional[int] = ...) -> None: ...

class DeleteSnapshotArg(_message.Message):
    __slots__ = ("vm_moref", "snapshot_moref", "remove_all", "consolidate")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALL_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATE_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    snapshot_moref: _vmware_common_pb2.MORef
    remove_all: bool
    consolidate: bool
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., remove_all: bool = ..., consolidate: bool = ...) -> None: ...

class DeleteSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevertToCurrentSnapshotArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class RevertToCurrentSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetScsiDiskDeviceInfoArg(_message.Message):
    __slots__ = ("datastore_moref", "host_system_moref", "scsi_disk_name")
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    SCSI_DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    datastore_moref: _vmware_common_pb2.MORef
    host_system_moref: _vmware_common_pb2.MORef
    scsi_disk_name: str
    def __init__(self, datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., scsi_disk_name: _Optional[str] = ...) -> None: ...

class GetScsiDiskDeviceInfoResult(_message.Message):
    __slots__ = ("serial_number", "uuid", "san_port_list")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SAN_PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    uuid: str
    san_port_list: _containers.RepeatedCompositeFieldContainer[_san_pb2.SanPort]
    def __init__(self, serial_number: _Optional[str] = ..., uuid: _Optional[str] = ..., san_port_list: _Optional[_Iterable[_Union[_san_pb2.SanPort, _Mapping]]] = ...) -> None: ...

class MetricIdProto(_message.Message):
    __slots__ = ("id", "instance", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    instance: str
    name: str
    def __init__(self, id: _Optional[int] = ..., instance: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class EntityMetricIdsProto(_message.Message):
    __slots__ = ("entity_moref", "metric_ids")
    ENTITY_MOREF_FIELD_NUMBER: _ClassVar[int]
    METRIC_IDS_FIELD_NUMBER: _ClassVar[int]
    entity_moref: _vmware_common_pb2.MORef
    metric_ids: _containers.RepeatedCompositeFieldContainer[MetricIdProto]
    def __init__(self, entity_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., metric_ids: _Optional[_Iterable[_Union[MetricIdProto, _Mapping]]] = ...) -> None: ...

class QueryAvailableMetricIdsArg(_message.Message):
    __slots__ = ("entity_morefs", "interval_secs", "historical_duration_secs")
    ENTITY_MOREFS_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    entity_morefs: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    interval_secs: int
    historical_duration_secs: int
    def __init__(self, entity_morefs: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., interval_secs: _Optional[int] = ..., historical_duration_secs: _Optional[int] = ...) -> None: ...

class QueryAvailableMetricIdsResult(_message.Message):
    __slots__ = ("entity_metric_ids_vec",)
    ENTITY_METRIC_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_metric_ids_vec: _containers.RepeatedCompositeFieldContainer[EntityMetricIdsProto]
    def __init__(self, entity_metric_ids_vec: _Optional[_Iterable[_Union[EntityMetricIdsProto, _Mapping]]] = ...) -> None: ...

class MoveIntoFolderArg(_message.Message):
    __slots__ = ("folder_moref", "entity_moref")
    FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MOREF_FIELD_NUMBER: _ClassVar[int]
    folder_moref: _vmware_common_pb2.MORef
    entity_moref: _vmware_common_pb2.MORef
    def __init__(self, folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., entity_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class MoveIntoFolderResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchMORefsPropertiesArg(_message.Message):
    __slots__ = ("morefs", "property_names", "entity_info_params")
    class EntityInfoParams(_message.Message):
        __slots__ = ("entity_type_to_properties_map", "populate_vm_bios_uuid", "preferred_subnet_vec")
        class PropertiesList(_message.Message):
            __slots__ = ("property_names",)
            PROPERTY_NAMES_FIELD_NUMBER: _ClassVar[int]
            property_names: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, property_names: _Optional[_Iterable[str]] = ...) -> None: ...
        class EntityTypeToPropertiesMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: FetchMORefsPropertiesArg.EntityInfoParams.PropertiesList
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FetchMORefsPropertiesArg.EntityInfoParams.PropertiesList, _Mapping]] = ...) -> None: ...
        ENTITY_TYPE_TO_PROPERTIES_MAP_FIELD_NUMBER: _ClassVar[int]
        POPULATE_VM_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
        PREFERRED_SUBNET_VEC_FIELD_NUMBER: _ClassVar[int]
        entity_type_to_properties_map: _containers.MessageMap[str, FetchMORefsPropertiesArg.EntityInfoParams.PropertiesList]
        populate_vm_bios_uuid: bool
        preferred_subnet_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
        def __init__(self, entity_type_to_properties_map: _Optional[_Mapping[str, FetchMORefsPropertiesArg.EntityInfoParams.PropertiesList]] = ..., populate_vm_bios_uuid: bool = ..., preferred_subnet_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ...) -> None: ...
    MOREFS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAMES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_INFO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    morefs: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    property_names: _containers.RepeatedScalarFieldContainer[str]
    entity_info_params: FetchMORefsPropertiesArg.EntityInfoParams
    def __init__(self, morefs: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., property_names: _Optional[_Iterable[str]] = ..., entity_info_params: _Optional[_Union[FetchMORefsPropertiesArg.EntityInfoParams, _Mapping]] = ...) -> None: ...

class FetchMORefsPropertiesResult(_message.Message):
    __slots__ = ("morefs_properties",)
    class MORefProperties(_message.Message):
        __slots__ = ("moref", "string_type_properties", "moref_type_properties", "vmware_entity")
        class StringTypePropertiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class MorefTypePropertiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _vmware_common_pb2.MORef
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
        MOREF_FIELD_NUMBER: _ClassVar[int]
        STRING_TYPE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        MOREF_TYPE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        VMWARE_ENTITY_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        string_type_properties: _containers.ScalarMap[str, str]
        moref_type_properties: _containers.MessageMap[str, _vmware_common_pb2.MORef]
        vmware_entity: _vmware_pb2.Entity
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., string_type_properties: _Optional[_Mapping[str, str]] = ..., moref_type_properties: _Optional[_Mapping[str, _vmware_common_pb2.MORef]] = ..., vmware_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ...) -> None: ...
    MOREFS_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    morefs_properties: _containers.RepeatedCompositeFieldContainer[FetchMORefsPropertiesResult.MORefProperties]
    def __init__(self, morefs_properties: _Optional[_Iterable[_Union[FetchMORefsPropertiesResult.MORefProperties, _Mapping]]] = ...) -> None: ...

class FetchNetworkInfoArg(_message.Message):
    __slots__ = ("network_object_moref",)
    NETWORK_OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    network_object_moref: _vmware_common_pb2.MORef
    def __init__(self, network_object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchNetworkInfoResult(_message.Message):
    __slots__ = ("vswitch_network_info", "dv_port_group_info", "opaque_network_info")
    VSWITCH_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    DV_PORT_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    vswitch_network_info: _vmware_pb2_1.VSwitchNetworkInfo
    dv_port_group_info: _vmware_pb2_1.DVPortGroupInfo
    opaque_network_info: _vmware_pb2_1.OpaqueNetworkInfo
    def __init__(self, vswitch_network_info: _Optional[_Union[_vmware_pb2_1.VSwitchNetworkInfo, _Mapping]] = ..., dv_port_group_info: _Optional[_Union[_vmware_pb2_1.DVPortGroupInfo, _Mapping]] = ..., opaque_network_info: _Optional[_Union[_vmware_pb2_1.OpaqueNetworkInfo, _Mapping]] = ...) -> None: ...

class EntityMetricSetProto(_message.Message):
    __slots__ = ("entity_moref", "timestamp_secs_vec", "metric_values_vec")
    class MetricValues(_message.Message):
        __slots__ = ("metric_id", "values")
        METRIC_ID_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        metric_id: MetricIdProto
        values: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, metric_id: _Optional[_Union[MetricIdProto, _Mapping]] = ..., values: _Optional[_Iterable[int]] = ...) -> None: ...
    ENTITY_MOREF_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_SECS_VEC_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUES_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_moref: _vmware_common_pb2.MORef
    timestamp_secs_vec: _containers.RepeatedScalarFieldContainer[int]
    metric_values_vec: _containers.RepeatedCompositeFieldContainer[EntityMetricSetProto.MetricValues]
    def __init__(self, entity_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., timestamp_secs_vec: _Optional[_Iterable[int]] = ..., metric_values_vec: _Optional[_Iterable[_Union[EntityMetricSetProto.MetricValues, _Mapping]]] = ...) -> None: ...

class QueryMetricsArg(_message.Message):
    __slots__ = ("entity_metric_ids_vec", "interval_secs")
    ENTITY_METRIC_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_SECS_FIELD_NUMBER: _ClassVar[int]
    entity_metric_ids_vec: _containers.RepeatedCompositeFieldContainer[EntityMetricIdsProto]
    interval_secs: int
    def __init__(self, entity_metric_ids_vec: _Optional[_Iterable[_Union[EntityMetricIdsProto, _Mapping]]] = ..., interval_secs: _Optional[int] = ...) -> None: ...

class QueryMetricsResult(_message.Message):
    __slots__ = ("entity_metric_set_vec",)
    ENTITY_METRIC_SET_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_metric_set_vec: _containers.RepeatedCompositeFieldContainer[EntityMetricSetProto]
    def __init__(self, entity_metric_set_vec: _Optional[_Iterable[_Union[EntityMetricSetProto, _Mapping]]] = ...) -> None: ...

class EnableSIOStatsCollectionArg(_message.Message):
    __slots__ = ("datastore_morefs",)
    DATASTORE_MOREFS_FIELD_NUMBER: _ClassVar[int]
    datastore_morefs: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    def __init__(self, datastore_morefs: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ...) -> None: ...

class EnableSIOStatsCollectionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchDatacenterArg(_message.Message):
    __slots__ = ("resource_pool_moref",)
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    resource_pool_moref: _vmware_common_pb2.MORef
    def __init__(self, resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchDatacenterResult(_message.Message):
    __slots__ = ("datacenter_entity",)
    DATACENTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    datacenter_entity: _vmware_pb2.Entity
    def __init__(self, datacenter_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ...) -> None: ...

class CreateVMFolderArg(_message.Message):
    __slots__ = ("vm_folder_name", "datacenter_moref", "is_vmc_env")
    VM_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    IS_VMC_ENV_FIELD_NUMBER: _ClassVar[int]
    vm_folder_name: str
    datacenter_moref: _vmware_common_pb2.MORef
    is_vmc_env: bool
    def __init__(self, vm_folder_name: _Optional[str] = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., is_vmc_env: bool = ...) -> None: ...

class CreateVMFolderResult(_message.Message):
    __slots__ = ("vm_folder_moref",)
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_folder_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchVMDiskDeviceInfoArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchVMDiskDeviceInfoResult(_message.Message):
    __slots__ = ("virtual_disk_controller_info_vec", "virtual_disk_device_info_vec", "non_disk_virtual_device_info_vec")
    VIRTUAL_DISK_CONTROLLER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_DEVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NON_DISK_VIRTUAL_DEVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disk_controller_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskControllerInfo]
    virtual_disk_device_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskDeviceInfo]
    non_disk_virtual_device_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDeviceInfo]
    def __init__(self, virtual_disk_controller_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskControllerInfo, _Mapping]]] = ..., virtual_disk_device_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskDeviceInfo, _Mapping]]] = ..., non_disk_virtual_device_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDeviceInfo, _Mapping]]] = ...) -> None: ...

class AttachDisksSpec(_message.Message):
    __slots__ = ("relative_path", "unit_number", "controller_key", "disk_id", "additional_vmdk_info")
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_VMDK_INFO_FIELD_NUMBER: _ClassVar[int]
    relative_path: str
    unit_number: int
    controller_key: int
    disk_id: str
    additional_vmdk_info: _vmware_pb2_1.AdditionalVMDKInformation
    def __init__(self, relative_path: _Optional[str] = ..., unit_number: _Optional[int] = ..., controller_key: _Optional[int] = ..., disk_id: _Optional[str] = ..., additional_vmdk_info: _Optional[_Union[_vmware_pb2_1.AdditionalVMDKInformation, _Mapping]] = ...) -> None: ...

class AttachVirtualDisksToVMArg(_message.Message):
    __slots__ = ("vm_moref", "virtual_disk_controller_info_vec", "virtual_disk_device_info_vec", "datastore_moref", "datastore_name", "virtual_disk_mode", "relative_file_path_vec", "create_new", "capacity_bytes_vec", "original_disk_unit_number_map", "attach_disks_params", "should_pick_globally_unique", "disk_provision_type", "old_to_new_disk_uuid_map", "vm_version", "skip_controller_check", "is_vmc_env", "device_key_vec", "type", "relative_file_disk_info", "existing_disk_handling")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAddExistingDisk: _ClassVar[AttachVirtualDisksToVMArg.RequestType]
        kCreateAndAddDisk: _ClassVar[AttachVirtualDisksToVMArg.RequestType]
        kEditAttachedDiskFileName: _ClassVar[AttachVirtualDisksToVMArg.RequestType]
    kAddExistingDisk: AttachVirtualDisksToVMArg.RequestType
    kCreateAndAddDisk: AttachVirtualDisksToVMArg.RequestType
    kEditAttachedDiskFileName: AttachVirtualDisksToVMArg.RequestType
    class ExistingDiskHandling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kControllerKeyUnitNumber: _ClassVar[AttachVirtualDisksToVMArg.ExistingDiskHandling]
        kVirtualDiskPath: _ClassVar[AttachVirtualDisksToVMArg.ExistingDiskHandling]
    kControllerKeyUnitNumber: AttachVirtualDisksToVMArg.ExistingDiskHandling
    kVirtualDiskPath: AttachVirtualDisksToVMArg.ExistingDiskHandling
    class OriginalDiskUnitNumberMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class AttachDisksParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttachDisksSpec
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttachDisksSpec, _Mapping]] = ...) -> None: ...
    class OldToNewDiskUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RelativeFileDiskInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttachDisksSpec
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AttachDisksSpec, _Mapping]] = ...) -> None: ...
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_CONTROLLER_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_DEVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_MODE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_VEC_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DISK_UNIT_NUMBER_MAP_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DISKS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_PICK_GLOBALLY_UNIQUE_FIELD_NUMBER: _ClassVar[int]
    DISK_PROVISION_TYPE_FIELD_NUMBER: _ClassVar[int]
    OLD_TO_NEW_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    VM_VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_CONTROLLER_CHECK_FIELD_NUMBER: _ClassVar[int]
    IS_VMC_ENV_FIELD_NUMBER: _ClassVar[int]
    DEVICE_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_FILE_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    EXISTING_DISK_HANDLING_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    virtual_disk_controller_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskControllerInfo]
    virtual_disk_device_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskDeviceInfo]
    datastore_moref: _vmware_common_pb2.MORef
    datastore_name: str
    virtual_disk_mode: _vmware_pb2.VirtualDiskMode.Type
    relative_file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    create_new: bool
    capacity_bytes_vec: _containers.RepeatedScalarFieldContainer[int]
    original_disk_unit_number_map: _containers.ScalarMap[str, int]
    attach_disks_params: _containers.MessageMap[str, AttachDisksSpec]
    should_pick_globally_unique: bool
    disk_provision_type: DiskProvisionType
    old_to_new_disk_uuid_map: _containers.ScalarMap[str, str]
    vm_version: str
    skip_controller_check: bool
    is_vmc_env: bool
    device_key_vec: _containers.RepeatedScalarFieldContainer[int]
    type: AttachVirtualDisksToVMArg.RequestType
    relative_file_disk_info: _containers.MessageMap[str, AttachDisksSpec]
    existing_disk_handling: AttachVirtualDisksToVMArg.ExistingDiskHandling
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., virtual_disk_controller_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskControllerInfo, _Mapping]]] = ..., virtual_disk_device_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskDeviceInfo, _Mapping]]] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_name: _Optional[str] = ..., virtual_disk_mode: _Optional[_Union[_vmware_pb2.VirtualDiskMode.Type, str]] = ..., relative_file_path_vec: _Optional[_Iterable[str]] = ..., create_new: bool = ..., capacity_bytes_vec: _Optional[_Iterable[int]] = ..., original_disk_unit_number_map: _Optional[_Mapping[str, int]] = ..., attach_disks_params: _Optional[_Mapping[str, AttachDisksSpec]] = ..., should_pick_globally_unique: bool = ..., disk_provision_type: _Optional[_Union[DiskProvisionType, str]] = ..., old_to_new_disk_uuid_map: _Optional[_Mapping[str, str]] = ..., vm_version: _Optional[str] = ..., skip_controller_check: bool = ..., is_vmc_env: bool = ..., device_key_vec: _Optional[_Iterable[int]] = ..., type: _Optional[_Union[AttachVirtualDisksToVMArg.RequestType, str]] = ..., relative_file_disk_info: _Optional[_Mapping[str, AttachDisksSpec]] = ..., existing_disk_handling: _Optional[_Union[AttachVirtualDisksToVMArg.ExistingDiskHandling, str]] = ...) -> None: ...

class AttachVirtualDisksToVMResult(_message.Message):
    __slots__ = ("virtual_disk_device_info_vec",)
    VIRTUAL_DISK_DEVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disk_device_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskDeviceInfo]
    def __init__(self, virtual_disk_device_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskDeviceInfo, _Mapping]]] = ...) -> None: ...

class DetachVirtualDisksFromVMArg(_message.Message):
    __slots__ = ("vm_moref", "virtual_disk_device_info_vec", "virtual_disk_device_info_vec_to_destroy")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_DEVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_DEVICE_INFO_VEC_TO_DESTROY_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    virtual_disk_device_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskDeviceInfo]
    virtual_disk_device_info_vec_to_destroy: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskDeviceInfo]
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., virtual_disk_device_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskDeviceInfo, _Mapping]]] = ..., virtual_disk_device_info_vec_to_destroy: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskDeviceInfo, _Mapping]]] = ...) -> None: ...

class DetachVirtualDisksFromVMResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerOnVMArg(_message.Message):
    __slots__ = ("datacenter_moref", "vm_moref")
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    datacenter_moref: _vmware_common_pb2.MORef
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class PowerOnVMResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerOffVMArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class PowerOffVMResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelocateVMDatastoreArg(_message.Message):
    __slots__ = ("vm_moref", "datastore_moref", "virtual_disk_relocate_specs", "relocate_virtual_disks_only")
    class VirtualDiskRelocateSpec(_message.Message):
        __slots__ = ("key", "datastore_moref", "disk_type", "is_thin_provisioned", "thick_eager_scrub_provision")
        KEY_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
        DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_THIN_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
        THICK_EAGER_SCRUB_PROVISION_FIELD_NUMBER: _ClassVar[int]
        key: int
        datastore_moref: _vmware_common_pb2.MORef
        disk_type: int
        is_thin_provisioned: bool
        thick_eager_scrub_provision: bool
        def __init__(self, key: _Optional[int] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disk_type: _Optional[int] = ..., is_thin_provisioned: bool = ..., thick_eager_scrub_provision: bool = ...) -> None: ...
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_RELOCATE_SPECS_FIELD_NUMBER: _ClassVar[int]
    RELOCATE_VIRTUAL_DISKS_ONLY_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    datastore_moref: _vmware_common_pb2.MORef
    virtual_disk_relocate_specs: _containers.RepeatedCompositeFieldContainer[RelocateVMDatastoreArg.VirtualDiskRelocateSpec]
    relocate_virtual_disks_only: bool
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., virtual_disk_relocate_specs: _Optional[_Iterable[_Union[RelocateVMDatastoreArg.VirtualDiskRelocateSpec, _Mapping]]] = ..., relocate_virtual_disks_only: bool = ...) -> None: ...

class RelocateVMDatastoreResult(_message.Message):
    __slots__ = ("task_moref",)
    TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    task_moref: _vmware_common_pb2.MORef
    def __init__(self, task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class UnregisterVMArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class UnregisterVMResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DestroyObjectArg(_message.Message):
    __slots__ = ("object_moref", "unregister")
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    unregister: bool
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., unregister: bool = ...) -> None: ...

class DestroyObjectResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchVMSnapshotsArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchVMSnapshotsResult(_message.Message):
    __slots__ = ("snapshot_infos",)
    class SnapshotInfo(_message.Message):
        __slots__ = ("name", "id", "moref", "quiesce_requested", "is_quiesced", "create_time_secs")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MOREF_FIELD_NUMBER: _ClassVar[int]
        QUIESCE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        IS_QUIESCED_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        name: str
        id: int
        moref: _vmware_common_pb2.MORef
        quiesce_requested: bool
        is_quiesced: bool
        create_time_secs: int
        def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ..., moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., quiesce_requested: bool = ..., is_quiesced: bool = ..., create_time_secs: _Optional[int] = ...) -> None: ...
    SNAPSHOT_INFOS_FIELD_NUMBER: _ClassVar[int]
    snapshot_infos: _containers.RepeatedCompositeFieldContainer[FetchVMSnapshotsResult.SnapshotInfo]
    def __init__(self, snapshot_infos: _Optional[_Iterable[_Union[FetchVMSnapshotsResult.SnapshotInfo, _Mapping]]] = ...) -> None: ...

class ConsolidateVMDisksArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class ConsolidateVMDisksResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateVMArg(_message.Message):
    __slots__ = ("vm_name", "xml_vm_config", "vm_folder_moref", "vm_vapp_moref", "resource_pool_moref", "host_moref", "datastore_name", "datastore_moref", "datastore_path_prefix", "include_original_datastore_name_in_path_prefix", "network_config_info", "create_blank_disks", "apply_recovered_tags", "tag_attributes_vec", "reset_bios_uuid", "apply_custom_attributes", "custom_attributes_vec", "fail_if_network_not_attached", "vm_temp_name", "should_rename", "use_vm_name_for_path", "vm_folder_suffix_in_path", "use_original_datastore", "vcd_vcenter_vm_name", "skip_attach_network", "old_to_new_datastore_name_map", "use_disk_paths_from_vmx", "datacenter_name", "controller_key_to_type_map", "delete_vmx_file_from_datastore", "datacenter_moref", "disk_provision_type", "nvram_file_name")
    class NetworkConfig(_message.Message):
        __slots__ = ("network_state_change", "vswitch_network_info", "dv_port_group_info", "opaque_network_info", "preserve_mac_address_on_new_network")
        NETWORK_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        VSWITCH_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
        DV_PORT_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
        OPAQUE_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
        PRESERVE_MAC_ADDRESS_ON_NEW_NETWORK_FIELD_NUMBER: _ClassVar[int]
        network_state_change: _vmware_pb2_1.NetworkConfigInfo.NetworkStateChange
        vswitch_network_info: _vmware_pb2_1.VSwitchNetworkInfo
        dv_port_group_info: _vmware_pb2_1.DVPortGroupInfo
        opaque_network_info: _vmware_pb2_1.OpaqueNetworkInfo
        preserve_mac_address_on_new_network: bool
        def __init__(self, network_state_change: _Optional[_Union[_vmware_pb2_1.NetworkConfigInfo.NetworkStateChange, str]] = ..., vswitch_network_info: _Optional[_Union[_vmware_pb2_1.VSwitchNetworkInfo, _Mapping]] = ..., dv_port_group_info: _Optional[_Union[_vmware_pb2_1.DVPortGroupInfo, _Mapping]] = ..., opaque_network_info: _Optional[_Union[_vmware_pb2_1.OpaqueNetworkInfo, _Mapping]] = ..., preserve_mac_address_on_new_network: bool = ...) -> None: ...
    class OldToNewDatastoreNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ControllerKeyToTypeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_VAPP_MOREF_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ORIGINAL_DATASTORE_NAME_IN_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_BLANK_DISKS_FIELD_NUMBER: _ClassVar[int]
    APPLY_RECOVERED_TAGS_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    RESET_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    APPLY_CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    FAIL_IF_NETWORK_NOT_ATTACHED_FIELD_NUMBER: _ClassVar[int]
    VM_TEMP_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RENAME_FIELD_NUMBER: _ClassVar[int]
    USE_VM_NAME_FOR_PATH_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_SUFFIX_IN_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_ORIGINAL_DATASTORE_FIELD_NUMBER: _ClassVar[int]
    VCD_VCENTER_VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_ATTACH_NETWORK_FIELD_NUMBER: _ClassVar[int]
    OLD_TO_NEW_DATASTORE_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    USE_DISK_PATHS_FROM_VMX_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_TO_TYPE_MAP_FIELD_NUMBER: _ClassVar[int]
    DELETE_VMX_FILE_FROM_DATASTORE_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    DISK_PROVISION_TYPE_FIELD_NUMBER: _ClassVar[int]
    NVRAM_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    xml_vm_config: str
    vm_folder_moref: _vmware_common_pb2.MORef
    vm_vapp_moref: _vmware_common_pb2.MORef
    resource_pool_moref: _vmware_common_pb2.MORef
    host_moref: _vmware_common_pb2.MORef
    datastore_name: str
    datastore_moref: _vmware_common_pb2.MORef
    datastore_path_prefix: str
    include_original_datastore_name_in_path_prefix: bool
    network_config_info: CreateVMArg.NetworkConfig
    create_blank_disks: bool
    apply_recovered_tags: bool
    tag_attributes_vec: _containers.RepeatedScalarFieldContainer[str]
    reset_bios_uuid: bool
    apply_custom_attributes: bool
    custom_attributes_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.CustomAttribute]
    fail_if_network_not_attached: bool
    vm_temp_name: str
    should_rename: bool
    use_vm_name_for_path: bool
    vm_folder_suffix_in_path: str
    use_original_datastore: bool
    vcd_vcenter_vm_name: str
    skip_attach_network: bool
    old_to_new_datastore_name_map: _containers.ScalarMap[str, str]
    use_disk_paths_from_vmx: bool
    datacenter_name: str
    controller_key_to_type_map: _containers.ScalarMap[int, str]
    delete_vmx_file_from_datastore: bool
    datacenter_moref: _vmware_common_pb2.MORef
    disk_provision_type: DiskProvisionType
    nvram_file_name: str
    def __init__(self, vm_name: _Optional[str] = ..., xml_vm_config: _Optional[str] = ..., vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_vapp_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_name: _Optional[str] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_path_prefix: _Optional[str] = ..., include_original_datastore_name_in_path_prefix: bool = ..., network_config_info: _Optional[_Union[CreateVMArg.NetworkConfig, _Mapping]] = ..., create_blank_disks: bool = ..., apply_recovered_tags: bool = ..., tag_attributes_vec: _Optional[_Iterable[str]] = ..., reset_bios_uuid: bool = ..., apply_custom_attributes: bool = ..., custom_attributes_vec: _Optional[_Iterable[_Union[_vmware_pb2.CustomAttribute, _Mapping]]] = ..., fail_if_network_not_attached: bool = ..., vm_temp_name: _Optional[str] = ..., should_rename: bool = ..., use_vm_name_for_path: bool = ..., vm_folder_suffix_in_path: _Optional[str] = ..., use_original_datastore: bool = ..., vcd_vcenter_vm_name: _Optional[str] = ..., skip_attach_network: bool = ..., old_to_new_datastore_name_map: _Optional[_Mapping[str, str]] = ..., use_disk_paths_from_vmx: bool = ..., datacenter_name: _Optional[str] = ..., controller_key_to_type_map: _Optional[_Mapping[int, str]] = ..., delete_vmx_file_from_datastore: bool = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disk_provision_type: _Optional[_Union[DiskProvisionType, str]] = ..., nvram_file_name: _Optional[str] = ...) -> None: ...

class CreateVMResult(_message.Message):
    __slots__ = ("error_vec", "vm_entity", "host_entity", "virtual_disk_device_vec", "virtual_disk_to_create_vec", "is_network_attached", "xml_vm_reconfig_spec", "used_disk_paths_from_vmx", "vm_folder_path", "kms_warning")
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_DEVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_TO_CREATE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_NETWORK_ATTACHED_FIELD_NUMBER: _ClassVar[int]
    XML_VM_RECONFIG_SPEC_FIELD_NUMBER: _ClassVar[int]
    USED_DISK_PATHS_FROM_VMX_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    KMS_WARNING_FIELD_NUMBER: _ClassVar[int]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    vm_entity: _vmware_pb2.Entity
    host_entity: _vmware_pb2.Entity
    virtual_disk_device_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDiskDeviceInfo]
    virtual_disk_to_create_vec: _containers.RepeatedCompositeFieldContainer[ConstructVMConfigSpecResult.VirtualDiskCreateInfo]
    is_network_attached: bool
    xml_vm_reconfig_spec: str
    used_disk_paths_from_vmx: bool
    vm_folder_path: str
    kms_warning: _error_pb2.ErrorProto
    def __init__(self, error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., host_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., virtual_disk_device_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDiskDeviceInfo, _Mapping]]] = ..., virtual_disk_to_create_vec: _Optional[_Iterable[_Union[ConstructVMConfigSpecResult.VirtualDiskCreateInfo, _Mapping]]] = ..., is_network_attached: bool = ..., xml_vm_reconfig_spec: _Optional[str] = ..., used_disk_paths_from_vmx: bool = ..., vm_folder_path: _Optional[str] = ..., kms_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RegisterVMArg(_message.Message):
    __slots__ = ("vm_name", "vm_folder_moref", "vmx_file_path", "resource_pool_moref", "remove_network_devices", "reset_uuid", "host_system_moref")
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    VMX_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    REMOVE_NETWORK_DEVICES_FIELD_NUMBER: _ClassVar[int]
    RESET_UUID_FIELD_NUMBER: _ClassVar[int]
    HOST_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    vm_folder_moref: _vmware_common_pb2.MORef
    vmx_file_path: str
    resource_pool_moref: _vmware_common_pb2.MORef
    remove_network_devices: bool
    reset_uuid: bool
    host_system_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_name: _Optional[str] = ..., vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vmx_file_path: _Optional[str] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., remove_network_devices: bool = ..., reset_uuid: bool = ..., host_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class RegisterVMResult(_message.Message):
    __slots__ = ("vm_entity",)
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    vm_entity: _vmware_pb2.Entity
    def __init__(self, vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ...) -> None: ...

class GetTaskUpdateArg(_message.Message):
    __slots__ = ("task_moref",)
    TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    task_moref: _vmware_common_pb2.MORef
    def __init__(self, task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class GetTaskUpdateResult(_message.Message):
    __slots__ = ("has_updates", "task_done", "task_progress_pct", "update_result")
    HAS_UPDATES_FIELD_NUMBER: _ClassVar[int]
    TASK_DONE_FIELD_NUMBER: _ClassVar[int]
    TASK_PROGRESS_PCT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    has_updates: bool
    task_done: bool
    task_progress_pct: int
    update_result: _vsphere_pb2.VsphereResultProto
    def __init__(self, has_updates: bool = ..., task_done: bool = ..., task_progress_pct: _Optional[int] = ..., update_result: _Optional[_Union[_vsphere_pb2.VsphereResultProto, _Mapping]] = ...) -> None: ...

class GetTaskListArg(_message.Message):
    __slots__ = ("entity_moref", "task_state_vec", "max_count", "description_id_filter_vec", "entity_type_str")
    ENTITY_MOREF_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_ID_FILTER_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_STR_FIELD_NUMBER: _ClassVar[int]
    entity_moref: _vmware_common_pb2.MORef
    task_state_vec: _containers.RepeatedScalarFieldContainer[_vmware_pb2_1.TaskInfo.State]
    max_count: int
    description_id_filter_vec: _containers.RepeatedScalarFieldContainer[_vmware_pb2_1.TaskDescriptionId.Type]
    entity_type_str: str
    def __init__(self, entity_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., task_state_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.TaskInfo.State, str]]] = ..., max_count: _Optional[int] = ..., description_id_filter_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.TaskDescriptionId.Type, str]]] = ..., entity_type_str: _Optional[str] = ...) -> None: ...

class GetTaskListResult(_message.Message):
    __slots__ = ("task_info_vec",)
    TASK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    task_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.TaskInfo]
    def __init__(self, task_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.TaskInfo, _Mapping]]] = ...) -> None: ...

class ValidateCredentialsInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params",)
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ...) -> None: ...

class ValidateCredentialsInGuestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartProgramInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "program_path", "arguments", "working_directory_path")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_PATH_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    program_path: str
    arguments: str
    working_directory_path: str
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., program_path: _Optional[str] = ..., arguments: _Optional[str] = ..., working_directory_path: _Optional[str] = ...) -> None: ...

class StartProgramInGuestResult(_message.Message):
    __slots__ = ("process_pid",)
    PROCESS_PID_FIELD_NUMBER: _ClassVar[int]
    process_pid: int
    def __init__(self, process_pid: _Optional[int] = ...) -> None: ...

class ProcessWaitInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "process_pid", "wait_timeout_secs")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_PID_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    process_pid: int
    wait_timeout_secs: int
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., process_pid: _Optional[int] = ..., wait_timeout_secs: _Optional[int] = ...) -> None: ...

class ProcessWaitInGuestResult(_message.Message):
    __slots__ = ("exit_code_valid", "exit_code")
    EXIT_CODE_VALID_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_code_valid: bool
    exit_code: int
    def __init__(self, exit_code_valid: bool = ..., exit_code: _Optional[int] = ...) -> None: ...

class ListProcessesInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "process_pid", "process_name_prefix")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_PID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    process_pid: int
    process_name_prefix: str
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., process_pid: _Optional[int] = ..., process_name_prefix: _Optional[str] = ...) -> None: ...

class ListProcessesInGuestResult(_message.Message):
    __slots__ = ("process_info_vec",)
    class ProcessInfo(_message.Message):
        __slots__ = ("process_pid", "process_name", "process_exited", "exit_code")
        PROCESS_PID_FIELD_NUMBER: _ClassVar[int]
        PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
        PROCESS_EXITED_FIELD_NUMBER: _ClassVar[int]
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        process_pid: int
        process_name: str
        process_exited: bool
        exit_code: int
        def __init__(self, process_pid: _Optional[int] = ..., process_name: _Optional[str] = ..., process_exited: bool = ..., exit_code: _Optional[int] = ...) -> None: ...
    PROCESS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    process_info_vec: _containers.RepeatedCompositeFieldContainer[ListProcessesInGuestResult.ProcessInfo]
    def __init__(self, process_info_vec: _Optional[_Iterable[_Union[ListProcessesInGuestResult.ProcessInfo, _Mapping]]] = ...) -> None: ...

class TerminateProcessInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "process_pid")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_PID_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    process_pid: int
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., process_pid: _Optional[int] = ...) -> None: ...

class TerminateProcessInGuestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateDirectoryInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "directory_path", "create_parent_directories")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATE_PARENT_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    directory_path: str
    create_parent_directories: bool
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., directory_path: _Optional[str] = ..., create_parent_directories: bool = ...) -> None: ...

class CreateDirectoryInGuestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateTempFileInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "is_directory", "directory_path", "prefix", "suffix")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    is_directory: bool
    directory_path: str
    prefix: str
    suffix: str
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., is_directory: bool = ..., directory_path: _Optional[str] = ..., prefix: _Optional[str] = ..., suffix: _Optional[str] = ...) -> None: ...

class CreateTempFileInGuestResult(_message.Message):
    __slots__ = ("absolute_path",)
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    absolute_path: str
    def __init__(self, absolute_path: _Optional[str] = ...) -> None: ...

class FileEntry(_message.Message):
    __slots__ = ("path", "is_directory", "recursive")
    PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    path: str
    is_directory: bool
    recursive: bool
    def __init__(self, path: _Optional[str] = ..., is_directory: bool = ..., recursive: bool = ...) -> None: ...

class DeleteFilesInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "file_entry_vec")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    file_entry_vec: _containers.RepeatedCompositeFieldContainer[FileEntry]
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., file_entry_vec: _Optional[_Iterable[_Union[FileEntry, _Mapping]]] = ...) -> None: ...

class DeleteFilesInGuestResult(_message.Message):
    __slots__ = ("file_entry_result_vec",)
    class FileEntryResult(_message.Message):
        __slots__ = ("file_entry", "error")
        FILE_ENTRY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        file_entry: FileEntry
        error: _error_pb2.ErrorProto
        def __init__(self, file_entry: _Optional[_Union[FileEntry, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    FILE_ENTRY_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    file_entry_result_vec: _containers.RepeatedCompositeFieldContainer[DeleteFilesInGuestResult.FileEntryResult]
    def __init__(self, file_entry_result_vec: _Optional[_Iterable[_Union[DeleteFilesInGuestResult.FileEntryResult, _Mapping]]] = ...) -> None: ...

class FetchFileFromGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "file_path", "host_name")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    file_path: str
    host_name: str
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., file_path: _Optional[str] = ..., host_name: _Optional[str] = ...) -> None: ...

class FetchFileFromGuestResult(_message.Message):
    __slots__ = ("file_data",)
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    file_data: bytes
    def __init__(self, file_data: _Optional[bytes] = ...) -> None: ...

class GuestFileAttributes(_message.Message):
    __slots__ = ("access_time", "modification_time", "symlink_target", "posix_file_attributes", "windows_file_attributes")
    class GuestPosixFileAttributes(_message.Message):
        __slots__ = ("group_id", "owner_id", "permissions")
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        group_id: int
        owner_id: int
        permissions: int
        def __init__(self, group_id: _Optional[int] = ..., owner_id: _Optional[int] = ..., permissions: _Optional[int] = ...) -> None: ...
    class GuestWindowsFileAttributes(_message.Message):
        __slots__ = ("create_time", "hidden", "read_only")
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        create_time: int
        hidden: bool
        read_only: bool
        def __init__(self, create_time: _Optional[int] = ..., hidden: bool = ..., read_only: bool = ...) -> None: ...
    ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    POSIX_FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    access_time: int
    modification_time: int
    symlink_target: str
    posix_file_attributes: GuestFileAttributes.GuestPosixFileAttributes
    windows_file_attributes: GuestFileAttributes.GuestWindowsFileAttributes
    def __init__(self, access_time: _Optional[int] = ..., modification_time: _Optional[int] = ..., symlink_target: _Optional[str] = ..., posix_file_attributes: _Optional[_Union[GuestFileAttributes.GuestPosixFileAttributes, _Mapping]] = ..., windows_file_attributes: _Optional[_Union[GuestFileAttributes.GuestWindowsFileAttributes, _Mapping]] = ...) -> None: ...

class PushFileToGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "file_data", "local_file_path", "timeout_secs", "put_url")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    PUT_URL_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    file_data: bytes
    local_file_path: str
    timeout_secs: int
    put_url: str
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., file_data: _Optional[bytes] = ..., local_file_path: _Optional[str] = ..., timeout_secs: _Optional[int] = ..., put_url: _Optional[str] = ...) -> None: ...

class PushFileToGuestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGuestFileTransferUrlArg(_message.Message):
    __slots__ = ("guest_operation_params", "file_data", "local_file_path", "remote_file_path", "overwrite_file", "posix_file_permissions", "host_name", "guest_file_attributes", "file_size")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FILE_FIELD_NUMBER: _ClassVar[int]
    POSIX_FILE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    GUEST_FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    file_data: bytes
    local_file_path: str
    remote_file_path: str
    overwrite_file: bool
    posix_file_permissions: int
    host_name: str
    guest_file_attributes: GuestFileAttributes
    file_size: int
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., file_data: _Optional[bytes] = ..., local_file_path: _Optional[str] = ..., remote_file_path: _Optional[str] = ..., overwrite_file: bool = ..., posix_file_permissions: _Optional[int] = ..., host_name: _Optional[str] = ..., guest_file_attributes: _Optional[_Union[GuestFileAttributes, _Mapping]] = ..., file_size: _Optional[int] = ...) -> None: ...

class GetGuestFileTransferUrlResult(_message.Message):
    __slots__ = ("put_url",)
    PUT_URL_FIELD_NUMBER: _ClassVar[int]
    put_url: str
    def __init__(self, put_url: _Optional[str] = ...) -> None: ...

class ListFilesInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "file_path", "start_index", "max_results", "match_pattern")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MATCH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    file_path: str
    start_index: int
    max_results: int
    match_pattern: str
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., file_path: _Optional[str] = ..., start_index: _Optional[int] = ..., max_results: _Optional[int] = ..., match_pattern: _Optional[str] = ...) -> None: ...

class ListFilesInGuestResult(_message.Message):
    __slots__ = ("file_info_vec",)
    class FileInfo(_message.Message):
        __slots__ = ("path", "is_directory", "file_size")
        PATH_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        path: str
        is_directory: bool
        file_size: int
        def __init__(self, path: _Optional[str] = ..., is_directory: bool = ..., file_size: _Optional[int] = ...) -> None: ...
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    file_info_vec: _containers.RepeatedCompositeFieldContainer[ListFilesInGuestResult.FileInfo]
    def __init__(self, file_info_vec: _Optional[_Iterable[_Union[ListFilesInGuestResult.FileInfo, _Mapping]]] = ...) -> None: ...

class FetchMetricsInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchMetricsInfoResult(_message.Message):
    __slots__ = ("metric_infos_vec",)
    class MetricInfo(_message.Message):
        __slots__ = ("metric_name", "metric_id")
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        METRIC_ID_FIELD_NUMBER: _ClassVar[int]
        metric_name: str
        metric_id: int
        def __init__(self, metric_name: _Optional[str] = ..., metric_id: _Optional[int] = ...) -> None: ...
    METRIC_INFOS_VEC_FIELD_NUMBER: _ClassVar[int]
    metric_infos_vec: _containers.RepeatedCompositeFieldContainer[FetchMetricsInfoResult.MetricInfo]
    def __init__(self, metric_infos_vec: _Optional[_Iterable[_Union[FetchMetricsInfoResult.MetricInfo, _Mapping]]] = ...) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("task_moref", "idle_timeout_seconds", "poll_interval_seconds", "wait_for_task_to_cancel")
    TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    POLL_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_TASK_TO_CANCEL_FIELD_NUMBER: _ClassVar[int]
    task_moref: _vmware_common_pb2.MORef
    idle_timeout_seconds: int
    poll_interval_seconds: int
    wait_for_task_to_cancel: bool
    def __init__(self, task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., idle_timeout_seconds: _Optional[int] = ..., poll_interval_seconds: _Optional[int] = ..., wait_for_task_to_cancel: bool = ...) -> None: ...

class CancelTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MarkVMAsTemplateArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class MarkVMAsTemplateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchFileFromDatastoreArg(_message.Message):
    __slots__ = ("datacenter_name", "datastore_name", "file_path", "max_download_file_size")
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    MAX_DOWNLOAD_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    datacenter_name: str
    datastore_name: str
    file_path: str
    max_download_file_size: int
    def __init__(self, datacenter_name: _Optional[str] = ..., datastore_name: _Optional[str] = ..., file_path: _Optional[str] = ..., max_download_file_size: _Optional[int] = ...) -> None: ...

class FetchFileFromDatastoreResult(_message.Message):
    __slots__ = ("file_data", "error")
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    file_data: bytes
    error: _error_pb2.ErrorProto
    def __init__(self, file_data: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteFileFromDatastoreArg(_message.Message):
    __slots__ = ("datacenter_name", "datastore_name", "file_path")
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    datacenter_name: str
    datastore_name: str
    file_path: str
    def __init__(self, datacenter_name: _Optional[str] = ..., datastore_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class DeleteFileFromDatastoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PushFileToDatastoreArg(_message.Message):
    __slots__ = ("datacenter_name", "datastore_name", "file_path", "file_data")
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    datacenter_name: str
    datastore_name: str
    file_path: str
    file_data: bytes
    def __init__(self, datacenter_name: _Optional[str] = ..., datastore_name: _Optional[str] = ..., file_path: _Optional[str] = ..., file_data: _Optional[bytes] = ...) -> None: ...

class PushFileToDatastoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TerminateSessionArg(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class TerminateSessionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InstallIoFilterArg(_message.Message):
    __slots__ = ("vib_url", "comp_res_moref")
    VIB_URL_FIELD_NUMBER: _ClassVar[int]
    COMP_RES_MOREF_FIELD_NUMBER: _ClassVar[int]
    vib_url: str
    comp_res_moref: _vmware_common_pb2.MORef
    def __init__(self, vib_url: _Optional[str] = ..., comp_res_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class InstallIoFilterResult(_message.Message):
    __slots__ = ("io_filter_info", "host_io_filter_issues")
    IO_FILTER_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
    io_filter_info: _vmware_pb2_1.ClusterIoFilterInfo
    host_io_filter_issues: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.IoFilterHostIssue]
    def __init__(self, io_filter_info: _Optional[_Union[_vmware_pb2_1.ClusterIoFilterInfo, _Mapping]] = ..., host_io_filter_issues: _Optional[_Iterable[_Union[_vmware_pb2_1.IoFilterHostIssue, _Mapping]]] = ...) -> None: ...

class UpgradeIoFilterArg(_message.Message):
    __slots__ = ("filter_id", "vib_url", "comp_res_moref")
    FILTER_ID_FIELD_NUMBER: _ClassVar[int]
    VIB_URL_FIELD_NUMBER: _ClassVar[int]
    COMP_RES_MOREF_FIELD_NUMBER: _ClassVar[int]
    filter_id: str
    vib_url: str
    comp_res_moref: _vmware_common_pb2.MORef
    def __init__(self, filter_id: _Optional[str] = ..., vib_url: _Optional[str] = ..., comp_res_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class UpgradeIoFilterResult(_message.Message):
    __slots__ = ("io_filter_info", "host_io_filter_issues")
    IO_FILTER_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
    io_filter_info: _vmware_pb2_1.ClusterIoFilterInfo
    host_io_filter_issues: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.IoFilterHostIssue]
    def __init__(self, io_filter_info: _Optional[_Union[_vmware_pb2_1.ClusterIoFilterInfo, _Mapping]] = ..., host_io_filter_issues: _Optional[_Iterable[_Union[_vmware_pb2_1.IoFilterHostIssue, _Mapping]]] = ...) -> None: ...

class UninstallIoFilterArg(_message.Message):
    __slots__ = ("filter_id", "comp_res_moref")
    FILTER_ID_FIELD_NUMBER: _ClassVar[int]
    COMP_RES_MOREF_FIELD_NUMBER: _ClassVar[int]
    filter_id: str
    comp_res_moref: _vmware_common_pb2.MORef
    def __init__(self, filter_id: _Optional[str] = ..., comp_res_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class UninstallIoFilterResult(_message.Message):
    __slots__ = ("host_io_filter_issues",)
    HOST_IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
    host_io_filter_issues: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.IoFilterHostIssue]
    def __init__(self, host_io_filter_issues: _Optional[_Iterable[_Union[_vmware_pb2_1.IoFilterHostIssue, _Mapping]]] = ...) -> None: ...

class QueryIoFilterInfoArg(_message.Message):
    __slots__ = ("comp_res_moref", "filter_name")
    COMP_RES_MOREF_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    comp_res_moref: _vmware_common_pb2.MORef
    filter_name: str
    def __init__(self, comp_res_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., filter_name: _Optional[str] = ...) -> None: ...

class QueryIoFilterInfoResult(_message.Message):
    __slots__ = ("cluster_io_filter_infos",)
    CLUSTER_IO_FILTER_INFOS_FIELD_NUMBER: _ClassVar[int]
    cluster_io_filter_infos: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.ClusterIoFilterInfo]
    def __init__(self, cluster_io_filter_infos: _Optional[_Iterable[_Union[_vmware_pb2_1.ClusterIoFilterInfo, _Mapping]]] = ...) -> None: ...

class QueryAndResolveIoFilterIssuesArg(_message.Message):
    __slots__ = ("filter_id", "comp_res_moref", "resolve_issues")
    FILTER_ID_FIELD_NUMBER: _ClassVar[int]
    COMP_RES_MOREF_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_ISSUES_FIELD_NUMBER: _ClassVar[int]
    filter_id: str
    comp_res_moref: _vmware_common_pb2.MORef
    resolve_issues: bool
    def __init__(self, filter_id: _Optional[str] = ..., comp_res_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., resolve_issues: bool = ...) -> None: ...

class QueryAndResolveIoFilterIssuesResult(_message.Message):
    __slots__ = ("action", "host_io_filter_issues")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    HOST_IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
    action: str
    host_io_filter_issues: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.IoFilterHostIssue]
    def __init__(self, action: _Optional[str] = ..., host_io_filter_issues: _Optional[_Iterable[_Union[_vmware_pb2_1.IoFilterHostIssue, _Mapping]]] = ...) -> None: ...

class SetIoFilterClusterInfoArg(_message.Message):
    __slots__ = ("vm_moref", "io_filter_properties")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    IO_FILTER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    io_filter_properties: _vmware_pb2.IoFilterStoragePolicyProperties
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., io_filter_properties: _Optional[_Union[_vmware_pb2.IoFilterStoragePolicyProperties, _Mapping]] = ...) -> None: ...

class SetIoFilterClusterInfoResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StoragePolicyInfo(_message.Message):
    __slots__ = ("profile_id", "policy_name", "io_filter_properties")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    IO_FILTER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    policy_name: str
    io_filter_properties: _vmware_pb2.IoFilterStoragePolicyProperties
    def __init__(self, profile_id: _Optional[str] = ..., policy_name: _Optional[str] = ..., io_filter_properties: _Optional[_Union[_vmware_pb2.IoFilterStoragePolicyProperties, _Mapping]] = ...) -> None: ...

class RetrieveStoragePolicyArg(_message.Message):
    __slots__ = ("profile_id_vec",)
    PROFILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    profile_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, profile_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RetrieveStoragePolicyResult(_message.Message):
    __slots__ = ("storage_policy_vec",)
    STORAGE_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    storage_policy_vec: _containers.RepeatedCompositeFieldContainer[StoragePolicyInfo]
    def __init__(self, storage_policy_vec: _Optional[_Iterable[_Union[StoragePolicyInfo, _Mapping]]] = ...) -> None: ...

class FetchStoragePolicyArg(_message.Message):
    __slots__ = ("object_moref_vec",)
    OBJECT_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    object_moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    def __init__(self, object_moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ...) -> None: ...

class FetchStoragePolicyResult(_message.Message):
    __slots__ = ("object_profile_vec",)
    class ObjectProfileInfo(_message.Message):
        __slots__ = ("moref", "error", "profile_id_vec")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        PROFILE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        error: _error_pb2.ErrorProto
        profile_id_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., profile_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    OBJECT_PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    object_profile_vec: _containers.RepeatedCompositeFieldContainer[FetchStoragePolicyResult.ObjectProfileInfo]
    def __init__(self, object_profile_vec: _Optional[_Iterable[_Union[FetchStoragePolicyResult.ObjectProfileInfo, _Mapping]]] = ...) -> None: ...

class QueryStoragePolicyArg(_message.Message):
    __slots__ = ("policy_name",)
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    def __init__(self, policy_name: _Optional[str] = ...) -> None: ...

class QueryStoragePolicyResult(_message.Message):
    __slots__ = ("profile_id",)
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    def __init__(self, profile_id: _Optional[str] = ...) -> None: ...

class CreateCDPStoragePolicyArg(_message.Message):
    __slots__ = ("storage_policy_info",)
    STORAGE_POLICY_INFO_FIELD_NUMBER: _ClassVar[int]
    storage_policy_info: StoragePolicyInfo
    def __init__(self, storage_policy_info: _Optional[_Union[StoragePolicyInfo, _Mapping]] = ...) -> None: ...

class CreateCDPStoragePolicyResult(_message.Message):
    __slots__ = ("profile_id",)
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    def __init__(self, profile_id: _Optional[str] = ...) -> None: ...

class UpdateCDPStoragePolicyArg(_message.Message):
    __slots__ = ("storage_policy_info",)
    STORAGE_POLICY_INFO_FIELD_NUMBER: _ClassVar[int]
    storage_policy_info: StoragePolicyInfo
    def __init__(self, storage_policy_info: _Optional[_Union[StoragePolicyInfo, _Mapping]] = ...) -> None: ...

class UpdateCDPStoragePolicyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryDisksOnStoragePolicyArg(_message.Message):
    __slots__ = ("vm_moref", "profile_id")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    profile_id: str
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., profile_id: _Optional[str] = ...) -> None: ...

class QueryDisksOnStoragePolicyResult(_message.Message):
    __slots__ = ("virtual_disk_key_vec",)
    VIRTUAL_DISK_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disk_key_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, virtual_disk_key_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class AttachStoragePolicyArg(_message.Message):
    __slots__ = ("vm_moref", "disk_key_vec", "profile_id", "use_default_profile", "reapply_profile")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    DISK_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    REAPPLY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    disk_key_vec: _containers.RepeatedScalarFieldContainer[int]
    profile_id: str
    use_default_profile: bool
    reapply_profile: bool
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disk_key_vec: _Optional[_Iterable[int]] = ..., profile_id: _Optional[str] = ..., use_default_profile: bool = ..., reapply_profile: bool = ...) -> None: ...

class AttachStoragePolicyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchKmipServerListArg(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class FetchKmipServerListResult(_message.Message):
    __slots__ = ("kmip_server_key_provider_id",)
    KMIP_SERVER_KEY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    kmip_server_key_provider_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, kmip_server_key_provider_id: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchComputeResourceArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchComputeResourceResult(_message.Message):
    __slots__ = ("compute_resource_entity", "host_moref")
    COMPUTE_RESOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    compute_resource_entity: _vmware_pb2.Entity
    host_moref: _vmware_common_pb2.MORef
    def __init__(self, compute_resource_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchVCenterCustomAttributesArg(_message.Message):
    __slots__ = ("managed_object_type_vec",)
    MANAGED_OBJECT_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    managed_object_type_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, managed_object_type_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchVCenterCustomAttributesResult(_message.Message):
    __slots__ = ("custom_attributes",)
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.CustomAttribute]
    def __init__(self, custom_attributes: _Optional[_Iterable[_Union[_vmware_pb2.CustomAttribute, _Mapping]]] = ...) -> None: ...

class FetchObjectCustomAttributesArg(_message.Message):
    __slots__ = ("object_moref",)
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FetchObjectCustomAttributesResult(_message.Message):
    __slots__ = ("custom_attributes",)
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.CustomAttribute]
    def __init__(self, custom_attributes: _Optional[_Iterable[_Union[_vmware_pb2.CustomAttribute, _Mapping]]] = ...) -> None: ...

class ApplyCustomAttributesToObjectArg(_message.Message):
    __slots__ = ("custom_attributes_vec", "object_moref")
    CUSTOM_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    custom_attributes_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.CustomAttribute]
    object_moref: _vmware_common_pb2.MORef
    def __init__(self, custom_attributes_vec: _Optional[_Iterable[_Union[_vmware_pb2.CustomAttribute, _Mapping]]] = ..., object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class ApplyCustomAttributesToObjectResult(_message.Message):
    __slots__ = ("failed_custom_attributes_vec", "failed_custom_attributes_error_vec")
    FAILED_CUSTOM_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    FAILED_CUSTOM_ATTRIBUTES_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    failed_custom_attributes_vec: _containers.RepeatedScalarFieldContainer[str]
    failed_custom_attributes_error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, failed_custom_attributes_vec: _Optional[_Iterable[str]] = ..., failed_custom_attributes_error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class ChangeFileAttributesInGuestArg(_message.Message):
    __slots__ = ("guest_operation_params", "remote_file_path", "guest_file_attributes")
    GUEST_OPERATION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    GUEST_FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    guest_operation_params: _vmware_common_args_pb2.GuestOperationArg
    remote_file_path: str
    guest_file_attributes: GuestFileAttributes
    def __init__(self, guest_operation_params: _Optional[_Union[_vmware_common_args_pb2.GuestOperationArg, _Mapping]] = ..., remote_file_path: _Optional[str] = ..., guest_file_attributes: _Optional[_Union[GuestFileAttributes, _Mapping]] = ...) -> None: ...

class ChangeFileAttributesInGuestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RenameObjectArg(_message.Message):
    __slots__ = ("object_moref", "new_name")
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    new_name: str
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., new_name: _Optional[str] = ...) -> None: ...

class RenameObjectResult(_message.Message):
    __slots__ = ("object_moref", "error")
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    error: _error_pb2.ErrorProto
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ApplyTagsToObjectArg(_message.Message):
    __slots__ = ("object_moref", "tag_attributes_vec")
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    tag_attributes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., tag_attributes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ApplyTagsToObjectResult(_message.Message):
    __slots__ = ("failed_tag_id_vec", "error_message_vec")
    FAILED_TAG_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    failed_tag_id_vec: _containers.RepeatedScalarFieldContainer[str]
    error_message_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, failed_tag_id_vec: _Optional[_Iterable[str]] = ..., error_message_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DetachTagsFromObjectArg(_message.Message):
    __slots__ = ("object_moref", "tag_attributes_vec")
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    tag_attributes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., tag_attributes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DetachTagsFromObjectResult(_message.Message):
    __slots__ = ("failed_tag_id_vec", "error_message_vec")
    FAILED_TAG_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    failed_tag_id_vec: _containers.RepeatedScalarFieldContainer[str]
    error_message_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, failed_tag_id_vec: _Optional[_Iterable[str]] = ..., error_message_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchTagsForStorageProfileArg(_message.Message):
    __slots__ = ("storage_profile_name", "storage_profile_uuid")
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_UUID_FIELD_NUMBER: _ClassVar[int]
    storage_profile_name: str
    storage_profile_uuid: str
    def __init__(self, storage_profile_name: _Optional[str] = ..., storage_profile_uuid: _Optional[str] = ...) -> None: ...

class FetchTagsForStorageProfileResult(_message.Message):
    __slots__ = ("tag_name_vec",)
    TAG_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    tag_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tag_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteStoragePolicyArg(_message.Message):
    __slots__ = ("profile_id", "policy_name")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    policy_name: str
    def __init__(self, profile_id: _Optional[str] = ..., policy_name: _Optional[str] = ...) -> None: ...

class DeleteStoragePolicyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReconfigVMArg(_message.Message):
    __slots__ = ("vm_moref", "xml_vm_reconfig_spec", "new_vm_name", "reset_instance_uuid")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    XML_VM_RECONFIG_SPEC_FIELD_NUMBER: _ClassVar[int]
    NEW_VM_NAME_FIELD_NUMBER: _ClassVar[int]
    RESET_INSTANCE_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    xml_vm_reconfig_spec: str
    new_vm_name: str
    reset_instance_uuid: bool
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., xml_vm_reconfig_spec: _Optional[str] = ..., new_vm_name: _Optional[str] = ..., reset_instance_uuid: bool = ...) -> None: ...

class ReconfigVMResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class EnableChangeTrackingArg(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class EnableChangeTrackingResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchPbmCapabilitySchemaArg(_message.Message):
    __slots__ = ("vendor_id", "service_type_vec")
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    vendor_id: str
    service_type_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vendor_id: _Optional[str] = ..., service_type_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchPbmCapabilitySchemaResult(_message.Message):
    __slots__ = ("capability_schema_vec",)
    CAPABILITY_SCHEMA_VEC_FIELD_NUMBER: _ClassVar[int]
    capability_schema_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pbm_pb2.PbmCapabilitySchema]
    def __init__(self, capability_schema_vec: _Optional[_Iterable[_Union[_vmware_pbm_pb2.PbmCapabilitySchema, _Mapping]]] = ...) -> None: ...

class ConstructVMConfigSpecArg(_message.Message):
    __slots__ = ("xml_vm_config_info", "vm_name", "datastore_name", "datastore_moref", "datastore_path_prefix", "include_original_datastore_name_in_path_prefix", "network_config_info", "reset_bios_uuid", "create_blank_disks", "use_vm_name_for_path", "attach_default_device", "reset_change_version", "skip_disk_controllers", "skip_non_removable_devices", "vm_folder_suffix_in_path", "vcd_vcenter_vm_name", "skip_attach_network", "use_original_datastore", "old_to_new_datastore_name_map", "use_disk_paths_from_vmx", "datacenter_name", "controller_key_to_type_map", "datacenter_moref", "skip_migrate_host_log", "disk_provision_type", "is_nvram_file_available", "should_skip_populating_vm_path_name")
    class OldToNewDatastoreNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ControllerKeyToTypeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    XML_VM_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ORIGINAL_DATASTORE_NAME_IN_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    RESET_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_BLANK_DISKS_FIELD_NUMBER: _ClassVar[int]
    USE_VM_NAME_FOR_PATH_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DEFAULT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    RESET_CHANGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SKIP_DISK_CONTROLLERS_FIELD_NUMBER: _ClassVar[int]
    SKIP_NON_REMOVABLE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_SUFFIX_IN_PATH_FIELD_NUMBER: _ClassVar[int]
    VCD_VCENTER_VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_ATTACH_NETWORK_FIELD_NUMBER: _ClassVar[int]
    USE_ORIGINAL_DATASTORE_FIELD_NUMBER: _ClassVar[int]
    OLD_TO_NEW_DATASTORE_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    USE_DISK_PATHS_FROM_VMX_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_TO_TYPE_MAP_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    SKIP_MIGRATE_HOST_LOG_FIELD_NUMBER: _ClassVar[int]
    DISK_PROVISION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_NVRAM_FILE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_SKIP_POPULATING_VM_PATH_NAME_FIELD_NUMBER: _ClassVar[int]
    xml_vm_config_info: str
    vm_name: str
    datastore_name: str
    datastore_moref: _vmware_common_pb2.MORef
    datastore_path_prefix: str
    include_original_datastore_name_in_path_prefix: bool
    network_config_info: CreateVMArg.NetworkConfig
    reset_bios_uuid: bool
    create_blank_disks: bool
    use_vm_name_for_path: bool
    attach_default_device: bool
    reset_change_version: bool
    skip_disk_controllers: bool
    skip_non_removable_devices: bool
    vm_folder_suffix_in_path: str
    vcd_vcenter_vm_name: str
    skip_attach_network: bool
    use_original_datastore: bool
    old_to_new_datastore_name_map: _containers.ScalarMap[str, str]
    use_disk_paths_from_vmx: bool
    datacenter_name: str
    controller_key_to_type_map: _containers.ScalarMap[int, str]
    datacenter_moref: _vmware_common_pb2.MORef
    skip_migrate_host_log: bool
    disk_provision_type: DiskProvisionType
    is_nvram_file_available: bool
    should_skip_populating_vm_path_name: bool
    def __init__(self, xml_vm_config_info: _Optional[str] = ..., vm_name: _Optional[str] = ..., datastore_name: _Optional[str] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_path_prefix: _Optional[str] = ..., include_original_datastore_name_in_path_prefix: bool = ..., network_config_info: _Optional[_Union[CreateVMArg.NetworkConfig, _Mapping]] = ..., reset_bios_uuid: bool = ..., create_blank_disks: bool = ..., use_vm_name_for_path: bool = ..., attach_default_device: bool = ..., reset_change_version: bool = ..., skip_disk_controllers: bool = ..., skip_non_removable_devices: bool = ..., vm_folder_suffix_in_path: _Optional[str] = ..., vcd_vcenter_vm_name: _Optional[str] = ..., skip_attach_network: bool = ..., use_original_datastore: bool = ..., old_to_new_datastore_name_map: _Optional[_Mapping[str, str]] = ..., use_disk_paths_from_vmx: bool = ..., datacenter_name: _Optional[str] = ..., controller_key_to_type_map: _Optional[_Mapping[int, str]] = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., skip_migrate_host_log: bool = ..., disk_provision_type: _Optional[_Union[DiskProvisionType, str]] = ..., is_nvram_file_available: bool = ..., should_skip_populating_vm_path_name: bool = ...) -> None: ...

class ConstructVMConfigSpecResult(_message.Message):
    __slots__ = ("error", "xml_vm_config_spec", "virtual_disk_to_create_vec", "vm_hardware_version", "used_disk_paths_from_vmx", "original_vmx_file_path", "kms_warning")
    class VirtualDiskCreateInfo(_message.Message):
        __slots__ = ("file_path", "key", "controller_key", "unit_number", "datastore_moref", "datastore_name", "disk_provision_type", "uuid", "capacity_in_bytes")
        FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
        UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_PROVISION_TYPE_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        file_path: str
        key: int
        controller_key: int
        unit_number: int
        datastore_moref: _vmware_common_pb2.MORef
        datastore_name: str
        disk_provision_type: DiskProvisionType
        uuid: str
        capacity_in_bytes: int
        def __init__(self, file_path: _Optional[str] = ..., key: _Optional[int] = ..., controller_key: _Optional[int] = ..., unit_number: _Optional[int] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_name: _Optional[str] = ..., disk_provision_type: _Optional[_Union[DiskProvisionType, str]] = ..., uuid: _Optional[str] = ..., capacity_in_bytes: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_SPEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_TO_CREATE_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    USED_DISK_PATHS_FROM_VMX_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_VMX_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    KMS_WARNING_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    xml_vm_config_spec: str
    virtual_disk_to_create_vec: _containers.RepeatedCompositeFieldContainer[ConstructVMConfigSpecResult.VirtualDiskCreateInfo]
    vm_hardware_version: str
    used_disk_paths_from_vmx: bool
    original_vmx_file_path: str
    kms_warning: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., xml_vm_config_spec: _Optional[str] = ..., virtual_disk_to_create_vec: _Optional[_Iterable[_Union[ConstructVMConfigSpecResult.VirtualDiskCreateInfo, _Mapping]]] = ..., vm_hardware_version: _Optional[str] = ..., used_disk_paths_from_vmx: bool = ..., original_vmx_file_path: _Optional[str] = ..., kms_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MakeDirAndUpdateVMPathsArg(_message.Message):
    __slots__ = ("datacenter_moref", "xml_vm_config_spec", "virtual_disk_to_create_vec")
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_SPEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_TO_CREATE_VEC_FIELD_NUMBER: _ClassVar[int]
    datacenter_moref: _vmware_common_pb2.MORef
    xml_vm_config_spec: str
    virtual_disk_to_create_vec: _containers.RepeatedCompositeFieldContainer[ConstructVMConfigSpecResult.VirtualDiskCreateInfo]
    def __init__(self, datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., xml_vm_config_spec: _Optional[str] = ..., virtual_disk_to_create_vec: _Optional[_Iterable[_Union[ConstructVMConfigSpecResult.VirtualDiskCreateInfo, _Mapping]]] = ...) -> None: ...

class MakeDirAndUpdateVMPathsResult(_message.Message):
    __slots__ = ("error", "xml_vm_config_spec", "virtual_disk_to_create_vec", "vm_folder_path")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_SPEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_TO_CREATE_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    xml_vm_config_spec: str
    virtual_disk_to_create_vec: _containers.RepeatedCompositeFieldContainer[ConstructVMConfigSpecResult.VirtualDiskCreateInfo]
    vm_folder_path: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., xml_vm_config_spec: _Optional[str] = ..., virtual_disk_to_create_vec: _Optional[_Iterable[_Union[ConstructVMConfigSpecResult.VirtualDiskCreateInfo, _Mapping]]] = ..., vm_folder_path: _Optional[str] = ...) -> None: ...

class DetachVirtualDevicesFromVMArg(_message.Message):
    __slots__ = ("vm_moref", "virtual_device_info_vec")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DEVICE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    virtual_device_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDeviceInfo]
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., virtual_device_info_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDeviceInfo, _Mapping]]] = ...) -> None: ...

class DetachVirtualDevicesFromVMResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ResizeVMDisksArg(_message.Message):
    __slots__ = ("vm_moref", "disk_uuid_capacity_map")
    class DiskCapacity(_message.Message):
        __slots__ = ("capacity_bytes", "capacity_kb")
        CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_KB_FIELD_NUMBER: _ClassVar[int]
        capacity_bytes: int
        capacity_kb: int
        def __init__(self, capacity_bytes: _Optional[int] = ..., capacity_kb: _Optional[int] = ...) -> None: ...
    class DiskUuidCapacityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ResizeVMDisksArg.DiskCapacity
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ResizeVMDisksArg.DiskCapacity, _Mapping]] = ...) -> None: ...
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    DISK_UUID_CAPACITY_MAP_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    disk_uuid_capacity_map: _containers.MessageMap[str, ResizeVMDisksArg.DiskCapacity]
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disk_uuid_capacity_map: _Optional[_Mapping[str, ResizeVMDisksArg.DiskCapacity]] = ...) -> None: ...

class ResizeVMDisksResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class MakeDirectoryInDatastoreArg(_message.Message):
    __slots__ = ("directory_path", "datacenter_moref", "create_parent_directories")
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    CREATE_PARENT_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    directory_path: str
    datacenter_moref: _vmware_common_pb2.MORef
    create_parent_directories: bool
    def __init__(self, directory_path: _Optional[str] = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., create_parent_directories: bool = ...) -> None: ...

class MakeDirectoryInDatastoreResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConvertNamespacePathToUuidPathArg(_message.Message):
    __slots__ = ("datacenter_moref", "namespace_file_path")
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    datacenter_moref: _vmware_common_pb2.MORef
    namespace_file_path: str
    def __init__(self, datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., namespace_file_path: _Optional[str] = ...) -> None: ...

class ConvertNamespacePathToUuidPathResult(_message.Message):
    __slots__ = ("uuid_file_path",)
    UUID_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    uuid_file_path: str
    def __init__(self, uuid_file_path: _Optional[str] = ...) -> None: ...

class ChangeNetworkSettingsInGuestArg(_message.Message):
    __slots__ = ("vm_moref", "dns_server_vec", "dns_suffix_vec", "network_adapter_setting_vec", "linux_settings")
    class NetworkAdapterSetting(_message.Message):
        __slots__ = ("vm_nic", "gateway_vec")
        VM_NIC_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_VEC_FIELD_NUMBER: _ClassVar[int]
        vm_nic: _vmware_pb2_1.NICSetting
        gateway_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.DeviceGatewayMap]
        def __init__(self, vm_nic: _Optional[_Union[_vmware_pb2_1.NICSetting, _Mapping]] = ..., gateway_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.DeviceGatewayMap, _Mapping]]] = ...) -> None: ...
    class LinuxSettings(_message.Message):
        __slots__ = ("domain_name", "host_name")
        DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        domain_name: str
        host_name: str
        def __init__(self, domain_name: _Optional[str] = ..., host_name: _Optional[str] = ...) -> None: ...
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SUFFIX_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ADAPTER_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    LINUX_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_suffix_vec: _containers.RepeatedScalarFieldContainer[str]
    network_adapter_setting_vec: _containers.RepeatedCompositeFieldContainer[ChangeNetworkSettingsInGuestArg.NetworkAdapterSetting]
    linux_settings: ChangeNetworkSettingsInGuestArg.LinuxSettings
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., dns_suffix_vec: _Optional[_Iterable[str]] = ..., network_adapter_setting_vec: _Optional[_Iterable[_Union[ChangeNetworkSettingsInGuestArg.NetworkAdapterSetting, _Mapping]]] = ..., linux_settings: _Optional[_Union[ChangeNetworkSettingsInGuestArg.LinuxSettings, _Mapping]] = ...) -> None: ...

class ChangeNetworkSettingsInGuestResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RescanAllHbaArg(_message.Message):
    __slots__ = ("host_storage_system_moref",)
    HOST_STORAGE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
    host_storage_system_moref: _vmware_common_pb2.MORef
    def __init__(self, host_storage_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class RescanAllHbaResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryDiskLayoutArg(_message.Message):
    __slots__ = ("snapshot_moref", "disk_path", "read_only")
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    snapshot_moref: _vmware_common_pb2.MORef
    disk_path: str
    read_only: bool
    def __init__(self, snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., disk_path: _Optional[str] = ..., read_only: bool = ...) -> None: ...

class QueryDiskLayoutResult(_message.Message):
    __slots__ = ("disk_layout_info",)
    DISK_LAYOUT_INFO_FIELD_NUMBER: _ClassVar[int]
    disk_layout_info: _vmware_pb2_1.DiskLayoutInfo
    def __init__(self, disk_layout_info: _Optional[_Union[_vmware_pb2_1.DiskLayoutInfo, _Mapping]] = ...) -> None: ...

class FindByUuidArg(_message.Message):
    __slots__ = ("uuid", "vm_search", "instance_uuid", "datacenter_moref")
    UUID_FIELD_NUMBER: _ClassVar[int]
    VM_SEARCH_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_UUID_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    vm_search: bool
    instance_uuid: bool
    datacenter_moref: _vmware_common_pb2.MORef
    def __init__(self, uuid: _Optional[str] = ..., vm_search: bool = ..., instance_uuid: bool = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class FindByUuidResult(_message.Message):
    __slots__ = ("object_moref",)
    OBJECT_MOREF_FIELD_NUMBER: _ClassVar[int]
    object_moref: _vmware_common_pb2.MORef
    def __init__(self, object_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
