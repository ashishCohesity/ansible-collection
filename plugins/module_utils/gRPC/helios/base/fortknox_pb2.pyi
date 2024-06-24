from helios.base import helios_cluster_base_pb2 as _helios_cluster_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FortknoxCloudProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCloudProviderNotSet: _ClassVar[FortknoxCloudProvider]
    kAws: _ClassVar[FortknoxCloudProvider]
    kAzure: _ClassVar[FortknoxCloudProvider]

class CredCapability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCapabilityNotSet: _ClassVar[CredCapability]
    kReadPriv: _ClassVar[CredCapability]
    kWritePriv: _ClassVar[CredCapability]
    kListPriv: _ClassVar[CredCapability]
kCloudProviderNotSet: FortknoxCloudProvider
kAws: FortknoxCloudProvider
kAzure: FortknoxCloudProvider
kCapabilityNotSet: CredCapability
kReadPriv: CredCapability
kWritePriv: CredCapability
kListPriv: CredCapability

class GetFortknoxObjectStoreCredentialsRequest(_message.Message):
    __slots__ = ("cluster_identifier", "vault_id", "cloud_provider", "capability", "prefixes")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _helios_cluster_base_pb2.ClusterIdentifier
    vault_id: int
    cloud_provider: FortknoxCloudProvider
    capability: CredCapability
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2.ClusterIdentifier, _Mapping]] = ..., vault_id: _Optional[int] = ..., cloud_provider: _Optional[_Union[FortknoxCloudProvider, str]] = ..., capability: _Optional[_Union[CredCapability, str]] = ..., prefixes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFortknoxObjectStoreCredentialsResponse(_message.Message):
    __slots__ = ("credentials", "error")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    credentials: ObjectStoreCredentialsResult
    error: ErrorResponse
    def __init__(self, credentials: _Optional[_Union[ObjectStoreCredentialsResult, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class ErrorResponse(_message.Message):
    __slots__ = ("error_code", "description")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    error_code: int
    description: str
    def __init__(self, error_code: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class ObjectStoreCredentialsResult(_message.Message):
    __slots__ = ("cloud_provider", "expiry_timestamp_msecs", "capability", "prefixes", "aws_results", "azure_results")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    AWS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    AZURE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: FortknoxCloudProvider
    expiry_timestamp_msecs: int
    capability: CredCapability
    prefixes: _containers.RepeatedScalarFieldContainer[str]
    aws_results: AwsTemporaryCredentialsResult
    azure_results: AzureTemporaryObjectStoreCredentialsResult
    def __init__(self, cloud_provider: _Optional[_Union[FortknoxCloudProvider, str]] = ..., expiry_timestamp_msecs: _Optional[int] = ..., capability: _Optional[_Union[CredCapability, str]] = ..., prefixes: _Optional[_Iterable[str]] = ..., aws_results: _Optional[_Union[AwsTemporaryCredentialsResult, _Mapping]] = ..., azure_results: _Optional[_Union[AzureTemporaryObjectStoreCredentialsResult, _Mapping]] = ...) -> None: ...

class AwsTemporaryCredentialsResult(_message.Message):
    __slots__ = ("aws_role", "aws_access_key_id", "aws_access_secret", "aws_token", "aws_provider_name")
    AWS_ROLE_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_SECRET_FIELD_NUMBER: _ClassVar[int]
    AWS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AWS_PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    aws_role: str
    aws_access_key_id: str
    aws_access_secret: str
    aws_token: str
    aws_provider_name: str
    def __init__(self, aws_role: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_access_secret: _Optional[str] = ..., aws_token: _Optional[str] = ..., aws_provider_name: _Optional[str] = ...) -> None: ...

class AzureTemporaryObjectStoreCredentialsResult(_message.Message):
    __slots__ = ("bearer_token",)
    BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bearer_token: str
    def __init__(self, bearer_token: _Optional[str] = ...) -> None: ...

class GetFortknoxKmsCredentialsRequest(_message.Message):
    __slots__ = ("cluster_identifier", "kms_id", "cloud_provider")
    CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    KMS_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    cluster_identifier: _helios_cluster_base_pb2.ClusterIdentifier
    kms_id: int
    cloud_provider: FortknoxCloudProvider
    def __init__(self, cluster_identifier: _Optional[_Union[_helios_cluster_base_pb2.ClusterIdentifier, _Mapping]] = ..., kms_id: _Optional[int] = ..., cloud_provider: _Optional[_Union[FortknoxCloudProvider, str]] = ...) -> None: ...

class GetFortknoxKmsCredentialsResponse(_message.Message):
    __slots__ = ("credentials", "error")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    credentials: KmsCredentialsResult
    error: ErrorResponse
    def __init__(self, credentials: _Optional[_Union[KmsCredentialsResult, _Mapping]] = ..., error: _Optional[_Union[ErrorResponse, _Mapping]] = ...) -> None: ...

class KmsCredentialsResult(_message.Message):
    __slots__ = ("cloud_provider", "expiry_timestamp_msecs", "aws_results", "azure_results")
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    AWS_RESULTS_FIELD_NUMBER: _ClassVar[int]
    AZURE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    cloud_provider: FortknoxCloudProvider
    expiry_timestamp_msecs: int
    aws_results: AwsTemporaryCredentialsResult
    azure_results: AzureTemporaryKmsCredentialsResult
    def __init__(self, cloud_provider: _Optional[_Union[FortknoxCloudProvider, str]] = ..., expiry_timestamp_msecs: _Optional[int] = ..., aws_results: _Optional[_Union[AwsTemporaryCredentialsResult, _Mapping]] = ..., azure_results: _Optional[_Union[AzureTemporaryKmsCredentialsResult, _Mapping]] = ...) -> None: ...

class AzureTemporaryKmsCredentialsResult(_message.Message):
    __slots__ = ("bearer_token",)
    BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bearer_token: str
    def __init__(self, bearer_token: _Optional[str] = ...) -> None: ...
