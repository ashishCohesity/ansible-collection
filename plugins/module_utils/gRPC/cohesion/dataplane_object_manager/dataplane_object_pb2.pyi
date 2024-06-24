from cohesion.base import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectParamsProto(_message.Message):
    __slots__ = ("storage_handle", "object_name", "mode", "base_storage_handle", "upload_id")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ObjectParamsProto.Mode]
        kCreate: _ClassVar[ObjectParamsProto.Mode]
        kRead: _ClassVar[ObjectParamsProto.Mode]
        kUpdate: _ClassVar[ObjectParamsProto.Mode]
    kNone: ObjectParamsProto.Mode
    kCreate: ObjectParamsProto.Mode
    kRead: ObjectParamsProto.Mode
    kUpdate: ObjectParamsProto.Mode
    STORAGE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    BASE_STORAGE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    storage_handle: _common_pb2.BackupStorageHandle
    object_name: str
    mode: ObjectParamsProto.Mode
    base_storage_handle: _common_pb2.BackupStorageHandle
    upload_id: str
    def __init__(self, storage_handle: _Optional[_Union[_common_pb2.BackupStorageHandle, _Mapping]] = ..., object_name: _Optional[str] = ..., mode: _Optional[_Union[ObjectParamsProto.Mode, str]] = ..., base_storage_handle: _Optional[_Union[_common_pb2.BackupStorageHandle, _Mapping]] = ..., upload_id: _Optional[str] = ...) -> None: ...

class ObjectMetadataProto(_message.Message):
    __slots__ = ("blob_snap_tree_id", "object_checksum")
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    blob_snap_tree_id: int
    object_checksum: str
    def __init__(self, blob_snap_tree_id: _Optional[int] = ..., object_checksum: _Optional[str] = ...) -> None: ...
