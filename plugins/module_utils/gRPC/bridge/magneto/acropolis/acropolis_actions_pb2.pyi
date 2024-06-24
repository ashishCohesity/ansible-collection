from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import acropolis_pb2 as _acropolis_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import san_pb2 as _san_pb2
from magneto.connectors.acropolis import acropolis_pb2 as _acropolis_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupAcropolisVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "san_port_vec", "lun_serial_number", "vm_config", "owner_op_type", "owner_op_root_entity", "owner_op_vm_entity")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupAcropolisVMArg.Type]
        kSetupFiles: _ClassVar[BackupAcropolisVMArg.Type]
        kBackupDisk: _ClassVar[BackupAcropolisVMArg.Type]
        kEndSubTask: _ClassVar[BackupAcropolisVMArg.Type]
        kEndBackup: _ClassVar[BackupAcropolisVMArg.Type]
    kPrepareBackup: BackupAcropolisVMArg.Type
    kSetupFiles: BackupAcropolisVMArg.Type
    kBackupDisk: BackupAcropolisVMArg.Type
    kEndSubTask: BackupAcropolisVMArg.Type
    kEndBackup: BackupAcropolisVMArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SAN_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    LUN_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OWNER_OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_OP_ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    OWNER_OP_VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupAcropolisVMArg.Type
    root_entity: _acropolis_pb2.Entity
    vm_entity: _acropolis_pb2.Entity
    san_port_vec: _containers.RepeatedCompositeFieldContainer[_san_pb2.SanPort]
    lun_serial_number: str
    vm_config: _acropolis_pb2_1.VMConfig
    owner_op_type: _enums_pb2.Environment.Type
    owner_op_root_entity: _entity_pb2.EntityProto
    owner_op_vm_entity: _entity_pb2.EntityProto
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupAcropolisVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_acropolis_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_acropolis_pb2.Entity, _Mapping]] = ..., san_port_vec: _Optional[_Iterable[_Union[_san_pb2.SanPort, _Mapping]]] = ..., lun_serial_number: _Optional[str] = ..., vm_config: _Optional[_Union[_acropolis_pb2_1.VMConfig, _Mapping]] = ..., owner_op_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., owner_op_root_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., owner_op_vm_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class RestoreVMArg(_message.Message):
    __slots__ = ("base", "type", "vm_restore_info", "view_box_id", "view_name", "create_view", "is_internal_view", "san_port_vec", "lun_serial_number", "vm_restore_info_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneVMFiles: _ClassVar[RestoreVMArg.Type]
        kRestoreDiskArea: _ClassVar[RestoreVMArg.Type]
        kEndSubTask: _ClassVar[RestoreVMArg.Type]
        kDeleteVMFiles: _ClassVar[RestoreVMArg.Type]
    kCloneVMFiles: RestoreVMArg.Type
    kRestoreDiskArea: RestoreVMArg.Type
    kEndSubTask: RestoreVMArg.Type
    kDeleteVMFiles: RestoreVMArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "vm_entity", "root_entity")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        vm_entity: _acropolis_pb2.Entity
        root_entity: _acropolis_pb2.Entity
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., vm_entity: _Optional[_Union[_acropolis_pb2.Entity, _Mapping]] = ..., root_entity: _Optional[_Union[_acropolis_pb2.Entity, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    SAN_PORT_VEC_FIELD_NUMBER: _ClassVar[int]
    LUN_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreVMArg.Type
    vm_restore_info: RestoreVMArg.VMRestoreInfo
    view_box_id: int
    view_name: str
    create_view: bool
    is_internal_view: bool
    san_port_vec: _containers.RepeatedCompositeFieldContainer[_san_pb2.SanPort]
    lun_serial_number: str
    vm_restore_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreVMArg.VMRestoreInfo]
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreVMArg.Type, str]] = ..., vm_restore_info: _Optional[_Union[RestoreVMArg.VMRestoreInfo, _Mapping]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., create_view: bool = ..., is_internal_view: bool = ..., san_port_vec: _Optional[_Iterable[_Union[_san_pb2.SanPort, _Mapping]]] = ..., lun_serial_number: _Optional[str] = ..., vm_restore_info_vec: _Optional[_Iterable[_Union[RestoreVMArg.VMRestoreInfo, _Mapping]]] = ...) -> None: ...

class AcropolisActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_acropolis_vm_arg", "restore_vm_arg", "cancel_task_arg")
    ACROPOLIS_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    acropolis_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ACROPOLIS_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_acropolis_vm_arg: BackupAcropolisVMArg
    restore_vm_arg: RestoreVMArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_acropolis_vm_arg: _Optional[_Union[BackupAcropolisVMArg, _Mapping]] = ..., restore_vm_arg: _Optional[_Union[RestoreVMArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ...) -> None: ...
