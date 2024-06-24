from magneto.base import credentials_pb2 as _credentials_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class O365SPOConnectionParam(_message.Message):
    __slots__ = ("credentials", "url", "client_tag", "azure_environment")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TAG_FIELD_NUMBER: _ClassVar[int]
    AZURE_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    credentials: _credentials_pb2.Credentials
    url: str
    client_tag: str
    azure_environment: str
    def __init__(self, credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., url: _Optional[str] = ..., client_tag: _Optional[str] = ..., azure_environment: _Optional[str] = ...) -> None: ...

class SiteIdentity(_message.Message):
    __slots__ = ("url", "id", "server_relativeurl", "title", "webid")
    URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELATIVEURL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    WEBID_FIELD_NUMBER: _ClassVar[int]
    url: str
    id: str
    server_relativeurl: str
    title: str
    webid: str
    def __init__(self, url: _Optional[str] = ..., id: _Optional[str] = ..., server_relativeurl: _Optional[str] = ..., title: _Optional[str] = ..., webid: _Optional[str] = ...) -> None: ...

class SiteProperty(_message.Message):
    __slots__ = ("name", "datatype", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    datatype: str
    value: str
    def __init__(self, name: _Optional[str] = ..., datatype: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SiteInfo(_message.Message):
    __slots__ = ("site", "template", "lcid", "is_hubsite", "hubsite_id", "hubsite_url", "compatibility_level", "owner_vec", "root_web_id", "timezone_id", "description", "classification", "design", "design_id", "is_public", "locale_id", "is_subsite", "geolocation", "group_id", "read_only", "is_multilingual", "tenantsiteprop_vec", "siteprop_vec", "webprop_vec", "is_personalsite")
    SITE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LCID_FIELD_NUMBER: _ClassVar[int]
    IS_HUBSITE_FIELD_NUMBER: _ClassVar[int]
    HUBSITE_ID_FIELD_NUMBER: _ClassVar[int]
    HUBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OWNER_VEC_FIELD_NUMBER: _ClassVar[int]
    ROOT_WEB_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    DESIGN_FIELD_NUMBER: _ClassVar[int]
    DESIGN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LOCALE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSITE_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    IS_MULTILINGUAL_FIELD_NUMBER: _ClassVar[int]
    TENANTSITEPROP_VEC_FIELD_NUMBER: _ClassVar[int]
    SITEPROP_VEC_FIELD_NUMBER: _ClassVar[int]
    WEBPROP_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_PERSONALSITE_FIELD_NUMBER: _ClassVar[int]
    site: SiteIdentity
    template: str
    lcid: int
    is_hubsite: bool
    hubsite_id: str
    hubsite_url: str
    compatibility_level: int
    owner_vec: _containers.RepeatedScalarFieldContainer[str]
    root_web_id: str
    timezone_id: int
    description: str
    classification: str
    design: str
    design_id: str
    is_public: bool
    locale_id: int
    is_subsite: bool
    geolocation: str
    group_id: str
    read_only: bool
    is_multilingual: bool
    tenantsiteprop_vec: _containers.RepeatedCompositeFieldContainer[SiteProperty]
    siteprop_vec: _containers.RepeatedCompositeFieldContainer[SiteProperty]
    webprop_vec: _containers.RepeatedCompositeFieldContainer[SiteProperty]
    is_personalsite: bool
    def __init__(self, site: _Optional[_Union[SiteIdentity, _Mapping]] = ..., template: _Optional[str] = ..., lcid: _Optional[int] = ..., is_hubsite: bool = ..., hubsite_id: _Optional[str] = ..., hubsite_url: _Optional[str] = ..., compatibility_level: _Optional[int] = ..., owner_vec: _Optional[_Iterable[str]] = ..., root_web_id: _Optional[str] = ..., timezone_id: _Optional[int] = ..., description: _Optional[str] = ..., classification: _Optional[str] = ..., design: _Optional[str] = ..., design_id: _Optional[str] = ..., is_public: bool = ..., locale_id: _Optional[int] = ..., is_subsite: bool = ..., geolocation: _Optional[str] = ..., group_id: _Optional[str] = ..., read_only: bool = ..., is_multilingual: bool = ..., tenantsiteprop_vec: _Optional[_Iterable[_Union[SiteProperty, _Mapping]]] = ..., siteprop_vec: _Optional[_Iterable[_Union[SiteProperty, _Mapping]]] = ..., webprop_vec: _Optional[_Iterable[_Union[SiteProperty, _Mapping]]] = ..., is_personalsite: bool = ...) -> None: ...

class VerifyConnectivityArg(_message.Message):
    __slots__ = ("connection", "option_flags", "siteurl_noscript", "denyscript", "cmdlet_requiredversion", "readonly")
    class VerifyOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[VerifyConnectivityArg.VerifyOptionFlags]
        kDownloadPowerShellModulesIfNeeded: _ClassVar[VerifyConnectivityArg.VerifyOptionFlags]
        kUpdateSiteNoScript: _ClassVar[VerifyConnectivityArg.VerifyOptionFlags]
        kUpdateSiteReadOnly: _ClassVar[VerifyConnectivityArg.VerifyOptionFlags]
    kNone: VerifyConnectivityArg.VerifyOptionFlags
    kDownloadPowerShellModulesIfNeeded: VerifyConnectivityArg.VerifyOptionFlags
    kUpdateSiteNoScript: VerifyConnectivityArg.VerifyOptionFlags
    kUpdateSiteReadOnly: VerifyConnectivityArg.VerifyOptionFlags
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SITEURL_NOSCRIPT_FIELD_NUMBER: _ClassVar[int]
    DENYSCRIPT_FIELD_NUMBER: _ClassVar[int]
    CMDLET_REQUIREDVERSION_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    connection: O365SPOConnectionParam
    option_flags: int
    siteurl_noscript: str
    denyscript: bool
    cmdlet_requiredversion: str
    readonly: bool
    def __init__(self, connection: _Optional[_Union[O365SPOConnectionParam, _Mapping]] = ..., option_flags: _Optional[int] = ..., siteurl_noscript: _Optional[str] = ..., denyscript: bool = ..., cmdlet_requiredversion: _Optional[str] = ..., readonly: bool = ...) -> None: ...

class VerifyConnectivityResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackupSiteArg(_message.Message):
    __slots__ = ("connection", "site_param")
    class BackupSiteParam(_message.Message):
        __slots__ = ("site", "option_flags", "data_dir_path")
        class BackupSiteOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDefault: _ClassVar[BackupSiteArg.BackupSiteParam.BackupSiteOptionFlags]
        kDefault: BackupSiteArg.BackupSiteParam.BackupSiteOptionFlags
        SITE_FIELD_NUMBER: _ClassVar[int]
        OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
        DATA_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        site: SiteIdentity
        option_flags: int
        data_dir_path: str
        def __init__(self, site: _Optional[_Union[SiteIdentity, _Mapping]] = ..., option_flags: _Optional[int] = ..., data_dir_path: _Optional[str] = ...) -> None: ...
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SITE_PARAM_FIELD_NUMBER: _ClassVar[int]
    connection: O365SPOConnectionParam
    site_param: BackupSiteArg.BackupSiteParam
    def __init__(self, connection: _Optional[_Union[O365SPOConnectionParam, _Mapping]] = ..., site_param: _Optional[_Union[BackupSiteArg.BackupSiteParam, _Mapping]] = ...) -> None: ...

class SiteBackupFile(_message.Message):
    __slots__ = ("file_type", "file_path", "file_size")
    class SiteBackupFileType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSitePnPFile: _ClassVar[SiteBackupFile.SiteBackupFileType.Type]
        kSitePnPFile: SiteBackupFile.SiteBackupFileType.Type
        def __init__(self) -> None: ...
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_type: SiteBackupFile.SiteBackupFileType.Type
    file_path: str
    file_size: int
    def __init__(self, file_type: _Optional[_Union[SiteBackupFile.SiteBackupFileType.Type, str]] = ..., file_path: _Optional[str] = ..., file_size: _Optional[int] = ...) -> None: ...

class SiteBackupStatus(_message.Message):
    __slots__ = ("site_info", "option_flags", "backup_file_vec", "warning_vec")
    SITE_INFO_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
    site_info: SiteInfo
    option_flags: int
    backup_file_vec: _containers.RepeatedCompositeFieldContainer[SiteBackupFile]
    warning_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, site_info: _Optional[_Union[SiteInfo, _Mapping]] = ..., option_flags: _Optional[int] = ..., backup_file_vec: _Optional[_Iterable[_Union[SiteBackupFile, _Mapping]]] = ..., warning_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class BackupSiteResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBackupSiteOutputArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class GetBackupSiteOutputResult(_message.Message):
    __slots__ = ("site_result",)
    SITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    site_result: SiteBackupStatus
    def __init__(self, site_result: _Optional[_Union[SiteBackupStatus, _Mapping]] = ...) -> None: ...

class RestoreSiteArg(_message.Message):
    __slots__ = ("connection", "site_param", "different_tenant", "skip_lists_creation")
    class RestoreSiteParam(_message.Message):
        __slots__ = ("site_backup_status", "parent_site_url", "option_flags", "modern_theme_override")
        class RestoreSiteOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDefault: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kApplyOnTopOfRecycleBinIfFound: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kAssociateHubParent: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kEnableNoScriptOption: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kRecreateSite: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kSubsiteOverwriteNavigation: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kResetSubsiteParentSiteCollTopNavigation: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kCleanUpPnpFileParentDir: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
            kSkipApplyTemplate: _ClassVar[RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags]
        kDefault: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kApplyOnTopOfRecycleBinIfFound: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kAssociateHubParent: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kEnableNoScriptOption: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kRecreateSite: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kSubsiteOverwriteNavigation: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kResetSubsiteParentSiteCollTopNavigation: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kCleanUpPnpFileParentDir: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        kSkipApplyTemplate: RestoreSiteArg.RestoreSiteParam.RestoreSiteOptionFlags
        SITE_BACKUP_STATUS_FIELD_NUMBER: _ClassVar[int]
        PARENT_SITE_URL_FIELD_NUMBER: _ClassVar[int]
        OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
        MODERN_THEME_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        site_backup_status: SiteBackupStatus
        parent_site_url: str
        option_flags: int
        modern_theme_override: str
        def __init__(self, site_backup_status: _Optional[_Union[SiteBackupStatus, _Mapping]] = ..., parent_site_url: _Optional[str] = ..., option_flags: _Optional[int] = ..., modern_theme_override: _Optional[str] = ...) -> None: ...
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SITE_PARAM_FIELD_NUMBER: _ClassVar[int]
    DIFFERENT_TENANT_FIELD_NUMBER: _ClassVar[int]
    SKIP_LISTS_CREATION_FIELD_NUMBER: _ClassVar[int]
    connection: O365SPOConnectionParam
    site_param: RestoreSiteArg.RestoreSiteParam
    different_tenant: bool
    skip_lists_creation: bool
    def __init__(self, connection: _Optional[_Union[O365SPOConnectionParam, _Mapping]] = ..., site_param: _Optional[_Union[RestoreSiteArg.RestoreSiteParam, _Mapping]] = ..., different_tenant: bool = ..., skip_lists_creation: bool = ...) -> None: ...

class RestoreSiteResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRestoreSiteOutputArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class GetRestoreSiteOutputResult(_message.Message):
    __slots__ = ("site_status",)
    class SiteRestoreStatus(_message.Message):
        __slots__ = ("site", "warning_vec")
        SITE_FIELD_NUMBER: _ClassVar[int]
        WARNING_VEC_FIELD_NUMBER: _ClassVar[int]
        site: SiteIdentity
        warning_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, site: _Optional[_Union[SiteIdentity, _Mapping]] = ..., warning_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    SITE_STATUS_FIELD_NUMBER: _ClassVar[int]
    site_status: GetRestoreSiteOutputResult.SiteRestoreStatus
    def __init__(self, site_status: _Optional[_Union[GetRestoreSiteOutputResult.SiteRestoreStatus, _Mapping]] = ...) -> None: ...

class GetProgressArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class GetProgressResult(_message.Message):
    __slots__ = ("task_state", "last_update_time", "site_progress")
    class TaskProgressState(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[GetProgressResult.TaskProgressState.Type]
            kPending: _ClassVar[GetProgressResult.TaskProgressState.Type]
            kProgress: _ClassVar[GetProgressResult.TaskProgressState.Type]
            kCompleted: _ClassVar[GetProgressResult.TaskProgressState.Type]
        kUnknown: GetProgressResult.TaskProgressState.Type
        kPending: GetProgressResult.TaskProgressState.Type
        kProgress: GetProgressResult.TaskProgressState.Type
        kCompleted: GetProgressResult.TaskProgressState.Type
        def __init__(self) -> None: ...
    class SiteProgress(_message.Message):
        __slots__ = ("url", "activity_str", "percent_complete", "step", "potential_steps")
        URL_FIELD_NUMBER: _ClassVar[int]
        ACTIVITY_STR_FIELD_NUMBER: _ClassVar[int]
        PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
        STEP_FIELD_NUMBER: _ClassVar[int]
        POTENTIAL_STEPS_FIELD_NUMBER: _ClassVar[int]
        url: str
        activity_str: str
        percent_complete: int
        step: int
        potential_steps: int
        def __init__(self, url: _Optional[str] = ..., activity_str: _Optional[str] = ..., percent_complete: _Optional[int] = ..., step: _Optional[int] = ..., potential_steps: _Optional[int] = ...) -> None: ...
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SITE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    task_state: GetProgressResult.TaskProgressState.Type
    last_update_time: int
    site_progress: GetProgressResult.SiteProgress
    def __init__(self, task_state: _Optional[_Union[GetProgressResult.TaskProgressState.Type, str]] = ..., last_update_time: _Optional[int] = ..., site_progress: _Optional[_Union[GetProgressResult.SiteProgress, _Mapping]] = ...) -> None: ...

class DeleteSiteArg(_message.Message):
    __slots__ = ("connection", "siteurl", "purge")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SITEURL_FIELD_NUMBER: _ClassVar[int]
    PURGE_FIELD_NUMBER: _ClassVar[int]
    connection: O365SPOConnectionParam
    siteurl: str
    purge: bool
    def __init__(self, connection: _Optional[_Union[O365SPOConnectionParam, _Mapping]] = ..., siteurl: _Optional[str] = ..., purge: bool = ...) -> None: ...

class DeleteSiteResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CleanupArg(_message.Message):
    __slots__ = ("task_id", "cancel")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    cancel: bool
    def __init__(self, task_id: _Optional[int] = ..., cancel: bool = ...) -> None: ...

class CleanupResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelTaskArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...

class CancelTaskResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVerifyConnResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVerifyConnOutputArg(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    def __init__(self, task_id: _Optional[int] = ...) -> None: ...
