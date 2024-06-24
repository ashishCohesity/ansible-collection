from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FileInfo(_message.Message):
    __slots__ = ("mtime", "size")
    MTIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    mtime: int
    size: int
    def __init__(self, mtime: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "name", "uuid", "cluster_info", "file_info", "dir_info")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCluster: _ClassVar[Entity.Type]
        kFile: _ClassVar[Entity.Type]
        kDirectory: _ClassVar[Entity.Type]
    kCluster: Entity.Type
    kFile: Entity.Type
    kDirectory: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    DIR_INFO_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    name: str
    uuid: str
    cluster_info: ClusterInfo
    file_info: FileInfo
    dir_info: FileInfo
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ..., cluster_info: _Optional[_Union[ClusterInfo, _Mapping]] = ..., file_info: _Optional[_Union[FileInfo, _Mapping]] = ..., dir_info: _Optional[_Union[FileInfo, _Mapping]] = ...) -> None: ...
