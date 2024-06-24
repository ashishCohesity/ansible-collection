from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DBClusterMember(_message.Message):
    __slots__ = ("db_instance_identfier", "is_writer", "promotion_tier")
    DB_INSTANCE_IDENTFIER_FIELD_NUMBER: _ClassVar[int]
    IS_WRITER_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_TIER_FIELD_NUMBER: _ClassVar[int]
    db_instance_identfier: str
    is_writer: bool
    promotion_tier: int
    def __init__(self, db_instance_identfier: _Optional[str] = ..., is_writer: bool = ..., promotion_tier: _Optional[int] = ...) -> None: ...

class ServerlessV2ScalingConfigurationInfo(_message.Message):
    __slots__ = ("min_capacity", "max_capacity")
    MIN_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MAX_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    min_capacity: float
    max_capacity: float
    def __init__(self, min_capacity: _Optional[float] = ..., max_capacity: _Optional[float] = ...) -> None: ...

class ScalingConfigurationInfo(_message.Message):
    __slots__ = ("min_capacity", "max_capacity", "auto_pause", "seconds_until_auto_pause", "timeout_action", "seconds_before_timeout")
    MIN_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MAX_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    AUTO_PAUSE_FIELD_NUMBER: _ClassVar[int]
    SECONDS_UNTIL_AUTO_PAUSE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_ACTION_FIELD_NUMBER: _ClassVar[int]
    SECONDS_BEFORE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    min_capacity: int
    max_capacity: int
    auto_pause: bool
    seconds_until_auto_pause: int
    timeout_action: str
    seconds_before_timeout: int
    def __init__(self, min_capacity: _Optional[int] = ..., max_capacity: _Optional[int] = ..., auto_pause: bool = ..., seconds_until_auto_pause: _Optional[int] = ..., timeout_action: _Optional[str] = ..., seconds_before_timeout: _Optional[int] = ...) -> None: ...

class DBInfo(_message.Message):
    __slots__ = ("region_name", "db_cluster_identifier", "db_instance_arn", "db_instance_id", "db_instance_port", "db_engine_name", "db_engine_version", "master_username", "db_instance_class", "storage_type", "num_iops", "storage_size_bytes", "db_instance_status", "iam_db_authentication", "kms_key_id", "license_model", "multi_az_deployment", "availability_zone", "secondary_availability_zone", "auto_minor_version_upgrade", "backup_retention_period_days", "preferred_backup_window", "preferred_maintenance_window", "ca_certificate_identifier", "charset_name", "deletion_protection", "read_replica_cluster_id_vec", "read_replica_db_id_vec", "read_replica_source_db_id", "db_name", "latest_restorable_time_msecs", "db_parameter_group", "db_option_group", "db_subnet", "copy_tags_to_snapshots", "public_accessibility", "vpc_security_group_vec", "db_tag_vec", "db_cluster_arn", "db_cluster_member_count", "db_cluster_members", "db_endpoint", "serverless_v2_scaling_configuration_info", "scaling_configuration_info")
    class Endpoint(_message.Message):
        __slots__ = ("dns_address", "port", "hosted_zone_id")
        DNS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        HOSTED_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        dns_address: str
        port: int
        hosted_zone_id: str
        def __init__(self, dns_address: _Optional[str] = ..., port: _Optional[int] = ..., hosted_zone_id: _Optional[str] = ...) -> None: ...
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_ARN_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_PORT_FIELD_NUMBER: _ClassVar[int]
    DB_ENGINE_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    MASTER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_CLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_IOPS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    IAM_DB_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    LICENSE_MODEL_FIELD_NUMBER: _ClassVar[int]
    MULTI_AZ_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    AUTO_MINOR_VERSION_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_BACKUP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CHARSET_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    READ_REPLICA_CLUSTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    READ_REPLICA_DB_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    READ_REPLICA_SOURCE_DB_ID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    LATEST_RESTORABLE_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    DB_PARAMETER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DB_OPTION_GROUP_FIELD_NUMBER: _ClassVar[int]
    DB_SUBNET_FIELD_NUMBER: _ClassVar[int]
    COPY_TAGS_TO_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    VPC_SECURITY_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_ARN_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    DB_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SERVERLESS_V2_SCALING_CONFIGURATION_INFO_FIELD_NUMBER: _ClassVar[int]
    SCALING_CONFIGURATION_INFO_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_identifier: str
    db_instance_arn: str
    db_instance_id: str
    db_instance_port: int
    db_engine_name: str
    db_engine_version: str
    master_username: str
    db_instance_class: str
    storage_type: str
    num_iops: int
    storage_size_bytes: int
    db_instance_status: str
    iam_db_authentication: bool
    kms_key_id: str
    license_model: str
    multi_az_deployment: bool
    availability_zone: str
    secondary_availability_zone: str
    auto_minor_version_upgrade: bool
    backup_retention_period_days: int
    preferred_backup_window: str
    preferred_maintenance_window: str
    ca_certificate_identifier: str
    charset_name: str
    deletion_protection: bool
    read_replica_cluster_id_vec: _containers.RepeatedScalarFieldContainer[str]
    read_replica_db_id_vec: _containers.RepeatedScalarFieldContainer[str]
    read_replica_source_db_id: str
    db_name: str
    latest_restorable_time_msecs: int
    db_parameter_group: str
    db_option_group: str
    db_subnet: str
    copy_tags_to_snapshots: bool
    public_accessibility: bool
    vpc_security_group_vec: _containers.RepeatedScalarFieldContainer[str]
    db_tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    db_cluster_arn: str
    db_cluster_member_count: int
    db_cluster_members: _containers.RepeatedCompositeFieldContainer[DBClusterMember]
    db_endpoint: DBInfo.Endpoint
    serverless_v2_scaling_configuration_info: ServerlessV2ScalingConfigurationInfo
    scaling_configuration_info: ScalingConfigurationInfo
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_identifier: _Optional[str] = ..., db_instance_arn: _Optional[str] = ..., db_instance_id: _Optional[str] = ..., db_instance_port: _Optional[int] = ..., db_engine_name: _Optional[str] = ..., db_engine_version: _Optional[str] = ..., master_username: _Optional[str] = ..., db_instance_class: _Optional[str] = ..., storage_type: _Optional[str] = ..., num_iops: _Optional[int] = ..., storage_size_bytes: _Optional[int] = ..., db_instance_status: _Optional[str] = ..., iam_db_authentication: bool = ..., kms_key_id: _Optional[str] = ..., license_model: _Optional[str] = ..., multi_az_deployment: bool = ..., availability_zone: _Optional[str] = ..., secondary_availability_zone: _Optional[str] = ..., auto_minor_version_upgrade: bool = ..., backup_retention_period_days: _Optional[int] = ..., preferred_backup_window: _Optional[str] = ..., preferred_maintenance_window: _Optional[str] = ..., ca_certificate_identifier: _Optional[str] = ..., charset_name: _Optional[str] = ..., deletion_protection: bool = ..., read_replica_cluster_id_vec: _Optional[_Iterable[str]] = ..., read_replica_db_id_vec: _Optional[_Iterable[str]] = ..., read_replica_source_db_id: _Optional[str] = ..., db_name: _Optional[str] = ..., latest_restorable_time_msecs: _Optional[int] = ..., db_parameter_group: _Optional[str] = ..., db_option_group: _Optional[str] = ..., db_subnet: _Optional[str] = ..., copy_tags_to_snapshots: bool = ..., public_accessibility: bool = ..., vpc_security_group_vec: _Optional[_Iterable[str]] = ..., db_tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., db_cluster_arn: _Optional[str] = ..., db_cluster_member_count: _Optional[int] = ..., db_cluster_members: _Optional[_Iterable[_Union[DBClusterMember, _Mapping]]] = ..., db_endpoint: _Optional[_Union[DBInfo.Endpoint, _Mapping]] = ..., serverless_v2_scaling_configuration_info: _Optional[_Union[ServerlessV2ScalingConfigurationInfo, _Mapping]] = ..., scaling_configuration_info: _Optional[_Union[ScalingConfigurationInfo, _Mapping]] = ...) -> None: ...

class DescribeDBInstancesArg(_message.Message):
    __slots__ = ("region_name", "db_instance_id", "should_populate_kms_alias")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_POPULATE_KMS_ALIAS_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_instance_id: str
    should_populate_kms_alias: bool
    def __init__(self, region_name: _Optional[str] = ..., db_instance_id: _Optional[str] = ..., should_populate_kms_alias: bool = ...) -> None: ...

class DescribeDBInstancesResult(_message.Message):
    __slots__ = ("db_info_vec",)
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    db_info_vec: _containers.RepeatedCompositeFieldContainer[DBInfo]
    def __init__(self, db_info_vec: _Optional[_Iterable[_Union[DBInfo, _Mapping]]] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("db_snapshot_id", "db_snapshot_arn", "size_bytes", "status", "percent_progress", "snapshot_type", "snapshot_creation_time_usecs", "kms_key_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreating: _ClassVar[SnapshotInfo.Status]
        kAvailable: _ClassVar[SnapshotInfo.Status]
        kUnknown: _ClassVar[SnapshotInfo.Status]
    kCreating: SnapshotInfo.Status
    kAvailable: SnapshotInfo.Status
    kUnknown: SnapshotInfo.Status
    class SnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kManual: _ClassVar[SnapshotInfo.SnapshotType]
        kAutomated: _ClassVar[SnapshotInfo.SnapshotType]
    kManual: SnapshotInfo.SnapshotType
    kAutomated: SnapshotInfo.SnapshotType
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ARN_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    db_snapshot_id: str
    db_snapshot_arn: str
    size_bytes: int
    status: SnapshotInfo.Status
    percent_progress: int
    snapshot_type: SnapshotInfo.SnapshotType
    snapshot_creation_time_usecs: int
    kms_key_id: str
    def __init__(self, db_snapshot_id: _Optional[str] = ..., db_snapshot_arn: _Optional[str] = ..., size_bytes: _Optional[int] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., percent_progress: _Optional[int] = ..., snapshot_type: _Optional[_Union[SnapshotInfo.SnapshotType, str]] = ..., snapshot_creation_time_usecs: _Optional[int] = ..., kms_key_id: _Optional[str] = ...) -> None: ...

class CreateDBSnapshotArg(_message.Message):
    __slots__ = ("region_name", "db_instance_id", "db_snapshot_id", "tag_vec")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_instance_id: str
    db_snapshot_id: str
    tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, region_name: _Optional[str] = ..., db_instance_id: _Optional[str] = ..., db_snapshot_id: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class CreateDBSnapshotResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: SnapshotInfo
    def __init__(self, snapshot_info: _Optional[_Union[SnapshotInfo, _Mapping]] = ...) -> None: ...

class DescribeDBSnapshotsArg(_message.Message):
    __slots__ = ("region_name", "db_instance_id", "db_snapshot_id", "snapshot_type")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_instance_id: str
    db_snapshot_id: str
    snapshot_type: SnapshotInfo.SnapshotType
    def __init__(self, region_name: _Optional[str] = ..., db_instance_id: _Optional[str] = ..., db_snapshot_id: _Optional[str] = ..., snapshot_type: _Optional[_Union[SnapshotInfo.SnapshotType, str]] = ...) -> None: ...

class DescribeDBSnapshotsResult(_message.Message):
    __slots__ = ("snapshot_info_vec",)
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo]
    def __init__(self, snapshot_info_vec: _Optional[_Iterable[_Union[SnapshotInfo, _Mapping]]] = ...) -> None: ...

class RestoreDBInstanceArg(_message.Message):
    __slots__ = ("region_name", "db_info", "db_snapshot_id", "target_db_instance_id", "is_point_in_time_restore", "point_in_time_msecs")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_POINT_IN_TIME_RESTORE_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_info: DBInfo
    db_snapshot_id: str
    target_db_instance_id: str
    is_point_in_time_restore: bool
    point_in_time_msecs: int
    def __init__(self, region_name: _Optional[str] = ..., db_info: _Optional[_Union[DBInfo, _Mapping]] = ..., db_snapshot_id: _Optional[str] = ..., target_db_instance_id: _Optional[str] = ..., is_point_in_time_restore: bool = ..., point_in_time_msecs: _Optional[int] = ...) -> None: ...

class RestoreDBInstanceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeDBRegionsArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeDBRegionsResult(_message.Message):
    __slots__ = ("region_names",)
    REGION_NAMES_FIELD_NUMBER: _ClassVar[int]
    region_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, region_names: _Optional[_Iterable[str]] = ...) -> None: ...

class DBOptionGroup(_message.Message):
    __slots__ = ("name", "arn", "db_engine_type", "major_engine_version", "vpc_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARN_FIELD_NUMBER: _ClassVar[int]
    DB_ENGINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAJOR_ENGINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    arn: str
    db_engine_type: str
    major_engine_version: str
    vpc_id: str
    def __init__(self, name: _Optional[str] = ..., arn: _Optional[str] = ..., db_engine_type: _Optional[str] = ..., major_engine_version: _Optional[str] = ..., vpc_id: _Optional[str] = ...) -> None: ...

class DescribeDBOptionGroupsArg(_message.Message):
    __slots__ = ("region_name",)
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    def __init__(self, region_name: _Optional[str] = ...) -> None: ...

class DescribeDBOptionGroupsResult(_message.Message):
    __slots__ = ("option_group_vec",)
    OPTION_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    option_group_vec: _containers.RepeatedCompositeFieldContainer[DBOptionGroup]
    def __init__(self, option_group_vec: _Optional[_Iterable[_Union[DBOptionGroup, _Mapping]]] = ...) -> None: ...

class DBSubnetGroup(_message.Message):
    __slots__ = ("name", "arn", "vpc_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARN_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    arn: str
    vpc_id: str
    def __init__(self, name: _Optional[str] = ..., arn: _Optional[str] = ..., vpc_id: _Optional[str] = ...) -> None: ...

class DescribeDBSubnetGroupsArg(_message.Message):
    __slots__ = ("region_name",)
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    def __init__(self, region_name: _Optional[str] = ...) -> None: ...

class DescribeDBSubnetGroupsResult(_message.Message):
    __slots__ = ("subnet_group_vec",)
    SUBNET_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    subnet_group_vec: _containers.RepeatedCompositeFieldContainer[DBSubnetGroup]
    def __init__(self, subnet_group_vec: _Optional[_Iterable[_Union[DBSubnetGroup, _Mapping]]] = ...) -> None: ...

class DBParameterGroup(_message.Message):
    __slots__ = ("name", "arn", "family")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARN_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    name: str
    arn: str
    family: str
    def __init__(self, name: _Optional[str] = ..., arn: _Optional[str] = ..., family: _Optional[str] = ...) -> None: ...

class DescribeDBParameterGroupsArg(_message.Message):
    __slots__ = ("region_name",)
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    def __init__(self, region_name: _Optional[str] = ...) -> None: ...

class DescribeDBParameterGroupsResult(_message.Message):
    __slots__ = ("parameter_group_vec",)
    PARAMETER_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    parameter_group_vec: _containers.RepeatedCompositeFieldContainer[DBParameterGroup]
    def __init__(self, parameter_group_vec: _Optional[_Iterable[_Union[DBParameterGroup, _Mapping]]] = ...) -> None: ...

class CopyDBSnapshotArg(_message.Message):
    __slots__ = ("source_region_name", "destination_region_name", "source_snapshot_arn", "target_snapshot_id", "kms_key_id", "option_group_name", "should_copy_tags")
    SOURCE_REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_ARN_FIELD_NUMBER: _ClassVar[int]
    TARGET_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    OPTION_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOULD_COPY_TAGS_FIELD_NUMBER: _ClassVar[int]
    source_region_name: str
    destination_region_name: str
    source_snapshot_arn: str
    target_snapshot_id: str
    kms_key_id: str
    option_group_name: str
    should_copy_tags: bool
    def __init__(self, source_region_name: _Optional[str] = ..., destination_region_name: _Optional[str] = ..., source_snapshot_arn: _Optional[str] = ..., target_snapshot_id: _Optional[str] = ..., kms_key_id: _Optional[str] = ..., option_group_name: _Optional[str] = ..., should_copy_tags: bool = ...) -> None: ...

class CopyDBSnapshotResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: SnapshotInfo
    def __init__(self, snapshot_info: _Optional[_Union[SnapshotInfo, _Mapping]] = ...) -> None: ...

class ModifyDBSnapshotAttributeArg(_message.Message):
    __slots__ = ("region_name", "db_snapshot_id", "account_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_snapshot_id: str
    account_id: str
    def __init__(self, region_name: _Optional[str] = ..., db_snapshot_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class ModifyDBSnapshotAttributeResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDBSnapshotArg(_message.Message):
    __slots__ = ("region_name", "db_snapshot_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_snapshot_id: str
    def __init__(self, region_name: _Optional[str] = ..., db_snapshot_id: _Optional[str] = ...) -> None: ...

class DeleteDBSnapshotResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDBInstanceArg(_message.Message):
    __slots__ = ("region_name", "db_instance_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_instance_id: str
    def __init__(self, region_name: _Optional[str] = ..., db_instance_id: _Optional[str] = ...) -> None: ...

class DeleteDBInstanceResult(_message.Message):
    __slots__ = ("db_info_vec",)
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    db_info_vec: _containers.RepeatedCompositeFieldContainer[DBInfo]
    def __init__(self, db_info_vec: _Optional[_Iterable[_Union[DBInfo, _Mapping]]] = ...) -> None: ...

class DescribeDBClustersArg(_message.Message):
    __slots__ = ("region_name", "db_cluster_id", "should_populate_kms_alias")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_POPULATE_KMS_ALIAS_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_id: str
    should_populate_kms_alias: bool
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_id: _Optional[str] = ..., should_populate_kms_alias: bool = ...) -> None: ...

class DescribeDBClustersResult(_message.Message):
    __slots__ = ("db_info_vec",)
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    db_info_vec: _containers.RepeatedCompositeFieldContainer[DBInfo]
    def __init__(self, db_info_vec: _Optional[_Iterable[_Union[DBInfo, _Mapping]]] = ...) -> None: ...

class ClusterSnapshotInfo(_message.Message):
    __slots__ = ("db_cluster_snapshot_id", "db_cluster_snapshot_arn", "size_bytes", "status", "percent_progress", "snapshot_type", "snapshot_creation_time_usecs", "kms_key_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreating: _ClassVar[ClusterSnapshotInfo.Status]
        kAvailable: _ClassVar[ClusterSnapshotInfo.Status]
        kUnknown: _ClassVar[ClusterSnapshotInfo.Status]
    kCreating: ClusterSnapshotInfo.Status
    kAvailable: ClusterSnapshotInfo.Status
    kUnknown: ClusterSnapshotInfo.Status
    class SnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kManual: _ClassVar[ClusterSnapshotInfo.SnapshotType]
        kAutomated: _ClassVar[ClusterSnapshotInfo.SnapshotType]
    kManual: ClusterSnapshotInfo.SnapshotType
    kAutomated: ClusterSnapshotInfo.SnapshotType
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_SNAPSHOT_ARN_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PERCENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    db_cluster_snapshot_id: str
    db_cluster_snapshot_arn: str
    size_bytes: int
    status: ClusterSnapshotInfo.Status
    percent_progress: int
    snapshot_type: ClusterSnapshotInfo.SnapshotType
    snapshot_creation_time_usecs: int
    kms_key_id: str
    def __init__(self, db_cluster_snapshot_id: _Optional[str] = ..., db_cluster_snapshot_arn: _Optional[str] = ..., size_bytes: _Optional[int] = ..., status: _Optional[_Union[ClusterSnapshotInfo.Status, str]] = ..., percent_progress: _Optional[int] = ..., snapshot_type: _Optional[_Union[ClusterSnapshotInfo.SnapshotType, str]] = ..., snapshot_creation_time_usecs: _Optional[int] = ..., kms_key_id: _Optional[str] = ...) -> None: ...

class CreateDBClusterSnapshotArg(_message.Message):
    __slots__ = ("region_name", "db_cluster_id", "db_cluster_snapshot_id", "tag_vec")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_id: str
    db_cluster_snapshot_id: str
    tag_vec: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_id: _Optional[str] = ..., db_cluster_snapshot_id: _Optional[str] = ..., tag_vec: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class CreateDBClusterSnapshotResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: ClusterSnapshotInfo
    def __init__(self, snapshot_info: _Optional[_Union[ClusterSnapshotInfo, _Mapping]] = ...) -> None: ...

class DescribeDBClusterSnapshotsArg(_message.Message):
    __slots__ = ("region_name", "db_cluster_id", "db_cluster_snapshot_id", "snapshot_type")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_id: str
    db_cluster_snapshot_id: str
    snapshot_type: ClusterSnapshotInfo.SnapshotType
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_id: _Optional[str] = ..., db_cluster_snapshot_id: _Optional[str] = ..., snapshot_type: _Optional[_Union[ClusterSnapshotInfo.SnapshotType, str]] = ...) -> None: ...

class DescribeDBClusterSnapshotsResult(_message.Message):
    __slots__ = ("snapshot_info_vec",)
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[ClusterSnapshotInfo]
    def __init__(self, snapshot_info_vec: _Optional[_Iterable[_Union[ClusterSnapshotInfo, _Mapping]]] = ...) -> None: ...

class RestoreDBClusterArg(_message.Message):
    __slots__ = ("region_name", "db_info", "db_cluster_snapshot_id", "target_db_cluster_id", "is_point_in_time_restore", "point_in_time_msecs")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_POINT_IN_TIME_RESTORE_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_info: DBInfo
    db_cluster_snapshot_id: str
    target_db_cluster_id: str
    is_point_in_time_restore: bool
    point_in_time_msecs: int
    def __init__(self, region_name: _Optional[str] = ..., db_info: _Optional[_Union[DBInfo, _Mapping]] = ..., db_cluster_snapshot_id: _Optional[str] = ..., target_db_cluster_id: _Optional[str] = ..., is_point_in_time_restore: bool = ..., point_in_time_msecs: _Optional[int] = ...) -> None: ...

class RestoreDBClusterResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DBClusterParameterGroup(_message.Message):
    __slots__ = ("name", "arn", "family")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARN_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    name: str
    arn: str
    family: str
    def __init__(self, name: _Optional[str] = ..., arn: _Optional[str] = ..., family: _Optional[str] = ...) -> None: ...

class DescribeDBClusterParameterGroupsArg(_message.Message):
    __slots__ = ("region_name",)
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    def __init__(self, region_name: _Optional[str] = ...) -> None: ...

class DescribeDBClusterParameterGroupsResult(_message.Message):
    __slots__ = ("parameter_group_vec",)
    PARAMETER_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    parameter_group_vec: _containers.RepeatedCompositeFieldContainer[DBClusterParameterGroup]
    def __init__(self, parameter_group_vec: _Optional[_Iterable[_Union[DBClusterParameterGroup, _Mapping]]] = ...) -> None: ...

class CopyDBClusterSnapshotArg(_message.Message):
    __slots__ = ("source_region_name", "destination_region_name", "source_cluster_snapshot_arn", "target_cluster_snapshot_id", "kms_key_id", "should_copy_tags")
    SOURCE_REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLUSTER_SNAPSHOT_ARN_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_COPY_TAGS_FIELD_NUMBER: _ClassVar[int]
    source_region_name: str
    destination_region_name: str
    source_cluster_snapshot_arn: str
    target_cluster_snapshot_id: str
    kms_key_id: str
    should_copy_tags: bool
    def __init__(self, source_region_name: _Optional[str] = ..., destination_region_name: _Optional[str] = ..., source_cluster_snapshot_arn: _Optional[str] = ..., target_cluster_snapshot_id: _Optional[str] = ..., kms_key_id: _Optional[str] = ..., should_copy_tags: bool = ...) -> None: ...

class CopyDBClusterSnapshotResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: ClusterSnapshotInfo
    def __init__(self, snapshot_info: _Optional[_Union[ClusterSnapshotInfo, _Mapping]] = ...) -> None: ...

class ModifyDBClusterSnapshotAttributeArg(_message.Message):
    __slots__ = ("region_name", "db_cluster_snapshot_id", "account_id", "attribute_name", "values_to_add")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_snapshot_id: str
    account_id: str
    attribute_name: str
    values_to_add: str
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_snapshot_id: _Optional[str] = ..., account_id: _Optional[str] = ..., attribute_name: _Optional[str] = ..., values_to_add: _Optional[str] = ...) -> None: ...

class ModifyDBClusterSnapshotAttributeResult(_message.Message):
    __slots__ = ("db_cluster_snapshot_id",)
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    db_cluster_snapshot_id: str
    def __init__(self, db_cluster_snapshot_id: _Optional[str] = ...) -> None: ...

class DeleteDBClusterSnapshotArg(_message.Message):
    __slots__ = ("region_name", "db_cluster_snapshot_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_snapshot_id: str
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_snapshot_id: _Optional[str] = ...) -> None: ...

class DeleteDBClusterSnapshotResult(_message.Message):
    __slots__ = ("snapshot_info",)
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    snapshot_info: ClusterSnapshotInfo
    def __init__(self, snapshot_info: _Optional[_Union[ClusterSnapshotInfo, _Mapping]] = ...) -> None: ...

class DeleteDBClusterArg(_message.Message):
    __slots__ = ("region_name", "db_cluster_id")
    REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    DB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    region_name: str
    db_cluster_id: str
    def __init__(self, region_name: _Optional[str] = ..., db_cluster_id: _Optional[str] = ...) -> None: ...

class DeleteDBClusterResult(_message.Message):
    __slots__ = ("db_info_vec",)
    DB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    db_info_vec: _containers.RepeatedCompositeFieldContainer[DBInfo]
    def __init__(self, db_info_vec: _Optional[_Iterable[_Union[DBInfo, _Mapping]]] = ...) -> None: ...
