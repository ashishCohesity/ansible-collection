from gandalf.base import common_pb2 as _common_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionInfo(_message.Message):
    __slots__ = ("session_id", "master_incarnation_id", "tenant_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    master_incarnation_id: int
    tenant_id: str
    def __init__(self, session_id: _Optional[int] = ..., master_incarnation_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class ClientNotification(_message.Message):
    __slots__ = ("notification_id", "lock_acquired_notifications", "lock_watch_notifications", "lock_yield_notifications", "ns_watch_notifications", "key_watch_notification")
    class LockAcquiredNotification(_message.Message):
        __slots__ = ("lock_name", "request_id", "sequencer")
        LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        lock_name: str
        request_id: int
        sequencer: int
        def __init__(self, lock_name: _Optional[str] = ..., request_id: _Optional[int] = ..., sequencer: _Optional[int] = ...) -> None: ...
    class LockWatchNotification(_message.Message):
        __slots__ = ("lock_name", "request_id", "constituent_id", "session_id", "sequencer", "data", "is_exclusive", "is_acquired")
        LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        IS_ACQUIRED_FIELD_NUMBER: _ClassVar[int]
        lock_name: str
        request_id: int
        constituent_id: int
        session_id: int
        sequencer: int
        data: bytes
        is_exclusive: bool
        is_acquired: bool
        def __init__(self, lock_name: _Optional[str] = ..., request_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., sequencer: _Optional[int] = ..., data: _Optional[bytes] = ..., is_exclusive: bool = ..., is_acquired: bool = ...) -> None: ...
    class LockYieldNotification(_message.Message):
        __slots__ = ("lock_name", "request_id")
        LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        lock_name: str
        request_id: int
        def __init__(self, lock_name: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...
    class NamespaceWatchNotification(_message.Message):
        __slots__ = ("ns", "constituent_id", "session_id", "is_alive", "data", "request_id")
        NS_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        ns: str
        constituent_id: int
        session_id: int
        is_alive: bool
        data: bytes
        request_id: int
        def __init__(self, ns: _Optional[str] = ..., constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., is_alive: bool = ..., data: _Optional[bytes] = ..., request_id: _Optional[int] = ...) -> None: ...
    class KeyWatchNotification(_message.Message):
        __slots__ = ("key", "version", "value", "request_id")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        key: str
        version: int
        value: bytes
        request_id: int
        def __init__(self, key: _Optional[str] = ..., version: _Optional[int] = ..., value: _Optional[bytes] = ..., request_id: _Optional[int] = ...) -> None: ...
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCK_ACQUIRED_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCK_WATCH_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    LOCK_YIELD_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    NS_WATCH_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    KEY_WATCH_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification_id: int
    lock_acquired_notifications: ClientNotification.LockAcquiredNotification
    lock_watch_notifications: ClientNotification.LockWatchNotification
    lock_yield_notifications: ClientNotification.LockYieldNotification
    ns_watch_notifications: ClientNotification.NamespaceWatchNotification
    key_watch_notification: ClientNotification.KeyWatchNotification
    def __init__(self, notification_id: _Optional[int] = ..., lock_acquired_notifications: _Optional[_Union[ClientNotification.LockAcquiredNotification, _Mapping]] = ..., lock_watch_notifications: _Optional[_Union[ClientNotification.LockWatchNotification, _Mapping]] = ..., lock_yield_notifications: _Optional[_Union[ClientNotification.LockYieldNotification, _Mapping]] = ..., ns_watch_notifications: _Optional[_Union[ClientNotification.NamespaceWatchNotification, _Mapping]] = ..., key_watch_notification: _Optional[_Union[ClientNotification.KeyWatchNotification, _Mapping]] = ...) -> None: ...

class GetMasterArg(_message.Message):
    __slots__ = ("previous_incarnation_id",)
    PREVIOUS_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    previous_incarnation_id: int
    def __init__(self, previous_incarnation_id: _Optional[int] = ...) -> None: ...

class GetMasterResult(_message.Message):
    __slots__ = ("incarnation_id", "ip_address", "port")
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    incarnation_id: int
    ip_address: str
    port: int
    def __init__(self, incarnation_id: _Optional[int] = ..., ip_address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ReserveSessionIdArg(_message.Message):
    __slots__ = ("master_incarnation_id",)
    MASTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    master_incarnation_id: int
    def __init__(self, master_incarnation_id: _Optional[int] = ...) -> None: ...

class ReserveSessionIdResult(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class EstablishSessionArg(_message.Message):
    __slots__ = ("master_incarnation_id", "client_name", "client_healthz_port", "client_session_timeout_msecs", "session_id", "tenant_id")
    MASTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_HEALTHZ_PORT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SESSION_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    master_incarnation_id: int
    client_name: str
    client_healthz_port: int
    client_session_timeout_msecs: int
    session_id: int
    tenant_id: str
    def __init__(self, master_incarnation_id: _Optional[int] = ..., client_name: _Optional[str] = ..., client_healthz_port: _Optional[int] = ..., client_session_timeout_msecs: _Optional[int] = ..., session_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class EstablishSessionResult(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class FindHealthySessionsArg(_message.Message):
    __slots__ = ("session_info", "sessions")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    sessions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., sessions: _Optional[_Iterable[int]] = ...) -> None: ...

class FindHealthySessionsResult(_message.Message):
    __slots__ = ("healthy_sessions",)
    HEALTHY_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    healthy_sessions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, healthy_sessions: _Optional[_Iterable[int]] = ...) -> None: ...

class CloseSessionArg(_message.Message):
    __slots__ = ("session_info", "session_id_to_expire")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_TO_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    session_id_to_expire: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., session_id_to_expire: _Optional[int] = ...) -> None: ...

class CloseSessionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterSessionArg(_message.Message):
    __slots__ = ("session_id", "exec_name")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_NAME_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    exec_name: bytes
    def __init__(self, session_id: _Optional[int] = ..., exec_name: _Optional[bytes] = ...) -> None: ...

class RegisterSessionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeepAliveArg(_message.Message):
    __slots__ = ("session_info", "highest_processed_notification_id", "max_keepalive_hold_time_ms")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_PROCESSED_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_KEEPALIVE_HOLD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    highest_processed_notification_id: int
    max_keepalive_hold_time_ms: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., highest_processed_notification_id: _Optional[int] = ..., max_keepalive_hold_time_ms: _Optional[int] = ...) -> None: ...

class KeepAliveResult(_message.Message):
    __slots__ = ("client_notifications",)
    CLIENT_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    client_notifications: _containers.RepeatedCompositeFieldContainer[ClientNotification]
    def __init__(self, client_notifications: _Optional[_Iterable[_Union[ClientNotification, _Mapping]]] = ...) -> None: ...

class UpdateKeyArg(_message.Message):
    __slots__ = ("session_info", "key", "expected_version", "data")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    expected_version: int
    data: bytes
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ..., expected_version: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UpdateKeyResult(_message.Message):
    __slots__ = ("value_at_server",)
    VALUE_AT_SERVER_FIELD_NUMBER: _ClassVar[int]
    value_at_server: bytes
    def __init__(self, value_at_server: _Optional[bytes] = ...) -> None: ...

class LookupKeyArg(_message.Message):
    __slots__ = ("session_info", "key")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class LookupKeyResult(_message.Message):
    __slots__ = ("data", "current_version")
    DATA_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    current_version: int
    def __init__(self, data: _Optional[bytes] = ..., current_version: _Optional[int] = ...) -> None: ...

class DeleteKeyArg(_message.Message):
    __slots__ = ("session_info", "key", "expected_version")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    expected_version: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ..., expected_version: _Optional[int] = ...) -> None: ...

class DeleteKeyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchKeyArg(_message.Message):
    __slots__ = ("session_info", "key", "request_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    request_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...

class WatchKeyResult(_message.Message):
    __slots__ = ("current_version", "data")
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    current_version: int
    data: bytes
    def __init__(self, current_version: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class CancelWatchKeyArg(_message.Message):
    __slots__ = ("session_info", "key", "request_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    request_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...

class CancelWatchKeyResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AtomicIncrementArg(_message.Message):
    __slots__ = ("session_info", "key", "incr")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    INCR_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    incr: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ..., incr: _Optional[int] = ...) -> None: ...

class AtomicIncrementResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class SetGreaterThanOrEqualToArg(_message.Message):
    __slots__ = ("floor",)
    FLOOR_FIELD_NUMBER: _ClassVar[int]
    floor: int
    def __init__(self, floor: _Optional[int] = ...) -> None: ...

class SetGreaterThanOrEqualToResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class TransformKeyArg(_message.Message):
    __slots__ = ("session_info", "key", "operation_type", "set_greater_than_or_equal_to_arg")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SET_GREATER_THAN_OR_EQUAL_TO_ARG_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    key: str
    operation_type: _common_pb2.TransformKeyOperation.Type
    set_greater_than_or_equal_to_arg: SetGreaterThanOrEqualToArg
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., key: _Optional[str] = ..., operation_type: _Optional[_Union[_common_pb2.TransformKeyOperation.Type, str]] = ..., set_greater_than_or_equal_to_arg: _Optional[_Union[SetGreaterThanOrEqualToArg, _Mapping]] = ...) -> None: ...

class TransformKeyResult(_message.Message):
    __slots__ = ("set_greater_than_or_equal_to_res",)
    SET_GREATER_THAN_OR_EQUAL_TO_RES_FIELD_NUMBER: _ClassVar[int]
    set_greater_than_or_equal_to_res: SetGreaterThanOrEqualToResult
    def __init__(self, set_greater_than_or_equal_to_res: _Optional[_Union[SetGreaterThanOrEqualToResult, _Mapping]] = ...) -> None: ...

class RegisterLivenessArg(_message.Message):
    __slots__ = ("session_info", "name_space", "constituent_id", "data", "is_reregister", "persist_constituent_stats")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_REREGISTER_FIELD_NUMBER: _ClassVar[int]
    PERSIST_CONSTITUENT_STATS_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    name_space: str
    constituent_id: int
    data: bytes
    is_reregister: bool
    persist_constituent_stats: bool
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., name_space: _Optional[str] = ..., constituent_id: _Optional[int] = ..., data: _Optional[bytes] = ..., is_reregister: bool = ..., persist_constituent_stats: bool = ...) -> None: ...

class RegisterLivenessResult(_message.Message):
    __slots__ = ("prior_registration_session_id",)
    PRIOR_REGISTRATION_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    prior_registration_session_id: int
    def __init__(self, prior_registration_session_id: _Optional[int] = ...) -> None: ...

class WatchLivenessArg(_message.Message):
    __slots__ = ("session_info", "name_space", "request_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    name_space: str
    request_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., name_space: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...

class WatchLivenessResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelWatchLivenessArg(_message.Message):
    __slots__ = ("session_info", "name_space", "request_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    name_space: str
    request_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., name_space: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...

class CancelWatchLivenessResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchLiveArg(_message.Message):
    __slots__ = ("session_info", "name_space", "cookie")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    name_space: str
    cookie: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., name_space: _Optional[str] = ..., cookie: _Optional[int] = ...) -> None: ...

class FetchLiveResult(_message.Message):
    __slots__ = ("next_cookie", "constituents")
    class ConstituentInfo(_message.Message):
        __slots__ = ("constituent_id", "session_id", "data")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        session_id: int
        data: bytes
        def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    next_cookie: int
    constituents: _containers.RepeatedCompositeFieldContainer[FetchLiveResult.ConstituentInfo]
    def __init__(self, next_cookie: _Optional[int] = ..., constituents: _Optional[_Iterable[_Union[FetchLiveResult.ConstituentInfo, _Mapping]]] = ...) -> None: ...

class LookupConstituentHealthArg(_message.Message):
    __slots__ = ("session_info", "name_space", "constituent_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    name_space: str
    constituent_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., name_space: _Optional[str] = ..., constituent_id: _Optional[int] = ...) -> None: ...

class LookupConstituentHealthResult(_message.Message):
    __slots__ = ("is_alive", "session_id", "data")
    IS_ALIVE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    is_alive: bool
    session_id: int
    data: bytes
    def __init__(self, is_alive: bool = ..., session_id: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class LookupConstituentStatsArg(_message.Message):
    __slots__ = ("session_info", "name_space", "constituent_ids")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_IDS_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    name_space: str
    constituent_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., name_space: _Optional[str] = ..., constituent_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class LookupConstituentStatsResult(_message.Message):
    __slots__ = ("constituent_stats",)
    CONSTITUENT_STATS_FIELD_NUMBER: _ClassVar[int]
    constituent_stats: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConstituentStatsProto]
    def __init__(self, constituent_stats: _Optional[_Iterable[_Union[_common_pb2.ConstituentStatsProto, _Mapping]]] = ...) -> None: ...

class AcquireLockArg(_message.Message):
    __slots__ = ("session_info", "constituent_id", "is_exclusive", "lock_name", "force", "request_id", "data", "persistent", "node_id", "avoid_holder_of_lock", "can_crash", "priority_type")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    AVOID_HOLDER_OF_LOCK_FIELD_NUMBER: _ClassVar[int]
    CAN_CRASH_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    constituent_id: int
    is_exclusive: bool
    lock_name: str
    force: bool
    request_id: int
    data: bytes
    persistent: bool
    node_id: int
    avoid_holder_of_lock: str
    can_crash: bool
    priority_type: _common_pb2.LockPriority.PriorityType
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., constituent_id: _Optional[int] = ..., is_exclusive: bool = ..., lock_name: _Optional[str] = ..., force: bool = ..., request_id: _Optional[int] = ..., data: _Optional[bytes] = ..., persistent: bool = ..., node_id: _Optional[int] = ..., avoid_holder_of_lock: _Optional[str] = ..., can_crash: bool = ..., priority_type: _Optional[_Union[_common_pb2.LockPriority.PriorityType, str]] = ...) -> None: ...

class AcquireLockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReleaseLockArg(_message.Message):
    __slots__ = ("session_info", "lock_name", "request_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    lock_name: str
    request_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., lock_name: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...

class ReleaseLockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchLockHoldersArg(_message.Message):
    __slots__ = ("session_info", "lock_name")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    lock_name: str
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., lock_name: _Optional[str] = ...) -> None: ...

class FetchLockHoldersResult(_message.Message):
    __slots__ = ("lock_holders", "is_exclusive")
    class LockHolder(_message.Message):
        __slots__ = ("constituent_id", "session_id", "sequencer", "data")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        session_id: int
        sequencer: int
        data: bytes
        def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., sequencer: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    LOCK_HOLDERS_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    lock_holders: _containers.RepeatedCompositeFieldContainer[FetchLockHoldersResult.LockHolder]
    is_exclusive: bool
    def __init__(self, lock_holders: _Optional[_Iterable[_Union[FetchLockHoldersResult.LockHolder, _Mapping]]] = ..., is_exclusive: bool = ...) -> None: ...

class WatchLockArg(_message.Message):
    __slots__ = ("session_info", "request_id", "lock_name")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    request_id: int
    lock_name: str
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., request_id: _Optional[int] = ..., lock_name: _Optional[str] = ...) -> None: ...

class WatchLockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelWatchLockArg(_message.Message):
    __slots__ = ("session_info", "request_id", "lock_name")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    request_id: int
    lock_name: str
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., request_id: _Optional[int] = ..., lock_name: _Optional[str] = ...) -> None: ...

class CancelWatchLockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordOpClockArg(_message.Message):
    __slots__ = ("session_info", "op_clock")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    op_clock: _op_clock_pb2.OpClock
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ...) -> None: ...

class RecordOpClockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveOpClockArg(_message.Message):
    __slots__ = ("session_info", "constituent_id")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    constituent_id: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., constituent_id: _Optional[int] = ...) -> None: ...

class RemoveOpClockResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchOpClocksArg(_message.Message):
    __slots__ = ("session_info", "cookie")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    cookie: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., cookie: _Optional[int] = ...) -> None: ...

class FetchOpClocksResult(_message.Message):
    __slots__ = ("next_cookie", "op_clocks")
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCKS_FIELD_NUMBER: _ClassVar[int]
    next_cookie: int
    op_clocks: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, next_cookie: _Optional[int] = ..., op_clocks: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class FetchCachedOpClocksArg(_message.Message):
    __slots__ = ("session_info", "cookie", "duration_secs")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    session_info: SessionInfo
    cookie: int
    duration_secs: int
    def __init__(self, session_info: _Optional[_Union[SessionInfo, _Mapping]] = ..., cookie: _Optional[int] = ..., duration_secs: _Optional[int] = ...) -> None: ...

class FetchCachedOpClocksResult(_message.Message):
    __slots__ = ("next_cookie", "op_clocks")
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCKS_FIELD_NUMBER: _ClassVar[int]
    next_cookie: int
    op_clocks: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, next_cookie: _Optional[int] = ..., op_clocks: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class UrisProto(_message.Message):
    __slots__ = ("base_uri", "lookup_master_uri", "lock_details_uri")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_MASTER_URI_FIELD_NUMBER: _ClassVar[int]
    LOCK_DETAILS_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    lookup_master_uri: str
    lock_details_uri: str
    def __init__(self, base_uri: _Optional[str] = ..., lookup_master_uri: _Optional[str] = ..., lock_details_uri: _Optional[str] = ...) -> None: ...

class GandalfMasterInfo(_message.Message):
    __slots__ = ("ip_address", "port")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    port: int
    def __init__(self, ip_address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class GandalfLockInfoReq(_message.Message):
    __slots__ = ("lock_names",)
    LOCK_NAMES_FIELD_NUMBER: _ClassVar[int]
    lock_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lock_names: _Optional[_Iterable[str]] = ...) -> None: ...

class GandalfLockInfoResp(_message.Message):
    __slots__ = ("lock_info_vec",)
    class LockInfo(_message.Message):
        __slots__ = ("lock_name", "lock_holders")
        class LockHolderInfo(_message.Message):
            __slots__ = ("client_name", "client_ip_address")
            CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
            CLIENT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            client_name: str
            client_ip_address: str
            def __init__(self, client_name: _Optional[str] = ..., client_ip_address: _Optional[str] = ...) -> None: ...
        LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCK_HOLDERS_FIELD_NUMBER: _ClassVar[int]
        lock_name: str
        lock_holders: _containers.RepeatedCompositeFieldContainer[GandalfLockInfoResp.LockInfo.LockHolderInfo]
        def __init__(self, lock_name: _Optional[str] = ..., lock_holders: _Optional[_Iterable[_Union[GandalfLockInfoResp.LockInfo.LockHolderInfo, _Mapping]]] = ...) -> None: ...
    LOCK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    lock_info_vec: _containers.RepeatedCompositeFieldContainer[GandalfLockInfoResp.LockInfo]
    def __init__(self, lock_info_vec: _Optional[_Iterable[_Union[GandalfLockInfoResp.LockInfo, _Mapping]]] = ...) -> None: ...
