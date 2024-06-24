from magneto.base.entities import cloud_pb2 as _cloud_pb2
from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GCPAttributes(_message.Message):
    __slots__ = ("entity_id", "uuid", "name", "type", "key_DEPRECATED", "value_DEPRECATED")
    class TagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNetworkTag: _ClassVar[GCPAttributes.TagType]
        kLabel: _ClassVar[GCPAttributes.TagType]
        kCustomMetadata: _ClassVar[GCPAttributes.TagType]
    kNetworkTag: GCPAttributes.TagType
    kLabel: GCPAttributes.TagType
    kCustomMetadata: GCPAttributes.TagType
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    VALUE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    uuid: str
    name: str
    type: GCPAttributes.TagType
    key_DEPRECATED: str
    value_DEPRECATED: str
    def __init__(self, entity_id: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[GCPAttributes.TagType, str]] = ..., key_DEPRECATED: _Optional[str] = ..., value_DEPRECATED: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "owner_id", "iam_info", "common_info", "vpc_network", "vpc_subnetwork", "host_type", "private_ip_address", "region", "project_id", "zone", "allowed_project_id_vec", "tag_attributes_vec", "allowed_region_vec", "host_project_id", "gcp_fleet_params", "cluster_network_info", "disk_info_vec", "metadata_vec_DEPRECATED", "network_tag_vec_DEPRECATED")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIAMUser: _ClassVar[Entity.Type]
        kProject: _ClassVar[Entity.Type]
        kRegion: _ClassVar[Entity.Type]
        kAvailabilityZone: _ClassVar[Entity.Type]
        kVirtualMachine: _ClassVar[Entity.Type]
        kVPC: _ClassVar[Entity.Type]
        kSubnet: _ClassVar[Entity.Type]
        kNetworkSecurityGroup: _ClassVar[Entity.Type]
        kInstanceType: _ClassVar[Entity.Type]
        kLabel: _ClassVar[Entity.Type]
        kMetadata: _ClassVar[Entity.Type]
        kTag: _ClassVar[Entity.Type]
        kVPCConnector: _ClassVar[Entity.Type]
    kIAMUser: Entity.Type
    kProject: Entity.Type
    kRegion: Entity.Type
    kAvailabilityZone: Entity.Type
    kVirtualMachine: Entity.Type
    kVPC: Entity.Type
    kSubnet: Entity.Type
    kNetworkSecurityGroup: Entity.Type
    kInstanceType: Entity.Type
    kLabel: Entity.Type
    kMetadata: Entity.Type
    kTag: Entity.Type
    kVPCConnector: Entity.Type
    class IAMInfo(_message.Message):
        __slots__ = ("project_id", "client_email")
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_EMAIL_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        client_email: str
        def __init__(self, project_id: _Optional[str] = ..., client_email: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    IAM_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    VPC_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_PROJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_REGION_VEC_FIELD_NUMBER: _ClassVar[int]
    HOST_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    GCP_FLEET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAG_VEC_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    owner_id: str
    iam_info: Entity.IAMInfo
    common_info: _cloud_pb2.EntityCommonInfo
    vpc_network: str
    vpc_subnetwork: str
    host_type: _enums_pb2.HostEnv.Type
    private_ip_address: str
    region: str
    project_id: str
    zone: str
    allowed_project_id_vec: _containers.RepeatedScalarFieldContainer[str]
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[GCPAttributes]
    allowed_region_vec: _containers.RepeatedScalarFieldContainer[str]
    host_project_id: str
    gcp_fleet_params: GCPFleetParams
    cluster_network_info: FleetNetworkParams.NetworkParams
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[DiskInfo]
    metadata_vec_DEPRECATED: _containers.RepeatedCompositeFieldContainer[GCPAttributes]
    network_tag_vec_DEPRECATED: _containers.RepeatedCompositeFieldContainer[GCPAttributes]
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., owner_id: _Optional[str] = ..., iam_info: _Optional[_Union[Entity.IAMInfo, _Mapping]] = ..., common_info: _Optional[_Union[_cloud_pb2.EntityCommonInfo, _Mapping]] = ..., vpc_network: _Optional[str] = ..., vpc_subnetwork: _Optional[str] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., private_ip_address: _Optional[str] = ..., region: _Optional[str] = ..., project_id: _Optional[str] = ..., zone: _Optional[str] = ..., allowed_project_id_vec: _Optional[_Iterable[str]] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[GCPAttributes, _Mapping]]] = ..., allowed_region_vec: _Optional[_Iterable[str]] = ..., host_project_id: _Optional[str] = ..., gcp_fleet_params: _Optional[_Union[GCPFleetParams, _Mapping]] = ..., cluster_network_info: _Optional[_Union[FleetNetworkParams.NetworkParams, _Mapping]] = ..., disk_info_vec: _Optional[_Iterable[_Union[DiskInfo, _Mapping]]] = ..., metadata_vec_DEPRECATED: _Optional[_Iterable[_Union[GCPAttributes, _Mapping]]] = ..., network_tag_vec_DEPRECATED: _Optional[_Iterable[_Union[GCPAttributes, _Mapping]]] = ...) -> None: ...

class GCPFleetParams(_message.Message):
    __slots__ = ("kms_key_name", "fleet_nw_tag_vec", "service_account_name", "fleet_network_params_vec")
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    FLEET_NW_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    FLEET_NETWORK_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str
    fleet_nw_tag_vec: _containers.RepeatedScalarFieldContainer[str]
    service_account_name: str
    fleet_network_params_vec: _containers.RepeatedCompositeFieldContainer[FleetNetworkParams]
    def __init__(self, kms_key_name: _Optional[str] = ..., fleet_nw_tag_vec: _Optional[_Iterable[str]] = ..., service_account_name: _Optional[str] = ..., fleet_network_params_vec: _Optional[_Iterable[_Union[FleetNetworkParams, _Mapping]]] = ...) -> None: ...

class FleetNetworkParams(_message.Message):
    __slots__ = ("fleet_subnet_type", "network_params_vec", "fleet_subnet_priority")
    class FleetSubnetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[FleetNetworkParams.FleetSubnetType]
        kSourceVM: _ClassVar[FleetNetworkParams.FleetSubnetType]
        kCustom: _ClassVar[FleetNetworkParams.FleetSubnetType]
    kCluster: FleetNetworkParams.FleetSubnetType
    kSourceVM: FleetNetworkParams.FleetSubnetType
    kCustom: FleetNetworkParams.FleetSubnetType
    class FleetSubnetPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrimary: _ClassVar[FleetNetworkParams.FleetSubnetPriority]
        kSecondary: _ClassVar[FleetNetworkParams.FleetSubnetPriority]
        kTertiary: _ClassVar[FleetNetworkParams.FleetSubnetPriority]
    kPrimary: FleetNetworkParams.FleetSubnetPriority
    kSecondary: FleetNetworkParams.FleetSubnetPriority
    kTertiary: FleetNetworkParams.FleetSubnetPriority
    class NetworkParams(_message.Message):
        __slots__ = ("project_id", "vpc", "subnet", "zone", "region")
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        VPC_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        ZONE_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        vpc: str
        subnet: str
        zone: str
        region: str
        def __init__(self, project_id: _Optional[str] = ..., vpc: _Optional[str] = ..., subnet: _Optional[str] = ..., zone: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
    FLEET_SUBNET_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    FLEET_SUBNET_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    fleet_subnet_type: FleetNetworkParams.FleetSubnetType
    network_params_vec: _containers.RepeatedCompositeFieldContainer[FleetNetworkParams.NetworkParams]
    fleet_subnet_priority: FleetNetworkParams.FleetSubnetPriority
    def __init__(self, fleet_subnet_type: _Optional[_Union[FleetNetworkParams.FleetSubnetType, str]] = ..., network_params_vec: _Optional[_Iterable[_Union[FleetNetworkParams.NetworkParams, _Mapping]]] = ..., fleet_subnet_priority: _Optional[_Union[FleetNetworkParams.FleetSubnetPriority, str]] = ...) -> None: ...

class DiskInfo(_message.Message):
    __slots__ = ("disk_name", "device_name", "label_vec", "size_gb", "disk_type", "is_bootable", "id")
    class Label(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    disk_name: str
    device_name: str
    label_vec: _containers.RepeatedCompositeFieldContainer[DiskInfo.Label]
    size_gb: int
    disk_type: str
    is_bootable: bool
    id: int
    def __init__(self, disk_name: _Optional[str] = ..., device_name: _Optional[str] = ..., label_vec: _Optional[_Iterable[_Union[DiskInfo.Label, _Mapping]]] = ..., size_gb: _Optional[int] = ..., disk_type: _Optional[str] = ..., is_bootable: bool = ..., id: _Optional[int] = ...) -> None: ...
