from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForeignEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOREIGN_FOO: _ClassVar[ForeignEnum]
    FOREIGN_BAR: _ClassVar[ForeignEnum]
    FOREIGN_BAZ: _ClassVar[ForeignEnum]

class MapValueEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAP_VALUE_FOO: _ClassVar[MapValueEnum]
    MAP_VALUE_BAR: _ClassVar[MapValueEnum]
    MAP_VALUE_BAZ: _ClassVar[MapValueEnum]
FOREIGN_FOO: ForeignEnum
FOREIGN_BAR: ForeignEnum
FOREIGN_BAZ: ForeignEnum
MAP_VALUE_FOO: MapValueEnum
MAP_VALUE_BAR: MapValueEnum
MAP_VALUE_BAZ: MapValueEnum
EXTEND_OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
extend_optional_int32: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
extend_optional_int64: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
extend_optional_uint32: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
extend_optional_uint64: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_SINT32_FIELD_NUMBER: _ClassVar[int]
extend_optional_sint32: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_SINT64_FIELD_NUMBER: _ClassVar[int]
extend_optional_sint64: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_FIXED32_FIELD_NUMBER: _ClassVar[int]
extend_optional_fixed32: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_FIXED64_FIELD_NUMBER: _ClassVar[int]
extend_optional_fixed64: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_SFIXED32_FIELD_NUMBER: _ClassVar[int]
extend_optional_sfixed32: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_SFIXED64_FIELD_NUMBER: _ClassVar[int]
extend_optional_sfixed64: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
extend_optional_float: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
extend_optional_double: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_BOOL_FIELD_NUMBER: _ClassVar[int]
extend_optional_bool: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
extend_optional_string: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
extend_optional_bytes: _descriptor.FieldDescriptor
EXTEND_OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
extend_optional_foreign_enum: _descriptor.FieldDescriptor
EXTEND_REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
extend_repeated_int32: _descriptor.FieldDescriptor
EXTEND_REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
extend_repeated_int64: _descriptor.FieldDescriptor
EXTEND_REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
extend_repeated_uint32: _descriptor.FieldDescriptor
EXTEND_REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
extend_repeated_uint64: _descriptor.FieldDescriptor
EXTEND_REPEATED_SINT32_FIELD_NUMBER: _ClassVar[int]
extend_repeated_sint32: _descriptor.FieldDescriptor
EXTEND_REPEATED_SINT64_FIELD_NUMBER: _ClassVar[int]
extend_repeated_sint64: _descriptor.FieldDescriptor
EXTEND_REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
extend_repeated_fixed32: _descriptor.FieldDescriptor
EXTEND_REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
extend_repeated_fixed64: _descriptor.FieldDescriptor
EXTEND_REPEATED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
extend_repeated_sfixed32: _descriptor.FieldDescriptor
EXTEND_REPEATED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
extend_repeated_sfixed64: _descriptor.FieldDescriptor
EXTEND_REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
extend_repeated_float: _descriptor.FieldDescriptor
EXTEND_REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
extend_repeated_double: _descriptor.FieldDescriptor
EXTEND_REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
extend_repeated_bool: _descriptor.FieldDescriptor
EXTEND_REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
extend_repeated_string: _descriptor.FieldDescriptor
EXTEND_REPEATED_BYTES_FIELD_NUMBER: _ClassVar[int]
extend_repeated_bytes: _descriptor.FieldDescriptor
EXTEND_REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
extend_repeated_foreign_enum: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_int32: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_int64: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_uint32: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_uint64: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_SINT32_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_sint32: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_SINT64_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_sint64: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_fixed32: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_fixed64: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_sfixed32: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_sfixed64: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_float: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_double: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_bool: _descriptor.FieldDescriptor
EXTEND_PACKED_REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
extend_packed_repeated_foreign_enum: _descriptor.FieldDescriptor

class TestAllTypes(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optionalgroup", "optional_foreign_message", "optional_foreign_enum", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeatedgroup", "repeated_foreign_message", "repeated_foreign_enum", "packed_repeated_int32", "packed_repeated_int64", "packed_repeated_uint32", "packed_repeated_uint64", "packed_repeated_sint32", "packed_repeated_sint64", "packed_repeated_fixed32", "packed_repeated_fixed64", "packed_repeated_sfixed32", "packed_repeated_sfixed64", "packed_repeated_float", "packed_repeated_double", "packed_repeated_bool", "oneof_uint32", "oneof_foreign_message", "oneof_string", "oneof_bytes")
    class OptionalGroup(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    class RepeatedGroup(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIXED32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIXED64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONALGROUP_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPEATEDGROUP_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_SINT32_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_SINT64_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_FIXED32_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_FIXED64_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    PACKED_REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    optional_int64: int
    optional_uint32: int
    optional_uint64: int
    optional_sint32: int
    optional_sint64: int
    optional_fixed32: int
    optional_fixed64: int
    optional_sfixed32: int
    optional_sfixed64: int
    optional_float: float
    optional_double: float
    optional_bool: bool
    optional_string: str
    optional_bytes: bytes
    optionalgroup: TestAllTypes.OptionalGroup
    optional_foreign_message: ForeignMessage
    optional_foreign_enum: ForeignEnum
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_sint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_sint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_fixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    repeated_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    repeated_float: _containers.RepeatedScalarFieldContainer[float]
    repeated_double: _containers.RepeatedScalarFieldContainer[float]
    repeated_bool: _containers.RepeatedScalarFieldContainer[bool]
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[TestAllTypes.RepeatedGroup]
    repeated_foreign_message: _containers.RepeatedCompositeFieldContainer[ForeignMessage]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnum]
    packed_repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_int64: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_uint32: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_uint64: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_sint32: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_sint64: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_fixed32: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_fixed64: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_sfixed32: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_sfixed64: _containers.RepeatedScalarFieldContainer[int]
    packed_repeated_float: _containers.RepeatedScalarFieldContainer[float]
    packed_repeated_double: _containers.RepeatedScalarFieldContainer[float]
    packed_repeated_bool: _containers.RepeatedScalarFieldContainer[bool]
    oneof_uint32: int
    oneof_foreign_message: ForeignMessage
    oneof_string: str
    oneof_bytes: bytes
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optionalgroup: _Optional[_Union[TestAllTypes.OptionalGroup, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnum, str]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeatedgroup: _Optional[_Iterable[_Union[TestAllTypes.RepeatedGroup, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessage, _Mapping]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnum, str]]] = ..., packed_repeated_int32: _Optional[_Iterable[int]] = ..., packed_repeated_int64: _Optional[_Iterable[int]] = ..., packed_repeated_uint32: _Optional[_Iterable[int]] = ..., packed_repeated_uint64: _Optional[_Iterable[int]] = ..., packed_repeated_sint32: _Optional[_Iterable[int]] = ..., packed_repeated_sint64: _Optional[_Iterable[int]] = ..., packed_repeated_fixed32: _Optional[_Iterable[int]] = ..., packed_repeated_fixed64: _Optional[_Iterable[int]] = ..., packed_repeated_sfixed32: _Optional[_Iterable[int]] = ..., packed_repeated_sfixed64: _Optional[_Iterable[int]] = ..., packed_repeated_float: _Optional[_Iterable[float]] = ..., packed_repeated_double: _Optional[_Iterable[float]] = ..., packed_repeated_bool: _Optional[_Iterable[bool]] = ..., oneof_uint32: _Optional[int] = ..., oneof_foreign_message: _Optional[_Union[ForeignMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ...) -> None: ...

class ForeignMessage(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class TestExtendable(_message.Message):
    __slots__ = ()
    Extensions: _python_message._ExtensionDict
    def __init__(self) -> None: ...

class ExtendsWithMessage(_message.Message):
    __slots__ = ("foo",)
    OPTIONAL_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    optional_extension: _descriptor.FieldDescriptor
    REPEATED_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    repeated_extension: _descriptor.FieldDescriptor
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: int
    def __init__(self, foo: _Optional[int] = ...) -> None: ...

class TestMapFields(_message.Message):
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
        value: MapValueEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapValueEnum, str]] = ...) -> None: ...
    class MapStringMsgEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapValueMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapValueMessage, _Mapping]] = ...) -> None: ...
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
        value: TestMapFields
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestMapFields, _Mapping]] = ...) -> None: ...
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
    map_string_enum: _containers.ScalarMap[str, MapValueEnum]
    map_string_msg: _containers.MessageMap[str, MapValueMessage]
    map_int32_string: _containers.ScalarMap[int, str]
    map_int64_string: _containers.ScalarMap[int, str]
    map_bool_string: _containers.ScalarMap[bool, str]
    test_map_fields: TestMapFields
    map_string_testmapfields: _containers.MessageMap[str, TestMapFields]
    def __init__(self, map_string_string: _Optional[_Mapping[str, str]] = ..., map_string_int32: _Optional[_Mapping[str, int]] = ..., map_string_int64: _Optional[_Mapping[str, int]] = ..., map_string_bool: _Optional[_Mapping[str, bool]] = ..., map_string_double: _Optional[_Mapping[str, float]] = ..., map_string_enum: _Optional[_Mapping[str, MapValueEnum]] = ..., map_string_msg: _Optional[_Mapping[str, MapValueMessage]] = ..., map_int32_string: _Optional[_Mapping[int, str]] = ..., map_int64_string: _Optional[_Mapping[int, str]] = ..., map_bool_string: _Optional[_Mapping[bool, str]] = ..., test_map_fields: _Optional[_Union[TestMapFields, _Mapping]] = ..., map_string_testmapfields: _Optional[_Mapping[str, TestMapFields]] = ...) -> None: ...

class MapValueMessage(_message.Message):
    __slots__ = ("foo",)
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: int
    def __init__(self, foo: _Optional[int] = ...) -> None: ...
