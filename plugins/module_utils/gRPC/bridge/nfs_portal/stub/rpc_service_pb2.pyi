from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForwardArg(_message.Message):
    __slots__ = ("is_optional",)
    IS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    is_optional: bool
    def __init__(self, is_optional: bool = ...) -> None: ...

class ForwardResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
