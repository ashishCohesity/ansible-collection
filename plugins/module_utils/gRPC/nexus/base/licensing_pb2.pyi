from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LicensingProto(_message.Message):
    __slots__ = ("base_uri", "api_version", "api_version2", "account_usage_uri")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION2_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_USAGE_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    api_version: str
    api_version2: str
    account_usage_uri: str
    def __init__(self, base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., api_version2: _Optional[str] = ..., account_usage_uri: _Optional[str] = ...) -> None: ...
