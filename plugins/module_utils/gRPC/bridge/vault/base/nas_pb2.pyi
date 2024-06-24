from bridge.vault.base import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadContext(_message.Message):
    __slots__ = ("object_name", "archive_object_finalized", "archive_object_file_size_bytes")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    archive_object_finalized: bool
    archive_object_file_size_bytes: int
    def __init__(self, object_name: _Optional[str] = ..., archive_object_finalized: bool = ..., archive_object_file_size_bytes: _Optional[int] = ...) -> None: ...

class DownloadContext(_message.Message):
    __slots__ = ("object_size",)
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    object_size: int
    def __init__(self, object_size: _Optional[int] = ...) -> None: ...

class NasCookie(_message.Message):
    __slots__ = ("monitoring_cookie",)
    MONITORING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    monitoring_cookie: _common_pb2.MonitoringCookie
    def __init__(self, monitoring_cookie: _Optional[_Union[_common_pb2.MonitoringCookie, _Mapping]] = ...) -> None: ...
