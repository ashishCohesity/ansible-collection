from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kConnect: _ClassVar[MessageType]
    kData: _ClassVar[MessageType]
    kClose: _ClassVar[MessageType]
kConnect: MessageType
kData: MessageType
kClose: MessageType

class StreamMessage(_message.Message):
    __slots__ = ("type", "message")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: MessageType
    message: str
    def __init__(self, type: _Optional[_Union[MessageType, str]] = ..., message: _Optional[str] = ...) -> None: ...
