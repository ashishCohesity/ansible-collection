from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Factory1Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FACTORY_1_VALUE_0: _ClassVar[Factory1Enum]
    FACTORY_1_VALUE_1: _ClassVar[Factory1Enum]
FACTORY_1_VALUE_0: Factory1Enum
FACTORY_1_VALUE_1: Factory1Enum

class Factory1Message(_message.Message):
    __slots__ = ("factory_1_enum", "nested_factory_1_enum", "nested_factory_1_message", "scalar_value", "list_value")
    class NestedFactory1Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NESTED_FACTORY_1_VALUE_0: _ClassVar[Factory1Message.NestedFactory1Enum]
        NESTED_FACTORY_1_VALUE_1: _ClassVar[Factory1Message.NestedFactory1Enum]
    NESTED_FACTORY_1_VALUE_0: Factory1Message.NestedFactory1Enum
    NESTED_FACTORY_1_VALUE_1: Factory1Message.NestedFactory1Enum
    class NestedFactory1Message(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    FACTORY_1_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_FACTORY_1_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_FACTORY_1_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCALAR_VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    factory_1_enum: Factory1Enum
    nested_factory_1_enum: Factory1Message.NestedFactory1Enum
    nested_factory_1_message: Factory1Message.NestedFactory1Message
    scalar_value: int
    list_value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, factory_1_enum: _Optional[_Union[Factory1Enum, str]] = ..., nested_factory_1_enum: _Optional[_Union[Factory1Message.NestedFactory1Enum, str]] = ..., nested_factory_1_message: _Optional[_Union[Factory1Message.NestedFactory1Message, _Mapping]] = ..., scalar_value: _Optional[int] = ..., list_value: _Optional[_Iterable[str]] = ...) -> None: ...
