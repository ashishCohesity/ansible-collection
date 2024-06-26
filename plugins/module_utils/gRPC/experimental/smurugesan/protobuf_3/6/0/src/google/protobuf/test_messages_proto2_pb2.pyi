from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForeignEnumProto2(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOREIGN_FOO: _ClassVar[ForeignEnumProto2]
    FOREIGN_BAR: _ClassVar[ForeignEnumProto2]
    FOREIGN_BAZ: _ClassVar[ForeignEnumProto2]
FOREIGN_FOO: ForeignEnumProto2
FOREIGN_BAR: ForeignEnumProto2
FOREIGN_BAZ: ForeignEnumProto2
EXTENSION_INT32_FIELD_NUMBER: _ClassVar[int]
extension_int32: _descriptor.FieldDescriptor

class TestAllTypesProto2(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_nested_message", "optional_foreign_message", "optional_nested_enum", "optional_foreign_enum", "optional_string_piece", "optional_cord", "recursive_message", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeated_nested_message", "repeated_foreign_message", "repeated_nested_enum", "repeated_foreign_enum", "repeated_string_piece", "repeated_cord", "map_int32_int32", "map_int64_int64", "map_uint32_uint32", "map_uint64_uint64", "map_sint32_sint32", "map_sint64_sint64", "map_fixed32_fixed32", "map_fixed64_fixed64", "map_sfixed32_sfixed32", "map_sfixed64_sfixed64", "map_int32_float", "map_int32_double", "map_bool_bool", "map_string_string", "map_string_bytes", "map_string_nested_message", "map_string_foreign_message", "map_string_nested_enum", "map_string_foreign_enum", "oneof_uint32", "oneof_nested_message", "oneof_string", "oneof_bytes", "oneof_bool", "oneof_uint64", "oneof_float", "oneof_double", "oneof_enum", "data", "fieldname1", "field_name2", "_field_name3", "field__name4_", "field0name5", "field_0_name6", "fieldName7", "FieldName8", "field_Name9", "Field_Name10", "FIELD_NAME11", "FIELD_name12", "__field_name13", "__Field_name14", "field__name15", "field__Name16", "field_name17__", "Field_name18__")
    Extensions: _python_message._ExtensionDict
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestAllTypesProto2.NestedEnum]
        BAR: _ClassVar[TestAllTypesProto2.NestedEnum]
        BAZ: _ClassVar[TestAllTypesProto2.NestedEnum]
        NEG: _ClassVar[TestAllTypesProto2.NestedEnum]
    FOO: TestAllTypesProto2.NestedEnum
    BAR: TestAllTypesProto2.NestedEnum
    BAZ: TestAllTypesProto2.NestedEnum
    NEG: TestAllTypesProto2.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("a", "corecursive")
        A_FIELD_NUMBER: _ClassVar[int]
        CORECURSIVE_FIELD_NUMBER: _ClassVar[int]
        a: int
        corecursive: TestAllTypesProto2
        def __init__(self, a: _Optional[int] = ..., corecursive: _Optional[_Union[TestAllTypesProto2, _Mapping]] = ...) -> None: ...
    class MapInt32Int32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapInt64Int64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapUint32Uint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapUint64Uint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSint32Sint32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSint64Sint64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapFixed32Fixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapFixed64Fixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSfixed32Sfixed32Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapSfixed64Sfixed64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapInt32FloatEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class MapInt32DoubleEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class MapBoolBoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: bool
        def __init__(self, key: bool = ..., value: bool = ...) -> None: ...
    class MapStringStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapStringBytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapStringNestedMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestAllTypesProto2.NestedMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestAllTypesProto2.NestedMessage, _Mapping]] = ...) -> None: ...
    class MapStringForeignMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ForeignMessageProto2
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ForeignMessageProto2, _Mapping]] = ...) -> None: ...
    class MapStringNestedEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestAllTypesProto2.NestedEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestAllTypesProto2.NestedEnum, str]] = ...) -> None: ...
    class MapStringForeignEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ForeignEnumProto2
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ForeignEnumProto2, str]] = ...) -> None: ...
    class Data(_message.Message):
        __slots__ = ("group_int32", "group_uint32")
        GROUP_INT32_FIELD_NUMBER: _ClassVar[int]
        GROUP_UINT32_FIELD_NUMBER: _ClassVar[int]
        group_int32: int
        group_uint32: int
        def __init__(self, group_int32: _Optional[int] = ..., group_uint32: _Optional[int] = ...) -> None: ...
    class MessageSetCorrect(_message.Message):
        __slots__ = ()
        Extensions: _python_message._ExtensionDict
        def __init__(self) -> None: ...
    class MessageSetCorrectExtension1(_message.Message):
        __slots__ = ("str",)
        MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        message_set_extension: _descriptor.FieldDescriptor
        STR_FIELD_NUMBER: _ClassVar[int]
        str: str
        def __init__(self, str: _Optional[str] = ...) -> None: ...
    class MessageSetCorrectExtension2(_message.Message):
        __slots__ = ("i",)
        MESSAGE_SET_EXTENSION_FIELD_NUMBER: _ClassVar[int]
        message_set_extension: _descriptor.FieldDescriptor
        I_FIELD_NUMBER: _ClassVar[int]
        i: int
        def __init__(self, i: _Optional[int] = ...) -> None: ...
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
    OPTIONAL_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CORD_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_PIECE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_CORD_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_INT32_FIELD_NUMBER: _ClassVar[int]
    MAP_INT64_INT64_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT32_UINT32_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT64_UINT64_FIELD_NUMBER: _ClassVar[int]
    MAP_SINT32_SINT32_FIELD_NUMBER: _ClassVar[int]
    MAP_SINT64_SINT64_FIELD_NUMBER: _ClassVar[int]
    MAP_FIXED32_FIXED32_FIELD_NUMBER: _ClassVar[int]
    MAP_FIXED64_FIXED64_FIELD_NUMBER: _ClassVar[int]
    MAP_SFIXED32_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    MAP_SFIXED64_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_FLOAT_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    MAP_BOOL_BOOL_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_FOREIGN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_FOREIGN_ENUM_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BOOL_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ONEOF_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME1_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME2_FIELD_NUMBER: _ClassVar[int]
    _FIELD_NAME3_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME4__FIELD_NUMBER: _ClassVar[int]
    FIELD0NAME5_FIELD_NUMBER: _ClassVar[int]
    FIELD_0_NAME6_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME7_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME8_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME9_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME10_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME11_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME12_FIELD_NUMBER: _ClassVar[int]
    __FIELD_NAME13_FIELD_NUMBER: _ClassVar[int]
    __FIELD_NAME14_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME15_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME16_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME17___FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME18___FIELD_NUMBER: _ClassVar[int]
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
    optional_nested_message: TestAllTypesProto2.NestedMessage
    optional_foreign_message: ForeignMessageProto2
    optional_nested_enum: TestAllTypesProto2.NestedEnum
    optional_foreign_enum: ForeignEnumProto2
    optional_string_piece: str
    optional_cord: str
    recursive_message: TestAllTypesProto2
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
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypesProto2.NestedMessage]
    repeated_foreign_message: _containers.RepeatedCompositeFieldContainer[ForeignMessageProto2]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypesProto2.NestedEnum]
    repeated_foreign_enum: _containers.RepeatedScalarFieldContainer[ForeignEnumProto2]
    repeated_string_piece: _containers.RepeatedScalarFieldContainer[str]
    repeated_cord: _containers.RepeatedScalarFieldContainer[str]
    map_int32_int32: _containers.ScalarMap[int, int]
    map_int64_int64: _containers.ScalarMap[int, int]
    map_uint32_uint32: _containers.ScalarMap[int, int]
    map_uint64_uint64: _containers.ScalarMap[int, int]
    map_sint32_sint32: _containers.ScalarMap[int, int]
    map_sint64_sint64: _containers.ScalarMap[int, int]
    map_fixed32_fixed32: _containers.ScalarMap[int, int]
    map_fixed64_fixed64: _containers.ScalarMap[int, int]
    map_sfixed32_sfixed32: _containers.ScalarMap[int, int]
    map_sfixed64_sfixed64: _containers.ScalarMap[int, int]
    map_int32_float: _containers.ScalarMap[int, float]
    map_int32_double: _containers.ScalarMap[int, float]
    map_bool_bool: _containers.ScalarMap[bool, bool]
    map_string_string: _containers.ScalarMap[str, str]
    map_string_bytes: _containers.ScalarMap[str, bytes]
    map_string_nested_message: _containers.MessageMap[str, TestAllTypesProto2.NestedMessage]
    map_string_foreign_message: _containers.MessageMap[str, ForeignMessageProto2]
    map_string_nested_enum: _containers.ScalarMap[str, TestAllTypesProto2.NestedEnum]
    map_string_foreign_enum: _containers.ScalarMap[str, ForeignEnumProto2]
    oneof_uint32: int
    oneof_nested_message: TestAllTypesProto2.NestedMessage
    oneof_string: str
    oneof_bytes: bytes
    oneof_bool: bool
    oneof_uint64: int
    oneof_float: float
    oneof_double: float
    oneof_enum: TestAllTypesProto2.NestedEnum
    data: TestAllTypesProto2.Data
    fieldname1: int
    field_name2: int
    _field_name3: int
    field__name4_: int
    field0name5: int
    field_0_name6: int
    fieldName7: int
    FieldName8: int
    field_Name9: int
    Field_Name10: int
    FIELD_NAME11: int
    FIELD_name12: int
    __field_name13: int
    __Field_name14: int
    field__name15: int
    field__Name16: int
    field_name17__: int
    Field_name18__: int
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_nested_message: _Optional[_Union[TestAllTypesProto2.NestedMessage, _Mapping]] = ..., optional_foreign_message: _Optional[_Union[ForeignMessageProto2, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypesProto2.NestedEnum, str]] = ..., optional_foreign_enum: _Optional[_Union[ForeignEnumProto2, str]] = ..., optional_string_piece: _Optional[str] = ..., optional_cord: _Optional[str] = ..., recursive_message: _Optional[_Union[TestAllTypesProto2, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypesProto2.NestedMessage, _Mapping]]] = ..., repeated_foreign_message: _Optional[_Iterable[_Union[ForeignMessageProto2, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypesProto2.NestedEnum, str]]] = ..., repeated_foreign_enum: _Optional[_Iterable[_Union[ForeignEnumProto2, str]]] = ..., repeated_string_piece: _Optional[_Iterable[str]] = ..., repeated_cord: _Optional[_Iterable[str]] = ..., map_int32_int32: _Optional[_Mapping[int, int]] = ..., map_int64_int64: _Optional[_Mapping[int, int]] = ..., map_uint32_uint32: _Optional[_Mapping[int, int]] = ..., map_uint64_uint64: _Optional[_Mapping[int, int]] = ..., map_sint32_sint32: _Optional[_Mapping[int, int]] = ..., map_sint64_sint64: _Optional[_Mapping[int, int]] = ..., map_fixed32_fixed32: _Optional[_Mapping[int, int]] = ..., map_fixed64_fixed64: _Optional[_Mapping[int, int]] = ..., map_sfixed32_sfixed32: _Optional[_Mapping[int, int]] = ..., map_sfixed64_sfixed64: _Optional[_Mapping[int, int]] = ..., map_int32_float: _Optional[_Mapping[int, float]] = ..., map_int32_double: _Optional[_Mapping[int, float]] = ..., map_bool_bool: _Optional[_Mapping[bool, bool]] = ..., map_string_string: _Optional[_Mapping[str, str]] = ..., map_string_bytes: _Optional[_Mapping[str, bytes]] = ..., map_string_nested_message: _Optional[_Mapping[str, TestAllTypesProto2.NestedMessage]] = ..., map_string_foreign_message: _Optional[_Mapping[str, ForeignMessageProto2]] = ..., map_string_nested_enum: _Optional[_Mapping[str, TestAllTypesProto2.NestedEnum]] = ..., map_string_foreign_enum: _Optional[_Mapping[str, ForeignEnumProto2]] = ..., oneof_uint32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypesProto2.NestedMessage, _Mapping]] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneof_bool: bool = ..., oneof_uint64: _Optional[int] = ..., oneof_float: _Optional[float] = ..., oneof_double: _Optional[float] = ..., oneof_enum: _Optional[_Union[TestAllTypesProto2.NestedEnum, str]] = ..., data: _Optional[_Union[TestAllTypesProto2.Data, _Mapping]] = ..., fieldname1: _Optional[int] = ..., field_name2: _Optional[int] = ..., _field_name3: _Optional[int] = ..., field__name4_: _Optional[int] = ..., field0name5: _Optional[int] = ..., field_0_name6: _Optional[int] = ..., fieldName7: _Optional[int] = ..., FieldName8: _Optional[int] = ..., field_Name9: _Optional[int] = ..., Field_Name10: _Optional[int] = ..., FIELD_NAME11: _Optional[int] = ..., FIELD_name12: _Optional[int] = ..., __field_name13: _Optional[int] = ..., __Field_name14: _Optional[int] = ..., field__name15: _Optional[int] = ..., field__Name16: _Optional[int] = ..., field_name17__: _Optional[int] = ..., Field_name18__: _Optional[int] = ...) -> None: ...

class ForeignMessageProto2(_message.Message):
    __slots__ = ("c",)
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...
