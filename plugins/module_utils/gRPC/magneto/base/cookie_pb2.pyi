from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CookieProto(_message.Message):
    __slots__ = ("ordered_key_vec",)
    ORDERED_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    ordered_key_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, ordered_key_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...
