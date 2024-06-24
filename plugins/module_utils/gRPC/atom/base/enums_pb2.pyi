from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class JournalReaderType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kContinuousJournalReader: _ClassVar[JournalReaderType.Type]
        kShardedJournalReader: _ClassVar[JournalReaderType.Type]
    kContinuousJournalReader: JournalReaderType.Type
    kShardedJournalReader: JournalReaderType.Type
    def __init__(self) -> None: ...
