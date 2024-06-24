from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.windows.base import file_attrs_pb2 as _file_attrs_pb2
from magneto.agents.windows.base import vss_pb2 as _vss_pb2
from magneto.base.entities import hyperv_pb2 as _hyperv_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from util.disklib.base import enums_pb2 as _enums_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HyperVId(_message.Message):
    __slots__ = ("scvmm_uuid", "hyperv_uuid")
    SCVMM_UUID_FIELD_NUMBER: _ClassVar[int]
    HYPERV_UUID_FIELD_NUMBER: _ClassVar[int]
    scvmm_uuid: bytes
    hyperv_uuid: bytes
    def __init__(self, scvmm_uuid: _Optional[bytes] = ..., hyperv_uuid: _Optional[bytes] = ...) -> None: ...

class HyperVHostInfo(_message.Message):
    __slots__ = ("host_uuid", "host_name", "ip_addr_str_vec", "domain_name")
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    host_uuid: bytes
    host_name: str
    ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name: str
    def __init__(self, host_uuid: _Optional[bytes] = ..., host_name: _Optional[str] = ..., ip_addr_str_vec: _Optional[_Iterable[str]] = ..., domain_name: _Optional[str] = ...) -> None: ...

class HyperVVMInfo(_message.Message):
    __slots__ = ("vm_uuid", "vm_name", "host_info", "hyperv_vm_id", "config_directory_path", "snapshot_directory_path", "highly_available", "state", "internal_viewname_prefix_disk_vec", "vss_generated_vhd_vec", "computer_name", "ip_address_vec", "status", "virtual_disk_path_vec", "virtual_disk_info_vec", "user_excluded_virtual_disk_info_vec", "physical_size_in_bytes")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    HIGHLY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEWNAME_PREFIX_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    VSS_GENERATED_VHD_VEC_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_VIRTUAL_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: bytes
    vm_name: str
    host_info: HyperVHostInfo
    hyperv_vm_id: bytes
    config_directory_path: str
    snapshot_directory_path: str
    highly_available: bool
    state: int
    internal_viewname_prefix_disk_vec: _containers.RepeatedScalarFieldContainer[str]
    vss_generated_vhd_vec: _containers.RepeatedScalarFieldContainer[str]
    computer_name: str
    ip_address_vec: _containers.RepeatedScalarFieldContainer[str]
    status: int
    virtual_disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    virtual_disk_info_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.VirtualDiskBasicInfo]
    user_excluded_virtual_disk_info_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.VirtualDiskBasicInfo]
    physical_size_in_bytes: int
    def __init__(self, vm_uuid: _Optional[bytes] = ..., vm_name: _Optional[str] = ..., host_info: _Optional[_Union[HyperVHostInfo, _Mapping]] = ..., hyperv_vm_id: _Optional[bytes] = ..., config_directory_path: _Optional[str] = ..., snapshot_directory_path: _Optional[str] = ..., highly_available: bool = ..., state: _Optional[int] = ..., internal_viewname_prefix_disk_vec: _Optional[_Iterable[str]] = ..., vss_generated_vhd_vec: _Optional[_Iterable[str]] = ..., computer_name: _Optional[str] = ..., ip_address_vec: _Optional[_Iterable[str]] = ..., status: _Optional[int] = ..., virtual_disk_path_vec: _Optional[_Iterable[str]] = ..., virtual_disk_info_vec: _Optional[_Iterable[_Union[_hyperv_pb2.VirtualDiskBasicInfo, _Mapping]]] = ..., user_excluded_virtual_disk_info_vec: _Optional[_Iterable[_Union[_hyperv_pb2.VirtualDiskBasicInfo, _Mapping]]] = ..., physical_size_in_bytes: _Optional[int] = ...) -> None: ...

class ConsistencyLevel(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAppConsistent: _ClassVar[ConsistencyLevel.Type]
        kCrashConsistent: _ClassVar[ConsistencyLevel.Type]
    kAppConsistent: ConsistencyLevel.Type
    kCrashConsistent: ConsistencyLevel.Type
    def __init__(self) -> None: ...

class ReferencePointType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLogBased: _ClassVar[ReferencePointType.Type]
        kRCTBased: _ClassVar[ReferencePointType.Type]
    kLogBased: ReferencePointType.Type
    kRCTBased: ReferencePointType.Type
    def __init__(self) -> None: ...

class DiskReferencePoint(_message.Message):
    __slots__ = ("disk_id", "checkpoint_disk_id", "rct_id")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    RCT_ID_FIELD_NUMBER: _ClassVar[int]
    disk_id: bytes
    checkpoint_disk_id: bytes
    rct_id: bytes
    def __init__(self, disk_id: _Optional[bytes] = ..., checkpoint_disk_id: _Optional[bytes] = ..., rct_id: _Optional[bytes] = ...) -> None: ...

class VMReferencePoint(_message.Message):
    __slots__ = ("vm_uuid", "checkpoint_name", "instance_id", "reference_point_type", "consistency_level", "disk_reference_point_vec")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_POINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DISK_REFERENCE_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: bytes
    checkpoint_name: str
    instance_id: bytes
    reference_point_type: ReferencePointType.Type
    consistency_level: ConsistencyLevel.Type
    disk_reference_point_vec: _containers.RepeatedCompositeFieldContainer[DiskReferencePoint]
    def __init__(self, vm_uuid: _Optional[bytes] = ..., checkpoint_name: _Optional[str] = ..., instance_id: _Optional[bytes] = ..., reference_point_type: _Optional[_Union[ReferencePointType.Type, str]] = ..., consistency_level: _Optional[_Union[ConsistencyLevel.Type, str]] = ..., disk_reference_point_vec: _Optional[_Iterable[_Union[DiskReferencePoint, _Mapping]]] = ...) -> None: ...

class VirtualDisk(_message.Message):
    __slots__ = ("disk_id", "file_full_path", "snapshot_device_filepath", "total_disk_size_bytes", "checkpoint_disk_id", "disk_format", "disk_type", "logical_sector_size_bytes", "file_attributes", "parent_full_path", "parent_disk_id", "controller_location", "controller_number", "wmi_instance_id", "is_shared", "controller_type")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PARENT_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_DISK_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    WMI_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SHARED_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    disk_id: bytes
    file_full_path: str
    snapshot_device_filepath: str
    total_disk_size_bytes: int
    checkpoint_disk_id: bytes
    disk_format: _enums_pb2_1.DiskFormat.Type
    disk_type: _enums_pb2_1.VirtualHardDiskType.Type
    logical_sector_size_bytes: int
    file_attributes: _file_attrs_pb2.FileAttributes
    parent_full_path: str
    parent_disk_id: str
    controller_location: int
    controller_number: int
    wmi_instance_id: str
    is_shared: bool
    controller_type: str
    def __init__(self, disk_id: _Optional[bytes] = ..., file_full_path: _Optional[str] = ..., snapshot_device_filepath: _Optional[str] = ..., total_disk_size_bytes: _Optional[int] = ..., checkpoint_disk_id: _Optional[bytes] = ..., disk_format: _Optional[_Union[_enums_pb2_1.DiskFormat.Type, str]] = ..., disk_type: _Optional[_Union[_enums_pb2_1.VirtualHardDiskType.Type, str]] = ..., logical_sector_size_bytes: _Optional[int] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ..., parent_full_path: _Optional[str] = ..., parent_disk_id: _Optional[str] = ..., controller_location: _Optional[int] = ..., controller_number: _Optional[int] = ..., wmi_instance_id: _Optional[str] = ..., is_shared: bool = ..., controller_type: _Optional[str] = ...) -> None: ...

class CheckpointInfo(_message.Message):
    __slots__ = ("checkpoint_instance_id", "checkpoint_name", "parent_checkpoint_instance_id", "parent_checkpoint_name", "vm_config_version", "vm_info", "virtual_disk_vec", "vm_config_file_vec", "snapshot_type", "vm_vswitch_info_vec")
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    checkpoint_info: _descriptor.FieldDescriptor
    CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_CHECKPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_VSWITCH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    checkpoint_instance_id: bytes
    checkpoint_name: str
    parent_checkpoint_instance_id: bytes
    parent_checkpoint_name: bytes
    vm_config_version: str
    vm_info: HyperVVMInfo
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    vm_config_file_vec: _containers.RepeatedCompositeFieldContainer[VMConfigFile]
    snapshot_type: _magneto_pb2.ObjectSnapshotType
    vm_vswitch_info_vec: _containers.RepeatedCompositeFieldContainer[VMVirtualSwitchInfo]
    def __init__(self, checkpoint_instance_id: _Optional[bytes] = ..., checkpoint_name: _Optional[str] = ..., parent_checkpoint_instance_id: _Optional[bytes] = ..., parent_checkpoint_name: _Optional[bytes] = ..., vm_config_version: _Optional[str] = ..., vm_info: _Optional[_Union[HyperVVMInfo, _Mapping]] = ..., virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., vm_config_file_vec: _Optional[_Iterable[_Union[VMConfigFile, _Mapping]]] = ..., snapshot_type: _Optional[_Union[_magneto_pb2.ObjectSnapshotType, _Mapping]] = ..., vm_vswitch_info_vec: _Optional[_Iterable[_Union[VMVirtualSwitchInfo, _Mapping]]] = ...) -> None: ...

class VMConfigFile(_message.Message):
    __slots__ = ("file_type", "file_full_path", "snapshot_device_filepath")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVMCX: _ClassVar[VMConfigFile.Type]
        kVMRS: _ClassVar[VMConfigFile.Type]
        kOther: _ClassVar[VMConfigFile.Type]
        kVMCXML: _ClassVar[VMConfigFile.Type]
        kVMGS: _ClassVar[VMConfigFile.Type]
    kVMCX: VMConfigFile.Type
    kVMRS: VMConfigFile.Type
    kOther: VMConfigFile.Type
    kVMCXML: VMConfigFile.Type
    kVMGS: VMConfigFile.Type
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    file_type: VMConfigFile.Type
    file_full_path: str
    snapshot_device_filepath: str
    def __init__(self, file_type: _Optional[_Union[VMConfigFile.Type, str]] = ..., file_full_path: _Optional[str] = ..., snapshot_device_filepath: _Optional[str] = ...) -> None: ...

class VMConfigFileInfo(_message.Message):
    __slots__ = ("vm_config_file", "file_attributes", "data", "length")
    VM_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    vm_config_file: VMConfigFile
    file_attributes: _file_attrs_pb2.FileAttributes
    data: bytes
    length: int
    def __init__(self, vm_config_file: _Optional[_Union[VMConfigFile, _Mapping]] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ..., data: _Optional[bytes] = ..., length: _Optional[int] = ...) -> None: ...

class RestoreVMType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCopy: _ClassVar[RestoreVMType.Type]
        kInstant: _ClassVar[RestoreVMType.Type]
        kClone: _ClassVar[RestoreVMType.Type]
        kGrpcCopy: _ClassVar[RestoreVMType.Type]
    kCopy: RestoreVMType.Type
    kInstant: RestoreVMType.Type
    kClone: RestoreVMType.Type
    kGrpcCopy: RestoreVMType.Type
    def __init__(self) -> None: ...

class RestoreVirtualDiskInfo(_message.Message):
    __slots__ = ("disk_id", "cloned_file_path", "target_file_path", "original_file_path", "original_parent_full_path", "total_disk_size_bytes", "disk_format", "disk_type")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    CLONED_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PARENT_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    disk_id: bytes
    cloned_file_path: str
    target_file_path: str
    original_file_path: str
    original_parent_full_path: str
    total_disk_size_bytes: int
    disk_format: _enums_pb2_1.DiskFormat.Type
    disk_type: _enums_pb2_1.VirtualHardDiskType.Type
    def __init__(self, disk_id: _Optional[bytes] = ..., cloned_file_path: _Optional[str] = ..., target_file_path: _Optional[str] = ..., original_file_path: _Optional[str] = ..., original_parent_full_path: _Optional[str] = ..., total_disk_size_bytes: _Optional[int] = ..., disk_format: _Optional[_Union[_enums_pb2_1.DiskFormat.Type, str]] = ..., disk_type: _Optional[_Union[_enums_pb2_1.VirtualHardDiskType.Type, str]] = ...) -> None: ...

class NetworkConfigInfo(_message.Message):
    __slots__ = ("network_state_change", "virtual_switch_entity")
    class NetworkStateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisable: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kKeepOriginal: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kAttachNewNetwork: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kRemoveNetwork: _ClassVar[NetworkConfigInfo.NetworkStateChange]
    kDisable: NetworkConfigInfo.NetworkStateChange
    kKeepOriginal: NetworkConfigInfo.NetworkStateChange
    kAttachNewNetwork: NetworkConfigInfo.NetworkStateChange
    kRemoveNetwork: NetworkConfigInfo.NetworkStateChange
    NETWORK_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_SWITCH_ENTITY_FIELD_NUMBER: _ClassVar[int]
    network_state_change: NetworkConfigInfo.NetworkStateChange
    virtual_switch_entity: _hyperv_pb2.Entity
    def __init__(self, network_state_change: _Optional[_Union[NetworkConfigInfo.NetworkStateChange, str]] = ..., virtual_switch_entity: _Optional[_Union[_hyperv_pb2.Entity, _Mapping]] = ...) -> None: ...

class VMPathInfo(_message.Message):
    __slots__ = ("config_dir_path", "snapshot_dir_path")
    CONFIG_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    config_dir_path: str
    snapshot_dir_path: str
    def __init__(self, config_dir_path: _Optional[str] = ..., snapshot_dir_path: _Optional[str] = ...) -> None: ...

class RestoreVMParams(_message.Message):
    __slots__ = ("hyperv_vm_id", "restore_type", "backup_type", "restore_to_original_paths", "alternate_restore_base_directory_path", "nas_vm_config_filepath", "original_vm_path_info", "original_disk_filepath_vec", "remove_existing_vm", "preserve_uuid", "vm_name", "power_on_vm", "network_config_info", "make_highly_available", "internal_viewname_prefix_disk_vec", "user_excluded_disk_filepath_vec", "recover_excluded_disks_as_blank_disks", "use_prefix_suffix_for_vm_location")
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TO_ORIGINAL_PATHS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_RESTORE_BASE_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    NAS_VM_CONFIG_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_VM_PATH_INFO_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DISK_FILEPATH_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EXISTING_VM_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_VM_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    MAKE_HIGHLY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VIEWNAME_PREFIX_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_DISK_FILEPATH_VEC_FIELD_NUMBER: _ClassVar[int]
    RECOVER_EXCLUDED_DISKS_AS_BLANK_DISKS_FIELD_NUMBER: _ClassVar[int]
    USE_PREFIX_SUFFIX_FOR_VM_LOCATION_FIELD_NUMBER: _ClassVar[int]
    hyperv_vm_id: str
    restore_type: RestoreVMType.Type
    backup_type: _enums_pb2.Environment.Type
    restore_to_original_paths: bool
    alternate_restore_base_directory_path: str
    nas_vm_config_filepath: str
    original_vm_path_info: VMPathInfo
    original_disk_filepath_vec: _containers.RepeatedCompositeFieldContainer[RestoreVirtualDiskInfo]
    remove_existing_vm: bool
    preserve_uuid: bool
    vm_name: str
    power_on_vm: bool
    network_config_info: NetworkConfigInfo
    make_highly_available: bool
    internal_viewname_prefix_disk_vec: _containers.RepeatedScalarFieldContainer[str]
    user_excluded_disk_filepath_vec: _containers.RepeatedCompositeFieldContainer[RestoreVirtualDiskInfo]
    recover_excluded_disks_as_blank_disks: bool
    use_prefix_suffix_for_vm_location: bool
    def __init__(self, hyperv_vm_id: _Optional[str] = ..., restore_type: _Optional[_Union[RestoreVMType.Type, str]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., restore_to_original_paths: bool = ..., alternate_restore_base_directory_path: _Optional[str] = ..., nas_vm_config_filepath: _Optional[str] = ..., original_vm_path_info: _Optional[_Union[VMPathInfo, _Mapping]] = ..., original_disk_filepath_vec: _Optional[_Iterable[_Union[RestoreVirtualDiskInfo, _Mapping]]] = ..., remove_existing_vm: bool = ..., preserve_uuid: bool = ..., vm_name: _Optional[str] = ..., power_on_vm: bool = ..., network_config_info: _Optional[_Union[NetworkConfigInfo, _Mapping]] = ..., make_highly_available: bool = ..., internal_viewname_prefix_disk_vec: _Optional[_Iterable[str]] = ..., user_excluded_disk_filepath_vec: _Optional[_Iterable[_Union[RestoreVirtualDiskInfo, _Mapping]]] = ..., recover_excluded_disks_as_blank_disks: bool = ..., use_prefix_suffix_for_vm_location: bool = ...) -> None: ...

class RestoreVMState(_message.Message):
    __slots__ = ("status", "infos", "warnings", "errors")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[RestoreVMState.Status]
        kImportVMDone: _ClassVar[RestoreVMState.Status]
        kReconfigureVMDone: _ClassVar[RestoreVMState.Status]
        kRealizeVMDone: _ClassVar[RestoreVMState.Status]
        kStorageMigrationInProgress: _ClassVar[RestoreVMState.Status]
        kStorageMigrationDone: _ClassVar[RestoreVMState.Status]
        kFinished: _ClassVar[RestoreVMState.Status]
    kNotStarted: RestoreVMState.Status
    kImportVMDone: RestoreVMState.Status
    kReconfigureVMDone: RestoreVMState.Status
    kRealizeVMDone: RestoreVMState.Status
    kStorageMigrationInProgress: RestoreVMState.Status
    kStorageMigrationDone: RestoreVMState.Status
    kFinished: RestoreVMState.Status
    class Message(_message.Message):
        __slots__ = ("timestamp_usecs", "detail")
        TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        timestamp_usecs: int
        detail: str
        def __init__(self, timestamp_usecs: _Optional[int] = ..., detail: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    status: RestoreVMState.Status
    infos: _containers.RepeatedCompositeFieldContainer[RestoreVMState.Message]
    warnings: _containers.RepeatedCompositeFieldContainer[RestoreVMState.Message]
    errors: _containers.RepeatedCompositeFieldContainer[RestoreVMState.Message]
    def __init__(self, status: _Optional[_Union[RestoreVMState.Status, str]] = ..., infos: _Optional[_Iterable[_Union[RestoreVMState.Message, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[RestoreVMState.Message, _Mapping]]] = ..., errors: _Optional[_Iterable[_Union[RestoreVMState.Message, _Mapping]]] = ...) -> None: ...

class DiskCopyStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[DiskCopyStatus.Type]
        kCopyInProgress: _ClassVar[DiskCopyStatus.Type]
        kFinished: _ClassVar[DiskCopyStatus.Type]
    kNotStarted: DiskCopyStatus.Type
    kCopyInProgress: DiskCopyStatus.Type
    kFinished: DiskCopyStatus.Type
    def __init__(self) -> None: ...

class DiskCopyInfo(_message.Message):
    __slots__ = ("disk_id", "status", "copy_error", "next_offset_to_copy", "file_size_bytes", "async_copier_id")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COPY_ERROR_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ASYNC_COPIER_ID_FIELD_NUMBER: _ClassVar[int]
    disk_id: bytes
    status: DiskCopyStatus.Type
    copy_error: _error_pb2.ErrorProto
    next_offset_to_copy: int
    file_size_bytes: int
    async_copier_id: int
    def __init__(self, disk_id: _Optional[bytes] = ..., status: _Optional[_Union[DiskCopyStatus.Type, str]] = ..., copy_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., next_offset_to_copy: _Optional[int] = ..., file_size_bytes: _Optional[int] = ..., async_copier_id: _Optional[int] = ...) -> None: ...

class CopyVMDisksProgress(_message.Message):
    __slots__ = ("finished", "copy_error", "status", "disk_copy_info_vec")
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    COPY_ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DISK_COPY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    finished: bool
    copy_error: _error_pb2.ErrorProto
    status: DiskCopyStatus.Type
    disk_copy_info_vec: _containers.RepeatedCompositeFieldContainer[DiskCopyInfo]
    def __init__(self, finished: bool = ..., copy_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[DiskCopyStatus.Type, str]] = ..., disk_copy_info_vec: _Optional[_Iterable[_Union[DiskCopyInfo, _Mapping]]] = ...) -> None: ...

class StorageMigrationProgress(_message.Message):
    __slots__ = ("storage_migration_job_id", "finished", "migration_error", "progress_pct")
    STORAGE_MIGRATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PCT_FIELD_NUMBER: _ClassVar[int]
    storage_migration_job_id: str
    finished: bool
    migration_error: _error_pb2.ErrorProto
    progress_pct: int
    def __init__(self, storage_migration_job_id: _Optional[str] = ..., finished: bool = ..., migration_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., progress_pct: _Optional[int] = ...) -> None: ...

class RestoreVMHandle(_message.Message):
    __slots__ = ("restore_vm_params", "restore_vm_state", "planned_vm_id", "target_vm_path_info", "realized_vm_id", "copy_vm_disks_progress", "target_disk_filepath_vec", "storage_migration_progress", "target_excluded_disk_filepath_vec")
    RESTORE_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_STATE_FIELD_NUMBER: _ClassVar[int]
    PLANNED_VM_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VM_PATH_INFO_FIELD_NUMBER: _ClassVar[int]
    REALIZED_VM_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_VM_DISKS_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DISK_FILEPATH_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_MIGRATION_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TARGET_EXCLUDED_DISK_FILEPATH_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_vm_params: RestoreVMParams
    restore_vm_state: RestoreVMState
    planned_vm_id: str
    target_vm_path_info: VMPathInfo
    realized_vm_id: str
    copy_vm_disks_progress: CopyVMDisksProgress
    target_disk_filepath_vec: _containers.RepeatedCompositeFieldContainer[RestoreVirtualDiskInfo]
    storage_migration_progress: StorageMigrationProgress
    target_excluded_disk_filepath_vec: _containers.RepeatedCompositeFieldContainer[RestoreVirtualDiskInfo]
    def __init__(self, restore_vm_params: _Optional[_Union[RestoreVMParams, _Mapping]] = ..., restore_vm_state: _Optional[_Union[RestoreVMState, _Mapping]] = ..., planned_vm_id: _Optional[str] = ..., target_vm_path_info: _Optional[_Union[VMPathInfo, _Mapping]] = ..., realized_vm_id: _Optional[str] = ..., copy_vm_disks_progress: _Optional[_Union[CopyVMDisksProgress, _Mapping]] = ..., target_disk_filepath_vec: _Optional[_Iterable[_Union[RestoreVirtualDiskInfo, _Mapping]]] = ..., storage_migration_progress: _Optional[_Union[StorageMigrationProgress, _Mapping]] = ..., target_excluded_disk_filepath_vec: _Optional[_Iterable[_Union[RestoreVirtualDiskInfo, _Mapping]]] = ...) -> None: ...

class HyperVVSSBackupInfo(_message.Message):
    __slots__ = ("vm_config_file_vec", "virtual_disk_vec", "vm_info", "crash_consistent_downgrade_warning")
    HYPERV_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_backup_info: _descriptor.FieldDescriptor
    VM_CONFIG_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    CRASH_CONSISTENT_DOWNGRADE_WARNING_FIELD_NUMBER: _ClassVar[int]
    vm_config_file_vec: _containers.RepeatedCompositeFieldContainer[VMConfigFile]
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    vm_info: HyperVVMInfo
    crash_consistent_downgrade_warning: _error_pb2.ErrorProto
    def __init__(self, vm_config_file_vec: _Optional[_Iterable[_Union[VMConfigFile, _Mapping]]] = ..., virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., vm_info: _Optional[_Union[HyperVVMInfo, _Mapping]] = ..., crash_consistent_downgrade_warning: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VMVirtualSwitchInfo(_message.Message):
    __slots__ = ("ID", "Name", "VMHostID", "VMHost")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VMHOSTID_FIELD_NUMBER: _ClassVar[int]
    VMHOST_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    VMHostID: str
    VMHost: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., VMHostID: _Optional[str] = ..., VMHost: _Optional[str] = ...) -> None: ...
