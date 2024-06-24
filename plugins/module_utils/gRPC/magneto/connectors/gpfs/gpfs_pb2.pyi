from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("filesystem_path",)
    GPFS_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    gpfs_snapshot_info: _descriptor.FieldDescriptor
    FILESYSTEM_PATH_FIELD_NUMBER: _ClassVar[int]
    filesystem_path: str
    def __init__(self, filesystem_path: _Optional[str] = ...) -> None: ...
