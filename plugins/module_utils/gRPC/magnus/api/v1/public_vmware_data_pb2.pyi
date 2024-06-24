from magnus.base import error_pb2 as _error_pb2
from magnus.api.v1 import public_common_data_pb2 as _public_common_data_pb2
from magnus.api.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MountVMwareNasDatastoreParams(_message.Message):
    __slots__ = ("resource_pool_moref", "remote_host", "remote_path", "datastore_name")
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HOST_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PATH_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_pool_moref: str
    remote_host: str
    remote_path: str
    datastore_name: str
    def __init__(self, resource_pool_moref: _Optional[str] = ..., remote_host: _Optional[str] = ..., remote_path: _Optional[str] = ..., datastore_name: _Optional[str] = ...) -> None: ...

class MountVMwareNasDatastoreResult(_message.Message):
    __slots__ = ("datastore_name", "datastore_moref")
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    datastore_name: str
    datastore_moref: str
    def __init__(self, datastore_name: _Optional[str] = ..., datastore_moref: _Optional[str] = ...) -> None: ...

class UnmountVMwareNasDatastoreParams(_message.Message):
    __slots__ = ("datastore_moref",)
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    datastore_moref: str
    def __init__(self, datastore_moref: _Optional[str] = ...) -> None: ...

class VMwareDatastoreAction(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMountNasDatastore: _ClassVar[VMwareDatastoreAction.Type]
        kUnmountNasDatastore: _ClassVar[VMwareDatastoreAction.Type]
    kMountNasDatastore: VMwareDatastoreAction.Type
    kUnmountNasDatastore: VMwareDatastoreAction.Type
    def __init__(self) -> None: ...

class VMwareDatastoreActionArg(_message.Message):
    __slots__ = ("task_id", "registered_vcenter_id", "action", "mount_nas_datastore_params", "unmount_nas_datastore_params")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_VCENTER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MOUNT_NAS_DATASTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_NAS_DATASTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    registered_vcenter_id: int
    action: VMwareDatastoreAction.Type
    mount_nas_datastore_params: MountVMwareNasDatastoreParams
    unmount_nas_datastore_params: UnmountVMwareNasDatastoreParams
    def __init__(self, task_id: _Optional[str] = ..., registered_vcenter_id: _Optional[int] = ..., action: _Optional[_Union[VMwareDatastoreAction.Type, str]] = ..., mount_nas_datastore_params: _Optional[_Union[MountVMwareNasDatastoreParams, _Mapping]] = ..., unmount_nas_datastore_params: _Optional[_Union[UnmountVMwareNasDatastoreParams, _Mapping]] = ...) -> None: ...

class VMwareDatastoreActionResult(_message.Message):
    __slots__ = ("error", "task_id", "action")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_id: str
    action: VMwareDatastoreAction.Type
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_id: _Optional[str] = ..., action: _Optional[_Union[VMwareDatastoreAction.Type, str]] = ...) -> None: ...

class VMwareDatastoreActionTaskStatusArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class TaskStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAccepted: _ClassVar[TaskStatus.Type]
        kRunning: _ClassVar[TaskStatus.Type]
        kFinished: _ClassVar[TaskStatus.Type]
    kAccepted: TaskStatus.Type
    kRunning: TaskStatus.Type
    kFinished: TaskStatus.Type
    def __init__(self) -> None: ...

class VMwareDatastoreActionTaskStatusResult(_message.Message):
    __slots__ = ("task_id", "error", "status", "action", "mount_nas_datastore_result")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MOUNT_NAS_DATASTORE_RESULT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    error: _error_pb2.ErrorProto
    status: TaskStatus.Type
    action: VMwareDatastoreAction.Type
    mount_nas_datastore_result: MountVMwareNasDatastoreResult
    def __init__(self, task_id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., status: _Optional[_Union[TaskStatus.Type, str]] = ..., action: _Optional[_Union[VMwareDatastoreAction.Type, str]] = ..., mount_nas_datastore_result: _Optional[_Union[MountVMwareNasDatastoreResult, _Mapping]] = ...) -> None: ...

class VMwareNetworkType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNetwork: _ClassVar[VMwareNetworkType.Type]
        kDistributedVirtualPortgroup: _ClassVar[VMwareNetworkType.Type]
    kNetwork: VMwareNetworkType.Type
    kDistributedVirtualPortgroup: VMwareNetworkType.Type
    def __init__(self) -> None: ...

class CreateVMwareVMParams(_message.Message):
    __slots__ = ("resource_pool_moref", "datastore_moref", "vm_folder_name", "network_type", "network_moref", "cloned_view_name", "cloned_view_data_dir_path", "vm_name", "datastore_name")
    RESOURCE_POOL_MOREF_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_MOREF_FIELD_NUMBER: _ClassVar[int]
    CLONED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    CLONED_VIEW_DATA_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_pool_moref: str
    datastore_moref: str
    vm_folder_name: str
    network_type: VMwareNetworkType.Type
    network_moref: str
    cloned_view_name: str
    cloned_view_data_dir_path: str
    vm_name: str
    datastore_name: str
    def __init__(self, resource_pool_moref: _Optional[str] = ..., datastore_moref: _Optional[str] = ..., vm_folder_name: _Optional[str] = ..., network_type: _Optional[_Union[VMwareNetworkType.Type, str]] = ..., network_moref: _Optional[str] = ..., cloned_view_name: _Optional[str] = ..., cloned_view_data_dir_path: _Optional[str] = ..., vm_name: _Optional[str] = ..., datastore_name: _Optional[str] = ...) -> None: ...

class CreateVMwareVMResult(_message.Message):
    __slots__ = ("vm_moref", "vm_uuid", "esxi_host_name", "esxi_host_moref")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    ESXI_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    ESXI_HOST_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    vm_uuid: str
    esxi_host_name: str
    esxi_host_moref: str
    def __init__(self, vm_moref: _Optional[str] = ..., vm_uuid: _Optional[str] = ..., esxi_host_name: _Optional[str] = ..., esxi_host_moref: _Optional[str] = ...) -> None: ...

class DeleteVMwareVMParams(_message.Message):
    __slots__ = ("vm_moref",)
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    def __init__(self, vm_moref: _Optional[str] = ...) -> None: ...

class VMPowerStatus(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPowerOn: _ClassVar[VMPowerStatus.Type]
        kPowerOff: _ClassVar[VMPowerStatus.Type]
    kPowerOn: VMPowerStatus.Type
    kPowerOff: VMPowerStatus.Type
    def __init__(self) -> None: ...

class SetVMwareVMPowerStatusParams(_message.Message):
    __slots__ = ("vm_moref", "power_status")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    POWER_STATUS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    power_status: VMPowerStatus.Type
    def __init__(self, vm_moref: _Optional[str] = ..., power_status: _Optional[_Union[VMPowerStatus.Type, str]] = ...) -> None: ...

class GuestOS(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLinux: _ClassVar[GuestOS.Type]
        kWindows: _ClassVar[GuestOS.Type]
    kLinux: GuestOS.Type
    kWindows: GuestOS.Type
    def __init__(self) -> None: ...

class ConfigureVMwareVMIPAddressParams(_message.Message):
    __slots__ = ("vm_moref", "adapter_ip_settings", "guest_os", "dns_servers", "dns_suffixes", "domain_name", "host_name")
    class IPSettings(_message.Message):
        __slots__ = ("mac_address", "use_static_ip", "ip_address", "netmask", "gateway")
        MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        USE_STATIC_IP_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        NETMASK_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        mac_address: str
        use_static_ip: bool
        ip_address: str
        netmask: str
        gateway: str
        def __init__(self, mac_address: _Optional[str] = ..., use_static_ip: bool = ..., ip_address: _Optional[str] = ..., netmask: _Optional[str] = ..., gateway: _Optional[str] = ...) -> None: ...
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_IP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DNS_SUFFIXES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    adapter_ip_settings: _containers.RepeatedCompositeFieldContainer[ConfigureVMwareVMIPAddressParams.IPSettings]
    guest_os: GuestOS.Type
    dns_servers: _containers.RepeatedScalarFieldContainer[str]
    dns_suffixes: _containers.RepeatedScalarFieldContainer[str]
    domain_name: str
    host_name: str
    def __init__(self, vm_moref: _Optional[str] = ..., adapter_ip_settings: _Optional[_Iterable[_Union[ConfigureVMwareVMIPAddressParams.IPSettings, _Mapping]]] = ..., guest_os: _Optional[_Union[GuestOS.Type, str]] = ..., dns_servers: _Optional[_Iterable[str]] = ..., dns_suffixes: _Optional[_Iterable[str]] = ..., domain_name: _Optional[str] = ..., host_name: _Optional[str] = ...) -> None: ...

class PushFileVMwareVMParams(_message.Message):
    __slots__ = ("vm_moref", "vm_credentials", "file_data", "remote_file_path", "guest_os")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    vm_credentials: _public_common_data_pb2.Credentials
    file_data: bytes
    remote_file_path: str
    guest_os: GuestOS.Type
    def __init__(self, vm_moref: _Optional[str] = ..., vm_credentials: _Optional[_Union[_public_common_data_pb2.Credentials, _Mapping]] = ..., file_data: _Optional[bytes] = ..., remote_file_path: _Optional[str] = ..., guest_os: _Optional[_Union[GuestOS.Type, str]] = ...) -> None: ...

class RunProgramVMwareVMParams(_message.Message):
    __slots__ = ("vm_moref", "vm_credentials", "working_directory_path", "program_path", "program_args")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_PATH_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_ARGS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    vm_credentials: _public_common_data_pb2.Credentials
    working_directory_path: str
    program_path: str
    program_args: str
    def __init__(self, vm_moref: _Optional[str] = ..., vm_credentials: _Optional[_Union[_public_common_data_pb2.Credentials, _Mapping]] = ..., working_directory_path: _Optional[str] = ..., program_path: _Optional[str] = ..., program_args: _Optional[str] = ...) -> None: ...

class RunProgramVMwareVMResult(_message.Message):
    __slots__ = ("pid", "exit_code")
    PID_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    pid: int
    exit_code: int
    def __init__(self, pid: _Optional[int] = ..., exit_code: _Optional[int] = ...) -> None: ...

class RelocateVMwareVMParams(_message.Message):
    __slots__ = ("vm_moref", "target_datastore_moref")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATASTORE_MOREF_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    target_datastore_moref: str
    def __init__(self, vm_moref: _Optional[str] = ..., target_datastore_moref: _Optional[str] = ...) -> None: ...

class RelocateVMwareVMResult(_message.Message):
    __slots__ = ("progress_percentage", "task_moref")
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
    progress_percentage: int
    task_moref: str
    def __init__(self, progress_percentage: _Optional[int] = ..., task_moref: _Optional[str] = ...) -> None: ...

class CheckVMwareVMCredentialsParams(_message.Message):
    __slots__ = ("vm_moref", "vm_credentials")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: str
    vm_credentials: _public_common_data_pb2.Credentials
    def __init__(self, vm_moref: _Optional[str] = ..., vm_credentials: _Optional[_Union[_public_common_data_pb2.Credentials, _Mapping]] = ...) -> None: ...

class VMwareVMAction(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreate: _ClassVar[VMwareVMAction.Type]
        kDelete: _ClassVar[VMwareVMAction.Type]
        kReconfigureIP: _ClassVar[VMwareVMAction.Type]
        kPowerStatus: _ClassVar[VMwareVMAction.Type]
        kPushFile: _ClassVar[VMwareVMAction.Type]
        kRunProgram: _ClassVar[VMwareVMAction.Type]
        kRelocate: _ClassVar[VMwareVMAction.Type]
        kCheckCredentials: _ClassVar[VMwareVMAction.Type]
    kCreate: VMwareVMAction.Type
    kDelete: VMwareVMAction.Type
    kReconfigureIP: VMwareVMAction.Type
    kPowerStatus: VMwareVMAction.Type
    kPushFile: VMwareVMAction.Type
    kRunProgram: VMwareVMAction.Type
    kRelocate: VMwareVMAction.Type
    kCheckCredentials: VMwareVMAction.Type
    def __init__(self) -> None: ...

class VMwareVMActionArg(_message.Message):
    __slots__ = ("task_id", "registered_vcenter_id", "action", "create_params", "delete_params", "reconfigure_ip_params", "power_status_params", "push_file_params", "run_program_params", "relocate_params", "check_credentials_params")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_VCENTER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DELETE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RECONFIGURE_IP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    POWER_STATUS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PUSH_FILE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RUN_PROGRAM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RELOCATE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHECK_CREDENTIALS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    registered_vcenter_id: int
    action: VMwareVMAction.Type
    create_params: CreateVMwareVMParams
    delete_params: DeleteVMwareVMParams
    reconfigure_ip_params: ConfigureVMwareVMIPAddressParams
    power_status_params: SetVMwareVMPowerStatusParams
    push_file_params: PushFileVMwareVMParams
    run_program_params: RunProgramVMwareVMParams
    relocate_params: RelocateVMwareVMParams
    check_credentials_params: CheckVMwareVMCredentialsParams
    def __init__(self, task_id: _Optional[str] = ..., registered_vcenter_id: _Optional[int] = ..., action: _Optional[_Union[VMwareVMAction.Type, str]] = ..., create_params: _Optional[_Union[CreateVMwareVMParams, _Mapping]] = ..., delete_params: _Optional[_Union[DeleteVMwareVMParams, _Mapping]] = ..., reconfigure_ip_params: _Optional[_Union[ConfigureVMwareVMIPAddressParams, _Mapping]] = ..., power_status_params: _Optional[_Union[SetVMwareVMPowerStatusParams, _Mapping]] = ..., push_file_params: _Optional[_Union[PushFileVMwareVMParams, _Mapping]] = ..., run_program_params: _Optional[_Union[RunProgramVMwareVMParams, _Mapping]] = ..., relocate_params: _Optional[_Union[RelocateVMwareVMParams, _Mapping]] = ..., check_credentials_params: _Optional[_Union[CheckVMwareVMCredentialsParams, _Mapping]] = ...) -> None: ...

class VMwareVMActionResult(_message.Message):
    __slots__ = ("error", "task_id", "action")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    task_id: str
    action: VMwareVMAction.Type
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., task_id: _Optional[str] = ..., action: _Optional[_Union[VMwareVMAction.Type, str]] = ...) -> None: ...

class VMwareVMActionTaskStatusArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class VMwareVMActionTaskStatusResult(_message.Message):
    __slots__ = ("task_id", "status", "error", "action", "create_result", "relocate_result", "run_program_result")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    RELOCATE_RESULT_FIELD_NUMBER: _ClassVar[int]
    RUN_PROGRAM_RESULT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    status: TaskStatus.Type
    error: _error_pb2.ErrorProto
    action: VMwareVMAction.Type
    create_result: CreateVMwareVMResult
    relocate_result: RelocateVMwareVMResult
    run_program_result: RunProgramVMwareVMResult
    def __init__(self, task_id: _Optional[str] = ..., status: _Optional[_Union[TaskStatus.Type, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., action: _Optional[_Union[VMwareVMAction.Type, str]] = ..., create_result: _Optional[_Union[CreateVMwareVMResult, _Mapping]] = ..., relocate_result: _Optional[_Union[RelocateVMwareVMResult, _Mapping]] = ..., run_program_result: _Optional[_Union[RunProgramVMwareVMResult, _Mapping]] = ...) -> None: ...
