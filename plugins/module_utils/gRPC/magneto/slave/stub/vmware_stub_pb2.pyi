from atom.base import event_pb2 as _event_pb2
from bridge.base import error_pb2 as _error_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.connectors.vmware import vmware_pb2 as _vmware_pb2_1
from magneto.master.base import master_pb2 as _master_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareVMBackupUpdateArg(_message.Message):
    __slots__ = ("root_path", "relative_snapshot_dir")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...

class SetupVMFilesUpdateArg(_message.Message):
    __slots__ = ("root_path", "relative_snapshot_dir", "virtual_disk_vec", "nvram_file_download_status", "warnings")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    NVRAM_FILE_DOWNLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    relative_snapshot_dir: str
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDisk]
    nvram_file_download_status: _vmware_pb2_1.FileTransferStatus
    warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., virtual_disk_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDisk, _Mapping]]] = ..., nvram_file_download_status: _Optional[_Union[_vmware_pb2_1.FileTransferStatus, str]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class VMwareStartRestoreTaskArg(_message.Message):
    __slots__ = ("resource_pool_moref", "datastore_moref_vec", "network_config", "vcenter_connector_params", "vcd_config", "using_bios_uuid", "vm_name_in_vcd", "storage_profile_name", "storage_profile_uuid", "tag_name_to_uuid_map", "vc_id", "selected_datastore_idx", "catalog_uuid", "reuse_cdp_restore_view", "vm_name_DEPRECATED", "vm_folder_moref_DEPRECATED", "leverage_san_transport")
    class TagNameToUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VMWARE_START_RESTORE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    vmware_start_restore_task_arg: _descriptor.FieldDescriptor
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VCENTER_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VCD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USING_BIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_IN_VCD_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PROFILE_UUID_FIELD_NUMBER: _ClassVar[int]
    TAG_NAME_TO_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    VC_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DATASTORE_IDX_FIELD_NUMBER: _ClassVar[int]
    CATALOG_UUID_FIELD_NUMBER: _ClassVar[int]
    REUSE_CDP_RESTORE_VIEW_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    resource_pool_moref: _vmware_common_pb2.MORef
    datastore_moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    network_config: _vmware_pb2_1.NetworkConfigInfo
    vcenter_connector_params: _magneto_pb2.ConnectorParams
    vcd_config: _master_pb2.RestoredObjectVCDConfigProto
    using_bios_uuid: bool
    vm_name_in_vcd: _containers.RepeatedScalarFieldContainer[str]
    storage_profile_name: str
    storage_profile_uuid: str
    tag_name_to_uuid_map: _containers.ScalarMap[str, str]
    vc_id: str
    selected_datastore_idx: int
    catalog_uuid: str
    reuse_cdp_restore_view: bool
    vm_name_DEPRECATED: str
    vm_folder_moref_DEPRECATED: _vmware_common_pb2.MORef
    leverage_san_transport: bool
    def __init__(self, resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., network_config: _Optional[_Union[_vmware_pb2_1.NetworkConfigInfo, _Mapping]] = ..., vcenter_connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., vcd_config: _Optional[_Union[_master_pb2.RestoredObjectVCDConfigProto, _Mapping]] = ..., using_bios_uuid: bool = ..., vm_name_in_vcd: _Optional[_Iterable[str]] = ..., storage_profile_name: _Optional[str] = ..., storage_profile_uuid: _Optional[str] = ..., tag_name_to_uuid_map: _Optional[_Mapping[str, str]] = ..., vc_id: _Optional[str] = ..., selected_datastore_idx: _Optional[int] = ..., catalog_uuid: _Optional[str] = ..., reuse_cdp_restore_view: bool = ..., vm_name_DEPRECATED: _Optional[str] = ..., vm_folder_moref_DEPRECATED: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., leverage_san_transport: bool = ...) -> None: ...

class CloneVMsUpdateArg(_message.Message):
    __slots__ = ("cloned_vms",)
    class ClonedVM(_message.Message):
        __slots__ = ("vm_entity", "sparse_vm_config", "relative_cloned_paths", "relative_cloned_descriptor_paths", "xml_vm_config", "new_to_old_disk_uuid_map", "vapp_info", "nvram_file_clone_status", "warnings")
        class NewToOldDiskUuidMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONED_PATHS_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONED_DESCRIPTOR_PATHS_FIELD_NUMBER: _ClassVar[int]
        XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        NEW_TO_OLD_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
        VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
        NVRAM_FILE_CLONE_STATUS_FIELD_NUMBER: _ClassVar[int]
        WARNINGS_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _vmware_pb2.Entity
        sparse_vm_config: _vmware_pb2_1.SparseVMConfig
        relative_cloned_paths: _containers.RepeatedScalarFieldContainer[str]
        relative_cloned_descriptor_paths: _containers.RepeatedScalarFieldContainer[str]
        xml_vm_config: str
        new_to_old_disk_uuid_map: _containers.ScalarMap[str, str]
        vapp_info: _magneto_pb2.BackupTaskStateVappInfoProto
        nvram_file_clone_status: _vmware_pb2_1.FileTransferStatus
        warnings: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
        def __init__(self, vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[_vmware_pb2_1.SparseVMConfig, _Mapping]] = ..., relative_cloned_paths: _Optional[_Iterable[str]] = ..., relative_cloned_descriptor_paths: _Optional[_Iterable[str]] = ..., xml_vm_config: _Optional[str] = ..., new_to_old_disk_uuid_map: _Optional[_Mapping[str, str]] = ..., vapp_info: _Optional[_Union[_magneto_pb2.BackupTaskStateVappInfoProto, _Mapping]] = ..., nvram_file_clone_status: _Optional[_Union[_vmware_pb2_1.FileTransferStatus, str]] = ..., warnings: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...
    CLONED_VMS_FIELD_NUMBER: _ClassVar[int]
    cloned_vms: _containers.RepeatedCompositeFieldContainer[CloneVMsUpdateArg.ClonedVM]
    def __init__(self, cloned_vms: _Optional[_Iterable[_Union[CloneVMsUpdateArg.ClonedVM, _Mapping]]] = ...) -> None: ...

class PushFilesUpdateArg(_message.Message):
    __slots__ = ("transfer_status",)
    class TransferStatus(_message.Message):
        __slots__ = ("file_name", "file_upload_status", "warnings")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_UPLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
        WARNINGS_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        file_upload_status: _vmware_pb2_1.FileTransferStatus
        warnings: _error_pb2.ErrorProto
        def __init__(self, file_name: _Optional[str] = ..., file_upload_status: _Optional[_Union[_vmware_pb2_1.FileTransferStatus, str]] = ..., warnings: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    TRANSFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    transfer_status: _containers.RepeatedCompositeFieldContainer[PushFilesUpdateArg.TransferStatus]
    def __init__(self, transfer_status: _Optional[_Iterable[_Union[PushFilesUpdateArg.TransferStatus, _Mapping]]] = ...) -> None: ...

class FetchVMsInfoUpdateArg(_message.Message):
    __slots__ = ("vms_info",)
    class VMInfo(_message.Message):
        __slots__ = ("vm_entity", "xml_vm_config", "sparse_vm_config", "vapp_info")
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _vmware_pb2.Entity
        xml_vm_config: str
        sparse_vm_config: _vmware_pb2_1.SparseVMConfig
        vapp_info: _magneto_pb2.BackupTaskStateVappInfoProto
        def __init__(self, vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., xml_vm_config: _Optional[str] = ..., sparse_vm_config: _Optional[_Union[_vmware_pb2_1.SparseVMConfig, _Mapping]] = ..., vapp_info: _Optional[_Union[_magneto_pb2.BackupTaskStateVappInfoProto, _Mapping]] = ...) -> None: ...
    VMS_INFO_FIELD_NUMBER: _ClassVar[int]
    vms_info: _containers.RepeatedCompositeFieldContainer[FetchVMsInfoUpdateArg.VMInfo]
    def __init__(self, vms_info: _Optional[_Iterable[_Union[FetchVMsInfoUpdateArg.VMInfo, _Mapping]]] = ...) -> None: ...

class QueryAllocatedVMDiskUpdateArg(_message.Message):
    __slots__ = ("disk_index", "disk_areas")
    DISK_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISK_AREAS_FIELD_NUMBER: _ClassVar[int]
    disk_index: int
    disk_areas: _disk_pb2.DiskAreaListProto
    def __init__(self, disk_index: _Optional[int] = ..., disk_areas: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ...) -> None: ...

class LogApplyUpdateArg(_message.Message):
    __slots__ = ("restore_update_arg", "last_applied_sequence_number")
    RESTORE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    LAST_APPLIED_SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    restore_update_arg: _stub_pb2.RestoreDiskUpdateArg
    last_applied_sequence_number: _event_pb2.Sequencer
    def __init__(self, restore_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., last_applied_sequence_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ...) -> None: ...

class VMwareActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_vm_backup_update_arg", "setup_vm_files_update_arg", "backup_disk_update_arg", "clone_vms_update_arg", "fetch_vms_info_update_arg", "restore_disk_area_update_arg", "end_sub_task_update_arg", "query_allocated_vm_disk_update_arg", "log_apply_update_arg", "push_files_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareVMBackupUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kCloneVMsUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kFetchVMsInfoUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kCloseVMDiskUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kRestoreDiskAreaUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kRestoreEndSubTaskUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kQueryAllocatedVMDiskUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kLogApplyUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kEndVMAccessUpdate: _ClassVar[VMwareActionUpdateArg.Type]
        kPushFilesUpdate: _ClassVar[VMwareActionUpdateArg.Type]
    kPrepareVMBackupUpdate: VMwareActionUpdateArg.Type
    kSetupVMFilesUpdate: VMwareActionUpdateArg.Type
    kBackupVMDiskUpdate: VMwareActionUpdateArg.Type
    kCloneVMsUpdate: VMwareActionUpdateArg.Type
    kFetchVMsInfoUpdate: VMwareActionUpdateArg.Type
    kCloseVMDiskUpdate: VMwareActionUpdateArg.Type
    kEndVMBackupUpdate: VMwareActionUpdateArg.Type
    kRestoreDiskAreaUpdate: VMwareActionUpdateArg.Type
    kRestoreEndSubTaskUpdate: VMwareActionUpdateArg.Type
    kQueryAllocatedVMDiskUpdate: VMwareActionUpdateArg.Type
    kLogApplyUpdate: VMwareActionUpdateArg.Type
    kEndVMAccessUpdate: VMwareActionUpdateArg.Type
    kPushFilesUpdate: VMwareActionUpdateArg.Type
    VMWARE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    vmware_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_VM_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_VMS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_VMS_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_AREA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    QUERY_ALLOCATED_VM_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    LOG_APPLY_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    PUSH_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: VMwareActionUpdateArg.Type
    prepare_vm_backup_update_arg: PrepareVMBackupUpdateArg
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    clone_vms_update_arg: CloneVMsUpdateArg
    fetch_vms_info_update_arg: FetchVMsInfoUpdateArg
    restore_disk_area_update_arg: _stub_pb2.RestoreDiskUpdateArg
    end_sub_task_update_arg: _stub_pb2.EndSubTaskUpdateArg
    query_allocated_vm_disk_update_arg: QueryAllocatedVMDiskUpdateArg
    log_apply_update_arg: LogApplyUpdateArg
    push_files_update_arg: PushFilesUpdateArg
    def __init__(self, type: _Optional[_Union[VMwareActionUpdateArg.Type, str]] = ..., prepare_vm_backup_update_arg: _Optional[_Union[PrepareVMBackupUpdateArg, _Mapping]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., clone_vms_update_arg: _Optional[_Union[CloneVMsUpdateArg, _Mapping]] = ..., fetch_vms_info_update_arg: _Optional[_Union[FetchVMsInfoUpdateArg, _Mapping]] = ..., restore_disk_area_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., end_sub_task_update_arg: _Optional[_Union[_stub_pb2.EndSubTaskUpdateArg, _Mapping]] = ..., query_allocated_vm_disk_update_arg: _Optional[_Union[QueryAllocatedVMDiskUpdateArg, _Mapping]] = ..., log_apply_update_arg: _Optional[_Union[LogApplyUpdateArg, _Mapping]] = ..., push_files_update_arg: _Optional[_Union[PushFilesUpdateArg, _Mapping]] = ...) -> None: ...

class VMwareEndSubTaskUpdateArg(_message.Message):
    __slots__ = ("transport_mode",)
    VMWARE_END_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    vmware_end_sub_task_update_arg: _descriptor.FieldDescriptor
    TRANSPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    transport_mode: str
    def __init__(self, transport_mode: _Optional[str] = ...) -> None: ...

class RestoreEntityArg(_message.Message):
    __slots__ = ("storage_device_snapshot_info_set", "datastore_to_storage_device_snapshot_info_idx_map", "primary_storage_connection_params", "primary_storage_source_id", "virtual_disks_vec", "disks_with_allocated_blocks_info_vec", "allocated_block_info_file_suffix")
    class DatastoreToStorageDeviceSnapshotInfoIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VMWARE_RESTORE_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    vmware_restore_entity_arg: _descriptor.FieldDescriptor
    STORAGE_DEVICE_SNAPSHOT_INFO_SET_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_TO_STORAGE_DEVICE_SNAPSHOT_INFO_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    DISKS_WITH_ALLOCATED_BLOCKS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_BLOCK_INFO_FILE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    storage_device_snapshot_info_set: _containers.RepeatedCompositeFieldContainer[_storage_pb2.StorageDeviceSnapshotInfoProto]
    datastore_to_storage_device_snapshot_info_idx_map: _containers.ScalarMap[str, int]
    primary_storage_connection_params: _magneto_pb2.ConnectorParams
    primary_storage_source_id: int
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2_1.VirtualDisk]
    disks_with_allocated_blocks_info_vec: _containers.RepeatedScalarFieldContainer[str]
    allocated_block_info_file_suffix: str
    def __init__(self, storage_device_snapshot_info_set: _Optional[_Iterable[_Union[_storage_pb2.StorageDeviceSnapshotInfoProto, _Mapping]]] = ..., datastore_to_storage_device_snapshot_info_idx_map: _Optional[_Mapping[str, int]] = ..., primary_storage_connection_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., primary_storage_source_id: _Optional[int] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[_vmware_pb2_1.VirtualDisk, _Mapping]]] = ..., disks_with_allocated_blocks_info_vec: _Optional[_Iterable[str]] = ..., allocated_block_info_file_suffix: _Optional[str] = ...) -> None: ...
