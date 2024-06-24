from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CaRootCertificate(_message.Message):
    __slots__ = ("id", "name", "description", "certificate", "registration_time_usecs", "last_validated_time_usecs", "status")
    class ValidationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        valid: _ClassVar[CaRootCertificate.ValidationStatus]
        expired: _ClassVar[CaRootCertificate.ValidationStatus]
        revoked: _ClassVar[CaRootCertificate.ValidationStatus]
        unknown: _ClassVar[CaRootCertificate.ValidationStatus]
    valid: CaRootCertificate.ValidationStatus
    expired: CaRootCertificate.ValidationStatus
    revoked: CaRootCertificate.ValidationStatus
    unknown: CaRootCertificate.ValidationStatus
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_VALIDATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    certificate: bytes
    registration_time_usecs: int
    last_validated_time_usecs: int
    status: CaRootCertificate.ValidationStatus
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., certificate: _Optional[bytes] = ..., registration_time_usecs: _Optional[int] = ..., last_validated_time_usecs: _Optional[int] = ..., status: _Optional[_Union[CaRootCertificate.ValidationStatus, str]] = ...) -> None: ...

class CaTrustStoreProto(_message.Message):
    __slots__ = ("certificate_vec",)
    CERTIFICATE_VEC_FIELD_NUMBER: _ClassVar[int]
    certificate_vec: _containers.RepeatedCompositeFieldContainer[CaRootCertificate]
    def __init__(self, certificate_vec: _Optional[_Iterable[_Union[CaRootCertificate, _Mapping]]] = ...) -> None: ...
