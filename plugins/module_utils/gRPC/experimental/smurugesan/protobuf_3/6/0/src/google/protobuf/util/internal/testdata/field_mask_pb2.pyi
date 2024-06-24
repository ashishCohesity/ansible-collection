from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NestedFieldMask(_message.Message):
    __slots__ = ("data", "single_mask", "repeated_mask")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SINGLE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MASK_FIELD_NUMBER: _ClassVar[int]
    data: str
    single_mask: _field_mask_pb2.FieldMask
    repeated_mask: _containers.RepeatedCompositeFieldContainer[_field_mask_pb2.FieldMask]
    def __init__(self, data: _Optional[str] = ..., single_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., repeated_mask: _Optional[_Iterable[_Union[_field_mask_pb2.FieldMask, _Mapping]]] = ...) -> None: ...

class FieldMaskTest(_message.Message):
    __slots__ = ("id", "single_mask", "repeated_mask", "nested_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    SINGLE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MASK_FIELD_NUMBER: _ClassVar[int]
    NESTED_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    single_mask: _field_mask_pb2.FieldMask
    repeated_mask: _containers.RepeatedCompositeFieldContainer[_field_mask_pb2.FieldMask]
    nested_mask: _containers.RepeatedCompositeFieldContainer[NestedFieldMask]
    def __init__(self, id: _Optional[str] = ..., single_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., repeated_mask: _Optional[_Iterable[_Union[_field_mask_pb2.FieldMask, _Mapping]]] = ..., nested_mask: _Optional[_Iterable[_Union[NestedFieldMask, _Mapping]]] = ...) -> None: ...

class FieldMaskTestCases(_message.Message):
    __slots__ = ("single_mask", "multiple_mask", "snake_camel", "empty_field", "apiary_format1", "apiary_format2", "apiary_format3", "map_key1", "map_key2", "map_key3", "map_key4", "map_key5")
    SINGLE_MASK_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_MASK_FIELD_NUMBER: _ClassVar[int]
    SNAKE_CAMEL_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_FIELD_NUMBER: _ClassVar[int]
    APIARY_FORMAT1_FIELD_NUMBER: _ClassVar[int]
    APIARY_FORMAT2_FIELD_NUMBER: _ClassVar[int]
    APIARY_FORMAT3_FIELD_NUMBER: _ClassVar[int]
    MAP_KEY1_FIELD_NUMBER: _ClassVar[int]
    MAP_KEY2_FIELD_NUMBER: _ClassVar[int]
    MAP_KEY3_FIELD_NUMBER: _ClassVar[int]
    MAP_KEY4_FIELD_NUMBER: _ClassVar[int]
    MAP_KEY5_FIELD_NUMBER: _ClassVar[int]
    single_mask: FieldMaskWrapper
    multiple_mask: FieldMaskWrapper
    snake_camel: FieldMaskWrapper
    empty_field: FieldMaskWrapper
    apiary_format1: FieldMaskWrapper
    apiary_format2: FieldMaskWrapper
    apiary_format3: FieldMaskWrapper
    map_key1: FieldMaskWrapper
    map_key2: FieldMaskWrapper
    map_key3: FieldMaskWrapper
    map_key4: FieldMaskWrapper
    map_key5: FieldMaskWrapper
    def __init__(self, single_mask: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., multiple_mask: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., snake_camel: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., empty_field: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., apiary_format1: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., apiary_format2: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., apiary_format3: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., map_key1: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., map_key2: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., map_key3: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., map_key4: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ..., map_key5: _Optional[_Union[FieldMaskWrapper, _Mapping]] = ...) -> None: ...

class FieldMaskWrapper(_message.Message):
    __slots__ = ("mask",)
    MASK_FIELD_NUMBER: _ClassVar[int]
    mask: _field_mask_pb2.FieldMask
    def __init__(self, mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
