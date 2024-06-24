from util.storage import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checkpoint(_message.Message):
    __slots__ = ("root_dir", "path", "type", "mode", "uid", "gid", "ctime_usecs", "mtime_usecs", "create_time_usecs", "size", "symlink_target", "num_hardlinks", "major_device_number", "minor_device_number", "inode_id", "smb2_attributes", "first_path_to_hardlink", "extended_attributes", "cifs_xattr", "error", "serialized_metadata")
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[Checkpoint.EntityType]
        kDirectory: _ClassVar[Checkpoint.EntityType]
        kBlockDevice: _ClassVar[Checkpoint.EntityType]
        kCharacterDevice: _ClassVar[Checkpoint.EntityType]
        kSymLink: _ClassVar[Checkpoint.EntityType]
        kSocket: _ClassVar[Checkpoint.EntityType]
        kPipe: _ClassVar[Checkpoint.EntityType]
    kFile: Checkpoint.EntityType
    kDirectory: Checkpoint.EntityType
    kBlockDevice: Checkpoint.EntityType
    kCharacterDevice: Checkpoint.EntityType
    kSymLink: Checkpoint.EntityType
    kSocket: Checkpoint.EntityType
    kPipe: Checkpoint.EntityType
    class ExtendedAttribute(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: bytes
        def __init__(self, name: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    NUM_HARDLINKS_FIELD_NUMBER: _ClassVar[int]
    MAJOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MINOR_DEVICE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INODE_ID_FIELD_NUMBER: _ClassVar[int]
    SMB2_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FIRST_PATH_TO_HARDLINK_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CIFS_XATTR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_METADATA_FIELD_NUMBER: _ClassVar[int]
    root_dir: str
    path: str
    type: Checkpoint.EntityType
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    mtime_usecs: int
    create_time_usecs: int
    size: int
    symlink_target: str
    num_hardlinks: int
    major_device_number: int
    minor_device_number: int
    inode_id: int
    smb2_attributes: int
    first_path_to_hardlink: str
    extended_attributes: _containers.RepeatedCompositeFieldContainer[Checkpoint.ExtendedAttribute]
    cifs_xattr: bytes
    error: _error_pb2.ErrorProto
    serialized_metadata: bytes
    def __init__(self, root_dir: _Optional[str] = ..., path: _Optional[str] = ..., type: _Optional[_Union[Checkpoint.EntityType, str]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., create_time_usecs: _Optional[int] = ..., size: _Optional[int] = ..., symlink_target: _Optional[str] = ..., num_hardlinks: _Optional[int] = ..., major_device_number: _Optional[int] = ..., minor_device_number: _Optional[int] = ..., inode_id: _Optional[int] = ..., smb2_attributes: _Optional[int] = ..., first_path_to_hardlink: _Optional[str] = ..., extended_attributes: _Optional[_Iterable[_Union[Checkpoint.ExtendedAttribute, _Mapping]]] = ..., cifs_xattr: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., serialized_metadata: _Optional[bytes] = ...) -> None: ...
