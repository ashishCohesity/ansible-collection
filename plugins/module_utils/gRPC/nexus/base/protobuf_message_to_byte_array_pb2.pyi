from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnMarshalByteArray(_message.Message):
    __slots__ = ("byte_array",)
    BYTE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    byte_array: bytes
    def __init__(self, byte_array: _Optional[bytes] = ...) -> None: ...
