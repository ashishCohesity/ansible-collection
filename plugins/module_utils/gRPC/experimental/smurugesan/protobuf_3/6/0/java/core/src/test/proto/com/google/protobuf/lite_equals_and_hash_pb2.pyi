from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
VARINT_FIELD_NUMBER: _ClassVar[int]
varint: _descriptor.FieldDescriptor
FIXED32_FIELD_NUMBER: _ClassVar[int]
fixed32: _descriptor.FieldDescriptor
FIXED64_FIELD_NUMBER: _ClassVar[int]
fixed64: _descriptor.FieldDescriptor
MYGROUP_FIELD_NUMBER: _ClassVar[int]
mygroup: _descriptor.FieldDescriptor

class TestOneofEquals(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class Foo(_message.Message):
    __slots__ = ("value", "bar", "my_map", "sint64", "mygroup")
    Extensions: _python_message._ExtensionDict
    class MyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MyGroup(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    MY_MAP_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_NUMBER: _ClassVar[int]
    MYGROUP_FIELD_NUMBER: _ClassVar[int]
    value: int
    bar: _containers.RepeatedCompositeFieldContainer[Bar]
    my_map: _containers.ScalarMap[str, str]
    sint64: int
    mygroup: Foo.MyGroup
    def __init__(self, value: _Optional[int] = ..., bar: _Optional[_Iterable[_Union[Bar, _Mapping]]] = ..., my_map: _Optional[_Mapping[str, str]] = ..., sint64: _Optional[int] = ..., mygroup: _Optional[_Union[Foo.MyGroup, _Mapping]] = ...) -> None: ...

class Bar(_message.Message):
    __slots__ = ("name",)
    FOO_EXT_FIELD_NUMBER: _ClassVar[int]
    foo_ext: _descriptor.FieldDescriptor
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BarPrime(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MyGroup(_message.Message):
    __slots__ = ("group_value",)
    GROUP_VALUE_FIELD_NUMBER: _ClassVar[int]
    group_value: str
    def __init__(self, group_value: _Optional[str] = ...) -> None: ...

class TestRecursiveOneof(_message.Message):
    __slots__ = ("r",)
    R_FIELD_NUMBER: _ClassVar[int]
    r: TestRecursiveOneof
    def __init__(self, r: _Optional[_Union[TestRecursiveOneof, _Mapping]] = ...) -> None: ...
