from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
FOO_OPTIONS_FIELD_NUMBER: _ClassVar[int]
foo_options: _descriptor.FieldDescriptor

class FooOptions(_message.Message):
    __slots__ = ("foo_name",)
    FOO_NAME_FIELD_NUMBER: _ClassVar[int]
    foo_name: str
    def __init__(self, foo_name: _Optional[str] = ...) -> None: ...
