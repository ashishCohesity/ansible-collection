from magneto.api.common import azure_sql_pb2 as _azure_sql_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import policy_pb2 as _policy_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.azure import azure_param_pb2 as _azure_param_pb2
from magneto.connectors.cloud import cloud_pb2 as _cloud_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudDeployEntityInfo(_message.Message):
    __slots__ = ("vm_info", "snapshot_info", "common_info", "failed_over")
    class VMInfo(_message.Message):
        __slots__ = ("blob_info_vec", "vm_config", "managed_disk_info_vec", "private_ip_address", "tear_down_supported", "network_interface_vec", "name", "azure_blob_names", "azure_blob_sizes", "azure_blob_vm_disk_relative_filepaths", "azure_blob_source_offset_vec", "boot_disk_index", "is_windows_vm")
        class BlobInfo(_message.Message):
            __slots__ = ("blob_name", "azure_blob_size", "blob_vm_disk_relative_filepath", "blob_source_offset", "resource_group_name", "storage_account_name", "storage_container_name", "storage_access_key")
            BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
            AZURE_BLOB_SIZE_FIELD_NUMBER: _ClassVar[int]
            BLOB_VM_DISK_RELATIVE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
            BLOB_SOURCE_OFFSET_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            blob_name: str
            azure_blob_size: int
            blob_vm_disk_relative_filepath: str
            blob_source_offset: int
            resource_group_name: str
            storage_account_name: str
            storage_container_name: str
            storage_access_key: str
            def __init__(self, blob_name: _Optional[str] = ..., azure_blob_size: _Optional[int] = ..., blob_vm_disk_relative_filepath: _Optional[str] = ..., blob_source_offset: _Optional[int] = ..., resource_group_name: _Optional[str] = ..., storage_account_name: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., storage_access_key: _Optional[str] = ...) -> None: ...
        class NetworkInterfaceInfo(_message.Message):
            __slots__ = ("resource_group_name", "network_interface_name")
            RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            NETWORK_INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
            resource_group_name: str
            network_interface_name: str
            def __init__(self, resource_group_name: _Optional[str] = ..., network_interface_name: _Optional[str] = ...) -> None: ...
        BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        MANAGED_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TEAR_DOWN_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_VEC_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        AZURE_BLOB_NAMES_FIELD_NUMBER: _ClassVar[int]
        AZURE_BLOB_SIZES_FIELD_NUMBER: _ClassVar[int]
        AZURE_BLOB_VM_DISK_RELATIVE_FILEPATHS_FIELD_NUMBER: _ClassVar[int]
        AZURE_BLOB_SOURCE_OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_INDEX_FIELD_NUMBER: _ClassVar[int]
        IS_WINDOWS_VM_FIELD_NUMBER: _ClassVar[int]
        blob_info_vec: _containers.RepeatedCompositeFieldContainer[CloudDeployEntityInfo.VMInfo.BlobInfo]
        vm_config: VMConfig
        managed_disk_info_vec: _containers.RepeatedCompositeFieldContainer[_azure_param_pb2.ManagedDiskInfo]
        private_ip_address: str
        tear_down_supported: bool
        network_interface_vec: _containers.RepeatedCompositeFieldContainer[CloudDeployEntityInfo.VMInfo.NetworkInterfaceInfo]
        name: str
        azure_blob_names: _containers.RepeatedScalarFieldContainer[str]
        azure_blob_sizes: _containers.RepeatedScalarFieldContainer[int]
        azure_blob_vm_disk_relative_filepaths: _containers.RepeatedScalarFieldContainer[str]
        azure_blob_source_offset_vec: _containers.RepeatedScalarFieldContainer[int]
        boot_disk_index: int
        is_windows_vm: bool
        def __init__(self, blob_info_vec: _Optional[_Iterable[_Union[CloudDeployEntityInfo.VMInfo.BlobInfo, _Mapping]]] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., managed_disk_info_vec: _Optional[_Iterable[_Union[_azure_param_pb2.ManagedDiskInfo, _Mapping]]] = ..., private_ip_address: _Optional[str] = ..., tear_down_supported: bool = ..., network_interface_vec: _Optional[_Iterable[_Union[CloudDeployEntityInfo.VMInfo.NetworkInterfaceInfo, _Mapping]]] = ..., name: _Optional[str] = ..., azure_blob_names: _Optional[_Iterable[str]] = ..., azure_blob_sizes: _Optional[_Iterable[int]] = ..., azure_blob_vm_disk_relative_filepaths: _Optional[_Iterable[str]] = ..., azure_blob_source_offset_vec: _Optional[_Iterable[int]] = ..., boot_disk_index: _Optional[int] = ..., is_windows_vm: bool = ...) -> None: ...
    AZURE_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_restore_entity_info: _descriptor.FieldDescriptor
    AZURE_CLOUD_DEPLOY_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_cloud_deploy_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    FAILED_OVER_FIELD_NUMBER: _ClassVar[int]
    vm_info: CloudDeployEntityInfo.VMInfo
    snapshot_info: _magneto_pb2.SnapshotInfoProto
    common_info: _cloud_pb2.CloudEntityCommonInfo
    failed_over: bool
    def __init__(self, vm_info: _Optional[_Union[CloudDeployEntityInfo.VMInfo, _Mapping]] = ..., snapshot_info: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., common_info: _Optional[_Union[_cloud_pb2.CloudEntityCommonInfo, _Mapping]] = ..., failed_over: bool = ...) -> None: ...

class ReplicationInfo(_message.Message):
    __slots__ = ("status", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ReplicationInfo.Status]
        kPermitGranted: _ClassVar[ReplicationInfo.Status]
        kCloned: _ClassVar[ReplicationInfo.Status]
        kVMInfoFetched: _ClassVar[ReplicationInfo.Status]
        kConflictChecked: _ClassVar[ReplicationInfo.Status]
        kBlobsCreated: _ClassVar[ReplicationInfo.Status]
        kFinished: _ClassVar[ReplicationInfo.Status]
    kStarted: ReplicationInfo.Status
    kPermitGranted: ReplicationInfo.Status
    kCloned: ReplicationInfo.Status
    kVMInfoFetched: ReplicationInfo.Status
    kConflictChecked: ReplicationInfo.Status
    kBlobsCreated: ReplicationInfo.Status
    kFinished: ReplicationInfo.Status
    AZURE_REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_replication_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: ReplicationInfo.Status
    error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[ReplicationInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AzureToAzureCopyTaskInfo(_message.Message):
    __slots__ = ("status", "blob_info_vec", "current_disk_index", "vm_config")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[AzureToAzureCopyTaskInfo.Status]
        kSASUrlGenerated: _ClassVar[AzureToAzureCopyTaskInfo.Status]
        kPageRangesFetched: _ClassVar[AzureToAzureCopyTaskInfo.Status]
        kDiskAreaBuilt: _ClassVar[AzureToAzureCopyTaskInfo.Status]
        kSnapshotCopied: _ClassVar[AzureToAzureCopyTaskInfo.Status]
        kFinished: _ClassVar[AzureToAzureCopyTaskInfo.Status]
    kStarted: AzureToAzureCopyTaskInfo.Status
    kSASUrlGenerated: AzureToAzureCopyTaskInfo.Status
    kPageRangesFetched: AzureToAzureCopyTaskInfo.Status
    kDiskAreaBuilt: AzureToAzureCopyTaskInfo.Status
    kSnapshotCopied: AzureToAzureCopyTaskInfo.Status
    kFinished: AzureToAzureCopyTaskInfo.Status
    class BlobRelatedInfo(_message.Message):
        __slots__ = ("name", "size", "disk_area_list", "active_disk_areas", "snapshot_id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        DISK_AREA_LIST_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_DISK_AREAS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        size: int
        disk_area_list: _disk_pb2.DiskAreaListProto
        active_disk_areas: _disk_pb2.DiskAreaListProto
        snapshot_id: str
        def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., disk_area_list: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ..., active_disk_areas: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ..., snapshot_id: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DISK_INDEX_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    status: AzureToAzureCopyTaskInfo.Status
    blob_info_vec: _containers.RepeatedCompositeFieldContainer[AzureToAzureCopyTaskInfo.BlobRelatedInfo]
    current_disk_index: int
    vm_config: VMConfig
    def __init__(self, status: _Optional[_Union[AzureToAzureCopyTaskInfo.Status, str]] = ..., blob_info_vec: _Optional[_Iterable[_Union[AzureToAzureCopyTaskInfo.BlobRelatedInfo, _Mapping]]] = ..., current_disk_index: _Optional[int] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ...) -> None: ...

class RefBlobInfo(_message.Message):
    __slots__ = ("name", "size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class ReplicationEntityInfo(_message.Message):
    __slots__ = ("storage_resource_group", "storage_account", "storage_container", "snapshot_id_map", "vm_config", "cloud_replication_target", "ref_blob_id_map", "copy_sub_task_info")
    class SnapshotIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RefBlobIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RefBlobInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RefBlobInfo, _Mapping]] = ...) -> None: ...
    AZURE_REPLICATION_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_replication_entity_info: _descriptor.FieldDescriptor
    STORAGE_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    REF_BLOB_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    COPY_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    storage_resource_group: _entity_pb2.EntityProto
    storage_account: _entity_pb2.EntityProto
    storage_container: _entity_pb2.EntityProto
    snapshot_id_map: _containers.ScalarMap[str, str]
    vm_config: VMConfig
    cloud_replication_target: _policy_pb2.CloudDeployTarget
    ref_blob_id_map: _containers.MessageMap[str, RefBlobInfo]
    copy_sub_task_info: AzureToAzureCopyTaskInfo
    def __init__(self, storage_resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_account: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_container: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., snapshot_id_map: _Optional[_Mapping[str, str]] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., cloud_replication_target: _Optional[_Union[_policy_pb2.CloudDeployTarget, _Mapping]] = ..., ref_blob_id_map: _Optional[_Mapping[str, RefBlobInfo]] = ..., copy_sub_task_info: _Optional[_Union[AzureToAzureCopyTaskInfo, _Mapping]] = ...) -> None: ...

class CloudDeployInfo(_message.Message):
    __slots__ = ("status", "error", "view_deletion_error", "to_recover_vm_idx", "to_recover_disk_idx", "to_recover_disk_lowest_offset", "sub_tasks_vec", "total_bytes_to_write_to_source", "enable_max_disks_count", "enable_inline_linux_vm_conversion", "disk_area_list_map", "active_disk_areas", "warnings")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[CloudDeployInfo.Status]
        kCloned: _ClassVar[CloudDeployInfo.Status]
        kVMInfoFetched: _ClassVar[CloudDeployInfo.Status]
        kDiskMappingFetched: _ClassVar[CloudDeployInfo.Status]
        kPermitGranted: _ClassVar[CloudDeployInfo.Status]
        kConflictChecked: _ClassVar[CloudDeployInfo.Status]
        kBlobsCreated: _ClassVar[CloudDeployInfo.Status]
        kSubTasksCreated: _ClassVar[CloudDeployInfo.Status]
        kSubTasksFinished: _ClassVar[CloudDeployInfo.Status]
        kCopySnapshotDone: _ClassVar[CloudDeployInfo.Status]
        kManagedDiskCreationInitialized: _ClassVar[CloudDeployInfo.Status]
        kManagedDiskCreated: _ClassVar[CloudDeployInfo.Status]
        kWriteableSASUrlGenerated: _ClassVar[CloudDeployInfo.Status]
        kSASUrlRevoked: _ClassVar[CloudDeployInfo.Status]
        kVMFilesCopied: _ClassVar[CloudDeployInfo.Status]
        kVMsCreated: _ClassVar[CloudDeployInfo.Status]
        kDestinationViewDeleted: _ClassVar[CloudDeployInfo.Status]
        kFinished: _ClassVar[CloudDeployInfo.Status]
    kStarted: CloudDeployInfo.Status
    kCloned: CloudDeployInfo.Status
    kVMInfoFetched: CloudDeployInfo.Status
    kDiskMappingFetched: CloudDeployInfo.Status
    kPermitGranted: CloudDeployInfo.Status
    kConflictChecked: CloudDeployInfo.Status
    kBlobsCreated: CloudDeployInfo.Status
    kSubTasksCreated: CloudDeployInfo.Status
    kSubTasksFinished: CloudDeployInfo.Status
    kCopySnapshotDone: CloudDeployInfo.Status
    kManagedDiskCreationInitialized: CloudDeployInfo.Status
    kManagedDiskCreated: CloudDeployInfo.Status
    kWriteableSASUrlGenerated: CloudDeployInfo.Status
    kSASUrlRevoked: CloudDeployInfo.Status
    kVMFilesCopied: CloudDeployInfo.Status
    kVMsCreated: CloudDeployInfo.Status
    kDestinationViewDeleted: CloudDeployInfo.Status
    kFinished: CloudDeployInfo.Status
    class DiskAreaListMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _disk_pb2.DiskAreaListProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ...) -> None: ...
    class ActiveDiskAreasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _disk_pb2.DiskAreaProto
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ...) -> None: ...
    AZURE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_restore_info: _descriptor.FieldDescriptor
    AZURE_CLOUD_DEPLOY_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_cloud_deploy_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIEW_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_VM_IDX_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_DISK_IDX_FIELD_NUMBER: _ClassVar[int]
    TO_RECOVER_DISK_LOWEST_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MAX_DISKS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INLINE_LINUX_VM_CONVERSION_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_LIST_MAP_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DISK_AREAS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    status: CloudDeployInfo.Status
    error: _error_pb2.ErrorProto
    view_deletion_error: _error_pb2.ErrorProto
    to_recover_vm_idx: int
    to_recover_disk_idx: int
    to_recover_disk_lowest_offset: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    total_bytes_to_write_to_source: int
    enable_max_disks_count: bool
    enable_inline_linux_vm_conversion: bool
    disk_area_list_map: _containers.MessageMap[int, _disk_pb2.DiskAreaListProto]
    active_disk_areas: _containers.MessageMap[int, _disk_pb2.DiskAreaProto]
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, status: _Optional[_Union[CloudDeployInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., view_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., to_recover_vm_idx: _Optional[int] = ..., to_recover_disk_idx: _Optional[int] = ..., to_recover_disk_lowest_offset: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., enable_max_disks_count: bool = ..., enable_inline_linux_vm_conversion: bool = ..., disk_area_list_map: _Optional[_Mapping[int, _disk_pb2.DiskAreaListProto]] = ..., active_disk_areas: _Optional[_Mapping[int, _disk_pb2.DiskAreaProto]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class ClonedEntityInfo(_message.Message):
    __slots__ = ("vm_info", "physical_entity")
    class VMInfo(_message.Message):
        __slots__ = ("name", "azure_blob_names", "managed_disk_info_vec", "tear_down_supported")
        NAME_FIELD_NUMBER: _ClassVar[int]
        AZURE_BLOB_NAMES_FIELD_NUMBER: _ClassVar[int]
        MANAGED_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        TEAR_DOWN_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        name: str
        azure_blob_names: _containers.RepeatedScalarFieldContainer[str]
        managed_disk_info_vec: _containers.RepeatedCompositeFieldContainer[_azure_param_pb2.ManagedDiskInfo]
        tear_down_supported: bool
        def __init__(self, name: _Optional[str] = ..., azure_blob_names: _Optional[_Iterable[str]] = ..., managed_disk_info_vec: _Optional[_Iterable[_Union[_azure_param_pb2.ManagedDiskInfo, _Mapping]]] = ..., tear_down_supported: bool = ...) -> None: ...
    AZURE_CLONED_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_cloned_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    vm_info: ClonedEntityInfo.VMInfo
    physical_entity: _entity_pb2.EntityProto
    def __init__(self, vm_info: _Optional[_Union[ClonedEntityInfo.VMInfo, _Mapping]] = ..., physical_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class VirtualDisk(_message.Message):
    __slots__ = ("key", "disk_metadata", "snapshot_id", "snapshot_creation_time_usecs", "delta_type", "delta_info", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "query_disk_error", "previous_snapshot_id", "previous_snapshot_sas_url", "heimdall_request_id", "previous_heimdall_request_id", "zero_delta_info", "private_endpoint_fqdn", "private_endpoint_ipv4_address")
    AZURE_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    azure_virtual_disk: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    DISK_METADATA_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAPSHOT_SAS_URL_FIELD_NUMBER: _ClassVar[int]
    HEIMDALL_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_HEIMDALL_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ZERO_DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FQDN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    key: int
    disk_metadata: _azure_param_pb2.DiskMetadata
    snapshot_id: str
    snapshot_creation_time_usecs: int
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    query_disk_error: _error_pb2.ErrorProto
    previous_snapshot_id: str
    previous_snapshot_sas_url: str
    heimdall_request_id: str
    previous_heimdall_request_id: str
    zero_delta_info: _cbt_delta_pb2.CBTDeltaInfo
    private_endpoint_fqdn: str
    private_endpoint_ipv4_address: str
    def __init__(self, key: _Optional[int] = ..., disk_metadata: _Optional[_Union[_azure_param_pb2.DiskMetadata, _Mapping]] = ..., snapshot_id: _Optional[str] = ..., snapshot_creation_time_usecs: _Optional[int] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., previous_snapshot_id: _Optional[str] = ..., previous_snapshot_sas_url: _Optional[str] = ..., heimdall_request_id: _Optional[str] = ..., previous_heimdall_request_id: _Optional[str] = ..., zero_delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., private_endpoint_fqdn: _Optional[str] = ..., private_endpoint_ipv4_address: _Optional[str] = ...) -> None: ...

class VMConfig(_message.Message):
    __slots__ = ("vm_info", "virtual_disks_vec", "permit_entity")
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    PERMIT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    vm_info: _azure_param_pb2.VMInfoResult
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    permit_entity: _entity_pb2.EntityProto
    def __init__(self, vm_info: _Optional[_Union[_azure_param_pb2.VMInfoResult, _Mapping]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., permit_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "server_vm_info", "status", "virtual_disks_vec", "sub_tasks_vec", "error", "snapshot_deletion_error", "quiesced", "sub_file_size_mb", "take_separate_sub_task_permit")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kVMInfoFetched: _ClassVar[SnapshotInfo.Status]
        kCreateSnapshotInitialized: _ClassVar[SnapshotInfo.Status]
        kManagedSnapshotFinished: _ClassVar[SnapshotInfo.Status]
        kCopySnapshotInitialized: _ClassVar[SnapshotInfo.Status]
        kCreateSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kDeltaPageRangesFetched: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
        kSnapshotDeleted: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kVMInfoFetched: SnapshotInfo.Status
    kCreateSnapshotInitialized: SnapshotInfo.Status
    kManagedSnapshotFinished: SnapshotInfo.Status
    kCopySnapshotInitialized: SnapshotInfo.Status
    kCreateSnapshotDone: SnapshotInfo.Status
    kDeltaPageRangesFetched: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    kSnapshotDeleted: SnapshotInfo.Status
    AZURE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SERVER_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    TAKE_SEPARATE_SUB_TASK_PERMIT_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    server_vm_info: _azure_param_pb2.VMInfoResult
    status: SnapshotInfo.Status
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    snapshot_deletion_error: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    quiesced: bool
    sub_file_size_mb: int
    take_separate_sub_task_permit: bool
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., server_vm_info: _Optional[_Union[_azure_param_pb2.VMInfoResult, _Mapping]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., quiesced: bool = ..., sub_file_size_mb: _Optional[int] = ..., take_separate_sub_task_permit: bool = ...) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("vm_info", "cohesity_agent_installation_state_proto", "status", "should_uninstall_agent")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMInfoFetched: _ClassVar[RestoreEnvironmentInfo.Status]
        kCohesityAgentInstalled: _ClassVar[RestoreEnvironmentInfo.Status]
    kVMInfoFetched: RestoreEnvironmentInfo.Status
    kCohesityAgentInstalled: RestoreEnvironmentInfo.Status
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    COHESITY_AGENT_INSTALLATION_STATE_PROTO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_UNINSTALL_AGENT_FIELD_NUMBER: _ClassVar[int]
    vm_info: _azure_param_pb2.VMInfoResult
    cohesity_agent_installation_state_proto: _cloud_pb2.CohesityAgentInstallationStateProto
    status: RestoreEnvironmentInfo.Status
    should_uninstall_agent: bool
    def __init__(self, vm_info: _Optional[_Union[_azure_param_pb2.VMInfoResult, _Mapping]] = ..., cohesity_agent_installation_state_proto: _Optional[_Union[_cloud_pb2.CohesityAgentInstallationStateProto, _Mapping]] = ..., status: _Optional[_Union[RestoreEnvironmentInfo.Status, str]] = ..., should_uninstall_agent: bool = ...) -> None: ...

class AzureSqlEntityMetadata(_message.Message):
    __slots__ = ("azure_sql_metadata",)
    AZURE_SQL_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    azure_sql_entity_metadata: _descriptor.FieldDescriptor
    AZURE_SQL_METADATA_FIELD_NUMBER: _ClassVar[int]
    azure_sql_metadata: _azure_sql_pb2.AzureSQLMetadata
    def __init__(self, azure_sql_metadata: _Optional[_Union[_azure_sql_pb2.AzureSQLMetadata, _Mapping]] = ...) -> None: ...
