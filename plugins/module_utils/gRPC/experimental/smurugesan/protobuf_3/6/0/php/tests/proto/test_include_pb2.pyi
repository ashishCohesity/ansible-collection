from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestInclude(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class TestLegacyMessage(_message.Message):
    __slots__ = ("message", "enum")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZERO: _ClassVar[TestLegacyMessage.NestedEnum]
    ZERO: TestLegacyMessage.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    message: TestLegacyMessage.NestedMessage
    enum: TestLegacyMessage.NestedEnum
    def __init__(self, message: _Optional[_Union[TestLegacyMessage.NestedMessage, _Mapping]] = ..., enum: _Optional[_Union[TestLegacyMessage.NestedEnum, str]] = ...) -> None: ...
