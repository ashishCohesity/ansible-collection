from magneto.api.common import aws_pb2 as _aws_pb2
from magneto.api.common import azure_pb2 as _azure_pb2
from magneto.api.common import azure_sql_pb2 as _azure_sql_pb2
from magneto.api.common import base_pb2 as _base_pb2
from magneto.api.common import filters_pb2 as _filters_pb2
from magneto.api.common import o365_pb2 as _o365_pb2
from magneto.api.common import oracle_pb2 as _oracle_pb2
from magneto.api.common import physical_pb2 as _physical_pb2
from magneto.api.common import s3_pb2 as _s3_pb2
from magneto.api.common import sql_pb2 as _sql_pb2
from magneto.api import enums_pb2 as _enums_pb2
from magneto.api import enum_wrappers_pb2 as _enum_wrappers_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.api.common import sfdc_pb2 as _sfdc_pb2
from magneto.api.common import uda_pb2 as _uda_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonBackupParamsProto(_message.Message):
    __slots__ = ("uid", "storage_domain_id", "policy_id", "priority", "start_time", "timezone", "backup_qos_principal", "abort_in_exclusion_window", "pause_in_blackout_window", "incremental_sla_time_mins", "log_backup_sla_time_mins", "full_backup_sla_time_mins", "alerting_policy", "end_time_usecs", "skip_rigel_for_backup")
    UID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ABORT_IN_EXCLUSION_WINDOW_FIELD_NUMBER: _ClassVar[int]
    PAUSE_IN_BLACKOUT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_SLA_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
    LOG_BACKUP_SLA_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_SLA_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
    ALERTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SKIP_RIGEL_FOR_BACKUP_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    storage_domain_id: int
    policy_id: str
    priority: _enums_pb2.PriorityProto.Type
    start_time: _magneto_external_base_pb2.Time
    timezone: str
    backup_qos_principal: _enum_wrappers_pb2.BackupQoSPrincipal
    abort_in_exclusion_window: bool
    pause_in_blackout_window: bool
    incremental_sla_time_mins: int
    log_backup_sla_time_mins: int
    full_backup_sla_time_mins: int
    alerting_policy: _magneto_external_base_pb2.BackupAlertingPolicyProto
    end_time_usecs: int
    skip_rigel_for_backup: bool
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., storage_domain_id: _Optional[int] = ..., policy_id: _Optional[str] = ..., priority: _Optional[_Union[_enums_pb2.PriorityProto.Type, str]] = ..., start_time: _Optional[_Union[_magneto_external_base_pb2.Time, _Mapping]] = ..., timezone: _Optional[str] = ..., backup_qos_principal: _Optional[_Union[_enum_wrappers_pb2.BackupQoSPrincipal, _Mapping]] = ..., abort_in_exclusion_window: bool = ..., pause_in_blackout_window: bool = ..., incremental_sla_time_mins: _Optional[int] = ..., log_backup_sla_time_mins: _Optional[int] = ..., full_backup_sla_time_mins: _Optional[int] = ..., alerting_policy: _Optional[_Union[_magneto_external_base_pb2.BackupAlertingPolicyProto, _Mapping]] = ..., end_time_usecs: _Optional[int] = ..., skip_rigel_for_backup: bool = ...) -> None: ...

class VirtualizationEnvBackupParamsProto(_message.Message):
    __slots__ = ("app_consistent_snapshot", "fallback_to_crash_consistent_snapshot", "global_exclude_disk_vec", "indexing_policy")
    APP_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TO_CRASH_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_EXCLUDE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    app_consistent_snapshot: bool
    fallback_to_crash_consistent_snapshot: bool
    global_exclude_disk_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.DiskInfoProto]
    indexing_policy: _base_pb2.IndexingPolicyProto
    def __init__(self, app_consistent_snapshot: bool = ..., fallback_to_crash_consistent_snapshot: bool = ..., global_exclude_disk_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.DiskInfoProto, _Mapping]]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ...) -> None: ...

class VMwareEnvBackupParamsProto(_message.Message):
    __slots__ = ("app_consistent_snapshot", "fallback_to_crash_consistent_snapshot", "skip_physical_rdm_disks", "leverage_san_transport", "global_exclude_disk_vec", "indexing_policy", "allow_nbdssl_transport_fallback", "leverage_nutanix_snapshots")
    APP_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TO_CRASH_CONSISTENT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SKIP_PHYSICAL_RDM_DISKS_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_SAN_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_EXCLUDE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NBDSSL_TRANSPORT_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    LEVERAGE_NUTANIX_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    app_consistent_snapshot: bool
    fallback_to_crash_consistent_snapshot: bool
    skip_physical_rdm_disks: bool
    leverage_san_transport: bool
    global_exclude_disk_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.DiskInfoProto]
    indexing_policy: _base_pb2.IndexingPolicyProto
    allow_nbdssl_transport_fallback: bool
    leverage_nutanix_snapshots: bool
    def __init__(self, app_consistent_snapshot: bool = ..., fallback_to_crash_consistent_snapshot: bool = ..., skip_physical_rdm_disks: bool = ..., leverage_san_transport: bool = ..., global_exclude_disk_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.DiskInfoProto, _Mapping]]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ..., allow_nbdssl_transport_fallback: bool = ..., leverage_nutanix_snapshots: bool = ...) -> None: ...

class HyperVEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params",)
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_params: VirtualizationEnvBackupParamsProto
    def __init__(self, common_params: _Optional[_Union[VirtualizationEnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class FileLevelDataLockConfig(_message.Message):
    __slots__ = ("protocol", "auto_lock_duration_usecs", "default_retention_duration_usecs", "min_retention_duration_usecs", "max_retention_duration_usecs", "hold_timestamp_usecs", "mode", "default_retention_duration_years")
    class ExplicitLockingProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSetReadOnly: _ClassVar[FileLevelDataLockConfig.ExplicitLockingProtocol]
        kSetAtime: _ClassVar[FileLevelDataLockConfig.ExplicitLockingProtocol]
    kSetReadOnly: FileLevelDataLockConfig.ExplicitLockingProtocol
    kSetAtime: FileLevelDataLockConfig.ExplicitLockingProtocol
    class ExplicitLockingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCompliance: _ClassVar[FileLevelDataLockConfig.ExplicitLockingMode]
        kEnterprise: _ClassVar[FileLevelDataLockConfig.ExplicitLockingMode]
    kCompliance: FileLevelDataLockConfig.ExplicitLockingMode
    kEnterprise: FileLevelDataLockConfig.ExplicitLockingMode
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    AUTO_LOCK_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    MIN_RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    MAX_RETENTION_DURATION_USECS_FIELD_NUMBER: _ClassVar[int]
    HOLD_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RETENTION_DURATION_YEARS_FIELD_NUMBER: _ClassVar[int]
    protocol: FileLevelDataLockConfig.ExplicitLockingProtocol
    auto_lock_duration_usecs: int
    default_retention_duration_usecs: int
    min_retention_duration_usecs: int
    max_retention_duration_usecs: int
    hold_timestamp_usecs: int
    mode: FileLevelDataLockConfig.ExplicitLockingMode
    default_retention_duration_years: int
    def __init__(self, protocol: _Optional[_Union[FileLevelDataLockConfig.ExplicitLockingProtocol, str]] = ..., auto_lock_duration_usecs: _Optional[int] = ..., default_retention_duration_usecs: _Optional[int] = ..., min_retention_duration_usecs: _Optional[int] = ..., max_retention_duration_usecs: _Optional[int] = ..., hold_timestamp_usecs: _Optional[int] = ..., mode: _Optional[_Union[FileLevelDataLockConfig.ExplicitLockingMode, str]] = ..., default_retention_duration_years: _Optional[int] = ...) -> None: ...

class CommonNasEnvBackupParamsProto(_message.Message):
    __slots__ = ("mixed_mode_preference", "continue_on_error", "encryption_enabled", "blacklisted_ip_addrs", "whitelisted_ip_addrs", "indexing_policy", "filtering_policy", "fld_config", "pre_post_scripts")
    MIXED_MODE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_IP_ADDRS_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILTERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    FLD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    mixed_mode_preference: _enum_wrappers_pb2.NasProtocol
    continue_on_error: bool
    encryption_enabled: bool
    blacklisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    whitelisted_ip_addrs: _containers.RepeatedScalarFieldContainer[str]
    indexing_policy: _base_pb2.IndexingPolicyProto
    filtering_policy: _filters_pb2.FilteringPolicyProto
    fld_config: FileLevelDataLockConfig
    pre_post_scripts: _magneto_external_base_pb2.PrePostScriptsProto
    def __init__(self, mixed_mode_preference: _Optional[_Union[_enum_wrappers_pb2.NasProtocol, _Mapping]] = ..., continue_on_error: bool = ..., encryption_enabled: bool = ..., blacklisted_ip_addrs: _Optional[_Iterable[str]] = ..., whitelisted_ip_addrs: _Optional[_Iterable[str]] = ..., indexing_policy: _Optional[_Union[_base_pb2.IndexingPolicyProto, _Mapping]] = ..., filtering_policy: _Optional[_Union[_filters_pb2.FilteringPolicyProto, _Mapping]] = ..., fld_config: _Optional[_Union[FileLevelDataLockConfig, _Mapping]] = ..., pre_post_scripts: _Optional[_Union[_magneto_external_base_pb2.PrePostScriptsProto, _Mapping]] = ...) -> None: ...

class NetappEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params", "full_backup_snapshot_label", "incremental_backup_snapshot_label", "backup_all_existing_snapshot", "is_continuous_snapshotting_enabled", "max_allowed_source_snapshots")
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FULL_BACKUP_SNAPSHOT_LABEL_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_BACKUP_SNAPSHOT_LABEL_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ALL_EXISTING_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    IS_CONTINUOUS_SNAPSHOTTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOWED_SOURCE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    common_params: CommonNasEnvBackupParamsProto
    full_backup_snapshot_label: str
    incremental_backup_snapshot_label: str
    backup_all_existing_snapshot: bool
    is_continuous_snapshotting_enabled: bool
    max_allowed_source_snapshots: int
    def __init__(self, common_params: _Optional[_Union[CommonNasEnvBackupParamsProto, _Mapping]] = ..., full_backup_snapshot_label: _Optional[str] = ..., incremental_backup_snapshot_label: _Optional[str] = ..., backup_all_existing_snapshot: bool = ..., is_continuous_snapshotting_enabled: bool = ..., max_allowed_source_snapshots: _Optional[int] = ...) -> None: ...

class GenericNasEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params",)
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_params: CommonNasEnvBackupParamsProto
    def __init__(self, common_params: _Optional[_Union[CommonNasEnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class IsilonEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params", "snapshot_change_enabled", "is_continuous_snapshotting_enabled", "max_allowed_source_snapshots")
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CHANGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_CONTINUOUS_SNAPSHOTTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOWED_SOURCE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    common_params: CommonNasEnvBackupParamsProto
    snapshot_change_enabled: bool
    is_continuous_snapshotting_enabled: bool
    max_allowed_source_snapshots: int
    def __init__(self, common_params: _Optional[_Union[CommonNasEnvBackupParamsProto, _Mapping]] = ..., snapshot_change_enabled: bool = ..., is_continuous_snapshotting_enabled: bool = ..., max_allowed_source_snapshots: _Optional[int] = ...) -> None: ...

class FlashbladeEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params",)
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_params: CommonNasEnvBackupParamsProto
    def __init__(self, common_params: _Optional[_Union[CommonNasEnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class GPFSEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params",)
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_params: CommonNasEnvBackupParamsProto
    def __init__(self, common_params: _Optional[_Union[CommonNasEnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class ElastifileEnvBackupParamsProto(_message.Message):
    __slots__ = ("common_params",)
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_params: CommonNasEnvBackupParamsProto
    def __init__(self, common_params: _Optional[_Union[CommonNasEnvBackupParamsProto, _Mapping]] = ...) -> None: ...

class EnvSpecificBackupParamsProto(_message.Message):
    __slots__ = ("uid", "vmware_env_params", "netapp_env_params", "generic_nas_env_params", "isilon_env_params", "flashblade_env_params", "gpfs_env_params", "elastifile_env_params", "sql_env_params", "o365_env_params", "onedrive_env_params", "exchange_env_params", "sharepoint_env_params", "teams_env_params", "groups_env_params", "oracle_env_params", "aws_native_env_params", "aws_snapshot_manager_env_params", "aws_rds_snapshot_manager_env_params", "aws_aurora_snapshot_manager_env_params", "physical_env_params", "hyperv_env_params", "sfdc_env_params", "s3_env_params", "uda_env_params", "azure_sql_env_params", "azure_native_params", "aws_rds_postgres_env_params", "environment")
    UID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NETAPP_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GENERIC_NAS_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ISILON_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FLASHBLADE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GPFS_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ELASTIFILE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SQL_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    O365_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_NATIVE_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_SNAPSHOT_MANAGER_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_RDS_SNAPSHOT_MANAGER_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_AURORA_SNAPSHOT_MANAGER_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UDA_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AZURE_SQL_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AZURE_NATIVE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWS_RDS_POSTGRES_ENV_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    vmware_env_params: VMwareEnvBackupParamsProto
    netapp_env_params: NetappEnvBackupParamsProto
    generic_nas_env_params: GenericNasEnvBackupParamsProto
    isilon_env_params: IsilonEnvBackupParamsProto
    flashblade_env_params: FlashbladeEnvBackupParamsProto
    gpfs_env_params: GPFSEnvBackupParamsProto
    elastifile_env_params: ElastifileEnvBackupParamsProto
    sql_env_params: _sql_pb2.EnvBackupParamsProto
    o365_env_params: _o365_pb2.EnvBackupParamsProto
    onedrive_env_params: _o365_pb2.O365OneDriveEnvBackupParamsProto
    exchange_env_params: _o365_pb2.O365ExchangeEnvBackupParamsProto
    sharepoint_env_params: _o365_pb2.O365SharepointEnvBackupParamsProto
    teams_env_params: _o365_pb2.O365TeamsEnvBackupParamsProto
    groups_env_params: _o365_pb2.O365GroupsEnvBackupParamsProto
    oracle_env_params: _oracle_pb2.EnvBackupParamsProto
    aws_native_env_params: _aws_pb2.AWSNativeEnvBackupParams
    aws_snapshot_manager_env_params: _aws_pb2.AWSSnapshotManagerEnvBackupParams
    aws_rds_snapshot_manager_env_params: _aws_pb2.AWSRDSSnapshotManagerEnvBackupParams
    aws_aurora_snapshot_manager_env_params: _aws_pb2.AWSAuroraSnapshotManagerEnvBackupParams
    physical_env_params: _physical_pb2.EnvBackupParamsProto
    hyperv_env_params: HyperVEnvBackupParamsProto
    sfdc_env_params: _sfdc_pb2.EnvBackupParamsProto
    s3_env_params: _s3_pb2.S3BackupJobParams
    uda_env_params: _uda_pb2.EnvBackupParamsProto
    azure_sql_env_params: _azure_sql_pb2.AzureSqlEnvBackupParamsProto
    azure_native_params: _azure_pb2.AzureNativeBackupParams
    aws_rds_postgres_env_params: _aws_pb2.AwsRDSPostgresEnvBackupParams
    environment: _enum_wrappers_pb2.EnvironmentProto
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., vmware_env_params: _Optional[_Union[VMwareEnvBackupParamsProto, _Mapping]] = ..., netapp_env_params: _Optional[_Union[NetappEnvBackupParamsProto, _Mapping]] = ..., generic_nas_env_params: _Optional[_Union[GenericNasEnvBackupParamsProto, _Mapping]] = ..., isilon_env_params: _Optional[_Union[IsilonEnvBackupParamsProto, _Mapping]] = ..., flashblade_env_params: _Optional[_Union[FlashbladeEnvBackupParamsProto, _Mapping]] = ..., gpfs_env_params: _Optional[_Union[GPFSEnvBackupParamsProto, _Mapping]] = ..., elastifile_env_params: _Optional[_Union[ElastifileEnvBackupParamsProto, _Mapping]] = ..., sql_env_params: _Optional[_Union[_sql_pb2.EnvBackupParamsProto, _Mapping]] = ..., o365_env_params: _Optional[_Union[_o365_pb2.EnvBackupParamsProto, _Mapping]] = ..., onedrive_env_params: _Optional[_Union[_o365_pb2.O365OneDriveEnvBackupParamsProto, _Mapping]] = ..., exchange_env_params: _Optional[_Union[_o365_pb2.O365ExchangeEnvBackupParamsProto, _Mapping]] = ..., sharepoint_env_params: _Optional[_Union[_o365_pb2.O365SharepointEnvBackupParamsProto, _Mapping]] = ..., teams_env_params: _Optional[_Union[_o365_pb2.O365TeamsEnvBackupParamsProto, _Mapping]] = ..., groups_env_params: _Optional[_Union[_o365_pb2.O365GroupsEnvBackupParamsProto, _Mapping]] = ..., oracle_env_params: _Optional[_Union[_oracle_pb2.EnvBackupParamsProto, _Mapping]] = ..., aws_native_env_params: _Optional[_Union[_aws_pb2.AWSNativeEnvBackupParams, _Mapping]] = ..., aws_snapshot_manager_env_params: _Optional[_Union[_aws_pb2.AWSSnapshotManagerEnvBackupParams, _Mapping]] = ..., aws_rds_snapshot_manager_env_params: _Optional[_Union[_aws_pb2.AWSRDSSnapshotManagerEnvBackupParams, _Mapping]] = ..., aws_aurora_snapshot_manager_env_params: _Optional[_Union[_aws_pb2.AWSAuroraSnapshotManagerEnvBackupParams, _Mapping]] = ..., physical_env_params: _Optional[_Union[_physical_pb2.EnvBackupParamsProto, _Mapping]] = ..., hyperv_env_params: _Optional[_Union[HyperVEnvBackupParamsProto, _Mapping]] = ..., sfdc_env_params: _Optional[_Union[_sfdc_pb2.EnvBackupParamsProto, _Mapping]] = ..., s3_env_params: _Optional[_Union[_s3_pb2.S3BackupJobParams, _Mapping]] = ..., uda_env_params: _Optional[_Union[_uda_pb2.EnvBackupParamsProto, _Mapping]] = ..., azure_sql_env_params: _Optional[_Union[_azure_sql_pb2.AzureSqlEnvBackupParamsProto, _Mapping]] = ..., azure_native_params: _Optional[_Union[_azure_pb2.AzureNativeBackupParams, _Mapping]] = ..., aws_rds_postgres_env_params: _Optional[_Union[_aws_pb2.AwsRDSPostgresEnvBackupParams, _Mapping]] = ..., environment: _Optional[_Union[_enum_wrappers_pb2.EnvironmentProto, _Mapping]] = ...) -> None: ...

class VirtualizationBackupSourceParamsProto(_message.Message):
    __slots__ = ("exclude_disk_vec", "is_vss_copy_only")
    EXCLUDE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_VSS_COPY_ONLY_FIELD_NUMBER: _ClassVar[int]
    exclude_disk_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.DiskInfoProto]
    is_vss_copy_only: bool
    def __init__(self, exclude_disk_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.DiskInfoProto, _Mapping]]] = ..., is_vss_copy_only: bool = ...) -> None: ...

class VMwareBackupSourceParamsProto(_message.Message):
    __slots__ = ("exclude_disk_vec", "truncate_exchange_logs")
    EXCLUDE_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_EXCHANGE_LOGS_FIELD_NUMBER: _ClassVar[int]
    exclude_disk_vec: _containers.RepeatedCompositeFieldContainer[_magneto_external_base_pb2.DiskInfoProto]
    truncate_exchange_logs: bool
    def __init__(self, exclude_disk_vec: _Optional[_Iterable[_Union[_magneto_external_base_pb2.DiskInfoProto, _Mapping]]] = ..., truncate_exchange_logs: bool = ...) -> None: ...

class HyperVBackupSourceParamsProto(_message.Message):
    __slots__ = ("common_params",)
    COMMON_PARAMS_FIELD_NUMBER: _ClassVar[int]
    common_params: VirtualizationBackupSourceParamsProto
    def __init__(self, common_params: _Optional[_Union[VirtualizationBackupSourceParamsProto, _Mapping]] = ...) -> None: ...

class ObjectSpecificBackupParamsProto(_message.Message):
    __slots__ = ("exclude_source_ids", "source_filters", "pre_post_scripts", "vmware_source_params", "oracle_source_params", "physical_source_params", "ec2_object_params", "hyperv_source_params", "sharepoint_source_params", "sfdc_source_params", "s3_bucket_params_proto", "uda_source_params")
    EXCLUDE_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PRE_POST_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ORACLE_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EC2_OBJECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HYPERV_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SFDC_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_PARAMS_PROTO_FIELD_NUMBER: _ClassVar[int]
    UDA_SOURCE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    exclude_source_ids: _containers.RepeatedScalarFieldContainer[int]
    source_filters: _filters_pb2.SourceFilters
    pre_post_scripts: _magneto_external_base_pb2.PrePostScriptsProto
    vmware_source_params: VMwareBackupSourceParamsProto
    oracle_source_params: _oracle_pb2.OracleBackupSourceParamsProto
    physical_source_params: _physical_pb2.PhysicalBackupSourceParamsProto
    ec2_object_params: _aws_pb2.EC2ObjectParamsProto
    hyperv_source_params: HyperVBackupSourceParamsProto
    sharepoint_source_params: _o365_pb2.SharepointBackupSourceParams
    sfdc_source_params: _sfdc_pb2.SfdcBackupSourceParamsProto
    s3_bucket_params_proto: _s3_pb2.S3BucketParamsProto
    uda_source_params: _uda_pb2.UdaBackupSourceParamsProto
    def __init__(self, exclude_source_ids: _Optional[_Iterable[int]] = ..., source_filters: _Optional[_Union[_filters_pb2.SourceFilters, _Mapping]] = ..., pre_post_scripts: _Optional[_Union[_magneto_external_base_pb2.PrePostScriptsProto, _Mapping]] = ..., vmware_source_params: _Optional[_Union[VMwareBackupSourceParamsProto, _Mapping]] = ..., oracle_source_params: _Optional[_Union[_oracle_pb2.OracleBackupSourceParamsProto, _Mapping]] = ..., physical_source_params: _Optional[_Union[_physical_pb2.PhysicalBackupSourceParamsProto, _Mapping]] = ..., ec2_object_params: _Optional[_Union[_aws_pb2.EC2ObjectParamsProto, _Mapping]] = ..., hyperv_source_params: _Optional[_Union[HyperVBackupSourceParamsProto, _Mapping]] = ..., sharepoint_source_params: _Optional[_Union[_o365_pb2.SharepointBackupSourceParams, _Mapping]] = ..., sfdc_source_params: _Optional[_Union[_sfdc_pb2.SfdcBackupSourceParamsProto, _Mapping]] = ..., s3_bucket_params_proto: _Optional[_Union[_s3_pb2.S3BucketParamsProto, _Mapping]] = ..., uda_source_params: _Optional[_Union[_uda_pb2.UdaBackupSourceParamsProto, _Mapping]] = ...) -> None: ...

class ObjectBackupSpecificationProto(_message.Message):
    __slots__ = ("uid", "owner_object_id", "common_backup_params_uid", "env_specific_params_uid", "object_specific_params")
    UID_FIELD_NUMBER: _ClassVar[int]
    OWNER_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMON_BACKUP_PARAMS_UID_FIELD_NUMBER: _ClassVar[int]
    ENV_SPECIFIC_PARAMS_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    owner_object_id: int
    common_backup_params_uid: _universal_id_pb2.UniversalIdProto
    env_specific_params_uid: _universal_id_pb2.UniversalIdProto
    object_specific_params: ObjectSpecificBackupParamsProto
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., owner_object_id: _Optional[int] = ..., common_backup_params_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., env_specific_params_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_specific_params: _Optional[_Union[ObjectSpecificBackupParamsProto, _Mapping]] = ...) -> None: ...

class ObjectSpecInfo(_message.Message):
    __slots__ = ("uid", "owner_object_id", "owner_object_string_id", "exclude_source_string_ids", "common_backup_params", "env_specific_params", "object_specific_params", "is_paused", "is_active", "creation_time_usecs", "last_modification_time_usecs", "global_policy_id")
    UID_FIELD_NUMBER: _ClassVar[int]
    OWNER_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_OBJECT_STRING_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOURCE_STRING_IDS_FIELD_NUMBER: _ClassVar[int]
    COMMON_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENV_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SPECIFIC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_PAUSED_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    owner_object_id: int
    owner_object_string_id: str
    exclude_source_string_ids: _containers.RepeatedScalarFieldContainer[str]
    common_backup_params: CommonBackupParamsProto
    env_specific_params: EnvSpecificBackupParamsProto
    object_specific_params: ObjectSpecificBackupParamsProto
    is_paused: bool
    is_active: bool
    creation_time_usecs: int
    last_modification_time_usecs: int
    global_policy_id: str
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., owner_object_id: _Optional[int] = ..., owner_object_string_id: _Optional[str] = ..., exclude_source_string_ids: _Optional[_Iterable[str]] = ..., common_backup_params: _Optional[_Union[CommonBackupParamsProto, _Mapping]] = ..., env_specific_params: _Optional[_Union[EnvSpecificBackupParamsProto, _Mapping]] = ..., object_specific_params: _Optional[_Union[ObjectSpecificBackupParamsProto, _Mapping]] = ..., is_paused: bool = ..., is_active: bool = ..., creation_time_usecs: _Optional[int] = ..., last_modification_time_usecs: _Optional[int] = ..., global_policy_id: _Optional[str] = ...) -> None: ...
