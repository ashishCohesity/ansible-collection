from bridge.vault.base import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kBlockBlob: _ClassVar[BlobType]
    kAppendBlob: _ClassVar[BlobType]
    kPageBlob: _ClassVar[BlobType]
kBlockBlob: BlobType
kAppendBlob: BlobType
kPageBlob: BlobType

class CreateContext(_message.Message):
    __slots__ = ("object_size", "blob_type")
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    BLOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_size: int
    blob_type: BlobType
    def __init__(self, object_size: _Optional[int] = ..., blob_type: _Optional[_Union[BlobType, str]] = ...) -> None: ...

class UploadContext(_message.Message):
    __slots__ = ("part_vec", "blob_type", "object_finalized")
    class Part(_message.Message):
        __slots__ = ("part_num", "block_id")
        PART_NUM_FIELD_NUMBER: _ClassVar[int]
        BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
        part_num: int
        block_id: str
        def __init__(self, part_num: _Optional[int] = ..., block_id: _Optional[str] = ...) -> None: ...
    PART_VEC_FIELD_NUMBER: _ClassVar[int]
    BLOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    part_vec: _containers.RepeatedCompositeFieldContainer[UploadContext.Part]
    blob_type: BlobType
    object_finalized: bool
    def __init__(self, part_vec: _Optional[_Iterable[_Union[UploadContext.Part, _Mapping]]] = ..., blob_type: _Optional[_Union[BlobType, str]] = ..., object_finalized: bool = ...) -> None: ...

class DownloadContext(_message.Message):
    __slots__ = ("restore_in_progress", "restore_finished", "download_context_id", "version_id", "snapshot_id", "copy_blob_name")
    RESTORE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    restore_in_progress: bool
    restore_finished: bool
    download_context_id: str
    version_id: str
    snapshot_id: str
    copy_blob_name: str
    def __init__(self, restore_in_progress: bool = ..., restore_finished: bool = ..., download_context_id: _Optional[str] = ..., version_id: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., copy_blob_name: _Optional[str] = ...) -> None: ...

class LambdaConfig(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class AzureCookie(_message.Message):
    __slots__ = ("monitoring_cookie", "cold_tier_cookie", "worm_cookie")
    MONITORING_COOKIE_FIELD_NUMBER: _ClassVar[int]
    COLD_TIER_COOKIE_FIELD_NUMBER: _ClassVar[int]
    WORM_COOKIE_FIELD_NUMBER: _ClassVar[int]
    monitoring_cookie: _common_pb2.MonitoringCookie
    cold_tier_cookie: _common_pb2.ColdTierCookie
    worm_cookie: _common_pb2.WormCookie
    def __init__(self, monitoring_cookie: _Optional[_Union[_common_pb2.MonitoringCookie, _Mapping]] = ..., cold_tier_cookie: _Optional[_Union[_common_pb2.ColdTierCookie, _Mapping]] = ..., worm_cookie: _Optional[_Union[_common_pb2.WormCookie, _Mapping]] = ...) -> None: ...
