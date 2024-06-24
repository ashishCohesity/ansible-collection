from athena.apps.insight.base import task_pb2 as _task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectSpecProto(_message.Message):
    __slots__ = ("type", "name", "source_id", "root_source_id", "source_path", "directory_info_vec", "vm_volume_vec")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kView: _ClassVar[ObjectSpecProto.Type]
        kVirtualMachine: _ClassVar[ObjectSpecProto.Type]
        kNAS: _ClassVar[ObjectSpecProto.Type]
    kView: ObjectSpecProto.Type
    kVirtualMachine: ObjectSpecProto.Type
    kNAS: ObjectSpecProto.Type
    class DirectoryInfo(_message.Message):
        __slots__ = ("directory_rel_path", "namespace_root_name")
        DIRECTORY_REL_PATH_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
        directory_rel_path: str
        namespace_root_name: str
        def __init__(self, directory_rel_path: _Optional[str] = ..., namespace_root_name: _Optional[str] = ...) -> None: ...
    class VmVolumeInfo(_message.Message):
        __slots__ = ("volume_uid", "volume_name", "directory_rel_vec")
        VOLUME_UID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        DIRECTORY_REL_VEC_FIELD_NUMBER: _ClassVar[int]
        volume_uid: str
        volume_name: str
        directory_rel_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, volume_uid: _Optional[str] = ..., volume_name: _Optional[str] = ..., directory_rel_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    type: ObjectSpecProto.Type
    name: str
    source_id: int
    root_source_id: int
    source_path: str
    directory_info_vec: _containers.RepeatedCompositeFieldContainer[ObjectSpecProto.DirectoryInfo]
    vm_volume_vec: _containers.RepeatedCompositeFieldContainer[ObjectSpecProto.VmVolumeInfo]
    def __init__(self, type: _Optional[_Union[ObjectSpecProto.Type, str]] = ..., name: _Optional[str] = ..., source_id: _Optional[int] = ..., root_source_id: _Optional[int] = ..., source_path: _Optional[str] = ..., directory_info_vec: _Optional[_Iterable[_Union[ObjectSpecProto.DirectoryInfo, _Mapping]]] = ..., vm_volume_vec: _Optional[_Iterable[_Union[ObjectSpecProto.VmVolumeInfo, _Mapping]]] = ...) -> None: ...

class ApiServerCheckpointProto(_message.Message):
    __slots__ = ("object_vec", "global_file_filter")
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_FILE_FILTER_FIELD_NUMBER: _ClassVar[int]
    object_vec: _containers.RepeatedCompositeFieldContainer[ObjectSpecProto]
    global_file_filter: _task_pb2.FileFilterProto
    def __init__(self, object_vec: _Optional[_Iterable[_Union[ObjectSpecProto, _Mapping]]] = ..., global_file_filter: _Optional[_Union[_task_pb2.FileFilterProto, _Mapping]] = ...) -> None: ...
