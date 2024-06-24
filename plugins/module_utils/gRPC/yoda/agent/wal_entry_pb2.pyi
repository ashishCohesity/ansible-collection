from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersistentMount(_message.Message):
    __slots__ = ("mount_path", "mount_state", "device_vec", "mount_start_time_usecs", "snapshot_dir", "volume_info")
    class MountState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[PersistentMount.MountState]
        kStarted: _ClassVar[PersistentMount.MountState]
        kDone: _ClassVar[PersistentMount.MountState]
        kUnmounted: _ClassVar[PersistentMount.MountState]
        kInvalid: _ClassVar[PersistentMount.MountState]
    kUnknown: PersistentMount.MountState
    kStarted: PersistentMount.MountState
    kDone: PersistentMount.MountState
    kUnmounted: PersistentMount.MountState
    kInvalid: PersistentMount.MountState
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    MOUNT_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    mount_path: str
    mount_state: PersistentMount.MountState
    device_vec: _containers.RepeatedCompositeFieldContainer[_volume_info_pb2.Device]
    mount_start_time_usecs: int
    snapshot_dir: str
    volume_info: _volume_info_pb2.VolumeInfo
    def __init__(self, mount_path: _Optional[str] = ..., mount_state: _Optional[_Union[PersistentMount.MountState, str]] = ..., device_vec: _Optional[_Iterable[_Union[_volume_info_pb2.Device, _Mapping]]] = ..., mount_start_time_usecs: _Optional[int] = ..., snapshot_dir: _Optional[str] = ..., volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ...) -> None: ...

class WalRecord(_message.Message):
    __slots__ = ("persistent_mount_vec",)
    PERSISTENT_MOUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    persistent_mount_vec: _containers.RepeatedCompositeFieldContainer[PersistentMount]
    def __init__(self, persistent_mount_vec: _Optional[_Iterable[_Union[PersistentMount, _Mapping]]] = ...) -> None: ...
