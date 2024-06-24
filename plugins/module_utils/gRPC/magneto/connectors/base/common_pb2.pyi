from magneto.agents.windows.base import file_attrs_pb2 as _file_attrs_pb2
from magneto.utils.file_sync import file_sync_pb2 as _file_sync_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyChangedAreasTaskInfo(_message.Message):
    __slots__ = ("file_sync_task_info_vec", "progress_monitor_created")
    class FileSyncTaskInfo(_message.Message):
        __slots__ = ("uuid", "task_state", "target_host_mounted_file_path", "target_host_local_file_path")
        UUID_FIELD_NUMBER: _ClassVar[int]
        TASK_STATE_FIELD_NUMBER: _ClassVar[int]
        TARGET_HOST_MOUNTED_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        TARGET_HOST_LOCAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        task_state: _file_sync_pb2.TaskState
        target_host_mounted_file_path: str
        target_host_local_file_path: str
        def __init__(self, uuid: _Optional[str] = ..., task_state: _Optional[_Union[_file_sync_pb2.TaskState, _Mapping]] = ..., target_host_mounted_file_path: _Optional[str] = ..., target_host_local_file_path: _Optional[str] = ...) -> None: ...
    FILE_SYNC_TASK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MONITOR_CREATED_FIELD_NUMBER: _ClassVar[int]
    file_sync_task_info_vec: _containers.RepeatedCompositeFieldContainer[ApplyChangedAreasTaskInfo.FileSyncTaskInfo]
    progress_monitor_created: bool
    def __init__(self, file_sync_task_info_vec: _Optional[_Iterable[_Union[ApplyChangedAreasTaskInfo.FileSyncTaskInfo, _Mapping]]] = ..., progress_monitor_created: bool = ...) -> None: ...

class VSSSnapshotDbFileInfo(_message.Message):
    __slots__ = ("uuid", "host_full_filepath", "snapshot_device_filepath", "capacity", "file_attributes")
    UUID_FIELD_NUMBER: _ClassVar[int]
    HOST_FULL_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEVICE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FILE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    host_full_filepath: str
    snapshot_device_filepath: str
    capacity: int
    file_attributes: _file_attrs_pb2.FileAttributes
    def __init__(self, uuid: _Optional[str] = ..., host_full_filepath: _Optional[str] = ..., snapshot_device_filepath: _Optional[str] = ..., capacity: _Optional[int] = ..., file_attributes: _Optional[_Union[_file_attrs_pb2.FileAttributes, _Mapping]] = ...) -> None: ...
