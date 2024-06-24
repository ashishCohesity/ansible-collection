from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
FLOATING_MSG_FIELD_FIELD_NUMBER: _ClassVar[int]
floating_msg_field: _descriptor.FieldDescriptor
FLOATING_STR_FIELD_FIELD_NUMBER: _ClassVar[int]
floating_str_field: _descriptor.FieldDescriptor

class TestExtensionsMessage(_message.Message):
    __slots__ = ("intfield",)
    Extensions: _python_message._ExtensionDict
    INTFIELD_FIELD_NUMBER: _ClassVar[int]
    intfield: int
    def __init__(self, intfield: _Optional[int] = ...) -> None: ...

class ExtensionMessage(_message.Message):
    __slots__ = ("ext1",)
    EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ext_field: _descriptor.FieldDescriptor
    EXT1_FIELD_NUMBER: _ClassVar[int]
    ext1: str
    def __init__(self, ext1: _Optional[str] = ...) -> None: ...
