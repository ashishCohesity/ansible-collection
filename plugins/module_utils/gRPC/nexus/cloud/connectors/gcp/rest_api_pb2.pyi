from nexus.cloud.connectors.gcp import gcp_entities_pb2 as _gcp_entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[LifecycleState]
    ACTIVE: _ClassVar[LifecycleState]
    DELETE_REQUESTED: _ClassVar[LifecycleState]
    DELETE_IN_PROGRESS: _ClassVar[LifecycleState]
LIFECYCLE_STATE_UNSPECIFIED: LifecycleState
ACTIVE: LifecycleState
DELETE_REQUESTED: LifecycleState
DELETE_IN_PROGRESS: LifecycleState

class VMInfo(_message.Message):
    __slots__ = ("id", "name", "description", "status", "status_message", "zone", "machine_type", "network_interfaces", "metadata", "disks", "tags", "scheduling", "service_accounts", "labels_map", "deletion_protection", "can_ip_forward")
    class NetworkInterface(_message.Message):
        __slots__ = ("network_ip", "name", "network", "subnetwork", "access_configs")
        class AccessConfigs(_message.Message):
            __slots__ = ("type", "name", "nat_ip", "network_tier")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            NAT_IP_FIELD_NUMBER: _ClassVar[int]
            NETWORK_TIER_FIELD_NUMBER: _ClassVar[int]
            type: str
            name: str
            nat_ip: str
            network_tier: str
            def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., nat_ip: _Optional[str] = ..., network_tier: _Optional[str] = ...) -> None: ...
        NETWORK_IP_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        ACCESS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        network_ip: str
        name: str
        network: str
        subnetwork: str
        access_configs: _containers.RepeatedCompositeFieldContainer[VMInfo.NetworkInterface.AccessConfigs]
        def __init__(self, network_ip: _Optional[str] = ..., name: _Optional[str] = ..., network: _Optional[str] = ..., subnetwork: _Optional[str] = ..., access_configs: _Optional[_Iterable[_Union[VMInfo.NetworkInterface.AccessConfigs, _Mapping]]] = ...) -> None: ...
    class Metadata(_message.Message):
        __slots__ = ("fingerprint", "items")
        class KeyValue(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        fingerprint: str
        items: _containers.RepeatedCompositeFieldContainer[VMInfo.Metadata.KeyValue]
        def __init__(self, fingerprint: _Optional[str] = ..., items: _Optional[_Iterable[_Union[VMInfo.Metadata.KeyValue, _Mapping]]] = ...) -> None: ...
    class Disks(_message.Message):
        __slots__ = ("device_name", "description", "is_bootable", "mode", "status", "source", "auto_delete", "interface", "type", "licenses", "guest_os_features", "disk_encryption_key", "labels_map", "disk_size_gb", "id")
        class GuestOsFeatures(_message.Message):
            __slots__ = ("type",)
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: str
            def __init__(self, type: _Optional[str] = ...) -> None: ...
        class DiskEncryptionKey(_message.Message):
            __slots__ = ("kms_key_name",)
            KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
            kms_key_name: str
            def __init__(self, kms_key_name: _Optional[str] = ...) -> None: ...
        class LabelsMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        LICENSES_FIELD_NUMBER: _ClassVar[int]
        GUEST_OS_FEATURES_FIELD_NUMBER: _ClassVar[int]
        DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
        LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        device_name: str
        description: str
        is_bootable: bool
        mode: str
        status: str
        source: str
        auto_delete: bool
        interface: str
        type: str
        licenses: _containers.RepeatedScalarFieldContainer[str]
        guest_os_features: _containers.RepeatedCompositeFieldContainer[VMInfo.Disks.GuestOsFeatures]
        disk_encryption_key: VMInfo.Disks.DiskEncryptionKey
        labels_map: _containers.ScalarMap[str, str]
        disk_size_gb: int
        id: int
        def __init__(self, device_name: _Optional[str] = ..., description: _Optional[str] = ..., is_bootable: bool = ..., mode: _Optional[str] = ..., status: _Optional[str] = ..., source: _Optional[str] = ..., auto_delete: bool = ..., interface: _Optional[str] = ..., type: _Optional[str] = ..., licenses: _Optional[_Iterable[str]] = ..., guest_os_features: _Optional[_Iterable[_Union[VMInfo.Disks.GuestOsFeatures, _Mapping]]] = ..., disk_encryption_key: _Optional[_Union[VMInfo.Disks.DiskEncryptionKey, _Mapping]] = ..., labels_map: _Optional[_Mapping[str, str]] = ..., disk_size_gb: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...
    class Tags(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, items: _Optional[_Iterable[str]] = ...) -> None: ...
    class Scheduling(_message.Message):
        __slots__ = ("automatic_restart", "on_host_maintenance", "preemptible")
        AUTOMATIC_RESTART_FIELD_NUMBER: _ClassVar[int]
        ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
        PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
        automatic_restart: bool
        on_host_maintenance: str
        preemptible: bool
        def __init__(self, automatic_restart: bool = ..., on_host_maintenance: _Optional[str] = ..., preemptible: bool = ...) -> None: ...
    class ServiceAccount(_message.Message):
        __slots__ = ("email", "scopes")
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        SCOPES_FIELD_NUMBER: _ClassVar[int]
        email: str
        scopes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, email: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ...) -> None: ...
    class LabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    status: str
    status_message: str
    zone: str
    machine_type: str
    network_interfaces: _containers.RepeatedCompositeFieldContainer[VMInfo.NetworkInterface]
    metadata: VMInfo.Metadata
    disks: _containers.RepeatedCompositeFieldContainer[VMInfo.Disks]
    tags: VMInfo.Tags
    scheduling: VMInfo.Scheduling
    service_accounts: _containers.RepeatedCompositeFieldContainer[VMInfo.ServiceAccount]
    labels_map: _containers.ScalarMap[str, str]
    deletion_protection: bool
    can_ip_forward: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., status_message: _Optional[str] = ..., zone: _Optional[str] = ..., machine_type: _Optional[str] = ..., network_interfaces: _Optional[_Iterable[_Union[VMInfo.NetworkInterface, _Mapping]]] = ..., metadata: _Optional[_Union[VMInfo.Metadata, _Mapping]] = ..., disks: _Optional[_Iterable[_Union[VMInfo.Disks, _Mapping]]] = ..., tags: _Optional[_Union[VMInfo.Tags, _Mapping]] = ..., scheduling: _Optional[_Union[VMInfo.Scheduling, _Mapping]] = ..., service_accounts: _Optional[_Iterable[_Union[VMInfo.ServiceAccount, _Mapping]]] = ..., labels_map: _Optional[_Mapping[str, str]] = ..., deletion_protection: bool = ..., can_ip_forward: bool = ...) -> None: ...

class ListVirtualMachinesResult(_message.Message):
    __slots__ = ("id", "items", "next_page_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[VMInfo]
    next_page_token: str
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[VMInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListImagesResult(_message.Message):
    __slots__ = ("id", "items", "next_page_token")
    class Resource(_message.Message):
        __slots__ = ("id", "name", "description", "status", "source_type", "creation_timestamp")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        description: str
        status: str
        source_type: str
        creation_timestamp: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., source_type: _Optional[str] = ..., creation_timestamp: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[ListImagesResult.Resource]
    next_page_token: str
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ListImagesResult.Resource, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListDisksResult(_message.Message):
    __slots__ = ("id", "items", "next_page_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[_gcp_entities_pb2.DiskInfo]
    next_page_token: str
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_gcp_entities_pb2.DiskInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSubnetInfoResult(_message.Message):
    __slots__ = ("id", "name", "gateway_address", "ip_cidr_range", "network")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    gateway_address: str
    ip_cidr_range: str
    network: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., gateway_address: _Optional[str] = ..., ip_cidr_range: _Optional[str] = ..., network: _Optional[str] = ...) -> None: ...

class GetVpcInfoResult(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class IpAddress(_message.Message):
    __slots__ = ("address", "users")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    address: str
    users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, address: _Optional[str] = ..., users: _Optional[_Iterable[str]] = ...) -> None: ...

class RegionInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRegionsResult(_message.Message):
    __slots__ = ("id", "items", "next_page_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[RegionInfo]
    next_page_token: str
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[RegionInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListSubnetsResult(_message.Message):
    __slots__ = ("items", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GetSubnetInfoResult]
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[GetSubnetInfoResult, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListVpcResult(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GetVpcInfoResult]
    def __init__(self, items: _Optional[_Iterable[_Union[GetVpcInfoResult, _Mapping]]] = ...) -> None: ...

class ListIpAddressesResult(_message.Message):
    __slots__ = ("items", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[IpAddress]
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[IpAddress, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ZoneInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListZonesResult(_message.Message):
    __slots__ = ("id", "items", "next_page_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[ZoneInfo]
    next_page_token: str
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ZoneInfo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CommonInstanceMetadata(_message.Message):
    __slots__ = ("fingerprint", "items")
    class KeyValue(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    items: _containers.RepeatedCompositeFieldContainer[CommonInstanceMetadata.KeyValue]
    def __init__(self, fingerprint: _Optional[str] = ..., items: _Optional[_Iterable[_Union[CommonInstanceMetadata.KeyValue, _Mapping]]] = ...) -> None: ...

class ProjectInfo(_message.Message):
    __slots__ = ("id", "name", "default_service_account", "common_instance_metadata")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    COMMON_INSTANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    default_service_account: str
    common_instance_metadata: CommonInstanceMetadata
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., default_service_account: _Optional[str] = ..., common_instance_metadata: _Optional[_Union[CommonInstanceMetadata, _Mapping]] = ...) -> None: ...

class ProjectMetadata(_message.Message):
    __slots__ = ("project_id", "labels_map", "lifecycle_state")
    class LabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    labels_map: _containers.ScalarMap[str, str]
    lifecycle_state: LifecycleState
    def __init__(self, project_id: _Optional[str] = ..., labels_map: _Optional[_Mapping[str, str]] = ..., lifecycle_state: _Optional[_Union[LifecycleState, str]] = ...) -> None: ...

class ListProjectsResult(_message.Message):
    __slots__ = ("projects", "next_page_token")
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[ProjectMetadata]
    next_page_token: str
    def __init__(self, projects: _Optional[_Iterable[_Union[ProjectMetadata, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("id", "name", "description", "status", "source_disk", "labels_map", "disk_size_gb")
    class LabelsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DISK_FIELD_NUMBER: _ClassVar[int]
    LABELS_MAP_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    status: str
    source_disk: str
    labels_map: _containers.ScalarMap[str, str]
    disk_size_gb: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., source_disk: _Optional[str] = ..., labels_map: _Optional[_Mapping[str, str]] = ..., disk_size_gb: _Optional[int] = ...) -> None: ...

class VpcNetworkInfo(_message.Message):
    __slots__ = ("name", "subnetworks")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    subnetworks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., subnetworks: _Optional[_Iterable[str]] = ...) -> None: ...

class GetHostProjectResult(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SharedSubnetInfoResult(_message.Message):
    __slots__ = ("subnetwork", "network", "ip_cidr_range")
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    subnetwork: str
    network: str
    ip_cidr_range: str
    def __init__(self, subnetwork: _Optional[str] = ..., network: _Optional[str] = ..., ip_cidr_range: _Optional[str] = ...) -> None: ...

class ListUsableSubnetsResult(_message.Message):
    __slots__ = ("items", "next_page_token")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SharedSubnetInfoResult]
    next_page_token: str
    def __init__(self, items: _Optional[_Iterable[_Union[SharedSubnetInfoResult, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ListServerlessVPCLocationsResult(_message.Message):
    __slots__ = ("locations", "next_page_token")
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.RepeatedCompositeFieldContainer[Location]
    next_page_token: str
    def __init__(self, locations: _Optional[_Iterable[_Union[Location, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class VPCConnector(_message.Message):
    __slots__ = ("name", "network", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    network: str
    state: str
    def __init__(self, name: _Optional[str] = ..., network: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class ListVPCConnectorsResult(_message.Message):
    __slots__ = ("connectors", "next_page_token")
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connectors: _containers.RepeatedCompositeFieldContainer[VPCConnector]
    next_page_token: str
    def __init__(self, connectors: _Optional[_Iterable[_Union[VPCConnector, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CloudFunctionResponseBody(_message.Message):
    __slots__ = ("status_message", "response")
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    status_message: str
    response: str
    def __init__(self, status_message: _Optional[str] = ..., response: _Optional[str] = ...) -> None: ...

class HttpsTrigger(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CloudFunction(_message.Message):
    __slots__ = ("name", "status", "vpc_connector", "https_trigger")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    HTTPS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: str
    vpc_connector: str
    https_trigger: HttpsTrigger
    def __init__(self, name: _Optional[str] = ..., status: _Optional[str] = ..., vpc_connector: _Optional[str] = ..., https_trigger: _Optional[_Union[HttpsTrigger, _Mapping]] = ...) -> None: ...

class HttpsError(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class OperationStatusError(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[HttpsError]
    def __init__(self, errors: _Optional[_Iterable[_Union[HttpsError, _Mapping]]] = ...) -> None: ...

class GetOperationStatusResult(_message.Message):
    __slots__ = ("status", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: str
    error: OperationStatusError
    def __init__(self, status: _Optional[str] = ..., error: _Optional[_Union[OperationStatusError, _Mapping]] = ...) -> None: ...
