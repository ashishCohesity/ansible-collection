from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CertificateInfo(_message.Message):
    __slots__ = ("version", "certificate", "host_type", "host_ips")
    class HostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOther: _ClassVar[CertificateInfo.HostType]
        kSapOracle: _ClassVar[CertificateInfo.HostType]
        kSapHana: _ClassVar[CertificateInfo.HostType]
    kOther: CertificateInfo.HostType
    kSapOracle: CertificateInfo.HostType
    kSapHana: CertificateInfo.HostType
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOST_IPS_FIELD_NUMBER: _ClassVar[int]
    version: int
    certificate: Certificate
    host_type: CertificateInfo.HostType
    host_ips: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, version: _Optional[int] = ..., certificate: _Optional[_Union[Certificate, _Mapping]] = ..., host_type: _Optional[_Union[CertificateInfo.HostType, str]] = ..., host_ips: _Optional[_Iterable[str]] = ...) -> None: ...

class Certificate(_message.Message):
    __slots__ = ("certificate_id", "content", "validity_period", "certificate_version")
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    content: bytes
    validity_period: str
    certificate_version: int
    def __init__(self, certificate_id: _Optional[str] = ..., content: _Optional[bytes] = ..., validity_period: _Optional[str] = ..., certificate_version: _Optional[int] = ...) -> None: ...
