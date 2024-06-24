from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VolumeShadowStorageInfo(_message.Message):
    __slots__ = ("name", "volume", "shadow_storage_volume", "allocated_space", "max_space", "used_space")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SHADOW_STORAGE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_SPACE_FIELD_NUMBER: _ClassVar[int]
    MAX_SPACE_FIELD_NUMBER: _ClassVar[int]
    USED_SPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    volume: str
    shadow_storage_volume: str
    allocated_space: int
    max_space: int
    used_space: int
    def __init__(self, name: _Optional[str] = ..., volume: _Optional[str] = ..., shadow_storage_volume: _Optional[str] = ..., allocated_space: _Optional[int] = ..., max_space: _Optional[int] = ..., used_space: _Optional[int] = ...) -> None: ...

class VolumeShadowStorageInfoList(_message.Message):
    __slots__ = ("volume_shadow_storage_vec",)
    VOLUME_SHADOW_STORAGE_VEC_FIELD_NUMBER: _ClassVar[int]
    volume_shadow_storage_vec: _containers.RepeatedCompositeFieldContainer[VolumeShadowStorageInfo]
    def __init__(self, volume_shadow_storage_vec: _Optional[_Iterable[_Union[VolumeShadowStorageInfo, _Mapping]]] = ...) -> None: ...
