from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientMssg(_message.Message):
    __slots__ = ("message", "message_type")
    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST: _ClassVar[ClientMssg.MessageType]
        REPLY: _ClassVar[ClientMssg.MessageType]
    REQUEST: ClientMssg.MessageType
    REPLY: ClientMssg.MessageType
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    message_type: ClientMssg.MessageType
    def __init__(self, message: _Optional[str] = ..., message_type: _Optional[_Union[ClientMssg.MessageType, str]] = ...) -> None: ...

class ServerMssg(_message.Message):
    __slots__ = ("message", "message_type")
    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST: _ClassVar[ServerMssg.MessageType]
        REPLY: _ClassVar[ServerMssg.MessageType]
    REQUEST: ServerMssg.MessageType
    REPLY: ServerMssg.MessageType
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    message_type: ServerMssg.MessageType
    def __init__(self, message: _Optional[str] = ..., message_type: _Optional[_Union[ServerMssg.MessageType, str]] = ...) -> None: ...
