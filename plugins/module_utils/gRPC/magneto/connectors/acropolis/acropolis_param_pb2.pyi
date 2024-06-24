from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base.entities import acropolis_pb2 as _acropolis_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApiVersion(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kVersion1: _ClassVar[ApiVersion.Type]
        kVersion2: _ClassVar[ApiVersion.Type]
        kVersion3: _ClassVar[ApiVersion.Type]
    kVersion1: ApiVersion.Type
    kVersion2: ApiVersion.Type
    kVersion3: ApiVersion.Type
    def __init__(self) -> None: ...

class PowerState(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPowerOn: _ClassVar[PowerState.Type]
        kPowerOff: _ClassVar[PowerState.Type]
        kPaused: _ClassVar[PowerState.Type]
        kInvalid: _ClassVar[PowerState.Type]
    kPowerOn: PowerState.Type
    kPowerOff: PowerState.Type
    kPaused: PowerState.Type
    kInvalid: PowerState.Type
    def __init__(self) -> None: ...

class AcropolisHierarchyArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class AcropolisHierarchyResult(_message.Message):
    __slots__ = ("error", "entity_hierarchy")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class ClusterConfigArg(_message.Message):
    __slots__ = ("cluster_uuid",)
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    cluster_uuid: str
    def __init__(self, cluster_uuid: _Optional[str] = ...) -> None: ...

class ClusterConfigResult(_message.Message):
    __slots__ = ("cluster_uuid", "cluster_name", "data_services_ip_address", "is_prism_central", "is_acropolis_cluster", "version", "management_servers")
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SERVICES_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_PRISM_CENTRAL_FIELD_NUMBER: _ClassVar[int]
    IS_ACROPOLIS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SERVERS_FIELD_NUMBER: _ClassVar[int]
    cluster_uuid: str
    cluster_name: str
    data_services_ip_address: str
    is_prism_central: bool
    is_acropolis_cluster: bool
    version: str
    management_servers: _containers.RepeatedCompositeFieldContainer[_acropolis_pb2.ManagementServer]
    def __init__(self, cluster_uuid: _Optional[str] = ..., cluster_name: _Optional[str] = ..., data_services_ip_address: _Optional[str] = ..., is_prism_central: bool = ..., is_acropolis_cluster: bool = ..., version: _Optional[str] = ..., management_servers: _Optional[_Iterable[_Union[_acropolis_pb2.ManagementServer, _Mapping]]] = ...) -> None: ...

class ExternalRepoState(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPending: _ClassVar[ExternalRepoState.Type]
        kComplete: _ClassVar[ExternalRepoState.Type]
        kRunning: _ClassVar[ExternalRepoState.Type]
        kDeletePending: _ClassVar[ExternalRepoState.Type]
        kDeleteinProgress: _ClassVar[ExternalRepoState.Type]
        kRetry: _ClassVar[ExternalRepoState.Type]
        kError: _ClassVar[ExternalRepoState.Type]
        kInvalidState: _ClassVar[ExternalRepoState.Type]
    kPending: ExternalRepoState.Type
    kComplete: ExternalRepoState.Type
    kRunning: ExternalRepoState.Type
    kDeletePending: ExternalRepoState.Type
    kDeleteinProgress: ExternalRepoState.Type
    kRetry: ExternalRepoState.Type
    kError: ExternalRepoState.Type
    kInvalidState: ExternalRepoState.Type
    def __init__(self) -> None: ...

class DatasourceState(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPending: _ClassVar[DatasourceState.Type]
        kComplete: _ClassVar[DatasourceState.Type]
        kRunning: _ClassVar[DatasourceState.Type]
        kDeletePending: _ClassVar[DatasourceState.Type]
        kDeleteinProgress: _ClassVar[DatasourceState.Type]
        kRetry: _ClassVar[DatasourceState.Type]
        kError: _ClassVar[DatasourceState.Type]
        kInvalidState: _ClassVar[DatasourceState.Type]
    kPending: DatasourceState.Type
    kComplete: DatasourceState.Type
    kRunning: DatasourceState.Type
    kDeletePending: DatasourceState.Type
    kDeleteinProgress: DatasourceState.Type
    kRetry: DatasourceState.Type
    kError: DatasourceState.Type
    kInvalidState: DatasourceState.Type
    def __init__(self) -> None: ...

class SnapshotType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCrashConsistent: _ClassVar[SnapshotType.Type]
        kAppConsistent: _ClassVar[SnapshotType.Type]
        kInvalidType: _ClassVar[SnapshotType.Type]
    kCrashConsistent: SnapshotType.Type
    kAppConsistent: SnapshotType.Type
    kInvalidType: SnapshotType.Type
    def __init__(self) -> None: ...

class SnapshotState(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPending: _ClassVar[SnapshotState.Type]
        kComplete: _ClassVar[SnapshotState.Type]
        kRunning: _ClassVar[SnapshotState.Type]
        kDeletePending: _ClassVar[SnapshotState.Type]
        kDeleteinProgress: _ClassVar[SnapshotState.Type]
        kRetry: _ClassVar[SnapshotState.Type]
        kError: _ClassVar[SnapshotState.Type]
        kInvalidState: _ClassVar[SnapshotState.Type]
    kPending: SnapshotState.Type
    kComplete: SnapshotState.Type
    kRunning: SnapshotState.Type
    kDeletePending: SnapshotState.Type
    kDeleteinProgress: SnapshotState.Type
    kRetry: SnapshotState.Type
    kError: SnapshotState.Type
    kInvalidState: SnapshotState.Type
    def __init__(self) -> None: ...

class HypervisorType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAcropolisType: _ClassVar[HypervisorType.Type]
        kInvalidType: _ClassVar[HypervisorType.Type]
    kAcropolisType: HypervisorType.Type
    kInvalidType: HypervisorType.Type
    def __init__(self) -> None: ...

class CreateExternalRepoArg(_message.Message):
    __slots__ = ("exported_directory", "server_ip", "external_repo_uuid", "external_repo_name")
    EXPORTED_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_UUID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    exported_directory: str
    server_ip: str
    external_repo_uuid: str
    external_repo_name: str
    def __init__(self, exported_directory: _Optional[str] = ..., server_ip: _Optional[str] = ..., external_repo_uuid: _Optional[str] = ..., external_repo_name: _Optional[str] = ...) -> None: ...

class CreateExternalRepoResult(_message.Message):
    __slots__ = ("error", "external_repo_uuid", "external_repo_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_UUID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    external_repo_uuid: str
    external_repo_info: GetExternalRepoInfoResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., external_repo_uuid: _Optional[str] = ..., external_repo_info: _Optional[_Union[GetExternalRepoInfoResult, _Mapping]] = ...) -> None: ...

class NfsConfiguration(_message.Message):
    __slots__ = ("access_mode", "exported_directory", "server_address_vec")
    class ServerAddress(_message.Message):
        __slots__ = ("ip",)
        IP_FIELD_NUMBER: _ClassVar[int]
        ip: str
        def __init__(self, ip: _Optional[str] = ...) -> None: ...
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SERVER_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    access_mode: str
    exported_directory: str
    server_address_vec: _containers.RepeatedCompositeFieldContainer[NfsConfiguration.ServerAddress]
    def __init__(self, access_mode: _Optional[str] = ..., exported_directory: _Optional[str] = ..., server_address_vec: _Optional[_Iterable[_Union[NfsConfiguration.ServerAddress, _Mapping]]] = ...) -> None: ...

class GetExternalRepoInfoArg(_message.Message):
    __slots__ = ("external_repo_uuid",)
    EXTERNAL_REPO_UUID_FIELD_NUMBER: _ClassVar[int]
    external_repo_uuid: str
    def __init__(self, external_repo_uuid: _Optional[str] = ...) -> None: ...

class GetExternalRepoInfoResult(_message.Message):
    __slots__ = ("error", "external_repo_name", "external_repo_state", "nfs_configuration")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPO_STATE_FIELD_NUMBER: _ClassVar[int]
    NFS_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    external_repo_name: str
    external_repo_state: ExternalRepoState.Type
    nfs_configuration: NfsConfiguration
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., external_repo_name: _Optional[str] = ..., external_repo_state: _Optional[_Union[ExternalRepoState.Type, str]] = ..., nfs_configuration: _Optional[_Union[NfsConfiguration, _Mapping]] = ...) -> None: ...

class CreateVMSnapshotArg(_message.Message):
    __slots__ = ("vm_uuid", "vm_name", "snapshot_uuid", "snapshot_name", "snapshot_type", "expiration_time")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    vm_name: str
    snapshot_uuid: str
    snapshot_name: str
    snapshot_type: SnapshotType.Type
    expiration_time: int
    def __init__(self, vm_uuid: _Optional[str] = ..., vm_name: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., snapshot_name: _Optional[str] = ..., snapshot_type: _Optional[_Union[SnapshotType.Type, str]] = ..., expiration_time: _Optional[int] = ...) -> None: ...

class CreateVMSnapshotResult(_message.Message):
    __slots__ = ("error", "snapshot_uuid", "snapshot_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    snapshot_uuid: str
    snapshot_info: GetSnapshotInfoResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_uuid: _Optional[str] = ..., snapshot_info: _Optional[_Union[GetSnapshotInfoResult, _Mapping]] = ...) -> None: ...

class GetSnapshotInfoArg(_message.Message):
    __slots__ = ("vm_uuid", "vm_name", "snapshot_uuid")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    vm_name: str
    snapshot_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ..., vm_name: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ...) -> None: ...

class VirtualDiskInfo(_message.Message):
    __slots__ = ("disk_uuid", "disk_path", "snapshot_disk_path", "capacity_bytes")
    DISK_UUID_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    disk_uuid: str
    disk_path: str
    snapshot_disk_path: str
    capacity_bytes: int
    def __init__(self, disk_uuid: _Optional[str] = ..., disk_path: _Optional[str] = ..., snapshot_disk_path: _Optional[str] = ..., capacity_bytes: _Optional[int] = ...) -> None: ...

class GetSnapshotInfoResult(_message.Message):
    __slots__ = ("error", "snapshot_name", "snapshot_type", "snapshot_state", "disk_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    snapshot_name: str
    snapshot_type: SnapshotType.Type
    snapshot_state: SnapshotState.Type
    disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., snapshot_name: _Optional[str] = ..., snapshot_type: _Optional[_Union[SnapshotType.Type, str]] = ..., snapshot_state: _Optional[_Union[SnapshotState.Type, str]] = ..., disk_vec: _Optional[_Iterable[_Union[VirtualDiskInfo, _Mapping]]] = ...) -> None: ...

class GetVirtualDiskChangesArg(_message.Message):
    __slots__ = ("vm_uuid", "snapshot_uuid", "disk_uuid", "curr_disk_path", "prev_disk_path", "start_offset_bytes")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    DISK_UUID_FIELD_NUMBER: _ClassVar[int]
    CURR_DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    PREV_DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    snapshot_uuid: str
    disk_uuid: str
    curr_disk_path: str
    prev_disk_path: str
    start_offset_bytes: int
    def __init__(self, vm_uuid: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ..., disk_uuid: _Optional[str] = ..., curr_disk_path: _Optional[str] = ..., prev_disk_path: _Optional[str] = ..., start_offset_bytes: _Optional[int] = ...) -> None: ...

class GetVirtualDiskChangesResult(_message.Message):
    __slots__ = ("error", "delta_type", "delta_info", "file_size_bytes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    file_size_bytes: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ..., file_size_bytes: _Optional[int] = ...) -> None: ...

class DeleteVMSnapshotArg(_message.Message):
    __slots__ = ("vm_uuid", "snapshot_uuid")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_UUID_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    snapshot_uuid: str
    def __init__(self, vm_uuid: _Optional[str] = ..., snapshot_uuid: _Optional[str] = ...) -> None: ...

class DeleteVMSnapshotResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateUUIDArg(_message.Message):
    __slots__ = ("client_identifier", "count")
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    client_identifier: str
    count: int
    def __init__(self, client_identifier: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CreateUUIDResult(_message.Message):
    __slots__ = ("client_identifier", "count", "uuid_vec")
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UUID_VEC_FIELD_NUMBER: _ClassVar[int]
    client_identifier: str
    count: int
    uuid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_identifier: _Optional[str] = ..., count: _Optional[int] = ..., uuid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteUUIDArg(_message.Message):
    __slots__ = ("client_identifier",)
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    client_identifier: str
    def __init__(self, client_identifier: _Optional[str] = ...) -> None: ...

class DeleteUUIDResult(_message.Message):
    __slots__ = ("error", "client_identifier")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    client_identifier: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., client_identifier: _Optional[str] = ...) -> None: ...

class CreateVMArg(_message.Message):
    __slots__ = ("entity", "vm_details", "recover_excluded_disks_as_blank_disks", "copy_recovery")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    RECOVER_EXCLUDED_DISKS_AS_BLANK_DISKS_FIELD_NUMBER: _ClassVar[int]
    COPY_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    entity: VMEntity
    vm_details: VMDetails
    recover_excluded_disks_as_blank_disks: bool
    copy_recovery: bool
    def __init__(self, entity: _Optional[_Union[VMEntity, _Mapping]] = ..., vm_details: _Optional[_Union[VMDetails, _Mapping]] = ..., recover_excluded_disks_as_blank_disks: bool = ..., copy_recovery: bool = ...) -> None: ...

class CreateVMResult(_message.Message):
    __slots__ = ("error", "vm_uuid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_uuid: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_uuid: _Optional[str] = ...) -> None: ...

class CreateConfig(_message.Message):
    __slots__ = ("storage_container_uuid", "size_bytes")
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    storage_container_uuid: str
    size_bytes: int
    def __init__(self, storage_container_uuid: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class CloneConfig(_message.Message):
    __slots__ = ("storage_container_uuid", "ndfs_filepath", "vmdisk_uuid")
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    NDFS_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    VMDISK_UUID_FIELD_NUMBER: _ClassVar[int]
    storage_container_uuid: str
    ndfs_filepath: str
    vmdisk_uuid: str
    def __init__(self, storage_container_uuid: _Optional[str] = ..., ndfs_filepath: _Optional[str] = ..., vmdisk_uuid: _Optional[str] = ...) -> None: ...

class CreateVolumeGroupArg(_message.Message):
    __slots__ = ("volume_group_name", "volume_group_uuid", "iscsi_target_prefix", "iscsi_target", "disk_spec_vec", "client_address_vec")
    class DiskSpec(_message.Message):
        __slots__ = ("create_config", "clone_config")
        CREATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        CLONE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        create_config: CreateConfig
        clone_config: CloneConfig
        def __init__(self, create_config: _Optional[_Union[CreateConfig, _Mapping]] = ..., clone_config: _Optional[_Union[CloneConfig, _Mapping]] = ...) -> None: ...
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_FIELD_NUMBER: _ClassVar[int]
    DISK_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_group_name: str
    volume_group_uuid: str
    iscsi_target_prefix: str
    iscsi_target: str
    disk_spec_vec: _containers.RepeatedCompositeFieldContainer[CreateVolumeGroupArg.DiskSpec]
    client_address_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, volume_group_name: _Optional[str] = ..., volume_group_uuid: _Optional[str] = ..., iscsi_target_prefix: _Optional[str] = ..., iscsi_target: _Optional[str] = ..., disk_spec_vec: _Optional[_Iterable[_Union[CreateVolumeGroupArg.DiskSpec, _Mapping]]] = ..., client_address_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateVolumeGroupResult(_message.Message):
    __slots__ = ("error", "volume_group_uuid", "volume_group_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_group_uuid: str
    volume_group_info: VolumeGroupInfoResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_group_uuid: _Optional[str] = ..., volume_group_info: _Optional[_Union[VolumeGroupInfoResult, _Mapping]] = ...) -> None: ...

class DeleteVolumeGroupArg(_message.Message):
    __slots__ = ("volume_group_uuid", "volume_group_name")
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    volume_group_uuid: str
    volume_group_name: str
    def __init__(self, volume_group_uuid: _Optional[str] = ..., volume_group_name: _Optional[str] = ...) -> None: ...

class DeleteVolumeGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateVolumeGroupArg(_message.Message):
    __slots__ = ("volume_group_uuid", "client_address_vec", "name", "iscsi_target_prefix")
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_PREFIX_FIELD_NUMBER: _ClassVar[int]
    volume_group_uuid: str
    client_address_vec: _containers.RepeatedScalarFieldContainer[str]
    name: str
    iscsi_target_prefix: str
    def __init__(self, volume_group_uuid: _Optional[str] = ..., client_address_vec: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., iscsi_target_prefix: _Optional[str] = ...) -> None: ...

class UpdateVolumeGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CloseVolumeGroupArg(_message.Message):
    __slots__ = ("volume_group_uuid", "iscsi_client")
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    ISCSI_CLIENT_FIELD_NUMBER: _ClassVar[int]
    volume_group_uuid: str
    iscsi_client: str
    def __init__(self, volume_group_uuid: _Optional[str] = ..., iscsi_client: _Optional[str] = ...) -> None: ...

class CloseVolumeGroupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VolumeGroupInfoArg(_message.Message):
    __slots__ = ("volume_group_uuid",)
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    volume_group_uuid: str
    def __init__(self, volume_group_uuid: _Optional[str] = ...) -> None: ...

class VolumeGroupInfoResult(_message.Message):
    __slots__ = ("error", "volume_group_uuid", "is_deleted", "initiator_vec", "iscsi_target", "volume_group_name", "volume_disk_vec")
    class Initiators(_message.Message):
        __slots__ = ("initiator_ip_address", "iscsi_initiator_name")
        INITIATOR_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        ISCSI_INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
        initiator_ip_address: str
        iscsi_initiator_name: str
        def __init__(self, initiator_ip_address: _Optional[str] = ..., iscsi_initiator_name: _Optional[str] = ...) -> None: ...
    class VolumeDiskList(_message.Message):
        __slots__ = ("index", "storage_container_uuid", "vmdisk_uuid", "vmdisk_size_mb")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
        VMDISK_UUID_FIELD_NUMBER: _ClassVar[int]
        VMDISK_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        index: int
        storage_container_uuid: str
        vmdisk_uuid: str
        vmdisk_size_mb: int
        def __init__(self, index: _Optional[int] = ..., storage_container_uuid: _Optional[str] = ..., vmdisk_uuid: _Optional[str] = ..., vmdisk_size_mb: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_VEC_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    volume_group_uuid: str
    is_deleted: bool
    initiator_vec: _containers.RepeatedCompositeFieldContainer[VolumeGroupInfoResult.Initiators]
    iscsi_target: str
    volume_group_name: str
    volume_disk_vec: _containers.RepeatedCompositeFieldContainer[VolumeGroupInfoResult.VolumeDiskList]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., volume_group_uuid: _Optional[str] = ..., is_deleted: bool = ..., initiator_vec: _Optional[_Iterable[_Union[VolumeGroupInfoResult.Initiators, _Mapping]]] = ..., iscsi_target: _Optional[str] = ..., volume_group_name: _Optional[str] = ..., volume_disk_vec: _Optional[_Iterable[_Union[VolumeGroupInfoResult.VolumeDiskList, _Mapping]]] = ...) -> None: ...

class WaitForTaskArg(_message.Message):
    __slots__ = ("task_uuid", "poll_interval_msecs", "timeout_msecs")
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    POLL_INTERVAL_MSECS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    poll_interval_msecs: int
    timeout_msecs: int
    def __init__(self, task_uuid: _Optional[str] = ..., poll_interval_msecs: _Optional[int] = ..., timeout_msecs: _Optional[int] = ...) -> None: ...

class WaitForTaskResult(_message.Message):
    __slots__ = ("error", "task_uuid", "entity_uuid", "entity_name")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_UUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_uuid: str
    entity_uuid: str
    entity_name: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_uuid: _Optional[str] = ..., entity_uuid: _Optional[str] = ..., entity_name: _Optional[str] = ...) -> None: ...

class EntityMetadataConf(_message.Message):
    __slots__ = ("uuid", "hypervisor_vm_uuid", "name", "kind", "entity_version", "running_on_ndfs", "non_ndfs_details")
    UUID_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_VM_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    RUNNING_ON_NDFS_FIELD_NUMBER: _ClassVar[int]
    NON_NDFS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    hypervisor_vm_uuid: str
    name: str
    kind: str
    entity_version: int
    running_on_ndfs: bool
    non_ndfs_details: str
    def __init__(self, uuid: _Optional[str] = ..., hypervisor_vm_uuid: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ..., entity_version: _Optional[int] = ..., running_on_ndfs: bool = ..., non_ndfs_details: _Optional[str] = ...) -> None: ...

class DiskConfig(_message.Message):
    __slots__ = ("disk_size_bytes", "device_type", "storage_container_uuid", "storage_container_name", "ndfs_filepath", "vmdisk_uuid", "hypervisor_vmdisk_uuid", "volume_group_uuid", "device_index", "disk_label", "device_bus", "is_cdrom", "is_scsi_passthrough", "is_empty", "flash_mode_enabled", "datasource_uuid", "external_disk_url")
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    NDFS_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    VMDISK_UUID_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_VMDISK_UUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISK_LABEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BUS_FIELD_NUMBER: _ClassVar[int]
    IS_CDROM_FIELD_NUMBER: _ClassVar[int]
    IS_SCSI_PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
    IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
    FLASH_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DISK_URL_FIELD_NUMBER: _ClassVar[int]
    disk_size_bytes: int
    device_type: str
    storage_container_uuid: str
    storage_container_name: str
    ndfs_filepath: str
    vmdisk_uuid: str
    hypervisor_vmdisk_uuid: str
    volume_group_uuid: str
    device_index: int
    disk_label: str
    device_bus: str
    is_cdrom: bool
    is_scsi_passthrough: bool
    is_empty: bool
    flash_mode_enabled: bool
    datasource_uuid: str
    external_disk_url: str
    def __init__(self, disk_size_bytes: _Optional[int] = ..., device_type: _Optional[str] = ..., storage_container_uuid: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., ndfs_filepath: _Optional[str] = ..., vmdisk_uuid: _Optional[str] = ..., hypervisor_vmdisk_uuid: _Optional[str] = ..., volume_group_uuid: _Optional[str] = ..., device_index: _Optional[int] = ..., disk_label: _Optional[str] = ..., device_bus: _Optional[str] = ..., is_cdrom: bool = ..., is_scsi_passthrough: bool = ..., is_empty: bool = ..., flash_mode_enabled: bool = ..., datasource_uuid: _Optional[str] = ..., external_disk_url: _Optional[str] = ...) -> None: ...

class VMNicConfig(_message.Message):
    __slots__ = ("nic_type", "mac_address", "network_uuid", "request_ip", "requested_ip_address", "model", "ip_address", "is_connected")
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_IP_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    nic_type: str
    mac_address: str
    network_uuid: str
    request_ip: bool
    requested_ip_address: str
    model: str
    ip_address: str
    is_connected: bool
    def __init__(self, nic_type: _Optional[str] = ..., mac_address: _Optional[str] = ..., network_uuid: _Optional[str] = ..., request_ip: bool = ..., requested_ip_address: _Optional[str] = ..., model: _Optional[str] = ..., ip_address: _Optional[str] = ..., is_connected: bool = ...) -> None: ...

class DiskAddress(_message.Message):
    __slots__ = ("ndfs_filepath", "vmdisk_uuid", "volume_group_uuid", "device_index", "disk_label", "device_bus", "device_uuid", "is_cdrom")
    NDFS_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    VMDISK_UUID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISK_LABEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_UUID_FIELD_NUMBER: _ClassVar[int]
    IS_CDROM_FIELD_NUMBER: _ClassVar[int]
    ndfs_filepath: str
    vmdisk_uuid: str
    volume_group_uuid: str
    device_index: int
    disk_label: str
    device_bus: str
    device_uuid: str
    is_cdrom: bool
    def __init__(self, ndfs_filepath: _Optional[str] = ..., vmdisk_uuid: _Optional[str] = ..., volume_group_uuid: _Optional[str] = ..., device_index: _Optional[int] = ..., disk_label: _Optional[str] = ..., device_bus: _Optional[str] = ..., device_uuid: _Optional[str] = ..., is_cdrom: bool = ...) -> None: ...

class VMDetails(_message.Message):
    __slots__ = ("memory_size_mb", "memory_reservation_size_mb", "hypervisor_type", "host_uuid", "num_sockets", "num_vcpus_per_socket", "nic_vec", "timezone", "vm_gpu_vec", "power_state", "vcpu_reservation_hz", "allow_live_migrate", "boot_device_type", "mac_address", "disk_address", "num_vcpus", "num_cores_per_vcpu", "memory_size_mib", "uefi_boot", "boot_device_order", "affinity", "gpus_assigned", "description")
    class VMGpuConfig(_message.Message):
        __slots__ = ("in_use", "device_name", "device_id", "assignable", "fraction", "frame_buffer_size_bytes", "gpu_mode", "gpu_profile", "gpu_type", "gpu_vendor", "guest_driver_version", "max_instances_per_vm", "max_resolution", "num_virtual_display_heads", "numa_node", "sbdf", "licenses_vec", "vm_uuids_vec")
        IN_USE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        ASSIGNABLE_FIELD_NUMBER: _ClassVar[int]
        FRACTION_FIELD_NUMBER: _ClassVar[int]
        FRAME_BUFFER_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        GPU_MODE_FIELD_NUMBER: _ClassVar[int]
        GPU_PROFILE_FIELD_NUMBER: _ClassVar[int]
        GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
        GPU_VENDOR_FIELD_NUMBER: _ClassVar[int]
        GUEST_DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
        MAX_INSTANCES_PER_VM_FIELD_NUMBER: _ClassVar[int]
        MAX_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        NUM_VIRTUAL_DISPLAY_HEADS_FIELD_NUMBER: _ClassVar[int]
        NUMA_NODE_FIELD_NUMBER: _ClassVar[int]
        SBDF_FIELD_NUMBER: _ClassVar[int]
        LICENSES_VEC_FIELD_NUMBER: _ClassVar[int]
        VM_UUIDS_VEC_FIELD_NUMBER: _ClassVar[int]
        in_use: bool
        device_name: str
        device_id: int
        assignable: bool
        fraction: int
        frame_buffer_size_bytes: int
        gpu_mode: str
        gpu_profile: str
        gpu_type: str
        gpu_vendor: str
        guest_driver_version: str
        max_instances_per_vm: int
        max_resolution: str
        num_virtual_display_heads: int
        numa_node: int
        sbdf: str
        licenses_vec: _containers.RepeatedScalarFieldContainer[str]
        vm_uuids_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, in_use: bool = ..., device_name: _Optional[str] = ..., device_id: _Optional[int] = ..., assignable: bool = ..., fraction: _Optional[int] = ..., frame_buffer_size_bytes: _Optional[int] = ..., gpu_mode: _Optional[str] = ..., gpu_profile: _Optional[str] = ..., gpu_type: _Optional[str] = ..., gpu_vendor: _Optional[str] = ..., guest_driver_version: _Optional[str] = ..., max_instances_per_vm: _Optional[int] = ..., max_resolution: _Optional[str] = ..., num_virtual_display_heads: _Optional[int] = ..., numa_node: _Optional[int] = ..., sbdf: _Optional[str] = ..., licenses_vec: _Optional[_Iterable[str]] = ..., vm_uuids_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    MEMORY_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_RESERVATION_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    NUM_SOCKETS_FIELD_NUMBER: _ClassVar[int]
    NUM_VCPUS_PER_SOCKET_FIELD_NUMBER: _ClassVar[int]
    NIC_VEC_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    VM_GPU_VEC_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    VCPU_RESERVATION_HZ_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LIVE_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NUM_VCPUS_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_PER_VCPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_MIB_FIELD_NUMBER: _ClassVar[int]
    UEFI_BOOT_FIELD_NUMBER: _ClassVar[int]
    BOOT_DEVICE_ORDER_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_FIELD_NUMBER: _ClassVar[int]
    GPUS_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    memory_size_mb: int
    memory_reservation_size_mb: int
    hypervisor_type: HypervisorType.Type
    host_uuid: str
    num_sockets: int
    num_vcpus_per_socket: int
    nic_vec: _containers.RepeatedCompositeFieldContainer[VMNicConfig]
    timezone: str
    vm_gpu_vec: _containers.RepeatedCompositeFieldContainer[VMDetails.VMGpuConfig]
    power_state: PowerState.Type
    vcpu_reservation_hz: int
    allow_live_migrate: bool
    boot_device_type: str
    mac_address: str
    disk_address: DiskAddress
    num_vcpus: int
    num_cores_per_vcpu: int
    memory_size_mib: int
    uefi_boot: bool
    boot_device_order: _containers.RepeatedScalarFieldContainer[str]
    affinity: Affinity
    gpus_assigned: bool
    description: str
    def __init__(self, memory_size_mb: _Optional[int] = ..., memory_reservation_size_mb: _Optional[int] = ..., hypervisor_type: _Optional[_Union[HypervisorType.Type, str]] = ..., host_uuid: _Optional[str] = ..., num_sockets: _Optional[int] = ..., num_vcpus_per_socket: _Optional[int] = ..., nic_vec: _Optional[_Iterable[_Union[VMNicConfig, _Mapping]]] = ..., timezone: _Optional[str] = ..., vm_gpu_vec: _Optional[_Iterable[_Union[VMDetails.VMGpuConfig, _Mapping]]] = ..., power_state: _Optional[_Union[PowerState.Type, str]] = ..., vcpu_reservation_hz: _Optional[int] = ..., allow_live_migrate: bool = ..., boot_device_type: _Optional[str] = ..., mac_address: _Optional[str] = ..., disk_address: _Optional[_Union[DiskAddress, _Mapping]] = ..., num_vcpus: _Optional[int] = ..., num_cores_per_vcpu: _Optional[int] = ..., memory_size_mib: _Optional[int] = ..., uefi_boot: bool = ..., boot_device_order: _Optional[_Iterable[str]] = ..., affinity: _Optional[_Union[Affinity, _Mapping]] = ..., gpus_assigned: bool = ..., description: _Optional[str] = ...) -> None: ...

class Affinity(_message.Message):
    __slots__ = ("policy", "host_uuids")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    HOST_UUIDS_FIELD_NUMBER: _ClassVar[int]
    policy: str
    host_uuids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, policy: _Optional[str] = ..., host_uuids: _Optional[_Iterable[str]] = ...) -> None: ...

class GuestToolsInfo(_message.Message):
    __slots__ = ("nutanix_guest_tools",)
    class NGTInfo(_message.Message):
        __slots__ = ("available_version", "ngt_state", "iso_mount_state", "state", "version", "enabled_capability_list", "guest_os_version", "is_reachable")
        AVAILABLE_VERSION_FIELD_NUMBER: _ClassVar[int]
        NGT_STATE_FIELD_NUMBER: _ClassVar[int]
        ISO_MOUNT_STATE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ENABLED_CAPABILITY_LIST_FIELD_NUMBER: _ClassVar[int]
        GUEST_OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        IS_REACHABLE_FIELD_NUMBER: _ClassVar[int]
        available_version: str
        ngt_state: str
        iso_mount_state: str
        state: str
        version: str
        enabled_capability_list: _containers.RepeatedScalarFieldContainer[str]
        guest_os_version: str
        is_reachable: bool
        def __init__(self, available_version: _Optional[str] = ..., ngt_state: _Optional[str] = ..., iso_mount_state: _Optional[str] = ..., state: _Optional[str] = ..., version: _Optional[str] = ..., enabled_capability_list: _Optional[_Iterable[str]] = ..., guest_os_version: _Optional[str] = ..., is_reachable: bool = ...) -> None: ...
    NUTANIX_GUEST_TOOLS_FIELD_NUMBER: _ClassVar[int]
    nutanix_guest_tools: GuestToolsInfo.NGTInfo
    def __init__(self, nutanix_guest_tools: _Optional[_Union[GuestToolsInfo.NGTInfo, _Mapping]] = ...) -> None: ...

class VMEntity(_message.Message):
    __slots__ = ("vm_config", "disk_config_vec", "user_excluded_disk_config_vec", "agent_vm", "flash_mode", "guest_tools")
    VM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISK_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUDED_DISK_CONFIG_VEC_FIELD_NUMBER: _ClassVar[int]
    AGENT_VM_FIELD_NUMBER: _ClassVar[int]
    FLASH_MODE_FIELD_NUMBER: _ClassVar[int]
    GUEST_TOOLS_FIELD_NUMBER: _ClassVar[int]
    vm_config: EntityMetadataConf
    disk_config_vec: _containers.RepeatedCompositeFieldContainer[DiskConfig]
    user_excluded_disk_config_vec: _containers.RepeatedCompositeFieldContainer[DiskConfig]
    agent_vm: bool
    flash_mode: bool
    guest_tools: GuestToolsInfo
    def __init__(self, vm_config: _Optional[_Union[EntityMetadataConf, _Mapping]] = ..., disk_config_vec: _Optional[_Iterable[_Union[DiskConfig, _Mapping]]] = ..., user_excluded_disk_config_vec: _Optional[_Iterable[_Union[DiskConfig, _Mapping]]] = ..., agent_vm: bool = ..., flash_mode: bool = ..., guest_tools: _Optional[_Union[GuestToolsInfo, _Mapping]] = ...) -> None: ...

class VMListArg(_message.Message):
    __slots__ = ("cluster_uuid", "filter", "kind", "sort_order", "offset", "length", "sort_attr")
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    SORT_ATTR_FIELD_NUMBER: _ClassVar[int]
    cluster_uuid: str
    filter: str
    kind: str
    sort_order: str
    offset: int
    length: int
    sort_attr: str
    def __init__(self, cluster_uuid: _Optional[str] = ..., filter: _Optional[str] = ..., kind: _Optional[str] = ..., sort_order: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., sort_attr: _Optional[str] = ...) -> None: ...

class VMListResult(_message.Message):
    __slots__ = ("error", "cluster_vec")
    class ClusterVMs(_message.Message):
        __slots__ = ("cluster_uuid", "vm_vec")
        CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
        VM_VEC_FIELD_NUMBER: _ClassVar[int]
        cluster_uuid: str
        vm_vec: _containers.RepeatedCompositeFieldContainer[VMEntity]
        def __init__(self, cluster_uuid: _Optional[str] = ..., vm_vec: _Optional[_Iterable[_Union[VMEntity, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cluster_vec: _containers.RepeatedCompositeFieldContainer[VMListResult.ClusterVMs]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cluster_vec: _Optional[_Iterable[_Union[VMListResult.ClusterVMs, _Mapping]]] = ...) -> None: ...

class VMInfoArg(_message.Message):
    __slots__ = ("vm_uuid", "include_vmdisk_vmnic_config", "include_hypervisor_vdisk_uuid", "include_nutanix_guest_tools_info", "get_vm_with_gpu_config", "acropolis_disk_exclusion_info", "acropolis_disk_inclusion_info")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VMDISK_VMNIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HYPERVISOR_VDISK_UUID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NUTANIX_GUEST_TOOLS_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_VM_WITH_GPU_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    include_vmdisk_vmnic_config: bool
    include_hypervisor_vdisk_uuid: bool
    include_nutanix_guest_tools_info: bool
    get_vm_with_gpu_config: bool
    acropolis_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.AcropolisDiskFilterProto]
    acropolis_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.AcropolisDiskFilterProto]
    def __init__(self, vm_uuid: _Optional[str] = ..., include_vmdisk_vmnic_config: bool = ..., include_hypervisor_vdisk_uuid: bool = ..., include_nutanix_guest_tools_info: bool = ..., get_vm_with_gpu_config: bool = ..., acropolis_disk_exclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.AcropolisDiskFilterProto, _Mapping]]] = ..., acropolis_disk_inclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.AcropolisDiskFilterProto, _Mapping]]] = ...) -> None: ...

class VMInfoResult(_message.Message):
    __slots__ = ("error", "entity", "vm_details")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity: VMEntity
    vm_details: VMDetails
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity: _Optional[_Union[VMEntity, _Mapping]] = ..., vm_details: _Optional[_Union[VMDetails, _Mapping]] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ("storage_container_uuid", "name", "max_capacity_bytes", "cluster_uuid")
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    storage_container_uuid: str
    name: str
    max_capacity_bytes: int
    cluster_uuid: str
    def __init__(self, storage_container_uuid: _Optional[str] = ..., name: _Optional[str] = ..., max_capacity_bytes: _Optional[int] = ..., cluster_uuid: _Optional[str] = ...) -> None: ...

class ContainerListArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContainerListResult(_message.Message):
    __slots__ = ("error", "entity_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[Container]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[Container, _Mapping]]] = ...) -> None: ...

class Network(_message.Message):
    __slots__ = ("uuid", "name", "network_address", "default_gateway")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    network_address: str
    default_gateway: str
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., network_address: _Optional[str] = ..., default_gateway: _Optional[str] = ...) -> None: ...

class NetworkListArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkListResult(_message.Message):
    __slots__ = ("error", "entity_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[Network]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[Network, _Mapping]]] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("name", "uuid", "memory_capacity_in_bytes", "controller_vm_backplane_ip")
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MEMORY_CAPACITY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_VM_BACKPLANE_IP_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    memory_capacity_in_bytes: int
    controller_vm_backplane_ip: str
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., memory_capacity_in_bytes: _Optional[int] = ..., controller_vm_backplane_ip: _Optional[str] = ...) -> None: ...

class HostListArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HostListResult(_message.Message):
    __slots__ = ("error", "entity_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_vec: _containers.RepeatedCompositeFieldContainer[Host]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[Host, _Mapping]]] = ...) -> None: ...

class SetVMPowerStateArg(_message.Message):
    __slots__ = ("vm_uuid", "power_state")
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    vm_uuid: str
    power_state: PowerState.Type
    def __init__(self, vm_uuid: _Optional[str] = ..., power_state: _Optional[_Union[PowerState.Type, str]] = ...) -> None: ...

class SetVMPowerStateResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteExternalRepoArg(_message.Message):
    __slots__ = ("external_repo_uuid",)
    EXTERNAL_REPO_UUID_FIELD_NUMBER: _ClassVar[int]
    external_repo_uuid: str
    def __init__(self, external_repo_uuid: _Optional[str] = ...) -> None: ...

class DeleteExternalRepoResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ExternalRepoListArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalRepoListResult(_message.Message):
    __slots__ = ("error", "num_external_repo")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_EXTERNAL_REPO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    num_external_repo: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., num_external_repo: _Optional[int] = ...) -> None: ...

class GetDatasourceInfoArg(_message.Message):
    __slots__ = ("datasource_uuid",)
    DATASOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    datasource_uuid: str
    def __init__(self, datasource_uuid: _Optional[str] = ...) -> None: ...

class GetDatasourceInfoResult(_message.Message):
    __slots__ = ("error", "datasource_state", "task_uuid", "container_uuid", "external_repository_uuid", "datasource_uuid", "datasource_size", "datasource_usage_mode", "background_migration_suspended", "background_migration_enabled", "spec_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REPOSITORY_UUID_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_USAGE_MODE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MIGRATION_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MIGRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SPEC_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    datasource_state: DatasourceState.Type
    task_uuid: str
    container_uuid: str
    external_repository_uuid: str
    datasource_uuid: str
    datasource_size: int
    datasource_usage_mode: str
    background_migration_suspended: bool
    background_migration_enabled: bool
    spec_version: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., datasource_state: _Optional[_Union[DatasourceState.Type, str]] = ..., task_uuid: _Optional[str] = ..., container_uuid: _Optional[str] = ..., external_repository_uuid: _Optional[str] = ..., datasource_uuid: _Optional[str] = ..., datasource_size: _Optional[int] = ..., datasource_usage_mode: _Optional[str] = ..., background_migration_suspended: bool = ..., background_migration_enabled: bool = ..., spec_version: _Optional[int] = ...) -> None: ...

class ConfigureStorageMigrationArg(_message.Message):
    __slots__ = ("datasource_uuid", "background_migration_suspended", "background_migration_enabled")
    DATASOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MIGRATION_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MIGRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    datasource_uuid: str
    background_migration_suspended: bool
    background_migration_enabled: bool
    def __init__(self, datasource_uuid: _Optional[str] = ..., background_migration_suspended: bool = ..., background_migration_enabled: bool = ...) -> None: ...

class ConfigureStorageMigrationResult(_message.Message):
    __slots__ = ("error", "datasource_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    datasource_info: GetDatasourceInfoResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., datasource_info: _Optional[_Union[GetDatasourceInfoResult, _Mapping]] = ...) -> None: ...

class WaitForTaskFinishArg(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class WaitForTaskFinishResult(_message.Message):
    __slots__ = ("error", "status", "progress_message", "percentage_complete", "task_uuid")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    status: str
    progress_message: str
    percentage_complete: int
    task_uuid: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[str] = ..., progress_message: _Optional[str] = ..., percentage_complete: _Optional[int] = ..., task_uuid: _Optional[str] = ...) -> None: ...
