from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message2(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_sint32", "optional_sint64", "optional_fixed32", "optional_fixed64", "optional_sfixed32", "optional_sfixed64", "optional_float", "optional_double", "optional_bool", "optional_string", "optional_bytes", "optionalgroup", "optional_message", "optional_enum", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_sint32", "repeated_sint64", "repeated_fixed32", "repeated_fixed64", "repeated_sfixed32", "repeated_sfixed64", "repeated_float", "repeated_double", "repeated_bool", "repeated_string", "repeated_bytes", "repeatedgroup", "repeated_message", "repeated_enum", "oneof_int32", "oneof_int64", "oneof_uint32", "oneof_uint64", "oneof_sint32", "oneof_sint64", "oneof_fixed32", "oneof_fixed64", "oneof_sfixed32", "oneof_sfixed64", "oneof_float", "oneof_double", "oneof_bool", "oneof_string", "oneof_bytes", "oneofgroup", "oneof_message", "oneof_enum", "map_int32_int32", "map_int64_int64", "map_uint32_uint32", "map_uint64_uint64", "map_sint32_sint32", "map_sint64_sint64", "map_fixed32_fixed32", "map_fixed64_fixed64", "map_sfixed32_sfixed32", "map_sfixed64_sfixed64", "map_int32_float", "map_int32_double", "map_bool_bool", "map_string_string", "map_string_bytes", "map_string_message", "map_int32_bytes", "map_int32_enum", "map_int32_message")
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FOO: _ClassVar[Message2.Enum]
        BAR: _ClassVar[Message2.Enum]
        BAZ: _ClassVar[Message2.Enum]
        EXTRA_2: _ClassVar[Message2.Enum]
    FOO: Message2.Enum
    BAR: Message2.Enum
    BAZ: Message2.Enum
    EXTRA_2: Message2.Enum
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
    class OneofGroup(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: int
        def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
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
    class MapStringMessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Message2
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Message2, _Mapping]] = ...) -> None: ...
    class MapInt32BytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bytes
        def __init__(self, key: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapInt32EnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Message2.Enum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Message2.Enum, str]] = ...) -> None: ...
    class MapInt32MessageEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Message2
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Message2, _Mapping]] = ...) -> None: ...
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
    OPTIONAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ENUM_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_SINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_SINT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIXED32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIXED64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_SFIXED32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ONEOF_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BOOL_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOFGROUP_FIELD_NUMBER: _ClassVar[int]
    ONEOF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_FIELD_NUMBER: _ClassVar[int]
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
    MAP_STRING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_MESSAGE_FIELD_NUMBER: _ClassVar[int]
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
    optionalgroup: Message2.OptionalGroup
    optional_message: Message2
    optional_enum: Message2.Enum
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
    repeatedgroup: _containers.RepeatedCompositeFieldContainer[Message2.RepeatedGroup]
    repeated_message: _containers.RepeatedCompositeFieldContainer[Message2]
    repeated_enum: _containers.RepeatedScalarFieldContainer[Message2.Enum]
    oneof_int32: int
    oneof_int64: int
    oneof_uint32: int
    oneof_uint64: int
    oneof_sint32: int
    oneof_sint64: int
    oneof_fixed32: int
    oneof_fixed64: int
    oneof_sfixed32: int
    oneof_sfixed64: int
    oneof_float: float
    oneof_double: float
    oneof_bool: bool
    oneof_string: str
    oneof_bytes: bytes
    oneofgroup: Message2.OneofGroup
    oneof_message: Message2
    oneof_enum: Message2.Enum
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
    map_string_message: _containers.MessageMap[str, Message2]
    map_int32_bytes: _containers.ScalarMap[int, bytes]
    map_int32_enum: _containers.ScalarMap[int, Message2.Enum]
    map_int32_message: _containers.MessageMap[int, Message2]
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_sint32: _Optional[int] = ..., optional_sint64: _Optional[int] = ..., optional_fixed32: _Optional[int] = ..., optional_fixed64: _Optional[int] = ..., optional_sfixed32: _Optional[int] = ..., optional_sfixed64: _Optional[int] = ..., optional_float: _Optional[float] = ..., optional_double: _Optional[float] = ..., optional_bool: bool = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optionalgroup: _Optional[_Union[Message2.OptionalGroup, _Mapping]] = ..., optional_message: _Optional[_Union[Message2, _Mapping]] = ..., optional_enum: _Optional[_Union[Message2.Enum, str]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_sint32: _Optional[_Iterable[int]] = ..., repeated_sint64: _Optional[_Iterable[int]] = ..., repeated_fixed32: _Optional[_Iterable[int]] = ..., repeated_fixed64: _Optional[_Iterable[int]] = ..., repeated_sfixed32: _Optional[_Iterable[int]] = ..., repeated_sfixed64: _Optional[_Iterable[int]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeatedgroup: _Optional[_Iterable[_Union[Message2.RepeatedGroup, _Mapping]]] = ..., repeated_message: _Optional[_Iterable[_Union[Message2, _Mapping]]] = ..., repeated_enum: _Optional[_Iterable[_Union[Message2.Enum, str]]] = ..., oneof_int32: _Optional[int] = ..., oneof_int64: _Optional[int] = ..., oneof_uint32: _Optional[int] = ..., oneof_uint64: _Optional[int] = ..., oneof_sint32: _Optional[int] = ..., oneof_sint64: _Optional[int] = ..., oneof_fixed32: _Optional[int] = ..., oneof_fixed64: _Optional[int] = ..., oneof_sfixed32: _Optional[int] = ..., oneof_sfixed64: _Optional[int] = ..., oneof_float: _Optional[float] = ..., oneof_double: _Optional[float] = ..., oneof_bool: bool = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneofgroup: _Optional[_Union[Message2.OneofGroup, _Mapping]] = ..., oneof_message: _Optional[_Union[Message2, _Mapping]] = ..., oneof_enum: _Optional[_Union[Message2.Enum, str]] = ..., map_int32_int32: _Optional[_Mapping[int, int]] = ..., map_int64_int64: _Optional[_Mapping[int, int]] = ..., map_uint32_uint32: _Optional[_Mapping[int, int]] = ..., map_uint64_uint64: _Optional[_Mapping[int, int]] = ..., map_sint32_sint32: _Optional[_Mapping[int, int]] = ..., map_sint64_sint64: _Optional[_Mapping[int, int]] = ..., map_fixed32_fixed32: _Optional[_Mapping[int, int]] = ..., map_fixed64_fixed64: _Optional[_Mapping[int, int]] = ..., map_sfixed32_sfixed32: _Optional[_Mapping[int, int]] = ..., map_sfixed64_sfixed64: _Optional[_Mapping[int, int]] = ..., map_int32_float: _Optional[_Mapping[int, float]] = ..., map_int32_double: _Optional[_Mapping[int, float]] = ..., map_bool_bool: _Optional[_Mapping[bool, bool]] = ..., map_string_string: _Optional[_Mapping[str, str]] = ..., map_string_bytes: _Optional[_Mapping[str, bytes]] = ..., map_string_message: _Optional[_Mapping[str, Message2]] = ..., map_int32_bytes: _Optional[_Mapping[int, bytes]] = ..., map_int32_enum: _Optional[_Mapping[int, Message2.Enum]] = ..., map_int32_message: _Optional[_Mapping[int, Message2]] = ...) -> None: ...
