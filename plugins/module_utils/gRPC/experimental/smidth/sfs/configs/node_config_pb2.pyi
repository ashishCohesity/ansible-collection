from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NodeConfigProto(_message.Message):
    __slots__ = ("sfs_port",)
    SFS_PORT_FIELD_NUMBER: _ClassVar[int]
    sfs_port: int
    def __init__(self, sfs_port: _Optional[int] = ...) -> None: ...
