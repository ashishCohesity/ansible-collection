from bridge.s3_portal.keystone import keystone2_pb2 as _keystone2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class System(_message.Message):
    __slots__ = ("all",)
    ALL_FIELD_NUMBER: _ClassVar[int]
    all: bool
    def __init__(self, all: bool = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("id", "name", "domain_id", "links", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    domain_id: str
    links: _keystone2_pb2.Links
    description: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., domain_id: _Optional[str] = ..., links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class Endpoint(_message.Message):
    __slots__ = ("id", "url", "enabled", "interface", "service_id", "region", "region_id", "links")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    enabled: bool
    interface: str
    service_id: str
    region: str
    region_id: str
    links: _keystone2_pb2.Links
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., enabled: bool = ..., interface: _Optional[str] = ..., service_id: _Optional[str] = ..., region: _Optional[str] = ..., region_id: _Optional[str] = ..., links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("id", "name", "type", "enabled", "description", "links")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    enabled: bool
    description: str
    links: _keystone2_pb2.Links
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., enabled: bool = ..., description: _Optional[str] = ..., links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ...) -> None: ...

class Catalog(_message.Message):
    __slots__ = ("id", "name", "type", "endpoints")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    endpoints: _containers.RepeatedCompositeFieldContainer[Endpoint]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., endpoints: _Optional[_Iterable[_Union[Endpoint, _Mapping]]] = ...) -> None: ...

class TokenInfo(_message.Message):
    __slots__ = ("issued_at", "expires_at", "methods", "user", "audit_ids", "catalog", "roles", "system", "domain", "is_domain", "project")
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    AUDIT_IDS_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    IS_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    issued_at: str
    expires_at: str
    methods: _containers.RepeatedScalarFieldContainer[str]
    user: _keystone2_pb2.User
    audit_ids: _containers.RepeatedScalarFieldContainer[str]
    catalog: _containers.RepeatedCompositeFieldContainer[Catalog]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    system: System
    domain: _keystone2_pb2.Domain
    is_domain: bool
    project: _keystone2_pb2.Project
    def __init__(self, issued_at: _Optional[str] = ..., expires_at: _Optional[str] = ..., methods: _Optional[_Iterable[str]] = ..., user: _Optional[_Union[_keystone2_pb2.User, _Mapping]] = ..., audit_ids: _Optional[_Iterable[str]] = ..., catalog: _Optional[_Iterable[_Union[Catalog, _Mapping]]] = ..., roles: _Optional[_Iterable[_Union[Role, _Mapping]]] = ..., system: _Optional[_Union[System, _Mapping]] = ..., domain: _Optional[_Union[_keystone2_pb2.Domain, _Mapping]] = ..., is_domain: bool = ..., project: _Optional[_Union[_keystone2_pb2.Project, _Mapping]] = ...) -> None: ...

class Scope(_message.Message):
    __slots__ = ("system", "domain", "project")
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    system: System
    domain: _keystone2_pb2.Domain
    project: _keystone2_pb2.Project
    def __init__(self, system: _Optional[_Union[System, _Mapping]] = ..., domain: _Optional[_Union[_keystone2_pb2.Domain, _Mapping]] = ..., project: _Optional[_Union[_keystone2_pb2.Project, _Mapping]] = ...) -> None: ...
