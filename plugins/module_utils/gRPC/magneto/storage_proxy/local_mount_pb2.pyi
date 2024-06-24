from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNAS: _ClassVar[MountType]
    kDisk: _ClassVar[MountType]
kNAS: MountType
kDisk: MountType

class MountPointInfo(_message.Message):
    __slots__ = ("mountpoint", "ref_count", "last_active_timestamp_secs")
    MOUNTPOINT_FIELD_NUMBER: _ClassVar[int]
    REF_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    mountpoint: str
    ref_count: int
    last_active_timestamp_secs: int
    def __init__(self, mountpoint: _Optional[str] = ..., ref_count: _Optional[int] = ..., last_active_timestamp_secs: _Optional[int] = ...) -> None: ...

class MountTargetInfo(_message.Message):
    __slots__ = ("type", "mount_target_map", "mount_point_map")
    class MountTargetMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MountPointInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MountPointInfo, _Mapping]] = ...) -> None: ...
    class MountPointMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_TARGET_MAP_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_MAP_FIELD_NUMBER: _ClassVar[int]
    type: MountType
    mount_target_map: _containers.MessageMap[str, MountPointInfo]
    mount_point_map: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[MountType, str]] = ..., mount_target_map: _Optional[_Mapping[str, MountPointInfo]] = ..., mount_point_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
