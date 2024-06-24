from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DefaultValueTestCases(_message.Message):
    __slots__ = ("empty_double", "double_with_default_value", "double_with_nondefault_value", "repeated_double", "nested_message", "repeated_nested_message", "double_message_with_oneof", "empty_struct", "empty_struct2", "struct_with_null_value", "struct_with_values", "struct_with_nested_struct", "struct_with_nested_list", "struct_with_list_of_nulls", "struct_with_list_of_lists", "struct_with_list_of_structs", "top_level_struct", "value_wrapper_simple", "value_wrapper_with_struct", "value_wrapper_with_list", "list_value_wrapper", "top_level_value_simple", "top_level_value_with_struct", "top_level_value_with_list", "top_level_listvalue", "empty_any", "type_only_any", "recursive_any", "any_with_message_value", "any_with_nested_message", "any_with_message_containing_map", "any_with_message_containing_struct", "top_level_any", "empty_map", "string_to_int", "int_to_string", "mixed1", "mixed2", "empty_mixed2", "map_of_objects", "mixed_empty", "message_map_empty", "double_value", "double_value_default")
    EMPTY_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_WITH_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_WITH_NONDEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_MESSAGE_WITH_ONEOF_FIELD_NUMBER: _ClassVar[int]
    EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    EMPTY_STRUCT2_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_NESTED_STRUCT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_NESTED_LIST_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_OF_NULLS_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_OF_LISTS_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_OF_STRUCTS_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_STRUCT_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_WITH_STRUCT_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_WITH_LIST_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_WITH_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_WITH_LIST_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_LISTVALUE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_ANY_FIELD_NUMBER: _ClassVar[int]
    TYPE_ONLY_ANY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_ANY_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_CONTAINING_MAP_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_CONTAINING_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_ANY_FIELD_NUMBER: _ClassVar[int]
    EMPTY_MAP_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT_FIELD_NUMBER: _ClassVar[int]
    INT_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    MIXED1_FIELD_NUMBER: _ClassVar[int]
    MIXED2_FIELD_NUMBER: _ClassVar[int]
    EMPTY_MIXED2_FIELD_NUMBER: _ClassVar[int]
    MAP_OF_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MIXED_EMPTY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_MAP_EMPTY_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    empty_double: DoubleMessage
    double_with_default_value: DoubleMessage
    double_with_nondefault_value: DoubleMessage
    repeated_double: DoubleMessage
    nested_message: DoubleMessage
    repeated_nested_message: DoubleMessage
    double_message_with_oneof: DoubleMessage
    empty_struct: StructMessage
    empty_struct2: StructMessage
    struct_with_null_value: StructMessage
    struct_with_values: StructMessage
    struct_with_nested_struct: StructMessage
    struct_with_nested_list: StructMessage
    struct_with_list_of_nulls: StructMessage
    struct_with_list_of_lists: StructMessage
    struct_with_list_of_structs: StructMessage
    top_level_struct: _struct_pb2.Struct
    value_wrapper_simple: ValueMessage
    value_wrapper_with_struct: ValueMessage
    value_wrapper_with_list: ValueMessage
    list_value_wrapper: ListValueMessage
    top_level_value_simple: _struct_pb2.Value
    top_level_value_with_struct: _struct_pb2.Value
    top_level_value_with_list: _struct_pb2.Value
    top_level_listvalue: _struct_pb2.ListValue
    empty_any: AnyMessage
    type_only_any: AnyMessage
    recursive_any: AnyMessage
    any_with_message_value: AnyMessage
    any_with_nested_message: AnyMessage
    any_with_message_containing_map: AnyMessage
    any_with_message_containing_struct: AnyMessage
    top_level_any: _any_pb2.Any
    empty_map: StringtoIntMap
    string_to_int: StringtoIntMap
    int_to_string: IntToStringMap
    mixed1: MixedMap
    mixed2: MixedMap2
    empty_mixed2: MixedMap2
    map_of_objects: MessageMap
    mixed_empty: MixedMap
    message_map_empty: MessageMap
    double_value: DoubleValueMessage
    double_value_default: DoubleValueMessage
    def __init__(self, empty_double: _Optional[_Union[DoubleMessage, _Mapping]] = ..., double_with_default_value: _Optional[_Union[DoubleMessage, _Mapping]] = ..., double_with_nondefault_value: _Optional[_Union[DoubleMessage, _Mapping]] = ..., repeated_double: _Optional[_Union[DoubleMessage, _Mapping]] = ..., nested_message: _Optional[_Union[DoubleMessage, _Mapping]] = ..., repeated_nested_message: _Optional[_Union[DoubleMessage, _Mapping]] = ..., double_message_with_oneof: _Optional[_Union[DoubleMessage, _Mapping]] = ..., empty_struct: _Optional[_Union[StructMessage, _Mapping]] = ..., empty_struct2: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_null_value: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_values: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_nested_struct: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_nested_list: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_list_of_nulls: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_list_of_lists: _Optional[_Union[StructMessage, _Mapping]] = ..., struct_with_list_of_structs: _Optional[_Union[StructMessage, _Mapping]] = ..., top_level_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., value_wrapper_simple: _Optional[_Union[ValueMessage, _Mapping]] = ..., value_wrapper_with_struct: _Optional[_Union[ValueMessage, _Mapping]] = ..., value_wrapper_with_list: _Optional[_Union[ValueMessage, _Mapping]] = ..., list_value_wrapper: _Optional[_Union[ListValueMessage, _Mapping]] = ..., top_level_value_simple: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_value_with_struct: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_value_with_list: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_listvalue: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., empty_any: _Optional[_Union[AnyMessage, _Mapping]] = ..., type_only_any: _Optional[_Union[AnyMessage, _Mapping]] = ..., recursive_any: _Optional[_Union[AnyMessage, _Mapping]] = ..., any_with_message_value: _Optional[_Union[AnyMessage, _Mapping]] = ..., any_with_nested_message: _Optional[_Union[AnyMessage, _Mapping]] = ..., any_with_message_containing_map: _Optional[_Union[AnyMessage, _Mapping]] = ..., any_with_message_containing_struct: _Optional[_Union[AnyMessage, _Mapping]] = ..., top_level_any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., empty_map: _Optional[_Union[StringtoIntMap, _Mapping]] = ..., string_to_int: _Optional[_Union[StringtoIntMap, _Mapping]] = ..., int_to_string: _Optional[_Union[IntToStringMap, _Mapping]] = ..., mixed1: _Optional[_Union[MixedMap, _Mapping]] = ..., mixed2: _Optional[_Union[MixedMap2, _Mapping]] = ..., empty_mixed2: _Optional[_Union[MixedMap2, _Mapping]] = ..., map_of_objects: _Optional[_Union[MessageMap, _Mapping]] = ..., mixed_empty: _Optional[_Union[MixedMap, _Mapping]] = ..., message_map_empty: _Optional[_Union[MessageMap, _Mapping]] = ..., double_value: _Optional[_Union[DoubleValueMessage, _Mapping]] = ..., double_value_default: _Optional[_Union[DoubleValueMessage, _Mapping]] = ...) -> None: ...

class DoubleMessage(_message.Message):
    __slots__ = ("double_value", "repeated_double", "nested_message", "repeated_nested_message", "double_wrapper", "str_value", "num_value")
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    double_value: float
    repeated_double: _containers.RepeatedScalarFieldContainer[float]
    nested_message: DoubleMessage
    repeated_nested_message: _containers.RepeatedCompositeFieldContainer[DoubleMessage]
    double_wrapper: _wrappers_pb2.DoubleValue
    str_value: str
    num_value: int
    def __init__(self, double_value: _Optional[float] = ..., repeated_double: _Optional[_Iterable[float]] = ..., nested_message: _Optional[_Union[DoubleMessage, _Mapping]] = ..., repeated_nested_message: _Optional[_Iterable[_Union[DoubleMessage, _Mapping]]] = ..., double_wrapper: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., str_value: _Optional[str] = ..., num_value: _Optional[int] = ...) -> None: ...

class StructMessage(_message.Message):
    __slots__ = ("struct",)
    STRUCT_FIELD_NUMBER: _ClassVar[int]
    struct: _struct_pb2.Struct
    def __init__(self, struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ValueMessage(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Value
    def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ListValueMessage(_message.Message):
    __slots__ = ("shopping_list",)
    SHOPPING_LIST_FIELD_NUMBER: _ClassVar[int]
    shopping_list: _struct_pb2.ListValue
    def __init__(self, shopping_list: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class RequestMessage(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class AnyMessage(_message.Message):
    __slots__ = ("any", "data")
    ANY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    any: _any_pb2.Any
    data: AnyData
    def __init__(self, any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., data: _Optional[_Union[AnyData, _Mapping]] = ...) -> None: ...

class AnyData(_message.Message):
    __slots__ = ("attr", "str", "msgs", "nested_data", "map_data", "struct_data", "repeated_data")
    class MapDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ATTR_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    MSGS_FIELD_NUMBER: _ClassVar[int]
    NESTED_DATA_FIELD_NUMBER: _ClassVar[int]
    MAP_DATA_FIELD_NUMBER: _ClassVar[int]
    STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DATA_FIELD_NUMBER: _ClassVar[int]
    attr: int
    str: str
    msgs: _containers.RepeatedScalarFieldContainer[str]
    nested_data: AnyData
    map_data: _containers.ScalarMap[str, str]
    struct_data: _struct_pb2.Struct
    repeated_data: _containers.RepeatedCompositeFieldContainer[AnyData]
    def __init__(self, attr: _Optional[int] = ..., str: _Optional[str] = ..., msgs: _Optional[_Iterable[str]] = ..., nested_data: _Optional[_Union[AnyData, _Mapping]] = ..., map_data: _Optional[_Mapping[str, str]] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., repeated_data: _Optional[_Iterable[_Union[AnyData, _Mapping]]] = ...) -> None: ...

class StringtoIntMap(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[str, int]
    def __init__(self, map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class IntToStringMap(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, str]
    def __init__(self, map: _Optional[_Mapping[int, str]] = ...) -> None: ...

class MixedMap(_message.Message):
    __slots__ = ("msg", "map", "int_value")
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    msg: str
    map: _containers.ScalarMap[str, float]
    int_value: int
    def __init__(self, msg: _Optional[str] = ..., map: _Optional[_Mapping[str, float]] = ..., int_value: _Optional[int] = ...) -> None: ...

class MixedMap2(_message.Message):
    __slots__ = ("map", "ee", "msg")
    class E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        E0: _ClassVar[MixedMap2.E]
        E1: _ClassVar[MixedMap2.E]
        E2: _ClassVar[MixedMap2.E]
        E3: _ClassVar[MixedMap2.E]
    E0: MixedMap2.E
    E1: MixedMap2.E
    E2: MixedMap2.E
    E3: MixedMap2.E
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    EE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, bool]
    ee: MixedMap2.E
    msg: str
    def __init__(self, map: _Optional[_Mapping[int, bool]] = ..., ee: _Optional[_Union[MixedMap2.E, str]] = ..., msg: _Optional[str] = ...) -> None: ...

class MessageMap(_message.Message):
    __slots__ = ("map",)
    class M(_message.Message):
        __slots__ = ("inner_int", "inner_text")
        INNER_INT_FIELD_NUMBER: _ClassVar[int]
        INNER_TEXT_FIELD_NUMBER: _ClassVar[int]
        inner_int: int
        inner_text: str
        def __init__(self, inner_int: _Optional[int] = ..., inner_text: _Optional[str] = ...) -> None: ...
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MessageMap.M
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MessageMap.M, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, MessageMap.M]
    def __init__(self, map: _Optional[_Mapping[str, MessageMap.M]] = ...) -> None: ...

class DoubleValueMessage(_message.Message):
    __slots__ = ("double",)
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    double: _wrappers_pb2.DoubleValue
    def __init__(self, double: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
