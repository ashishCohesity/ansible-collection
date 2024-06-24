from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntitlementInfo(_message.Message):
    __slots__ = ("state", "entitlement_id", "consumer_id", "subscription_timestamp", "unsubscription_timestamp", "plan")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSubscribed: _ClassVar[EntitlementInfo.State]
        kUnsubscribed: _ClassVar[EntitlementInfo.State]
    kSubscribed: EntitlementInfo.State
    kUnsubscribed: EntitlementInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIPTION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    state: EntitlementInfo.State
    entitlement_id: str
    consumer_id: str
    subscription_timestamp: int
    unsubscription_timestamp: int
    plan: str
    def __init__(self, state: _Optional[_Union[EntitlementInfo.State, str]] = ..., entitlement_id: _Optional[str] = ..., consumer_id: _Optional[str] = ..., subscription_timestamp: _Optional[int] = ..., unsubscription_timestamp: _Optional[int] = ..., plan: _Optional[str] = ...) -> None: ...

class AccountInfoProto(_message.Message):
    __slots__ = ("account_id", "state", "entitlement_info", "provisioning_info", "tenant_id", "service_account_email", "account_creation_timestamp", "account_deletion_timestamp", "storage_domain_name", "admin_user_email_list")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[AccountInfoProto.State]
        kRegistrationPending: _ClassVar[AccountInfoProto.State]
        kAssigningCluster: _ClassVar[AccountInfoProto.State]
        kResgiteringServiceAccount: _ClassVar[AccountInfoProto.State]
        kProvisioned: _ClassVar[AccountInfoProto.State]
        kApproved: _ClassVar[AccountInfoProto.State]
        kMarkedForRemoval: _ClassVar[AccountInfoProto.State]
        kOkToRemove: _ClassVar[AccountInfoProto.State]
    kNone: AccountInfoProto.State
    kRegistrationPending: AccountInfoProto.State
    kAssigningCluster: AccountInfoProto.State
    kResgiteringServiceAccount: AccountInfoProto.State
    kProvisioned: AccountInfoProto.State
    kApproved: AccountInfoProto.State
    kMarkedForRemoval: AccountInfoProto.State
    kOkToRemove: AccountInfoProto.State
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_INFO_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DELETION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ADMIN_USER_EMAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    state: AccountInfoProto.State
    entitlement_info: EntitlementInfo
    provisioning_info: ProvisioningInfoProto
    tenant_id: str
    service_account_email: str
    account_creation_timestamp: int
    account_deletion_timestamp: int
    storage_domain_name: str
    admin_user_email_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, account_id: _Optional[str] = ..., state: _Optional[_Union[AccountInfoProto.State, str]] = ..., entitlement_info: _Optional[_Union[EntitlementInfo, _Mapping]] = ..., provisioning_info: _Optional[_Union[ProvisioningInfoProto, _Mapping]] = ..., tenant_id: _Optional[str] = ..., service_account_email: _Optional[str] = ..., account_creation_timestamp: _Optional[int] = ..., account_deletion_timestamp: _Optional[int] = ..., storage_domain_name: _Optional[str] = ..., admin_user_email_list: _Optional[_Iterable[str]] = ...) -> None: ...

class ProvisioningInfoProto(_message.Message):
    __slots__ = ("organization_name", "contact_emails", "project_id", "data_size", "gcp_region")
    class DataSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSmall: _ClassVar[ProvisioningInfoProto.DataSize]
        kMedium: _ClassVar[ProvisioningInfoProto.DataSize]
        kLarge: _ClassVar[ProvisioningInfoProto.DataSize]
    kSmall: ProvisioningInfoProto.DataSize
    kMedium: ProvisioningInfoProto.DataSize
    kLarge: ProvisioningInfoProto.DataSize
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAILS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    GCP_REGION_FIELD_NUMBER: _ClassVar[int]
    organization_name: str
    contact_emails: _containers.RepeatedScalarFieldContainer[str]
    project_id: str
    data_size: ProvisioningInfoProto.DataSize
    gcp_region: str
    def __init__(self, organization_name: _Optional[str] = ..., contact_emails: _Optional[_Iterable[str]] = ..., project_id: _Optional[str] = ..., data_size: _Optional[_Union[ProvisioningInfoProto.DataSize, str]] = ..., gcp_region: _Optional[str] = ...) -> None: ...

class GcpBaasUriProto(_message.Message):
    __slots__ = ("base_uri", "api_version", "account_info_uri", "provision_account_uri", "provisioning_done_uri", "add_admin_user_uri", "delete_admin_user_uri")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_INFO_URI_FIELD_NUMBER: _ClassVar[int]
    PROVISION_ACCOUNT_URI_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_DONE_URI_FIELD_NUMBER: _ClassVar[int]
    ADD_ADMIN_USER_URI_FIELD_NUMBER: _ClassVar[int]
    DELETE_ADMIN_USER_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    api_version: str
    account_info_uri: str
    provision_account_uri: str
    provisioning_done_uri: str
    add_admin_user_uri: str
    delete_admin_user_uri: str
    def __init__(self, base_uri: _Optional[str] = ..., api_version: _Optional[str] = ..., account_info_uri: _Optional[str] = ..., provision_account_uri: _Optional[str] = ..., provisioning_done_uri: _Optional[str] = ..., add_admin_user_uri: _Optional[str] = ..., delete_admin_user_uri: _Optional[str] = ...) -> None: ...

class GetAccountInfoArg(_message.Message):
    __slots__ = ("account_id", "fetch_from_google")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FETCH_FROM_GOOGLE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    fetch_from_google: bool
    def __init__(self, account_id: _Optional[str] = ..., fetch_from_google: bool = ...) -> None: ...

class GetAccountInfoResult(_message.Message):
    __slots__ = ("account_info",)
    ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    account_info: AccountInfoProto
    def __init__(self, account_info: _Optional[_Union[AccountInfoProto, _Mapping]] = ...) -> None: ...

class UpsertAccountInfoArg(_message.Message):
    __slots__ = ("account_info",)
    ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    account_info: AccountInfoProto
    def __init__(self, account_info: _Optional[_Union[AccountInfoProto, _Mapping]] = ...) -> None: ...

class UpsertAccountInfoResult(_message.Message):
    __slots__ = ("upserted_account_info",)
    UPSERTED_ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    upserted_account_info: AccountInfoProto
    def __init__(self, upserted_account_info: _Optional[_Union[AccountInfoProto, _Mapping]] = ...) -> None: ...

class ProvisionAccountArg(_message.Message):
    __slots__ = ("account_id", "provisioning_info")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_INFO_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    provisioning_info: ProvisioningInfoProto
    def __init__(self, account_id: _Optional[str] = ..., provisioning_info: _Optional[_Union[ProvisioningInfoProto, _Mapping]] = ...) -> None: ...

class ProvisionAccountResult(_message.Message):
    __slots__ = ("error_detail",)
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_detail: str
    def __init__(self, error_detail: _Optional[str] = ...) -> None: ...

class ProvisioningDoneArg(_message.Message):
    __slots__ = ("account_id", "status", "service_account_email")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    status: bool
    service_account_email: str
    def __init__(self, account_id: _Optional[str] = ..., status: bool = ..., service_account_email: _Optional[str] = ...) -> None: ...

class ProvisioningDoneResult(_message.Message):
    __slots__ = ("error_detail",)
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_detail: str
    def __init__(self, error_detail: _Optional[str] = ...) -> None: ...

class AddAdminUserArg(_message.Message):
    __slots__ = ("account_id", "admin_user_email")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    admin_user_email: str
    def __init__(self, account_id: _Optional[str] = ..., admin_user_email: _Optional[str] = ...) -> None: ...

class AddAdminUserResult(_message.Message):
    __slots__ = ("error_detail",)
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_detail: str
    def __init__(self, error_detail: _Optional[str] = ...) -> None: ...

class DeleteAdminUserArg(_message.Message):
    __slots__ = ("account_id", "admin_user_email")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    admin_user_email: str
    def __init__(self, account_id: _Optional[str] = ..., admin_user_email: _Optional[str] = ...) -> None: ...

class DeleteAdminUserResult(_message.Message):
    __slots__ = ("error_detail",)
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_detail: str
    def __init__(self, error_detail: _Optional[str] = ...) -> None: ...
