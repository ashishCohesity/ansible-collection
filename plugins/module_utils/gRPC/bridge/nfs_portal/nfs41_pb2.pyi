from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TableKey(_message.Message):
    __slots__ = ("client_owner_id", "client_id", "session_id", "state_id")
    CLIENT_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    client_owner_id: bytes
    client_id: int
    session_id: int
    state_id: int
    def __init__(self, client_owner_id: _Optional[bytes] = ..., client_id: _Optional[int] = ..., session_id: _Optional[int] = ..., state_id: _Optional[int] = ...) -> None: ...

class TableValue(_message.Message):
    __slots__ = ("client_owner_id_mapping", "server_ip_mapping", "client_id_mapping", "session_id_mapping", "state_id_mapping")
    class ClientOwnerIdMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ServerIpMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class ClientIdMapping(_message.Message):
        __slots__ = ("client_owner_id", "verifier", "server_ip", "expiration_usecs", "session_id_vec", "state_id_vec", "update_intent", "cs_reply_cache_vec")
        class UpdateIntent(_message.Message):
            __slots__ = ("opclock", "is_creation", "session_id_vec", "state_id_vec")
            OPCLOCK_FIELD_NUMBER: _ClassVar[int]
            IS_CREATION_FIELD_NUMBER: _ClassVar[int]
            SESSION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            STATE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
            opclock: _op_clock_pb2.OpClock
            is_creation: bool
            session_id_vec: _containers.RepeatedScalarFieldContainer[int]
            state_id_vec: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, opclock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., is_creation: bool = ..., session_id_vec: _Optional[_Iterable[int]] = ..., state_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
        class CreateSessionReplyCache(_message.Message):
            __slots__ = ("session_id", "seq")
            SESSION_ID_FIELD_NUMBER: _ClassVar[int]
            SEQ_FIELD_NUMBER: _ClassVar[int]
            session_id: int
            seq: int
            def __init__(self, session_id: _Optional[int] = ..., seq: _Optional[int] = ...) -> None: ...
        CLIENT_OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        VERIFIER_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_USECS_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        STATE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INTENT_FIELD_NUMBER: _ClassVar[int]
        CS_REPLY_CACHE_VEC_FIELD_NUMBER: _ClassVar[int]
        client_owner_id: bytes
        verifier: int
        server_ip: str
        expiration_usecs: int
        session_id_vec: _containers.RepeatedScalarFieldContainer[int]
        state_id_vec: _containers.RepeatedScalarFieldContainer[int]
        update_intent: TableValue.ClientIdMapping.UpdateIntent
        cs_reply_cache_vec: _containers.RepeatedCompositeFieldContainer[TableValue.ClientIdMapping.CreateSessionReplyCache]
        def __init__(self, client_owner_id: _Optional[bytes] = ..., verifier: _Optional[int] = ..., server_ip: _Optional[str] = ..., expiration_usecs: _Optional[int] = ..., session_id_vec: _Optional[_Iterable[int]] = ..., state_id_vec: _Optional[_Iterable[int]] = ..., update_intent: _Optional[_Union[TableValue.ClientIdMapping.UpdateIntent, _Mapping]] = ..., cs_reply_cache_vec: _Optional[_Iterable[_Union[TableValue.ClientIdMapping.CreateSessionReplyCache, _Mapping]]] = ...) -> None: ...
    class SessionIdMapping(_message.Message):
        __slots__ = ("client_id", "flags")
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        client_id: int
        flags: int
        def __init__(self, client_id: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...
    class StateIdMapping(_message.Message):
        __slots__ = ("client_id", "session_id", "entity_handle", "seq", "open_details", "lock_details")
        class OpenDetails(_message.Message):
            __slots__ = ("open_id", "access", "share_access", "share_deny", "lock_state_ids")
            OPEN_ID_FIELD_NUMBER: _ClassVar[int]
            ACCESS_FIELD_NUMBER: _ClassVar[int]
            SHARE_ACCESS_FIELD_NUMBER: _ClassVar[int]
            SHARE_DENY_FIELD_NUMBER: _ClassVar[int]
            LOCK_STATE_IDS_FIELD_NUMBER: _ClassVar[int]
            open_id: int
            access: int
            share_access: int
            share_deny: int
            lock_state_ids: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, open_id: _Optional[int] = ..., access: _Optional[int] = ..., share_access: _Optional[int] = ..., share_deny: _Optional[int] = ..., lock_state_ids: _Optional[_Iterable[int]] = ...) -> None: ...
        class LockDetails(_message.Message):
            __slots__ = ("open_state_id", "open_id")
            OPEN_STATE_ID_FIELD_NUMBER: _ClassVar[int]
            OPEN_ID_FIELD_NUMBER: _ClassVar[int]
            open_state_id: int
            open_id: int
            def __init__(self, open_state_id: _Optional[int] = ..., open_id: _Optional[int] = ...) -> None: ...
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
        SEQ_FIELD_NUMBER: _ClassVar[int]
        OPEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
        LOCK_DETAILS_FIELD_NUMBER: _ClassVar[int]
        client_id: int
        session_id: int
        entity_handle: _entity_handle_pb2.EntityHandleProto
        seq: int
        open_details: TableValue.StateIdMapping.OpenDetails
        lock_details: TableValue.StateIdMapping.LockDetails
        def __init__(self, client_id: _Optional[int] = ..., session_id: _Optional[int] = ..., entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., seq: _Optional[int] = ..., open_details: _Optional[_Union[TableValue.StateIdMapping.OpenDetails, _Mapping]] = ..., lock_details: _Optional[_Union[TableValue.StateIdMapping.LockDetails, _Mapping]] = ...) -> None: ...
    CLIENT_OWNER_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SERVER_IP_MAPPING_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    client_owner_id_mapping: _containers.ScalarMap[int, int]
    server_ip_mapping: _containers.ScalarMap[int, str]
    client_id_mapping: TableValue.ClientIdMapping
    session_id_mapping: TableValue.SessionIdMapping
    state_id_mapping: TableValue.StateIdMapping
    def __init__(self, client_owner_id_mapping: _Optional[_Mapping[int, int]] = ..., server_ip_mapping: _Optional[_Mapping[int, str]] = ..., client_id_mapping: _Optional[_Union[TableValue.ClientIdMapping, _Mapping]] = ..., session_id_mapping: _Optional[_Union[TableValue.SessionIdMapping, _Mapping]] = ..., state_id_mapping: _Optional[_Union[TableValue.StateIdMapping, _Mapping]] = ...) -> None: ...
