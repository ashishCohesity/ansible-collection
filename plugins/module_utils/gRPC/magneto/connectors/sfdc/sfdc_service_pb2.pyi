from magneto.base import error_pb2 as _error_pb2
from magneto.base import sfdc_pb2 as _sfdc_pb2
from magneto.base.entities import sfdc_pb2 as _sfdc_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kLow: _ClassVar[Priority]
    kMedium: _ClassVar[Priority]
    kHigh: _ClassVar[Priority]
    kNumPriorities: _ClassVar[Priority]
kLow: Priority
kMedium: Priority
kHigh: Priority
kNumPriorities: Priority

class DiscoverSourceArg(_message.Message):
    __slots__ = ("source_connector_params",)
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ...) -> None: ...

class DiscoverSourceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetConnectorInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConnectorInfoResult(_message.Message):
    __slots__ = ("error", "sfdc_service_version")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SFDC_SERVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    sfdc_service_version: SfdcServiceVersion
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sfdc_service_version: _Optional[_Union[SfdcServiceVersion, _Mapping]] = ...) -> None: ...

class SfdcServiceVersion(_message.Message):
    __slots__ = ("major_version", "minor_version", "patch_version", "tag")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    patch_version: int
    tag: str
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., patch_version: _Optional[int] = ..., tag: _Optional[str] = ...) -> None: ...

class GetEntitiesArg(_message.Message):
    __slots__ = ("source_connector_params", "parent_entity", "task_id")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    parent_entity: _sfdc_pb2_1.Entity
    task_id: int
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., parent_entity: _Optional[_Union[_sfdc_pb2_1.Entity, _Mapping]] = ..., task_id: _Optional[int] = ...) -> None: ...

class GetEntitiesResult(_message.Message):
    __slots__ = ("error", "entities", "in_progress")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entities: _containers.RepeatedCompositeFieldContainer[_sfdc_pb2_1.Entity]
    in_progress: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entities: _Optional[_Iterable[_Union[_sfdc_pb2_1.Entity, _Mapping]]] = ..., in_progress: bool = ...) -> None: ...

class JobStats(_message.Message):
    __slots__ = ("objects_created", "objects_modified", "objects_deleted", "records_created", "records_modified", "records_deleted", "bytes_transferred", "bytes_protected")
    OBJECTS_CREATED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_DELETED_FIELD_NUMBER: _ClassVar[int]
    RECORDS_CREATED_FIELD_NUMBER: _ClassVar[int]
    RECORDS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    RECORDS_DELETED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    BYTES_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    objects_created: int
    objects_modified: int
    objects_deleted: int
    records_created: int
    records_modified: int
    records_deleted: int
    bytes_transferred: int
    bytes_protected: int
    def __init__(self, objects_created: _Optional[int] = ..., objects_modified: _Optional[int] = ..., objects_deleted: _Optional[int] = ..., records_created: _Optional[int] = ..., records_modified: _Optional[int] = ..., records_deleted: _Optional[int] = ..., bytes_transferred: _Optional[int] = ..., bytes_protected: _Optional[int] = ...) -> None: ...

class GetEntityRecordCountArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetEntityRecordCountResult(_message.Message):
    __slots__ = ("error", "objects_vec")
    class SfdcObjectDetail(_message.Message):
        __slots__ = ("count", "name")
        COUNT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        count: int
        name: str
        def __init__(self, count: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    objects_vec: _containers.RepeatedCompositeFieldContainer[GetEntityRecordCountResult.SfdcObjectDetail]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., objects_vec: _Optional[_Iterable[_Union[GetEntityRecordCountResult.SfdcObjectDetail, _Mapping]]] = ...) -> None: ...

class GetOrgInfoArg(_message.Message):
    __slots__ = ("source_connector_params",)
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ...) -> None: ...

class GetOrgInfoResult(_message.Message):
    __slots__ = ("error", "org_id", "org_name")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    org_id: str
    org_name: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., org_id: _Optional[str] = ..., org_name: _Optional[str] = ...) -> None: ...

class GetProfileInfoResult(_message.Message):
    __slots__ = ("error", "profile_id", "profile_api_name", "profile_name")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_API_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    profile_id: str
    profile_api_name: str
    profile_name: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., profile_id: _Optional[str] = ..., profile_api_name: _Optional[str] = ..., profile_name: _Optional[str] = ...) -> None: ...

class PopulateObjectMetadataStoreArg(_message.Message):
    __slots__ = ("source_connector_params", "should_dump_to_snapfs", "protected_objects_vec", "excluded_fields_info_vec")
    class ExcludedFieldsInfo(_message.Message):
        __slots__ = ("object_name", "excluded_field_names_vec")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_FIELD_NAMES_VEC_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        excluded_field_names_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, object_name: _Optional[str] = ..., excluded_field_names_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_DUMP_TO_SNAPFS_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_OBJECTS_VEC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FIELDS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    should_dump_to_snapfs: bool
    protected_objects_vec: _containers.RepeatedScalarFieldContainer[str]
    excluded_fields_info_vec: _containers.RepeatedCompositeFieldContainer[PopulateObjectMetadataStoreArg.ExcludedFieldsInfo]
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., should_dump_to_snapfs: bool = ..., protected_objects_vec: _Optional[_Iterable[str]] = ..., excluded_fields_info_vec: _Optional[_Iterable[_Union[PopulateObjectMetadataStoreArg.ExcludedFieldsInfo, _Mapping]]] = ...) -> None: ...

class PopulateObjectMetadataStoreResult(_message.Message):
    __slots__ = ("error", "object_store", "excluded_req_fields_vec")
    class ObjectReqField(_message.Message):
        __slots__ = ("object_name", "field_name")
        OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        object_name: str
        field_name: str
        def __init__(self, object_name: _Optional[str] = ..., field_name: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_REQ_FIELDS_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    object_store: _sfdc_pb2.SfdcObjectMetadataStore
    excluded_req_fields_vec: _containers.RepeatedCompositeFieldContainer[PopulateObjectMetadataStoreResult.ObjectReqField]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., object_store: _Optional[_Union[_sfdc_pb2.SfdcObjectMetadataStore, _Mapping]] = ..., excluded_req_fields_vec: _Optional[_Iterable[_Union[PopulateObjectMetadataStoreResult.ObjectReqField, _Mapping]]] = ...) -> None: ...

class CreateObjectFieldArg(_message.Message):
    __slots__ = ("source_connector_params", "object_metadata", "field_metadata", "profile_api_name")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    FIELD_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROFILE_API_NAME_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    object_metadata: _sfdc_pb2.SfdcObjectMetadata
    field_metadata: _sfdc_pb2.Field
    profile_api_name: str
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., object_metadata: _Optional[_Union[_sfdc_pb2.SfdcObjectMetadata, _Mapping]] = ..., field_metadata: _Optional[_Union[_sfdc_pb2.Field, _Mapping]] = ..., profile_api_name: _Optional[str] = ...) -> None: ...

class CreateObjectFieldResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteObjectFieldArg(_message.Message):
    __slots__ = ("source_connector_params", "object_metadata", "field_name")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    object_metadata: _sfdc_pb2.SfdcObjectMetadata
    field_name: str
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., object_metadata: _Optional[_Union[_sfdc_pb2.SfdcObjectMetadata, _Mapping]] = ..., field_name: _Optional[str] = ...) -> None: ...

class DeleteObjectFieldResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DownloadObjectDataArg(_message.Message):
    __slots__ = ("source_connector_params", "excluded_fields", "object_metadata", "sf_snapshot_time", "prev_sf_snapshot_time", "s3_info", "task_id", "sfdc_locator", "part_number", "upload_id", "etags_vec")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    SF_SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    PREV_SF_SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    S3_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SFDC_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    ETAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    excluded_fields: _containers.RepeatedScalarFieldContainer[str]
    object_metadata: _sfdc_pb2.SfdcObjectMetadata
    sf_snapshot_time: str
    prev_sf_snapshot_time: str
    s3_info: _sfdc_pb2.S3BucketInfo
    task_id: int
    sfdc_locator: str
    part_number: int
    upload_id: str
    etags_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., excluded_fields: _Optional[_Iterable[str]] = ..., object_metadata: _Optional[_Union[_sfdc_pb2.SfdcObjectMetadata, _Mapping]] = ..., sf_snapshot_time: _Optional[str] = ..., prev_sf_snapshot_time: _Optional[str] = ..., s3_info: _Optional[_Union[_sfdc_pb2.S3BucketInfo, _Mapping]] = ..., task_id: _Optional[int] = ..., sfdc_locator: _Optional[str] = ..., part_number: _Optional[int] = ..., upload_id: _Optional[str] = ..., etags_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class DownloadObjectDataResult(_message.Message):
    __slots__ = ("error", "is_uploaded_to_s3", "no_of_rows_returned", "no_of_records_in_sfdc_recycle_bin", "sfdc_locator", "etags_vec", "no_of_parts_uploaded_to_s3", "upload_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_UPLOADED_TO_S3_FIELD_NUMBER: _ClassVar[int]
    NO_OF_ROWS_RETURNED_FIELD_NUMBER: _ClassVar[int]
    NO_OF_RECORDS_IN_SFDC_RECYCLE_BIN_FIELD_NUMBER: _ClassVar[int]
    SFDC_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    ETAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    NO_OF_PARTS_UPLOADED_TO_S3_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    is_uploaded_to_s3: bool
    no_of_rows_returned: int
    no_of_records_in_sfdc_recycle_bin: int
    sfdc_locator: str
    etags_vec: _containers.RepeatedScalarFieldContainer[str]
    no_of_parts_uploaded_to_s3: int
    upload_id: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., is_uploaded_to_s3: bool = ..., no_of_rows_returned: _Optional[int] = ..., no_of_records_in_sfdc_recycle_bin: _Optional[int] = ..., sfdc_locator: _Optional[str] = ..., etags_vec: _Optional[_Iterable[str]] = ..., no_of_parts_uploaded_to_s3: _Optional[int] = ..., upload_id: _Optional[str] = ...) -> None: ...

class UploadObjectDataArg(_message.Message):
    __slots__ = ("source_connector_params", "csv_file_path", "csv_file_path_failed_records", "csv_fields_vec", "object_metadata_store", "should_create_records", "object_name")
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CSV_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CSV_FILE_PATH_FAILED_RECORDS_FIELD_NUMBER: _ClassVar[int]
    CSV_FIELDS_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_STORE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_CREATE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    csv_file_path: str
    csv_file_path_failed_records: str
    csv_fields_vec: _containers.RepeatedCompositeFieldContainer[_sfdc_pb2.SfdcRecoverField]
    object_metadata_store: _sfdc_pb2.SfdcObjectMetadataStore
    should_create_records: bool
    object_name: str
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ..., csv_file_path: _Optional[str] = ..., csv_file_path_failed_records: _Optional[str] = ..., csv_fields_vec: _Optional[_Iterable[_Union[_sfdc_pb2.SfdcRecoverField, _Mapping]]] = ..., object_metadata_store: _Optional[_Union[_sfdc_pb2.SfdcObjectMetadataStore, _Mapping]] = ..., should_create_records: bool = ..., object_name: _Optional[str] = ...) -> None: ...

class UploadObjectDataResult(_message.Message):
    __slots__ = ("error", "upload_data_stats", "updated_salesforce_ids")
    class UploadObjectDataStats(_message.Message):
        __slots__ = ("number_of_records_created", "number_of_records_modified", "number_of_records_failed")
        NUMBER_OF_RECORDS_CREATED_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_RECORDS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_RECORDS_FAILED_FIELD_NUMBER: _ClassVar[int]
        number_of_records_created: int
        number_of_records_modified: int
        number_of_records_failed: int
        def __init__(self, number_of_records_created: _Optional[int] = ..., number_of_records_modified: _Optional[int] = ..., number_of_records_failed: _Optional[int] = ...) -> None: ...
    class UpdatedSalesforceIds(_message.Message):
        __slots__ = ("backup_id", "new_id")
        BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
        NEW_ID_FIELD_NUMBER: _ClassVar[int]
        backup_id: str
        new_id: str
        def __init__(self, backup_id: _Optional[str] = ..., new_id: _Optional[str] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SALESFORCE_IDS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    upload_data_stats: UploadObjectDataResult.UploadObjectDataStats
    updated_salesforce_ids: _containers.RepeatedCompositeFieldContainer[UploadObjectDataResult.UpdatedSalesforceIds]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., upload_data_stats: _Optional[_Union[UploadObjectDataResult.UploadObjectDataStats, _Mapping]] = ..., updated_salesforce_ids: _Optional[_Iterable[_Union[UploadObjectDataResult.UpdatedSalesforceIds, _Mapping]]] = ...) -> None: ...

class RefreshAccessTokenArg(_message.Message):
    __slots__ = ("source_connector_params",)
    SOURCE_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    source_connector_params: _sfdc_pb2.RegisteredEntitySfdcParams
    def __init__(self, source_connector_params: _Optional[_Union[_sfdc_pb2.RegisteredEntitySfdcParams, _Mapping]] = ...) -> None: ...

class RefreshAccessTokenResult(_message.Message):
    __slots__ = ("error", "access_token", "signature", "scope", "instance_url", "id", "token_type", "access_token_issue_timestamp")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_ISSUE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    access_token: str
    signature: str
    scope: str
    instance_url: str
    id: str
    token_type: str
    access_token_issue_timestamp: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., access_token: _Optional[str] = ..., signature: _Optional[str] = ..., scope: _Optional[str] = ..., instance_url: _Optional[str] = ..., id: _Optional[str] = ..., token_type: _Optional[str] = ..., access_token_issue_timestamp: _Optional[str] = ...) -> None: ...

class GetServerTimestampArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetServerTimestampResult(_message.Message):
    __slots__ = ("sfdc_server_timestamp_usecs", "error")
    SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sfdc_server_timestamp_usecs: int
    error: _error_pb2.ErrorProto
    def __init__(self, sfdc_server_timestamp_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class BulkQueryJobArg(_message.Message):
    __slots__ = ("operation", "query", "content_type", "column_delimiter", "line_ending", "object_name", "task_id")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    operation: str
    query: str
    content_type: str
    column_delimiter: str
    line_ending: str
    object_name: str
    task_id: int
    def __init__(self, operation: _Optional[str] = ..., query: _Optional[str] = ..., content_type: _Optional[str] = ..., column_delimiter: _Optional[str] = ..., line_ending: _Optional[str] = ..., object_name: _Optional[str] = ..., task_id: _Optional[int] = ...) -> None: ...

class BulkQueryJobResult(_message.Message):
    __slots__ = ("id", "operation", "object", "created_by_id", "created_date", "system_modstamp", "state", "concurrency_mode", "content_type", "api_version", "line_ending", "column_delimiter", "job_type", "number_of_records_processed", "retries", "total_processing_time", "error", "bulk_unsupported")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MODSTAMP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_RECORDS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BULK_UNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    id: str
    operation: str
    object: str
    created_by_id: str
    created_date: str
    system_modstamp: str
    state: str
    concurrency_mode: str
    content_type: str
    api_version: float
    line_ending: str
    column_delimiter: str
    job_type: str
    number_of_records_processed: int
    retries: int
    total_processing_time: int
    error: _error_pb2.ErrorProto
    bulk_unsupported: bool
    def __init__(self, id: _Optional[str] = ..., operation: _Optional[str] = ..., object: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_date: _Optional[str] = ..., system_modstamp: _Optional[str] = ..., state: _Optional[str] = ..., concurrency_mode: _Optional[str] = ..., content_type: _Optional[str] = ..., api_version: _Optional[float] = ..., line_ending: _Optional[str] = ..., column_delimiter: _Optional[str] = ..., job_type: _Optional[str] = ..., number_of_records_processed: _Optional[int] = ..., retries: _Optional[int] = ..., total_processing_time: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., bulk_unsupported: bool = ...) -> None: ...

class BulkQueryJobInfoArg(_message.Message):
    __slots__ = ("job_id", "object_name", "task_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    object_name: str
    task_id: int
    def __init__(self, job_id: _Optional[str] = ..., object_name: _Optional[str] = ..., task_id: _Optional[int] = ...) -> None: ...

class BulkQueryJobDownloadResultsArg(_message.Message):
    __slots__ = ("job_id", "sfdc_locator", "no_of_records_to_download", "snapshot_time", "object_name", "part_number", "upload_id", "etags_vec", "s3_info", "task_id", "has_last_modified_date_field")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SFDC_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    NO_OF_RECORDS_TO_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    ETAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    S3_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_LAST_MODIFIED_DATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    sfdc_locator: str
    no_of_records_to_download: int
    snapshot_time: str
    object_name: str
    part_number: int
    upload_id: str
    etags_vec: _containers.RepeatedScalarFieldContainer[str]
    s3_info: _sfdc_pb2.S3BucketInfo
    task_id: int
    has_last_modified_date_field: bool
    def __init__(self, job_id: _Optional[str] = ..., sfdc_locator: _Optional[str] = ..., no_of_records_to_download: _Optional[int] = ..., snapshot_time: _Optional[str] = ..., object_name: _Optional[str] = ..., part_number: _Optional[int] = ..., upload_id: _Optional[str] = ..., etags_vec: _Optional[_Iterable[str]] = ..., s3_info: _Optional[_Union[_sfdc_pb2.S3BucketInfo, _Mapping]] = ..., task_id: _Optional[int] = ..., has_last_modified_date_field: bool = ...) -> None: ...

class BulkQueryJobDownloadResultsResult(_message.Message):
    __slots__ = ("error", "sfdc_locator", "no_of_rows_returned", "etags_vec", "no_of_parts_uploaded_to_s3", "upload_id", "is_uploaded_to_s3", "no_of_records_in_sfdc_recycle_bin", "downloaded_batch_size", "retry_download", "time_stats")
    class OperationTimeStats(_message.Message):
        __slots__ = ("csv_preprocessing_time", "data_download_time", "data_upload_s3_time")
        CSV_PREPROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
        DATA_DOWNLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
        DATA_UPLOAD_S3_TIME_FIELD_NUMBER: _ClassVar[int]
        csv_preprocessing_time: int
        data_download_time: int
        data_upload_s3_time: int
        def __init__(self, csv_preprocessing_time: _Optional[int] = ..., data_download_time: _Optional[int] = ..., data_upload_s3_time: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SFDC_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    NO_OF_ROWS_RETURNED_FIELD_NUMBER: _ClassVar[int]
    ETAGS_VEC_FIELD_NUMBER: _ClassVar[int]
    NO_OF_PARTS_UPLOADED_TO_S3_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    IS_UPLOADED_TO_S3_FIELD_NUMBER: _ClassVar[int]
    NO_OF_RECORDS_IN_SFDC_RECYCLE_BIN_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADED_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    RETRY_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    TIME_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    sfdc_locator: str
    no_of_rows_returned: int
    etags_vec: _containers.RepeatedScalarFieldContainer[str]
    no_of_parts_uploaded_to_s3: int
    upload_id: str
    is_uploaded_to_s3: bool
    no_of_records_in_sfdc_recycle_bin: int
    downloaded_batch_size: int
    retry_download: bool
    time_stats: BulkQueryJobDownloadResultsResult.OperationTimeStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., sfdc_locator: _Optional[str] = ..., no_of_rows_returned: _Optional[int] = ..., etags_vec: _Optional[_Iterable[str]] = ..., no_of_parts_uploaded_to_s3: _Optional[int] = ..., upload_id: _Optional[str] = ..., is_uploaded_to_s3: bool = ..., no_of_records_in_sfdc_recycle_bin: _Optional[int] = ..., downloaded_batch_size: _Optional[int] = ..., retry_download: bool = ..., time_stats: _Optional[_Union[BulkQueryJobDownloadResultsResult.OperationTimeStats, _Mapping]] = ...) -> None: ...

class GetFilesMetadataArg(_message.Message):
    __slots__ = ("query", "url_to_fetch_next_batch", "task_id")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    URL_TO_FETCH_NEXT_BATCH_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    query: str
    url_to_fetch_next_batch: str
    task_id: int
    def __init__(self, query: _Optional[str] = ..., url_to_fetch_next_batch: _Optional[str] = ..., task_id: _Optional[int] = ...) -> None: ...

class GetFilesMetadataResult(_message.Message):
    __slots__ = ("total_size", "is_done", "records", "next_records_url", "error")
    class Attributes(_message.Message):
        __slots__ = ("type", "url")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: str
        url: str
        def __init__(self, type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Linkedentity(_message.Message):
        __slots__ = ("attributes", "type")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        attributes: GetFilesMetadataResult.Attributes
        type: str
        def __init__(self, attributes: _Optional[_Union[GetFilesMetadataResult.Attributes, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...
    class ContentDocumentLinkRecord(_message.Message):
        __slots__ = ("attributes", "content_document_id", "linked_entity_id", "share_type", "visibility", "linked_entity", "system_modstamp")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        LINKED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        LINKED_ENTITY_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_MODSTAMP_FIELD_NUMBER: _ClassVar[int]
        attributes: GetFilesMetadataResult.Attributes
        content_document_id: str
        linked_entity_id: str
        share_type: str
        visibility: str
        linked_entity: GetFilesMetadataResult.Linkedentity
        system_modstamp: str
        def __init__(self, attributes: _Optional[_Union[GetFilesMetadataResult.Attributes, _Mapping]] = ..., content_document_id: _Optional[str] = ..., linked_entity_id: _Optional[str] = ..., share_type: _Optional[str] = ..., visibility: _Optional[str] = ..., linked_entity: _Optional[_Union[GetFilesMetadataResult.Linkedentity, _Mapping]] = ..., system_modstamp: _Optional[str] = ...) -> None: ...
    class ContentDocumentLinks(_message.Message):
        __slots__ = ("total_size", "done", "records")
        TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        DONE_FIELD_NUMBER: _ClassVar[int]
        RECORDS_FIELD_NUMBER: _ClassVar[int]
        total_size: int
        done: bool
        records: _containers.RepeatedCompositeFieldContainer[GetFilesMetadataResult.ContentDocumentLinkRecord]
        def __init__(self, total_size: _Optional[int] = ..., done: bool = ..., records: _Optional[_Iterable[_Union[GetFilesMetadataResult.ContentDocumentLinkRecord, _Mapping]]] = ...) -> None: ...
    class ContentVersionRecord(_message.Message):
        __slots__ = ("attributes", "content_document_id", "id", "checksum", "path_on_client", "content_location", "last_modified_date", "path_on_view", "version_number", "is_deleted", "file_size")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        PATH_ON_CLIENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_LOCATION_FIELD_NUMBER: _ClassVar[int]
        LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
        PATH_ON_VIEW_FIELD_NUMBER: _ClassVar[int]
        VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IS_DELETED_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        attributes: GetFilesMetadataResult.Attributes
        content_document_id: str
        id: str
        checksum: str
        path_on_client: str
        content_location: str
        last_modified_date: str
        path_on_view: str
        version_number: str
        is_deleted: bool
        file_size: int
        def __init__(self, attributes: _Optional[_Union[GetFilesMetadataResult.Attributes, _Mapping]] = ..., content_document_id: _Optional[str] = ..., id: _Optional[str] = ..., checksum: _Optional[str] = ..., path_on_client: _Optional[str] = ..., content_location: _Optional[str] = ..., last_modified_date: _Optional[str] = ..., path_on_view: _Optional[str] = ..., version_number: _Optional[str] = ..., is_deleted: bool = ..., file_size: _Optional[int] = ...) -> None: ...
    class ContentVersions(_message.Message):
        __slots__ = ("total_size", "done", "records")
        TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
        DONE_FIELD_NUMBER: _ClassVar[int]
        RECORDS_FIELD_NUMBER: _ClassVar[int]
        total_size: int
        done: bool
        records: _containers.RepeatedCompositeFieldContainer[GetFilesMetadataResult.ContentVersionRecord]
        def __init__(self, total_size: _Optional[int] = ..., done: bool = ..., records: _Optional[_Iterable[_Union[GetFilesMetadataResult.ContentVersionRecord, _Mapping]]] = ...) -> None: ...
    class ContentDocumentRecord(_message.Message):
        __slots__ = ("attributes", "id", "title", "file_extension", "is_deleted", "owner_id", "publish_status", "description", "sharing_privacy", "last_modified_date", "content_document_links", "content_versions")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        IS_DELETED_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        PUBLISH_STATUS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SHARING_PRIVACY_FIELD_NUMBER: _ClassVar[int]
        LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DOCUMENT_LINKS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        attributes: GetFilesMetadataResult.Attributes
        id: str
        title: str
        file_extension: str
        is_deleted: bool
        owner_id: str
        publish_status: str
        description: str
        sharing_privacy: str
        last_modified_date: str
        content_document_links: GetFilesMetadataResult.ContentDocumentLinks
        content_versions: GetFilesMetadataResult.ContentVersions
        def __init__(self, attributes: _Optional[_Union[GetFilesMetadataResult.Attributes, _Mapping]] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., file_extension: _Optional[str] = ..., is_deleted: bool = ..., owner_id: _Optional[str] = ..., publish_status: _Optional[str] = ..., description: _Optional[str] = ..., sharing_privacy: _Optional[str] = ..., last_modified_date: _Optional[str] = ..., content_document_links: _Optional[_Union[GetFilesMetadataResult.ContentDocumentLinks, _Mapping]] = ..., content_versions: _Optional[_Union[GetFilesMetadataResult.ContentVersions, _Mapping]] = ...) -> None: ...
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_RECORDS_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    total_size: int
    is_done: bool
    records: _containers.RepeatedCompositeFieldContainer[GetFilesMetadataResult.ContentDocumentRecord]
    next_records_url: str
    error: _error_pb2.ErrorProto
    def __init__(self, total_size: _Optional[int] = ..., is_done: bool = ..., records: _Optional[_Iterable[_Union[GetFilesMetadataResult.ContentDocumentRecord, _Mapping]]] = ..., next_records_url: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DownloadFileArg(_message.Message):
    __slots__ = ("id", "base_path", "file_name_on_view", "is_file", "task_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_ON_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_FILE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    base_path: str
    file_name_on_view: str
    is_file: bool
    task_id: int
    def __init__(self, id: _Optional[str] = ..., base_path: _Optional[str] = ..., file_name_on_view: _Optional[str] = ..., is_file: bool = ..., task_id: _Optional[int] = ...) -> None: ...

class DownloadFileResult(_message.Message):
    __slots__ = ("file_content",)
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    file_content: str
    def __init__(self, file_content: _Optional[str] = ...) -> None: ...

class UploadFilesArg(_message.Message):
    __slots__ = ("rows", "view_root_name", "last_content_document_id", "last_response_id", "task_id", "task_id_str")
    class Row(_message.Message):
        __slots__ = ("row",)
        class RowEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ROW_FIELD_NUMBER: _ClassVar[int]
        row: _containers.ScalarMap[str, str]
        def __init__(self, row: _Optional[_Mapping[str, str]] = ...) -> None: ...
    ROWS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_CONTENT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_STR_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[UploadFilesArg.Row]
    view_root_name: str
    last_content_document_id: str
    last_response_id: str
    task_id: int
    task_id_str: str
    def __init__(self, rows: _Optional[_Iterable[_Union[UploadFilesArg.Row, _Mapping]]] = ..., view_root_name: _Optional[str] = ..., last_content_document_id: _Optional[str] = ..., last_response_id: _Optional[str] = ..., task_id: _Optional[int] = ..., task_id_str: _Optional[str] = ...) -> None: ...

class UploadFilesResult(_message.Message):
    __slots__ = ("last_content_document_id", "last_response_id")
    LAST_CONTENT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    last_content_document_id: str
    last_response_id: str
    def __init__(self, last_content_document_id: _Optional[str] = ..., last_response_id: _Optional[str] = ...) -> None: ...

class UploadFileVersionArg(_message.Message):
    __slots__ = ("title", "path_on_client", "content_location", "owner_id", "version_data", "sharing_privacy", "description")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PATH_ON_CLIENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_DATA_FIELD_NUMBER: _ClassVar[int]
    SHARING_PRIVACY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    title: str
    path_on_client: str
    content_location: str
    owner_id: str
    version_data: str
    sharing_privacy: str
    description: str
    def __init__(self, title: _Optional[str] = ..., path_on_client: _Optional[str] = ..., content_location: _Optional[str] = ..., owner_id: _Optional[str] = ..., version_data: _Optional[str] = ..., sharing_privacy: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class FetchFilesContentDocumentIdResult(_message.Message):
    __slots__ = ("total_size", "done", "records")
    class Record(_message.Message):
        __slots__ = ("id", "content_record_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        CONTENT_RECORD_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        content_record_id: str
        def __init__(self, id: _Optional[str] = ..., content_record_id: _Optional[str] = ...) -> None: ...
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    total_size: int
    done: bool
    records: _containers.RepeatedCompositeFieldContainer[FetchFilesContentDocumentIdResult.Record]
    def __init__(self, total_size: _Optional[int] = ..., done: bool = ..., records: _Optional[_Iterable[_Union[FetchFilesContentDocumentIdResult.Record, _Mapping]]] = ...) -> None: ...

class LinkFileRecordArg(_message.Message):
    __slots__ = ("content_document_id", "linked_entity_id", "visibility", "sharetype")
    CONTENT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LINKED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    SHARETYPE_FIELD_NUMBER: _ClassVar[int]
    content_document_id: str
    linked_entity_id: str
    visibility: str
    sharetype: str
    def __init__(self, content_document_id: _Optional[str] = ..., linked_entity_id: _Optional[str] = ..., visibility: _Optional[str] = ..., sharetype: _Optional[str] = ...) -> None: ...

class IdResult(_message.Message):
    __slots__ = ("id", "success", "errors", "message", "fields", "error_code")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    success: bool
    errors: _containers.RepeatedScalarFieldContainer[str]
    message: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    error_code: str
    def __init__(self, id: _Optional[str] = ..., success: bool = ..., errors: _Optional[_Iterable[str]] = ..., message: _Optional[str] = ..., fields: _Optional[_Iterable[str]] = ..., error_code: _Optional[str] = ...) -> None: ...

class CompositeLinkFileRecordArg(_message.Message):
    __slots__ = ("all_or_none", "collate_subrequests", "composite_request")
    class CompositeRequest(_message.Message):
        __slots__ = ("method", "url", "reference_id", "link_file_record_arg")
        METHOD_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
        LINK_FILE_RECORD_ARG_FIELD_NUMBER: _ClassVar[int]
        method: str
        url: str
        reference_id: str
        link_file_record_arg: LinkFileRecordArg
        def __init__(self, method: _Optional[str] = ..., url: _Optional[str] = ..., reference_id: _Optional[str] = ..., link_file_record_arg: _Optional[_Union[LinkFileRecordArg, _Mapping]] = ...) -> None: ...
    ALL_OR_NONE_FIELD_NUMBER: _ClassVar[int]
    COLLATE_SUBREQUESTS_FIELD_NUMBER: _ClassVar[int]
    COMPOSITE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    all_or_none: bool
    collate_subrequests: bool
    composite_request: _containers.RepeatedCompositeFieldContainer[CompositeLinkFileRecordArg.CompositeRequest]
    def __init__(self, all_or_none: bool = ..., collate_subrequests: bool = ..., composite_request: _Optional[_Iterable[_Union[CompositeLinkFileRecordArg.CompositeRequest, _Mapping]]] = ...) -> None: ...

class GetAttachmentsMetadataArg(_message.Message):
    __slots__ = ("query", "url_to_fetch_next_batch", "task_id")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    URL_TO_FETCH_NEXT_BATCH_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    query: str
    url_to_fetch_next_batch: str
    task_id: int
    def __init__(self, query: _Optional[str] = ..., url_to_fetch_next_batch: _Optional[str] = ..., task_id: _Optional[int] = ...) -> None: ...

class Attributes(_message.Message):
    __slots__ = ("type", "url")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    type: str
    url: str
    def __init__(self, type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class Linkedentity(_message.Message):
    __slots__ = ("attributes", "type")
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attributes: Attributes
    type: str
    def __init__(self, attributes: _Optional[_Union[Attributes, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...

class GetAttachmentsMetadataResult(_message.Message):
    __slots__ = ("total_size", "is_done", "records", "next_records_url")
    class Records(_message.Message):
        __slots__ = ("record_attributes", "id", "name", "content_type", "is_deleted", "owner_id", "parent_id", "last_modified_date", "url", "attachment_size", "description", "path_on_view", "parent_object")
        RECORD_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_DELETED_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        ATTACHMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PATH_ON_VIEW_FIELD_NUMBER: _ClassVar[int]
        PARENT_OBJECT_FIELD_NUMBER: _ClassVar[int]
        record_attributes: Attributes
        id: str
        name: str
        content_type: str
        is_deleted: bool
        owner_id: str
        parent_id: str
        last_modified_date: str
        url: str
        attachment_size: int
        description: str
        path_on_view: str
        parent_object: Linkedentity
        def __init__(self, record_attributes: _Optional[_Union[Attributes, _Mapping]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., content_type: _Optional[str] = ..., is_deleted: bool = ..., owner_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., last_modified_date: _Optional[str] = ..., url: _Optional[str] = ..., attachment_size: _Optional[int] = ..., description: _Optional[str] = ..., path_on_view: _Optional[str] = ..., parent_object: _Optional[_Union[Linkedentity, _Mapping]] = ...) -> None: ...
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_RECORDS_URL_FIELD_NUMBER: _ClassVar[int]
    total_size: int
    is_done: bool
    records: _containers.RepeatedCompositeFieldContainer[GetAttachmentsMetadataResult.Records]
    next_records_url: str
    def __init__(self, total_size: _Optional[int] = ..., is_done: bool = ..., records: _Optional[_Iterable[_Union[GetAttachmentsMetadataResult.Records, _Mapping]]] = ..., next_records_url: _Optional[str] = ...) -> None: ...

class GetProfileApiNameFromIdArg(_message.Message):
    __slots__ = ("query", "url_to_fetch_next_batch")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    URL_TO_FETCH_NEXT_BATCH_FIELD_NUMBER: _ClassVar[int]
    query: str
    url_to_fetch_next_batch: str
    def __init__(self, query: _Optional[str] = ..., url_to_fetch_next_batch: _Optional[str] = ...) -> None: ...

class GetProfileApiNameFromIdResult(_message.Message):
    __slots__ = ("size", "total_size", "is_done", "records", "query_locator", "entity_type_name")
    class Attributes(_message.Message):
        __slots__ = ("type", "url")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: str
        url: str
        def __init__(self, type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Records(_message.Message):
        __slots__ = ("attributes", "id", "name", "full_name")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        attributes: GetProfileApiNameFromIdResult.Attributes
        id: str
        name: str
        full_name: str
        def __init__(self, attributes: _Optional[_Union[GetProfileApiNameFromIdResult.Attributes, _Mapping]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    QUERY_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    size: int
    total_size: int
    is_done: bool
    records: _containers.RepeatedCompositeFieldContainer[GetProfileApiNameFromIdResult.Records]
    query_locator: str
    entity_type_name: str
    def __init__(self, size: _Optional[int] = ..., total_size: _Optional[int] = ..., is_done: bool = ..., records: _Optional[_Iterable[_Union[GetProfileApiNameFromIdResult.Records, _Mapping]]] = ..., query_locator: _Optional[str] = ..., entity_type_name: _Optional[str] = ...) -> None: ...

class BulkIngestCreateJobRequestInfo(_message.Message):
    __slots__ = ("object_name", "operation", "line_ending", "external_id_field_name")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    operation: str
    line_ending: str
    external_id_field_name: str
    def __init__(self, object_name: _Optional[str] = ..., operation: _Optional[str] = ..., line_ending: _Optional[str] = ..., external_id_field_name: _Optional[str] = ...) -> None: ...

class BulkIngestCreateJobResponseInfo(_message.Message):
    __slots__ = ("job_id", "object_name", "operation", "state", "content_type", "api_version", "line_ending", "error_message")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    object_name: str
    operation: str
    state: str
    content_type: str
    api_version: float
    line_ending: str
    error_message: str
    def __init__(self, job_id: _Optional[str] = ..., object_name: _Optional[str] = ..., operation: _Optional[str] = ..., state: _Optional[str] = ..., content_type: _Optional[str] = ..., api_version: _Optional[float] = ..., line_ending: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkIngestUploadDataRequestInfo(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class BulkIngestUploadDataResponseInfo(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class BulkIngestCloseOrAbortJobRequestInfo(_message.Message):
    __slots__ = ("state", "job_id")
    STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    state: str
    job_id: str
    def __init__(self, state: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class BulkIngestCloseOrAbortJobResponseInfo(_message.Message):
    __slots__ = ("state", "job_id", "error_message")
    STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    state: str
    job_id: str
    error_message: str
    def __init__(self, state: _Optional[str] = ..., job_id: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkIngestGetJobInfoRequestInfo(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class BulkIngestGetJobInfoResponseInfo(_message.Message):
    __slots__ = ("job_id", "state", "num_records_processed", "num_records_failed", "error_message")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_FAILED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    state: str
    num_records_processed: int
    num_records_failed: int
    error_message: str
    def __init__(self, job_id: _Optional[str] = ..., state: _Optional[str] = ..., num_records_processed: _Optional[int] = ..., num_records_failed: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkIngestGetJobFailedRecordsRequestInfo(_message.Message):
    __slots__ = ("job_id", "skip_headers", "return_only_backup_sfids")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_BACKUP_SFIDS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    skip_headers: bool
    return_only_backup_sfids: bool
    def __init__(self, job_id: _Optional[str] = ..., skip_headers: bool = ..., return_only_backup_sfids: bool = ...) -> None: ...

class BulkIngestGetJobFailedRecordsResponseInfo(_message.Message):
    __slots__ = ("error_vec", "backup_sfid_vec")
    ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SFID_VEC_FIELD_NUMBER: _ClassVar[int]
    error_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    backup_sfid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., backup_sfid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BulkIngestGetJobUnprocessedRecordsRequestInfo(_message.Message):
    __slots__ = ("job_id", "skip_headers", "return_only_backup_sfids")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ONLY_BACKUP_SFIDS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    skip_headers: bool
    return_only_backup_sfids: bool
    def __init__(self, job_id: _Optional[str] = ..., skip_headers: bool = ..., return_only_backup_sfids: bool = ...) -> None: ...

class BulkIngestGetJobUnprocessedRecordsResponseInfo(_message.Message):
    __slots__ = ("backup_sfid_vec",)
    BACKUP_SFID_VEC_FIELD_NUMBER: _ClassVar[int]
    backup_sfid_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backup_sfid_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BulkIngestGetJobSuccessfulRecordsRequestInfo(_message.Message):
    __slots__ = ("job_id", "skip_headers")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    skip_headers: bool
    def __init__(self, job_id: _Optional[str] = ..., skip_headers: bool = ...) -> None: ...

class BulkIngestGetJobSuccessfulRecordsResponseInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAccessAndRefreshTokenArg(_message.Message):
    __slots__ = ("callback_url", "auth_code", "grant_type", "format", "client_id", "client_secret")
    CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    AUTH_CODE_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    callback_url: str
    auth_code: str
    grant_type: str
    format: str
    client_id: str
    client_secret: str
    def __init__(self, callback_url: _Optional[str] = ..., auth_code: _Optional[str] = ..., grant_type: _Optional[str] = ..., format: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class GetAccessAndRefreshTokenResult(_message.Message):
    __slots__ = ("access_token", "refresh_token", "identity_url", "error")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    identity_url: str
    error: _error_pb2.ErrorProto
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., identity_url: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetSoapUrlsArg(_message.Message):
    __slots__ = ("endpoint", "access_token")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    access_token: str
    def __init__(self, endpoint: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class GetSoapUrlsResult(_message.Message):
    __slots__ = ("urls", "error")
    class Urls(_message.Message):
        __slots__ = ("metadata_url", "partner_url")
        METADATA_URL_FIELD_NUMBER: _ClassVar[int]
        PARTNER_URL_FIELD_NUMBER: _ClassVar[int]
        metadata_url: str
        partner_url: str
        def __init__(self, metadata_url: _Optional[str] = ..., partner_url: _Optional[str] = ...) -> None: ...
    URLS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    urls: GetSoapUrlsResult.Urls
    error: _error_pb2.ErrorProto
    def __init__(self, urls: _Optional[_Union[GetSoapUrlsResult.Urls, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetUserLicensesInfoResult(_message.Message):
    __slots__ = ("error", "total_licenses", "used_licenses", "last_updated_time")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
    USED_LICENSES_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIME_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    total_licenses: int
    used_licenses: int
    last_updated_time: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., total_licenses: _Optional[int] = ..., used_licenses: _Optional[int] = ..., last_updated_time: _Optional[str] = ...) -> None: ...

class GetUserLicensesInfoApiArg(_message.Message):
    __slots__ = ("query", "url_to_fetch_next_batch")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    URL_TO_FETCH_NEXT_BATCH_FIELD_NUMBER: _ClassVar[int]
    query: str
    url_to_fetch_next_batch: str
    def __init__(self, query: _Optional[str] = ..., url_to_fetch_next_batch: _Optional[str] = ...) -> None: ...

class GetUserLicensesInfoApiResult(_message.Message):
    __slots__ = ("total_size", "is_done", "records")
    class Attributes(_message.Message):
        __slots__ = ("type", "url")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: str
        url: str
        def __init__(self, type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Records(_message.Message):
        __slots__ = ("attributes", "total_licenses", "used_licenses", "last_updated_time")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_LICENSES_FIELD_NUMBER: _ClassVar[int]
        USED_LICENSES_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_TIME_FIELD_NUMBER: _ClassVar[int]
        attributes: GetUserLicensesInfoApiResult.Attributes
        total_licenses: int
        used_licenses: int
        last_updated_time: str
        def __init__(self, attributes: _Optional[_Union[GetUserLicensesInfoApiResult.Attributes, _Mapping]] = ..., total_licenses: _Optional[int] = ..., used_licenses: _Optional[int] = ..., last_updated_time: _Optional[str] = ...) -> None: ...
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    total_size: int
    is_done: bool
    records: _containers.RepeatedCompositeFieldContainer[GetUserLicensesInfoApiResult.Records]
    def __init__(self, total_size: _Optional[int] = ..., is_done: bool = ..., records: _Optional[_Iterable[_Union[GetUserLicensesInfoApiResult.Records, _Mapping]]] = ...) -> None: ...

class GetOrganizationInfoResult(_message.Message):
    __slots__ = ("error", "organization_type")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    organization_type: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., organization_type: _Optional[str] = ...) -> None: ...

class GetOrganizationInfoApiArg(_message.Message):
    __slots__ = ("query", "url_to_fetch_next_batch")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    URL_TO_FETCH_NEXT_BATCH_FIELD_NUMBER: _ClassVar[int]
    query: str
    url_to_fetch_next_batch: str
    def __init__(self, query: _Optional[str] = ..., url_to_fetch_next_batch: _Optional[str] = ...) -> None: ...

class GetOrganizationInfoApiResult(_message.Message):
    __slots__ = ("total_size", "is_done", "records")
    class Attributes(_message.Message):
        __slots__ = ("type", "url")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: str
        url: str
        def __init__(self, type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Records(_message.Message):
        __slots__ = ("attributes", "organization_type")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        attributes: GetOrganizationInfoApiResult.Attributes
        organization_type: str
        def __init__(self, attributes: _Optional[_Union[GetOrganizationInfoApiResult.Attributes, _Mapping]] = ..., organization_type: _Optional[str] = ...) -> None: ...
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    total_size: int
    is_done: bool
    records: _containers.RepeatedCompositeFieldContainer[GetOrganizationInfoApiResult.Records]
    def __init__(self, total_size: _Optional[int] = ..., is_done: bool = ..., records: _Optional[_Iterable[_Union[GetOrganizationInfoApiResult.Records, _Mapping]]] = ...) -> None: ...
