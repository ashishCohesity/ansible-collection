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

class VMConfig(_message.Message):
    __slots__ = ("vm_name", "uuid", "num_cores_per_vcpu", "num_v_cpus", "memory_capacity_in_bytes", "memory_reserved_capacity_in_bytes", "timezone", "power_state", "cpu_reservation_in_hz", "host_uuid", "vm_id", "cluster_uuid", "running_on_ndfs", "non_ndfs_details", "nutanix_virtual_disk_uuids", "nutanix_virtual_disks", "nutanix_virtual_disk_ids")
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_PER_VCPU_FIELD_NUMBER: _ClassVar[int]
    NUM_V_CPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_CAPACITY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_RESERVED_CAPACITY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    CPU_RESERVATION_IN_HZ_FIELD_NUMBER: _ClassVar[int]
    HOST_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    RUNNING_ON_NDFS_FIELD_NUMBER: _ClassVar[int]
    NON_NDFS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NUTANIX_VIRTUAL_DISK_UUIDS_FIELD_NUMBER: _ClassVar[int]
    NUTANIX_VIRTUAL_DISKS_FIELD_NUMBER: _ClassVar[int]
    NUTANIX_VIRTUAL_DISK_IDS_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    uuid: str
    num_cores_per_vcpu: int
    num_v_cpus: int
    memory_capacity_in_bytes: int
    memory_reserved_capacity_in_bytes: int
    timezone: str
    power_state: str
    cpu_reservation_in_hz: int
    host_uuid: str
    vm_id: str
    cluster_uuid: str
    running_on_ndfs: bool
    non_ndfs_details: str
    nutanix_virtual_disk_uuids: _containers.RepeatedScalarFieldContainer[str]
    nutanix_virtual_disks: _containers.RepeatedScalarFieldContainer[str]
    nutanix_virtual_disk_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vm_name: _Optional[str] = ..., uuid: _Optional[str] = ..., num_cores_per_vcpu: _Optional[int] = ..., num_v_cpus: _Optional[int] = ..., memory_capacity_in_bytes: _Optional[int] = ..., memory_reserved_capacity_in_bytes: _Optional[int] = ..., timezone: _Optional[str] = ..., power_state: _Optional[str] = ..., cpu_reservation_in_hz: _Optional[int] = ..., host_uuid: _Optional[str] = ..., vm_id: _Optional[str] = ..., cluster_uuid: _Optional[str] = ..., running_on_ndfs: bool = ..., non_ndfs_details: _Optional[str] = ..., nutanix_virtual_disk_uuids: _Optional[_Iterable[str]] = ..., nutanix_virtual_disks: _Optional[_Iterable[str]] = ..., nutanix_virtual_disk_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class VMListResult(_message.Message):
    __slots__ = ("entities", "metadata", "error_info")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[VMConfig]
    metadata: ListMetadata
    error_info: ErrorInfo
    def __init__(self, entities: _Optional[_Iterable[_Union[VMConfig, _Mapping]]] = ..., metadata: _Optional[_Union[ListMetadata, _Mapping]] = ..., error_info: _Optional[_Union[ErrorInfo, _Mapping]] = ...) -> None: ...
