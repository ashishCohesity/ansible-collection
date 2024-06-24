from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
RECURSIVE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
recursive_extension: _descriptor.FieldDescriptor

class Message1(_message.Message):
    __slots__ = ("map_field",)
    Extensions: _python_message._ExtensionDict
    class MapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    map_field: _containers.ScalarMap[str, bool]
    def __init__(self, map_field: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class RedactAllTypes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
