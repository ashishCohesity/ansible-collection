from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Proto3Message(_message.Message):
    __slots__ = ("enum_value",)
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[Proto3Message.NestedEnum]
        BAR: _ClassVar[Proto3Message.NestedEnum]
        BAZ: _ClassVar[Proto3Message.NestedEnum]
    FOO: Proto3Message.NestedEnum
    BAR: Proto3Message.NestedEnum
    BAZ: Proto3Message.NestedEnum
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    enum_value: Proto3Message.NestedEnum
    def __init__(self, enum_value: _Optional[_Union[Proto3Message.NestedEnum, str]] = ...) -> None: ...
