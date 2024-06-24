from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.connectors.outlook import outlook_pb2 as _outlook_pb2
from magneto.connectors.outlook import outlook_external_pb2 as _outlook_external_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EwsBaseResult(_message.Message):
    __slots__ = ("num_api_calls",)
    NUM_API_CALLS_FIELD_NUMBER: _ClassVar[int]
    num_api_calls: int
    def __init__(self, num_api_calls: _Optional[int] = ...) -> None: ...

class GetMailboxListArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMailboxListResult(_message.Message):
    __slots__ = ("error", "mailbox_vec", "ews_base_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_VEC_FIELD_NUMBER: _ClassVar[int]
    EWS_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mailbox_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.Mailbox]
    ews_base_result: EwsBaseResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mailbox_vec: _Optional[_Iterable[_Union[_outlook_pb2.Mailbox, _Mapping]]] = ..., ews_base_result: _Optional[_Union[EwsBaseResult, _Mapping]] = ...) -> None: ...

class ValidateUserCredentialsArg(_message.Message):
    __slots__ = ("validate_account_idx",)
    VALIDATE_ACCOUNT_IDX_FIELD_NUMBER: _ClassVar[int]
    validate_account_idx: int
    def __init__(self, validate_account_idx: _Optional[int] = ...) -> None: ...

class ValidateUserCredentialsResult(_message.Message):
    __slots__ = ("error", "ews_base_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EWS_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    ews_base_result: EwsBaseResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ews_base_result: _Optional[_Union[EwsBaseResult, _Mapping]] = ...) -> None: ...

class GetOutlookHierarchyArg(_message.Message):
    __slots__ = ("is_async_phase_supported", "old_entity_hierarchy", "registered_entity", "is_new_entity", "is_user_initiated", "is_async_phase", "o365_params", "use_get_searchable_mailboxes_api", "fetch_only_root_sites", "background_mode_fetch_full_sites_tree", "discover_multi_geo_sites", "discoverable_multi_geo_region_codes_vec")
    IS_ASYNC_PHASE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    OLD_ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_ENTITY_FIELD_NUMBER: _ClassVar[int]
    IS_USER_INITIATED_FIELD_NUMBER: _ClassVar[int]
    IS_ASYNC_PHASE_FIELD_NUMBER: _ClassVar[int]
    O365_PARAMS_FIELD_NUMBER: _ClassVar[int]
    USE_GET_SEARCHABLE_MAILBOXES_API_FIELD_NUMBER: _ClassVar[int]
    FETCH_ONLY_ROOT_SITES_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_MODE_FETCH_FULL_SITES_TREE_FIELD_NUMBER: _ClassVar[int]
    DISCOVER_MULTI_GEO_SITES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERABLE_MULTI_GEO_REGION_CODES_VEC_FIELD_NUMBER: _ClassVar[int]
    is_async_phase_supported: bool
    old_entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    registered_entity: _entity_pb2.EntityProto
    is_new_entity: bool
    is_user_initiated: bool
    is_async_phase: bool
    o365_params: _magneto_pb2.RegisteredEntityO365Params
    use_get_searchable_mailboxes_api: bool
    fetch_only_root_sites: bool
    background_mode_fetch_full_sites_tree: bool
    discover_multi_geo_sites: bool
    discoverable_multi_geo_region_codes_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_async_phase_supported: bool = ..., old_entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., registered_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., is_new_entity: bool = ..., is_user_initiated: bool = ..., is_async_phase: bool = ..., o365_params: _Optional[_Union[_magneto_pb2.RegisteredEntityO365Params, _Mapping]] = ..., use_get_searchable_mailboxes_api: bool = ..., fetch_only_root_sites: bool = ..., background_mode_fetch_full_sites_tree: bool = ..., discover_multi_geo_sites: bool = ..., discoverable_multi_geo_region_codes_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetOutlookHierarchyResult(_message.Message):
    __slots__ = ("error", "entity_hierarchy", "teams_vec", "dead_time", "throttling_time_usecs", "num_api_calls")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    TEAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    NUM_API_CALLS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    entity_hierarchy: _magneto_pb2.EntityHierarchyProto
    teams_vec: _containers.RepeatedCompositeFieldContainer[_magneto_pb2.O365TeamsChannelsList]
    dead_time: int
    throttling_time_usecs: int
    num_api_calls: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., entity_hierarchy: _Optional[_Union[_magneto_pb2.EntityHierarchyProto, _Mapping]] = ..., teams_vec: _Optional[_Iterable[_Union[_magneto_pb2.O365TeamsChannelsList, _Mapping]]] = ..., dead_time: _Optional[int] = ..., throttling_time_usecs: _Optional[int] = ..., num_api_calls: _Optional[int] = ...) -> None: ...

class GetFolderHierarchyChangesArg(_message.Message):
    __slots__ = ("mailbox_id", "folder_root_info", "group_mailbox_id")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_INFO_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    folder_root_info: _outlook_pb2.FolderRootInfo
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., folder_root_info: _Optional[_Union[_outlook_pb2.FolderRootInfo, _Mapping]] = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class GetFolderHierarchyChangesResult(_message.Message):
    __slots__ = ("error", "change_vec", "folder_root_info", "o365_error_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_INFO_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    change_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.FolderHierarchyChange]
    folder_root_info: _outlook_pb2.FolderRootInfo
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., change_vec: _Optional[_Iterable[_Union[_outlook_pb2.FolderHierarchyChange, _Mapping]]] = ..., folder_root_info: _Optional[_Union[_outlook_pb2.FolderRootInfo, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class GetMultipleFolderHierarchyChangesArg(_message.Message):
    __slots__ = ("mailbox_id", "folder_root_info_vec", "group_mailbox_id")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    folder_root_info_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.FolderRootInfo]
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., folder_root_info_vec: _Optional[_Iterable[_Union[_outlook_pb2.FolderRootInfo, _Mapping]]] = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class GetMultipleFolderHierarchyChangesResult(_message.Message):
    __slots__ = ("error", "folder_hierarchy_changes_result_vec", "o365_error_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_HIERARCHY_CHANGES_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    folder_hierarchy_changes_result_vec: _containers.RepeatedCompositeFieldContainer[GetFolderHierarchyChangesResult]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_hierarchy_changes_result_vec: _Optional[_Iterable[_Union[GetFolderHierarchyChangesResult, _Mapping]]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class GetFolderChangesArg(_message.Message):
    __slots__ = ("mailbox_id", "folder_id", "previous_sync_state", "public_folder_mailbox", "group_mailbox_id")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    folder_id: str
    previous_sync_state: str
    public_folder_mailbox: str
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., folder_id: _Optional[str] = ..., previous_sync_state: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class GetFolderChangesResult(_message.Message):
    __slots__ = ("error", "change_vec", "sync_state", "has_more", "folder_not_found", "o365_error_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    change_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.FolderItemChange]
    sync_state: str
    has_more: bool
    folder_not_found: bool
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., change_vec: _Optional[_Iterable[_Union[_outlook_pb2.FolderItemChange, _Mapping]]] = ..., sync_state: _Optional[str] = ..., has_more: bool = ..., folder_not_found: bool = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class GetItemsArg(_message.Message):
    __slots__ = ("mailbox_id", "item_id_vec", "public_folder_mailbox", "group_mailbox_id")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    public_folder_mailbox: str
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., item_id_vec: _Optional[_Iterable[str]] = ..., public_folder_mailbox: _Optional[str] = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class GetItemsResult(_message.Message):
    __slots__ = ("error", "item_vec", "o365_error_proto", "dead_time", "ews_base_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    EWS_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    item_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.Item]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    dead_time: int
    ews_base_result: EwsBaseResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., item_vec: _Optional[_Iterable[_Union[_outlook_pb2.Item, _Mapping]]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., dead_time: _Optional[int] = ..., ews_base_result: _Optional[_Union[EwsBaseResult, _Mapping]] = ...) -> None: ...

class GetItemMetadataArg(_message.Message):
    __slots__ = ("mailbox_id", "item_id_vec", "public_folder_mailbox", "parent_folder_id", "group_mailbox_id")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    public_folder_mailbox: str
    parent_folder_id: str
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., item_id_vec: _Optional[_Iterable[str]] = ..., public_folder_mailbox: _Optional[str] = ..., parent_folder_id: _Optional[str] = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class GetItemMetadataResult(_message.Message):
    __slots__ = ("error", "item_vec", "o365_error_proto", "dead_time", "ews_base_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    EWS_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    item_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.Item]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    dead_time: int
    ews_base_result: EwsBaseResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., item_vec: _Optional[_Iterable[_Union[_outlook_pb2.Item, _Mapping]]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., dead_time: _Optional[int] = ..., ews_base_result: _Optional[_Union[EwsBaseResult, _Mapping]] = ...) -> None: ...

class GetAttachmentsArg(_message.Message):
    __slots__ = ("mailbox_id", "attachment_id_vec")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    attachment_id_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mailbox_id: _Optional[str] = ..., attachment_id_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAttachmentsResult(_message.Message):
    __slots__ = ("error", "attachment_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    attachment_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.Attachment]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., attachment_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.Attachment, _Mapping]]] = ...) -> None: ...

class PutItemsArg(_message.Message):
    __slots__ = ("mailbox_id", "upload_item_vec", "public_folder_mailbox", "should_use_update_or_create", "use_exp_backoff_for_num_items", "group_mailbox_id")
    class UploadItem(_message.Message):
        __slots__ = ("parent_folder_id", "item_vec", "parent_folder_path")
        PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
        PARENT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
        parent_folder_id: str
        item_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.Item]
        parent_folder_path: str
        def __init__(self, parent_folder_id: _Optional[str] = ..., item_vec: _Optional[_Iterable[_Union[_outlook_pb2.Item, _Mapping]]] = ..., parent_folder_path: _Optional[str] = ...) -> None: ...
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    SHOULD_USE_UPDATE_OR_CREATE_FIELD_NUMBER: _ClassVar[int]
    USE_EXP_BACKOFF_FOR_NUM_ITEMS_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    upload_item_vec: _containers.RepeatedCompositeFieldContainer[PutItemsArg.UploadItem]
    public_folder_mailbox: str
    should_use_update_or_create: bool
    use_exp_backoff_for_num_items: bool
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., upload_item_vec: _Optional[_Iterable[_Union[PutItemsArg.UploadItem, _Mapping]]] = ..., public_folder_mailbox: _Optional[str] = ..., should_use_update_or_create: bool = ..., use_exp_backoff_for_num_items: bool = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class PutItemsResult(_message.Message):
    __slots__ = ("error", "dead_time", "fall_back_to_create_new", "should_retry", "ews_base_result")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    FALL_BACK_TO_CREATE_NEW_FIELD_NUMBER: _ClassVar[int]
    SHOULD_RETRY_FIELD_NUMBER: _ClassVar[int]
    EWS_BASE_RESULT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    dead_time: int
    fall_back_to_create_new: bool
    should_retry: bool
    ews_base_result: EwsBaseResult
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., dead_time: _Optional[int] = ..., fall_back_to_create_new: bool = ..., should_retry: bool = ..., ews_base_result: _Optional[_Union[EwsBaseResult, _Mapping]] = ...) -> None: ...

class CreateMailboxArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateMailboxResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class CreateFolderPathArg(_message.Message):
    __slots__ = ("mailbox_id", "parent_folder_id", "folder_path_vec", "folder_type", "should_use_archive_as_parent")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_USE_ARCHIVE_AS_PARENT_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    parent_folder_id: str
    folder_path_vec: _containers.RepeatedScalarFieldContainer[str]
    folder_type: _outlook_external_pb2.FolderType.Type
    should_use_archive_as_parent: bool
    def __init__(self, mailbox_id: _Optional[str] = ..., parent_folder_id: _Optional[str] = ..., folder_path_vec: _Optional[_Iterable[str]] = ..., folder_type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., should_use_archive_as_parent: bool = ...) -> None: ...

class CreateFolderPathResult(_message.Message):
    __slots__ = ("error", "folder_id_vec", "folder_already_exists")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    folder_id_vec: _containers.RepeatedScalarFieldContainer[str]
    folder_already_exists: bool
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_id_vec: _Optional[_Iterable[str]] = ..., folder_already_exists: bool = ...) -> None: ...

class PoxAutodiscoverArg(_message.Message):
    __slots__ = ("email_address",)
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    def __init__(self, email_address: _Optional[str] = ...) -> None: ...

class PoxAutodiscoverResult(_message.Message):
    __slots__ = ("error", "mailbox_server_id", "autodiscover_smtp_address")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    AUTODISCOVER_SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mailbox_server_id: str
    autodiscover_smtp_address: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mailbox_server_id: _Optional[str] = ..., autodiscover_smtp_address: _Optional[str] = ...) -> None: ...

class GetUserSettingsArg(_message.Message):
    __slots__ = ("user_vec", "requested_setting_vec")
    class User(_message.Message):
        __slots__ = ("mailbox",)
        MAILBOX_FIELD_NUMBER: _ClassVar[int]
        mailbox: str
        def __init__(self, mailbox: _Optional[str] = ...) -> None: ...
    USER_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
    user_vec: _containers.RepeatedCompositeFieldContainer[GetUserSettingsArg.User]
    requested_setting_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_vec: _Optional[_Iterable[_Union[GetUserSettingsArg.User, _Mapping]]] = ..., requested_setting_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUserSettingsResult(_message.Message):
    __slots__ = ("error", "user_response_vec")
    class UserSetting(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class UserSettingError(_message.Message):
        __slots__ = ("name", "error_code", "error_message")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        name: str
        error_code: str
        error_message: str
        def __init__(self, name: _Optional[str] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...
    class UserResponse(_message.Message):
        __slots__ = ("redirect_target", "user_setting_vec", "error_code", "error_message", "user_setting_error_vec")
        REDIRECT_TARGET_FIELD_NUMBER: _ClassVar[int]
        USER_SETTING_VEC_FIELD_NUMBER: _ClassVar[int]
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        USER_SETTING_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
        redirect_target: str
        user_setting_vec: _containers.RepeatedCompositeFieldContainer[GetUserSettingsResult.UserSetting]
        error_code: str
        error_message: str
        user_setting_error_vec: _containers.RepeatedCompositeFieldContainer[GetUserSettingsResult.UserSettingError]
        def __init__(self, redirect_target: _Optional[str] = ..., user_setting_vec: _Optional[_Iterable[_Union[GetUserSettingsResult.UserSetting, _Mapping]]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., user_setting_error_vec: _Optional[_Iterable[_Union[GetUserSettingsResult.UserSettingError, _Mapping]]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_RESPONSE_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    user_response_vec: _containers.RepeatedCompositeFieldContainer[GetUserSettingsResult.UserResponse]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., user_response_vec: _Optional[_Iterable[_Union[GetUserSettingsResult.UserResponse, _Mapping]]] = ...) -> None: ...

class FindFolderArg(_message.Message):
    __slots__ = ("mailbox_id", "public_folder_mailbox", "folder_traversal_type", "folder_shape", "parent_folder_ids", "indexed_page_folder_view", "restriction", "retry_when_no_results_found_with_restriction")
    class AdditionalProperties(_message.Message):
        __slots__ = ("field_uri_type_vec", "extended_field_uri_vec")
        FIELD_URI_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_FIELD_URI_VEC_FIELD_NUMBER: _ClassVar[int]
        field_uri_type_vec: _containers.RepeatedScalarFieldContainer[_outlook_pb2.FieldUriType.Type]
        extended_field_uri_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.ExtendedFieldURI]
        def __init__(self, field_uri_type_vec: _Optional[_Iterable[_Union[_outlook_pb2.FieldUriType.Type, str]]] = ..., extended_field_uri_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.ExtendedFieldURI, _Mapping]]] = ...) -> None: ...
    class FolderShape(_message.Message):
        __slots__ = ("base_shape", "additional_properties")
        BASE_SHAPE_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        base_shape: _outlook_pb2.BaseShapeType.Type
        additional_properties: FindFolderArg.AdditionalProperties
        def __init__(self, base_shape: _Optional[_Union[_outlook_pb2.BaseShapeType.Type, str]] = ..., additional_properties: _Optional[_Union[FindFolderArg.AdditionalProperties, _Mapping]] = ...) -> None: ...
    class ParentFolderIds(_message.Message):
        __slots__ = ("distinguished_folder_id_vec", "folder_id_vec")
        DISTINGUISHED_FOLDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        FOLDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        distinguished_folder_id_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.DistinguishedFolderId]
        folder_id_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderId]
        def __init__(self, distinguished_folder_id_vec: _Optional[_Iterable[_Union[_outlook_pb2.DistinguishedFolderId, _Mapping]]] = ..., folder_id_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderId, _Mapping]]] = ...) -> None: ...
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    FOLDER_TRAVERSAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_SHAPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_IDS_FIELD_NUMBER: _ClassVar[int]
    INDEXED_PAGE_FOLDER_VIEW_FIELD_NUMBER: _ClassVar[int]
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    RETRY_WHEN_NO_RESULTS_FOUND_WITH_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    public_folder_mailbox: str
    folder_traversal_type: _outlook_pb2.FolderTraversalType.Type
    folder_shape: FindFolderArg.FolderShape
    parent_folder_ids: FindFolderArg.ParentFolderIds
    indexed_page_folder_view: _outlook_pb2.IndexedPageFolderView
    restriction: _outlook_pb2.Restriction
    retry_when_no_results_found_with_restriction: bool
    def __init__(self, mailbox_id: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., folder_traversal_type: _Optional[_Union[_outlook_pb2.FolderTraversalType.Type, str]] = ..., folder_shape: _Optional[_Union[FindFolderArg.FolderShape, _Mapping]] = ..., parent_folder_ids: _Optional[_Union[FindFolderArg.ParentFolderIds, _Mapping]] = ..., indexed_page_folder_view: _Optional[_Union[_outlook_pb2.IndexedPageFolderView, _Mapping]] = ..., restriction: _Optional[_Union[_outlook_pb2.Restriction, _Mapping]] = ..., retry_when_no_results_found_with_restriction: bool = ...) -> None: ...

class FindFolderResult(_message.Message):
    __slots__ = ("error", "o365_error_proto", "root_folder_vec")
    class RootFolder(_message.Message):
        __slots__ = ("folder_type", "folder_vec", "indexed_paging_offset", "includes_last_item_in_range", "total_items_in_view")
        class Folder(_message.Message):
            __slots__ = ("property_vec", "extended_property_vec", "folder_id", "type")
            class Property(_message.Message):
                __slots__ = ("name", "value")
                NAME_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                name: _outlook_pb2.FieldUriType.Type
                value: str
                def __init__(self, name: _Optional[_Union[_outlook_pb2.FieldUriType.Type, str]] = ..., value: _Optional[str] = ...) -> None: ...
            class ExtendedProperty(_message.Message):
                __slots__ = ("extended_field_uri", "value")
                EXTENDED_FIELD_URI_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                extended_field_uri: _outlook_external_pb2.ExtendedFieldURI
                value: str
                def __init__(self, extended_field_uri: _Optional[_Union[_outlook_external_pb2.ExtendedFieldURI, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...
            PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
            EXTENDED_PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
            FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            property_vec: _containers.RepeatedCompositeFieldContainer[FindFolderResult.RootFolder.Folder.Property]
            extended_property_vec: _containers.RepeatedCompositeFieldContainer[FindFolderResult.RootFolder.Folder.ExtendedProperty]
            folder_id: _outlook_external_pb2.FolderId
            type: _outlook_external_pb2.FolderType.Type
            def __init__(self, property_vec: _Optional[_Iterable[_Union[FindFolderResult.RootFolder.Folder.Property, _Mapping]]] = ..., extended_property_vec: _Optional[_Iterable[_Union[FindFolderResult.RootFolder.Folder.ExtendedProperty, _Mapping]]] = ..., folder_id: _Optional[_Union[_outlook_external_pb2.FolderId, _Mapping]] = ..., type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ...) -> None: ...
        FOLDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        FOLDER_VEC_FIELD_NUMBER: _ClassVar[int]
        INDEXED_PAGING_OFFSET_FIELD_NUMBER: _ClassVar[int]
        INCLUDES_LAST_ITEM_IN_RANGE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ITEMS_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
        folder_type: _outlook_external_pb2.FolderType.Type
        folder_vec: _containers.RepeatedCompositeFieldContainer[FindFolderResult.RootFolder.Folder]
        indexed_paging_offset: int
        includes_last_item_in_range: bool
        total_items_in_view: int
        def __init__(self, folder_type: _Optional[_Union[_outlook_external_pb2.FolderType.Type, str]] = ..., folder_vec: _Optional[_Iterable[_Union[FindFolderResult.RootFolder.Folder, _Mapping]]] = ..., indexed_paging_offset: _Optional[int] = ..., includes_last_item_in_range: bool = ..., total_items_in_view: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    ROOT_FOLDER_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    root_folder_vec: _containers.RepeatedCompositeFieldContainer[FindFolderResult.RootFolder]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., root_folder_vec: _Optional[_Iterable[_Union[FindFolderResult.RootFolder, _Mapping]]] = ...) -> None: ...

class GetFolderArg(_message.Message):
    __slots__ = ("mailbox_id", "public_folder_mailbox", "folder_id_vec", "base_shape", "additional_properties", "group_mailbox_id")
    class AdditionalProperties(_message.Message):
        __slots__ = ("field_uri_type_vec", "extended_field_uri_vec")
        FIELD_URI_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        EXTENDED_FIELD_URI_VEC_FIELD_NUMBER: _ClassVar[int]
        field_uri_type_vec: _containers.RepeatedScalarFieldContainer[_outlook_pb2.FieldUriType.Type]
        extended_field_uri_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.ExtendedFieldURI]
        def __init__(self, field_uri_type_vec: _Optional[_Iterable[_Union[_outlook_pb2.FieldUriType.Type, str]]] = ..., extended_field_uri_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.ExtendedFieldURI, _Mapping]]] = ...) -> None: ...
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    BASE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    public_folder_mailbox: str
    folder_id_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderId]
    base_shape: _outlook_pb2.BaseShapeType.Type
    additional_properties: GetFolderArg.AdditionalProperties
    group_mailbox_id: str
    def __init__(self, mailbox_id: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., folder_id_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderId, _Mapping]]] = ..., base_shape: _Optional[_Union[_outlook_pb2.BaseShapeType.Type, str]] = ..., additional_properties: _Optional[_Union[GetFolderArg.AdditionalProperties, _Mapping]] = ..., group_mailbox_id: _Optional[str] = ...) -> None: ...

class GetFolderResult(_message.Message):
    __slots__ = ("error", "folder_content_info_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_CONTENT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    folder_content_info_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderContentInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_content_info_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderContentInfo, _Mapping]]] = ...) -> None: ...

class CreateFolderOutlookArg(_message.Message):
    __slots__ = ("mailbox_id", "public_folder_mailbox", "parent_folder_id", "folder_vec")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_VEC_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    public_folder_mailbox: str
    parent_folder_id: _outlook_pb2.TargetFolderId
    folder_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderContentInfo]
    def __init__(self, mailbox_id: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., parent_folder_id: _Optional[_Union[_outlook_pb2.TargetFolderId, _Mapping]] = ..., folder_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderContentInfo, _Mapping]]] = ...) -> None: ...

class CreateFolderOutlookResult(_message.Message):
    __slots__ = ("error", "folder_id_vec", "folder_already_exists", "o365_error_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    folder_id_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderId]
    folder_already_exists: bool
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_id_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderId, _Mapping]]] = ..., folder_already_exists: bool = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class CreateFolderOutlookPathArg(_message.Message):
    __slots__ = ("mailbox_id", "public_folder_mailbox", "parent_folder_id", "folder_path_vec")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    public_folder_mailbox: str
    parent_folder_id: _outlook_pb2.TargetFolderId
    folder_path_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderContentInfo]
    def __init__(self, mailbox_id: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., parent_folder_id: _Optional[_Union[_outlook_pb2.TargetFolderId, _Mapping]] = ..., folder_path_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderContentInfo, _Mapping]]] = ...) -> None: ...

class CreateFolderOutlookPathResult(_message.Message):
    __slots__ = ("error", "folder_path_id_vec", "o365_error_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    folder_path_id_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderId]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_path_id_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderId, _Mapping]]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...

class UpdateFolderArg(_message.Message):
    __slots__ = ("mailbox_id", "public_folder_mailbox", "folder_change_vec")
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDER_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    FOLDER_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    mailbox_id: str
    public_folder_mailbox: str
    folder_change_vec: _containers.RepeatedCompositeFieldContainer[_outlook_pb2.FolderChange]
    def __init__(self, mailbox_id: _Optional[str] = ..., public_folder_mailbox: _Optional[str] = ..., folder_change_vec: _Optional[_Iterable[_Union[_outlook_pb2.FolderChange, _Mapping]]] = ...) -> None: ...

class UpdateFolderResult(_message.Message):
    __slots__ = ("error", "folder_id_vec", "o365_error_proto")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    folder_id_vec: _containers.RepeatedCompositeFieldContainer[_outlook_external_pb2.FolderId]
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., folder_id_vec: _Optional[_Iterable[_Union[_outlook_external_pb2.FolderId, _Mapping]]] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ...) -> None: ...
