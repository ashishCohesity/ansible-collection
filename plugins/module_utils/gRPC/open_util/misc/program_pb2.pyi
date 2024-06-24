from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestartStateProto(_message.Message):
    __slots__ = ("restart_reason", "restart_reason_string", "pid")
    class RestartReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kReasonCleared: _ClassVar[RestartStateProto.RestartReason]
        kReasonOutOfMemory: _ClassVar[RestartStateProto.RestartReason]
    kReasonCleared: RestartStateProto.RestartReason
    kReasonOutOfMemory: RestartStateProto.RestartReason
    RESTART_REASON_FIELD_NUMBER: _ClassVar[int]
    RESTART_REASON_STRING_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    restart_reason: RestartStateProto.RestartReason
    restart_reason_string: str
    pid: int
    def __init__(self, restart_reason: _Optional[_Union[RestartStateProto.RestartReason, str]] = ..., restart_reason_string: _Optional[str] = ..., pid: _Optional[int] = ...) -> None: ...
