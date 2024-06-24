from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestAny(_message.Message):
    __slots__ = ("value", "int_value", "map_value")
    Extensions: _python_message._ExtensionDict
    class MapValueEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _any_pb2.Any
    int_value: int
    map_value: _containers.ScalarMap[str, int]
    def __init__(self, value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., int_value: _Optional[int] = ..., map_value: _Optional[_Mapping[str, int]] = ...) -> None: ...

class TestAnyExtension1(_message.Message):
    __slots__ = ("i",)
    EXTENSION1_FIELD_NUMBER: _ClassVar[int]
    extension1: _descriptor.FieldDescriptor
    I_FIELD_NUMBER: _ClassVar[int]
    i: int
    def __init__(self, i: _Optional[int] = ...) -> None: ...
