from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import gcp_pb2 as _gcp_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.connectors.gcp import gcp_pb2 as _gcp_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupGCPVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "vm_config")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupGCPVMArg.Type]
        kSetupFiles: _ClassVar[BackupGCPVMArg.Type]
        kBackupDisk: _ClassVar[BackupGCPVMArg.Type]
        kEndSubTask: _ClassVar[BackupGCPVMArg.Type]
        kEndBackup: _ClassVar[BackupGCPVMArg.Type]
    kPrepareBackup: BackupGCPVMArg.Type
    kSetupFiles: BackupGCPVMArg.Type
    kBackupDisk: BackupGCPVMArg.Type
    kEndSubTask: BackupGCPVMArg.Type
    kEndBackup: BackupGCPVMArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupGCPVMArg.Type
    root_entity: _gcp_pb2.Entity
    vm_entity: _gcp_pb2.Entity
    vm_config: _gcp_pb2_1.VMConfig
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupGCPVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_gcp_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_gcp_pb2.Entity, _Mapping]] = ..., vm_config: _Optional[_Union[_gcp_pb2_1.VMConfig, _Mapping]] = ...) -> None: ...

class RestoreGCPVMArg(_message.Message):
    __slots__ = ("base", "type", "vm_restore_infos", "view_box_id", "destination_view_name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFetchVMInfo: _ClassVar[RestoreGCPVMArg.Type]
        kRestoreDisk: _ClassVar[RestoreGCPVMArg.Type]
        kEndSubTask: _ClassVar[RestoreGCPVMArg.Type]
        kEndRestore: _ClassVar[RestoreGCPVMArg.Type]
    kFetchVMInfo: RestoreGCPVMArg.Type
    kRestoreDisk: RestoreGCPVMArg.Type
    kEndSubTask: RestoreGCPVMArg.Type
    kEndRestore: RestoreGCPVMArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("entity", "gcp_entity_infos", "snapshot_relative_dir_path")
        class GCPEntityInfo(_message.Message):
            __slots__ = ("name", "vm_disk_relative_filepath", "size", "disk_info")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VM_DISK_RELATIVE_FILEPATH_FIELD_NUMBER: _ClassVar[int]
            SIZE_FIELD_NUMBER: _ClassVar[int]
            DISK_INFO_FIELD_NUMBER: _ClassVar[int]
            name: str
            vm_disk_relative_filepath: str
            size: int
            disk_info: _gcp_pb2_1.CloudDeployEntityInfo.DiskInfo
            def __init__(self, name: _Optional[str] = ..., vm_disk_relative_filepath: _Optional[str] = ..., size: _Optional[int] = ..., disk_info: _Optional[_Union[_gcp_pb2_1.CloudDeployEntityInfo.DiskInfo, _Mapping]] = ...) -> None: ...
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        GCP_ENTITY_INFOS_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        entity: _entity_pb2.EntityProto
        gcp_entity_infos: _containers.RepeatedCompositeFieldContainer[RestoreGCPVMArg.VMRestoreInfo.GCPEntityInfo]
        snapshot_relative_dir_path: str
        def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., gcp_entity_infos: _Optional[_Iterable[_Union[RestoreGCPVMArg.VMRestoreInfo.GCPEntityInfo, _Mapping]]] = ..., snapshot_relative_dir_path: _Optional[str] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.RestoreBaseArg
    type: RestoreGCPVMArg.Type
    vm_restore_infos: _containers.RepeatedCompositeFieldContainer[RestoreGCPVMArg.VMRestoreInfo]
    view_box_id: int
    destination_view_name: str
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.RestoreBaseArg, _Mapping]] = ..., type: _Optional[_Union[RestoreGCPVMArg.Type, str]] = ..., vm_restore_infos: _Optional[_Iterable[_Union[RestoreGCPVMArg.VMRestoreInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., destination_view_name: _Optional[str] = ...) -> None: ...

class GCPActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_vm_arg", "restore_vm_arg")
    GCP_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    gcp_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_vm_arg: BackupGCPVMArg
    restore_vm_arg: RestoreGCPVMArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_vm_arg: _Optional[_Union[BackupGCPVMArg, _Mapping]] = ..., restore_vm_arg: _Optional[_Union[RestoreGCPVMArg, _Mapping]] = ...) -> None: ...
