from bridge.base import error_pb2 as _error_pb2
from bridge.smb_portal import smb_portal_metadata_pb2 as _smb_portal_metadata_pb2
from bridge.stub import rpc_service_pb2 as _rpc_service_pb2
from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionStateProto(_message.Message):
    __slots__ = ("smb_session_metadata_proto", "scribe_version", "current_session_setup_connection_id")
    SMB_SESSION_METADATA_PROTO_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SESSION_SETUP_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    smb_session_metadata_proto: _smb_portal_metadata_pb2.SmbSessionMetadataProto
    scribe_version: int
    current_session_setup_connection_id: int
    def __init__(self, smb_session_metadata_proto: _Optional[_Union[_smb_portal_metadata_pb2.SmbSessionMetadataProto, _Mapping]] = ..., scribe_version: _Optional[int] = ..., current_session_setup_connection_id: _Optional[int] = ...) -> None: ...

class AuthenticateSessionArg(_message.Message):
    __slots__ = ("session_state", "client_security_buffer_bytes")
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECURITY_BUFFER_BYTES_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    client_security_buffer_bytes: bytes
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ..., client_security_buffer_bytes: _Optional[bytes] = ...) -> None: ...

class AuthenticateSessionResult(_message.Message):
    __slots__ = ("error", "client_security_buffer_bytes", "smb_auth_type", "session_state")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECURITY_BUFFER_BYTES_FIELD_NUMBER: _ClassVar[int]
    SMB_AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    client_security_buffer_bytes: bytes
    smb_auth_type: str
    session_state: SessionStateProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., client_security_buffer_bytes: _Optional[bytes] = ..., smb_auth_type: _Optional[str] = ..., session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class GetUnixIdsFromSidsArg(_message.Message):
    __slots__ = ("domain_name", "sid_vec")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, domain_name: _Optional[str] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class GetUnixIdsFromSidsResult(_message.Message):
    __slots__ = ("get_unix_ids_from_sids_map",)
    class GetUnixIdsFromSidsPair(_message.Message):
        __slots__ = ("sid", "unix_id")
        SID_FIELD_NUMBER: _ClassVar[int]
        UNIX_ID_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        unix_id: int
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., unix_id: _Optional[int] = ...) -> None: ...
    GET_UNIX_IDS_FROM_SIDS_MAP_FIELD_NUMBER: _ClassVar[int]
    get_unix_ids_from_sids_map: _containers.RepeatedCompositeFieldContainer[GetUnixIdsFromSidsResult.GetUnixIdsFromSidsPair]
    def __init__(self, get_unix_ids_from_sids_map: _Optional[_Iterable[_Union[GetUnixIdsFromSidsResult.GetUnixIdsFromSidsPair, _Mapping]]] = ...) -> None: ...

class GetUnixIdsFromSidArg(_message.Message):
    __slots__ = ("account_sid",)
    ACCOUNT_SID_FIELD_NUMBER: _ClassVar[int]
    account_sid: str
    def __init__(self, account_sid: _Optional[str] = ...) -> None: ...

class GetUnixIdsFromSidResult(_message.Message):
    __slots__ = ("uid", "gid")
    UID_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    uid: int
    gid: int
    def __init__(self, uid: _Optional[int] = ..., gid: _Optional[int] = ...) -> None: ...

class LookupUnixIdsArg(_message.Message):
    __slots__ = ("domain_name", "uid_vec", "gid_vec")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_VEC_FIELD_NUMBER: _ClassVar[int]
    GID_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    uid_vec: _containers.RepeatedScalarFieldContainer[int]
    gid_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, domain_name: _Optional[str] = ..., uid_vec: _Optional[_Iterable[int]] = ..., gid_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class LookupUnixIdsResult(_message.Message):
    __slots__ = ("uid_to_sid_map", "gid_to_sid_map")
    class UidToSidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cluster_config_pb2.ClusterConfigProto.SID
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...
    class GidToSidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _cluster_config_pb2.ClusterConfigProto.SID
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...
    UID_TO_SID_MAP_FIELD_NUMBER: _ClassVar[int]
    GID_TO_SID_MAP_FIELD_NUMBER: _ClassVar[int]
    uid_to_sid_map: _containers.MessageMap[int, _cluster_config_pb2.ClusterConfigProto.SID]
    gid_to_sid_map: _containers.MessageMap[int, _cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, uid_to_sid_map: _Optional[_Mapping[int, _cluster_config_pb2.ClusterConfigProto.SID]] = ..., gid_to_sid_map: _Optional[_Mapping[int, _cluster_config_pb2.ClusterConfigProto.SID]] = ...) -> None: ...

class GetAdUserInfoArg(_message.Message):
    __slots__ = ("domain_name", "uid_vec", "sid_vec")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_VEC_FIELD_NUMBER: _ClassVar[int]
    SID_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    uid_vec: _containers.RepeatedScalarFieldContainer[int]
    sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, domain_name: _Optional[str] = ..., uid_vec: _Optional[_Iterable[int]] = ..., sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class AdUserInfo(_message.Message):
    __slots__ = ("principal_name", "account_name", "display_name", "domain_name", "email_id", "object_class")
    PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
    principal_name: str
    account_name: str
    display_name: str
    domain_name: str
    email_id: str
    object_class: _rpc_service_pb2.GetAdInfoFromSidsResult.AdInfo.ObjectClass
    def __init__(self, principal_name: _Optional[str] = ..., account_name: _Optional[str] = ..., display_name: _Optional[str] = ..., domain_name: _Optional[str] = ..., email_id: _Optional[str] = ..., object_class: _Optional[_Union[_rpc_service_pb2.GetAdInfoFromSidsResult.AdInfo.ObjectClass, str]] = ...) -> None: ...

class GetAdUserInfoResult(_message.Message):
    __slots__ = ("uid_to_ad_user_info_map", "sid_to_ad_user_info_map")
    class UidToAdUserInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AdUserInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AdUserInfo, _Mapping]] = ...) -> None: ...
    class SidToAdUserInfoPair(_message.Message):
        __slots__ = ("sid", "ad_user_info")
        SID_FIELD_NUMBER: _ClassVar[int]
        AD_USER_INFO_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        ad_user_info: AdUserInfo
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., ad_user_info: _Optional[_Union[AdUserInfo, _Mapping]] = ...) -> None: ...
    UID_TO_AD_USER_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    SID_TO_AD_USER_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    uid_to_ad_user_info_map: _containers.MessageMap[int, AdUserInfo]
    sid_to_ad_user_info_map: _containers.RepeatedCompositeFieldContainer[GetAdUserInfoResult.SidToAdUserInfoPair]
    def __init__(self, uid_to_ad_user_info_map: _Optional[_Mapping[int, AdUserInfo]] = ..., sid_to_ad_user_info_map: _Optional[_Iterable[_Union[GetAdUserInfoResult.SidToAdUserInfoPair, _Mapping]]] = ...) -> None: ...

class SearchNamesArg(_message.Message):
    __slots__ = ("input_name", "domain_name")
    INPUT_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    input_name: str
    domain_name: str
    def __init__(self, input_name: _Optional[str] = ..., domain_name: _Optional[str] = ...) -> None: ...

class SearchNamesResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.SearchNamesInDomainResult.SearchResult]
    def __init__(self, result: _Optional[_Iterable[_Union[_rpc_service_pb2.SearchNamesInDomainResult.SearchResult, _Mapping]]] = ...) -> None: ...

class SearchLdapArg(_message.Message):
    __slots__ = ("domain_name", "search_base", "search_scope", "search_filter", "max_results", "attributes_vec")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_BASE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    search_base: str
    search_scope: int
    search_filter: str
    max_results: int
    attributes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain_name: _Optional[str] = ..., search_base: _Optional[str] = ..., search_scope: _Optional[int] = ..., search_filter: _Optional[str] = ..., max_results: _Optional[int] = ..., attributes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchLdapResult(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_rpc_service_pb2.SearchLdapResult.LdapResult]
    def __init__(self, result: _Optional[_Iterable[_Union[_rpc_service_pb2.SearchLdapResult.LdapResult, _Mapping]]] = ...) -> None: ...

class GetUnixIdAdGroupSidsArg(_message.Message):
    __slots__ = ("uid", "domain_name")
    UID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    uid: int
    domain_name: str
    def __init__(self, uid: _Optional[int] = ..., domain_name: _Optional[str] = ...) -> None: ...

class GetUnixIdAdGroupSidsResult(_message.Message):
    __slots__ = ("user_sid", "group_sid_vec")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SID_VEC_FIELD_NUMBER: _ClassVar[int]
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    group_sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., group_sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class UpdateUnixIdsArg(_message.Message):
    __slots__ = ("session_state",)
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class UpdateUnixIdsResult(_message.Message):
    __slots__ = ("session_state",)
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class UpdateSidsArg(_message.Message):
    __slots__ = ("session_state",)
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class UpdateSidsResult(_message.Message):
    __slots__ = ("session_state",)
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class LookupSidsArg(_message.Message):
    __slots__ = ("sid_string_vec", "domain_name")
    SID_STRING_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    sid_string_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name: str
    def __init__(self, sid_string_vec: _Optional[_Iterable[str]] = ..., domain_name: _Optional[str] = ...) -> None: ...

class LookupSidsResult(_message.Message):
    __slots__ = ("domain_to_sid_map", "sid_name_tuple_vec")
    class DomainToSidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _cluster_config_pb2.ClusterConfigProto.SID
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...
    class SidNameTuple(_message.Message):
        __slots__ = ("sid_name", "domain", "sid_type")
        SID_NAME_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        SID_TYPE_FIELD_NUMBER: _ClassVar[int]
        sid_name: str
        domain: str
        sid_type: int
        def __init__(self, sid_name: _Optional[str] = ..., domain: _Optional[str] = ..., sid_type: _Optional[int] = ...) -> None: ...
    DOMAIN_TO_SID_MAP_FIELD_NUMBER: _ClassVar[int]
    SID_NAME_TUPLE_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_to_sid_map: _containers.MessageMap[str, _cluster_config_pb2.ClusterConfigProto.SID]
    sid_name_tuple_vec: _containers.RepeatedCompositeFieldContainer[LookupSidsResult.SidNameTuple]
    def __init__(self, domain_to_sid_map: _Optional[_Mapping[str, _cluster_config_pb2.ClusterConfigProto.SID]] = ..., sid_name_tuple_vec: _Optional[_Iterable[_Union[LookupSidsResult.SidNameTuple, _Mapping]]] = ...) -> None: ...

class LookupNamesArg(_message.Message):
    __slots__ = ("name_vec", "domain_name")
    NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    name_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name: str
    def __init__(self, name_vec: _Optional[_Iterable[str]] = ..., domain_name: _Optional[str] = ...) -> None: ...

class LookupNamesResult(_message.Message):
    __slots__ = ("domain_to_sid_map", "sid_tuple_vec")
    class DomainToSidMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _cluster_config_pb2.ClusterConfigProto.SID
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ...) -> None: ...
    class SidTuple(_message.Message):
        __slots__ = ("sid", "domain", "sid_type")
        SID_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        SID_TYPE_FIELD_NUMBER: _ClassVar[int]
        sid: _cluster_config_pb2.ClusterConfigProto.SID
        domain: str
        sid_type: int
        def __init__(self, sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., domain: _Optional[str] = ..., sid_type: _Optional[int] = ...) -> None: ...
    DOMAIN_TO_SID_MAP_FIELD_NUMBER: _ClassVar[int]
    SID_TUPLE_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_to_sid_map: _containers.MessageMap[str, _cluster_config_pb2.ClusterConfigProto.SID]
    sid_tuple_vec: _containers.RepeatedCompositeFieldContainer[LookupNamesResult.SidTuple]
    def __init__(self, domain_to_sid_map: _Optional[_Mapping[str, _cluster_config_pb2.ClusterConfigProto.SID]] = ..., sid_tuple_vec: _Optional[_Iterable[_Union[LookupNamesResult.SidTuple, _Mapping]]] = ...) -> None: ...

class AuthenticateUserArg(_message.Message):
    __slots__ = ("domain_name", "user_name", "user_password", "exclude_group_membership_cache")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_GROUP_MEMBERSHIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    user_name: str
    user_password: str
    exclude_group_membership_cache: bool
    def __init__(self, domain_name: _Optional[str] = ..., user_name: _Optional[str] = ..., user_password: _Optional[str] = ..., exclude_group_membership_cache: bool = ...) -> None: ...

class AuthenticateUserResult(_message.Message):
    __slots__ = ("user_sid", "group_sid_vec")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SID_VEC_FIELD_NUMBER: _ClassVar[int]
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    group_sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., group_sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class GetAdUserGroupSidsArg(_message.Message):
    __slots__ = ("user_sid", "exclude_group_membership_cache")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_GROUP_MEMBERSHIP_CACHE_FIELD_NUMBER: _ClassVar[int]
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    exclude_group_membership_cache: bool
    def __init__(self, user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., exclude_group_membership_cache: bool = ...) -> None: ...

class GetAdUserGroupSidsResult(_message.Message):
    __slots__ = ("user_sid", "group_sid_vec")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SID_VEC_FIELD_NUMBER: _ClassVar[int]
    user_sid: _cluster_config_pb2.ClusterConfigProto.SID
    group_sid_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.SID]
    def __init__(self, user_sid: _Optional[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]] = ..., group_sid_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.SID, _Mapping]]] = ...) -> None: ...

class GetPrimaryDomainArg(_message.Message):
    __slots__ = ("trusted_domain",)
    TRUSTED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    trusted_domain: str
    def __init__(self, trusted_domain: _Optional[str] = ...) -> None: ...

class GetPrimaryDomainResult(_message.Message):
    __slots__ = ("domain_name",)
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    def __init__(self, domain_name: _Optional[str] = ...) -> None: ...

class GetTrustedDomainsArg(_message.Message):
    __slots__ = ("primary_domain_name", "only_get_active")
    PRIMARY_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ONLY_GET_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    primary_domain_name: str
    only_get_active: bool
    def __init__(self, primary_domain_name: _Optional[str] = ..., only_get_active: bool = ...) -> None: ...

class GetTrustedDomainsResult(_message.Message):
    __slots__ = ("trusted_domains_list",)
    TRUSTED_DOMAINS_LIST_FIELD_NUMBER: _ClassVar[int]
    trusted_domains_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, trusted_domains_list: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUnixRootUserInfoArg(_message.Message):
    __slots__ = ("session_state",)
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class UpdateUnixRootUserInfoResult(_message.Message):
    __slots__ = ("session_state",)
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    session_state: SessionStateProto
    def __init__(self, session_state: _Optional[_Union[SessionStateProto, _Mapping]] = ...) -> None: ...

class ClearAdProviderCacheArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearAdProviderCacheResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TriggerManualTrustDiscoveryArg(_message.Message):
    __slots__ = ("primary_domain_fqdn", "task_identifier")
    PRIMARY_DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    primary_domain_fqdn: str
    task_identifier: str
    def __init__(self, primary_domain_fqdn: _Optional[str] = ..., task_identifier: _Optional[str] = ...) -> None: ...

class TriggerManualTrustDiscoveryResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsManualTrustDiscoveryRunnningArg(_message.Message):
    __slots__ = ("primary_domain_fqdn", "task_identifier")
    PRIMARY_DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    TASK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    primary_domain_fqdn: str
    task_identifier: str
    def __init__(self, primary_domain_fqdn: _Optional[str] = ..., task_identifier: _Optional[str] = ...) -> None: ...

class IsManualTrustDiscoveryRunnningResult(_message.Message):
    __slots__ = ("is_running",)
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    is_running: bool
    def __init__(self, is_running: bool = ...) -> None: ...

class GetDomainControllerStatusArg(_message.Message):
    __slots__ = ("domain_fqdn",)
    DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    domain_fqdn: str
    def __init__(self, domain_fqdn: _Optional[str] = ...) -> None: ...

class GetDomainControllerStatusResult(_message.Message):
    __slots__ = ("dc_status_vec",)
    class DCAndStatusPair(_message.Message):
        __slots__ = ("dc_fqdn", "status")
        DC_FQDN_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        dc_fqdn: str
        status: str
        def __init__(self, dc_fqdn: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...
    DC_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    dc_status_vec: _containers.RepeatedCompositeFieldContainer[GetDomainControllerStatusResult.DCAndStatusPair]
    def __init__(self, dc_status_vec: _Optional[_Iterable[_Union[GetDomainControllerStatusResult.DCAndStatusPair, _Mapping]]] = ...) -> None: ...

class GetDomainControllersArg(_message.Message):
    __slots__ = ("domain_fqdn",)
    DOMAIN_FQDN_FIELD_NUMBER: _ClassVar[int]
    domain_fqdn: str
    def __init__(self, domain_fqdn: _Optional[str] = ...) -> None: ...

class GetDomainControllersResult(_message.Message):
    __slots__ = ("domain_controllers_vec",)
    DOMAIN_CONTROLLERS_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_controllers_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain_controllers_vec: _Optional[_Iterable[str]] = ...) -> None: ...
