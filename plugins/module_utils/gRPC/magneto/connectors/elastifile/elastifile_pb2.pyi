from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("snapshot_id", "share_id")
    ELASTIFILE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    elastifile_snapshot_info: _descriptor.FieldDescriptor
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    snapshot_id: int
    share_id: int
    def __init__(self, snapshot_id: _Optional[int] = ..., share_id: _Optional[int] = ...) -> None: ...
