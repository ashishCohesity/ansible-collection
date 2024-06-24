from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("tag", "object")
    TAG_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    tag: int
    object: _any_pb2.Any
    def __init__(self, tag: _Optional[int] = ..., object: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ("tag", "str")
    TAG_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    tag: int
    str: str
    def __init__(self, tag: _Optional[int] = ..., str: _Optional[str] = ...) -> None: ...
