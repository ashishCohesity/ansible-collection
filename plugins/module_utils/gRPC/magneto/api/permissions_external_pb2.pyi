from stats.base import stats_types_pb2 as _stats_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SID(_message.Message):
    __slots__ = ("revision_level", "identifier_authority", "sub_authority")
    REVISION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    SUB_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    revision_level: int
    identifier_authority: bytes
    sub_authority: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, revision_level: _Optional[int] = ..., identifier_authority: _Optional[bytes] = ..., sub_authority: _Optional[_Iterable[int]] = ...) -> None: ...

class EntityPermissionInfoProto(_message.Message):
    __slots__ = ("permissions", "tenant_id", "is_inferred")
    class Permission(_message.Message):
        __slots__ = ("sid",)
        SID_FIELD_NUMBER: _ClassVar[int]
        sid: SID
        def __init__(self, sid: _Optional[_Union[SID, _Mapping]] = ...) -> None: ...
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_INFERRED_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[EntityPermissionInfoProto.Permission]
    tenant_id: str
    is_inferred: bool
    def __init__(self, permissions: _Optional[_Iterable[_Union[EntityPermissionInfoProto.Permission, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., is_inferred: bool = ...) -> None: ...

class UserInformationProto(_message.Message):
    __slots__ = ("pulse_attribute_vec", "sid_vec", "tenant_id_vec", "include_subtenant_objects")
    PULSE_ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SUBTENANT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    pulse_attribute_vec: _containers.RepeatedCompositeFieldContainer[_stats_types_pb2.KeyValuePair]
    sid_vec: _containers.RepeatedCompositeFieldContainer[SID]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    include_subtenant_objects: bool
    def __init__(self, pulse_attribute_vec: _Optional[_Iterable[_Union[_stats_types_pb2.KeyValuePair, _Mapping]]] = ..., sid_vec: _Optional[_Iterable[_Union[SID, _Mapping]]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., include_subtenant_objects: bool = ...) -> None: ...
