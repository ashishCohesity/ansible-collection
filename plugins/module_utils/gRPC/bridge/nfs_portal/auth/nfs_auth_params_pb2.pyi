from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserGidsFromUidArg(_message.Message):
    __slots__ = ("ldap_provider_id", "uid")
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ldap_provider_id: int
    uid: int
    def __init__(self, ldap_provider_id: _Optional[int] = ..., uid: _Optional[int] = ...) -> None: ...

class GetUserGidsFromUidResult(_message.Message):
    __slots__ = ("uid", "gids_vec")
    UID_FIELD_NUMBER: _ClassVar[int]
    GIDS_VEC_FIELD_NUMBER: _ClassVar[int]
    uid: int
    gids_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uid: _Optional[int] = ..., gids_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetUnixIdsFromUserNameArg(_message.Message):
    __slots__ = ("user_name", "ldap_provider_id")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    ldap_provider_id: int
    def __init__(self, user_name: _Optional[str] = ..., ldap_provider_id: _Optional[int] = ...) -> None: ...

class GetUnixIdsFromUserNameResult(_message.Message):
    __slots__ = ("uid", "gid", "secondary_gids_vec")
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_GIDS_VEC_FIELD_NUMBER: _ClassVar[int]
    uid: int
    gid: int
    secondary_gids_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uid: _Optional[int] = ..., gid: _Optional[int] = ..., secondary_gids_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class ValidateLdapProviderConfigArg(_message.Message):
    __slots__ = ("ldap_provider_id",)
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    ldap_provider_id: int
    def __init__(self, ldap_provider_id: _Optional[int] = ...) -> None: ...

class ValidateLdapProviderConfigResult(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class ClearLdapProviderCacheArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearLdapProviderCacheResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNamesFromUnixIdsArg(_message.Message):
    __slots__ = ("ldap_provider_id", "uid_vec", "gid_vec")
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    UID_VEC_FIELD_NUMBER: _ClassVar[int]
    GID_VEC_FIELD_NUMBER: _ClassVar[int]
    ldap_provider_id: int
    uid_vec: _containers.RepeatedScalarFieldContainer[int]
    gid_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ldap_provider_id: _Optional[int] = ..., uid_vec: _Optional[_Iterable[int]] = ..., gid_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class GetNamesFromUnixIdsResult(_message.Message):
    __slots__ = ("uid_2_name_map", "gid_2_name_map")
    class Uid2NameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class Gid2NameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    UID_2_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    GID_2_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    uid_2_name_map: _containers.ScalarMap[int, str]
    gid_2_name_map: _containers.ScalarMap[int, str]
    def __init__(self, uid_2_name_map: _Optional[_Mapping[int, str]] = ..., gid_2_name_map: _Optional[_Mapping[int, str]] = ...) -> None: ...

class GetUnixIdsFromNamesArg(_message.Message):
    __slots__ = ("ldap_provider_id", "user_name_vec", "group_name_vec")
    LDAP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ldap_provider_id: int
    user_name_vec: _containers.RepeatedScalarFieldContainer[str]
    group_name_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ldap_provider_id: _Optional[int] = ..., user_name_vec: _Optional[_Iterable[str]] = ..., group_name_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUnixIdsFromNamesResult(_message.Message):
    __slots__ = ("name_2_uid_map", "name_2_gid_map")
    class Name2UidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class Name2GidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NAME_2_UID_MAP_FIELD_NUMBER: _ClassVar[int]
    NAME_2_GID_MAP_FIELD_NUMBER: _ClassVar[int]
    name_2_uid_map: _containers.ScalarMap[str, int]
    name_2_gid_map: _containers.ScalarMap[str, int]
    def __init__(self, name_2_uid_map: _Optional[_Mapping[str, int]] = ..., name_2_gid_map: _Optional[_Mapping[str, int]] = ...) -> None: ...
