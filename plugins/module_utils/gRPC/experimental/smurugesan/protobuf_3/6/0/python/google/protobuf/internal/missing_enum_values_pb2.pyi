from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnumValues(_message.Message):
    __slots__ = ("optional_nested_enum", "repeated_nested_enum", "packed_nested_enum")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZERO: _ClassVar[TestEnumValues.NestedEnum]
        ONE: _ClassVar[TestEnumValues.NestedEnum]
    ZERO: TestEnumValues.NestedEnum
    ONE: TestEnumValues.NestedEnum
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    PACKED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    optional_nested_enum: TestEnumValues.NestedEnum
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestEnumValues.NestedEnum]
    packed_nested_enum: _containers.RepeatedScalarFieldContainer[TestEnumValues.NestedEnum]
    def __init__(self, optional_nested_enum: _Optional[_Union[TestEnumValues.NestedEnum, str]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestEnumValues.NestedEnum, str]]] = ..., packed_nested_enum: _Optional[_Iterable[_Union[TestEnumValues.NestedEnum, str]]] = ...) -> None: ...

class TestMissingEnumValues(_message.Message):
    __slots__ = ("optional_nested_enum", "repeated_nested_enum", "packed_nested_enum")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TWO: _ClassVar[TestMissingEnumValues.NestedEnum]
    TWO: TestMissingEnumValues.NestedEnum
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    PACKED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    optional_nested_enum: TestMissingEnumValues.NestedEnum
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestMissingEnumValues.NestedEnum]
    packed_nested_enum: _containers.RepeatedScalarFieldContainer[TestMissingEnumValues.NestedEnum]
    def __init__(self, optional_nested_enum: _Optional[_Union[TestMissingEnumValues.NestedEnum, str]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestMissingEnumValues.NestedEnum, str]]] = ..., packed_nested_enum: _Optional[_Iterable[_Union[TestMissingEnumValues.NestedEnum, str]]] = ...) -> None: ...

class JustString(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: str
    def __init__(self, dummy: _Optional[str] = ...) -> None: ...
