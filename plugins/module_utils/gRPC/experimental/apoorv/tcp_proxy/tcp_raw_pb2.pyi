from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chunk(_message.Message):
    __slots__ = ("data", "uuid", "message_type", "sequence")
    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST: _ClassVar[Chunk.MessageType]
        REPLY: _ClassVar[Chunk.MessageType]
        FINISH: _ClassVar[Chunk.MessageType]
    REQUEST: Chunk.MessageType
    REPLY: Chunk.MessageType
    FINISH: Chunk.MessageType
    DATA_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    uuid: str
    message_type: Chunk.MessageType
    sequence: int
    def __init__(self, data: _Optional[bytes] = ..., uuid: _Optional[str] = ..., message_type: _Optional[_Union[Chunk.MessageType, str]] = ..., sequence: _Optional[int] = ...) -> None: ...
