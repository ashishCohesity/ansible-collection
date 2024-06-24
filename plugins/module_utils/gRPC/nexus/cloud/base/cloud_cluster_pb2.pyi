from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudClusterInfo(_message.Message):
    __slots__ = ("name", "description", "physical_location", "type", "ntp_servers", "dns_server", "domain_name", "num_vms", "vm_ip_addresses", "azure_resource_groups", "azure_vpn_resource_group_name", "azure_storage_resource_group_name", "azure_vpn_virtual_network_name", "azure_vpn_subnet_name", "azure_vhd_file_path", "azure_vm_type", "azure_num_vms_per_storage_account", "azure_num_vms_per_resource_group", "external_kms", "external_target", "provider_cluster_info", "replication_factor", "vm_vec", "is_encryption_enabled", "is_ce_in_existing_resource_group", "storage_account_prefix", "existing_storage_account_name", "cohesity_cluster_name", "deletion_protection", "host_name", "use_managed_disks", "apps_subnet", "apps_subnet_mask")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSmall: _ClassVar[CloudClusterInfo.Type]
        kMedium: _ClassVar[CloudClusterInfo.Type]
        kLarge: _ClassVar[CloudClusterInfo.Type]
        kXLarge: _ClassVar[CloudClusterInfo.Type]
        kNextGen: _ClassVar[CloudClusterInfo.Type]
    kSmall: CloudClusterInfo.Type
    kMedium: CloudClusterInfo.Type
    kLarge: CloudClusterInfo.Type
    kXLarge: CloudClusterInfo.Type
    kNextGen: CloudClusterInfo.Type
    class ExternalKMS(_message.Message):
        __slots__ = ("kms_key_name", "key_vault_url", "keyvault_key_name")
        KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        KEY_VAULT_URL_FIELD_NUMBER: _ClassVar[int]
        KEYVAULT_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        kms_key_name: str
        key_vault_url: str
        keyvault_key_name: str
        def __init__(self, kms_key_name: _Optional[str] = ..., key_vault_url: _Optional[str] = ..., keyvault_key_name: _Optional[str] = ...) -> None: ...
    class ExternalTarget(_message.Message):
        __slots__ = ("storage_account_name", "storage_container_name", "storage_access_key", "target_name", "is_gov_target", "managed_identity_client_id")
        STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_GOV_TARGET_FIELD_NUMBER: _ClassVar[int]
        MANAGED_IDENTITY_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        storage_account_name: str
        storage_container_name: str
        storage_access_key: str
        target_name: str
        is_gov_target: bool
        managed_identity_client_id: str
        def __init__(self, storage_account_name: _Optional[str] = ..., storage_container_name: _Optional[str] = ..., storage_access_key: _Optional[str] = ..., target_name: _Optional[str] = ..., is_gov_target: bool = ..., managed_identity_client_id: _Optional[str] = ...) -> None: ...
    class CloudProviderClusterInfo(_message.Message):
        __slots__ = ("aws_cluster_info", "gcp_cluster_info", "azure_cluster_info")
        AWS_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
        GCP_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
        AZURE_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
        aws_cluster_info: AWSCloudClusterInfo
        gcp_cluster_info: GoogleCloudClusterInfo
        azure_cluster_info: AzureCloudClusterInfo
        def __init__(self, aws_cluster_info: _Optional[_Union[AWSCloudClusterInfo, _Mapping]] = ..., gcp_cluster_info: _Optional[_Union[GoogleCloudClusterInfo, _Mapping]] = ..., azure_cluster_info: _Optional[_Union[AzureCloudClusterInfo, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NTP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_VMS_FIELD_NUMBER: _ClassVar[int]
    VM_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    AZURE_RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    AZURE_VPN_RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AZURE_STORAGE_RESOURCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AZURE_VPN_VIRTUAL_NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    AZURE_VPN_SUBNET_NAME_FIELD_NUMBER: _ClassVar[int]
    AZURE_VHD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    AZURE_VM_TYPE_FIELD_NUMBER: _ClassVar[int]
    AZURE_NUM_VMS_PER_STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AZURE_NUM_VMS_PER_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_KMS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    VM_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_CE_IN_EXISTING_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ACCOUNT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    EXISTING_STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    COHESITY_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_MANAGED_DISKS_FIELD_NUMBER: _ClassVar[int]
    APPS_SUBNET_FIELD_NUMBER: _ClassVar[int]
    APPS_SUBNET_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    physical_location: str
    type: CloudClusterInfo.Type
    ntp_servers: str
    dns_server: str
    domain_name: str
    num_vms: int
    vm_ip_addresses: str
    azure_resource_groups: str
    azure_vpn_resource_group_name: str
    azure_storage_resource_group_name: str
    azure_vpn_virtual_network_name: str
    azure_vpn_subnet_name: str
    azure_vhd_file_path: str
    azure_vm_type: str
    azure_num_vms_per_storage_account: int
    azure_num_vms_per_resource_group: int
    external_kms: CloudClusterInfo.ExternalKMS
    external_target: CloudClusterInfo.ExternalTarget
    provider_cluster_info: CloudClusterInfo.CloudProviderClusterInfo
    replication_factor: int
    vm_vec: _containers.RepeatedScalarFieldContainer[str]
    is_encryption_enabled: bool
    is_ce_in_existing_resource_group: bool
    storage_account_prefix: str
    existing_storage_account_name: str
    cohesity_cluster_name: str
    deletion_protection: bool
    host_name: str
    use_managed_disks: bool
    apps_subnet: str
    apps_subnet_mask: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., physical_location: _Optional[str] = ..., type: _Optional[_Union[CloudClusterInfo.Type, str]] = ..., ntp_servers: _Optional[str] = ..., dns_server: _Optional[str] = ..., domain_name: _Optional[str] = ..., num_vms: _Optional[int] = ..., vm_ip_addresses: _Optional[str] = ..., azure_resource_groups: _Optional[str] = ..., azure_vpn_resource_group_name: _Optional[str] = ..., azure_storage_resource_group_name: _Optional[str] = ..., azure_vpn_virtual_network_name: _Optional[str] = ..., azure_vpn_subnet_name: _Optional[str] = ..., azure_vhd_file_path: _Optional[str] = ..., azure_vm_type: _Optional[str] = ..., azure_num_vms_per_storage_account: _Optional[int] = ..., azure_num_vms_per_resource_group: _Optional[int] = ..., external_kms: _Optional[_Union[CloudClusterInfo.ExternalKMS, _Mapping]] = ..., external_target: _Optional[_Union[CloudClusterInfo.ExternalTarget, _Mapping]] = ..., provider_cluster_info: _Optional[_Union[CloudClusterInfo.CloudProviderClusterInfo, _Mapping]] = ..., replication_factor: _Optional[int] = ..., vm_vec: _Optional[_Iterable[str]] = ..., is_encryption_enabled: bool = ..., is_ce_in_existing_resource_group: bool = ..., storage_account_prefix: _Optional[str] = ..., existing_storage_account_name: _Optional[str] = ..., cohesity_cluster_name: _Optional[str] = ..., deletion_protection: bool = ..., host_name: _Optional[str] = ..., use_managed_disks: bool = ..., apps_subnet: _Optional[str] = ..., apps_subnet_mask: _Optional[str] = ...) -> None: ...

class AzureCloudClusterInfo(_message.Message):
    __slots__ = ("num_ssds_per_vm", "ssd_capacity_gb", "ssd_disk_type", "ssd_provisioned_iops", "ssd_provisioned_throughput_mb", "num_hdds_per_vm", "hdd_capacity_gb", "hdd_disk_type", "hdd_provisioned_iops", "hdd_provisioned_throughput_mb", "availability_zones", "tags")
    class Tag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NUM_SSDS_PER_VM_FIELD_NUMBER: _ClassVar[int]
    SSD_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    SSD_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SSD_PROVISIONED_IOPS_FIELD_NUMBER: _ClassVar[int]
    SSD_PROVISIONED_THROUGHPUT_MB_FIELD_NUMBER: _ClassVar[int]
    NUM_HDDS_PER_VM_FIELD_NUMBER: _ClassVar[int]
    HDD_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    HDD_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    HDD_PROVISIONED_IOPS_FIELD_NUMBER: _ClassVar[int]
    HDD_PROVISIONED_THROUGHPUT_MB_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    num_ssds_per_vm: int
    ssd_capacity_gb: int
    ssd_disk_type: str
    ssd_provisioned_iops: int
    ssd_provisioned_throughput_mb: int
    num_hdds_per_vm: int
    hdd_capacity_gb: int
    hdd_disk_type: str
    hdd_provisioned_iops: int
    hdd_provisioned_throughput_mb: int
    availability_zones: str
    tags: _containers.RepeatedCompositeFieldContainer[AzureCloudClusterInfo.Tag]
    def __init__(self, num_ssds_per_vm: _Optional[int] = ..., ssd_capacity_gb: _Optional[int] = ..., ssd_disk_type: _Optional[str] = ..., ssd_provisioned_iops: _Optional[int] = ..., ssd_provisioned_throughput_mb: _Optional[int] = ..., num_hdds_per_vm: _Optional[int] = ..., hdd_capacity_gb: _Optional[int] = ..., hdd_disk_type: _Optional[str] = ..., hdd_provisioned_iops: _Optional[int] = ..., hdd_provisioned_throughput_mb: _Optional[int] = ..., availability_zones: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[AzureCloudClusterInfo.Tag, _Mapping]]] = ...) -> None: ...

class AWSCloudClusterInfo(_message.Message):
    __slots__ = ("instance_type", "ami_id", "vpn_vpc_id", "vpn_subnet_id", "security_group_id", "num_hdds_per_vm", "hdd_capacity_gb", "ssd_type", "ssd_capacity_gb", "provisioned_iops", "availability_zone", "vm_prefix", "deletion_protection", "host_name", "s3_bucket_name", "max_cf_template_size_supported_inline", "max_cf_template_size_supported_s3_bucket", "tags", "external_target", "permission_boundary_arn", "iam_resources_prefix")
    class Tag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ExternalTarget(_message.Message):
        __slots__ = ("access_key_id", "secret_access_key", "region_name", "bucket_name", "target_name", "tier_type", "is_gov_target")
        ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        REGION_NAME_FIELD_NUMBER: _ClassVar[int]
        BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
        TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_GOV_TARGET_FIELD_NUMBER: _ClassVar[int]
        access_key_id: str
        secret_access_key: str
        region_name: str
        bucket_name: str
        target_name: str
        tier_type: str
        is_gov_target: bool
        def __init__(self, access_key_id: _Optional[str] = ..., secret_access_key: _Optional[str] = ..., region_name: _Optional[str] = ..., bucket_name: _Optional[str] = ..., target_name: _Optional[str] = ..., tier_type: _Optional[str] = ..., is_gov_target: bool = ...) -> None: ...
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AMI_ID_FIELD_NUMBER: _ClassVar[int]
    VPN_VPC_ID_FIELD_NUMBER: _ClassVar[int]
    VPN_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_HDDS_PER_VM_FIELD_NUMBER: _ClassVar[int]
    HDD_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    SSD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SSD_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_IOPS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    VM_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_CF_TEMPLATE_SIZE_SUPPORTED_INLINE_FIELD_NUMBER: _ClassVar[int]
    MAX_CF_TEMPLATE_SIZE_SUPPORTED_S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_BOUNDARY_ARN_FIELD_NUMBER: _ClassVar[int]
    IAM_RESOURCES_PREFIX_FIELD_NUMBER: _ClassVar[int]
    instance_type: str
    ami_id: str
    vpn_vpc_id: str
    vpn_subnet_id: str
    security_group_id: str
    num_hdds_per_vm: int
    hdd_capacity_gb: int
    ssd_type: str
    ssd_capacity_gb: int
    provisioned_iops: int
    availability_zone: str
    vm_prefix: str
    deletion_protection: bool
    host_name: str
    s3_bucket_name: str
    max_cf_template_size_supported_inline: int
    max_cf_template_size_supported_s3_bucket: int
    tags: _containers.RepeatedCompositeFieldContainer[AWSCloudClusterInfo.Tag]
    external_target: AWSCloudClusterInfo.ExternalTarget
    permission_boundary_arn: str
    iam_resources_prefix: str
    def __init__(self, instance_type: _Optional[str] = ..., ami_id: _Optional[str] = ..., vpn_vpc_id: _Optional[str] = ..., vpn_subnet_id: _Optional[str] = ..., security_group_id: _Optional[str] = ..., num_hdds_per_vm: _Optional[int] = ..., hdd_capacity_gb: _Optional[int] = ..., ssd_type: _Optional[str] = ..., ssd_capacity_gb: _Optional[int] = ..., provisioned_iops: _Optional[int] = ..., availability_zone: _Optional[str] = ..., vm_prefix: _Optional[str] = ..., deletion_protection: bool = ..., host_name: _Optional[str] = ..., s3_bucket_name: _Optional[str] = ..., max_cf_template_size_supported_inline: _Optional[int] = ..., max_cf_template_size_supported_s3_bucket: _Optional[int] = ..., tags: _Optional[_Iterable[_Union[AWSCloudClusterInfo.Tag, _Mapping]]] = ..., external_target: _Optional[_Union[AWSCloudClusterInfo.ExternalTarget, _Mapping]] = ..., permission_boundary_arn: _Optional[str] = ..., iam_resources_prefix: _Optional[str] = ...) -> None: ...

class GoogleCloudClusterInfo(_message.Message):
    __slots__ = ("machine_type", "src_image_file_path", "bucket_name", "src_image_name", "vpc_network_name", "vpc_subnetwork_name", "region", "availability_zone", "num_hdds_per_vm", "hdd_capacity_gb", "ssd_capacity_gb", "authentication_filepath", "src_image_project_id", "deletion_protection", "replica_zone", "host_name", "external_target", "kms_key_name", "service_account_name", "labels", "network_tags", "ssd_disk_type", "hdd_disk_type")
    class ExternalTarget(_message.Message):
        __slots__ = ("project_id", "client_private_key_file_path", "client_email_id", "bucket_name", "target_name", "tier_type")
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_PRIVATE_KEY_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        CLIENT_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
        BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
        TIER_TYPE_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        client_private_key_file_path: str
        client_email_id: str
        bucket_name: str
        target_name: str
        tier_type: str
        def __init__(self, project_id: _Optional[str] = ..., client_private_key_file_path: _Optional[str] = ..., client_email_id: _Optional[str] = ..., bucket_name: _Optional[str] = ..., target_name: _Optional[str] = ..., tier_type: _Optional[str] = ...) -> None: ...
    class Label(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_IMAGE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    VPC_SUBNETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    NUM_HDDS_PER_VM_FIELD_NUMBER: _ClassVar[int]
    HDD_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    SSD_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    SRC_IMAGE_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONE_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    SSD_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    HDD_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    src_image_file_path: str
    bucket_name: str
    src_image_name: str
    vpc_network_name: str
    vpc_subnetwork_name: str
    region: str
    availability_zone: str
    num_hdds_per_vm: int
    hdd_capacity_gb: int
    ssd_capacity_gb: int
    authentication_filepath: str
    src_image_project_id: str
    deletion_protection: bool
    replica_zone: str
    host_name: str
    external_target: GoogleCloudClusterInfo.ExternalTarget
    kms_key_name: str
    service_account_name: str
    labels: _containers.RepeatedCompositeFieldContainer[GoogleCloudClusterInfo.Label]
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    ssd_disk_type: str
    hdd_disk_type: str
    def __init__(self, machine_type: _Optional[str] = ..., src_image_file_path: _Optional[str] = ..., bucket_name: _Optional[str] = ..., src_image_name: _Optional[str] = ..., vpc_network_name: _Optional[str] = ..., vpc_subnetwork_name: _Optional[str] = ..., region: _Optional[str] = ..., availability_zone: _Optional[str] = ..., num_hdds_per_vm: _Optional[int] = ..., hdd_capacity_gb: _Optional[int] = ..., ssd_capacity_gb: _Optional[int] = ..., authentication_filepath: _Optional[str] = ..., src_image_project_id: _Optional[str] = ..., deletion_protection: bool = ..., replica_zone: _Optional[str] = ..., host_name: _Optional[str] = ..., external_target: _Optional[_Union[GoogleCloudClusterInfo.ExternalTarget, _Mapping]] = ..., kms_key_name: _Optional[str] = ..., service_account_name: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[GoogleCloudClusterInfo.Label, _Mapping]]] = ..., network_tags: _Optional[_Iterable[str]] = ..., ssd_disk_type: _Optional[str] = ..., hdd_disk_type: _Optional[str] = ...) -> None: ...
