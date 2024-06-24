from helios.baas.base import gcp_baas_pb2 as _gcp_baas_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UriProto(_message.Message):
    __slots__ = ("base_uri", "allocate_cluster")
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    ALLOCATE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    allocate_cluster: str
    def __init__(self, base_uri: _Optional[str] = ..., allocate_cluster: _Optional[str] = ...) -> None: ...

class AllocateClusterArg(_message.Message):
    __slots__ = ("request_id", "service_type", "cloud_type", "baas_account_id", "region", "organization_name", "tenant_id", "storage_domain_name", "data_size")
    class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KGcpbaas: _ClassVar[AllocateClusterArg.ServiceType]
        Kthunderbolt: _ClassVar[AllocateClusterArg.ServiceType]
    KGcpbaas: AllocateClusterArg.ServiceType
    Kthunderbolt: AllocateClusterArg.ServiceType
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    BAAS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    service_type: AllocateClusterArg.ServiceType
    cloud_type: str
    baas_account_id: str
    region: str
    organization_name: str
    tenant_id: str
    storage_domain_name: str
    data_size: _gcp_baas_pb2.ProvisioningInfoProto.DataSize
    def __init__(self, request_id: _Optional[str] = ..., service_type: _Optional[_Union[AllocateClusterArg.ServiceType, str]] = ..., cloud_type: _Optional[str] = ..., baas_account_id: _Optional[str] = ..., region: _Optional[str] = ..., organization_name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., storage_domain_name: _Optional[str] = ..., data_size: _Optional[_Union[_gcp_baas_pb2.ProvisioningInfoProto.DataSize, str]] = ...) -> None: ...

class AllocateClusterResult(_message.Message):
    __slots__ = ("error_detail",)
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    error_detail: str
    def __init__(self, error_detail: _Optional[str] = ...) -> None: ...

class CreateClusterArg(_message.Message):
    __slots__ = ("cloud_type", "baas_account_id", "region", "organization_name", "data_size")
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    BAAS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    cloud_type: str
    baas_account_id: str
    region: str
    organization_name: str
    data_size: _gcp_baas_pb2.ProvisioningInfoProto.DataSize
    def __init__(self, cloud_type: _Optional[str] = ..., baas_account_id: _Optional[str] = ..., region: _Optional[str] = ..., organization_name: _Optional[str] = ..., data_size: _Optional[_Union[_gcp_baas_pb2.ProvisioningInfoProto.DataSize, str]] = ...) -> None: ...

class CreateClusterResult(_message.Message):
    __slots__ = ("cluster_ip",)
    CLUSTER_IP_FIELD_NUMBER: _ClassVar[int]
    cluster_ip: str
    def __init__(self, cluster_ip: _Optional[str] = ...) -> None: ...

class GetAccessTokenArg(_message.Message):
    __slots__ = ("cluster_ip",)
    CLUSTER_IP_FIELD_NUMBER: _ClassVar[int]
    cluster_ip: str
    def __init__(self, cluster_ip: _Optional[str] = ...) -> None: ...

class GetAccessTokenResult(_message.Message):
    __slots__ = ("helios_token",)
    HELIOS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    helios_token: str
    def __init__(self, helios_token: _Optional[str] = ...) -> None: ...

class CreateTenantArg(_message.Message):
    __slots__ = ("organization_name", "tenant_id", "cluster_ip", "helios_token")
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IP_FIELD_NUMBER: _ClassVar[int]
    HELIOS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    organization_name: str
    tenant_id: str
    cluster_ip: str
    helios_token: str
    def __init__(self, organization_name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., cluster_ip: _Optional[str] = ..., helios_token: _Optional[str] = ...) -> None: ...

class CreateTenantResult(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class CreateServiceAccountArg(_message.Message):
    __slots__ = ("organization_name", "project_id", "tenant_id")
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    organization_name: str
    project_id: str
    tenant_id: str
    def __init__(self, organization_name: _Optional[str] = ..., project_id: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class CreateServiceAccountResult(_message.Message):
    __slots__ = ("service_account", "private_key")
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    private_key: str
    def __init__(self, service_account: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...

class RegisterSourceArg(_message.Message):
    __slots__ = ("cluster_ip", "helios_token", "service_account", "private_key", "tenant_id", "region", "data_size")
    CLUSTER_IP_FIELD_NUMBER: _ClassVar[int]
    HELIOS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    cluster_ip: str
    helios_token: str
    service_account: str
    private_key: str
    tenant_id: str
    region: str
    data_size: _gcp_baas_pb2.ProvisioningInfoProto.DataSize
    def __init__(self, cluster_ip: _Optional[str] = ..., helios_token: _Optional[str] = ..., service_account: _Optional[str] = ..., private_key: _Optional[str] = ..., tenant_id: _Optional[str] = ..., region: _Optional[str] = ..., data_size: _Optional[_Union[_gcp_baas_pb2.ProvisioningInfoProto.DataSize, str]] = ...) -> None: ...

class RegisterSourceResult(_message.Message):
    __slots__ = ("service_account", "private_key")
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    private_key: str
    def __init__(self, service_account: _Optional[str] = ..., private_key: _Optional[str] = ...) -> None: ...

class CreateStorageDomainArg(_message.Message):
    __slots__ = ("cluster_ip", "helios_token", "storage_domain_name", "tenant_id")
    CLUSTER_IP_FIELD_NUMBER: _ClassVar[int]
    HELIOS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_ip: str
    helios_token: str
    storage_domain_name: str
    tenant_id: str
    def __init__(self, cluster_ip: _Optional[str] = ..., helios_token: _Optional[str] = ..., storage_domain_name: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class CreateStorageDomainResult(_message.Message):
    __slots__ = ("storage_domain_id",)
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    storage_domain_id: int
    def __init__(self, storage_domain_id: _Optional[int] = ...) -> None: ...

class ProvisioningDoneArg(_message.Message):
    __slots__ = ("account_id", "service_account", "status")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    service_account: str
    status: bool
    def __init__(self, account_id: _Optional[str] = ..., service_account: _Optional[str] = ..., status: bool = ...) -> None: ...

class ProvisioningDoneResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
