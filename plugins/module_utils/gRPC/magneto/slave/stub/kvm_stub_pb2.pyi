from magneto.base.entities import kvm_pb2 as _kvm_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.kvm import kvm_pb2 as _kvm_pb2_1
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrepareVMBackupUpdateArg(_message.Message):
    __slots__ = ("root_path", "relative_snapshot_dir")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    relative_snapshot_dir: str
    def __init__(self, root_path: _Optional[str] = ..., relative_snapshot_dir: _Optional[str] = ...) -> None: ...

class SetupVMFilesUpdateArg(_message.Message):
    __slots__ = ("virtual_disks_vec",)
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[_kvm_pb2_1.VirtualDisk]
    def __init__(self, virtual_disks_vec: _Optional[_Iterable[_Union[_kvm_pb2_1.VirtualDisk, _Mapping]]] = ...) -> None: ...

class CloneVMFilesUpdateArg(_message.Message):
    __slots__ = ("vm_entity", "vm_config", "relative_cloned_path_vec")
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_CLONED_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_entity: _kvm_pb2.Entity
    vm_config: _kvm_pb2_1.VMConfig
    relative_cloned_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vm_entity: _Optional[_Union[_kvm_pb2.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_kvm_pb2_1.VMConfig, _Mapping]] = ..., relative_cloned_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class KVMActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_vm_backup_update_arg", "setup_vm_files_update_arg", "backup_disk_update_arg", "clone_vm_update_arg", "restore_disk_area_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareVMBackupUpdate: _ClassVar[KVMActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[KVMActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[KVMActionUpdateArg.Type]
        kCloseVMDiskUpdate: _ClassVar[KVMActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[KVMActionUpdateArg.Type]
        kCloneVMFilesUpdate: _ClassVar[KVMActionUpdateArg.Type]
        kRestoreDiskAreaUpdate: _ClassVar[KVMActionUpdateArg.Type]
    kPrepareVMBackupUpdate: KVMActionUpdateArg.Type
    kSetupVMFilesUpdate: KVMActionUpdateArg.Type
    kBackupVMDiskUpdate: KVMActionUpdateArg.Type
    kCloseVMDiskUpdate: KVMActionUpdateArg.Type
    kEndVMBackupUpdate: KVMActionUpdateArg.Type
    kCloneVMFilesUpdate: KVMActionUpdateArg.Type
    kRestoreDiskAreaUpdate: KVMActionUpdateArg.Type
    KVM_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    kvm_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_VM_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_VM_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_AREA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: KVMActionUpdateArg.Type
    prepare_vm_backup_update_arg: PrepareVMBackupUpdateArg
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    clone_vm_update_arg: CloneVMFilesUpdateArg
    restore_disk_area_update_arg: _stub_pb2.RestoreDiskUpdateArg
    def __init__(self, type: _Optional[_Union[KVMActionUpdateArg.Type, str]] = ..., prepare_vm_backup_update_arg: _Optional[_Union[PrepareVMBackupUpdateArg, _Mapping]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., clone_vm_update_arg: _Optional[_Union[CloneVMFilesUpdateArg, _Mapping]] = ..., restore_disk_area_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ...) -> None: ...
