from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.base.entities import cloud_pb2 as _cloud_pb2
from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AzureDisk(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPremium_LRS: _ClassVar[AzureDisk.Type]
        kPremiumV2_LRS: _ClassVar[AzureDisk.Type]
        kPremium_ZRS: _ClassVar[AzureDisk.Type]
        kStandardSSD_LRS: _ClassVar[AzureDisk.Type]
        kStandardSSD_ZRS: _ClassVar[AzureDisk.Type]
        kStandard_LRS: _ClassVar[AzureDisk.Type]
        kUltraSSD_LRS: _ClassVar[AzureDisk.Type]
    kPremium_LRS: AzureDisk.Type
    kPremiumV2_LRS: AzureDisk.Type
    kPremium_ZRS: AzureDisk.Type
    kStandardSSD_LRS: AzureDisk.Type
    kStandardSSD_ZRS: AzureDisk.Type
    kStandard_LRS: AzureDisk.Type
    kUltraSSD_LRS: AzureDisk.Type
    def __init__(self) -> None: ...

class TagAttributes(_message.Message):
    __slots__ = ("entity_id", "uuid", "name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    uuid: str
    name: str
    def __init__(self, entity_id: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AzureSnapshotProps(_message.Message):
    __slots__ = ("compression",)
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    compression: Entity.CompressionOption
    def __init__(self, compression: _Optional[_Union[Entity.CompressionOption, str]] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "location", "num_cores", "memory_mb", "max_no_of_data_disks_supported", "host_type", "private_ip_address_vec", "common_info", "tag_attributes_vec", "version", "state", "fqdn", "public_network_access", "collation", "max_size_bytes", "status", "creation_date", "administrator_login", "is_top_level_entity", "current_size_bytes", "sku", "private_endpoint_connection_vec", "front_end_size_info", "is_managed_db", "name", "id", "is_managed_vm")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSubscription: _ClassVar[Entity.Type]
        kResourceGroup: _ClassVar[Entity.Type]
        kVirtualMachine: _ClassVar[Entity.Type]
        kStorageAccount: _ClassVar[Entity.Type]
        kStorageKey: _ClassVar[Entity.Type]
        kStorageContainer: _ClassVar[Entity.Type]
        kStorageBlob: _ClassVar[Entity.Type]
        kNetworkSecurityGroup: _ClassVar[Entity.Type]
        kVirtualNetwork: _ClassVar[Entity.Type]
        kSubnet: _ClassVar[Entity.Type]
        kComputeOptions: _ClassVar[Entity.Type]
        kSnapshotManagerPermit: _ClassVar[Entity.Type]
        kTag: _ClassVar[Entity.Type]
        kAvailabilitySet: _ClassVar[Entity.Type]
        kSQLServer: _ClassVar[Entity.Type]
        kSQLManagedInstance: _ClassVar[Entity.Type]
        kSQLDatabase: _ClassVar[Entity.Type]
        kTenant: _ClassVar[Entity.Type]
        kRegion: _ClassVar[Entity.Type]
        kSQLServerPermit: _ClassVar[Entity.Type]
        kSQLManagedInstancePermit: _ClassVar[Entity.Type]
        kSQLResourceGroupPermit: _ClassVar[Entity.Type]
        kSQLSubscriptionPermit: _ClassVar[Entity.Type]
        kSQLTenantPermit: _ClassVar[Entity.Type]
        kAzureVMNativePermit: _ClassVar[Entity.Type]
        kApplicationSecurityGroup: _ClassVar[Entity.Type]
        kSQLServerRestorePermit: _ClassVar[Entity.Type]
        kSQLManagedInstanceRestorePermit: _ClassVar[Entity.Type]
    kSubscription: Entity.Type
    kResourceGroup: Entity.Type
    kVirtualMachine: Entity.Type
    kStorageAccount: Entity.Type
    kStorageKey: Entity.Type
    kStorageContainer: Entity.Type
    kStorageBlob: Entity.Type
    kNetworkSecurityGroup: Entity.Type
    kVirtualNetwork: Entity.Type
    kSubnet: Entity.Type
    kComputeOptions: Entity.Type
    kSnapshotManagerPermit: Entity.Type
    kTag: Entity.Type
    kAvailabilitySet: Entity.Type
    kSQLServer: Entity.Type
    kSQLManagedInstance: Entity.Type
    kSQLDatabase: Entity.Type
    kTenant: Entity.Type
    kRegion: Entity.Type
    kSQLServerPermit: Entity.Type
    kSQLManagedInstancePermit: Entity.Type
    kSQLResourceGroupPermit: Entity.Type
    kSQLSubscriptionPermit: Entity.Type
    kSQLTenantPermit: Entity.Type
    kAzureVMNativePermit: Entity.Type
    kApplicationSecurityGroup: Entity.Type
    kSQLServerRestorePermit: Entity.Type
    kSQLManagedInstanceRestorePermit: Entity.Type
    class CompressionOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNormal: _ClassVar[Entity.CompressionOption]
        kMaximum: _ClassVar[Entity.CompressionOption]
        kFast: _ClassVar[Entity.CompressionOption]
        kSuperFast: _ClassVar[Entity.CompressionOption]
        kNotCompressed: _ClassVar[Entity.CompressionOption]
    kNormal: Entity.CompressionOption
    kMaximum: Entity.CompressionOption
    kFast: Entity.CompressionOption
    kSuperFast: Entity.CompressionOption
    kNotCompressed: Entity.CompressionOption
    class SKU(_message.Message):
        __slots__ = ("name", "tier", "capacity", "name_type", "tier_type")
        class Name(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kBasic: _ClassVar[Entity.SKU.Name.Type]
                kStandard: _ClassVar[Entity.SKU.Name.Type]
                kPremium: _ClassVar[Entity.SKU.Name.Type]
                kGeneralPurpose: _ClassVar[Entity.SKU.Name.Type]
                kBusinessCritical: _ClassVar[Entity.SKU.Name.Type]
                kHyperscale: _ClassVar[Entity.SKU.Name.Type]
                kDataWarehouse: _ClassVar[Entity.SKU.Name.Type]
                kStretch: _ClassVar[Entity.SKU.Name.Type]
            kBasic: Entity.SKU.Name.Type
            kStandard: Entity.SKU.Name.Type
            kPremium: Entity.SKU.Name.Type
            kGeneralPurpose: Entity.SKU.Name.Type
            kBusinessCritical: Entity.SKU.Name.Type
            kHyperscale: Entity.SKU.Name.Type
            kDataWarehouse: Entity.SKU.Name.Type
            kStretch: Entity.SKU.Name.Type
            def __init__(self) -> None: ...
        class Tier(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kFree: _ClassVar[Entity.SKU.Tier.Type]
                kBasic: _ClassVar[Entity.SKU.Tier.Type]
                kStandard: _ClassVar[Entity.SKU.Tier.Type]
                kPremium: _ClassVar[Entity.SKU.Tier.Type]
                kDataWarehouse: _ClassVar[Entity.SKU.Tier.Type]
                kStretch: _ClassVar[Entity.SKU.Tier.Type]
                kBC_DC: _ClassVar[Entity.SKU.Tier.Type]
                kBC_Gen5: _ClassVar[Entity.SKU.Tier.Type]
                kBC_M: _ClassVar[Entity.SKU.Tier.Type]
                kGP_DC: _ClassVar[Entity.SKU.Tier.Type]
                kGP_Fsv2: _ClassVar[Entity.SKU.Tier.Type]
                kGP_Gen5: _ClassVar[Entity.SKU.Tier.Type]
                kGP_S_Gen5: _ClassVar[Entity.SKU.Tier.Type]
                kHS_DC: _ClassVar[Entity.SKU.Tier.Type]
                kHS_Gen5: _ClassVar[Entity.SKU.Tier.Type]
                kHS_S_Gen5: _ClassVar[Entity.SKU.Tier.Type]
                kHS_MOPRMS: _ClassVar[Entity.SKU.Tier.Type]
                kHS_PRMS: _ClassVar[Entity.SKU.Tier.Type]
            kFree: Entity.SKU.Tier.Type
            kBasic: Entity.SKU.Tier.Type
            kStandard: Entity.SKU.Tier.Type
            kPremium: Entity.SKU.Tier.Type
            kDataWarehouse: Entity.SKU.Tier.Type
            kStretch: Entity.SKU.Tier.Type
            kBC_DC: Entity.SKU.Tier.Type
            kBC_Gen5: Entity.SKU.Tier.Type
            kBC_M: Entity.SKU.Tier.Type
            kGP_DC: Entity.SKU.Tier.Type
            kGP_Fsv2: Entity.SKU.Tier.Type
            kGP_Gen5: Entity.SKU.Tier.Type
            kGP_S_Gen5: Entity.SKU.Tier.Type
            kHS_DC: Entity.SKU.Tier.Type
            kHS_Gen5: Entity.SKU.Tier.Type
            kHS_S_Gen5: Entity.SKU.Tier.Type
            kHS_MOPRMS: Entity.SKU.Tier.Type
            kHS_PRMS: Entity.SKU.Tier.Type
            def __init__(self) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        TIER_FIELD_NUMBER: _ClassVar[int]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        NAME_TYPE_FIELD_NUMBER: _ClassVar[int]
        TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        tier: str
        capacity: int
        name_type: Entity.SKU.Name.Type
        tier_type: Entity.SKU.Tier.Type
        def __init__(self, name: _Optional[str] = ..., tier: _Optional[str] = ..., capacity: _Optional[int] = ..., name_type: _Optional[_Union[Entity.SKU.Name.Type, str]] = ..., tier_type: _Optional[_Union[Entity.SKU.Tier.Type, str]] = ...) -> None: ...
    class PrivateEndpointConnection(_message.Message):
        __slots__ = ("private_endpoint_id", "subnet_id")
        PRIVATE_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
        SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
        private_endpoint_id: str
        subnet_id: str
        def __init__(self, private_endpoint_id: _Optional[str] = ..., subnet_id: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    MAX_NO_OF_DATA_DISKS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_VEC_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_NETWORK_ACCESS_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATOR_LOGIN_FIELD_NUMBER: _ClassVar[int]
    IS_TOP_LEVEL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_CONNECTION_VEC_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_MANAGED_DB_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_MANAGED_VM_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    location: str
    num_cores: int
    memory_mb: int
    max_no_of_data_disks_supported: int
    host_type: _enums_pb2.HostEnv.Type
    private_ip_address_vec: _containers.RepeatedScalarFieldContainer[str]
    common_info: _cloud_pb2.EntityCommonInfo
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[TagAttributes]
    version: str
    state: str
    fqdn: str
    public_network_access: str
    collation: str
    max_size_bytes: int
    status: str
    creation_date: str
    administrator_login: str
    is_top_level_entity: bool
    current_size_bytes: int
    sku: Entity.SKU
    private_endpoint_connection_vec: _containers.RepeatedCompositeFieldContainer[Entity.PrivateEndpointConnection]
    front_end_size_info: _stats_pb2.SizeInfo
    is_managed_db: bool
    name: str
    id: str
    is_managed_vm: bool
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., location: _Optional[str] = ..., num_cores: _Optional[int] = ..., memory_mb: _Optional[int] = ..., max_no_of_data_disks_supported: _Optional[int] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., private_ip_address_vec: _Optional[_Iterable[str]] = ..., common_info: _Optional[_Union[_cloud_pb2.EntityCommonInfo, _Mapping]] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[TagAttributes, _Mapping]]] = ..., version: _Optional[str] = ..., state: _Optional[str] = ..., fqdn: _Optional[str] = ..., public_network_access: _Optional[str] = ..., collation: _Optional[str] = ..., max_size_bytes: _Optional[int] = ..., status: _Optional[str] = ..., creation_date: _Optional[str] = ..., administrator_login: _Optional[str] = ..., is_top_level_entity: bool = ..., current_size_bytes: _Optional[int] = ..., sku: _Optional[_Union[Entity.SKU, _Mapping]] = ..., private_endpoint_connection_vec: _Optional[_Iterable[_Union[Entity.PrivateEndpointConnection, _Mapping]]] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ..., is_managed_db: bool = ..., name: _Optional[str] = ..., id: _Optional[str] = ..., is_managed_vm: bool = ...) -> None: ...
