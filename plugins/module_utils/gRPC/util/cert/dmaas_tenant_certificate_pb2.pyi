from util.cert import helios_certificate_pb2 as _helios_certificate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DmaasTenantCertificateProto(_message.Message):
    __slots__ = ("tenant_cert_info_vec", "connector_ca_chain")
    class TenantCertInfo(_message.Message):
        __slots__ = ("tenant_id", "tenant_certificate", "notify_dms_cert_renewal_done")
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        TENANT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        NOTIFY_DMS_CERT_RENEWAL_DONE_FIELD_NUMBER: _ClassVar[int]
        tenant_id: str
        tenant_certificate: _helios_certificate_pb2.CertProto
        notify_dms_cert_renewal_done: bool
        def __init__(self, tenant_id: _Optional[str] = ..., tenant_certificate: _Optional[_Union[_helios_certificate_pb2.CertProto, _Mapping]] = ..., notify_dms_cert_renewal_done: bool = ...) -> None: ...
    TENANT_CERT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CA_CHAIN_FIELD_NUMBER: _ClassVar[int]
    tenant_cert_info_vec: _containers.RepeatedCompositeFieldContainer[DmaasTenantCertificateProto.TenantCertInfo]
    connector_ca_chain: bytes
    def __init__(self, tenant_cert_info_vec: _Optional[_Iterable[_Union[DmaasTenantCertificateProto.TenantCertInfo, _Mapping]]] = ..., connector_ca_chain: _Optional[bytes] = ...) -> None: ...
