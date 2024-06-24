from elrond.slave import log_checkpoint_pb2 as _log_checkpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransitionModelProto(_message.Message):
    __slots__ = ("bucket_creation_time_usecs", "transition_vec", "marked_for_decay", "checkpoint_vec")
    class TransitionCount(_message.Message):
        __slots__ = ("previous_brick_vec", "future_brick_vec")
        class FutureTransition(_message.Message):
            __slots__ = ("brick", "transition_frequency")
            BRICK_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            brick: int
            transition_frequency: float
            def __init__(self, brick: _Optional[int] = ..., transition_frequency: _Optional[float] = ...) -> None: ...
        PREVIOUS_BRICK_VEC_FIELD_NUMBER: _ClassVar[int]
        FUTURE_BRICK_VEC_FIELD_NUMBER: _ClassVar[int]
        previous_brick_vec: _containers.RepeatedScalarFieldContainer[int]
        future_brick_vec: _containers.RepeatedCompositeFieldContainer[TransitionModelProto.TransitionCount.FutureTransition]
        def __init__(self, previous_brick_vec: _Optional[_Iterable[int]] = ..., future_brick_vec: _Optional[_Iterable[_Union[TransitionModelProto.TransitionCount.FutureTransition, _Mapping]]] = ...) -> None: ...
    BUCKET_CREATION_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_VEC_FIELD_NUMBER: _ClassVar[int]
    MARKED_FOR_DECAY_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_VEC_FIELD_NUMBER: _ClassVar[int]
    bucket_creation_time_usecs: int
    transition_vec: _containers.RepeatedCompositeFieldContainer[TransitionModelProto.TransitionCount]
    marked_for_decay: bool
    checkpoint_vec: _containers.RepeatedCompositeFieldContainer[_log_checkpoint_pb2.LogCheckPointProto]
    def __init__(self, bucket_creation_time_usecs: _Optional[int] = ..., transition_vec: _Optional[_Iterable[_Union[TransitionModelProto.TransitionCount, _Mapping]]] = ..., marked_for_decay: bool = ..., checkpoint_vec: _Optional[_Iterable[_Union[_log_checkpoint_pb2.LogCheckPointProto, _Mapping]]] = ...) -> None: ...
