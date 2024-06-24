from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpenIdPublicKeysProto(_message.Message):
    __slots__ = ("version", "open_id_provider_vec")
    class OpenIdProvider(_message.Message):
        __slots__ = ("domain", "last_updated_timestamp_usecs", "public_key_vec")
        class PublicKey(_message.Message):
            __slots__ = ("x5t", "x5c", "n", "e")
            X5T_FIELD_NUMBER: _ClassVar[int]
            X5C_FIELD_NUMBER: _ClassVar[int]
            N_FIELD_NUMBER: _ClassVar[int]
            E_FIELD_NUMBER: _ClassVar[int]
            x5t: str
            x5c: str
            n: str
            e: str
            def __init__(self, x5t: _Optional[str] = ..., x5c: _Optional[str] = ..., n: _Optional[str] = ..., e: _Optional[str] = ...) -> None: ...
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
        domain: str
        last_updated_timestamp_usecs: int
        public_key_vec: _containers.RepeatedCompositeFieldContainer[OpenIdPublicKeysProto.OpenIdProvider.PublicKey]
        def __init__(self, domain: _Optional[str] = ..., last_updated_timestamp_usecs: _Optional[int] = ..., public_key_vec: _Optional[_Iterable[_Union[OpenIdPublicKeysProto.OpenIdProvider.PublicKey, _Mapping]]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_PROVIDER_VEC_FIELD_NUMBER: _ClassVar[int]
    version: int
    open_id_provider_vec: _containers.RepeatedCompositeFieldContainer[OpenIdPublicKeysProto.OpenIdProvider]
    def __init__(self, version: _Optional[int] = ..., open_id_provider_vec: _Optional[_Iterable[_Union[OpenIdPublicKeysProto.OpenIdProvider, _Mapping]]] = ...) -> None: ...
