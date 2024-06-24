from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Value(_message.Message):
    __slots__ = ("type", "data")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInt64: _ClassVar[Value.Type]
        kDouble: _ClassVar[Value.Type]
        kString: _ClassVar[Value.Type]
        kBytes: _ClassVar[Value.Type]
    kInt64: Value.Type
    kDouble: Value.Type
    kString: Value.Type
    kBytes: Value.Type
    class Data(_message.Message):
        __slots__ = ("int64_value", "double_value", "string_value", "bytes_value")
        INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
        int64_value: int
        double_value: float
        string_value: str
        bytes_value: bytes
        def __init__(self, int64_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bytes_value: _Optional[bytes] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: Value.Type
    data: Value.Data
    def __init__(self, type: _Optional[_Union[Value.Type, str]] = ..., data: _Optional[_Union[Value.Data, _Mapping]] = ...) -> None: ...

class KeyValuePair(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: Value
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
