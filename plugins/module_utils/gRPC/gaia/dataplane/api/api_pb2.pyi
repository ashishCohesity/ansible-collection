from gaia.dataplane.base import error_pb2 as _error_pb2
from gaia.dataplane.api import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Filter(_message.Message):
    __slots__ = ("mailbox_accept_filter", "mailbox_reject_filter", "onedrive_accept_filter", "onedrive_reject_filter", "vm_accept_filter", "vm_reject_filter", "cohesity_view_accept_filter", "cohesity_view_reject_filter")
    class DataSensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLow: _ClassVar[Filter.DataSensitivity]
        kMedium: _ClassVar[Filter.DataSensitivity]
        kHigh: _ClassVar[Filter.DataSensitivity]
    kLow: Filter.DataSensitivity
    kMedium: Filter.DataSensitivity
    kHigh: Filter.DataSensitivity
    class MailboxFilter(_message.Message):
        __slots__ = ("data_sensitivity", "expression")
        class Expression(_message.Message):
            __slots__ = ("owner", "from_regex", "to_regex", "date_secs_floor", "date_secs_ceiling", "repeated_expression_or", "repeated_expression_and", "case_insensitive")
            class RepeatedExpression(_message.Message):
                __slots__ = ("expression_vec",)
                EXPRESSION_VEC_FIELD_NUMBER: _ClassVar[int]
                expression_vec: _containers.RepeatedCompositeFieldContainer[Filter.MailboxFilter.Expression]
                def __init__(self, expression_vec: _Optional[_Iterable[_Union[Filter.MailboxFilter.Expression, _Mapping]]] = ...) -> None: ...
            OWNER_FIELD_NUMBER: _ClassVar[int]
            FROM_REGEX_FIELD_NUMBER: _ClassVar[int]
            TO_REGEX_FIELD_NUMBER: _ClassVar[int]
            DATE_SECS_FLOOR_FIELD_NUMBER: _ClassVar[int]
            DATE_SECS_CEILING_FIELD_NUMBER: _ClassVar[int]
            REPEATED_EXPRESSION_OR_FIELD_NUMBER: _ClassVar[int]
            REPEATED_EXPRESSION_AND_FIELD_NUMBER: _ClassVar[int]
            CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
            owner: str
            from_regex: str
            to_regex: str
            date_secs_floor: int
            date_secs_ceiling: int
            repeated_expression_or: Filter.MailboxFilter.Expression.RepeatedExpression
            repeated_expression_and: Filter.MailboxFilter.Expression.RepeatedExpression
            case_insensitive: bool
            def __init__(self, owner: _Optional[str] = ..., from_regex: _Optional[str] = ..., to_regex: _Optional[str] = ..., date_secs_floor: _Optional[int] = ..., date_secs_ceiling: _Optional[int] = ..., repeated_expression_or: _Optional[_Union[Filter.MailboxFilter.Expression.RepeatedExpression, _Mapping]] = ..., repeated_expression_and: _Optional[_Union[Filter.MailboxFilter.Expression.RepeatedExpression, _Mapping]] = ..., case_insensitive: bool = ...) -> None: ...
        DATA_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        data_sensitivity: _containers.RepeatedScalarFieldContainer[Filter.DataSensitivity]
        expression: Filter.MailboxFilter.Expression
        def __init__(self, data_sensitivity: _Optional[_Iterable[_Union[Filter.DataSensitivity, str]]] = ..., expression: _Optional[_Union[Filter.MailboxFilter.Expression, _Mapping]] = ...) -> None: ...
    class FileFilter(_message.Message):
        __slots__ = ("data_sensitivity", "expression")
        class Expression(_message.Message):
            __slots__ = ("owner", "modtime_secs_floor", "modtime_secs_ceiling", "filename_regex", "path_prefix_regex", "document_type", "file_data_sensitivity", "repeated_expression_or", "repeated_expression_and", "case_insensitive")
            class RepeatedExpression(_message.Message):
                __slots__ = ("expression_vec",)
                EXPRESSION_VEC_FIELD_NUMBER: _ClassVar[int]
                expression_vec: _containers.RepeatedCompositeFieldContainer[Filter.FileFilter.Expression]
                def __init__(self, expression_vec: _Optional[_Iterable[_Union[Filter.FileFilter.Expression, _Mapping]]] = ...) -> None: ...
            OWNER_FIELD_NUMBER: _ClassVar[int]
            MODTIME_SECS_FLOOR_FIELD_NUMBER: _ClassVar[int]
            MODTIME_SECS_CEILING_FIELD_NUMBER: _ClassVar[int]
            FILENAME_REGEX_FIELD_NUMBER: _ClassVar[int]
            PATH_PREFIX_REGEX_FIELD_NUMBER: _ClassVar[int]
            DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            FILE_DATA_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
            REPEATED_EXPRESSION_OR_FIELD_NUMBER: _ClassVar[int]
            REPEATED_EXPRESSION_AND_FIELD_NUMBER: _ClassVar[int]
            CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
            owner: str
            modtime_secs_floor: int
            modtime_secs_ceiling: int
            filename_regex: str
            path_prefix_regex: str
            document_type: _base_pb2.DocumentType.Type
            file_data_sensitivity: Filter.DataSensitivity
            repeated_expression_or: Filter.FileFilter.Expression.RepeatedExpression
            repeated_expression_and: Filter.FileFilter.Expression.RepeatedExpression
            case_insensitive: bool
            def __init__(self, owner: _Optional[str] = ..., modtime_secs_floor: _Optional[int] = ..., modtime_secs_ceiling: _Optional[int] = ..., filename_regex: _Optional[str] = ..., path_prefix_regex: _Optional[str] = ..., document_type: _Optional[_Union[_base_pb2.DocumentType.Type, str]] = ..., file_data_sensitivity: _Optional[_Union[Filter.DataSensitivity, str]] = ..., repeated_expression_or: _Optional[_Union[Filter.FileFilter.Expression.RepeatedExpression, _Mapping]] = ..., repeated_expression_and: _Optional[_Union[Filter.FileFilter.Expression.RepeatedExpression, _Mapping]] = ..., case_insensitive: bool = ...) -> None: ...
        DATA_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        data_sensitivity: _containers.RepeatedScalarFieldContainer[Filter.DataSensitivity]
        expression: Filter.FileFilter.Expression
        def __init__(self, data_sensitivity: _Optional[_Iterable[_Union[Filter.DataSensitivity, str]]] = ..., expression: _Optional[_Union[Filter.FileFilter.Expression, _Mapping]] = ...) -> None: ...
    MAILBOX_ACCEPT_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_REJECT_FILTER_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_ACCEPT_FILTER_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_REJECT_FILTER_FIELD_NUMBER: _ClassVar[int]
    VM_ACCEPT_FILTER_FIELD_NUMBER: _ClassVar[int]
    VM_REJECT_FILTER_FIELD_NUMBER: _ClassVar[int]
    COHESITY_VIEW_ACCEPT_FILTER_FIELD_NUMBER: _ClassVar[int]
    COHESITY_VIEW_REJECT_FILTER_FIELD_NUMBER: _ClassVar[int]
    mailbox_accept_filter: Filter.MailboxFilter
    mailbox_reject_filter: Filter.MailboxFilter
    onedrive_accept_filter: Filter.FileFilter
    onedrive_reject_filter: Filter.FileFilter
    vm_accept_filter: Filter.FileFilter
    vm_reject_filter: Filter.FileFilter
    cohesity_view_accept_filter: Filter.FileFilter
    cohesity_view_reject_filter: Filter.FileFilter
    def __init__(self, mailbox_accept_filter: _Optional[_Union[Filter.MailboxFilter, _Mapping]] = ..., mailbox_reject_filter: _Optional[_Union[Filter.MailboxFilter, _Mapping]] = ..., onedrive_accept_filter: _Optional[_Union[Filter.FileFilter, _Mapping]] = ..., onedrive_reject_filter: _Optional[_Union[Filter.FileFilter, _Mapping]] = ..., vm_accept_filter: _Optional[_Union[Filter.FileFilter, _Mapping]] = ..., vm_reject_filter: _Optional[_Union[Filter.FileFilter, _Mapping]] = ..., cohesity_view_accept_filter: _Optional[_Union[Filter.FileFilter, _Mapping]] = ..., cohesity_view_reject_filter: _Optional[_Union[Filter.FileFilter, _Mapping]] = ...) -> None: ...

class GetObjectsArg(_message.Message):
    __slots__ = ("object_types", "filter", "need_all_snapshots_info", "cookie", "forwarding_disallowed", "account_id", "tenant_id")
    OBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    NEED_ALL_SNAPSHOTS_INFO_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    object_types: _containers.RepeatedScalarFieldContainer[_base_pb2.Object.ObjectType]
    filter: Filter
    need_all_snapshots_info: bool
    cookie: bytes
    forwarding_disallowed: bool
    account_id: bytes
    tenant_id: bytes
    def __init__(self, object_types: _Optional[_Iterable[_Union[_base_pb2.Object.ObjectType, str]]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., need_all_snapshots_info: bool = ..., cookie: _Optional[bytes] = ..., forwarding_disallowed: bool = ..., account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ...) -> None: ...

class GetObjectsResult(_message.Message):
    __slots__ = ("next_cookie", "objects")
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    next_cookie: bytes
    objects: _containers.RepeatedCompositeFieldContainer[_base_pb2.Object]
    def __init__(self, next_cookie: _Optional[bytes] = ..., objects: _Optional[_Iterable[_Union[_base_pb2.Object, _Mapping]]] = ...) -> None: ...

class GetSubObjectsArg(_message.Message):
    __slots__ = ("account_id", "tenant_id", "object_id", "type", "snapshot_handle", "filter", "forwarding_disallowed")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    object_id: bytes
    type: _base_pb2.Object.ObjectType
    snapshot_handle: _base_pb2.SnapshotHandle
    filter: Filter
    forwarding_disallowed: bool
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., object_id: _Optional[bytes] = ..., type: _Optional[_Union[_base_pb2.Object.ObjectType, str]] = ..., snapshot_handle: _Optional[_Union[_base_pb2.SnapshotHandle, _Mapping]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., forwarding_disallowed: bool = ...) -> None: ...

class GetSubObjectsResult(_message.Message):
    __slots__ = ("sub_objects",)
    SUB_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    sub_objects: _containers.RepeatedCompositeFieldContainer[_base_pb2.SubObjectHandle]
    def __init__(self, sub_objects: _Optional[_Iterable[_Union[_base_pb2.SubObjectHandle, _Mapping]]] = ...) -> None: ...

class ListDocumentsArg(_message.Message):
    __slots__ = ("account_id", "tenant_id", "object_id", "type", "snapshot_handle", "base_snapshot_handle", "sub_object_handle", "filter", "cookie", "forwarding_disallowed", "max_document_size", "content_disallowed")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SUB_OBJECT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    MAX_DOCUMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    object_id: bytes
    type: _base_pb2.Object.ObjectType
    snapshot_handle: _base_pb2.SnapshotHandle
    base_snapshot_handle: _base_pb2.SnapshotHandle
    sub_object_handle: _base_pb2.SubObjectHandle
    filter: Filter
    cookie: bytes
    forwarding_disallowed: bool
    max_document_size: int
    content_disallowed: bool
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., object_id: _Optional[bytes] = ..., type: _Optional[_Union[_base_pb2.Object.ObjectType, str]] = ..., snapshot_handle: _Optional[_Union[_base_pb2.SnapshotHandle, _Mapping]] = ..., base_snapshot_handle: _Optional[_Union[_base_pb2.SnapshotHandle, _Mapping]] = ..., sub_object_handle: _Optional[_Union[_base_pb2.SubObjectHandle, _Mapping]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., cookie: _Optional[bytes] = ..., forwarding_disallowed: bool = ..., max_document_size: _Optional[int] = ..., content_disallowed: bool = ...) -> None: ...

class DocumentDataRange(_message.Message):
    __slots__ = ("offset", "contents", "contents_size")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    contents: bytes
    contents_size: int
    def __init__(self, offset: _Optional[int] = ..., contents: _Optional[bytes] = ..., contents_size: _Optional[int] = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ("id", "document_type", "range_vec", "total_original_length")
    ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ORIGINAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    document_type: _base_pb2.DocumentType
    range_vec: _containers.RepeatedCompositeFieldContainer[DocumentDataRange]
    total_original_length: int
    def __init__(self, id: _Optional[bytes] = ..., document_type: _Optional[_Union[_base_pb2.DocumentType, _Mapping]] = ..., range_vec: _Optional[_Iterable[_Union[DocumentDataRange, _Mapping]]] = ..., total_original_length: _Optional[int] = ...) -> None: ...

class ListDocumentsResult(_message.Message):
    __slots__ = ("next_cookie", "documents")
    NEXT_COOKIE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    next_cookie: bytes
    documents: _containers.RepeatedCompositeFieldContainer[Document]
    def __init__(self, next_cookie: _Optional[bytes] = ..., documents: _Optional[_Iterable[_Union[Document, _Mapping]]] = ...) -> None: ...

class GetDocumentsArg(_message.Message):
    __slots__ = ("account_id", "tenant_id", "object_id", "type", "snapshot_handle", "sub_object_handle", "document_spec_vec", "forwarding_disallowed", "filter", "document_metadata_required")
    class DocumentSpec(_message.Message):
        __slots__ = ("doc_id", "offset_vec", "length_vec")
        DOC_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
        LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
        doc_id: bytes
        offset_vec: _containers.RepeatedScalarFieldContainer[int]
        length_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, doc_id: _Optional[bytes] = ..., offset_vec: _Optional[_Iterable[int]] = ..., length_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SUB_OBJECT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_METADATA_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    object_id: bytes
    type: _base_pb2.Object.ObjectType
    snapshot_handle: _base_pb2.SnapshotHandle
    sub_object_handle: _base_pb2.SubObjectHandle
    document_spec_vec: _containers.RepeatedCompositeFieldContainer[GetDocumentsArg.DocumentSpec]
    forwarding_disallowed: bool
    filter: Filter
    document_metadata_required: bool
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., object_id: _Optional[bytes] = ..., type: _Optional[_Union[_base_pb2.Object.ObjectType, str]] = ..., snapshot_handle: _Optional[_Union[_base_pb2.SnapshotHandle, _Mapping]] = ..., sub_object_handle: _Optional[_Union[_base_pb2.SubObjectHandle, _Mapping]] = ..., document_spec_vec: _Optional[_Iterable[_Union[GetDocumentsArg.DocumentSpec, _Mapping]]] = ..., forwarding_disallowed: bool = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., document_metadata_required: bool = ...) -> None: ...

class GetDocumentsResult(_message.Message):
    __slots__ = ("document_result_vec",)
    class DocumentResult(_message.Message):
        __slots__ = ("document", "error_proto")
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
        document: Document
        error_proto: _error_pb2.ErrorProto
        def __init__(self, document: _Optional[_Union[Document, _Mapping]] = ..., error_proto: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    DOCUMENT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    document_result_vec: _containers.RepeatedCompositeFieldContainer[GetDocumentsResult.DocumentResult]
    def __init__(self, document_result_vec: _Optional[_Iterable[_Union[GetDocumentsResult.DocumentResult, _Mapping]]] = ...) -> None: ...

class GetConvertedDocumentsArg(_message.Message):
    __slots__ = ("account_id", "tenant_id", "emblem_service_info", "document_spec_vec", "max_unconverted_document_size")
    class DocumentSpec(_message.Message):
        __slots__ = ("document_locator", "offset_vec", "length_vec")
        DOCUMENT_LOCATOR_FIELD_NUMBER: _ClassVar[int]
        OFFSET_VEC_FIELD_NUMBER: _ClassVar[int]
        LENGTH_VEC_FIELD_NUMBER: _ClassVar[int]
        document_locator: bytes
        offset_vec: _containers.RepeatedScalarFieldContainer[int]
        length_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, document_locator: _Optional[bytes] = ..., offset_vec: _Optional[_Iterable[int]] = ..., length_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SPEC_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_UNCONVERTED_DOCUMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    emblem_service_info: bytes
    document_spec_vec: _containers.RepeatedCompositeFieldContainer[GetConvertedDocumentsArg.DocumentSpec]
    max_unconverted_document_size: int
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., emblem_service_info: _Optional[bytes] = ..., document_spec_vec: _Optional[_Iterable[_Union[GetConvertedDocumentsArg.DocumentSpec, _Mapping]]] = ..., max_unconverted_document_size: _Optional[int] = ...) -> None: ...

class GetConvertedDocumentsResult(_message.Message):
    __slots__ = ("document_result_vec",)
    class DocumentResult(_message.Message):
        __slots__ = ("range_vec", "error_proto")
        RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
        range_vec: _containers.RepeatedCompositeFieldContainer[DocumentDataRange]
        error_proto: _error_pb2.ErrorProto
        def __init__(self, range_vec: _Optional[_Iterable[_Union[DocumentDataRange, _Mapping]]] = ..., error_proto: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    DOCUMENT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    document_result_vec: _containers.RepeatedCompositeFieldContainer[GetConvertedDocumentsResult.DocumentResult]
    def __init__(self, document_result_vec: _Optional[_Iterable[_Union[GetConvertedDocumentsResult.DocumentResult, _Mapping]]] = ...) -> None: ...

class UpdateCleanupStateArg(_message.Message):
    __slots__ = ("session_id", "logical_timestamp", "cleanup_state")
    class CleanupState(_message.Message):
        __slots__ = ("cloned_view_vec",)
        CLONED_VIEW_VEC_FIELD_NUMBER: _ClassVar[int]
        cloned_view_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, cloned_view_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_STATE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    logical_timestamp: int
    cleanup_state: UpdateCleanupStateArg.CleanupState
    def __init__(self, session_id: _Optional[int] = ..., logical_timestamp: _Optional[int] = ..., cleanup_state: _Optional[_Union[UpdateCleanupStateArg.CleanupState, _Mapping]] = ...) -> None: ...

class UpdateCleanupStateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexingStats(_message.Message):
    __slots__ = ("num_objects", "num_snapshots", "num_finished_objects", "num_finished_snapshots", "num_finished_sub_objects", "num_finished_docs", "num_converted_docs", "num_errors_seen", "num_indexed_docs", "num_indexed_chunks", "num_total_chunks", "num_indexed_bytes", "num_vectorized_bytes", "outofspace_error")
    NUM_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FINISHED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FINISHED_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FINISHED_SUB_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FINISHED_DOCS_FIELD_NUMBER: _ClassVar[int]
    NUM_CONVERTED_DOCS_FIELD_NUMBER: _ClassVar[int]
    NUM_ERRORS_SEEN_FIELD_NUMBER: _ClassVar[int]
    NUM_INDEXED_DOCS_FIELD_NUMBER: _ClassVar[int]
    NUM_INDEXED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    NUM_INDEXED_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_VECTORIZED_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTOFSPACE_ERROR_FIELD_NUMBER: _ClassVar[int]
    num_objects: int
    num_snapshots: int
    num_finished_objects: int
    num_finished_snapshots: int
    num_finished_sub_objects: int
    num_finished_docs: int
    num_converted_docs: int
    num_errors_seen: int
    num_indexed_docs: int
    num_indexed_chunks: int
    num_total_chunks: int
    num_indexed_bytes: int
    num_vectorized_bytes: int
    outofspace_error: bool
    def __init__(self, num_objects: _Optional[int] = ..., num_snapshots: _Optional[int] = ..., num_finished_objects: _Optional[int] = ..., num_finished_snapshots: _Optional[int] = ..., num_finished_sub_objects: _Optional[int] = ..., num_finished_docs: _Optional[int] = ..., num_converted_docs: _Optional[int] = ..., num_errors_seen: _Optional[int] = ..., num_indexed_docs: _Optional[int] = ..., num_indexed_chunks: _Optional[int] = ..., num_total_chunks: _Optional[int] = ..., num_indexed_bytes: _Optional[int] = ..., num_vectorized_bytes: _Optional[int] = ..., outofspace_error: bool = ...) -> None: ...

class IndexDocumentsArg(_message.Message):
    __slots__ = ("account_id", "tenant_id", "objects", "filter", "emblem_service_info", "collection_id", "forwarding_disallowed", "job_handle", "slave_data", "max_indexed_document_size")
    class SlaveData(_message.Message):
        __slots__ = ("task_handle", "expected_session_id", "indexing_cookie", "stats")
        TASK_HANDLE_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        INDEXING_COOKIE_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        task_handle: int
        expected_session_id: int
        indexing_cookie: bytes
        stats: IndexingStats
        def __init__(self, task_handle: _Optional[int] = ..., expected_session_id: _Optional[int] = ..., indexing_cookie: _Optional[bytes] = ..., stats: _Optional[_Union[IndexingStats, _Mapping]] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    EMBLEM_SERVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    JOB_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SLAVE_DATA_FIELD_NUMBER: _ClassVar[int]
    MAX_INDEXED_DOCUMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    account_id: bytes
    tenant_id: bytes
    objects: _containers.RepeatedCompositeFieldContainer[_base_pb2.Object]
    filter: Filter
    emblem_service_info: bytes
    collection_id: bytes
    forwarding_disallowed: bool
    job_handle: bytes
    slave_data: IndexDocumentsArg.SlaveData
    max_indexed_document_size: int
    def __init__(self, account_id: _Optional[bytes] = ..., tenant_id: _Optional[bytes] = ..., objects: _Optional[_Iterable[_Union[_base_pb2.Object, _Mapping]]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., emblem_service_info: _Optional[bytes] = ..., collection_id: _Optional[bytes] = ..., forwarding_disallowed: bool = ..., job_handle: _Optional[bytes] = ..., slave_data: _Optional[_Union[IndexDocumentsArg.SlaveData, _Mapping]] = ..., max_indexed_document_size: _Optional[int] = ...) -> None: ...

class IndexDocumentsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIndexingStatusArg(_message.Message):
    __slots__ = ("job_handle", "forwarding_disallowed")
    JOB_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    job_handle: bytes
    forwarding_disallowed: bool
    def __init__(self, job_handle: _Optional[bytes] = ..., forwarding_disallowed: bool = ...) -> None: ...

class GetIndexingStatusResult(_message.Message):
    __slots__ = ("finished", "cancellation_scheduled", "stats", "start_time_usecs", "finish_time_usecs")
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    finished: bool
    cancellation_scheduled: bool
    stats: IndexingStats
    start_time_usecs: int
    finish_time_usecs: int
    def __init__(self, finished: bool = ..., cancellation_scheduled: bool = ..., stats: _Optional[_Union[IndexingStats, _Mapping]] = ..., start_time_usecs: _Optional[int] = ..., finish_time_usecs: _Optional[int] = ...) -> None: ...

class ReportIndexingStatusArg(_message.Message):
    __slots__ = ("slave_session_id", "logical_timestamp", "forwarding_disallowed", "task_status_vec")
    class TaskStatus(_message.Message):
        __slots__ = ("job_handle", "task_handle", "finished", "canceled", "indexing_cookie", "stats")
        JOB_HANDLE_FIELD_NUMBER: _ClassVar[int]
        TASK_HANDLE_FIELD_NUMBER: _ClassVar[int]
        FINISHED_FIELD_NUMBER: _ClassVar[int]
        CANCELED_FIELD_NUMBER: _ClassVar[int]
        INDEXING_COOKIE_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        job_handle: bytes
        task_handle: int
        finished: bool
        canceled: bool
        indexing_cookie: bytes
        stats: IndexingStats
        def __init__(self, job_handle: _Optional[bytes] = ..., task_handle: _Optional[int] = ..., finished: bool = ..., canceled: bool = ..., indexing_cookie: _Optional[bytes] = ..., stats: _Optional[_Union[IndexingStats, _Mapping]] = ...) -> None: ...
    SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    slave_session_id: int
    logical_timestamp: int
    forwarding_disallowed: bool
    task_status_vec: _containers.RepeatedCompositeFieldContainer[ReportIndexingStatusArg.TaskStatus]
    def __init__(self, slave_session_id: _Optional[int] = ..., logical_timestamp: _Optional[int] = ..., forwarding_disallowed: bool = ..., task_status_vec: _Optional[_Iterable[_Union[ReportIndexingStatusArg.TaskStatus, _Mapping]]] = ...) -> None: ...

class ReportIndexingStatusResult(_message.Message):
    __slots__ = ("error_proto_vec",)
    ERROR_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    error_proto_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    def __init__(self, error_proto_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...

class CancelIndexingArg(_message.Message):
    __slots__ = ("job_handle", "task_handle", "forwarding_disallowed")
    JOB_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TASK_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_DISALLOWED_FIELD_NUMBER: _ClassVar[int]
    job_handle: bytes
    task_handle: int
    forwarding_disallowed: bool
    def __init__(self, job_handle: _Optional[bytes] = ..., task_handle: _Optional[int] = ..., forwarding_disallowed: bool = ...) -> None: ...

class CancelIndexingResult(_message.Message):
    __slots__ = ("canceled",)
    CANCELED_FIELD_NUMBER: _ClassVar[int]
    canceled: bool
    def __init__(self, canceled: bool = ...) -> None: ...
