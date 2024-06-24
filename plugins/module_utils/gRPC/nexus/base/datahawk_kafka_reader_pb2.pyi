from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DHTelemetryEvent(_message.Message):
    __slots__ = ("dataPoolsStatsList",)
    DATAPOOLSSTATSLIST_FIELD_NUMBER: _ClassVar[int]
    dataPoolsStatsList: _containers.RepeatedCompositeFieldContainer[DataPoolStats]
    def __init__(self, dataPoolsStatsList: _Optional[_Iterable[_Union[DataPoolStats, _Mapping]]] = ...) -> None: ...

class DataPoolStats(_message.Message):
    __slots__ = ("sf_account_id", "data_pool_id", "data_pool_name", "data_pool_shield_type", "data_source_id", "view_id", "view_name", "vm_id", "vm_name", "smartfilesStats", "antiRansomwareStats", "threatDetectionStats")
    SF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_POOL_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_POOL_SHIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    SMARTFILESSTATS_FIELD_NUMBER: _ClassVar[int]
    ANTIRANSOMWARESTATS_FIELD_NUMBER: _ClassVar[int]
    THREATDETECTIONSTATS_FIELD_NUMBER: _ClassVar[int]
    sf_account_id: str
    data_pool_id: str
    data_pool_name: str
    data_pool_shield_type: str
    data_source_id: str
    view_id: str
    view_name: str
    vm_id: str
    vm_name: str
    smartfilesStats: SmartfilesStats
    antiRansomwareStats: AntiRansomwareStats
    threatDetectionStats: ThreatDetectionStats
    def __init__(self, sf_account_id: _Optional[str] = ..., data_pool_id: _Optional[str] = ..., data_pool_name: _Optional[str] = ..., data_pool_shield_type: _Optional[str] = ..., data_source_id: _Optional[str] = ..., view_id: _Optional[str] = ..., view_name: _Optional[str] = ..., vm_id: _Optional[str] = ..., vm_name: _Optional[str] = ..., smartfilesStats: _Optional[_Union[SmartfilesStats, _Mapping]] = ..., antiRansomwareStats: _Optional[_Union[AntiRansomwareStats, _Mapping]] = ..., threatDetectionStats: _Optional[_Union[ThreatDetectionStats, _Mapping]] = ...) -> None: ...

class SmartfilesStats(_message.Message):
    __slots__ = ("data_governed_gb",)
    DATA_GOVERNED_GB_FIELD_NUMBER: _ClassVar[int]
    data_governed_gb: float
    def __init__(self, data_governed_gb: _Optional[float] = ...) -> None: ...

class AntiRansomwareStats(_message.Message):
    __slots__ = ("data_classified_gb",)
    DATA_CLASSIFIED_GB_FIELD_NUMBER: _ClassVar[int]
    data_classified_gb: float
    def __init__(self, data_classified_gb: _Optional[float] = ...) -> None: ...

class ThreatDetectionStats(_message.Message):
    __slots__ = ("data_scanned_gb",)
    DATA_SCANNED_GB_FIELD_NUMBER: _ClassVar[int]
    data_scanned_gb: float
    def __init__(self, data_scanned_gb: _Optional[float] = ...) -> None: ...
