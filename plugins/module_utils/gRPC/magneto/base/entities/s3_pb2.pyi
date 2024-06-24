from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Versioning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnversioned: _ClassVar[Versioning]
    kEnabled: _ClassVar[Versioning]
    kSuspended: _ClassVar[Versioning]
kUnversioned: Versioning
kEnabled: Versioning
kSuspended: Versioning

class TagAttributes(_message.Message):
    __slots__ = ("entity_id", "name")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    name: str
    def __init__(self, entity_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("type", "id", "name", "create_time_msecs", "tag_attributes_vec", "versioning", "region_id", "object_level_acls_enabled")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kS3Account: _ClassVar[Entity.Type]
        kS3Bucket: _ClassVar[Entity.Type]
        kS3Tag: _ClassVar[Entity.Type]
    kS3Account: Entity.Type
    kS3Bucket: Entity.Type
    kS3Tag: Entity.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    TAG_ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSIONING_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_ACLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    id: str
    name: str
    create_time_msecs: int
    tag_attributes_vec: _containers.RepeatedCompositeFieldContainer[TagAttributes]
    versioning: Versioning
    region_id: str
    object_level_acls_enabled: bool
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., create_time_msecs: _Optional[int] = ..., tag_attributes_vec: _Optional[_Iterable[_Union[TagAttributes, _Mapping]]] = ..., versioning: _Optional[_Union[Versioning, str]] = ..., region_id: _Optional[str] = ..., object_level_acls_enabled: bool = ...) -> None: ...
