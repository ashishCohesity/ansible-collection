from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NegativeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEGATIVE_ENUM_ZERO: _ClassVar[NegativeEnum]
    FiveBelow: _ClassVar[NegativeEnum]
    MinusOne: _ClassVar[NegativeEnum]

class DeprecatedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPRECATED_ZERO: _ClassVar[DeprecatedEnum]
    one: _ClassVar[DeprecatedEnum]
NEGATIVE_ENUM_ZERO: NegativeEnum
FiveBelow: NegativeEnum
MinusOne: NegativeEnum
DEPRECATED_ZERO: DeprecatedEnum
one: DeprecatedEnum

class Issue307(_message.Message):
    __slots__ = ()
    class NestedOnce(_message.Message):
        __slots__ = ()
        class NestedTwice(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class NegativeEnumMessage(_message.Message):
    __slots__ = ("value", "values", "packed_values")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    PACKED_VALUES_FIELD_NUMBER: _ClassVar[int]
    value: NegativeEnum
    values: _containers.RepeatedScalarFieldContainer[NegativeEnum]
    packed_values: _containers.RepeatedScalarFieldContainer[NegativeEnum]
    def __init__(self, value: _Optional[_Union[NegativeEnum, str]] = ..., values: _Optional[_Iterable[_Union[NegativeEnum, str]]] = ..., packed_values: _Optional[_Iterable[_Union[NegativeEnum, str]]] = ...) -> None: ...

class DeprecatedChild(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeprecatedFieldsMessage(_message.Message):
    __slots__ = ("PrimitiveValue", "PrimitiveArray", "MessageValue", "MessageArray", "EnumValue", "EnumArray")
    PRIMITIVEVALUE_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVEARRAY_FIELD_NUMBER: _ClassVar[int]
    MESSAGEVALUE_FIELD_NUMBER: _ClassVar[int]
    MESSAGEARRAY_FIELD_NUMBER: _ClassVar[int]
    ENUMVALUE_FIELD_NUMBER: _ClassVar[int]
    ENUMARRAY_FIELD_NUMBER: _ClassVar[int]
    PrimitiveValue: int
    PrimitiveArray: _containers.RepeatedScalarFieldContainer[int]
    MessageValue: DeprecatedChild
    MessageArray: _containers.RepeatedCompositeFieldContainer[DeprecatedChild]
    EnumValue: DeprecatedEnum
    EnumArray: _containers.RepeatedScalarFieldContainer[DeprecatedEnum]
    def __init__(self, PrimitiveValue: _Optional[int] = ..., PrimitiveArray: _Optional[_Iterable[int]] = ..., MessageValue: _Optional[_Union[DeprecatedChild, _Mapping]] = ..., MessageArray: _Optional[_Iterable[_Union[DeprecatedChild, _Mapping]]] = ..., EnumValue: _Optional[_Union[DeprecatedEnum, str]] = ..., EnumArray: _Optional[_Iterable[_Union[DeprecatedEnum, str]]] = ...) -> None: ...

class ItemField(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: int
    def __init__(self, item: _Optional[int] = ...) -> None: ...

class ReservedNames(_message.Message):
    __slots__ = ("types", "descriptor")
    class SomeNestedType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    TYPES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    types: int
    descriptor: int
    def __init__(self, types: _Optional[int] = ..., descriptor: _Optional[int] = ...) -> None: ...

class TestJsonFieldOrdering(_message.Message):
    __slots__ = ("plain_int32", "o1_string", "o1_int32", "plain_string", "o2_int32", "o2_string")
    PLAIN_INT32_FIELD_NUMBER: _ClassVar[int]
    O1_STRING_FIELD_NUMBER: _ClassVar[int]
    O1_INT32_FIELD_NUMBER: _ClassVar[int]
    PLAIN_STRING_FIELD_NUMBER: _ClassVar[int]
    O2_INT32_FIELD_NUMBER: _ClassVar[int]
    O2_STRING_FIELD_NUMBER: _ClassVar[int]
    plain_int32: int
    o1_string: str
    o1_int32: int
    plain_string: str
    o2_int32: int
    o2_string: str
    def __init__(self, plain_int32: _Optional[int] = ..., o1_string: _Optional[str] = ..., o1_int32: _Optional[int] = ..., plain_string: _Optional[str] = ..., o2_int32: _Optional[int] = ..., o2_string: _Optional[str] = ...) -> None: ...

class TestJsonName(_message.Message):
    __slots__ = ("name", "description", "guid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    guid: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., guid: _Optional[str] = ...) -> None: ...

class OneofMerging(_message.Message):
    __slots__ = ("text", "nested")
    class Nested(_message.Message):
        __slots__ = ("x", "y")
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        x: int
        y: int
        def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    text: str
    nested: OneofMerging.Nested
    def __init__(self, text: _Optional[str] = ..., nested: _Optional[_Union[OneofMerging.Nested, _Mapping]] = ...) -> None: ...
