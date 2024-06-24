from util.base import universal_id_pb2 as _universal_id_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cookie(_message.Message):
    __slots__ = ("object_uid", "runs_pagination_cookie")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    RUNS_PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    runs_pagination_cookie: bytes
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., runs_pagination_cookie: _Optional[bytes] = ...) -> None: ...

class ReconciliationState(_message.Message):
    __slots__ = ()
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[ReconciliationState.State]
        kGetMissingSnapshots: _ClassVar[ReconciliationState.State]
        kApplyMissingSnapshots: _ClassVar[ReconciliationState.State]
        kFinished: _ClassVar[ReconciliationState.State]
    kInvalid: ReconciliationState.State
    kGetMissingSnapshots: ReconciliationState.State
    kApplyMissingSnapshots: ReconciliationState.State
    kFinished: ReconciliationState.State
    def __init__(self) -> None: ...

class PersistentStateProto(_message.Message):
    __slots__ = ("state", "source_pagination_cookie", "last_snapshot_notified", "next_snapshot_to_notify", "error", "missing_snapshots_record_counter_id", "total_missing_snapshots")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    LAST_SNAPSHOT_NOTIFIED_FIELD_NUMBER: _ClassVar[int]
    NEXT_SNAPSHOT_TO_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MISSING_SNAPSHOTS_RECORD_COUNTER_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MISSING_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    state: ReconciliationState.State
    source_pagination_cookie: bytes
    last_snapshot_notified: bytes
    next_snapshot_to_notify: bytes
    error: _error_pb2.ErrorProto
    missing_snapshots_record_counter_id: int
    total_missing_snapshots: int
    def __init__(self, state: _Optional[_Union[ReconciliationState.State, str]] = ..., source_pagination_cookie: _Optional[bytes] = ..., last_snapshot_notified: _Optional[bytes] = ..., next_snapshot_to_notify: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., missing_snapshots_record_counter_id: _Optional[int] = ..., total_missing_snapshots: _Optional[int] = ...) -> None: ...

class MissingSnapshotsProto(_message.Message):
    __slots__ = ("tenant_id", "migration_uuid", "missing_snapshots")
    class SnapshotProto(_message.Message):
        __slots__ = ("job_uid", "run_start_time_usecs", "entity")
        JOB_UID_FIELD_NUMBER: _ClassVar[int]
        RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        ENTITY_FIELD_NUMBER: _ClassVar[int]
        job_uid: _universal_id_pb2.UniversalIdProto
        run_start_time_usecs: int
        entity: _entity_pb2.EntityProto
        def __init__(self, job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., run_start_time_usecs: _Optional[int] = ..., entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UUID_FIELD_NUMBER: _ClassVar[int]
    MISSING_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    migration_uuid: str
    missing_snapshots: _containers.RepeatedCompositeFieldContainer[MissingSnapshotsProto.SnapshotProto]
    def __init__(self, tenant_id: _Optional[str] = ..., migration_uuid: _Optional[str] = ..., missing_snapshots: _Optional[_Iterable[_Union[MissingSnapshotsProto.SnapshotProto, _Mapping]]] = ...) -> None: ...
