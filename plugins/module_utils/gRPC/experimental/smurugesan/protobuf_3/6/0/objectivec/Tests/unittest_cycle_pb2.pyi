from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CycleFoo(_message.Message):
    __slots__ = ("a_foo", "a_bar", "a_baz")
    A_FOO_FIELD_NUMBER: _ClassVar[int]
    A_BAR_FIELD_NUMBER: _ClassVar[int]
    A_BAZ_FIELD_NUMBER: _ClassVar[int]
    a_foo: CycleFoo
    a_bar: CycleBar
    a_baz: CycleBaz
    def __init__(self, a_foo: _Optional[_Union[CycleFoo, _Mapping]] = ..., a_bar: _Optional[_Union[CycleBar, _Mapping]] = ..., a_baz: _Optional[_Union[CycleBaz, _Mapping]] = ...) -> None: ...

class CycleBar(_message.Message):
    __slots__ = ("a_bar", "a_baz", "a_foo")
    A_BAR_FIELD_NUMBER: _ClassVar[int]
    A_BAZ_FIELD_NUMBER: _ClassVar[int]
    A_FOO_FIELD_NUMBER: _ClassVar[int]
    a_bar: CycleBar
    a_baz: CycleBaz
    a_foo: CycleFoo
    def __init__(self, a_bar: _Optional[_Union[CycleBar, _Mapping]] = ..., a_baz: _Optional[_Union[CycleBaz, _Mapping]] = ..., a_foo: _Optional[_Union[CycleFoo, _Mapping]] = ...) -> None: ...

class CycleBaz(_message.Message):
    __slots__ = ("a_baz", "a_foo", "a_bar")
    A_BAZ_FIELD_NUMBER: _ClassVar[int]
    A_FOO_FIELD_NUMBER: _ClassVar[int]
    A_BAR_FIELD_NUMBER: _ClassVar[int]
    a_baz: CycleBaz
    a_foo: CycleFoo
    a_bar: CycleBar
    def __init__(self, a_baz: _Optional[_Union[CycleBaz, _Mapping]] = ..., a_foo: _Optional[_Union[CycleFoo, _Mapping]] = ..., a_bar: _Optional[_Union[CycleBar, _Mapping]] = ...) -> None: ...
