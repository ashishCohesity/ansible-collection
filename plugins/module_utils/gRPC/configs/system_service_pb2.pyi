from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourcePool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSystemApps: _ClassVar[ResourcePool]
    kMarketplace: _ClassVar[ResourcePool]
kSystemApps: ResourcePool
kMarketplace: ResourcePool

class SystemServiceUidMapProto(_message.Message):
    __slots__ = ("kBifrost", "kTestservice", "kStatsService", "kAgentinstall", "kMetadataService", "kWorkqueueServer", "kElasticsearchService", "kAxon", "kMagnus", "kShelteredHarbor", "kCoreDNS", "kMetricServer", "kInfraOperator", "kMarketplaceOperator", "kSpireApp", "kSFTPUIApp")
    KBIFROST_FIELD_NUMBER: _ClassVar[int]
    KTESTSERVICE_FIELD_NUMBER: _ClassVar[int]
    KSTATSSERVICE_FIELD_NUMBER: _ClassVar[int]
    KAGENTINSTALL_FIELD_NUMBER: _ClassVar[int]
    KMETADATASERVICE_FIELD_NUMBER: _ClassVar[int]
    KWORKQUEUESERVER_FIELD_NUMBER: _ClassVar[int]
    KELASTICSEARCHSERVICE_FIELD_NUMBER: _ClassVar[int]
    KAXON_FIELD_NUMBER: _ClassVar[int]
    KMAGNUS_FIELD_NUMBER: _ClassVar[int]
    KSHELTEREDHARBOR_FIELD_NUMBER: _ClassVar[int]
    KCOREDNS_FIELD_NUMBER: _ClassVar[int]
    KMETRICSERVER_FIELD_NUMBER: _ClassVar[int]
    KINFRAOPERATOR_FIELD_NUMBER: _ClassVar[int]
    KMARKETPLACEOPERATOR_FIELD_NUMBER: _ClassVar[int]
    KSPIREAPP_FIELD_NUMBER: _ClassVar[int]
    KSFTPUIAPP_FIELD_NUMBER: _ClassVar[int]
    kBifrost: int
    kTestservice: int
    kStatsService: int
    kAgentinstall: int
    kMetadataService: int
    kWorkqueueServer: int
    kElasticsearchService: int
    kAxon: int
    kMagnus: int
    kShelteredHarbor: int
    kCoreDNS: int
    kMetricServer: int
    kInfraOperator: int
    kMarketplaceOperator: int
    kSpireApp: int
    kSFTPUIApp: int
    def __init__(self, kBifrost: _Optional[int] = ..., kTestservice: _Optional[int] = ..., kStatsService: _Optional[int] = ..., kAgentinstall: _Optional[int] = ..., kMetadataService: _Optional[int] = ..., kWorkqueueServer: _Optional[int] = ..., kElasticsearchService: _Optional[int] = ..., kAxon: _Optional[int] = ..., kMagnus: _Optional[int] = ..., kShelteredHarbor: _Optional[int] = ..., kCoreDNS: _Optional[int] = ..., kMetricServer: _Optional[int] = ..., kInfraOperator: _Optional[int] = ..., kMarketplaceOperator: _Optional[int] = ..., kSpireApp: _Optional[int] = ..., kSFTPUIApp: _Optional[int] = ...) -> None: ...

class SystemServiceInfoProto(_message.Message):
    __slots__ = ("service_name", "app_uid", "qos", "max_replicas", "min_replicas", "cpu_millicore", "memory_mb", "enabled", "required_services", "resource_pool")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    CPU_MILLICORE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    app_uid: int
    qos: str
    max_replicas: str
    min_replicas: str
    cpu_millicore: int
    memory_mb: int
    enabled: bool
    required_services: _containers.RepeatedScalarFieldContainer[str]
    resource_pool: ResourcePool
    def __init__(self, service_name: _Optional[str] = ..., app_uid: _Optional[int] = ..., qos: _Optional[str] = ..., max_replicas: _Optional[str] = ..., min_replicas: _Optional[str] = ..., cpu_millicore: _Optional[int] = ..., memory_mb: _Optional[int] = ..., enabled: bool = ..., required_services: _Optional[_Iterable[str]] = ..., resource_pool: _Optional[_Union[ResourcePool, str]] = ...) -> None: ...

class SystemServiceProtoVec(_message.Message):
    __slots__ = ("system_services", "version", "system_service_enabled")
    SYSTEM_SERVICES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SERVICE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    system_services: _containers.RepeatedCompositeFieldContainer[SystemServiceInfoProto]
    version: int
    system_service_enabled: bool
    def __init__(self, system_services: _Optional[_Iterable[_Union[SystemServiceInfoProto, _Mapping]]] = ..., version: _Optional[int] = ..., system_service_enabled: bool = ...) -> None: ...

class DockerCatalogProto(_message.Message):
    __slots__ = ("repositories",)
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, repositories: _Optional[_Iterable[str]] = ...) -> None: ...

class DockerTagsListProto(_message.Message):
    __slots__ = ("name", "tags")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
