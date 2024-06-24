from configs import cluster_config_pb2 as _cluster_config_pb2
from magneto.api import worm_pb2 as _worm_pb2
from magneto.base import cloud_deploy_pb2 as _cloud_deploy_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import env_params_pb2 as _env_params_pb2_1
from magneto.base import onprem_deploy_pb2 as _onprem_deploy_pb2
from magneto.base import permissions_pb2 as _permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Time(_message.Message):
    __slots__ = ("hour", "minute")
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    hour: int
    minute: int
    def __init__(self, hour: _Optional[int] = ..., minute: _Optional[int] = ...) -> None: ...

class DayTime(_message.Message):
    __slots__ = ("day", "time")
    DAY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    day: _enums_pb2.Day.Type
    time: Time
    def __init__(self, day: _Optional[_Union[_enums_pb2.Day.Type, str]] = ..., time: _Optional[_Union[Time, _Mapping]] = ...) -> None: ...

class DateTime(_message.Message):
    __slots__ = ("day_of_the_month", "month", "year", "time")
    DAY_OF_THE_MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    day_of_the_month: int
    month: int
    year: int
    time: Time
    def __init__(self, day_of_the_month: _Optional[int] = ..., month: _Optional[int] = ..., year: _Optional[int] = ..., time: _Optional[_Union[Time, _Mapping]] = ...) -> None: ...

class DayTimeWindow(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: DayTime
    end_time: DayTime
    def __init__(self, start_time: _Optional[_Union[DayTime, _Mapping]] = ..., end_time: _Optional[_Union[DayTime, _Mapping]] = ...) -> None: ...

class ExclusionTimeRange(_message.Message):
    __slots__ = ("day", "start_time", "end_time", "id")
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    day: _enums_pb2.Day.Type
    start_time: Time
    end_time: Time
    id: str
    def __init__(self, day: _Optional[_Union[_enums_pb2.Day.Type, str]] = ..., start_time: _Optional[_Union[Time, _Mapping]] = ..., end_time: _Optional[_Union[Time, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class ExclusionDates(_message.Message):
    __slots__ = ("dates_vec",)
    DATES_VEC_FIELD_NUMBER: _ClassVar[int]
    dates_vec: _containers.RepeatedCompositeFieldContainer[DateTime]
    def __init__(self, dates_vec: _Optional[_Iterable[_Union[DateTime, _Mapping]]] = ...) -> None: ...

class ReplicationTarget(_message.Message):
    __slots__ = ("cluster_id", "cluster_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: int
    cluster_name: str
    def __init__(self, cluster_id: _Optional[int] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class ArchivalTarget(_message.Message):
    __slots__ = ("vault_id", "type", "name", "cloud_tier_setting", "usage_type", "ownership_context")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloud: _ClassVar[ArchivalTarget.Type]
        kTape: _ClassVar[ArchivalTarget.Type]
        kNas: _ClassVar[ArchivalTarget.Type]
    kCloud: ArchivalTarget.Type
    kTape: ArchivalTarget.Type
    kNas: ArchivalTarget.Type
    class UsageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kArchival: _ClassVar[ArchivalTarget.UsageType]
        kRpaasArchival: _ClassVar[ArchivalTarget.UsageType]
    kArchival: ArchivalTarget.UsageType
    kRpaasArchival: ArchivalTarget.UsageType
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TIER_SETTING_FIELD_NUMBER: _ClassVar[int]
    USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    vault_id: int
    type: ArchivalTarget.Type
    name: str
    cloud_tier_setting: _cluster_config_pb2.ClusterConfigProto.Vault.CloudTierSetting
    usage_type: ArchivalTarget.UsageType
    ownership_context: _cluster_config_pb2.ClusterConfigProto.OwnershipContext
    def __init__(self, vault_id: _Optional[int] = ..., type: _Optional[_Union[ArchivalTarget.Type, str]] = ..., name: _Optional[str] = ..., cloud_tier_setting: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.CloudTierSetting, _Mapping]] = ..., usage_type: _Optional[_Union[ArchivalTarget.UsageType, str]] = ..., ownership_context: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.OwnershipContext, str]] = ...) -> None: ...

class CloudDeployTarget(_message.Message):
    __slots__ = ("type", "target_entity", "deploy_vms_to_cloud_params")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAzure: _ClassVar[CloudDeployTarget.Type]
        kAWS: _ClassVar[CloudDeployTarget.Type]
        kGCP: _ClassVar[CloudDeployTarget.Type]
    kAzure: CloudDeployTarget.Type
    kAWS: CloudDeployTarget.Type
    kGCP: CloudDeployTarget.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: CloudDeployTarget.Type
    target_entity: _entity_pb2.EntityProto
    deploy_vms_to_cloud_params: _cloud_deploy_pb2.DeployVMsToCloudParams
    def __init__(self, type: _Optional[_Union[CloudDeployTarget.Type, str]] = ..., target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., deploy_vms_to_cloud_params: _Optional[_Union[_cloud_deploy_pb2.DeployVMsToCloudParams, _Mapping]] = ...) -> None: ...

class OnPremDeployTarget(_message.Message):
    __slots__ = ("type", "target_entity", "deploy_vms_to_onprem_params")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_VMS_TO_ONPREM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    target_entity: _entity_pb2.EntityProto
    deploy_vms_to_onprem_params: _onprem_deploy_pb2.DeployVMsToOnPremParams
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., target_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., deploy_vms_to_onprem_params: _Optional[_Union[_onprem_deploy_pb2.DeployVMsToOnPremParams, _Mapping]] = ...) -> None: ...

class SnapshotTarget(_message.Message):
    __slots__ = ("type", "replication_target", "archival_target", "cloud_deploy_target", "onprem_deploy_target")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLocal: _ClassVar[SnapshotTarget.Type]
        kRemote: _ClassVar[SnapshotTarget.Type]
        kArchival: _ClassVar[SnapshotTarget.Type]
        kCloudDeploy: _ClassVar[SnapshotTarget.Type]
        kCloudReplication: _ClassVar[SnapshotTarget.Type]
        kOnPremDeploy: _ClassVar[SnapshotTarget.Type]
    kLocal: SnapshotTarget.Type
    kRemote: SnapshotTarget.Type
    kArchival: SnapshotTarget.Type
    kCloudDeploy: SnapshotTarget.Type
    kCloudReplication: SnapshotTarget.Type
    kOnPremDeploy: SnapshotTarget.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TARGET_FIELD_NUMBER: _ClassVar[int]
    ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DEPLOY_TARGET_FIELD_NUMBER: _ClassVar[int]
    ONPREM_DEPLOY_TARGET_FIELD_NUMBER: _ClassVar[int]
    type: SnapshotTarget.Type
    replication_target: ReplicationTarget
    archival_target: ArchivalTarget
    cloud_deploy_target: CloudDeployTarget
    onprem_deploy_target: OnPremDeployTarget
    def __init__(self, type: _Optional[_Union[SnapshotTarget.Type, str]] = ..., replication_target: _Optional[_Union[ReplicationTarget, _Mapping]] = ..., archival_target: _Optional[_Union[ArchivalTarget, _Mapping]] = ..., cloud_deploy_target: _Optional[_Union[CloudDeployTarget, _Mapping]] = ..., onprem_deploy_target: _Optional[_Union[OnPremDeployTarget, _Mapping]] = ...) -> None: ...

class GranularityBucket(_message.Message):
    __slots__ = ("granularity", "multiplier", "exact_dates")
    class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEvery: _ClassVar[GranularityBucket.Granularity]
        kHour: _ClassVar[GranularityBucket.Granularity]
        kDay: _ClassVar[GranularityBucket.Granularity]
        kWeek: _ClassVar[GranularityBucket.Granularity]
        kMonth: _ClassVar[GranularityBucket.Granularity]
        kYear: _ClassVar[GranularityBucket.Granularity]
        kExactDates: _ClassVar[GranularityBucket.Granularity]
    kEvery: GranularityBucket.Granularity
    kHour: GranularityBucket.Granularity
    kDay: GranularityBucket.Granularity
    kWeek: GranularityBucket.Granularity
    kMonth: GranularityBucket.Granularity
    kYear: GranularityBucket.Granularity
    kExactDates: GranularityBucket.Granularity
    class ExactDatesInfo(_message.Message):
        __slots__ = ("dates_vec",)
        DATES_VEC_FIELD_NUMBER: _ClassVar[int]
        dates_vec: _containers.RepeatedCompositeFieldContainer[DateTime]
        def __init__(self, dates_vec: _Optional[_Iterable[_Union[DateTime, _Mapping]]] = ...) -> None: ...
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    EXACT_DATES_FIELD_NUMBER: _ClassVar[int]
    granularity: GranularityBucket.Granularity
    multiplier: int
    exact_dates: GranularityBucket.ExactDatesInfo
    def __init__(self, granularity: _Optional[_Union[GranularityBucket.Granularity, str]] = ..., multiplier: _Optional[int] = ..., exact_dates: _Optional[_Union[GranularityBucket.ExactDatesInfo, _Mapping]] = ...) -> None: ...

class SchedulingPolicyProto(_message.Message):
    __slots__ = ("periodicity", "continuous_schedule", "daily_schedule", "monthly_schedule", "rpo_schedule", "date_schedule", "yearly_schedule")
    class Periodicity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kContinuous: _ClassVar[SchedulingPolicyProto.Periodicity]
        kDaily: _ClassVar[SchedulingPolicyProto.Periodicity]
        kMonthly: _ClassVar[SchedulingPolicyProto.Periodicity]
        kContinuousRPO: _ClassVar[SchedulingPolicyProto.Periodicity]
        kCDP: _ClassVar[SchedulingPolicyProto.Periodicity]
        kDate: _ClassVar[SchedulingPolicyProto.Periodicity]
        kYearly: _ClassVar[SchedulingPolicyProto.Periodicity]
    kContinuous: SchedulingPolicyProto.Periodicity
    kDaily: SchedulingPolicyProto.Periodicity
    kMonthly: SchedulingPolicyProto.Periodicity
    kContinuousRPO: SchedulingPolicyProto.Periodicity
    kCDP: SchedulingPolicyProto.Periodicity
    kDate: SchedulingPolicyProto.Periodicity
    kYearly: SchedulingPolicyProto.Periodicity
    class ContinuousSchedule(_message.Message):
        __slots__ = ("backup_interval_mins",)
        BACKUP_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
        backup_interval_mins: int
        def __init__(self, backup_interval_mins: _Optional[int] = ...) -> None: ...
    class DailySchedule(_message.Message):
        __slots__ = ("days", "frequency")
        DAYS_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        days: _containers.RepeatedScalarFieldContainer[_enums_pb2.Day.Type]
        frequency: int
        def __init__(self, days: _Optional[_Iterable[_Union[_enums_pb2.Day.Type, str]]] = ..., frequency: _Optional[int] = ...) -> None: ...
    class MonthlySchedule(_message.Message):
        __slots__ = ("day", "count", "day_of_month")
        class DayCountInMonth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFirst: _ClassVar[SchedulingPolicyProto.MonthlySchedule.DayCountInMonth]
            kSecond: _ClassVar[SchedulingPolicyProto.MonthlySchedule.DayCountInMonth]
            kThird: _ClassVar[SchedulingPolicyProto.MonthlySchedule.DayCountInMonth]
            kFourth: _ClassVar[SchedulingPolicyProto.MonthlySchedule.DayCountInMonth]
            kLast: _ClassVar[SchedulingPolicyProto.MonthlySchedule.DayCountInMonth]
        kFirst: SchedulingPolicyProto.MonthlySchedule.DayCountInMonth
        kSecond: SchedulingPolicyProto.MonthlySchedule.DayCountInMonth
        kThird: SchedulingPolicyProto.MonthlySchedule.DayCountInMonth
        kFourth: SchedulingPolicyProto.MonthlySchedule.DayCountInMonth
        kLast: SchedulingPolicyProto.MonthlySchedule.DayCountInMonth
        DAY_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
        day: _enums_pb2.Day.Type
        count: SchedulingPolicyProto.MonthlySchedule.DayCountInMonth
        day_of_month: int
        def __init__(self, day: _Optional[_Union[_enums_pb2.Day.Type, str]] = ..., count: _Optional[_Union[SchedulingPolicyProto.MonthlySchedule.DayCountInMonth, str]] = ..., day_of_month: _Optional[int] = ...) -> None: ...
    class YearlySchedule(_message.Message):
        __slots__ = ("day_of_the_year",)
        class DayOfTheYear(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kFirst: _ClassVar[SchedulingPolicyProto.YearlySchedule.DayOfTheYear]
            kLast: _ClassVar[SchedulingPolicyProto.YearlySchedule.DayOfTheYear]
        kFirst: SchedulingPolicyProto.YearlySchedule.DayOfTheYear
        kLast: SchedulingPolicyProto.YearlySchedule.DayOfTheYear
        DAY_OF_THE_YEAR_FIELD_NUMBER: _ClassVar[int]
        day_of_the_year: SchedulingPolicyProto.YearlySchedule.DayOfTheYear
        def __init__(self, day_of_the_year: _Optional[_Union[SchedulingPolicyProto.YearlySchedule.DayOfTheYear, str]] = ...) -> None: ...
    class RPOSchedule(_message.Message):
        __slots__ = ("rpo_interval_mins",)
        RPO_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
        rpo_interval_mins: int
        def __init__(self, rpo_interval_mins: _Optional[int] = ...) -> None: ...
    class DateSchedule(_message.Message):
        __slots__ = ("dates_vec",)
        DATES_VEC_FIELD_NUMBER: _ClassVar[int]
        dates_vec: _containers.RepeatedCompositeFieldContainer[DateTime]
        def __init__(self, dates_vec: _Optional[_Iterable[_Union[DateTime, _Mapping]]] = ...) -> None: ...
    PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DAILY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RPO_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DATE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    YEARLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    periodicity: SchedulingPolicyProto.Periodicity
    continuous_schedule: SchedulingPolicyProto.ContinuousSchedule
    daily_schedule: SchedulingPolicyProto.DailySchedule
    monthly_schedule: SchedulingPolicyProto.MonthlySchedule
    rpo_schedule: SchedulingPolicyProto.RPOSchedule
    date_schedule: SchedulingPolicyProto.DateSchedule
    yearly_schedule: SchedulingPolicyProto.YearlySchedule
    def __init__(self, periodicity: _Optional[_Union[SchedulingPolicyProto.Periodicity, str]] = ..., continuous_schedule: _Optional[_Union[SchedulingPolicyProto.ContinuousSchedule, _Mapping]] = ..., daily_schedule: _Optional[_Union[SchedulingPolicyProto.DailySchedule, _Mapping]] = ..., monthly_schedule: _Optional[_Union[SchedulingPolicyProto.MonthlySchedule, _Mapping]] = ..., rpo_schedule: _Optional[_Union[SchedulingPolicyProto.RPOSchedule, _Mapping]] = ..., date_schedule: _Optional[_Union[SchedulingPolicyProto.DateSchedule, _Mapping]] = ..., yearly_schedule: _Optional[_Union[SchedulingPolicyProto.YearlySchedule, _Mapping]] = ...) -> None: ...

class RetentionPolicyProto(_message.Message):
    __slots__ = ("num_days_to_keep", "worm_retention", "num_secs_to_keep")
    NUM_DAYS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    WORM_RETENTION_FIELD_NUMBER: _ClassVar[int]
    NUM_SECS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    num_days_to_keep: int
    worm_retention: _worm_pb2.WormRetentionProto
    num_secs_to_keep: int
    def __init__(self, num_days_to_keep: _Optional[int] = ..., worm_retention: _Optional[_Union[_worm_pb2.WormRetentionProto, _Mapping]] = ..., num_secs_to_keep: _Optional[int] = ...) -> None: ...

class CancellationTimeout(_message.Message):
    __slots__ = ("backup_type", "timeout_mins")
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MINS_FIELD_NUMBER: _ClassVar[int]
    backup_type: _enums_pb2.ScheduledBackupType.Type
    timeout_mins: int
    def __init__(self, backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., timeout_mins: _Optional[int] = ...) -> None: ...

class ExtendedRetentionPolicyProto(_message.Message):
    __slots__ = ("granularity_bucket", "backup_type", "copy_partially_successful_run", "retention_policy", "id")
    GRANULARITY_BUCKET_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    COPY_PARTIALLY_SUCCESSFUL_RUN_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    granularity_bucket: GranularityBucket
    backup_type: _enums_pb2.ScheduledBackupType.Type
    copy_partially_successful_run: bool
    retention_policy: RetentionPolicyProto
    id: str
    def __init__(self, granularity_bucket: _Optional[_Union[GranularityBucket, _Mapping]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., copy_partially_successful_run: bool = ..., retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class SnapshotTargetPolicyProto(_message.Message):
    __slots__ = ("granularity_bucket", "copy_partially_successful_run", "snapshot_target", "retention_policy", "id", "extended_retention_policy_vec", "copy_backup_timeout_vec", "backup_type", "log_retention_policy", "num_days_to_keep")
    GRANULARITY_BUCKET_FIELD_NUMBER: _ClassVar[int]
    COPY_PARTIALLY_SUCCESSFUL_RUN_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_RETENTION_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    COPY_BACKUP_TIMEOUT_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOG_RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    NUM_DAYS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    granularity_bucket: GranularityBucket
    copy_partially_successful_run: bool
    snapshot_target: SnapshotTarget
    retention_policy: RetentionPolicyProto
    id: str
    extended_retention_policy_vec: _containers.RepeatedCompositeFieldContainer[ExtendedRetentionPolicyProto]
    copy_backup_timeout_vec: _containers.RepeatedCompositeFieldContainer[CancellationTimeout]
    backup_type: _enums_pb2.ScheduledBackupType.Type
    log_retention_policy: RetentionPolicyProto
    num_days_to_keep: int
    def __init__(self, granularity_bucket: _Optional[_Union[GranularityBucket, _Mapping]] = ..., copy_partially_successful_run: bool = ..., snapshot_target: _Optional[_Union[SnapshotTarget, _Mapping]] = ..., retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., id: _Optional[str] = ..., extended_retention_policy_vec: _Optional[_Iterable[_Union[ExtendedRetentionPolicyProto, _Mapping]]] = ..., copy_backup_timeout_vec: _Optional[_Iterable[_Union[CancellationTimeout, _Mapping]]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., log_retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., num_days_to_keep: _Optional[int] = ...) -> None: ...

class RPOPolicySettingsProto(_message.Message):
    __slots__ = ("view_box_id", "env_backup_params", "backup_qos_principal", "indexing_policy", "alerting_policy")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_BACKUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_QOS_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ALERTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    env_backup_params: _env_params_pb2_1.EnvBackupParams
    backup_qos_principal: _enums_pb2.BackupQoSPrincipal.Type
    indexing_policy: _env_params_pb2_1.IndexingPolicyProto
    alerting_policy: _env_params_pb2_1.AlertingPolicyProto
    def __init__(self, view_box_id: _Optional[int] = ..., env_backup_params: _Optional[_Union[_env_params_pb2_1.EnvBackupParams, _Mapping]] = ..., backup_qos_principal: _Optional[_Union[_enums_pb2.BackupQoSPrincipal.Type, str]] = ..., indexing_policy: _Optional[_Union[_env_params_pb2_1.IndexingPolicyProto, _Mapping]] = ..., alerting_policy: _Optional[_Union[_env_params_pb2_1.AlertingPolicyProto, _Mapping]] = ...) -> None: ...

class ScheduleInfoProto(_message.Message):
    __slots__ = ("scheduling_policy", "retention_policy")
    SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    scheduling_policy: SchedulingPolicyProto
    retention_policy: RetentionPolicyProto
    def __init__(self, scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ...) -> None: ...

class BackupSchedulesProto(_message.Message):
    __slots__ = ("backup_type", "schedule_info_vec")
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_type: _enums_pb2.ScheduledBackupType.Type
    schedule_info_vec: _containers.RepeatedCompositeFieldContainer[ScheduleInfoProto]
    def __init__(self, backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., schedule_info_vec: _Optional[_Iterable[_Union[ScheduleInfoProto, _Mapping]]] = ...) -> None: ...

class MultipleSchedulesProto(_message.Message):
    __slots__ = ("backup_schedules_vec",)
    BACKUP_SCHEDULES_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_schedules_vec: _containers.RepeatedCompositeFieldContainer[BackupSchedulesProto]
    def __init__(self, backup_schedules_vec: _Optional[_Iterable[_Union[BackupSchedulesProto, _Mapping]]] = ...) -> None: ...

class ProtectionPolicyProto(_message.Message):
    __slots__ = ("policy_type", "id", "name", "description", "is_seeded", "status", "scheduling_policy", "full_scheduling_policy", "log_scheduling_policy", "cdp_scheduling_policy", "storage_array_snapshot_scheduling_policy", "system_scheduling_policy", "refresh_scheduling_policy", "multiple_schedules", "retention_policy", "log_retention_policy", "cdp_retention_policy", "storage_array_snapshot_retention_policy", "system_retention_policy", "extended_retention_policy_vec", "num_retries", "retry_delay_mins", "exclusion_ranges", "exclusion_dates", "snapshot_target_policy_vec", "start_window_interval_mins", "last_modification_time_usecs", "user_information", "rpo_policy_settings", "authorized_tenant_id_vec", "is_stubbing_policy", "global_policy_fields", "primary_backup_target", "is_replicated", "last_updated_username", "look_ahead_window_mins", "policy_provenance", "policy_version", "cascaded_snapshot_target_vec", "run_timeout_vec")
    class PolicyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[ProtectionPolicyProto.PolicyType]
        kRPO: _ClassVar[ProtectionPolicyProto.PolicyType]
        kInternal: _ClassVar[ProtectionPolicyProto.PolicyType]
        kProtectOnce: _ClassVar[ProtectionPolicyProto.PolicyType]
        kExternallyTriggered: _ClassVar[ProtectionPolicyProto.PolicyType]
    kRegular: ProtectionPolicyProto.PolicyType
    kRPO: ProtectionPolicyProto.PolicyType
    kInternal: ProtectionPolicyProto.PolicyType
    kProtectOnce: ProtectionPolicyProto.PolicyType
    kExternallyTriggered: ProtectionPolicyProto.PolicyType
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kValid: _ClassVar[ProtectionPolicyProto.Status]
        kDeleted: _ClassVar[ProtectionPolicyProto.Status]
    kValid: ProtectionPolicyProto.Status
    kDeleted: ProtectionPolicyProto.Status
    class PolicyProvenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnassigned: _ClassVar[ProtectionPolicyProto.PolicyProvenance]
        kLocal: _ClassVar[ProtectionPolicyProto.PolicyProvenance]
        kGlobal: _ClassVar[ProtectionPolicyProto.PolicyProvenance]
        kReplicated: _ClassVar[ProtectionPolicyProto.PolicyProvenance]
    kUnassigned: ProtectionPolicyProto.PolicyProvenance
    kLocal: ProtectionPolicyProto.PolicyProvenance
    kGlobal: ProtectionPolicyProto.PolicyProvenance
    kReplicated: ProtectionPolicyProto.PolicyProvenance
    class GlobalPolicyFields(_message.Message):
        __slots__ = ("is_template", "parent_policy_id", "is_usable")
        IS_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        PARENT_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
        IS_USABLE_FIELD_NUMBER: _ClassVar[int]
        is_template: bool
        parent_policy_id: str
        is_usable: bool
        def __init__(self, is_template: bool = ..., parent_policy_id: _Optional[str] = ..., is_usable: bool = ...) -> None: ...
    class PrimaryBackupTarget(_message.Message):
        __slots__ = ("type", "primary_archival_target")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_ARCHIVAL_TARGET_FIELD_NUMBER: _ClassVar[int]
        type: SnapshotTarget.Type
        primary_archival_target: ArchivalTarget
        def __init__(self, type: _Optional[_Union[SnapshotTarget.Type, str]] = ..., primary_archival_target: _Optional[_Union[ArchivalTarget, _Mapping]] = ...) -> None: ...
    class CascadedSnapshotTargetPolicyProto(_message.Message):
        __slots__ = ("source_cluster_id", "snapshot_target_policy_vec")
        SOURCE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_TARGET_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
        source_cluster_id: int
        snapshot_target_policy_vec: _containers.RepeatedCompositeFieldContainer[SnapshotTargetPolicyProto]
        def __init__(self, source_cluster_id: _Optional[int] = ..., snapshot_target_policy_vec: _Optional[_Iterable[_Union[SnapshotTargetPolicyProto, _Mapping]]] = ...) -> None: ...
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_SEEDED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    FULL_SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    LOG_SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    CDP_SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_SCHEDULING_POLICY_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    LOG_RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    CDP_RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ARRAY_SNAPSHOT_RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_RETENTION_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_MINS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_RANGES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_DATES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TARGET_POLICY_VEC_FIELD_NUMBER: _ClassVar[int]
    START_WINDOW_INTERVAL_MINS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    RPO_POLICY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_STUBBING_POLICY_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_POLICY_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BACKUP_TARGET_FIELD_NUMBER: _ClassVar[int]
    IS_REPLICATED_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_USERNAME_FIELD_NUMBER: _ClassVar[int]
    LOOK_AHEAD_WINDOW_MINS_FIELD_NUMBER: _ClassVar[int]
    POLICY_PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    CASCADED_SNAPSHOT_TARGET_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_TIMEOUT_VEC_FIELD_NUMBER: _ClassVar[int]
    policy_type: ProtectionPolicyProto.PolicyType
    id: str
    name: str
    description: str
    is_seeded: bool
    status: ProtectionPolicyProto.Status
    scheduling_policy: SchedulingPolicyProto
    full_scheduling_policy: SchedulingPolicyProto
    log_scheduling_policy: SchedulingPolicyProto
    cdp_scheduling_policy: SchedulingPolicyProto
    storage_array_snapshot_scheduling_policy: SchedulingPolicyProto
    system_scheduling_policy: SchedulingPolicyProto
    refresh_scheduling_policy: SchedulingPolicyProto
    multiple_schedules: MultipleSchedulesProto
    retention_policy: RetentionPolicyProto
    log_retention_policy: RetentionPolicyProto
    cdp_retention_policy: RetentionPolicyProto
    storage_array_snapshot_retention_policy: RetentionPolicyProto
    system_retention_policy: RetentionPolicyProto
    extended_retention_policy_vec: _containers.RepeatedCompositeFieldContainer[ExtendedRetentionPolicyProto]
    num_retries: int
    retry_delay_mins: int
    exclusion_ranges: _containers.RepeatedCompositeFieldContainer[ExclusionTimeRange]
    exclusion_dates: ExclusionDates
    snapshot_target_policy_vec: _containers.RepeatedCompositeFieldContainer[SnapshotTargetPolicyProto]
    start_window_interval_mins: int
    last_modification_time_usecs: int
    user_information: _permissions_pb2.UserInformation
    rpo_policy_settings: RPOPolicySettingsProto
    authorized_tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    is_stubbing_policy: bool
    global_policy_fields: ProtectionPolicyProto.GlobalPolicyFields
    primary_backup_target: ProtectionPolicyProto.PrimaryBackupTarget
    is_replicated: bool
    last_updated_username: str
    look_ahead_window_mins: int
    policy_provenance: ProtectionPolicyProto.PolicyProvenance
    policy_version: int
    cascaded_snapshot_target_vec: _containers.RepeatedCompositeFieldContainer[ProtectionPolicyProto.CascadedSnapshotTargetPolicyProto]
    run_timeout_vec: _containers.RepeatedCompositeFieldContainer[CancellationTimeout]
    def __init__(self, policy_type: _Optional[_Union[ProtectionPolicyProto.PolicyType, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_seeded: bool = ..., status: _Optional[_Union[ProtectionPolicyProto.Status, str]] = ..., scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., full_scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., log_scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., cdp_scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., storage_array_snapshot_scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., system_scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., refresh_scheduling_policy: _Optional[_Union[SchedulingPolicyProto, _Mapping]] = ..., multiple_schedules: _Optional[_Union[MultipleSchedulesProto, _Mapping]] = ..., retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., log_retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., cdp_retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., storage_array_snapshot_retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., system_retention_policy: _Optional[_Union[RetentionPolicyProto, _Mapping]] = ..., extended_retention_policy_vec: _Optional[_Iterable[_Union[ExtendedRetentionPolicyProto, _Mapping]]] = ..., num_retries: _Optional[int] = ..., retry_delay_mins: _Optional[int] = ..., exclusion_ranges: _Optional[_Iterable[_Union[ExclusionTimeRange, _Mapping]]] = ..., exclusion_dates: _Optional[_Union[ExclusionDates, _Mapping]] = ..., snapshot_target_policy_vec: _Optional[_Iterable[_Union[SnapshotTargetPolicyProto, _Mapping]]] = ..., start_window_interval_mins: _Optional[int] = ..., last_modification_time_usecs: _Optional[int] = ..., user_information: _Optional[_Union[_permissions_pb2.UserInformation, _Mapping]] = ..., rpo_policy_settings: _Optional[_Union[RPOPolicySettingsProto, _Mapping]] = ..., authorized_tenant_id_vec: _Optional[_Iterable[str]] = ..., is_stubbing_policy: bool = ..., global_policy_fields: _Optional[_Union[ProtectionPolicyProto.GlobalPolicyFields, _Mapping]] = ..., primary_backup_target: _Optional[_Union[ProtectionPolicyProto.PrimaryBackupTarget, _Mapping]] = ..., is_replicated: bool = ..., last_updated_username: _Optional[str] = ..., look_ahead_window_mins: _Optional[int] = ..., policy_provenance: _Optional[_Union[ProtectionPolicyProto.PolicyProvenance, str]] = ..., policy_version: _Optional[int] = ..., cascaded_snapshot_target_vec: _Optional[_Iterable[_Union[ProtectionPolicyProto.CascadedSnapshotTargetPolicyProto, _Mapping]]] = ..., run_timeout_vec: _Optional[_Iterable[_Union[CancellationTimeout, _Mapping]]] = ...) -> None: ...
