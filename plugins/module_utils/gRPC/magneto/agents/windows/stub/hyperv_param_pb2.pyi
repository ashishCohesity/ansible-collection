from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from magneto.agents.windows.base import hyperv_pb2 as _hyperv_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import hyperv_pb2 as _hyperv_pb2_1
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from util import cbt_delta_pb2 as _cbt_delta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HyperVAccessParams(_message.Message):
    __slots__ = ("endpoint", "username", "password", "type")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    username: str
    password: str
    type: _hyperv_pb2_1.Entity.Type
    def __init__(self, endpoint: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., type: _Optional[_Union[_hyperv_pb2_1.Entity.Type, str]] = ...) -> None: ...

class HyperVGuestAccessParams(_message.Message):
    __slots__ = ("endpoint", "username", "password", "hyperv_vm_id", "is_guest", "exec_path", "guest_os_type", "access_state", "additional_rpc_args", "ip_address_vec")
    class GuestOsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWindows: _ClassVar[HyperVGuestAccessParams.GuestOsType]
        kLinux: _ClassVar[HyperVGuestAccessParams.GuestOsType]
        kUnknown: _ClassVar[HyperVGuestAccessParams.GuestOsType]
    kWindows: HyperVGuestAccessParams.GuestOsType
    kLinux: HyperVGuestAccessParams.GuestOsType
    kUnknown: HyperVGuestAccessParams.GuestOsType
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    IS_GUEST_FIELD_NUMBER: _ClassVar[int]
    EXEC_PATH_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_STATE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_RPC_ARGS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    username: str
    password: str
    hyperv_vm_id: str
    is_guest: bool
    exec_path: str
    guest_os_type: HyperVGuestAccessParams.GuestOsType
    access_state: HyperVAccessState
    additional_rpc_args: str
    ip_address_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, endpoint: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., hyperv_vm_id: _Optional[str] = ..., is_guest: bool = ..., exec_path: _Optional[str] = ..., guest_os_type: _Optional[_Union[HyperVGuestAccessParams.GuestOsType, str]] = ..., access_state: _Optional[_Union[HyperVAccessState, _Mapping]] = ..., additional_rpc_args: _Optional[str] = ..., ip_address_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class HyperVAccessState(_message.Message):
    __slots__ = ("process_id", "guest_tmp_dir")
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    GUEST_TMP_DIR_FIELD_NUMBER: _ClassVar[int]
    process_id: int
    guest_tmp_dir: str
    def __init__(self, process_id: _Optional[int] = ..., guest_tmp_dir: _Optional[str] = ...) -> None: ...

class GetHyperVHierarchyArg(_message.Message):
    __slots__ = ("header", "access_params", "return_unsupported_vms", "minimal")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETURN_UNSUPPORTED_VMS_FIELD_NUMBER: _ClassVar[int]
    MINIMAL_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    return_unsupported_vms: bool
    minimal: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., return_unsupported_vms: bool = ..., minimal: bool = ...) -> None: ...

class GetHyperVHierarchyResult(_message.Message):
    __slots__ = ("error", "entity_hierarchy")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ...) -> None: ...

class CreateVMCheckpointArg(_message.Message):
    __slots__ = ("header", "access_params", "hyperv_vm_id", "checkpoint_name", "quiesce", "allow_crash_consistent_snapshot", "is_vss_copy_only")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    QUIESCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CRASH_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    IS_VSS_COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    hyperv_vm_id: str
    checkpoint_name: str
    quiesce: bool
    allow_crash_consistent_snapshot: bool
    is_vss_copy_only: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., hyperv_vm_id: _Optional[str] = ..., checkpoint_name: _Optional[str] = ..., quiesce: bool = ..., allow_crash_consistent_snapshot: bool = ..., is_vss_copy_only: bool = ...) -> None: ...

class CreateVMCheckpointResult(_message.Message):
    __slots__ = ("error", "checkpoint_instance_id", "is_app_consistent")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_APP_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    checkpoint_instance_id: bytes
    is_app_consistent: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., checkpoint_instance_id: _Optional[bytes] = ..., is_app_consistent: bool = ...) -> None: ...

class DeleteVMCheckpointArg(_message.Message):
    __slots__ = ("header", "access_params", "hyperv_vm_id", "checkpoint_instance_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    hyperv_vm_id: str
    checkpoint_instance_id: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., hyperv_vm_id: _Optional[str] = ..., checkpoint_instance_id: _Optional[bytes] = ...) -> None: ...

class DeleteVMCheckpointResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetCheckpointInfoArg(_message.Message):
    __slots__ = ("header", "access_params", "hyperv_vm_id", "checkpoint_instance_id", "hyperv_disk_exclusion_info", "hyperv_disk_inclusion_info")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    hyperv_vm_id: str
    checkpoint_instance_id: bytes
    hyperv_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.HyperVDiskFilterProto]
    hyperv_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.HyperVDiskFilterProto]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., hyperv_vm_id: _Optional[str] = ..., checkpoint_instance_id: _Optional[bytes] = ..., hyperv_disk_exclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.HyperVDiskFilterProto, _Mapping]]] = ..., hyperv_disk_inclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.HyperVDiskFilterProto, _Mapping]]] = ...) -> None: ...

class GetCheckpointInfoResult(_message.Message):
    __slots__ = ("error", "checkpoint_info", "vm_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    checkpoint_info: _hyperv_pb2.CheckpointInfo
    vm_info: _hyperv_pb2.HyperVVMInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., checkpoint_info: _Optional[_Union[_hyperv_pb2.CheckpointInfo, _Mapping]] = ..., vm_info: _Optional[_Union[_hyperv_pb2.HyperVVMInfo, _Mapping]] = ...) -> None: ...

class GetCheckpointVMConfigArg(_message.Message):
    __slots__ = ("header", "vm_config_file_vec", "fail_on_large_config_file")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    FAIL_ON_LARGE_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    vm_config_file_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.VMConfigFile]
    fail_on_large_config_file: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., vm_config_file_vec: _Optional[_Iterable[_Union[_hyperv_pb2.VMConfigFile, _Mapping]]] = ..., fail_on_large_config_file: bool = ...) -> None: ...

class GetCheckpointVMConfigResult(_message.Message):
    __slots__ = ("error", "vm_config_file_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_CONFIG_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_config_file_info_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.VMConfigFileInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_config_file_info_vec: _Optional[_Iterable[_Union[_hyperv_pb2.VMConfigFileInfo, _Mapping]]] = ...) -> None: ...

class LocateVMArg(_message.Message):
    __slots__ = ("header", "access_params", "vm_uuid")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    vm_uuid: bytes
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., vm_uuid: _Optional[bytes] = ...) -> None: ...

class LocateVMResult(_message.Message):
    __slots__ = ("error", "vm_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_info: _hyperv_pb2.HyperVVMInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_info: _Optional[_Union[_hyperv_pb2.HyperVVMInfo, _Mapping]] = ...) -> None: ...

class GetVirtualDiskChangesArg(_message.Message):
    __slots__ = ("header", "disk_full_path", "previous_rct_id", "offset", "length")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DISK_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RCT_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    disk_full_path: str
    previous_rct_id: bytes
    offset: int
    length: int
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., disk_full_path: _Optional[str] = ..., previous_rct_id: _Optional[bytes] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class GetVirtualDiskChangesResult(_message.Message):
    __slots__ = ("error", "delta_type", "delta_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DELTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELTA_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    delta_type: _cbt_delta_pb2.CBTDeltaType.Type
    delta_info: _cbt_delta_pb2.CBTDeltaInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., delta_type: _Optional[_Union[_cbt_delta_pb2.CBTDeltaType.Type, str]] = ..., delta_info: _Optional[_Union[_cbt_delta_pb2.CBTDeltaInfo, _Mapping]] = ...) -> None: ...

class ReadVirtualDiskArg(_message.Message):
    __slots__ = ("header", "disk_full_path", "offset", "length", "optimize_zero_filled_reads", "rpc_stats")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DISK_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_ZERO_FILLED_READS_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    disk_full_path: str
    offset: int
    length: int
    optimize_zero_filled_reads: bool
    rpc_stats: _agent_pb2.RpcStats
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., disk_full_path: _Optional[str] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., optimize_zero_filled_reads: bool = ..., rpc_stats: _Optional[_Union[_agent_pb2.RpcStats, _Mapping]] = ...) -> None: ...

class ReadVirtualDiskResult(_message.Message):
    __slots__ = ("error", "data", "is_data_zero_filled", "length", "io_latency_usecs", "rpc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_DATA_ZERO_FILLED_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    IO_LATENCY_USECS_FIELD_NUMBER: _ClassVar[int]
    RPC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    data: bytes
    is_data_zero_filled: bool
    length: int
    io_latency_usecs: int
    rpc_stats: _agent_pb2.RpcStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., data: _Optional[bytes] = ..., is_data_zero_filled: bool = ..., length: _Optional[int] = ..., io_latency_usecs: _Optional[int] = ..., rpc_stats: _Optional[_Union[_agent_pb2.RpcStats, _Mapping]] = ...) -> None: ...

class DetachVirtualDiskArg(_message.Message):
    __slots__ = ("header", "virtual_disk_path_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    virtual_disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., virtual_disk_path_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DetachVirtualDiskResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ConvertToReferencePointArg(_message.Message):
    __slots__ = ("header", "access_params", "hyperv_vm_id", "checkpoint_instance_id", "previous_reference_point_id", "virtual_disk_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_REFERENCE_POINT_ID_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    hyperv_vm_id: str
    checkpoint_instance_id: bytes
    previous_reference_point_id: bytes
    virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.VirtualDisk]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., hyperv_vm_id: _Optional[str] = ..., checkpoint_instance_id: _Optional[bytes] = ..., previous_reference_point_id: _Optional[bytes] = ..., virtual_disk_vec: _Optional[_Iterable[_Union[_hyperv_pb2.VirtualDisk, _Mapping]]] = ...) -> None: ...

class ConvertToReferencePointResult(_message.Message):
    __slots__ = ("error", "vm_reference_point")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_REFERENCE_POINT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_reference_point: _hyperv_pb2.VMReferencePoint
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_reference_point: _Optional[_Union[_hyperv_pb2.VMReferencePoint, _Mapping]] = ...) -> None: ...

class GetHostClusterInfoArg(_message.Message):
    __slots__ = ("header", "access_params", "entity_vec")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    entity_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2_1.Entity]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., entity_vec: _Optional[_Iterable[_Union[_hyperv_pb2_1.Entity, _Mapping]]] = ...) -> None: ...

class GetHostClusterInfoResult(_message.Message):
    __slots__ = ("error", "hyperv_host_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HYPERV_HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    hyperv_host_info_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.HyperVHostInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., hyperv_host_info_vec: _Optional[_Iterable[_Union[_hyperv_pb2.HyperVHostInfo, _Mapping]]] = ...) -> None: ...

class ImportVMArg(_message.Message):
    __slots__ = ("header", "restore_vm_params")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    restore_vm_params: _hyperv_pb2.RestoreVMParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., restore_vm_params: _Optional[_Union[_hyperv_pb2.RestoreVMParams, _Mapping]] = ...) -> None: ...

class ImportVMResult(_message.Message):
    __slots__ = ("error", "restore_vm_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ...) -> None: ...

class MigrateVMStorageArg(_message.Message):
    __slots__ = ("header", "restore_vm_handle")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ...) -> None: ...

class MigrateVMStorageResult(_message.Message):
    __slots__ = ("error", "restore_vm_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ...) -> None: ...

class RealizeVMArg(_message.Message):
    __slots__ = ("header", "restore_vm_handle")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ...) -> None: ...

class RealizeVMResult(_message.Message):
    __slots__ = ("error", "restore_vm_handle", "poweron_error", "makehighlyavailable_error")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    POWERON_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAKEHIGHLYAVAILABLE_ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    poweron_error: _error_pb2.ErrorProto
    makehighlyavailable_error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ..., poweron_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., makehighlyavailable_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetClonedVMInfoArg(_message.Message):
    __slots__ = ("header", "access_params", "host_uuid", "hyperv_vm_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    host_uuid: str
    hyperv_vm_id: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., host_uuid: _Optional[str] = ..., hyperv_vm_id: _Optional[str] = ...) -> None: ...

class GetClonedVMInfoResult(_message.Message):
    __slots__ = ("error", "vm_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VM_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    vm_info: _hyperv_pb2.HyperVVMInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., vm_info: _Optional[_Union[_hyperv_pb2.HyperVVMInfo, _Mapping]] = ...) -> None: ...

class GetVMStorageMigrationProgressArg(_message.Message):
    __slots__ = ("header", "restore_vm_handle", "cancel_vm_storage_migration")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_VM_STORAGE_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    cancel_vm_storage_migration: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ..., cancel_vm_storage_migration: bool = ...) -> None: ...

class GetVMStorageMigrationProgressResult(_message.Message):
    __slots__ = ("error", "restore_vm_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ...) -> None: ...

class FinalizeVMArg(_message.Message):
    __slots__ = ("header", "restore_vm_handle", "should_commit")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_VM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_COMMIT_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    restore_vm_handle: _hyperv_pb2.RestoreVMHandle
    should_commit: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., restore_vm_handle: _Optional[_Union[_hyperv_pb2.RestoreVMHandle, _Mapping]] = ..., should_commit: bool = ...) -> None: ...

class GetVMVSSSnapshotArg(_message.Message):
    __slots__ = ("header", "snapshot_set_id", "hyperv_vm_id", "hyperv_disk_exclusion_info", "hyperv_disk_inclusion_info")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_SET_ID_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    snapshot_set_id: bytes
    hyperv_vm_id: str
    hyperv_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.HyperVDiskFilterProto]
    hyperv_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[_env_params_pb2.HyperVDiskFilterProto]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., snapshot_set_id: _Optional[bytes] = ..., hyperv_vm_id: _Optional[str] = ..., hyperv_disk_exclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.HyperVDiskFilterProto, _Mapping]]] = ..., hyperv_disk_inclusion_info: _Optional[_Iterable[_Union[_env_params_pb2.HyperVDiskFilterProto, _Mapping]]] = ...) -> None: ...

class GetVMVSSSnapshotResult(_message.Message):
    __slots__ = ("error", "server_snapshot_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERVER_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    server_snapshot_info: _agent_pb2.ServerSnapshotInfo
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., server_snapshot_info: _Optional[_Union[_agent_pb2.ServerSnapshotInfo, _Mapping]] = ...) -> None: ...

class CreateTempFileInGuestArg(_message.Message):
    __slots__ = ("header", "is_directory", "directory_path", "prefix", "suffix", "guest_access_params")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    is_directory: bool
    directory_path: str
    prefix: str
    suffix: str
    guest_access_params: HyperVGuestAccessParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., is_directory: bool = ..., directory_path: _Optional[str] = ..., prefix: _Optional[str] = ..., suffix: _Optional[str] = ..., guest_access_params: _Optional[_Union[HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class CreateTempFileInGuestResult(_message.Message):
    __slots__ = ("error", "temp_fullpath")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEMP_FULLPATH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    temp_fullpath: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., temp_fullpath: _Optional[str] = ...) -> None: ...

class PushFileToGuestArg(_message.Message):
    __slots__ = ("header", "hyperv_vm_id", "file_info_vec")
    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWindowsAgentService: _ClassVar[PushFileToGuestArg.FileType]
        kParamsFile: _ClassVar[PushFileToGuestArg.FileType]
    kWindowsAgentService: PushFileToGuestArg.FileType
    kParamsFile: PushFileToGuestArg.FileType
    class FileInfo(_message.Message):
        __slots__ = ("local_file_path", "remote_file_path", "overwrite_file", "create_remote_file_path", "file_type")
        LOCAL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        REMOTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        OVERWRITE_FILE_FIELD_NUMBER: _ClassVar[int]
        CREATE_REMOTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        local_file_path: str
        remote_file_path: str
        overwrite_file: bool
        create_remote_file_path: bool
        file_type: PushFileToGuestArg.FileType
        def __init__(self, local_file_path: _Optional[str] = ..., remote_file_path: _Optional[str] = ..., overwrite_file: bool = ..., create_remote_file_path: bool = ..., file_type: _Optional[_Union[PushFileToGuestArg.FileType, str]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    hyperv_vm_id: str
    file_info_vec: _containers.RepeatedCompositeFieldContainer[PushFileToGuestArg.FileInfo]
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., hyperv_vm_id: _Optional[str] = ..., file_info_vec: _Optional[_Iterable[_Union[PushFileToGuestArg.FileInfo, _Mapping]]] = ...) -> None: ...

class PushFileToGuestResult(_message.Message):
    __slots__ = ("error", "file_result_vec")
    class FileResult(_message.Message):
        __slots__ = ("remote_file_path", "error")
        REMOTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        remote_file_path: str
        error: _error_pb2.ErrorProto
        def __init__(self, remote_file_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_result_vec: _containers.RepeatedCompositeFieldContainer[PushFileToGuestResult.FileResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_result_vec: _Optional[_Iterable[_Union[PushFileToGuestResult.FileResult, _Mapping]]] = ...) -> None: ...

class FetchVMDiskDeviceInfoArg(_message.Message):
    __slots__ = ("header",)
    HEADER_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ...) -> None: ...

class FetchVMDiskDeviceInfoResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class FetchFilesFromGuestArg(_message.Message):
    __slots__ = ("header", "file_type", "host_file_directory", "guest_access_params")
    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kWindowsAgentServiceLog: _ClassVar[FetchFilesFromGuestArg.FileType]
        kScript: _ClassVar[FetchFilesFromGuestArg.FileType]
    kWindowsAgentServiceLog: FetchFilesFromGuestArg.FileType
    kScript: FetchFilesFromGuestArg.FileType
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_FILE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    file_type: FetchFilesFromGuestArg.FileType
    host_file_directory: str
    guest_access_params: HyperVGuestAccessParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., file_type: _Optional[_Union[FetchFilesFromGuestArg.FileType, str]] = ..., host_file_directory: _Optional[str] = ..., guest_access_params: _Optional[_Union[HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class FetchFilesFromGuestResult(_message.Message):
    __slots__ = ("error", "cohesity_agent_log_file_dir", "file_result_vec")
    class FileResult(_message.Message):
        __slots__ = ("guest_file_path", "error")
        GUEST_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        guest_file_path: str
        error: _error_pb2.ErrorProto
        def __init__(self, guest_file_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COHESITY_AGENT_LOG_FILE_DIR_FIELD_NUMBER: _ClassVar[int]
    FILE_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cohesity_agent_log_file_dir: str
    file_result_vec: _containers.RepeatedCompositeFieldContainer[FetchFilesFromGuestResult.FileResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cohesity_agent_log_file_dir: _Optional[str] = ..., file_result_vec: _Optional[_Iterable[_Union[FetchFilesFromGuestResult.FileResult, _Mapping]]] = ...) -> None: ...

class StartProgramInGuestArg(_message.Message):
    __slots__ = ("header", "hyperv_vm_id", "credentials", "program_fullpath", "arguments", "working_directory_path")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_FULLPATH_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    hyperv_vm_id: str
    credentials: _credentials_pb2.Credentials
    program_fullpath: str
    arguments: str
    working_directory_path: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., hyperv_vm_id: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., program_fullpath: _Optional[str] = ..., arguments: _Optional[str] = ..., working_directory_path: _Optional[str] = ...) -> None: ...

class StartProgramInGuestResult(_message.Message):
    __slots__ = ("error", "process_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    process_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., process_id: _Optional[int] = ...) -> None: ...

class ListProcessesInGuestArg(_message.Message):
    __slots__ = ("header", "process_id", "process_name_prefix", "guest_access_params")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    process_id: int
    process_name_prefix: str
    guest_access_params: HyperVGuestAccessParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., process_id: _Optional[int] = ..., process_name_prefix: _Optional[str] = ..., guest_access_params: _Optional[_Union[HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class ListProcessesInGuestResult(_message.Message):
    __slots__ = ("error", "process_info_vec")
    class ProcessInfo(_message.Message):
        __slots__ = ("process_id", "process_name", "process_exited", "exit_code")
        PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
        PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
        PROCESS_EXITED_FIELD_NUMBER: _ClassVar[int]
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        process_id: int
        process_name: str
        process_exited: bool
        exit_code: int
        def __init__(self, process_id: _Optional[int] = ..., process_name: _Optional[str] = ..., process_exited: bool = ..., exit_code: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROCESS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    process_info_vec: _containers.RepeatedCompositeFieldContainer[ListProcessesInGuestResult.ProcessInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., process_info_vec: _Optional[_Iterable[_Union[ListProcessesInGuestResult.ProcessInfo, _Mapping]]] = ...) -> None: ...

class DeleteFilesInGuestArg(_message.Message):
    __slots__ = ("header", "file_info_vec", "guest_access_params")
    class FileInfo(_message.Message):
        __slots__ = ("file_fullpath", "is_directory", "recursive")
        FILE_FULLPATH_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        RECURSIVE_FIELD_NUMBER: _ClassVar[int]
        file_fullpath: str
        is_directory: bool
        recursive: bool
        def __init__(self, file_fullpath: _Optional[str] = ..., is_directory: bool = ..., recursive: bool = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    file_info_vec: _containers.RepeatedCompositeFieldContainer[DeleteFilesInGuestArg.FileInfo]
    guest_access_params: HyperVGuestAccessParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., file_info_vec: _Optional[_Iterable[_Union[DeleteFilesInGuestArg.FileInfo, _Mapping]]] = ..., guest_access_params: _Optional[_Union[HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class DeleteFilesInGuestResult(_message.Message):
    __slots__ = ("error", "file_result_vec")
    class FileResult(_message.Message):
        __slots__ = ("file_fullpath", "error")
        FILE_FULLPATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        file_fullpath: str
        error: _error_pb2.ErrorProto
        def __init__(self, file_fullpath: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FILE_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    file_result_vec: _containers.RepeatedCompositeFieldContainer[DeleteFilesInGuestResult.FileResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., file_result_vec: _Optional[_Iterable[_Union[DeleteFilesInGuestResult.FileResult, _Mapping]]] = ...) -> None: ...

class TerminateProcessInGuestArg(_message.Message):
    __slots__ = ("header", "process_id", "guest_access_params")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    process_id: int
    guest_access_params: HyperVGuestAccessParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., process_id: _Optional[int] = ..., guest_access_params: _Optional[_Union[HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class TerminateProcessInGuestResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AttachDisksArg(_message.Message):
    __slots__ = ("header", "hyperv_vm_id", "disk_chain_info_vec", "continue_on_error", "update_disk_uid")
    class DiskChainInfo(_message.Message):
        __slots__ = ("disk_id", "disk_path", "disk_chain_vec")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_PATH_FIELD_NUMBER: _ClassVar[int]
        DISK_CHAIN_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_id: bytes
        disk_path: str
        disk_chain_vec: _containers.RepeatedCompositeFieldContainer[_hyperv_pb2.RestoreVirtualDiskInfo]
        def __init__(self, disk_id: _Optional[bytes] = ..., disk_path: _Optional[str] = ..., disk_chain_vec: _Optional[_Iterable[_Union[_hyperv_pb2.RestoreVirtualDiskInfo, _Mapping]]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_CHAIN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DISK_UID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    hyperv_vm_id: bytes
    disk_chain_info_vec: _containers.RepeatedCompositeFieldContainer[AttachDisksArg.DiskChainInfo]
    continue_on_error: bool
    update_disk_uid: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., hyperv_vm_id: _Optional[bytes] = ..., disk_chain_info_vec: _Optional[_Iterable[_Union[AttachDisksArg.DiskChainInfo, _Mapping]]] = ..., continue_on_error: bool = ..., update_disk_uid: bool = ...) -> None: ...

class AttachDisksResult(_message.Message):
    __slots__ = ("error", "attach_disk_result_vec")
    class AttachDiskResult(_message.Message):
        __slots__ = ("disk_id", "disk_path", "error", "disk")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DISK_FIELD_NUMBER: _ClassVar[int]
        disk_id: bytes
        disk_path: str
        error: _error_pb2.ErrorProto
        disk: _hyperv_pb2.VirtualDisk
        def __init__(self, disk_id: _Optional[bytes] = ..., disk_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., disk: _Optional[_Union[_hyperv_pb2.VirtualDisk, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DISK_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    attach_disk_result_vec: _containers.RepeatedCompositeFieldContainer[AttachDisksResult.AttachDiskResult]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., attach_disk_result_vec: _Optional[_Iterable[_Union[AttachDisksResult.AttachDiskResult, _Mapping]]] = ...) -> None: ...

class DetachDisksArg(_message.Message):
    __slots__ = ("header", "hyperv_vm_id", "disk_path_vec", "continue_on_error")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    HYPERV_VM_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    hyperv_vm_id: bytes
    disk_path_vec: _containers.RepeatedScalarFieldContainer[str]
    continue_on_error: bool
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., hyperv_vm_id: _Optional[bytes] = ..., disk_path_vec: _Optional[_Iterable[str]] = ..., continue_on_error: bool = ...) -> None: ...

class DetachDisksResult(_message.Message):
    __slots__ = ("error", "detach_disk_error_vec")
    class DetachDiskError(_message.Message):
        __slots__ = ("disk_path", "error")
        DISK_PATH_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        disk_path: str
        error: _error_pb2.ErrorProto
        def __init__(self, disk_path: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DETACH_DISK_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    detach_disk_error_vec: _containers.RepeatedCompositeFieldContainer[DetachDisksResult.DetachDiskError]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., detach_disk_error_vec: _Optional[_Iterable[_Union[DetachDisksResult.DetachDiskError, _Mapping]]] = ...) -> None: ...

class ValidateCredentialsInGuestArg(_message.Message):
    __slots__ = ("header", "guest_access_params")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    guest_access_params: HyperVGuestAccessParams
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., guest_access_params: _Optional[_Union[HyperVGuestAccessParams, _Mapping]] = ...) -> None: ...

class RestoreHyperVVmOnScvmmArg(_message.Message):
    __slots__ = ("header", "access_params", "source_vm", "hyperv_uuid", "host_uuid")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VM_FIELD_NUMBER: _ClassVar[int]
    HYPERV_UUID_FIELD_NUMBER: _ClassVar[int]
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    source_vm: _hyperv_pb2_1.Entity
    hyperv_uuid: str
    host_uuid: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., source_vm: _Optional[_Union[_hyperv_pb2_1.Entity, _Mapping]] = ..., hyperv_uuid: _Optional[str] = ..., host_uuid: _Optional[str] = ...) -> None: ...

class RestoreHyperVVmOnScvmmResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class PowerOffVMArg(_message.Message):
    __slots__ = ("header", "access_params", "vm_uuid")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    vm_uuid: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., vm_uuid: _Optional[str] = ...) -> None: ...

class PowerOffVMResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RemoveVMArg(_message.Message):
    __slots__ = ("header", "access_params", "vm_uuid")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    access_params: HyperVAccessParams
    vm_uuid: str
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., access_params: _Optional[_Union[HyperVAccessParams, _Mapping]] = ..., vm_uuid: _Optional[str] = ...) -> None: ...

class RemoveVMResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
