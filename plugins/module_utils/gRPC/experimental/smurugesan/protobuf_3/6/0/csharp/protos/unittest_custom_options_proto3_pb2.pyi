from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MethodOpt1(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METHODOPT1_UNSPECIFIED: _ClassVar[MethodOpt1]
    METHODOPT1_VAL1: _ClassVar[MethodOpt1]
    METHODOPT1_VAL2: _ClassVar[MethodOpt1]

class AggregateEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[AggregateEnum]
    VALUE: _ClassVar[AggregateEnum]
METHODOPT1_UNSPECIFIED: MethodOpt1
METHODOPT1_VAL1: MethodOpt1
METHODOPT1_VAL2: MethodOpt1
UNSPECIFIED: AggregateEnum
VALUE: AggregateEnum
FILE_OPT1_FIELD_NUMBER: _ClassVar[int]
file_opt1: _descriptor.FieldDescriptor
MESSAGE_OPT1_FIELD_NUMBER: _ClassVar[int]
message_opt1: _descriptor.FieldDescriptor
FIELD_OPT1_FIELD_NUMBER: _ClassVar[int]
field_opt1: _descriptor.FieldDescriptor
ONEOF_OPT1_FIELD_NUMBER: _ClassVar[int]
oneof_opt1: _descriptor.FieldDescriptor
ENUM_OPT1_FIELD_NUMBER: _ClassVar[int]
enum_opt1: _descriptor.FieldDescriptor
ENUM_VALUE_OPT1_FIELD_NUMBER: _ClassVar[int]
enum_value_opt1: _descriptor.FieldDescriptor
SERVICE_OPT1_FIELD_NUMBER: _ClassVar[int]
service_opt1: _descriptor.FieldDescriptor
METHOD_OPT1_FIELD_NUMBER: _ClassVar[int]
method_opt1: _descriptor.FieldDescriptor
BOOL_OPT_FIELD_NUMBER: _ClassVar[int]
bool_opt: _descriptor.FieldDescriptor
INT32_OPT_FIELD_NUMBER: _ClassVar[int]
int32_opt: _descriptor.FieldDescriptor
INT64_OPT_FIELD_NUMBER: _ClassVar[int]
int64_opt: _descriptor.FieldDescriptor
UINT32_OPT_FIELD_NUMBER: _ClassVar[int]
uint32_opt: _descriptor.FieldDescriptor
UINT64_OPT_FIELD_NUMBER: _ClassVar[int]
uint64_opt: _descriptor.FieldDescriptor
SINT32_OPT_FIELD_NUMBER: _ClassVar[int]
sint32_opt: _descriptor.FieldDescriptor
SINT64_OPT_FIELD_NUMBER: _ClassVar[int]
sint64_opt: _descriptor.FieldDescriptor
FIXED32_OPT_FIELD_NUMBER: _ClassVar[int]
fixed32_opt: _descriptor.FieldDescriptor
FIXED64_OPT_FIELD_NUMBER: _ClassVar[int]
fixed64_opt: _descriptor.FieldDescriptor
SFIXED32_OPT_FIELD_NUMBER: _ClassVar[int]
sfixed32_opt: _descriptor.FieldDescriptor
SFIXED64_OPT_FIELD_NUMBER: _ClassVar[int]
sfixed64_opt: _descriptor.FieldDescriptor
FLOAT_OPT_FIELD_NUMBER: _ClassVar[int]
float_opt: _descriptor.FieldDescriptor
DOUBLE_OPT_FIELD_NUMBER: _ClassVar[int]
double_opt: _descriptor.FieldDescriptor
STRING_OPT_FIELD_NUMBER: _ClassVar[int]
string_opt: _descriptor.FieldDescriptor
BYTES_OPT_FIELD_NUMBER: _ClassVar[int]
bytes_opt: _descriptor.FieldDescriptor
ENUM_OPT_FIELD_NUMBER: _ClassVar[int]
enum_opt: _descriptor.FieldDescriptor
MESSAGE_TYPE_OPT_FIELD_NUMBER: _ClassVar[int]
message_type_opt: _descriptor.FieldDescriptor
COMPLEX_OPT1_FIELD_NUMBER: _ClassVar[int]
complex_opt1: _descriptor.FieldDescriptor
COMPLEX_OPT2_FIELD_NUMBER: _ClassVar[int]
complex_opt2: _descriptor.FieldDescriptor
COMPLEX_OPT3_FIELD_NUMBER: _ClassVar[int]
complex_opt3: _descriptor.FieldDescriptor
FILEOPT_FIELD_NUMBER: _ClassVar[int]
fileopt: _descriptor.FieldDescriptor
MSGOPT_FIELD_NUMBER: _ClassVar[int]
msgopt: _descriptor.FieldDescriptor
FIELDOPT_FIELD_NUMBER: _ClassVar[int]
fieldopt: _descriptor.FieldDescriptor
ENUMOPT_FIELD_NUMBER: _ClassVar[int]
enumopt: _descriptor.FieldDescriptor
ENUMVALOPT_FIELD_NUMBER: _ClassVar[int]
enumvalopt: _descriptor.FieldDescriptor
SERVICEOPT_FIELD_NUMBER: _ClassVar[int]
serviceopt: _descriptor.FieldDescriptor
METHODOPT_FIELD_NUMBER: _ClassVar[int]
methodopt: _descriptor.FieldDescriptor

class TestMessageWithCustomOptions(_message.Message):
    __slots__ = ("field1", "oneof_field")
    class AnEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANENUM_UNSPECIFIED: _ClassVar[TestMessageWithCustomOptions.AnEnum]
        ANENUM_VAL1: _ClassVar[TestMessageWithCustomOptions.AnEnum]
        ANENUM_VAL2: _ClassVar[TestMessageWithCustomOptions.AnEnum]
    ANENUM_UNSPECIFIED: TestMessageWithCustomOptions.AnEnum
    ANENUM_VAL1: TestMessageWithCustomOptions.AnEnum
    ANENUM_VAL2: TestMessageWithCustomOptions.AnEnum
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIELD_FIELD_NUMBER: _ClassVar[int]
    field1: str
    oneof_field: int
    def __init__(self, field1: _Optional[str] = ..., oneof_field: _Optional[int] = ...) -> None: ...

class CustomOptionFooRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionFooResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionFooClientMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionFooServerMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DummyMessageContainingEnum(_message.Message):
    __slots__ = ()
    class TestEnumType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEST_OPTION_ENUM_UNSPECIFIED: _ClassVar[DummyMessageContainingEnum.TestEnumType]
        TEST_OPTION_ENUM_TYPE1: _ClassVar[DummyMessageContainingEnum.TestEnumType]
        TEST_OPTION_ENUM_TYPE2: _ClassVar[DummyMessageContainingEnum.TestEnumType]
    TEST_OPTION_ENUM_UNSPECIFIED: DummyMessageContainingEnum.TestEnumType
    TEST_OPTION_ENUM_TYPE1: DummyMessageContainingEnum.TestEnumType
    TEST_OPTION_ENUM_TYPE2: DummyMessageContainingEnum.TestEnumType
    def __init__(self) -> None: ...

class DummyMessageInvalidAsOptionType(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionMinIntegerValues(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionMaxIntegerValues(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomOptionOtherValues(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromPositiveInts(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingRealsFromNegativeInts(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ComplexOptionType1(_message.Message):
    __slots__ = ("foo", "foo2", "foo3", "foo4")
    FOO_FIELD_NUMBER: _ClassVar[int]
    FOO2_FIELD_NUMBER: _ClassVar[int]
    FOO3_FIELD_NUMBER: _ClassVar[int]
    FOO4_FIELD_NUMBER: _ClassVar[int]
    foo: int
    foo2: int
    foo3: int
    foo4: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, foo: _Optional[int] = ..., foo2: _Optional[int] = ..., foo3: _Optional[int] = ..., foo4: _Optional[_Iterable[int]] = ...) -> None: ...

class ComplexOptionType2(_message.Message):
    __slots__ = ("bar", "baz", "fred", "barney")
    class ComplexOptionType4(_message.Message):
        __slots__ = ("waldo",)
        COMPLEX_OPT4_FIELD_NUMBER: _ClassVar[int]
        complex_opt4: _descriptor.FieldDescriptor
        WALDO_FIELD_NUMBER: _ClassVar[int]
        waldo: int
        def __init__(self, waldo: _Optional[int] = ...) -> None: ...
    BAR_FIELD_NUMBER: _ClassVar[int]
    BAZ_FIELD_NUMBER: _ClassVar[int]
    FRED_FIELD_NUMBER: _ClassVar[int]
    BARNEY_FIELD_NUMBER: _ClassVar[int]
    bar: ComplexOptionType1
    baz: int
    fred: ComplexOptionType2.ComplexOptionType4
    barney: _containers.RepeatedCompositeFieldContainer[ComplexOptionType2.ComplexOptionType4]
    def __init__(self, bar: _Optional[_Union[ComplexOptionType1, _Mapping]] = ..., baz: _Optional[int] = ..., fred: _Optional[_Union[ComplexOptionType2.ComplexOptionType4, _Mapping]] = ..., barney: _Optional[_Iterable[_Union[ComplexOptionType2.ComplexOptionType4, _Mapping]]] = ...) -> None: ...

class ComplexOptionType3(_message.Message):
    __slots__ = ("qux",)
    QUX_FIELD_NUMBER: _ClassVar[int]
    qux: int
    def __init__(self, qux: _Optional[int] = ...) -> None: ...

class VariousComplexOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Aggregate(_message.Message):
    __slots__ = ("i", "s", "sub")
    I_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    i: int
    s: str
    sub: Aggregate
    def __init__(self, i: _Optional[int] = ..., s: _Optional[str] = ..., sub: _Optional[_Union[Aggregate, _Mapping]] = ...) -> None: ...

class AggregateMessage(_message.Message):
    __slots__ = ("fieldname",)
    FIELDNAME_FIELD_NUMBER: _ClassVar[int]
    fieldname: int
    def __init__(self, fieldname: _Optional[int] = ...) -> None: ...

class NestedOptionType(_message.Message):
    __slots__ = ()
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NestedOptionType.NestedEnum]
        NESTED_ENUM_VALUE: _ClassVar[NestedOptionType.NestedEnum]
    UNSPECIFIED: NestedOptionType.NestedEnum
    NESTED_ENUM_VALUE: NestedOptionType.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("nested_field",)
        NESTED_FIELD_FIELD_NUMBER: _ClassVar[int]
        nested_field: int
        def __init__(self, nested_field: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
