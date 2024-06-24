from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshSfdcAccessTokenRestRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshSfdcAccessTokenRestResponse(_message.Message):
    __slots__ = ("access_token", "signature", "scope", "instance_url", "id", "token_type", "issued_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    signature: str
    scope: str
    instance_url: str
    id: str
    token_type: str
    issued_at: str
    def __init__(self, access_token: _Optional[str] = ..., signature: _Optional[str] = ..., scope: _Optional[str] = ..., instance_url: _Optional[str] = ..., id: _Optional[str] = ..., token_type: _Optional[str] = ..., issued_at: _Optional[str] = ...) -> None: ...

class BulkBackupRestRequest(_message.Message):
    __slots__ = ("operation", "query", "content_type", "column_delimiter", "line_ending")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    operation: str
    query: str
    content_type: str
    column_delimiter: str
    line_ending: str
    def __init__(self, operation: _Optional[str] = ..., query: _Optional[str] = ..., content_type: _Optional[str] = ..., column_delimiter: _Optional[str] = ..., line_ending: _Optional[str] = ...) -> None: ...

class BulkBackupRestResponse(_message.Message):
    __slots__ = ("id", "operation", "object", "created_by_id", "created_date", "system_modstamp", "state", "concurrency_mode", "content_type", "api_version", "line_ending", "column_delimiter", "job_type", "number_of_records_processed", "retries", "total_processing_time", "error_message")
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
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    error_message: str
    def __init__(self, id: _Optional[str] = ..., operation: _Optional[str] = ..., object: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_date: _Optional[str] = ..., system_modstamp: _Optional[str] = ..., state: _Optional[str] = ..., concurrency_mode: _Optional[str] = ..., content_type: _Optional[str] = ..., api_version: _Optional[float] = ..., line_ending: _Optional[str] = ..., column_delimiter: _Optional[str] = ..., job_type: _Optional[str] = ..., number_of_records_processed: _Optional[int] = ..., retries: _Optional[int] = ..., total_processing_time: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkQueryJobInfoRestRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkQueryJobResultRestRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestCreateJobRequest(_message.Message):
    __slots__ = ("object", "content_type", "operation", "line_ending", "external_id_field_name")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    object: str
    content_type: str
    operation: str
    line_ending: str
    external_id_field_name: str
    def __init__(self, object: _Optional[str] = ..., content_type: _Optional[str] = ..., operation: _Optional[str] = ..., line_ending: _Optional[str] = ..., external_id_field_name: _Optional[str] = ...) -> None: ...

class BulkIngestCreateJobResponse(_message.Message):
    __slots__ = ("id", "operation", "object", "created_by_id", "created_date", "system_mod_stamp", "state", "concurrency_mode", "content_type", "api_version", "content_url", "line_ending", "column_delimiter", "error_message")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MOD_STAMP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    operation: str
    object: str
    created_by_id: str
    created_date: str
    system_mod_stamp: str
    state: str
    concurrency_mode: str
    content_type: str
    api_version: float
    content_url: str
    line_ending: str
    column_delimiter: str
    error_message: str
    def __init__(self, id: _Optional[str] = ..., operation: _Optional[str] = ..., object: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_date: _Optional[str] = ..., system_mod_stamp: _Optional[str] = ..., state: _Optional[str] = ..., concurrency_mode: _Optional[str] = ..., content_type: _Optional[str] = ..., api_version: _Optional[float] = ..., content_url: _Optional[str] = ..., line_ending: _Optional[str] = ..., column_delimiter: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkIngestUploadDataRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestUploadDataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestCloseOrAbortJobRequest(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class BulkIngestCloseOrAbortJobResponse(_message.Message):
    __slots__ = ("id", "operation", "object", "created_by_id", "created_date", "system_mod_stamp", "state", "concurrency_mode", "content_type", "api_version", "error_message")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MOD_STAMP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    operation: str
    object: str
    created_by_id: str
    created_date: str
    system_mod_stamp: str
    state: str
    concurrency_mode: str
    content_type: str
    api_version: float
    error_message: str
    def __init__(self, id: _Optional[str] = ..., operation: _Optional[str] = ..., object: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_date: _Optional[str] = ..., system_mod_stamp: _Optional[str] = ..., state: _Optional[str] = ..., concurrency_mode: _Optional[str] = ..., content_type: _Optional[str] = ..., api_version: _Optional[float] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkIngestGetJobInfoRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class BulkIngestGetJobInfoResponse(_message.Message):
    __slots__ = ("id", "operation", "object", "created_by_id", "created_date", "system_mod_stamp", "state", "concurrency_mode", "content_type", "api_version", "job_type", "line_ending", "column_delimiter", "num_records_processed", "num_records_failed", "retries", "total_processing_time", "api_active_processing_time", "apex_processing_time", "error_message")
    ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MOD_STAMP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    LINE_ENDING_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORDS_FAILED_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    API_ACTIVE_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    APEX_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    operation: str
    object: str
    created_by_id: str
    created_date: str
    system_mod_stamp: str
    state: str
    concurrency_mode: str
    content_type: str
    api_version: float
    job_type: str
    line_ending: str
    column_delimiter: str
    num_records_processed: int
    num_records_failed: int
    retries: int
    total_processing_time: int
    api_active_processing_time: int
    apex_processing_time: int
    error_message: str
    def __init__(self, id: _Optional[str] = ..., operation: _Optional[str] = ..., object: _Optional[str] = ..., created_by_id: _Optional[str] = ..., created_date: _Optional[str] = ..., system_mod_stamp: _Optional[str] = ..., state: _Optional[str] = ..., concurrency_mode: _Optional[str] = ..., content_type: _Optional[str] = ..., api_version: _Optional[float] = ..., job_type: _Optional[str] = ..., line_ending: _Optional[str] = ..., column_delimiter: _Optional[str] = ..., num_records_processed: _Optional[int] = ..., num_records_failed: _Optional[int] = ..., retries: _Optional[int] = ..., total_processing_time: _Optional[int] = ..., api_active_processing_time: _Optional[int] = ..., apex_processing_time: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class BulkIngestGetJobFailedRecordsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestGetJobFailedRecordsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestGetJobUnprocessedRecordsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestGetJobUnprocessedRecordsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestGetJobSuccessfulRecordsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkIngestGetJobSuccessfulRecordsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
