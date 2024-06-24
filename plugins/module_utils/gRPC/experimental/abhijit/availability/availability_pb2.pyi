from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Disk(_message.Message):
    __slots__ = ("type", "id", "mtbf_hours", "node_id", "cluster_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHDD: _ClassVar[Disk.Type]
        kSSD: _ClassVar[Disk.Type]
    kHDD: Disk.Type
    kSSD: Disk.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MTBF_HOURS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    type: Disk.Type
    id: int
    mtbf_hours: int
    node_id: int
    cluster_id: int
    def __init__(self, type: _Optional[_Union[Disk.Type, str]] = ..., id: _Optional[int] = ..., mtbf_hours: _Optional[int] = ..., node_id: _Optional[int] = ..., cluster_id: _Optional[int] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("id", "cluster_id", "hdd_disk_id_vec", "ssd_disk_id_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    HDD_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SSD_DISK_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    cluster_id: int
    hdd_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    ssd_disk_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., cluster_id: _Optional[int] = ..., hdd_disk_id_vec: _Optional[_Iterable[int]] = ..., ssd_disk_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("id", "node_vec", "hdd_disk_vec", "ssd_disk_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    HDD_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    SSD_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_vec: _containers.RepeatedCompositeFieldContainer[Node]
    hdd_disk_vec: _containers.RepeatedCompositeFieldContainer[Disk]
    ssd_disk_vec: _containers.RepeatedCompositeFieldContainer[Disk]
    def __init__(self, id: _Optional[int] = ..., node_vec: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., hdd_disk_vec: _Optional[_Iterable[_Union[Disk, _Mapping]]] = ..., ssd_disk_vec: _Optional[_Iterable[_Union[Disk, _Mapping]]] = ...) -> None: ...

class DiskFailureSummaryInfo(_message.Message):
    __slots__ = ("num_disk_failures", "num_disk_healed", "num_node_failures")
    NUM_DISK_FAILURES_FIELD_NUMBER: _ClassVar[int]
    NUM_DISK_HEALED_FIELD_NUMBER: _ClassVar[int]
    NUM_NODE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    num_disk_failures: int
    num_disk_healed: int
    num_node_failures: int
    def __init__(self, num_disk_failures: _Optional[int] = ..., num_disk_healed: _Optional[int] = ..., num_node_failures: _Optional[int] = ...) -> None: ...

class SimulationResult(_message.Message):
    __slots__ = ("failed_disks_map", "hdd_failure_summary_info", "ssd_failure_summary_info", "failure_time_hours")
    class FailedDisksMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    FAILED_DISKS_MAP_FIELD_NUMBER: _ClassVar[int]
    HDD_FAILURE_SUMMARY_INFO_FIELD_NUMBER: _ClassVar[int]
    SSD_FAILURE_SUMMARY_INFO_FIELD_NUMBER: _ClassVar[int]
    FAILURE_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
    failed_disks_map: _containers.ScalarMap[int, int]
    hdd_failure_summary_info: DiskFailureSummaryInfo
    ssd_failure_summary_info: DiskFailureSummaryInfo
    failure_time_hours: int
    def __init__(self, failed_disks_map: _Optional[_Mapping[int, int]] = ..., hdd_failure_summary_info: _Optional[_Union[DiskFailureSummaryInfo, _Mapping]] = ..., ssd_failure_summary_info: _Optional[_Union[DiskFailureSummaryInfo, _Mapping]] = ..., failure_time_hours: _Optional[int] = ...) -> None: ...
