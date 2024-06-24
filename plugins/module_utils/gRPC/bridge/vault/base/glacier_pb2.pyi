from bridge.vault.base import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadContext(_message.Message):
    __slots__ = ("upload_id", "upload_part_vec", "object_name", "archive_object_finalized", "archive_object_size_bytes", "max_object_part_size_bytes")
    class UploadPart(_message.Message):
        __slots__ = ("part_num", "sha256_tree_hash")
        PART_NUM_FIELD_NUMBER: _ClassVar[int]
        SHA256_TREE_HASH_FIELD_NUMBER: _ClassVar[int]
        part_num: int
        sha256_tree_hash: bytes
        def __init__(self, part_num: _Optional[int] = ..., sha256_tree_hash: _Optional[bytes] = ...) -> None: ...
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_PART_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_OBJECT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECT_PART_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    upload_part_vec: _containers.RepeatedCompositeFieldContainer[UploadContext.UploadPart]
    object_name: str
    archive_object_finalized: bool
    archive_object_size_bytes: int
    max_object_part_size_bytes: int
    def __init__(self, upload_id: _Optional[str] = ..., upload_part_vec: _Optional[_Iterable[_Union[UploadContext.UploadPart, _Mapping]]] = ..., object_name: _Optional[str] = ..., archive_object_finalized: bool = ..., archive_object_size_bytes: _Optional[int] = ..., max_object_part_size_bytes: _Optional[int] = ...) -> None: ...

class DownloadContext(_message.Message):
    __slots__ = ("job_id", "offset", "size")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    offset: int
    size: int
    def __init__(self, job_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListObjectsContext(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class JobStatusProto(_message.Message):
    __slots__ = ("action", "archive_id", "archive_size_in_bytes", "archive_SHA256_tree_hash", "completed", "completion_date", "creation_date", "inventory_size_in_bytes", "job_description", "job_id", "retrieval_byte_range", "SHA256_tree_hash", "SNS_topic", "status_code", "status_message", "tier", "vault_ARN", "inventory_retrieval_parameters")
    class InventoryRetrievalParams(_message.Message):
        __slots__ = ("format", "start_date", "end_date", "limit", "marker")
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        START_DATE_FIELD_NUMBER: _ClassVar[int]
        END_DATE_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        MARKER_FIELD_NUMBER: _ClassVar[int]
        format: str
        start_date: str
        end_date: str
        limit: str
        marker: str
        def __init__(self, format: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., limit: _Optional[str] = ..., marker: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_SHA256_TREE_HASH_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_DATE_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_BYTE_RANGE_FIELD_NUMBER: _ClassVar[int]
    SHA256_TREE_HASH_FIELD_NUMBER: _ClassVar[int]
    SNS_TOPIC_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    VAULT_ARN_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_RETRIEVAL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    action: str
    archive_id: str
    archive_size_in_bytes: int
    archive_SHA256_tree_hash: str
    completed: bool
    completion_date: str
    creation_date: str
    inventory_size_in_bytes: int
    job_description: str
    job_id: str
    retrieval_byte_range: str
    SHA256_tree_hash: str
    SNS_topic: str
    status_code: str
    status_message: str
    tier: str
    vault_ARN: str
    inventory_retrieval_parameters: JobStatusProto.InventoryRetrievalParams
    def __init__(self, action: _Optional[str] = ..., archive_id: _Optional[str] = ..., archive_size_in_bytes: _Optional[int] = ..., archive_SHA256_tree_hash: _Optional[str] = ..., completed: bool = ..., completion_date: _Optional[str] = ..., creation_date: _Optional[str] = ..., inventory_size_in_bytes: _Optional[int] = ..., job_description: _Optional[str] = ..., job_id: _Optional[str] = ..., retrieval_byte_range: _Optional[str] = ..., SHA256_tree_hash: _Optional[str] = ..., SNS_topic: _Optional[str] = ..., status_code: _Optional[str] = ..., status_message: _Optional[str] = ..., tier: _Optional[str] = ..., vault_ARN: _Optional[str] = ..., inventory_retrieval_parameters: _Optional[_Union[JobStatusProto.InventoryRetrievalParams, _Mapping]] = ...) -> None: ...

class ListObjectsResultProto(_message.Message):
    __slots__ = ("vault_ARN", "inventory_date", "archive_list")
    class Archive(_message.Message):
        __slots__ = ("archive_id", "archive_description", "creation_date", "size", "SHA256_tree_hash")
        ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        SHA256_TREE_HASH_FIELD_NUMBER: _ClassVar[int]
        archive_id: str
        archive_description: str
        creation_date: str
        size: int
        SHA256_tree_hash: str
        def __init__(self, archive_id: _Optional[str] = ..., archive_description: _Optional[str] = ..., creation_date: _Optional[str] = ..., size: _Optional[int] = ..., SHA256_tree_hash: _Optional[str] = ...) -> None: ...
    VAULT_ARN_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_DATE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_LIST_FIELD_NUMBER: _ClassVar[int]
    vault_ARN: str
    inventory_date: str
    archive_list: _containers.RepeatedCompositeFieldContainer[ListObjectsResultProto.Archive]
    def __init__(self, vault_ARN: _Optional[str] = ..., inventory_date: _Optional[str] = ..., archive_list: _Optional[_Iterable[_Union[ListObjectsResultProto.Archive, _Mapping]]] = ...) -> None: ...

class ListJobsResultProto(_message.Message):
    __slots__ = ("job_list", "marker")
    class Job(_message.Message):
        __slots__ = ("action", "archive_id", "archive_size_in_bytes", "completed", "completion_date", "creation_date", "job_description", "job_id", "retrieval_byte_range", "status_code", "status_message", "completion_timestamp_secs")
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_DATE_FIELD_NUMBER: _ClassVar[int]
        CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
        JOB_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        RETRIEVAL_BYTE_RANGE_FIELD_NUMBER: _ClassVar[int]
        STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
        STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
        action: str
        archive_id: str
        archive_size_in_bytes: int
        completed: bool
        completion_date: str
        creation_date: str
        job_description: str
        job_id: str
        retrieval_byte_range: str
        status_code: str
        status_message: str
        completion_timestamp_secs: int
        def __init__(self, action: _Optional[str] = ..., archive_id: _Optional[str] = ..., archive_size_in_bytes: _Optional[int] = ..., completed: bool = ..., completion_date: _Optional[str] = ..., creation_date: _Optional[str] = ..., job_description: _Optional[str] = ..., job_id: _Optional[str] = ..., retrieval_byte_range: _Optional[str] = ..., status_code: _Optional[str] = ..., status_message: _Optional[str] = ..., completion_timestamp_secs: _Optional[int] = ...) -> None: ...
    JOB_LIST_FIELD_NUMBER: _ClassVar[int]
    MARKER_FIELD_NUMBER: _ClassVar[int]
    job_list: _containers.RepeatedCompositeFieldContainer[ListJobsResultProto.Job]
    marker: str
    def __init__(self, job_list: _Optional[_Iterable[_Union[ListJobsResultProto.Job, _Mapping]]] = ..., marker: _Optional[str] = ...) -> None: ...

class ListObjectPartsProto(_message.Message):
    __slots__ = ("archive_description", "creation_date", "marker", "multi_part_upload_id", "part_vec", "vault_ARN")
    class Parts(_message.Message):
        __slots__ = ("range_in_bytes", "sha256_tree_hash")
        RANGE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        SHA256_TREE_HASH_FIELD_NUMBER: _ClassVar[int]
        range_in_bytes: str
        sha256_tree_hash: str
        def __init__(self, range_in_bytes: _Optional[str] = ..., sha256_tree_hash: _Optional[str] = ...) -> None: ...
    ARCHIVE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    MARKER_FIELD_NUMBER: _ClassVar[int]
    MULTI_PART_UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_VEC_FIELD_NUMBER: _ClassVar[int]
    VAULT_ARN_FIELD_NUMBER: _ClassVar[int]
    archive_description: str
    creation_date: str
    marker: str
    multi_part_upload_id: str
    part_vec: _containers.RepeatedCompositeFieldContainer[ListObjectPartsProto.Parts]
    vault_ARN: str
    def __init__(self, archive_description: _Optional[str] = ..., creation_date: _Optional[str] = ..., marker: _Optional[str] = ..., multi_part_upload_id: _Optional[str] = ..., part_vec: _Optional[_Iterable[_Union[ListObjectPartsProto.Parts, _Mapping]]] = ..., vault_ARN: _Optional[str] = ...) -> None: ...

class GlacierCookie(_message.Message):
    __slots__ = ("monitoring_cookie", "cold_tier_cookie")
    MONITORING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    COLD_TIER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    monitoring_cookie: _common_pb2.MonitoringCookie
    cold_tier_cookie: _common_pb2.ColdTierCookie
    def __init__(self, monitoring_cookie: _Optional[_Union[_common_pb2.MonitoringCookie, _Mapping]] = ..., cold_tier_cookie: _Optional[_Union[_common_pb2.ColdTierCookie, _Mapping]] = ...) -> None: ...
