from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.app_file import app_file_pb2 as _app_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupAppFilesArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "source_entity", "app_file_group_info_vec", "common_host_dir_name", "perform_dedup_read", "min_dedup_chunk_size", "max_dedup_chunk_size", "non_dedup_chunk_size", "cluster_id", "cluster_incarnation_id", "enable_file_handle_cache")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupAppFilesArg.Type]
        kSetupFiles: _ClassVar[BackupAppFilesArg.Type]
        kBackupFile: _ClassVar[BackupAppFilesArg.Type]
        kCloseFile: _ClassVar[BackupAppFilesArg.Type]
        kEndBackup: _ClassVar[BackupAppFilesArg.Type]
    kPrepareBackup: BackupAppFilesArg.Type
    kSetupFiles: BackupAppFilesArg.Type
    kBackupFile: BackupAppFilesArg.Type
    kCloseFile: BackupAppFilesArg.Type
    kEndBackup: BackupAppFilesArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COMMON_HOST_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    PERFORM_DEDUP_READ_FIELD_NUMBER: _ClassVar[int]
    MIN_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    NON_DEDUP_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FILE_HANDLE_CACHE_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupAppFilesArg.Type
    root_entity: _entity_pb2.EntityProto
    source_entity: _entity_pb2.EntityProto
    app_file_group_info_vec: _containers.RepeatedCompositeFieldContainer[_app_file_pb2.AppFileGroupInfo]
    common_host_dir_name: str
    perform_dedup_read: bool
    min_dedup_chunk_size: int
    max_dedup_chunk_size: int
    non_dedup_chunk_size: int
    cluster_id: int
    cluster_incarnation_id: int
    enable_file_handle_cache: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupAppFilesArg.Type, str]] = ..., root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., source_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., app_file_group_info_vec: _Optional[_Iterable[_Union[_app_file_pb2.AppFileGroupInfo, _Mapping]]] = ..., common_host_dir_name: _Optional[str] = ..., perform_dedup_read: bool = ..., min_dedup_chunk_size: _Optional[int] = ..., max_dedup_chunk_size: _Optional[int] = ..., non_dedup_chunk_size: _Optional[int] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ..., enable_file_handle_cache: bool = ...) -> None: ...

class RestoreAppFilesArg(_message.Message):
    __slots__ = ("type", "app_file_group_restore_info_vec", "view_box_id", "view_name", "create_view", "is_internal_view", "path_prefix", "view_whitelist_ip_addr_str_vec", "view_whitelist_ip_ranges_vec", "use_non_atomic_clone")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneAppFiles: _ClassVar[RestoreAppFilesArg.Type]
        kDeleteAppFiles: _ClassVar[RestoreAppFilesArg.Type]
    kCloneAppFiles: RestoreAppFilesArg.Type
    kDeleteAppFiles: RestoreAppFilesArg.Type
    class AppFileGroupRestoreInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "group_dir_name", "create_directory_per_group", "source_entity", "delete_file_relative_path_vec")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        GROUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        CREATE_DIRECTORY_PER_GROUP_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ENTITY_FIELD_NUMBER: _ClassVar[int]
        DELETE_FILE_RELATIVE_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        group_dir_name: str
        create_directory_per_group: bool
        source_entity: _entity_pb2.EntityProto
        delete_file_relative_path_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., group_dir_name: _Optional[str] = ..., create_directory_per_group: bool = ..., source_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., delete_file_relative_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_RESTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_RANGES_VEC_FIELD_NUMBER: _ClassVar[int]
    USE_NON_ATOMIC_CLONE_FIELD_NUMBER: _ClassVar[int]
    type: RestoreAppFilesArg.Type
    app_file_group_restore_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreAppFilesArg.AppFileGroupRestoreInfo]
    view_box_id: int
    view_name: str
    create_view: bool
    is_internal_view: bool
    path_prefix: str
    view_whitelist_ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    view_whitelist_ip_ranges_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.Subnet]
    use_non_atomic_clone: bool
    def __init__(self, type: _Optional[_Union[RestoreAppFilesArg.Type, str]] = ..., app_file_group_restore_info_vec: _Optional[_Iterable[_Union[RestoreAppFilesArg.AppFileGroupRestoreInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., create_view: bool = ..., is_internal_view: bool = ..., path_prefix: _Optional[str] = ..., view_whitelist_ip_addr_str_vec: _Optional[_Iterable[str]] = ..., view_whitelist_ip_ranges_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.Subnet, _Mapping]]] = ..., use_non_atomic_clone: bool = ...) -> None: ...

class AppFileActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_app_files_arg", "restore_app_files_arg", "cancel_task_arg")
    APP_FILE_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    app_file_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_APP_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_APP_FILES_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_app_files_arg: BackupAppFilesArg
    restore_app_files_arg: RestoreAppFilesArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_app_files_arg: _Optional[_Union[BackupAppFilesArg, _Mapping]] = ..., restore_app_files_arg: _Optional[_Union[RestoreAppFilesArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ...) -> None: ...
