from magneto.agents.windows.base import hyperv_pb2 as _hyperv_pb2
from magneto.base import cloud_pb2 as _cloud_pb2
from magneto.base.entities import hyperv_pb2 as _hyperv_pb2_1
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.hyperv import hyperv_pb2 as _hyperv_pb2_1_1
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
    __slots__ = ("virtual_disks",)
    VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    virtual_disks: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2_1_1.VirtualDisk]
    def __init__(self, virtual_disks: _Optional[_Iterable[_Union[_hyperv_pb2_1_1.VirtualDisk, _Mapping]]] = ...) -> None: ...

class HyperVStartRestoreTaskArg(_message.Message):
    __slots__ = ("network_config",)
    HYPERV_START_RESTORE_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    hyperv_start_restore_task_arg: _descriptor.FieldDescriptor
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    network_config: _hyperv_pb2.NetworkConfigInfo
    def __init__(self, network_config: _Optional[_Union[_hyperv_pb2.NetworkConfigInfo, _Mapping]] = ...) -> None: ...

class CloneVMsUpdateArg(_message.Message):
    __slots__ = ("cloned_vms",)
    class ClonedVM(_message.Message):
        __slots__ = ("vm_entity", "sparse_vm_config", "relative_cloned_paths")
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONED_PATHS_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _hyperv_pb2_1.Entity
        sparse_vm_config: _hyperv_pb2_1_1.SparseVMConfig
        relative_cloned_paths: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, vm_entity: _Optional[_Union[_hyperv_pb2_1.Entity, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[_hyperv_pb2_1_1.SparseVMConfig, _Mapping]] = ..., relative_cloned_paths: _Optional[_Iterable[str]] = ...) -> None: ...
    CLONED_VMS_FIELD_NUMBER: _ClassVar[int]
    cloned_vms: _containers.RepeatedCompositeFieldContainer[CloneVMsUpdateArg.ClonedVM]
    def __init__(self, cloned_vms: _Optional[_Iterable[_Union[CloneVMsUpdateArg.ClonedVM, _Mapping]]] = ...) -> None: ...

class FetchDiskMappingUpdateArg(_message.Message):
    __slots__ = ("chained_logical_disk_mapping",)
    CHAINED_LOGICAL_DISK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    chained_logical_disk_mapping: _cloud_pb2.ChainedLogicalDiskMapping
    def __init__(self, chained_logical_disk_mapping: _Optional[_Union[_cloud_pb2.ChainedLogicalDiskMapping, _Mapping]] = ...) -> None: ...

class CloneVMFilesUpdateArg(_message.Message):
    __slots__ = ("vm_entity", "sparse_vm_config", "relative_cloned_path_vec")
    VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_CLONED_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_entity: _hyperv_pb2_1.Entity
    sparse_vm_config: _hyperv_pb2_1_1.SparseVMConfig
    relative_cloned_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vm_entity: _Optional[_Union[_hyperv_pb2_1.Entity, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[_hyperv_pb2_1_1.SparseVMConfig, _Mapping]] = ..., relative_cloned_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchVMsInfoUpdateArg(_message.Message):
    __slots__ = ("vm_info_vec",)
    class VMInfo(_message.Message):
        __slots__ = ("vm_entity", "sparse_vm_config")
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        SPARSE_VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _hyperv_pb2_1.Entity
        sparse_vm_config: _hyperv_pb2_1_1.SparseVMConfig
        def __init__(self, vm_entity: _Optional[_Union[_hyperv_pb2_1.Entity, _Mapping]] = ..., sparse_vm_config: _Optional[_Union[_hyperv_pb2_1_1.SparseVMConfig, _Mapping]] = ...) -> None: ...
    VM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_info_vec: _containers.RepeatedCompositeFieldContainer[FetchVMsInfoUpdateArg.VMInfo]
    def __init__(self, vm_info_vec: _Optional[_Iterable[_Union[FetchVMsInfoUpdateArg.VMInfo, _Mapping]]] = ...) -> None: ...

class HyperVActionUpdateArg(_message.Message):
    __slots__ = ("type", "prepare_vm_backup_update_arg", "setup_vm_files_update_arg", "backup_disk_update_arg", "clone_vms_update_arg", "fetch_disk_mapping_update_arg", "clone_vm_update_arg", "fetch_vms_info_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrepareVMBackupUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kSetupVMFilesUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kBackupVMDiskUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kCloseVMDiskUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kEndVMBackupUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kCloneVMsUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kFetchDiskMappingUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kCloneVMFilesUpdate: _ClassVar[HyperVActionUpdateArg.Type]
        kFetchVMsInfoUpdate: _ClassVar[HyperVActionUpdateArg.Type]
    kPrepareVMBackupUpdate: HyperVActionUpdateArg.Type
    kSetupVMFilesUpdate: HyperVActionUpdateArg.Type
    kBackupVMDiskUpdate: HyperVActionUpdateArg.Type
    kCloseVMDiskUpdate: HyperVActionUpdateArg.Type
    kEndVMBackupUpdate: HyperVActionUpdateArg.Type
    kCloneVMsUpdate: HyperVActionUpdateArg.Type
    kFetchDiskMappingUpdate: HyperVActionUpdateArg.Type
    kCloneVMFilesUpdate: HyperVActionUpdateArg.Type
    kFetchVMsInfoUpdate: HyperVActionUpdateArg.Type
    HYPERV_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    hyperv_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PREPARE_VM_BACKUP_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_FILES_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DISK_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_VMS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_DISK_MAPPING_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_VM_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_VMS_INFO_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: HyperVActionUpdateArg.Type
    prepare_vm_backup_update_arg: PrepareVMBackupUpdateArg
    setup_vm_files_update_arg: SetupVMFilesUpdateArg
    backup_disk_update_arg: _stub_pb2.BackupDiskUpdateArg
    clone_vms_update_arg: CloneVMsUpdateArg
    fetch_disk_mapping_update_arg: FetchDiskMappingUpdateArg
    clone_vm_update_arg: CloneVMFilesUpdateArg
    fetch_vms_info_update_arg: FetchVMsInfoUpdateArg
    def __init__(self, type: _Optional[_Union[HyperVActionUpdateArg.Type, str]] = ..., prepare_vm_backup_update_arg: _Optional[_Union[PrepareVMBackupUpdateArg, _Mapping]] = ..., setup_vm_files_update_arg: _Optional[_Union[SetupVMFilesUpdateArg, _Mapping]] = ..., backup_disk_update_arg: _Optional[_Union[_stub_pb2.BackupDiskUpdateArg, _Mapping]] = ..., clone_vms_update_arg: _Optional[_Union[CloneVMsUpdateArg, _Mapping]] = ..., fetch_disk_mapping_update_arg: _Optional[_Union[FetchDiskMappingUpdateArg, _Mapping]] = ..., clone_vm_update_arg: _Optional[_Union[CloneVMFilesUpdateArg, _Mapping]] = ..., fetch_vms_info_update_arg: _Optional[_Union[FetchVMsInfoUpdateArg, _Mapping]] = ...) -> None: ...

class RestoreEntityArg(_message.Message):
    __slots__ = ("connector_params_id",)
    HYPERV_RESTORE_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    hyperv_restore_entity_arg: _descriptor.FieldDescriptor
    CONNECTOR_PARAMS_ID_FIELD_NUMBER: _ClassVar[int]
    connector_params_id: int
    def __init__(self, connector_params_id: _Optional[int] = ...) -> None: ...
