from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base import cloud_pb2 as _cloud_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import azure_pb2 as _azure_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.connectors.azure import azure_pb2 as _azure_pb2_1
from magneto.connectors.azure import azure_param_pb2 as _azure_param_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupAzureVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "vm_config", "page_range_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupAzureVMArg.Type]
        kSetupFiles: _ClassVar[BackupAzureVMArg.Type]
        kBackupDisk: _ClassVar[BackupAzureVMArg.Type]
        kEndSubTask: _ClassVar[BackupAzureVMArg.Type]
        kEndBackup: _ClassVar[BackupAzureVMArg.Type]
        kQueryPageRange: _ClassVar[BackupAzureVMArg.Type]
    kPrepareBackup: BackupAzureVMArg.Type
    kSetupFiles: BackupAzureVMArg.Type
    kBackupDisk: BackupAzureVMArg.Type
    kEndSubTask: BackupAzureVMArg.Type
    kEndBackup: BackupAzureVMArg.Type
    kQueryPageRange: BackupAzureVMArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PAGE_RANGE_ARG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupAzureVMArg.Type
    root_entity: _azure_pb2.Entity
    vm_entity: _azure_pb2.Entity
    vm_config: _azure_pb2_1.VMConfig
    page_range_arg: _azure_param_pb2.GetPageRangesArg
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupAzureVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_azure_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_azure_pb2.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_azure_pb2_1.VMConfig, _Mapping]] = ..., page_range_arg: _Optional[_Union[_azure_param_pb2.GetPageRangesArg, _Mapping]] = ...) -> None: ...

class RestoreVMsArg(_message.Message):
    __slots__ = ("type", "vm_restore_infos", "view_box_id", "destination_view_name", "storage_account", "storage_container", "storage_key")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreateBlobs: _ClassVar[RestoreVMsArg.Type]
        kCopyDiskArea: _ClassVar[RestoreVMsArg.Type]
        kEndRestore: _ClassVar[RestoreVMsArg.Type]
        kDeleteBlobs: _ClassVar[RestoreVMsArg.Type]
        kEndSubTask: _ClassVar[RestoreVMsArg.Type]
        kFetchVMsInfo: _ClassVar[RestoreVMsArg.Type]
    kCreateBlobs: RestoreVMsArg.Type
    kCopyDiskArea: RestoreVMsArg.Type
    kEndRestore: RestoreVMsArg.Type
    kDeleteBlobs: RestoreVMsArg.Type
    kEndSubTask: RestoreVMsArg.Type
    kFetchVMsInfo: RestoreVMsArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("vm_entity", "entity", "azure_blob_infos", "chained_disk_mapping_info")
        class AzureBlobInfo(_message.Message):
            __slots__ = ("name", "disk_relative_filepath", "size", "area", "is_last_disk_area", "source_offset", "resource_group_name", "storage_account_name", "storage_container_name", "storage_access_key", "dest_sas_url", "azure_stack_region", "azure_stack_hub_domain_name", "private_endpoint_fqdn", "private_endpoint_ipv4_address")
            NAME_FIELD_NUMBER: _ClassVar[int]
            DISK_RELATIVE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            AREA_FIELD_NUMBER: _ClassVar[int]
            IS_LAST_DISK_AREA_FIELD_NUMBER: _ClassVar[int]
            SOURCE_OFFSET_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            DEST_SAS_URL_FIELD_NUMBER: _ClassVar[int]
            AZURE_STACK_REGION_FIELD_NUMBER: _ClassVar[int]
            AZURE_STACK_HUB_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
            PRIVATE_ENDPOINT_FQDN_FIELD_NUMBER: _ClassVar[int]
            PRIVATE_ENDPOINT_IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            name: str
            disk_relative_filepath: str
            size: int
            area: _disk_pb2.DiskAreaProto
            is_last_disk_area: bool
            source_offset: int
            resource_group_name: str
            storage_account_name: str
            storage_container_name: str
            storage_access_key: str
            dest_sas_url: str
            azure_stack_region: str
            azure_stack_hub_domain_name: str
            private_endpoint_fqdn: str
            private_endpoint_ipv4_address: str
            def __init__(self, name: _Optional[str] = ..., disk_relative_filepath: _Optional[str] = ..., size: _Optional[int] = ..., area: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ..., is_last_disk_area: bool = ..., source_offset: _Optional[int] = ..., resource_group_name: _Optional[str] = ..., storage_account_name: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., storage_access_key: _Optional[str] = ..., dest_sas_url: _Optional[str] = ..., azure_stack_region: _Optional[str] = ..., azure_stack_hub_domain_name: _Optional[str] = ..., private_endpoint_fqdn: _Optional[str] = ..., private_endpoint_ipv4_address: _Optional[str] = ...) -> None: ...
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        AZURE_BLOB_INFOS_FIELD_NUMBER: _ClassVar[int]
        CHAINED_DISK_MAPPING_INFO_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _vmware_pb2.Entity
        entity: _entity_pb2.EntityProto
        azure_blob_infos: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo.AzureBlobInfo]
        chained_disk_mapping_info: _cloud_pb2.ChainedDiskMappingInfo
        def __init__(self, vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., azure_blob_infos: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo.AzureBlobInfo, _Mapping]]] = ..., chained_disk_mapping_info: _Optional[_Union[_cloud_pb2.ChainedDiskMappingInfo, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    type: RestoreVMsArg.Type
    vm_restore_infos: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo]
    view_box_id: int
    destination_view_name: str
    storage_account: _azure_pb2.Entity
    storage_container: _azure_pb2.Entity
    storage_key: _azure_pb2.Entity
    def __init__(self, type: _Optional[_Union[RestoreVMsArg.Type, str]] = ..., vm_restore_infos: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., destination_view_name: _Optional[str] = ..., storage_account: _Optional[_Union[_azure_pb2.Entity, _Mapping]] = ..., storage_container: _Optional[_Union[_azure_pb2.Entity, _Mapping]] = ..., storage_key: _Optional[_Union[_azure_pb2.Entity, _Mapping]] = ...) -> None: ...

class AzureActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_vm_arg", "restore_vms_arg", "cancel_task_arg", "vault_type")
    AZURE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    azure_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMS_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    VAULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_vm_arg: BackupAzureVMArg
    restore_vms_arg: RestoreVMsArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    vault_type: _cluster_config_pb2.ClusterConfigProto.Vault.Type
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_vm_arg: _Optional[_Union[BackupAzureVMArg, _Mapping]] = ..., restore_vms_arg: _Optional[_Union[RestoreVMsArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ..., vault_type: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.Type, str]] = ...) -> None: ...
