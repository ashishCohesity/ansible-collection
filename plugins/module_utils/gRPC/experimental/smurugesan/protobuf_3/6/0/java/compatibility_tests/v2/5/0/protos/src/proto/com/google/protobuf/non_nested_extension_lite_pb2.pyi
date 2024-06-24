from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
NONNESTEDEXTENSIONLITE_FIELD_NUMBER: _ClassVar[int]
nonNestedExtensionLite: _descriptor.FieldDescriptor

class MessageLiteToBeExtended(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class MyNonNestedExtensionLite(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
