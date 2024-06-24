from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloWorldTaskType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[HelloWorldTaskType.Type]
        kEmitString: _ClassVar[HelloWorldTaskType.Type]
        kEmitStringUsingSubtasks: _ClassVar[HelloWorldTaskType.Type]
        kEmitChar: _ClassVar[HelloWorldTaskType.Type]
        kTaskCount: _ClassVar[HelloWorldTaskType.Type]
    kUnknown: HelloWorldTaskType.Type
    kEmitString: HelloWorldTaskType.Type
    kEmitStringUsingSubtasks: HelloWorldTaskType.Type
    kEmitChar: HelloWorldTaskType.Type
    kTaskCount: HelloWorldTaskType.Type
    def __init__(self) -> None: ...

class EmitStringArg(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class EmitStringResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmitStringState(_message.Message):
    __slots__ = ("num_chars_done",)
    NUM_CHARS_DONE_FIELD_NUMBER: _ClassVar[int]
    num_chars_done: int
    def __init__(self, num_chars_done: _Optional[int] = ...) -> None: ...

class EmitStringUsingSubtasksArg(_message.Message):
    __slots__ = ("value", "parallelism", "sleep_time_msecs")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    SLEEP_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    value: str
    parallelism: int
    sleep_time_msecs: int
    def __init__(self, value: _Optional[str] = ..., parallelism: _Optional[int] = ..., sleep_time_msecs: _Optional[int] = ...) -> None: ...

class EmitStringUsingSubtasksResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmitStringUsingSubtasksState(_message.Message):
    __slots__ = ("num_chars_started", "num_chars_done", "num_chars_in_progress")
    NUM_CHARS_STARTED_FIELD_NUMBER: _ClassVar[int]
    NUM_CHARS_DONE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHARS_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    num_chars_started: int
    num_chars_done: int
    num_chars_in_progress: int
    def __init__(self, num_chars_started: _Optional[int] = ..., num_chars_done: _Optional[int] = ..., num_chars_in_progress: _Optional[int] = ...) -> None: ...

class EmitCharArg(_message.Message):
    __slots__ = ("character", "pos", "sleep_time_msecs")
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SLEEP_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    character: int
    pos: int
    sleep_time_msecs: int
    def __init__(self, character: _Optional[int] = ..., pos: _Optional[int] = ..., sleep_time_msecs: _Optional[int] = ...) -> None: ...

class EmitCharResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmitCharState(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
