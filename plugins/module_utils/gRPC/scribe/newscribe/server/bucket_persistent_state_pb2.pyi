from scribe.newscribe.server import data_format_pb2 as _data_format_pb2
from scribe.newscribe.server.tablet import bucket_iterator_pb2 as _bucket_iterator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BucketPersistentStateProto(_message.Message):
    __slots__ = ("replica_incarnation", "last_known_caughtup_sequencer")
    REPLICA_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_CAUGHTUP_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    replica_incarnation: int
    last_known_caughtup_sequencer: int
    def __init__(self, replica_incarnation: _Optional[int] = ..., last_known_caughtup_sequencer: _Optional[int] = ...) -> None: ...

class BucketCatchupStatusProto(_message.Message):
    __slots__ = ("op_start_replica_incarnation", "last_known_caughtup_sequencer", "op_start_leader_lock_sequencer", "status_per_replica")
    class ReplicaCatchupStatus(_message.Message):
        __slots__ = ("replica_incarnation", "next_scan_cookie", "start_time", "completion_time", "num_keys_caught_up")
        REPLICA_INCARNATION_FIELD_NUMBER: _ClassVar[int]
        NEXT_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
        NUM_KEYS_CAUGHT_UP_FIELD_NUMBER: _ClassVar[int]
        replica_incarnation: int
        next_scan_cookie: bytes
        start_time: int
        completion_time: int
        num_keys_caught_up: int
        def __init__(self, replica_incarnation: _Optional[int] = ..., next_scan_cookie: _Optional[bytes] = ..., start_time: _Optional[int] = ..., completion_time: _Optional[int] = ..., num_keys_caught_up: _Optional[int] = ...) -> None: ...
    class StatusPerReplicaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BucketCatchupStatusProto.ReplicaCatchupStatus
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BucketCatchupStatusProto.ReplicaCatchupStatus, _Mapping]] = ...) -> None: ...
    OP_START_REPLICA_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_CAUGHTUP_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    OP_START_LEADER_LOCK_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    STATUS_PER_REPLICA_FIELD_NUMBER: _ClassVar[int]
    op_start_replica_incarnation: int
    last_known_caughtup_sequencer: int
    op_start_leader_lock_sequencer: int
    status_per_replica: _containers.MessageMap[int, BucketCatchupStatusProto.ReplicaCatchupStatus]
    def __init__(self, op_start_replica_incarnation: _Optional[int] = ..., last_known_caughtup_sequencer: _Optional[int] = ..., op_start_leader_lock_sequencer: _Optional[int] = ..., status_per_replica: _Optional[_Mapping[int, BucketCatchupStatusProto.ReplicaCatchupStatus]] = ...) -> None: ...

class ReplicaBackgroundScanStatusProto(_message.Message):
    __slots__ = ("incarnation", "scan_start_time", "scan_completion_time", "current_position")
    INCARNATION_FIELD_NUMBER: _ClassVar[int]
    SCAN_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SCAN_COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    incarnation: int
    scan_start_time: int
    scan_completion_time: int
    current_position: _bucket_iterator_pb2.IteratorPositionProto
    def __init__(self, incarnation: _Optional[int] = ..., scan_start_time: _Optional[int] = ..., scan_completion_time: _Optional[int] = ..., current_position: _Optional[_Union[_bucket_iterator_pb2.IteratorPositionProto, _Mapping]] = ...) -> None: ...

class LeaderBackgroundScanStatusProto(_message.Message):
    __slots__ = ("leader_incarnation", "gc_instance_id_threshold", "scan_start_time", "scan_completion_time", "current_position", "num_keys_scanned", "num_keys_gced")
    LEADER_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    GC_INSTANCE_ID_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SCAN_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SCAN_COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    NUM_KEYS_SCANNED_FIELD_NUMBER: _ClassVar[int]
    NUM_KEYS_GCED_FIELD_NUMBER: _ClassVar[int]
    leader_incarnation: int
    gc_instance_id_threshold: _data_format_pb2.PaxosInstance
    scan_start_time: int
    scan_completion_time: int
    current_position: _bucket_iterator_pb2.IteratorPositionProto
    num_keys_scanned: int
    num_keys_gced: int
    def __init__(self, leader_incarnation: _Optional[int] = ..., gc_instance_id_threshold: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ..., scan_start_time: _Optional[int] = ..., scan_completion_time: _Optional[int] = ..., current_position: _Optional[_Union[_bucket_iterator_pb2.IteratorPositionProto, _Mapping]] = ..., num_keys_scanned: _Optional[int] = ..., num_keys_gced: _Optional[int] = ...) -> None: ...

class TransferDbProgressState(_message.Message):
    __slots__ = ("view_version", "transfer_resume_position")
    VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_RESUME_POSITION_FIELD_NUMBER: _ClassVar[int]
    view_version: int
    transfer_resume_position: _bucket_iterator_pb2.IteratorPositionProto
    def __init__(self, view_version: _Optional[int] = ..., transfer_resume_position: _Optional[_Union[_bucket_iterator_pb2.IteratorPositionProto, _Mapping]] = ...) -> None: ...

class TransferSstFilesReceiverState(_message.Message):
    __slots__ = ("view_version", "tablet_id", "transfer_index", "next_offset", "is_last")
    VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    TABLET_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_INDEX_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_FIELD_NUMBER: _ClassVar[int]
    view_version: int
    tablet_id: int
    transfer_index: int
    next_offset: int
    is_last: bool
    def __init__(self, view_version: _Optional[int] = ..., tablet_id: _Optional[int] = ..., transfer_index: _Optional[int] = ..., next_offset: _Optional[int] = ..., is_last: bool = ...) -> None: ...

class TransferWALProgressState(_message.Message):
    __slots__ = ("view_version", "last_logical_timestamp")
    VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    view_version: int
    last_logical_timestamp: int
    def __init__(self, view_version: _Optional[int] = ..., last_logical_timestamp: _Optional[int] = ...) -> None: ...

class LiveMigrationState(_message.Message):
    __slots__ = ("view_version",)
    VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    view_version: int
    def __init__(self, view_version: _Optional[int] = ...) -> None: ...

class LiveMigrateToTargetViewState(_message.Message):
    __slots__ = ("view_version", "sender_caughtup_sequencer")
    VIEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    SENDER_CAUGHTUP_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    view_version: int
    sender_caughtup_sequencer: int
    def __init__(self, view_version: _Optional[int] = ..., sender_caughtup_sequencer: _Optional[int] = ...) -> None: ...
