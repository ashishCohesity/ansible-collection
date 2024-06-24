from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FRUData(_message.Message):
    __slots__ = ("cluster_id", "rack_id", "chassis_id", "node_id", "disk_list", "fan_list")
    class FRUType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDisk: _ClassVar[FRUData.FRUType]
        kFan: _ClassVar[FRUData.FRUType]
    kDisk: FRUData.FRUType
    kFan: FRUData.FRUType
    class DiskData(_message.Message):
        __slots__ = ("fru_type", "id", "slot_id", "name", "serial_no", "label", "type", "size", "vendor_name", "error_count", "wear_percentage")
        FRU_TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERIAL_NO_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        WEAR_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        fru_type: FRUData.FRUType
        id: str
        slot_id: str
        name: str
        serial_no: str
        label: _containers.RepeatedScalarFieldContainer[str]
        type: str
        size: int
        vendor_name: str
        error_count: int
        wear_percentage: float
        def __init__(self, fru_type: _Optional[_Union[FRUData.FRUType, str]] = ..., id: _Optional[str] = ..., slot_id: _Optional[str] = ..., name: _Optional[str] = ..., serial_no: _Optional[str] = ..., label: _Optional[_Iterable[str]] = ..., type: _Optional[str] = ..., size: _Optional[int] = ..., vendor_name: _Optional[str] = ..., error_count: _Optional[int] = ..., wear_percentage: _Optional[float] = ...) -> None: ...
    class FanData(_message.Message):
        __slots__ = ("fru_type", "id", "name", "vendor_name", "avg_rpm_percent")
        FRU_TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VENDOR_NAME_FIELD_NUMBER: _ClassVar[int]
        AVG_RPM_PERCENT_FIELD_NUMBER: _ClassVar[int]
        fru_type: FRUData.FRUType
        id: str
        name: str
        vendor_name: str
        avg_rpm_percent: float
        def __init__(self, fru_type: _Optional[_Union[FRUData.FRUType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., vendor_name: _Optional[str] = ..., avg_rpm_percent: _Optional[float] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RACK_ID_FIELD_NUMBER: _ClassVar[int]
    CHASSIS_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_LIST_FIELD_NUMBER: _ClassVar[int]
    FAN_LIST_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    rack_id: int
    chassis_id: int
    node_id: int
    disk_list: _containers.RepeatedCompositeFieldContainer[FRUData.DiskData]
    fan_list: _containers.RepeatedCompositeFieldContainer[FRUData.FanData]
    def __init__(self, cluster_id: _Optional[int] = ..., rack_id: _Optional[int] = ..., chassis_id: _Optional[int] = ..., node_id: _Optional[int] = ..., disk_list: _Optional[_Iterable[_Union[FRUData.DiskData, _Mapping]]] = ..., fan_list: _Optional[_Iterable[_Union[FRUData.FanData, _Mapping]]] = ...) -> None: ...
