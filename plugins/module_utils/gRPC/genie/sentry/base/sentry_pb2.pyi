from genie.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HardwareComponents(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kChassis: _ClassVar[HardwareComponents]
    kNode: _ClassVar[HardwareComponents]
    kPowerSupply: _ClassVar[HardwareComponents]
    kFan: _ClassVar[HardwareComponents]
    kCpu: _ClassVar[HardwareComponents]
    kMem: _ClassVar[HardwareComponents]
    kNic: _ClassVar[HardwareComponents]
    kSataDom: _ClassVar[HardwareComponents]
    kNvmeSsd: _ClassVar[HardwareComponents]
    kHdd: _ClassVar[HardwareComponents]
    kSsd: _ClassVar[HardwareComponents]
    kWatchdog: _ClassVar[HardwareComponents]
    kMisc: _ClassVar[HardwareComponents]

class AlertCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kTemp: _ClassVar[AlertCategory]
    kVolt: _ClassVar[AlertCategory]
    kCurr: _ClassVar[AlertCategory]
    kRedundancy: _ClassVar[AlertCategory]
    kPowerState: _ClassVar[AlertCategory]
    kSlotState: _ClassVar[AlertCategory]
    kLinkState: _ClassVar[AlertCategory]
    kMemEcc: _ClassVar[AlertCategory]
    kReboot: _ClassVar[AlertCategory]
    kFault: _ClassVar[AlertCategory]
    kMiscState: _ClassVar[AlertCategory]

class AlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCritical: _ClassVar[AlertSeverity]
    kWarning: _ClassVar[AlertSeverity]
    kInfo: _ClassVar[AlertSeverity]

class LinkEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLinkNoChange: _ClassVar[LinkEvent]
    kCableUnplugged: _ClassVar[LinkEvent]
    kCableInserted: _ClassVar[LinkEvent]
    kLinkIsDown: _ClassVar[LinkEvent]
    kLinkIsUp: _ClassVar[LinkEvent]
    kLinkStartFlapping: _ClassVar[LinkEvent]
    kLinkStopFlapping: _ClassVar[LinkEvent]

class HardwareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDisk: _ClassVar[HardwareType]
    kNIC: _ClassVar[HardwareType]
    kBIOS: _ClassVar[HardwareType]
    kRAID: _ClassVar[HardwareType]
kChassis: HardwareComponents
kNode: HardwareComponents
kPowerSupply: HardwareComponents
kFan: HardwareComponents
kCpu: HardwareComponents
kMem: HardwareComponents
kNic: HardwareComponents
kSataDom: HardwareComponents
kNvmeSsd: HardwareComponents
kHdd: HardwareComponents
kSsd: HardwareComponents
kWatchdog: HardwareComponents
kMisc: HardwareComponents
kTemp: AlertCategory
kVolt: AlertCategory
kCurr: AlertCategory
kRedundancy: AlertCategory
kPowerState: AlertCategory
kSlotState: AlertCategory
kLinkState: AlertCategory
kMemEcc: AlertCategory
kReboot: AlertCategory
kFault: AlertCategory
kMiscState: AlertCategory
kCritical: AlertSeverity
kWarning: AlertSeverity
kInfo: AlertSeverity
kLinkNoChange: LinkEvent
kCableUnplugged: LinkEvent
kCableInserted: LinkEvent
kLinkIsDown: LinkEvent
kLinkIsUp: LinkEvent
kLinkStartFlapping: LinkEvent
kLinkStopFlapping: LinkEvent
kDisk: HardwareType
kNIC: HardwareType
kBIOS: HardwareType
kRAID: HardwareType

class UrisProto(_message.Message):
    __slots__ = ("sentry_base_uri", "ipmi_info_uri", "non_ipmi_info_uri", "node_health_info_uri", "cluster_health_info_uri", "firmware_info_uri", "ipmi_sel_uri")
    SENTRY_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    IPMI_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    NON_IPMI_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    NODE_HEALTH_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_HEALTH_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    IPMI_SEL_URI_FIELD_NUMBER: _ClassVar[int]
    sentry_base_uri: str
    ipmi_info_uri: str
    non_ipmi_info_uri: str
    node_health_info_uri: str
    cluster_health_info_uri: str
    firmware_info_uri: str
    ipmi_sel_uri: str
    def __init__(self, sentry_base_uri: _Optional[str] = ..., ipmi_info_uri: _Optional[str] = ..., non_ipmi_info_uri: _Optional[str] = ..., node_health_info_uri: _Optional[str] = ..., cluster_health_info_uri: _Optional[str] = ..., firmware_info_uri: _Optional[str] = ..., ipmi_sel_uri: _Optional[str] = ...) -> None: ...

class IpmiInfoProto(_message.Message):
    __slots__ = ("power_supply_info_vec", "fan_info_vec", "drive_info_vec", "power_management_info_vec", "cpu_info_vec", "mem_info_vec", "motherboard_info_vec", "system_led_info")
    class MetricInfo(_message.Message):
        __slots__ = ("name", "status", "value", "sensor", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        SENSOR_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        status: bool
        value: str
        sensor: str
        description: str
        def __init__(self, name: _Optional[str] = ..., status: bool = ..., value: _Optional[str] = ..., sensor: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    POWER_SUPPLY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    DRIVE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    POWER_MANAGEMENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CPU_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOTHERBOARD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_LED_INFO_FIELD_NUMBER: _ClassVar[int]
    power_supply_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    fan_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    drive_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    power_management_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    cpu_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    mem_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    motherboard_info_vec: _containers.RepeatedCompositeFieldContainer[IpmiInfoProto.MetricInfo]
    system_led_info: str
    def __init__(self, power_supply_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., fan_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., drive_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., power_management_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., cpu_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., mem_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., motherboard_info_vec: _Optional[_Iterable[_Union[IpmiInfoProto.MetricInfo, _Mapping]]] = ..., system_led_info: _Optional[str] = ...) -> None: ...

class IpmiSelProto(_message.Message):
    __slots__ = ("node_status", "sel_info", "sel_record_vec", "node_presence_vec")
    class NodeStatus(_message.Message):
        __slots__ = ("present", "power_on", "power_restore_policy", "last_power_event", "send_alert")
        PRESENT_FIELD_NUMBER: _ClassVar[int]
        POWER_ON_FIELD_NUMBER: _ClassVar[int]
        POWER_RESTORE_POLICY_FIELD_NUMBER: _ClassVar[int]
        LAST_POWER_EVENT_FIELD_NUMBER: _ClassVar[int]
        SEND_ALERT_FIELD_NUMBER: _ClassVar[int]
        present: bool
        power_on: bool
        power_restore_policy: str
        last_power_event: str
        send_alert: bool
        def __init__(self, present: bool = ..., power_on: bool = ..., power_restore_policy: _Optional[str] = ..., last_power_event: _Optional[str] = ..., send_alert: bool = ...) -> None: ...
    class NodePresence(_message.Message):
        __slots__ = ("slot_id", "present", "chassis_id")
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        PRESENT_FIELD_NUMBER: _ClassVar[int]
        CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
        slot_id: int
        present: bool
        chassis_id: str
        def __init__(self, slot_id: _Optional[int] = ..., present: bool = ..., chassis_id: _Optional[str] = ...) -> None: ...
    class SelInfo(_message.Message):
        __slots__ = ("version", "entries", "percent_used", "last_add_time", "last_del_time")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        PERCENT_USED_FIELD_NUMBER: _ClassVar[int]
        LAST_ADD_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_DEL_TIME_FIELD_NUMBER: _ClassVar[int]
        version: str
        entries: int
        percent_used: int
        last_add_time: str
        last_del_time: str
        def __init__(self, version: _Optional[str] = ..., entries: _Optional[int] = ..., percent_used: _Optional[int] = ..., last_add_time: _Optional[str] = ..., last_del_time: _Optional[str] = ...) -> None: ...
    class SelRecord(_message.Message):
        __slots__ = ("record_id", "timestamp", "sensor_id", "entity_id", "event_type", "event_direction", "event_data", "event_description", "hw_component", "alert_category", "instance_info", "alert_severity", "alert_description", "alert_id", "master_event")
        RECORD_ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        EVENT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
        EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
        EVENT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        HW_COMPONENT_FIELD_NUMBER: _ClassVar[int]
        ALERT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
        ALERT_SEVERITY_FIELD_NUMBER: _ClassVar[int]
        ALERT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ALERT_ID_FIELD_NUMBER: _ClassVar[int]
        MASTER_EVENT_FIELD_NUMBER: _ClassVar[int]
        record_id: str
        timestamp: str
        sensor_id: str
        entity_id: str
        event_type: str
        event_direction: str
        event_data: str
        event_description: str
        hw_component: HardwareComponents
        alert_category: AlertCategory
        instance_info: str
        alert_severity: AlertSeverity
        alert_description: str
        alert_id: int
        master_event: bool
        def __init__(self, record_id: _Optional[str] = ..., timestamp: _Optional[str] = ..., sensor_id: _Optional[str] = ..., entity_id: _Optional[str] = ..., event_type: _Optional[str] = ..., event_direction: _Optional[str] = ..., event_data: _Optional[str] = ..., event_description: _Optional[str] = ..., hw_component: _Optional[_Union[HardwareComponents, str]] = ..., alert_category: _Optional[_Union[AlertCategory, str]] = ..., instance_info: _Optional[str] = ..., alert_severity: _Optional[_Union[AlertSeverity, str]] = ..., alert_description: _Optional[str] = ..., alert_id: _Optional[int] = ..., master_event: bool = ...) -> None: ...
    NODE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SEL_INFO_FIELD_NUMBER: _ClassVar[int]
    SEL_RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_PRESENCE_VEC_FIELD_NUMBER: _ClassVar[int]
    node_status: IpmiSelProto.NodeStatus
    sel_info: IpmiSelProto.SelInfo
    sel_record_vec: _containers.RepeatedCompositeFieldContainer[IpmiSelProto.SelRecord]
    node_presence_vec: _containers.RepeatedCompositeFieldContainer[IpmiSelProto.NodePresence]
    def __init__(self, node_status: _Optional[_Union[IpmiSelProto.NodeStatus, _Mapping]] = ..., sel_info: _Optional[_Union[IpmiSelProto.SelInfo, _Mapping]] = ..., sel_record_vec: _Optional[_Iterable[_Union[IpmiSelProto.SelRecord, _Mapping]]] = ..., node_presence_vec: _Optional[_Iterable[_Union[IpmiSelProto.NodePresence, _Mapping]]] = ...) -> None: ...

class NonIpmiInfoProto(_message.Message):
    __slots__ = ("cpu_info_vec", "cpu_core_stats_vec", "memory_info_vec", "memory_stats", "disk_info_vec", "nic_info_vec", "total_cpu_core_count", "total_memory_kb", "total_hdd_capacity_kb", "total_ssd_capacity_kb", "total_nic_capacity")
    class CpuInfo(_message.Message):
        __slots__ = ("name", "status", "family", "manufacturer", "max_speed", "current_speed", "core_count", "enabled_core_count", "thread_count", "normal_speed", "is_cpu_throttled")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        FAMILY_FIELD_NUMBER: _ClassVar[int]
        MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
        MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
        CURRENT_SPEED_FIELD_NUMBER: _ClassVar[int]
        CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
        ENABLED_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
        THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
        NORMAL_SPEED_FIELD_NUMBER: _ClassVar[int]
        IS_CPU_THROTTLED_FIELD_NUMBER: _ClassVar[int]
        name: str
        status: bool
        family: str
        manufacturer: str
        max_speed: str
        current_speed: str
        core_count: str
        enabled_core_count: str
        thread_count: str
        normal_speed: str
        is_cpu_throttled: bool
        def __init__(self, name: _Optional[str] = ..., status: bool = ..., family: _Optional[str] = ..., manufacturer: _Optional[str] = ..., max_speed: _Optional[str] = ..., current_speed: _Optional[str] = ..., core_count: _Optional[str] = ..., enabled_core_count: _Optional[str] = ..., thread_count: _Optional[str] = ..., normal_speed: _Optional[str] = ..., is_cpu_throttled: bool = ...) -> None: ...
    class CpuCoreStats(_message.Message):
        __slots__ = ("name", "usage_pct")
        NAME_FIELD_NUMBER: _ClassVar[int]
        USAGE_PCT_FIELD_NUMBER: _ClassVar[int]
        name: str
        usage_pct: float
        def __init__(self, name: _Optional[str] = ..., usage_pct: _Optional[float] = ...) -> None: ...
    class MemoryInfo(_message.Message):
        __slots__ = ("name", "status", "type", "size", "speed", "manufacturer", "serial_number")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        SPEED_FIELD_NUMBER: _ClassVar[int]
        MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        name: str
        status: bool
        type: str
        size: str
        speed: str
        manufacturer: str
        serial_number: str
        def __init__(self, name: _Optional[str] = ..., status: bool = ..., type: _Optional[str] = ..., size: _Optional[str] = ..., speed: _Optional[str] = ..., manufacturer: _Optional[str] = ..., serial_number: _Optional[str] = ...) -> None: ...
    class MemoryStats(_message.Message):
        __slots__ = ("used_pct", "free_kb", "used_kb")
        USED_PCT_FIELD_NUMBER: _ClassVar[int]
        FREE_KB_FIELD_NUMBER: _ClassVar[int]
        USED_KB_FIELD_NUMBER: _ClassVar[int]
        used_pct: float
        free_kb: int
        used_kb: int
        def __init__(self, used_pct: _Optional[float] = ..., free_kb: _Optional[int] = ..., used_kb: _Optional[int] = ...) -> None: ...
    class DiskInfo(_message.Message):
        __slots__ = ("device_path", "status", "type", "device_model", "serial_number", "capacity", "error_message", "mount_path_vec", "percentage_used")
        DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_USED_FIELD_NUMBER: _ClassVar[int]
        device_path: str
        status: bool
        type: str
        device_model: str
        serial_number: str
        capacity: str
        error_message: str
        mount_path_vec: _containers.RepeatedScalarFieldContainer[str]
        percentage_used: int
        def __init__(self, device_path: _Optional[str] = ..., status: bool = ..., type: _Optional[str] = ..., device_model: _Optional[str] = ..., serial_number: _Optional[str] = ..., capacity: _Optional[str] = ..., error_message: _Optional[str] = ..., mount_path_vec: _Optional[_Iterable[str]] = ..., percentage_used: _Optional[int] = ...) -> None: ...
    class NicInfo(_message.Message):
        __slots__ = ("name", "status", "speed", "capacity", "link_event", "send_alert", "stats_summary", "crc_err_count", "lsc_int_err_count", "rx_csum_offload_err_count")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SPEED_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        LINK_EVENT_FIELD_NUMBER: _ClassVar[int]
        SEND_ALERT_FIELD_NUMBER: _ClassVar[int]
        STATS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        CRC_ERR_COUNT_FIELD_NUMBER: _ClassVar[int]
        LSC_INT_ERR_COUNT_FIELD_NUMBER: _ClassVar[int]
        RX_CSUM_OFFLOAD_ERR_COUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        status: bool
        speed: str
        capacity: str
        link_event: LinkEvent
        send_alert: bool
        stats_summary: str
        crc_err_count: int
        lsc_int_err_count: int
        rx_csum_offload_err_count: int
        def __init__(self, name: _Optional[str] = ..., status: bool = ..., speed: _Optional[str] = ..., capacity: _Optional[str] = ..., link_event: _Optional[_Union[LinkEvent, str]] = ..., send_alert: bool = ..., stats_summary: _Optional[str] = ..., crc_err_count: _Optional[int] = ..., lsc_int_err_count: _Optional[int] = ..., rx_csum_offload_err_count: _Optional[int] = ...) -> None: ...
    CPU_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CPU_CORE_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    MEMORY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MEMORY_STATS_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    NIC_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CPU_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_KB_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HDD_CAPACITY_KB_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SSD_CAPACITY_KB_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NIC_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    cpu_info_vec: _containers.RepeatedCompositeFieldContainer[NonIpmiInfoProto.CpuInfo]
    cpu_core_stats_vec: _containers.RepeatedCompositeFieldContainer[NonIpmiInfoProto.CpuCoreStats]
    memory_info_vec: _containers.RepeatedCompositeFieldContainer[NonIpmiInfoProto.MemoryInfo]
    memory_stats: NonIpmiInfoProto.MemoryStats
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[NonIpmiInfoProto.DiskInfo]
    nic_info_vec: _containers.RepeatedCompositeFieldContainer[NonIpmiInfoProto.NicInfo]
    total_cpu_core_count: int
    total_memory_kb: int
    total_hdd_capacity_kb: int
    total_ssd_capacity_kb: int
    total_nic_capacity: str
    def __init__(self, cpu_info_vec: _Optional[_Iterable[_Union[NonIpmiInfoProto.CpuInfo, _Mapping]]] = ..., cpu_core_stats_vec: _Optional[_Iterable[_Union[NonIpmiInfoProto.CpuCoreStats, _Mapping]]] = ..., memory_info_vec: _Optional[_Iterable[_Union[NonIpmiInfoProto.MemoryInfo, _Mapping]]] = ..., memory_stats: _Optional[_Union[NonIpmiInfoProto.MemoryStats, _Mapping]] = ..., disk_info_vec: _Optional[_Iterable[_Union[NonIpmiInfoProto.DiskInfo, _Mapping]]] = ..., nic_info_vec: _Optional[_Iterable[_Union[NonIpmiInfoProto.NicInfo, _Mapping]]] = ..., total_cpu_core_count: _Optional[int] = ..., total_memory_kb: _Optional[int] = ..., total_hdd_capacity_kb: _Optional[int] = ..., total_ssd_capacity_kb: _Optional[int] = ..., total_nic_capacity: _Optional[str] = ...) -> None: ...

class FirmwareProto(_message.Message):
    __slots__ = ("hardware_type", "hardware_id", "hardware_desc", "hardware_model", "firmware_version")
    HARDWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_DESC_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    hardware_type: HardwareType
    hardware_id: str
    hardware_desc: str
    hardware_model: str
    firmware_version: str
    def __init__(self, hardware_type: _Optional[_Union[HardwareType, str]] = ..., hardware_id: _Optional[str] = ..., hardware_desc: _Optional[str] = ..., hardware_model: _Optional[str] = ..., firmware_version: _Optional[str] = ...) -> None: ...

class NodeHealthInfoProto(_message.Message):
    __slots__ = ("status", "ipmi_info", "non_ipmi_info", "node_id", "node_ip", "node_ipmi_ip", "num_consecutive_non_ipmi_rpc_timeouts", "firmware_vec", "ipmi_sel", "num_consecutive_ping_request_timeouts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IPMI_INFO_FIELD_NUMBER: _ClassVar[int]
    NON_IPMI_INFO_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_IPMI_IP_FIELD_NUMBER: _ClassVar[int]
    NUM_CONSECUTIVE_NON_IPMI_RPC_TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VEC_FIELD_NUMBER: _ClassVar[int]
    IPMI_SEL_FIELD_NUMBER: _ClassVar[int]
    NUM_CONSECUTIVE_PING_REQUEST_TIMEOUTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    ipmi_info: IpmiInfoProto
    non_ipmi_info: NonIpmiInfoProto
    node_id: int
    node_ip: str
    node_ipmi_ip: str
    num_consecutive_non_ipmi_rpc_timeouts: int
    firmware_vec: _containers.RepeatedCompositeFieldContainer[FirmwareProto]
    ipmi_sel: IpmiSelProto
    num_consecutive_ping_request_timeouts: int
    def __init__(self, status: bool = ..., ipmi_info: _Optional[_Union[IpmiInfoProto, _Mapping]] = ..., non_ipmi_info: _Optional[_Union[NonIpmiInfoProto, _Mapping]] = ..., node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., node_ipmi_ip: _Optional[str] = ..., num_consecutive_non_ipmi_rpc_timeouts: _Optional[int] = ..., firmware_vec: _Optional[_Iterable[_Union[FirmwareProto, _Mapping]]] = ..., ipmi_sel: _Optional[_Union[IpmiSelProto, _Mapping]] = ..., num_consecutive_ping_request_timeouts: _Optional[int] = ...) -> None: ...

class GetIpmiInfoArgs(_message.Message):
    __slots__ = ("ipmi_ip", "ipmi_username", "encrypted_ipmi_password", "cluster_id")
    IPMI_IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_IPMI_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ipmi_ip: str
    ipmi_username: str
    encrypted_ipmi_password: bytes
    cluster_id: int
    def __init__(self, ipmi_ip: _Optional[str] = ..., ipmi_username: _Optional[str] = ..., encrypted_ipmi_password: _Optional[bytes] = ..., cluster_id: _Optional[int] = ...) -> None: ...

class GetIpmiInfoResult(_message.Message):
    __slots__ = ("error", "ipmi_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IPMI_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    ipmi_info: IpmiInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ipmi_info: _Optional[_Union[IpmiInfoProto, _Mapping]] = ...) -> None: ...

class GetIpmiSelArgs(_message.Message):
    __slots__ = ("ipmi_ip", "ipmi_username", "encrypted_ipmi_password", "cluster_id")
    IPMI_IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_IPMI_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ipmi_ip: str
    ipmi_username: str
    encrypted_ipmi_password: bytes
    cluster_id: int
    def __init__(self, ipmi_ip: _Optional[str] = ..., ipmi_username: _Optional[str] = ..., encrypted_ipmi_password: _Optional[bytes] = ..., cluster_id: _Optional[int] = ...) -> None: ...

class GetIpmiSelResult(_message.Message):
    __slots__ = ("error", "ipmi_sel")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IPMI_SEL_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    ipmi_sel: IpmiSelProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ipmi_sel: _Optional[_Union[IpmiSelProto, _Mapping]] = ...) -> None: ...

class GetNonIpmiInfoResult(_message.Message):
    __slots__ = ("error", "non_ipmi_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NON_IPMI_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    non_ipmi_info: NonIpmiInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., non_ipmi_info: _Optional[_Union[NonIpmiInfoProto, _Mapping]] = ...) -> None: ...

class GetFirmwareInfoResult(_message.Message):
    __slots__ = ("error", "firmware_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    firmware_vec: _containers.RepeatedCompositeFieldContainer[FirmwareProto]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., firmware_vec: _Optional[_Iterable[_Union[FirmwareProto, _Mapping]]] = ...) -> None: ...

class GetNodeHealthInfoArgs(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    def __init__(self, node_id: _Optional[int] = ...) -> None: ...

class GetNodeHealthInfoResult(_message.Message):
    __slots__ = ("error", "node_health_info")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NODE_HEALTH_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    node_health_info: NodeHealthInfoProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., node_health_info: _Optional[_Union[NodeHealthInfoProto, _Mapping]] = ...) -> None: ...

class GetClusterHealthInfoResult(_message.Message):
    __slots__ = ("error", "node_health_info_vec", "total_cpu_core_count", "total_memory_kb", "total_ssd_capacity_kb", "total_hdd_capacity_kb")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NODE_HEALTH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CPU_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_KB_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SSD_CAPACITY_KB_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HDD_CAPACITY_KB_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    node_health_info_vec: _containers.RepeatedCompositeFieldContainer[NodeHealthInfoProto]
    total_cpu_core_count: int
    total_memory_kb: int
    total_ssd_capacity_kb: int
    total_hdd_capacity_kb: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., node_health_info_vec: _Optional[_Iterable[_Union[NodeHealthInfoProto, _Mapping]]] = ..., total_cpu_core_count: _Optional[int] = ..., total_memory_kb: _Optional[int] = ..., total_ssd_capacity_kb: _Optional[int] = ..., total_hdd_capacity_kb: _Optional[int] = ...) -> None: ...
