from bridge.base import error_pb2 as _error_pb2
from util.base import op_clock_pb2 as _op_clock_pb2
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BridgeActionUpdateArg(_message.Message):
    __slots__ = ("op_clock", "task_id", "sub_task_id", "error")
    Extensions: _python_message._ExtensionDict
    OP_CLOCK_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    op_clock: _op_clock_pb2.OpClock
    task_id: int
    sub_task_id: int
    error: _error_pb2.ErrorProto
    def __init__(self, op_clock: _Optional[_Union[_op_clock_pb2.OpClock, _Mapping]] = ..., task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class BridgeActionUpdateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
