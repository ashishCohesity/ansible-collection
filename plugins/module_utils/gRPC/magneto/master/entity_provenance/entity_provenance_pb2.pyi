from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityProvenanceEdgeProto(_message.Message):
    __slots__ = ("type", "from_entity_uid", "to_entity_uid")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[EntityProvenanceEdgeProto.Type]
        kReplication: _ClassVar[EntityProvenanceEdgeProto.Type]
        kFailoverRestore: _ClassVar[EntityProvenanceEdgeProto.Type]
        kVMMigration: _ClassVar[EntityProvenanceEdgeProto.Type]
    kUnused: EntityProvenanceEdgeProto.Type
    kReplication: EntityProvenanceEdgeProto.Type
    kFailoverRestore: EntityProvenanceEdgeProto.Type
    kVMMigration: EntityProvenanceEdgeProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_ENTITY_UID_FIELD_NUMBER: _ClassVar[int]
    TO_ENTITY_UID_FIELD_NUMBER: _ClassVar[int]
    type: EntityProvenanceEdgeProto.Type
    from_entity_uid: _universal_id_pb2.UniversalIdProto
    to_entity_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, type: _Optional[_Union[EntityProvenanceEdgeProto.Type, str]] = ..., from_entity_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., to_entity_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...
