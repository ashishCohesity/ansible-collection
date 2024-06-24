from gandalf.base import error_pb2 as _error_pb2
from gandalf.server.stub import gandalf_pb2 as _gandalf_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchKeysArg(_message.Message):
    __slots__ = ("all_keys_watched_vec",)
    ALL_KEYS_WATCHED_VEC_FIELD_NUMBER: _ClassVar[int]
    all_keys_watched_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, all_keys_watched_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class WatchKeysUpdate(_message.Message):
    __slots__ = ("key_value_info_vec",)
    class KeyValueInfo(_message.Message):
        __slots__ = ("key", "val", "version")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VAL_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        key: str
        val: bytes
        version: int
        def __init__(self, key: _Optional[str] = ..., val: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...
    KEY_VALUE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    key_value_info_vec: _containers.RepeatedCompositeFieldContainer[WatchKeysUpdate.KeyValueInfo]
    def __init__(self, key_value_info_vec: _Optional[_Iterable[_Union[WatchKeysUpdate.KeyValueInfo, _Mapping]]] = ...) -> None: ...

class LookupKeyArgWrapper(_message.Message):
    __slots__ = ("arg",)
    ARG_FIELD_NUMBER: _ClassVar[int]
    arg: _gandalf_pb2.LookupKeyArg
    def __init__(self, arg: _Optional[_Union[_gandalf_pb2.LookupKeyArg, _Mapping]] = ...) -> None: ...

class LookupKeyResultWrapper(_message.Message):
    __slots__ = ("error_type", "result")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    error_type: _error_pb2.ErrorProto.Type
    result: _gandalf_pb2.LookupKeyResult
    def __init__(self, error_type: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., result: _Optional[_Union[_gandalf_pb2.LookupKeyResult, _Mapping]] = ...) -> None: ...

class UpdateKeyArgWrapper(_message.Message):
    __slots__ = ("arg", "is_value_cas_fallback")
    ARG_FIELD_NUMBER: _ClassVar[int]
    IS_VALUE_CAS_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    arg: _gandalf_pb2.UpdateKeyArg
    is_value_cas_fallback: bool
    def __init__(self, arg: _Optional[_Union[_gandalf_pb2.UpdateKeyArg, _Mapping]] = ..., is_value_cas_fallback: bool = ...) -> None: ...

class UpdateKeyResultWrapper(_message.Message):
    __slots__ = ("error_type", "result")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    error_type: _error_pb2.ErrorProto.Type
    result: _gandalf_pb2.UpdateKeyResult
    def __init__(self, error_type: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., result: _Optional[_Union[_gandalf_pb2.UpdateKeyResult, _Mapping]] = ...) -> None: ...

class DeleteKeyArgWrapper(_message.Message):
    __slots__ = ("arg",)
    ARG_FIELD_NUMBER: _ClassVar[int]
    arg: _gandalf_pb2.DeleteKeyArg
    def __init__(self, arg: _Optional[_Union[_gandalf_pb2.DeleteKeyArg, _Mapping]] = ...) -> None: ...

class DeleteKeyResultWrapper(_message.Message):
    __slots__ = ("error_type", "result")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    error_type: _error_pb2.ErrorProto.Type
    result: _gandalf_pb2.DeleteKeyResult
    def __init__(self, error_type: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ..., result: _Optional[_Union[_gandalf_pb2.DeleteKeyResult, _Mapping]] = ...) -> None: ...

class AtomicIncrementArgWrapper(_message.Message):
    __slots__ = ("arg",)
    ARG_FIELD_NUMBER: _ClassVar[int]
    arg: _gandalf_pb2.AtomicIncrementArg
    def __init__(self, arg: _Optional[_Union[_gandalf_pb2.AtomicIncrementArg, _Mapping]] = ...) -> None: ...

class AtomicIncrementResultWrapper(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _gandalf_pb2.AtomicIncrementResult
    def __init__(self, result: _Optional[_Union[_gandalf_pb2.AtomicIncrementResult, _Mapping]] = ...) -> None: ...

class SsMessage(_message.Message):
    __slots__ = ("type", "request_id", "watch_keys_arg", "watch_keys_update", "wrapper_lookup_key_arg", "wrapper_lookup_key_result", "wrapper_update_key_arg", "wrapper_update_key_result", "wrapper_delete_key_arg", "wrapper_delete_key_result", "wrapper_atomic_increment_arg", "wrapper_atomic_increment_result")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[SsMessage.Type]
        kWatchKey: _ClassVar[SsMessage.Type]
        kLookupKey: _ClassVar[SsMessage.Type]
        kUpdateKey: _ClassVar[SsMessage.Type]
        kDeleteKey: _ClassVar[SsMessage.Type]
        kAtomicIncrement: _ClassVar[SsMessage.Type]
    kUnknown: SsMessage.Type
    kWatchKey: SsMessage.Type
    kLookupKey: SsMessage.Type
    kUpdateKey: SsMessage.Type
    kDeleteKey: SsMessage.Type
    kAtomicIncrement: SsMessage.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    WATCH_KEYS_ARG_FIELD_NUMBER: _ClassVar[int]
    WATCH_KEYS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_LOOKUP_KEY_ARG_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_LOOKUP_KEY_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_UPDATE_KEY_ARG_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_UPDATE_KEY_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_DELETE_KEY_ARG_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_DELETE_KEY_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_ATOMIC_INCREMENT_ARG_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_ATOMIC_INCREMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    type: SsMessage.Type
    request_id: int
    watch_keys_arg: WatchKeysArg
    watch_keys_update: WatchKeysUpdate
    wrapper_lookup_key_arg: LookupKeyArgWrapper
    wrapper_lookup_key_result: LookupKeyResultWrapper
    wrapper_update_key_arg: UpdateKeyArgWrapper
    wrapper_update_key_result: UpdateKeyResultWrapper
    wrapper_delete_key_arg: DeleteKeyArgWrapper
    wrapper_delete_key_result: DeleteKeyResultWrapper
    wrapper_atomic_increment_arg: AtomicIncrementArgWrapper
    wrapper_atomic_increment_result: AtomicIncrementResultWrapper
    def __init__(self, type: _Optional[_Union[SsMessage.Type, str]] = ..., request_id: _Optional[int] = ..., watch_keys_arg: _Optional[_Union[WatchKeysArg, _Mapping]] = ..., watch_keys_update: _Optional[_Union[WatchKeysUpdate, _Mapping]] = ..., wrapper_lookup_key_arg: _Optional[_Union[LookupKeyArgWrapper, _Mapping]] = ..., wrapper_lookup_key_result: _Optional[_Union[LookupKeyResultWrapper, _Mapping]] = ..., wrapper_update_key_arg: _Optional[_Union[UpdateKeyArgWrapper, _Mapping]] = ..., wrapper_update_key_result: _Optional[_Union[UpdateKeyResultWrapper, _Mapping]] = ..., wrapper_delete_key_arg: _Optional[_Union[DeleteKeyArgWrapper, _Mapping]] = ..., wrapper_delete_key_result: _Optional[_Union[DeleteKeyResultWrapper, _Mapping]] = ..., wrapper_atomic_increment_arg: _Optional[_Union[AtomicIncrementArgWrapper, _Mapping]] = ..., wrapper_atomic_increment_result: _Optional[_Union[AtomicIncrementResultWrapper, _Mapping]] = ...) -> None: ...

class Constants(_message.Message):
    __slots__ = ()
    class GrpcMetadataKeys(_message.Message):
        __slots__ = ("tenant_id_key",)
        TENANT_ID_KEY_FIELD_NUMBER: _ClassVar[int]
        tenant_id_key: str
        def __init__(self, tenant_id_key: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
