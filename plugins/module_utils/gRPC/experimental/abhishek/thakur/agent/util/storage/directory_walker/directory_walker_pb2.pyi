from util.storage import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityMetadata(_message.Message):
    __slots__ = ("root_dir", "path", "type", "mode", "uid", "gid", "ctime_usecs", "mtime_usecs", "access_time_usecs", "size", "symlink_target", "cifs_xattr", "error")
    Extensions: _python_message._ExtensionDict
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[EntityMetadata.EntityType]
        kDirectory: _ClassVar[EntityMetadata.EntityType]
        kSymLink: _ClassVar[EntityMetadata.EntityType]
    kFile: EntityMetadata.EntityType
    kDirectory: EntityMetadata.EntityType
    kSymLink: EntityMetadata.EntityType
    ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    CTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SYMLINK_TARGET_FIELD_NUMBER: _ClassVar[int]
    CIFS_XATTR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    root_dir: bytes
    path: bytes
    type: EntityMetadata.EntityType
    mode: int
    uid: int
    gid: int
    ctime_usecs: int
    mtime_usecs: int
    access_time_usecs: int
    size: int
    symlink_target: bytes
    cifs_xattr: bytes
    error: _error_pb2.ErrorProto
    def __init__(self, root_dir: _Optional[bytes] = ..., path: _Optional[bytes] = ..., type: _Optional[_Union[EntityMetadata.EntityType, str]] = ..., mode: _Optional[int] = ..., uid: _Optional[int] = ..., gid: _Optional[int] = ..., ctime_usecs: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., access_time_usecs: _Optional[int] = ..., size: _Optional[int] = ..., symlink_target: _Optional[bytes] = ..., cifs_xattr: _Optional[bytes] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class InodeMetadataProto(_message.Message):
    __slots__ = ("extended_attributes",)
    class ExtendedAttributes(_message.Message):
        __slots__ = ("linux_extended_attributes",)
        class LinuxFileExtendedAttribute(_message.Message):
            __slots__ = ("name", "value")
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        LINUX_EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        linux_extended_attributes: _containers.RepeatedCompositeFieldContainer[InodeMetadataProto.ExtendedAttributes.LinuxFileExtendedAttribute]
        def __init__(self, linux_extended_attributes: _Optional[_Iterable[_Union[InodeMetadataProto.ExtendedAttributes.LinuxFileExtendedAttribute, _Mapping]]] = ...) -> None: ...
    EXTENDED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    extended_attributes: InodeMetadataProto.ExtendedAttributes
    def __init__(self, extended_attributes: _Optional[_Union[InodeMetadataProto.ExtendedAttributes, _Mapping]] = ...) -> None: ...
