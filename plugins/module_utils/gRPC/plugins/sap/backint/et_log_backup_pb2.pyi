from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IpcFileProto(_message.Message):
    __slots__ = ("bytes_transferred", "total_bytes", "status", "externally_triggered_run_id", "err_msg")
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_TRIGGERED_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    bytes_transferred: int
    total_bytes: int
    status: str
    externally_triggered_run_id: str
    err_msg: str
    def __init__(self, bytes_transferred: _Optional[int] = ..., total_bytes: _Optional[int] = ..., status: _Optional[str] = ..., externally_triggered_run_id: _Optional[str] = ..., err_msg: _Optional[str] = ...) -> None: ...
