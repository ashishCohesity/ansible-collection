from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShadowCopySetProto(_message.Message):
    __slots__ = ("server_shadow_copy_set_guid", "status", "context", "fsrvp_version", "shadow_copy_map")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[ShadowCopySetProto.Status]
        kAdded: _ClassVar[ShadowCopySetProto.Status]
        kCreationInProgress: _ClassVar[ShadowCopySetProto.Status]
        kCommitted: _ClassVar[ShadowCopySetProto.Status]
        kExposed: _ClassVar[ShadowCopySetProto.Status]
        kRecovered: _ClassVar[ShadowCopySetProto.Status]
    kStarted: ShadowCopySetProto.Status
    kAdded: ShadowCopySetProto.Status
    kCreationInProgress: ShadowCopySetProto.Status
    kCommitted: ShadowCopySetProto.Status
    kExposed: ShadowCopySetProto.Status
    kRecovered: ShadowCopySetProto.Status
    class ShadowShareMapProto(_message.Message):
        __slots__ = ("share_name", "shadow_copy_share_name", "is_exposed")
        SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
        SHADOW_COPY_SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_EXPOSED_FIELD_NUMBER: _ClassVar[int]
        share_name: str
        shadow_copy_share_name: str
        is_exposed: bool
        def __init__(self, share_name: _Optional[str] = ..., shadow_copy_share_name: _Optional[str] = ..., is_exposed: bool = ...) -> None: ...
    class ShadowCopyProto(_message.Message):
        __slots__ = ("server_shadow_copy_guid", "view_name", "view_id", "creation_timestamp", "share_map")
        class ShareMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ShadowCopySetProto.ShadowShareMapProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ShadowCopySetProto.ShadowShareMapProto, _Mapping]] = ...) -> None: ...
        SERVER_SHADOW_COPY_GUID_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SHARE_MAP_FIELD_NUMBER: _ClassVar[int]
        server_shadow_copy_guid: str
        view_name: str
        view_id: int
        creation_timestamp: int
        share_map: _containers.MessageMap[str, ShadowCopySetProto.ShadowShareMapProto]
        def __init__(self, server_shadow_copy_guid: _Optional[str] = ..., view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., creation_timestamp: _Optional[int] = ..., share_map: _Optional[_Mapping[str, ShadowCopySetProto.ShadowShareMapProto]] = ...) -> None: ...
    class ShadowCopyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ShadowCopySetProto.ShadowCopyProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ShadowCopySetProto.ShadowCopyProto, _Mapping]] = ...) -> None: ...
    SERVER_SHADOW_COPY_SET_GUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FSRVP_VERSION_FIELD_NUMBER: _ClassVar[int]
    SHADOW_COPY_MAP_FIELD_NUMBER: _ClassVar[int]
    server_shadow_copy_set_guid: str
    status: ShadowCopySetProto.Status
    context: int
    fsrvp_version: int
    shadow_copy_map: _containers.MessageMap[str, ShadowCopySetProto.ShadowCopyProto]
    def __init__(self, server_shadow_copy_set_guid: _Optional[str] = ..., status: _Optional[_Union[ShadowCopySetProto.Status, str]] = ..., context: _Optional[int] = ..., fsrvp_version: _Optional[int] = ..., shadow_copy_map: _Optional[_Mapping[str, ShadowCopySetProto.ShadowCopyProto]] = ...) -> None: ...

class ShadowCopySetContextProto(_message.Message):
    __slots__ = ("current_context", "client_retry_count", "context_timestamp", "current_shadow_copy_set")
    CURRENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SHADOW_COPY_SET_FIELD_NUMBER: _ClassVar[int]
    current_context: int
    client_retry_count: int
    context_timestamp: int
    current_shadow_copy_set: ShadowCopySetProto
    def __init__(self, current_context: _Optional[int] = ..., client_retry_count: _Optional[int] = ..., context_timestamp: _Optional[int] = ..., current_shadow_copy_set: _Optional[_Union[ShadowCopySetProto, _Mapping]] = ...) -> None: ...
