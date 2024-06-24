from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.base.entities import physical_pb2 as _physical_pb2
from magneto.base import physical_pb2 as _physical_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "physical_host_entity", "sparse_host_config", "max_vhd_volume_size_bytes", "perform_dedup_read", "min_dedup_chunk_size", "max_dedup_chunk_size", "non_dedup_chunk_size", "virtual_disk_filepaths_to_be_deleted", "create_ancillary_view", "ancillary_view_name", "system_backup_error", "cluster_id", "cluster_incarnation_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupArg.Type]
        kSetupFiles: _ClassVar[BackupArg.Type]
        kBackupDisk: _ClassVar[BackupArg.Type]
        kCloseDisk: _ClassVar[BackupArg.Type]
        kEndBackup: _ClassVar[BackupArg.Type]
    kPrepareBackup: BackupArg.Type
    kSetupFiles: BackupArg.Type
    kBackupDisk: BackupArg.Type
    kCloseDisk: BackupArg.Type
    kEndBackup: BackupArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SPARSE_HOST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_VHD_VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PERFORM_DEDUP_READ_FIELD_NUMBER: _ClassVar[int]
    MIN_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NON_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_FILEPATHS_TO_BE_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATE_ANCILLARY_VIEW_FIELD_NUMBER: _ClassVar[int]
    ANCILLARY_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupArg.Type
    root_entity: _physical_pb2.Entity
    physical_host_entity: _physical_pb2.Entity
    sparse_host_config: _physical_pb2_1.SparseHostConfig
    max_vhd_volume_size_bytes: int
    perform_dedup_read: bool
    min_dedup_chunk_size: int
    max_dedup_chunk_size: int
    non_dedup_chunk_size: int
    virtual_disk_filepaths_to_be_deleted: _containers.RepeatedScalarFieldContainer[str]
    create_ancillary_view: bool
    ancillary_view_name: str
    system_backup_error: int
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupArg.Type, str]] = ..., root_entity: _Optional[_Union[_physical_pb2.Entity, _Mapping]] = ..., physical_host_entity: _Optional[_Union[_physical_pb2.Entity, _Mapping]] = ..., sparse_host_config: _Optional[_Union[_physical_pb2_1.SparseHostConfig, _Mapping]] = ..., max_vhd_volume_size_bytes: _Optional[int] = ..., perform_dedup_read: bool = ..., min_dedup_chunk_size: _Optional[int] = ..., max_dedup_chunk_size: _Optional[int] = ..., non_dedup_chunk_size: _Optional[int] = ..., virtual_disk_filepaths_to_be_deleted: _Optional[_Iterable[str]] = ..., create_ancillary_view: bool = ..., ancillary_view_name: _Optional[str] = ..., system_backup_error: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class RestoreArg(_message.Message):
    __slots__ = ("base", "type", "clone_info_vec", "view_box_id", "view_name", "volume_dev_path", "is_internal_view", "view_whitelist_ip_addr_str_vec", "view_whitelist_ip_ranges_vec", "is_system_restore", "file_restore_through_local_mount", "cluster_id", "cluster_incarnation_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneHosts: _ClassVar[RestoreArg.Type]
        kDeleteClonedHosts: _ClassVar[RestoreArg.Type]
        kRestoreDisk: _ClassVar[RestoreArg.Type]
    kCloneHosts: RestoreArg.Type
    kDeleteClonedHosts: RestoreArg.Type
    kRestoreDisk: RestoreArg.Type
    class CloneInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "host_entity")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        HOST_ENTITY_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        host_entity: _physical_pb2.Entity
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., host_entity: _Optional[_Union[_physical_pb2.Entity, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLONE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DEV_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_RANGES_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_RESTORE_FIELD_NUMBER: _ClassVar[int]
    FILE_RESTORE_THROUGH_LOCAL_MOUNT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreArg.Type
    clone_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreArg.CloneInfo]
    view_box_id: int
    view_name: str
    volume_dev_path: str
    is_internal_view: bool
    view_whitelist_ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    view_whitelist_ip_ranges_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    is_system_restore: bool
    file_restore_through_local_mount: bool
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreArg.Type, str]] = ..., clone_info_vec: _Optional[_Iterable[_Union[RestoreArg.CloneInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., volume_dev_path: _Optional[str] = ..., is_internal_view: bool = ..., view_whitelist_ip_addr_str_vec: _Optional[_Iterable[str]] = ..., view_whitelist_ip_ranges_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., is_system_restore: bool = ..., file_restore_through_local_mount: bool = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class PhysicalActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_arg", "restore_arg", "cancel_task_arg")
    PHYSICAL_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    physical_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_arg: BackupArg
    restore_arg: RestoreArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_arg: _Optional[_Union[BackupArg, _Mapping]] = ..., restore_arg: _Optional[_Union[RestoreArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ...) -> None: ...
