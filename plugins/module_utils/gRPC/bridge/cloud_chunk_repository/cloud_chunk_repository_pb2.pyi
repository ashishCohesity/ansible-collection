from configs import cluster_config_pb2 as _cluster_config_pb2
from bridge.blob_store import blob_store_pb2 as _blob_store_pb2
from keychain.base import keychain_pb2 as _keychain_pb2
from open_util.base import aes_encryptor_pb2 as _aes_encryptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudChunkFileMetadataProto(_message.Message):
    __slots__ = ("data_format_version", "compression_level", "chunk_info_vec", "chunk_group_info_vec", "morphed_data_size", "touch_usecs", "max_issued_local_chunk_id")
    class ChunkInfo(_message.Message):
        __slots__ = ("chunk_id", "chunk_column")
        CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNK_COLUMN_FIELD_NUMBER: _ClassVar[int]
        chunk_id: _blob_store_pb2.CloudChunkIdProto
        chunk_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkColumn
        def __init__(self, chunk_id: _Optional[_Union[_blob_store_pb2.CloudChunkIdProto, _Mapping]] = ..., chunk_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkColumn, _Mapping]] = ...) -> None: ...
    class ChunkGroupInfo(_message.Message):
        __slots__ = ("chunkgroup_id", "chunkgroup_column")
        CHUNKGROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CHUNKGROUP_COLUMN_FIELD_NUMBER: _ClassVar[int]
        chunkgroup_id: int
        chunkgroup_column: _blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn
        def __init__(self, chunkgroup_id: _Optional[int] = ..., chunkgroup_column: _Optional[_Union[_blob_store_pb2.ChunkFileMetadataProto.ChunkGroupColumn, _Mapping]] = ...) -> None: ...
    DATA_FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CHUNK_GROUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MORPHED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOUCH_USECS_FIELD_NUMBER: _ClassVar[int]
    MAX_ISSUED_LOCAL_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    data_format_version: int
    compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    chunk_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileMetadataProto.ChunkInfo]
    chunk_group_info_vec: _containers.RepeatedCompositeFieldContainer[CloudChunkFileMetadataProto.ChunkGroupInfo]
    morphed_data_size: int
    touch_usecs: int
    max_issued_local_chunk_id: int
    def __init__(self, data_format_version: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., chunk_info_vec: _Optional[_Iterable[_Union[CloudChunkFileMetadataProto.ChunkInfo, _Mapping]]] = ..., chunk_group_info_vec: _Optional[_Iterable[_Union[CloudChunkFileMetadataProto.ChunkGroupInfo, _Mapping]]] = ..., morphed_data_size: _Optional[int] = ..., touch_usecs: _Optional[int] = ..., max_issued_local_chunk_id: _Optional[int] = ...) -> None: ...

class CloudChunkFileEncryptionMetadataProto(_message.Message):
    __slots__ = ("edek_info", "morphed_metadata_size", "encryption_mode")
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    MORPHED_METADATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    edek_info: _keychain_pb2.EdekProto
    morphed_metadata_size: int
    encryption_mode: _aes_encryptor_pb2.AESEncryptorMode
    def __init__(self, edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., morphed_metadata_size: _Optional[int] = ..., encryption_mode: _Optional[_Union[_aes_encryptor_pb2.AESEncryptorMode, str]] = ...) -> None: ...
