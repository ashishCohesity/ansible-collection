from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestDescriptorsEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZERO: _ClassVar[TestDescriptorsEnum]
    ONE: _ClassVar[TestDescriptorsEnum]
ZERO: TestDescriptorsEnum
ONE: TestDescriptorsEnum

class TestDescriptorsMessage(_message.Message):
    __slots__ = ("optional_int32", "optional_enum", "optional_message", "repeated_int32", "repeated_message", "oneof_int32", "map_int32_enum")
    class EnumSub(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZERO: _ClassVar[TestDescriptorsMessage.EnumSub]
        ONE: _ClassVar[TestDescriptorsMessage.EnumSub]
    ZERO: TestDescriptorsMessage.EnumSub
    ONE: TestDescriptorsMessage.EnumSub
    class MapInt32EnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestDescriptorsMessage.EnumSub
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestDescriptorsMessage.EnumSub, str]] = ...) -> None: ...
    class Sub(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, a: _Optional[int] = ..., b: _Optional[_Iterable[int]] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_ENUM_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    optional_enum: TestDescriptorsEnum
    optional_message: TestDescriptorsMessage.Sub
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    repeated_message: _containers.RepeatedCompositeFieldContainer[TestDescriptorsMessage.Sub]
    oneof_int32: int
    map_int32_enum: _containers.ScalarMap[int, TestDescriptorsMessage.EnumSub]
    def __init__(self, optional_int32: _Optional[int] = ..., optional_enum: _Optional[_Union[TestDescriptorsEnum, str]] = ..., optional_message: _Optional[_Union[TestDescriptorsMessage.Sub, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_message: _Optional[_Iterable[_Union[TestDescriptorsMessage.Sub, _Mapping]]] = ..., oneof_int32: _Optional[int] = ..., map_int32_enum: _Optional[_Mapping[int, TestDescriptorsMessage.EnumSub]] = ...) -> None: ...
