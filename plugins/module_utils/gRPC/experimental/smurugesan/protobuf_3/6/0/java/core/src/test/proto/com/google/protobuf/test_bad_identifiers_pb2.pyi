from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMessage(_message.Message):
    __slots__ = ("cached_size", "serialized_size")
    CACHED_SIZE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    cached_size: str
    serialized_size: str
    def __init__(self, cached_size: _Optional[str] = ..., serialized_size: _Optional[str] = ..., **kwargs) -> None: ...

class Descriptor(_message.Message):
    __slots__ = ("descriptor", "nested_descriptor")
    class NestedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Descriptor.NestedEnum]
        FOO: _ClassVar[Descriptor.NestedEnum]
    UNKNOWN: Descriptor.NestedEnum
    FOO: Descriptor.NestedEnum
    class NestedDescriptor(_message.Message):
        __slots__ = ("descriptor",)
        DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        descriptor: str
        def __init__(self, descriptor: _Optional[str] = ...) -> None: ...
    DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    NESTED_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    descriptor: str
    nested_descriptor: Descriptor.NestedDescriptor
    def __init__(self, descriptor: _Optional[str] = ..., nested_descriptor: _Optional[_Union[Descriptor.NestedDescriptor, _Mapping]] = ...) -> None: ...

class Parser(_message.Message):
    __slots__ = ("parser",)
    class ParserEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Parser.ParserEnum]
        PARSER: _ClassVar[Parser.ParserEnum]
    UNKNOWN: Parser.ParserEnum
    PARSER: Parser.ParserEnum
    PARSER_FIELD_NUMBER: _ClassVar[int]
    parser: Parser.ParserEnum
    def __init__(self, parser: _Optional[_Union[Parser.ParserEnum, str]] = ...) -> None: ...

class Deprecated(_message.Message):
    __slots__ = ("field1", "field2", "field3")
    class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Deprecated.TestEnum]
        FOO: _ClassVar[Deprecated.TestEnum]
        BAR: _ClassVar[Deprecated.TestEnum]
    UNKNOWN: Deprecated.TestEnum
    FOO: Deprecated.TestEnum
    BAR: Deprecated.TestEnum
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    field1: int
    field2: Deprecated.TestEnum
    field3: TestMessage
    def __init__(self, field1: _Optional[int] = ..., field2: _Optional[_Union[Deprecated.TestEnum, str]] = ..., field3: _Optional[_Union[TestMessage, _Mapping]] = ...) -> None: ...

class Override(_message.Message):
    __slots__ = ("override",)
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    override: int
    def __init__(self, override: _Optional[int] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ("object", "string_object")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    STRING_OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: int
    string_object: str
    def __init__(self, object: _Optional[int] = ..., string_object: _Optional[str] = ...) -> None: ...

class String(_message.Message):
    __slots__ = ("string",)
    STRING_FIELD_NUMBER: _ClassVar[int]
    string: str
    def __init__(self, string: _Optional[str] = ...) -> None: ...

class Integer(_message.Message):
    __slots__ = ("integer",)
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    integer: int
    def __init__(self, integer: _Optional[int] = ...) -> None: ...

class Long(_message.Message):
    __slots__ = ("long",)
    LONG_FIELD_NUMBER: _ClassVar[int]
    long: int
    def __init__(self, long: _Optional[int] = ...) -> None: ...

class Float(_message.Message):
    __slots__ = ("float",)
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    float: float
    def __init__(self, float: _Optional[float] = ...) -> None: ...

class Double(_message.Message):
    __slots__ = ("double",)
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    double: float
    def __init__(self, double: _Optional[float] = ...) -> None: ...

class TestConflictingFieldNames(_message.Message):
    __slots__ = ("int32_field", "enum_field", "string_field", "bytes_field", "message_field", "int32_field_count", "enum_field_count", "string_field_count", "bytes_field_count", "message_field_count", "Int32Field", "EnumField", "StringField", "BytesField", "MessageField", "int32_field_list", "field_name", "field__name", "_2conflict", "__2conflict", "int64_field")
    Extensions: _python_message._ExtensionDict
    class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[TestConflictingFieldNames.TestEnum]
        FOO: _ClassVar[TestConflictingFieldNames.TestEnum]
    UNKNOWN: TestConflictingFieldNames.TestEnum
    FOO: TestConflictingFieldNames.TestEnum
    class TestMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    INT64_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    int64_field_count: _descriptor.FieldDescriptor
    INT64_FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    int64_field_list: _descriptor.FieldDescriptor
    INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_COUNT_FIELD_NUMBER: _ClassVar[int]
    INT32FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUMFIELD_FIELD_NUMBER: _ClassVar[int]
    STRINGFIELD_FIELD_NUMBER: _ClassVar[int]
    BYTESFIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGEFIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD__NAME_FIELD_NUMBER: _ClassVar[int]
    _2CONFLICT_FIELD_NUMBER: _ClassVar[int]
    __2CONFLICT_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    int32_field: _containers.RepeatedScalarFieldContainer[int]
    enum_field: _containers.RepeatedScalarFieldContainer[TestConflictingFieldNames.TestEnum]
    string_field: _containers.RepeatedScalarFieldContainer[str]
    bytes_field: _containers.RepeatedScalarFieldContainer[bytes]
    message_field: _containers.RepeatedCompositeFieldContainer[TestConflictingFieldNames.TestMessage]
    int32_field_count: int
    enum_field_count: TestConflictingFieldNames.TestEnum
    string_field_count: str
    bytes_field_count: bytes
    message_field_count: TestConflictingFieldNames.TestMessage
    Int32Field: _containers.RepeatedScalarFieldContainer[int]
    EnumField: _containers.RepeatedScalarFieldContainer[TestConflictingFieldNames.TestEnum]
    StringField: _containers.RepeatedScalarFieldContainer[str]
    BytesField: _containers.RepeatedScalarFieldContainer[bytes]
    MessageField: _containers.RepeatedCompositeFieldContainer[TestConflictingFieldNames.TestMessage]
    int32_field_list: int
    field_name: str
    field__name: str
    _2conflict: int
    __2conflict: int
    int64_field: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, int32_field: _Optional[_Iterable[int]] = ..., enum_field: _Optional[_Iterable[_Union[TestConflictingFieldNames.TestEnum, str]]] = ..., string_field: _Optional[_Iterable[str]] = ..., bytes_field: _Optional[_Iterable[bytes]] = ..., message_field: _Optional[_Iterable[_Union[TestConflictingFieldNames.TestMessage, _Mapping]]] = ..., int32_field_count: _Optional[int] = ..., enum_field_count: _Optional[_Union[TestConflictingFieldNames.TestEnum, str]] = ..., string_field_count: _Optional[str] = ..., bytes_field_count: _Optional[bytes] = ..., message_field_count: _Optional[_Union[TestConflictingFieldNames.TestMessage, _Mapping]] = ..., Int32Field: _Optional[_Iterable[int]] = ..., EnumField: _Optional[_Iterable[_Union[TestConflictingFieldNames.TestEnum, str]]] = ..., StringField: _Optional[_Iterable[str]] = ..., BytesField: _Optional[_Iterable[bytes]] = ..., MessageField: _Optional[_Iterable[_Union[TestConflictingFieldNames.TestMessage, _Mapping]]] = ..., int32_field_list: _Optional[int] = ..., field_name: _Optional[str] = ..., field__name: _Optional[str] = ..., _2conflict: _Optional[int] = ..., __2conflict: _Optional[int] = ..., int64_field: _Optional[_Iterable[int]] = ...) -> None: ...

class TestMapField(_message.Message):
    __slots__ = ("map_field",)
    class MapField(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Pair(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Message(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    map_field: _containers.ScalarMap[int, int]
    def __init__(self, map_field: _Optional[_Mapping[int, int]] = ...) -> None: ...

class TestLeadingNumberFields(_message.Message):
    __slots__ = ("_30day_impressions", "_60day_impressions", "__2_underscores", "__2repeated_underscores", "_32", "_64")
    _30DAY_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    _60DAY_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    __2_UNDERSCORES_FIELD_NUMBER: _ClassVar[int]
    __2REPEATED_UNDERSCORES_FIELD_NUMBER: _ClassVar[int]
    _32_FIELD_NUMBER: _ClassVar[int]
    _64_FIELD_NUMBER: _ClassVar[int]
    _30day_impressions: int
    _60day_impressions: _containers.RepeatedScalarFieldContainer[str]
    __2_underscores: str
    __2repeated_underscores: _containers.RepeatedScalarFieldContainer[str]
    _32: int
    _64: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, _30day_impressions: _Optional[int] = ..., _60day_impressions: _Optional[_Iterable[str]] = ..., __2_underscores: _Optional[str] = ..., __2repeated_underscores: _Optional[_Iterable[str]] = ..., _32: _Optional[int] = ..., _64: _Optional[_Iterable[int]] = ...) -> None: ...
