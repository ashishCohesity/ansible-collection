from magneto.api.common import filters_pb2 as _filters_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvBackupParamsProto(_message.Message):
    __slots__ = ("enable_incremental_backup_after_restart", "filtering_policy")
    ENABLE_INCREMENTAL_BACKUP_AFTER_RESTART_FIELD_NUMBER: _ClassVar[int]
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    enable_incremental_backup_after_restart: bool
    filtering_policy: _filters_pb2.FilteringPolicyProto
    def __init__(self, enable_incremental_backup_after_restart: bool = ..., filtering_policy: _Optional[_Union[_filters_pb2.FilteringPolicyProto, _Mapping]] = ...) -> None: ...

class PhysicalFileBackupParams(_message.Message):
    __slots__ = ("backup_path_info_vec", "uses_skip_nested_volumes_vec", "symlink_follow_nas_target", "skip_nested_volumes_vec", "metadata_file_path", "global_include_exclude")
    class GlobalIncludeExclude(_message.Message):
        __slots__ = ("exclude_vec",)
        EXCLUDE_VEC_FIELD_NUMBER: _ClassVar[int]
        exclude_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, exclude_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class BackupPathInfo(_message.Message):
        __slots__ = ("include_path", "exclude_paths", "skip_nested_volumes")
        INCLUDE_PATH_FIELD_NUMBER: _ClassVar[int]
        EXCLUDE_PATHS_FIELD_NUMBER: _ClassVar[int]
        SKIP_NESTED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
        include_path: str
        exclude_paths: _containers.RepeatedScalarFieldContainer[str]
        skip_nested_volumes: bool
        def __init__(self, include_path: _Optional[str] = ..., exclude_paths: _Optional[_Iterable[str]] = ..., skip_nested_volumes: bool = ...) -> None: ...
    BACKUP_PATH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USES_SKIP_NESTED_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_FOLLOW_NAS_TARGET_FIELD_NUMBER: _ClassVar[int]
    SKIP_NESTED_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_INCLUDE_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    backup_path_info_vec: _containers.RepeatedCompositeFieldContainer[PhysicalFileBackupParams.BackupPathInfo]
    uses_skip_nested_volumes_vec: bool
    symlink_follow_nas_target: bool
    skip_nested_volumes_vec: _containers.RepeatedScalarFieldContainer[str]
    metadata_file_path: str
    global_include_exclude: PhysicalFileBackupParams.GlobalIncludeExclude
    def __init__(self, backup_path_info_vec: _Optional[_Iterable[_Union[PhysicalFileBackupParams.BackupPathInfo, _Mapping]]] = ..., uses_skip_nested_volumes_vec: bool = ..., symlink_follow_nas_target: bool = ..., skip_nested_volumes_vec: _Optional[_Iterable[str]] = ..., metadata_file_path: _Optional[str] = ..., global_include_exclude: _Optional[_Union[PhysicalFileBackupParams.GlobalIncludeExclude, _Mapping]] = ...) -> None: ...

class PhysicalSnapshotParams(_message.Message):
    __slots__ = ("vss_excluded_writers", "vss_copy_only_backup", "fetch_snapshot_metadata_disabled", "notify_backup_complete_disabled")
    VSS_EXCLUDED_WRITERS_FIELD_NUMBER: _ClassVar[int]
    VSS_COPY_ONLY_BACKUP_FIELD_NUMBER: _ClassVar[int]
    FETCH_SNAPSHOT_METADATA_DISABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    vss_excluded_writers: _containers.RepeatedScalarFieldContainer[str]
    vss_copy_only_backup: bool
    fetch_snapshot_metadata_disabled: bool
    notify_backup_complete_disabled: bool
    def __init__(self, vss_excluded_writers: _Optional[_Iterable[str]] = ..., vss_copy_only_backup: bool = ..., fetch_snapshot_metadata_disabled: bool = ..., notify_backup_complete_disabled: bool = ...) -> None: ...

class PhysicalBackupSourceParamsProto(_message.Message):
    __slots__ = ("volume_guid_vec", "file_backup_params", "snapshot_params", "enable_system_backup", "quiesce", "continue_on_quiesce_failure", "perform_source_side_dedup", "perform_brick_based_dedup")
    VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SYSTEM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_QUIESCE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    PERFORM_SOURCE_SIDE_DEDUP_FIELD_NUMBER: _ClassVar[int]
    PERFORM_BRICK_BASED_DEDUP_FIELD_NUMBER: _ClassVar[int]
    volume_guid_vec: _containers.RepeatedScalarFieldContainer[str]
    file_backup_params: PhysicalFileBackupParams
    snapshot_params: PhysicalSnapshotParams
    enable_system_backup: bool
    quiesce: bool
    continue_on_quiesce_failure: bool
    perform_source_side_dedup: bool
    perform_brick_based_dedup: bool
    def __init__(self, volume_guid_vec: _Optional[_Iterable[str]] = ..., file_backup_params: _Optional[_Union[PhysicalFileBackupParams, _Mapping]] = ..., snapshot_params: _Optional[_Union[PhysicalSnapshotParams, _Mapping]] = ..., enable_system_backup: bool = ..., quiesce: bool = ..., continue_on_quiesce_failure: bool = ..., perform_source_side_dedup: bool = ..., perform_brick_based_dedup: bool = ...) -> None: ...
