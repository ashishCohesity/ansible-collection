from bridge.base import cloud_pb2 as _cloud_pb2
from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapFSInodeDataInfo(_message.Message):
    __slots__ = ("type", "blob_id", "blob_offset")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[SnapFSInodeDataInfo.Type]
        kDataFragment: _ClassVar[SnapFSInodeDataInfo.Type]
        kBlobRange: _ClassVar[SnapFSInodeDataInfo.Type]
        kBlob: _ClassVar[SnapFSInodeDataInfo.Type]
        kMegaFile: _ClassVar[SnapFSInodeDataInfo.Type]
    kNone: SnapFSInodeDataInfo.Type
    kDataFragment: SnapFSInodeDataInfo.Type
    kBlobRange: SnapFSInodeDataInfo.Type
    kBlob: SnapFSInodeDataInfo.Type
    kMegaFile: SnapFSInodeDataInfo.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
    type: SnapFSInodeDataInfo.Type
    blob_id: int
    blob_offset: int
    def __init__(self, type: _Optional[_Union[SnapFSInodeDataInfo.Type, str]] = ..., blob_id: _Optional[int] = ..., blob_offset: _Optional[int] = ...) -> None: ...

class SnapFSDirectoryWalkerEntityMetadata(_message.Message):
    __slots__ = ("eh", "parent_eh", "smb_extended_attributes", "s3_metadata", "mega_file_subfile_size_mb", "data_info", "file_level_datalock_metadata", "antivirus_metadata", "archived_location_vec", "data_fragment_id_vec")
    SNAP_FS_ENTITY_MD_FIELD_NUMBER: _ClassVar[int]
    snap_fs_entity_md: _descriptor.FieldDescriptor
    EH_FIELD_NUMBER: _ClassVar[int]
    PARENT_EH_FIELD_NUMBER: _ClassVar[int]
    SMB_EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    MEGA_FILE_SUBFILE_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
    DATA_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_LEVEL_DATALOCK_METADATA_FIELD_NUMBER: _ClassVar[int]
    ANTIVIRUS_METADATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_LOCATION_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_FRAGMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    eh: _entity_handle_pb2.EntityHandleProto
    parent_eh: _entity_handle_pb2.EntityHandleProto
    smb_extended_attributes: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    s3_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata
    mega_file_subfile_size_mb: int
    data_info: SnapFSInodeDataInfo
    file_level_datalock_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata
    antivirus_metadata: _snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata
    archived_location_vec: _containers.RepeatedCompositeFieldContainer[_cloud_pb2.ArchivedLocation]
    data_fragment_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., parent_eh: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., smb_extended_attributes: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ..., s3_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.S3Metadata, _Mapping]] = ..., mega_file_subfile_size_mb: _Optional[int] = ..., data_info: _Optional[_Union[SnapFSInodeDataInfo, _Mapping]] = ..., file_level_datalock_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.FileLevelDataLockMetadata, _Mapping]] = ..., antivirus_metadata: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.AntivirusMetadata, _Mapping]] = ..., archived_location_vec: _Optional[_Iterable[_Union[_cloud_pb2.ArchivedLocation, _Mapping]]] = ..., data_fragment_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
