from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WALInjectInfo(_message.Message):
    __slots__ = ("name", "reason", "timestamp", "node_id", "wal_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    WAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    reason: bytes
    timestamp: int
    node_id: int
    wal_type: bytes
    def __init__(self, name: _Optional[bytes] = ..., reason: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., node_id: _Optional[int] = ..., wal_type: _Optional[bytes] = ...) -> None: ...

class WALInjectHistory(_message.Message):
    __slots__ = ("gandalf_key", "wal_inject_info")
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    WAL_INJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: bytes
    wal_inject_info: _containers.RepeatedCompositeFieldContainer[WALInjectInfo]
    def __init__(self, gandalf_key: _Optional[bytes] = ..., wal_inject_info: _Optional[_Iterable[_Union[WALInjectInfo, _Mapping]]] = ...) -> None: ...
