from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeInfo(_message.Message):
    __slots__ = ("offset", "chunk_len", "sha1", "is_zero", "has_data", "chunk_offset", "range_len", "is_dedup_chunk", "cloud_chunk_location_vec", "skip_cloud_chunk_mapping", "brick_level_sha1", "skip_unnecessary_metadata_lookups")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LEN_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    IS_ZERO_FIELD_NUMBER: _ClassVar[int]
    HAS_DATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RANGE_LEN_FIELD_NUMBER: _ClassVar[int]
    IS_DEDUP_CHUNK_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_CLOUD_CHUNK_MAPPING_FIELD_NUMBER: _ClassVar[int]
    BRICK_LEVEL_SHA1_FIELD_NUMBER: _ClassVar[int]
    SKIP_UNNECESSARY_METADATA_LOOKUPS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    chunk_len: int
    sha1: bytes
    is_zero: bool
    has_data: bool
    chunk_offset: int
    range_len: int
    is_dedup_chunk: bool
    cloud_chunk_location_vec: _containers.RepeatedCompositeFieldContainer[_blob_store_pb2.CloudChunkLocationProto]
    skip_cloud_chunk_mapping: bool
    brick_level_sha1: bytes
    skip_unnecessary_metadata_lookups: bool
    def __init__(self, offset: _Optional[int] = ..., chunk_len: _Optional[int] = ..., sha1: _Optional[bytes] = ..., is_zero: bool = ..., has_data: bool = ..., chunk_offset: _Optional[int] = ..., range_len: _Optional[int] = ..., is_dedup_chunk: bool = ..., cloud_chunk_location_vec: _Optional[_Iterable[_Union[_blob_store_pb2.CloudChunkLocationProto, _Mapping]]] = ..., skip_cloud_chunk_mapping: bool = ..., brick_level_sha1: _Optional[bytes] = ..., skip_unnecessary_metadata_lookups: bool = ...) -> None: ...

class CloudChunkFileInfo(_message.Message):
    __slots__ = ("cloud_object_id", "version", "chunk_count", "morphed_data_size", "bypass_write_permission", "lease_vec")
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNK_COUNT_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_WRITE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    LEASE_VEC_FIELD_NUMBER: _ClassVar[int]
    cloud_object_id: _cloud_pb2.CloudObjectIdProto
    version: int
    chunk_count: int
    morphed_data_size: int
    bypass_write_permission: bool
    lease_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.LeaseProto]
    def __init__(self, cloud_object_id: _Optional[_Union[_cloud_pb2.CloudObjectIdProto, _Mapping]] = ..., version: _Optional[int] = ..., chunk_count: _Optional[int] = ..., morphed_data_size: _Optional[int] = ..., bypass_write_permission: bool = ..., lease_vec: _Optional[_Iterable[_Union[_cloud_pb2.LeaseProto, _Mapping]]] = ...) -> None: ...

class DedupRange(_message.Message):
    __slots__ = ("range_vec", "cloud_chunk_file_info_vec")
    RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CHUNK_FILE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    range_vec: _containers.RepeatedCompositeFieldContainer[RangeInfo]
    cloud_chunk_file_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileInfo]
    def __init__(self, range_vec: _Optional[_Iterable[_Union[RangeInfo, _Mapping]]] = ..., cloud_chunk_file_info_vec: _Optional[_Iterable[_Union[CloudChunkFileInfo, _Mapping]]] = ...) -> None: ...
