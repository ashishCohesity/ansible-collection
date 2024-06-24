from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VdbenchWriteState(_message.Message):
    __slots__ = ("write_cmd", "is_write_job_done", "mount_path", "io_dir", "journal_dir", "last_update_timestamp")
    WRITE_CMD_FIELD_NUMBER: _ClassVar[int]
    IS_WRITE_JOB_DONE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    IO_DIR_FIELD_NUMBER: _ClassVar[int]
    JOURNAL_DIR_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    write_cmd: str
    is_write_job_done: bool
    mount_path: str
    io_dir: str
    journal_dir: str
    last_update_timestamp: str
    def __init__(self, write_cmd: _Optional[str] = ..., is_write_job_done: bool = ..., mount_path: _Optional[str] = ..., io_dir: _Optional[str] = ..., journal_dir: _Optional[str] = ..., last_update_timestamp: _Optional[str] = ...) -> None: ...
