from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorInfo(_message.Message):
    __slots__ = ("error_code", "detailed_message", "message")
    class ErrorCode(_message.Message):
        __slots__ = ("code", "help_url")
        CODE_FIELD_NUMBER: _ClassVar[int]
        HELP_URL_FIELD_NUMBER: _ClassVar[int]
        code: int
        help_url: str
        def __init__(self, code: _Optional[int] = ..., help_url: _Optional[str] = ...) -> None: ...
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_code: ErrorInfo.ErrorCode
    detailed_message: str
    message: str
    def __init__(self, error_code: _Optional[_Union[ErrorInfo.ErrorCode, _Mapping]] = ..., detailed_message: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("timeout_absolute", "timeout_inactive")
    TIMEOUT_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    timeout_absolute: int
    timeout_inactive: int
    def __init__(self, timeout_absolute: _Optional[int] = ..., timeout_inactive: _Optional[int] = ...) -> None: ...

class ListMetadata(_message.Message):
    __slots__ = ("total_entities", "count", "grand_total_entities", "next_cursor", "page", "end_index", "start_index")
    TOTAL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    END_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    total_entities: int
    count: int
    grand_total_entities: int
    next_cursor: str
    page: int
    end_index: int
    start_index: int
    def __init__(self, total_entities: _Optional[int] = ..., count: _Optional[int] = ..., grand_total_entities: _Optional[int] = ..., next_cursor: _Optional[str] = ..., page: _Optional[int] = ..., end_index: _Optional[int] = ..., start_index: _Optional[int] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ("display_name", "progress_status", "start_time_usecs", "cluster_uuid", "uuid", "entity_list", "meta_response")
    class TaskEntity(_message.Message):
        __slots__ = ("entity_id", "entity_name", "entity_type")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        entity_id: str
        entity_name: str
        entity_type: str
        def __init__(self, entity_id: _Optional[str] = ..., entity_name: _Optional[str] = ..., entity_type: _Optional[str] = ...) -> None: ...
    class MetaResponse(_message.Message):
        __slots__ = ("error_code", "error_detail")
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
        error_code: int
        error_detail: str
        def __init__(self, error_code: _Optional[int] = ..., error_detail: _Optional[str] = ...) -> None: ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LIST_FIELD_NUMBER: _ClassVar[int]
    META_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    progress_status: str
    start_time_usecs: int
    cluster_uuid: str
    uuid: str
    entity_list: _containers.RepeatedCompositeFieldContainer[Task.TaskEntity]
    meta_response: Task.MetaResponse
    def __init__(self, display_name: _Optional[str] = ..., progress_status: _Optional[str] = ..., start_time_usecs: _Optional[int] = ..., cluster_uuid: _Optional[str] = ..., uuid: _Optional[str] = ..., entity_list: _Optional[_Iterable[_Union[Task.TaskEntity, _Mapping]]] = ..., meta_response: _Optional[_Union[Task.MetaResponse, _Mapping]] = ...) -> None: ...

class TaskPollArg(_message.Message):
    __slots__ = ("completed_tasks", "timeout_interval")
    COMPLETED_TASKS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    completed_tasks: _containers.RepeatedScalarFieldContainer[str]
    timeout_interval: int
    def __init__(self, completed_tasks: _Optional[_Iterable[str]] = ..., timeout_interval: _Optional[int] = ...) -> None: ...

class TaskPollResult(_message.Message):
    __slots__ = ("timed_out", "completed_tasks_info")
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TASKS_INFO_FIELD_NUMBER: _ClassVar[int]
    timed_out: bool
    completed_tasks_info: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, timed_out: bool = ..., completed_tasks_info: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class VMNic(_message.Message):
    __slots__ = ("network_uuid", "mac_address", "request_ip", "requested_ip_address", "model", "ip_address", "is_connected")
    NETWORK_UUID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_IP_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    network_uuid: str
    mac_address: str
    request_ip: bool
    requested_ip_address: str
    model: str
    ip_address: str
    is_connected: bool
    def __init__(self, network_uuid: _Optional[str] = ..., mac_address: _Optional[str] = ..., request_ip: bool = ..., requested_ip_address: _Optional[str] = ..., model: _Optional[str] = ..., ip_address: _Optional[str] = ..., is_connected: bool = ...) -> None: ...

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

class Disk(_message.Message):
    __slots__ = ("disk_address", "vm_disk_clone", "vm_disk_create", "is_cdrom", "is_scsi_passthrough", "is_empty", "size", "storage_container_uuid", "storage_container_name", "flash_mode_enabled", "datasource_uuid", "vm_disk_clone_external")
    DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_CLONE_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_CREATE_FIELD_NUMBER: _ClassVar[int]
    IS_CDROM_FIELD_NUMBER: _ClassVar[int]
    IS_SCSI_PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
    IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    FLASH_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_CLONE_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    disk_address: DiskAddress
    vm_disk_clone: VMDiskClone
    vm_disk_create: VMDiskCreate
    is_cdrom: bool
    is_scsi_passthrough: bool
    is_empty: bool
    size: int
    storage_container_uuid: str
    storage_container_name: str
    flash_mode_enabled: bool
    datasource_uuid: str
    vm_disk_clone_external: VMDiskCloneExternal
    def __init__(self, disk_address: _Optional[_Union[DiskAddress, _Mapping]] = ..., vm_disk_clone: _Optional[_Union[VMDiskClone, _Mapping]] = ..., vm_disk_create: _Optional[_Union[VMDiskCreate, _Mapping]] = ..., is_cdrom: bool = ..., is_scsi_passthrough: bool = ..., is_empty: bool = ..., size: _Optional[int] = ..., storage_container_uuid: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., flash_mode_enabled: bool = ..., datasource_uuid: _Optional[str] = ..., vm_disk_clone_external: _Optional[_Union[VMDiskCloneExternal, _Mapping]] = ...) -> None: ...

class Affinity(_message.Message):
    __slots__ = ("policy", "host_uuids")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    HOST_UUIDS_FIELD_NUMBER: _ClassVar[int]
    policy: str
    host_uuids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, policy: _Optional[str] = ..., host_uuids: _Optional[_Iterable[str]] = ...) -> None: ...

class VMConfig(_message.Message):
    __slots__ = ("name", "uuid", "num_cores_per_vcpu", "num_vcpus", "memory_mb", "memory_reservation_mb", "vm_nics", "vm_disk_info", "timezone", "vm_gpus", "power_state", "vcpu_reservation_hz", "allow_live_migrate", "boot", "vm_features", "host_uuid", "affinity", "gpus_assigned", "description")
    class VMGpuConfig(_message.Message):
        __slots__ = ("in_use", "device_name", "device_id", "assignable", "fraction", "frame_buffer_size_bytes", "gpu_mode", "gpu_profile", "gpu_type", "gpu_vendor", "guest_driver_version", "max_instances_per_vm", "max_resolution", "num_virtual_display_heads", "numa_node", "sbdf", "licenses", "vm_uuids")
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
        LICENSES_FIELD_NUMBER: _ClassVar[int]
        VM_UUIDS_FIELD_NUMBER: _ClassVar[int]
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
        licenses: _containers.RepeatedScalarFieldContainer[str]
        vm_uuids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, in_use: bool = ..., device_name: _Optional[str] = ..., device_id: _Optional[int] = ..., assignable: bool = ..., fraction: _Optional[int] = ..., frame_buffer_size_bytes: _Optional[int] = ..., gpu_mode: _Optional[str] = ..., gpu_profile: _Optional[str] = ..., gpu_type: _Optional[str] = ..., gpu_vendor: _Optional[str] = ..., guest_driver_version: _Optional[str] = ..., max_instances_per_vm: _Optional[int] = ..., max_resolution: _Optional[str] = ..., num_virtual_display_heads: _Optional[int] = ..., numa_node: _Optional[int] = ..., sbdf: _Optional[str] = ..., licenses: _Optional[_Iterable[str]] = ..., vm_uuids: _Optional[_Iterable[str]] = ...) -> None: ...
    class BootConfig(_message.Message):
        __slots__ = ("boot_device_type", "mac_addr", "disk_address", "uefi_boot", "boot_device_order")
        BOOT_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDR_FIELD_NUMBER: _ClassVar[int]
        DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        UEFI_BOOT_FIELD_NUMBER: _ClassVar[int]
        BOOT_DEVICE_ORDER_FIELD_NUMBER: _ClassVar[int]
        boot_device_type: str
        mac_addr: str
        disk_address: DiskAddress
        uefi_boot: bool
        boot_device_order: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, boot_device_type: _Optional[str] = ..., mac_addr: _Optional[str] = ..., disk_address: _Optional[_Union[DiskAddress, _Mapping]] = ..., uefi_boot: bool = ..., boot_device_order: _Optional[_Iterable[str]] = ...) -> None: ...
    class vm_feature_list(_message.Message):
        __slots__ = ("agent_vm", "flash_mode")
        AGENT_VM_FIELD_NUMBER: _ClassVar[int]
        FLASH_MODE_FIELD_NUMBER: _ClassVar[int]
        agent_vm: bool
        flash_mode: bool
        def __init__(self, agent_vm: bool = ..., flash_mode: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_PER_VCPU_FIELD_NUMBER: _ClassVar[int]
    NUM_VCPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_RESERVATION_MB_FIELD_NUMBER: _ClassVar[int]
    VM_NICS_FIELD_NUMBER: _ClassVar[int]
    VM_DISK_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    VM_GPUS_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    VCPU_RESERVATION_HZ_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LIVE_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    BOOT_FIELD_NUMBER: _ClassVar[int]
    VM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_FIELD_NUMBER: _ClassVar[int]
    GPUS_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    num_cores_per_vcpu: int
    num_vcpus: int
    memory_mb: int
    memory_reservation_mb: int
    vm_nics: _containers.RepeatedCompositeFieldContainer[VMNic]
    vm_disk_info: _containers.RepeatedCompositeFieldContainer[Disk]
    timezone: str
    vm_gpus: _containers.RepeatedCompositeFieldContainer[VMConfig.VMGpuConfig]
    power_state: str
    vcpu_reservation_hz: int
    allow_live_migrate: bool
    boot: VMConfig.BootConfig
    vm_features: VMConfig.vm_feature_list
    host_uuid: str
    affinity: Affinity
    gpus_assigned: bool
    description: str
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., num_cores_per_vcpu: _Optional[int] = ..., num_vcpus: _Optional[int] = ..., memory_mb: _Optional[int] = ..., memory_reservation_mb: _Optional[int] = ..., vm_nics: _Optional[_Iterable[_Union[VMNic, _Mapping]]] = ..., vm_disk_info: _Optional[_Iterable[_Union[Disk, _Mapping]]] = ..., timezone: _Optional[str] = ..., vm_gpus: _Optional[_Iterable[_Union[VMConfig.VMGpuConfig, _Mapping]]] = ..., power_state: _Optional[str] = ..., vcpu_reservation_hz: _Optional[int] = ..., allow_live_migrate: bool = ..., boot: _Optional[_Union[VMConfig.BootConfig, _Mapping]] = ..., vm_features: _Optional[_Union[VMConfig.vm_feature_list, _Mapping]] = ..., host_uuid: _Optional[str] = ..., affinity: _Optional[_Union[Affinity, _Mapping]] = ..., gpus_assigned: bool = ..., description: _Optional[str] = ...) -> None: ...

class CreateVMConfig(_message.Message):
    __slots__ = ("name", "uuid", "num_cores_per_vcpu", "num_vcpus", "memory_mb", "memory_reservation_mb", "vm_nics", "vm_disks", "timezone", "vm_gpus", "power_state", "vcpu_reservation_hz", "allow_live_migrate", "boot", "vm_features", "host_uuid", "affinity", "gpus_assigned", "description")
    class VMGpuConfig(_message.Message):
        __slots__ = ("in_use", "device_name", "device_id", "assignable", "fraction", "frame_buffer_size_bytes", "gpu_mode", "gpu_profile", "gpu_type", "gpu_vendor", "guest_driver_version", "max_instances_per_vm", "max_resolution", "num_virtual_display_heads", "numa_node", "sbdf", "licenses", "vm_uuids")
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
        LICENSES_FIELD_NUMBER: _ClassVar[int]
        VM_UUIDS_FIELD_NUMBER: _ClassVar[int]
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
        licenses: _containers.RepeatedScalarFieldContainer[str]
        vm_uuids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, in_use: bool = ..., device_name: _Optional[str] = ..., device_id: _Optional[int] = ..., assignable: bool = ..., fraction: _Optional[int] = ..., frame_buffer_size_bytes: _Optional[int] = ..., gpu_mode: _Optional[str] = ..., gpu_profile: _Optional[str] = ..., gpu_type: _Optional[str] = ..., gpu_vendor: _Optional[str] = ..., guest_driver_version: _Optional[str] = ..., max_instances_per_vm: _Optional[int] = ..., max_resolution: _Optional[str] = ..., num_virtual_display_heads: _Optional[int] = ..., numa_node: _Optional[int] = ..., sbdf: _Optional[str] = ..., licenses: _Optional[_Iterable[str]] = ..., vm_uuids: _Optional[_Iterable[str]] = ...) -> None: ...
    class BootConfig(_message.Message):
        __slots__ = ("boot_device_type", "mac_addr", "disk_address", "uefi_boot", "boot_device_order")
        BOOT_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDR_FIELD_NUMBER: _ClassVar[int]
        DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        UEFI_BOOT_FIELD_NUMBER: _ClassVar[int]
        BOOT_DEVICE_ORDER_FIELD_NUMBER: _ClassVar[int]
        boot_device_type: str
        mac_addr: str
        disk_address: DiskAddress
        uefi_boot: bool
        boot_device_order: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, boot_device_type: _Optional[str] = ..., mac_addr: _Optional[str] = ..., disk_address: _Optional[_Union[DiskAddress, _Mapping]] = ..., uefi_boot: bool = ..., boot_device_order: _Optional[_Iterable[str]] = ...) -> None: ...
    class vm_feature_list(_message.Message):
        __slots__ = ("agent_vm",)
        AGENT_VM_FIELD_NUMBER: _ClassVar[int]
        agent_vm: bool
        def __init__(self, agent_vm: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_PER_VCPU_FIELD_NUMBER: _ClassVar[int]
    NUM_VCPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_RESERVATION_MB_FIELD_NUMBER: _ClassVar[int]
    VM_NICS_FIELD_NUMBER: _ClassVar[int]
    VM_DISKS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    VM_GPUS_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    VCPU_RESERVATION_HZ_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LIVE_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    BOOT_FIELD_NUMBER: _ClassVar[int]
    VM_FEATURES_FIELD_NUMBER: _ClassVar[int]
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_FIELD_NUMBER: _ClassVar[int]
    GPUS_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    uuid: str
    num_cores_per_vcpu: int
    num_vcpus: int
    memory_mb: int
    memory_reservation_mb: int
    vm_nics: _containers.RepeatedCompositeFieldContainer[VMNic]
    vm_disks: _containers.RepeatedCompositeFieldContainer[Disk]
    timezone: str
    vm_gpus: _containers.RepeatedCompositeFieldContainer[CreateVMConfig.VMGpuConfig]
    power_state: str
    vcpu_reservation_hz: int
    allow_live_migrate: bool
    boot: CreateVMConfig.BootConfig
    vm_features: CreateVMConfig.vm_feature_list
    host_uuid: str
    affinity: Affinity
    gpus_assigned: bool
    description: str
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., num_cores_per_vcpu: _Optional[int] = ..., num_vcpus: _Optional[int] = ..., memory_mb: _Optional[int] = ..., memory_reservation_mb: _Optional[int] = ..., vm_nics: _Optional[_Iterable[_Union[VMNic, _Mapping]]] = ..., vm_disks: _Optional[_Iterable[_Union[Disk, _Mapping]]] = ..., timezone: _Optional[str] = ..., vm_gpus: _Optional[_Iterable[_Union[CreateVMConfig.VMGpuConfig, _Mapping]]] = ..., power_state: _Optional[str] = ..., vcpu_reservation_hz: _Optional[int] = ..., allow_live_migrate: bool = ..., boot: _Optional[_Union[CreateVMConfig.BootConfig, _Mapping]] = ..., vm_features: _Optional[_Union[CreateVMConfig.vm_feature_list, _Mapping]] = ..., host_uuid: _Optional[str] = ..., affinity: _Optional[_Union[Affinity, _Mapping]] = ..., gpus_assigned: bool = ..., description: _Optional[str] = ...) -> None: ...

class CreateVMResult(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class VMListResult(_message.Message):
    __slots__ = ("entities", "metadata", "error_info")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[VMConfig]
    metadata: ListMetadata
    error_info: ErrorInfo
    def __init__(self, entities: _Optional[_Iterable[_Union[VMConfig, _Mapping]]] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ..., error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ...) -> None: ...

class VMDiskCreate(_message.Message):
    __slots__ = ("storage_container_uuid", "size")
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    storage_container_uuid: str
    size: int
    def __init__(self, storage_container_uuid: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class VMDiskClone(_message.Message):
    __slots__ = ("storage_container_uuid", "minimum_size", "disk_address")
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    storage_container_uuid: str
    minimum_size: int
    disk_address: DiskAddress
    def __init__(self, storage_container_uuid: _Optional[str] = ..., minimum_size: _Optional[int] = ..., disk_address: _Optional[_Union[DiskAddress, _Mapping]] = ...) -> None: ...

class VMDiskCloneExternal(_message.Message):
    __slots__ = ("external_disk_url", "storage_container_uuid")
    EXTERNAL_DISK_URL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    external_disk_url: str
    storage_container_uuid: str
    def __init__(self, external_disk_url: _Optional[str] = ..., storage_container_uuid: _Optional[str] = ...) -> None: ...

class VolumeDiskSpec(_message.Message):
    __slots__ = ("volume_group_uuid", "create_config", "clone_config", "index")
    VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLONE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    volume_group_uuid: str
    create_config: VMDiskCreate
    clone_config: VMDiskClone
    index: int
    def __init__(self, volume_group_uuid: _Optional[str] = ..., create_config: _Optional[_Union[VMDiskCreate, _Mapping]] = ..., clone_config: _Optional[_Union[VMDiskClone, _Mapping]] = ..., index: _Optional[int] = ...) -> None: ...

class IscsiClient(_message.Message):
    __slots__ = ("client_address",)
    CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    client_address: str
    def __init__(self, client_address: _Optional[str] = ...) -> None: ...

class CreateVolumeGroupArg(_message.Message):
    __slots__ = ("uuid", "name", "iscsi_target", "iscsi_target_prefix", "disk_list", "attached_clients", "is_shared")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DISK_LIST_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    IS_SHARED_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    iscsi_target: str
    iscsi_target_prefix: str
    disk_list: _containers.RepeatedCompositeFieldContainer[VolumeDiskSpec]
    attached_clients: _containers.RepeatedCompositeFieldContainer[IscsiClient]
    is_shared: bool
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., iscsi_target: _Optional[str] = ..., iscsi_target_prefix: _Optional[str] = ..., disk_list: _Optional[_Iterable[_Union[VolumeDiskSpec, _Mapping]]] = ..., attached_clients: _Optional[_Iterable[_Union[IscsiClient, _Mapping]]] = ..., is_shared: bool = ...) -> None: ...

class CreateVolumeGroupResult(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class DeleteVolumeGroupResult(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...

class ScsiClient(_message.Message):
    __slots__ = ("client_address",)
    CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    client_address: str
    def __init__(self, client_address: _Optional[str] = ...) -> None: ...

class UpdateVolumeGroupArg(_message.Message):
    __slots__ = ("attached_clients", "name", "iscsi_target_prefix", "is_shared")
    ATTACHED_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IS_SHARED_FIELD_NUMBER: _ClassVar[int]
    attached_clients: _containers.RepeatedCompositeFieldContainer[ScsiClient]
    name: str
    iscsi_target_prefix: str
    is_shared: bool
    def __init__(self, attached_clients: _Optional[_Iterable[_Union[ScsiClient, _Mapping]]] = ..., name: _Optional[str] = ..., iscsi_target_prefix: _Optional[str] = ..., is_shared: bool = ...) -> None: ...

class CloseVolumeGroupArg(_message.Message):
    __slots__ = ("iscsi_client",)
    ISCSI_CLIENT_FIELD_NUMBER: _ClassVar[int]
    iscsi_client: ScsiClient
    def __init__(self, iscsi_client: _Optional[_Union[ScsiClient, _Mapping]] = ...) -> None: ...

class CloseVolumeGroupResult(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class VolumeGroupInfoResult(_message.Message):
    __slots__ = ("uuid", "is_deleted", "attachment_list", "iscsi_target", "name", "disk_list")
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
    UUID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    ISCSI_TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_LIST_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    is_deleted: bool
    attachment_list: _containers.RepeatedCompositeFieldContainer[VolumeGroupInfoResult.Initiators]
    iscsi_target: str
    name: str
    disk_list: _containers.RepeatedCompositeFieldContainer[VolumeGroupInfoResult.VolumeDiskList]
    def __init__(self, uuid: _Optional[str] = ..., is_deleted: bool = ..., attachment_list: _Optional[_Iterable[_Union[VolumeGroupInfoResult.Initiators, _Mapping]]] = ..., iscsi_target: _Optional[str] = ..., name: _Optional[str] = ..., disk_list: _Optional[_Iterable[_Union[VolumeGroupInfoResult.VolumeDiskList, _Mapping]]] = ...) -> None: ...

class ClusterConfig(_message.Message):
    __slots__ = ("multicluster", "cluster_uuid", "name", "cluster_external_data_services_ipaddress", "version", "hypervisor_types", "management_servers")
    MULTICLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_EXTERNAL_DATA_SERVICES_IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HYPERVISOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SERVERS_FIELD_NUMBER: _ClassVar[int]
    multicluster: bool
    cluster_uuid: str
    name: str
    cluster_external_data_services_ipaddress: str
    version: str
    hypervisor_types: _containers.RepeatedScalarFieldContainer[str]
    management_servers: _containers.RepeatedCompositeFieldContainer[ManagementServerConfig]
    def __init__(self, multicluster: bool = ..., cluster_uuid: _Optional[str] = ..., name: _Optional[str] = ..., cluster_external_data_services_ipaddress: _Optional[str] = ..., version: _Optional[str] = ..., hypervisor_types: _Optional[_Iterable[str]] = ..., management_servers: _Optional[_Iterable[_Union[ManagementServerConfig, _Mapping]]] = ...) -> None: ...

class ManagementServerConfig(_message.Message):
    __slots__ = ("ip_address", "management_server_type")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SERVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    management_server_type: str
    def __init__(self, ip_address: _Optional[str] = ..., management_server_type: _Optional[str] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ("storage_container_uuid", "name", "max_capacity", "marked_for_removal", "cluster_uuid")
    STORAGE_CONTAINER_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_REMOVAL_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    storage_container_uuid: str
    name: str
    max_capacity: int
    marked_for_removal: bool
    cluster_uuid: str
    def __init__(self, storage_container_uuid: _Optional[str] = ..., name: _Optional[str] = ..., max_capacity: _Optional[int] = ..., marked_for_removal: bool = ..., cluster_uuid: _Optional[str] = ...) -> None: ...

class ContainerListResult(_message.Message):
    __slots__ = ("entities", "metadata", "error_info")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Container]
    metadata: ListMetadata
    error_info: ErrorInfo
    def __init__(self, entities: _Optional[_Iterable[_Union[Container, _Mapping]]] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ..., error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ...) -> None: ...

class IPConfig(_message.Message):
    __slots__ = ("network_address", "default_gateway")
    NETWORK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    network_address: str
    default_gateway: str
    def __init__(self, network_address: _Optional[str] = ..., default_gateway: _Optional[str] = ...) -> None: ...

class Network(_message.Message):
    __slots__ = ("uuid", "name", "ip_config")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    ip_config: IPConfig
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., ip_config: _Optional[_Union[IPConfig, _Mapping]] = ...) -> None: ...

class NetworkListResult(_message.Message):
    __slots__ = ("entities", "metadata", "error_info")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Network]
    metadata: ListMetadata
    error_info: ErrorInfo
    def __init__(self, entities: _Optional[_Iterable[_Union[Network, _Mapping]]] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ..., error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ...) -> None: ...

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

class HostListResult(_message.Message):
    __slots__ = ("entities", "metadata", "error_info")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Host]
    metadata: ListMetadata
    error_info: ErrorInfo
    def __init__(self, entities: _Optional[_Iterable[_Union[Host, _Mapping]]] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ..., error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ...) -> None: ...

class SetVMPowerStateArg(_message.Message):
    __slots__ = ("uuid", "transition")
    UUID_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    transition: str
    def __init__(self, uuid: _Optional[str] = ..., transition: _Optional[str] = ...) -> None: ...

class SetVMPowerStateResult(_message.Message):
    __slots__ = ("task_uuid",)
    TASK_UUID_FIELD_NUMBER: _ClassVar[int]
    task_uuid: str
    def __init__(self, task_uuid: _Optional[str] = ...) -> None: ...
