from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ("version", "session_id", "user_session_claims", "created_time_msecs", "last_access_time_msecs")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_SESSION_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESS_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    version: int
    session_id: str
    user_session_claims: SessionClaims
    created_time_msecs: int
    last_access_time_msecs: int
    def __init__(self, version: _Optional[int] = ..., session_id: _Optional[str] = ..., user_session_claims: _Optional[_Union[SessionClaims, _Mapping]] = ..., created_time_msecs: _Optional[int] = ..., last_access_time_msecs: _Optional[int] = ...) -> None: ...

class SessionClaims(_message.Message):
    __slots__ = ("username", "first_name", "last_name", "domain", "tenant_id", "sid", "sids_hash", "roles_str", "privileges_str", "account_id", "user_id", "in_cluster", "locale", "expiry_time", "auth_type", "idp_groups", "idp_id", "idp_user_id", "cluster_identifiers")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    SIDS_HASH_FIELD_NUMBER: _ClassVar[int]
    ROLES_STR_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_STR_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IN_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDP_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IDP_ID_FIELD_NUMBER: _ClassVar[int]
    IDP_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    username: str
    first_name: str
    last_name: str
    domain: str
    tenant_id: str
    sid: str
    sids_hash: str
    roles_str: str
    privileges_str: str
    account_id: str
    user_id: str
    in_cluster: bool
    locale: str
    expiry_time: int
    auth_type: int
    idp_groups: _containers.RepeatedScalarFieldContainer[str]
    idp_id: int
    idp_user_id: str
    cluster_identifiers: str
    def __init__(self, username: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., domain: _Optional[str] = ..., tenant_id: _Optional[str] = ..., sid: _Optional[str] = ..., sids_hash: _Optional[str] = ..., roles_str: _Optional[str] = ..., privileges_str: _Optional[str] = ..., account_id: _Optional[str] = ..., user_id: _Optional[str] = ..., in_cluster: bool = ..., locale: _Optional[str] = ..., expiry_time: _Optional[int] = ..., auth_type: _Optional[int] = ..., idp_groups: _Optional[_Iterable[str]] = ..., idp_id: _Optional[int] = ..., idp_user_id: _Optional[str] = ..., cluster_identifiers: _Optional[str] = ...) -> None: ...
