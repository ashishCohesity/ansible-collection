from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpgradeInfo(_message.Message):
    __slots__ = ("target_version", "package_url", "timestamp_msecs")
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_URL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    target_version: str
    package_url: str
    timestamp_msecs: int
    def __init__(self, target_version: _Optional[str] = ..., package_url: _Optional[str] = ..., timestamp_msecs: _Optional[int] = ...) -> None: ...
