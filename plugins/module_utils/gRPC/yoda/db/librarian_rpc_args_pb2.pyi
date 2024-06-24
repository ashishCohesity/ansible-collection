from yoda.base import yoda_pb2 as _yoda_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from yoda.master.stub import yoda_rpc_args_pb2 as _yoda_rpc_args_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteVersionsArg(_message.Message):
    __slots__ = ("instance_id_vec", "all_instance_ids", "range_usage")
    INSTANCE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ALL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    RANGE_USAGE_FIELD_NUMBER: _ClassVar[int]
    instance_id_vec: _containers.RepeatedCompositeFieldContainer[_yoda_types_pb2.MagnetoInstanceId]
    all_instance_ids: _containers.RepeatedScalarFieldContainer[int]
    range_usage: _yoda_pb2.RangeUsage.Type
    def __init__(self, instance_id_vec: _Optional[_Iterable[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]]] = ..., all_instance_ids: _Optional[_Iterable[int]] = ..., range_usage: _Optional[_Union[_yoda_pb2.RangeUsage.Type, str]] = ...) -> None: ...

class ReplicateVersionsArg(_message.Message):
    __slots__ = ("from_instance_id", "to_instance_id", "all_instance_ids", "range_usage")
    FROM_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TO_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    RANGE_USAGE_FIELD_NUMBER: _ClassVar[int]
    from_instance_id: _yoda_types_pb2.MagnetoInstanceId
    to_instance_id: _yoda_types_pb2.MagnetoInstanceId
    all_instance_ids: _containers.RepeatedScalarFieldContainer[int]
    range_usage: _yoda_pb2.RangeUsage.Type
    def __init__(self, from_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., to_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., all_instance_ids: _Optional[_Iterable[int]] = ..., range_usage: _Optional[_Union[_yoda_pb2.RangeUsage.Type, str]] = ...) -> None: ...

class ApplyDeltaIndexArg(_message.Message):
    __slots__ = ("cfile_index_handle", "cfile_doc_batch_metadata", "cfile_doc_vec")
    CFILE_INDEX_HANDLE_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_BATCH_METADATA_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_VEC_FIELD_NUMBER: _ClassVar[int]
    cfile_index_handle: _yoda_rpc_args_pb2.PutCrackedFileIndexHandle
    cfile_doc_batch_metadata: _yoda_rpc_args_pb2.CrackedFileArchiveDocBatchMetadata
    cfile_doc_vec: _containers.RepeatedCompositeFieldContainer[_yoda_rpc_args_pb2.CrackedFileArchiveDoc]
    def __init__(self, cfile_index_handle: _Optional[_Union[_yoda_rpc_args_pb2.PutCrackedFileIndexHandle, _Mapping]] = ..., cfile_doc_batch_metadata: _Optional[_Union[_yoda_rpc_args_pb2.CrackedFileArchiveDocBatchMetadata, _Mapping]] = ..., cfile_doc_vec: _Optional[_Iterable[_Union[_yoda_rpc_args_pb2.CrackedFileArchiveDoc, _Mapping]]] = ...) -> None: ...

class CrackedFileDocumentMergeArg(_message.Message):
    __slots__ = ("all_instance_ids", "range_usage", "instance_id_to_be_removed", "base_job_instance_id", "tags_to_be_added_vec", "tags_to_be_removed_vec", "job_instance_ids_to_tag_vec", "delete_older_versions")
    ALL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    RANGE_USAGE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_TO_BE_REMOVED_FIELD_NUMBER: _ClassVar[int]
    BASE_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_TO_BE_ADDED_VEC_FIELD_NUMBER: _ClassVar[int]
    TAGS_TO_BE_REMOVED_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_IDS_TO_TAG_VEC_FIELD_NUMBER: _ClassVar[int]
    DELETE_OLDER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    all_instance_ids: _containers.RepeatedScalarFieldContainer[int]
    range_usage: _yoda_pb2.RangeUsage.Type
    instance_id_to_be_removed: int
    base_job_instance_id: int
    tags_to_be_added_vec: _containers.RepeatedScalarFieldContainer[str]
    tags_to_be_removed_vec: _containers.RepeatedScalarFieldContainer[str]
    job_instance_ids_to_tag_vec: _containers.RepeatedScalarFieldContainer[int]
    delete_older_versions: bool
    def __init__(self, all_instance_ids: _Optional[_Iterable[int]] = ..., range_usage: _Optional[_Union[_yoda_pb2.RangeUsage.Type, str]] = ..., instance_id_to_be_removed: _Optional[int] = ..., base_job_instance_id: _Optional[int] = ..., tags_to_be_added_vec: _Optional[_Iterable[str]] = ..., tags_to_be_removed_vec: _Optional[_Iterable[str]] = ..., job_instance_ids_to_tag_vec: _Optional[_Iterable[int]] = ..., delete_older_versions: bool = ...) -> None: ...

class UpdateFolderNameArg(_message.Message):
    __slots__ = ("new_folder_name",)
    NEW_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    new_folder_name: str
    def __init__(self, new_folder_name: _Optional[str] = ...) -> None: ...

class GCTagsArg(_message.Message):
    __slots__ = ("tags_to_gc_vec",)
    TAGS_TO_GC_VEC_FIELD_NUMBER: _ClassVar[int]
    tags_to_gc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags_to_gc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetImmediateChildrenBucketArg(_message.Message):
    __slots__ = ("document",)
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: str
    def __init__(self, document: _Optional[str] = ...) -> None: ...
