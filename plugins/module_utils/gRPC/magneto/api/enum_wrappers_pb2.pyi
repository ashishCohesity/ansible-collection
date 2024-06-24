from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.object_graph import enums_pb2 as _enums_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentProto(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ...) -> None: ...

class OperationProto(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2_1.OperationProto.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2_1.OperationProto.Type, str]] = ...) -> None: ...

class HostEnvProto(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.HostEnv.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2.HostEnv.Type, str]] = ...) -> None: ...

class MagnetoErrorTypeProto(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _error_pb2.ErrorProto.Type
    def __init__(self, type: _Optional[_Union[_error_pb2.ErrorProto.Type, str]] = ...) -> None: ...

class MagnetoPublicStatus(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.PublicTaskStatus.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2.PublicTaskStatus.Type, str]] = ...) -> None: ...

class MagnetoBackupType(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.ScheduledBackupType.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ...) -> None: ...

class BackupQoSPrincipal(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.BackupQoSPrincipal.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2.BackupQoSPrincipal.Type, str]] = ...) -> None: ...

class NasProtocol(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.NasProtocol.Type
    def __init__(self, type: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ...) -> None: ...
