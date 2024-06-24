from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sfdc_pb2 as _sfdc_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("job_instance_id", "attempt_num", "status", "error", "sfdc_object_metadata_proto_path", "sfdc_server_timestamp_usecs", "prev_full_sfdc_server_timestamp_usecs", "sfdc_bulk_job_id", "query_locator_string", "num_records_downloaded", "object_download_start_time", "part_number", "upload_id", "etags_vec", "org_id", "record_stats", "object_has_files_or_attachments", "backup_database_name", "num_records_bulk_batch", "s3_csv_file_key")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kFetchMetadata: _ClassVar[SnapshotInfo.Status]
        kCreateBulkQueryJob: _ClassVar[SnapshotInfo.Status]
        kPollBulkQueryJobProgress: _ClassVar[SnapshotInfo.Status]
        kDownloadBulkQueryJobResults: _ClassVar[SnapshotInfo.Status]
        kDownloadSoapData: _ClassVar[SnapshotInfo.Status]
        kImportCsvFromS3ToDatabase: _ClassVar[SnapshotInfo.Status]
        kCreateTable: _ClassVar[SnapshotInfo.Status]
        kGetFilesMetadata: _ClassVar[SnapshotInfo.Status]
        kGetAttachmentsMetadata: _ClassVar[SnapshotInfo.Status]
        kCopyExistingDownloads: _ClassVar[SnapshotInfo.Status]
        kDownloadFilesAndAttachments: _ClassVar[SnapshotInfo.Status]
        kFinished: _ClassVar[SnapshotInfo.Status]
        kCleanupExtraClonedFilesFromView: _ClassVar[SnapshotInfo.Status]
        kCleanupFilesFromS3: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kFetchMetadata: SnapshotInfo.Status
    kCreateBulkQueryJob: SnapshotInfo.Status
    kPollBulkQueryJobProgress: SnapshotInfo.Status
    kDownloadBulkQueryJobResults: SnapshotInfo.Status
    kDownloadSoapData: SnapshotInfo.Status
    kImportCsvFromS3ToDatabase: SnapshotInfo.Status
    kCreateTable: SnapshotInfo.Status
    kGetFilesMetadata: SnapshotInfo.Status
    kGetAttachmentsMetadata: SnapshotInfo.Status
    kCopyExistingDownloads: SnapshotInfo.Status
    kDownloadFilesAndAttachments: SnapshotInfo.Status
    kFinished: SnapshotInfo.Status
    kCleanupExtraClonedFilesFromView: SnapshotInfo.Status
    kCleanupFilesFromS3: SnapshotInfo.Status
    class RecordStats(_message.Message):
        __slots__ = ("deleted", "modified")
        DELETED_FIELD_NUMBER: _ClassVar[int]
        MODIFIED_FIELD_NUMBER: _ClassVar[int]
        deleted: int
        modified: int
        def __init__(self, deleted: _Optional[int] = ..., modified: _Optional[int] = ...) -> None: ...
    SFDC_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    sfdc_snapshot_info: _descriptor.FieldDescriptor
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SFDC_OBJECT_METADATA_PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    PREV_FULL_SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SFDC_BULK_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_LOCATOR_STRING_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DOWNLOAD_START_TIME_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    ETAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_STATS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_HAS_FILES_OR_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_BULK_BATCH_FIELD_NUMBER: _ClassVar[int]
    S3_CSV_FILE_KEY_FIELD_NUMBER: _ClassVar[int]
    job_instance_id: int
    attempt_num: int
    status: SnapshotInfo.Status
    error: _error_pb2.ErrorProto
    sfdc_object_metadata_proto_path: str
    sfdc_server_timestamp_usecs: int
    prev_full_sfdc_server_timestamp_usecs: int
    sfdc_bulk_job_id: str
    query_locator_string: str
    num_records_downloaded: int
    object_download_start_time: int
    part_number: int
    upload_id: str
    etags_vec: _containers.RepeatedScalarFieldContainer[str]
    org_id: str
    record_stats: SnapshotInfo.RecordStats
    object_has_files_or_attachments: bool
    backup_database_name: str
    num_records_bulk_batch: int
    s3_csv_file_key: str
    def __init__(self, job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sfdc_object_metadata_proto_path: _Optional[str] = ..., sfdc_server_timestamp_usecs: _Optional[int] = ..., prev_full_sfdc_server_timestamp_usecs: _Optional[int] = ..., sfdc_bulk_job_id: _Optional[str] = ..., query_locator_string: _Optional[str] = ..., num_records_downloaded: _Optional[int] = ..., object_download_start_time: _Optional[int] = ..., part_number: _Optional[int] = ..., upload_id: _Optional[str] = ..., etags_vec: _Optional[_Iterable[str]] = ..., org_id: _Optional[str] = ..., record_stats: _Optional[_Union[SnapshotInfo.RecordStats, _Mapping]] = ..., object_has_files_or_attachments: bool = ..., backup_database_name: _Optional[str] = ..., num_records_bulk_batch: _Optional[int] = ..., s3_csv_file_key: _Optional[str] = ...) -> None: ...

class SfdcAdditionalRunInfo(_message.Message):
    __slots__ = ("sfdc_server_timestamp_usecs", "sfdc_object_metadata_proto_path", "backup_database_name", "access_token_refresh_time_usecs")
    SFDC_ADDITIONAL_RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    sfdc_additional_run_info: _descriptor.FieldDescriptor
    SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SFDC_OBJECT_METADATA_PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_REFRESH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    sfdc_server_timestamp_usecs: int
    sfdc_object_metadata_proto_path: str
    backup_database_name: str
    access_token_refresh_time_usecs: int
    def __init__(self, sfdc_server_timestamp_usecs: _Optional[int] = ..., sfdc_object_metadata_proto_path: _Optional[str] = ..., backup_database_name: _Optional[str] = ..., access_token_refresh_time_usecs: _Optional[int] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ()
    SFDC_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    sfdc_restore_entity_info: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("recover_task_state", "sub_task_vec", "progress_percent", "error", "temp_tables_schema_name", "next_subtask_index", "profile_api_name")
    class RecoverTaskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.RecoverTaskState]
        kCloneBackupView: _ClassVar[RestoreInfo.RecoverTaskState]
        kValidateObjectMetadata: _ClassVar[RestoreInfo.RecoverTaskState]
        kValidateObjectDependencies: _ClassVar[RestoreInfo.RecoverTaskState]
        kCreateTemporaryDatabaseSchema: _ClassVar[RestoreInfo.RecoverTaskState]
        kCreateTemporaryRecoveryTables: _ClassVar[RestoreInfo.RecoverTaskState]
        kPopulateRecoveryTables: _ClassVar[RestoreInfo.RecoverTaskState]
        kFetchProfileApiName: _ClassVar[RestoreInfo.RecoverTaskState]
        kAddExternalColumn: _ClassVar[RestoreInfo.RecoverTaskState]
        kCreateSubTasks: _ClassVar[RestoreInfo.RecoverTaskState]
        kStartSubTasks: _ClassVar[RestoreInfo.RecoverTaskState]
        kCreateFilesRestoreSubTask: _ClassVar[RestoreInfo.RecoverTaskState]
        kCreateStage2SubTasks: _ClassVar[RestoreInfo.RecoverTaskState]
        kRunSecondRecoveryStageAndFilesRestoreSubtasks: _ClassVar[RestoreInfo.RecoverTaskState]
        kDeleteTemporaryDatabaseSchema: _ClassVar[RestoreInfo.RecoverTaskState]
        kRemoveExternalColumn: _ClassVar[RestoreInfo.RecoverTaskState]
        kCleanupCsvFilesFromS3: _ClassVar[RestoreInfo.RecoverTaskState]
        kDeleteClonedView: _ClassVar[RestoreInfo.RecoverTaskState]
        kReleasePermit: _ClassVar[RestoreInfo.RecoverTaskState]
        kFinished: _ClassVar[RestoreInfo.RecoverTaskState]
    kStarted: RestoreInfo.RecoverTaskState
    kCloneBackupView: RestoreInfo.RecoverTaskState
    kValidateObjectMetadata: RestoreInfo.RecoverTaskState
    kValidateObjectDependencies: RestoreInfo.RecoverTaskState
    kCreateTemporaryDatabaseSchema: RestoreInfo.RecoverTaskState
    kCreateTemporaryRecoveryTables: RestoreInfo.RecoverTaskState
    kPopulateRecoveryTables: RestoreInfo.RecoverTaskState
    kFetchProfileApiName: RestoreInfo.RecoverTaskState
    kAddExternalColumn: RestoreInfo.RecoverTaskState
    kCreateSubTasks: RestoreInfo.RecoverTaskState
    kStartSubTasks: RestoreInfo.RecoverTaskState
    kCreateFilesRestoreSubTask: RestoreInfo.RecoverTaskState
    kCreateStage2SubTasks: RestoreInfo.RecoverTaskState
    kRunSecondRecoveryStageAndFilesRestoreSubtasks: RestoreInfo.RecoverTaskState
    kDeleteTemporaryDatabaseSchema: RestoreInfo.RecoverTaskState
    kRemoveExternalColumn: RestoreInfo.RecoverTaskState
    kCleanupCsvFilesFromS3: RestoreInfo.RecoverTaskState
    kDeleteClonedView: RestoreInfo.RecoverTaskState
    kReleasePermit: RestoreInfo.RecoverTaskState
    kFinished: RestoreInfo.RecoverTaskState
    SFDC_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    sfdc_restore_info: _descriptor.FieldDescriptor
    RECOVER_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_VEC_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TEMP_TABLES_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    NEXT_SUBTASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    PROFILE_API_NAME_FIELD_NUMBER: _ClassVar[int]
    recover_task_state: RestoreInfo.RecoverTaskState
    sub_task_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    progress_percent: int
    error: _error_pb2.ErrorProto
    temp_tables_schema_name: str
    next_subtask_index: int
    profile_api_name: str
    def __init__(self, recover_task_state: _Optional[_Union[RestoreInfo.RecoverTaskState, str]] = ..., sub_task_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., progress_percent: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., temp_tables_schema_name: _Optional[str] = ..., next_subtask_index: _Optional[int] = ..., profile_api_name: _Optional[str] = ...) -> None: ...

class SfdcRestoreSubTaskInfo(_message.Message):
    __slots__ = ("object_name", "s3_csv_file_key", "s3_csv_file_size_in_bytes", "ingest_upload_size_in_bytes", "num_parallel_ops", "job_state_info_vec", "total_record_count", "soap_upload_state_vec", "sub_task_purpose", "file_ids_start_index", "file_ids_end_index", "field_vec")
    class SubTaskPurpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRecordRestore: _ClassVar[SfdcRestoreSubTaskInfo.SubTaskPurpose]
        kFilesRestore: _ClassVar[SfdcRestoreSubTaskInfo.SubTaskPurpose]
        kLookupRestore: _ClassVar[SfdcRestoreSubTaskInfo.SubTaskPurpose]
    kRecordRestore: SfdcRestoreSubTaskInfo.SubTaskPurpose
    kFilesRestore: SfdcRestoreSubTaskInfo.SubTaskPurpose
    kLookupRestore: SfdcRestoreSubTaskInfo.SubTaskPurpose
    SFDC_RESTORE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    sfdc_restore_sub_task_info: _descriptor.FieldDescriptor
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_CSV_FILE_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_CSV_FILE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    INGEST_UPLOAD_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_PARALLEL_OPS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOAP_UPLOAD_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_START_INDEX_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_END_INDEX_FIELD_NUMBER: _ClassVar[int]
    FIELD_VEC_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    s3_csv_file_key: str
    s3_csv_file_size_in_bytes: int
    ingest_upload_size_in_bytes: int
    num_parallel_ops: int
    job_state_info_vec: _containers.RepeatedCompositeFieldContainer[JobStateInfo]
    total_record_count: int
    soap_upload_state_vec: _containers.RepeatedCompositeFieldContainer[SoapUploadState]
    sub_task_purpose: SfdcRestoreSubTaskInfo.SubTaskPurpose
    file_ids_start_index: int
    file_ids_end_index: int
    field_vec: _containers.RepeatedCompositeFieldContainer[_sfdc_pb2.SfdcRecoverField]
    def __init__(self, object_name: _Optional[str] = ..., s3_csv_file_key: _Optional[str] = ..., s3_csv_file_size_in_bytes: _Optional[int] = ..., ingest_upload_size_in_bytes: _Optional[int] = ..., num_parallel_ops: _Optional[int] = ..., job_state_info_vec: _Optional[_Iterable[_Union[JobStateInfo, _Mapping]]] = ..., total_record_count: _Optional[int] = ..., soap_upload_state_vec: _Optional[_Iterable[_Union[SoapUploadState, _Mapping]]] = ..., sub_task_purpose: _Optional[_Union[SfdcRestoreSubTaskInfo.SubTaskPurpose, str]] = ..., file_ids_start_index: _Optional[int] = ..., file_ids_end_index: _Optional[int] = ..., field_vec: _Optional[_Iterable[_Union[_sfdc_pb2.SfdcRecoverField, _Mapping]]] = ...) -> None: ...

class ObjectByteRange(_message.Message):
    __slots__ = ("start_bytes", "end_bytes", "is_processed")
    START_BYTES_FIELD_NUMBER: _ClassVar[int]
    END_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    start_bytes: int
    end_bytes: int
    is_processed: bool
    def __init__(self, start_bytes: _Optional[int] = ..., end_bytes: _Optional[int] = ..., is_processed: bool = ...) -> None: ...

class JobStateInfo(_message.Message):
    __slots__ = ("obj_byte_range_vec", "state", "ingest_op", "ingest_job_info", "unprocessed_job_id", "failed_job_id", "ingest_retry_count", "s3_csv_file_key")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[JobStateInfo.State]
        kCreateBulkV2Job: _ClassVar[JobStateInfo.State]
        kUploadData: _ClassVar[JobStateInfo.State]
        kCloseOrAbortJob: _ClassVar[JobStateInfo.State]
        kGetJobInfo: _ClassVar[JobStateInfo.State]
        kFetchFailedRecordsInfo: _ClassVar[JobStateInfo.State]
        kFetchUnprocessedRecordsInfo: _ClassVar[JobStateInfo.State]
        kFinished: _ClassVar[JobStateInfo.State]
        kIngestFailed: _ClassVar[JobStateInfo.State]
        kFetchSuccessfulRecordsInfo: _ClassVar[JobStateInfo.State]
        kDone: _ClassVar[JobStateInfo.State]
    kInvalid: JobStateInfo.State
    kCreateBulkV2Job: JobStateInfo.State
    kUploadData: JobStateInfo.State
    kCloseOrAbortJob: JobStateInfo.State
    kGetJobInfo: JobStateInfo.State
    kFetchFailedRecordsInfo: JobStateInfo.State
    kFetchUnprocessedRecordsInfo: JobStateInfo.State
    kFinished: JobStateInfo.State
    kIngestFailed: JobStateInfo.State
    kFetchSuccessfulRecordsInfo: JobStateInfo.State
    kDone: JobStateInfo.State
    class IngestOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalidOp: _ClassVar[JobStateInfo.IngestOperation]
        kUpdateAll: _ClassVar[JobStateInfo.IngestOperation]
        kInsert: _ClassVar[JobStateInfo.IngestOperation]
        kInsertUnprocessed: _ClassVar[JobStateInfo.IngestOperation]
        kCompleted: _ClassVar[JobStateInfo.IngestOperation]
        kFailed: _ClassVar[JobStateInfo.IngestOperation]
    kInvalidOp: JobStateInfo.IngestOperation
    kUpdateAll: JobStateInfo.IngestOperation
    kInsert: JobStateInfo.IngestOperation
    kInsertUnprocessed: JobStateInfo.IngestOperation
    kCompleted: JobStateInfo.IngestOperation
    kFailed: JobStateInfo.IngestOperation
    OBJ_BYTE_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INGEST_OP_FIELD_NUMBER: _ClassVar[int]
    INGEST_JOB_INFO_FIELD_NUMBER: _ClassVar[int]
    UNPROCESSED_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    FAILED_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    INGEST_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    S3_CSV_FILE_KEY_FIELD_NUMBER: _ClassVar[int]
    obj_byte_range_vec: _containers.RepeatedCompositeFieldContainer[ObjectByteRange]
    state: JobStateInfo.State
    ingest_op: JobStateInfo.IngestOperation
    ingest_job_info: BulkIngestJobInfo
    unprocessed_job_id: str
    failed_job_id: str
    ingest_retry_count: int
    s3_csv_file_key: str
    def __init__(self, obj_byte_range_vec: _Optional[_Iterable[_Union[ObjectByteRange, _Mapping]]] = ..., state: _Optional[_Union[JobStateInfo.State, str]] = ..., ingest_op: _Optional[_Union[JobStateInfo.IngestOperation, str]] = ..., ingest_job_info: _Optional[_Union[BulkIngestJobInfo, _Mapping]] = ..., unprocessed_job_id: _Optional[str] = ..., failed_job_id: _Optional[str] = ..., ingest_retry_count: _Optional[int] = ..., s3_csv_file_key: _Optional[str] = ...) -> None: ...

class BulkIngestJobInfo(_message.Message):
    __slots__ = ("job_id", "job_state", "job_total_record_count", "job_processed_record_count", "job_failed_record_count", "retry_count")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_TOTAL_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    JOB_PROCESSED_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    JOB_FAILED_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    job_state: str
    job_total_record_count: int
    job_processed_record_count: int
    job_failed_record_count: int
    retry_count: int
    def __init__(self, job_id: _Optional[str] = ..., job_state: _Optional[str] = ..., job_total_record_count: _Optional[int] = ..., job_processed_record_count: _Optional[int] = ..., job_failed_record_count: _Optional[int] = ..., retry_count: _Optional[int] = ...) -> None: ...

class SoapUploadState(_message.Message):
    __slots__ = ("start_record", "end_record", "s3_csv_file_key", "s3_csv_file_size_in_bytes", "current_file_offset", "num_records_uploaded", "upload_complete", "error")
    START_RECORD_FIELD_NUMBER: _ClassVar[int]
    END_RECORD_FIELD_NUMBER: _ClassVar[int]
    S3_CSV_FILE_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_CSV_FILE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    start_record: int
    end_record: int
    s3_csv_file_key: str
    s3_csv_file_size_in_bytes: int
    current_file_offset: int
    num_records_uploaded: int
    upload_complete: bool
    error: _error_pb2.ErrorProto
    def __init__(self, start_record: _Optional[int] = ..., end_record: _Optional[int] = ..., s3_csv_file_key: _Optional[str] = ..., s3_csv_file_size_in_bytes: _Optional[int] = ..., current_file_offset: _Optional[int] = ..., num_records_uploaded: _Optional[int] = ..., upload_complete: bool = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
