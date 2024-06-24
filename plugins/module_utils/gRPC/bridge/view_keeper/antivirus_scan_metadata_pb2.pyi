from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileAntivirusScanInfo(_message.Message):
    __slots__ = ("state", "service_group_id", "service_id", "service_icap_uri", "service_icap_tag", "service_icap_tag_id", "scan_timestamp_usecs", "mtime_usecs", "remediation", "threat_list")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnconfigured: _ClassVar[FileAntivirusScanInfo.State]
        kScanned: _ClassVar[FileAntivirusScanInfo.State]
        kStaleScan: _ClassVar[FileAntivirusScanInfo.State]
    kUnconfigured: FileAntivirusScanInfo.State
    kScanned: FileAntivirusScanInfo.State
    kStaleScan: FileAntivirusScanInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ICAP_URI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ICAP_TAG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ICAP_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    SCAN_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    THREAT_LIST_FIELD_NUMBER: _ClassVar[int]
    state: FileAntivirusScanInfo.State
    service_group_id: int
    service_id: int
    service_icap_uri: str
    service_icap_tag: str
    service_icap_tag_id: int
    scan_timestamp_usecs: int
    mtime_usecs: int
    remediation: _snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata.Remediation
    threat_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, state: _Optional[_Union[FileAntivirusScanInfo.State, str]] = ..., service_group_id: _Optional[int] = ..., service_id: _Optional[int] = ..., service_icap_uri: _Optional[str] = ..., service_icap_tag: _Optional[str] = ..., service_icap_tag_id: _Optional[int] = ..., scan_timestamp_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., remediation: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata.Remediation, str]] = ..., threat_list: _Optional[_Iterable[str]] = ...) -> None: ...
