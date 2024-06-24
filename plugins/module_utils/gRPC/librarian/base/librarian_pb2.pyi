from librarian.base import config_pb2 as _config_pb2
from librarian.base import error_pb2 as _error_pb2
from librarian.base import schema_pb2 as _schema_pb2
from librarian.base import stats_pb2 as _stats_pb2
from yoda.db import documents_pb2 as _documents_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateIndexArg(_message.Message):
    __slots__ = ("schema", "bucket_id", "data_directory_path", "field_ids_fqn", "for_search_index", "cloud_config", "disk_id")
    class FieldIdsFqnEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    FIELD_IDS_FQN_FIELD_NUMBER: _ClassVar[int]
    FOR_SEARCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    schema: _schema_pb2.IndexSchema
    bucket_id: int
    data_directory_path: str
    field_ids_fqn: _containers.ScalarMap[int, str]
    for_search_index: bool
    cloud_config: _config_pb2.CloudConfig
    disk_id: int
    def __init__(self, schema: _Optional[_Union[_schema_pb2.IndexSchema, _Mapping]] = ..., bucket_id: _Optional[int] = ..., data_directory_path: _Optional[str] = ..., field_ids_fqn: _Optional[_Mapping[int, str]] = ..., for_search_index: bool = ..., cloud_config: _Optional[_Union[_config_pb2.CloudConfig, _Mapping]] = ..., disk_id: _Optional[int] = ...) -> None: ...

class CreateIndexResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteIndexArg(_message.Message):
    __slots__ = ("index_name", "for_search_index", "cloud_config")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    FOR_SEARCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    for_search_index: bool
    cloud_config: _config_pb2.CloudConfig
    def __init__(self, index_name: _Optional[str] = ..., for_search_index: bool = ..., cloud_config: _Optional[_Union[_config_pb2.CloudConfig, _Mapping]] = ...) -> None: ...

class DeleteIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateIndexArg(_message.Message):
    __slots__ = ("schema", "field_ids_fqn", "for_search_index", "cloud_config")
    class FieldIdsFqnEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    FIELD_IDS_FQN_FIELD_NUMBER: _ClassVar[int]
    FOR_SEARCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    schema: _schema_pb2.IndexSchema
    field_ids_fqn: _containers.ScalarMap[int, str]
    for_search_index: bool
    cloud_config: _config_pb2.CloudConfig
    def __init__(self, schema: _Optional[_Union[_schema_pb2.IndexSchema, _Mapping]] = ..., field_ids_fqn: _Optional[_Mapping[int, str]] = ..., for_search_index: bool = ..., cloud_config: _Optional[_Union[_config_pb2.CloudConfig, _Mapping]] = ...) -> None: ...

class UpdateIndexResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BucketRpcError(_message.Message):
    __slots__ = ("bucket_id", "error")
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, bucket_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetIndexStatusArg(_message.Message):
    __slots__ = ("name", "bucket_rpc_error_vec", "for_search_index")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKET_RPC_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    FOR_SEARCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    name: str
    bucket_rpc_error_vec: _containers.RepeatedCompositeFieldContainer[BucketRpcError]
    for_search_index: bool
    def __init__(self, name: _Optional[str] = ..., bucket_rpc_error_vec: _Optional[_Iterable[_Union[BucketRpcError, _Mapping]]] = ..., for_search_index: bool = ...) -> None: ...

class GetIndexStatusResult(_message.Message):
    __slots__ = ("index_info", "reassigned")
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    REASSIGNED_FIELD_NUMBER: _ClassVar[int]
    index_info: _config_pb2.IndexInfo
    reassigned: bool
    def __init__(self, index_info: _Optional[_Union[_config_pb2.IndexInfo, _Mapping]] = ..., reassigned: bool = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ("id", "data", "index_fields", "index_field_ids", "index_field_values")
    class Value(_message.Message):
        __slots__ = ("string_value", "int64_value", "uint64_value", "bool_value", "multi_string_value")
        class MultiStringValue(_message.Message):
            __slots__ = ("string_vec",)
            STRING_VEC_FIELD_NUMBER: _ClassVar[int]
            string_vec: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, string_vec: _Optional[_Iterable[str]] = ...) -> None: ...
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        MULTI_STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        string_value: str
        int64_value: int
        uint64_value: int
        bool_value: bool
        multi_string_value: Document.Value.MultiStringValue
        def __init__(self, string_value: _Optional[str] = ..., int64_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., bool_value: bool = ..., multi_string_value: _Optional[_Union[Document.Value.MultiStringValue, _Mapping]] = ...) -> None: ...
    class IndexFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Document.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Document.Value, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_VALUES_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: bytes
    index_fields: _containers.MessageMap[str, Document.Value]
    index_field_ids: _containers.RepeatedScalarFieldContainer[int]
    index_field_values: _containers.RepeatedCompositeFieldContainer[Document.Value]
    def __init__(self, id: _Optional[str] = ..., data: _Optional[bytes] = ..., index_fields: _Optional[_Mapping[str, Document.Value]] = ..., index_field_ids: _Optional[_Iterable[int]] = ..., index_field_values: _Optional[_Iterable[_Union[Document.Value, _Mapping]]] = ...) -> None: ...

class DocumentResponse(_message.Message):
    __slots__ = ("document", "error", "score", "debug_data")
    class DebugData(_message.Message):
        __slots__ = ("node", "explanation")
        NODE_FIELD_NUMBER: _ClassVar[int]
        EXPLANATION_FIELD_NUMBER: _ClassVar[int]
        node: str
        explanation: str
        def __init__(self, node: _Optional[str] = ..., explanation: _Optional[str] = ...) -> None: ...
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_DATA_FIELD_NUMBER: _ClassVar[int]
    document: Document
    error: _error_pb2.ErrorProto
    score: float
    debug_data: DocumentResponse.DebugData
    def __init__(self, document: _Optional[_Union[Document, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., score: _Optional[float] = ..., debug_data: _Optional[_Union[DocumentResponse.DebugData, _Mapping]] = ...) -> None: ...

class AddDocumentsArg(_message.Message):
    __slots__ = ("index_name", "document_vec", "bucket_id", "index_incarnation_id", "bucket_incarnation_id", "for_replication", "document_id_prefix", "commit", "destination_session_id", "merge_function_arg", "overwrite", "disk_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    FOR_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MERGE_FUNCTION_ARG_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    document_vec: _containers.RepeatedCompositeFieldContainer[Document]
    bucket_id: int
    index_incarnation_id: int
    bucket_incarnation_id: int
    for_replication: bool
    document_id_prefix: _containers.RepeatedScalarFieldContainer[str]
    commit: bool
    destination_session_id: int
    merge_function_arg: bytes
    overwrite: bool
    disk_id: int
    def __init__(self, index_name: _Optional[str] = ..., document_vec: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., bucket_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., for_replication: bool = ..., document_id_prefix: _Optional[_Iterable[str]] = ..., commit: bool = ..., destination_session_id: _Optional[int] = ..., merge_function_arg: _Optional[bytes] = ..., overwrite: bool = ..., disk_id: _Optional[int] = ...) -> None: ...

class AddDocumentsResult(_message.Message):
    __slots__ = ("error", "response_vec", "doc_stats")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VEC_FIELD_NUMBER: _ClassVar[int]
    DOC_STATS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    response_vec: _containers.RepeatedCompositeFieldContainer[DocumentResponse]
    doc_stats: _stats_pb2.DocumentStats
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., response_vec: _Optional[_Iterable[_Union[DocumentResponse, _Mapping]]] = ..., doc_stats: _Optional[_Union[_stats_pb2.DocumentStats, _Mapping]] = ...) -> None: ...

class DeleteDocumentsArg(_message.Message):
    __slots__ = ("index_name", "document_vec", "bucket_id", "index_incarnation_id", "bucket_incarnation_id", "document_id_prefix", "commit", "disk_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    document_vec: _containers.RepeatedCompositeFieldContainer[Document]
    bucket_id: int
    index_incarnation_id: int
    bucket_incarnation_id: int
    document_id_prefix: str
    commit: bool
    disk_id: int
    def __init__(self, index_name: _Optional[str] = ..., document_vec: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., bucket_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., document_id_prefix: _Optional[str] = ..., commit: bool = ..., disk_id: _Optional[int] = ...) -> None: ...

class DeleteDocumentsResult(_message.Message):
    __slots__ = ("error", "response_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    response_vec: _containers.RepeatedCompositeFieldContainer[DocumentResponse]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., response_vec: _Optional[_Iterable[_Union[DocumentResponse, _Mapping]]] = ...) -> None: ...

class LuceneSearchCookie(_message.Message):
    __slots__ = ("doc_id", "score")
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    doc_id: int
    score: float
    def __init__(self, doc_id: _Optional[int] = ..., score: _Optional[float] = ...) -> None: ...

class Cookie(_message.Message):
    __slots__ = ("offset", "scan_cookie", "update_cookie", "pagination_cookie", "websafe_pagination_cookie")
    class ScanState(_message.Message):
        __slots__ = ("document_for_replica", "incarnation_id")
        class DocumentForReplicaEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: str
            def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
        DOCUMENT_FOR_REPLICA_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        document_for_replica: _containers.ScalarMap[int, str]
        incarnation_id: int
        def __init__(self, document_for_replica: _Optional[_Mapping[int, str]] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
    class PaginationState(_message.Message):
        __slots__ = ("lucene_search_cookie", "bucket_id", "replica_disk_id", "bucket_incarnation_id")
        LUCENE_SEARCH_COOKIE_FIELD_NUMBER: _ClassVar[int]
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        REPLICA_DISK_ID_FIELD_NUMBER: _ClassVar[int]
        BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        lucene_search_cookie: LuceneSearchCookie
        bucket_id: int
        replica_disk_id: int
        bucket_incarnation_id: int
        def __init__(self, lucene_search_cookie: _Optional[_Union[LuceneSearchCookie, _Mapping]] = ..., bucket_id: _Optional[int] = ..., replica_disk_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ...) -> None: ...
    class ScanCookieEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Cookie.ScanState
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Cookie.ScanState, _Mapping]] = ...) -> None: ...
    class UpdateCookieEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    WEBSAFE_PAGINATION_COOKIE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    scan_cookie: _containers.MessageMap[int, Cookie.ScanState]
    update_cookie: _containers.ScalarMap[int, int]
    pagination_cookie: Cookie.PaginationState
    websafe_pagination_cookie: str
    def __init__(self, offset: _Optional[int] = ..., scan_cookie: _Optional[_Mapping[int, Cookie.ScanState]] = ..., update_cookie: _Optional[_Mapping[int, int]] = ..., pagination_cookie: _Optional[_Union[Cookie.PaginationState, _Mapping]] = ..., websafe_pagination_cookie: _Optional[str] = ...) -> None: ...

class SearchQuery(_message.Message):
    __slots__ = ("search_clause", "sort_order_vec")
    class SortDirectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAscending: _ClassVar[SearchQuery.SortDirectionType]
        kDescending: _ClassVar[SearchQuery.SortDirectionType]
    kAscending: SearchQuery.SortDirectionType
    kDescending: SearchQuery.SortDirectionType
    class SortOrder(_message.Message):
        __slots__ = ("field_name", "direction")
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        direction: SearchQuery.SortDirectionType
        def __init__(self, field_name: _Optional[str] = ..., direction: _Optional[_Union[SearchQuery.SortDirectionType, str]] = ...) -> None: ...
    SEARCH_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_VEC_FIELD_NUMBER: _ClassVar[int]
    search_clause: _schema_pb2.SearchClause
    sort_order_vec: SearchQuery.SortOrder
    def __init__(self, search_clause: _Optional[_Union[_schema_pb2.SearchClause, _Mapping]] = ..., sort_order_vec: _Optional[_Union[SearchQuery.SortOrder, _Mapping]] = ...) -> None: ...

class GetDocumentsArg(_message.Message):
    __slots__ = ("index_name", "document_id_vec", "search_query", "cookie", "num_results", "debug", "transform_documents_function", "bucket_id", "index_incarnation_id", "bucket_incarnation_id", "paginate_search_results", "disk_id", "tenant_id", "read_mode")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    NUM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_DOCUMENTS_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    READ_MODE_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    document_id_vec: _containers.RepeatedScalarFieldContainer[str]
    search_query: SearchQuery
    cookie: Cookie
    num_results: int
    debug: bool
    transform_documents_function: str
    bucket_id: int
    index_incarnation_id: int
    bucket_incarnation_id: int
    paginate_search_results: bool
    disk_id: int
    tenant_id: str
    read_mode: _documents_pb2.LibrarianObjectPrefixFormatMode
    def __init__(self, index_name: _Optional[str] = ..., document_id_vec: _Optional[_Iterable[str]] = ..., search_query: _Optional[_Union[SearchQuery, _Mapping]] = ..., cookie: _Optional[_Union[Cookie, _Mapping]] = ..., num_results: _Optional[int] = ..., debug: bool = ..., transform_documents_function: _Optional[str] = ..., bucket_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., paginate_search_results: bool = ..., disk_id: _Optional[int] = ..., tenant_id: _Optional[str] = ..., read_mode: _Optional[_Union[_documents_pb2.LibrarianObjectPrefixFormatMode, str]] = ...) -> None: ...

class DocumentsResultMetadata(_message.Message):
    __slots__ = ("bucket_id", "pre_scan_result_metadata", "post_scan_result_metadata")
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_SCAN_RESULT_METADATA_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_RESULT_METADATA_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    pre_scan_result_metadata: bytes
    post_scan_result_metadata: bytes
    def __init__(self, bucket_id: _Optional[int] = ..., pre_scan_result_metadata: _Optional[bytes] = ..., post_scan_result_metadata: _Optional[bytes] = ...) -> None: ...

class GetDocumentsResult(_message.Message):
    __slots__ = ("error", "response_vec", "cookie", "result_metadata", "read_mode")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    RESULT_METADATA_FIELD_NUMBER: _ClassVar[int]
    READ_MODE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    response_vec: _containers.RepeatedCompositeFieldContainer[DocumentResponse]
    cookie: Cookie
    result_metadata: DocumentsResultMetadata
    read_mode: _documents_pb2.LibrarianObjectPrefixFormatMode
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., response_vec: _Optional[_Iterable[_Union[DocumentResponse, _Mapping]]] = ..., cookie: _Optional[_Union[Cookie, _Mapping]] = ..., result_metadata: _Optional[_Union[DocumentsResultMetadata, _Mapping]] = ..., read_mode: _Optional[_Union[_documents_pb2.LibrarianObjectPrefixFormatMode, str]] = ...) -> None: ...

class ScanDocumentsArg(_message.Message):
    __slots__ = ("index_name", "document_id_prefix", "scan_documents_function", "scan_documents_function_arg", "max_response_size_bytes", "max_time_for_processing_usecs", "cookie", "scan_buckets_filter_function", "num_results", "bucket_id", "index_incarnation_id", "bucket_incarnation_id", "disk_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SCAN_DOCUMENTS_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    SCAN_DOCUMENTS_FUNCTION_ARG_FIELD_NUMBER: _ClassVar[int]
    MAX_RESPONSE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_FOR_PROCESSING_USECS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    SCAN_BUCKETS_FILTER_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    NUM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    document_id_prefix: str
    scan_documents_function: str
    scan_documents_function_arg: bytes
    max_response_size_bytes: int
    max_time_for_processing_usecs: int
    cookie: Cookie
    scan_buckets_filter_function: str
    num_results: int
    bucket_id: int
    index_incarnation_id: int
    bucket_incarnation_id: int
    disk_id: int
    def __init__(self, index_name: _Optional[str] = ..., document_id_prefix: _Optional[str] = ..., scan_documents_function: _Optional[str] = ..., scan_documents_function_arg: _Optional[bytes] = ..., max_response_size_bytes: _Optional[int] = ..., max_time_for_processing_usecs: _Optional[int] = ..., cookie: _Optional[_Union[Cookie, _Mapping]] = ..., scan_buckets_filter_function: _Optional[str] = ..., num_results: _Optional[int] = ..., bucket_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., disk_id: _Optional[int] = ...) -> None: ...

class UpdateDocumentsArg(_message.Message):
    __slots__ = ("index_name", "document_id_prefix", "update_documents_function", "update_documents_function_arg", "max_time_for_processing_usecs", "cookie", "start_key", "bucket_id", "index_incarnation_id", "bucket_incarnation_id", "commit", "destination_session_id", "disk_id")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DOCUMENTS_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DOCUMENTS_FUNCTION_ARG_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_FOR_PROCESSING_USECS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    START_KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DISK_ID_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    document_id_prefix: str
    update_documents_function: str
    update_documents_function_arg: bytes
    max_time_for_processing_usecs: int
    cookie: Cookie
    start_key: str
    bucket_id: int
    index_incarnation_id: int
    bucket_incarnation_id: int
    commit: bool
    destination_session_id: int
    disk_id: int
    def __init__(self, index_name: _Optional[str] = ..., document_id_prefix: _Optional[str] = ..., update_documents_function: _Optional[str] = ..., update_documents_function_arg: _Optional[bytes] = ..., max_time_for_processing_usecs: _Optional[int] = ..., cookie: _Optional[_Union[Cookie, _Mapping]] = ..., start_key: _Optional[str] = ..., bucket_id: _Optional[int] = ..., index_incarnation_id: _Optional[int] = ..., bucket_incarnation_id: _Optional[int] = ..., commit: bool = ..., destination_session_id: _Optional[int] = ..., disk_id: _Optional[int] = ...) -> None: ...

class UpdateDocumentsResult(_message.Message):
    __slots__ = ("error", "response_vec", "cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    response_vec: _containers.RepeatedCompositeFieldContainer[DocumentResponse]
    cookie: Cookie
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., response_vec: _Optional[_Iterable[_Union[DocumentResponse, _Mapping]]] = ..., cookie: _Optional[_Union[Cookie, _Mapping]] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LookupMasterResult(_message.Message):
    __slots__ = ("ip", "port", "node_id", "error")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    node_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., node_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetDocumentsBucketIdArg(_message.Message):
    __slots__ = ("index_name", "document_id_vec", "num_buckets", "sharding_function")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    SHARDING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    document_id_vec: _containers.RepeatedScalarFieldContainer[str]
    num_buckets: int
    sharding_function: str
    def __init__(self, index_name: _Optional[str] = ..., document_id_vec: _Optional[_Iterable[str]] = ..., num_buckets: _Optional[int] = ..., sharding_function: _Optional[str] = ...) -> None: ...

class GetDocumentsBucketIdResult(_message.Message):
    __slots__ = ("doc_id_bucket_mapping",)
    class DocIdBucketMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    DOC_ID_BUCKET_MAPPING_FIELD_NUMBER: _ClassVar[int]
    doc_id_bucket_mapping: _containers.ScalarMap[str, int]
    def __init__(self, doc_id_bucket_mapping: _Optional[_Mapping[str, int]] = ...) -> None: ...

class ReadDirScanFunctionArg(_message.Message):
    __slots__ = ("parent_path", "instance_id", "all_instance_ids")
    PARENT_PATH_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    parent_path: str
    instance_id: int
    all_instance_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, parent_path: _Optional[str] = ..., instance_id: _Optional[int] = ..., all_instance_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class FilterChildPrefixesFunctionArg(_message.Message):
    __slots__ = ("child_prefixes_to_filter", "instance_id", "all_instance_ids")
    CHILD_PREFIXES_TO_FILTER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    child_prefixes_to_filter: _containers.RepeatedScalarFieldContainer[str]
    instance_id: int
    all_instance_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, child_prefixes_to_filter: _Optional[_Iterable[str]] = ..., instance_id: _Optional[int] = ..., all_instance_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class ReleaseIndexArg(_message.Message):
    __slots__ = ("index_name",)
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    def __init__(self, index_name: _Optional[str] = ...) -> None: ...

class ReleaseIndexResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class InitiateDataStoreReshardArg(_message.Message):
    __slots__ = ("index_name", "num_desired_shards", "force_clear_old_migration_state")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_DESIRED_SHARDS_FIELD_NUMBER: _ClassVar[int]
    FORCE_CLEAR_OLD_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    num_desired_shards: int
    force_clear_old_migration_state: bool
    def __init__(self, index_name: _Optional[str] = ..., num_desired_shards: _Optional[int] = ..., force_clear_old_migration_state: bool = ...) -> None: ...

class InitiateDataStoreReshardResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
