from alerts.base import alert_pb2 as _alert_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from magneto.api.common import aws_pb2 as _aws_pb2
from magneto.api.common import azure_sql_pb2 as _azure_sql_pb2
from magneto.api.common import o365_pb2 as _o365_pb2
from magneto.base import common_pb2 as _common_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import kubernetes_pb2 as _kubernetes_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import nosql_pb2 as _nosql_pb2
from magneto.base import sfdc_pb2 as _sfdc_pb2
from magneto.base import uda_pb2 as _uda_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertingPolicyProto(_message.Message):
    __slots__ = ("policy", "emails", "raise_object_level_failure_alert", "raise_object_level_failure_alert_after_last_attempt", "raise_object_level_failure_alert_after_each_attempt", "delivery_target_vec")
    class Policy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSuccess: _ClassVar[AlertingPolicyProto.Policy]
        kFailure: _ClassVar[AlertingPolicyProto.Policy]
        kSlaViolation: _ClassVar[AlertingPolicyProto.Policy]
        kWarning: _ClassVar[AlertingPolicyProto.Policy]
        kAll: _ClassVar[AlertingPolicyProto.Policy]
    kSuccess: AlertingPolicyProto.Policy
    kFailure: AlertingPolicyProto.Policy
    kSlaViolation: AlertingPolicyProto.Policy
    kWarning: AlertingPolicyProto.Policy
    kAll: AlertingPolicyProto.Policy
    POLICY_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    RAISE_OBJECT_LEVEL_FAILURE_ALERT_FIELD_NUMBER: _ClassVar[int]
    RAISE_OBJECT_LEVEL_FAILURE_ALERT_AFTER_LAST_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    RAISE_OBJECT_LEVEL_FAILURE_ALERT_AFTER_EACH_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    policy: int
    emails: _containers.RepeatedScalarFieldContainer[str]
    raise_object_level_failure_alert: bool
    raise_object_level_failure_alert_after_last_attempt: bool
    raise_object_level_failure_alert_after_each_attempt: bool
    delivery_target_vec: _containers.RepeatedCompositeFieldContainer[_alert_pb2.DeliveryRuleProto.DeliveryTarget]
    def __init__(self, policy: _Optional[int] = ..., emails: _Optional[_Iterable[str]] = ..., raise_object_level_failure_alert: bool = ..., raise_object_level_failure_alert_after_last_attempt: bool = ..., raise_object_level_failure_alert_after_each_attempt: bool = ..., delivery_target_vec: _Optional[_Iterable[_Union[_alert_pb2.DeliveryRuleProto.DeliveryTarget, _Mapping]]] = ...) -> None: ...

class IndexingPolicyProto(_message.Message):
    __slots__ = ("disable_indexing", "allow_prefixes", "deny_prefixes")
    DISABLE_INDEXING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    DENY_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    disable_indexing: bool
    allow_prefixes: _containers.RepeatedScalarFieldContainer[str]
    deny_prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, disable_indexing: bool = ..., allow_prefixes: _Optional[_Iterable[str]] = ..., deny_prefixes: _Optional[_Iterable[str]] = ...) -> None: ...

class AWSSnapshotManagerParams(_message.Message):
    __slots__ = ("should_create_ami", "ami_creation_frequency", "create_ami_for_run", "volume_exclusion_params")
    SHOULD_CREATE_AMI_FIELD_NUMBER: _ClassVar[int]
    AMI_CREATION_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CREATE_AMI_FOR_RUN_FIELD_NUMBER: _ClassVar[int]
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    should_create_ami: bool
    ami_creation_frequency: int
    create_ami_for_run: bool
    volume_exclusion_params: EBSVolumeExclusionParams
    def __init__(self, should_create_ami: bool = ..., ami_creation_frequency: _Optional[int] = ..., create_ami_for_run: bool = ..., volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ...) -> None: ...

class SnapshotManagerParams(_message.Message):
    __slots__ = ("aws_snapshot_manager_params",)
    AWS_SNAPSHOT_MANAGER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    aws_snapshot_manager_params: AWSSnapshotManagerParams
    def __init__(self, aws_snapshot_manager_params: _Optional[_Union[AWSSnapshotManagerParams, _Mapping]] = ...) -> None: ...

class AcropolisDiskFilterProto(_message.Message):
    __slots__ = ("bus_type", "index")
    BUS_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    bus_type: str
    index: int
    def __init__(self, bus_type: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class VMwareDiskExclusionProto(_message.Message):
    __slots__ = ("unit_number", "controller_bus_number", "controller_type")
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    unit_number: int
    controller_bus_number: int
    controller_type: str
    def __init__(self, unit_number: _Optional[int] = ..., controller_bus_number: _Optional[int] = ..., controller_type: _Optional[str] = ...) -> None: ...

class HyperVDiskFilterProto(_message.Message):
    __slots__ = ("unit_number", "controller_bus_number", "controller_type")
    UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_BUS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    unit_number: int
    controller_bus_number: int
    controller_type: str
    def __init__(self, unit_number: _Optional[int] = ..., controller_bus_number: _Optional[int] = ..., controller_type: _Optional[str] = ...) -> None: ...

class MSExchangeParams(_message.Message):
    __slots__ = ("perform_log_truncation",)
    PERFORM_LOG_TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    perform_log_truncation: bool
    def __init__(self, perform_log_truncation: bool = ...) -> None: ...

class SourceAppParams(_message.Message):
    __slots__ = ("ms_exchange_params", "is_vss_copy_only")
    MS_EXCHANGE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_VSS_COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    ms_exchange_params: MSExchangeParams
    is_vss_copy_only: bool
    def __init__(self, ms_exchange_params: _Optional[_Union[MSExchangeParams, _Mapping]] = ..., is_vss_copy_only: bool = ...) -> None: ...

class PhysicalSnapshotParams(_message.Message):
    __slots__ = ("vss_excluded_writers", "vss_copy_only_backup", "fetch_snapshot_metadata_disabled", "notify_backup_complete_disabled")
    VSS_EXCLUDED_WRITERS_FIELD_NUMBER: _ClassVar[int]
    VSS_COPY_ONLY_BACKUP_FIELD_NUMBER: _ClassVar[int]
    FETCH_SNAPSHOT_METADATA_DISABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_BACKUP_COMPLETE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    vss_excluded_writers: _containers.RepeatedScalarFieldContainer[str]
    vss_copy_only_backup: bool
    fetch_snapshot_metadata_disabled: bool
    notify_backup_complete_disabled: bool
    def __init__(self, vss_excluded_writers: _Optional[_Iterable[str]] = ..., vss_copy_only_backup: bool = ..., fetch_snapshot_metadata_disabled: bool = ..., notify_backup_complete_disabled: bool = ...) -> None: ...

class PhysicalFileBackupParams(_message.Message):
    __slots__ = ("backup_path_info_vec", "uses_skip_nested_volumes_vec", "symlink_follow_nas_target", "skip_nested_volumes_vec", "metadata_file_path")
    class GlobalIncludeExclude(_message.Message):
        __slots__ = ("exclude_vec", "fs_exclude")
        EXCLUDE_VEC_FIELD_NUMBER: _ClassVar[int]
        FS_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
        exclude_vec: _containers.RepeatedScalarFieldContainer[str]
        fs_exclude: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, exclude_vec: _Optional[_Iterable[str]] = ..., fs_exclude: _Optional[_Iterable[str]] = ...) -> None: ...
    class BackupPathInfo(_message.Message):
        __slots__ = ("include_path", "exclude_paths", "skip_nested_volumes")
        INCLUDE_PATH_FIELD_NUMBER: _ClassVar[int]
        EXCLUDE_PATHS_FIELD_NUMBER: _ClassVar[int]
        SKIP_NESTED_VOLUMES_FIELD_NUMBER: _ClassVar[int]
        include_path: str
        exclude_paths: _containers.RepeatedScalarFieldContainer[str]
        skip_nested_volumes: bool
        def __init__(self, include_path: _Optional[str] = ..., exclude_paths: _Optional[_Iterable[str]] = ..., skip_nested_volumes: bool = ...) -> None: ...
    BACKUP_PATH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    USES_SKIP_NESTED_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_FOLLOW_NAS_TARGET_FIELD_NUMBER: _ClassVar[int]
    SKIP_NESTED_VOLUMES_VEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    backup_path_info_vec: _containers.RepeatedCompositeFieldContainer[PhysicalFileBackupParams.BackupPathInfo]
    uses_skip_nested_volumes_vec: bool
    symlink_follow_nas_target: bool
    skip_nested_volumes_vec: _containers.RepeatedScalarFieldContainer[str]
    metadata_file_path: str
    def __init__(self, backup_path_info_vec: _Optional[_Iterable[_Union[PhysicalFileBackupParams.BackupPathInfo, _Mapping]]] = ..., uses_skip_nested_volumes_vec: bool = ..., symlink_follow_nas_target: bool = ..., skip_nested_volumes_vec: _Optional[_Iterable[str]] = ..., metadata_file_path: _Optional[str] = ...) -> None: ...

class PhysicalBackupSourceParams(_message.Message):
    __slots__ = ("volume_guid_vec", "file_backup_params", "source_app_params", "snapshot_params", "enable_system_backup")
    VOLUME_GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SYSTEM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    volume_guid_vec: _containers.RepeatedScalarFieldContainer[str]
    file_backup_params: PhysicalFileBackupParams
    source_app_params: SourceAppParams
    snapshot_params: PhysicalSnapshotParams
    enable_system_backup: bool
    def __init__(self, volume_guid_vec: _Optional[_Iterable[str]] = ..., file_backup_params: _Optional[_Union[PhysicalFileBackupParams, _Mapping]] = ..., source_app_params: _Optional[_Union[SourceAppParams, _Mapping]] = ..., snapshot_params: _Optional[_Union[PhysicalSnapshotParams, _Mapping]] = ..., enable_system_backup: bool = ...) -> None: ...

class VMwareBackupSourceParams(_message.Message):
    __slots__ = ("source_app_params", "vm_credentials", "vmware_disk_exclusion_info")
    SOURCE_APP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    source_app_params: SourceAppParams
    vm_credentials: _credentials_pb2.Credentials
    vmware_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[VMwareDiskExclusionProto]
    def __init__(self, source_app_params: _Optional[_Union[SourceAppParams, _Mapping]] = ..., vm_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., vmware_disk_exclusion_info: _Optional[_Iterable[_Union[VMwareDiskExclusionProto, _Mapping]]] = ...) -> None: ...

class HyperVBackupSourceParams(_message.Message):
    __slots__ = ("source_app_params", "hyperv_disk_exclusion_info", "hyperv_disk_inclusion_info")
    SOURCE_APP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    source_app_params: SourceAppParams
    hyperv_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[HyperVDiskFilterProto]
    hyperv_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[HyperVDiskFilterProto]
    def __init__(self, source_app_params: _Optional[_Union[SourceAppParams, _Mapping]] = ..., hyperv_disk_exclusion_info: _Optional[_Iterable[_Union[HyperVDiskFilterProto, _Mapping]]] = ..., hyperv_disk_inclusion_info: _Optional[_Iterable[_Union[HyperVDiskFilterProto, _Mapping]]] = ...) -> None: ...

class AcropolisBackupSourceParams(_message.Message):
    __slots__ = ("acropolis_disk_exclusion_info", "acropolis_disk_inclusion_info")
    ACROPOLIS_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    acropolis_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[AcropolisDiskFilterProto]
    acropolis_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[AcropolisDiskFilterProto]
    def __init__(self, acropolis_disk_exclusion_info: _Optional[_Iterable[_Union[AcropolisDiskFilterProto, _Mapping]]] = ..., acropolis_disk_inclusion_info: _Optional[_Iterable[_Union[AcropolisDiskFilterProto, _Mapping]]] = ...) -> None: ...

class UdaBackupSourceParams(_message.Message):
    __slots__ = ("throttling_params",)
    THROTTLING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    throttling_params: UdaThrottlingParams
    def __init__(self, throttling_params: _Optional[_Union[UdaThrottlingParams, _Mapping]] = ...) -> None: ...

class KubernetesBackupSourceParams(_message.Message):
    __slots__ = ("exclude_params", "include_params")
    EXCLUDE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    exclude_params: K8sFilterParams
    include_params: K8sFilterParams
    def __init__(self, exclude_params: _Optional[_Union[K8sFilterParams, _Mapping]] = ..., include_params: _Optional[_Union[K8sFilterParams, _Mapping]] = ...) -> None: ...

class OracleRmanBackupType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kImageCopy: _ClassVar[OracleRmanBackupType.Type]
        kBackupSets: _ClassVar[OracleRmanBackupType.Type]
        kSbt: _ClassVar[OracleRmanBackupType.Type]
    kImageCopy: OracleRmanBackupType.Type
    kBackupSets: OracleRmanBackupType.Type
    kSbt: OracleRmanBackupType.Type
    def __init__(self) -> None: ...

class OracleArchiveLogRetentionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kHour: _ClassVar[OracleArchiveLogRetentionType.Type]
        kDay: _ClassVar[OracleArchiveLogRetentionType.Type]
    kHour: OracleArchiveLogRetentionType.Type
    kDay: OracleArchiveLogRetentionType.Type
    def __init__(self) -> None: ...

class OracleVlanInfo(_message.Message):
    __slots__ = ("ip_vec", "gateway", "id", "subnet_ip")
    IP_VEC_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    ip_vec: _containers.RepeatedScalarFieldContainer[str]
    gateway: str
    id: int
    subnet_ip: str
    def __init__(self, ip_vec: _Optional[_Iterable[str]] = ..., gateway: _Optional[str] = ..., id: _Optional[int] = ..., subnet_ip: _Optional[str] = ...) -> None: ...

class OracleSbtHostParams(_message.Message):
    __slots__ = ("sbt_library_path", "view_fs_path", "vip_vec", "vlan_info_vec")
    SBT_LIBRARY_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_FS_PATH_FIELD_NUMBER: _ClassVar[int]
    VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    VLAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    sbt_library_path: str
    view_fs_path: str
    vip_vec: _containers.RepeatedScalarFieldContainer[str]
    vlan_info_vec: _containers.RepeatedCompositeFieldContainer[OracleVlanInfo]
    def __init__(self, sbt_library_path: _Optional[str] = ..., view_fs_path: _Optional[str] = ..., vip_vec: _Optional[_Iterable[str]] = ..., vlan_info_vec: _Optional[_Iterable[_Union[OracleVlanInfo, _Mapping]]] = ...) -> None: ...

class OracleDBChannelInfo(_message.Message):
    __slots__ = ("host_info_vec", "max_num_host", "num_channels", "db_uuid", "db_unique_name", "archivelog_keep_days", "enable_dg_primary_backup", "rman_backup_type", "credentials", "archivelog_keep_hours")
    class HostInfo(_message.Message):
        __slots__ = ("host", "num_channels", "portnum", "sbt_host_params")
        HOST_FIELD_NUMBER: _ClassVar[int]
        NUM_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        PORTNUM_FIELD_NUMBER: _ClassVar[int]
        SBT_HOST_PARAMS_FIELD_NUMBER: _ClassVar[int]
        host: str
        num_channels: int
        portnum: int
        sbt_host_params: OracleSbtHostParams
        def __init__(self, host: _Optional[str] = ..., num_channels: _Optional[int] = ..., portnum: _Optional[int] = ..., sbt_host_params: _Optional[_Union[OracleSbtHostParams, _Mapping]] = ...) -> None: ...
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_HOST_FIELD_NUMBER: _ClassVar[int]
    NUM_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DB_UUID_FIELD_NUMBER: _ClassVar[int]
    DB_UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_DAYS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DG_PRIMARY_BACKUP_FIELD_NUMBER: _ClassVar[int]
    RMAN_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVELOG_KEEP_HOURS_FIELD_NUMBER: _ClassVar[int]
    host_info_vec: _containers.RepeatedCompositeFieldContainer[OracleDBChannelInfo.HostInfo]
    max_num_host: int
    num_channels: int
    db_uuid: str
    db_unique_name: str
    archivelog_keep_days: int
    enable_dg_primary_backup: bool
    rman_backup_type: OracleRmanBackupType.Type
    credentials: _credentials_pb2.Credentials
    archivelog_keep_hours: int
    def __init__(self, host_info_vec: _Optional[_Iterable[_Union[OracleDBChannelInfo.HostInfo, _Mapping]]] = ..., max_num_host: _Optional[int] = ..., num_channels: _Optional[int] = ..., db_uuid: _Optional[str] = ..., db_unique_name: _Optional[str] = ..., archivelog_keep_days: _Optional[int] = ..., enable_dg_primary_backup: bool = ..., rman_backup_type: _Optional[_Union[OracleRmanBackupType.Type, str]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., archivelog_keep_hours: _Optional[int] = ...) -> None: ...

class AdditionalOracleDBParams(_message.Message):
    __slots__ = ("app_entity_id", "db_info_channel_vec")
    APP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_CHANNEL_VEC_FIELD_NUMBER: _ClassVar[int]
    app_entity_id: int
    db_info_channel_vec: _containers.RepeatedCompositeFieldContainer[OracleDBChannelInfo]
    def __init__(self, app_entity_id: _Optional[int] = ..., db_info_channel_vec: _Optional[_Iterable[_Union[OracleDBChannelInfo, _Mapping]]] = ...) -> None: ...

class OracleSourceParams(_message.Message):
    __slots__ = ("additional_oracle_db_params_vec", "persist_mountpoints")
    ADDITIONAL_ORACLE_DB_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    PERSIST_MOUNTPOINTS_FIELD_NUMBER: _ClassVar[int]
    additional_oracle_db_params_vec: _containers.RepeatedCompositeFieldContainer[AdditionalOracleDBParams]
    persist_mountpoints: bool
    def __init__(self, additional_oracle_db_params_vec: _Optional[_Iterable[_Union[AdditionalOracleDBParams, _Mapping]]] = ..., persist_mountpoints: bool = ...) -> None: ...

class NasThrottlingParams(_message.Message):
    __slots__ = ("max_parallel_metadata_fetch_full_percentage", "max_parallel_metadata_fetch_incremental_percentage", "max_parallel_io_full_percentage", "max_parallel_io_incremental_percentage")
    MAX_PARALLEL_METADATA_FETCH_FULL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_PARALLEL_METADATA_FETCH_INCREMENTAL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_PARALLEL_IO_FULL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_PARALLEL_IO_INCREMENTAL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    max_parallel_metadata_fetch_full_percentage: int
    max_parallel_metadata_fetch_incremental_percentage: int
    max_parallel_io_full_percentage: int
    max_parallel_io_incremental_percentage: int
    def __init__(self, max_parallel_metadata_fetch_full_percentage: _Optional[int] = ..., max_parallel_metadata_fetch_incremental_percentage: _Optional[int] = ..., max_parallel_io_full_percentage: _Optional[int] = ..., max_parallel_io_incremental_percentage: _Optional[int] = ...) -> None: ...

class UdaThrottlingParams(_message.Message):
    __slots__ = ("max_backup_resources", "max_log_backup_resources", "max_restore_resources", "max_anyjob_resources")
    MAX_BACKUP_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_BACKUP_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MAX_RESTORE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MAX_ANYJOB_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    max_backup_resources: int
    max_log_backup_resources: int
    max_restore_resources: int
    max_anyjob_resources: int
    def __init__(self, max_backup_resources: _Optional[int] = ..., max_log_backup_resources: _Optional[int] = ..., max_restore_resources: _Optional[int] = ..., max_anyjob_resources: _Optional[int] = ...) -> None: ...

class AWSNativeBackupSourceParams(_message.Message):
    __slots__ = ("volume_exclusion_params",)
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    volume_exclusion_params: EBSVolumeExclusionParams
    def __init__(self, volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ...) -> None: ...

class AWSSnapshotManagerBackupSourceParams(_message.Message):
    __slots__ = ("volume_exclusion_params",)
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    volume_exclusion_params: EBSVolumeExclusionParams
    def __init__(self, volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ...) -> None: ...

class GCPNativeObjectParams(_message.Message):
    __slots__ = ("disk_exclusion_params",)
    DISK_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    disk_exclusion_params: GCPDiskExclusionObjectParams
    def __init__(self, disk_exclusion_params: _Optional[_Union[GCPDiskExclusionObjectParams, _Mapping]] = ...) -> None: ...

class SharepointBackupSourceParams(_message.Message):
    __slots__ = ("autoprotect_entity",)
    AUTOPROTECT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    autoprotect_entity: bool
    def __init__(self, autoprotect_entity: bool = ...) -> None: ...

class S3BucketParamsProto(_message.Message):
    __slots__ = ("filtering_policies",)
    FILTERING_POLICIES_FIELD_NUMBER: _ClassVar[int]
    filtering_policies: _containers.RepeatedCompositeFieldContainer[FilteringPolicyProto]
    def __init__(self, filtering_policies: _Optional[_Iterable[_Union[FilteringPolicyProto, _Mapping]]] = ...) -> None: ...

class BackupSourceParams(_message.Message):
    __slots__ = ("source_id", "physical_params", "vmware_params", "hyperv_params", "oracle_params", "aws_native_params", "aws_snapshot_manager_params", "acropolis_params", "skip_indexing", "app_entity_id_vec", "sharepoint_params", "sfdc_params", "gcp_native_params", "s3_bucket_params_proto", "uda_backup_source_params", "kubernetes_params")
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_NATIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_SNAPSHOT_MANAGER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SKIP_INDEXING_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GCP_NATIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_PARAMS_PROTO_FIELD_NUMBER: _ClassVar[int]
    UDA_BACKUP_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_id: int
    physical_params: PhysicalBackupSourceParams
    vmware_params: VMwareBackupSourceParams
    hyperv_params: HyperVBackupSourceParams
    oracle_params: OracleSourceParams
    aws_native_params: AWSNativeBackupSourceParams
    aws_snapshot_manager_params: AWSSnapshotManagerBackupSourceParams
    acropolis_params: AcropolisBackupSourceParams
    skip_indexing: bool
    app_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    sharepoint_params: SharepointBackupSourceParams
    sfdc_params: _sfdc_pb2.SfdcBackupSourceParamsProto
    gcp_native_params: GCPNativeObjectParams
    s3_bucket_params_proto: S3BucketParamsProto
    uda_backup_source_params: UdaBackupSourceParams
    kubernetes_params: KubernetesBackupSourceParams
    def __init__(self, source_id: _Optional[int] = ..., physical_params: _Optional[_Union[PhysicalBackupSourceParams, _Mapping]] = ..., vmware_params: _Optional[_Union[VMwareBackupSourceParams, _Mapping]] = ..., hyperv_params: _Optional[_Union[HyperVBackupSourceParams, _Mapping]] = ..., oracle_params: _Optional[_Union[OracleSourceParams, _Mapping]] = ..., aws_native_params: _Optional[_Union[AWSNativeBackupSourceParams, _Mapping]] = ..., aws_snapshot_manager_params: _Optional[_Union[AWSSnapshotManagerBackupSourceParams, _Mapping]] = ..., acropolis_params: _Optional[_Union[AcropolisBackupSourceParams, _Mapping]] = ..., skip_indexing: bool = ..., app_entity_id_vec: _Optional[_Iterable[int]] = ..., sharepoint_params: _Optional[_Union[SharepointBackupSourceParams, _Mapping]] = ..., sfdc_params: _Optional[_Union[_sfdc_pb2.SfdcBackupSourceParamsProto, _Mapping]] = ..., gcp_native_params: _Optional[_Union[GCPNativeObjectParams, _Mapping]] = ..., s3_bucket_params_proto: _Optional[_Union[S3BucketParamsProto, _Mapping]] = ..., uda_backup_source_params: _Optional[_Union[UdaBackupSourceParams, _Mapping]] = ..., kubernetes_params: _Optional[_Union[KubernetesBackupSourceParams, _Mapping]] = ...) -> None: ...

class FilteringPolicyProto(_message.Message):
    __slots__ = ("allow_filters", "deny_filters")
    ALLOW_FILTERS_FIELD_NUMBER: _ClassVar[int]
    DENY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    allow_filters: _containers.RepeatedScalarFieldContainer[str]
    deny_filters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allow_filters: _Optional[_Iterable[str]] = ..., deny_filters: _Optional[_Iterable[str]] = ...) -> None: ...

class NasBackupParams(_message.Message):
    __slots__ = ("filtering_policy", "mixed_mode_preference", "nfs_version_preference", "continue_on_error", "snapshot_change_enabled", "full_backup_snapshot_label", "incremental_backup_snapshot_label", "encryption_enabled", "blacklisted_ip_addrs", "whitelisted_ip_addrs", "fld_config", "backup_all_existing_snapshot", "is_source_initiated_backup", "s3viewbackupproperties", "throttling_params", "modify_source_permissions", "shared_view_name")
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    MIXED_MODE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    NFS_VERSION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CHANGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_SNAPSHOT_LABEL_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_SNAPSHOT_LABEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ALL_EXISTING_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    IS_SOURCE_INITIATED_BACKUP_FIELD_NUMBER: _ClassVar[int]
    S3VIEWBACKUPPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MODIFY_SOURCE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SHARED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: FilteringPolicyProto
    mixed_mode_preference: _enums_pb2.NasProtocol.Type
    nfs_version_preference: _enums_pb2.NasProtocol.Type
    continue_on_error: bool
    snapshot_change_enabled: bool
    full_backup_snapshot_label: str
    incremental_backup_snapshot_label: str
    encryption_enabled: bool
    blacklisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    whitelisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    fld_config: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig
    backup_all_existing_snapshot: bool
    is_source_initiated_backup: bool
    s3viewbackupproperties: S3ViewBackupProperties
    throttling_params: NasThrottlingParams
    modify_source_permissions: bool
    shared_view_name: str
    def __init__(self, filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., mixed_mode_preference: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., nfs_version_preference: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., continue_on_error: bool = ..., snapshot_change_enabled: bool = ..., full_backup_snapshot_label: _Optional[str] = ..., incremental_backup_snapshot_label: _Optional[str] = ..., encryption_enabled: bool = ..., blacklisted_ip_addrs: _Optional[_Iterable[str]] = ..., whitelisted_ip_addrs: _Optional[_Iterable[str]] = ..., fld_config: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig, _Mapping]] = ..., backup_all_existing_snapshot: bool = ..., is_source_initiated_backup: bool = ..., s3viewbackupproperties: _Optional[_Union[S3ViewBackupProperties, _Mapping]] = ..., throttling_params: _Optional[_Union[NasThrottlingParams, _Mapping]] = ..., modify_source_permissions: bool = ..., shared_view_name: _Optional[str] = ...) -> None: ...

class S3ViewBackupProperties(_message.Message):
    __slots__ = ("s3_config", "access_key", "secret_key", "view_id", "snapshot_prefix_name")
    S3_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PREFIX_NAME_FIELD_NUMBER: _ClassVar[int]
    s3_config: _s3_metadata_pb2.S3BucketConfigProto
    access_key: str
    secret_key: str
    view_id: int
    snapshot_prefix_name: str
    def __init__(self, s3_config: _Optional[_Union[_s3_metadata_pb2.S3BucketConfigProto, _Mapping]] = ..., access_key: _Optional[str] = ..., secret_key: _Optional[str] = ..., view_id: _Optional[int] = ..., snapshot_prefix_name: _Optional[str] = ...) -> None: ...

class PhysicalBackupEnvParams(_message.Message):
    __slots__ = ("enable_incremental_backup_after_restart", "filtering_policy", "cobmr_backup", "vss_excluded_writers")
    ENABLE_INCREMENTAL_BACKUP_AFTER_RESTART_FIELD_NUMBER: _ClassVar[int]
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    COBMR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    VSS_EXCLUDED_WRITERS_FIELD_NUMBER: _ClassVar[int]
    enable_incremental_backup_after_restart: bool
    filtering_policy: FilteringPolicyProto
    cobmr_backup: bool
    vss_excluded_writers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enable_incremental_backup_after_restart: bool = ..., filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., cobmr_backup: bool = ..., vss_excluded_writers: _Optional[_Iterable[str]] = ...) -> None: ...

class VMwareBackupEnvParams(_message.Message):
    __slots__ = ("allow_crash_consistent_snapshot", "allow_vms_with_physical_rdm_disks", "vmware_disk_exclusion_info", "allow_nbdssl_transport_fallback", "enable_cbt_allowed", "vapps_to_vms_list")
    class VAppChildVMsList(_message.Message):
        __slots__ = ("vapp_entity_id", "vm_entity_ids")
        VAPP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        VM_ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
        vapp_entity_id: int
        vm_entity_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, vapp_entity_id: _Optional[int] = ..., vm_entity_ids: _Optional[_Iterable[int]] = ...) -> None: ...
    ALLOW_CRASH_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_VMS_WITH_PHYSICAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NBDSSL_TRANSPORT_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CBT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    VAPPS_TO_VMS_LIST_FIELD_NUMBER: _ClassVar[int]
    allow_crash_consistent_snapshot: bool
    allow_vms_with_physical_rdm_disks: bool
    vmware_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[VMwareDiskExclusionProto]
    allow_nbdssl_transport_fallback: bool
    enable_cbt_allowed: bool
    vapps_to_vms_list: _containers.RepeatedCompositeFieldContainer[VMwareBackupEnvParams.VAppChildVMsList]
    def __init__(self, allow_crash_consistent_snapshot: bool = ..., allow_vms_with_physical_rdm_disks: bool = ..., vmware_disk_exclusion_info: _Optional[_Iterable[_Union[VMwareDiskExclusionProto, _Mapping]]] = ..., allow_nbdssl_transport_fallback: bool = ..., enable_cbt_allowed: bool = ..., vapps_to_vms_list: _Optional[_Iterable[_Union[VMwareBackupEnvParams.VAppChildVMsList, _Mapping]]] = ...) -> None: ...

class SqlBackupJobParams(_message.Message):
    __slots__ = ("user_db_preference_type", "backup_system_dbs", "use_aag_preferences_from_sql_server", "aag_backup_preference_type", "backup_database_volumes_only", "full_backup_type", "is_copy_only_full", "is_copy_only_log", "enable_checksum", "continue_after_error", "num_dbs_per_batch", "num_streams", "with_clause", "log_backup_num_streams", "log_backup_with_clause", "enable_incremental_backup_after_restart", "advanced_settings")
    class UserDatabaseBackupPreferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackupAllDatabases: _ClassVar[SqlBackupJobParams.UserDatabaseBackupPreferenceType]
        kBackupAllExceptAAGDatabases: _ClassVar[SqlBackupJobParams.UserDatabaseBackupPreferenceType]
        kBackupOnlyAAGDatabases: _ClassVar[SqlBackupJobParams.UserDatabaseBackupPreferenceType]
    kBackupAllDatabases: SqlBackupJobParams.UserDatabaseBackupPreferenceType
    kBackupAllExceptAAGDatabases: SqlBackupJobParams.UserDatabaseBackupPreferenceType
    kBackupOnlyAAGDatabases: SqlBackupJobParams.UserDatabaseBackupPreferenceType
    class FullBackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSqlVSSVolume: _ClassVar[SqlBackupJobParams.FullBackupType]
        kSqlVSSFile: _ClassVar[SqlBackupJobParams.FullBackupType]
        kSqlNative: _ClassVar[SqlBackupJobParams.FullBackupType]
    kSqlVSSVolume: SqlBackupJobParams.FullBackupType
    kSqlVSSFile: SqlBackupJobParams.FullBackupType
    kSqlNative: SqlBackupJobParams.FullBackupType
    USER_DB_PREFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SYSTEM_DBS_FIELD_NUMBER: _ClassVar[int]
    USE_AAG_PREFERENCES_FROM_SQL_SERVER_FIELD_NUMBER: _ClassVar[int]
    AAG_BACKUP_PREFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DATABASE_VOLUMES_ONLY_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_ONLY_FULL_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_ONLY_LOG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AFTER_ERROR_FIELD_NUMBER: _ClassVar[int]
    NUM_DBS_PER_BATCH_FIELD_NUMBER: _ClassVar[int]
    NUM_STREAMS_FIELD_NUMBER: _ClassVar[int]
    WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_NUM_STREAMS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_WITH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INCREMENTAL_BACKUP_AFTER_RESTART_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    user_db_preference_type: SqlBackupJobParams.UserDatabaseBackupPreferenceType
    backup_system_dbs: bool
    use_aag_preferences_from_sql_server: bool
    aag_backup_preference_type: _sql_pb2.AAGBackupPreference.Type
    backup_database_volumes_only: bool
    full_backup_type: SqlBackupJobParams.FullBackupType
    is_copy_only_full: bool
    is_copy_only_log: bool
    enable_checksum: bool
    continue_after_error: bool
    num_dbs_per_batch: int
    num_streams: int
    with_clause: str
    log_backup_num_streams: int
    log_backup_with_clause: str
    enable_incremental_backup_after_restart: bool
    advanced_settings: _sql_pb2.AdvancedSettings
    def __init__(self, user_db_preference_type: _Optional[_Union[SqlBackupJobParams.UserDatabaseBackupPreferenceType, str]] = ..., backup_system_dbs: bool = ..., use_aag_preferences_from_sql_server: bool = ..., aag_backup_preference_type: _Optional[_Union[_sql_pb2.AAGBackupPreference.Type, str]] = ..., backup_database_volumes_only: bool = ..., full_backup_type: _Optional[_Union[SqlBackupJobParams.FullBackupType, str]] = ..., is_copy_only_full: bool = ..., is_copy_only_log: bool = ..., enable_checksum: bool = ..., continue_after_error: bool = ..., num_dbs_per_batch: _Optional[int] = ..., num_streams: _Optional[int] = ..., with_clause: _Optional[str] = ..., log_backup_num_streams: _Optional[int] = ..., log_backup_with_clause: _Optional[str] = ..., enable_incremental_backup_after_restart: bool = ..., advanced_settings: _Optional[_Union[_sql_pb2.AdvancedSettings, _Mapping]] = ...) -> None: ...

class OracleBackupJobParams(_message.Message):
    __slots__ = ("persist_mountpoints", "vlan_params", "log_auto_kill_timeout_secs", "incr_auto_kill_timeout_secs", "full_auto_kill_timeout_secs")
    PERSIST_MOUNTPOINTS_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOG_AUTO_KILL_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    INCR_AUTO_KILL_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    FULL_AUTO_KILL_TIMEOUT_SECS_FIELD_NUMBER: _ClassVar[int]
    persist_mountpoints: bool
    vlan_params: _common_pb2.VlanParams
    log_auto_kill_timeout_secs: int
    incr_auto_kill_timeout_secs: int
    full_auto_kill_timeout_secs: int
    def __init__(self, persist_mountpoints: bool = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ..., log_auto_kill_timeout_secs: _Optional[int] = ..., incr_auto_kill_timeout_secs: _Optional[int] = ..., full_auto_kill_timeout_secs: _Optional[int] = ...) -> None: ...

class AcropolisBackupJobParams(_message.Message):
    __slots__ = ("acropolis_disk_exclusion_info", "acropolis_disk_inclusion_info")
    ACROPOLIS_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    acropolis_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[AcropolisDiskFilterProto]
    acropolis_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[AcropolisDiskFilterProto]
    def __init__(self, acropolis_disk_exclusion_info: _Optional[_Iterable[_Union[AcropolisDiskFilterProto, _Mapping]]] = ..., acropolis_disk_inclusion_info: _Optional[_Iterable[_Union[AcropolisDiskFilterProto, _Mapping]]] = ...) -> None: ...

class SanBackupJobParams(_message.Message):
    __slots__ = ("use_secured_snapshot",)
    USE_SECURED_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    use_secured_snapshot: bool
    def __init__(self, use_secured_snapshot: bool = ...) -> None: ...

class ExternallyTriggeredJobParams(_message.Message):
    __slots__ = ("client_type", "sbt_params", "tags")
    class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGeneric: _ClassVar[ExternallyTriggeredJobParams.ClientType]
        kSbt: _ClassVar[ExternallyTriggeredJobParams.ClientType]
    kGeneric: ExternallyTriggeredJobParams.ClientType
    kSbt: ExternallyTriggeredJobParams.ClientType
    class ExternallyTriggeredSbtParams(_message.Message):
        __slots__ = ("catalog_view",)
        CATALOG_VIEW_FIELD_NUMBER: _ClassVar[int]
        catalog_view: str
        def __init__(self, catalog_view: _Optional[str] = ...) -> None: ...
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SBT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    client_type: ExternallyTriggeredJobParams.ClientType
    sbt_params: ExternallyTriggeredJobParams.ExternallyTriggeredSbtParams
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_type: _Optional[_Union[ExternallyTriggeredJobParams.ClientType, str]] = ..., sbt_params: _Optional[_Union[ExternallyTriggeredJobParams.ExternallyTriggeredSbtParams, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class HyperVBackupEnvParams(_message.Message):
    __slots__ = ("allow_crash_consistent_snapshot", "backup_job_type", "hyperv_disk_exclusion_info", "hyperv_disk_inclusion_info")
    class BackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAuto: _ClassVar[HyperVBackupEnvParams.BackupType]
        kRctBackup: _ClassVar[HyperVBackupEnvParams.BackupType]
        kVSSBackup: _ClassVar[HyperVBackupEnvParams.BackupType]
    kAuto: HyperVBackupEnvParams.BackupType
    kRctBackup: HyperVBackupEnvParams.BackupType
    kVSSBackup: HyperVBackupEnvParams.BackupType
    ALLOW_CRASH_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    HYPERV_DISK_INCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    allow_crash_consistent_snapshot: bool
    backup_job_type: HyperVBackupEnvParams.BackupType
    hyperv_disk_exclusion_info: _containers.RepeatedCompositeFieldContainer[HyperVDiskFilterProto]
    hyperv_disk_inclusion_info: _containers.RepeatedCompositeFieldContainer[HyperVDiskFilterProto]
    def __init__(self, allow_crash_consistent_snapshot: bool = ..., backup_job_type: _Optional[_Union[HyperVBackupEnvParams.BackupType, str]] = ..., hyperv_disk_exclusion_info: _Optional[_Iterable[_Union[HyperVDiskFilterProto, _Mapping]]] = ..., hyperv_disk_inclusion_info: _Optional[_Iterable[_Union[HyperVDiskFilterProto, _Mapping]]] = ...) -> None: ...

class AttributeFilterParams(_message.Message):
    __slots__ = ("attr_key", "attr_value_vec")
    ATTR_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTR_VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
    attr_key: _enums_pb2.AttributeType.Type
    attr_value_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, attr_key: _Optional[_Union[_enums_pb2.AttributeType.Type, str]] = ..., attr_value_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class AttributeFilterPolicy(_message.Message):
    __slots__ = ("inclusion_attr_params", "exclusion_attr_params")
    INCLUSION_ATTR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_ATTR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    inclusion_attr_params: _containers.RepeatedCompositeFieldContainer[AttributeFilterParams]
    exclusion_attr_params: _containers.RepeatedCompositeFieldContainer[AttributeFilterParams]
    def __init__(self, inclusion_attr_params: _Optional[_Iterable[_Union[AttributeFilterParams, _Mapping]]] = ..., exclusion_attr_params: _Optional[_Iterable[_Union[AttributeFilterParams, _Mapping]]] = ...) -> None: ...

class OutlookBackupEnvParams(_message.Message):
    __slots__ = ("filtering_policy", "should_backup_mailbox", "attr_filter_policy")
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BACKUP_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    ATTR_FILTER_POLICY_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: FilteringPolicyProto
    should_backup_mailbox: bool
    attr_filter_policy: AttributeFilterPolicy
    def __init__(self, filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., should_backup_mailbox: bool = ..., attr_filter_policy: _Optional[_Union[AttributeFilterPolicy, _Mapping]] = ...) -> None: ...

class OneDriveBackupEnvParams(_message.Message):
    __slots__ = ("filtering_policy", "should_backup_onedrive", "attr_filter_policy", "phl_params")
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SHOULD_BACKUP_ONEDRIVE_FIELD_NUMBER: _ClassVar[int]
    ATTR_FILTER_POLICY_FIELD_NUMBER: _ClassVar[int]
    PHL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: FilteringPolicyProto
    should_backup_onedrive: bool
    attr_filter_policy: AttributeFilterPolicy
    phl_params: _o365_pb2.PreservationHoldLibraryProtectionParams
    def __init__(self, filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., should_backup_onedrive: bool = ..., attr_filter_policy: _Optional[_Union[AttributeFilterPolicy, _Mapping]] = ..., phl_params: _Optional[_Union[_o365_pb2.PreservationHoldLibraryProtectionParams, _Mapping]] = ...) -> None: ...

class SharepPointSiteBackupEnvParams(_message.Message):
    __slots__ = ("doc_lib_filtering_policy", "phl_params")
    DOC_LIB_FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    PHL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    doc_lib_filtering_policy: FilteringPolicyProto
    phl_params: _o365_pb2.PreservationHoldLibraryProtectionParams
    def __init__(self, doc_lib_filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., phl_params: _Optional[_Union[_o365_pb2.PreservationHoldLibraryProtectionParams, _Mapping]] = ...) -> None: ...

class GroupBackupEnvParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TeamsBackupEnvParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublicFoldersBackupEnvParams(_message.Message):
    __slots__ = ("filtering_policy",)
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: FilteringPolicyProto
    def __init__(self, filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ...) -> None: ...

class O365BackupEnvParams(_message.Message):
    __slots__ = ("filtering_policy", "outlook_backup_params", "onedrive_backup_params", "site_backup_params", "public_folders_backup_params", "group_backup_params", "teams_backup_params")
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SITE_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDERS_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GROUP_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    filtering_policy: FilteringPolicyProto
    outlook_backup_params: OutlookBackupEnvParams
    onedrive_backup_params: OneDriveBackupEnvParams
    site_backup_params: SharepPointSiteBackupEnvParams
    public_folders_backup_params: PublicFoldersBackupEnvParams
    group_backup_params: GroupBackupEnvParams
    teams_backup_params: TeamsBackupEnvParams
    def __init__(self, filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., outlook_backup_params: _Optional[_Union[OutlookBackupEnvParams, _Mapping]] = ..., onedrive_backup_params: _Optional[_Union[OneDriveBackupEnvParams, _Mapping]] = ..., site_backup_params: _Optional[_Union[SharepPointSiteBackupEnvParams, _Mapping]] = ..., public_folders_backup_params: _Optional[_Union[PublicFoldersBackupEnvParams, _Mapping]] = ..., group_backup_params: _Optional[_Union[GroupBackupEnvParams, _Mapping]] = ..., teams_backup_params: _Optional[_Union[TeamsBackupEnvParams, _Mapping]] = ...) -> None: ...

class FileUptieringParams(_message.Message):
    __slots__ = ("source_view_name", "file_select_policy", "num_file_access", "hot_file_window", "file_size_policy", "file_size", "nfs_mount_path", "uptier_all_files", "source_view_map", "enable_audit_logging")
    class FileSelectPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLastAccessed: _ClassVar[FileUptieringParams.FileSelectPolicy]
        kLastModified: _ClassVar[FileUptieringParams.FileSelectPolicy]
    kLastAccessed: FileUptieringParams.FileSelectPolicy
    kLastModified: FileUptieringParams.FileSelectPolicy
    class FileSizePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGreaterThan: _ClassVar[FileUptieringParams.FileSizePolicy]
        kSmallerThan: _ClassVar[FileUptieringParams.FileSizePolicy]
    kGreaterThan: FileUptieringParams.FileSizePolicy
    kSmallerThan: FileUptieringParams.FileSizePolicy
    class SourceViewData(_message.Message):
        __slots__ = ("source_view_name", "nfs_mount_path")
        SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        source_view_name: str
        nfs_mount_path: str
        def __init__(self, source_view_name: _Optional[str] = ..., nfs_mount_path: _Optional[str] = ...) -> None: ...
    class SourceViewMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FileUptieringParams.SourceViewData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FileUptieringParams.SourceViewData, _Mapping]] = ...) -> None: ...
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SELECT_POLICY_FIELD_NUMBER: _ClassVar[int]
    NUM_FILE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    HOT_FILE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    UPTIER_ALL_FILES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_MAP_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    source_view_name: str
    file_select_policy: FileUptieringParams.FileSelectPolicy
    num_file_access: int
    hot_file_window: int
    file_size_policy: FileUptieringParams.FileSizePolicy
    file_size: int
    nfs_mount_path: str
    uptier_all_files: bool
    source_view_map: _containers.MessageMap[int, FileUptieringParams.SourceViewData]
    enable_audit_logging: bool
    def __init__(self, source_view_name: _Optional[str] = ..., file_select_policy: _Optional[_Union[FileUptieringParams.FileSelectPolicy, str]] = ..., num_file_access: _Optional[int] = ..., hot_file_window: _Optional[int] = ..., file_size_policy: _Optional[_Union[FileUptieringParams.FileSizePolicy, str]] = ..., file_size: _Optional[int] = ..., nfs_mount_path: _Optional[str] = ..., uptier_all_files: bool = ..., source_view_map: _Optional[_Mapping[int, FileUptieringParams.SourceViewData]] = ..., enable_audit_logging: bool = ...) -> None: ...

class ExchangeBackupJobParams(_message.Message):
    __slots__ = ("is_copy_only_full",)
    IS_COPY_ONLY_FULL_FIELD_NUMBER: _ClassVar[int]
    is_copy_only_full: bool
    def __init__(self, is_copy_only_full: bool = ...) -> None: ...

class NasAnalysisJobParams(_message.Message):
    __slots__ = ("file_type_buckets", "file_size_buckets", "access_time_buckets", "mod_time_buckets")
    class FileTypeBucket(_message.Message):
        __slots__ = ("file_type_bucket_name", "file_type_bucket_extensions")
        FILE_TYPE_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_TYPE_BUCKET_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
        file_type_bucket_name: str
        file_type_bucket_extensions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, file_type_bucket_name: _Optional[str] = ..., file_type_bucket_extensions: _Optional[_Iterable[str]] = ...) -> None: ...
    class FileSizeBucket(_message.Message):
        __slots__ = ("file_size_start_bytes", "file_size_end_bytes", "file_size_bucket_name")
        FILE_SIZE_START_BYTES_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_END_BYTES_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        file_size_start_bytes: int
        file_size_end_bytes: int
        file_size_bucket_name: str
        def __init__(self, file_size_start_bytes: _Optional[int] = ..., file_size_end_bytes: _Optional[int] = ..., file_size_bucket_name: _Optional[str] = ...) -> None: ...
    class AccessTimeBucket(_message.Message):
        __slots__ = ("access_time_start_days", "access_time_end_days", "access_time_bucket_name")
        ACCESS_TIME_START_DAYS_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TIME_END_DAYS_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TIME_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        access_time_start_days: int
        access_time_end_days: int
        access_time_bucket_name: str
        def __init__(self, access_time_start_days: _Optional[int] = ..., access_time_end_days: _Optional[int] = ..., access_time_bucket_name: _Optional[str] = ...) -> None: ...
    class ModTimeBucket(_message.Message):
        __slots__ = ("mod_time_start_days", "mod_time_end_days", "mod_time_bucket_name")
        MOD_TIME_START_DAYS_FIELD_NUMBER: _ClassVar[int]
        MOD_TIME_END_DAYS_FIELD_NUMBER: _ClassVar[int]
        MOD_TIME_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
        mod_time_start_days: int
        mod_time_end_days: int
        mod_time_bucket_name: str
        def __init__(self, mod_time_start_days: _Optional[int] = ..., mod_time_end_days: _Optional[int] = ..., mod_time_bucket_name: _Optional[str] = ...) -> None: ...
    FILE_TYPE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    file_type_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.FileTypeBucket]
    file_size_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.FileSizeBucket]
    access_time_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.AccessTimeBucket]
    mod_time_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.ModTimeBucket]
    def __init__(self, file_type_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.FileTypeBucket, _Mapping]]] = ..., file_size_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.FileSizeBucket, _Mapping]]] = ..., access_time_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.AccessTimeBucket, _Mapping]]] = ..., mod_time_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.ModTimeBucket, _Mapping]]] = ...) -> None: ...

class FileStubbingParams(_message.Message):
    __slots__ = ("target_view_name", "filtering_policy", "cold_file_window", "file_size", "file_select_policy", "file_size_policy", "nfs_mount_path", "migrate_without_stub", "delete_orphan_data", "target_view_prefix", "nfs_mount_path_prefix", "target_view_map", "tiering_goal", "enable_audit_logging", "enable_checksum_verification", "file_size_buckets", "access_time_buckets", "mod_time_buckets", "file_type_buckets", "denied_file_type_buckets")
    class FileSelectPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOlderThan: _ClassVar[FileStubbingParams.FileSelectPolicy]
        kLastAccessed: _ClassVar[FileStubbingParams.FileSelectPolicy]
        kLastModified: _ClassVar[FileStubbingParams.FileSelectPolicy]
        kAccessModTimeBuckets: _ClassVar[FileStubbingParams.FileSelectPolicy]
    kOlderThan: FileStubbingParams.FileSelectPolicy
    kLastAccessed: FileStubbingParams.FileSelectPolicy
    kLastModified: FileStubbingParams.FileSelectPolicy
    kAccessModTimeBuckets: FileStubbingParams.FileSelectPolicy
    class FileSizePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGreaterThan: _ClassVar[FileStubbingParams.FileSizePolicy]
        kSmallerThan: _ClassVar[FileStubbingParams.FileSizePolicy]
        kFileSizeBuckets: _ClassVar[FileStubbingParams.FileSizePolicy]
    kGreaterThan: FileStubbingParams.FileSizePolicy
    kSmallerThan: FileStubbingParams.FileSizePolicy
    kFileSizeBuckets: FileStubbingParams.FileSizePolicy
    class TargetViewData(_message.Message):
        __slots__ = ("target_view_name", "nfs_mount_path")
        TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        target_view_name: str
        nfs_mount_path: str
        def __init__(self, target_view_name: _Optional[str] = ..., nfs_mount_path: _Optional[str] = ...) -> None: ...
    class TargetViewMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FileStubbingParams.TargetViewData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FileStubbingParams.TargetViewData, _Mapping]] = ...) -> None: ...
    TARGET_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    COLD_FILE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_SELECT_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_POLICY_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    MIGRATE_WITHOUT_STUB_FIELD_NUMBER: _ClassVar[int]
    DELETE_ORPHAN_DATA_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNT_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    TARGET_VIEW_MAP_FIELD_NUMBER: _ClassVar[int]
    TIERING_GOAL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CHECKSUM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    MOD_TIME_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    DENIED_FILE_TYPE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    target_view_name: str
    filtering_policy: FilteringPolicyProto
    cold_file_window: int
    file_size: int
    file_select_policy: FileStubbingParams.FileSelectPolicy
    file_size_policy: FileStubbingParams.FileSizePolicy
    nfs_mount_path: str
    migrate_without_stub: bool
    delete_orphan_data: bool
    target_view_prefix: str
    nfs_mount_path_prefix: str
    target_view_map: _containers.MessageMap[int, FileStubbingParams.TargetViewData]
    tiering_goal: int
    enable_audit_logging: bool
    enable_checksum_verification: bool
    file_size_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.FileSizeBucket]
    access_time_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.AccessTimeBucket]
    mod_time_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.ModTimeBucket]
    file_type_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.FileTypeBucket]
    denied_file_type_buckets: _containers.RepeatedCompositeFieldContainer[NasAnalysisJobParams.FileTypeBucket]
    def __init__(self, target_view_name: _Optional[str] = ..., filtering_policy: _Optional[_Union[FilteringPolicyProto, _Mapping]] = ..., cold_file_window: _Optional[int] = ..., file_size: _Optional[int] = ..., file_select_policy: _Optional[_Union[FileStubbingParams.FileSelectPolicy, str]] = ..., file_size_policy: _Optional[_Union[FileStubbingParams.FileSizePolicy, str]] = ..., nfs_mount_path: _Optional[str] = ..., migrate_without_stub: bool = ..., delete_orphan_data: bool = ..., target_view_prefix: _Optional[str] = ..., nfs_mount_path_prefix: _Optional[str] = ..., target_view_map: _Optional[_Mapping[int, FileStubbingParams.TargetViewData]] = ..., tiering_goal: _Optional[int] = ..., enable_audit_logging: bool = ..., enable_checksum_verification: bool = ..., file_size_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.FileSizeBucket, _Mapping]]] = ..., access_time_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.AccessTimeBucket, _Mapping]]] = ..., mod_time_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.ModTimeBucket, _Mapping]]] = ..., file_type_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.FileTypeBucket, _Mapping]]] = ..., denied_file_type_buckets: _Optional[_Iterable[_Union[NasAnalysisJobParams.FileTypeBucket, _Mapping]]] = ...) -> None: ...

class IsilonEnvParams(_message.Message):
    __slots__ = ("zone_config_map",)
    class ZoneConfig(_message.Message):
        __slots__ = ("groupnet", "static_network_pool_config", "dynamic_network_pool_config", "smb_credentials")
        class NetworkPoolConfig(_message.Message):
            __slots__ = ("subnet", "pool_name", "use_smartconnect")
            SUBNET_FIELD_NUMBER: _ClassVar[int]
            POOL_NAME_FIELD_NUMBER: _ClassVar[int]
            USE_SMARTCONNECT_FIELD_NUMBER: _ClassVar[int]
            subnet: str
            pool_name: str
            use_smartconnect: bool
            def __init__(self, subnet: _Optional[str] = ..., pool_name: _Optional[str] = ..., use_smartconnect: bool = ...) -> None: ...
        GROUPNET_FIELD_NUMBER: _ClassVar[int]
        STATIC_NETWORK_POOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        DYNAMIC_NETWORK_POOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SMB_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        groupnet: str
        static_network_pool_config: IsilonEnvParams.ZoneConfig.NetworkPoolConfig
        dynamic_network_pool_config: IsilonEnvParams.ZoneConfig.NetworkPoolConfig
        smb_credentials: _credentials_pb2.NasMountCredentials
        def __init__(self, groupnet: _Optional[str] = ..., static_network_pool_config: _Optional[_Union[IsilonEnvParams.ZoneConfig.NetworkPoolConfig, _Mapping]] = ..., dynamic_network_pool_config: _Optional[_Union[IsilonEnvParams.ZoneConfig.NetworkPoolConfig, _Mapping]] = ..., smb_credentials: _Optional[_Union[_credentials_pb2.NasMountCredentials, _Mapping]] = ...) -> None: ...
    class ZoneConfigMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IsilonEnvParams.ZoneConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IsilonEnvParams.ZoneConfig, _Mapping]] = ...) -> None: ...
    ZONE_CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
    zone_config_map: _containers.MessageMap[str, IsilonEnvParams.ZoneConfig]
    def __init__(self, zone_config_map: _Optional[_Mapping[str, IsilonEnvParams.ZoneConfig]] = ...) -> None: ...

class AWSNativeEnvParams(_message.Message):
    __slots__ = ("volume_exclusion_params",)
    VOLUME_EXCLUSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    volume_exclusion_params: EBSVolumeExclusionParams
    def __init__(self, volume_exclusion_params: _Optional[_Union[EBSVolumeExclusionParams, _Mapping]] = ...) -> None: ...

class GCPNativeJobParams(_message.Message):
    __slots__ = ("disk_exclusion_rule_vec", "disk_exclusion_raw_query", "exclude_vm_without_disk")
    DISK_EXCLUSION_RULE_VEC_FIELD_NUMBER: _ClassVar[int]
    DISK_EXCLUSION_RAW_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_VM_WITHOUT_DISK_FIELD_NUMBER: _ClassVar[int]
    disk_exclusion_rule_vec: _containers.RepeatedCompositeFieldContainer[GCPJobDiskExclusionRule]
    disk_exclusion_raw_query: str
    exclude_vm_without_disk: bool
    def __init__(self, disk_exclusion_rule_vec: _Optional[_Iterable[_Union[GCPJobDiskExclusionRule, _Mapping]]] = ..., disk_exclusion_raw_query: _Optional[str] = ..., exclude_vm_without_disk: bool = ...) -> None: ...

class KubernetesEnvParams(_message.Message):
    __slots__ = ("include_params", "exclude_params", "leverage_csi_snapshot", "vlan_params")
    INCLUDE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_CSI_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VLAN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    include_params: K8sFilterParams
    exclude_params: K8sFilterParams
    leverage_csi_snapshot: bool
    vlan_params: _common_pb2.VlanParams
    def __init__(self, include_params: _Optional[_Union[K8sFilterParams, _Mapping]] = ..., exclude_params: _Optional[_Union[K8sFilterParams, _Mapping]] = ..., leverage_csi_snapshot: bool = ..., vlan_params: _Optional[_Union[_common_pb2.VlanParams, _Mapping]] = ...) -> None: ...

class S3BackupJobParams(_message.Message):
    __slots__ = ("storage_classes", "skip_files_on_error", "backup_object_acls")
    class StorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kS3Standard: _ClassVar[S3BackupJobParams.StorageClass]
        kS3IntelligentTiering: _ClassVar[S3BackupJobParams.StorageClass]
        kS3StandardIA: _ClassVar[S3BackupJobParams.StorageClass]
        kS3OneZoneIA: _ClassVar[S3BackupJobParams.StorageClass]
        kUnknown: _ClassVar[S3BackupJobParams.StorageClass]
    kS3Standard: S3BackupJobParams.StorageClass
    kS3IntelligentTiering: S3BackupJobParams.StorageClass
    kS3StandardIA: S3BackupJobParams.StorageClass
    kS3OneZoneIA: S3BackupJobParams.StorageClass
    kUnknown: S3BackupJobParams.StorageClass
    STORAGE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    SKIP_FILES_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    BACKUP_OBJECT_ACLS_FIELD_NUMBER: _ClassVar[int]
    storage_classes: _containers.RepeatedScalarFieldContainer[S3BackupJobParams.StorageClass]
    skip_files_on_error: bool
    backup_object_acls: bool
    def __init__(self, storage_classes: _Optional[_Iterable[_Union[S3BackupJobParams.StorageClass, str]]] = ..., skip_files_on_error: bool = ..., backup_object_acls: bool = ...) -> None: ...

class EnvBackupParams(_message.Message):
    __slots__ = ("nas_backup_params", "physical_backup_params", "vmware_backup_params", "sql_backup_job_params", "hyperv_backup_params", "outlook_backup_params", "file_stubbing_params", "o365_backup_params", "snapshot_manager_params", "file_uptiering_params", "nosql_backup_job_params", "oracle_backup_job_params", "exchange_backup_job_params", "nas_analysis_job_params", "isilon_env_params", "uda_backup_job_params", "aws_native_env_params", "externally_triggered_job_params", "kubernetes_env_params", "sfdc_backup_job_params", "gcp_native_job_params", "s3_backup_job_params", "acropolis_backup_job_params", "azure_sql_env_params", "san_backup_job_params", "aws_rds_postgres_env_params")
    NAS_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SQL_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OUTLOOK_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_STUBBING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    O365_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_MANAGER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FILE_UPTIERING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NOSQL_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NAS_ANALYSIS_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ISILON_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_NATIVE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_TRIGGERED_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GCP_NATIVE_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AZURE_SQL_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SAN_BACKUP_JOB_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_RDS_POSTGRES_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    nas_backup_params: NasBackupParams
    physical_backup_params: PhysicalBackupEnvParams
    vmware_backup_params: VMwareBackupEnvParams
    sql_backup_job_params: SqlBackupJobParams
    hyperv_backup_params: HyperVBackupEnvParams
    outlook_backup_params: OutlookBackupEnvParams
    file_stubbing_params: FileStubbingParams
    o365_backup_params: O365BackupEnvParams
    snapshot_manager_params: SnapshotManagerParams
    file_uptiering_params: FileUptieringParams
    nosql_backup_job_params: _nosql_pb2.NoSqlBackupJobParams
    oracle_backup_job_params: OracleBackupJobParams
    exchange_backup_job_params: ExchangeBackupJobParams
    nas_analysis_job_params: NasAnalysisJobParams
    isilon_env_params: IsilonEnvParams
    uda_backup_job_params: _uda_pb2.UdaBackupJobParams
    aws_native_env_params: AWSNativeEnvParams
    externally_triggered_job_params: ExternallyTriggeredJobParams
    kubernetes_env_params: KubernetesEnvParams
    sfdc_backup_job_params: _sfdc_pb2.SfdcBackupJobParams
    gcp_native_job_params: GCPNativeJobParams
    s3_backup_job_params: S3BackupJobParams
    acropolis_backup_job_params: AcropolisBackupJobParams
    azure_sql_env_params: _azure_sql_pb2.AzureSqlEnvBackupParamsProto
    san_backup_job_params: SanBackupJobParams
    aws_rds_postgres_env_params: _aws_pb2.AwsRDSPostgresEnvBackupParams
    def __init__(self, nas_backup_params: _Optional[_Union[NasBackupParams, _Mapping]] = ..., physical_backup_params: _Optional[_Union[PhysicalBackupEnvParams, _Mapping]] = ..., vmware_backup_params: _Optional[_Union[VMwareBackupEnvParams, _Mapping]] = ..., sql_backup_job_params: _Optional[_Union[SqlBackupJobParams, _Mapping]] = ..., hyperv_backup_params: _Optional[_Union[HyperVBackupEnvParams, _Mapping]] = ..., outlook_backup_params: _Optional[_Union[OutlookBackupEnvParams, _Mapping]] = ..., file_stubbing_params: _Optional[_Union[FileStubbingParams, _Mapping]] = ..., o365_backup_params: _Optional[_Union[O365BackupEnvParams, _Mapping]] = ..., snapshot_manager_params: _Optional[_Union[SnapshotManagerParams, _Mapping]] = ..., file_uptiering_params: _Optional[_Union[FileUptieringParams, _Mapping]] = ..., nosql_backup_job_params: _Optional[_Union[_nosql_pb2.NoSqlBackupJobParams, _Mapping]] = ..., oracle_backup_job_params: _Optional[_Union[OracleBackupJobParams, _Mapping]] = ..., exchange_backup_job_params: _Optional[_Union[ExchangeBackupJobParams, _Mapping]] = ..., nas_analysis_job_params: _Optional[_Union[NasAnalysisJobParams, _Mapping]] = ..., isilon_env_params: _Optional[_Union[IsilonEnvParams, _Mapping]] = ..., uda_backup_job_params: _Optional[_Union[_uda_pb2.UdaBackupJobParams, _Mapping]] = ..., aws_native_env_params: _Optional[_Union[AWSNativeEnvParams, _Mapping]] = ..., externally_triggered_job_params: _Optional[_Union[ExternallyTriggeredJobParams, _Mapping]] = ..., kubernetes_env_params: _Optional[_Union[KubernetesEnvParams, _Mapping]] = ..., sfdc_backup_job_params: _Optional[_Union[_sfdc_pb2.SfdcBackupJobParams, _Mapping]] = ..., gcp_native_job_params: _Optional[_Union[GCPNativeJobParams, _Mapping]] = ..., s3_backup_job_params: _Optional[_Union[S3BackupJobParams, _Mapping]] = ..., acropolis_backup_job_params: _Optional[_Union[AcropolisBackupJobParams, _Mapping]] = ..., azure_sql_env_params: _Optional[_Union[_azure_sql_pb2.AzureSqlEnvBackupParamsProto, _Mapping]] = ..., san_backup_job_params: _Optional[_Union[SanBackupJobParams, _Mapping]] = ..., aws_rds_postgres_env_params: _Optional[_Union[_aws_pb2.AwsRDSPostgresEnvBackupParams, _Mapping]] = ...) -> None: ...

class GCPDiskExclusionObjectParams(_message.Message):
    __slots__ = ("disk_name_vec",)
    DISK_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, disk_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GCPJobDiskExclusionRule(_message.Message):
    __slots__ = ("disk_name", "disk_type", "label_vec")
    class Label(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
    disk_name: str
    disk_type: str
    label_vec: _containers.RepeatedCompositeFieldContainer[GCPJobDiskExclusionRule.Label]
    def __init__(self, disk_name: _Optional[str] = ..., disk_type: _Optional[str] = ..., label_vec: _Optional[_Iterable[_Union[GCPJobDiskExclusionRule.Label, _Mapping]]] = ...) -> None: ...

class EBSVolumeExclusionParams(_message.Message):
    __slots__ = ("volume_id_vec", "max_volume_size_bytes", "volume_type_vec", "device_name_vec", "tag_params_vec", "raw_query")
    class Tag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TagParams(_message.Message):
        __slots__ = ("exclusion_tag_vec", "inclusion_tag_vec")
        EXCLUSION_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
        INCLUSION_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
        exclusion_tag_vec: _containers.RepeatedCompositeFieldContainer[EBSVolumeExclusionParams.Tag]
        inclusion_tag_vec: _containers.RepeatedCompositeFieldContainer[EBSVolumeExclusionParams.Tag]
        def __init__(self, exclusion_tag_vec: _Optional[_Iterable[_Union[EBSVolumeExclusionParams.Tag, _Mapping]]] = ..., inclusion_tag_vec: _Optional[_Iterable[_Union[EBSVolumeExclusionParams.Tag, _Mapping]]] = ...) -> None: ...
    VOLUME_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    TAG_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    RAW_QUERY_FIELD_NUMBER: _ClassVar[int]
    volume_id_vec: _containers.RepeatedScalarFieldContainer[str]
    max_volume_size_bytes: int
    volume_type_vec: _containers.RepeatedScalarFieldContainer[str]
    device_name_vec: _containers.RepeatedScalarFieldContainer[str]
    tag_params_vec: _containers.RepeatedCompositeFieldContainer[EBSVolumeExclusionParams.TagParams]
    raw_query: str
    def __init__(self, volume_id_vec: _Optional[_Iterable[str]] = ..., max_volume_size_bytes: _Optional[int] = ..., volume_type_vec: _Optional[_Iterable[str]] = ..., device_name_vec: _Optional[_Iterable[str]] = ..., tag_params_vec: _Optional[_Iterable[_Union[EBSVolumeExclusionParams.TagParams, _Mapping]]] = ..., raw_query: _Optional[str] = ...) -> None: ...

class K8sFilterParams(_message.Message):
    __slots__ = ("object_id_vec", "entity_vec", "label_vec_vec")
    class LabelVec(_message.Message):
        __slots__ = ("label_vec", "label_str_vec")
        LABEL_VEC_FIELD_NUMBER: _ClassVar[int]
        LABEL_STR_VEC_FIELD_NUMBER: _ClassVar[int]
        label_vec: _containers.RepeatedScalarFieldContainer[int]
        label_str_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, label_vec: _Optional[_Iterable[int]] = ..., label_str_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    OBJECT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    LABEL_VEC_VEC_FIELD_NUMBER: _ClassVar[int]
    object_id_vec: _containers.RepeatedScalarFieldContainer[int]
    entity_vec: _containers.RepeatedCompositeFieldContainer[_kubernetes_pb2.Entity]
    label_vec_vec: _containers.RepeatedCompositeFieldContainer[K8sFilterParams.LabelVec]
    def __init__(self, object_id_vec: _Optional[_Iterable[int]] = ..., entity_vec: _Optional[_Iterable[_Union[_kubernetes_pb2.Entity, _Mapping]]] = ..., label_vec_vec: _Optional[_Iterable[_Union[K8sFilterParams.LabelVec, _Mapping]]] = ...) -> None: ...

class DataTransferInfo(_message.Message):
    __slots__ = ("is_private_network", "use_protection_job_info", "private_network_info_vec")
    class PrivateNetworkInfo(_message.Message):
        __slots__ = ("vpn", "location", "subnet", "region")
        VPN_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        SUBNET_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        vpn: _entity_pb2.EntityProto
        location: str
        subnet: _entity_pb2.EntityProto
        region: _entity_pb2.EntityProto
        def __init__(self, vpn: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., location: _Optional[str] = ..., subnet: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., region: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ...) -> None: ...
    IS_PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    USE_PROTECTION_JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NETWORK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    is_private_network: bool
    use_protection_job_info: bool
    private_network_info_vec: _containers.RepeatedCompositeFieldContainer[DataTransferInfo.PrivateNetworkInfo]
    def __init__(self, is_private_network: bool = ..., use_protection_job_info: bool = ..., private_network_info_vec: _Optional[_Iterable[_Union[DataTransferInfo.PrivateNetworkInfo, _Mapping]]] = ...) -> None: ...
