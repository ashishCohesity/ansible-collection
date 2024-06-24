from iris.base import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SchedulerProto(_message.Message):
    __slots__ = ("scheduler_jobs",)
    class SchedulerJob(_message.Message):
        __slots__ = ("id", "name", "schedules", "type", "schedule_job_parameters", "enable_recurring_email", "tenant_id")
        class SchedulerJobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSchedulerJobReport: _ClassVar[SchedulerProto.SchedulerJob.SchedulerJobType]
            kSCHEDULER_JOB_REPORT: _ClassVar[SchedulerProto.SchedulerJob.SchedulerJobType]
        kSchedulerJobReport: SchedulerProto.SchedulerJob.SchedulerJobType
        kSCHEDULER_JOB_REPORT: SchedulerProto.SchedulerJob.SchedulerJobType
        class Schedule(_message.Message):
            __slots__ = ("hour", "day", "timezone")
            HOUR_FIELD_NUMBER: _ClassVar[int]
            DAY_FIELD_NUMBER: _ClassVar[int]
            TIMEZONE_FIELD_NUMBER: _ClassVar[int]
            hour: int
            day: int
            timezone: str
            def __init__(self, hour: _Optional[int] = ..., day: _Optional[int] = ..., timezone: _Optional[str] = ...) -> None: ...
        class ScheduleJobParameters(_message.Message):
            __slots__ = ("report_job_parameter",)
            class ReportJobParameter(_message.Message):
                __slots__ = ("receiver_emails", "reports")
                class Report(_message.Message):
                    __slots__ = ("type", "parameters", "output_format", "name", "subject_line")
                    class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                        __slots__ = ()
                        kAvailableLocalSnapshotsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kBackupSummaryReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kFailedObjectsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kProtectionDetailsPerObjectReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kProtectionJobsInventoryAndScheduleReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kProtectionSummaryByObjectTypeReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kSourceGrowthAndVarianceReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kStorageConsumedByBackupReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kStorageConsumedByFileCategoriesReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kStorageConsumedByServersReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kStorageConsumedByViewBoxReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kDataTransferredToExternalTargetsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kUnprotectedVMsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kUserQuotasReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kGdprReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kAgentDeploymentReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kProtectedObjectsTrendsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kStorageConsumedByTenantsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kProtectionRunsSummaryReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kStorageConsumedByTenantPerViewBoxReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kDirQuotasReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kObjectsProtectedByMultipleGroupsReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                        kArchivalSummaryReport: _ClassVar[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType]
                    kAvailableLocalSnapshotsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kBackupSummaryReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kFailedObjectsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kProtectionDetailsPerObjectReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kProtectionJobsInventoryAndScheduleReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kProtectionSummaryByObjectTypeReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kSourceGrowthAndVarianceReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kStorageConsumedByBackupReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kStorageConsumedByFileCategoriesReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kStorageConsumedByServersReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kStorageConsumedByViewBoxReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kDataTransferredToExternalTargetsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kUnprotectedVMsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kUserQuotasReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kGdprReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kAgentDeploymentReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kProtectedObjectsTrendsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kStorageConsumedByTenantsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kProtectionRunsSummaryReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kStorageConsumedByTenantPerViewBoxReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kDirQuotasReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kObjectsProtectedByMultipleGroupsReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    kArchivalSummaryReport: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    class Parameters(_message.Message):
                        __slots__ = ("last_n_days", "job_name", "job_id", "run_status", "object_type", "object_ids", "vm_name", "registered_source_ids", "view_box_id", "vault_ids", "view_name", "unix_uid", "sid", "consecutive_failures", "host_os_type", "compact_version", "health_status", "environment", "rollup", "timezone", "registered_source_id", "tenant_id_vec", "allUnderHierarchy", "group_by", "viewbox_ids", "exclude_users_within_alert_threshold")
                        LAST_N_DAYS_FIELD_NUMBER: _ClassVar[int]
                        JOB_NAME_FIELD_NUMBER: _ClassVar[int]
                        JOB_ID_FIELD_NUMBER: _ClassVar[int]
                        RUN_STATUS_FIELD_NUMBER: _ClassVar[int]
                        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
                        OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
                        VM_NAME_FIELD_NUMBER: _ClassVar[int]
                        REGISTERED_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
                        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
                        VAULT_IDS_FIELD_NUMBER: _ClassVar[int]
                        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
                        UNIX_UID_FIELD_NUMBER: _ClassVar[int]
                        SID_FIELD_NUMBER: _ClassVar[int]
                        CONSECUTIVE_FAILURES_FIELD_NUMBER: _ClassVar[int]
                        HOST_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
                        COMPACT_VERSION_FIELD_NUMBER: _ClassVar[int]
                        HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
                        ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
                        ROLLUP_FIELD_NUMBER: _ClassVar[int]
                        TIMEZONE_FIELD_NUMBER: _ClassVar[int]
                        REGISTERED_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
                        TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
                        ALLUNDERHIERARCHY_FIELD_NUMBER: _ClassVar[int]
                        GROUP_BY_FIELD_NUMBER: _ClassVar[int]
                        VIEWBOX_IDS_FIELD_NUMBER: _ClassVar[int]
                        EXCLUDE_USERS_WITHIN_ALERT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
                        last_n_days: int
                        job_name: str
                        job_id: int
                        run_status: _containers.RepeatedScalarFieldContainer[str]
                        object_type: str
                        object_ids: _containers.RepeatedScalarFieldContainer[int]
                        vm_name: str
                        registered_source_ids: _containers.RepeatedScalarFieldContainer[int]
                        view_box_id: int
                        vault_ids: _containers.RepeatedScalarFieldContainer[int]
                        view_name: str
                        unix_uid: int
                        sid: str
                        consecutive_failures: int
                        host_os_type: _containers.RepeatedScalarFieldContainer[str]
                        compact_version: str
                        health_status: _containers.RepeatedScalarFieldContainer[str]
                        environment: str
                        rollup: str
                        timezone: str
                        registered_source_id: int
                        tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
                        allUnderHierarchy: bool
                        group_by: _enums_pb2.GroupBy
                        viewbox_ids: _containers.RepeatedScalarFieldContainer[int]
                        exclude_users_within_alert_threshold: bool
                        def __init__(self, last_n_days: _Optional[int] = ..., job_name: _Optional[str] = ..., job_id: _Optional[int] = ..., run_status: _Optional[_Iterable[str]] = ..., object_type: _Optional[str] = ..., object_ids: _Optional[_Iterable[int]] = ..., vm_name: _Optional[str] = ..., registered_source_ids: _Optional[_Iterable[int]] = ..., view_box_id: _Optional[int] = ..., vault_ids: _Optional[_Iterable[int]] = ..., view_name: _Optional[str] = ..., unix_uid: _Optional[int] = ..., sid: _Optional[str] = ..., consecutive_failures: _Optional[int] = ..., host_os_type: _Optional[_Iterable[str]] = ..., compact_version: _Optional[str] = ..., health_status: _Optional[_Iterable[str]] = ..., environment: _Optional[str] = ..., rollup: _Optional[str] = ..., timezone: _Optional[str] = ..., registered_source_id: _Optional[int] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., allUnderHierarchy: bool = ..., group_by: _Optional[_Union[_enums_pb2.GroupBy, str]] = ..., viewbox_ids: _Optional[_Iterable[int]] = ..., exclude_users_within_alert_threshold: bool = ...) -> None: ...
                    TYPE_FIELD_NUMBER: _ClassVar[int]
                    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
                    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
                    NAME_FIELD_NUMBER: _ClassVar[int]
                    SUBJECT_LINE_FIELD_NUMBER: _ClassVar[int]
                    type: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType
                    parameters: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.Parameters
                    output_format: str
                    name: str
                    subject_line: str
                    def __init__(self, type: _Optional[_Union[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.ReportType, str]] = ..., parameters: _Optional[_Union[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report.Parameters, _Mapping]] = ..., output_format: _Optional[str] = ..., name: _Optional[str] = ..., subject_line: _Optional[str] = ...) -> None: ...
                RECEIVER_EMAILS_FIELD_NUMBER: _ClassVar[int]
                REPORTS_FIELD_NUMBER: _ClassVar[int]
                receiver_emails: _containers.RepeatedScalarFieldContainer[str]
                reports: _containers.RepeatedCompositeFieldContainer[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report]
                def __init__(self, receiver_emails: _Optional[_Iterable[str]] = ..., reports: _Optional[_Iterable[_Union[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter.Report, _Mapping]]] = ...) -> None: ...
            REPORT_JOB_PARAMETER_FIELD_NUMBER: _ClassVar[int]
            report_job_parameter: SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter
            def __init__(self, report_job_parameter: _Optional[_Union[SchedulerProto.SchedulerJob.ScheduleJobParameters.ReportJobParameter, _Mapping]] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SCHEDULES_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_JOB_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_RECURRING_EMAIL_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        schedules: _containers.RepeatedCompositeFieldContainer[SchedulerProto.SchedulerJob.Schedule]
        type: SchedulerProto.SchedulerJob.SchedulerJobType
        schedule_job_parameters: SchedulerProto.SchedulerJob.ScheduleJobParameters
        enable_recurring_email: bool
        tenant_id: str
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., schedules: _Optional[_Iterable[_Union[SchedulerProto.SchedulerJob.Schedule, _Mapping]]] = ..., type: _Optional[_Union[SchedulerProto.SchedulerJob.SchedulerJobType, str]] = ..., schedule_job_parameters: _Optional[_Union[SchedulerProto.SchedulerJob.ScheduleJobParameters, _Mapping]] = ..., enable_recurring_email: bool = ..., tenant_id: _Optional[str] = ...) -> None: ...
    SCHEDULER_JOBS_FIELD_NUMBER: _ClassVar[int]
    scheduler_jobs: _containers.RepeatedCompositeFieldContainer[SchedulerProto.SchedulerJob]
    def __init__(self, scheduler_jobs: _Optional[_Iterable[_Union[SchedulerProto.SchedulerJob, _Mapping]]] = ...) -> None: ...
