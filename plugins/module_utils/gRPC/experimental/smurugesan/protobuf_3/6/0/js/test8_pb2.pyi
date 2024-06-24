from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestNestedExtensionsMessage(_message.Message):
    __slots__ = ("intfield",)
    Extensions: _python_message._ExtensionDict
    INTFIELD_FIELD_NUMBER: _ClassVar[int]
    intfield: int
    def __init__(self, intfield: _Optional[int] = ...) -> None: ...

class TestOuterMessage(_message.Message):
    __slots__ = ()
    class NestedExtensionMessage(_message.Message):
        __slots__ = ("ext1",)
        EXT1_FIELD_NUMBER: _ClassVar[int]
        ext1: str
        def __init__(self, ext1: _Optional[str] = ...) -> None: ...
    INNER_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    inner_extension: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...
