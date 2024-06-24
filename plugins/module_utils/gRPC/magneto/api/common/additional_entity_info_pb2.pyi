from magneto.base import enums_pb2 as _enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdditionalEntityInfo(_message.Message):
    __slots__ = ("id", "env")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    id: int
    env: _enums_pb2.Environment.Type
    def __init__(self, id: _Optional[int] = ..., env: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...
