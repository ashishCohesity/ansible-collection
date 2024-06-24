from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import cdp_pb2 as _cdp_pb2
from magneto.base import cloud_pb2 as _cloud_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import nas_pb2 as _nas_pb2
from magneto.base import standby_pb2 as _standby_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from magneto.connectors.vmware import vmware_base_pb2 as _vmware_base_pb2
from magneto.connectors.vmware import vmware_setup_restore_disks_pb2 as _vmware_setup_restore_disks_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskRestoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCompleteRestore: _ClassVar[DiskRestoreType]
    kDifferentialRestore: _ClassVar[DiskRestoreType]

class FileTransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kIncomplete: _ClassVar[FileTransferStatus]
    kComplete: _ClassVar[FileTransferStatus]

class VirtualMachinePowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[VirtualMachinePowerState]
    kPoweredOff: _ClassVar[VirtualMachinePowerState]
    kPoweredOn: _ClassVar[VirtualMachinePowerState]
    kSuspended: _ClassVar[VirtualMachinePowerState]

class NbdsslCompressionScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNone: _ClassVar[NbdsslCompressionScheme]
    kZlib: _ClassVar[NbdsslCompressionScheme]
    kFastlz: _ClassVar[NbdsslCompressionScheme]
    kSkipz: _ClassVar[NbdsslCompressionScheme]
kCompleteRestore: DiskRestoreType
kDifferentialRestore: DiskRestoreType
kIncomplete: FileTransferStatus
kComplete: FileTransferStatus
kUnknown: VirtualMachinePowerState
kPoweredOff: VirtualMachinePowerState
kPoweredOn: VirtualMachinePowerState
kSuspended: VirtualMachinePowerState
kNone: NbdsslCompressionScheme
kZlib: NbdsslCompressionScheme
kFastlz: NbdsslCompressionScheme
kSkipz: NbdsslCompressionScheme

class VirtualDeviceInfo(_message.Message):
    __slots__ = ("key", "controller_key", "unit_number", "device_type")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    key: int
    controller_key: int
    unit_number: int
    device_type: int
    def __init__(self, key: _Optional[int] = ..., controller_key: _Optional[int] = ..., unit_number: _Optional[int] = ..., device_type: _Optional[int] = ...) -> None: ...

class VirtualDisk(_message.Message):
    __slots__ = ("key", "unit_number", "uuid", "disk_unique_id", "type", "filepath", "filepath_in_tmp_vm", "datastore_moref", "capacity", "change_id", "thin_provisioned", "thick_eager_scrub_provision", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "use_uuid_for_encoded_filename", "query_disk_error", "controller_bus_number", "controller_type", "disk_queried_with_previous_snapshot", "controller_key", "additional_disk_info")
    VMWARE_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    vmware_virtual_disk: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DISK_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_IN_TMP_VM_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    THIN_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
    THICK_EAGER_SCRUB_PROVISION_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    USE_UUID_FOR_ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_QUERIED_WITH_PREVIOUS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    key: int
    unit_number: int
    uuid: str
    disk_unique_id: str
    type: int
    filepath: str
    filepath_in_tmp_vm: str
    datastore_moref: _vmware_common_pb2.MORef
    capacity: int
    change_id: str
    thin_provisioned: bool
    thick_eager_scrub_provision: bool
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    use_uuid_for_encoded_filename: bool
    query_disk_error: _error_pb2.ErrorProto
    controller_bus_number: int
    controller_type: str
    disk_queried_with_previous_snapshot: bool
    controller_key: int
    additional_disk_info: AdditionalVMDKInformation
    def __init__(self, key: _Optional[int] = ..., unit_number: _Optional[int] = ..., uuid: _Optional[str] = ..., disk_unique_id: _Optional[str] = ..., type: _Optional[int] = ..., filepath: _Optional[str] = ..., filepath_in_tmp_vm: _Optional[str] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., capacity: _Optional[int] = ..., change_id: _Optional[str] = ..., thin_provisioned: bool = ..., thick_eager_scrub_provision: bool = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., use_uuid_for_encoded_filename: bool = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., controller_bus_number: _Optional[int] = ..., controller_type: _Optional[str] = ..., disk_queried_with_previous_snapshot: bool = ..., controller_key: _Optional[int] = ..., additional_disk_info: _Optional[_Union[AdditionalVMDKInformation, _Mapping]] = ...) -> None: ...

class AdditionalVMDKInformation(_message.Message):
    __slots__ = ("shares_info", "storage_io_allocation")
    class SharesInfo(_message.Message):
        __slots__ = ("shares", "level")
        class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kLow: _ClassVar[AdditionalVMDKInformation.SharesInfo.Level]
            kNormal: _ClassVar[AdditionalVMDKInformation.SharesInfo.Level]
            kHigh: _ClassVar[AdditionalVMDKInformation.SharesInfo.Level]
            kCustom: _ClassVar[AdditionalVMDKInformation.SharesInfo.Level]
        kLow: AdditionalVMDKInformation.SharesInfo.Level
        kNormal: AdditionalVMDKInformation.SharesInfo.Level
        kHigh: AdditionalVMDKInformation.SharesInfo.Level
        kCustom: AdditionalVMDKInformation.SharesInfo.Level
        SHARES_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        shares: int
        level: AdditionalVMDKInformation.SharesInfo.Level
        def __init__(self, shares: _Optional[int] = ..., level: _Optional[_Union[AdditionalVMDKInformation.SharesInfo.Level, str]] = ...) -> None: ...
    class StorageIOAllocationInfo(_message.Message):
        __slots__ = ("limit", "reservation", "shares")
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_FIELD_NUMBER: _ClassVar[int]
        SHARES_FIELD_NUMBER: _ClassVar[int]
        limit: int
        reservation: int
        shares: AdditionalVMDKInformation.SharesInfo
        def __init__(self, limit: _Optional[int] = ..., reservation: _Optional[int] = ..., shares: _Optional[_Union[AdditionalVMDKInformation.SharesInfo, _Mapping]] = ...) -> None: ...
    SHARES_INFO_FIELD_NUMBER: _ClassVar[int]
    STORAGE_IO_ALLOCATION_FIELD_NUMBER: _ClassVar[int]
    shares_info: AdditionalVMDKInformation.SharesInfo
    storage_io_allocation: AdditionalVMDKInformation.StorageIOAllocationInfo
    def __init__(self, shares_info: _Optional[_Union[AdditionalVMDKInformation.SharesInfo, _Mapping]] = ..., storage_io_allocation: _Optional[_Union[AdditionalVMDKInformation.StorageIOAllocationInfo, _Mapping]] = ...) -> None: ...

class SparseVMConfig(_message.Message):
    __slots__ = ("vm_name", "vm_folder_moref", "vm_vapp_moref", "resource_pool_moref", "datastore_moref", "virtual_disks", "independent_virtual_disks", "physical_rdm_disks", "user_excluded_virtual_disks", "vm_encrypted", "has_virtual_rdm_disks", "virtual_rdm_disks", "tag_attributes_vec", "custom_attributes_vec", "datastore_name", "nvram_filepath", "nvram_file_download_status")
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_VAPP_MOREF_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    INDEPENDENT_VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    VM_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    HAS_VIRTUAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    NVRAM_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    NVRAM_FILE_DOWNLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    vm_folder_moref: _vmware_common_pb2.MORef
    vm_vapp_moref: _vmware_common_pb2.MORef
    resource_pool_moref: _vmware_common_pb2.MORef
    datastore_moref: _vmware_common_pb2.MORef
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    independent_virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    physical_rdm_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    user_excluded_virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    vm_encrypted: bool
    has_virtual_rdm_disks: bool
    virtual_rdm_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.TagAttributes]
    custom_attributes_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.CustomAttribute]
    datastore_name: str
    nvram_filepath: str
    nvram_file_download_status: FileTransferStatus
    def __init__(self, vm_name: _Optional[str] = ..., vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_vapp_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., independent_virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., physical_rdm_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., user_excluded_virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., vm_encrypted: bool = ..., has_virtual_rdm_disks: bool = ..., virtual_rdm_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[_vmware_pb2.TagAttributes, _Mapping]]] = ..., custom_attributes_vec: _Optional[_Iterable[_Union[_vmware_pb2.CustomAttribute, _Mapping]]] = ..., datastore_name: _Optional[str] = ..., nvram_filepath: _Optional[str] = ..., nvram_file_download_status: _Optional[_Union[FileTransferStatus, str]] = ...) -> None: ...

class VSSSnapshotInfoProto(_message.Message):
    __slots__ = ("state", "snapshot_set_id", "server_snapshot_info", "server_snapshot_info_file_name", "server_snapshot_serialized_fetch_info", "error", "snapshot_needs_deletion", "delete_snapshot_error", "host_summary")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[VSSSnapshotInfoProto.State]
        kPrepareDone: _ClassVar[VSSSnapshotInfoProto.State]
        kSnapshotTaken: _ClassVar[VSSSnapshotInfoProto.State]
        kMetadataFetchDone: _ClassVar[VSSSnapshotInfoProto.State]
        kSnapshotDeleted: _ClassVar[VSSSnapshotInfoProto.State]
    kNone: VSSSnapshotInfoProto.State
    kPrepareDone: VSSSnapshotInfoProto.State
    kSnapshotTaken: VSSSnapshotInfoProto.State
    kMetadataFetchDone: VSSSnapshotInfoProto.State
    kSnapshotDeleted: VSSSnapshotInfoProto.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_SERIALIZED_FETCH_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NEEDS_DELETION_FIELD_NUMBER: _ClassVar[int]
    DELETE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    state: VSSSnapshotInfoProto.State
    snapshot_set_id: bytes
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    server_snapshot_info_file_name: str
    server_snapshot_serialized_fetch_info: _agent_pb2.ServerSnapshotSerializedFetchInfo
    error: _error_pb2.ErrorProto
    snapshot_needs_deletion: bool
    delete_snapshot_error: _error_pb2.ErrorProto
    host_summary: _agent_pb2.SnapshotHostInfoSummary
    def __init__(self, state: _Optional[_Union[VSSSnapshotInfoProto.State, str]] = ..., snapshot_set_id: _Optional[bytes] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., server_snapshot_info_file_name: _Optional[str] = ..., server_snapshot_serialized_fetch_info: _Optional[_Union[_agent_pb2.ServerSnapshotSerializedFetchInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_needs_deletion: bool = ..., delete_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., host_summary: _Optional[_Union[_agent_pb2.SnapshotHostInfoSummary, _Mapping]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("vm_name", "snapshot_id", "snapshot_moref", "job_instance_id", "attempt_num", "host_moref", "nic_ip_addr_vec", "networks", "status", "virtual_disks", "independent_virtual_disks", "physical_rdm_disks", "has_virtual_rdm_disks", "xml_vm_config", "vm_config_filepath", "fetched_file_info_vec", "sub_tasks_vec", "error", "app_user_messages", "vm_power_state", "skip_end_backup", "snapshot_deletion_error", "backup_done", "change_tracking_disabled_DEPRECATED", "vss_snapshot_info", "app_warnings_DEPRECATED", "quiesced", "sub_file_size_mb", "user_excluded_virtual_disks", "dr_to_cloud_vm_info", "datastore_space_check", "datastore_morefs", "datastore_throttling_feature_enabled", "vapp_entity", "vcd_attributes", "vm_encrypted", "tag_attributes_vec", "is_template", "registered_source_throttling_feature_enabled", "custom_attributes_vec", "guest_id", "host_name", "vm_nic_vec", "search_domain_vec", "dns_server_vec", "domain_name", "ipv4_gateway", "vmware_version_tools_status", "vmware_tools_running_status", "guest_host_name", "ds_url_pairs", "snapshot_create_time_secs", "org_vdc_network_vec", "primary_network_connection_index", "aggregate_guest_disk_space_used", "storage_array_snapshot", "storage_device_snapshot_info_set", "datastore_to_storage_device_snapshot_info_idx_map", "primary_storage_source_id", "sparse_vm_config", "is_backup_block_intersection_enabled", "is_save_allocated_blocks_info_enabled", "disks_with_allocated_blocks_info_vec", "allocated_block_info_file_suffix", "cbt_delta_info_persisted", "disks_with_unmap_disk_areas_key_vec", "should_zero_fill_unmapped_disk_areas")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kTasksCreated: _ClassVar[SnapshotInfo.Status]
        kTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
        kVMLocated: _ClassVar[SnapshotInfo.Status]
        kPrepareVMBackupDone: _ClassVar[SnapshotInfo.Status]
        kSetupVMFilesDone: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kTasksCreated: SnapshotInfo.Status
    kTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    kVMLocated: SnapshotInfo.Status
    kPrepareVMBackupDone: SnapshotInfo.Status
    kSetupVMFilesDone: SnapshotInfo.Status
    class FileInfo(_message.Message):
        __slots__ = ("file_type", "file_name", "error")
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        file_type: _vmware_base_pb2.FileType
        file_name: str
        error: _error_pb2.ErrorProto
        def __init__(self, file_type: _Optional[_Union[_vmware_base_pb2.FileType, str]] = ..., file_name: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class DsUrlPairsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DatastoreToStorageDeviceSnapshotInfoIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VMWARE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_snapshot_info: _descriptor.FieldDescriptor
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    NIC_IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    INDEPENDENT_VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    HAS_VIRTUAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    FETCHED_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    VM_POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    SKIP_END_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DONE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TRACKING_DISABLED_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VSS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    APP_WARNINGS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    DR_TO_CLOUD_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_SPACE_CHECK_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREFS_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VAPP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VCD_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VM_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    GUEST_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_NIC_VEC_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DOMAIN_VEC_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    IPV4_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    VMWARE_VERSION_TOOLS_STATUS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_TOOLS_RUNNING_STATUS_FIELD_NUMBER: _ClassVar[int]
    GUEST_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    DS_URL_PAIRS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATE_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    ORG_VDC_NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_NETWORK_CONNECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_GUEST_DISK_SPACE_USED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_SNAPSHOT_INFO_SET_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_TO_STORAGE_DEVICE_SNAPSHOT_INFO_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_BACKUP_BLOCK_INTERSECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SAVE_ALLOCATED_BLOCKS_INFO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISKS_WITH_ALLOCATED_BLOCKS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_BLOCK_INFO_FILE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    CBT_DELTA_INFO_PERSISTED_FIELD_NUMBER: _ClassVar[int]
    DISKS_WITH_UNMAP_DISK_AREAS_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    SHOULD_ZERO_FILL_UNMAPPED_DISK_AREAS_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    snapshot_id: int
    snapshot_moref: _vmware_common_pb2.MORef
    job_instance_id: int
    attempt_num: int
    host_moref: _vmware_common_pb2.MORef
    nic_ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
    networks: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    status: SnapshotInfo.Status
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    independent_virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    physical_rdm_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    has_virtual_rdm_disks: bool
    xml_vm_config: bytes
    vm_config_filepath: str
    fetched_file_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.FileInfo]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    app_user_messages: _magneto_pb2.UserMessageProto
    vm_power_state: VirtualMachinePowerState
    skip_end_backup: bool
    snapshot_deletion_error: _error_pb2.ErrorProto
    backup_done: bool
    change_tracking_disabled_DEPRECATED: bool
    vss_snapshot_info: VSSSnapshotInfoProto
    app_warnings_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    quiesced: bool
    sub_file_size_mb: int
    user_excluded_virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    dr_to_cloud_vm_info: _cloud_pb2.DRToCloudVMInfo
    datastore_space_check: _magneto_pb2.DatastoreSpaceCheckProto
    datastore_morefs: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    datastore_throttling_feature_enabled: bool
    vapp_entity: _entity_pb2.EntityProto
    vcd_attributes: _vmware_pb2.VCDAttributes
    vm_encrypted: bool
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.TagAttributes]
    is_template: bool
    registered_source_throttling_feature_enabled: bool
    custom_attributes_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.CustomAttribute]
    guest_id: str
    host_name: str
    vm_nic_vec: _containers.RepeatedCompositeFieldContainer[NICSetting]
    search_domain_vec: _containers.RepeatedScalarFieldContainer[str]
    dns_server_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name: str
    ipv4_gateway: _containers.RepeatedCompositeFieldContainer[DeviceGatewayMap]
    vmware_version_tools_status: _vmware_pb2.VMwareToolsVersionStatus.Type
    vmware_tools_running_status: _vmware_pb2.VMwareToolsRunningStatus.Type
    guest_host_name: str
    ds_url_pairs: _containers.ScalarMap[str, str]
    snapshot_create_time_secs: int
    org_vdc_network_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VMOrgVDCNetwork]
    primary_network_connection_index: int
    aggregate_guest_disk_space_used: int
    storage_array_snapshot: bool
    storage_device_snapshot_info_set: _containers.RepeatedCompositeFieldContainer[_storage_pb2.StorageDeviceSnapshotInfoProto]
    datastore_to_storage_device_snapshot_info_idx_map: _containers.ScalarMap[str, int]
    primary_storage_source_id: int
    sparse_vm_config: SparseVMConfig
    is_backup_block_intersection_enabled: bool
    is_save_allocated_blocks_info_enabled: bool
    disks_with_allocated_blocks_info_vec: _containers.RepeatedScalarFieldContainer[str]
    allocated_block_info_file_suffix: str
    cbt_delta_info_persisted: bool
    disks_with_unmap_disk_areas_key_vec: _containers.RepeatedScalarFieldContainer[int]
    should_zero_fill_unmapped_disk_areas: bool
    def __init__(self, vm_name: _Optional[str] = ..., snapshot_id: _Optional[int] = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., nic_ip_addr_vec: _Optional[_Iterable[str]] = ..., networks: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., independent_virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., physical_rdm_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., has_virtual_rdm_disks: bool = ..., xml_vm_config: _Optional[bytes] = ..., vm_config_filepath: _Optional[str] = ..., fetched_file_info_vec: _Optional[_Iterable[_Union[SnapshotInfo.FileInfo, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ..., vm_power_state: _Optional[_Union[VirtualMachinePowerState, str]] = ..., skip_end_backup: bool = ..., snapshot_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., backup_done: bool = ..., change_tracking_disabled_DEPRECATED: bool = ..., vss_snapshot_info: _Optional[_Union[VSSSnapshotInfoProto, _Mapping]] = ..., app_warnings_DEPRECATED: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., quiesced: bool = ..., sub_file_size_mb: _Optional[int] = ..., user_excluded_virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., dr_to_cloud_vm_info: _Optional[_Union[_cloud_pb2.DRToCloudVMInfo, _Mapping]] = ..., datastore_space_check: _Optional[_Union[_magneto_pb2.DatastoreSpaceCheckProto, _Mapping]] = ..., datastore_morefs: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., datastore_throttling_feature_enabled: bool = ..., vapp_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., vcd_attributes: _Optional[_Union[_vmware_pb2.VCDAttributes, _Mapping]] = ..., vm_encrypted: bool = ..., tag_attributes_vec: _Optional[_Iterable[_Union[_vmware_pb2.TagAttributes, _Mapping]]] = ..., is_template: bool = ..., registered_source_throttling_feature_enabled: bool = ..., custom_attributes_vec: _Optional[_Iterable[_Union[_vmware_pb2.CustomAttribute, _Mapping]]] = ..., guest_id: _Optional[str] = ..., host_name: _Optional[str] = ..., vm_nic_vec: _Optional[_Iterable[_Union[NICSetting, _Mapping]]] = ..., search_domain_vec: _Optional[_Iterable[str]] = ..., dns_server_vec: _Optional[_Iterable[str]] = ..., domain_name: _Optional[str] = ..., ipv4_gateway: _Optional[_Iterable[_Union[DeviceGatewayMap, _Mapping]]] = ..., vmware_version_tools_status: _Optional[_Union[_vmware_pb2.VMwareToolsVersionStatus.Type, str]] = ..., vmware_tools_running_status: _Optional[_Union[_vmware_pb2.VMwareToolsRunningStatus.Type, str]] = ..., guest_host_name: _Optional[str] = ..., ds_url_pairs: _Optional[_Mapping[str, str]] = ..., snapshot_create_time_secs: _Optional[int] = ..., org_vdc_network_vec: _Optional[_Iterable[_Union[_magneto_pb2.VMOrgVDCNetwork, _Mapping]]] = ..., primary_network_connection_index: _Optional[int] = ..., aggregate_guest_disk_space_used: _Optional[int] = ..., storage_array_snapshot: bool = ..., storage_device_snapshot_info_set: _Optional[_Iterable[_Union[_storage_pb2.StorageDeviceSnapshotInfoProto, _Mapping]]] = ..., datastore_to_storage_device_snapshot_info_idx_map: _Optional[_Mapping[str, int]] = ..., primary_storage_source_id: _Optional[int] = ..., sparse_vm_config: _Optional[_Union[SparseVMConfig, _Mapping]] = ..., is_backup_block_intersection_enabled: bool = ..., is_save_allocated_blocks_info_enabled: bool = ..., disks_with_allocated_blocks_info_vec: _Optional[_Iterable[str]] = ..., allocated_block_info_file_suffix: _Optional[str] = ..., cbt_delta_info_persisted: bool = ..., disks_with_unmap_disk_areas_key_vec: _Optional[_Iterable[int]] = ..., should_zero_fill_unmapped_disk_areas: bool = ...) -> None: ...

class StorageDevice(_message.Message):
    __slots__ = ("datastore_moref", "datastore_name", "vmfs_datastore_uuid")
    VMWARE_STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    vmware_storage_device: _descriptor.FieldDescriptor
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    VMFS_DATASTORE_UUID_FIELD_NUMBER: _ClassVar[int]
    datastore_moref: _vmware_common_pb2.MORef
    datastore_name: str
    vmfs_datastore_uuid: str
    def __init__(self, datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_name: _Optional[str] = ..., vmfs_datastore_uuid: _Optional[str] = ...) -> None: ...

class EntityStorageMetadata(_message.Message):
    __slots__ = ("resource_pool_moref",)
    VMWARE_ENTITY_STORAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    vmware_entity_storage_metadata: _descriptor.FieldDescriptor
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    resource_pool_moref: _vmware_common_pb2.MORef
    def __init__(self, resource_pool_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...

class EntitySnapshotInfo(_message.Message):
    __slots__ = ("vm_name", "snapshot_id", "snapshot_moref", "snapshot_name", "vm_moref", "virtual_disks", "independent_virtual_disks", "physical_rdm_disks", "has_virtual_rdm_disks", "xml_vm_config", "fetched_file_info_vec", "sparse_vm_config", "vm_config_filepath", "quiesced", "vm_power_state", "tmp_vm", "snapshot_deletion_error", "tag_attributes_vec", "update_tmp_vm_config", "storage_device_snapshot_info_set", "datastore_to_storage_device_snapshot_info_idx_map", "primary_storage_source_id", "leverage_san_storage_snapshot_v2", "snapshot_info_proto", "san_protocol")
    class FileInfo(_message.Message):
        __slots__ = ("file_type", "file_name", "error", "file_data")
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        FILE_DATA_FIELD_NUMBER: _ClassVar[int]
        file_type: _vmware_base_pb2.FileType
        file_name: str
        error: _error_pb2.ErrorProto
        file_data: bytes
        def __init__(self, file_type: _Optional[_Union[_vmware_base_pb2.FileType, str]] = ..., file_name: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_data: _Optional[bytes] = ...) -> None: ...
    class DatastoreToStorageDeviceSnapshotInfoIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VMWARE_ENTITY_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_entity_snapshot_info: _descriptor.FieldDescriptor
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    INDEPENDENT_VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    HAS_VIRTUAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FETCHED_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    VM_POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    TMP_VM_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TMP_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_SNAPSHOT_INFO_SET_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_TO_STORAGE_DEVICE_SNAPSHOT_INFO_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STORAGE_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_STORAGE_SNAPSHOT_V2_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_PROTO_FIELD_NUMBER: _ClassVar[int]
    SAN_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    snapshot_id: int
    snapshot_moref: _vmware_common_pb2.MORef
    snapshot_name: str
    vm_moref: _vmware_common_pb2.MORef
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    independent_virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    physical_rdm_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    has_virtual_rdm_disks: bool
    xml_vm_config: bytes
    fetched_file_info_vec: _containers.RepeatedCompositeFieldContainer[EntitySnapshotInfo.FileInfo]
    sparse_vm_config: SparseVMConfig
    vm_config_filepath: str
    quiesced: bool
    vm_power_state: VirtualMachinePowerState
    tmp_vm: _vmware_pb2.Entity
    snapshot_deletion_error: _error_pb2.ErrorProto
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    update_tmp_vm_config: bool
    storage_device_snapshot_info_set: _containers.RepeatedCompositeFieldContainer[_storage_pb2.StorageDeviceSnapshotInfoProto]
    datastore_to_storage_device_snapshot_info_idx_map: _containers.ScalarMap[str, int]
    primary_storage_source_id: int
    leverage_san_storage_snapshot_v2: bool
    snapshot_info_proto: _magneto_pb2.SnapshotInfoProto
    san_protocol: _storage_pb2.SanProtocol
    def __init__(self, vm_name: _Optional[str] = ..., snapshot_id: _Optional[int] = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_name: _Optional[str] = ..., vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., independent_virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., physical_rdm_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., has_virtual_rdm_disks: bool = ..., xml_vm_config: _Optional[bytes] = ..., fetched_file_info_vec: _Optional[_Iterable[_Union[EntitySnapshotInfo.FileInfo, _Mapping]]] = ..., sparse_vm_config: _Optional[_Union[SparseVMConfig, _Mapping]] = ..., vm_config_filepath: _Optional[str] = ..., quiesced: bool = ..., vm_power_state: _Optional[_Union[VirtualMachinePowerState, str]] = ..., tmp_vm: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., update_tmp_vm_config: bool = ..., storage_device_snapshot_info_set: _Optional[_Iterable[_Union[_storage_pb2.StorageDeviceSnapshotInfoProto, _Mapping]]] = ..., datastore_to_storage_device_snapshot_info_idx_map: _Optional[_Mapping[str, int]] = ..., primary_storage_source_id: _Optional[int] = ..., leverage_san_storage_snapshot_v2: bool = ..., snapshot_info_proto: _Optional[_Union[_magneto_pb2.SnapshotInfoProto, _Mapping]] = ..., san_protocol: _Optional[_Union[_storage_pb2.SanProtocol, str]] = ...) -> None: ...

class EntitiesGroupSnapshotInfo(_message.Message):
    __slots__ = ("status", "vm_folder_name", "vm_folder_moref", "datastore_name", "datastore_moref", "snapshot_datastore_info_set", "datacenter_entity", "cancellation_in_progress", "last_error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kVMwareSnapshotsTaken: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kStorageSnapshotsTaken: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kVMwareSnapshotsDeleted: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kTmpVMsCreated: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kFinished: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kCancelled: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kTmpVMsConfigUpdated: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kStorageSnapshotsMounted: _ClassVar[EntitiesGroupSnapshotInfo.Status]
    kStarted: EntitiesGroupSnapshotInfo.Status
    kVMwareSnapshotsTaken: EntitiesGroupSnapshotInfo.Status
    kStorageSnapshotsTaken: EntitiesGroupSnapshotInfo.Status
    kVMwareSnapshotsDeleted: EntitiesGroupSnapshotInfo.Status
    kTmpVMsCreated: EntitiesGroupSnapshotInfo.Status
    kFinished: EntitiesGroupSnapshotInfo.Status
    kCancelled: EntitiesGroupSnapshotInfo.Status
    kTmpVMsConfigUpdated: EntitiesGroupSnapshotInfo.Status
    kStorageSnapshotsMounted: EntitiesGroupSnapshotInfo.Status
    class SnapshotDatastoreInfo(_message.Message):
        __slots__ = ("datastore_name", "datastore_moref")
        DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
        datastore_name: str
        datastore_moref: _vmware_common_pb2.MORef
        def __init__(self, datastore_name: _Optional[str] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    VMWARE_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_group_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DATASTORE_INFO_SET_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    status: EntitiesGroupSnapshotInfo.Status
    vm_folder_name: str
    vm_folder_moref: _vmware_common_pb2.MORef
    datastore_name: str
    datastore_moref: _vmware_common_pb2.MORef
    snapshot_datastore_info_set: _containers.RepeatedCompositeFieldContainer[EntitiesGroupSnapshotInfo.SnapshotDatastoreInfo]
    datacenter_entity: _vmware_pb2.Entity
    cancellation_in_progress: bool
    last_error: _error_pb2.ErrorProto
    def __init__(self, status: _Optional[_Union[EntitiesGroupSnapshotInfo.Status, str]] = ..., vm_folder_name: _Optional[str] = ..., vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_name: _Optional[str] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., snapshot_datastore_info_set: _Optional[_Iterable[_Union[EntitiesGroupSnapshotInfo.SnapshotDatastoreInfo, _Mapping]]] = ..., datacenter_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., cancellation_in_progress: bool = ..., last_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class NetworkConfigInfo(_message.Message):
    __slots__ = ("network_state_change", "network_moref", "preserve_mac_address_on_new_network", "mappings", "org_vdc_network_vec")
    class NetworkStateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisable: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kKeepOriginal: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kAttachNewNetwork: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kRemoveNetwork: _ClassVar[NetworkConfigInfo.NetworkStateChange]
        kApplyNetworkMapping: _ClassVar[NetworkConfigInfo.NetworkStateChange]
    kDisable: NetworkConfigInfo.NetworkStateChange
    kKeepOriginal: NetworkConfigInfo.NetworkStateChange
    kAttachNewNetwork: NetworkConfigInfo.NetworkStateChange
    kRemoveNetwork: NetworkConfigInfo.NetworkStateChange
    kApplyNetworkMapping: NetworkConfigInfo.NetworkStateChange
    NETWORK_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_MOREF_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_MAC_ADDRESS_ON_NEW_NETWORK_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    ORG_VDC_NETWORK_VEC_FIELD_NUMBER: _ClassVar[int]
    network_state_change: NetworkConfigInfo.NetworkStateChange
    network_moref: _vmware_common_pb2.MORef
    preserve_mac_address_on_new_network: bool
    mappings: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.NetworkMappingProto]
    org_vdc_network_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.VMOrgVDCNetwork]
    def __init__(self, network_state_change: _Optional[_Union[NetworkConfigInfo.NetworkStateChange, str]] = ..., network_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., preserve_mac_address_on_new_network: bool = ..., mappings: _Optional[_Iterable[_Union[_magneto_pb2.NetworkMappingProto, _Mapping]]] = ..., org_vdc_network_vec: _Optional[_Iterable[_Union[_magneto_pb2.VMOrgVDCNetwork, _Mapping]]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("restore_task_state", "vm_folder_name", "vm_folder_moref", "vm_folder_created", "clone_files_path_prefix", "datastore_info_vec", "num_additional_view_clones_needed", "additional_views_vec", "cloned_storage_snapshot_info_vec", "storage_vmotion_skipped", "sub_tasks_vec", "total_bytes_to_write_to_target", "error", "virtual_disks", "resource_pool_host_info_map", "composed_vapp_uuid_vec", "composed_vapp_name_vec", "disk_restore_type_map", "changed_disk_area_list_proto_map", "bytes_saved_by_differential_restore", "log_apply_restore_info", "existing_vm_info", "existing_vm_devices_info", "enabled_features", "differential_restore_in_progress", "rehydrate_vm_restore_info", "xml_vm_reconfig_spec", "old_to_new_disk_uuid_map", "storage_array_snapshot", "vm_info_DEPRECATED", "resource_pool_moref_DEPRECATED", "datastore_system_morefs_DEPRECATED", "datacenter_moref_DEPRECATED", "restore_disks_task_info_DEPRECATED", "renamed_vm_name", "is_copy_recovery_used_blocks_optimization_enabled", "is_full_restore_used_blocks_optimization_enabled", "is_persist_disk_areas_in_record_io_enabled", "disk_areas_persisted_in_record_io_uuid_vec", "sub_task_version", "differential_restore_fallback_in_progress", "disk_uuid_to_optimization_method_map", "vm_folder_path")
    class RestoreTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.RestoreTaskState]
        kReadyToFetchVMsInfo: _ClassVar[RestoreInfo.RestoreTaskState]
        kFetchedVMsInfo: _ClassVar[RestoreInfo.RestoreTaskState]
        kAdditionalViewsCloned: _ClassVar[RestoreInfo.RestoreTaskState]
        kCreatedVM: _ClassVar[RestoreInfo.RestoreTaskState]
        kFinished: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMsFilesCloned: _ClassVar[RestoreInfo.RestoreTaskState]
        kPermitGranted: _ClassVar[RestoreInfo.RestoreTaskState]
        kSubTasksCreated: _ClassVar[RestoreInfo.RestoreTaskState]
        kSubTasksFinished: _ClassVar[RestoreInfo.RestoreTaskState]
        kDataCenterInfoFetched: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMRenamedToTempName: _ClassVar[RestoreInfo.RestoreTaskState]
        kPushedFilesToDatastore: _ClassVar[RestoreInfo.RestoreTaskState]
        kExistingVMPoweredOff: _ClassVar[RestoreInfo.RestoreTaskState]
        kFetchedVMDiskInfo: _ClassVar[RestoreInfo.RestoreTaskState]
        kPopulatedDiskRestoreTypeMap: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMDisksReconfigured: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMsClonedToView: _ClassVar[RestoreInfo.RestoreTaskState]
        kBackupVMFilesConverted: _ClassVar[RestoreInfo.RestoreTaskState]
        kStorageSnapshotsCloned: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMImported: _ClassVar[RestoreInfo.RestoreTaskState]
        kPermitReleasedForHost: _ClassVar[RestoreInfo.RestoreTaskState]
        kPermitGrantedForVapp: _ClassVar[RestoreInfo.RestoreTaskState]
    kStarted: RestoreInfo.RestoreTaskState
    kReadyToFetchVMsInfo: RestoreInfo.RestoreTaskState
    kFetchedVMsInfo: RestoreInfo.RestoreTaskState
    kAdditionalViewsCloned: RestoreInfo.RestoreTaskState
    kCreatedVM: RestoreInfo.RestoreTaskState
    kFinished: RestoreInfo.RestoreTaskState
    kVMsFilesCloned: RestoreInfo.RestoreTaskState
    kPermitGranted: RestoreInfo.RestoreTaskState
    kSubTasksCreated: RestoreInfo.RestoreTaskState
    kSubTasksFinished: RestoreInfo.RestoreTaskState
    kDataCenterInfoFetched: RestoreInfo.RestoreTaskState
    kVMRenamedToTempName: RestoreInfo.RestoreTaskState
    kPushedFilesToDatastore: RestoreInfo.RestoreTaskState
    kExistingVMPoweredOff: RestoreInfo.RestoreTaskState
    kFetchedVMDiskInfo: RestoreInfo.RestoreTaskState
    kPopulatedDiskRestoreTypeMap: RestoreInfo.RestoreTaskState
    kVMDisksReconfigured: RestoreInfo.RestoreTaskState
    kVMsClonedToView: RestoreInfo.RestoreTaskState
    kBackupVMFilesConverted: RestoreInfo.RestoreTaskState
    kStorageSnapshotsCloned: RestoreInfo.RestoreTaskState
    kVMImported: RestoreInfo.RestoreTaskState
    kPermitReleasedForHost: RestoreInfo.RestoreTaskState
    kPermitGrantedForVapp: RestoreInfo.RestoreTaskState
    class OptimizationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoOptimization: _ClassVar[RestoreInfo.OptimizationMethod]
        kAllocatedBlocks: _ClassVar[RestoreInfo.OptimizationMethod]
        kChangedBlocks: _ClassVar[RestoreInfo.OptimizationMethod]
        kIntersectedBlocks: _ClassVar[RestoreInfo.OptimizationMethod]
    kNoOptimization: RestoreInfo.OptimizationMethod
    kAllocatedBlocks: RestoreInfo.OptimizationMethod
    kChangedBlocks: RestoreInfo.OptimizationMethod
    kIntersectedBlocks: RestoreInfo.OptimizationMethod
    class DatastoreInfo(_message.Message):
        __slots__ = ("moref", "name", "remote_host", "remote_path", "datacenter_moref", "datastore_system_moref_vec", "resource_pool_moref_vec", "datacenter_name", "datacenter_inventory_path", "datastore_type", "url", "is_top_level_directory_create_supported")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
        REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
        DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_POOL_MOREF_VEC_FIELD_NUMBER: _ClassVar[int]
        DATACENTER_NAME_FIELD_NUMBER: _ClassVar[int]
        DATACENTER_INVENTORY_PATH_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        IS_TOP_LEVEL_DIRECTORY_CREATE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        name: str
        remote_host: str
        remote_path: str
        datacenter_moref: _vmware_common_pb2.MORef
        datastore_system_moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
        resource_pool_moref_vec: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
        datacenter_name: str
        datacenter_inventory_path: str
        datastore_type: DatastoreType.Type
        url: str
        is_top_level_directory_create_supported: bool
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., name: _Optional[str] = ..., remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., resource_pool_moref_vec: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., datacenter_name: _Optional[str] = ..., datacenter_inventory_path: _Optional[str] = ..., datastore_type: _Optional[_Union[DatastoreType.Type, str]] = ..., url: _Optional[str] = ..., is_top_level_directory_create_supported: bool = ...) -> None: ...
    class AdditionalViewInfo(_message.Message):
        __slots__ = ("view_name", "datastore_info_vec", "mounted_on_all_resources")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        MOUNTED_ON_ALL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        datastore_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.DatastoreInfo]
        mounted_on_all_resources: bool
        def __init__(self, view_name: _Optional[str] = ..., datastore_info_vec: _Optional[_Iterable[_Union[RestoreInfo.DatastoreInfo, _Mapping]]] = ..., mounted_on_all_resources: bool = ...) -> None: ...
    class ClonedStorageSnapshotInfo(_message.Message):
        __slots__ = ("storage_device_snapshot_info", "dependent_entity_idx_vec", "datastore_info_vec", "mounted_on_all_resources", "connector_params_id", "record_volume_for_gc", "primary_storage_source_id", "snapshot_time_usecs")
        STORAGE_DEVICE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
        DEPENDENT_ENTITY_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        MOUNTED_ON_ALL_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        CONNECTOR_PARAMS_ID_FIELD_NUMBER: _ClassVar[int]
        RECORD_VOLUME_FOR_GC_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_STORAGE_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        storage_device_snapshot_info: _storage_pb2.StorageDeviceSnapshotInfoProto
        dependent_entity_idx_vec: _containers.RepeatedScalarFieldContainer[int]
        datastore_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.DatastoreInfo]
        mounted_on_all_resources: bool
        connector_params_id: int
        record_volume_for_gc: bool
        primary_storage_source_id: int
        snapshot_time_usecs: int
        def __init__(self, storage_device_snapshot_info: _Optional[_Union[_storage_pb2.StorageDeviceSnapshotInfoProto, _Mapping]] = ..., dependent_entity_idx_vec: _Optional[_Iterable[int]] = ..., datastore_info_vec: _Optional[_Iterable[_Union[RestoreInfo.DatastoreInfo, _Mapping]]] = ..., mounted_on_all_resources: bool = ..., connector_params_id: _Optional[int] = ..., record_volume_for_gc: bool = ..., primary_storage_source_id: _Optional[int] = ..., snapshot_time_usecs: _Optional[int] = ...) -> None: ...
    class HostInfoList(_message.Message):
        __slots__ = ("hosts",)
        class HostInfo(_message.Message):
            __slots__ = ("moref", "datastores")
            MOREF_FIELD_NUMBER: _ClassVar[int]
            DATASTORES_FIELD_NUMBER: _ClassVar[int]
            moref: _vmware_common_pb2.MORef
            datastores: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
            def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastores: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ...) -> None: ...
        HOSTS_FIELD_NUMBER: _ClassVar[int]
        hosts: _containers.RepeatedCompositeFieldContainer[RestoreInfo.HostInfoList.HostInfo]
        def __init__(self, hosts: _Optional[_Iterable[_Union[RestoreInfo.HostInfoList.HostInfo, _Mapping]]] = ...) -> None: ...
    class ResourcePoolHostInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RestoreInfo.HostInfoList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RestoreInfo.HostInfoList, _Mapping]] = ...) -> None: ...
    class DiskRestoreTypeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DiskRestoreType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DiskRestoreType, str]] = ...) -> None: ...
    class ChangedDiskAreaListProtoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _disk_pb2.DiskAreaListProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ...) -> None: ...
    class LogApplyRestoreInfo(_message.Message):
        __slots__ = ("task_status", "log_apply_restore_params", "updated_cdp_virtual_disk_vec", "updated_backup_to_standby_disk_uuid_map")
        class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kLogFilesCloned: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kVMLocated: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kPermitGranted: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kSnapshotCreated: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kDisksDeleted: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kSubTasksCreated: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kSubTasksFinished: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kSnapshotDeleted: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kFinished: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kDisksResized: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
            kStandbyReady: _ClassVar[RestoreInfo.LogApplyRestoreInfo.TaskStatus]
        kStarted: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kLogFilesCloned: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kVMLocated: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kPermitGranted: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kSnapshotCreated: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kDisksDeleted: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kSubTasksCreated: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kSubTasksFinished: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kSnapshotDeleted: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kFinished: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kDisksResized: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        kStandbyReady: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        class UpdatedBackupToStandbyDiskUuidMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
        LOG_APPLY_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        UPDATED_CDP_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        UPDATED_BACKUP_TO_STANDBY_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
        task_status: RestoreInfo.LogApplyRestoreInfo.TaskStatus
        log_apply_restore_params: _standby_pb2.LogApplyRestoreParams
        updated_cdp_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_cdp_pb2.VirtualDiskInfo]
        updated_backup_to_standby_disk_uuid_map: _containers.ScalarMap[str, str]
        def __init__(self, task_status: _Optional[_Union[RestoreInfo.LogApplyRestoreInfo.TaskStatus, str]] = ..., log_apply_restore_params: _Optional[_Union[_standby_pb2.LogApplyRestoreParams, _Mapping]] = ..., updated_cdp_virtual_disk_vec: _Optional[_Iterable[_Union[_cdp_pb2.VirtualDiskInfo, _Mapping]]] = ..., updated_backup_to_standby_disk_uuid_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class ExistingVMInfo(_message.Message):
        __slots__ = ("hardware_version", "tags_vec", "moref")
        HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        TAGS_VEC_FIELD_NUMBER: _ClassVar[int]
        MOREF_FIELD_NUMBER: _ClassVar[int]
        hardware_version: str
        tags_vec: _containers.RepeatedScalarFieldContainer[str]
        moref: _vmware_common_pb2.MORef
        def __init__(self, hardware_version: _Optional[str] = ..., tags_vec: _Optional[_Iterable[str]] = ..., moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    class ExistingVMDevicesInfo(_message.Message):
        __slots__ = ("virtual_disk_vec", "virtual_disk_controller_vec", "non_disk_virtual_device_vec")
        VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_DISK_CONTROLLER_VEC_FIELD_NUMBER: _ClassVar[int]
        NON_DISK_VIRTUAL_DEVICE_VEC_FIELD_NUMBER: _ClassVar[int]
        virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskDeviceInfo]
        virtual_disk_controller_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskControllerInfo]
        non_disk_virtual_device_vec: _containers.RepeatedCompositeFieldContainer[VirtualDeviceInfo]
        def __init__(self, virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDiskDeviceInfo, _Mapping]]] = ..., virtual_disk_controller_vec: _Optional[_Iterable[_Union[VirtualDiskControllerInfo, _Mapping]]] = ..., non_disk_virtual_device_vec: _Optional[_Iterable[_Union[VirtualDeviceInfo, _Mapping]]] = ...) -> None: ...
    class EnabledFeatures(_message.Message):
        __slots__ = ("datastore_throttling_feature_enabled", "registered_source_throttling_feature_enabled")
        DATASTORE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        REGISTERED_SOURCE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        datastore_throttling_feature_enabled: bool
        registered_source_throttling_feature_enabled: bool
        def __init__(self, datastore_throttling_feature_enabled: bool = ..., registered_source_throttling_feature_enabled: bool = ...) -> None: ...
    class ReHydrateVMRestoreInfo(_message.Message):
        __slots__ = ("status", "rehydrate_vm_restore_params", "updated_cdp_virtual_disk_vec", "pre_rehydration_standby_virtual_disk_vec", "updated_backup_to_standby_disk_uuid_map", "standby_hydration_info", "backup_hydration_info")
        class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kStarted: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kVMFilesCloned: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kStandbyReady: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kDisksResized: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kSnapshotCreated: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kDisksDeleted: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kDisksAdded: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kVMLocated: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kVMReconfigured: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kPermitGranted: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kSubTasksCreated: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kSubTasksFinished: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kSnapshotDeleted: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kFinished: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kVMHostLocated_DEPRECATED: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            KHydrationPermitGranted_DEPRECATED: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            kRestoreViewCreated_DEPRECATED: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
            KHydrationPermitReleased_DEPRECATED: _ClassVar[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus]
        kStarted: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kVMFilesCloned: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kStandbyReady: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kDisksResized: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kSnapshotCreated: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kDisksDeleted: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kDisksAdded: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kVMLocated: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kVMReconfigured: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kPermitGranted: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kSubTasksCreated: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kSubTasksFinished: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kSnapshotDeleted: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kFinished: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kVMHostLocated_DEPRECATED: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        KHydrationPermitGranted_DEPRECATED: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        kRestoreViewCreated_DEPRECATED: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        KHydrationPermitReleased_DEPRECATED: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        class UpdatedBackupToStandbyDiskUuidMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        STATUS_FIELD_NUMBER: _ClassVar[int]
        REHYDRATE_VM_RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
        UPDATED_CDP_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        PRE_REHYDRATION_STANDBY_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
        UPDATED_BACKUP_TO_STANDBY_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
        STANDBY_HYDRATION_INFO_FIELD_NUMBER: _ClassVar[int]
        BACKUP_HYDRATION_INFO_FIELD_NUMBER: _ClassVar[int]
        status: RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus
        rehydrate_vm_restore_params: _standby_pb2.ReHydrateVMRestoreParams
        updated_cdp_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_cdp_pb2.VirtualDiskInfo]
        pre_rehydration_standby_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
        updated_backup_to_standby_disk_uuid_map: _containers.ScalarMap[str, str]
        standby_hydration_info: _cdp_pb2.HydrationInfo
        backup_hydration_info: _cdp_pb2.HydrationInfo
        def __init__(self, status: _Optional[_Union[RestoreInfo.ReHydrateVMRestoreInfo.TaskStatus, str]] = ..., rehydrate_vm_restore_params: _Optional[_Union[_standby_pb2.ReHydrateVMRestoreParams, _Mapping]] = ..., updated_cdp_virtual_disk_vec: _Optional[_Iterable[_Union[_cdp_pb2.VirtualDiskInfo, _Mapping]]] = ..., pre_rehydration_standby_virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., updated_backup_to_standby_disk_uuid_map: _Optional[_Mapping[str, str]] = ..., standby_hydration_info: _Optional[_Union[_cdp_pb2.HydrationInfo, _Mapping]] = ..., backup_hydration_info: _Optional[_Union[_cdp_pb2.HydrationInfo, _Mapping]] = ...) -> None: ...
    class OldToNewDiskUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VMInfo(_message.Message):
        __slots__ = ("moref", "name", "xml_vm_config", "sparse_vm_config")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        name: str
        xml_vm_config: bytes
        sparse_vm_config: SparseVMConfig
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., name: _Optional[str] = ..., xml_vm_config: _Optional[bytes] = ..., sparse_vm_config: _Optional[_Union[SparseVMConfig, _Mapping]] = ...) -> None: ...
    class DiskUuidToOptimizationMethodMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RestoreInfo.OptimizationMethod
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RestoreInfo.OptimizationMethod, str]] = ...) -> None: ...
    VMWARE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_restore_info: _descriptor.FieldDescriptor
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_CREATED_FIELD_NUMBER: _ClassVar[int]
    CLONE_FILES_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_ADDITIONAL_VIEW_CLONES_NEEDED_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_VIEWS_VEC_FIELD_NUMBER: _ClassVar[int]
    CLONED_STORAGE_SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    STORAGE_VMOTION_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_TARGET_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_HOST_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    COMPOSED_VAPP_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    COMPOSED_VAPP_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_RESTORE_TYPE_MAP_FIELD_NUMBER: _ClassVar[int]
    CHANGED_DISK_AREA_LIST_PROTO_MAP_FIELD_NUMBER: _ClassVar[int]
    BYTES_SAVED_BY_DIFFERENTIAL_RESTORE_FIELD_NUMBER: _ClassVar[int]
    LOG_APPLY_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    EXISTING_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    EXISTING_VM_DEVICES_INFO_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    DIFFERENTIAL_RESTORE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REHYDRATE_VM_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    XML_VM_RECONFIG_SPEC_FIELD_NUMBER: _ClassVar[int]
    OLD_TO_NEW_DISK_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_MOREF_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_SYSTEM_MOREFS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    RENAMED_VM_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_RECOVERY_USED_BLOCKS_OPTIMIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_RESTORE_USED_BLOCKS_OPTIMIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_PERSIST_DISK_AREAS_IN_RECORD_IO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISK_AREAS_PERSISTED_IN_RECORD_IO_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VERSION_FIELD_NUMBER: _ClassVar[int]
    DIFFERENTIAL_RESTORE_FALLBACK_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    DISK_UUID_TO_OPTIMIZATION_METHOD_MAP_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: RestoreInfo.RestoreTaskState
    vm_folder_name: str
    vm_folder_moref: _vmware_common_pb2.MORef
    vm_folder_created: bool
    clone_files_path_prefix: str
    datastore_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.DatastoreInfo]
    num_additional_view_clones_needed: int
    additional_views_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.AdditionalViewInfo]
    cloned_storage_snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.ClonedStorageSnapshotInfo]
    storage_vmotion_skipped: bool
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    total_bytes_to_write_to_target: int
    error: _error_pb2.ErrorProto
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    resource_pool_host_info_map: _containers.MessageMap[str, RestoreInfo.HostInfoList]
    composed_vapp_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    composed_vapp_name_vec: _containers.RepeatedScalarFieldContainer[str]
    disk_restore_type_map: _containers.ScalarMap[str, DiskRestoreType]
    changed_disk_area_list_proto_map: _containers.MessageMap[str, _disk_pb2.DiskAreaListProto]
    bytes_saved_by_differential_restore: int
    log_apply_restore_info: RestoreInfo.LogApplyRestoreInfo
    existing_vm_info: RestoreInfo.ExistingVMInfo
    existing_vm_devices_info: RestoreInfo.ExistingVMDevicesInfo
    enabled_features: RestoreInfo.EnabledFeatures
    differential_restore_in_progress: bool
    rehydrate_vm_restore_info: RestoreInfo.ReHydrateVMRestoreInfo
    xml_vm_reconfig_spec: str
    old_to_new_disk_uuid_map: _containers.ScalarMap[str, str]
    storage_array_snapshot: bool
    vm_info_DEPRECATED: RestoreInfo.VMInfo
    resource_pool_moref_DEPRECATED: _vmware_common_pb2.MORef
    datastore_system_morefs_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_vmware_common_pb2.MORef]
    datacenter_moref_DEPRECATED: _vmware_common_pb2.MORef
    restore_disks_task_info_DEPRECATED: _vmware_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo
    renamed_vm_name: str
    is_copy_recovery_used_blocks_optimization_enabled: bool
    is_full_restore_used_blocks_optimization_enabled: bool
    is_persist_disk_areas_in_record_io_enabled: bool
    disk_areas_persisted_in_record_io_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_task_version: int
    differential_restore_fallback_in_progress: bool
    disk_uuid_to_optimization_method_map: _containers.ScalarMap[str, RestoreInfo.OptimizationMethod]
    vm_folder_path: str
    def __init__(self, restore_task_state: _Optional[_Union[RestoreInfo.RestoreTaskState, str]] = ..., vm_folder_name: _Optional[str] = ..., vm_folder_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_folder_created: bool = ..., clone_files_path_prefix: _Optional[str] = ..., datastore_info_vec: _Optional[_Iterable[_Union[RestoreInfo.DatastoreInfo, _Mapping]]] = ..., num_additional_view_clones_needed: _Optional[int] = ..., additional_views_vec: _Optional[_Iterable[_Union[RestoreInfo.AdditionalViewInfo, _Mapping]]] = ..., cloned_storage_snapshot_info_vec: _Optional[_Iterable[_Union[RestoreInfo.ClonedStorageSnapshotInfo, _Mapping]]] = ..., storage_vmotion_skipped: bool = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., total_bytes_to_write_to_target: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., resource_pool_host_info_map: _Optional[_Mapping[str, RestoreInfo.HostInfoList]] = ..., composed_vapp_uuid_vec: _Optional[_Iterable[str]] = ..., composed_vapp_name_vec: _Optional[_Iterable[str]] = ..., disk_restore_type_map: _Optional[_Mapping[str, DiskRestoreType]] = ..., changed_disk_area_list_proto_map: _Optional[_Mapping[str, _disk_pb2.DiskAreaListProto]] = ..., bytes_saved_by_differential_restore: _Optional[int] = ..., log_apply_restore_info: _Optional[_Union[RestoreInfo.LogApplyRestoreInfo, _Mapping]] = ..., existing_vm_info: _Optional[_Union[RestoreInfo.ExistingVMInfo, _Mapping]] = ..., existing_vm_devices_info: _Optional[_Union[RestoreInfo.ExistingVMDevicesInfo, _Mapping]] = ..., enabled_features: _Optional[_Union[RestoreInfo.EnabledFeatures, _Mapping]] = ..., differential_restore_in_progress: bool = ..., rehydrate_vm_restore_info: _Optional[_Union[RestoreInfo.ReHydrateVMRestoreInfo, _Mapping]] = ..., xml_vm_reconfig_spec: _Optional[str] = ..., old_to_new_disk_uuid_map: _Optional[_Mapping[str, str]] = ..., storage_array_snapshot: bool = ..., vm_info_DEPRECATED: _Optional[_Union[RestoreInfo.VMInfo, _Mapping]] = ..., resource_pool_moref_DEPRECATED: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_morefs_DEPRECATED: _Optional[_Iterable[_Union[_vmware_common_pb2.MORef, _Mapping]]] = ..., datacenter_moref_DEPRECATED: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., restore_disks_task_info_DEPRECATED: _Optional[_Union[_vmware_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo, _Mapping]] = ..., renamed_vm_name: _Optional[str] = ..., is_copy_recovery_used_blocks_optimization_enabled: bool = ..., is_full_restore_used_blocks_optimization_enabled: bool = ..., is_persist_disk_areas_in_record_io_enabled: bool = ..., disk_areas_persisted_in_record_io_uuid_vec: _Optional[_Iterable[str]] = ..., sub_task_version: _Optional[int] = ..., differential_restore_fallback_in_progress: bool = ..., disk_uuid_to_optimization_method_map: _Optional[_Mapping[str, RestoreInfo.OptimizationMethod]] = ..., vm_folder_path: _Optional[str] = ...) -> None: ...

class RestoreScribeInfo(_message.Message):
    __slots__ = ("changed_disk_area_list_proto_map",)
    class ChangedDiskAreaListProtoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _disk_pb2.DiskAreaListProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ...) -> None: ...
    VMWARE_RESTORE_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_restore_scribe_info: _descriptor.FieldDescriptor
    CHANGED_DISK_AREA_LIST_PROTO_MAP_FIELD_NUMBER: _ClassVar[int]
    changed_disk_area_list_proto_map: _containers.MessageMap[str, _disk_pb2.DiskAreaListProto]
    def __init__(self, changed_disk_area_list_proto_map: _Optional[_Mapping[str, _disk_pb2.DiskAreaListProto]] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("vm_info", "previous_vm_info", "datacenter_moref", "storage_vmotion_task_moref", "host_entity", "entity_continue_on_error", "snapshot_moref", "attempted_target_ds_idx_vec", "num_svmotions_retried", "snapshot_deleted", "datastore_to_storage_device_snapshot_info_idx_map", "nvram_file_clone_status")
    class VMInfo(_message.Message):
        __slots__ = ("moref", "name", "xml_vm_config", "sparse_vm_config", "vapp_info", "vm_nic_vec")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        XML_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VAPP_INFO_FIELD_NUMBER: _ClassVar[int]
        VM_NIC_VEC_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        name: str
        xml_vm_config: bytes
        sparse_vm_config: SparseVMConfig
        vapp_info: _magneto_pb2.BackupTaskStateVappInfoProto
        vm_nic_vec: _containers.RepeatedCompositeFieldContainer[NICSetting]
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., name: _Optional[str] = ..., xml_vm_config: _Optional[bytes] = ..., sparse_vm_config: _Optional[_Union[SparseVMConfig, _Mapping]] = ..., vapp_info: _Optional[_Union[_magneto_pb2.BackupTaskStateVappInfoProto, _Mapping]] = ..., vm_nic_vec: _Optional[_Iterable[_Union[NICSetting, _Mapping]]] = ...) -> None: ...
    class DatastoreToStorageDeviceSnapshotInfoIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VMWARE_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_restore_entity_info: _descriptor.FieldDescriptor
    VMWARE_CLOUD_DEPLOY_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_cloud_deploy_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_MOREF_FIELD_NUMBER: _ClassVar[int]
    STORAGE_VMOTION_TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ENTITY_CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MOREF_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTED_TARGET_DS_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_SVMOTIONS_RETRIED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_TO_STORAGE_DEVICE_SNAPSHOT_INFO_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    NVRAM_FILE_CLONE_STATUS_FIELD_NUMBER: _ClassVar[int]
    vm_info: RestoreEntityInfo.VMInfo
    previous_vm_info: RestoreEntityInfo.VMInfo
    datacenter_moref: _vmware_common_pb2.MORef
    storage_vmotion_task_moref: _vmware_common_pb2.MORef
    host_entity: _entity_pb2.EntityProto
    entity_continue_on_error: bool
    snapshot_moref: _vmware_common_pb2.MORef
    attempted_target_ds_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    num_svmotions_retried: int
    snapshot_deleted: bool
    datastore_to_storage_device_snapshot_info_idx_map: _containers.ScalarMap[str, int]
    nvram_file_clone_status: FileTransferStatus
    def __init__(self, vm_info: _Optional[_Union[RestoreEntityInfo.VMInfo, _Mapping]] = ..., previous_vm_info: _Optional[_Union[RestoreEntityInfo.VMInfo, _Mapping]] = ..., datacenter_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., storage_vmotion_task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., entity_continue_on_error: bool = ..., snapshot_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., attempted_target_ds_idx_vec: _Optional[_Iterable[int]] = ..., num_svmotions_retried: _Optional[int] = ..., snapshot_deleted: bool = ..., datastore_to_storage_device_snapshot_info_idx_map: _Optional[_Mapping[str, int]] = ..., nvram_file_clone_status: _Optional[_Union[FileTransferStatus, str]] = ...) -> None: ...

class DestroyClonedTaskInfo(_message.Message):
    __slots__ = ()
    VMWARE_DESTROY_CLONED_VM_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_destroy_cloned_vm_task_info: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class RestoreFilesInfo(_message.Message):
    __slots__ = ("vm_moref", "task_state", "target_vm_util_dir", "cloned_vmdk_path_map", "cloned_vmdk_source_virtual_disk_map", "datastore_info", "on_start_info_expected", "pse_fallback_enabled", "current_process_launch_api", "vm_ip_addr_vec", "target_agent_ip_addr", "vmware_api_on_start_state", "pse_api_on_start_state", "restore_disks_task_info")
    class RestoreFilesTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kCloneFilesComplete: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kMountedDatastore: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kAttachedVMDKs: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kCopyFilesComplete: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kFinished: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kSetupCompleted: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kCopyFilesInitiated: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
    kStarted: RestoreFilesInfo.RestoreFilesTaskState
    kCloneFilesComplete: RestoreFilesInfo.RestoreFilesTaskState
    kMountedDatastore: RestoreFilesInfo.RestoreFilesTaskState
    kAttachedVMDKs: RestoreFilesInfo.RestoreFilesTaskState
    kCopyFilesComplete: RestoreFilesInfo.RestoreFilesTaskState
    kFinished: RestoreFilesInfo.RestoreFilesTaskState
    kSetupCompleted: RestoreFilesInfo.RestoreFilesTaskState
    kCopyFilesInitiated: RestoreFilesInfo.RestoreFilesTaskState
    class ProcessLaunchAPI(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVSphere: _ClassVar[RestoreFilesInfo.ProcessLaunchAPI]
        kPSE: _ClassVar[RestoreFilesInfo.ProcessLaunchAPI]
    kVSphere: RestoreFilesInfo.ProcessLaunchAPI
    kPSE: RestoreFilesInfo.ProcessLaunchAPI
    class ClonedVmdkPathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ClonedVmdkSourceVirtualDiskMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: VirtualDisk
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[VirtualDisk, _Mapping]] = ...) -> None: ...
    class DatastoreInfo(_message.Message):
        __slots__ = ("moref", "host_moref", "datastore_system_moref", "name", "remote_host", "remote_path")
        MOREF_FIELD_NUMBER: _ClassVar[int]
        HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_SYSTEM_MOREF_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
        REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
        moref: _vmware_common_pb2.MORef
        host_moref: _vmware_common_pb2.MORef
        datastore_system_moref: _vmware_common_pb2.MORef
        name: str
        remote_host: str
        remote_path: str
        def __init__(self, moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_system_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., name: _Optional[str] = ..., remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ...) -> None: ...
    class GuestProcessStartState(_message.Message):
        __slots__ = ("pid", "admin_privileges_verified")
        PID_FIELD_NUMBER: _ClassVar[int]
        ADMIN_PRIVILEGES_VERIFIED_FIELD_NUMBER: _ClassVar[int]
        pid: int
        admin_privileges_verified: bool
        def __init__(self, pid: _Optional[int] = ..., admin_privileges_verified: bool = ...) -> None: ...
    VMWARE_RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_restore_files_info: _descriptor.FieldDescriptor
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    TARGET_VM_UTIL_DIR_FIELD_NUMBER: _ClassVar[int]
    CLONED_VMDK_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    CLONED_VMDK_SOURCE_VIRTUAL_DISK_MAP_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    ON_START_INFO_EXPECTED_FIELD_NUMBER: _ClassVar[int]
    PSE_FALLBACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROCESS_LAUNCH_API_FIELD_NUMBER: _ClassVar[int]
    VM_IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    VMWARE_API_ON_START_STATE_FIELD_NUMBER: _ClassVar[int]
    PSE_API_ON_START_STATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    task_state: RestoreFilesInfo.RestoreFilesTaskState
    target_vm_util_dir: str
    cloned_vmdk_path_map: _containers.ScalarMap[str, str]
    cloned_vmdk_source_virtual_disk_map: _containers.MessageMap[str, VirtualDisk]
    datastore_info: RestoreFilesInfo.DatastoreInfo
    on_start_info_expected: bool
    pse_fallback_enabled: bool
    current_process_launch_api: RestoreFilesInfo.ProcessLaunchAPI
    vm_ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
    target_agent_ip_addr: str
    vmware_api_on_start_state: RestoreFilesInfo.GuestProcessStartState
    pse_api_on_start_state: RestoreFilesInfo.GuestProcessStartState
    restore_disks_task_info: _vmware_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., task_state: _Optional[_Union[RestoreFilesInfo.RestoreFilesTaskState, str]] = ..., target_vm_util_dir: _Optional[str] = ..., cloned_vmdk_path_map: _Optional[_Mapping[str, str]] = ..., cloned_vmdk_source_virtual_disk_map: _Optional[_Mapping[str, VirtualDisk]] = ..., datastore_info: _Optional[_Union[RestoreFilesInfo.DatastoreInfo, _Mapping]] = ..., on_start_info_expected: bool = ..., pse_fallback_enabled: bool = ..., current_process_launch_api: _Optional[_Union[RestoreFilesInfo.ProcessLaunchAPI, str]] = ..., vm_ip_addr_vec: _Optional[_Iterable[str]] = ..., target_agent_ip_addr: _Optional[str] = ..., vmware_api_on_start_state: _Optional[_Union[RestoreFilesInfo.GuestProcessStartState, _Mapping]] = ..., pse_api_on_start_state: _Optional[_Union[RestoreFilesInfo.GuestProcessStartState, _Mapping]] = ..., restore_disks_task_info: _Optional[_Union[_vmware_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo, _Mapping]] = ...) -> None: ...

class MountVolumesInfo(_message.Message):
    __slots__ = ("vm_nic_ip_addr_vec", "target_agent_ip_addr")
    VMWARE_MOUNT_VOLUMES_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_mount_volumes_info: _descriptor.FieldDescriptor
    VM_NIC_IP_ADDR_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    vm_nic_ip_addr_vec: _containers.RepeatedScalarFieldContainer[str]
    target_agent_ip_addr: str
    def __init__(self, vm_nic_ip_addr_vec: _Optional[_Iterable[str]] = ..., target_agent_ip_addr: _Optional[str] = ...) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("encoded_flat_file_map",)
    class EncodedFlatFileMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    ENCODED_FLAT_FILE_MAP_FIELD_NUMBER: _ClassVar[int]
    encoded_flat_file_map: _containers.ScalarMap[str, str]
    def __init__(self, encoded_flat_file_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DatastoreType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLocal: _ClassVar[DatastoreType.Type]
        kNFS: _ClassVar[DatastoreType.Type]
        kVMFS: _ClassVar[DatastoreType.Type]
        kVvol: _ClassVar[DatastoreType.Type]
        kUnknown: _ClassVar[DatastoreType.Type]
        kvSAN: _ClassVar[DatastoreType.Type]
    kLocal: DatastoreType.Type
    kNFS: DatastoreType.Type
    kVMFS: DatastoreType.Type
    kVvol: DatastoreType.Type
    kUnknown: DatastoreType.Type
    kvSAN: DatastoreType.Type
    def __init__(self) -> None: ...

class VSwitchNetworkInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DVPortGroupInfo(_message.Message):
    __slots__ = ("name", "key", "dvswitch_uuid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DVSWITCH_UUID_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    dvswitch_uuid: str
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ..., dvswitch_uuid: _Optional[str] = ...) -> None: ...

class OpaqueNetworkInfo(_message.Message):
    __slots__ = ("name", "id", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    type: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class VmfsDatastoreInfo(_message.Message):
    __slots__ = ("uuid", "disk_partition_list")
    class HostScsiDiskPartition(_message.Message):
        __slots__ = ("scsi_disk_device_name", "partition_number")
        SCSI_DISK_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        PARTITION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        scsi_disk_device_name: str
        partition_number: int
        def __init__(self, scsi_disk_device_name: _Optional[str] = ..., partition_number: _Optional[int] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    DISK_PARTITION_LIST_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    disk_partition_list: _containers.RepeatedCompositeFieldContainer[VmfsDatastoreInfo.HostScsiDiskPartition]
    def __init__(self, uuid: _Optional[str] = ..., disk_partition_list: _Optional[_Iterable[_Union[VmfsDatastoreInfo.HostScsiDiskPartition, _Mapping]]] = ...) -> None: ...

class NasDatastoreInfo(_message.Message):
    __slots__ = ("nas_path",)
    NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    nas_path: _nas_pb2.NasPathProto
    def __init__(self, nas_path: _Optional[_Union[_nas_pb2.NasPathProto, _Mapping]] = ...) -> None: ...

class VirtualDiskControllerInfo(_message.Message):
    __slots__ = ("type", "key", "controller_key", "unit_number", "bus_number", "scsi_controller_unit_number", "device_key_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[VirtualDiskControllerInfo.Type]
        kScsiLsiLogic: _ClassVar[VirtualDiskControllerInfo.Type]
        kScsiLsiLogicSAS: _ClassVar[VirtualDiskControllerInfo.Type]
        kScsiVMwareParaVirtual: _ClassVar[VirtualDiskControllerInfo.Type]
        kIde: _ClassVar[VirtualDiskControllerInfo.Type]
        kNvme: _ClassVar[VirtualDiskControllerInfo.Type]
        kScsiBusLogic: _ClassVar[VirtualDiskControllerInfo.Type]
        kAhci: _ClassVar[VirtualDiskControllerInfo.Type]
    kUnknown: VirtualDiskControllerInfo.Type
    kScsiLsiLogic: VirtualDiskControllerInfo.Type
    kScsiLsiLogicSAS: VirtualDiskControllerInfo.Type
    kScsiVMwareParaVirtual: VirtualDiskControllerInfo.Type
    kIde: VirtualDiskControllerInfo.Type
    kNvme: VirtualDiskControllerInfo.Type
    kScsiBusLogic: VirtualDiskControllerInfo.Type
    kAhci: VirtualDiskControllerInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SCSI_CONTROLLER_UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    type: VirtualDiskControllerInfo.Type
    key: int
    controller_key: int
    unit_number: int
    bus_number: int
    scsi_controller_unit_number: int
    device_key_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[_Union[VirtualDiskControllerInfo.Type, str]] = ..., key: _Optional[int] = ..., controller_key: _Optional[int] = ..., unit_number: _Optional[int] = ..., bus_number: _Optional[int] = ..., scsi_controller_unit_number: _Optional[int] = ..., device_key_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class VirtualDiskDeviceInfo(_message.Message):
    __slots__ = ("disk_id", "datastore_moref", "datastore_name", "file_path", "key", "unit_number", "controller_key", "capacity", "thin_provisioned", "thick_eager_scrub_provision")
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEY_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    THIN_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
    THICK_EAGER_SCRUB_PROVISION_FIELD_NUMBER: _ClassVar[int]
    disk_id: str
    datastore_moref: _vmware_common_pb2.MORef
    datastore_name: str
    file_path: str
    key: int
    unit_number: int
    controller_key: int
    capacity: int
    thin_provisioned: bool
    thick_eager_scrub_provision: bool
    def __init__(self, disk_id: _Optional[str] = ..., datastore_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., datastore_name: _Optional[str] = ..., file_path: _Optional[str] = ..., key: _Optional[int] = ..., unit_number: _Optional[int] = ..., controller_key: _Optional[int] = ..., capacity: _Optional[int] = ..., thin_provisioned: bool = ..., thick_eager_scrub_provision: bool = ...) -> None: ...

class ClusterIoFilterInfo(_message.Message):
    __slots__ = ("id", "name", "vendor", "version", "type", "summary", "release_date", "op_type", "vib_url", "io_filter_issues")
    class IoFilterIssues(_message.Message):
        __slots__ = ("action", "host_io_filter_issues")
        ACTION_FIELD_NUMBER: _ClassVar[int]
        HOST_IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
        action: str
        host_io_filter_issues: _containers.RepeatedCompositeFieldContainer[IoFilterHostIssue]
        def __init__(self, action: _Optional[str] = ..., host_io_filter_issues: _Optional[_Iterable[_Union[IoFilterHostIssue, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIB_URL_FIELD_NUMBER: _ClassVar[int]
    IO_FILTER_ISSUES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    vendor: str
    version: str
    type: str
    summary: str
    release_date: str
    op_type: str
    vib_url: str
    io_filter_issues: ClusterIoFilterInfo.IoFilterIssues
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., vendor: _Optional[str] = ..., version: _Optional[str] = ..., type: _Optional[str] = ..., summary: _Optional[str] = ..., release_date: _Optional[str] = ..., op_type: _Optional[str] = ..., vib_url: _Optional[str] = ..., io_filter_issues: _Optional[_Union[ClusterIoFilterInfo.IoFilterIssues, _Mapping]] = ...) -> None: ...

class IoFilterHostIssue(_message.Message):
    __slots__ = ("host_moref", "errors")
    HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    host_moref: _vmware_common_pb2.MORef
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, host_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class IPSetting(_message.Message):
    __slots__ = ("ipv4_addr", "prefix_length", "ipv6_addr")
    IPV4_ADDR_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDR_FIELD_NUMBER: _ClassVar[int]
    ipv4_addr: str
    prefix_length: int
    ipv6_addr: str
    def __init__(self, ipv4_addr: _Optional[str] = ..., prefix_length: _Optional[int] = ..., ipv6_addr: _Optional[str] = ...) -> None: ...

class NICSetting(_message.Message):
    __slots__ = ("device_id", "mac_address", "ip_setting_vec", "device_idx", "adapter_type", "is_connected")
    class NetworkAdapterType(_message.Message):
        __slots__ = ("vcenter_adapter_type", "vcd_adapter_type")
        VCENTER_ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        VCD_ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        vcenter_adapter_type: int
        vcd_adapter_type: str
        def __init__(self, vcenter_adapter_type: _Optional[int] = ..., vcd_adapter_type: _Optional[str] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDX_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    mac_address: str
    ip_setting_vec: _containers.RepeatedCompositeFieldContainer[IPSetting]
    device_idx: int
    adapter_type: NICSetting.NetworkAdapterType
    is_connected: bool
    def __init__(self, device_id: _Optional[int] = ..., mac_address: _Optional[str] = ..., ip_setting_vec: _Optional[_Iterable[_Union[IPSetting, _Mapping]]] = ..., device_idx: _Optional[int] = ..., adapter_type: _Optional[_Union[NICSetting.NetworkAdapterType, _Mapping]] = ..., is_connected: bool = ...) -> None: ...

class DeviceGatewayMap(_message.Message):
    __slots__ = ("ip_addr", "device_id")
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ip_addr: str
    device_id: str
    def __init__(self, ip_addr: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...

class TaskDescriptionId(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TaskDescriptionId.Type]
        kCreateSnapshot: _ClassVar[TaskDescriptionId.Type]
        kRemoveAllSnapshots: _ClassVar[TaskDescriptionId.Type]
        kConsolidateDisks: _ClassVar[TaskDescriptionId.Type]
        kRemoveSnapshot: _ClassVar[TaskDescriptionId.Type]
    kUnknown: TaskDescriptionId.Type
    kCreateSnapshot: TaskDescriptionId.Type
    kRemoveAllSnapshots: TaskDescriptionId.Type
    kConsolidateDisks: TaskDescriptionId.Type
    kRemoveSnapshot: TaskDescriptionId.Type
    def __init__(self) -> None: ...

class TaskInfo(_message.Message):
    __slots__ = ("state", "task_moref", "description_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[TaskInfo.State]
        kQueued: _ClassVar[TaskInfo.State]
        kRunning: _ClassVar[TaskInfo.State]
        kSuccess: _ClassVar[TaskInfo.State]
        kError: _ClassVar[TaskInfo.State]
    kUnknown: TaskInfo.State
    kQueued: TaskInfo.State
    kRunning: TaskInfo.State
    kSuccess: TaskInfo.State
    kError: TaskInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    state: TaskInfo.State
    task_moref: _vmware_common_pb2.MORef
    description_id: TaskDescriptionId.Type
    def __init__(self, state: _Optional[_Union[TaskInfo.State, str]] = ..., task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., description_id: _Optional[_Union[TaskDescriptionId.Type, str]] = ...) -> None: ...

class VMwareEntityConnectivityInfo(_message.Message):
    __slots__ = ("entity_type", "soap_connection_state", "soap_connection_error_msg")
    VMWARE_ENTITY_CONNECTIVITY_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_entity_connectivity_info: _descriptor.FieldDescriptor
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOAP_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    SOAP_CONNECTION_ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    entity_type: _vmware_pb2.Entity.Type
    soap_connection_state: _magneto_pb2.EntityConnectivityProto.ConnectionState
    soap_connection_error_msg: str
    def __init__(self, entity_type: _Optional[_Union[_vmware_pb2.Entity.Type, str]] = ..., soap_connection_state: _Optional[_Union[_magneto_pb2.EntityConnectivityProto.ConnectionState, str]] = ..., soap_connection_error_msg: _Optional[str] = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ("disk_delta_info_map",)
    class DiskDeltaInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cbt_delta_pb2.CBTDeltaInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ...) -> None: ...
    VMWARE_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    vmware_snapshot_scribe_info: _descriptor.FieldDescriptor
    DISK_DELTA_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    disk_delta_info_map: _containers.MessageMap[int, _cbt_delta_pb2.CBTDeltaInfo]
    def __init__(self, disk_delta_info_map: _Optional[_Mapping[int, _cbt_delta_pb2.CBTDeltaInfo]] = ...) -> None: ...

class DiskLayoutInfo(_message.Message):
    __slots__ = ("size", "granularity", "min_block_size", "provision_block_size", "map_start", "map_length", "host_disk_block_info_vmfs_mapping")
    class HostDiskBlockInfoVmfsMapping(_message.Message):
        __slots__ = ("element", "extents")
        class Extent(_message.Message):
            __slots__ = ("logical_start", "physical_start", "length", "read_only", "lazy_zero")
            LOGICAL_START_FIELD_NUMBER: _ClassVar[int]
            PHYSICAL_START_FIELD_NUMBER: _ClassVar[int]
            LENGTH_FIELD_NUMBER: _ClassVar[int]
            READ_ONLY_FIELD_NUMBER: _ClassVar[int]
            LAZY_ZERO_FIELD_NUMBER: _ClassVar[int]
            logical_start: int
            physical_start: int
            length: int
            read_only: bool
            lazy_zero: bool
            def __init__(self, logical_start: _Optional[int] = ..., physical_start: _Optional[int] = ..., length: _Optional[int] = ..., read_only: bool = ..., lazy_zero: bool = ...) -> None: ...
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        EXTENTS_FIELD_NUMBER: _ClassVar[int]
        element: str
        extents: _containers.RepeatedCompositeFieldContainer[DiskLayoutInfo.HostDiskBlockInfoVmfsMapping.Extent]
        def __init__(self, element: _Optional[str] = ..., extents: _Optional[_Iterable[_Union[DiskLayoutInfo.HostDiskBlockInfoVmfsMapping.Extent, _Mapping]]] = ...) -> None: ...
    SIZE_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    MIN_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    PROVISION_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAP_START_FIELD_NUMBER: _ClassVar[int]
    MAP_LENGTH_FIELD_NUMBER: _ClassVar[int]
    HOST_DISK_BLOCK_INFO_VMFS_MAPPING_FIELD_NUMBER: _ClassVar[int]
    size: int
    granularity: int
    min_block_size: int
    provision_block_size: int
    map_start: int
    map_length: int
    host_disk_block_info_vmfs_mapping: DiskLayoutInfo.HostDiskBlockInfoVmfsMapping
    def __init__(self, size: _Optional[int] = ..., granularity: _Optional[int] = ..., min_block_size: _Optional[int] = ..., provision_block_size: _Optional[int] = ..., map_start: _Optional[int] = ..., map_length: _Optional[int] = ..., host_disk_block_info_vmfs_mapping: _Optional[_Union[DiskLayoutInfo.HostDiskBlockInfoVmfsMapping, _Mapping]] = ...) -> None: ...

class VMwareDiskAreaProto(_message.Message):
    __slots__ = ("physical_start_pos",)
    VMWARE_DISK_AREA_FIELD_NUMBER: _ClassVar[int]
    vmware_disk_area: _descriptor.FieldDescriptor
    PHYSICAL_START_POS_FIELD_NUMBER: _ClassVar[int]
    physical_start_pos: int
    def __init__(self, physical_start_pos: _Optional[int] = ...) -> None: ...
