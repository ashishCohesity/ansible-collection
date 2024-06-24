from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Links(_message.Message):
    __slots__ = ("self", "previous", "next")
    SELF_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    self: str
    previous: str
    next: str
    def __init__(self, self_: _Optional[str] = ..., previous: _Optional[str] = ..., next: _Optional[str] = ...) -> None: ...

class Domain(_message.Message):
    __slots__ = ("id", "name", "description", "enabled", "links")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    enabled: bool
    links: Links
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enabled: bool = ..., links: _Optional[_Union[Links, _Mapping]] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ("id", "name", "domain", "domain_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    domain: Domain
    domain_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., domain: _Optional[_Union[Domain, _Mapping]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "name", "password", "password_expires_at", "domain", "domain_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    password: str
    password_expires_at: str
    domain: Domain
    domain_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ..., password_expires_at: _Optional[str] = ..., domain: _Optional[_Union[Domain, _Mapping]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ("description", "id", "links", "parent_region_id")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    PARENT_REGION_ID_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    links: Links
    parent_region_id: str
    def __init__(self, description: _Optional[str] = ..., id: _Optional[str] = ..., links: _Optional[_Union[Links, _Mapping]] = ..., parent_region_id: _Optional[str] = ...) -> None: ...
