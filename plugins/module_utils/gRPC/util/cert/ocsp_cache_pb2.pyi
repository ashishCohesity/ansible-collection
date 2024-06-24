from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheEntry(_message.Message):
    __slots__ = ("key", "value")
    class CacheKey(_message.Message):
        __slots__ = ("SerialNumber", "Issuer")
        SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        SerialNumber: str
        Issuer: str
        def __init__(self, SerialNumber: _Optional[str] = ..., Issuer: _Optional[str] = ...) -> None: ...
    class CacheValue(_message.Message):
        __slots__ = ("status", "added_time_usecs", "valid_till_time_usecs")
        class CertificateStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Good: _ClassVar[CacheEntry.CacheValue.CertificateStatus]
            Revoked: _ClassVar[CacheEntry.CacheValue.CertificateStatus]
            Unknown: _ClassVar[CacheEntry.CacheValue.CertificateStatus]
        Good: CacheEntry.CacheValue.CertificateStatus
        Revoked: CacheEntry.CacheValue.CertificateStatus
        Unknown: CacheEntry.CacheValue.CertificateStatus
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ADDED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        VALID_TILL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        status: CacheEntry.CacheValue.CertificateStatus
        added_time_usecs: int
        valid_till_time_usecs: int
        def __init__(self, status: _Optional[_Union[CacheEntry.CacheValue.CertificateStatus, str]] = ..., added_time_usecs: _Optional[int] = ..., valid_till_time_usecs: _Optional[int] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: CacheEntry.CacheKey
    value: CacheEntry.CacheValue
    def __init__(self, key: _Optional[_Union[CacheEntry.CacheKey, _Mapping]] = ..., value: _Optional[_Union[CacheEntry.CacheValue, _Mapping]] = ...) -> None: ...

class OcspCacheProto(_message.Message):
    __slots__ = ("cache_entry_vec",)
    CACHE_ENTRY_VEC_FIELD_NUMBER: _ClassVar[int]
    cache_entry_vec: _containers.RepeatedCompositeFieldContainer[CacheEntry]
    def __init__(self, cache_entry_vec: _Optional[_Iterable[_Union[CacheEntry, _Mapping]]] = ...) -> None: ...
