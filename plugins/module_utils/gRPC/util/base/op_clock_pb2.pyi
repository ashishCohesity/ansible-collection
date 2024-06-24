from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpClock(_message.Message):
    __slots__ = ("constituent_id", "incarnation_id", "operation_id")
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    constituent_id: int
    incarnation_id: int
    operation_id: int
    def __init__(self, constituent_id: _Optional[int] = ..., incarnation_id: _Optional[int] = ..., operation_id: _Optional[int] = ...) -> None: ...

class OpClockVectorSnapshot(_message.Message):
    __slots__ = ("op_clock", "timestamp_msecs")
    OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    op_clock: _containers.RepeatedCompositeFieldContainer[OpClock]
    timestamp_msecs: int
    def __init__(self, op_clock: _Optional[_Iterable[_Union[OpClock, _Mapping]]] = ..., timestamp_msecs: _Optional[int] = ...) -> None: ...

class OpClockVectorCacheBucket(_message.Message):
    __slots__ = ("duration_secs", "opclock_vector_list")
    DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    OPCLOCK_VECTOR_LIST_FIELD_NUMBER: _ClassVar[int]
    duration_secs: int
    opclock_vector_list: _containers.RepeatedCompositeFieldContainer[OpClockVectorSnapshot]
    def __init__(self, duration_secs: _Optional[int] = ..., opclock_vector_list: _Optional[_Iterable[_Union[OpClockVectorSnapshot, _Mapping]]] = ...) -> None: ...
