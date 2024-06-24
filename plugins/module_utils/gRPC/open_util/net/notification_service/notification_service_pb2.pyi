from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Int128Id(_message.Message):
    __slots__ = ("namespace_id", "value_high", "value_low")
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_HIGH_FIELD_NUMBER: _ClassVar[int]
    VALUE_LOW_FIELD_NUMBER: _ClassVar[int]
    namespace_id: int
    value_high: int
    value_low: int
    def __init__(self, namespace_id: _Optional[int] = ..., value_high: _Optional[int] = ..., value_low: _Optional[int] = ...) -> None: ...

class StringId(_message.Message):
    __slots__ = ("namespace_id", "value")
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    namespace_id: int
    value: str
    def __init__(self, namespace_id: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class EntityIdProto(_message.Message):
    __slots__ = ("protorpc_id", "string_id", "int128_id")
    PROTORPC_ID_FIELD_NUMBER: _ClassVar[int]
    STRING_ID_FIELD_NUMBER: _ClassVar[int]
    INT128_ID_FIELD_NUMBER: _ClassVar[int]
    protorpc_id: _protorpc_pb2.ProtoRpcId
    string_id: StringId
    int128_id: Int128Id
    def __init__(self, protorpc_id: _Optional[_Union[_protorpc_pb2.ProtoRpcId, _Mapping]] = ..., string_id: _Optional[_Union[StringId, _Mapping]] = ..., int128_id: _Optional[_Union[Int128Id, _Mapping]] = ...) -> None: ...
