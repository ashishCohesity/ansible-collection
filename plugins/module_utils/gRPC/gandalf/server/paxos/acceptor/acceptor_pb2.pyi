from gandalf.server.paxos.base import paxos_pb2 as _paxos_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstanceStateHeader(_message.Message):
    __slots__ = ("is_chosen", "instance", "proposal")
    IS_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    is_chosen: bool
    instance: int
    proposal: _paxos_pb2.ProposalId
    def __init__(self, is_chosen: bool = ..., instance: _Optional[int] = ..., proposal: _Optional[_Union[_paxos_pb2.ProposalId, _Mapping]] = ...) -> None: ...

class MaxDiscoveredInstance(_message.Message):
    __slots__ = ("instance",)
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    instance: int
    def __init__(self, instance: _Optional[int] = ...) -> None: ...
