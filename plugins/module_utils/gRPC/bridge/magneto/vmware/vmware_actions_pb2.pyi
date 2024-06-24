from atom.base import event_pb2 as _event_pb2
from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import san_pb2 as _san_pb2
from magneto.connectors.vmware import vmware_pb2 as _vmware_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "tmp_vm_entity", "snapshot_moref", "xml_vm_config", "sparse_vm_config", "vapp_info", "query_allocated_vm_disk_info", "vm_disk_lun_info_vec", "use_san_transport", "use_fc_san_transport", "allow_nbdssl_transport_fallback", "skip_write_descriptor_file", "include_vm_nvram_file", "datacenter_name", "leverage_san_storage_snapshot_v2", "processs_vm_storage_snapshot_v2")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareVMBackup: _ClassVar[BackupVMArg.Type]
        kSetupVMFiles: _ClassVar[BackupVMArg.Type]
        kQueryAllocatedVMDisk: _ClassVar[BackupVMArg.Type]
        kBackupVMDisk: _ClassVar[BackupVMArg.Type]
        kCloseVMDisk: _ClassVar[BackupVMArg.Type]
        kEndVMBackup: _ClassVar[BackupVMArg.Type]
        kEndVMAccess: _ClassVar[BackupVMArg.Type]
    kPrepareVMBackup: BackupVMArg.Type
    kSetupVMFiles: BackupVMArg.Type
    kQueryAllocatedVMDisk: BackupVMArg.Type
    kBackupVMDisk: BackupVMArg.Type
    kCloseVMDisk: BackupVMArg.Type
    kEndVMBackup: BackupVMArg.Type
    kEndVMAccess: BackupVMArg.Type
    class QueryAllocatedVMDiskInfo(_message.Message):
        __slots__ = ("disk_name", "disk_capacity", "disk_index", "chunk_size")
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_CAPACITY_FIELD_NUMBER: _ClassVar[int]
        DISK_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        disk_name: str
        disk_capacity: int
        disk_index: int
        chunk_size: int
        def __init__(self, disk_name: _Optional[str] = ..., disk_capacity: _Optional[int] = ..., disk_index: _Optional[int] = ..., chunk_size: _Optional[int] = ...) -> None: ...
    class VMDiskLunInfo(_message.Message):
        __slots__ = ("san_port_vec", "lun_serial_number")
        SAN_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
        LUN_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        san_port_vec: _containers.RepeatedCompositeFieldContainer[_san_pb2.SanPort]
        lun_serial_number: str
        def __init__(self, san_port_vec: _Optional[_Iterable[_Union[_san_pb2.SanPort, _Mapping]]] = ..., lun_serial_number: _Optional[str] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TMP_VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
    QUERY_ALLOCATED_VM_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_LUN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    USE_FC_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NBDSSL_TRANSPORT_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    SKIP_WRITE_DESCRIPTOR_FILE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VM_NVRAM_FILE_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    PROCESSS_VM_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupVMArg.Type
    root_entity: _vmware_pb2.Entity
    vm_entity: _vmware_pb2.Entity
    tmp_vm_entity: _vmware_pb2.Entity
    snapshot_moref: _vmware_common_pb2.MORef
    xml_vm_config: bytes
    sparse_vm_config: _vmware_pb2_1.SparseVMConfig
    vapp_info: _magneto_pb2.BackupTaskStateVappInfoProto
    query_allocated_vm_disk_info: BackupVMArg.QueryAllocatedVMDiskInfo
    vm_disk_lun_info_vec: _containers.RepeatedCompositeFieldContainer[BackupVMArg.VMDiskLunInfo]
    use_san_transport: bool
    use_fc_san_transport: bool
    allow_nbdssl_transport_fallback: bool
    skip_write_descriptor_file: bool
    include_vm_nvram_file: bool
    datacenter_name: str
    leverage_san_storage_snapshot_v2: bool
    processs_vm_storage_snapshot_v2: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., tmp_vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., xml_vm_config: _Optional[bytes] = ..., sparse_vm_config: _Optional[_Union[_vmware_pb2_1.SparseVMConfig, _Mapping]] = ..., vapp_info: _Optional[_Union[_magneto_pb2.BackupTaskStateVappInfoProto, _Mapping]] = ..., query_allocated_vm_disk_info: _Optional[_Union[BackupVMArg.QueryAllocatedVMDiskInfo, _Mapping]] = ..., vm_disk_lun_info_vec: _Optional[_Iterable[_Union[BackupVMArg.VMDiskLunInfo, _Mapping]]] = ..., use_san_transport: bool = ..., use_fc_san_transport: bool = ..., allow_nbdssl_transport_fallback: bool = ..., skip_write_descriptor_file: bool = ..., include_vm_nvram_file: bool = ..., datacenter_name: _Optional[str] = ..., leverage_san_storage_snapshot_v2: bool = ..., processs_vm_storage_snapshot_v2: bool = ...) -> None: ...

class PushFilesToDatastoreArg(_message.Message):
    __slots__ = ("file_path_vec", "datastore_name", "datacenter_name", "target_folder_path")
    FILE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path_vec: _containers.RepeatedScalarFieldContainer[str]
    datastore_name: str
    datacenter_name: str
    target_folder_path: str
    def __init__(self, file_path_vec: _Optional[_Iterable[str]] = ..., datastore_name: _Optional[str] = ..., datacenter_name: _Optional[str] = ..., target_folder_path: _Optional[str] = ...) -> None: ...

class RestoreVMsArg(_message.Message):
    __slots__ = ("type", "vm_restore_infos", "view_box_id", "view_name", "create_view", "is_internal_view", "path_prefix", "generate_random_disk_uuid_for_all_disks", "view_whitelist_ip_addr_str_vec", "view_whitelist_ip_ranges_vec", "force_include_vmdk_suffix", "generate_random_disk_uuid_update_map", "include_vm_config", "root_path", "skip_clone_flat_vmdk_file", "skip_clone_virtual_disk_files", "skip_clone_and_rename_vmdk_files", "include_xml_config", "use_san_transport", "allow_nbdssl_transport_fallback", "include_vm_nvram_file", "push_files_to_datastore_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneVMs: _ClassVar[RestoreVMsArg.Type]
        kFetchVMsInfo: _ClassVar[RestoreVMsArg.Type]
        kRestoreVMDisk: _ClassVar[RestoreVMsArg.Type]
        kEndSubTask: _ClassVar[RestoreVMsArg.Type]
        kDeleteVMs: _ClassVar[RestoreVMsArg.Type]
        kLogApply: _ClassVar[RestoreVMsArg.Type]
        kPushFilesToDatastore: _ClassVar[RestoreVMsArg.Type]
    kCloneVMs: RestoreVMsArg.Type
    kFetchVMsInfo: RestoreVMsArg.Type
    kRestoreVMDisk: RestoreVMsArg.Type
    kEndSubTask: RestoreVMsArg.Type
    kDeleteVMs: RestoreVMsArg.Type
    kLogApply: RestoreVMsArg.Type
    kPushFilesToDatastore: RestoreVMsArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "vm_entity", "root_entity", "dynamic_disk_volumes_to_convert", "update_disk_unique_id", "fetch_vapp_info", "base", "created_vm_moref", "snapshot_moref", "allow_zero_filled_data", "log_apply_info", "include_vapp_config", "fetch_vapp_xml_info")
        class VMDKDynamicDiskVolume(_message.Message):
            __slots__ = ("disk_file_name", "partition_vec")
            class Partition(_message.Message):
                __slots__ = ("partition_type", "volume_start_offset", "volume_size_bytes", "logical_sector_size_bytes")
                PARTITION_TYPE_FIELD_NUMBER: _ClassVar[int]
                VOLUME_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
                VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
                partition_type: _yoda_types_pb2.DiskPartitionType.PartitionType
                volume_start_offset: int
                volume_size_bytes: int
                logical_sector_size_bytes: int
                def __init__(self, partition_type: _Optional[_Union[_yoda_types_pb2.DiskPartitionType.PartitionType, str]] = ..., volume_start_offset: _Optional[int] = ..., volume_size_bytes: _Optional[int] = ..., logical_sector_size_bytes: _Optional[int] = ...) -> None: ...
            DISK_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
            PARTITION_VEC_FIELD_NUMBER: _ClassVar[int]
            disk_file_name: str
            partition_vec: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo.VMDKDynamicDiskVolume.Partition]
            def __init__(self, disk_file_name: _Optional[str] = ..., partition_vec: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo.VMDKDynamicDiskVolume.Partition, _Mapping]]] = ...) -> None: ...
        class LogApplyInfo(_message.Message):
            __slots__ = ("log_file_path", "start_seq_number", "end_seq_number", "end_time_usecs", "is_journal_sharded")
            LOG_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
            START_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
            END_SEQ_NUMBER_FIELD_NUMBER: _ClassVar[int]
            END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            IS_JOURNAL_SHARDED_FIELD_NUMBER: _ClassVar[int]
            log_file_path: str
            start_seq_number: _event_pb2.Sequencer
            end_seq_number: _event_pb2.Sequencer
            end_time_usecs: int
            is_journal_sharded: bool
            def __init__(self, log_file_path: _Optional[str] = ..., start_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_seq_number: _Optional[_Union[_event_pb2.Sequencer, _Mapping]] = ..., end_time_usecs: _Optional[int] = ..., is_journal_sharded: bool = ...) -> None: ...
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_DISK_VOLUMES_TO_CONVERT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_DISK_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
        FETCH_VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
        BASE_FIELD_NUMBER: _ClassVar[int]
        CREATED_VM_MOREF_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ZERO_FILLED_DATA_FIELD_NUMBER: _ClassVar[int]
        LOG_APPLY_INFO_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_VAPP_CONFIG_FIELD_NUMBER: _ClassVar[int]
        FETCH_VAPP_XML_INFO_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        vm_entity: _vmware_pb2.Entity
        root_entity: _vmware_pb2.Entity
        dynamic_disk_volumes_to_convert: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo.VMDKDynamicDiskVolume]
        update_disk_unique_id: bool
        fetch_vapp_info: bool
        base: _magneto_actions_pb2.RestoreBaseArg
        created_vm_moref: _vmware_common_pb2.MORef
        snapshot_moref: _vmware_common_pb2.MORef
        allow_zero_filled_data: bool
        log_apply_info: RestoreVMsArg.VMRestoreInfo.LogApplyInfo
        include_vapp_config: bool
        fetch_vapp_xml_info: bool
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., vm_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., root_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., dynamic_disk_volumes_to_convert: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo.VMDKDynamicDiskVolume, _Mapping]]] = ..., update_disk_unique_id: bool = ..., fetch_vapp_info: bool = ..., base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., created_vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., allow_zero_filled_data: bool = ..., log_apply_info: _Optional[_Union[RestoreVMsArg.VMRestoreInfo.LogApplyInfo, _Mapping]] = ..., include_vapp_config: bool = ..., fetch_vapp_xml_info: bool = ...) -> None: ...
    class GenerateRandomDiskUuidUpdateMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GENERATE_RANDOM_DISK_UUID_FOR_ALL_DISKS_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_RANGES_VEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_INCLUDE_VMDK_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    GENERATE_RANDOM_DISK_UUID_UPDATE_MAP_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_FLAT_VMDK_FILE_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_VIRTUAL_DISK_FILES_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLONE_AND_RENAME_VMDK_FILES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_XML_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NBDSSL_TRANSPORT_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VM_NVRAM_FILE_FIELD_NUMBER: _ClassVar[int]
    PUSH_FILES_TO_DATASTORE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: RestoreVMsArg.Type
    vm_restore_infos: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo]
    view_box_id: int
    view_name: str
    create_view: bool
    is_internal_view: bool
    path_prefix: str
    generate_random_disk_uuid_for_all_disks: bool
    view_whitelist_ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    view_whitelist_ip_ranges_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    force_include_vmdk_suffix: bool
    generate_random_disk_uuid_update_map: _containers.ScalarMap[str, bool]
    include_vm_config: bool
    root_path: str
    skip_clone_flat_vmdk_file: bool
    skip_clone_virtual_disk_files: bool
    skip_clone_and_rename_vmdk_files: bool
    include_xml_config: bool
    use_san_transport: bool
    allow_nbdssl_transport_fallback: bool
    include_vm_nvram_file: bool
    push_files_to_datastore_arg: PushFilesToDatastoreArg
    def __init__(self, type: _Optional[_Union[RestoreVMsArg.Type, str]] = ..., vm_restore_infos: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., create_view: bool = ..., is_internal_view: bool = ..., path_prefix: _Optional[str] = ..., generate_random_disk_uuid_for_all_disks: bool = ..., view_whitelist_ip_addr_str_vec: _Optional[_Iterable[str]] = ..., view_whitelist_ip_ranges_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., force_include_vmdk_suffix: bool = ..., generate_random_disk_uuid_update_map: _Optional[_Mapping[str, bool]] = ..., include_vm_config: bool = ..., root_path: _Optional[str] = ..., skip_clone_flat_vmdk_file: bool = ..., skip_clone_virtual_disk_files: bool = ..., skip_clone_and_rename_vmdk_files: bool = ..., include_xml_config: bool = ..., use_san_transport: bool = ..., allow_nbdssl_transport_fallback: bool = ..., include_vm_nvram_file: bool = ..., push_files_to_datastore_arg: _Optional[_Union[PushFilesToDatastoreArg, _Mapping]] = ...) -> None: ...

class VMwareActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_vm_arg", "restore_vms_arg", "cancel_task_arg", "is_using_bifrost", "nbdssl_compression_scheme")
    VMWARE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    vmware_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMS_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    IS_USING_BIFROST_FIELD_NUMBER: _ClassVar[int]
    NBDSSL_COMPRESSION_SCHEME_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_vm_arg: BackupVMArg
    restore_vms_arg: RestoreVMsArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    is_using_bifrost: bool
    nbdssl_compression_scheme: _vmware_pb2_1.NbdsslCompressionScheme
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_vm_arg: _Optional[_Union[BackupVMArg, _Mapping]] = ..., restore_vms_arg: _Optional[_Union[RestoreVMsArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ..., is_using_bifrost: bool = ..., nbdssl_compression_scheme: _Optional[_Union[_vmware_pb2_1.NbdsslCompressionScheme, str]] = ...) -> None: ...
