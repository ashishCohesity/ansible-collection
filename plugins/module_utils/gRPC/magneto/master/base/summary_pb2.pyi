from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupJobRuns(_message.Message):
    __slots__ = ("total_runs", "sla_violations", "errors", "running", "policy_vec", "cancelled_runs", "successful_runs")
    class ObjectDetails(_message.Message):
        __slots__ = ("protected_size", "object_count")
        PROTECTED_SIZE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        protected_size: int
        object_count: int
        def __init__(self, protected_size: _Optional[int] = ..., object_count: _Optional[int] = ...) -> None: ...
    class Policy(_message.Message):
        __slots__ = ("id", "name", "details_map")
        class DetailsMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: BackupJobRuns.ObjectDetails
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BackupJobRuns.ObjectDetails, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DETAILS_MAP_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        details_map: _containers.MessageMap[int, BackupJobRuns.ObjectDetails]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., details_map: _Optional[_Mapping[int, BackupJobRuns.ObjectDetails]] = ...) -> None: ...
    TOTAL_RUNS_FIELD_NUMBER: _ClassVar[int]
    SLA_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_RUNS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_RUNS_FIELD_NUMBER: _ClassVar[int]
    total_runs: int
    sla_violations: int
    errors: int
    running: int
    policy_vec: _containers.RepeatedCompositeFieldContainer[BackupJobRuns.Policy]
    cancelled_runs: int
    successful_runs: int
    def __init__(self, total_runs: _Optional[int] = ..., sla_violations: _Optional[int] = ..., errors: _Optional[int] = ..., running: _Optional[int] = ..., policy_vec: _Optional[_Iterable[_Union[BackupJobRuns.Policy, _Mapping]]] = ..., cancelled_runs: _Optional[int] = ..., successful_runs: _Optional[int] = ...) -> None: ...

class Protection(_message.Message):
    __slots__ = ("backup", "replication_rx", "replication_tx", "archival")
    class Details(_message.Message):
        __slots__ = ("object_count", "error_count", "bytes_transferred")
        OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
        object_count: int
        error_count: int
        bytes_transferred: int
        def __init__(self, object_count: _Optional[int] = ..., error_count: _Optional[int] = ..., bytes_transferred: _Optional[int] = ...) -> None: ...
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_RX_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TX_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_FIELD_NUMBER: _ClassVar[int]
    backup: Protection.Details
    replication_rx: Protection.Details
    replication_tx: Protection.Details
    archival: Protection.Details
    def __init__(self, backup: _Optional[_Union[Protection.Details, _Mapping]] = ..., replication_rx: _Optional[_Union[Protection.Details, _Mapping]] = ..., replication_tx: _Optional[_Union[Protection.Details, _Mapping]] = ..., archival: _Optional[_Union[Protection.Details, _Mapping]] = ...) -> None: ...

class ProtectedObjects(_message.Message):
    __slots__ = ("object_details_map",)
    class Details(_message.Message):
        __slots__ = ("protected_object_count", "protected_size", "unprotected_object_count", "unprotected_size")
        PROTECTED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_SIZE_FIELD_NUMBER: _ClassVar[int]
        UNPROTECTED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
        UNPROTECTED_SIZE_FIELD_NUMBER: _ClassVar[int]
        protected_object_count: int
        protected_size: int
        unprotected_object_count: int
        unprotected_size: int
        def __init__(self, protected_object_count: _Optional[int] = ..., protected_size: _Optional[int] = ..., unprotected_object_count: _Optional[int] = ..., unprotected_size: _Optional[int] = ...) -> None: ...
    class ObjectDetailsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProtectedObjects.Details
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProtectedObjects.Details, _Mapping]] = ...) -> None: ...
    OBJECT_DETAILS_MAP_FIELD_NUMBER: _ClassVar[int]
    object_details_map: _containers.MessageMap[int, ProtectedObjects.Details]
    def __init__(self, object_details_map: _Optional[_Mapping[int, ProtectedObjects.Details]] = ...) -> None: ...

class RestoreObjects(_message.Message):
    __slots__ = ("object_counts_map", "tasks_in_progress", "total_size_bytes")
    class ObjectCountsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OBJECT_COUNTS_MAP_FIELD_NUMBER: _ClassVar[int]
    TASKS_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    object_counts_map: _containers.ScalarMap[int, int]
    tasks_in_progress: int
    total_size_bytes: int
    def __init__(self, object_counts_map: _Optional[_Mapping[int, int]] = ..., tasks_in_progress: _Optional[int] = ..., total_size_bytes: _Optional[int] = ...) -> None: ...
