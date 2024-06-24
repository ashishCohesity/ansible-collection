from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PayloadMsg(_message.Message):
    __slots__ = ("tag", "str")
    TAG_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    tag: int
    str: str
    def __init__(self, tag: _Optional[int] = ..., str: _Optional[str] = ...) -> None: ...

class PayloadReply(_message.Message):
    __slots__ = ("tag", "str")
    TAG_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    tag: int
    str: str
    def __init__(self, tag: _Optional[int] = ..., str: _Optional[str] = ...) -> None: ...
