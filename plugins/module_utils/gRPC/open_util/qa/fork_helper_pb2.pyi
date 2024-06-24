from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForkHelperSvcError(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRetry: _ClassVar[ForkHelperSvcError.Type]
        kInvalidPid: _ClassVar[ForkHelperSvcError.Type]
    kRetry: ForkHelperSvcError.Type
    kInvalidPid: ForkHelperSvcError.Type
    def __init__(self) -> None: ...

class ForkHelperArg(_message.Message):
    __slots__ = ("function_addr", "command_line_options", "pid_to_kill")
    class CommandLineOption(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FUNCTION_ADDR_FIELD_NUMBER: _ClassVar[int]
    COMMAND_LINE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PID_TO_KILL_FIELD_NUMBER: _ClassVar[int]
    function_addr: int
    command_line_options: _containers.RepeatedCompositeFieldContainer[ForkHelperArg.CommandLineOption]
    pid_to_kill: int
    def __init__(self, function_addr: _Optional[int] = ..., command_line_options: _Optional[_Iterable[_Union[ForkHelperArg.CommandLineOption, _Mapping]]] = ..., pid_to_kill: _Optional[int] = ...) -> None: ...

class ForkHelperResult(_message.Message):
    __slots__ = ("pid",)
    PID_FIELD_NUMBER: _ClassVar[int]
    pid: int
    def __init__(self, pid: _Optional[int] = ...) -> None: ...
