from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadStatusResponse(_message.Message):
    __slots__ = ("status", "progress_pct")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[DownloadStatusResponse.Status]
        kInProgress: _ClassVar[DownloadStatusResponse.Status]
        kComplete: _ClassVar[DownloadStatusResponse.Status]
        kFailed: _ClassVar[DownloadStatusResponse.Status]
    kNotStarted: DownloadStatusResponse.Status
    kInProgress: DownloadStatusResponse.Status
    kComplete: DownloadStatusResponse.Status
    kFailed: DownloadStatusResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PCT_FIELD_NUMBER: _ClassVar[int]
    status: DownloadStatusResponse.Status
    progress_pct: float
    def __init__(self, status: _Optional[_Union[DownloadStatusResponse.Status, str]] = ..., progress_pct: _Optional[float] = ...) -> None: ...
