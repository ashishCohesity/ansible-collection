from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VirtualDisk(_message.Message):
    __slots__ = ("volume_guid", "snapshot_guid", "snapshot_device_path", "capacity_bytes", "logical_sector_size_bytes", "key", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "volume_area_start_offset", "disk_area_start_offset", "delta_type", "mount_point_vec")
    PHYSICAL_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    physical_virtual_disk: _descriptor.FieldDescriptor
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_GUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_AREA_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_guid: bytes
    snapshot_guid: bytes
    snapshot_device_path: str
    capacity_bytes: int
    logical_sector_size_bytes: int
    key: int
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    volume_area_start_offset: int
    disk_area_start_offset: int
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, volume_guid: _Optional[bytes] = ..., snapshot_guid: _Optional[bytes] = ..., snapshot_device_path: _Optional[str] = ..., capacity_bytes: _Optional[int] = ..., logical_sector_size_bytes: _Optional[int] = ..., key: _Optional[int] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., volume_area_start_offset: _Optional[int] = ..., disk_area_start_offset: _Optional[int] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., mount_point_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("status", "error", "app_user_messages", "job_instance_id", "attempt_num", "virtual_disks", "sub_tasks_vec", "max_vhd_volume_size_bytes", "server_snapshot_info", "virtual_disk_filepaths_to_be_deleted", "server_snapshot_info_file_name", "server_snapshot_serialized_fetch_info", "take_snapshot_error", "fetch_snapshot_metadata_error", "notify_backup_complete_error", "end_backup_error", "snapshot_deletion_pending", "delete_snapshot_error", "abort_snapshot_error", "host_summary", "agent_info", "sub_file_size_mb", "system_backup_unc_path", "system_backup_nfs_path", "system_backup_view_name", "post_421a_backup")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kPrepareHostForSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kSnapshotTaken: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kPrepareHostForSnapshotDone: SnapshotInfo.Status
    kSnapshotTaken: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    PHYSICAL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    physical_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_VHD_VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_FILEPATHS_TO_BE_DELETED_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_SERIALIZED_FETCH_INFO_FIELD_NUMBER: _ClassVar[int]
    TAKE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    FETCH_SNAPSHOT_METADATA_ERROR_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_ERROR_FIELD_NUMBER: _ClassVar[int]
    END_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_PENDING_FIELD_NUMBER: _ClassVar[int]
    DELETE_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    ABORT_SNAPSHOT_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_BACKUP_UNC_PATH_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_BACKUP_NFS_PATH_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_BACKUP_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    POST_421A_BACKUP_FIELD_NUMBER: _ClassVar[int]
    status: SnapshotInfo.Status
    error: _error_pb2.ErrorProto
    app_user_messages: _magneto_pb2.UserMessageProto
    job_instance_id: int
    attempt_num: int
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    max_vhd_volume_size_bytes: int
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    virtual_disk_filepaths_to_be_deleted: _containers.RepeatedScalarFieldContainer[str]
    server_snapshot_info_file_name: str
    server_snapshot_serialized_fetch_info: _agent_pb2.ServerSnapshotSerializedFetchInfo
    take_snapshot_error: _error_pb2.ErrorProto
    fetch_snapshot_metadata_error: _error_pb2.ErrorProto
    notify_backup_complete_error: _error_pb2.ErrorProto
    end_backup_error: _error_pb2.ErrorProto
    snapshot_deletion_pending: bool
    delete_snapshot_error: _error_pb2.ErrorProto
    abort_snapshot_error: _error_pb2.ErrorProto
    host_summary: _agent_pb2.SnapshotHostInfoSummary
    agent_info: _agent_pb2.AgentInfoProto
    sub_file_size_mb: int
    system_backup_unc_path: str
    system_backup_nfs_path: str
    system_backup_view_name: str
    post_421a_backup: bool
    def __init__(self, status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_user_messages: _Optional[_Union[_magneto_pb2.UserMessageProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., max_vhd_volume_size_bytes: _Optional[int] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ..., virtual_disk_filepaths_to_be_deleted: _Optional[_Iterable[str]] = ..., server_snapshot_info_file_name: _Optional[str] = ..., server_snapshot_serialized_fetch_info: _Optional[_Union[_agent_pb2.ServerSnapshotSerializedFetchInfo, _Mapping]] = ..., take_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., fetch_snapshot_metadata_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., notify_backup_complete_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., end_backup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_pending: bool = ..., delete_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., abort_snapshot_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., host_summary: _Optional[_Union[_agent_pb2.SnapshotHostInfoSummary, _Mapping]] = ..., agent_info: _Optional[_Union[_agent_pb2.AgentInfoProto, _Mapping]] = ..., sub_file_size_mb: _Optional[int] = ..., system_backup_unc_path: _Optional[str] = ..., system_backup_nfs_path: _Optional[str] = ..., system_backup_view_name: _Optional[str] = ..., post_421a_backup: bool = ...) -> None: ...

class SystemBackup(_message.Message):
    __slots__ = ("image_filename",)
    IMAGE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    image_filename: str
    def __init__(self, image_filename: _Optional[str] = ...) -> None: ...

class SparseHostConfig(_message.Message):
    __slots__ = ("host_name", "host_type", "os_version_string", "virtual_disks", "system_backup")
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    host_type: _enums_pb2.HostEnv.Type
    os_version_string: str
    virtual_disks: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    system_backup: SystemBackup
    def __init__(self, host_name: _Optional[str] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., os_version_string: _Optional[str] = ..., virtual_disks: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., system_backup: _Optional[_Union[SystemBackup, _Mapping]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("state", "total_bytes_to_write_to_source", "disk_map", "sub_tasks_vec", "connector_params", "error")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.State]
        kFilesCloned: _ClassVar[RestoreInfo.State]
        kSubTasksCreated: _ClassVar[RestoreInfo.State]
        kSubTasksFinished: _ClassVar[RestoreInfo.State]
        kFinished: _ClassVar[RestoreInfo.State]
    kStarted: RestoreInfo.State
    kFilesCloned: RestoreInfo.State
    kSubTasksCreated: RestoreInfo.State
    kSubTasksFinished: RestoreInfo.State
    kFinished: RestoreInfo.State
    class DiskInfo(_message.Message):
        __slots__ = ("image_path", "vdisk", "volume_dev_path")
        IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
        VDISK_FIELD_NUMBER: _ClassVar[int]
        VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
        image_path: str
        vdisk: VirtualDisk
        volume_dev_path: str
        def __init__(self, image_path: _Optional[str] = ..., vdisk: _Optional[_Union[VirtualDisk, _Mapping]] = ..., volume_dev_path: _Optional[str] = ...) -> None: ...
    class DiskMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RestoreInfo.DiskInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RestoreInfo.DiskInfo, _Mapping]] = ...) -> None: ...
    PHYSICAL_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    physical_restore_info: _descriptor.FieldDescriptor
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DISK_MAP_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: RestoreInfo.State
    total_bytes_to_write_to_source: int
    disk_map: _containers.MessageMap[str, RestoreInfo.DiskInfo]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    connector_params: _magneto_pb2.ConnectorParams
    error: _error_pb2.ErrorProto
    def __init__(self, state: _Optional[_Union[RestoreInfo.State, str]] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., disk_map: _Optional[_Mapping[str, RestoreInfo.DiskInfo]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
