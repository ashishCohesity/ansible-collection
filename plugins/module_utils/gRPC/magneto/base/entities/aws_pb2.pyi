from magneto.api.common import stats_pb2 as _stats_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import cloud_pb2 as _cloud_pb2
from magneto.base.entities import s3_pb2 as _s3_pb2
from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagAttributes(_message.Message):
    __slots__ = ("entity_id", "uuid", "name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    uuid: str
    name: str
    def __init__(self, entity_id: _Optional[int] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "owner_id", "iam_info", "common_info", "host_type", "private_ip_address", "region_id", "availability_zone", "tag_attributes_vec", "db_engine_id", "latest_db_restorable_time_msecs", "db_backup_retention_period_days", "aws_fleet_params", "cluster_network_info", "volume_info_vec", "front_end_size_info", "use_case", "s3_entity_info", "kms_key_info", "rds_db_connector_params", "s3_protection_params")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIAMUser: _ClassVar[Entity.Type]
        kRegion: _ClassVar[Entity.Type]
        kAvailabilityZone: _ClassVar[Entity.Type]
        kEC2Instance: _ClassVar[Entity.Type]
        kVPC: _ClassVar[Entity.Type]
        kSubnet: _ClassVar[Entity.Type]
        kNetworkSecurityGroup: _ClassVar[Entity.Type]
        kInstanceType: _ClassVar[Entity.Type]
        kKeyPair: _ClassVar[Entity.Type]
        kTag: _ClassVar[Entity.Type]
        kRDSOptionGroup: _ClassVar[Entity.Type]
        kRDSParameterGroup: _ClassVar[Entity.Type]
        kRDSInstance: _ClassVar[Entity.Type]
        kRDSSubnet: _ClassVar[Entity.Type]
        kRDSTag: _ClassVar[Entity.Type]
        kAuroraTag: _ClassVar[Entity.Type]
        kAccount: _ClassVar[Entity.Type]
        kAuroraCluster: _ClassVar[Entity.Type]
        kSubTaskPermit: _ClassVar[Entity.Type]
        kS3Bucket: _ClassVar[Entity.Type]
        kS3Tag: _ClassVar[Entity.Type]
        kKmsKey: _ClassVar[Entity.Type]
        kRDSPostgresDb: _ClassVar[Entity.Type]
        kAuroraClusterPostgresDb: _ClassVar[Entity.Type]
    kIAMUser: Entity.Type
    kRegion: Entity.Type
    kAvailabilityZone: Entity.Type
    kEC2Instance: Entity.Type
    kVPC: Entity.Type
    kSubnet: Entity.Type
    kNetworkSecurityGroup: Entity.Type
    kInstanceType: Entity.Type
    kKeyPair: Entity.Type
    kTag: Entity.Type
    kRDSOptionGroup: Entity.Type
    kRDSParameterGroup: Entity.Type
    kRDSInstance: Entity.Type
    kRDSSubnet: Entity.Type
    kRDSTag: Entity.Type
    kAuroraTag: Entity.Type
    kAccount: Entity.Type
    kAuroraCluster: Entity.Type
    kSubTaskPermit: Entity.Type
    kS3Bucket: Entity.Type
    kS3Tag: Entity.Type
    kKmsKey: Entity.Type
    kRDSPostgresDb: Entity.Type
    kAuroraClusterPostgresDb: Entity.Type
    class UseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEC2: _ClassVar[Entity.UseCase]
        kRDS: _ClassVar[Entity.UseCase]
        kSiteContinuity: _ClassVar[Entity.UseCase]
    kEC2: Entity.UseCase
    kRDS: Entity.UseCase
    kSiteContinuity: Entity.UseCase
    class IAMInfo(_message.Message):
        __slots__ = ("arn", "account_id")
        ARN_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        arn: str
        account_id: str
        def __init__(self, arn: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    IAM_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMON_INFO_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_DB_RESTORABLE_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DB_BACKUP_RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    AWS_FLEET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_CASE_FIELD_NUMBER: _ClassVar[int]
    S3_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    RDS_DB_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_PROTECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    owner_id: str
    iam_info: Entity.IAMInfo
    common_info: _cloud_pb2.EntityCommonInfo
    host_type: _enums_pb2.HostEnv.Type
    private_ip_address: str
    region_id: str
    availability_zone: str
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[TagAttributes]
    db_engine_id: str
    latest_db_restorable_time_msecs: int
    db_backup_retention_period_days: int
    aws_fleet_params: AWSFleetParams
    cluster_network_info: AWSFleetParams.NetworkParams
    volume_info_vec: _containers.RepeatedCompositeFieldContainer[EBSVolumeInfo]
    front_end_size_info: _stats_pb2.SizeInfo
    use_case: _containers.RepeatedScalarFieldContainer[Entity.UseCase]
    s3_entity_info: _s3_pb2.Entity
    kms_key_info: KmsKeyInfo
    rds_db_connector_params: RDSDbConnectorParams
    s3_protection_params: S3ProtectionParams
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., owner_id: _Optional[str] = ..., iam_info: _Optional[_Union[Entity.IAMInfo, _Mapping]] = ..., common_info: _Optional[_Union[_cloud_pb2.EntityCommonInfo, _Mapping]] = ..., host_type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ..., private_ip_address: _Optional[str] = ..., region_id: _Optional[str] = ..., availability_zone: _Optional[str] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[TagAttributes, _Mapping]]] = ..., db_engine_id: _Optional[str] = ..., latest_db_restorable_time_msecs: _Optional[int] = ..., db_backup_retention_period_days: _Optional[int] = ..., aws_fleet_params: _Optional[_Union[AWSFleetParams, _Mapping]] = ..., cluster_network_info: _Optional[_Union[AWSFleetParams.NetworkParams, _Mapping]] = ..., volume_info_vec: _Optional[_Iterable[_Union[EBSVolumeInfo, _Mapping]]] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ..., use_case: _Optional[_Iterable[_Union[Entity.UseCase, str]]] = ..., s3_entity_info: _Optional[_Union[_s3_pb2.Entity, _Mapping]] = ..., kms_key_info: _Optional[_Union[KmsKeyInfo, _Mapping]] = ..., rds_db_connector_params: _Optional[_Union[RDSDbConnectorParams, _Mapping]] = ..., s3_protection_params: _Optional[_Union[S3ProtectionParams, _Mapping]] = ...) -> None: ...

class AWSFleetParams(_message.Message):
    __slots__ = ("fleet_tag_vec", "fleet_subnet_type", "network_params", "network_params_map", "network_params_vec")
    class FleetSubnetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[AWSFleetParams.FleetSubnetType]
        kSourceVM: _ClassVar[AWSFleetParams.FleetSubnetType]
        kCustom: _ClassVar[AWSFleetParams.FleetSubnetType]
    kCluster: AWSFleetParams.FleetSubnetType
    kSourceVM: AWSFleetParams.FleetSubnetType
    kCustom: AWSFleetParams.FleetSubnetType
    class Tag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class NetworkParams(_message.Message):
        __slots__ = ("vpc", "subnet", "region")
        VPC_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        vpc: str
        subnet: str
        region: str
        def __init__(self, vpc: _Optional[str] = ..., subnet: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
    class NetworkParamsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AWSFleetParams.NetworkParams
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AWSFleetParams.NetworkParams, _Mapping]] = ...) -> None: ...
    FLEET_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    FLEET_SUBNET_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAMS_MAP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    fleet_tag_vec: _containers.RepeatedCompositeFieldContainer[AWSFleetParams.Tag]
    fleet_subnet_type: AWSFleetParams.FleetSubnetType
    network_params: AWSFleetParams.NetworkParams
    network_params_map: _containers.MessageMap[str, AWSFleetParams.NetworkParams]
    network_params_vec: _containers.RepeatedCompositeFieldContainer[AWSFleetParams.NetworkParams]
    def __init__(self, fleet_tag_vec: _Optional[_Iterable[_Union[AWSFleetParams.Tag, _Mapping]]] = ..., fleet_subnet_type: _Optional[_Union[AWSFleetParams.FleetSubnetType, str]] = ..., network_params: _Optional[_Union[AWSFleetParams.NetworkParams, _Mapping]] = ..., network_params_map: _Optional[_Mapping[str, AWSFleetParams.NetworkParams]] = ..., network_params_vec: _Optional[_Iterable[_Union[AWSFleetParams.NetworkParams, _Mapping]]] = ...) -> None: ...

class EBSVolumeInfo(_message.Message):
    __slots__ = ("id", "name", "size_bytes", "type", "device_name", "is_root_device", "tag_vec")
    class Tag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    size_bytes: int
    type: str
    device_name: str
    is_root_device: bool
    tag_vec: _containers.RepeatedCompositeFieldContainer[EBSVolumeInfo.Tag]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., type: _Optional[str] = ..., device_name: _Optional[str] = ..., is_root_device: bool = ..., tag_vec: _Optional[_Iterable[_Union[EBSVolumeInfo.Tag, _Mapping]]] = ...) -> None: ...

class KmsKeyInfo(_message.Message):
    __slots__ = ("arn", "alias", "enabled")
    ARN_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    arn: str
    alias: str
    enabled: bool
    def __init__(self, arn: _Optional[str] = ..., alias: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class RDSDbConnectorParams(_message.Message):
    __slots__ = ("endpoint", "port", "default_db")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DB_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    port: int
    default_db: str
    def __init__(self, endpoint: _Optional[str] = ..., port: _Optional[int] = ..., default_db: _Optional[str] = ...) -> None: ...

class S3ProtectionParams(_message.Message):
    __slots__ = ("s3_inventory_report_destination_bucket", "s3_inventory_report_destination_bucket_prefix")
    S3_INVENTORY_REPORT_DESTINATION_BUCKET_FIELD_NUMBER: _ClassVar[int]
    S3_INVENTORY_REPORT_DESTINATION_BUCKET_PREFIX_FIELD_NUMBER: _ClassVar[int]
    s3_inventory_report_destination_bucket: str
    s3_inventory_report_destination_bucket_prefix: str
    def __init__(self, s3_inventory_report_destination_bucket: _Optional[str] = ..., s3_inventory_report_destination_bucket_prefix: _Optional[str] = ...) -> None: ...
