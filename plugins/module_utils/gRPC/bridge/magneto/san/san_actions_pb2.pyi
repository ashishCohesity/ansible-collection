from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupSanArg(_message.Message):
    __slots__ = ("base", "type", "source_disk", "disk_area_list", "sub_file_size_mb")
    Extensions: _python_message._ExtensionDict
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupSanArg.ActionType]
        kSetupFiles: _ClassVar[BackupSanArg.ActionType]
        kBackupDiskArea: _ClassVar[BackupSanArg.ActionType]
        kEndSubTask: _ClassVar[BackupSanArg.ActionType]
        kEndBackup: _ClassVar[BackupSanArg.ActionType]
    kPrepareBackup: BackupSanArg.ActionType
    kSetupFiles: BackupSanArg.ActionType
    kBackupDiskArea: BackupSanArg.ActionType
    kEndSubTask: BackupSanArg.ActionType
    kEndBackup: BackupSanArg.ActionType
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DISK_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_LIST_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupSanArg.ActionType
    source_disk: _disk_pb2.DiskProto
    disk_area_list: _disk_pb2.DiskAreaListProto
    sub_file_size_mb: int
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupSanArg.ActionType, str]] = ..., source_disk: _Optional[_Union[_disk_pb2.DiskProto, _Mapping]] = ..., disk_area_list: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ..., sub_file_size_mb: _Optional[int] = ...) -> None: ...

class RestoreSanArg(_message.Message):
    __slots__ = ("type", "source_view_name", "view_box_id", "view_name", "snapshot_relative_dir_path", "changed_areas_relative_dir_path_vec", "target_disk", "connector_params", "area")
    Extensions: _python_message._ExtensionDict
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneFiles: _ClassVar[RestoreSanArg.ActionType]
        kFetchDiskInfo: _ClassVar[RestoreSanArg.ActionType]
        kRestoreDiskArea: _ClassVar[RestoreSanArg.ActionType]
        kEndSubTask: _ClassVar[RestoreSanArg.ActionType]
        kEndRestore: _ClassVar[RestoreSanArg.ActionType]
    kCloneFiles: RestoreSanArg.ActionType
    kFetchDiskInfo: RestoreSanArg.ActionType
    kRestoreDiskArea: RestoreSanArg.ActionType
    kEndSubTask: RestoreSanArg.ActionType
    kEndRestore: RestoreSanArg.ActionType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    CHANGED_AREAS_RELATIVE_DIR_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    TARGET_DISK_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    type: RestoreSanArg.ActionType
    source_view_name: str
    view_box_id: int
    view_name: str
    snapshot_relative_dir_path: str
    changed_areas_relative_dir_path_vec: _containers.RepeatedScalarFieldContainer[str]
    target_disk: _disk_pb2.DiskProto
    connector_params: _magneto_pb2.ConnectorParams
    area: _disk_pb2.DiskAreaProto
    def __init__(self, type: _Optional[_Union[RestoreSanArg.ActionType, str]] = ..., source_view_name: _Optional[str] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., changed_areas_relative_dir_path_vec: _Optional[_Iterable[str]] = ..., target_disk: _Optional[_Union[_disk_pb2.DiskProto, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ..., area: _Optional[_Union[_disk_pb2.DiskAreaProto, _Mapping]] = ...) -> None: ...

class SanActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_san_arg", "restore_san_arg")
    SAN_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    san_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SAN_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_SAN_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_san_arg: BackupSanArg
    restore_san_arg: RestoreSanArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_san_arg: _Optional[_Union[BackupSanArg, _Mapping]] = ..., restore_san_arg: _Optional[_Union[RestoreSanArg, _Mapping]] = ...) -> None: ...

class GroupActionArg(_message.Message):
    __slots__ = ("source_disks", "volume_arg_vec")
    Extensions: _python_message._ExtensionDict
    class VolumeActionArg(_message.Message):
        __slots__ = ("volume_action_arg",)
        VOLUME_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
        volume_action_arg: _magneto_actions_pb2.ExecuteActionArg
        def __init__(self, volume_action_arg: _Optional[_Union[_magneto_actions_pb2.ExecuteActionArg, _Mapping]] = ...) -> None: ...
    GROUP_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    group_action_arg: _descriptor.FieldDescriptor
    SOURCE_DISKS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ARG_VEC_FIELD_NUMBER: _ClassVar[int]
    source_disks: _containers.RepeatedCompositeFieldContainer[_disk_pb2.DiskProto]
    volume_arg_vec: _containers.RepeatedCompositeFieldContainer[GroupActionArg.VolumeActionArg]
    def __init__(self, source_disks: _Optional[_Iterable[_Union[_disk_pb2.DiskProto, _Mapping]]] = ..., volume_arg_vec: _Optional[_Iterable[_Union[GroupActionArg.VolumeActionArg, _Mapping]]] = ...) -> None: ...
