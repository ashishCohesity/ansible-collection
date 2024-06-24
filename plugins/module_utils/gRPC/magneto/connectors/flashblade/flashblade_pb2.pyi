from magneto.connectors.file import file_pb2 as _file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("nfs_export_rules",)
    FLASHBLADE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    flashblade_snapshot_info: _descriptor.FieldDescriptor
    NFS_EXPORT_RULES_FIELD_NUMBER: _ClassVar[int]
    nfs_export_rules: str
    def __init__(self, nfs_export_rules: _Optional[str] = ...) -> None: ...
