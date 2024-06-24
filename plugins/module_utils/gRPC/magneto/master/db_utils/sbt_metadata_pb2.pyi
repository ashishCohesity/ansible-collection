from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SbtMetadataProto(_message.Message):
    __slots__ = ("major_version", "minor_version", "db_name", "db_id", "mount_path", "vip", "enable_sbt_list")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    VIP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SBT_LIST_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    db_name: str
    db_id: int
    mount_path: str
    vip: str
    enable_sbt_list: bool
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., db_name: _Optional[str] = ..., db_id: _Optional[int] = ..., mount_path: _Optional[str] = ..., vip: _Optional[str] = ..., enable_sbt_list: bool = ...) -> None: ...
