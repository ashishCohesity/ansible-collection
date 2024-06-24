from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

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
    __slots__ = ("job_id", "object_size")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    object_size: int
    def __init__(self, job_id: _Optional[int] = ..., object_size: _Optional[int] = ...) -> None: ...
