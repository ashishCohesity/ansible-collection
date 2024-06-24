from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEmptyNamespace(_message.Message):
    __slots__ = ("a", "nested_message", "nested_enum")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZERO: _ClassVar[TestEmptyNamespace.NestedEnum]
    ZERO: TestEmptyNamespace.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    a: int
    nested_message: TestEmptyNamespace.NestedMessage
    nested_enum: TestEmptyNamespace.NestedEnum
    def __init__(self, a: _Optional[int] = ..., nested_message: _Optional[_Union[TestEmptyNamespace.NestedMessage, _Mapping]] = ..., nested_enum: _Optional[_Union[TestEmptyNamespace.NestedEnum, str]] = ...) -> None: ...
