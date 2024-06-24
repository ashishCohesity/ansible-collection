from yoda.base import error_pb2 as _error_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AsyncVolumeMountArg(_message.Message):
    __slots__ = ("disk_files_path", "volume_name", "volume_info", "mount_point")
    DISK_FILES_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_INFO_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    disk_files_path: str
    volume_name: str
    volume_info: _volume_info_pb2.VolumeInfo
    mount_point: str
    def __init__(self, disk_files_path: _Optional[str] = ..., volume_name: _Optional[str] = ..., volume_info: _Optional[_Union[_volume_info_pb2.VolumeInfo, _Mapping]] = ..., mount_point: _Optional[str] = ...) -> None: ...

class AsyncVolumeMountResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class VolumeUnmountArg(_message.Message):
    __slots__ = ("mount_point",)
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    mount_point: str
    def __init__(self, mount_point: _Optional[str] = ...) -> None: ...

class VolumeUnmountResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
