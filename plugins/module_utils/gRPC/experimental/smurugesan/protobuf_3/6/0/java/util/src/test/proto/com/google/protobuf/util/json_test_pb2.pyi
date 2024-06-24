from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestAllTypes(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optional_nested_message", "optional_nested_enum", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeated_nested_message", "repeated_nested_enum")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[TestAllTypes.NestedEnum]
        BAR: _ClassVar[TestAllTypes.NestedEnum]
        BAZ: _ClassVar[TestAllTypes.NestedEnum]
    FOO: TestAllTypes.NestedEnum
    BAR: TestAllTypes.NestedEnum
    BAZ: TestAllTypes.NestedEnum
    class NestedMessage(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
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
    OPTIONAL_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    REPEATED_NESTED_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    optional_nested_message: TestAllTypes.NestedMessage
    optional_nested_enum: TestAllTypes.NestedEnum
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
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[TestAllTypes.NestedMessage]
    repeated_nested_enum: _containers.RepeatedScalarFieldContainer[TestAllTypes.NestedEnum]
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., optional_nested_enum: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[TestAllTypes.NestedMessage, _Mapping]]] = ..., repeated_nested_enum: _Optional[_Iterable[_Union[TestAllTypes.NestedEnum, str]]] = ...) -> None: ...

class TestOneof(_message.Message):
    __slots__ = ("oneof_int32", "oneof_nested_message", "oneof_null_value")
    ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    oneof_int32: int
    oneof_nested_message: TestAllTypes.NestedMessage
    oneof_null_value: _struct_pb2.NullValue
    def __init__(self, oneof_int32: _Optional[int] = ..., oneof_nested_message: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ..., oneof_null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ...) -> None: ...

class TestMap(_message.Message):
    __slots__ = ("int32_to_int32_map", "int64_to_int32_map", "uint32_to_int32_map", "uint64_to_int32_map", "sint32_to_int32_map", "sint64_to_int32_map", "fixed32_to_int32_map", "fixed64_to_int32_map", "sfixed32_to_int32_map", "sfixed64_to_int32_map", "bool_to_int32_map", "string_to_int32_map", "int32_to_int64_map", "int32_to_uint32_map", "int32_to_uint64_map", "int32_to_sint32_map", "int32_to_sint64_map", "int32_to_fixed32_map", "int32_to_fixed64_map", "int32_to_sfixed32_map", "int32_to_sfixed64_map", "int32_to_float_map", "int32_to_double_map", "int32_to_bool_map", "int32_to_string_map", "int32_to_bytes_map", "int32_to_message_map", "int32_to_enum_map")
    class Int32ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int64ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint32ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Uint64ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Sint32ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Sint64ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Fixed32ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Fixed64ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Sfixed32ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Sfixed64ToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class BoolToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: int
        def __init__(self, key: bool = ..., value: _Optional[int] = ...) -> None: ...
    class StringToInt32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToInt64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToUint32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToUint64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToSint32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToSint64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToFixed32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToFixed64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToSfixed32MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToSfixed64MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class Int32ToFloatMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class Int32ToDoubleMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    class Int32ToBoolMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class Int32ToStringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Int32ToBytesMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class Int32ToMessageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestAllTypes.NestedMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestAllTypes.NestedMessage, _Mapping]] = ...) -> None: ...
    class Int32ToEnumMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TestAllTypes.NestedEnum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TestAllTypes.NestedEnum, str]] = ...) -> None: ...
    INT32_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT64_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    UINT32_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    UINT64_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    SINT32_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    SINT64_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    FIXED32_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    FIXED64_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    SFIXED32_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    SFIXED64_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    BOOL_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_INT64_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_UINT32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_UINT64_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_SINT32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_SINT64_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_FIXED32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_FIXED64_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_SFIXED32_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_SFIXED64_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_FLOAT_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_DOUBLE_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_BOOL_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_BYTES_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_MESSAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    INT32_TO_ENUM_MAP_FIELD_NUMBER: _ClassVar[int]
    int32_to_int32_map: _containers.ScalarMap[int, int]
    int64_to_int32_map: _containers.ScalarMap[int, int]
    uint32_to_int32_map: _containers.ScalarMap[int, int]
    uint64_to_int32_map: _containers.ScalarMap[int, int]
    sint32_to_int32_map: _containers.ScalarMap[int, int]
    sint64_to_int32_map: _containers.ScalarMap[int, int]
    fixed32_to_int32_map: _containers.ScalarMap[int, int]
    fixed64_to_int32_map: _containers.ScalarMap[int, int]
    sfixed32_to_int32_map: _containers.ScalarMap[int, int]
    sfixed64_to_int32_map: _containers.ScalarMap[int, int]
    bool_to_int32_map: _containers.ScalarMap[bool, int]
    string_to_int32_map: _containers.ScalarMap[str, int]
    int32_to_int64_map: _containers.ScalarMap[int, int]
    int32_to_uint32_map: _containers.ScalarMap[int, int]
    int32_to_uint64_map: _containers.ScalarMap[int, int]
    int32_to_sint32_map: _containers.ScalarMap[int, int]
    int32_to_sint64_map: _containers.ScalarMap[int, int]
    int32_to_fixed32_map: _containers.ScalarMap[int, int]
    int32_to_fixed64_map: _containers.ScalarMap[int, int]
    int32_to_sfixed32_map: _containers.ScalarMap[int, int]
    int32_to_sfixed64_map: _containers.ScalarMap[int, int]
    int32_to_float_map: _containers.ScalarMap[int, float]
    int32_to_double_map: _containers.ScalarMap[int, float]
    int32_to_bool_map: _containers.ScalarMap[int, bool]
    int32_to_string_map: _containers.ScalarMap[int, str]
    int32_to_bytes_map: _containers.ScalarMap[int, bytes]
    int32_to_message_map: _containers.MessageMap[int, TestAllTypes.NestedMessage]
    int32_to_enum_map: _containers.ScalarMap[int, TestAllTypes.NestedEnum]
    def __init__(self, int32_to_int32_map: _Optional[_Mapping[int, int]] = ..., int64_to_int32_map: _Optional[_Mapping[int, int]] = ..., uint32_to_int32_map: _Optional[_Mapping[int, int]] = ..., uint64_to_int32_map: _Optional[_Mapping[int, int]] = ..., sint32_to_int32_map: _Optional[_Mapping[int, int]] = ..., sint64_to_int32_map: _Optional[_Mapping[int, int]] = ..., fixed32_to_int32_map: _Optional[_Mapping[int, int]] = ..., fixed64_to_int32_map: _Optional[_Mapping[int, int]] = ..., sfixed32_to_int32_map: _Optional[_Mapping[int, int]] = ..., sfixed64_to_int32_map: _Optional[_Mapping[int, int]] = ..., bool_to_int32_map: _Optional[_Mapping[bool, int]] = ..., string_to_int32_map: _Optional[_Mapping[str, int]] = ..., int32_to_int64_map: _Optional[_Mapping[int, int]] = ..., int32_to_uint32_map: _Optional[_Mapping[int, int]] = ..., int32_to_uint64_map: _Optional[_Mapping[int, int]] = ..., int32_to_sint32_map: _Optional[_Mapping[int, int]] = ..., int32_to_sint64_map: _Optional[_Mapping[int, int]] = ..., int32_to_fixed32_map: _Optional[_Mapping[int, int]] = ..., int32_to_fixed64_map: _Optional[_Mapping[int, int]] = ..., int32_to_sfixed32_map: _Optional[_Mapping[int, int]] = ..., int32_to_sfixed64_map: _Optional[_Mapping[int, int]] = ..., int32_to_float_map: _Optional[_Mapping[int, float]] = ..., int32_to_double_map: _Optional[_Mapping[int, float]] = ..., int32_to_bool_map: _Optional[_Mapping[int, bool]] = ..., int32_to_string_map: _Optional[_Mapping[int, str]] = ..., int32_to_bytes_map: _Optional[_Mapping[int, bytes]] = ..., int32_to_message_map: _Optional[_Mapping[int, TestAllTypes.NestedMessage]] = ..., int32_to_enum_map: _Optional[_Mapping[int, TestAllTypes.NestedEnum]] = ...) -> None: ...

class TestWrappers(_message.Message):
    __slots__ = ("int32_value", "uint32_value", "int64_value", "uint64_value", "float_value", "double_value", "bool_value", "string_value", "bytes_value")
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    int32_value: _wrappers_pb2.Int32Value
    uint32_value: _wrappers_pb2.UInt32Value
    int64_value: _wrappers_pb2.Int64Value
    uint64_value: _wrappers_pb2.UInt64Value
    float_value: _wrappers_pb2.FloatValue
    double_value: _wrappers_pb2.DoubleValue
    bool_value: _wrappers_pb2.BoolValue
    string_value: _wrappers_pb2.StringValue
    bytes_value: _wrappers_pb2.BytesValue
    def __init__(self, int32_value: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., uint32_value: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., int64_value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., uint64_value: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., float_value: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., double_value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., bool_value: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., string_value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., bytes_value: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class TestTimestamp(_message.Message):
    __slots__ = ("timestamp_value",)
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp_value: _timestamp_pb2.Timestamp
    def __init__(self, timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TestDuration(_message.Message):
    __slots__ = ("duration_value",)
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    duration_value: _duration_pb2.Duration
    def __init__(self, duration_value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TestFieldMask(_message.Message):
    __slots__ = ("field_mask_value",)
    FIELD_MASK_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_mask_value: _field_mask_pb2.FieldMask
    def __init__(self, field_mask_value: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class TestStruct(_message.Message):
    __slots__ = ("struct_value", "value", "list_value")
    STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    struct_value: _struct_pb2.Struct
    value: _struct_pb2.Value
    list_value: _struct_pb2.ListValue
    def __init__(self, struct_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., list_value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class TestAny(_message.Message):
    __slots__ = ("any_value", "any_map")
    class AnyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    ANY_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANY_MAP_FIELD_NUMBER: _ClassVar[int]
    any_value: _any_pb2.Any
    any_map: _containers.MessageMap[str, _any_pb2.Any]
    def __init__(self, any_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., any_map: _Optional[_Mapping[str, _any_pb2.Any]] = ...) -> None: ...

class TestCustomJsonName(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class TestRecursive(_message.Message):
    __slots__ = ("value", "nested")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    value: int
    nested: TestRecursive
    def __init__(self, value: _Optional[int] = ..., nested: _Optional[_Union[TestRecursive, _Mapping]] = ...) -> None: ...
