from gandalf.base import common_pb2 as _common_pb2
from gandalf.server.stub import gandalf_pb2 as _gandalf_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DbValue(_message.Message):
    __slots__ = ("session_record", "lock_record", "key_record", "name_space_record", "op_clock_record", "active_notification_record", "session_id_generator", "incarnation_id_generator", "newlock_sequencer_generator", "active_notification_record_id_generator", "data_format_record", "constituent_stats_record", "op_clock_bucket_cache_record")
    SESSION_RECORD_FIELD_NUMBER: _ClassVar[int]
    LOCK_RECORD_FIELD_NUMBER: _ClassVar[int]
    KEY_RECORD_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_RECORD_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_RECORD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_NOTIFICATION_RECORD_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    NEWLOCK_SEQUENCER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_NOTIFICATION_RECORD_ID_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_RECORD_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_STATS_RECORD_FIELD_NUMBER: _ClassVar[int]
    OP_CLOCK_BUCKET_CACHE_RECORD_FIELD_NUMBER: _ClassVar[int]
    session_record: SessionRecord
    lock_record: LockRecord
    key_record: KeyRecord
    name_space_record: NamespaceRecord
    op_clock_record: OpClockRecord
    active_notification_record: ActiveNotificationRecord
    session_id_generator: int
    incarnation_id_generator: int
    newlock_sequencer_generator: int
    active_notification_record_id_generator: int
    data_format_record: DataFormatRecord
    constituent_stats_record: _common_pb2.ConstituentStatsProto
    op_clock_bucket_cache_record: _op_clock_pb2.OpClockVectorCacheBucket
    def __init__(self, session_record: _Optional[_Union[SessionRecord, _Mapping]] = ..., lock_record: _Optional[_Union[LockRecord, _Mapping]] = ..., key_record: _Optional[_Union[KeyRecord, _Mapping]] = ..., name_space_record: _Optional[_Union[NamespaceRecord, _Mapping]] = ..., op_clock_record: _Optional[_Union[OpClockRecord, _Mapping]] = ..., active_notification_record: _Optional[_Union[ActiveNotificationRecord, _Mapping]] = ..., session_id_generator: _Optional[int] = ..., incarnation_id_generator: _Optional[int] = ..., newlock_sequencer_generator: _Optional[int] = ..., active_notification_record_id_generator: _Optional[int] = ..., data_format_record: _Optional[_Union[DataFormatRecord, _Mapping]] = ..., constituent_stats_record: _Optional[_Union[_common_pb2.ConstituentStatsProto, _Mapping]] = ..., op_clock_bucket_cache_record: _Optional[_Union[_op_clock_pb2.OpClockVectorCacheBucket, _Mapping]] = ...) -> None: ...

class SessionRecord(_message.Message):
    __slots__ = ("session_id", "expiration_time_msec", "highest_notification_id", "highest_notification_id_sent_to_client", "legacy_unacked_notifications_DEPRECATED", "unacked_queued_notification_vec", "resources", "client_name", "client_ip_address", "client_healthz_port", "creation_time_msecs", "client_session_timeout_msecs", "tenant_id")
    class QueuedNotification(_message.Message):
        __slots__ = ("active_notification_record_id", "session_local_id", "request_id")
        ACTIVE_NOTIFICATION_RECORD_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        active_notification_record_id: int
        session_local_id: int
        request_id: int
        def __init__(self, active_notification_record_id: _Optional[int] = ..., session_local_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...
    class RegisteredRequest(_message.Message):
        __slots__ = ("type", "entity_name", "request_id")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kKeyWatch: _ClassVar[SessionRecord.RegisteredRequest.Type]
            kLockWatch: _ClassVar[SessionRecord.RegisteredRequest.Type]
            kLockRequest: _ClassVar[SessionRecord.RegisteredRequest.Type]
            kLivenessWatch: _ClassVar[SessionRecord.RegisteredRequest.Type]
            kLivenessRegistration: _ClassVar[SessionRecord.RegisteredRequest.Type]
        kKeyWatch: SessionRecord.RegisteredRequest.Type
        kLockWatch: SessionRecord.RegisteredRequest.Type
        kLockRequest: SessionRecord.RegisteredRequest.Type
        kLivenessWatch: SessionRecord.RegisteredRequest.Type
        kLivenessRegistration: SessionRecord.RegisteredRequest.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        type: SessionRecord.RegisteredRequest.Type
        entity_name: str
        request_id: int
        def __init__(self, type: _Optional[_Union[SessionRecord.RegisteredRequest.Type, str]] = ..., entity_name: _Optional[str] = ..., request_id: _Optional[int] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_MSEC_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_NOTIFICATION_ID_SENT_TO_CLIENT_FIELD_NUMBER: _ClassVar[int]
    LEGACY_UNACKED_NOTIFICATIONS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    UNACKED_QUEUED_NOTIFICATION_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_HEALTHZ_PORT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SESSION_TIMEOUT_MSECS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    expiration_time_msec: int
    highest_notification_id: int
    highest_notification_id_sent_to_client: int
    legacy_unacked_notifications_DEPRECATED: _containers.RepeatedCompositeFieldContainer[_gandalf_pb2.ClientNotification]
    unacked_queued_notification_vec: _containers.RepeatedCompositeFieldContainer[SessionRecord.QueuedNotification]
    resources: _containers.RepeatedCompositeFieldContainer[SessionRecord.RegisteredRequest]
    client_name: str
    client_ip_address: str
    client_healthz_port: int
    creation_time_msecs: int
    client_session_timeout_msecs: int
    tenant_id: str
    def __init__(self, session_id: _Optional[int] = ..., expiration_time_msec: _Optional[int] = ..., highest_notification_id: _Optional[int] = ..., highest_notification_id_sent_to_client: _Optional[int] = ..., legacy_unacked_notifications_DEPRECATED: _Optional[_Iterable[_Union[_gandalf_pb2.ClientNotification, _Mapping]]] = ..., unacked_queued_notification_vec: _Optional[_Iterable[_Union[SessionRecord.QueuedNotification, _Mapping]]] = ..., resources: _Optional[_Iterable[_Union[SessionRecord.RegisteredRequest, _Mapping]]] = ..., client_name: _Optional[str] = ..., client_ip_address: _Optional[str] = ..., client_healthz_port: _Optional[int] = ..., creation_time_msecs: _Optional[int] = ..., client_session_timeout_msecs: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class LockRecord(_message.Message):
    __slots__ = ("lock_name", "sequencer", "requesters", "watchers", "persistent")
    class LockRequester(_message.Message):
        __slots__ = ("session_id", "request_id", "constituent_id", "is_exclusive", "is_force", "data", "is_held", "persistent", "node_id", "can_crash", "priority_type", "avoid_holder_of_lock")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        IS_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        IS_FORCE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        IS_HELD_FIELD_NUMBER: _ClassVar[int]
        PERSISTENT_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        CAN_CRASH_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        AVOID_HOLDER_OF_LOCK_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        request_id: int
        constituent_id: int
        is_exclusive: bool
        is_force: bool
        data: bytes
        is_held: bool
        persistent: bool
        node_id: int
        can_crash: bool
        priority_type: _common_pb2.LockPriority.PriorityType
        avoid_holder_of_lock: str
        def __init__(self, session_id: _Optional[int] = ..., request_id: _Optional[int] = ..., constituent_id: _Optional[int] = ..., is_exclusive: bool = ..., is_force: bool = ..., data: _Optional[bytes] = ..., is_held: bool = ..., persistent: bool = ..., node_id: _Optional[int] = ..., can_crash: bool = ..., priority_type: _Optional[_Union[_common_pb2.LockPriority.PriorityType, str]] = ..., avoid_holder_of_lock: _Optional[str] = ...) -> None: ...
    class Watcher(_message.Message):
        __slots__ = ("session_id", "request_id")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        request_id: int
        def __init__(self, session_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...
    LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    REQUESTERS_FIELD_NUMBER: _ClassVar[int]
    WATCHERS_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    lock_name: str
    sequencer: int
    requesters: _containers.RepeatedCompositeFieldContainer[LockRecord.LockRequester]
    watchers: _containers.RepeatedCompositeFieldContainer[LockRecord.Watcher]
    persistent: bool
    def __init__(self, lock_name: _Optional[str] = ..., sequencer: _Optional[int] = ..., requesters: _Optional[_Iterable[_Union[LockRecord.LockRequester, _Mapping]]] = ..., watchers: _Optional[_Iterable[_Union[LockRecord.Watcher, _Mapping]]] = ..., persistent: bool = ...) -> None: ...

class KeyRecord(_message.Message):
    __slots__ = ("key", "version", "value", "watchers")
    class KeyWatcher(_message.Message):
        __slots__ = ("session_id", "request_id")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        request_id: int
        def __init__(self, session_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    WATCHERS_FIELD_NUMBER: _ClassVar[int]
    key: str
    version: int
    value: bytes
    watchers: _containers.RepeatedCompositeFieldContainer[KeyRecord.KeyWatcher]
    def __init__(self, key: _Optional[str] = ..., version: _Optional[int] = ..., value: _Optional[bytes] = ..., watchers: _Optional[_Iterable[_Union[KeyRecord.KeyWatcher, _Mapping]]] = ...) -> None: ...

class NamespaceRecord(_message.Message):
    __slots__ = ("name_space", "registered_constituents", "watchers", "num_recently_seen_unique_constituents")
    class Constituent(_message.Message):
        __slots__ = ("constituent_id", "session_id", "data", "prior_registration_session_id", "persist_constituent_stats")
        CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        PRIOR_REGISTRATION_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        PERSIST_CONSTITUENT_STATS_FIELD_NUMBER: _ClassVar[int]
        constituent_id: int
        session_id: int
        data: bytes
        prior_registration_session_id: int
        persist_constituent_stats: bool
        def __init__(self, constituent_id: _Optional[int] = ..., session_id: _Optional[int] = ..., data: _Optional[bytes] = ..., prior_registration_session_id: _Optional[int] = ..., persist_constituent_stats: bool = ...) -> None: ...
    class NamespaceWatcher(_message.Message):
        __slots__ = ("session_id", "request_id")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: int
        request_id: int
        def __init__(self, session_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    WATCHERS_FIELD_NUMBER: _ClassVar[int]
    NUM_RECENTLY_SEEN_UNIQUE_CONSTITUENTS_FIELD_NUMBER: _ClassVar[int]
    name_space: str
    registered_constituents: _containers.RepeatedCompositeFieldContainer[NamespaceRecord.Constituent]
    watchers: _containers.RepeatedCompositeFieldContainer[NamespaceRecord.NamespaceWatcher]
    num_recently_seen_unique_constituents: int
    def __init__(self, name_space: _Optional[str] = ..., registered_constituents: _Optional[_Iterable[_Union[NamespaceRecord.Constituent, _Mapping]]] = ..., watchers: _Optional[_Iterable[_Union[NamespaceRecord.NamespaceWatcher, _Mapping]]] = ..., num_recently_seen_unique_constituents: _Optional[int] = ...) -> None: ...

class OpClockRecord(_message.Message):
    __slots__ = ("op_clocks",)
    OP_CLOCKS_FIELD_NUMBER: _ClassVar[int]
    op_clocks: _containers.RepeatedCompositeFieldContainer[_op_clock_pb2.OpClock]
    def __init__(self, op_clocks: _Optional[_Iterable[_Union[_op_clock_pb2.OpClock, _Mapping]]] = ...) -> None: ...

class ActiveNotificationRecord(_message.Message):
    __slots__ = ("id", "client_notification", "ref_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    REF_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    client_notification: _gandalf_pb2.ClientNotification
    ref_count: int
    def __init__(self, id: _Optional[int] = ..., client_notification: _Optional[_Union[_gandalf_pb2.ClientNotification, _Mapping]] = ..., ref_count: _Optional[int] = ...) -> None: ...

class DataFormatRecord(_message.Message):
    __slots__ = ("use_refcounted_notifications", "enable_opclock_caching")
    USE_REFCOUNTED_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OPCLOCK_CACHING_FIELD_NUMBER: _ClassVar[int]
    use_refcounted_notifications: bool
    enable_opclock_caching: bool
    def __init__(self, use_refcounted_notifications: bool = ..., enable_opclock_caching: bool = ...) -> None: ...

class GandalfWALRecord(_message.Message):
    __slots__ = ("updated_keys", "updated_values", "deleted_keys")
    UPDATED_KEYS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_VALUES_FIELD_NUMBER: _ClassVar[int]
    DELETED_KEYS_FIELD_NUMBER: _ClassVar[int]
    updated_keys: _containers.RepeatedScalarFieldContainer[str]
    updated_values: _containers.RepeatedCompositeFieldContainer[DbValue]
    deleted_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, updated_keys: _Optional[_Iterable[str]] = ..., updated_values: _Optional[_Iterable[_Union[DbValue, _Mapping]]] = ..., deleted_keys: _Optional[_Iterable[str]] = ...) -> None: ...
