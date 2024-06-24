from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemTracerProto(_message.Message):
    __slots__ = ("component_value_map",)
    class ValueProto(_message.Message):
        __slots__ = ("op_value_map",)
        class OpProto(_message.Message):
            __slots__ = ("bucket_value_map",)
            class BucketProto(_message.Message):
                __slots__ = ("num_data_points", "mean", "median", "eighty_ptl", "ninety_five_ptl", "ninety_nine_ptl")
                NUM_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
                MEAN_FIELD_NUMBER: _ClassVar[int]
                MEDIAN_FIELD_NUMBER: _ClassVar[int]
                EIGHTY_PTL_FIELD_NUMBER: _ClassVar[int]
                NINETY_FIVE_PTL_FIELD_NUMBER: _ClassVar[int]
                NINETY_NINE_PTL_FIELD_NUMBER: _ClassVar[int]
                num_data_points: int
                mean: int
                median: int
                eighty_ptl: int
                ninety_five_ptl: int
                ninety_nine_ptl: int
                def __init__(self, num_data_points: _Optional[int] = ..., mean: _Optional[int] = ..., median: _Optional[int] = ..., eighty_ptl: _Optional[int] = ..., ninety_five_ptl: _Optional[int] = ..., ninety_nine_ptl: _Optional[int] = ...) -> None: ...
            class BucketValueMapEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: int
                value: MemTracerProto.ValueProto.OpProto.BucketProto
                def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MemTracerProto.ValueProto.OpProto.BucketProto, _Mapping]] = ...) -> None: ...
            BUCKET_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
            bucket_value_map: _containers.MessageMap[int, MemTracerProto.ValueProto.OpProto.BucketProto]
            def __init__(self, bucket_value_map: _Optional[_Mapping[int, MemTracerProto.ValueProto.OpProto.BucketProto]] = ...) -> None: ...
        class OpValueMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: MemTracerProto.ValueProto.OpProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MemTracerProto.ValueProto.OpProto, _Mapping]] = ...) -> None: ...
        OP_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
        op_value_map: _containers.MessageMap[str, MemTracerProto.ValueProto.OpProto]
        def __init__(self, op_value_map: _Optional[_Mapping[str, MemTracerProto.ValueProto.OpProto]] = ...) -> None: ...
    class ComponentValueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MemTracerProto.ValueProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MemTracerProto.ValueProto, _Mapping]] = ...) -> None: ...
    COMPONENT_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    component_value_map: _containers.MessageMap[str, MemTracerProto.ValueProto]
    def __init__(self, component_value_map: _Optional[_Mapping[str, MemTracerProto.ValueProto]] = ...) -> None: ...
