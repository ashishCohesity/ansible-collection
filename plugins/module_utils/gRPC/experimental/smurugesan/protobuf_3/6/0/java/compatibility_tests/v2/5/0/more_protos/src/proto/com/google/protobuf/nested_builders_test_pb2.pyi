from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vehicle(_message.Message):
    __slots__ = ("engine", "wheel")
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    WHEEL_FIELD_NUMBER: _ClassVar[int]
    engine: Engine
    wheel: _containers.RepeatedCompositeFieldContainer[Wheel]
    def __init__(self, engine: _Optional[_Union[Engine, _Mapping]] = ..., wheel: _Optional[_Iterable[_Union[Wheel, _Mapping]]] = ...) -> None: ...

class Engine(_message.Message):
    __slots__ = ("cylinder", "liters")
    CYLINDER_FIELD_NUMBER: _ClassVar[int]
    LITERS_FIELD_NUMBER: _ClassVar[int]
    cylinder: int
    liters: int
    def __init__(self, cylinder: _Optional[int] = ..., liters: _Optional[int] = ...) -> None: ...

class Wheel(_message.Message):
    __slots__ = ("radius", "width")
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    radius: int
    width: int
    def __init__(self, radius: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...
