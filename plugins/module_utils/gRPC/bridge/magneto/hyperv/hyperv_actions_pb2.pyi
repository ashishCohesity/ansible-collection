from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base.entities import hyperv_pb2 as _hyperv_pb2
from magneto.connectors.hyperv import hyperv_pb2 as _hyperv_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupHyperVVMArg(_message.Message):
    __slots__ = ("base", "type", "root_entity", "vm_entity", "sparse_vm_config", "cluster_id", "cluster_incarnation_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareBackup: _ClassVar[BackupHyperVVMArg.Type]
        kSetupFiles: _ClassVar[BackupHyperVVMArg.Type]
        kBackupDisk: _ClassVar[BackupHyperVVMArg.Type]
        kCloseDisk: _ClassVar[BackupHyperVVMArg.Type]
        kEndBackup: _ClassVar[BackupHyperVVMArg.Type]
    kPrepareBackup: BackupHyperVVMArg.Type
    kSetupFiles: BackupHyperVVMArg.Type
    kBackupDisk: BackupHyperVVMArg.Type
    kCloseDisk: BackupHyperVVMArg.Type
    kEndBackup: BackupHyperVVMArg.Type
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _magneto_actions_pb2.BackupBaseArg
    type: BackupHyperVVMArg.Type
    root_entity: _hyperv_pb2.Entity
    vm_entity: _hyperv_pb2.Entity
    sparse_vm_config: _hyperv_pb2_1.SparseVMConfig
    cluster_id: int
    cluster_incarnation_id: int
    def __init__(self, base: _Optional[_Union[_magneto_actions_pb2.BackupBaseArg, _Mapping]] = ..., type: _Optional[_Union[BackupHyperVVMArg.Type, str]] = ..., root_entity: _Optional[_Union[_hyperv_pb2.Entity, _Mapping]] = ..., vm_entity: _Optional[_Union[_hyperv_pb2.Entity, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[_hyperv_pb2_1.SparseVMConfig, _Mapping]] = ..., cluster_id: _Optional[int] = ..., cluster_incarnation_id: _Optional[int] = ...) -> None: ...

class FetchDiskMappingArg(_message.Message):
    __slots__ = ("head_filenames", "encoded_filepath_map")
    class EncodedFilepathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEAD_FILENAMES_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILEPATH_MAP_FIELD_NUMBER: _ClassVar[int]
    head_filenames: _containers.RepeatedScalarFieldContainer[str]
    encoded_filepath_map: _containers.ScalarMap[str, str]
    def __init__(self, head_filenames: _Optional[_Iterable[str]] = ..., encoded_filepath_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RestoreVMsArg(_message.Message):
    __slots__ = ("type", "vm_restore_infos", "view_box_id", "view_name", "create_view", "is_internal_view", "path_prefix", "preserve_original_dir_path", "view_whitelist_ip_addr_str_vec", "fetch_disk_mapping_arg", "include_sparse_vm_config", "use_filenames_from_backup_view")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneVMs: _ClassVar[RestoreVMsArg.Type]
        kDeleteVMs: _ClassVar[RestoreVMsArg.Type]
        kFetchDiskMapping: _ClassVar[RestoreVMsArg.Type]
        kFetchVMsInfo: _ClassVar[RestoreVMsArg.Type]
    kCloneVMs: RestoreVMsArg.Type
    kDeleteVMs: RestoreVMsArg.Type
    kFetchDiskMapping: RestoreVMsArg.Type
    kFetchVMsInfo: RestoreVMsArg.Type
    class VMRestoreInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "vm_entity", "root_entity")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        ROOT_ENTITY_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        vm_entity: _hyperv_pb2.Entity
        root_entity: _hyperv_pb2.Entity
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., vm_entity: _Optional[_Union[_hyperv_pb2.Entity, _Mapping]] = ..., root_entity: _Optional[_Union[_hyperv_pb2.Entity, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VM_RESTORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_VIEW_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ORIGINAL_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_WHITELIST_IP_ADDR_STR_VEC_FIELD_NUMBER: _ClassVar[int]
    FETCH_DISK_MAPPING_ARG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USE_FILENAMES_FROM_BACKUP_VIEW_FIELD_NUMBER: _ClassVar[int]
    type: RestoreVMsArg.Type
    vm_restore_infos: _containers.RepeatedCompositeFieldContainer[RestoreVMsArg.VMRestoreInfo]
    view_box_id: int
    view_name: str
    create_view: bool
    is_internal_view: bool
    path_prefix: str
    preserve_original_dir_path: bool
    view_whitelist_ip_addr_str_vec: _containers.RepeatedScalarFieldContainer[str]
    fetch_disk_mapping_arg: FetchDiskMappingArg
    include_sparse_vm_config: bool
    use_filenames_from_backup_view: bool
    def __init__(self, type: _Optional[_Union[RestoreVMsArg.Type, str]] = ..., vm_restore_infos: _Optional[_Iterable[_Union[RestoreVMsArg.VMRestoreInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., create_view: bool = ..., is_internal_view: bool = ..., path_prefix: _Optional[str] = ..., preserve_original_dir_path: bool = ..., view_whitelist_ip_addr_str_vec: _Optional[_Iterable[str]] = ..., fetch_disk_mapping_arg: _Optional[_Union[FetchDiskMappingArg, _Mapping]] = ..., include_sparse_vm_config: bool = ..., use_filenames_from_backup_view: bool = ...) -> None: ...

class HyperVActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "backup_hyperv_vm_arg", "restore_vms_arg", "cancel_task_arg")
    HYPERV_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    hyperv_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_HYPERV_VM_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VMS_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    backup_hyperv_vm_arg: BackupHyperVVMArg
    restore_vms_arg: RestoreVMsArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., backup_hyperv_vm_arg: _Optional[_Union[BackupHyperVVMArg, _Mapping]] = ..., restore_vms_arg: _Optional[_Union[RestoreVMsArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ...) -> None: ...
