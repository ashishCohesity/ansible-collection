from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdDomainDiscoveryLockProto(_message.Message):
    __slots__ = ("gandalf_key", "primary_map")
    class Record(_message.Message):
        __slots__ = ("intent_time_secs", "intent_node_id", "last_discovery_time_secs", "last_discovery_node_id", "is_last_discovery_success")
        INTENT_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        INTENT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_DISCOVERY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
        LAST_DISCOVERY_NODE_ID_FIELD_NUMBER: _ClassVar[int]
        IS_LAST_DISCOVERY_SUCCESS_FIELD_NUMBER: _ClassVar[int]
        intent_time_secs: int
        intent_node_id: int
        last_discovery_time_secs: int
        last_discovery_node_id: int
        is_last_discovery_success: bool
        def __init__(self, intent_time_secs: _Optional[int] = ..., intent_node_id: _Optional[int] = ..., last_discovery_time_secs: _Optional[int] = ..., last_discovery_node_id: _Optional[int] = ..., is_last_discovery_success: bool = ...) -> None: ...
    class PrimaryMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AdDomainDiscoveryLockProto.Record
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AdDomainDiscoveryLockProto.Record, _Mapping]] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_MAP_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    primary_map: _containers.MessageMap[str, AdDomainDiscoveryLockProto.Record]
    def __init__(self, gandalf_key: _Optional[str] = ..., primary_map: _Optional[_Mapping[str, AdDomainDiscoveryLockProto.Record]] = ...) -> None: ...
