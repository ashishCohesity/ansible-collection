from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Default: _ClassVar[TestEnum]
    A: _ClassVar[TestEnum]
    B: _ClassVar[TestEnum]
    C: _ClassVar[TestEnum]
Default: TestEnum
A: TestEnum
B: TestEnum
C: TestEnum

class TestMessage(_message.Message):
    __slots__ = ("optional_int32", "optional_int64", "optional_uint32", "optional_uint64", "optional_bool", "optional_double", "optional_float", "optional_string", "optional_bytes", "optional_enum", "optional_msg", "repeated_int32", "repeated_int64", "repeated_uint32", "repeated_uint64", "repeated_bool", "repeated_double", "repeated_float", "repeated_string", "repeated_bytes", "repeated_enum", "repeated_msg", "oneof_int32", "oneof_int64", "oneof_uint32", "oneof_uint64", "oneof_bool", "oneof_double", "oneof_float", "oneof_string", "oneof_bytes", "oneof_enum", "oneof_msg", "map_int32_string", "map_int64_string", "map_uint32_string", "map_uint64_string", "map_bool_string", "map_string_string", "map_string_msg", "map_string_enum", "map_string_int32", "map_string_bool", "nested_message")
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
    class MapUint32StringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class MapUint64StringEntry(_message.Message):
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
    class MapStringStringEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapStringMsgEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestMessage, _Mapping]] = ...) -> None: ...
    class MapStringEnumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestEnum, str]] = ...) -> None: ...
    class MapStringInt32Entry(_message.Message):
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
    class NestedMessage(_message.Message):
        __slots__ = ("foo",)
        FOO_FIELD_NUMBER: _ClassVar[int]
        foo: int
        def __init__(self, foo: _Optional[int] = ...) -> None: ...
    OPTIONAL_INT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_INT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT32_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_UINT64_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BOOL_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_STRING_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ENUM_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_MSG_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT32_FIELD_NUMBER: _ClassVar[int]
    REPEATED_UINT64_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BOOL_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FLOAT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_STRING_FIELD_NUMBER: _ClassVar[int]
    REPEATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ENUM_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MSG_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_UINT64_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BOOL_FIELD_NUMBER: _ClassVar[int]
    ONEOF_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STRING_FIELD_NUMBER: _ClassVar[int]
    ONEOF_BYTES_FIELD_NUMBER: _ClassVar[int]
    ONEOF_ENUM_FIELD_NUMBER: _ClassVar[int]
    ONEOF_MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_INT32_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_INT64_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT32_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_UINT64_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_BOOL_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_STRING_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_ENUM_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_INT32_FIELD_NUMBER: _ClassVar[int]
    MAP_STRING_BOOL_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    optional_int32: int
    optional_int64: int
    optional_uint32: int
    optional_uint64: int
    optional_bool: bool
    optional_double: float
    optional_float: float
    optional_string: str
    optional_bytes: bytes
    optional_enum: TestEnum
    optional_msg: TestMessage
    repeated_int32: _containers.RepeatedScalarFieldContainer[int]
    repeated_int64: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint32: _containers.RepeatedScalarFieldContainer[int]
    repeated_uint64: _containers.RepeatedScalarFieldContainer[int]
    repeated_bool: _containers.RepeatedScalarFieldContainer[bool]
    repeated_double: _containers.RepeatedScalarFieldContainer[float]
    repeated_float: _containers.RepeatedScalarFieldContainer[float]
    repeated_string: _containers.RepeatedScalarFieldContainer[str]
    repeated_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    repeated_enum: _containers.RepeatedScalarFieldContainer[TestEnum]
    repeated_msg: _containers.RepeatedCompositeFieldContainer[TestMessage]
    oneof_int32: int
    oneof_int64: int
    oneof_uint32: int
    oneof_uint64: int
    oneof_bool: bool
    oneof_double: float
    oneof_float: float
    oneof_string: str
    oneof_bytes: bytes
    oneof_enum: TestEnum
    oneof_msg: TestMessage
    map_int32_string: _containers.ScalarMap[int, str]
    map_int64_string: _containers.ScalarMap[int, str]
    map_uint32_string: _containers.ScalarMap[int, str]
    map_uint64_string: _containers.ScalarMap[int, str]
    map_bool_string: _containers.ScalarMap[bool, str]
    map_string_string: _containers.ScalarMap[str, str]
    map_string_msg: _containers.MessageMap[str, TestMessage]
    map_string_enum: _containers.ScalarMap[str, TestEnum]
    map_string_int32: _containers.ScalarMap[str, int]
    map_string_bool: _containers.ScalarMap[str, bool]
    nested_message: TestMessage.NestedMessage
    def __init__(self, optional_int32: _Optional[int] = ..., optional_int64: _Optional[int] = ..., optional_uint32: _Optional[int] = ..., optional_uint64: _Optional[int] = ..., optional_bool: bool = ..., optional_double: _Optional[float] = ..., optional_float: _Optional[float] = ..., optional_string: _Optional[str] = ..., optional_bytes: _Optional[bytes] = ..., optional_enum: _Optional[_Union[TestEnum, str]] = ..., optional_msg: _Optional[_Union[TestMessage, _Mapping]] = ..., repeated_int32: _Optional[_Iterable[int]] = ..., repeated_int64: _Optional[_Iterable[int]] = ..., repeated_uint32: _Optional[_Iterable[int]] = ..., repeated_uint64: _Optional[_Iterable[int]] = ..., repeated_bool: _Optional[_Iterable[bool]] = ..., repeated_double: _Optional[_Iterable[float]] = ..., repeated_float: _Optional[_Iterable[float]] = ..., repeated_string: _Optional[_Iterable[str]] = ..., repeated_bytes: _Optional[_Iterable[bytes]] = ..., repeated_enum: _Optional[_Iterable[_Union[TestEnum, str]]] = ..., repeated_msg: _Optional[_Iterable[_Union[TestMessage, _Mapping]]] = ..., oneof_int32: _Optional[int] = ..., oneof_int64: _Optional[int] = ..., oneof_uint32: _Optional[int] = ..., oneof_uint64: _Optional[int] = ..., oneof_bool: bool = ..., oneof_double: _Optional[float] = ..., oneof_float: _Optional[float] = ..., oneof_string: _Optional[str] = ..., oneof_bytes: _Optional[bytes] = ..., oneof_enum: _Optional[_Union[TestEnum, str]] = ..., oneof_msg: _Optional[_Union[TestMessage, _Mapping]] = ..., map_int32_string: _Optional[_Mapping[int, str]] = ..., map_int64_string: _Optional[_Mapping[int, str]] = ..., map_uint32_string: _Optional[_Mapping[int, str]] = ..., map_uint64_string: _Optional[_Mapping[int, str]] = ..., map_bool_string: _Optional[_Mapping[bool, str]] = ..., map_string_string: _Optional[_Mapping[str, str]] = ..., map_string_msg: _Optional[_Mapping[str, TestMessage]] = ..., map_string_enum: _Optional[_Mapping[str, TestEnum]] = ..., map_string_int32: _Optional[_Mapping[str, int]] = ..., map_string_bool: _Optional[_Mapping[str, bool]] = ..., nested_message: _Optional[_Union[TestMessage.NestedMessage, _Mapping]] = ...) -> None: ...
