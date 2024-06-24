from magneto.master.base import master_pb2 as _master_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupWorkUnitsUpdateArg(_message.Message):
    __slots__ = ("backup_update_vec",)
    BACKUP_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_update_vec: _containers.RepeatedCompositeFieldContainer[_stub_pb2.BackupDiskUpdateArg]
    def __init__(self, backup_update_vec: _Optional[_Iterable[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]]] = ...) -> None: ...

class RestoreWorkUnitsUpdateArg(_message.Message):
    __slots__ = ("restore_update_vec",)
    RESTORE_UPDATE_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_update_vec: _containers.RepeatedCompositeFieldContainer[_stub_pb2.RestoreDiskUpdateArg]
    def __init__(self, restore_update_vec: _Optional[_Iterable[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]]] = ...) -> None: ...

class FileActionUpdateArg(_message.Message):
    __slots__ = ("type", "backup_work_units_update_arg", "restore_work_units_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackupUpdate: _ClassVar[FileActionUpdateArg.Type]
        kBackupWorkUnitsUpdate: _ClassVar[FileActionUpdateArg.Type]
        kEndBackupSubTaskUpdate: _ClassVar[FileActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[FileActionUpdateArg.Type]
        kRestoreWorkUnitsUpdate: _ClassVar[FileActionUpdateArg.Type]
        kEndRestoreSubTaskUpdate: _ClassVar[FileActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[FileActionUpdateArg.Type]
    kPrepareBackupUpdate: FileActionUpdateArg.Type
    kBackupWorkUnitsUpdate: FileActionUpdateArg.Type
    kEndBackupSubTaskUpdate: FileActionUpdateArg.Type
    kEndBackupUpdate: FileActionUpdateArg.Type
    kRestoreWorkUnitsUpdate: FileActionUpdateArg.Type
    kEndRestoreSubTaskUpdate: FileActionUpdateArg.Type
    kEndRestoreUpdate: FileActionUpdateArg.Type
    FILE_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    file_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WORK_UNITS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_WORK_UNITS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: FileActionUpdateArg.Type
    backup_work_units_update_arg: BackupWorkUnitsUpdateArg
    restore_work_units_update_arg: RestoreWorkUnitsUpdateArg
    def __init__(self, type: _Optional[_Union[FileActionUpdateArg.Type, str]] = ..., backup_work_units_update_arg: _Optional[_Union[BackupWorkUnitsUpdateArg, _Mapping]] = ..., restore_work_units_update_arg: _Optional[_Union[RestoreWorkUnitsUpdateArg, _Mapping]] = ...) -> None: ...

class FileStartRestoreTaskArg(_message.Message):
    __slots__ = ("mount_volume", "view_params")
    FILE_START_RESTORE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    file_start_restore_task_arg: _descriptor.FieldDescriptor
    MOUNT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    mount_volume: bool
    view_params: _master_pb2.ViewParams
    def __init__(self, mount_volume: bool = ..., view_params: _Optional[_Union[_master_pb2.ViewParams, _Mapping]] = ...) -> None: ...
