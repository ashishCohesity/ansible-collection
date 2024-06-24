from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapsTestCases(_message.Message):
    __slots__ = ("empty_map", "string_to_int", "int_to_string", "mixed1", "mixed2", "map_of_objects", "empty_key_string_to_int1", "empty_key_string_to_int2", "empty_key_string_to_int3", "empty_key_bool_to_string", "empty_key_int_to_string", "empty_key_mixed", "empty_key_map_objects")
    EMPTY_MAP_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT_FIELD_NUMBER: _ClassVar[int]
    INT_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    MIXED1_FIELD_NUMBER: _ClassVar[int]
    MIXED2_FIELD_NUMBER: _ClassVar[int]
    MAP_OF_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_STRING_TO_INT1_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_STRING_TO_INT2_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_STRING_TO_INT3_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_BOOL_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_INT_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_MIXED_FIELD_NUMBER: _ClassVar[int]
    EMPTY_KEY_MAP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    empty_map: EmptyMap
    string_to_int: StringtoInt
    int_to_string: IntToString
    mixed1: Mixed1
    mixed2: Mixed2
    map_of_objects: MapOfObjects
    empty_key_string_to_int1: StringtoInt
    empty_key_string_to_int2: StringtoInt
    empty_key_string_to_int3: StringtoInt
    empty_key_bool_to_string: BoolToString
    empty_key_int_to_string: IntToString
    empty_key_mixed: Mixed1
    empty_key_map_objects: MapOfObjects
    def __init__(self, empty_map: _Optional[_Union[EmptyMap, _Mapping]] = ..., string_to_int: _Optional[_Union[StringtoInt, _Mapping]] = ..., int_to_string: _Optional[_Union[IntToString, _Mapping]] = ..., mixed1: _Optional[_Union[Mixed1, _Mapping]] = ..., mixed2: _Optional[_Union[Mixed2, _Mapping]] = ..., map_of_objects: _Optional[_Union[MapOfObjects, _Mapping]] = ..., empty_key_string_to_int1: _Optional[_Union[StringtoInt, _Mapping]] = ..., empty_key_string_to_int2: _Optional[_Union[StringtoInt, _Mapping]] = ..., empty_key_string_to_int3: _Optional[_Union[StringtoInt, _Mapping]] = ..., empty_key_bool_to_string: _Optional[_Union[BoolToString, _Mapping]] = ..., empty_key_int_to_string: _Optional[_Union[IntToString, _Mapping]] = ..., empty_key_mixed: _Optional[_Union[Mixed1, _Mapping]] = ..., empty_key_map_objects: _Optional[_Union[MapOfObjects, _Mapping]] = ...) -> None: ...

class EmptyMap(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, int]
    def __init__(self, map: _Optional[_Mapping[int, int]] = ...) -> None: ...

class StringtoInt(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[str, int]
    def __init__(self, map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class IntToString(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, str]
    def __init__(self, map: _Optional[_Mapping[int, str]] = ...) -> None: ...

class BoolToString(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[bool, str]
    def __init__(self, map: _Optional[_Mapping[bool, str]] = ...) -> None: ...

class Mixed1(_message.Message):
    __slots__ = ("msg", "map")
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    msg: str
    map: _containers.ScalarMap[str, float]
    def __init__(self, msg: _Optional[str] = ..., map: _Optional[_Mapping[str, float]] = ...) -> None: ...

class Mixed2(_message.Message):
    __slots__ = ("map", "ee")
    class E(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        E0: _ClassVar[Mixed2.E]
        E1: _ClassVar[Mixed2.E]
        E2: _ClassVar[Mixed2.E]
        E3: _ClassVar[Mixed2.E]
    E0: Mixed2.E
    E1: Mixed2.E
    E2: Mixed2.E
    E3: Mixed2.E
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    EE_FIELD_NUMBER: _ClassVar[int]
    map: _containers.ScalarMap[int, bool]
    ee: Mixed2.E
    def __init__(self, map: _Optional[_Mapping[int, bool]] = ..., ee: _Optional[_Union[Mixed2.E, str]] = ...) -> None: ...

class MapOfObjects(_message.Message):
    __slots__ = ("map",)
    class M(_message.Message):
        __slots__ = ("inner_text",)
        INNER_TEXT_FIELD_NUMBER: _ClassVar[int]
        inner_text: str
        def __init__(self, inner_text: _Optional[str] = ...) -> None: ...
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapOfObjects.M
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapOfObjects.M, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, MapOfObjects.M]
    def __init__(self, map: _Optional[_Mapping[str, MapOfObjects.M]] = ...) -> None: ...

class DummyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MapIn(_message.Message):
    __slots__ = ("other", "things", "map_input")
    class MapInputEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OTHER_FIELD_NUMBER: _ClassVar[int]
    THINGS_FIELD_NUMBER: _ClassVar[int]
    MAP_INPUT_FIELD_NUMBER: _ClassVar[int]
    other: str
    things: _containers.RepeatedScalarFieldContainer[str]
    map_input: _containers.ScalarMap[str, str]
    def __init__(self, other: _Optional[str] = ..., things: _Optional[_Iterable[str]] = ..., map_input: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MapOut(_message.Message):
    __slots__ = ("map1", "map2", "map3", "map4", "bar")
    class Map1Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapM
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapM, _Mapping]] = ...) -> None: ...
    class Map2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapOut
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapOut, _Mapping]] = ...) -> None: ...
    class Map3Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Map4Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    MAP1_FIELD_NUMBER: _ClassVar[int]
    MAP2_FIELD_NUMBER: _ClassVar[int]
    MAP3_FIELD_NUMBER: _ClassVar[int]
    MAP4_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    map1: _containers.MessageMap[str, MapM]
    map2: _containers.MessageMap[str, MapOut]
    map3: _containers.ScalarMap[int, str]
    map4: _containers.ScalarMap[bool, str]
    bar: str
    def __init__(self, map1: _Optional[_Mapping[str, MapM]] = ..., map2: _Optional[_Mapping[str, MapOut]] = ..., map3: _Optional[_Mapping[int, str]] = ..., map4: _Optional[_Mapping[bool, str]] = ..., bar: _Optional[str] = ...) -> None: ...

class MapOutWireFormat(_message.Message):
    __slots__ = ("map1", "map2", "map3", "map4", "bar")
    class Map1Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapM
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapM, _Mapping]] = ...) -> None: ...
    class Map2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MapOut
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MapOut, _Mapping]] = ...) -> None: ...
    class Map3Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Map4Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: str
        def __init__(self, key: bool = ..., value: _Optional[str] = ...) -> None: ...
    MAP1_FIELD_NUMBER: _ClassVar[int]
    MAP2_FIELD_NUMBER: _ClassVar[int]
    MAP3_FIELD_NUMBER: _ClassVar[int]
    MAP4_FIELD_NUMBER: _ClassVar[int]
    BAR_FIELD_NUMBER: _ClassVar[int]
    map1: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map1Entry]
    map2: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map2Entry]
    map3: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map3Entry]
    map4: _containers.RepeatedCompositeFieldContainer[MapOutWireFormat.Map4Entry]
    bar: str
    def __init__(self, map1: _Optional[_Iterable[_Union[MapOutWireFormat.Map1Entry, _Mapping]]] = ..., map2: _Optional[_Iterable[_Union[MapOutWireFormat.Map2Entry, _Mapping]]] = ..., map3: _Optional[_Iterable[_Union[MapOutWireFormat.Map3Entry, _Mapping]]] = ..., map4: _Optional[_Iterable[_Union[MapOutWireFormat.Map4Entry, _Mapping]]] = ..., bar: _Optional[str] = ...) -> None: ...

class MapM(_message.Message):
    __slots__ = ("foo",)
    FOO_FIELD_NUMBER: _ClassVar[int]
    foo: str
    def __init__(self, foo: _Optional[str] = ...) -> None: ...
