from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LicensingUrisProto(_message.Message):
    __slots__ = ("licensing_server_port", "base_uri", "api_version", "generate_certificate_uri", "download_certificate_uri", "cluster_usage_uri", "account_list_uri", "account_usage_uri", "orders_uri", "download_license_uri", "upload_audit_report_uri", "unregister_cluster_uri", "generate_license_uri", "is_account_classified_uri", "generate_license_key_uri", "health_check_uri", "map_dp_xpr", "tenant_overusage")
    LICENSING_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATE_CERTIFICATE_URI_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CERTIFICATE_URI_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_USAGE_URI_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LIST_URI_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_USAGE_URI_FIELD_NUMBER: _ClassVar[int]
    ORDERS_URI_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LICENSE_URI_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_AUDIT_REPORT_URI_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_CLUSTER_URI_FIELD_NUMBER: _ClassVar[int]
    GENERATE_LICENSE_URI_FIELD_NUMBER: _ClassVar[int]
    IS_ACCOUNT_CLASSIFIED_URI_FIELD_NUMBER: _ClassVar[int]
    GENERATE_LICENSE_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_URI_FIELD_NUMBER: _ClassVar[int]
    MAP_DP_XPR_FIELD_NUMBER: _ClassVar[int]
    TENANT_OVERUSAGE_FIELD_NUMBER: _ClassVar[int]
    licensing_server_port: int
    base_uri: str
    api_version: str
    generate_certificate_uri: str
    download_certificate_uri: str
    cluster_usage_uri: str
    account_list_uri: str
    account_usage_uri: str
    orders_uri: str
    download_license_uri: str
    upload_audit_report_uri: str
    unregister_cluster_uri: str
    generate_license_uri: str
    is_account_classified_uri: str
    generate_license_key_uri: str
    health_check_uri: str
    map_dp_xpr: str
    tenant_overusage: str
    def __init__(self, licensing_server_port: _Optional[int] = ..., base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., generate_certificate_uri: _Optional[str] = ..., download_certificate_uri: _Optional[str] = ..., cluster_usage_uri: _Optional[str] = ..., account_list_uri: _Optional[str] = ..., account_usage_uri: _Optional[str] = ..., orders_uri: _Optional[str] = ..., download_license_uri: _Optional[str] = ..., upload_audit_report_uri: _Optional[str] = ..., unregister_cluster_uri: _Optional[str] = ..., generate_license_uri: _Optional[str] = ..., is_account_classified_uri: _Optional[str] = ..., generate_license_key_uri: _Optional[str] = ..., health_check_uri: _Optional[str] = ..., map_dp_xpr: _Optional[str] = ..., tenant_overusage: _Optional[str] = ...) -> None: ...

class CustomerDetailsProto(_message.Message):
    __slots__ = ("customer_id", "name", "salesforce_id", "details", "contact_info_vec")
    class ContactInfo(_message.Message):
        __slots__ = ("name", "email", "phone_number")
        NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        name: str
        email: str
        phone_number: str
        def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone_number: _Optional[str] = ...) -> None: ...
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALESFORCE_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    customer_id: int
    name: str
    salesforce_id: str
    details: bytes
    contact_info_vec: _containers.RepeatedCompositeFieldContainer[CustomerDetailsProto.ContactInfo]
    def __init__(self, customer_id: _Optional[int] = ..., name: _Optional[str] = ..., salesforce_id: _Optional[str] = ..., details: _Optional[bytes] = ..., contact_info_vec: _Optional[_Iterable[_Union[CustomerDetailsProto.ContactInfo, _Mapping]]] = ...) -> None: ...
