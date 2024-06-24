from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from yoda.base import error_pb2 as _error_pb2
from yoda.base import yoda_pb2 as _yoda_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from yoda.db import documents_pb2 as _documents_pb2
from yoda.util import work_item_pb2 as _work_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CrackedFileArchiveDoc(_message.Message):
    __slots__ = ("cfile_op", "cfile_doc", "doc_range", "extended_metadata_attributes")
    class CFileOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdd: _ClassVar[CrackedFileArchiveDoc.CFileOp]
        kDelete: _ClassVar[CrackedFileArchiveDoc.CFileOp]
        kCopy: _ClassVar[CrackedFileArchiveDoc.CFileOp]
    kAdd: CrackedFileArchiveDoc.CFileOp
    kDelete: CrackedFileArchiveDoc.CFileOp
    kCopy: CrackedFileArchiveDoc.CFileOp
    class DocumentRange(_message.Message):
        __slots__ = ("lower_bound", "upper_bound")
        LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
        lower_bound: bytes
        upper_bound: bytes
        def __init__(self, lower_bound: _Optional[bytes] = ..., upper_bound: _Optional[bytes] = ...) -> None: ...
    class ExtendedMetadataAttributes(_message.Message):
        __slots__ = ("base_instance_size_bytes", "current_instance_size_bytes", "base_instance_mtime_usecs", "current_instance_mtime_usecs", "is_tag_diff")
        BASE_INSTANCE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        CURRENT_INSTANCE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        BASE_INSTANCE_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_INSTANCE_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
        IS_TAG_DIFF_FIELD_NUMBER: _ClassVar[int]
        base_instance_size_bytes: int
        current_instance_size_bytes: int
        base_instance_mtime_usecs: int
        current_instance_mtime_usecs: int
        is_tag_diff: bool
        def __init__(self, base_instance_size_bytes: _Optional[int] = ..., current_instance_size_bytes: _Optional[int] = ..., base_instance_mtime_usecs: _Optional[int] = ..., current_instance_mtime_usecs: _Optional[int] = ..., is_tag_diff: bool = ...) -> None: ...
    CFILE_OP_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_FIELD_NUMBER: _ClassVar[int]
    DOC_RANGE_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_METADATA_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    cfile_op: CrackedFileArchiveDoc.CFileOp
    cfile_doc: _documents_pb2.CrackedFileDocument
    doc_range: CrackedFileArchiveDoc.DocumentRange
    extended_metadata_attributes: CrackedFileArchiveDoc.ExtendedMetadataAttributes
    def __init__(self, cfile_op: _Optional[_Union[CrackedFileArchiveDoc.CFileOp, str]] = ..., cfile_doc: _Optional[_Union[_documents_pb2.CrackedFileDocument, _Mapping]] = ..., doc_range: _Optional[_Union[CrackedFileArchiveDoc.DocumentRange, _Mapping]] = ..., extended_metadata_attributes: _Optional[_Union[CrackedFileArchiveDoc.ExtendedMetadataAttributes, _Mapping]] = ...) -> None: ...

class CrackedFileIndexMetadata(_message.Message):
    __slots__ = ("version_id", "num_buckets", "sharding_function")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    SHARDING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    version_id: int
    num_buckets: int
    sharding_function: str
    def __init__(self, version_id: _Optional[int] = ..., num_buckets: _Optional[int] = ..., sharding_function: _Optional[str] = ...) -> None: ...

class CrackedFileArchiveDocBatchMetadata(_message.Message):
    __slots__ = ("bucket_id",)
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    def __init__(self, bucket_id: _Optional[int] = ...) -> None: ...

class CrackedFileExtendedMetadataParams(_message.Message):
    __slots__ = ("populate_size", "populate_mtime")
    POPULATE_SIZE_FIELD_NUMBER: _ClassVar[int]
    POPULATE_MTIME_FIELD_NUMBER: _ClassVar[int]
    populate_size: bool
    populate_mtime: bool
    def __init__(self, populate_size: bool = ..., populate_mtime: bool = ...) -> None: ...

class CrackedFileIndexHandle(_message.Message):
    __slots__ = ("db_dir_path", "object_id", "instance_id", "base_instance_id", "cluster_partition_id", "all_instance_ids", "use_tags_for_diff", "extended_metadata_params")
    DB_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_INSTANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    USE_TAGS_FOR_DIFF_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_METADATA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    db_dir_path: str
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    cluster_partition_id: int
    all_instance_ids: _containers.RepeatedScalarFieldContainer[int]
    use_tags_for_diff: bool
    extended_metadata_params: CrackedFileExtendedMetadataParams
    def __init__(self, db_dir_path: _Optional[str] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., all_instance_ids: _Optional[_Iterable[int]] = ..., use_tags_for_diff: bool = ..., extended_metadata_params: _Optional[_Union[CrackedFileExtendedMetadataParams, _Mapping]] = ...) -> None: ...

class PrepareCrackedFileIndexArg(_message.Message):
    __slots__ = ("task_id", "object_id", "instance_id", "base_instance_id", "cluster_partition_id", "use_tags_for_diff", "extended_metadata_params")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    USE_TAGS_FOR_DIFF_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_METADATA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    cluster_partition_id: int
    use_tags_for_diff: bool
    extended_metadata_params: CrackedFileExtendedMetadataParams
    def __init__(self, task_id: _Optional[int] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., use_tags_for_diff: bool = ..., extended_metadata_params: _Optional[_Union[CrackedFileExtendedMetadataParams, _Mapping]] = ...) -> None: ...

class PrepareCrackedFileIndexResult(_message.Message):
    __slots__ = ("error", "cfile_handle", "object_doc", "aux_db", "cfile_index_metadata")
    class AuxDbEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DOC_FIELD_NUMBER: _ClassVar[int]
    AUX_DB_FIELD_NUMBER: _ClassVar[int]
    CFILE_INDEX_METADATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cfile_handle: CrackedFileIndexHandle
    object_doc: _documents_pb2.ObjectSnapshotDocument
    aux_db: _containers.ScalarMap[str, bytes]
    cfile_index_metadata: CrackedFileIndexMetadata
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cfile_handle: _Optional[_Union[CrackedFileIndexHandle, _Mapping]] = ..., object_doc: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument, _Mapping]] = ..., aux_db: _Optional[_Mapping[str, bytes]] = ..., cfile_index_metadata: _Optional[_Union[CrackedFileIndexMetadata, _Mapping]] = ...) -> None: ...

class GetCrackedFileIndexArg(_message.Message):
    __slots__ = ("cfile_handle", "cookie_val")
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_VAL_FIELD_NUMBER: _ClassVar[int]
    cfile_handle: CrackedFileIndexHandle
    cookie_val: bytes
    def __init__(self, cfile_handle: _Optional[_Union[CrackedFileIndexHandle, _Mapping]] = ..., cookie_val: _Optional[bytes] = ...) -> None: ...

class GetCrackedFileIndexResult(_message.Message):
    __slots__ = ("error", "cfile_doc_vec", "cookie_val", "cfile_doc_batch_metadata")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_VEC_FIELD_NUMBER: _ClassVar[int]
    COOKIE_VAL_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_BATCH_METADATA_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cfile_doc_vec: _containers.RepeatedCompositeFieldContainer[CrackedFileArchiveDoc]
    cookie_val: bytes
    cfile_doc_batch_metadata: CrackedFileArchiveDocBatchMetadata
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cfile_doc_vec: _Optional[_Iterable[_Union[CrackedFileArchiveDoc, _Mapping]]] = ..., cookie_val: _Optional[bytes] = ..., cfile_doc_batch_metadata: _Optional[_Union[CrackedFileArchiveDocBatchMetadata, _Mapping]] = ...) -> None: ...

class ReleaseCrackedFileIndexArg(_message.Message):
    __slots__ = ("cfile_handle",)
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    cfile_handle: CrackedFileIndexHandle
    def __init__(self, cfile_handle: _Optional[_Union[CrackedFileIndexHandle, _Mapping]] = ...) -> None: ...

class ReleaseCrackedFileIndexResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class PutCrackedFileIndexHandle(_message.Message):
    __slots__ = ("db_dir_path", "DEPRECATED_src_db_mtime_usecs", "object_id", "instance_id", "base_instance_id", "cluster_partition_id", "restore_cfile_index_supported", "cfile_index_metadata", "backup_type", "can_use_ranges")
    DB_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_SRC_DB_MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CFILE_INDEX_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CFILE_INDEX_METADATA_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAN_USE_RANGES_FIELD_NUMBER: _ClassVar[int]
    db_dir_path: str
    DEPRECATED_src_db_mtime_usecs: int
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    cluster_partition_id: int
    restore_cfile_index_supported: bool
    cfile_index_metadata: CrackedFileIndexMetadata
    backup_type: _enums_pb2.Environment.Type
    can_use_ranges: bool
    def __init__(self, db_dir_path: _Optional[str] = ..., DEPRECATED_src_db_mtime_usecs: _Optional[int] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., restore_cfile_index_supported: bool = ..., cfile_index_metadata: _Optional[_Union[CrackedFileIndexMetadata, _Mapping]] = ..., backup_type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., can_use_ranges: bool = ...) -> None: ...

class PreparePutCrackedFileIndexArg(_message.Message):
    __slots__ = ("task_id", "object_id", "instance_id", "base_instance_id", "cluster_partition_id", "cfile_index_metadata")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    CFILE_INDEX_METADATA_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    object_id: _magneto_pb2.MagnetoObjectId
    instance_id: _yoda_types_pb2.MagnetoInstanceId
    base_instance_id: _yoda_types_pb2.MagnetoInstanceId
    cluster_partition_id: int
    cfile_index_metadata: CrackedFileIndexMetadata
    def __init__(self, task_id: _Optional[int] = ..., object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., base_instance_id: _Optional[_Union[_yoda_types_pb2.MagnetoInstanceId, _Mapping]] = ..., cluster_partition_id: _Optional[int] = ..., cfile_index_metadata: _Optional[_Union[CrackedFileIndexMetadata, _Mapping]] = ...) -> None: ...

class PreparePutCrackedFileIndexResult(_message.Message):
    __slots__ = ("error", "cfile_handle")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cfile_handle: PutCrackedFileIndexHandle
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cfile_handle: _Optional[_Union[PutCrackedFileIndexHandle, _Mapping]] = ...) -> None: ...

class PutCrackedFileIndexArg(_message.Message):
    __slots__ = ("cfile_handle", "cfile_doc_vec", "view_box_id", "registered_source", "cfile_doc_batch_metadata", "cookie")
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CFILE_DOC_BATCH_METADATA_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    cfile_handle: PutCrackedFileIndexHandle
    cfile_doc_vec: _containers.RepeatedCompositeFieldContainer[CrackedFileArchiveDoc]
    view_box_id: int
    registered_source: _entity_pb2.EntityProto
    cfile_doc_batch_metadata: CrackedFileArchiveDocBatchMetadata
    cookie: bytes
    def __init__(self, cfile_handle: _Optional[_Union[PutCrackedFileIndexHandle, _Mapping]] = ..., cfile_doc_vec: _Optional[_Iterable[_Union[CrackedFileArchiveDoc, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., registered_source: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., cfile_doc_batch_metadata: _Optional[_Union[CrackedFileArchiveDocBatchMetadata, _Mapping]] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class PutCrackedFileIndexResult(_message.Message):
    __slots__ = ("error", "cookie")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    cookie: bytes
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., cookie: _Optional[bytes] = ...) -> None: ...

class ReleasePutCrackedFileIndexArg(_message.Message):
    __slots__ = ("cfile_handle", "should_commit", "add_snapshot_arg", "object_doc", "slave_processing_error", "aux_db")
    class AuxDbEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    WORK_EXT_FIELD_NUMBER: _ClassVar[int]
    work_ext: _descriptor.FieldDescriptor
    CFILE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_COMMIT_FIELD_NUMBER: _ClassVar[int]
    ADD_SNAPSHOT_ARG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DOC_FIELD_NUMBER: _ClassVar[int]
    SLAVE_PROCESSING_ERROR_FIELD_NUMBER: _ClassVar[int]
    AUX_DB_FIELD_NUMBER: _ClassVar[int]
    cfile_handle: PutCrackedFileIndexHandle
    should_commit: bool
    add_snapshot_arg: _yoda_pb2.AddSnapshotArg
    object_doc: _documents_pb2.ObjectSnapshotDocument
    slave_processing_error: _error_pb2.ErrorProto
    aux_db: _containers.ScalarMap[str, bytes]
    def __init__(self, cfile_handle: _Optional[_Union[PutCrackedFileIndexHandle, _Mapping]] = ..., should_commit: bool = ..., add_snapshot_arg: _Optional[_Union[_yoda_pb2.AddSnapshotArg, _Mapping]] = ..., object_doc: _Optional[_Union[_documents_pb2.ObjectSnapshotDocument, _Mapping]] = ..., slave_processing_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., aux_db: _Optional[_Mapping[str, bytes]] = ...) -> None: ...

class ReleasePutCrackedFileIndexResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetMissingMigratedSnapshotsArg(_message.Message):
    __slots__ = ("tenant_id", "migration_uuid", "objects")
    class ObjectInfo(_message.Message):
        __slots__ = ("object_id", "tx_entity_id", "run_info_vec", "previous_run_start_time_usecs", "previous_job_instance_id", "next_run_start_time_usecs", "next_job_instance_id")
        class RunInfo(_message.Message):
            __slots__ = ("run_start_time_usecs", "job_instance_id", "view_box_id", "view_name", "replica_info")
            RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
            VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
            VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
            REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
            run_start_time_usecs: int
            job_instance_id: int
            view_box_id: int
            view_name: str
            replica_info: _yoda_pb2.SnapshotReplicas
            def __init__(self, run_start_time_usecs: _Optional[int] = ..., job_instance_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., replica_info: _Optional[_Union[_yoda_pb2.SnapshotReplicas, _Mapping]] = ...) -> None: ...
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        TX_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        RUN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        NEXT_RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        NEXT_JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        object_id: _magneto_pb2.MagnetoObjectId
        tx_entity_id: int
        run_info_vec: _containers.RepeatedCompositeFieldContainer[GetMissingMigratedSnapshotsArg.ObjectInfo.RunInfo]
        previous_run_start_time_usecs: int
        previous_job_instance_id: int
        next_run_start_time_usecs: int
        next_job_instance_id: int
        def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., tx_entity_id: _Optional[int] = ..., run_info_vec: _Optional[_Iterable[_Union[GetMissingMigratedSnapshotsArg.ObjectInfo.RunInfo, _Mapping]]] = ..., previous_run_start_time_usecs: _Optional[int] = ..., previous_job_instance_id: _Optional[int] = ..., next_run_start_time_usecs: _Optional[int] = ..., next_job_instance_id: _Optional[int] = ...) -> None: ...
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_UUID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    migration_uuid: str
    objects: _containers.RepeatedCompositeFieldContainer[GetMissingMigratedSnapshotsArg.ObjectInfo]
    def __init__(self, tenant_id: _Optional[str] = ..., migration_uuid: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[GetMissingMigratedSnapshotsArg.ObjectInfo, _Mapping]]] = ...) -> None: ...

class GetMissingMigratedSnapshotsResult(_message.Message):
    __slots__ = ("error", "objects")
    class ObjectInfo(_message.Message):
        __slots__ = ("object_id", "missing_run_info_vec")
        class RunInfo(_message.Message):
            __slots__ = ("run_start_time_usecs", "replica_info")
            RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
            REPLICA_INFO_FIELD_NUMBER: _ClassVar[int]
            run_start_time_usecs: int
            replica_info: _yoda_pb2.SnapshotReplicas
            def __init__(self, run_start_time_usecs: _Optional[int] = ..., replica_info: _Optional[_Union[_yoda_pb2.SnapshotReplicas, _Mapping]] = ...) -> None: ...
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        MISSING_RUN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        object_id: _magneto_pb2.MagnetoObjectId
        missing_run_info_vec: _containers.RepeatedCompositeFieldContainer[GetMissingMigratedSnapshotsResult.ObjectInfo.RunInfo]
        def __init__(self, object_id: _Optional[_Union[_magneto_pb2.MagnetoObjectId, _Mapping]] = ..., missing_run_info_vec: _Optional[_Iterable[_Union[GetMissingMigratedSnapshotsResult.ObjectInfo.RunInfo, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    objects: _containers.RepeatedCompositeFieldContainer[GetMissingMigratedSnapshotsResult.ObjectInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[GetMissingMigratedSnapshotsResult.ObjectInfo, _Mapping]]] = ...) -> None: ...
