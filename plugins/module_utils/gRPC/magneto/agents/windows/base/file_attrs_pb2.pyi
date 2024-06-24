from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileAttributes(_message.Message):
    __slots__ = ("logical_size", "ctime_usecs", "mtime_usecs", "create_time_usecs", "attributes")
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    logical_size: int
    ctime_usecs: int
    mtime_usecs: int
    create_time_usecs: int
    attributes: _snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes
    def __init__(self, logical_size: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., create_time_usecs: _Optional[int] = ..., attributes: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.ExtendedAttributes, _Mapping]] = ...) -> None: ...
