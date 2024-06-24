from magneto.agents.windows.base import hyperv_pb2 as _hyperv_pb2
from magneto.agents.windows.base import file_attrs_pb2 as _file_attrs_pb2
from magneto.base import cloud_pb2 as _cloud_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import storage_pb2 as _storage_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from magneto.connectors.hyperv import hyperv_setup_restore_disks_pb2 as _hyperv_setup_restore_disks_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from util.disklib.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VirtualDisk(_message.Message):
    __slots__ = ("key", "uuid", "filepath", "snapshot_device_filepath", "parent_full_path", "parent_disk_uuid", "capacity", "logical_disk_size", "disk_format", "disk_type", "rct_id", "snapshot_uuid", "delta_type", "delta_info", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "disk_area_start_offset", "query_disk_error", "file_attributes", "logical_sector_size_bytes", "unit_number", "controller_bus_number", "controller_type")
    Extensions: _python_message._ExtensionDict
    HYPERV_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    hyperv_virtual_disk: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_DISK_UUID_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    RCT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    key: int
    uuid: str
    filepath: str
    snapshot_device_filepath: str
    parent_full_path: str
    parent_disk_uuid: str
    capacity: int
    logical_disk_size: int
    disk_format: _enums_pb2.DiskFormat.Type
    disk_type: _enums_pb2.VirtualHardDiskType.Type
    rct_id: str
    snapshot_uuid: bytes
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    disk_area_start_offset: int
    query_disk_error: _error_pb2.ErrorProto
    file_attributes: _file_attrs_pb2.FileAttributes
    logical_sector_size_bytes: int
    unit_number: int
    controller_bus_number: int
    controller_type: str
    def __init__(self, key: _Optional[int] = ..., uuid: _Optional[str] = ..., filepath: _Optional[str] = ..., snapshot_device_filepath: _Optional[str] = ..., parent_full_path: _Optional[str] = ..., parent_disk_uuid: _Optional[str] = ..., capacity: _Optional[int] = ..., logical_disk_size: _Optional[int] = ..., disk_format: _Optional[_Union[_enums_pb2.DiskFormat.Type, str]] = ..., disk_type: _Optional[_Union[_enums_pb2.VirtualHardDiskType.Type, str]] = ..., rct_id: _Optional[str] = ..., snapshot_uuid: _Optional[bytes] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., disk_area_start_offset: _Optional[int] = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ..., logical_sector_size_bytes: _Optional[int] = ..., unit_number: _Optional[int] = ..., controller_bus_number: _Optional[int] = ..., controller_type: _Optional[str] = ...) -> None: ...

class LargeConfigFile(_message.Message):
    __slots__ = ("type", "base")
    LARGE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    large_config_file: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    type: _hyperv_pb2.VMConfigFile.Type
    base: VirtualDisk
    def __init__(self, type: _Optional[_Union[_hyperv_pb2.VMConfigFile.Type, str]] = ..., base: _Optional[_Union[VirtualDisk, _Mapping]] = ...) -> None: ...

class LogicalVirtualDisk(_message.Message):
    __slots__ = ("key", "uuid", "capacity", "virtual_disks", "logical_sector_size_bytes", "disk_format", "disk_type")
    KEY_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    key: int
    uuid: str
    capacity: int
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    logical_sector_size_bytes: int
    disk_format: _enums_pb2.DiskFormat.Type
    disk_type: _enums_pb2.VirtualHardDiskType.Type
    def __init__(self, key: _Optional[int] = ..., uuid: _Optional[str] = ..., capacity: _Optional[int] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., logical_sector_size_bytes: _Optional[int] = ..., disk_format: _Optional[_Union[_enums_pb2.DiskFormat.Type, str]] = ..., disk_type: _Optional[_Union[_enums_pb2.VirtualHardDiskType.Type, str]] = ...) -> None: ...

class SparseVMConfig(_message.Message):
    __slots__ = ("hyperv_vm_info", "logical_virtual_disk_vec", "virtual_disks", "additional_file_info_vec", "vm_snapshot_directory_path", "user_excluded_virtual_disks_vec")
    class AdditionalFileInfo(_message.Message):
        __slots__ = ("file_name", "type", "file_attributes")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        type: _hyperv_pb2.VMConfigFile.Type
        file_attributes: _file_attrs_pb2.FileAttributes
        def __init__(self, file_name: _Optional[str] = ..., type: _Optional[_Union[_hyperv_pb2.VMConfigFile.Type, str]] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ...) -> None: ...
    HYPERV_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_SNAPSHOT_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    hyperv_vm_info: _hyperv_pb2.HyperVVMInfo
    logical_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[LogicalVirtualDisk]
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    additional_file_info_vec: _containers.RepeatedCompositeFieldContainer[SparseVMConfig.AdditionalFileInfo]
    vm_snapshot_directory_path: str
    user_excluded_virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    def __init__(self, hyperv_vm_info: _Optional[_Union[_hyperv_pb2.HyperVVMInfo, _Mapping]] = ..., logical_virtual_disk_vec: _Optional[_Iterable[_Union[LogicalVirtualDisk, _Mapping]]] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., additional_file_info_vec: _Optional[_Iterable[_Union[SparseVMConfig.AdditionalFileInfo, _Mapping]]] = ..., vm_snapshot_directory_path: _Optional[str] = ..., user_excluded_virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ...) -> None: ...

class VolumeInfo(_message.Message):
    __slots__ = ("uuid", "name")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("vm_name", "checkpoint_instance_id", "job_instance_id", "attempt_num", "hyperv_vm_id", "is_app_consistent", "vm_snapshot_directory_path", "permit_host_info", "permit_volume_info_vec", "datastore_throttling_feature_enabled", "server_checkpoint_info", "server_reference_point", "status", "fetched_file_info_vec", "snapshot_set_id", "is_snapshot_owner", "snapshot_deletion_pending", "virtual_disks", "user_excluded_virtual_disks_vec", "large_config_files", "logical_virtual_disk_vec", "sub_tasks_vec", "error", "app_user_messages", "convert_to_reference_point_error", "snapshot_deletion_error", "sub_file_size_mb", "take_snapshot_error", "notify_backup_complete_error", "abort_snapshot_error", "delta_info_in_scribe", "fetch_vss_snapshot_error", "networks", "num_locate_vm_calls")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kPermitGranted: _ClassVar[SnapshotInfo.Status]
        kPrepareHostForSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kCreateCheckpointDone: _ClassVar[SnapshotInfo.Status]
        kCheckpointInfoFetched: _ClassVar[SnapshotInfo.Status]
        kQueryChangesVirtualDiskDone: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kPermitGranted: SnapshotInfo.Status
    kPrepareHostForSnapshotDone: SnapshotInfo.Status
    kCreateCheckpointDone: SnapshotInfo.Status
    kCheckpointInfoFetched: SnapshotInfo.Status
    kQueryChangesVirtualDiskDone: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    class FileInfo(_message.Message):
        __slots__ = ("file_name", "data", "error", "type", "is_compressed", "file_attributes", "length")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
        FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        data: bytes
        error: _error_pb2.ErrorProto
        type: _hyperv_pb2.VMConfigFile.Type
        is_compressed: bool
        file_attributes: _file_attrs_pb2.FileAttributes
        length: int
        def __init__(self, file_name: _Optional[str] = ..., data: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., type: _Optional[_Union[_hyperv_pb2.VMConfigFile.Type, str]] = ..., is_compressed: bool = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ..., length: _Optional[int] = ...) -> None: ...
    HYPERV_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_snapshot_info: _descriptor.FieldDescriptor
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_APP_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    VM_SNAPSHOT_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    PERMIT_HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    PERMIT_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVER_CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVER_REFERENCE_POINT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FETCHED_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SNAPSHOT_OWNER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_PENDING_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    LARGE_CONFIG_FILES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TO_REFERENCE_POINT_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    TAKE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_ERROR_FIELD_NUMBER: _ClassVar[int]
    ABORT_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_IN_SCRIBE_FIELD_NUMBER: _ClassVar[int]
    FETCH_VSS_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NUM_LOCATE_VM_CALLS_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    checkpoint_instance_id: bytes
    job_instance_id: int
    attempt_num: int
    hyperv_vm_id: bytes
    is_app_consistent: bool
    vm_snapshot_directory_path: str
    permit_host_info: _hyperv_pb2.HyperVHostInfo
    permit_volume_info_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfo]
    datastore_throttling_feature_enabled: bool
    server_checkpoint_info: _hyperv_pb2.CheckpointInfo
    server_reference_point: _hyperv_pb2.VMReferencePoint
    status: SnapshotInfo.Status
    fetched_file_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.FileInfo]
    snapshot_set_id: bytes
    is_snapshot_owner: bool
    snapshot_deletion_pending: bool
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    user_excluded_virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    large_config_files: _containers.RepeatedCompositeFieldContainer[LargeConfigFile]
    logical_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[LogicalVirtualDisk]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    app_user_messages: _magneto_pb2.UserMessageProto
    convert_to_reference_point_error: _error_pb2.ErrorProto
    snapshot_deletion_error: _error_pb2.ErrorProto
    sub_file_size_mb: int
    take_snapshot_error: _error_pb2.ErrorProto
    notify_backup_complete_error: _error_pb2.ErrorProto
    abort_snapshot_error: _error_pb2.ErrorProto
    delta_info_in_scribe: bool
    fetch_vss_snapshot_error: _error_pb2.ErrorProto
    networks: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    num_locate_vm_calls: int
    def __init__(self, vm_name: _Optional[str] = ..., checkpoint_instance_id: _Optional[bytes] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., hyperv_vm_id: _Optional[bytes] = ..., is_app_consistent: bool = ..., vm_snapshot_directory_path: _Optional[str] = ..., permit_host_info: _Optional[_Union[_hyperv_pb2.HyperVHostInfo, _Mapping]] = ..., permit_volume_info_vec: _Optional[_Iterable[_Union[VolumeInfo, _Mapping]]] = ..., datastore_throttling_feature_enabled: bool = ..., server_checkpoint_info: _Optional[_Union[_hyperv_pb2.CheckpointInfo, _Mapping]] = ..., server_reference_point: _Optional[_Union[_hyperv_pb2.VMReferencePoint, _Mapping]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., fetched_file_info_vec: _Optional[_Iterable[_Union[SnapshotInfo.FileInfo, _Mapping]]] = ..., snapshot_set_id: _Optional[bytes] = ..., is_snapshot_owner: bool = ..., snapshot_deletion_pending: bool = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., user_excluded_virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., large_config_files: _Optional[_Iterable[_Union[LargeConfigFile, _Mapping]]] = ..., logical_virtual_disk_vec: _Optional[_Iterable[_Union[LogicalVirtualDisk, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ..., convert_to_reference_point_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sub_file_size_mb: _Optional[int] = ..., take_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., notify_backup_complete_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., abort_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delta_info_in_scribe: bool = ..., fetch_vss_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., networks: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., num_locate_vm_calls: _Optional[int] = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ("virtual_disk_vec",)
    HYPERV_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_snapshot_scribe_info: _descriptor.FieldDescriptor
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    def __init__(self, virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ...) -> None: ...

class EntitiesGroupSnapshotInfo(_message.Message):
    __slots__ = ("status", "snapshot_set_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kPrepareHostForSnapshotDone: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kTakeSnapshotDone: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kFinished: _ClassVar[EntitiesGroupSnapshotInfo.Status]
        kCancelled: _ClassVar[EntitiesGroupSnapshotInfo.Status]
    kStarted: EntitiesGroupSnapshotInfo.Status
    kPrepareHostForSnapshotDone: EntitiesGroupSnapshotInfo.Status
    kTakeSnapshotDone: EntitiesGroupSnapshotInfo.Status
    kFinished: EntitiesGroupSnapshotInfo.Status
    kCancelled: EntitiesGroupSnapshotInfo.Status
    HYPERV_VSS_GROUP_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_vss_group_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    status: EntitiesGroupSnapshotInfo.Status
    snapshot_set_id: bytes
    def __init__(self, status: _Optional[_Union[EntitiesGroupSnapshotInfo.Status, str]] = ..., snapshot_set_id: _Optional[bytes] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("restore_task_state", "vm_folder_name", "vm_folder_created", "clone_files_path_prefix", "storage_vmotion_skipped", "restore_task_start_time_usecs", "host_info_proto_map", "unmount_datastore_after_cancellation")
    class RestoreTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMsCloned: _ClassVar[RestoreInfo.RestoreTaskState]
        kHostAssigned: _ClassVar[RestoreInfo.RestoreTaskState]
        kDatastoreMounted: _ClassVar[RestoreInfo.RestoreTaskState]
        kVMCreated: _ClassVar[RestoreInfo.RestoreTaskState]
        kDatastoreUnmounted: _ClassVar[RestoreInfo.RestoreTaskState]
        kPermitGranted: _ClassVar[RestoreInfo.RestoreTaskState]
        kPermitReleased: _ClassVar[RestoreInfo.RestoreTaskState]
    kStarted: RestoreInfo.RestoreTaskState
    kVMsCloned: RestoreInfo.RestoreTaskState
    kHostAssigned: RestoreInfo.RestoreTaskState
    kDatastoreMounted: RestoreInfo.RestoreTaskState
    kVMCreated: RestoreInfo.RestoreTaskState
    kDatastoreUnmounted: RestoreInfo.RestoreTaskState
    kPermitGranted: RestoreInfo.RestoreTaskState
    kPermitReleased: RestoreInfo.RestoreTaskState
    class HostInfoProto(_message.Message):
        __slots__ = ("name", "nas_mount_error", "nas_mount_path")
        NAME_FIELD_NUMBER: _ClassVar[int]
        NAS_MOUNT_ERROR_FIELD_NUMBER: _ClassVar[int]
        NAS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        name: str
        nas_mount_error: _error_pb2.ErrorProto
        nas_mount_path: str
        def __init__(self, name: _Optional[str] = ..., nas_mount_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., nas_mount_path: _Optional[str] = ...) -> None: ...
    class HostInfoProtoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RestoreInfo.HostInfoProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RestoreInfo.HostInfoProto, _Mapping]] = ...) -> None: ...
    HYPERV_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_restore_info: _descriptor.FieldDescriptor
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_CREATED_FIELD_NUMBER: _ClassVar[int]
    CLONE_FILES_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    STORAGE_VMOTION_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_PROTO_MAP_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_DATASTORE_AFTER_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: RestoreInfo.RestoreTaskState
    vm_folder_name: str
    vm_folder_created: bool
    clone_files_path_prefix: str
    storage_vmotion_skipped: bool
    restore_task_start_time_usecs: int
    host_info_proto_map: _containers.MessageMap[str, RestoreInfo.HostInfoProto]
    unmount_datastore_after_cancellation: bool
    def __init__(self, restore_task_state: _Optional[_Union[RestoreInfo.RestoreTaskState, str]] = ..., vm_folder_name: _Optional[str] = ..., vm_folder_created: bool = ..., clone_files_path_prefix: _Optional[str] = ..., storage_vmotion_skipped: bool = ..., restore_task_start_time_usecs: _Optional[int] = ..., host_info_proto_map: _Optional[_Mapping[str, RestoreInfo.HostInfoProto]] = ..., unmount_datastore_after_cancellation: bool = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("state", "host_info", "agent_handle", "sparse_vm_config", "chained_logical_disk_mapping", "restore_files_info")
    class RestoreEntityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreEntityInfo.RestoreEntityState]
        kImported: _ClassVar[RestoreEntityInfo.RestoreEntityState]
        kDataMigrated: _ClassVar[RestoreEntityInfo.RestoreEntityState]
        kRealized: _ClassVar[RestoreEntityInfo.RestoreEntityState]
        kFinalized: _ClassVar[RestoreEntityInfo.RestoreEntityState]
    kStarted: RestoreEntityInfo.RestoreEntityState
    kImported: RestoreEntityInfo.RestoreEntityState
    kDataMigrated: RestoreEntityInfo.RestoreEntityState
    kRealized: RestoreEntityInfo.RestoreEntityState
    kFinalized: RestoreEntityInfo.RestoreEntityState
    HYPERV_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_restore_entity_info: _descriptor.FieldDescriptor
    HYPERV_CLOUD_DEPLOY_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_cloud_deploy_entity_info: _descriptor.FieldDescriptor
    STATE_FIELD_NUMBER: _ClassVar[int]
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    AGENT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CHAINED_LOGICAL_DISK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    state: RestoreEntityInfo.RestoreEntityState
    host_info: _hyperv_pb2.HyperVHostInfo
    agent_handle: _hyperv_pb2.RestoreVMHandle
    sparse_vm_config: SparseVMConfig
    chained_logical_disk_mapping: _cloud_pb2.ChainedLogicalDiskMapping
    restore_files_info: _magneto_pb2.RestoreFilesInfoProto
    def __init__(self, state: _Optional[_Union[RestoreEntityInfo.RestoreEntityState, str]] = ..., host_info: _Optional[_Union[_hyperv_pb2.HyperVHostInfo, _Mapping]] = ..., agent_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[SparseVMConfig, _Mapping]] = ..., chained_logical_disk_mapping: _Optional[_Union[_cloud_pb2.ChainedLogicalDiskMapping, _Mapping]] = ..., restore_files_info: _Optional[_Union[_magneto_pb2.RestoreFilesInfoProto, _Mapping]] = ...) -> None: ...

class EntitySnapshotInfo(_message.Message):
    __slots__ = ("snapshot_set_id",)
    HYPERV_VSS_ENTITY_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_vss_entity_snapshot_info: _descriptor.FieldDescriptor
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    snapshot_set_id: str
    def __init__(self, snapshot_set_id: _Optional[str] = ...) -> None: ...

class RestoreFilesInfo(_message.Message):
    __slots__ = ("task_state", "restore_disks_task_info", "error", "tear_down_error")
    class RestoreFilesTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kSetupCompleted: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kCopyFilesInitiated: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kCopyFilesCompleted: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kTeardownInitiated: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kFinished: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
        kCancelled: _ClassVar[RestoreFilesInfo.RestoreFilesTaskState]
    kStarted: RestoreFilesInfo.RestoreFilesTaskState
    kSetupCompleted: RestoreFilesInfo.RestoreFilesTaskState
    kCopyFilesInitiated: RestoreFilesInfo.RestoreFilesTaskState
    kCopyFilesCompleted: RestoreFilesInfo.RestoreFilesTaskState
    kTeardownInitiated: RestoreFilesInfo.RestoreFilesTaskState
    kFinished: RestoreFilesInfo.RestoreFilesTaskState
    kCancelled: RestoreFilesInfo.RestoreFilesTaskState
    HYPERV_RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_restore_files_info: _descriptor.FieldDescriptor
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEAR_DOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    task_state: RestoreFilesInfo.RestoreFilesTaskState
    restore_disks_task_info: _hyperv_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo
    error: _error_pb2.ErrorProto
    tear_down_error: _error_pb2.ErrorProto
    def __init__(self, task_state: _Optional[_Union[RestoreFilesInfo.RestoreFilesTaskState, str]] = ..., restore_disks_task_info: _Optional[_Union[_hyperv_setup_restore_disks_pb2.SetupRestoreDiskTaskInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., tear_down_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("vm_info", "encoded_flat_file_map")
    class EncodedFlatFileMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FLAT_FILE_MAP_FIELD_NUMBER: _ClassVar[int]
    vm_info: _hyperv_pb2.HyperVVMInfo
    encoded_flat_file_map: _containers.ScalarMap[str, str]
    def __init__(self, vm_info: _Optional[_Union[_hyperv_pb2.HyperVVMInfo, _Mapping]] = ..., encoded_flat_file_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DestroyClonedTaskInfo(_message.Message):
    __slots__ = ("host_info_vec",)
    HYPERV_DESTROY_CLONED_VM_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_destroy_cloned_vm_task_info: _descriptor.FieldDescriptor
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    host_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreInfo.HostInfoProto]
    def __init__(self, host_info_vec: _Optional[_Iterable[_Union[RestoreInfo.HostInfoProto, _Mapping]]] = ...) -> None: ...
