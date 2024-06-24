from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentSetupRestoreDiskTaskInfo(_message.Message):
    __slots__ = ("setup_state", "setup_error", "teardown_state", "teardown_error", "relative_restore_path_vec_DEPRECATED", "volume_file_info_vec", "mount_info", "file_to_relative_path_map", "snapshot_files_cloned", "full_nas_path", "restore_view_cloned", "agent_ip_address", "target_vm_credentials")
    class SetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSetupStarted: _ClassVar[AgentSetupRestoreDiskTaskInfo.SetupState]
        kCloneFilesCompleted: _ClassVar[AgentSetupRestoreDiskTaskInfo.SetupState]
        kMountedNAS: _ClassVar[AgentSetupRestoreDiskTaskInfo.SetupState]
        kSetupFinished: _ClassVar[AgentSetupRestoreDiskTaskInfo.SetupState]
        kSetupCancelled: _ClassVar[AgentSetupRestoreDiskTaskInfo.SetupState]
    kSetupStarted: AgentSetupRestoreDiskTaskInfo.SetupState
    kCloneFilesCompleted: AgentSetupRestoreDiskTaskInfo.SetupState
    kMountedNAS: AgentSetupRestoreDiskTaskInfo.SetupState
    kSetupFinished: AgentSetupRestoreDiskTaskInfo.SetupState
    kSetupCancelled: AgentSetupRestoreDiskTaskInfo.SetupState
    class TeardownState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kTeardownStarted: _ClassVar[AgentSetupRestoreDiskTaskInfo.TeardownState]
        kUnmountedVirtualDisks: _ClassVar[AgentSetupRestoreDiskTaskInfo.TeardownState]
        kUnmountedNAS: _ClassVar[AgentSetupRestoreDiskTaskInfo.TeardownState]
        kTeardownFinished: _ClassVar[AgentSetupRestoreDiskTaskInfo.TeardownState]
    kTeardownStarted: AgentSetupRestoreDiskTaskInfo.TeardownState
    kUnmountedVirtualDisks: AgentSetupRestoreDiskTaskInfo.TeardownState
    kUnmountedNAS: AgentSetupRestoreDiskTaskInfo.TeardownState
    kTeardownFinished: AgentSetupRestoreDiskTaskInfo.TeardownState
    class MountInfo(_message.Message):
        __slots__ = ("remote_host", "remote_path", "nas_mount_point", "volume_fs_uuid_vec", "volume_guid_vec", "virtual_disk_mount_point_vec", "virtual_disk_path_vec", "remote_host_vec")
        REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
        REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
        NAS_MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        VOLUME_FS_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
        VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_DISK_MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        REMOTE_HOST_VEC_FIELD_NUMBER: _ClassVar[int]
        remote_host: str
        remote_path: str
        nas_mount_point: str
        volume_fs_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
        volume_guid_vec: _containers.RepeatedScalarFieldContainer[str]
        virtual_disk_mount_point_vec: _containers.RepeatedScalarFieldContainer[str]
        virtual_disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
        remote_host_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., nas_mount_point: _Optional[str] = ..., volume_fs_uuid_vec: _Optional[_Iterable[str]] = ..., volume_guid_vec: _Optional[_Iterable[str]] = ..., virtual_disk_mount_point_vec: _Optional[_Iterable[str]] = ..., virtual_disk_path_vec: _Optional[_Iterable[str]] = ..., remote_host_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    class FileToRelativePathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AGENT_SETUP_RESTORE_DISK_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    agent_setup_restore_disk_task_info: _descriptor.FieldDescriptor
    SETUP_STATE_FIELD_NUMBER: _ClassVar[int]
    SETUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_STATE_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_RESTORE_PATH_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_TO_RELATIVE_PATH_MAP_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILES_CLONED_FIELD_NUMBER: _ClassVar[int]
    FULL_NAS_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VIEW_CLONED_FIELD_NUMBER: _ClassVar[int]
    AGENT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    setup_state: AgentSetupRestoreDiskTaskInfo.SetupState
    setup_error: _error_pb2.ErrorProto
    teardown_state: AgentSetupRestoreDiskTaskInfo.TeardownState
    teardown_error: _error_pb2.ErrorProto
    relative_restore_path_vec_DEPRECATED: _containers.RepeatedScalarFieldContainer[str]
    volume_file_info_vec: _containers.RepeatedCompositeFieldContainer[_volume_info_pb2.VolumeInfo]
    mount_info: AgentSetupRestoreDiskTaskInfo.MountInfo
    file_to_relative_path_map: _containers.ScalarMap[str, str]
    snapshot_files_cloned: bool
    full_nas_path: str
    restore_view_cloned: bool
    agent_ip_address: str
    target_vm_credentials: _credentials_pb2.Credentials
    def __init__(self, setup_state: _Optional[_Union[AgentSetupRestoreDiskTaskInfo.SetupState, str]] = ..., setup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., teardown_state: _Optional[_Union[AgentSetupRestoreDiskTaskInfo.TeardownState, str]] = ..., teardown_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., relative_restore_path_vec_DEPRECATED: _Optional[_Iterable[str]] = ..., volume_file_info_vec: _Optional[_Iterable[_Union[_volume_info_pb2.VolumeInfo, _Mapping]]] = ..., mount_info: _Optional[_Union[AgentSetupRestoreDiskTaskInfo.MountInfo, _Mapping]] = ..., file_to_relative_path_map: _Optional[_Mapping[str, str]] = ..., snapshot_files_cloned: bool = ..., full_nas_path: _Optional[str] = ..., restore_view_cloned: bool = ..., agent_ip_address: _Optional[str] = ..., target_vm_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class AgentRestoreFilesInfo(_message.Message):
    __slots__ = ("task_state", "restore_disks_task_info", "error", "tear_down_error")
    class RestoreFilesTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[AgentRestoreFilesInfo.RestoreFilesTaskState]
        kSetupCompleted: _ClassVar[AgentRestoreFilesInfo.RestoreFilesTaskState]
        kCopyFilesInitiated: _ClassVar[AgentRestoreFilesInfo.RestoreFilesTaskState]
        kCopyFilesCompleted: _ClassVar[AgentRestoreFilesInfo.RestoreFilesTaskState]
        kTeardownCompleted: _ClassVar[AgentRestoreFilesInfo.RestoreFilesTaskState]
    kStarted: AgentRestoreFilesInfo.RestoreFilesTaskState
    kSetupCompleted: AgentRestoreFilesInfo.RestoreFilesTaskState
    kCopyFilesInitiated: AgentRestoreFilesInfo.RestoreFilesTaskState
    kCopyFilesCompleted: AgentRestoreFilesInfo.RestoreFilesTaskState
    kTeardownCompleted: AgentRestoreFilesInfo.RestoreFilesTaskState
    AGENT_RESTORE_FILES_INFO_FIELD_NUMBER: _ClassVar[int]
    agent_restore_files_info: _descriptor.FieldDescriptor
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISKS_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEAR_DOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    task_state: AgentRestoreFilesInfo.RestoreFilesTaskState
    restore_disks_task_info: AgentSetupRestoreDiskTaskInfo
    error: _error_pb2.ErrorProto
    tear_down_error: _error_pb2.ErrorProto
    def __init__(self, task_state: _Optional[_Union[AgentRestoreFilesInfo.RestoreFilesTaskState, str]] = ..., restore_disks_task_info: _Optional[_Union[AgentSetupRestoreDiskTaskInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., tear_down_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
