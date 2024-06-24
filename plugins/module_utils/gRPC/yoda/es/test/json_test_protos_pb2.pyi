from yoda.es import jsonname_pb2 as _jsonname_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlatProto(_message.Message):
    __slots__ = ("opt_int32", "opt_int64", "opt_double", "opt_float", "opt_str")
    OPT_INT32_FIELD_NUMBER: _ClassVar[int]
    OPT_INT64_FIELD_NUMBER: _ClassVar[int]
    OPT_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    OPT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    OPT_STR_FIELD_NUMBER: _ClassVar[int]
    opt_int32: int
    opt_int64: int
    opt_double: float
    opt_float: float
    opt_str: str
    def __init__(self, opt_int32: _Optional[int] = ..., opt_int64: _Optional[int] = ..., opt_double: _Optional[float] = ..., opt_float: _Optional[float] = ..., opt_str: _Optional[str] = ...) -> None: ...

class ArrayProto(_message.Message):
    __slots__ = ("rep_int", "rep_str")
    REP_INT_FIELD_NUMBER: _ClassVar[int]
    REP_STR_FIELD_NUMBER: _ClassVar[int]
    rep_int: _containers.RepeatedScalarFieldContainer[int]
    rep_str: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rep_int: _Optional[_Iterable[int]] = ..., rep_str: _Optional[_Iterable[str]] = ...) -> None: ...

class NestedProto(_message.Message):
    __slots__ = ("opt_msg", "rep_msg", "rep_array")
    OPT_MSG_FIELD_NUMBER: _ClassVar[int]
    REP_MSG_FIELD_NUMBER: _ClassVar[int]
    REP_ARRAY_FIELD_NUMBER: _ClassVar[int]
    opt_msg: FlatProto
    rep_msg: _containers.RepeatedCompositeFieldContainer[FlatProto]
    rep_array: _containers.RepeatedCompositeFieldContainer[ArrayProto]
    def __init__(self, opt_msg: _Optional[_Union[FlatProto, _Mapping]] = ..., rep_msg: _Optional[_Iterable[_Union[FlatProto, _Mapping]]] = ..., rep_array: _Optional[_Iterable[_Union[ArrayProto, _Mapping]]] = ...) -> None: ...

class RenamedProto(_message.Message):
    __slots__ = ("delete",)
    DELETE_FIELD_NUMBER: _ClassVar[int]
    delete: int
    def __init__(self, delete: _Optional[int] = ...) -> None: ...

class MapEntryStringString(_message.Message):
    __slots__ = ("_key", "_value")
    _KEY_FIELD_NUMBER: _ClassVar[int]
    _VALUE_FIELD_NUMBER: _ClassVar[int]
    _key: str
    _value: str
    def __init__(self, _key: _Optional[str] = ..., _value: _Optional[str] = ...) -> None: ...

class MapTestProto(_message.Message):
    __slots__ = ("term_maps",)
    TERM_MAPS_FIELD_NUMBER: _ClassVar[int]
    term_maps: _containers.RepeatedCompositeFieldContainer[MapEntryStringString]
    def __init__(self, term_maps: _Optional[_Iterable[_Union[MapEntryStringString, _Mapping]]] = ...) -> None: ...

class BytesProto(_message.Message):
    __slots__ = ("opt_bytes", "rep_bytes")
    OPT_BYTES_FIELD_NUMBER: _ClassVar[int]
    REP_BYTES_FIELD_NUMBER: _ClassVar[int]
    opt_bytes: bytes
    rep_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, opt_bytes: _Optional[bytes] = ..., rep_bytes: _Optional[_Iterable[bytes]] = ...) -> None: ...

class StringProto(_message.Message):
    __slots__ = ("opt_string", "rep_string")
    OPT_STRING_FIELD_NUMBER: _ClassVar[int]
    REP_STRING_FIELD_NUMBER: _ClassVar[int]
    opt_string: str
    rep_string: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, opt_string: _Optional[str] = ..., rep_string: _Optional[_Iterable[str]] = ...) -> None: ...

class NumericRangeQueryTestProto(_message.Message):
    __slots__ = ("range",)
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: _containers.RepeatedCompositeFieldContainer[MapEntryStringMap]
    def __init__(self, range: _Optional[_Iterable[_Union[MapEntryStringMap, _Mapping]]] = ...) -> None: ...

class MapEntryStringMap(_message.Message):
    __slots__ = ("_key", "_value")
    _KEY_FIELD_NUMBER: _ClassVar[int]
    _VALUE_FIELD_NUMBER: _ClassVar[int]
    _key: str
    _value: _containers.RepeatedCompositeFieldContainer[MapEntryStringInt]
    def __init__(self, _key: _Optional[str] = ..., _value: _Optional[_Iterable[_Union[MapEntryStringInt, _Mapping]]] = ...) -> None: ...

class MapEntryStringInt(_message.Message):
    __slots__ = ("_key", "_value")
    _KEY_FIELD_NUMBER: _ClassVar[int]
    _VALUE_FIELD_NUMBER: _ClassVar[int]
    _key: str
    _value: int
    def __init__(self, _key: _Optional[str] = ..., _value: _Optional[int] = ...) -> None: ...
