from magneto.agents.base import error_pb2 as _error_pb2
from magneto.agents.stub import agent_base_pb2 as _agent_base_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EngineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kOracleEe: _ClassVar[EngineType]
    kOracleEeCdb: _ClassVar[EngineType]
    kOracleSe2: _ClassVar[EngineType]
    kOracleSe2Cdb: _ClassVar[EngineType]
kOracleEe: EngineType
kOracleEeCdb: EngineType
kOracleSe2: EngineType
kOracleSe2Cdb: EngineType

class PrepareInstanceArg(_message.Message):
    __slots__ = ("header", "engine_type")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENGINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    engine_type: EngineType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., engine_type: _Optional[_Union[EngineType, str]] = ...) -> None: ...

class PrepareInstanceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class BackupArg(_message.Message):
    __slots__ = ("header", "engine_type")
    Extensions: _python_message._ExtensionDict
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ENGINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    header: _agent_base_pb2.AgentBaseArg
    engine_type: EngineType
    def __init__(self, header: _Optional[_Union[_agent_base_pb2.AgentBaseArg, _Mapping]] = ..., engine_type: _Optional[_Union[EngineType, str]] = ...) -> None: ...

class BackupResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
