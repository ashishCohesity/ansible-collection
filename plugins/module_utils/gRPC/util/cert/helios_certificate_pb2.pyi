from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CertProto(_message.Message):
    __slots__ = ("certificate", "private_key", "passphrase", "ca_chain")
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    certificate: bytes
    private_key: bytes
    passphrase: bytes
    ca_chain: bytes
    def __init__(self, certificate: _Optional[bytes] = ..., private_key: _Optional[bytes] = ..., passphrase: _Optional[bytes] = ..., ca_chain: _Optional[bytes] = ...) -> None: ...

class HeliosCertificateProto(_message.Message):
    __slots__ = ("rigel_controlplane_certificate_vec", "cluster_controlplane_certificate", "helios_public_certificate", "tenant_certificate", "notify_dms_cert_renewal_done")
    class RigelCertificateInfo(_message.Message):
        __slots__ = ("rigel_guid", "rigel_controlplane_certificate", "notify_rms_cert_renewal_done")
        RIGEL_GUID_FIELD_NUMBER: _ClassVar[int]
        RIGEL_CONTROLPLANE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        NOTIFY_RMS_CERT_RENEWAL_DONE_FIELD_NUMBER: _ClassVar[int]
        rigel_guid: int
        rigel_controlplane_certificate: CertProto
        notify_rms_cert_renewal_done: bool
        def __init__(self, rigel_guid: _Optional[int] = ..., rigel_controlplane_certificate: _Optional[_Union[CertProto, _Mapping]] = ..., notify_rms_cert_renewal_done: bool = ...) -> None: ...
    RIGEL_CONTROLPLANE_CERTIFICATE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONTROLPLANE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    HELIOS_PUBLIC_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    TENANT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_DMS_CERT_RENEWAL_DONE_FIELD_NUMBER: _ClassVar[int]
    rigel_controlplane_certificate_vec: _containers.RepeatedCompositeFieldContainer[HeliosCertificateProto.RigelCertificateInfo]
    cluster_controlplane_certificate: CertProto
    helios_public_certificate: bytes
    tenant_certificate: CertProto
    notify_dms_cert_renewal_done: bool
    def __init__(self, rigel_controlplane_certificate_vec: _Optional[_Iterable[_Union[HeliosCertificateProto.RigelCertificateInfo, _Mapping]]] = ..., cluster_controlplane_certificate: _Optional[_Union[CertProto, _Mapping]] = ..., helios_public_certificate: _Optional[bytes] = ..., tenant_certificate: _Optional[_Union[CertProto, _Mapping]] = ..., notify_dms_cert_renewal_done: bool = ...) -> None: ...
