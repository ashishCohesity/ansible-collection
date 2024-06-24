from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.app_file import app_file_pb2 as _app_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppFileGroupCloneInfo(_message.Message):
    __slots__ = ("source_relative_dir_path", "group_dir_name", "target_relative_group_dir_path")
    SOURCE_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    GROUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_RELATIVE_GROUP_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    source_relative_dir_path: str
    group_dir_name: str
    target_relative_group_dir_path: str
    def __init__(self, source_relative_dir_path: _Optional[str] = ..., group_dir_name: _Optional[str] = ..., target_relative_group_dir_path: _Optional[str] = ...) -> None: ...

class SetupRestoreTaskInfo(_message.Message):
    __slots__ = ("setup_state", "setup_error", "snapshot_files_cloned", "teardown_state", "teardown_error", "app_file_group_info_vec", "app_file_group_clone_info_vec", "mount_point", "delete_app_file_info_vec", "secondary_endpoint_vec")
    class SetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneFiles: _ClassVar[SetupRestoreTaskInfo.SetupState]
        kMountView: _ClassVar[SetupRestoreTaskInfo.SetupState]
        kSetupFinished: _ClassVar[SetupRestoreTaskInfo.SetupState]
        kSetupCancelled: _ClassVar[SetupRestoreTaskInfo.SetupState]
    kCloneFiles: SetupRestoreTaskInfo.SetupState
    kMountView: SetupRestoreTaskInfo.SetupState
    kSetupFinished: SetupRestoreTaskInfo.SetupState
    kSetupCancelled: SetupRestoreTaskInfo.SetupState
    class TeardownState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnmountView: _ClassVar[SetupRestoreTaskInfo.TeardownState]
        kDeleteView: _ClassVar[SetupRestoreTaskInfo.TeardownState]
        kTeardownFinished: _ClassVar[SetupRestoreTaskInfo.TeardownState]
    kUnmountView: SetupRestoreTaskInfo.TeardownState
    kDeleteView: SetupRestoreTaskInfo.TeardownState
    kTeardownFinished: SetupRestoreTaskInfo.TeardownState
    APP_FILE_SETUP_RESTORE_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    app_file_setup_restore_task_info: _descriptor.FieldDescriptor
    SETUP_STATE_FIELD_NUMBER: _ClassVar[int]
    SETUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILES_CLONED_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_STATE_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_FILE_GROUP_CLONE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    DELETE_APP_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_ENDPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    setup_state: SetupRestoreTaskInfo.SetupState
    setup_error: _error_pb2.ErrorProto
    snapshot_files_cloned: bool
    teardown_state: SetupRestoreTaskInfo.TeardownState
    teardown_error: _error_pb2.ErrorProto
    app_file_group_info_vec: _containers.RepeatedCompositeFieldContainer[_app_file_pb2.AppFileGroupInfo]
    app_file_group_clone_info_vec: _containers.RepeatedCompositeFieldContainer[AppFileGroupCloneInfo]
    mount_point: str
    delete_app_file_info_vec: _containers.RepeatedCompositeFieldContainer[DeleteAppFileInfo]
    secondary_endpoint_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, setup_state: _Optional[_Union[SetupRestoreTaskInfo.SetupState, str]] = ..., setup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_files_cloned: bool = ..., teardown_state: _Optional[_Union[SetupRestoreTaskInfo.TeardownState, str]] = ..., teardown_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., app_file_group_info_vec: _Optional[_Iterable[_Union[_app_file_pb2.AppFileGroupInfo, _Mapping]]] = ..., app_file_group_clone_info_vec: _Optional[_Iterable[_Union[AppFileGroupCloneInfo, _Mapping]]] = ..., mount_point: _Optional[str] = ..., delete_app_file_info_vec: _Optional[_Iterable[_Union[DeleteAppFileInfo, _Mapping]]] = ..., secondary_endpoint_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteAppFileInfo(_message.Message):
    __slots__ = ("group_dir_name", "delete_file_vec")
    GROUP_DIR_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    group_dir_name: str
    delete_file_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_dir_name: _Optional[str] = ..., delete_file_vec: _Optional[_Iterable[str]] = ...) -> None: ...
