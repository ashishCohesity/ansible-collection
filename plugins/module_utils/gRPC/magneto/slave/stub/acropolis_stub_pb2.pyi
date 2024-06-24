from magneto.connectors.acropolis import acropolis_pb2 as _acropolis_pb2
from magneto.slave.stub import stub_pb2 as _stub_pb2
from magneto.base.entities import acropolis_pb2 as _acropolis_pb2_1
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

class ClonedVMEntity(_message.Message):
    __slots__ = ("vm_entity", "vm_config", "relative_cloned_path_vec")
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_CLONED_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_entity: _acropolis_pb2_1.Entity
    vm_config: _acropolis_pb2.VMConfig
    relative_cloned_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vm_entity: _Optional[_Union[_acropolis_pb2_1.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_acropolis_pb2.VMConfig, _Mapping]] = ..., relative_cloned_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CloneVMFilesUpdateArg(_message.Message):
    __slots__ = ("vm_entity", "vm_config", "relative_cloned_path_vec", "cloned_vm_vec")
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_CLONED_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    CLONED_VM_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_entity: _acropolis_pb2_1.Entity
    vm_config: _acropolis_pb2.VMConfig
    relative_cloned_path_vec: _containers.RepeatedScalarFieldContainer[str]
    cloned_vm_vec: _containers.RepeatedCompositeFieldContainer[ClonedVMEntity]
    def __init__(self, vm_entity: _Optional[_Union[_acropolis_pb2_1.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_acropolis_pb2.VMConfig, _Mapping]] = ..., relative_cloned_path_vec: _Optional[_Iterable[str]] = ..., cloned_vm_vec: _Optional[_Iterable[_Union[ClonedVMEntity, _Mapping]]] = ...) -> None: ...

class SetupVMFilesUpdateArg(_message.Message):
    __slots__ = ("virtual_disks_vec",)
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[_acropolis_pb2.VirtualDisk]
    def __init__(self, virtual_disks_vec: _Optional[_Iterable[_Union[_acropolis_pb2.VirtualDisk, _Mapping]]] = ...) -> None: ...

class AcropolisActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_vm_backup_update_arg", "setup_vm_files_update_arg", "backup_disk_update_arg", "clone_vm_update_arg", "restore_disk_area_update_arg", "end_sub_task_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareVMBackupUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
        kCloneVMFilesUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
        kRestoreDiskAreaUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
        kEndSubTaskUpdate: _ClassVar[AcropolisActionUpdateArg.Type]
    kPrepareVMBackupUpdate: AcropolisActionUpdateArg.Type
    kSetupVMFilesUpdate: AcropolisActionUpdateArg.Type
    kBackupVMDiskUpdate: AcropolisActionUpdateArg.Type
    kEndVMBackupUpdate: AcropolisActionUpdateArg.Type
    kCloneVMFilesUpdate: AcropolisActionUpdateArg.Type
    kRestoreDiskAreaUpdate: AcropolisActionUpdateArg.Type
    kEndSubTaskUpdate: AcropolisActionUpdateArg.Type
    ACROPOLIS_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    acropolis_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_VM_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_VM_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DISK_AREA_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    END_SUB_TASK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: AcropolisActionUpdateArg.Type
    prepare_vm_backup_update_arg: PrepareVMBackupUpdateArg
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    clone_vm_update_arg: CloneVMFilesUpdateArg
    restore_disk_area_update_arg: _stub_pb2.RestoreDiskUpdateArg
    end_sub_task_update_arg: _stub_pb2.EndSubTaskUpdateArg
    def __init__(self, type: _Optional[_Union[AcropolisActionUpdateArg.Type, str]] = ..., prepare_vm_backup_update_arg: _Optional[_Union[PrepareVMBackupUpdateArg, _Mapping]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., clone_vm_update_arg: _Optional[_Union[CloneVMFilesUpdateArg, _Mapping]] = ..., restore_disk_area_update_arg: _Optional[_Union[_stub_pb2.RestoreDiskUpdateArg, _Mapping]] = ..., end_sub_task_update_arg: _Optional[_Union[_stub_pb2.EndSubTaskUpdateArg, _Mapping]] = ...) -> None: ...
