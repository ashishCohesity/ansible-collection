from bridge.smb_portal import smb_portal_metadata_pb2 as _smb_portal_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmbSessionInfoProto(_message.Message):
    __slots__ = ("is_active", "entity_ids")
    class EntityIdInfo(_message.Message):
        __slots__ = ("entity_id", "entity_id_proto")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_PROTO_FIELD_NUMBER: _ClassVar[int]
        entity_id: int
        entity_id_proto: _smb_portal_metadata_pb2.SmbEntityIdProto
        def __init__(self, entity_id: _Optional[int] = ..., entity_id_proto: _Optional[_Union[_smb_portal_metadata_pb2.SmbEntityIdProto, _Mapping]] = ...) -> None: ...
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    is_active: bool
    entity_ids: _containers.RepeatedCompositeFieldContainer[SmbSessionInfoProto.EntityIdInfo]
    def __init__(self, is_active: bool = ..., entity_ids: _Optional[_Iterable[_Union[SmbSessionInfoProto.EntityIdInfo, _Mapping]]] = ...) -> None: ...
