from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NumberGeneratorArg(_message.Message):
    __slots__ = ("range_start", "range_size", "skip_sending_result")
    RANGE_START_FIELD_NUMBER: _ClassVar[int]
    RANGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SKIP_SENDING_RESULT_FIELD_NUMBER: _ClassVar[int]
    range_start: int
    range_size: int
    skip_sending_result: bool
    def __init__(self, range_start: _Optional[int] = ..., range_size: _Optional[int] = ..., skip_sending_result: bool = ...) -> None: ...

class NumberGeneratorResult(_message.Message):
    __slots__ = ("numbers", "missing_numbers_due_to_cancellation")
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    MISSING_NUMBERS_DUE_TO_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    missing_numbers_due_to_cancellation: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, numbers: _Optional[_Iterable[int]] = ..., missing_numbers_due_to_cancellation: _Optional[_Iterable[int]] = ...) -> None: ...

class NumberGeneratorPendingSubtaskState(_message.Message):
    __slots__ = ("subtasks", "next_number_to_generate_after_all_subtasks_done")
    class SubTask(_message.Message):
        __slots__ = ("name", "arg")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        name: str
        arg: NumberGeneratorArg
        def __init__(self, name: _Optional[str] = ..., arg: _Optional[_Union[NumberGeneratorArg, _Mapping]] = ...) -> None: ...
    SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_NUMBER_TO_GENERATE_AFTER_ALL_SUBTASKS_DONE_FIELD_NUMBER: _ClassVar[int]
    subtasks: _containers.RepeatedCompositeFieldContainer[NumberGeneratorPendingSubtaskState.SubTask]
    next_number_to_generate_after_all_subtasks_done: int
    def __init__(self, subtasks: _Optional[_Iterable[_Union[NumberGeneratorPendingSubtaskState.SubTask, _Mapping]]] = ..., next_number_to_generate_after_all_subtasks_done: _Optional[int] = ...) -> None: ...

class NumberGeneratorCheckpointState(_message.Message):
    __slots__ = ("next_number_to_generate", "pending_subtasks", "accumulated_result")
    NEXT_NUMBER_TO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATED_RESULT_FIELD_NUMBER: _ClassVar[int]
    next_number_to_generate: int
    pending_subtasks: NumberGeneratorPendingSubtaskState
    accumulated_result: NumberGeneratorResult
    def __init__(self, next_number_to_generate: _Optional[int] = ..., pending_subtasks: _Optional[_Union[NumberGeneratorPendingSubtaskState, _Mapping]] = ..., accumulated_result: _Optional[_Union[NumberGeneratorResult, _Mapping]] = ...) -> None: ...
