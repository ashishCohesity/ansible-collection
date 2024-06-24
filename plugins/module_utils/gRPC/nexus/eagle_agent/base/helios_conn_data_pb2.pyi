from nexus.eagle_agent.base import helios_magneto_state_pb2 as _helios_magneto_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosAgentConnInfoProto(_message.Message):
    __slots__ = ("real_bundle_info", "nightly_bundle_info", "onprem_magneto_state_collection_info", "helios_magneto_state_collection_info", "vulscan_metadata_collection_info", "software_version", "stats_collection_info", "data_classification_collection_info", "tag_updates_collection_info", "audit_log_collection_info", "alerts_collection_info")
    REAL_BUNDLE_INFO_FIELD_NUMBER: _ClassVar[int]
    NIGHTLY_BUNDLE_INFO_FIELD_NUMBER: _ClassVar[int]
    ONPREM_MAGNETO_STATE_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    HELIOS_MAGNETO_STATE_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    VULSCAN_METADATA_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASSIFICATION_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    TAG_UPDATES_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOG_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ALERTS_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    real_bundle_info: RealTimeBundleInfo
    nightly_bundle_info: NightlyBundleInfo
    onprem_magneto_state_collection_info: MagnetoStateCollectionInfo
    helios_magneto_state_collection_info: MagnetoStateCollectionInfo
    vulscan_metadata_collection_info: VulscanMetadataCollectionInfo
    software_version: str
    stats_collection_info: LocalStatsCollectionInfo
    data_classification_collection_info: DataClassificationCollectionInfo
    tag_updates_collection_info: TagUpdatesCollectionInfo
    audit_log_collection_info: AuditLogCollectionInfo
    alerts_collection_info: AlertsCollectionInfo
    def __init__(self, real_bundle_info: _Optional[_Union[RealTimeBundleInfo, _Mapping]] = ..., nightly_bundle_info: _Optional[_Union[NightlyBundleInfo, _Mapping]] = ..., onprem_magneto_state_collection_info: _Optional[_Union[MagnetoStateCollectionInfo, _Mapping]] = ..., helios_magneto_state_collection_info: _Optional[_Union[MagnetoStateCollectionInfo, _Mapping]] = ..., vulscan_metadata_collection_info: _Optional[_Union[VulscanMetadataCollectionInfo, _Mapping]] = ..., software_version: _Optional[str] = ..., stats_collection_info: _Optional[_Union[LocalStatsCollectionInfo, _Mapping]] = ..., data_classification_collection_info: _Optional[_Union[DataClassificationCollectionInfo, _Mapping]] = ..., tag_updates_collection_info: _Optional[_Union[TagUpdatesCollectionInfo, _Mapping]] = ..., audit_log_collection_info: _Optional[_Union[AuditLogCollectionInfo, _Mapping]] = ..., alerts_collection_info: _Optional[_Union[AlertsCollectionInfo, _Mapping]] = ...) -> None: ...

class MagnetoStateCollectionInfo(_message.Message):
    __slots__ = ("cookie",)
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    cookie: _helios_magneto_state_pb2.MagnetoStateCookie
    def __init__(self, cookie: _Optional[_Union[_helios_magneto_state_pb2.MagnetoStateCookie, _Mapping]] = ...) -> None: ...

class RealTimeBundleInfo(_message.Message):
    __slots__ = ("real_bundle_usecs",)
    REAL_BUNDLE_USECS_FIELD_NUMBER: _ClassVar[int]
    real_bundle_usecs: int
    def __init__(self, real_bundle_usecs: _Optional[int] = ...) -> None: ...

class VulscanMetadataCollectionInfo(_message.Message):
    __slots__ = ("vulscan_metadata_collection_usecs",)
    VULSCAN_METADATA_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    vulscan_metadata_collection_usecs: int
    def __init__(self, vulscan_metadata_collection_usecs: _Optional[int] = ...) -> None: ...

class LocalStatsCollectionInfo(_message.Message):
    __slots__ = ("last_collection_usecs",)
    LAST_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    last_collection_usecs: int
    def __init__(self, last_collection_usecs: _Optional[int] = ...) -> None: ...

class DataClassificationCollectionInfo(_message.Message):
    __slots__ = ("data_classification_collection_usecs",)
    DATA_CLASSIFICATION_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    data_classification_collection_usecs: int
    def __init__(self, data_classification_collection_usecs: _Optional[int] = ...) -> None: ...

class NightlyBundleInfo(_message.Message):
    __slots__ = ("alerts_collection_usecs", "stats_collection_usecs", "tricorder_collection_usecs")
    ALERTS_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    STATS_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    TRICORDER_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    alerts_collection_usecs: int
    stats_collection_usecs: int
    tricorder_collection_usecs: int
    def __init__(self, alerts_collection_usecs: _Optional[int] = ..., stats_collection_usecs: _Optional[int] = ..., tricorder_collection_usecs: _Optional[int] = ...) -> None: ...

class TagUpdatesCollectionInfo(_message.Message):
    __slots__ = ("tag_updates_collection_usecs",)
    TAG_UPDATES_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    tag_updates_collection_usecs: int
    def __init__(self, tag_updates_collection_usecs: _Optional[int] = ...) -> None: ...

class AuditLogCollectionInfo(_message.Message):
    __slots__ = ("last_line_number", "last_file_read", "audit_log_collection_usecs")
    LAST_LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LAST_FILE_READ_FIELD_NUMBER: _ClassVar[int]
    AUDIT_LOG_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    last_line_number: int
    last_file_read: str
    audit_log_collection_usecs: int
    def __init__(self, last_line_number: _Optional[int] = ..., last_file_read: _Optional[str] = ..., audit_log_collection_usecs: _Optional[int] = ...) -> None: ...

class AlertsCollectionInfo(_message.Message):
    __slots__ = ("last_collection_usecs",)
    LAST_COLLECTION_USECS_FIELD_NUMBER: _ClassVar[int]
    last_collection_usecs: int
    def __init__(self, last_collection_usecs: _Optional[int] = ...) -> None: ...
