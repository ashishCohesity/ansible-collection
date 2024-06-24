from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NisProviderConfFilesProto(_message.Message):
    __slots__ = ("yp_conf",)
    YP_CONF_FIELD_NUMBER: _ClassVar[int]
    yp_conf: bytes
    def __init__(self, yp_conf: _Optional[bytes] = ...) -> None: ...
