from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadContext(_message.Message):
    __slots__ = ("job_id", "restore_finished")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    job_id: int
    restore_finished: bool
    def __init__(self, job_id: _Optional[int] = ..., restore_finished: bool = ...) -> None: ...
