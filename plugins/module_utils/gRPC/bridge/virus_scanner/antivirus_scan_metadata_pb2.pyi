from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AntivirusSnapTreeValueProto(_message.Message):
    __slots__ = ("path", "threat_list", "scan_timestamp_usecs", "service_icap_uri", "service_group_id", "service_id", "service_icap_tag", "service_icap_tag_id", "service_provider_name")
    PATH_FIELD_NUMBER: _ClassVar[int]
    THREAT_LIST_FIELD_NUMBER: _ClassVar[int]
    SCAN_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ICAP_URI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ICAP_TAG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ICAP_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    threat_list: _containers.RepeatedScalarFieldContainer[str]
    scan_timestamp_usecs: int
    service_icap_uri: str
    service_group_id: int
    service_id: int
    service_icap_tag: str
    service_icap_tag_id: int
    service_provider_name: str
    def __init__(self, path: _Optional[str] = ..., threat_list: _Optional[_Iterable[str]] = ..., scan_timestamp_usecs: _Optional[int] = ..., service_icap_uri: _Optional[str] = ..., service_group_id: _Optional[int] = ..., service_id: _Optional[int] = ..., service_icap_tag: _Optional[str] = ..., service_icap_tag_id: _Optional[int] = ..., service_provider_name: _Optional[str] = ...) -> None: ...

class ListInfectedFilesCookie(_message.Message):
    __slots__ = ("view_id_vec", "include_quarantined_files", "include_unquarantined_files", "current_view_id", "previous_snap_tree_key")
    VIEW_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_QUARANTINED_FILES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNQUARANTINED_FILES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SNAP_TREE_KEY_FIELD_NUMBER: _ClassVar[int]
    view_id_vec: _containers.RepeatedScalarFieldContainer[int]
    include_quarantined_files: bool
    include_unquarantined_files: bool
    current_view_id: int
    previous_snap_tree_key: bytes
    def __init__(self, view_id_vec: _Optional[_Iterable[int]] = ..., include_quarantined_files: bool = ..., include_unquarantined_files: bool = ..., current_view_id: _Optional[int] = ..., previous_snap_tree_key: _Optional[bytes] = ...) -> None: ...
