from bridge.vault.base import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadContext(_message.Message):
    __slots__ = ("resumable_upload_url", "intent_object_info_vec", "finalized_object_info", "is_object_empty", "is_multipart_disabled")
    class MD5Ctx(_message.Message):
        __slots__ = ("a", "b", "c", "d", "nl", "nh", "data_vec", "num")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        C_FIELD_NUMBER: _ClassVar[int]
        D_FIELD_NUMBER: _ClassVar[int]
        NL_FIELD_NUMBER: _ClassVar[int]
        NH_FIELD_NUMBER: _ClassVar[int]
        DATA_VEC_FIELD_NUMBER: _ClassVar[int]
        NUM_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: int
        c: int
        d: int
        nl: int
        nh: int
        data_vec: _containers.RepeatedScalarFieldContainer[int]
        num: int
        def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., c: _Optional[int] = ..., d: _Optional[int] = ..., nl: _Optional[int] = ..., nh: _Optional[int] = ..., data_vec: _Optional[_Iterable[int]] = ..., num: _Optional[int] = ...) -> None: ...
    class ObjectInfo(_message.Message):
        __slots__ = ("context", "checksum", "size")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        context: UploadContext.MD5Ctx
        checksum: bytes
        size: int
        def __init__(self, context: _Optional[_Union[UploadContext.MD5Ctx, _Mapping]] = ..., checksum: _Optional[bytes] = ..., size: _Optional[int] = ...) -> None: ...
    RESUMABLE_UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    INTENT_OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_EMPTY_FIELD_NUMBER: _ClassVar[int]
    IS_MULTIPART_DISABLED_FIELD_NUMBER: _ClassVar[int]
    resumable_upload_url: bytes
    intent_object_info_vec: _containers.RepeatedCompositeFieldContainer[UploadContext.ObjectInfo]
    finalized_object_info: UploadContext.ObjectInfo
    is_object_empty: bool
    is_multipart_disabled: bool
    def __init__(self, resumable_upload_url: _Optional[bytes] = ..., intent_object_info_vec: _Optional[_Iterable[_Union[UploadContext.ObjectInfo, _Mapping]]] = ..., finalized_object_info: _Optional[_Union[UploadContext.ObjectInfo, _Mapping]] = ..., is_object_empty: bool = ..., is_multipart_disabled: bool = ...) -> None: ...

class DownloadContext(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListObjectsResultProto(_message.Message):
    __slots__ = ("item_vec", "next_page_token")
    class Item(_message.Message):
        __slots__ = ("name", "size")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        name: str
        size: int
        def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...
    ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    item_vec: _containers.RepeatedCompositeFieldContainer[ListObjectsResultProto.Item]
    next_page_token: str
    def __init__(self, item_vec: _Optional[_Iterable[_Union[ListObjectsResultProto.Item, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class LifecycleProto(_message.Message):
    __slots__ = ("lifecycle",)
    class Lifecycle(_message.Message):
        __slots__ = ("rule",)
        class Rule(_message.Message):
            __slots__ = ("action", "condition")
            class Action(_message.Message):
                __slots__ = ("type",)
                TYPE_FIELD_NUMBER: _ClassVar[int]
                type: str
                def __init__(self, type: _Optional[str] = ...) -> None: ...
            class Condition(_message.Message):
                __slots__ = ("age", "created_before", "is_live", "matches_storage_class", "num_newer_versions")
                AGE_FIELD_NUMBER: _ClassVar[int]
                CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
                IS_LIVE_FIELD_NUMBER: _ClassVar[int]
                MATCHES_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
                NUM_NEWER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
                age: int
                created_before: str
                is_live: bool
                matches_storage_class: _containers.RepeatedScalarFieldContainer[str]
                num_newer_versions: int
                def __init__(self, age: _Optional[int] = ..., created_before: _Optional[str] = ..., is_live: bool = ..., matches_storage_class: _Optional[_Iterable[str]] = ..., num_newer_versions: _Optional[int] = ...) -> None: ...
            ACTION_FIELD_NUMBER: _ClassVar[int]
            CONDITION_FIELD_NUMBER: _ClassVar[int]
            action: LifecycleProto.Lifecycle.Rule.Action
            condition: LifecycleProto.Lifecycle.Rule.Condition
            def __init__(self, action: _Optional[_Union[LifecycleProto.Lifecycle.Rule.Action, _Mapping]] = ..., condition: _Optional[_Union[LifecycleProto.Lifecycle.Rule.Condition, _Mapping]] = ...) -> None: ...
        RULE_FIELD_NUMBER: _ClassVar[int]
        rule: _containers.RepeatedCompositeFieldContainer[LifecycleProto.Lifecycle.Rule]
        def __init__(self, rule: _Optional[_Iterable[_Union[LifecycleProto.Lifecycle.Rule, _Mapping]]] = ...) -> None: ...
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    lifecycle: LifecycleProto.Lifecycle
    def __init__(self, lifecycle: _Optional[_Union[LifecycleProto.Lifecycle, _Mapping]] = ...) -> None: ...

class NearlineCookie(_message.Message):
    __slots__ = ("monitoring_cookie",)
    MONITORING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    monitoring_cookie: _common_pb2.MonitoringCookie
    def __init__(self, monitoring_cookie: _Optional[_Union[_common_pb2.MonitoringCookie, _Mapping]] = ...) -> None: ...
