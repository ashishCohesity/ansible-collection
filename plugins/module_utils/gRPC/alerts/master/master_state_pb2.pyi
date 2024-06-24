from alerts.base import alert_pb2 as _alert_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertIndexProto(_message.Message):
    __slots__ = ("index_type", "index_key", "alert_id_list", "update_type", "intent")
    class IndexType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAlertType: _ClassVar[AlertIndexProto.IndexType]
        kAlertCategory: _ClassVar[AlertIndexProto.IndexType]
        kSeverity: _ClassVar[AlertIndexProto.IndexType]
        kAlertState: _ClassVar[AlertIndexProto.IndexType]
        kResolution: _ClassVar[AlertIndexProto.IndexType]
        kProperty: _ClassVar[AlertIndexProto.IndexType]
        kAll: _ClassVar[AlertIndexProto.IndexType]
        kIntent: _ClassVar[AlertIndexProto.IndexType]
        kHidden: _ClassVar[AlertIndexProto.IndexType]
        kSupport: _ClassVar[AlertIndexProto.IndexType]
        kTenantId: _ClassVar[AlertIndexProto.IndexType]
        kLastOccurrence: _ClassVar[AlertIndexProto.IndexType]
        kResolvedTime: _ClassVar[AlertIndexProto.IndexType]
    kAlertType: AlertIndexProto.IndexType
    kAlertCategory: AlertIndexProto.IndexType
    kSeverity: AlertIndexProto.IndexType
    kAlertState: AlertIndexProto.IndexType
    kResolution: AlertIndexProto.IndexType
    kProperty: AlertIndexProto.IndexType
    kAll: AlertIndexProto.IndexType
    kIntent: AlertIndexProto.IndexType
    kHidden: AlertIndexProto.IndexType
    kSupport: AlertIndexProto.IndexType
    kTenantId: AlertIndexProto.IndexType
    kLastOccurrence: AlertIndexProto.IndexType
    kResolvedTime: AlertIndexProto.IndexType
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdd: _ClassVar[AlertIndexProto.UpdateType]
        kRemove: _ClassVar[AlertIndexProto.UpdateType]
    kAdd: AlertIndexProto.UpdateType
    kRemove: AlertIndexProto.UpdateType
    INDEX_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_KEY_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    index_type: AlertIndexProto.IndexType
    index_key: str
    alert_id_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertIdProto]
    update_type: AlertIndexProto.UpdateType
    intent: bool
    def __init__(self, index_type: _Optional[_Union[AlertIndexProto.IndexType, str]] = ..., index_key: _Optional[str] = ..., alert_id_list: _Optional[_Iterable[_Union[_alert_pb2.AlertIdProto, _Mapping]]] = ..., update_type: _Optional[_Union[AlertIndexProto.UpdateType, str]] = ..., intent: bool = ...) -> None: ...

class ResolutionIndexProto(_message.Message):
    __slots__ = ("resolution_list", "update_type", "intent")
    class ResolutionIdPair(_message.Message):
        __slots__ = ("resolution_id", "resolution_creation_time_usecs")
        RESOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        resolution_id: int
        resolution_creation_time_usecs: int
        def __init__(self, resolution_id: _Optional[int] = ..., resolution_creation_time_usecs: _Optional[int] = ...) -> None: ...
    RESOLUTION_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    resolution_list: _containers.RepeatedCompositeFieldContainer[ResolutionIndexProto.ResolutionIdPair]
    update_type: AlertIndexProto.UpdateType
    intent: bool
    def __init__(self, resolution_list: _Optional[_Iterable[_Union[ResolutionIndexProto.ResolutionIdPair, _Mapping]]] = ..., update_type: _Optional[_Union[AlertIndexProto.UpdateType, str]] = ..., intent: bool = ...) -> None: ...

class AlertByTimeStampIndexProto(_message.Message):
    __slots__ = ("index_type", "ts_alert_id_list", "update_type", "intent")
    class AlertByTimeStampPair(_message.Message):
        __slots__ = ("timestamp", "alert_id")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ALERT_ID_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        alert_id: _alert_pb2.AlertIdProto
        def __init__(self, timestamp: _Optional[int] = ..., alert_id: _Optional[_Union[_alert_pb2.AlertIdProto, _Mapping]] = ...) -> None: ...
    INDEX_TYPE_FIELD_NUMBER: _ClassVar[int]
    TS_ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    index_type: AlertIndexProto.IndexType
    ts_alert_id_list: _containers.RepeatedCompositeFieldContainer[AlertByTimeStampIndexProto.AlertByTimeStampPair]
    update_type: AlertIndexProto.UpdateType
    intent: bool
    def __init__(self, index_type: _Optional[_Union[AlertIndexProto.IndexType, str]] = ..., ts_alert_id_list: _Optional[_Iterable[_Union[AlertByTimeStampIndexProto.AlertByTimeStampPair, _Mapping]]] = ..., update_type: _Optional[_Union[AlertIndexProto.UpdateType, str]] = ..., intent: bool = ...) -> None: ...

class AlertCategoryUpdateProto(_message.Message):
    __slots__ = ("alert_type", "src_category", "target_category", "expected_version", "update_done")
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TARGET_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DONE_FIELD_NUMBER: _ClassVar[int]
    alert_type: int
    src_category: _alert_pb2.AlertMetadataProto.AlertCategory
    target_category: _alert_pb2.AlertMetadataProto.AlertCategory
    expected_version: int
    update_done: bool
    def __init__(self, alert_type: _Optional[int] = ..., src_category: _Optional[_Union[_alert_pb2.AlertMetadataProto.AlertCategory, str]] = ..., target_category: _Optional[_Union[_alert_pb2.AlertMetadataProto.AlertCategory, str]] = ..., expected_version: _Optional[int] = ..., update_done: bool = ...) -> None: ...

class WALRecordProto(_message.Message):
    __slots__ = ("alert_index_list", "resolution_index_list", "alert_category_update_list", "alert_last_time_list", "alert_ts_index_list")
    ALERT_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_CATEGORY_UPDATE_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_LAST_TIME_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_TS_INDEX_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_index_list: _containers.RepeatedCompositeFieldContainer[AlertIndexProto]
    resolution_index_list: _containers.RepeatedCompositeFieldContainer[ResolutionIndexProto]
    alert_category_update_list: _containers.RepeatedCompositeFieldContainer[AlertCategoryUpdateProto]
    alert_last_time_list: _containers.RepeatedCompositeFieldContainer[AlertIndexProto]
    alert_ts_index_list: _containers.RepeatedCompositeFieldContainer[AlertByTimeStampIndexProto]
    def __init__(self, alert_index_list: _Optional[_Iterable[_Union[AlertIndexProto, _Mapping]]] = ..., resolution_index_list: _Optional[_Iterable[_Union[ResolutionIndexProto, _Mapping]]] = ..., alert_category_update_list: _Optional[_Iterable[_Union[AlertCategoryUpdateProto, _Mapping]]] = ..., alert_last_time_list: _Optional[_Iterable[_Union[AlertIndexProto, _Mapping]]] = ..., alert_ts_index_list: _Optional[_Iterable[_Union[AlertByTimeStampIndexProto, _Mapping]]] = ...) -> None: ...
