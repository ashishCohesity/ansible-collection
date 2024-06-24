from configs import cluster_config_pb2 as _cluster_config_pb2
from keychain.base import keychain_pb2 as _keychain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudObjectEncryptionMetadataProto(_message.Message):
    __slots__ = ("edek_info", "cloud_object_metadata_size", "cloud_object_metadata_checksum")
    EDEK_INFO_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_METADATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_METADATA_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    edek_info: _keychain_pb2.EdekProto
    cloud_object_metadata_size: int
    cloud_object_metadata_checksum: int
    def __init__(self, edek_info: _Optional[_Union[_keychain_pb2.EdekProto, _Mapping]] = ..., cloud_object_metadata_size: _Optional[int] = ..., cloud_object_metadata_checksum: _Optional[int] = ...) -> None: ...

class CloudObjectMetadataProto(_message.Message):
    __slots__ = ("data_format_version", "cloud_object_id", "compression_level", "object_type", "max_allocated_local_id", "segment_metadata_vec")
    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMetadataObjectType: _ClassVar[CloudObjectMetadataProto.ObjectType]
        kSnapTreeObjectType: _ClassVar[CloudObjectMetadataProto.ObjectType]
        kDomainConfigObjectType: _ClassVar[CloudObjectMetadataProto.ObjectType]
    kMetadataObjectType: CloudObjectMetadataProto.ObjectType
    kSnapTreeObjectType: CloudObjectMetadataProto.ObjectType
    kDomainConfigObjectType: CloudObjectMetadataProto.ObjectType
    class SegmentMetadataProto(_message.Message):
        __slots__ = ("start_offset", "morphed_size", "morphed_checksum", "unmorphed_size", "unmorphed_checksum", "unmorphed_header_size", "min_local_id", "max_local_id", "num_entries")
        START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        MORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        MORPHED_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        UNMORPHED_SIZE_FIELD_NUMBER: _ClassVar[int]
        UNMORPHED_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
        UNMORPHED_HEADER_SIZE_FIELD_NUMBER: _ClassVar[int]
        MIN_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        start_offset: int
        morphed_size: int
        morphed_checksum: int
        unmorphed_size: int
        unmorphed_checksum: int
        unmorphed_header_size: int
        min_local_id: int
        max_local_id: int
        num_entries: int
        def __init__(self, start_offset: _Optional[int] = ..., morphed_size: _Optional[int] = ..., morphed_checksum: _Optional[int] = ..., unmorphed_size: _Optional[int] = ..., unmorphed_checksum: _Optional[int] = ..., unmorphed_header_size: _Optional[int] = ..., min_local_id: _Optional[int] = ..., max_local_id: _Optional[int] = ..., num_entries: _Optional[int] = ...) -> None: ...
    DATA_FORMAT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_ALLOCATED_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_METADATA_VEC_FIELD_NUMBER: _ClassVar[int]
    data_format_version: int
    cloud_object_id: int
    compression_level: _cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel
    object_type: CloudObjectMetadataProto.ObjectType
    max_allocated_local_id: int
    segment_metadata_vec: _containers.RepeatedCompositeFieldContainer[CloudObjectMetadataProto.SegmentMetadataProto]
    def __init__(self, data_format_version: _Optional[int] = ..., cloud_object_id: _Optional[int] = ..., compression_level: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.StoragePolicy.CompressionLevel, str]] = ..., object_type: _Optional[_Union[CloudObjectMetadataProto.ObjectType, str]] = ..., max_allocated_local_id: _Optional[int] = ..., segment_metadata_vec: _Optional[_Iterable[_Union[CloudObjectMetadataProto.SegmentMetadataProto, _Mapping]]] = ...) -> None: ...

class SegmentHeaderProto(_message.Message):
    __slots__ = ("entry_index_vec",)
    class EntryIndexProto(_message.Message):
        __slots__ = ("object_local_id", "relative_offset", "payload_size", "entry_type", "tags")
        class EntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNoneEntryType: _ClassVar[SegmentHeaderProto.EntryIndexProto.EntryType]
            kViewSnapTreeNode: _ClassVar[SegmentHeaderProto.EntryIndexProto.EntryType]
            kBlobSnapTreeNode: _ClassVar[SegmentHeaderProto.EntryIndexProto.EntryType]
            kMetadataType: _ClassVar[SegmentHeaderProto.EntryIndexProto.EntryType]
            kS3ObjectSnapTreeNode: _ClassVar[SegmentHeaderProto.EntryIndexProto.EntryType]
        kNoneEntryType: SegmentHeaderProto.EntryIndexProto.EntryType
        kViewSnapTreeNode: SegmentHeaderProto.EntryIndexProto.EntryType
        kBlobSnapTreeNode: SegmentHeaderProto.EntryIndexProto.EntryType
        kMetadataType: SegmentHeaderProto.EntryIndexProto.EntryType
        kS3ObjectSnapTreeNode: SegmentHeaderProto.EntryIndexProto.EntryType
        class TagsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        OBJECT_LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
        ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        object_local_id: int
        relative_offset: int
        payload_size: int
        entry_type: SegmentHeaderProto.EntryIndexProto.EntryType
        tags: _containers.ScalarMap[str, str]
        def __init__(self, object_local_id: _Optional[int] = ..., relative_offset: _Optional[int] = ..., payload_size: _Optional[int] = ..., entry_type: _Optional[_Union[SegmentHeaderProto.EntryIndexProto.EntryType, str]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
    ENTRY_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
    entry_index_vec: _containers.RepeatedCompositeFieldContainer[SegmentHeaderProto.EntryIndexProto]
    def __init__(self, entry_index_vec: _Optional[_Iterable[_Union[SegmentHeaderProto.EntryIndexProto, _Mapping]]] = ...) -> None: ...
