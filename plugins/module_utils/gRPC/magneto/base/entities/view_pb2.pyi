from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("type", "uid", "name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kViewBox: _ClassVar[Entity.Type]
        kView: _ClassVar[Entity.Type]
    kViewBox: Entity.Type
    kView: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uid: _universal_id_pb2.UniversalIdProto
    name: str
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
