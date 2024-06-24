from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterLogsProto(_message.Message):
    __slots__ = ("log_vec",)
    class Log(_message.Message):
        __slots__ = ("timestamp_msecs", "message", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            info: _ClassVar[ClusterLogsProto.Log.Type]
            warning: _ClassVar[ClusterLogsProto.Log.Type]
            error: _ClassVar[ClusterLogsProto.Log.Type]
        info: ClusterLogsProto.Log.Type
        warning: ClusterLogsProto.Log.Type
        error: ClusterLogsProto.Log.Type
        TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        timestamp_msecs: int
        message: str
        type: ClusterLogsProto.Log.Type
        def __init__(self, timestamp_msecs: _Optional[int] = ..., message: _Optional[str] = ..., type: _Optional[_Union[ClusterLogsProto.Log.Type, str]] = ...) -> None: ...
    LOG_VEC_FIELD_NUMBER: _ClassVar[int]
    log_vec: _containers.RepeatedCompositeFieldContainer[ClusterLogsProto.Log]
    def __init__(self, log_vec: _Optional[_Iterable[_Union[ClusterLogsProto.Log, _Mapping]]] = ...) -> None: ...
