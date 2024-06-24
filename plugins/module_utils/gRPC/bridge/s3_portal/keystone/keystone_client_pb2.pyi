from bridge.s3_portal.keystone import keystone2_pb2 as _keystone2_pb2
from bridge.s3_portal.keystone import keystone_pb2 as _keystone_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PasswordIdentity(_message.Message):
    __slots__ = ("methods", "password")
    class Password(_message.Message):
        __slots__ = ("user",)
        USER_FIELD_NUMBER: _ClassVar[int]
        user: _keystone2_pb2.User
        def __init__(self, user: _Optional[_Union[_keystone2_pb2.User, _Mapping]] = ...) -> None: ...
    METHODS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    methods: _containers.RepeatedScalarFieldContainer[str]
    password: PasswordIdentity.Password
    def __init__(self, methods: _Optional[_Iterable[str]] = ..., password: _Optional[_Union[PasswordIdentity.Password, _Mapping]] = ...) -> None: ...

class PasswordAuthentication(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ("auth",)
        class Auth(_message.Message):
            __slots__ = ("identity", "scope")
            IDENTITY_FIELD_NUMBER: _ClassVar[int]
            SCOPE_FIELD_NUMBER: _ClassVar[int]
            identity: PasswordIdentity
            scope: _keystone_pb2.Scope
            def __init__(self, identity: _Optional[_Union[PasswordIdentity, _Mapping]] = ..., scope: _Optional[_Union[_keystone_pb2.Scope, _Mapping]] = ...) -> None: ...
        AUTH_FIELD_NUMBER: _ClassVar[int]
        auth: PasswordAuthentication.RequestBody.Auth
        def __init__(self, auth: _Optional[_Union[PasswordAuthentication.RequestBody.Auth, _Mapping]] = ...) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("token",)
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        token: _keystone_pb2.TokenInfo
        def __init__(self, token: _Optional[_Union[_keystone_pb2.TokenInfo, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class PasswordAuthenticationUnscoped(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ("auth",)
        class Auth(_message.Message):
            __slots__ = ("identity", "scope")
            IDENTITY_FIELD_NUMBER: _ClassVar[int]
            SCOPE_FIELD_NUMBER: _ClassVar[int]
            identity: PasswordIdentity
            scope: str
            def __init__(self, identity: _Optional[_Union[PasswordIdentity, _Mapping]] = ..., scope: _Optional[str] = ...) -> None: ...
        AUTH_FIELD_NUMBER: _ClassVar[int]
        auth: PasswordAuthenticationUnscoped.RequestBody.Auth
        def __init__(self, auth: _Optional[_Union[PasswordAuthenticationUnscoped.RequestBody.Auth, _Mapping]] = ...) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("token",)
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        token: _keystone_pb2.TokenInfo
        def __init__(self, token: _Optional[_Union[_keystone_pb2.TokenInfo, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class VerifyToken(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("token",)
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        token: _keystone_pb2.TokenInfo
        def __init__(self, token: _Optional[_Union[_keystone_pb2.TokenInfo, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ServiceCatalog(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("catalog", "links")
        CATALOG_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        catalog: _containers.RepeatedCompositeFieldContainer[_keystone_pb2.Catalog]
        links: _keystone2_pb2.Links
        def __init__(self, catalog: _Optional[_Iterable[_Union[_keystone_pb2.Catalog, _Mapping]]] = ..., links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListServices(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("links", "services")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        links: _keystone2_pb2.Links
        services: _containers.RepeatedCompositeFieldContainer[_keystone_pb2.Service]
        def __init__(self, links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., services: _Optional[_Iterable[_Union[_keystone_pb2.Service, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class CreateOrUpdateService(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ("service",)
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: _keystone_pb2.Service
        def __init__(self, service: _Optional[_Union[_keystone_pb2.Service, _Mapping]] = ...) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("service",)
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: _keystone_pb2.Service
        def __init__(self, service: _Optional[_Union[_keystone_pb2.Service, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ServiceDetails(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("service",)
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: _keystone_pb2.Service
        def __init__(self, service: _Optional[_Union[_keystone_pb2.Service, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListEndpoints(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("endpoints", "links")
        ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        endpoints: _containers.RepeatedCompositeFieldContainer[_keystone_pb2.Endpoint]
        links: _keystone2_pb2.Links
        def __init__(self, endpoints: _Optional[_Iterable[_Union[_keystone_pb2.Endpoint, _Mapping]]] = ..., links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class CreateOrUpdateEndpoint(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ("endpoint",)
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        endpoint: _keystone_pb2.Endpoint
        def __init__(self, endpoint: _Optional[_Union[_keystone_pb2.Endpoint, _Mapping]] = ...) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("endpoint",)
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        endpoint: _keystone_pb2.Endpoint
        def __init__(self, endpoint: _Optional[_Union[_keystone_pb2.Endpoint, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class EndpointDetails(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("endpoint",)
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        endpoint: _keystone_pb2.Endpoint
        def __init__(self, endpoint: _Optional[_Union[_keystone_pb2.Endpoint, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListRoles(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("links", "roles")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        ROLES_FIELD_NUMBER: _ClassVar[int]
        links: _keystone2_pb2.Links
        roles: _containers.RepeatedCompositeFieldContainer[_keystone_pb2.Role]
        def __init__(self, links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., roles: _Optional[_Iterable[_Union[_keystone_pb2.Role, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListDomains(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("links", "domains")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        DOMAINS_FIELD_NUMBER: _ClassVar[int]
        links: _keystone2_pb2.Links
        domains: _containers.RepeatedCompositeFieldContainer[_keystone2_pb2.Domain]
        def __init__(self, links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., domains: _Optional[_Iterable[_Union[_keystone2_pb2.Domain, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListProjects(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("links", "projects")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        PROJECTS_FIELD_NUMBER: _ClassVar[int]
        links: _keystone2_pb2.Links
        projects: _containers.RepeatedCompositeFieldContainer[_keystone2_pb2.Project]
        def __init__(self, links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., projects: _Optional[_Iterable[_Union[_keystone2_pb2.Project, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListUsers(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("links", "users")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        USERS_FIELD_NUMBER: _ClassVar[int]
        links: _keystone2_pb2.Links
        users: _containers.RepeatedCompositeFieldContainer[_keystone2_pb2.User]
        def __init__(self, links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., users: _Optional[_Iterable[_Union[_keystone2_pb2.User, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class ListRegions(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("links", "regions")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        REGIONS_FIELD_NUMBER: _ClassVar[int]
        links: _keystone2_pb2.Links
        regions: _containers.RepeatedCompositeFieldContainer[_keystone2_pb2.Region]
        def __init__(self, links: _Optional[_Union[_keystone2_pb2.Links, _Mapping]] = ..., regions: _Optional[_Iterable[_Union[_keystone2_pb2.Region, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class GetRegion(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("region",)
        REGION_FIELD_NUMBER: _ClassVar[int]
        region: _keystone2_pb2.Region
        def __init__(self, region: _Optional[_Union[_keystone2_pb2.Region, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class CreateOrUpdateRegion(_message.Message):
    __slots__ = ()
    class RequestBody(_message.Message):
        __slots__ = ("region",)
        REGION_FIELD_NUMBER: _ClassVar[int]
        region: _keystone2_pb2.Region
        def __init__(self, region: _Optional[_Union[_keystone2_pb2.Region, _Mapping]] = ...) -> None: ...
    class ResponseBody(_message.Message):
        __slots__ = ("region",)
        REGION_FIELD_NUMBER: _ClassVar[int]
        region: _keystone2_pb2.Region
        def __init__(self, region: _Optional[_Union[_keystone2_pb2.Region, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
