from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnyTestCases(_message.Message):
    __slots__ = ("empty_any", "type_only_any", "wrapper_any", "any_with_timestamp_value", "any_with_duration_value", "any_with_struct_value", "recursive_any", "any_with_message_value", "any_with_nested_message", "any_with_message_with_wrapper_type", "any_with_message_with_timestamp", "any_with_message_containing_map", "any_with_message_containing_struct", "any_with_message_containing_repeated_message", "recursive_any_with_type_field_at_end", "top_level_any", "top_level_any_with_type_field_at_end")
    EMPTY_ANY_FIELD_NUMBER: _ClassVar[int]
    TYPE_ONLY_ANY_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_ANY_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_ANY_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_NESTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_WITH_WRAPPER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_WITH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_CONTAINING_MAP_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_CONTAINING_STRUCT_FIELD_NUMBER: _ClassVar[int]
    ANY_WITH_MESSAGE_CONTAINING_REPEATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_ANY_WITH_TYPE_FIELD_AT_END_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_ANY_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_ANY_WITH_TYPE_FIELD_AT_END_FIELD_NUMBER: _ClassVar[int]
    empty_any: AnyWrapper
    type_only_any: AnyWrapper
    wrapper_any: AnyWrapper
    any_with_timestamp_value: AnyWrapper
    any_with_duration_value: AnyWrapper
    any_with_struct_value: AnyWrapper
    recursive_any: AnyWrapper
    any_with_message_value: AnyWrapper
    any_with_nested_message: AnyWrapper
    any_with_message_with_wrapper_type: AnyWrapper
    any_with_message_with_timestamp: AnyWrapper
    any_with_message_containing_map: AnyWrapper
    any_with_message_containing_struct: AnyWrapper
    any_with_message_containing_repeated_message: AnyWrapper
    recursive_any_with_type_field_at_end: AnyWrapper
    top_level_any: _any_pb2.Any
    top_level_any_with_type_field_at_end: _any_pb2.Any
    def __init__(self, empty_any: _Optional[_Union[AnyWrapper, _Mapping]] = ..., type_only_any: _Optional[_Union[AnyWrapper, _Mapping]] = ..., wrapper_any: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_timestamp_value: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_duration_value: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_struct_value: _Optional[_Union[AnyWrapper, _Mapping]] = ..., recursive_any: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_message_value: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_nested_message: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_message_with_wrapper_type: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_message_with_timestamp: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_message_containing_map: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_message_containing_struct: _Optional[_Union[AnyWrapper, _Mapping]] = ..., any_with_message_containing_repeated_message: _Optional[_Union[AnyWrapper, _Mapping]] = ..., recursive_any_with_type_field_at_end: _Optional[_Union[AnyWrapper, _Mapping]] = ..., top_level_any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., top_level_any_with_type_field_at_end: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AnyWrapper(_message.Message):
    __slots__ = ("any",)
    ANY_FIELD_NUMBER: _ClassVar[int]
    any: _any_pb2.Any
    def __init__(self, any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class Imports(_message.Message):
    __slots__ = ("dbl", "struct", "timestamp", "duration", "i32", "data")
    DBL_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    I32_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    dbl: _wrappers_pb2.DoubleValue
    struct: _struct_pb2.Struct
    timestamp: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    i32: _wrappers_pb2.Int32Value
    data: Data
    def __init__(self, dbl: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., struct: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., i32: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("attr", "str", "msgs", "nested_data", "int_wrapper", "time", "map_data", "struct_data", "repeated_data")
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
    INT_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    MAP_DATA_FIELD_NUMBER: _ClassVar[int]
    STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DATA_FIELD_NUMBER: _ClassVar[int]
    attr: int
    str: str
    msgs: _containers.RepeatedScalarFieldContainer[str]
    nested_data: Data
    int_wrapper: _wrappers_pb2.Int32Value
    time: _timestamp_pb2.Timestamp
    map_data: _containers.ScalarMap[str, str]
    struct_data: _struct_pb2.Struct
    repeated_data: _containers.RepeatedCompositeFieldContainer[Data]
    def __init__(self, attr: _Optional[int] = ..., str: _Optional[str] = ..., msgs: _Optional[_Iterable[str]] = ..., nested_data: _Optional[_Union[Data, _Mapping]] = ..., int_wrapper: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., map_data: _Optional[_Mapping[str, str]] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., repeated_data: _Optional[_Iterable[_Union[Data, _Mapping]]] = ...) -> None: ...

class AnyIn(_message.Message):
    __slots__ = ("something", "any")
    SOMETHING_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    something: str
    any: _any_pb2.Any
    def __init__(self, something: _Optional[str] = ..., any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AnyOut(_message.Message):
    __slots__ = ("any",)
    ANY_FIELD_NUMBER: _ClassVar[int]
    any: _any_pb2.Any
    def __init__(self, any: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AnyM(_message.Message):
    __slots__ = ("foo",)
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: str
    def __init__(self, foo: _Optional[str] = ...) -> None: ...
