from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
OPTIONAL_INT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_int_extension: _descriptor.FieldDescriptor
OPTIONAL_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
optional_message_extension: _descriptor.FieldDescriptor
REPEATED_INT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_int_extension: _descriptor.FieldDescriptor
REPEATED_MESSAGE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
repeated_message_extension: _descriptor.FieldDescriptor

class TopLevelMessage(_message.Message):
    __slots__ = ("submessage",)
    SUBMESSAGE_FIELD_NUMBER: _ClassVar[int]
    submessage: ExtendedMessage
    def __init__(self, submessage: _Optional[_Union[ExtendedMessage, _Mapping]] = ...) -> None: ...

class ExtendedMessage(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("foreign_message_int",)
    FOREIGN_MESSAGE_INT_FIELD_NUMBER: _ClassVar[int]
    foreign_message_int: int
    def __init__(self, foreign_message_int: _Optional[int] = ...) -> None: ...
