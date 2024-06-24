from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.kvm import kvm_param_pb2 as _kvm_param_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VirtualDisk(_message.Message):
    __slots__ = ("key", "uuid", "filepath", "snapshot_filepath", "capacity_bytes", "delta_type", "delta_info", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "query_disk_error")
    KVM_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    kvm_virtual_disk: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    key: int
    uuid: str
    filepath: str
    snapshot_filepath: str
    capacity_bytes: int
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    query_disk_error: _error_pb2.ErrorProto
    def __init__(self, key: _Optional[int] = ..., uuid: _Optional[str] = ..., filepath: _Optional[str] = ..., snapshot_filepath: _Optional[str] = ..., capacity_bytes: _Optional[int] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VMConfig(_message.Message):
    __slots__ = ("vm_info", "virtual_disks_vec")
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_info: _kvm_param_pb2.VMInfo
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    def __init__(self, vm_info: _Optional[_Union[_kvm_param_pb2.VMInfo, _Mapping]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("vm_name", "snapshot_uuid", "job_instance_id", "attempt_num", "vm_info", "status", "virtual_disks_vec", "sub_tasks_vec", "error", "snapshot_deletion_error", "quiesced", "sub_file_size_mb", "datastore_throttling_feature_enabled", "storage_domain_info_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kVMInfoFetched: _ClassVar[SnapshotInfo.Status]
        kCreateSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kQueryChangesVirtualDiskDone: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kVMInfoFetched: SnapshotInfo.Status
    kCreateSnapshotDone: SnapshotInfo.Status
    kQueryChangesVirtualDiskDone: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    class StorageDomainInfo(_message.Message):
        __slots__ = ("name", "uuid")
        NAME_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        name: str
        uuid: str
        def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...
    KVM_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    kvm_snapshot_info: _descriptor.FieldDescriptor
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    snapshot_uuid: bytes
    job_instance_id: int
    attempt_num: int
    vm_info: _kvm_param_pb2.VMInfo
    status: SnapshotInfo.Status
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    snapshot_deletion_error: _error_pb2.ErrorProto
    quiesced: bool
    sub_file_size_mb: int
    datastore_throttling_feature_enabled: bool
    storage_domain_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.StorageDomainInfo]
    def __init__(self, vm_name: _Optional[str] = ..., snapshot_uuid: _Optional[bytes] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., vm_info: _Optional[_Union[_kvm_param_pb2.VMInfo, _Mapping]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., quiesced: bool = ..., sub_file_size_mb: _Optional[int] = ..., datastore_throttling_feature_enabled: bool = ..., storage_domain_info_vec: _Optional[_Iterable[_Union[SnapshotInfo.StorageDomainInfo, _Mapping]]] = ...) -> None: ...

class VMRecoveryInfo(_message.Message):
    __slots__ = ("restore_task_state", "total_bytes_to_write_to_source", "sub_tasks_vec")
    class RecoverTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kVMsFilesCloned: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kCreatedVM: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kSubTasksCreated: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kSubTasksFinished: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kPowerOnVMDone: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kFinished: _ClassVar[VMRecoveryInfo.RecoverTaskState]
    kStarted: VMRecoveryInfo.RecoverTaskState
    kVMsFilesCloned: VMRecoveryInfo.RecoverTaskState
    kCreatedVM: VMRecoveryInfo.RecoverTaskState
    kSubTasksCreated: VMRecoveryInfo.RecoverTaskState
    kSubTasksFinished: VMRecoveryInfo.RecoverTaskState
    kPowerOnVMDone: VMRecoveryInfo.RecoverTaskState
    kFinished: VMRecoveryInfo.RecoverTaskState
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: VMRecoveryInfo.RecoverTaskState
    total_bytes_to_write_to_source: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    def __init__(self, restore_task_state: _Optional[_Union[VMRecoveryInfo.RecoverTaskState, str]] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("vm_recovery_info", "error")
    KVM_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    kvm_restore_info: _descriptor.FieldDescriptor
    VM_RECOVERY_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    vm_recovery_info: VMRecoveryInfo
    error: _error_pb2.ErrorProto
    def __init__(self, vm_recovery_info: _Optional[_Union[VMRecoveryInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("vm_info",)
    class VMInfo(_message.Message):
        __slots__ = ("uuid", "name", "host_ip", "vm_config", "virtual_disks_vec")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        HOST_IP_FIELD_NUMBER: _ClassVar[int]
        VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        name: str
        host_ip: str
        vm_config: VMConfig
        virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
        def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., host_ip: _Optional[str] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ...) -> None: ...
    KVM_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    kvm_restore_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_info: RestoreEntityInfo.VMInfo
    def __init__(self, vm_info: _Optional[_Union[RestoreEntityInfo.VMInfo, _Mapping]] = ...) -> None: ...
