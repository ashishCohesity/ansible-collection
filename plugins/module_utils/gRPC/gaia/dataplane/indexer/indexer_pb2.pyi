from gaia.dataplane.api import api_pb2 as _api_pb2
from gaia.dataplane.api import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MasterWALRecordProto(_message.Message):
    __slots__ = ("update_job_vec", "update_object_state_vec")
    class UpdateJob(_message.Message):
        __slots__ = ("arg", "job_handle", "remove_job", "indexing_started_approx_usecs", "indexing_finished_approx_usecs", "cancellation_scheduled")
        ARG_FIELD_NUMBER: _ClassVar[int]
        JOB_HANDLE_FIELD_NUMBER: _ClassVar[int]
        REMOVE_JOB_FIELD_NUMBER: _ClassVar[int]
        INDEXING_STARTED_APPROX_USECS_FIELD_NUMBER: _ClassVar[int]
        INDEXING_FINISHED_APPROX_USECS_FIELD_NUMBER: _ClassVar[int]
        CANCELLATION_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
        arg: _api_pb2.IndexDocumentsArg
        job_handle: bytes
        remove_job: bool
        indexing_started_approx_usecs: int
        indexing_finished_approx_usecs: int
        cancellation_scheduled: bool
        def __init__(self, arg: _Optional[_Union[_api_pb2.IndexDocumentsArg, _Mapping]] = ..., job_handle: _Optional[bytes] = ..., remove_job: bool = ..., indexing_started_approx_usecs: _Optional[int] = ..., indexing_finished_approx_usecs: _Optional[int] = ..., cancellation_scheduled: bool = ...) -> None: ...
    class UpdateObjectState(_message.Message):
        __slots__ = ("job_handle", "object_index", "stats", "indexing_cookie", "slave_logical_timestamp", "indexing_finished", "slave_session_id", "slave_constituent_id", "task_handle", "last_status_report_approx_usecs")
        JOB_HANDLE_FIELD_NUMBER: _ClassVar[int]
        OBJECT_INDEX_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        INDEXING_COOKIE_FIELD_NUMBER: _ClassVar[int]
        SLAVE_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        INDEXING_FINISHED_FIELD_NUMBER: _ClassVar[int]
        SLAVE_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        SLAVE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
        TASK_HANDLE_FIELD_NUMBER: _ClassVar[int]
        LAST_STATUS_REPORT_APPROX_USECS_FIELD_NUMBER: _ClassVar[int]
        job_handle: bytes
        object_index: int
        stats: _api_pb2.IndexingStats
        indexing_cookie: bytes
        slave_logical_timestamp: int
        indexing_finished: bool
        slave_session_id: int
        slave_constituent_id: int
        task_handle: int
        last_status_report_approx_usecs: int
        def __init__(self, job_handle: _Optional[bytes] = ..., object_index: _Optional[int] = ..., stats: _Optional[_Union[_api_pb2.IndexingStats, _Mapping]] = ..., indexing_cookie: _Optional[bytes] = ..., slave_logical_timestamp: _Optional[int] = ..., indexing_finished: bool = ..., slave_session_id: _Optional[int] = ..., slave_constituent_id: _Optional[int] = ..., task_handle: _Optional[int] = ..., last_status_report_approx_usecs: _Optional[int] = ...) -> None: ...
    UPDATE_JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_OBJECT_STATE_VEC_FIELD_NUMBER: _ClassVar[int]
    update_job_vec: _containers.RepeatedCompositeFieldContainer[MasterWALRecordProto.UpdateJob]
    update_object_state_vec: _containers.RepeatedCompositeFieldContainer[MasterWALRecordProto.UpdateObjectState]
    def __init__(self, update_job_vec: _Optional[_Iterable[_Union[MasterWALRecordProto.UpdateJob, _Mapping]]] = ..., update_object_state_vec: _Optional[_Iterable[_Union[MasterWALRecordProto.UpdateObjectState, _Mapping]]] = ...) -> None: ...

class IndexingCookieProto(_message.Message):
    __slots__ = ("next_snapshot_index", "base_snapshot_handle", "next_snapshot_errors_seen", "remaining_subobject_vec", "doc_index_map", "next_list_documents_cookie", "next_document_index")
    class DocumentPersistentInfo(_message.Message):
        __slots__ = ("docid", "total_original_length", "document_type", "next_offset_to_upload", "upload_handle", "num_errors_seen", "needed_conversion")
        DOCID_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ORIGINAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        NEXT_OFFSET_TO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_HANDLE_FIELD_NUMBER: _ClassVar[int]
        NUM_ERRORS_SEEN_FIELD_NUMBER: _ClassVar[int]
        NEEDED_CONVERSION_FIELD_NUMBER: _ClassVar[int]
        docid: bytes
        total_original_length: int
        document_type: _base_pb2.DocumentType
        next_offset_to_upload: int
        upload_handle: bytes
        num_errors_seen: int
        needed_conversion: bool
        def __init__(self, docid: _Optional[bytes] = ..., total_original_length: _Optional[int] = ..., document_type: _Optional[_Union[_base_pb2.DocumentType, _Mapping]] = ..., next_offset_to_upload: _Optional[int] = ..., upload_handle: _Optional[bytes] = ..., num_errors_seen: _Optional[int] = ..., needed_conversion: bool = ...) -> None: ...
    class DocIndexMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: IndexingCookieProto.DocumentPersistentInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[IndexingCookieProto.DocumentPersistentInfo, _Mapping]] = ...) -> None: ...
    NEXT_SNAPSHOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    BASE_SNAPSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    NEXT_SNAPSHOT_ERRORS_SEEN_FIELD_NUMBER: _ClassVar[int]
    REMAINING_SUBOBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    DOC_INDEX_MAP_FIELD_NUMBER: _ClassVar[int]
    NEXT_LIST_DOCUMENTS_COOKIE_FIELD_NUMBER: _ClassVar[int]
    NEXT_DOCUMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    next_snapshot_index: int
    base_snapshot_handle: _base_pb2.SnapshotHandle
    next_snapshot_errors_seen: bool
    remaining_subobject_vec: _containers.RepeatedCompositeFieldContainer[_base_pb2.SubObjectHandle]
    doc_index_map: _containers.MessageMap[int, IndexingCookieProto.DocumentPersistentInfo]
    next_list_documents_cookie: bytes
    next_document_index: int
    def __init__(self, next_snapshot_index: _Optional[int] = ..., base_snapshot_handle: _Optional[_Union[_base_pb2.SnapshotHandle, _Mapping]] = ..., next_snapshot_errors_seen: bool = ..., remaining_subobject_vec: _Optional[_Iterable[_Union[_base_pb2.SubObjectHandle, _Mapping]]] = ..., doc_index_map: _Optional[_Mapping[int, IndexingCookieProto.DocumentPersistentInfo]] = ..., next_list_documents_cookie: _Optional[bytes] = ..., next_document_index: _Optional[int] = ...) -> None: ...
