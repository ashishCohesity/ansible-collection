from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VarExporterProto(_message.Message):
    __slots__ = ("key_value_pair_map",)
    class ValueProto(_message.Message):
        __slots__ = ("val_bool", "val_int64", "val_int128_msb", "val_uint64", "val_uint128_msb", "val_string", "val_double", "val_vec", "val_mapkey_vec")
        VAL_BOOL_FIELD_NUMBER: _ClassVar[int]
        VAL_INT64_FIELD_NUMBER: _ClassVar[int]
        VAL_INT128_MSB_FIELD_NUMBER: _ClassVar[int]
        VAL_UINT64_FIELD_NUMBER: _ClassVar[int]
        VAL_UINT128_MSB_FIELD_NUMBER: _ClassVar[int]
        VAL_STRING_FIELD_NUMBER: _ClassVar[int]
        VAL_DOUBLE_FIELD_NUMBER: _ClassVar[int]
        VAL_VEC_FIELD_NUMBER: _ClassVar[int]
        VAL_MAPKEY_VEC_FIELD_NUMBER: _ClassVar[int]
        val_bool: bool
        val_int64: int
        val_int128_msb: int
        val_uint64: int
        val_uint128_msb: int
        val_string: str
        val_double: float
        val_vec: _containers.RepeatedCompositeFieldContainer[VarExporterProto.ValueProto]
        val_mapkey_vec: _containers.RepeatedCompositeFieldContainer[VarExporterProto.ValueProto]
        def __init__(self, val_bool: bool = ..., val_int64: _Optional[int] = ..., val_int128_msb: _Optional[int] = ..., val_uint64: _Optional[int] = ..., val_uint128_msb: _Optional[int] = ..., val_string: _Optional[str] = ..., val_double: _Optional[float] = ..., val_vec: _Optional[_Iterable[_Union[VarExporterProto.ValueProto, _Mapping]]] = ..., val_mapkey_vec: _Optional[_Iterable[_Union[VarExporterProto.ValueProto, _Mapping]]] = ...) -> None: ...
    class KeyValuePairMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: VarExporterProto.ValueProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[VarExporterProto.ValueProto, _Mapping]] = ...) -> None: ...
    KEY_VALUE_PAIR_MAP_FIELD_NUMBER: _ClassVar[int]
    key_value_pair_map: _containers.MessageMap[str, VarExporterProto.ValueProto]
    def __init__(self, key_value_pair_map: _Optional[_Mapping[str, VarExporterProto.ValueProto]] = ...) -> None: ...
