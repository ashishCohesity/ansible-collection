from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.app_file import app_file_setup_restore_pb2 as _app_file_setup_restore_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareBackupUpdateArg(_message.Message):
    __slots__ = ("root_path", "relative_snapshot_dir")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...

class SetupFilesUpdateArg(_message.Message):
    __slots__ = ("is_common_host_dir_cloned_under_app_file_groups",)
    IS_COMMON_HOST_DIR_CLONED_UNDER_APP_FILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    is_common_host_dir_cloned_under_app_file_groups: bool
    def __init__(self, is_common_host_dir_cloned_under_app_file_groups: bool = ...) -> None: ...

class AppFileStartRestoreTaskArg(_message.Message):
    __slots__ = ()
    APP_FILE_START_RESTORE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    app_file_start_restore_task_arg: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class CloneAppFilesUpdateArg(_message.Message):
    __slots__ = ("cloned_app_file_group_vec", "app_file_group_clone_info_vec")
    class ClonedAppFileGroup(_message.Message):
        __slots__ = ("group_dir_name", "relative_cloned_file_paths")
        GROUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONED_FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
        group_dir_name: str
        relative_cloned_file_paths: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, group_dir_name: _Optional[str] = ..., relative_cloned_file_paths: _Optional[_Iterable[str]] = ...) -> None: ...
    CLONED_APP_FILE_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_CLONE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    cloned_app_file_group_vec: _containers.RepeatedCompositeFieldContainer[CloneAppFilesUpdateArg.ClonedAppFileGroup]
    app_file_group_clone_info_vec: _containers.RepeatedCompositeFieldContainer[_app_file_setup_restore_pb2.AppFileGroupCloneInfo]
    def __init__(self, cloned_app_file_group_vec: _Optional[_Iterable[_Union[CloneAppFilesUpdateArg.ClonedAppFileGroup, _Mapping]]] = ..., app_file_group_clone_info_vec: _Optional[_Iterable[_Union[_app_file_setup_restore_pb2.AppFileGroupCloneInfo, _Mapping]]] = ...) -> None: ...

class AppFileActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_backup_update_arg", "setup_files_update_arg", "backup_file_update_arg", "clone_app_files_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackupUpdate: _ClassVar[AppFileActionUpdateArg.Type]
        kSetupFilesUpdate: _ClassVar[AppFileActionUpdateArg.Type]
        kBackupFileUpdate: _ClassVar[AppFileActionUpdateArg.Type]
        kCloseFileUpdate: _ClassVar[AppFileActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[AppFileActionUpdateArg.Type]
        kCloneAppFilesUpdate: _ClassVar[AppFileActionUpdateArg.Type]
    kPrepareBackupUpdate: AppFileActionUpdateArg.Type
    kSetupFilesUpdate: AppFileActionUpdateArg.Type
    kBackupFileUpdate: AppFileActionUpdateArg.Type
    kCloseFileUpdate: AppFileActionUpdateArg.Type
    kEndBackupUpdate: AppFileActionUpdateArg.Type
    kCloneAppFilesUpdate: AppFileActionUpdateArg.Type
    APP_FILE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    app_file_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_APP_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: AppFileActionUpdateArg.Type
    prepare_backup_update_arg: PrepareBackupUpdateArg
    setup_files_update_arg: SetupFilesUpdateArg
    backup_file_update_arg: _stub_pb2.BackupDiskUpdateArg
    clone_app_files_update_arg: CloneAppFilesUpdateArg
    def __init__(self, type: _Optional[_Union[AppFileActionUpdateArg.Type, str]] = ..., prepare_backup_update_arg: _Optional[_Union[PrepareBackupUpdateArg, _Mapping]] = ..., setup_files_update_arg: _Optional[_Union[SetupFilesUpdateArg, _Mapping]] = ..., backup_file_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., clone_app_files_update_arg: _Optional[_Union[CloneAppFilesUpdateArg, _Mapping]] = ...) -> None: ...
