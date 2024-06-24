from configs import cluster_config_pb2 as _cluster_config_pb2
from util.base import cluster_instance_identifier_pb2 as _cluster_instance_identifier_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArchivedLocation(_message.Message):
    __slots__ = ("archive_uid", "base_archive_id", "data_object_vec", "morphed_info", "data_ptr", "blob_data_location_vec")
    class MorphedInfo(_message.Message):
        __slots__ = ("object_prefix", "block_size", "compression_level", "encryption_info")
        class EncryptionInfo(_message.Message):
            __slots__ = ("cluster_instance_id", "random_nonce", "encryption_level", "encryption_config")
            CLUSTER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
            RANDOM_NONCE_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
            ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
            cluster_instance_id: _cluster_instance_identifier_pb2.ClusterInstanceIdentifier
            random_nonce: bytes
            encryption_level: _cluster_config_pb2.ClusterConfigProto.EncryptionLevel
            encryption_config: _cluster_config_pb2.ClusterConfigProto.Vault.EncryptionConfig
            def __init__(self, cluster_instance_id: _Optional[_Union[_cluster_instance_identifier_pb2.ClusterInstanceIdentifier, _Mapping]] = ..., random_nonce: _Optional[bytes] = ..., encryption_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.EncryptionLevel, str]] = ..., encryption_config: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.Vault.EncryptionConfig, _Mapping]] = ...) -> None: ...
        OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
        object_prefix: bytes
        block_size: int
        compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
        encryption_info: ArchivedLocation.MorphedInfo.EncryptionInfo
        def __init__(self, object_prefix: _Optional[bytes] = ..., block_size: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., encryption_info: _Optional[_Union[ArchivedLocation.MorphedInfo.EncryptionInfo, _Mapping]] = ...) -> None: ...
    ARCHIVE_UID_FIELD_NUMBER: _ClassVar[int]
    BASE_ARCHIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    MORPHED_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_PTR_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    archive_uid: _universal_id_pb2.UniversalIdProto
    base_archive_id: int
    data_object_vec: _containers.RepeatedCompositeFieldContainer[ArchivedObject]
    morphed_info: ArchivedLocation.MorphedInfo
    data_ptr: ArchiveSnapTreeNodePtrProto
    blob_data_location_vec: _containers.RepeatedCompositeFieldContainer[ArchiveDataRange]
    def __init__(self, archive_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., base_archive_id: _Optional[int] = ..., data_object_vec: _Optional[_Iterable[_Union[ArchivedObject, _Mapping]]] = ..., morphed_info: _Optional[_Union[ArchivedLocation.MorphedInfo, _Mapping]] = ..., data_ptr: _Optional[_Union[ArchiveSnapTreeNodePtrProto, _Mapping]] = ..., blob_data_location_vec: _Optional[_Iterable[_Union[ArchiveDataRange, _Mapping]]] = ...) -> None: ...

class ArchiveSnapTreeNodePtrProto(_message.Message):
    __slots__ = ("object_uid", "segment_offset", "data_offset")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    segment_offset: int
    data_offset: int
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., segment_offset: _Optional[int] = ..., data_offset: _Optional[int] = ...) -> None: ...

class CloudChunkFileIdProto(_message.Message):
    __slots__ = ("object_id", "uid")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, object_id: _Optional[int] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ArchiveChunkPtrProto(_message.Message):
    __slots__ = ("object_uid", "segment_offset", "data_offset", "domain_uid", "chunk_file_id")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_UID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    segment_offset: int
    data_offset: int
    domain_uid: _universal_id_pb2.UniversalIdProto
    chunk_file_id: CloudChunkFileIdProto
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., segment_offset: _Optional[int] = ..., data_offset: _Optional[int] = ..., domain_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., chunk_file_id: _Optional[_Union[CloudChunkFileIdProto, _Mapping]] = ...) -> None: ...

class ArchiveSegmentPtrProto(_message.Message):
    __slots__ = ("object_uid", "segment_offset")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    segment_offset: int
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., segment_offset: _Optional[int] = ...) -> None: ...

class ArchivedObject(_message.Message):
    __slots__ = ("object_uid", "object_name", "size")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    object_name: bytes
    size: int
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., object_name: _Optional[bytes] = ..., size: _Optional[int] = ...) -> None: ...

class ArchiveDataRange(_message.Message):
    __slots__ = ("object_uid", "offset", "size", "object_name")
    OBJECT_UID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_uid: _universal_id_pb2.UniversalIdProto
    offset: int
    size: int
    object_name: str
    def __init__(self, object_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., object_name: _Optional[str] = ...) -> None: ...

class CloudObjectIdProto(_message.Message):
    __slots__ = ("domain_id", "object_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: int
    object_id: int
    def __init__(self, domain_id: _Optional[int] = ..., object_id: _Optional[int] = ...) -> None: ...

class CloudNodePtrProto(_message.Message):
    __slots__ = ("object_id", "object_local_id")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: int
    object_local_id: int
    def __init__(self, object_id: _Optional[int] = ..., object_local_id: _Optional[int] = ...) -> None: ...

class CloudNodePrefixPtrProto(_message.Message):
    __slots__ = ("cloud_node_ptr", "cloud_object_prefix")
    CLOUD_NODE_PTR_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    cloud_node_ptr: CloudNodePtrProto
    cloud_object_prefix: str
    def __init__(self, cloud_node_ptr: _Optional[_Union[CloudNodePtrProto, _Mapping]] = ..., cloud_object_prefix: _Optional[str] = ...) -> None: ...

class LeaseProto(_message.Message):
    __slots__ = ("lessee_cluster_id", "network_realm_id", "lease_id", "most_recent_reference_timestamp_secs")
    LESSEE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    MOST_RECENT_REFERENCE_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    lessee_cluster_id: int
    network_realm_id: int
    lease_id: int
    most_recent_reference_timestamp_secs: int
    def __init__(self, lessee_cluster_id: _Optional[int] = ..., network_realm_id: _Optional[int] = ..., lease_id: _Optional[int] = ..., most_recent_reference_timestamp_secs: _Optional[int] = ...) -> None: ...
