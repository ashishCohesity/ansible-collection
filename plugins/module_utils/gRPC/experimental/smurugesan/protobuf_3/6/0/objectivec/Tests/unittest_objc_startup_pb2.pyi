from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
OPTIONAL_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_int32_extension: _descriptor.FieldDescriptor
REPEATED_INT32_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_int32_extension: _descriptor.FieldDescriptor

class TestObjCStartupMessage(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestObjCStartupNested(_message.Message):
    __slots__ = ()
    NESTED_STRING_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    nested_string_extension: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...
