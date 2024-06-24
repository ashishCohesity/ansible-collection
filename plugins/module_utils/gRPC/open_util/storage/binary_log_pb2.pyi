from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BinaryLogRecordProto(_message.Message):
    __slots__ = ("time_usecs", "element_vec")
    class Element(_message.Message):
        __slots__ = ("protobuf_id", "size")
        PROTOBUF_ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        protobuf_id: int
        size: int
        def __init__(self, protobuf_id: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
    TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    time_usecs: int
    element_vec: _containers.RepeatedCompositeFieldContainer[BinaryLogRecordProto.Element]
    def __init__(self, time_usecs: _Optional[int] = ..., element_vec: _Optional[_Iterable[_Union[BinaryLogRecordProto.Element, _Mapping]]] = ...) -> None: ...

class BinaryLogRecordBatchProto(_message.Message):
    __slots__ = ("protobuf_name_map", "record_vec")
    class MagicNumber(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMagicNumber: _ClassVar[BinaryLogRecordBatchProto.MagicNumber]
    kMagicNumber: BinaryLogRecordBatchProto.MagicNumber
    class ProtobufNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    PROTOBUF_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
    protobuf_name_map: _containers.ScalarMap[str, int]
    record_vec: _containers.RepeatedCompositeFieldContainer[BinaryLogRecordProto]
    def __init__(self, protobuf_name_map: _Optional[_Mapping[str, int]] = ..., record_vec: _Optional[_Iterable[_Union[BinaryLogRecordProto, _Mapping]]] = ...) -> None: ...
