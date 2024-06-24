from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PruneKeyArg(_message.Message):
    __slots__ = ("num_buckets", "sharding_function", "bucket_id")
    NUM_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    SHARDING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    num_buckets: int
    sharding_function: str
    bucket_id: int
    def __init__(self, num_buckets: _Optional[int] = ..., sharding_function: _Optional[str] = ..., bucket_id: _Optional[int] = ...) -> None: ...

class PruneKeysCookie(_message.Message):
    __slots__ = ("bucket_id", "cookie", "status", "time_taken_usecs", "num_docs_scanned", "num_docs_deleted", "start_time_usecs")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[PruneKeysCookie.Status]
        kStarted: _ClassVar[PruneKeysCookie.Status]
        kDone: _ClassVar[PruneKeysCookie.Status]
    kNotStarted: PruneKeysCookie.Status
    kStarted: PruneKeysCookie.Status
    kDone: PruneKeysCookie.Status
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_DOCS_SCANNED_FIELD_NUMBER: _ClassVar[int]
    NUM_DOCS_DELETED_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    cookie: bytes
    status: PruneKeysCookie.Status
    time_taken_usecs: int
    num_docs_scanned: int
    num_docs_deleted: int
    start_time_usecs: int
    def __init__(self, bucket_id: _Optional[int] = ..., cookie: _Optional[bytes] = ..., status: _Optional[_Union[PruneKeysCookie.Status, str]] = ..., time_taken_usecs: _Optional[int] = ..., num_docs_scanned: _Optional[int] = ..., num_docs_deleted: _Optional[int] = ..., start_time_usecs: _Optional[int] = ...) -> None: ...

class ShuffleKeysCookie(_message.Message):
    __slots__ = ("bucket_id", "status", "start_time_secs", "time_taken_secs", "keys_copied_stats", "key", "num_docs_scanned")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[ShuffleKeysCookie.Status]
        kStarted: _ClassVar[ShuffleKeysCookie.Status]
        kDone: _ClassVar[ShuffleKeysCookie.Status]
    kNotStarted: ShuffleKeysCookie.Status
    kStarted: ShuffleKeysCookie.Status
    kDone: ShuffleKeysCookie.Status
    class KeysCopiedStats(_message.Message):
        __slots__ = ("bucket_id", "disk_id", "doc_count")
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DOC_COUNT_FIELD_NUMBER: _ClassVar[int]
        bucket_id: int
        disk_id: int
        doc_count: int
        def __init__(self, bucket_id: _Optional[int] = ..., disk_id: _Optional[int] = ..., doc_count: _Optional[int] = ...) -> None: ...
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    TIME_TAKEN_SECS_FIELD_NUMBER: _ClassVar[int]
    KEYS_COPIED_STATS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NUM_DOCS_SCANNED_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    status: ShuffleKeysCookie.Status
    start_time_secs: int
    time_taken_secs: int
    keys_copied_stats: _containers.RepeatedCompositeFieldContainer[ShuffleKeysCookie.KeysCopiedStats]
    key: str
    num_docs_scanned: int
    def __init__(self, bucket_id: _Optional[int] = ..., status: _Optional[_Union[ShuffleKeysCookie.Status, str]] = ..., start_time_secs: _Optional[int] = ..., time_taken_secs: _Optional[int] = ..., keys_copied_stats: _Optional[_Iterable[_Union[ShuffleKeysCookie.KeysCopiedStats, _Mapping]]] = ..., key: _Optional[str] = ..., num_docs_scanned: _Optional[int] = ...) -> None: ...
