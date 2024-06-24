from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
MESSAGE_SET_EXTENSION3_FIELD_NUMBER: _ClassVar[int]
message_set_extension3: _descriptor.FieldDescriptor

class TestMessageSet(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class TestMessageSetExtension1(_message.Message):
    __slots__ = ("i",)
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    I_FIELD_NUMBER: _ClassVar[int]
    i: int
    def __init__(self, i: _Optional[int] = ...) -> None: ...

class TestMessageSetExtension2(_message.Message):
    __slots__ = ("str",)
    MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    message_set_extension: _descriptor.FieldDescriptor
    STR_FIELD_NUMBER: _ClassVar[int]
    str: str
    def __init__(self, str: _Optional[str] = ...) -> None: ...

class TestMessageSetExtension3(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
