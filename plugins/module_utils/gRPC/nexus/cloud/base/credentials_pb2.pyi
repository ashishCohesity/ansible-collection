from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kAzureCommercial: _ClassVar[SubscriptionType]
    kAzureGovCloud: _ClassVar[SubscriptionType]
    kAWSCommercial: _ClassVar[SubscriptionType]
    kAWSGovCloud: _ClassVar[SubscriptionType]
    kAzureStackCommercial: _ClassVar[SubscriptionType]
    kAWSC2S: _ClassVar[SubscriptionType]
    kAzureStackADFS: _ClassVar[SubscriptionType]

class AwsAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUseIAMUser: _ClassVar[AwsAuthMethod]
    kUseIAMRole: _ClassVar[AwsAuthMethod]
    kUseSTS: _ClassVar[AwsAuthMethod]
    kUseHelios: _ClassVar[AwsAuthMethod]
kAzureCommercial: SubscriptionType
kAzureGovCloud: SubscriptionType
kAWSCommercial: SubscriptionType
kAWSGovCloud: SubscriptionType
kAzureStackCommercial: SubscriptionType
kAWSC2S: SubscriptionType
kAzureStackADFS: SubscriptionType
kUseIAMUser: AwsAuthMethod
kUseIAMRole: AwsAuthMethod
kUseSTS: AwsAuthMethod
kUseHelios: AwsAuthMethod

class AzureSubscription(_message.Message):
    __slots__ = ("subscription_id",)
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class AzureApplication(_message.Message):
    __slots__ = ("application_id", "encrypted_application_key", "application_object_id")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    encrypted_application_key: str
    application_object_id: str
    def __init__(self, application_id: _Optional[str] = ..., encrypted_application_key: _Optional[str] = ..., application_object_id: _Optional[str] = ...) -> None: ...

class AzureCredentials(_message.Message):
    __slots__ = ("subscription_id", "application_id", "application_key", "encrypted_application_key", "tenant_id", "azure_stack_region", "azure_stack_hub_domain_name", "subscription_type", "subscriptions", "applications")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_APPLICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    AZURE_STACK_REGION_FIELD_NUMBER: _ClassVar[int]
    AZURE_STACK_HUB_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    application_id: str
    application_key: str
    encrypted_application_key: bytes
    tenant_id: str
    azure_stack_region: str
    azure_stack_hub_domain_name: str
    subscription_type: SubscriptionType
    subscriptions: _containers.RepeatedCompositeFieldContainer[AzureSubscription]
    applications: _containers.RepeatedCompositeFieldContainer[AzureApplication]
    def __init__(self, subscription_id: _Optional[str] = ..., application_id: _Optional[str] = ..., application_key: _Optional[str] = ..., encrypted_application_key: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., azure_stack_region: _Optional[str] = ..., azure_stack_hub_domain_name: _Optional[str] = ..., subscription_type: _Optional[_Union[SubscriptionType, str]] = ..., subscriptions: _Optional[_Iterable[_Union[AzureSubscription, _Mapping]]] = ..., applications: _Optional[_Iterable[_Union[AzureApplication, _Mapping]]] = ...) -> None: ...

class C2SCAPServerInfo(_message.Message):
    __slots__ = ("agency", "mission", "role", "password", "decrypted_password", "base_url", "server_ca_certificate", "client_certificate", "client_private_key")
    AGENCY_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DECRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    agency: str
    mission: str
    role: str
    password: bytes
    decrypted_password: str
    base_url: str
    server_ca_certificate: str
    client_certificate: str
    client_private_key: str
    def __init__(self, agency: _Optional[str] = ..., mission: _Optional[str] = ..., role: _Optional[str] = ..., password: _Optional[bytes] = ..., decrypted_password: _Optional[str] = ..., base_url: _Optional[str] = ..., server_ca_certificate: _Optional[str] = ..., client_certificate: _Optional[str] = ..., client_private_key: _Optional[str] = ...) -> None: ...

class AwsCredentials(_message.Message):
    __slots__ = ("auth_method", "access_key_id", "secret_access_key", "encrypted_secret_access_key", "subscription_type", "iam_role_arn", "c2s_server_cap_info", "cp_iam_role_arn", "endpoint")
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    C2S_SERVER_CAP_INFO_FIELD_NUMBER: _ClassVar[int]
    CP_IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    auth_method: AwsAuthMethod
    access_key_id: str
    secret_access_key: str
    encrypted_secret_access_key: bytes
    subscription_type: SubscriptionType
    iam_role_arn: str
    c2s_server_cap_info: C2SCAPServerInfo
    cp_iam_role_arn: str
    endpoint: str
    def __init__(self, auth_method: _Optional[_Union[AwsAuthMethod, str]] = ..., access_key_id: _Optional[str] = ..., secret_access_key: _Optional[str] = ..., encrypted_secret_access_key: _Optional[bytes] = ..., subscription_type: _Optional[_Union[SubscriptionType, str]] = ..., iam_role_arn: _Optional[str] = ..., c2s_server_cap_info: _Optional[_Union[C2SCAPServerInfo, _Mapping]] = ..., cp_iam_role_arn: _Optional[str] = ..., endpoint: _Optional[str] = ...) -> None: ...

class GcpCredentials(_message.Message):
    __slots__ = ("type", "project_id", "private_key_id", "encrypted_private_key_id", "encrypted_client_private_key", "client_email_address", "client_id", "auth_uri", "token_uri", "auth_provider_x509_cert_url", "client_x509_cert_url")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PRIVATE_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_CLIENT_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTH_URI_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URI_FIELD_NUMBER: _ClassVar[int]
    AUTH_PROVIDER_X509_CERT_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_X509_CERT_URL_FIELD_NUMBER: _ClassVar[int]
    type: str
    project_id: str
    private_key_id: str
    encrypted_private_key_id: str
    encrypted_client_private_key: bytes
    client_email_address: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    def __init__(self, type: _Optional[str] = ..., project_id: _Optional[str] = ..., private_key_id: _Optional[str] = ..., encrypted_private_key_id: _Optional[str] = ..., encrypted_client_private_key: _Optional[bytes] = ..., client_email_address: _Optional[str] = ..., client_id: _Optional[str] = ..., auth_uri: _Optional[str] = ..., token_uri: _Optional[str] = ..., auth_provider_x509_cert_url: _Optional[str] = ..., client_x509_cert_url: _Optional[str] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("azure_credentials", "aws_credentials", "gcp_credentials")
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AWS_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    GCP_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    azure_credentials: AzureCredentials
    aws_credentials: AwsCredentials
    gcp_credentials: GcpCredentials
    def __init__(self, azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]] = ..., aws_credentials: _Optional[_Union[AwsCredentials, _Mapping]] = ..., gcp_credentials: _Optional[_Union[GcpCredentials, _Mapping]] = ...) -> None: ...
