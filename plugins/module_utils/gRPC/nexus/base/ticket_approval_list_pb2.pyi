from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TicketApprovalListProto(_message.Message):
    __slots__ = ("ticket_approval_list", "version")
    class TicketApproval(_message.Message):
        __slots__ = ("jira_epic_id", "is_rma_for_enablement", "modified_by", "timestamp_secs", "notes")
        JIRA_EPIC_ID_FIELD_NUMBER: _ClassVar[int]
        IS_RMA_FOR_ENABLEMENT_FIELD_NUMBER: _ClassVar[int]
        MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        NOTES_FIELD_NUMBER: _ClassVar[int]
        jira_epic_id: str
        is_rma_for_enablement: bool
        modified_by: str
        timestamp_secs: int
        notes: str
        def __init__(self, jira_epic_id: _Optional[str] = ..., is_rma_for_enablement: bool = ..., modified_by: _Optional[str] = ..., timestamp_secs: _Optional[int] = ..., notes: _Optional[str] = ...) -> None: ...
    TICKET_APPROVAL_LIST_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ticket_approval_list: _containers.RepeatedCompositeFieldContainer[TicketApprovalListProto.TicketApproval]
    version: int
    def __init__(self, ticket_approval_list: _Optional[_Iterable[_Union[TicketApprovalListProto.TicketApproval, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...
