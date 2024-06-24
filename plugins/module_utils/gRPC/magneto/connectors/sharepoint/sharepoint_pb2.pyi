from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeToken(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ODataMetadataVerbose(_message.Message):
    __slots__ = ("id", "uri", "etag", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    uri: str
    etag: str
    type: str
    def __init__(self, id: _Optional[str] = ..., uri: _Optional[str] = ..., etag: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class ResourcePath(_message.Message):
    __slots__ = ("decoded_url",)
    DECODED_URL_FIELD_NUMBER: _ClassVar[int]
    decoded_url: str
    def __init__(self, decoded_url: _Optional[str] = ...) -> None: ...

class List(_message.Message):
    __slots__ = ("metadata_verbose", "odata_type", "odata_id", "odata_etag", "odata_edit_link", "allow_content_types", "base_template", "base_type", "content_types_enabled", "crawl_non_default_views", "created", "current_change_token", "default_content_approval_workflow_id", "default_item_open_use_list_setting", "description", "direction", "disable_commenting", "disable_grid_editing", "document_template_url", "draft_version_visibility", "enable_attachments", "enable_folder_creation", "enable_minor_versions", "enable_moderation", "enable_request_sign_off", "enable_versioning", "entity_type_name", "exempt_from_block_download_of_non_viewable_files", "file_save_post_processing_enabled", "force_checkout", "has_external_data_source", "hidden", "id", "image_path", "image_url", "default_sensitivity_label_for_library", "irm_enabled", "irm_expire", "irm_reject", "is_application_list", "is_catalog", "is_private", "item_count", "last_item_deleted_date", "last_item_modified_date", "last_item_user_modified_date", "list_experience_options", "list_item_entity_type_full_name", "major_version_limit", "major_with_minor_versions_limit", "multiple_data_list", "no_crawl", "parent_web_path", "parent_web_url", "parser_disabled", "server_template_can_create_folders", "template_feature_id", "title", "root_folder", "has_unique_role_assignments")
    class RootFolder(_message.Message):
        __slots__ = ("name", "server_relative_url", "storage_metrics")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SERVER_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
        STORAGE_METRICS_FIELD_NUMBER: _ClassVar[int]
        name: str
        server_relative_url: str
        storage_metrics: StorageMetrics
        def __init__(self, name: _Optional[str] = ..., server_relative_url: _Optional[str] = ..., storage_metrics: _Optional[_Union[StorageMetrics, _Mapping]] = ...) -> None: ...
    METADATA_VERBOSE_FIELD_NUMBER: _ClassVar[int]
    ODATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ODATA_ID_FIELD_NUMBER: _ClassVar[int]
    ODATA_ETAG_FIELD_NUMBER: _ClassVar[int]
    ODATA_EDIT_LINK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CONTENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    BASE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    BASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CRAWL_NON_DEFAULT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CHANGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONTENT_APPROVAL_WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ITEM_OPEN_USE_LIST_SETTING_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_COMMENTING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_GRID_EDITING_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TEMPLATE_URL_FIELD_NUMBER: _ClassVar[int]
    DRAFT_VERSION_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FOLDER_CREATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINOR_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MODERATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REQUEST_SIGN_OFF_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VERSIONING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXEMPT_FROM_BLOCK_DOWNLOAD_OF_NON_VIEWABLE_FILES_FIELD_NUMBER: _ClassVar[int]
    FILE_SAVE_POST_PROCESSING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHECKOUT_FIELD_NUMBER: _ClassVar[int]
    HAS_EXTERNAL_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SENSITIVITY_LABEL_FOR_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    IRM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IRM_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    IRM_REJECT_FIELD_NUMBER: _ClassVar[int]
    IS_APPLICATION_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_CATALOG_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ITEM_DELETED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_ITEM_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_ITEM_USER_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    LIST_EXPERIENCE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ENTITY_TYPE_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_VERSION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAJOR_WITH_MINOR_VERSIONS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_DATA_LIST_FIELD_NUMBER: _ClassVar[int]
    NO_CRAWL_FIELD_NUMBER: _ClassVar[int]
    PARENT_WEB_PATH_FIELD_NUMBER: _ClassVar[int]
    PARENT_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    PARSER_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SERVER_TEMPLATE_CAN_CREATE_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ROOT_FOLDER_FIELD_NUMBER: _ClassVar[int]
    HAS_UNIQUE_ROLE_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    metadata_verbose: ODataMetadataVerbose
    odata_type: str
    odata_id: str
    odata_etag: str
    odata_edit_link: str
    allow_content_types: bool
    base_template: int
    base_type: int
    content_types_enabled: bool
    crawl_non_default_views: bool
    created: str
    current_change_token: ChangeToken
    default_content_approval_workflow_id: str
    default_item_open_use_list_setting: bool
    description: str
    direction: str
    disable_commenting: bool
    disable_grid_editing: bool
    document_template_url: str
    draft_version_visibility: int
    enable_attachments: bool
    enable_folder_creation: bool
    enable_minor_versions: bool
    enable_moderation: bool
    enable_request_sign_off: bool
    enable_versioning: bool
    entity_type_name: str
    exempt_from_block_download_of_non_viewable_files: bool
    file_save_post_processing_enabled: bool
    force_checkout: bool
    has_external_data_source: bool
    hidden: bool
    id: str
    image_path: ResourcePath
    image_url: str
    default_sensitivity_label_for_library: str
    irm_enabled: bool
    irm_expire: bool
    irm_reject: bool
    is_application_list: bool
    is_catalog: bool
    is_private: bool
    item_count: int
    last_item_deleted_date: str
    last_item_modified_date: str
    last_item_user_modified_date: str
    list_experience_options: int
    list_item_entity_type_full_name: str
    major_version_limit: int
    major_with_minor_versions_limit: int
    multiple_data_list: bool
    no_crawl: bool
    parent_web_path: ResourcePath
    parent_web_url: str
    parser_disabled: bool
    server_template_can_create_folders: bool
    template_feature_id: str
    title: str
    root_folder: List.RootFolder
    has_unique_role_assignments: bool
    def __init__(self, metadata_verbose: _Optional[_Union[ODataMetadataVerbose, _Mapping]] = ..., odata_type: _Optional[str] = ..., odata_id: _Optional[str] = ..., odata_etag: _Optional[str] = ..., odata_edit_link: _Optional[str] = ..., allow_content_types: bool = ..., base_template: _Optional[int] = ..., base_type: _Optional[int] = ..., content_types_enabled: bool = ..., crawl_non_default_views: bool = ..., created: _Optional[str] = ..., current_change_token: _Optional[_Union[ChangeToken, _Mapping]] = ..., default_content_approval_workflow_id: _Optional[str] = ..., default_item_open_use_list_setting: bool = ..., description: _Optional[str] = ..., direction: _Optional[str] = ..., disable_commenting: bool = ..., disable_grid_editing: bool = ..., document_template_url: _Optional[str] = ..., draft_version_visibility: _Optional[int] = ..., enable_attachments: bool = ..., enable_folder_creation: bool = ..., enable_minor_versions: bool = ..., enable_moderation: bool = ..., enable_request_sign_off: bool = ..., enable_versioning: bool = ..., entity_type_name: _Optional[str] = ..., exempt_from_block_download_of_non_viewable_files: bool = ..., file_save_post_processing_enabled: bool = ..., force_checkout: bool = ..., has_external_data_source: bool = ..., hidden: bool = ..., id: _Optional[str] = ..., image_path: _Optional[_Union[ResourcePath, _Mapping]] = ..., image_url: _Optional[str] = ..., default_sensitivity_label_for_library: _Optional[str] = ..., irm_enabled: bool = ..., irm_expire: bool = ..., irm_reject: bool = ..., is_application_list: bool = ..., is_catalog: bool = ..., is_private: bool = ..., item_count: _Optional[int] = ..., last_item_deleted_date: _Optional[str] = ..., last_item_modified_date: _Optional[str] = ..., last_item_user_modified_date: _Optional[str] = ..., list_experience_options: _Optional[int] = ..., list_item_entity_type_full_name: _Optional[str] = ..., major_version_limit: _Optional[int] = ..., major_with_minor_versions_limit: _Optional[int] = ..., multiple_data_list: bool = ..., no_crawl: bool = ..., parent_web_path: _Optional[_Union[ResourcePath, _Mapping]] = ..., parent_web_url: _Optional[str] = ..., parser_disabled: bool = ..., server_template_can_create_folders: bool = ..., template_feature_id: _Optional[str] = ..., title: _Optional[str] = ..., root_folder: _Optional[_Union[List.RootFolder, _Mapping]] = ..., has_unique_role_assignments: bool = ...) -> None: ...

class GetSiteScriptFromListRequest(_message.Message):
    __slots__ = ("list_url",)
    LIST_URL_FIELD_NUMBER: _ClassVar[int]
    list_url: str
    def __init__(self, list_url: _Optional[str] = ...) -> None: ...

class GetSiteScriptFromListResponse(_message.Message):
    __slots__ = ("site_script",)
    SITE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    site_script: str
    def __init__(self, site_script: _Optional[str] = ...) -> None: ...

class SiteScriptActionResult(_message.Message):
    __slots__ = ("error_code", "outcome", "outcome_text", "target", "target_id", "title")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    error_code: int
    outcome: str
    outcome_text: str
    target: str
    target_id: str
    title: str
    def __init__(self, error_code: _Optional[int] = ..., outcome: _Optional[str] = ..., outcome_text: _Optional[str] = ..., target: _Optional[str] = ..., target_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class SiteScriptActionResultVec(_message.Message):
    __slots__ = ("site_script_action_result_values",)
    SITE_SCRIPT_ACTION_RESULT_VALUES_FIELD_NUMBER: _ClassVar[int]
    site_script_action_result_values: _containers.RepeatedCompositeFieldContainer[SiteScriptActionResult]
    def __init__(self, site_script_action_result_values: _Optional[_Iterable[_Union[SiteScriptActionResult, _Mapping]]] = ...) -> None: ...

class SiteScriptActions(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _struct_pb2.ListValue
    def __init__(self, actions: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class ExecuteTemplateScriptRequest(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: str
    def __init__(self, script: _Optional[str] = ...) -> None: ...

class ExecuteTemplateScriptBody(_message.Message):
    __slots__ = ("actions", "schema", "bindings")
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    actions: _struct_pb2.ListValue
    schema: str
    bindings: _struct_pb2.Value
    def __init__(self, actions: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., schema: _Optional[str] = ..., bindings: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ChangeQuery(_message.Message):
    __slots__ = ("list", "item", "file", "folder", "field", "add", "update", "delete_object", "move", "rename", "restore", "role_assignment_add", "role_assignment_delete", "role_definition_add", "role_definition_delete", "role_definition_update", "system_update", "activity", "recursive_all", "fetch_limit", "change_token_start")
    LIST_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    ADD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    MOVE_FIELD_NUMBER: _ClassVar[int]
    RENAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ASSIGNMENT_ADD_FIELD_NUMBER: _ClassVar[int]
    ROLE_ASSIGNMENT_DELETE_FIELD_NUMBER: _ClassVar[int]
    ROLE_DEFINITION_ADD_FIELD_NUMBER: _ClassVar[int]
    ROLE_DEFINITION_DELETE_FIELD_NUMBER: _ClassVar[int]
    ROLE_DEFINITION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_ALL_FIELD_NUMBER: _ClassVar[int]
    FETCH_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TOKEN_START_FIELD_NUMBER: _ClassVar[int]
    list: bool
    item: bool
    file: bool
    folder: bool
    field: bool
    add: bool
    update: bool
    delete_object: bool
    move: bool
    rename: bool
    restore: bool
    role_assignment_add: bool
    role_assignment_delete: bool
    role_definition_add: bool
    role_definition_delete: bool
    role_definition_update: bool
    system_update: bool
    activity: bool
    recursive_all: bool
    fetch_limit: str
    change_token_start: ChangeToken
    def __init__(self, list: bool = ..., item: bool = ..., file: bool = ..., folder: bool = ..., field: bool = ..., add: bool = ..., update: bool = ..., delete_object: bool = ..., move: bool = ..., rename: bool = ..., restore: bool = ..., role_assignment_add: bool = ..., role_assignment_delete: bool = ..., role_definition_add: bool = ..., role_definition_delete: bool = ..., role_definition_update: bool = ..., system_update: bool = ..., activity: bool = ..., recursive_all: bool = ..., fetch_limit: _Optional[str] = ..., change_token_start: _Optional[_Union[ChangeToken, _Mapping]] = ...) -> None: ...

class Change(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoChange: _ClassVar[Change.Type]
        kAdd: _ClassVar[Change.Type]
        kUpdate: _ClassVar[Change.Type]
        kDelete: _ClassVar[Change.Type]
        kRename: _ClassVar[Change.Type]
        kMoveAway: _ClassVar[Change.Type]
        kMoveInto: _ClassVar[Change.Type]
        kRestore: _ClassVar[Change.Type]
        kRoleAdd: _ClassVar[Change.Type]
        kRoleDelete: _ClassVar[Change.Type]
        kRoleUpdate: _ClassVar[Change.Type]
        kAssignmentAdd: _ClassVar[Change.Type]
        kAssignmentDelete: _ClassVar[Change.Type]
        kMemberAdd: _ClassVar[Change.Type]
        kMemberDelete: _ClassVar[Change.Type]
        kSystemUpdate: _ClassVar[Change.Type]
        kNavigation: _ClassVar[Change.Type]
        kScopeAdd: _ClassVar[Change.Type]
        kScopeDelete: _ClassVar[Change.Type]
        kListContentTypeAdd: _ClassVar[Change.Type]
        kListContentTypeDelete: _ClassVar[Change.Type]
        kDirty: _ClassVar[Change.Type]
        kActivity: _ClassVar[Change.Type]
    kNoChange: Change.Type
    kAdd: Change.Type
    kUpdate: Change.Type
    kDelete: Change.Type
    kRename: Change.Type
    kMoveAway: Change.Type
    kMoveInto: Change.Type
    kRestore: Change.Type
    kRoleAdd: Change.Type
    kRoleDelete: Change.Type
    kRoleUpdate: Change.Type
    kAssignmentAdd: Change.Type
    kAssignmentDelete: Change.Type
    kMemberAdd: Change.Type
    kMemberDelete: Change.Type
    kSystemUpdate: Change.Type
    kNavigation: Change.Type
    kScopeAdd: Change.Type
    kScopeDelete: Change.Type
    kListContentTypeAdd: Change.Type
    kListContentTypeDelete: Change.Type
    kDirty: Change.Type
    kActivity: Change.Type
    def __init__(self) -> None: ...

class GetChangesRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: ChangeQuery
    def __init__(self, query: _Optional[_Union[ChangeQuery, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "is_hidden_in_ui", "login_name", "title", "email", "is_site_admin", "user_principal_name")
    class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOwner: _ClassVar[User.UserType]
        kMember: _ClassVar[User.UserType]
        kVisitor: _ClassVar[User.UserType]
    kOwner: User.UserType
    kMember: User.UserType
    kVisitor: User.UserType
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_IN_UI_FIELD_NUMBER: _ClassVar[int]
    LOGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_SITE_ADMIN_FIELD_NUMBER: _ClassVar[int]
    USER_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_hidden_in_ui: bool
    login_name: str
    title: str
    email: str
    is_site_admin: bool
    user_principal_name: str
    def __init__(self, id: _Optional[int] = ..., is_hidden_in_ui: bool = ..., login_name: _Optional[str] = ..., title: _Optional[str] = ..., email: _Optional[str] = ..., is_site_admin: bool = ..., user_principal_name: _Optional[str] = ...) -> None: ...

class SiteGroup(_message.Message):
    __slots__ = ("id", "is_hidden_in_ui", "login_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_IN_UI_FIELD_NUMBER: _ClassVar[int]
    LOGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_hidden_in_ui: bool
    login_name: str
    def __init__(self, id: _Optional[int] = ..., is_hidden_in_ui: bool = ..., login_name: _Optional[str] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("type", "id", "login_name", "title", "email", "owner_title")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    OWNER_TITLE_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: int
    login_name: str
    title: str
    email: str
    owner_title: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[int] = ..., login_name: _Optional[str] = ..., title: _Optional[str] = ..., email: _Optional[str] = ..., owner_title: _Optional[str] = ...) -> None: ...

class RoleDefinitionBindings(_message.Message):
    __slots__ = ("id", "name", "description", "role_type", "action")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdd: _ClassVar[RoleDefinitionBindings.ActionType]
        kRemove: _ClassVar[RoleDefinitionBindings.ActionType]
        kSkip: _ClassVar[RoleDefinitionBindings.ActionType]
    kAdd: RoleDefinitionBindings.ActionType
    kRemove: RoleDefinitionBindings.ActionType
    kSkip: RoleDefinitionBindings.ActionType
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    role_type: int
    action: RoleDefinitionBindings.ActionType
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., role_type: _Optional[int] = ..., action: _Optional[_Union[RoleDefinitionBindings.ActionType, str]] = ...) -> None: ...

class SPListItemPermissions(_message.Message):
    __slots__ = ("member", "role_definition", "principal_id")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    ROLE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    member: Member
    role_definition: _containers.RepeatedCompositeFieldContainer[RoleDefinitionBindings]
    principal_id: int
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ..., role_definition: _Optional[_Iterable[_Union[RoleDefinitionBindings, _Mapping]]] = ..., principal_id: _Optional[int] = ...) -> None: ...

class SPListItemUniquePermissions(_message.Message):
    __slots__ = ("permission_vec", "is_unique_role_assignment_present")
    PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_UNIQUE_ROLE_ASSIGNMENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
    permission_vec: _containers.RepeatedCompositeFieldContainer[SPListItemPermissions]
    is_unique_role_assignment_present: bool
    def __init__(self, permission_vec: _Optional[_Iterable[_Union[SPListItemPermissions, _Mapping]]] = ..., is_unique_role_assignment_present: bool = ...) -> None: ...

class SPListItemAttachments(_message.Message):
    __slots__ = ("attachment_name", "attachment_url", "attachment_path", "server_relative_url", "attachment_size", "is_skipped_from_backup", "server_relative_path")
    class ServerRelativePath(_message.Message):
        __slots__ = ("decoded_url",)
        DECODED_URL_FIELD_NUMBER: _ClassVar[int]
        decoded_url: str
        def __init__(self, decoded_url: _Optional[str] = ...) -> None: ...
    ATTACHMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_URL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_PATH_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_SKIPPED_FROM_BACKUP_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    attachment_name: str
    attachment_url: str
    attachment_path: str
    server_relative_url: str
    attachment_size: int
    is_skipped_from_backup: bool
    server_relative_path: SPListItemAttachments.ServerRelativePath
    def __init__(self, attachment_name: _Optional[str] = ..., attachment_url: _Optional[str] = ..., attachment_path: _Optional[str] = ..., server_relative_url: _Optional[str] = ..., attachment_size: _Optional[int] = ..., is_skipped_from_backup: bool = ..., server_relative_path: _Optional[_Union[SPListItemAttachments.ServerRelativePath, _Mapping]] = ...) -> None: ...

class ListItemMetadataProto(_message.Message):
    __slots__ = ("list_item", "list_item_comments", "permissions", "attachments_vec", "is_root_item")
    LIST_ITEM_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_ITEM_FIELD_NUMBER: _ClassVar[int]
    list_item: _struct_pb2.Value
    list_item_comments: _struct_pb2.ListValue
    permissions: SPListItemUniquePermissions
    attachments_vec: _containers.RepeatedCompositeFieldContainer[SPListItemAttachments]
    is_root_item: bool
    def __init__(self, list_item: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., list_item_comments: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., permissions: _Optional[_Union[SPListItemUniquePermissions, _Mapping]] = ..., attachments_vec: _Optional[_Iterable[_Union[SPListItemAttachments, _Mapping]]] = ..., is_root_item: bool = ...) -> None: ...

class ListItemPermissionMemberLookupProto(_message.Message):
    __slots__ = ("user", "group_id")
    USER_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedCompositeFieldContainer[Member]
    group_id: int
    def __init__(self, user: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., group_id: _Optional[int] = ...) -> None: ...

class StorageMetrics(_message.Message):
    __slots__ = ("total_file_count", "total_file_stream_size", "total_size", "signed_total_size")
    TOTAL_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_STREAM_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    total_file_count: int
    total_file_stream_size: int
    total_size: int
    signed_total_size: int
    def __init__(self, total_file_count: _Optional[int] = ..., total_file_stream_size: _Optional[int] = ..., total_size: _Optional[int] = ..., signed_total_size: _Optional[int] = ...) -> None: ...
