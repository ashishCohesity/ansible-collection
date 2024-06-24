from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagID(_message.Message):
    __slots__ = ("tenant_id", "tag_namespace", "name", "uuid")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    tag_namespace: str
    name: str
    uuid: str
    def __init__(self, tenant_id: _Optional[str] = ..., tag_namespace: _Optional[str] = ..., name: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("tag_id", "modified_time_usecs", "created_time_usecs", "active", "description", "ui_color", "ui_path_vec", "removed_from_global_entity", "removed_from_cfileindex")
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UI_COLOR_FIELD_NUMBER: _ClassVar[int]
    UI_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FROM_GLOBAL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FROM_CFILEINDEX_FIELD_NUMBER: _ClassVar[int]
    tag_id: TagID
    modified_time_usecs: int
    created_time_usecs: int
    active: bool
    description: str
    ui_color: str
    ui_path_vec: _containers.RepeatedScalarFieldContainer[str]
    removed_from_global_entity: bool
    removed_from_cfileindex: bool
    def __init__(self, tag_id: _Optional[_Union[TagID, _Mapping]] = ..., modified_time_usecs: _Optional[int] = ..., created_time_usecs: _Optional[int] = ..., active: bool = ..., description: _Optional[str] = ..., ui_color: _Optional[str] = ..., ui_path_vec: _Optional[_Iterable[str]] = ..., removed_from_global_entity: bool = ..., removed_from_cfileindex: bool = ...) -> None: ...
