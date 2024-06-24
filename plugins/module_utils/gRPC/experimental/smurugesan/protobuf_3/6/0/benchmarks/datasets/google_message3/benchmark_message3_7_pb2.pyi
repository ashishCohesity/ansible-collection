from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message11018(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Message10800(_message.Message):
    __slots__ = ("field10808", "field10809", "field10810", "field10811")
    FIELD10808_FIELD_NUMBER: _ClassVar[int]
    FIELD10809_FIELD_NUMBER: _ClassVar[int]
    FIELD10810_FIELD_NUMBER: _ClassVar[int]
    FIELD10811_FIELD_NUMBER: _ClassVar[int]
    field10808: str
    field10809: int
    field10810: bool
    field10811: float
    def __init__(self, field10808: _Optional[str] = ..., field10809: _Optional[int] = ..., field10810: bool = ..., field10811: _Optional[float] = ...) -> None: ...

class Message10802(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Message10748(_message.Message):
    __slots__ = ("field10750", "field10751", "field10752", "field10753")
    FIELD10750_FIELD_NUMBER: _ClassVar[int]
    FIELD10751_FIELD_NUMBER: _ClassVar[int]
    FIELD10752_FIELD_NUMBER: _ClassVar[int]
    FIELD10753_FIELD_NUMBER: _ClassVar[int]
    field10750: str
    field10751: int
    field10752: int
    field10753: int
    def __init__(self, field10750: _Optional[str] = ..., field10751: _Optional[int] = ..., field10752: _Optional[int] = ..., field10753: _Optional[int] = ...) -> None: ...

class Message7966(_message.Message):
    __slots__ = ("field7969", "field7970")
    FIELD7969_FIELD_NUMBER: _ClassVar[int]
    FIELD7970_FIELD_NUMBER: _ClassVar[int]
    field7969: str
    field7970: bool
    def __init__(self, field7969: _Optional[str] = ..., field7970: bool = ...) -> None: ...

class Message708(_message.Message):
    __slots__ = ("field823", "field824", "field825", "field826", "field827", "field828")
    FIELD823_FIELD_NUMBER: _ClassVar[int]
    FIELD824_FIELD_NUMBER: _ClassVar[int]
    FIELD825_FIELD_NUMBER: _ClassVar[int]
    FIELD826_FIELD_NUMBER: _ClassVar[int]
    FIELD827_FIELD_NUMBER: _ClassVar[int]
    FIELD828_FIELD_NUMBER: _ClassVar[int]
    field823: Message741
    field824: _containers.RepeatedScalarFieldContainer[str]
    field825: str
    field826: str
    field827: _containers.RepeatedScalarFieldContainer[str]
    field828: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field823: _Optional[_Union[Message741, _Mapping]] = ..., field824: _Optional[_Iterable[str]] = ..., field825: _Optional[str] = ..., field826: _Optional[str] = ..., field827: _Optional[_Iterable[str]] = ..., field828: _Optional[_Iterable[str]] = ...) -> None: ...

class Message8942(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Message11011(_message.Message):
    __slots__ = ("field11752", "field11753")
    FIELD11752_FIELD_NUMBER: _ClassVar[int]
    FIELD11753_FIELD_NUMBER: _ClassVar[int]
    field11752: bytes
    field11753: bytes
    def __init__(self, field11752: _Optional[bytes] = ..., field11753: _Optional[bytes] = ...) -> None: ...

class UnusedEmptyMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Message741(_message.Message):
    __slots__ = ("field936",)
    FIELD936_FIELD_NUMBER: _ClassVar[int]
    field936: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field936: _Optional[_Iterable[str]] = ...) -> None: ...
