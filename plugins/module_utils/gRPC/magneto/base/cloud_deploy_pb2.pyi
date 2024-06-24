from magneto.base import entity_pb2 as _entity_pb2
from magneto.base.entities import aws_pb2 as _aws_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from magneto.base.env_params_pb2 import AlertingPolicyProto as AlertingPolicyProto
from magneto.base.env_params_pb2 import IndexingPolicyProto as IndexingPolicyProto
from magneto.base.env_params_pb2 import AWSSnapshotManagerParams as AWSSnapshotManagerParams
from magneto.base.env_params_pb2 import SnapshotManagerParams as SnapshotManagerParams
from magneto.base.env_params_pb2 import AcropolisDiskFilterProto as AcropolisDiskFilterProto
from magneto.base.env_params_pb2 import VMwareDiskExclusionProto as VMwareDiskExclusionProto
from magneto.base.env_params_pb2 import HyperVDiskFilterProto as HyperVDiskFilterProto
from magneto.base.env_params_pb2 import MSExchangeParams as MSExchangeParams
from magneto.base.env_params_pb2 import SourceAppParams as SourceAppParams
from magneto.base.env_params_pb2 import PhysicalSnapshotParams as PhysicalSnapshotParams
from magneto.base.env_params_pb2 import PhysicalFileBackupParams as PhysicalFileBackupParams
from magneto.base.env_params_pb2 import PhysicalBackupSourceParams as PhysicalBackupSourceParams
from magneto.base.env_params_pb2 import VMwareBackupSourceParams as VMwareBackupSourceParams
from magneto.base.env_params_pb2 import HyperVBackupSourceParams as HyperVBackupSourceParams
from magneto.base.env_params_pb2 import AcropolisBackupSourceParams as AcropolisBackupSourceParams
from magneto.base.env_params_pb2 import UdaBackupSourceParams as UdaBackupSourceParams
from magneto.base.env_params_pb2 import KubernetesBackupSourceParams as KubernetesBackupSourceParams
from magneto.base.env_params_pb2 import OracleRmanBackupType as OracleRmanBackupType
from magneto.base.env_params_pb2 import OracleArchiveLogRetentionType as OracleArchiveLogRetentionType
from magneto.base.env_params_pb2 import OracleVlanInfo as OracleVlanInfo
from magneto.base.env_params_pb2 import OracleSbtHostParams as OracleSbtHostParams
from magneto.base.env_params_pb2 import OracleDBChannelInfo as OracleDBChannelInfo
from magneto.base.env_params_pb2 import AdditionalOracleDBParams as AdditionalOracleDBParams
from magneto.base.env_params_pb2 import OracleSourceParams as OracleSourceParams
from magneto.base.env_params_pb2 import NasThrottlingParams as NasThrottlingParams
from magneto.base.env_params_pb2 import UdaThrottlingParams as UdaThrottlingParams
from magneto.base.env_params_pb2 import AWSNativeBackupSourceParams as AWSNativeBackupSourceParams
from magneto.base.env_params_pb2 import AWSSnapshotManagerBackupSourceParams as AWSSnapshotManagerBackupSourceParams
from magneto.base.env_params_pb2 import GCPNativeObjectParams as GCPNativeObjectParams
from magneto.base.env_params_pb2 import SharepointBackupSourceParams as SharepointBackupSourceParams
from magneto.base.env_params_pb2 import S3BucketParamsProto as S3BucketParamsProto
from magneto.base.env_params_pb2 import BackupSourceParams as BackupSourceParams
from magneto.base.env_params_pb2 import FilteringPolicyProto as FilteringPolicyProto
from magneto.base.env_params_pb2 import NasBackupParams as NasBackupParams
from magneto.base.env_params_pb2 import S3ViewBackupProperties as S3ViewBackupProperties
from magneto.base.env_params_pb2 import PhysicalBackupEnvParams as PhysicalBackupEnvParams
from magneto.base.env_params_pb2 import VMwareBackupEnvParams as VMwareBackupEnvParams
from magneto.base.env_params_pb2 import SqlBackupJobParams as SqlBackupJobParams
from magneto.base.env_params_pb2 import OracleBackupJobParams as OracleBackupJobParams
from magneto.base.env_params_pb2 import AcropolisBackupJobParams as AcropolisBackupJobParams
from magneto.base.env_params_pb2 import SanBackupJobParams as SanBackupJobParams
from magneto.base.env_params_pb2 import ExternallyTriggeredJobParams as ExternallyTriggeredJobParams
from magneto.base.env_params_pb2 import HyperVBackupEnvParams as HyperVBackupEnvParams
from magneto.base.env_params_pb2 import AttributeFilterParams as AttributeFilterParams
from magneto.base.env_params_pb2 import AttributeFilterPolicy as AttributeFilterPolicy
from magneto.base.env_params_pb2 import OutlookBackupEnvParams as OutlookBackupEnvParams
from magneto.base.env_params_pb2 import OneDriveBackupEnvParams as OneDriveBackupEnvParams
from magneto.base.env_params_pb2 import SharepPointSiteBackupEnvParams as SharepPointSiteBackupEnvParams
from magneto.base.env_params_pb2 import GroupBackupEnvParams as GroupBackupEnvParams
from magneto.base.env_params_pb2 import TeamsBackupEnvParams as TeamsBackupEnvParams
from magneto.base.env_params_pb2 import PublicFoldersBackupEnvParams as PublicFoldersBackupEnvParams
from magneto.base.env_params_pb2 import O365BackupEnvParams as O365BackupEnvParams
from magneto.base.env_params_pb2 import FileUptieringParams as FileUptieringParams
from magneto.base.env_params_pb2 import ExchangeBackupJobParams as ExchangeBackupJobParams
from magneto.base.env_params_pb2 import NasAnalysisJobParams as NasAnalysisJobParams
from magneto.base.env_params_pb2 import FileStubbingParams as FileStubbingParams
from magneto.base.env_params_pb2 import IsilonEnvParams as IsilonEnvParams
from magneto.base.env_params_pb2 import AWSNativeEnvParams as AWSNativeEnvParams
from magneto.base.env_params_pb2 import GCPNativeJobParams as GCPNativeJobParams
from magneto.base.env_params_pb2 import KubernetesEnvParams as KubernetesEnvParams
from magneto.base.env_params_pb2 import S3BackupJobParams as S3BackupJobParams
from magneto.base.env_params_pb2 import EnvBackupParams as EnvBackupParams
from magneto.base.env_params_pb2 import GCPDiskExclusionObjectParams as GCPDiskExclusionObjectParams
from magneto.base.env_params_pb2 import GCPJobDiskExclusionRule as GCPJobDiskExclusionRule
from magneto.base.env_params_pb2 import EBSVolumeExclusionParams as EBSVolumeExclusionParams
from magneto.base.env_params_pb2 import K8sFilterParams as K8sFilterParams
from magneto.base.env_params_pb2 import DataTransferInfo as DataTransferInfo

DESCRIPTOR: _descriptor.FileDescriptor

class AzureManagedDiskParams(_message.Message):
    __slots__ = ("os_disk_sku_type", "data_disks_sku_type")
    class SKUType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPremiumSSD: _ClassVar[AzureManagedDiskParams.SKUType]
        kStandardSSD: _ClassVar[AzureManagedDiskParams.SKUType]
        kStandardHDD: _ClassVar[AzureManagedDiskParams.SKUType]
    kPremiumSSD: AzureManagedDiskParams.SKUType
    kStandardSSD: AzureManagedDiskParams.SKUType
    kStandardHDD: AzureManagedDiskParams.SKUType
    OS_DISK_SKU_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_DISKS_SKU_TYPE_FIELD_NUMBER: _ClassVar[int]
    os_disk_sku_type: AzureManagedDiskParams.SKUType
    data_disks_sku_type: AzureManagedDiskParams.SKUType
    def __init__(self, os_disk_sku_type: _Optional[_Union[AzureManagedDiskParams.SKUType, str]] = ..., data_disks_sku_type: _Optional[_Union[AzureManagedDiskParams.SKUType, str]] = ...) -> None: ...

class DeployVMsToAzureParams(_message.Message):
    __slots__ = ("subscription", "region", "resource_group", "compute_options", "storage_resource_group", "storage_account", "storage_container", "storage_key", "network_security_group", "network_resource_group", "virtual_network", "subnet", "azure_managed_disk_params", "temp_vm_resource_group", "temp_vm_storage_account", "temp_vm_storage_container", "temp_vm_virtual_network", "temp_vm_subnet", "availability_set", "data_transfer_info")
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    STORAGE_KEY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    AZURE_MANAGED_DISK_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_VIRTUAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
    TEMP_VM_SUBNET_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_SET_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_INFO_FIELD_NUMBER: _ClassVar[int]
    subscription: _entity_pb2.EntityProto
    region: _entity_pb2.EntityProto
    resource_group: _entity_pb2.EntityProto
    compute_options: _entity_pb2.EntityProto
    storage_resource_group: _entity_pb2.EntityProto
    storage_account: _entity_pb2.EntityProto
    storage_container: _entity_pb2.EntityProto
    storage_key: _entity_pb2.EntityProto
    network_security_group: _entity_pb2.EntityProto
    network_resource_group: _entity_pb2.EntityProto
    virtual_network: _entity_pb2.EntityProto
    subnet: _entity_pb2.EntityProto
    azure_managed_disk_params: AzureManagedDiskParams
    temp_vm_resource_group: _entity_pb2.EntityProto
    temp_vm_storage_account: _entity_pb2.EntityProto
    temp_vm_storage_container: _entity_pb2.EntityProto
    temp_vm_virtual_network: _entity_pb2.EntityProto
    temp_vm_subnet: _entity_pb2.EntityProto
    availability_set: _entity_pb2.EntityProto
    data_transfer_info: _env_params_pb2.DataTransferInfo
    def __init__(self, subscription: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., region: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., compute_options: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_account: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_container: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_key: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., network_security_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., network_resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., virtual_network: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., subnet: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., azure_managed_disk_params: _Optional[_Union[AzureManagedDiskParams, _Mapping]] = ..., temp_vm_resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., temp_vm_storage_account: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., temp_vm_storage_container: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., temp_vm_virtual_network: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., temp_vm_subnet: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., availability_set: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., data_transfer_info: _Optional[_Union[_env_params_pb2.DataTransferInfo, _Mapping]] = ...) -> None: ...

class DeployDBInstancesToRDSParams(_message.Message):
    __slots__ = ("db_instance_id", "availability_zone", "db_parameter_group", "db_option_group", "multi_az_deployment", "db_port", "auto_minor_version_upgrade", "copy_tags_to_snapshots", "iam_db_authentication", "public_accessibility", "point_in_time_params")
    class PointInTimeRestoreParams(_message.Message):
        __slots__ = ("timestamp_msecs",)
        TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        timestamp_msecs: int
        def __init__(self, timestamp_msecs: _Optional[int] = ...) -> None: ...
    DB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    DB_PARAMETER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DB_OPTION_GROUP_FIELD_NUMBER: _ClassVar[int]
    MULTI_AZ_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    DB_PORT_FIELD_NUMBER: _ClassVar[int]
    AUTO_MINOR_VERSION_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    COPY_TAGS_TO_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    IAM_DB_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_PARAMS_FIELD_NUMBER: _ClassVar[int]
    db_instance_id: str
    availability_zone: _entity_pb2.EntityProto
    db_parameter_group: _entity_pb2.EntityProto
    db_option_group: _entity_pb2.EntityProto
    multi_az_deployment: bool
    db_port: int
    auto_minor_version_upgrade: bool
    copy_tags_to_snapshots: bool
    iam_db_authentication: bool
    public_accessibility: bool
    point_in_time_params: DeployDBInstancesToRDSParams.PointInTimeRestoreParams
    def __init__(self, db_instance_id: _Optional[str] = ..., availability_zone: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., db_parameter_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., db_option_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., multi_az_deployment: bool = ..., db_port: _Optional[int] = ..., auto_minor_version_upgrade: bool = ..., copy_tags_to_snapshots: bool = ..., iam_db_authentication: bool = ..., public_accessibility: bool = ..., point_in_time_params: _Optional[_Union[DeployDBInstancesToRDSParams.PointInTimeRestoreParams, _Mapping]] = ...) -> None: ...

class DeployVMsToAWSParams(_message.Message):
    __slots__ = ("region", "instance_type", "vpc", "subnet", "network_security_groups", "key_pair_name", "rds_params", "aurora_params", "proxy_vm_vpc", "proxy_vm_subnet", "custom_tag_vec", "encryption_params")
    REGION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    KEY_PAIR_NAME_FIELD_NUMBER: _ClassVar[int]
    RDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AURORA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PROXY_VM_VPC_FIELD_NUMBER: _ClassVar[int]
    PROXY_VM_SUBNET_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    region: _entity_pb2.EntityProto
    instance_type: _entity_pb2.EntityProto
    vpc: _entity_pb2.EntityProto
    subnet: _entity_pb2.EntityProto
    network_security_groups: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    key_pair_name: _entity_pb2.EntityProto
    rds_params: DeployDBInstancesToRDSParams
    aurora_params: DeployDBInstancesToRDSParams
    proxy_vm_vpc: _entity_pb2.EntityProto
    proxy_vm_subnet: _entity_pb2.EntityProto
    custom_tag_vec: _containers.RepeatedCompositeFieldContainer[CustomTag]
    encryption_params: EncryptionParams
    def __init__(self, region: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., instance_type: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., vpc: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., subnet: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., network_security_groups: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., key_pair_name: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., rds_params: _Optional[_Union[DeployDBInstancesToRDSParams, _Mapping]] = ..., aurora_params: _Optional[_Union[DeployDBInstancesToRDSParams, _Mapping]] = ..., proxy_vm_vpc: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., proxy_vm_subnet: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., custom_tag_vec: _Optional[_Iterable[_Union[CustomTag, _Mapping]]] = ..., encryption_params: _Optional[_Union[EncryptionParams, _Mapping]] = ...) -> None: ...

class CustomTag(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DeployVMsToGCPParams(_message.Message):
    __slots__ = ("project_id", "region", "zone", "subnet")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    project_id: _entity_pb2.EntityProto
    region: _entity_pb2.EntityProto
    zone: _entity_pb2.EntityProto
    subnet: _entity_pb2.EntityProto
    def __init__(self, project_id: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., region: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., zone: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., subnet: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class ReplicateSnapshotsToAWSParams(_message.Message):
    __slots__ = ("region",)
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: _entity_pb2.EntityProto
    def __init__(self, region: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class ReplicateSnapshotsToAzureParams(_message.Message):
    __slots__ = ("storage_resource_group", "storage_account", "storage_container", "resource_group")
    STORAGE_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    storage_resource_group: _entity_pb2.EntityProto
    storage_account: _entity_pb2.EntityProto
    storage_container: _entity_pb2.EntityProto
    resource_group: _entity_pb2.EntityProto
    def __init__(self, storage_resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_account: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., storage_container: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., resource_group: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...

class DeployFleetParams(_message.Message):
    __slots__ = ("aws_fleet_params",)
    AWS_FLEET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    aws_fleet_params: _aws_pb2.AWSFleetParams
    def __init__(self, aws_fleet_params: _Optional[_Union[_aws_pb2.AWSFleetParams, _Mapping]] = ...) -> None: ...

class DeployVMsToCloudParams(_message.Message):
    __slots__ = ("deploy_vms_to_azure_params", "deploy_vms_to_aws_params", "deploy_vms_to_gcp_params", "replicate_snapshots_to_aws_params", "replicate_snapshots_to_azure_params", "deploy_fleet_params")
    DEPLOY_VMS_TO_AZURE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_AWS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_GCP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_SNAPSHOTS_TO_AWS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REPLICATE_SNAPSHOTS_TO_AZURE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_FLEET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    deploy_vms_to_azure_params: DeployVMsToAzureParams
    deploy_vms_to_aws_params: DeployVMsToAWSParams
    deploy_vms_to_gcp_params: DeployVMsToGCPParams
    replicate_snapshots_to_aws_params: ReplicateSnapshotsToAWSParams
    replicate_snapshots_to_azure_params: ReplicateSnapshotsToAzureParams
    deploy_fleet_params: DeployFleetParams
    def __init__(self, deploy_vms_to_azure_params: _Optional[_Union[DeployVMsToAzureParams, _Mapping]] = ..., deploy_vms_to_aws_params: _Optional[_Union[DeployVMsToAWSParams, _Mapping]] = ..., deploy_vms_to_gcp_params: _Optional[_Union[DeployVMsToGCPParams, _Mapping]] = ..., replicate_snapshots_to_aws_params: _Optional[_Union[ReplicateSnapshotsToAWSParams, _Mapping]] = ..., replicate_snapshots_to_azure_params: _Optional[_Union[ReplicateSnapshotsToAzureParams, _Mapping]] = ..., deploy_fleet_params: _Optional[_Union[DeployFleetParams, _Mapping]] = ...) -> None: ...

class EncryptionParams(_message.Message):
    __slots__ = ("should_encrypt", "kms_key", "custom_kms_key_arn")
    SHOULD_ENCRYPT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_KMS_KEY_ARN_FIELD_NUMBER: _ClassVar[int]
    should_encrypt: bool
    kms_key: _entity_pb2.EntityProto
    custom_kms_key_arn: str
    def __init__(self, should_encrypt: bool = ..., kms_key: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., custom_kms_key_arn: _Optional[str] = ...) -> None: ...
