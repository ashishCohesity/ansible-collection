from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PureFlashBladeEndpointsProto(_message.Message):
    __slots__ = ("current_version", "login_uri", "api_versions_uri", "network_interfaces_uri", "filesystems_uri", "available_space_uri", "array_info_uri", "file_system_snapshots_uri")
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOGIN_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSIONS_URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_URI_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEMS_URI_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SPACE_URI_FIELD_NUMBER: _ClassVar[int]
    ARRAY_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_SNAPSHOTS_URI_FIELD_NUMBER: _ClassVar[int]
    current_version: str
    login_uri: str
    api_versions_uri: str
    network_interfaces_uri: str
    filesystems_uri: str
    available_space_uri: str
    array_info_uri: str
    file_system_snapshots_uri: str
    def __init__(self, current_version: _Optional[str] = ..., login_uri: _Optional[str] = ..., api_versions_uri: _Optional[str] = ..., network_interfaces_uri: _Optional[str] = ..., filesystems_uri: _Optional[str] = ..., available_space_uri: _Optional[str] = ..., array_info_uri: _Optional[str] = ..., file_system_snapshots_uri: _Optional[str] = ...) -> None: ...
