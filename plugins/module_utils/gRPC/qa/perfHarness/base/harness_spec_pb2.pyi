from qa.lib.cohesityConnector.base import backup_pb2 as _backup_pb2
from qa.lib.cohesityConnector.base import platform_pb2 as _platform_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OSType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Windows: _ClassVar[OSType]
    Linux: _ClassVar[OSType]
Windows: OSType
Linux: OSType

class Credentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ConnectionParams(_message.Message):
    __slots__ = ("endpoint", "credentials")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    credentials: Credentials
    def __init__(self, endpoint: _Optional[str] = ..., credentials: _Optional[_Union[Credentials, _Mapping]] = ...) -> None: ...

class VirtualDiskInfo(_message.Message):
    __slots__ = ("type", "capacity_kb")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Thin: _ClassVar[VirtualDiskInfo.Type]
        EZThick: _ClassVar[VirtualDiskInfo.Type]
        TBZThick: _ClassVar[VirtualDiskInfo.Type]
    Thin: VirtualDiskInfo.Type
    EZThick: VirtualDiskInfo.Type
    TBZThick: VirtualDiskInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_KB_FIELD_NUMBER: _ClassVar[int]
    type: VirtualDiskInfo.Type
    capacity_kb: int
    def __init__(self, type: _Optional[_Union[VirtualDiskInfo.Type, str]] = ..., capacity_kb: _Optional[int] = ...) -> None: ...

class DiskPrepInfo(_message.Message):
    __slots__ = ("fill_pct", "dedup_ratio")
    FILL_PCT_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RATIO_FIELD_NUMBER: _ClassVar[int]
    fill_pct: int
    dedup_ratio: int
    def __init__(self, fill_pct: _Optional[int] = ..., dedup_ratio: _Optional[int] = ...) -> None: ...

class WorkLoadInfo(_message.Message):
    __slots__ = ("type", "num_vms", "dedup_ratio", "dedup_unit_size", "iorate", "elapsed_secs", "max_data_transfer", "write_block_size", "read_block_size", "read_pct", "rand_read_pct", "rand_write_pct", "num_outstanding_ios", "verification_directory")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCustom: _ClassVar[WorkLoadInfo.Type]
        kMSExchange: _ClassVar[WorkLoadInfo.Type]
        kMSSql: _ClassVar[WorkLoadInfo.Type]
        kMSSharePoint: _ClassVar[WorkLoadInfo.Type]
        kFileServer: _ClassVar[WorkLoadInfo.Type]
    kCustom: WorkLoadInfo.Type
    kMSExchange: WorkLoadInfo.Type
    kMSSql: WorkLoadInfo.Type
    kMSSharePoint: WorkLoadInfo.Type
    kFileServer: WorkLoadInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_VMS_FIELD_NUMBER: _ClassVar[int]
    DEDUP_RATIO_FIELD_NUMBER: _ClassVar[int]
    DEDUP_UNIT_SIZE_FIELD_NUMBER: _ClassVar[int]
    IORATE_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_SECS_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    WRITE_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_PCT_FIELD_NUMBER: _ClassVar[int]
    RAND_READ_PCT_FIELD_NUMBER: _ClassVar[int]
    RAND_WRITE_PCT_FIELD_NUMBER: _ClassVar[int]
    NUM_OUTSTANDING_IOS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    type: WorkLoadInfo.Type
    num_vms: int
    dedup_ratio: int
    dedup_unit_size: int
    iorate: int
    elapsed_secs: int
    max_data_transfer: int
    write_block_size: int
    read_block_size: int
    read_pct: int
    rand_read_pct: int
    rand_write_pct: int
    num_outstanding_ios: int
    verification_directory: str
    def __init__(self, type: _Optional[_Union[WorkLoadInfo.Type, str]] = ..., num_vms: _Optional[int] = ..., dedup_ratio: _Optional[int] = ..., dedup_unit_size: _Optional[int] = ..., iorate: _Optional[int] = ..., elapsed_secs: _Optional[int] = ..., max_data_transfer: _Optional[int] = ..., write_block_size: _Optional[int] = ..., read_block_size: _Optional[int] = ..., read_pct: _Optional[int] = ..., rand_read_pct: _Optional[int] = ..., rand_write_pct: _Optional[int] = ..., num_outstanding_ios: _Optional[int] = ..., verification_directory: _Optional[str] = ...) -> None: ...

class VMSetupInfo(_message.Message):
    __slots__ = ("num_vms", "vm_template", "datastore_name", "hypervisor_host_name", "vm_os_customization_spec", "extra_virtual_disk_vec", "os_type")
    NUM_VMS_FIELD_NUMBER: _ClassVar[int]
    VM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_OS_CUSTOMIZATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXTRA_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    num_vms: int
    vm_template: str
    datastore_name: str
    hypervisor_host_name: str
    vm_os_customization_spec: str
    extra_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[VirtualDiskInfo]
    os_type: OSType
    def __init__(self, num_vms: _Optional[int] = ..., vm_template: _Optional[str] = ..., datastore_name: _Optional[str] = ..., hypervisor_host_name: _Optional[str] = ..., vm_os_customization_spec: _Optional[str] = ..., extra_virtual_disk_vec: _Optional[_Iterable[_Union[VirtualDiskInfo, _Mapping]]] = ..., os_type: _Optional[_Union[OSType, str]] = ...) -> None: ...

class VMwareSetupInfo(_message.Message):
    __slots__ = ("ps_host_connection_params", "vcenter_connection_params", "vm_name_prefix", "cluster_name", "vm_setup_info_vec", "vm_credentials", "disk_prep_info")
    PS_HOST_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VCENTER_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_SETUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    DISK_PREP_INFO_FIELD_NUMBER: _ClassVar[int]
    ps_host_connection_params: ConnectionParams
    vcenter_connection_params: ConnectionParams
    vm_name_prefix: str
    cluster_name: str
    vm_setup_info_vec: _containers.RepeatedCompositeFieldContainer[VMSetupInfo]
    vm_credentials: Credentials
    disk_prep_info: DiskPrepInfo
    def __init__(self, ps_host_connection_params: _Optional[_Union[ConnectionParams, _Mapping]] = ..., vcenter_connection_params: _Optional[_Union[ConnectionParams, _Mapping]] = ..., vm_name_prefix: _Optional[str] = ..., cluster_name: _Optional[str] = ..., vm_setup_info_vec: _Optional[_Iterable[_Union[VMSetupInfo, _Mapping]]] = ..., vm_credentials: _Optional[_Union[Credentials, _Mapping]] = ..., disk_prep_info: _Optional[_Union[DiskPrepInfo, _Mapping]] = ...) -> None: ...

class BackupJobSetupInfo(_message.Message):
    __slots__ = ("num_vms", "viewbox_name", "viewbox_storage_policy", "name", "backup_freqency_minutes", "indexing_policy")
    NUM_VMS_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_STORAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FREQENCY_MINUTES_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    num_vms: int
    viewbox_name: str
    viewbox_storage_policy: _platform_pb2.StoragePolicy
    name: str
    backup_freqency_minutes: int
    indexing_policy: _backup_pb2.IndexingPolicy
    def __init__(self, num_vms: _Optional[int] = ..., viewbox_name: _Optional[str] = ..., viewbox_storage_policy: _Optional[_Union[_platform_pb2.StoragePolicy, _Mapping]] = ..., name: _Optional[str] = ..., backup_freqency_minutes: _Optional[int] = ..., indexing_policy: _Optional[_Union[_backup_pb2.IndexingPolicy, _Mapping]] = ...) -> None: ...

class CohesitySetupInfo(_message.Message):
    __slots__ = ("connection_params", "backup_job_vec", "num_backup_tasks_per_node")
    CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BACKUP_TASKS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    connection_params: ConnectionParams
    backup_job_vec: _containers.RepeatedCompositeFieldContainer[BackupJobSetupInfo]
    num_backup_tasks_per_node: int
    def __init__(self, connection_params: _Optional[_Union[ConnectionParams, _Mapping]] = ..., backup_job_vec: _Optional[_Iterable[_Union[BackupJobSetupInfo, _Mapping]]] = ..., num_backup_tasks_per_node: _Optional[int] = ...) -> None: ...

class HarnessSpec(_message.Message):
    __slots__ = ("working_dir", "vmware_setup_info", "cohesity_setup_info", "workload_info_vec", "vm_credentials")
    WORKING_DIR_FIELD_NUMBER: _ClassVar[int]
    VMWARE_SETUP_INFO_FIELD_NUMBER: _ClassVar[int]
    COHESITY_SETUP_INFO_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    working_dir: str
    vmware_setup_info: VMwareSetupInfo
    cohesity_setup_info: CohesitySetupInfo
    workload_info_vec: _containers.RepeatedCompositeFieldContainer[WorkLoadInfo]
    vm_credentials: Credentials
    def __init__(self, working_dir: _Optional[str] = ..., vmware_setup_info: _Optional[_Union[VMwareSetupInfo, _Mapping]] = ..., cohesity_setup_info: _Optional[_Union[CohesitySetupInfo, _Mapping]] = ..., workload_info_vec: _Optional[_Iterable[_Union[WorkLoadInfo, _Mapping]]] = ..., vm_credentials: _Optional[_Union[Credentials, _Mapping]] = ...) -> None: ...
