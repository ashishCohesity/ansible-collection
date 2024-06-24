from magneto.base.entities import physical_pb2 as _physical_pb2
from magneto.base import physical_pb2 as _physical_pb2_1
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareBackupUpdateArg(_message.Message):
    __slots__ = ("root_path", "relative_snapshot_dir", "ancillary_view_name")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    ANCILLARY_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    relative_snapshot_dir: str
    ancillary_view_name: str
    def __init__(self, root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ..., ancillary_view_name: _Optional[str] = ...) -> None: ...

class SetupFilesUpdateArg(_message.Message):
    __slots__ = ("virtual_disks", "virtual_disk_filepaths_to_be_deleted", "root_path", "relative_snapshot_dir")
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_FILEPATHS_TO_BE_DELETED_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    virtual_disks: _containers.RepeatedCompositeFieldContainer[_physical_pb2_1.VirtualDisk]
    virtual_disk_filepaths_to_be_deleted: _containers.RepeatedScalarFieldContainer[str]
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, virtual_disks: _Optional[_Iterable[_Union[_physical_pb2_1.VirtualDisk, _Mapping]]] = ..., virtual_disk_filepaths_to_be_deleted: _Optional[_Iterable[str]] = ..., root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...

class CloneHostsUpdateArg(_message.Message):
    __slots__ = ("cloned_hosts",)
    class ClonedHost(_message.Message):
        __slots__ = ("entity", "sparse_host_config", "relative_cloned_paths")
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        SPARSE_HOST_CONFIG_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONED_PATHS_FIELD_NUMBER: _ClassVar[int]
        entity: _physical_pb2.Entity
        sparse_host_config: _physical_pb2_1.SparseHostConfig
        relative_cloned_paths: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, entity: _Optional[_Union[_physical_pb2.Entity, _Mapping]] = ..., sparse_host_config: _Optional[_Union[_physical_pb2_1.SparseHostConfig, _Mapping]] = ..., relative_cloned_paths: _Optional[_Iterable[str]] = ...) -> None: ...
    CLONED_HOSTS_FIELD_NUMBER: _ClassVar[int]
    cloned_hosts: _containers.RepeatedCompositeFieldContainer[CloneHostsUpdateArg.ClonedHost]
    def __init__(self, cloned_hosts: _Optional[_Iterable[_Union[CloneHostsUpdateArg.ClonedHost, _Mapping]]] = ...) -> None: ...

class ActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_backup_update_arg", "backup_disk_update_arg", "setup_files_update_arg", "clone_hosts_update_arg", "restore_disk_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackupUpdate: _ClassVar[ActionUpdateArg.Type]
        kSetupFilesUpdate: _ClassVar[ActionUpdateArg.Type]
        kBackupDiskUpdate: _ClassVar[ActionUpdateArg.Type]
        kCloseDiskUpdate: _ClassVar[ActionUpdateArg.Type]
        kEndBackupUpdate: _ClassVar[ActionUpdateArg.Type]
        kCloneHostsUpdate: _ClassVar[ActionUpdateArg.Type]
        kDeleteClonedHostsUpdate: _ClassVar[ActionUpdateArg.Type]
        kRestoreDiskUpdate: _ClassVar[ActionUpdateArg.Type]
    kPrepareBackupUpdate: ActionUpdateArg.Type
    kSetupFilesUpdate: ActionUpdateArg.Type
    kBackupDiskUpdate: ActionUpdateArg.Type
    kCloseDiskUpdate: ActionUpdateArg.Type
    kEndBackupUpdate: ActionUpdateArg.Type
    kCloneHostsUpdate: ActionUpdateArg.Type
    kDeleteClonedHostsUpdate: ActionUpdateArg.Type
    kRestoreDiskUpdate: ActionUpdateArg.Type
    PHYSICAL_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    physical_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_HOSTS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: ActionUpdateArg.Type
    prepare_backup_update_arg: PrepareBackupUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    setup_files_update_arg: SetupFilesUpdateArg
    clone_hosts_update_arg: CloneHostsUpdateArg
    restore_disk_update_arg: _stub_pb2.RestoreDiskUpdateArg
    def __init__(self, type: _Optional[_Union[ActionUpdateArg.Type, str]] = ..., prepare_backup_update_arg: _Optional[_Union[PrepareBackupUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., setup_files_update_arg: _Optional[_Union[SetupFilesUpdateArg, _Mapping]] = ..., clone_hosts_update_arg: _Optional[_Union[CloneHostsUpdateArg, _Mapping]] = ..., restore_disk_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ...) -> None: ...
