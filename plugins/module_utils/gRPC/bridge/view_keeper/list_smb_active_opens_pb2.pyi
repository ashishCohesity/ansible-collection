from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListSmbActiveOpensResult(_message.Message):
    __slots__ = ("sessions", "view_id", "view_name", "file_path")
    class ActiveSession(_message.Message):
        __slots__ = ("client_ip", "server_ip", "user_id", "domain_id", "opens")
        class ActiveOpen(_message.Message):
            __slots__ = ("access_vec", "sharing", "lease")
            class Access(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kFileReadData: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileWriteData: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileAppendData: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileReadEa: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileWriteEa: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileExecute: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileDeleteChild: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileReadAttributes: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kFileWriteAttributes: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kDelete: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kReadControl: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kWriteDac: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kWriteOwner: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kSynchronize: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kAccessSystemSecurity: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kMaximumAllowed: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kGenericAll: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kGenericExecute: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kGenericWrite: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
                kGenericRead: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
            kFileReadData: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileWriteData: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileAppendData: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileReadEa: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileWriteEa: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileExecute: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileDeleteChild: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileReadAttributes: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kFileWriteAttributes: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kDelete: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kReadControl: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kWriteDac: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kWriteOwner: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kSynchronize: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kAccessSystemSecurity: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kMaximumAllowed: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kGenericAll: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kGenericExecute: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kGenericWrite: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            kGenericRead: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access
            class LeaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                kNoCacheLease: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType]
                kReadCacheLease: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType]
                kHandleCacheLease: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType]
                kWriteCacheLease: _ClassVar[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType]
            kNoCacheLease: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType
            kReadCacheLease: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType
            kHandleCacheLease: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType
            kWriteCacheLease: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType
            class Share(_message.Message):
                __slots__ = ("other_reads_allowed", "other_writes_allowed", "other_deletes_allowed")
                OTHER_READS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
                OTHER_WRITES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
                OTHER_DELETES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
                other_reads_allowed: bool
                other_writes_allowed: bool
                other_deletes_allowed: bool
                def __init__(self, other_reads_allowed: bool = ..., other_writes_allowed: bool = ..., other_deletes_allowed: bool = ...) -> None: ...
            class LeaseInfo(_message.Message):
                __slots__ = ("lease_type_vec", "is_breaking", "lease_breaking_to_vec")
                LEASE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
                IS_BREAKING_FIELD_NUMBER: _ClassVar[int]
                LEASE_BREAKING_TO_VEC_FIELD_NUMBER: _ClassVar[int]
                lease_type_vec: _containers.RepeatedScalarFieldContainer[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType]
                is_breaking: bool
                lease_breaking_to_vec: _containers.RepeatedScalarFieldContainer[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType]
                def __init__(self, lease_type_vec: _Optional[_Iterable[_Union[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType, str]]] = ..., is_breaking: bool = ..., lease_breaking_to_vec: _Optional[_Iterable[_Union[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseType, str]]] = ...) -> None: ...
            ACCESS_VEC_FIELD_NUMBER: _ClassVar[int]
            SHARING_FIELD_NUMBER: _ClassVar[int]
            LEASE_FIELD_NUMBER: _ClassVar[int]
            access_vec: _containers.RepeatedScalarFieldContainer[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access]
            sharing: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Share
            lease: ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseInfo
            def __init__(self, access_vec: _Optional[_Iterable[_Union[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Access, str]]] = ..., sharing: _Optional[_Union[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.Share, _Mapping]] = ..., lease: _Optional[_Union[ListSmbActiveOpensResult.ActiveSession.ActiveOpen.LeaseInfo, _Mapping]] = ...) -> None: ...
        class OpensEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: ListSmbActiveOpensResult.ActiveSession.ActiveOpen
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ListSmbActiveOpensResult.ActiveSession.ActiveOpen, _Mapping]] = ...) -> None: ...
        CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        OPENS_FIELD_NUMBER: _ClassVar[int]
        client_ip: str
        server_ip: str
        user_id: str
        domain_id: str
        opens: _containers.MessageMap[int, ListSmbActiveOpensResult.ActiveSession.ActiveOpen]
        def __init__(self, client_ip: _Optional[str] = ..., server_ip: _Optional[str] = ..., user_id: _Optional[str] = ..., domain_id: _Optional[str] = ..., opens: _Optional[_Mapping[int, ListSmbActiveOpensResult.ActiveSession.ActiveOpen]] = ...) -> None: ...
    class SessionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ListSmbActiveOpensResult.ActiveSession
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ListSmbActiveOpensResult.ActiveSession, _Mapping]] = ...) -> None: ...
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.MessageMap[int, ListSmbActiveOpensResult.ActiveSession]
    view_id: int
    view_name: str
    file_path: str
    def __init__(self, sessions: _Optional[_Mapping[int, ListSmbActiveOpensResult.ActiveSession]] = ..., view_id: _Optional[int] = ..., view_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class ListSmbAllActiveOpensResult(_message.Message):
    __slots__ = ("active_opens", "cookie")
    ACTIVE_OPENS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    active_opens: _containers.RepeatedCompositeFieldContainer[ListSmbActiveOpensResult]
    cookie: str
    def __init__(self, active_opens: _Optional[_Iterable[_Union[ListSmbActiveOpensResult, _Mapping]]] = ..., cookie: _Optional[str] = ...) -> None: ...
