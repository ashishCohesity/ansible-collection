from magneto.base import disk_pb2 as _disk_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetupFilesUpdateArg(_message.Message):
    __slots__ = ("root_path", "relative_snapshot_dir")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...

class FetchDiskInfoUpdateArg(_message.Message):
    __slots__ = ("disk", "disk_area_list")
    DISK_FIELD_NUMBER: _ClassVar[int]
    DISK_AREA_LIST_FIELD_NUMBER: _ClassVar[int]
    disk: _disk_pb2.DiskProto
    disk_area_list: _disk_pb2.DiskAreaListProto
    def __init__(self, disk: _Optional[_Union[_disk_pb2.DiskProto, _Mapping]] = ..., disk_area_list: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ...) -> None: ...

class SanActionUpdateArg(_message.Message):
    __slots__ = ("type", "setup_files_update_arg", "backup_disk_area_update_arg", "restore_disk_area_update_arg", "fetch_disk_info_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackupUpdate: _ClassVar[SanActionUpdateArg.Type]
        kSetupFilesUpdate: _ClassVar[SanActionUpdateArg.Type]
        kBackupDiskAreaUpdate: _ClassVar[SanActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[SanActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[SanActionUpdateArg.Type]
        kCloneFilesUpdate: _ClassVar[SanActionUpdateArg.Type]
        kFetchDiskInfoUpdate: _ClassVar[SanActionUpdateArg.Type]
        kRestoreDiskAreaUpdate: _ClassVar[SanActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[SanActionUpdateArg.Type]
    kPrepareBackupUpdate: SanActionUpdateArg.Type
    kSetupFilesUpdate: SanActionUpdateArg.Type
    kBackupDiskAreaUpdate: SanActionUpdateArg.Type
    kEndSubTaskUpdate: SanActionUpdateArg.Type
    kEndBackupUpdate: SanActionUpdateArg.Type
    kCloneFilesUpdate: SanActionUpdateArg.Type
    kFetchDiskInfoUpdate: SanActionUpdateArg.Type
    kRestoreDiskAreaUpdate: SanActionUpdateArg.Type
    kEndRestoreUpdate: SanActionUpdateArg.Type
    SAN_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    san_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SETUP_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_AREA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_AREA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_DISK_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: SanActionUpdateArg.Type
    setup_files_update_arg: SetupFilesUpdateArg
    backup_disk_area_update_arg: _stub_pb2.BackupDiskUpdateArg
    restore_disk_area_update_arg: _stub_pb2.RestoreDiskUpdateArg
    fetch_disk_info_update_arg: FetchDiskInfoUpdateArg
    def __init__(self, type: _Optional[_Union[SanActionUpdateArg.Type, str]] = ..., setup_files_update_arg: _Optional[_Union[SetupFilesUpdateArg, _Mapping]] = ..., backup_disk_area_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., restore_disk_area_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., fetch_disk_info_update_arg: _Optional[_Union[FetchDiskInfoUpdateArg, _Mapping]] = ...) -> None: ...
