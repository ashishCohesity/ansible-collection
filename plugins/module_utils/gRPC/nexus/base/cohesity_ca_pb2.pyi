from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserBootstrapCaKeyIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kInit: _ClassVar[UserBootstrapCaKeyIntent]
    kUpdate: _ClassVar[UserBootstrapCaKeyIntent]
kInit: UserBootstrapCaKeyIntent
kUpdate: UserBootstrapCaKeyIntent

class CertKeyPair(_message.Message):
    __slots__ = ("certificate", "private_key")
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    certificate: bytes
    private_key: bytes
    def __init__(self, certificate: _Optional[bytes] = ..., private_key: _Optional[bytes] = ...) -> None: ...

class CertProto(_message.Message):
    __slots__ = ("certs",)
    class CertsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CertKeyPair
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CertKeyPair, _Mapping]] = ...) -> None: ...
    CERTS_FIELD_NUMBER: _ClassVar[int]
    certs: _containers.MessageMap[str, CertKeyPair]
    def __init__(self, certs: _Optional[_Mapping[str, CertKeyPair]] = ...) -> None: ...

class UserBootstrapCaKeyPair(_message.Message):
    __slots__ = ("cert_chain_pem", "private_key", "intent")
    CERT_CHAIN_PEM_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    cert_chain_pem: _containers.RepeatedScalarFieldContainer[str]
    private_key: str
    intent: UserBootstrapCaKeyIntent
    def __init__(self, cert_chain_pem: _Optional[_Iterable[str]] = ..., private_key: _Optional[str] = ..., intent: _Optional[_Union[UserBootstrapCaKeyIntent, str]] = ...) -> None: ...

class UserBootstrapCaKeyProto(_message.Message):
    __slots__ = ("certs",)
    class CertsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UserBootstrapCaKeyPair
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UserBootstrapCaKeyPair, _Mapping]] = ...) -> None: ...
    CERTS_FIELD_NUMBER: _ClassVar[int]
    certs: _containers.MessageMap[str, UserBootstrapCaKeyPair]
    def __init__(self, certs: _Optional[_Mapping[str, UserBootstrapCaKeyPair]] = ...) -> None: ...
