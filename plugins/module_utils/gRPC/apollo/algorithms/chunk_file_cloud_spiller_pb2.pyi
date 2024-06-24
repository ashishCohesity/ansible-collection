from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChunkFileCloudSpillerContextDataProto(_message.Message):
    __slots__ = ("cluster_config_proto",)
    CLUSTER_CONFIG_PROTO_FIELD_NUMBER: _ClassVar[int]
    cluster_config_proto: _cluster_config_pb2.ClusterConfigProto
    def __init__(self, cluster_config_proto: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto, _Mapping]] = ...) -> None: ...

class ChunkFileCloudSpillerMapKeyProto(_message.Message):
    __slots__ = ("chunk_file_id",)
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_file_id: int
    def __init__(self, chunk_file_id: _Optional[int] = ...) -> None: ...

class ChunkFileCloudSpillerMapValueProto(_message.Message):
    __slots__ = ("last_access_time_secs", "view_box_id", "chunk_file_storage_size", "owner_blob_id", "scribe_row_version", "current_compression_level", "current_encryption_level", "is_erasure_coded")
    LAST_ACCESS_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_STORAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    OWNER_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_ERASURE_CODED_FIELD_NUMBER: _ClassVar[int]
    last_access_time_secs: int
    view_box_id: int
    chunk_file_storage_size: int
    owner_blob_id: int
    scribe_row_version: int
    current_compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    current_encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
    is_erasure_coded: bool
    def __init__(self, last_access_time_secs: _Optional[int] = ..., view_box_id: _Optional[int] = ..., chunk_file_storage_size: _Optional[int] = ..., owner_blob_id: _Optional[int] = ..., scribe_row_version: _Optional[int] = ..., current_compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., current_encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., is_erasure_coded: bool = ...) -> None: ...
