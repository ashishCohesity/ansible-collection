from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import kvm_pb2 as _kvm_pb2
from magneto.connectors.kvm import kvm_pb2 as _kvm_pb2_1
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupKVMVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "vm_config")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupKVMVMArg.Type]
        kSetupFiles: _ClassVar[BackupKVMVMArg.Type]
        kBackupDisk: _ClassVar[BackupKVMVMArg.Type]
        kCloseDisk: _ClassVar[BackupKVMVMArg.Type]
        kEndBackup: _ClassVar[BackupKVMVMArg.Type]
    kPrepareBackup: BackupKVMVMArg.Type
    kSetupFiles: BackupKVMVMArg.Type
    kBackupDisk: BackupKVMVMArg.Type
    kCloseDisk: BackupKVMVMArg.Type
    kEndBackup: BackupKVMVMArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupKVMVMArg.Type
    root_entity: _kvm_pb2.Entity
    vm_entity: _kvm_pb2.Entity
    vm_config: _kvm_pb2_1.VMConfig
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupKVMVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_kvm_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_kvm_pb2.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_kvm_pb2_1.VMConfig, _Mapping]] = ...) -> None: ...

class RestoreVMArg(_message.Message):
    __slots__ = ("base", "type", "vm_restore_info", "view_box_id", "view_name", "create_view", "is_internal_view")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneVMFiles: _ClassVar[RestoreVMArg.Type]
        kRestoreDiskArea: _ClassVar[RestoreVMArg.Type]
        kCloseDisk: _ClassVar[RestoreVMArg.Type]
        kDeleteVMFiles: _ClassVar[RestoreVMArg.Type]
    kCloneVMFiles: RestoreVMArg.Type
    kRestoreDiskArea: RestoreVMArg.Type
    kCloseDisk: RestoreVMArg.Type
    kDeleteVMFiles: RestoreVMArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "vm_entity", "root_entity")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        vm_entity: _kvm_pb2.Entity
        root_entity: _kvm_pb2.Entity
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., vm_entity: _Optional[_Union[_kvm_pb2.Entity, _Mapping]] = ..., root_entity: _Optional[_Union[_kvm_pb2.Entity, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreVMArg.Type
    vm_restore_info: RestoreVMArg.VMRestoreInfo
    view_box_id: int
    view_name: str
    create_view: bool
    is_internal_view: bool
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreVMArg.Type, str]] = ..., vm_restore_info: _Optional[_Union[RestoreVMArg.VMRestoreInfo, _Mapping]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., create_view: bool = ..., is_internal_view: bool = ...) -> None: ...

class KVMActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_kvm_vm_arg", "restore_vm_arg", "cancel_task_arg")
    KVM_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    kvm_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_KVM_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_kvm_vm_arg: BackupKVMVMArg
    restore_vm_arg: RestoreVMArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_kvm_vm_arg: _Optional[_Union[BackupKVMVMArg, _Mapping]] = ..., restore_vm_arg: _Optional[_Union[RestoreVMArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ...) -> None: ...
