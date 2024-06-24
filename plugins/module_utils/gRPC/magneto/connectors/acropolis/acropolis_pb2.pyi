from magneto.base import disk_pb2 as _disk_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.acropolis import acropolis_param_pb2 as _acropolis_param_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VirtualDisk(_message.Message):
    __slots__ = ("key", "uuid", "hypervisor_disk_uuid", "filepath", "snapshot_filepath", "capacity_bytes", "storage_container_uuid", "lun_serial_number", "target_suffix", "delta_type", "delta_info", "last_position_backed_up", "total_bytes_read_from_source", "encoded_filename", "query_disk_error", "disk_address")
    ACROPOLIS_VIRTUAL_DISK_FIELD_NUMBER: _ClassVar[int]
    acropolis_virtual_disk: _descriptor.FieldDescriptor
    KEY_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_DISK_UUID_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    LUN_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TARGET_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    LAST_POSITION_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_READ_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILENAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_DISK_ERROR_FIELD_NUMBER: _ClassVar[int]
    DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    key: int
    uuid: str
    hypervisor_disk_uuid: str
    filepath: str
    snapshot_filepath: str
    capacity_bytes: int
    storage_container_uuid: str
    lun_serial_number: str
    target_suffix: str
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    last_position_backed_up: int
    total_bytes_read_from_source: int
    encoded_filename: str
    query_disk_error: _error_pb2.ErrorProto
    disk_address: str
    def __init__(self, key: _Optional[int] = ..., uuid: _Optional[str] = ..., hypervisor_disk_uuid: _Optional[str] = ..., filepath: _Optional[str] = ..., snapshot_filepath: _Optional[str] = ..., capacity_bytes: _Optional[int] = ..., storage_container_uuid: _Optional[str] = ..., lun_serial_number: _Optional[str] = ..., target_suffix: _Optional[str] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., last_position_backed_up: _Optional[int] = ..., total_bytes_read_from_source: _Optional[int] = ..., encoded_filename: _Optional[str] = ..., query_disk_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., disk_address: _Optional[str] = ...) -> None: ...

class VMConfig(_message.Message):
    __slots__ = ("server_vm_info", "virtual_disks_vec")
    SERVER_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    server_vm_info: _acropolis_param_pb2.VMInfoResult
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    def __init__(self, server_vm_info: _Optional[_Union[_acropolis_param_pb2.VMInfoResult, _Mapping]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ...) -> None: ...

class VolumeGroupInfo(_message.Message):
    __slots__ = ("volume_group_uuid", "volume_group_name", "volume_group_uuid_client_identifier")
    VOLUME_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    volume_group_info: _descriptor.FieldDescriptor
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    volume_group_uuid: str
    volume_group_name: str
    volume_group_uuid_client_identifier: str
    def __init__(self, volume_group_uuid: _Optional[str] = ..., volume_group_name: _Optional[str] = ..., volume_group_uuid_client_identifier: _Optional[str] = ...) -> None: ...

class ExternalRepoInfo(_message.Message):
    __slots__ = ("external_repo_uuid_vec", "external_repo_uuid_client_identifier")
    EXTERNAL_REPO_INFO_FIELD_NUMBER: _ClassVar[int]
    external_repo_info: _descriptor.FieldDescriptor
    EXTERNAL_REPO_UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    external_repo_uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    external_repo_uuid_client_identifier: str
    def __init__(self, external_repo_uuid_vec: _Optional[_Iterable[str]] = ..., external_repo_uuid_client_identifier: _Optional[str] = ...) -> None: ...

class AdditionalSnapshotInfo(_message.Message):
    __slots__ = ("snapshot_uuid_client_identifier",)
    ADDITIONAL_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    additional_snapshot_info: _descriptor.FieldDescriptor
    SNAPSHOT_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    snapshot_uuid_client_identifier: str
    def __init__(self, snapshot_uuid_client_identifier: _Optional[str] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("vm_name", "snapshot_uuid", "job_instance_id", "attempt_num", "server_vm_info", "status", "virtual_disks_vec", "user_excluded_virtual_disks_vec", "volume_group_name", "volume_group_uuid", "client_iqn_vec", "sub_tasks_vec", "error", "snapshot_deletion_error", "volume_group_deletion_error", "quiesced", "data_services_ip_address", "sub_file_size_mb", "datastore_throttling_feature_enabled", "storage_containers_in_vm", "ngt_capable_of_app_consistent_snapshot", "ss_uuid_client_identifier", "vg_uuid_client_identifier", "snapshot_uuid_deletion_error", "volume_group_uuid_deletion_error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kVMInfoFetched: _ClassVar[SnapshotInfo.Status]
        kSnapshotUuidGenerated: _ClassVar[SnapshotInfo.Status]
        kCreateSnapshotDone: _ClassVar[SnapshotInfo.Status]
        kQueryChangesVirtualDiskDone: _ClassVar[SnapshotInfo.Status]
        kVolumeGroupCreated: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
        kSetupFilesFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
        kVolumeGroupDeleted: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kVMInfoFetched: SnapshotInfo.Status
    kSnapshotUuidGenerated: SnapshotInfo.Status
    kCreateSnapshotDone: SnapshotInfo.Status
    kQueryChangesVirtualDiskDone: SnapshotInfo.Status
    kVolumeGroupCreated: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    kSetupFilesFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    kVolumeGroupDeleted: SnapshotInfo.Status
    ACROPOLIS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    acropolis_snapshot_info: _descriptor.FieldDescriptor
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SERVER_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IQN_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    QUIESCED_FIELD_NUMBER: _ClassVar[int]
    DATA_SERVICES_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUB_FILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_THROTTLING_FEATURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINERS_IN_VM_FIELD_NUMBER: _ClassVar[int]
    NGT_CAPABLE_OF_APP_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SS_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VG_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    snapshot_uuid: bytes
    job_instance_id: int
    attempt_num: int
    server_vm_info: _acropolis_param_pb2.VMInfoResult
    status: SnapshotInfo.Status
    virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    user_excluded_virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
    volume_group_name: str
    volume_group_uuid: str
    client_iqn_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    snapshot_deletion_error: _error_pb2.ErrorProto
    volume_group_deletion_error: _error_pb2.ErrorProto
    quiesced: bool
    data_services_ip_address: str
    sub_file_size_mb: int
    datastore_throttling_feature_enabled: bool
    storage_containers_in_vm: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    ngt_capable_of_app_consistent_snapshot: bool
    ss_uuid_client_identifier: str
    vg_uuid_client_identifier: str
    snapshot_uuid_deletion_error: _error_pb2.ErrorProto
    volume_group_uuid_deletion_error: _error_pb2.ErrorProto
    def __init__(self, vm_name: _Optional[str] = ..., snapshot_uuid: _Optional[bytes] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., server_vm_info: _Optional[_Union[_acropolis_param_pb2.VMInfoResult, _Mapping]] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., user_excluded_virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., volume_group_name: _Optional[str] = ..., volume_group_uuid: _Optional[str] = ..., client_iqn_vec: _Optional[_Iterable[str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_group_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., quiesced: bool = ..., data_services_ip_address: _Optional[str] = ..., sub_file_size_mb: _Optional[int] = ..., datastore_throttling_feature_enabled: bool = ..., storage_containers_in_vm: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., ngt_capable_of_app_consistent_snapshot: bool = ..., ss_uuid_client_identifier: _Optional[str] = ..., vg_uuid_client_identifier: _Optional[str] = ..., snapshot_uuid_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_group_uuid_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VMRecoveryInfo(_message.Message):
    __slots__ = ("restore_task_state", "volume_group_name", "volume_group_uuid", "total_bytes_to_write_to_source", "client_iqn_vec", "sub_tasks_vec", "data_services_ip_address", "vg_uuid_client_identifier", "volume_group_deletion_error", "volume_group_uuid_deletion_error", "er_uuid_client_identifier", "er_uuid_deletion_error", "er_repo_info_vec", "ds_uuid_to_er_uuid_map")
    class RecoverTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kVMsFilesCloned: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kUuidsGenerated: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kVolumeGroupCreated: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kSubTasksCreated: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kSubTasksFinished: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kCreatedVM: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kVolumeGroupDeleted: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kFinished: _ClassVar[VMRecoveryInfo.RecoverTaskState]
        kExternalRepoCreated: _ClassVar[VMRecoveryInfo.RecoverTaskState]
    kStarted: VMRecoveryInfo.RecoverTaskState
    kVMsFilesCloned: VMRecoveryInfo.RecoverTaskState
    kUuidsGenerated: VMRecoveryInfo.RecoverTaskState
    kVolumeGroupCreated: VMRecoveryInfo.RecoverTaskState
    kSubTasksCreated: VMRecoveryInfo.RecoverTaskState
    kSubTasksFinished: VMRecoveryInfo.RecoverTaskState
    kCreatedVM: VMRecoveryInfo.RecoverTaskState
    kVolumeGroupDeleted: VMRecoveryInfo.RecoverTaskState
    kFinished: VMRecoveryInfo.RecoverTaskState
    kExternalRepoCreated: VMRecoveryInfo.RecoverTaskState
    class ExternalRepoInfo(_message.Message):
        __slots__ = ("uuid", "name", "er_deletion_error", "server_ip_address", "vms_index_vec")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ER_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        VMS_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        name: str
        er_deletion_error: _error_pb2.ErrorProto
        server_ip_address: str
        vms_index_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., er_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., server_ip_address: _Optional[str] = ..., vms_index_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class DsUuidToErUuidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESTORE_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_TO_WRITE_TO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IQN_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_SERVICES_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VG_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    ER_UUID_CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ER_UUID_DELETION_ERROR_FIELD_NUMBER: _ClassVar[int]
    ER_REPO_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DS_UUID_TO_ER_UUID_MAP_FIELD_NUMBER: _ClassVar[int]
    restore_task_state: VMRecoveryInfo.RecoverTaskState
    volume_group_name: str
    volume_group_uuid: str
    total_bytes_to_write_to_source: int
    client_iqn_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    data_services_ip_address: str
    vg_uuid_client_identifier: str
    volume_group_deletion_error: _error_pb2.ErrorProto
    volume_group_uuid_deletion_error: _error_pb2.ErrorProto
    er_uuid_client_identifier: str
    er_uuid_deletion_error: _error_pb2.ErrorProto
    er_repo_info_vec: _containers.RepeatedCompositeFieldContainer[VMRecoveryInfo.ExternalRepoInfo]
    ds_uuid_to_er_uuid_map: _containers.ScalarMap[str, str]
    def __init__(self, restore_task_state: _Optional[_Union[VMRecoveryInfo.RecoverTaskState, str]] = ..., volume_group_name: _Optional[str] = ..., volume_group_uuid: _Optional[str] = ..., total_bytes_to_write_to_source: _Optional[int] = ..., client_iqn_vec: _Optional[_Iterable[str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., data_services_ip_address: _Optional[str] = ..., vg_uuid_client_identifier: _Optional[str] = ..., volume_group_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_group_uuid_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., er_uuid_client_identifier: _Optional[str] = ..., er_uuid_deletion_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., er_repo_info_vec: _Optional[_Iterable[_Union[VMRecoveryInfo.ExternalRepoInfo, _Mapping]]] = ..., ds_uuid_to_er_uuid_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("vm_recovery_info", "error")
    ACROPOLIS_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    acropolis_restore_info: _descriptor.FieldDescriptor
    VM_RECOVERY_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    vm_recovery_info: VMRecoveryInfo
    error: _error_pb2.ErrorProto
    def __init__(self, vm_recovery_info: _Optional[_Union[VMRecoveryInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("vm_info",)
    class DatasourceInfo(_message.Message):
        __slots__ = ("uuid", "migration_suspended_count", "error")
        UUID_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_SUSPENDED_COUNT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        migration_suspended_count: int
        error: _error_pb2.ErrorProto
        def __init__(self, uuid: _Optional[str] = ..., migration_suspended_count: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class VMInfo(_message.Message):
        __slots__ = ("uuid", "name", "vm_config", "virtual_disks_vec", "finished_ds_migration_vec", "suspended_ds_migration_vec")
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_DISKS_VEC_FIELD_NUMBER: _ClassVar[int]
        FINISHED_DS_MIGRATION_VEC_FIELD_NUMBER: _ClassVar[int]
        SUSPENDED_DS_MIGRATION_VEC_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        name: str
        vm_config: VMConfig
        virtual_disks_vec: _containers.RepeatedCompositeFieldContainer[VirtualDisk]
        finished_ds_migration_vec: _containers.RepeatedCompositeFieldContainer[RestoreEntityInfo.DatasourceInfo]
        suspended_ds_migration_vec: _containers.RepeatedCompositeFieldContainer[RestoreEntityInfo.DatasourceInfo]
        def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., vm_config: _Optional[_Union[VMConfig, _Mapping]] = ..., virtual_disks_vec: _Optional[_Iterable[_Union[VirtualDisk, _Mapping]]] = ..., finished_ds_migration_vec: _Optional[_Iterable[_Union[RestoreEntityInfo.DatasourceInfo, _Mapping]]] = ..., suspended_ds_migration_vec: _Optional[_Iterable[_Union[RestoreEntityInfo.DatasourceInfo, _Mapping]]] = ...) -> None: ...
    ACROPOLIS_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    acropolis_restore_entity_info: _descriptor.FieldDescriptor
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_info: RestoreEntityInfo.VMInfo
    def __init__(self, vm_info: _Optional[_Union[RestoreEntityInfo.VMInfo, _Mapping]] = ...) -> None: ...

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("server_vm_info", "vm_uuid")
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    SERVER_VM_INFO_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    server_vm_info: _acropolis_param_pb2.VMInfoResult
    vm_uuid: str
    def __init__(self, server_vm_info: _Optional[_Union[_acropolis_param_pb2.VMInfoResult, _Mapping]] = ..., vm_uuid: _Optional[str] = ...) -> None: ...
