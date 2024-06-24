from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AcquireArg(_message.Message):
    __slots__ = ("domain_id", "entity_id", "is_exclusive", "can_forward", "recall_if_idle", "slave_session_id", "slave_has_pinned_tickets", "acquire_token", "need_remote_session_id_if_not_pinned", "expected_ticket_sequencer_high", "expected_ticket_sequencer_low", "rpc_version")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    CAN_FORWARD_FIELD_NUMBER: _ClassVar[int]
    RECALL_IF_IDLE_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SLAVE_HAS_PINNED_TICKETS_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEED_REMOTE_SESSION_ID_IF_NOT_PINNED_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    RPC_VERSION_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    entity_id: int
    is_exclusive: bool
    can_forward: bool
    recall_if_idle: bool
    slave_session_id: int
    slave_has_pinned_tickets: bool
    acquire_token: int
    need_remote_session_id_if_not_pinned: bool
    expected_ticket_sequencer_high: int
    expected_ticket_sequencer_low: int
    rpc_version: int
    def __init__(self, domain_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., is_exclusive: bool = ..., can_forward: bool = ..., recall_if_idle: bool = ..., slave_session_id: _Optional[int] = ..., slave_has_pinned_tickets: bool = ..., acquire_token: _Optional[int] = ..., need_remote_session_id_if_not_pinned: bool = ..., expected_ticket_sequencer_high: _Optional[int] = ..., expected_ticket_sequencer_low: _Optional[int] = ..., rpc_version: _Optional[int] = ...) -> None: ...

class AcquireResult(_message.Message):
    __slots__ = ("is_exclusive", "remote_slave_session_id", "ticket_sequencer_high", "ticket_sequencer_low", "last_exclusive_holder_death_relative_usecs", "last_slave_death_relative_usecs")
    IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_SEQUENCER_HIGH_FIELD_NUMBER: _ClassVar[int]
    TICKET_SEQUENCER_LOW_FIELD_NUMBER: _ClassVar[int]
    LAST_EXCLUSIVE_HOLDER_DEATH_RELATIVE_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_SLAVE_DEATH_RELATIVE_USECS_FIELD_NUMBER: _ClassVar[int]
    is_exclusive: int
    remote_slave_session_id: int
    ticket_sequencer_high: int
    ticket_sequencer_low: int
    last_exclusive_holder_death_relative_usecs: int
    last_slave_death_relative_usecs: int
    def __init__(self, is_exclusive: _Optional[int] = ..., remote_slave_session_id: _Optional[int] = ..., ticket_sequencer_high: _Optional[int] = ..., ticket_sequencer_low: _Optional[int] = ..., last_exclusive_holder_death_relative_usecs: _Optional[int] = ..., last_slave_death_relative_usecs: _Optional[int] = ...) -> None: ...

class IdleArg(_message.Message):
    __slots__ = ("domain_id", "entity_vec", "slave_session_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    entity_vec: _containers.RepeatedScalarFieldContainer[int]
    slave_session_id: int
    def __init__(self, domain_id: _Optional[int] = ..., entity_vec: _Optional[_Iterable[int]] = ..., slave_session_id: _Optional[int] = ...) -> None: ...

class IdleResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecallArg(_message.Message):
    __slots__ = ("domain_id", "entity_id", "recall_if_idle", "recall_exclusive_only", "master_sequencer", "acquire_token", "initiator_slave_session_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RECALL_IF_IDLE_FIELD_NUMBER: _ClassVar[int]
    RECALL_EXCLUSIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    MASTER_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    ACQUIRE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    entity_id: int
    recall_if_idle: bool
    recall_exclusive_only: bool
    master_sequencer: int
    acquire_token: int
    initiator_slave_session_id: int
    def __init__(self, domain_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., recall_if_idle: bool = ..., recall_exclusive_only: bool = ..., master_sequencer: _Optional[int] = ..., acquire_token: _Optional[int] = ..., initiator_slave_session_id: _Optional[int] = ...) -> None: ...

class RecallResult(_message.Message):
    __slots__ = ("recalled_all", "slave_session_id")
    RECALLED_ALL_FIELD_NUMBER: _ClassVar[int]
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    recalled_all: bool
    slave_session_id: int
    def __init__(self, recalled_all: bool = ..., slave_session_id: _Optional[int] = ...) -> None: ...

class GetAllArg(_message.Message):
    __slots__ = ("domain_id", "master_sequencer", "master_ip", "master_port")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    MASTER_IP_FIELD_NUMBER: _ClassVar[int]
    MASTER_PORT_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    master_sequencer: int
    master_ip: str
    master_port: int
    def __init__(self, domain_id: _Optional[int] = ..., master_sequencer: _Optional[int] = ..., master_ip: _Optional[str] = ..., master_port: _Optional[int] = ...) -> None: ...

class GetAllResult(_message.Message):
    __slots__ = ("slave_session_id", "entity_vec", "is_exclusive_vec", "ticket_sequencer_high_vec", "ticket_sequencer_low_vec", "last_exclusive_holder_death_relative_usecs")
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_VEC_FIELD_NUMBER: _ClassVar[int]
    TICKET_SEQUENCER_HIGH_VEC_FIELD_NUMBER: _ClassVar[int]
    TICKET_SEQUENCER_LOW_VEC_FIELD_NUMBER: _ClassVar[int]
    LAST_EXCLUSIVE_HOLDER_DEATH_RELATIVE_USECS_FIELD_NUMBER: _ClassVar[int]
    slave_session_id: int
    entity_vec: _containers.RepeatedScalarFieldContainer[int]
    is_exclusive_vec: _containers.RepeatedScalarFieldContainer[bool]
    ticket_sequencer_high_vec: _containers.RepeatedScalarFieldContainer[int]
    ticket_sequencer_low_vec: _containers.RepeatedScalarFieldContainer[int]
    last_exclusive_holder_death_relative_usecs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, slave_session_id: _Optional[int] = ..., entity_vec: _Optional[_Iterable[int]] = ..., is_exclusive_vec: _Optional[_Iterable[bool]] = ..., ticket_sequencer_high_vec: _Optional[_Iterable[int]] = ..., ticket_sequencer_low_vec: _Optional[_Iterable[int]] = ..., last_exclusive_holder_death_relative_usecs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetOwnerSessionIdArg(_message.Message):
    __slots__ = ("domain_id", "entity_id", "is_exclusive")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    entity_id: int
    is_exclusive: bool
    def __init__(self, domain_id: _Optional[int] = ..., entity_id: _Optional[int] = ..., is_exclusive: bool = ...) -> None: ...

class GetOwnerSessionIdResult(_message.Message):
    __slots__ = ("slave_session_id",)
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    slave_session_id: int
    def __init__(self, slave_session_id: _Optional[int] = ...) -> None: ...
