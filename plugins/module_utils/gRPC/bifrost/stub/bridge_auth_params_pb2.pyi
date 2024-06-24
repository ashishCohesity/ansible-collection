from bridge.base import error_pb2 as _error_pb2
from bridge.nfs_portal.auth import nfs_auth_params_pb2 as _nfs_auth_params_pb2
from bridge.smb_portal import active_dir_params_pb2 as _active_dir_params_pb2
from bridge.smb_portal import smb_auth_params_pb2 as _smb_auth_params_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BridgeAuthArg(_message.Message):
    __slots__ = ("version", "type", "active_directory_arg", "smb_auth_arg", "nfs_auth_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[BridgeAuthArg.Type]
        kSmbAuth: _ClassVar[BridgeAuthArg.Type]
        kActiveDir: _ClassVar[BridgeAuthArg.Type]
        kBase: _ClassVar[BridgeAuthArg.Type]
        kNfsAuth: _ClassVar[BridgeAuthArg.Type]
    kUnused: BridgeAuthArg.Type
    kSmbAuth: BridgeAuthArg.Type
    kActiveDir: BridgeAuthArg.Type
    kBase: BridgeAuthArg.Type
    kNfsAuth: BridgeAuthArg.Type
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_ARG_FIELD_NUMBER: _ClassVar[int]
    SMB_AUTH_ARG_FIELD_NUMBER: _ClassVar[int]
    NFS_AUTH_ARG_FIELD_NUMBER: _ClassVar[int]
    version: int
    type: BridgeAuthArg.Type
    active_directory_arg: ActiveDirectoryArg
    smb_auth_arg: SmbAuthArg
    nfs_auth_arg: NfsAuthArg
    def __init__(self, version: _Optional[int] = ..., type: _Optional[_Union[BridgeAuthArg.Type, str]] = ..., active_directory_arg: _Optional[_Union[ActiveDirectoryArg, _Mapping]] = ..., smb_auth_arg: _Optional[_Union[SmbAuthArg, _Mapping]] = ..., nfs_auth_arg: _Optional[_Union[NfsAuthArg, _Mapping]] = ...) -> None: ...

class BridgeAuthResult(_message.Message):
    __slots__ = ("error", "active_directory_result", "smb_auth_result", "nfs_auth_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SMB_AUTH_RESULT_FIELD_NUMBER: _ClassVar[int]
    NFS_AUTH_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    active_directory_result: ActiveDirectoryResult
    smb_auth_result: SmbAuthResult
    nfs_auth_result: NfsAuthResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., active_directory_result: _Optional[_Union[ActiveDirectoryResult, _Mapping]] = ..., smb_auth_result: _Optional[_Union[SmbAuthResult, _Mapping]] = ..., nfs_auth_result: _Optional[_Union[NfsAuthResult, _Mapping]] = ...) -> None: ...

class ActiveDirectoryArg(_message.Message):
    __slots__ = ("version", "type", "add_domain_params", "edit_domain_params", "remove_domain_params", "update_preferred_domain_controllers_params", "modify_capaths_params")
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[ActiveDirectoryArg.CallType]
        kAddDomain: _ClassVar[ActiveDirectoryArg.CallType]
        kEditDomain: _ClassVar[ActiveDirectoryArg.CallType]
        kRemoveDomain: _ClassVar[ActiveDirectoryArg.CallType]
        kUpdatePreferredDCs: _ClassVar[ActiveDirectoryArg.CallType]
        kModifyCapaths: _ClassVar[ActiveDirectoryArg.CallType]
    kUnused: ActiveDirectoryArg.CallType
    kAddDomain: ActiveDirectoryArg.CallType
    kEditDomain: ActiveDirectoryArg.CallType
    kRemoveDomain: ActiveDirectoryArg.CallType
    kUpdatePreferredDCs: ActiveDirectoryArg.CallType
    kModifyCapaths: ActiveDirectoryArg.CallType
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADD_DOMAIN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EDIT_DOMAIN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DOMAIN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PREFERRED_DOMAIN_CONTROLLERS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MODIFY_CAPATHS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    version: int
    type: ActiveDirectoryArg.CallType
    add_domain_params: _active_dir_params_pb2.AddDomainArg
    edit_domain_params: _active_dir_params_pb2.EditDomainArg
    remove_domain_params: _active_dir_params_pb2.RemoveDomainArg
    update_preferred_domain_controllers_params: _active_dir_params_pb2.UpdatePreferredDCsArg
    modify_capaths_params: _active_dir_params_pb2.ModifyCapathsArg
    def __init__(self, version: _Optional[int] = ..., type: _Optional[_Union[ActiveDirectoryArg.CallType, str]] = ..., add_domain_params: _Optional[_Union[_active_dir_params_pb2.AddDomainArg, _Mapping]] = ..., edit_domain_params: _Optional[_Union[_active_dir_params_pb2.EditDomainArg, _Mapping]] = ..., remove_domain_params: _Optional[_Union[_active_dir_params_pb2.RemoveDomainArg, _Mapping]] = ..., update_preferred_domain_controllers_params: _Optional[_Union[_active_dir_params_pb2.UpdatePreferredDCsArg, _Mapping]] = ..., modify_capaths_params: _Optional[_Union[_active_dir_params_pb2.ModifyCapathsArg, _Mapping]] = ...) -> None: ...

class ActiveDirectoryResult(_message.Message):
    __slots__ = ("add_domain_result", "edit_domain_result", "remove_domain_result", "update_perferred_domain_controllers_result", "modify_capaths_result")
    ADD_DOMAIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    EDIT_DOMAIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DOMAIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PERFERRED_DOMAIN_CONTROLLERS_RESULT_FIELD_NUMBER: _ClassVar[int]
    MODIFY_CAPATHS_RESULT_FIELD_NUMBER: _ClassVar[int]
    add_domain_result: _active_dir_params_pb2.AddDomainResult
    edit_domain_result: _active_dir_params_pb2.EditDomainResult
    remove_domain_result: _active_dir_params_pb2.RemoveDomainResult
    update_perferred_domain_controllers_result: _active_dir_params_pb2.UpdatePreferredDCsResult
    modify_capaths_result: _active_dir_params_pb2.ModifyCapathsResult
    def __init__(self, add_domain_result: _Optional[_Union[_active_dir_params_pb2.AddDomainResult, _Mapping]] = ..., edit_domain_result: _Optional[_Union[_active_dir_params_pb2.EditDomainResult, _Mapping]] = ..., remove_domain_result: _Optional[_Union[_active_dir_params_pb2.RemoveDomainResult, _Mapping]] = ..., update_perferred_domain_controllers_result: _Optional[_Union[_active_dir_params_pb2.UpdatePreferredDCsResult, _Mapping]] = ..., modify_capaths_result: _Optional[_Union[_active_dir_params_pb2.ModifyCapathsResult, _Mapping]] = ...) -> None: ...

class SmbAuthArg(_message.Message):
    __slots__ = ("version", "type", "authenticate_session_params", "get_unix_ids_from_sids_params", "get_unix_ids_from_sid_params", "look_up_unix_ids_params", "get_ad_user_info_params", "search_names_params", "search_ldap_params", "get_unix_id_ad_group_sids_params", "authenticate_user_params", "get_ad_user_group_sids_params", "update_unix_ids_params", "update_sids_params", "lookup_sids_params", "lookup_names_params", "update_unix_root_user_info_params", "get_primary_domain_params", "get_trusted_domains_params", "clear_ad_provider_cache_params", "trigger_manual_trust_discovery_params", "is_manual_trust_discovery_running_params", "get_domain_controller_status_params", "get_domain_controllers_params")
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[SmbAuthArg.CallType]
        kAuthenticateSession: _ClassVar[SmbAuthArg.CallType]
        kGetUnixIdsFromSids: _ClassVar[SmbAuthArg.CallType]
        kGetUnixIdsFromSid: _ClassVar[SmbAuthArg.CallType]
        kLookupUnixIds: _ClassVar[SmbAuthArg.CallType]
        kGetUserInfo: _ClassVar[SmbAuthArg.CallType]
        kSearchNames: _ClassVar[SmbAuthArg.CallType]
        kSearchLdap: _ClassVar[SmbAuthArg.CallType]
        kGetUnixIdAdGroupSids: _ClassVar[SmbAuthArg.CallType]
        kAuthenticateUser: _ClassVar[SmbAuthArg.CallType]
        kGetAdUserGroupSids: _ClassVar[SmbAuthArg.CallType]
        kUpdateUnixIds: _ClassVar[SmbAuthArg.CallType]
        kUpdateSids: _ClassVar[SmbAuthArg.CallType]
        kLookupSids: _ClassVar[SmbAuthArg.CallType]
        kLookupNames: _ClassVar[SmbAuthArg.CallType]
        kUpdateUnixRootUserInfo: _ClassVar[SmbAuthArg.CallType]
        kGetPrimaryDomain: _ClassVar[SmbAuthArg.CallType]
        kGetTrustedDomains: _ClassVar[SmbAuthArg.CallType]
        kClearAdProviderCache: _ClassVar[SmbAuthArg.CallType]
        kGetAllTrustedDomains: _ClassVar[SmbAuthArg.CallType]
        kTriggerManualTrustDiscovery: _ClassVar[SmbAuthArg.CallType]
        kIsManualTrustDiscoveryRunning: _ClassVar[SmbAuthArg.CallType]
        kGetDomainControllerStatus: _ClassVar[SmbAuthArg.CallType]
        kGetDomainControllers: _ClassVar[SmbAuthArg.CallType]
    kUnused: SmbAuthArg.CallType
    kAuthenticateSession: SmbAuthArg.CallType
    kGetUnixIdsFromSids: SmbAuthArg.CallType
    kGetUnixIdsFromSid: SmbAuthArg.CallType
    kLookupUnixIds: SmbAuthArg.CallType
    kGetUserInfo: SmbAuthArg.CallType
    kSearchNames: SmbAuthArg.CallType
    kSearchLdap: SmbAuthArg.CallType
    kGetUnixIdAdGroupSids: SmbAuthArg.CallType
    kAuthenticateUser: SmbAuthArg.CallType
    kGetAdUserGroupSids: SmbAuthArg.CallType
    kUpdateUnixIds: SmbAuthArg.CallType
    kUpdateSids: SmbAuthArg.CallType
    kLookupSids: SmbAuthArg.CallType
    kLookupNames: SmbAuthArg.CallType
    kUpdateUnixRootUserInfo: SmbAuthArg.CallType
    kGetPrimaryDomain: SmbAuthArg.CallType
    kGetTrustedDomains: SmbAuthArg.CallType
    kClearAdProviderCache: SmbAuthArg.CallType
    kGetAllTrustedDomains: SmbAuthArg.CallType
    kTriggerManualTrustDiscovery: SmbAuthArg.CallType
    kIsManualTrustDiscoveryRunning: SmbAuthArg.CallType
    kGetDomainControllerStatus: SmbAuthArg.CallType
    kGetDomainControllers: SmbAuthArg.CallType
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATE_SESSION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_SIDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_SID_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOOK_UP_UNIX_IDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_AD_USER_INFO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_NAMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LDAP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_ID_AD_GROUP_SIDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATE_USER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_AD_USER_GROUP_SIDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_UNIX_IDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SIDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_SIDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_NAMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_UNIX_ROOT_USER_INFO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_PRIMARY_DOMAIN_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_TRUSTED_DOMAINS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_AD_PROVIDER_CACHE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MANUAL_TRUST_DISCOVERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_TRUST_DISCOVERY_RUNNING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_DOMAIN_CONTROLLER_STATUS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_DOMAIN_CONTROLLERS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    version: int
    type: SmbAuthArg.CallType
    authenticate_session_params: _smb_auth_params_pb2.AuthenticateSessionArg
    get_unix_ids_from_sids_params: _smb_auth_params_pb2.GetUnixIdsFromSidsArg
    get_unix_ids_from_sid_params: _smb_auth_params_pb2.GetUnixIdsFromSidArg
    look_up_unix_ids_params: _smb_auth_params_pb2.LookupUnixIdsArg
    get_ad_user_info_params: _smb_auth_params_pb2.GetAdUserInfoArg
    search_names_params: _smb_auth_params_pb2.SearchNamesArg
    search_ldap_params: _smb_auth_params_pb2.SearchLdapArg
    get_unix_id_ad_group_sids_params: _smb_auth_params_pb2.GetUnixIdAdGroupSidsArg
    authenticate_user_params: _smb_auth_params_pb2.AuthenticateUserArg
    get_ad_user_group_sids_params: _smb_auth_params_pb2.GetAdUserGroupSidsArg
    update_unix_ids_params: _smb_auth_params_pb2.UpdateUnixIdsArg
    update_sids_params: _smb_auth_params_pb2.UpdateSidsArg
    lookup_sids_params: _smb_auth_params_pb2.LookupSidsArg
    lookup_names_params: _smb_auth_params_pb2.LookupNamesArg
    update_unix_root_user_info_params: _smb_auth_params_pb2.UpdateUnixRootUserInfoArg
    get_primary_domain_params: _smb_auth_params_pb2.GetPrimaryDomainArg
    get_trusted_domains_params: _smb_auth_params_pb2.GetTrustedDomainsArg
    clear_ad_provider_cache_params: _smb_auth_params_pb2.ClearAdProviderCacheArg
    trigger_manual_trust_discovery_params: _smb_auth_params_pb2.TriggerManualTrustDiscoveryArg
    is_manual_trust_discovery_running_params: _smb_auth_params_pb2.IsManualTrustDiscoveryRunnningArg
    get_domain_controller_status_params: _smb_auth_params_pb2.GetDomainControllerStatusArg
    get_domain_controllers_params: _smb_auth_params_pb2.GetDomainControllersArg
    def __init__(self, version: _Optional[int] = ..., type: _Optional[_Union[SmbAuthArg.CallType, str]] = ..., authenticate_session_params: _Optional[_Union[_smb_auth_params_pb2.AuthenticateSessionArg, _Mapping]] = ..., get_unix_ids_from_sids_params: _Optional[_Union[_smb_auth_params_pb2.GetUnixIdsFromSidsArg, _Mapping]] = ..., get_unix_ids_from_sid_params: _Optional[_Union[_smb_auth_params_pb2.GetUnixIdsFromSidArg, _Mapping]] = ..., look_up_unix_ids_params: _Optional[_Union[_smb_auth_params_pb2.LookupUnixIdsArg, _Mapping]] = ..., get_ad_user_info_params: _Optional[_Union[_smb_auth_params_pb2.GetAdUserInfoArg, _Mapping]] = ..., search_names_params: _Optional[_Union[_smb_auth_params_pb2.SearchNamesArg, _Mapping]] = ..., search_ldap_params: _Optional[_Union[_smb_auth_params_pb2.SearchLdapArg, _Mapping]] = ..., get_unix_id_ad_group_sids_params: _Optional[_Union[_smb_auth_params_pb2.GetUnixIdAdGroupSidsArg, _Mapping]] = ..., authenticate_user_params: _Optional[_Union[_smb_auth_params_pb2.AuthenticateUserArg, _Mapping]] = ..., get_ad_user_group_sids_params: _Optional[_Union[_smb_auth_params_pb2.GetAdUserGroupSidsArg, _Mapping]] = ..., update_unix_ids_params: _Optional[_Union[_smb_auth_params_pb2.UpdateUnixIdsArg, _Mapping]] = ..., update_sids_params: _Optional[_Union[_smb_auth_params_pb2.UpdateSidsArg, _Mapping]] = ..., lookup_sids_params: _Optional[_Union[_smb_auth_params_pb2.LookupSidsArg, _Mapping]] = ..., lookup_names_params: _Optional[_Union[_smb_auth_params_pb2.LookupNamesArg, _Mapping]] = ..., update_unix_root_user_info_params: _Optional[_Union[_smb_auth_params_pb2.UpdateUnixRootUserInfoArg, _Mapping]] = ..., get_primary_domain_params: _Optional[_Union[_smb_auth_params_pb2.GetPrimaryDomainArg, _Mapping]] = ..., get_trusted_domains_params: _Optional[_Union[_smb_auth_params_pb2.GetTrustedDomainsArg, _Mapping]] = ..., clear_ad_provider_cache_params: _Optional[_Union[_smb_auth_params_pb2.ClearAdProviderCacheArg, _Mapping]] = ..., trigger_manual_trust_discovery_params: _Optional[_Union[_smb_auth_params_pb2.TriggerManualTrustDiscoveryArg, _Mapping]] = ..., is_manual_trust_discovery_running_params: _Optional[_Union[_smb_auth_params_pb2.IsManualTrustDiscoveryRunnningArg, _Mapping]] = ..., get_domain_controller_status_params: _Optional[_Union[_smb_auth_params_pb2.GetDomainControllerStatusArg, _Mapping]] = ..., get_domain_controllers_params: _Optional[_Union[_smb_auth_params_pb2.GetDomainControllersArg, _Mapping]] = ...) -> None: ...

class SmbAuthResult(_message.Message):
    __slots__ = ("authenticate_session_result", "get_unix_ids_from_sids_result", "get_unix_ids_from_sid_result", "look_up_unix_ids_result", "get_ad_user_info_result", "search_names_result", "search_ldap_result", "get_unix_id_ad_group_sids_result", "authenticate_user_result", "get_ad_user_group_sids_result", "update_unix_ids_result", "update_sids_result", "lookup_sids_result", "lookup_names_result", "update_unix_root_user_info_result", "get_primary_domain_result", "get_trusted_domains_result", "clear_ad_provider_cache_result", "trigger_manual_trust_discovery_result", "is_manual_trust_discovery_running_result", "get_domain_controller_status_result", "get_domain_controllers_result")
    AUTHENTICATE_SESSION_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_SIDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_SID_RESULT_FIELD_NUMBER: _ClassVar[int]
    LOOK_UP_UNIX_IDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_AD_USER_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_NAMES_RESULT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LDAP_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_ID_AD_GROUP_SIDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATE_USER_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_AD_USER_GROUP_SIDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_UNIX_IDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SIDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_SIDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_NAMES_RESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_UNIX_ROOT_USER_INFO_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_PRIMARY_DOMAIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_TRUSTED_DOMAINS_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLEAR_AD_PROVIDER_CACHE_RESULT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MANUAL_TRUST_DISCOVERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_TRUST_DISCOVERY_RUNNING_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_DOMAIN_CONTROLLER_STATUS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_DOMAIN_CONTROLLERS_RESULT_FIELD_NUMBER: _ClassVar[int]
    authenticate_session_result: _smb_auth_params_pb2.AuthenticateSessionResult
    get_unix_ids_from_sids_result: _smb_auth_params_pb2.GetUnixIdsFromSidsResult
    get_unix_ids_from_sid_result: _smb_auth_params_pb2.GetUnixIdsFromSidResult
    look_up_unix_ids_result: _smb_auth_params_pb2.LookupUnixIdsResult
    get_ad_user_info_result: _smb_auth_params_pb2.GetAdUserInfoResult
    search_names_result: _smb_auth_params_pb2.SearchNamesResult
    search_ldap_result: _smb_auth_params_pb2.SearchLdapResult
    get_unix_id_ad_group_sids_result: _smb_auth_params_pb2.GetUnixIdAdGroupSidsResult
    authenticate_user_result: _smb_auth_params_pb2.AuthenticateUserResult
    get_ad_user_group_sids_result: _smb_auth_params_pb2.GetAdUserGroupSidsResult
    update_unix_ids_result: _smb_auth_params_pb2.UpdateUnixIdsResult
    update_sids_result: _smb_auth_params_pb2.UpdateSidsResult
    lookup_sids_result: _smb_auth_params_pb2.LookupSidsResult
    lookup_names_result: _smb_auth_params_pb2.LookupNamesResult
    update_unix_root_user_info_result: _smb_auth_params_pb2.UpdateUnixRootUserInfoResult
    get_primary_domain_result: _smb_auth_params_pb2.GetPrimaryDomainResult
    get_trusted_domains_result: _smb_auth_params_pb2.GetTrustedDomainsResult
    clear_ad_provider_cache_result: _smb_auth_params_pb2.ClearAdProviderCacheResult
    trigger_manual_trust_discovery_result: _smb_auth_params_pb2.TriggerManualTrustDiscoveryResult
    is_manual_trust_discovery_running_result: _smb_auth_params_pb2.IsManualTrustDiscoveryRunnningResult
    get_domain_controller_status_result: _smb_auth_params_pb2.GetDomainControllerStatusResult
    get_domain_controllers_result: _smb_auth_params_pb2.GetDomainControllersResult
    def __init__(self, authenticate_session_result: _Optional[_Union[_smb_auth_params_pb2.AuthenticateSessionResult, _Mapping]] = ..., get_unix_ids_from_sids_result: _Optional[_Union[_smb_auth_params_pb2.GetUnixIdsFromSidsResult, _Mapping]] = ..., get_unix_ids_from_sid_result: _Optional[_Union[_smb_auth_params_pb2.GetUnixIdsFromSidResult, _Mapping]] = ..., look_up_unix_ids_result: _Optional[_Union[_smb_auth_params_pb2.LookupUnixIdsResult, _Mapping]] = ..., get_ad_user_info_result: _Optional[_Union[_smb_auth_params_pb2.GetAdUserInfoResult, _Mapping]] = ..., search_names_result: _Optional[_Union[_smb_auth_params_pb2.SearchNamesResult, _Mapping]] = ..., search_ldap_result: _Optional[_Union[_smb_auth_params_pb2.SearchLdapResult, _Mapping]] = ..., get_unix_id_ad_group_sids_result: _Optional[_Union[_smb_auth_params_pb2.GetUnixIdAdGroupSidsResult, _Mapping]] = ..., authenticate_user_result: _Optional[_Union[_smb_auth_params_pb2.AuthenticateUserResult, _Mapping]] = ..., get_ad_user_group_sids_result: _Optional[_Union[_smb_auth_params_pb2.GetAdUserGroupSidsResult, _Mapping]] = ..., update_unix_ids_result: _Optional[_Union[_smb_auth_params_pb2.UpdateUnixIdsResult, _Mapping]] = ..., update_sids_result: _Optional[_Union[_smb_auth_params_pb2.UpdateSidsResult, _Mapping]] = ..., lookup_sids_result: _Optional[_Union[_smb_auth_params_pb2.LookupSidsResult, _Mapping]] = ..., lookup_names_result: _Optional[_Union[_smb_auth_params_pb2.LookupNamesResult, _Mapping]] = ..., update_unix_root_user_info_result: _Optional[_Union[_smb_auth_params_pb2.UpdateUnixRootUserInfoResult, _Mapping]] = ..., get_primary_domain_result: _Optional[_Union[_smb_auth_params_pb2.GetPrimaryDomainResult, _Mapping]] = ..., get_trusted_domains_result: _Optional[_Union[_smb_auth_params_pb2.GetTrustedDomainsResult, _Mapping]] = ..., clear_ad_provider_cache_result: _Optional[_Union[_smb_auth_params_pb2.ClearAdProviderCacheResult, _Mapping]] = ..., trigger_manual_trust_discovery_result: _Optional[_Union[_smb_auth_params_pb2.TriggerManualTrustDiscoveryResult, _Mapping]] = ..., is_manual_trust_discovery_running_result: _Optional[_Union[_smb_auth_params_pb2.IsManualTrustDiscoveryRunnningResult, _Mapping]] = ..., get_domain_controller_status_result: _Optional[_Union[_smb_auth_params_pb2.GetDomainControllerStatusResult, _Mapping]] = ..., get_domain_controllers_result: _Optional[_Union[_smb_auth_params_pb2.GetDomainControllersResult, _Mapping]] = ...) -> None: ...

class NfsAuthArg(_message.Message):
    __slots__ = ("version", "type", "get_user_gids_from_uid_params", "get_unix_ids_from_user_name_params", "validate_ldap_provider_config_params", "clear_ldap_provider_params", "get_names_from_unix_ids_params", "get_unix_ids_from_names_params")
    class CallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[NfsAuthArg.CallType]
        kGetUserGidsFromUid: _ClassVar[NfsAuthArg.CallType]
        kGetUnixIdsFromUserName: _ClassVar[NfsAuthArg.CallType]
        kValidateLdapProviderConfig: _ClassVar[NfsAuthArg.CallType]
        kClearLdapProviderCache: _ClassVar[NfsAuthArg.CallType]
        kGetNamesFromUnixIds: _ClassVar[NfsAuthArg.CallType]
        kGetUnixIdsFromNames: _ClassVar[NfsAuthArg.CallType]
    kUnused: NfsAuthArg.CallType
    kGetUserGidsFromUid: NfsAuthArg.CallType
    kGetUnixIdsFromUserName: NfsAuthArg.CallType
    kValidateLdapProviderConfig: NfsAuthArg.CallType
    kClearLdapProviderCache: NfsAuthArg.CallType
    kGetNamesFromUnixIds: NfsAuthArg.CallType
    kGetUnixIdsFromNames: NfsAuthArg.CallType
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GET_USER_GIDS_FROM_UID_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_USER_NAME_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_LDAP_PROVIDER_CONFIG_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_LDAP_PROVIDER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_NAMES_FROM_UNIX_IDS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_NAMES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    version: int
    type: NfsAuthArg.CallType
    get_user_gids_from_uid_params: _nfs_auth_params_pb2.GetUserGidsFromUidArg
    get_unix_ids_from_user_name_params: _nfs_auth_params_pb2.GetUnixIdsFromUserNameArg
    validate_ldap_provider_config_params: _nfs_auth_params_pb2.ValidateLdapProviderConfigArg
    clear_ldap_provider_params: _nfs_auth_params_pb2.ClearLdapProviderCacheArg
    get_names_from_unix_ids_params: _nfs_auth_params_pb2.GetNamesFromUnixIdsArg
    get_unix_ids_from_names_params: _nfs_auth_params_pb2.GetUnixIdsFromNamesArg
    def __init__(self, version: _Optional[int] = ..., type: _Optional[_Union[NfsAuthArg.CallType, str]] = ..., get_user_gids_from_uid_params: _Optional[_Union[_nfs_auth_params_pb2.GetUserGidsFromUidArg, _Mapping]] = ..., get_unix_ids_from_user_name_params: _Optional[_Union[_nfs_auth_params_pb2.GetUnixIdsFromUserNameArg, _Mapping]] = ..., validate_ldap_provider_config_params: _Optional[_Union[_nfs_auth_params_pb2.ValidateLdapProviderConfigArg, _Mapping]] = ..., clear_ldap_provider_params: _Optional[_Union[_nfs_auth_params_pb2.ClearLdapProviderCacheArg, _Mapping]] = ..., get_names_from_unix_ids_params: _Optional[_Union[_nfs_auth_params_pb2.GetNamesFromUnixIdsArg, _Mapping]] = ..., get_unix_ids_from_names_params: _Optional[_Union[_nfs_auth_params_pb2.GetUnixIdsFromNamesArg, _Mapping]] = ...) -> None: ...

class NfsAuthResult(_message.Message):
    __slots__ = ("get_user_gids_from_uid_result", "get_unix_ids_from_user_name_result", "validate_ldap_provider_config_result", "clear_ldap_provider_result", "get_names_from_unix_ids_result", "get_unix_ids_from_names_result")
    GET_USER_GIDS_FROM_UID_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_USER_NAME_RESULT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_LDAP_PROVIDER_CONFIG_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLEAR_LDAP_PROVIDER_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_NAMES_FROM_UNIX_IDS_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_UNIX_IDS_FROM_NAMES_RESULT_FIELD_NUMBER: _ClassVar[int]
    get_user_gids_from_uid_result: _nfs_auth_params_pb2.GetUserGidsFromUidResult
    get_unix_ids_from_user_name_result: _nfs_auth_params_pb2.GetUnixIdsFromUserNameResult
    validate_ldap_provider_config_result: _nfs_auth_params_pb2.ValidateLdapProviderConfigResult
    clear_ldap_provider_result: _nfs_auth_params_pb2.ClearLdapProviderCacheResult
    get_names_from_unix_ids_result: _nfs_auth_params_pb2.GetNamesFromUnixIdsResult
    get_unix_ids_from_names_result: _nfs_auth_params_pb2.GetUnixIdsFromNamesResult
    def __init__(self, get_user_gids_from_uid_result: _Optional[_Union[_nfs_auth_params_pb2.GetUserGidsFromUidResult, _Mapping]] = ..., get_unix_ids_from_user_name_result: _Optional[_Union[_nfs_auth_params_pb2.GetUnixIdsFromUserNameResult, _Mapping]] = ..., validate_ldap_provider_config_result: _Optional[_Union[_nfs_auth_params_pb2.ValidateLdapProviderConfigResult, _Mapping]] = ..., clear_ldap_provider_result: _Optional[_Union[_nfs_auth_params_pb2.ClearLdapProviderCacheResult, _Mapping]] = ..., get_names_from_unix_ids_result: _Optional[_Union[_nfs_auth_params_pb2.GetNamesFromUnixIdsResult, _Mapping]] = ..., get_unix_ids_from_names_result: _Optional[_Union[_nfs_auth_params_pb2.GetUnixIdsFromNamesResult, _Mapping]] = ...) -> None: ...
