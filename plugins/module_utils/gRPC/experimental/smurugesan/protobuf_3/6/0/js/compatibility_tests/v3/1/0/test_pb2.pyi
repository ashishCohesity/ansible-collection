from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OuterEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOO: _ClassVar[OuterEnum]
    BAR: _ClassVar[OuterEnum]

class MapValueEnumNoBinary(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAP_VALUE_FOO_NOBINARY: _ClassVar[MapValueEnumNoBinary]
    MAP_VALUE_BAR_NOBINARY: _ClassVar[MapValueEnumNoBinary]
    MAP_VALUE_BAZ_NOBINARY: _ClassVar[MapValueEnumNoBinary]
FOO: OuterEnum
BAR: OuterEnum
MAP_VALUE_FOO_NOBINARY: MapValueEnumNoBinary
MAP_VALUE_BAR_NOBINARY: MapValueEnumNoBinary
MAP_VALUE_BAZ_NOBINARY: MapValueEnumNoBinary
SIMPLE1_FIELD_NUMBER: _ClassVar[int]
simple1: _descriptor.FieldDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnumContainer(_message.Message):
    __slots__ = ("outer_enum",)
    OUTER_ENUM_FIELD_NUMBER: _ClassVar[int]
    outer_enum: OuterEnum
    def __init__(self, outer_enum: _Optional[_Union[OuterEnum, str]] = ...) -> None: ...

class Simple1(_message.Message):
    __slots__ = ("a_string", "a_repeated_string", "a_boolean")
    A_STRING_FIELD_NUMBER: _ClassVar[int]
    A_REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    A_BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    a_string: str
    a_repeated_string: _containers.RepeatedScalarFieldContainer[str]
    a_boolean: bool
    def __init__(self, a_string: _Optional[str] = ..., a_repeated_string: _Optional[_Iterable[str]] = ..., a_boolean: bool = ...) -> None: ...

class Simple2(_message.Message):
    __slots__ = ("a_string", "a_repeated_string")
    A_STRING_FIELD_NUMBER: _ClassVar[int]
    A_REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    a_string: str
    a_repeated_string: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, a_string: _Optional[str] = ..., a_repeated_string: _Optional[_Iterable[str]] = ...) -> None: ...

class SpecialCases(_message.Message):
    __slots__ = ("normal", "default", "function", "var")
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    normal: str
    default: str
    function: str
    var: str
    def __init__(self, normal: _Optional[str] = ..., default: _Optional[str] = ..., function: _Optional[str] = ..., var: _Optional[str] = ...) -> None: ...

class OptionalFields(_message.Message):
    __slots__ = ("a_string", "a_bool", "a_nested_message", "a_repeated_message", "a_repeated_string")
    class Nested(_message.Message):
        __slots__ = ("an_int",)
        AN_INT_FIELD_NUMBER: _ClassVar[int]
        an_int: int
        def __init__(self, an_int: _Optional[int] = ...) -> None: ...
    A_STRING_FIELD_NUMBER: _ClassVar[int]
    A_BOOL_FIELD_NUMBER: _ClassVar[int]
    A_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    A_REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    A_REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    a_string: str
    a_bool: bool
    a_nested_message: OptionalFields.Nested
    a_repeated_message: _containers.RepeatedCompositeFieldContainer[OptionalFields.Nested]
    a_repeated_string: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, a_string: _Optional[str] = ..., a_bool: bool = ..., a_nested_message: _Optional[_Union[OptionalFields.Nested, _Mapping]] = ..., a_repeated_message: _Optional[_Iterable[_Union[OptionalFields.Nested, _Mapping]]] = ..., a_repeated_string: _Optional[_Iterable[str]] = ...) -> None: ...

class HasExtensions(_message.Message):
    __slots__ = ("str1", "str2", "str3")
    Extensions: _python_message._ExtensionDict
    STR1_FIELD_NUMBER: _ClassVar[int]
    STR2_FIELD_NUMBER: _ClassVar[int]
    STR3_FIELD_NUMBER: _ClassVar[int]
    str1: str
    str2: str
    str3: str
    def __init__(self, str1: _Optional[str] = ..., str2: _Optional[str] = ..., str3: _Optional[str] = ...) -> None: ...

class Complex(_message.Message):
    __slots__ = ("a_string", "an_out_of_order_bool", "a_nested_message", "a_repeated_message", "a_repeated_string")
    class Nested(_message.Message):
        __slots__ = ("an_int",)
        AN_INT_FIELD_NUMBER: _ClassVar[int]
        an_int: int
        def __init__(self, an_int: _Optional[int] = ...) -> None: ...
    A_STRING_FIELD_NUMBER: _ClassVar[int]
    AN_OUT_OF_ORDER_BOOL_FIELD_NUMBER: _ClassVar[int]
    A_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    A_REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    A_REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    a_string: str
    an_out_of_order_bool: bool
    a_nested_message: Complex.Nested
    a_repeated_message: _containers.RepeatedCompositeFieldContainer[Complex.Nested]
    a_repeated_string: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, a_string: _Optional[str] = ..., an_out_of_order_bool: bool = ..., a_nested_message: _Optional[_Union[Complex.Nested, _Mapping]] = ..., a_repeated_message: _Optional[_Iterable[_Union[Complex.Nested, _Mapping]]] = ..., a_repeated_string: _Optional[_Iterable[str]] = ...) -> None: ...

class OuterMessage(_message.Message):
    __slots__ = ()
    class Complex(_message.Message):
        __slots__ = ("inner_complex_field",)
        INNER_COMPLEX_FIELD_FIELD_NUMBER: _ClassVar[int]
        inner_complex_field: int
        def __init__(self, inner_complex_field: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class IsExtension(_message.Message):
    __slots__ = ("ext1",)
    EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ext_field: _descriptor.FieldDescriptor
    SIMPLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    simple_option: _descriptor.FieldDescriptor
    EXT1_FIELD_NUMBER: _ClassVar[int]
    ext1: str
    def __init__(self, ext1: _Optional[str] = ...) -> None: ...

class IndirectExtension(_message.Message):
    __slots__ = ()
    SIMPLE_FIELD_NUMBER: _ClassVar[int]
    simple: _descriptor.FieldDescriptor
    STR_FIELD_NUMBER: _ClassVar[int]
    str: _descriptor.FieldDescriptor
    REPEATED_STR_FIELD_NUMBER: _ClassVar[int]
    repeated_str: _descriptor.FieldDescriptor
    REPEATED_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    repeated_simple: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class DefaultValues(_message.Message):
    __slots__ = ("string_field", "bool_field", "int_field", "enum_field", "empty_field", "bytes_field")
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        E1: _ClassVar[DefaultValues.Enum]
        E2: _ClassVar[DefaultValues.Enum]
    E1: DefaultValues.Enum
    E2: DefaultValues.Enum
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    string_field: str
    bool_field: bool
    int_field: int
    enum_field: DefaultValues.Enum
    empty_field: str
    bytes_field: bytes
    def __init__(self, string_field: _Optional[str] = ..., bool_field: bool = ..., int_field: _Optional[int] = ..., enum_field: _Optional[_Union[DefaultValues.Enum, str]] = ..., empty_field: _Optional[str] = ..., bytes_field: _Optional[bytes] = ...) -> None: ...

class FloatingPointFields(_message.Message):
    __slots__ = ("optional_float_field", "required_float_field", "repeated_float_field", "default_float_field", "optional_double_field", "required_double_field", "repeated_double_field", "default_double_field")
    OPTIONAL_FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    optional_float_field: float
    required_float_field: float
    repeated_float_field: _containers.RepeatedScalarFieldContainer[float]
    default_float_field: float
    optional_double_field: float
    required_double_field: float
    repeated_double_field: _containers.RepeatedScalarFieldContainer[float]
    default_double_field: float
    def __init__(self, optional_float_field: _Optional[float] = ..., required_float_field: _Optional[float] = ..., repeated_float_field: _Optional[_Iterable[float]] = ..., default_float_field: _Optional[float] = ..., optional_double_field: _Optional[float] = ..., required_double_field: _Optional[float] = ..., repeated_double_field: _Optional[_Iterable[float]] = ..., default_double_field: _Optional[float] = ...) -> None: ...

class TestClone(_message.Message):
    __slots__ = ("str", "simple1", "simple2", "bytes_field", "unused")
    Extensions: _python_message._ExtensionDict
    STR_FIELD_NUMBER: _ClassVar[int]
    SIMPLE1_FIELD_NUMBER: _ClassVar[int]
    SIMPLE2_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    UNUSED_FIELD_NUMBER: _ClassVar[int]
    str: str
    simple1: Simple1
    simple2: _containers.RepeatedCompositeFieldContainer[Simple1]
    bytes_field: bytes
    unused: str
    def __init__(self, str: _Optional[str] = ..., simple1: _Optional[_Union[Simple1, _Mapping]] = ..., simple2: _Optional[_Iterable[_Union[Simple1, _Mapping]]] = ..., bytes_field: _Optional[bytes] = ..., unused: _Optional[str] = ...) -> None: ...

class CloneExtension(_message.Message):
    __slots__ = ("ext",)
    EXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    ext_field: _descriptor.FieldDescriptor
    EXT_FIELD_NUMBER: _ClassVar[int]
    ext: str
    def __init__(self, ext: _Optional[str] = ...) -> None: ...

class TestGroup(_message.Message):
    __slots__ = ("repeatedgroup", "requiredgroup", "optionalgroup", "id", "required_simple", "optional_simple")
    class RepeatedGroup(_message.Message):
        __slots__ = ("id", "some_bool")
        ID_FIELD_NUMBER: _ClassVar[int]
        SOME_BOOL_FIELD_NUMBER: _ClassVar[int]
        id: str
        some_bool: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, id: _Optional[str] = ..., some_bool: _Optional[_Iterable[bool]] = ...) -> None: ...
    class RequiredGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class OptionalGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    REQUIREDGROUP_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestGroup.RepeatedGroup]
    requiredgroup: TestGroup.RequiredGroup
    optionalgroup: TestGroup.OptionalGroup
    id: str
    required_simple: Simple2
    optional_simple: Simple2
    def __init__(self, repeatedgroup: _Optional[_Iterable[_Union[TestGroup.RepeatedGroup, _Mapping]]] = ..., requiredgroup: _Optional[_Union[TestGroup.RequiredGroup, _Mapping]] = ..., optionalgroup: _Optional[_Union[TestGroup.OptionalGroup, _Mapping]] = ..., id: _Optional[str] = ..., required_simple: _Optional[_Union[Simple2, _Mapping]] = ..., optional_simple: _Optional[_Union[Simple2, _Mapping]] = ...) -> None: ...

class TestGroup1(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: TestGroup.RepeatedGroup
    def __init__(self, group: _Optional[_Union[TestGroup.RepeatedGroup, _Mapping]] = ...) -> None: ...

class TestReservedNames(_message.Message):
    __slots__ = ("extension",)
    Extensions: _python_message._ExtensionDict
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    extension: int
    def __init__(self, extension: _Optional[int] = ...) -> None: ...

class TestReservedNamesExtension(_message.Message):
    __slots__ = ()
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...

class TestMessageWithOneof(_message.Message):
    __slots__ = ("pone", "pthree", "rone", "rtwo", "normal_field", "repeated_field", "aone", "atwo", "bone", "btwo")
    PONE_FIELD_NUMBER: _ClassVar[int]
    PTHREE_FIELD_NUMBER: _ClassVar[int]
    RONE_FIELD_NUMBER: _ClassVar[int]
    RTWO_FIELD_NUMBER: _ClassVar[int]
    NORMAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIELD_FIELD_NUMBER: _ClassVar[int]
    AONE_FIELD_NUMBER: _ClassVar[int]
    ATWO_FIELD_NUMBER: _ClassVar[int]
    BONE_FIELD_NUMBER: _ClassVar[int]
    BTWO_FIELD_NUMBER: _ClassVar[int]
    pone: str
    pthree: str
    rone: TestMessageWithOneof
    rtwo: str
    normal_field: bool
    repeated_field: _containers.RepeatedScalarFieldContainer[str]
    aone: int
    atwo: int
    bone: int
    btwo: int
    def __init__(self, pone: _Optional[str] = ..., pthree: _Optional[str] = ..., rone: _Optional[_Union[TestMessageWithOneof, _Mapping]] = ..., rtwo: _Optional[str] = ..., normal_field: bool = ..., repeated_field: _Optional[_Iterable[str]] = ..., aone: _Optional[int] = ..., atwo: _Optional[int] = ..., bone: _Optional[int] = ..., btwo: _Optional[int] = ...) -> None: ...

class TestEndsWithBytes(_message.Message):
    __slots__ = ("value", "data")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    value: int
    data: bytes
    def __init__(self, value: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class TestMapFieldsNoBinary(_message.Message):
    __slots__ = ("map_string_string", "map_string_int32", "map_string_int64", "map_string_bool", "map_string_double", "map_string_enum", "map_string_msg", "map_int32_string", "map_int64_string", "map_bool_string", "test_map_fields", "map_string_testmapfields")
    class MapStringStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapStringInt32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class MapStringInt64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class MapStringBoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class MapStringDoubleEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    class MapStringEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapValueEnumNoBinary
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapValueEnumNoBinary, str]] = ...) -> None: ...
    class MapStringMsgEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapValueMessageNoBinary
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapValueMessageNoBinary, _Mapping]] = ...) -> None: ...
    class MapInt32StringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class MapInt64StringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class MapBoolStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    class MapStringTestmapfieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestMapFieldsNoBinary
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestMapFieldsNoBinary, _Mapping]] = ...) -> None: ...
    MAP_STRING_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_INT32_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_INT64_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_BOOL_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_INT64_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_BOOL_STRING_FIELD_NUMBER: _ClassVar[int]
    TEST_MAP_FIELDS_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_TESTMAPFIELDS_FIELD_NUMBER: _ClassVar[int]
    map_string_string: _containers.ScalarMap[str, str]
    map_string_int32: _containers.ScalarMap[str, int]
    map_string_int64: _containers.ScalarMap[str, int]
    map_string_bool: _containers.ScalarMap[str, bool]
    map_string_double: _containers.ScalarMap[str, float]
    map_string_enum: _containers.ScalarMap[str, MapValueEnumNoBinary]
    map_string_msg: _containers.MessageMap[str, MapValueMessageNoBinary]
    map_int32_string: _containers.ScalarMap[int, str]
    map_int64_string: _containers.ScalarMap[int, str]
    map_bool_string: _containers.ScalarMap[bool, str]
    test_map_fields: TestMapFieldsNoBinary
    map_string_testmapfields: _containers.MessageMap[str, TestMapFieldsNoBinary]
    def __init__(self, map_string_string: _Optional[_Mapping[str, str]] = ..., map_string_int32: _Optional[_Mapping[str, int]] = ..., map_string_int64: _Optional[_Mapping[str, int]] = ..., map_string_bool: _Optional[_Mapping[str, bool]] = ..., map_string_double: _Optional[_Mapping[str, float]] = ..., map_string_enum: _Optional[_Mapping[str, MapValueEnumNoBinary]] = ..., map_string_msg: _Optional[_Mapping[str, MapValueMessageNoBinary]] = ..., map_int32_string: _Optional[_Mapping[int, str]] = ..., map_int64_string: _Optional[_Mapping[int, str]] = ..., map_bool_string: _Optional[_Mapping[bool, str]] = ..., test_map_fields: _Optional[_Union[TestMapFieldsNoBinary, _Mapping]] = ..., map_string_testmapfields: _Optional[_Mapping[str, TestMapFieldsNoBinary]] = ...) -> None: ...

class MapValueMessageNoBinary(_message.Message):
    __slots__ = ("foo",)
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: int
    def __init__(self, foo: _Optional[int] = ...) -> None: ...
