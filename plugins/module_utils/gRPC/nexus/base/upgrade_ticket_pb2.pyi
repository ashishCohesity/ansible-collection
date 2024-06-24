from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpgradeTicketProto(_message.Message):
    __slots__ = ("node_id", "ticket_acquired_time_secs", "acquire_reason", "gandalf_key")
    class AcquireReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpgrade: _ClassVar[UpgradeTicketProto.AcquireReason]
        kClusterRestart: _ClassVar[UpgradeTicketProto.AcquireReason]
        kYodaXFSIssue: _ClassVar[UpgradeTicketProto.AcquireReason]
    kUpgrade: UpgradeTicketProto.AcquireReason
    kClusterRestart: UpgradeTicketProto.AcquireReason
    kYodaXFSIssue: UpgradeTicketProto.AcquireReason
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ACQUIRED_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_REASON_FIELD_NUMBER: _ClassVar[int]
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    ticket_acquired_time_secs: int
    acquire_reason: UpgradeTicketProto.AcquireReason
    gandalf_key: str
    def __init__(self, node_id: _Optional[int] = ..., ticket_acquired_time_secs: _Optional[int] = ..., acquire_reason: _Optional[_Union[UpgradeTicketProto.AcquireReason, str]] = ..., gandalf_key: _Optional[str] = ...) -> None: ...
