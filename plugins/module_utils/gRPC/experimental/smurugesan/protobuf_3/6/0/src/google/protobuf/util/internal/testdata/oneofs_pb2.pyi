from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OneOfsRequest(_message.Message):
    __slots__ = ("value", "str_data", "int_data", "message_data", "more_data", "struct_data", "value_data", "list_value_data", "ts_data", "any_data")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    STR_DATA_FIELD_NUMBER: _ClassVar[int]
    INT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    MORE_DATA_FIELD_NUMBER: _ClassVar[int]
    STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    VALUE_DATA_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_DATA_FIELD_NUMBER: _ClassVar[int]
    TS_DATA_FIELD_NUMBER: _ClassVar[int]
    ANY_DATA_FIELD_NUMBER: _ClassVar[int]
    value: str
    str_data: str
    int_data: int
    message_data: Data
    more_data: MoreData
    struct_data: _struct_pb2.Struct
    value_data: _struct_pb2.Value
    list_value_data: _struct_pb2.ListValue
    ts_data: _timestamp_pb2.Timestamp
    any_data: _any_pb2.Any
    def __init__(self, value: _Optional[str] = ..., str_data: _Optional[str] = ..., int_data: _Optional[int] = ..., message_data: _Optional[_Union[Data, _Mapping]] = ..., more_data: _Optional[_Union[MoreData, _Mapping]] = ..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., value_data: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., list_value_data: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., ts_data: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., any_data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class RequestWithSimpleOneof(_message.Message):
    __slots__ = ("value", "str_data", "int_data", "message_data", "more_data")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    STR_DATA_FIELD_NUMBER: _ClassVar[int]
    INT_DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    MORE_DATA_FIELD_NUMBER: _ClassVar[int]
    value: str
    str_data: str
    int_data: int
    message_data: Data
    more_data: MoreData
    def __init__(self, value: _Optional[str] = ..., str_data: _Optional[str] = ..., int_data: _Optional[int] = ..., message_data: _Optional[_Union[Data, _Mapping]] = ..., more_data: _Optional[_Union[MoreData, _Mapping]] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("data_value",)
    DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_value: int
    def __init__(self, data_value: _Optional[int] = ...) -> None: ...

class MoreData(_message.Message):
    __slots__ = ("str_value",)
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    str_value: str
    def __init__(self, str_value: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...
