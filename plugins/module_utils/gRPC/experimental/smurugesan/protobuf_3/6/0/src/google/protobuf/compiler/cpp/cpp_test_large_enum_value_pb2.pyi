from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TestLargeEnumValue(_message.Message):
    __slots__ = ()
    class EnumWithLargeValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_1: _ClassVar[TestLargeEnumValue.EnumWithLargeValue]
        VALUE_MAX: _ClassVar[TestLargeEnumValue.EnumWithLargeValue]
    VALUE_1: TestLargeEnumValue.EnumWithLargeValue
    VALUE_MAX: TestLargeEnumValue.EnumWithLargeValue
    def __init__(self) -> None: ...
