from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Clearance(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("uuid", "clearances")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CLEARANCES_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    clearances: _containers.RepeatedCompositeFieldContainer[Clearance]
    def __init__(self, uuid: _Optional[str] = ..., clearances: _Optional[_Iterable[_Union[Clearance, _Mapping]]] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: Entity
    def __init__(self, entity: _Optional[_Union[Entity, _Mapping]] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("name", "dn", "display_name", "member_vec")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_VEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    dn: str
    display_name: str
    member_vec: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, name: _Optional[str] = ..., dn: _Optional[str] = ..., display_name: _Optional[str] = ..., member_vec: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class Groups(_message.Message):
    __slots__ = ("uuid", "group_vec")
    UUID_FIELD_NUMBER: _ClassVar[int]
    GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    group_vec: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, uuid: _Optional[str] = ..., group_vec: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...

class GroupResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: Groups
    def __init__(self, entity: _Optional[_Union[Groups, _Mapping]] = ...) -> None: ...
