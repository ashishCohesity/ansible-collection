from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class APIVersion(_message.Message):
    __slots__ = ("version", "replication_version", "master_version", "export_metadata_version")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPORT_METADATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    replication_version: int
    master_version: int
    export_metadata_version: int
    def __init__(self, version: _Optional[int] = ..., replication_version: _Optional[int] = ..., master_version: _Optional[int] = ..., export_metadata_version: _Optional[int] = ...) -> None: ...
