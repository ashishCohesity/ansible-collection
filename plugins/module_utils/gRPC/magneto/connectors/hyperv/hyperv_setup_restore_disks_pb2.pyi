from magneto.agents.base import agent_pb2 as _agent_pb2
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

class SetupRestoreDiskTaskInfo(_message.Message):
    __slots__ = ("setup_state", "setup_error", "teardown_state", "teardown_error", "cloned_disk_info_vec", "hyperv_host_name_vec", "nas_mount_point", "attached_disk_map", "existing_volume_info_vec", "attached_volume_info_vec", "volume_file_info_vec", "guest_vm_temp_dir", "guest_vm_agent_path")
    class SetupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneVMFiles: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kMountDatastore: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kAttachDisks: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kCopyAgentToGuest: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kBringDisksOnline: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kSetupFinished: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
        kSetupCancelled: _ClassVar[SetupRestoreDiskTaskInfo.SetupState]
    kCloneVMFiles: SetupRestoreDiskTaskInfo.SetupState
    kMountDatastore: SetupRestoreDiskTaskInfo.SetupState
    kAttachDisks: SetupRestoreDiskTaskInfo.SetupState
    kCopyAgentToGuest: SetupRestoreDiskTaskInfo.SetupState
    kBringDisksOnline: SetupRestoreDiskTaskInfo.SetupState
    kSetupFinished: SetupRestoreDiskTaskInfo.SetupState
    kSetupCancelled: SetupRestoreDiskTaskInfo.SetupState
    class TeardownState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDetachDisks: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
        kUnmountDatastore: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
        kDeleteView: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
        kTeardownFinished: _ClassVar[SetupRestoreDiskTaskInfo.TeardownState]
    kDetachDisks: SetupRestoreDiskTaskInfo.TeardownState
    kUnmountDatastore: SetupRestoreDiskTaskInfo.TeardownState
    kDeleteView: SetupRestoreDiskTaskInfo.TeardownState
    kTeardownFinished: SetupRestoreDiskTaskInfo.TeardownState
    class ClonedDiskInfo(_message.Message):
        __slots__ = ("uuid", "parent_disk_uuid", "relative_disk_file_path", "encoded_disk_filename", "original_disk_file_path", "original_parent_disk_file_path")
        UUID_FIELD_NUMBER: _ClassVar[int]
        PARENT_DISK_UUID_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_DISK_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ENCODED_DISK_FILENAME_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_DISK_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_PARENT_DISK_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        parent_disk_uuid: str
        relative_disk_file_path: str
        encoded_disk_filename: str
        original_disk_file_path: str
        original_parent_disk_file_path: str
        def __init__(self, uuid: _Optional[str] = ..., parent_disk_uuid: _Optional[str] = ..., relative_disk_file_path: _Optional[str] = ..., encoded_disk_filename: _Optional[str] = ..., original_disk_file_path: _Optional[str] = ..., original_parent_disk_file_path: _Optional[str] = ...) -> None: ...
    class AttachedDiskInfo(_message.Message):
        __slots__ = ("disk_id", "disk_path", "controller_location", "controller_number")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_PATH_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_LOCATION_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_NUMBER_FIELD_NUMBER: _ClassVar[int]
        disk_id: bytes
        disk_path: str
        controller_location: int
        controller_number: int
        def __init__(self, disk_id: _Optional[bytes] = ..., disk_path: _Optional[str] = ..., controller_location: _Optional[int] = ..., controller_number: _Optional[int] = ...) -> None: ...
    class AttachedDiskMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SetupRestoreDiskTaskInfo.AttachedDiskInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SetupRestoreDiskTaskInfo.AttachedDiskInfo, _Mapping]] = ...) -> None: ...
    HYPERV_SETUP_RESTORE_DISK_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    hyperv_setup_restore_disk_task_info: _descriptor.FieldDescriptor
    SETUP_STATE_FIELD_NUMBER: _ClassVar[int]
    SETUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_STATE_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    CLONED_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    HYPERV_HOST_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    NAS_MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_DISK_MAP_FIELD_NUMBER: _ClassVar[int]
    EXISTING_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    GUEST_VM_TEMP_DIR_FIELD_NUMBER: _ClassVar[int]
    GUEST_VM_AGENT_PATH_FIELD_NUMBER: _ClassVar[int]
    setup_state: SetupRestoreDiskTaskInfo.SetupState
    setup_error: _error_pb2.ErrorProto
    teardown_state: SetupRestoreDiskTaskInfo.TeardownState
    teardown_error: _error_pb2.ErrorProto
    cloned_disk_info_vec: _containers.RepeatedCompositeFieldContainer[SetupRestoreDiskTaskInfo.ClonedDiskInfo]
    hyperv_host_name_vec: _containers.RepeatedScalarFieldContainer[str]
    nas_mount_point: str
    attached_disk_map: _containers.MessageMap[str, SetupRestoreDiskTaskInfo.AttachedDiskInfo]
    existing_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    attached_volume_info_vec: _containers.RepeatedCompositeFieldContainer[_agent_pb2.VolumeInfoProto]
    volume_file_info_vec: _containers.RepeatedCompositeFieldContainer[_volume_info_pb2.VolumeInfo]
    guest_vm_temp_dir: str
    guest_vm_agent_path: str
    def __init__(self, setup_state: _Optional[_Union[SetupRestoreDiskTaskInfo.SetupState, str]] = ..., setup_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., teardown_state: _Optional[_Union[SetupRestoreDiskTaskInfo.TeardownState, str]] = ..., teardown_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cloned_disk_info_vec: _Optional[_Iterable[_Union[SetupRestoreDiskTaskInfo.ClonedDiskInfo, _Mapping]]] = ..., hyperv_host_name_vec: _Optional[_Iterable[str]] = ..., nas_mount_point: _Optional[str] = ..., attached_disk_map: _Optional[_Mapping[str, SetupRestoreDiskTaskInfo.AttachedDiskInfo]] = ..., existing_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ..., attached_volume_info_vec: _Optional[_Iterable[_Union[_agent_pb2.VolumeInfoProto, _Mapping]]] = ..., volume_file_info_vec: _Optional[_Iterable[_Union[_volume_info_pb2.VolumeInfo, _Mapping]]] = ..., guest_vm_temp_dir: _Optional[str] = ..., guest_vm_agent_path: _Optional[str] = ...) -> None: ...
