from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MergeSortTaskType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[MergeSortTaskType.Type]
        kMergeSort: _ClassVar[MergeSortTaskType.Type]
        kTaskCount: _ClassVar[MergeSortTaskType.Type]
    kUnknown: MergeSortTaskType.Type
    kMergeSort: MergeSortTaskType.Type
    kTaskCount: MergeSortTaskType.Type
    def __init__(self) -> None: ...

class MergeSortArg(_message.Message):
    __slots__ = ("numbers", "max_splits")
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    MAX_SPLITS_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    max_splits: int
    def __init__(self, numbers: _Optional[_Iterable[int]] = ..., max_splits: _Optional[int] = ...) -> None: ...

class MergeSortResult(_message.Message):
    __slots__ = ("numbers", "missing_numbers_due_to_cancellation")
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    MISSING_NUMBERS_DUE_TO_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    missing_numbers_due_to_cancellation: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, numbers: _Optional[_Iterable[int]] = ..., missing_numbers_due_to_cancellation: _Optional[_Iterable[int]] = ...) -> None: ...

class MergeSortState(_message.Message):
    __slots__ = ("subtasks",)
    class SubTask(_message.Message):
        __slots__ = ("name", "arg", "result")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARG_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        name: str
        arg: MergeSortArg
        result: MergeSortResult
        def __init__(self, name: _Optional[str] = ..., arg: _Optional[_Union[MergeSortArg, _Mapping]] = ..., result: _Optional[_Union[MergeSortResult, _Mapping]] = ...) -> None: ...
    SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    subtasks: _containers.RepeatedCompositeFieldContainer[MergeSortState.SubTask]
    def __init__(self, subtasks: _Optional[_Iterable[_Union[MergeSortState.SubTask, _Mapping]]] = ...) -> None: ...
