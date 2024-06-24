from heimdall.master.base import master_pb2 as _master_pb2
from heimdall.master.stub import rpc_service_pb2 as _rpc_service_pb2
from nexus.cloud.connectors.azure import rest_api_pb2 as _rest_api_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskSkuTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPremium: _ClassVar[DiskSkuTier]
    kStandard: _ClassVar[DiskSkuTier]
    kUltra: _ClassVar[DiskSkuTier]

class DiskSkuName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPremium_LRS: _ClassVar[DiskSkuName]
    kPremiumV2_LRS: _ClassVar[DiskSkuName]
    kPremium_ZRS: _ClassVar[DiskSkuName]
    kStandardSSD_LRS: _ClassVar[DiskSkuName]
    kStandardSSD_ZRS: _ClassVar[DiskSkuName]
    kStandard_LRS: _ClassVar[DiskSkuName]
    kUltraSSD_LRS: _ClassVar[DiskSkuName]
kPremium: DiskSkuTier
kStandard: DiskSkuTier
kUltra: DiskSkuTier
kPremium_LRS: DiskSkuName
kPremiumV2_LRS: DiskSkuName
kPremium_ZRS: DiskSkuName
kStandardSSD_LRS: DiskSkuName
kStandardSSD_ZRS: DiskSkuName
kStandard_LRS: DiskSkuName
kUltraSSD_LRS: DiskSkuName

class AzureAcquireDisksArg(_message.Message):
    __slots__ = ("disk_name", "subscription_id", "resource_group_name", "size_bytes", "logical_sector_size", "region", "tags", "sku_name", "sku_tier", "vm_id", "fs", "partition_type", "number_of_disks")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AZURE_ACQUIRE_DISKS_ARG_FIELD_NUMBER: _ClassVar[int]
    azure_acquire_disks_arg: _descriptor.FieldDescriptor
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SKU_NAME_FIELD_NUMBER: _ClassVar[int]
    SKU_TIER_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    FS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_DISKS_FIELD_NUMBER: _ClassVar[int]
    disk_name: str
    subscription_id: str
    resource_group_name: str
    size_bytes: int
    logical_sector_size: int
    region: str
    tags: _containers.ScalarMap[str, str]
    sku_name: DiskSkuName
    sku_tier: DiskSkuTier
    vm_id: str
    fs: _master_pb2.FileSystemType
    partition_type: _master_pb2.DiskPartitionType
    number_of_disks: int
    def __init__(self, disk_name: _Optional[str] = ..., subscription_id: _Optional[str] = ..., resource_group_name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., logical_sector_size: _Optional[int] = ..., region: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., sku_name: _Optional[_Union[DiskSkuName, str]] = ..., sku_tier: _Optional[_Union[DiskSkuTier, str]] = ..., vm_id: _Optional[str] = ..., fs: _Optional[_Union[_master_pb2.FileSystemType, str]] = ..., partition_type: _Optional[_Union[_master_pb2.DiskPartitionType, str]] = ..., number_of_disks: _Optional[int] = ...) -> None: ...

class AzureDisksInfo(_message.Message):
    __slots__ = ("region", "tags", "subscription_id", "resource_group_name", "vm_id", "mount_point", "sku_name", "sku_tier", "fs", "partition_type")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AZURE_DISKS_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_disks_info: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    SKU_NAME_FIELD_NUMBER: _ClassVar[int]
    SKU_TIER_FIELD_NUMBER: _ClassVar[int]
    FS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    region: str
    tags: _containers.ScalarMap[str, str]
    subscription_id: str
    resource_group_name: str
    vm_id: str
    mount_point: str
    sku_name: DiskSkuName
    sku_tier: DiskSkuTier
    fs: _master_pb2.FileSystemType
    partition_type: _master_pb2.DiskPartitionType
    def __init__(self, region: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., subscription_id: _Optional[str] = ..., resource_group_name: _Optional[str] = ..., vm_id: _Optional[str] = ..., mount_point: _Optional[str] = ..., sku_name: _Optional[_Union[DiskSkuName, str]] = ..., sku_tier: _Optional[_Union[DiskSkuTier, str]] = ..., fs: _Optional[_Union[_master_pb2.FileSystemType, str]] = ..., partition_type: _Optional[_Union[_master_pb2.DiskPartitionType, str]] = ...) -> None: ...

class AzureAcquireDisksResult(_message.Message):
    __slots__ = ("disk_info_vec", "mount_point")
    class DiskInfo(_message.Message):
        __slots__ = ("disk_id", "device_name")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        disk_id: str
        device_name: str
        def __init__(self, disk_id: _Optional[str] = ..., device_name: _Optional[str] = ...) -> None: ...
    AZURE_ACQUIRE_DISKS_RESULT_FIELD_NUMBER: _ClassVar[int]
    azure_acquire_disks_result: _descriptor.FieldDescriptor
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[AzureAcquireDisksResult.DiskInfo]
    mount_point: str
    def __init__(self, disk_info_vec: _Optional[_Iterable[_Union[AzureAcquireDisksResult.DiskInfo, _Mapping]]] = ..., mount_point: _Optional[str] = ...) -> None: ...

class AzureAcquireDiskAccessArg(_message.Message):
    __slots__ = ("region", "vpn_id", "subnet", "tags", "resource_group_name", "add_dns_to_etc_hosts", "subscription_id")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AZURE_ACQUIRE_DISK_ACCESS_ARG_FIELD_NUMBER: _ClassVar[int]
    azure_acquire_disk_access_arg: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPN_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_DNS_TO_ETC_HOSTS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    region: str
    vpn_id: str
    subnet: str
    tags: _containers.ScalarMap[str, str]
    resource_group_name: str
    add_dns_to_etc_hosts: bool
    subscription_id: str
    def __init__(self, region: _Optional[str] = ..., vpn_id: _Optional[str] = ..., subnet: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., resource_group_name: _Optional[str] = ..., add_dns_to_etc_hosts: bool = ..., subscription_id: _Optional[str] = ...) -> None: ...

class AzureDiskAccessInfo(_message.Message):
    __slots__ = ("region", "vpn_id", "subnet", "tags", "resource_group_name", "add_dns_to_etc_hosts", "subscription_id", "subnet_resource_group")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AZURE_DISK_ACCESS_INFO_FIELD_NUMBER: _ClassVar[int]
    azure_disk_access_info: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPN_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_DNS_TO_ETC_HOSTS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    region: str
    vpn_id: str
    subnet: str
    tags: _containers.ScalarMap[str, str]
    resource_group_name: str
    add_dns_to_etc_hosts: bool
    subscription_id: str
    subnet_resource_group: str
    def __init__(self, region: _Optional[str] = ..., vpn_id: _Optional[str] = ..., subnet: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., resource_group_name: _Optional[str] = ..., add_dns_to_etc_hosts: bool = ..., subscription_id: _Optional[str] = ..., subnet_resource_group: _Optional[str] = ...) -> None: ...

class AzureAcquireDiskAccessResult(_message.Message):
    __slots__ = ("disk_access_id", "private_endpoint_id", "private_endpoint_fqdn", "private_endpoint_ipv4_address")
    AZURE_ACQUIRE_DISK_ACCESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    azure_acquire_disk_access_result: _descriptor.FieldDescriptor
    DISK_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FQDN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    disk_access_id: str
    private_endpoint_id: str
    private_endpoint_fqdn: str
    private_endpoint_ipv4_address: str
    def __init__(self, disk_access_id: _Optional[str] = ..., private_endpoint_id: _Optional[str] = ..., private_endpoint_fqdn: _Optional[str] = ..., private_endpoint_ipv4_address: _Optional[str] = ...) -> None: ...
