from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.connectors.gcp import gcp_pb2 as _gcp_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetupVMFilesUpdateArg(_message.Message):
    __slots__ = ("persistent_disks_vec",)
    PERSISTENT_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    persistent_disks_vec: _containers.RepeatedCompositeFieldContainer[_gcp_pb2.PersistentDisk]
    def __init__(self, persistent_disks_vec: _Optional[_Iterable[_Union[_gcp_pb2.PersistentDisk, _Mapping]]] = ...) -> None: ...

class EndVMBackupUpdateArg(_message.Message):
    __slots__ = ("closed_persistent_disks_vec",)
    CLOSED_PERSISTENT_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    closed_persistent_disks_vec: _containers.RepeatedCompositeFieldContainer[_gcp_pb2.PersistentDisk]
    def __init__(self, closed_persistent_disks_vec: _Optional[_Iterable[_Union[_gcp_pb2.PersistentDisk, _Mapping]]] = ...) -> None: ...

class EndVMRestoreUpdateArg(_message.Message):
    __slots__ = ("closed_persistent_disks_vec",)
    CLOSED_PERSISTENT_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    closed_persistent_disks_vec: _containers.RepeatedCompositeFieldContainer[_gcp_pb2.PersistentDisk]
    def __init__(self, closed_persistent_disks_vec: _Optional[_Iterable[_Union[_gcp_pb2.PersistentDisk, _Mapping]]] = ...) -> None: ...

class GCPActionUpdateArg(_message.Message):
    __slots__ = ("type", "setup_vm_files_update_arg", "backup_disk_update_arg", "end_vm_backup_update_arg", "restore_disk_update_arg", "end_vm_restore_update_arg", "vm_config")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareVMBackupUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kCreateDisksUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kCopyDiskAreaUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kEndRestoreUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kDeleteGCPEntitiesUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kDownloadDiskPortionUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kConvertDiskUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kCopyVolumeDataUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kFetchVMInfoUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kRestoreVMDiskUpdate: _ClassVar[GCPActionUpdateArg.Type]
        kEndVMRestoreUpdate: _ClassVar[GCPActionUpdateArg.Type]
    kPrepareVMBackupUpdate: GCPActionUpdateArg.Type
    kSetupVMFilesUpdate: GCPActionUpdateArg.Type
    kCreateDisksUpdate: GCPActionUpdateArg.Type
    kCopyDiskAreaUpdate: GCPActionUpdateArg.Type
    kEndRestoreUpdate: GCPActionUpdateArg.Type
    kDeleteGCPEntitiesUpdate: GCPActionUpdateArg.Type
    kDownloadDiskPortionUpdate: GCPActionUpdateArg.Type
    kConvertDiskUpdate: GCPActionUpdateArg.Type
    kCopyVolumeDataUpdate: GCPActionUpdateArg.Type
    kBackupVMDiskUpdate: GCPActionUpdateArg.Type
    kEndSubTaskUpdate: GCPActionUpdateArg.Type
    kFetchVMInfoUpdate: GCPActionUpdateArg.Type
    kEndVMBackupUpdate: GCPActionUpdateArg.Type
    kRestoreVMDiskUpdate: GCPActionUpdateArg.Type
    kEndVMRestoreUpdate: GCPActionUpdateArg.Type
    GCP_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    gcp_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_VM_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_VM_RESTORE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    type: GCPActionUpdateArg.Type
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    end_vm_backup_update_arg: EndVMBackupUpdateArg
    restore_disk_update_arg: _stub_pb2.RestoreDiskUpdateArg
    end_vm_restore_update_arg: EndVMRestoreUpdateArg
    vm_config: _gcp_pb2.VMConfig
    def __init__(self, type: _Optional[_Union[GCPActionUpdateArg.Type, str]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., end_vm_backup_update_arg: _Optional[_Union[EndVMBackupUpdateArg, _Mapping]] = ..., restore_disk_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., end_vm_restore_update_arg: _Optional[_Union[EndVMRestoreUpdateArg, _Mapping]] = ..., vm_config: _Optional[_Union[_gcp_pb2.VMConfig, _Mapping]] = ...) -> None: ...
