from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatscollectorUrisProto(_message.Message):
    __slots__ = ("base_uri", "api_version", "iostat_uri", "stat_uri")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    IOSTAT_URI_FIELD_NUMBER: _ClassVar[int]
    STAT_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    api_version: str
    iostat_uri: str
    stat_uri: str
    def __init__(self, base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., iostat_uri: _Optional[str] = ..., stat_uri: _Optional[str] = ...) -> None: ...

class Stats(_message.Message):
    __slots__ = ("iostat_proto", "df_stat_proto", "interrupt_stat_proto", "memory_info_stat_proto", "mpstat_info", "sar_stat_info", "top_stat_proto", "io_top_stat_proto")
    IOSTAT_PROTO_FIELD_NUMBER: _ClassVar[int]
    DF_STAT_PROTO_FIELD_NUMBER: _ClassVar[int]
    INTERRUPT_STAT_PROTO_FIELD_NUMBER: _ClassVar[int]
    MEMORY_INFO_STAT_PROTO_FIELD_NUMBER: _ClassVar[int]
    MPSTAT_INFO_FIELD_NUMBER: _ClassVar[int]
    SAR_STAT_INFO_FIELD_NUMBER: _ClassVar[int]
    TOP_STAT_PROTO_FIELD_NUMBER: _ClassVar[int]
    IO_TOP_STAT_PROTO_FIELD_NUMBER: _ClassVar[int]
    iostat_proto: IostatProto
    df_stat_proto: DfstatProto
    interrupt_stat_proto: Interrput
    memory_info_stat_proto: MemInfoProto
    mpstat_info: MemStat
    sar_stat_info: SarProto
    top_stat_proto: TopProto
    io_top_stat_proto: IoTopProto
    def __init__(self, iostat_proto: _Optional[_Union[IostatProto, _Mapping]] = ..., df_stat_proto: _Optional[_Union[DfstatProto, _Mapping]] = ..., interrupt_stat_proto: _Optional[_Union[Interrput, _Mapping]] = ..., memory_info_stat_proto: _Optional[_Union[MemInfoProto, _Mapping]] = ..., mpstat_info: _Optional[_Union[MemStat, _Mapping]] = ..., sar_stat_info: _Optional[_Union[SarProto, _Mapping]] = ..., top_stat_proto: _Optional[_Union[TopProto, _Mapping]] = ..., io_top_stat_proto: _Optional[_Union[IoTopProto, _Mapping]] = ...) -> None: ...

class IostatProto(_message.Message):
    __slots__ = ("timestamp", "disk_stats_vec")
    class DiskStats(_message.Message):
        __slots__ = ("device", "await_time_msecs")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        AWAIT_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
        device: str
        await_time_msecs: float
        def __init__(self, device: _Optional[str] = ..., await_time_msecs: _Optional[float] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DISK_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    disk_stats_vec: _containers.RepeatedCompositeFieldContainer[IostatProto.DiskStats]
    def __init__(self, timestamp: _Optional[int] = ..., disk_stats_vec: _Optional[_Iterable[_Union[IostatProto.DiskStats, _Mapping]]] = ...) -> None: ...

class DfstatProto(_message.Message):
    __slots__ = ("timestamp", "df_stats_vec")
    class DfStats(_message.Message):
        __slots__ = ("file_system", "disk_size", "used_size", "available_size", "used_disk_percentage", "mount_point")
        FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        USED_SIZE_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SIZE_FIELD_NUMBER: _ClassVar[int]
        USED_DISK_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        file_system: str
        disk_size: str
        used_size: str
        available_size: str
        used_disk_percentage: str
        mount_point: str
        def __init__(self, file_system: _Optional[str] = ..., disk_size: _Optional[str] = ..., used_size: _Optional[str] = ..., available_size: _Optional[str] = ..., used_disk_percentage: _Optional[str] = ..., mount_point: _Optional[str] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DF_STATS_VEC_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    df_stats_vec: _containers.RepeatedCompositeFieldContainer[DfstatProto.DfStats]
    def __init__(self, timestamp: _Optional[int] = ..., df_stats_vec: _Optional[_Iterable[_Union[DfstatProto.DfStats, _Mapping]]] = ...) -> None: ...

class Interrput(_message.Message):
    __slots__ = ("irq", "drivers")
    IRQ_FIELD_NUMBER: _ClassVar[int]
    DRIVERS_FIELD_NUMBER: _ClassVar[int]
    irq: IrqInterrupts
    drivers: DriverInterrupts
    def __init__(self, irq: _Optional[_Union[IrqInterrupts, _Mapping]] = ..., drivers: _Optional[_Union[DriverInterrupts, _Mapping]] = ...) -> None: ...

class IrqInterrupts(_message.Message):
    __slots__ = ("interrupt_id", "category", "type", "cpu_map")
    INTERRUPT_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CPU_MAP_FIELD_NUMBER: _ClassVar[int]
    interrupt_id: str
    category: str
    type: str
    cpu_map: _containers.RepeatedCompositeFieldContainer[CpuMap]
    def __init__(self, interrupt_id: _Optional[str] = ..., category: _Optional[str] = ..., type: _Optional[str] = ..., cpu_map: _Optional[_Iterable[_Union[CpuMap, _Mapping]]] = ...) -> None: ...

class CpuMap(_message.Message):
    __slots__ = ("cpu_id", "number_of_interrupts")
    CPU_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_INTERRUPTS_FIELD_NUMBER: _ClassVar[int]
    cpu_id: str
    number_of_interrupts: int
    def __init__(self, cpu_id: _Optional[str] = ..., number_of_interrupts: _Optional[int] = ...) -> None: ...

class DriverInterrupts(_message.Message):
    __slots__ = ("interrupt_id", "description", "cpu_map")
    INTERRUPT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CPU_MAP_FIELD_NUMBER: _ClassVar[int]
    interrupt_id: str
    description: str
    cpu_map: _containers.RepeatedCompositeFieldContainer[CpuMap]
    def __init__(self, interrupt_id: _Optional[str] = ..., description: _Optional[str] = ..., cpu_map: _Optional[_Iterable[_Union[CpuMap, _Mapping]]] = ...) -> None: ...

class MemInfoArrayProto(_message.Message):
    __slots__ = ("category", "size")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    category: str
    size: str
    def __init__(self, category: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class MemInfoProto(_message.Message):
    __slots__ = ("memory_info_vector",)
    MEMORY_INFO_VECTOR_FIELD_NUMBER: _ClassVar[int]
    memory_info_vector: _containers.RepeatedCompositeFieldContainer[MemInfoArrayProto]
    def __init__(self, memory_info_vector: _Optional[_Iterable[_Union[MemInfoArrayProto, _Mapping]]] = ...) -> None: ...

class MemStat(_message.Message):
    __slots__ = ("mem_stat_vector",)
    class MemStatCpuInfo(_message.Message):
        __slots__ = ("cpu_id", "percentage_usr", "percentage_nice", "percentage_sys", "percentage_iowait", "percentage_irq", "percentage_soft", "percentage_guest", "percentage_gnice", "percentage_idle", "timestamp", "percentage_steal")
        CPU_ID_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_USR_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_NICE_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_SYS_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_IOWAIT_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_IRQ_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_SOFT_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_GUEST_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_GNICE_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_IDLE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_STEAL_FIELD_NUMBER: _ClassVar[int]
        cpu_id: str
        percentage_usr: float
        percentage_nice: float
        percentage_sys: float
        percentage_iowait: float
        percentage_irq: float
        percentage_soft: float
        percentage_guest: float
        percentage_gnice: float
        percentage_idle: float
        timestamp: str
        percentage_steal: float
        def __init__(self, cpu_id: _Optional[str] = ..., percentage_usr: _Optional[float] = ..., percentage_nice: _Optional[float] = ..., percentage_sys: _Optional[float] = ..., percentage_iowait: _Optional[float] = ..., percentage_irq: _Optional[float] = ..., percentage_soft: _Optional[float] = ..., percentage_guest: _Optional[float] = ..., percentage_gnice: _Optional[float] = ..., percentage_idle: _Optional[float] = ..., timestamp: _Optional[str] = ..., percentage_steal: _Optional[float] = ...) -> None: ...
    MEM_STAT_VECTOR_FIELD_NUMBER: _ClassVar[int]
    mem_stat_vector: _containers.RepeatedCompositeFieldContainer[MemStat.MemStatCpuInfo]
    def __init__(self, mem_stat_vector: _Optional[_Iterable[_Union[MemStat.MemStatCpuInfo, _Mapping]]] = ...) -> None: ...

class SarProto(_message.Message):
    __slots__ = ("interfaces",)
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    interfaces: _containers.RepeatedCompositeFieldContainer[SarInterfaces]
    def __init__(self, interfaces: _Optional[_Iterable[_Union[SarInterfaces, _Mapping]]] = ...) -> None: ...

class SarInterfaces(_message.Message):
    __slots__ = ("interface_id", "stats_list")
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_LIST_FIELD_NUMBER: _ClassVar[int]
    interface_id: str
    stats_list: InterfaceStats
    def __init__(self, interface_id: _Optional[str] = ..., stats_list: _Optional[_Union[InterfaceStats, _Mapping]] = ...) -> None: ...

class InterfaceStats(_message.Message):
    __slots__ = ("rxpck", "txpck", "rxKb", "txKb", "rxcmp", "txcmp", "rxmcst")
    RXPCK_FIELD_NUMBER: _ClassVar[int]
    TXPCK_FIELD_NUMBER: _ClassVar[int]
    RXKB_FIELD_NUMBER: _ClassVar[int]
    TXKB_FIELD_NUMBER: _ClassVar[int]
    RXCMP_FIELD_NUMBER: _ClassVar[int]
    TXCMP_FIELD_NUMBER: _ClassVar[int]
    RXMCST_FIELD_NUMBER: _ClassVar[int]
    rxpck: float
    txpck: float
    rxKb: float
    txKb: float
    rxcmp: float
    txcmp: float
    rxmcst: float
    def __init__(self, rxpck: _Optional[float] = ..., txpck: _Optional[float] = ..., rxKb: _Optional[float] = ..., txKb: _Optional[float] = ..., rxcmp: _Optional[float] = ..., txcmp: _Optional[float] = ..., rxmcst: _Optional[float] = ...) -> None: ...

class TopProto(_message.Message):
    __slots__ = ("top_stat", "process_stat")
    TOP_STAT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_STAT_FIELD_NUMBER: _ClassVar[int]
    top_stat: _containers.RepeatedCompositeFieldContainer[TopInfo]
    process_stat: _containers.RepeatedCompositeFieldContainer[ProcessInfo]
    def __init__(self, top_stat: _Optional[_Iterable[_Union[TopInfo, _Mapping]]] = ..., process_stat: _Optional[_Iterable[_Union[ProcessInfo, _Mapping]]] = ...) -> None: ...

class TopInfo(_message.Message):
    __slots__ = ("stat_name", "Value")
    STAT_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    stat_name: str
    Value: str
    def __init__(self, stat_name: _Optional[str] = ..., Value: _Optional[str] = ...) -> None: ...

class ProcessInfo(_message.Message):
    __slots__ = ("pid", "ppid", "user", "ni", "virt", "res", "shr", "percentage_cpu", "percentage_mem", "timestamp", "process", "priority")
    PID_FIELD_NUMBER: _ClassVar[int]
    PPID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    NI_FIELD_NUMBER: _ClassVar[int]
    VIRT_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    SHR_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_CPU_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_MEM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    pid: int
    ppid: int
    user: str
    ni: int
    virt: str
    res: str
    shr: str
    percentage_cpu: float
    percentage_mem: float
    timestamp: str
    process: str
    priority: str
    def __init__(self, pid: _Optional[int] = ..., ppid: _Optional[int] = ..., user: _Optional[str] = ..., ni: _Optional[int] = ..., virt: _Optional[str] = ..., res: _Optional[str] = ..., shr: _Optional[str] = ..., percentage_cpu: _Optional[float] = ..., percentage_mem: _Optional[float] = ..., timestamp: _Optional[str] = ..., process: _Optional[str] = ..., priority: _Optional[str] = ...) -> None: ...

class IoTopProto(_message.Message):
    __slots__ = ("io_top_general", "io_top_process")
    IO_TOP_GENERAL_FIELD_NUMBER: _ClassVar[int]
    IO_TOP_PROCESS_FIELD_NUMBER: _ClassVar[int]
    io_top_general: IoTopGeneralProto
    io_top_process: _containers.RepeatedCompositeFieldContainer[IoTopProcessProto]
    def __init__(self, io_top_general: _Optional[_Union[IoTopGeneralProto, _Mapping]] = ..., io_top_process: _Optional[_Iterable[_Union[IoTopProcessProto, _Mapping]]] = ...) -> None: ...

class IoTopGeneralProto(_message.Message):
    __slots__ = ("total_disk_read", "actual_disk_read", "total_disk_write", "actual_disk_write")
    TOTAL_DISK_READ_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DISK_READ_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_WRITE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DISK_WRITE_FIELD_NUMBER: _ClassVar[int]
    total_disk_read: float
    actual_disk_read: float
    total_disk_write: float
    actual_disk_write: float
    def __init__(self, total_disk_read: _Optional[float] = ..., actual_disk_read: _Optional[float] = ..., total_disk_write: _Optional[float] = ..., actual_disk_write: _Optional[float] = ...) -> None: ...

class IoTopProcessProto(_message.Message):
    __slots__ = ("timestamp", "process_id", "prio", "user", "disk_read", "disk_write", "percentage_swapin", "percentage_io", "command")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PRIO_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DISK_READ_FIELD_NUMBER: _ClassVar[int]
    DISK_WRITE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_SWAPIN_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_IO_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    process_id: int
    prio: str
    user: str
    disk_read: float
    disk_write: float
    percentage_swapin: float
    percentage_io: float
    command: str
    def __init__(self, timestamp: _Optional[str] = ..., process_id: _Optional[int] = ..., prio: _Optional[str] = ..., user: _Optional[str] = ..., disk_read: _Optional[float] = ..., disk_write: _Optional[float] = ..., percentage_swapin: _Optional[float] = ..., percentage_io: _Optional[float] = ..., command: _Optional[str] = ...) -> None: ...
