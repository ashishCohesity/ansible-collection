from magneto.base import enums_pb2 as _enums_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("type", "uid", "name", "protocol", "path", "description", "skip_validation")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGroup: _ClassVar[Entity.Type]
        kHost: _ClassVar[Entity.Type]
        kDfsGroup: _ClassVar[Entity.Type]
        kDfsTopDir: _ClassVar[Entity.Type]
    kGroup: Entity.Type
    kHost: Entity.Type
    kDfsGroup: Entity.Type
    kDfsTopDir: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uid: _universal_id_pb2.UniversalIdProto
    name: str
    protocol: _enums_pb2.NasProtocol.Type
    path: str
    description: str
    skip_validation: bool
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ..., protocol: _Optional[_Union[_enums_pb2.NasProtocol.Type, str]] = ..., path: _Optional[str] = ..., description: _Optional[str] = ..., skip_validation: bool = ...) -> None: ...
