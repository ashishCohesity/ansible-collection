from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StructTestCases(_message.Message):
    __slots__ = ("empty_value", "empty_value2", "null_value", "simple_struct", "longer_struct", "struct_with_nested_struct", "struct_with_nested_list", "struct_with_list_of_nulls", "struct_with_list_of_lists", "struct_with_list_of_structs", "struct_with_empty_list", "struct_with_list_with_empty_struct", "top_level_struct", "top_level_struct_with_empty_list", "top_level_struct_with_list_with_empty_struct", "value_wrapper_simple", "value_wrapper_with_struct", "value_wrapper_with_list", "value_wrapper_with_empty_list", "value_wrapper_with_list_with_empty_struct", "list_value_wrapper", "list_value_wrapper_with_empty_list", "list_value_wrapper_with_list_with_empty_struct", "top_level_value_simple", "top_level_value_with_struct", "top_level_value_with_list", "top_level_value_with_empty_list", "top_level_value_with_list_with_empty_struct", "top_level_listvalue", "top_level_empty_listvalue", "top_level_listvalue_with_empty_struct", "repeated_value", "repeated_value_nested_list", "repeated_value_nested_list2", "repeated_value_nested_list3", "repeated_listvalue", "map_of_struct", "map_of_struct_value", "map_of_listvalue")
    EMPTY_VALUE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_VALUE2_FIELD_NUMBER: _ClassVar[int]
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_STRUCT_FIELD_NUMBER: _ClassVar[int]
    LONGER_STRUCT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_NESTED_STRUCT_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_NESTED_LIST_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_OF_NULLS_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_OF_LISTS_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_OF_STRUCTS_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_EMPTY_LIST_FIELD_NUMBER: _ClassVar[int]
    STRUCT_WITH_LIST_WITH_EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_STRUCT_WITH_EMPTY_LIST_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_STRUCT_WITH_LIST_WITH_EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_WITH_STRUCT_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_WITH_LIST_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_WITH_EMPTY_LIST_FIELD_NUMBER: _ClassVar[int]
    VALUE_WRAPPER_WITH_LIST_WITH_EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_WRAPPER_WITH_EMPTY_LIST_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_WRAPPER_WITH_LIST_WITH_EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_WITH_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_WITH_LIST_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_WITH_EMPTY_LIST_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_VALUE_WITH_LIST_WITH_EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_LISTVALUE_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_EMPTY_LISTVALUE_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_LISTVALUE_WITH_EMPTY_STRUCT_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_NESTED_LIST_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_NESTED_LIST2_FIELD_NUMBER: _ClassVar[int]
    REPEATED_VALUE_NESTED_LIST3_FIELD_NUMBER: _ClassVar[int]
    REPEATED_LISTVALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_OF_STRUCT_FIELD_NUMBER: _ClassVar[int]
    MAP_OF_STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_OF_LISTVALUE_FIELD_NUMBER: _ClassVar[int]
    empty_value: StructWrapper
    empty_value2: StructWrapper
    null_value: StructWrapper
    simple_struct: StructWrapper
    longer_struct: StructWrapper
    struct_with_nested_struct: StructWrapper
    struct_with_nested_list: StructWrapper
    struct_with_list_of_nulls: StructWrapper
    struct_with_list_of_lists: StructWrapper
    struct_with_list_of_structs: StructWrapper
    struct_with_empty_list: StructWrapper
    struct_with_list_with_empty_struct: StructWrapper
    top_level_struct: _struct_pb2.Struct
    top_level_struct_with_empty_list: _struct_pb2.Struct
    top_level_struct_with_list_with_empty_struct: _struct_pb2.Struct
    value_wrapper_simple: ValueWrapper
    value_wrapper_with_struct: ValueWrapper
    value_wrapper_with_list: ValueWrapper
    value_wrapper_with_empty_list: ValueWrapper
    value_wrapper_with_list_with_empty_struct: ValueWrapper
    list_value_wrapper: ListValueWrapper
    list_value_wrapper_with_empty_list: ListValueWrapper
    list_value_wrapper_with_list_with_empty_struct: ListValueWrapper
    top_level_value_simple: _struct_pb2.Value
    top_level_value_with_struct: _struct_pb2.Value
    top_level_value_with_list: _struct_pb2.Value
    top_level_value_with_empty_list: _struct_pb2.Value
    top_level_value_with_list_with_empty_struct: _struct_pb2.Value
    top_level_listvalue: _struct_pb2.ListValue
    top_level_empty_listvalue: _struct_pb2.ListValue
    top_level_listvalue_with_empty_struct: _struct_pb2.ListValue
    repeated_value: RepeatedValueWrapper
    repeated_value_nested_list: RepeatedValueWrapper
    repeated_value_nested_list2: RepeatedValueWrapper
    repeated_value_nested_list3: RepeatedValueWrapper
    repeated_listvalue: RepeatedListValueWrapper
    map_of_struct: MapOfStruct
    map_of_struct_value: MapOfStruct
    map_of_listvalue: MapOfStruct
    def __init__(self, empty_value: _Optional[_Union[StructWrapper, _Mapping]] = ..., empty_value2: _Optional[_Union[StructWrapper, _Mapping]] = ..., null_value: _Optional[_Union[StructWrapper, _Mapping]] = ..., simple_struct: _Optional[_Union[StructWrapper, _Mapping]] = ..., longer_struct: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_nested_struct: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_nested_list: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_list_of_nulls: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_list_of_lists: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_list_of_structs: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_empty_list: _Optional[_Union[StructWrapper, _Mapping]] = ..., struct_with_list_with_empty_struct: _Optional[_Union[StructWrapper, _Mapping]] = ..., top_level_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., top_level_struct_with_empty_list: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., top_level_struct_with_list_with_empty_struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., value_wrapper_simple: _Optional[_Union[ValueWrapper, _Mapping]] = ..., value_wrapper_with_struct: _Optional[_Union[ValueWrapper, _Mapping]] = ..., value_wrapper_with_list: _Optional[_Union[ValueWrapper, _Mapping]] = ..., value_wrapper_with_empty_list: _Optional[_Union[ValueWrapper, _Mapping]] = ..., value_wrapper_with_list_with_empty_struct: _Optional[_Union[ValueWrapper, _Mapping]] = ..., list_value_wrapper: _Optional[_Union[ListValueWrapper, _Mapping]] = ..., list_value_wrapper_with_empty_list: _Optional[_Union[ListValueWrapper, _Mapping]] = ..., list_value_wrapper_with_list_with_empty_struct: _Optional[_Union[ListValueWrapper, _Mapping]] = ..., top_level_value_simple: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_value_with_struct: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_value_with_list: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_value_with_empty_list: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_value_with_list_with_empty_struct: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., top_level_listvalue: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., top_level_empty_listvalue: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., top_level_listvalue_with_empty_struct: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., repeated_value: _Optional[_Union[RepeatedValueWrapper, _Mapping]] = ..., repeated_value_nested_list: _Optional[_Union[RepeatedValueWrapper, _Mapping]] = ..., repeated_value_nested_list2: _Optional[_Union[RepeatedValueWrapper, _Mapping]] = ..., repeated_value_nested_list3: _Optional[_Union[RepeatedValueWrapper, _Mapping]] = ..., repeated_listvalue: _Optional[_Union[RepeatedListValueWrapper, _Mapping]] = ..., map_of_struct: _Optional[_Union[MapOfStruct, _Mapping]] = ..., map_of_struct_value: _Optional[_Union[MapOfStruct, _Mapping]] = ..., map_of_listvalue: _Optional[_Union[MapOfStruct, _Mapping]] = ...) -> None: ...

class StructWrapper(_message.Message):
    __slots__ = ("struct",)
    STRUCT_FIELD_NUMBER: _ClassVar[int]
    struct: _struct_pb2.Struct
    def __init__(self, struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ValueWrapper(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _struct_pb2.Value
    def __init__(self, value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class RepeatedValueWrapper(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    def __init__(self, values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ...) -> None: ...

class ListValueWrapper(_message.Message):
    __slots__ = ("shopping_list",)
    SHOPPING_LIST_FIELD_NUMBER: _ClassVar[int]
    shopping_list: _struct_pb2.ListValue
    def __init__(self, shopping_list: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class RepeatedListValueWrapper(_message.Message):
    __slots__ = ("dimensions",)
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
    def __init__(self, dimensions: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]] = ...) -> None: ...

class MapOfStruct(_message.Message):
    __slots__ = ("struct_map", "value_map", "listvalue_map")
    class StructMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    class ValueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    class ListvalueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.ListValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...
    STRUCT_MAP_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    LISTVALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    struct_map: _containers.MessageMap[str, _struct_pb2.Struct]
    value_map: _containers.MessageMap[str, _struct_pb2.Value]
    listvalue_map: _containers.MessageMap[str, _struct_pb2.ListValue]
    def __init__(self, struct_map: _Optional[_Mapping[str, _struct_pb2.Struct]] = ..., value_map: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., listvalue_map: _Optional[_Mapping[str, _struct_pb2.ListValue]] = ...) -> None: ...

class Dummy(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class StructType(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _struct_pb2.Struct
    def __init__(self, object: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
