from google.protobuf import struct_pb2 as _struct_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.connectors.sharepoint import sharepoint_pb2 as _sharepoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseArg(_message.Message):
    __slots__ = ("sharepoint_domain_name", "web_url", "continue_on_error")
    SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_ERROR_FIELD_NUMBER: _ClassVar[int]
    sharepoint_domain_name: str
    web_url: str
    continue_on_error: bool
    def __init__(self, sharepoint_domain_name: _Optional[str] = ..., web_url: _Optional[str] = ..., continue_on_error: bool = ...) -> None: ...

class GetTokenArg(_message.Message):
    __slots__ = ("sharepoint_domain_name", "ms_graph_credentials")
    SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    MS_GRAPH_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    sharepoint_domain_name: str
    ms_graph_credentials: _credentials_pb2.MSGraphAppCredentials
    def __init__(self, sharepoint_domain_name: _Optional[str] = ..., ms_graph_credentials: _Optional[_Union[_credentials_pb2.MSGraphAppCredentials, _Mapping]] = ...) -> None: ...

class GetTokenResult(_message.Message):
    __slots__ = ("access_token",)
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class FileContent(_message.Message):
    __slots__ = ("file_content",)
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    file_content: bytes
    def __init__(self, file_content: _Optional[bytes] = ...) -> None: ...

class UpdateFileContentArg(_message.Message):
    __slots__ = ("base_arg", "parent_folder_path", "file_name", "content")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    parent_folder_path: str
    file_name: str
    content: FileContent
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., parent_folder_path: _Optional[str] = ..., file_name: _Optional[str] = ..., content: _Optional[_Union[FileContent, _Mapping]] = ...) -> None: ...

class UpdateFileContentResult(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateFileContentPartialArg(_message.Message):
    __slots__ = ("base_arg", "file_url", "upload_id", "upload_step", "offset", "content", "parent_folder_path", "file_name")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_STEP_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    file_url: str
    upload_id: str
    upload_step: str
    offset: int
    content: FileContent
    parent_folder_path: str
    file_name: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., file_url: _Optional[str] = ..., upload_id: _Optional[str] = ..., upload_step: _Optional[str] = ..., offset: _Optional[int] = ..., content: _Optional[_Union[FileContent, _Mapping]] = ..., parent_folder_path: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...

class UpdateFileContentPartialResult(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSystemFolderArg(_message.Message):
    __slots__ = ("base_arg", "folder_path")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    folder_path: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., folder_path: _Optional[str] = ...) -> None: ...

class CreateSystemFolderResult(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSiteAssetsListArg(_message.Message):
    __slots__ = ("base_arg",)
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ...) -> None: ...

class CreateSiteAssetsListResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Web(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetWebIdsArg(_message.Message):
    __slots__ = ("base_arg", "web_type_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    WEB_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    web_type_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., web_type_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetWebIdsResult(_message.Message):
    __slots__ = ("web_vec",)
    WEB_VEC_FIELD_NUMBER: _ClassVar[int]
    web_vec: _containers.RepeatedCompositeFieldContainer[Web]
    def __init__(self, web_vec: _Optional[_Iterable[_Union[Web, _Mapping]]] = ...) -> None: ...

class GetSiteInformationArg(_message.Message):
    __slots__ = ("base_arg",)
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ...) -> None: ...

class GetSiteInformationResult(_message.Message):
    __slots__ = ("metadata", "type", "odata_id", "edit_link", "allow_rss_feeds", "alternate_css_url", "app_instance_id", "configuration", "created", "custom_master_url", "description", "design_package_id", "document_library_callout_office_web_app_previewers_disabled", "enable_minimal_download", "footer_emphasis", "footer_enabled", "footer_layout", "header_emphasis", "header_layout", "hide_title_in_header", "horizontal_quick_launch", "id", "is_homepage_modernized", "is_multilingual", "is_revert_homepage_link_hidden", "keep_field_user_resources", "language", "last_item_modified_date", "last_item_user_modified_date", "logo_alignment", "master_url", "mega_menu_enabled", "nav_audience_targeting_enabled", "no_crawl", "object_cache_enabled", "overwrite_translations_on_change", "resource_path", "quick_launch_enabled", "recycle_bin_enabled", "search_scope", "server_relative_url", "site_logo_url", "syndication_enabled", "tenant_admin_members_can_share", "title", "tree_view_enabled", "ui_version", "ui_version_configuration_enabled", "url", "web_template", "welcome_page")
    class Resourcepath(_message.Message):
        __slots__ = ("decoded_url",)
        DECODED_URL_FIELD_NUMBER: _ClassVar[int]
        decoded_url: str
        def __init__(self, decoded_url: _Optional[str] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ODATA_ID_FIELD_NUMBER: _ClassVar[int]
    EDIT_LINK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RSS_FEEDS_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_CSS_URL_FIELD_NUMBER: _ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESIGN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_LIBRARY_CALLOUT_OFFICE_WEB_APP_PREVIEWERS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MINIMAL_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    FOOTER_EMPHASIS_FIELD_NUMBER: _ClassVar[int]
    FOOTER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FOOTER_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    HEADER_EMPHASIS_FIELD_NUMBER: _ClassVar[int]
    HEADER_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    HIDE_TITLE_IN_HEADER_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_QUICK_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_HOMEPAGE_MODERNIZED_FIELD_NUMBER: _ClassVar[int]
    IS_MULTILINGUAL_FIELD_NUMBER: _ClassVar[int]
    IS_REVERT_HOMEPAGE_LINK_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    KEEP_FIELD_USER_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LAST_ITEM_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_ITEM_USER_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    LOGO_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    MEGA_MENU_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAV_AUDIENCE_TARGETING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NO_CRAWL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CACHE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_TRANSLATIONS_ON_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    QUICK_LAUNCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RECYCLE_BIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    SITE_LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    SYNDICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TENANT_ADMIN_MEMBERS_CAN_SHARE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TREE_VIEW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UI_VERSION_FIELD_NUMBER: _ClassVar[int]
    UI_VERSION_CONFIGURATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WEB_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WELCOME_PAGE_FIELD_NUMBER: _ClassVar[int]
    metadata: str
    type: str
    odata_id: str
    edit_link: str
    allow_rss_feeds: bool
    alternate_css_url: str
    app_instance_id: str
    configuration: int
    created: str
    custom_master_url: str
    description: str
    design_package_id: str
    document_library_callout_office_web_app_previewers_disabled: bool
    enable_minimal_download: bool
    footer_emphasis: int
    footer_enabled: bool
    footer_layout: int
    header_emphasis: int
    header_layout: int
    hide_title_in_header: bool
    horizontal_quick_launch: bool
    id: str
    is_homepage_modernized: bool
    is_multilingual: bool
    is_revert_homepage_link_hidden: bool
    keep_field_user_resources: bool
    language: int
    last_item_modified_date: str
    last_item_user_modified_date: str
    logo_alignment: int
    master_url: str
    mega_menu_enabled: bool
    nav_audience_targeting_enabled: bool
    no_crawl: bool
    object_cache_enabled: bool
    overwrite_translations_on_change: bool
    resource_path: GetSiteInformationResult.Resourcepath
    quick_launch_enabled: bool
    recycle_bin_enabled: bool
    search_scope: int
    server_relative_url: str
    site_logo_url: str
    syndication_enabled: bool
    tenant_admin_members_can_share: int
    title: str
    tree_view_enabled: bool
    ui_version: int
    ui_version_configuration_enabled: bool
    url: str
    web_template: str
    welcome_page: str
    def __init__(self, metadata: _Optional[str] = ..., type: _Optional[str] = ..., odata_id: _Optional[str] = ..., edit_link: _Optional[str] = ..., allow_rss_feeds: bool = ..., alternate_css_url: _Optional[str] = ..., app_instance_id: _Optional[str] = ..., configuration: _Optional[int] = ..., created: _Optional[str] = ..., custom_master_url: _Optional[str] = ..., description: _Optional[str] = ..., design_package_id: _Optional[str] = ..., document_library_callout_office_web_app_previewers_disabled: bool = ..., enable_minimal_download: bool = ..., footer_emphasis: _Optional[int] = ..., footer_enabled: bool = ..., footer_layout: _Optional[int] = ..., header_emphasis: _Optional[int] = ..., header_layout: _Optional[int] = ..., hide_title_in_header: bool = ..., horizontal_quick_launch: bool = ..., id: _Optional[str] = ..., is_homepage_modernized: bool = ..., is_multilingual: bool = ..., is_revert_homepage_link_hidden: bool = ..., keep_field_user_resources: bool = ..., language: _Optional[int] = ..., last_item_modified_date: _Optional[str] = ..., last_item_user_modified_date: _Optional[str] = ..., logo_alignment: _Optional[int] = ..., master_url: _Optional[str] = ..., mega_menu_enabled: bool = ..., nav_audience_targeting_enabled: bool = ..., no_crawl: bool = ..., object_cache_enabled: bool = ..., overwrite_translations_on_change: bool = ..., resource_path: _Optional[_Union[GetSiteInformationResult.Resourcepath, _Mapping]] = ..., quick_launch_enabled: bool = ..., recycle_bin_enabled: bool = ..., search_scope: _Optional[int] = ..., server_relative_url: _Optional[str] = ..., site_logo_url: _Optional[str] = ..., syndication_enabled: bool = ..., tenant_admin_members_can_share: _Optional[int] = ..., title: _Optional[str] = ..., tree_view_enabled: bool = ..., ui_version: _Optional[int] = ..., ui_version_configuration_enabled: bool = ..., url: _Optional[str] = ..., web_template: _Optional[str] = ..., welcome_page: _Optional[str] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: SharepointError
    def __init__(self, error: _Optional[_Union[SharepointError, _Mapping]] = ...) -> None: ...

class SharepointError(_message.Message):
    __slots__ = ("code", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: str
    error: SharepointErrorMessage
    def __init__(self, code: _Optional[str] = ..., error: _Optional[_Union[SharepointErrorMessage, _Mapping]] = ...) -> None: ...

class SharepointErrorMessage(_message.Message):
    __slots__ = ("err_msg",)
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    err_msg: str
    def __init__(self, err_msg: _Optional[str] = ...) -> None: ...

class GetSPListsArg(_message.Message):
    __slots__ = ("base_arg", "list_id_vec", "list_title_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id_vec: _containers.RepeatedScalarFieldContainer[str]
    list_title_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id_vec: _Optional[_Iterable[str]] = ..., list_title_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSPListsResult(_message.Message):
    __slots__ = ("list_vec",)
    LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    list_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.List]
    def __init__(self, list_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.List, _Mapping]]] = ...) -> None: ...

class GetSiteScriptFromListArg(_message.Message):
    __slots__ = ("base_arg", "list_title_vec", "list_relative_url_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_VEC_FIELD_NUMBER: _ClassVar[int]
    LIST_RELATIVE_URL_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_title_vec: _containers.RepeatedScalarFieldContainer[str]
    list_relative_url_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_title_vec: _Optional[_Iterable[str]] = ..., list_relative_url_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSiteScriptFromListResult(_message.Message):
    __slots__ = ("list_script_vec",)
    LIST_SCRIPT_VEC_FIELD_NUMBER: _ClassVar[int]
    list_script_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, list_script_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteTemplateScriptArg(_message.Message):
    __slots__ = ("base_arg", "list_script_vec", "ignore_list_exists_error")
    class ListScript(_message.Message):
        __slots__ = ("new_list_name", "script")
        NEW_LIST_NAME_FIELD_NUMBER: _ClassVar[int]
        SCRIPT_FIELD_NUMBER: _ClassVar[int]
        new_list_name: str
        script: str
        def __init__(self, new_list_name: _Optional[str] = ..., script: _Optional[str] = ...) -> None: ...
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_SCRIPT_VEC_FIELD_NUMBER: _ClassVar[int]
    IGNORE_LIST_EXISTS_ERROR_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_script_vec: _containers.RepeatedCompositeFieldContainer[ExecuteTemplateScriptArg.ListScript]
    ignore_list_exists_error: bool
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_script_vec: _Optional[_Iterable[_Union[ExecuteTemplateScriptArg.ListScript, _Mapping]]] = ..., ignore_list_exists_error: bool = ...) -> None: ...

class ExecuteTemplateScriptResult(_message.Message):
    __slots__ = ("script_result_vec",)
    SCRIPT_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    script_result_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.SiteScriptActionResultVec]
    def __init__(self, script_result_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.SiteScriptActionResultVec, _Mapping]]] = ...) -> None: ...

class GetSPListItemsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "next_link", "max_pages_to_fetch", "fetch_changes_in_pages", "page_size", "item_ids_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHANGES_IN_PAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ITEM_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    next_link: str
    max_pages_to_fetch: int
    fetch_changes_in_pages: bool
    page_size: int
    item_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., next_link: _Optional[str] = ..., max_pages_to_fetch: _Optional[int] = ..., fetch_changes_in_pages: bool = ..., page_size: _Optional[int] = ..., item_ids_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSPListItemsResult(_message.Message):
    __slots__ = ("list_items", "next_link", "skipped_item_ids_vec")
    LIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_ITEM_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    list_items: _struct_pb2.ListValue
    next_link: str
    skipped_item_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, list_items: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., next_link: _Optional[str] = ..., skipped_item_ids_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSPListItemsResponse(_message.Message):
    __slots__ = ("root", "next_link")
    class RootNode(_message.Message):
        __slots__ = ("list_items",)
        LIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
        list_items: _struct_pb2.ListValue
        def __init__(self, list_items: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...
    ROOT_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    root: GetSPListItemsResponse.RootNode
    next_link: str
    def __init__(self, root: _Optional[_Union[GetSPListItemsResponse.RootNode, _Mapping]] = ..., next_link: _Optional[str] = ...) -> None: ...

class PutSPListItemsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_items", "list_item_entity_type_full_name")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ENTITY_TYPE_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_items: _struct_pb2.ListValue
    list_item_entity_type_full_name: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_items: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., list_item_entity_type_full_name: _Optional[str] = ...) -> None: ...

class PutSPListItemsResult(_message.Message):
    __slots__ = ("restored_item_info_vec",)
    class RestoredItemInfo(_message.Message):
        __slots__ = ("restored_item_id", "sharepoint_error")
        RESTORED_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        SHAREPOINT_ERROR_FIELD_NUMBER: _ClassVar[int]
        restored_item_id: int
        sharepoint_error: ErrorContext
        def __init__(self, restored_item_id: _Optional[int] = ..., sharepoint_error: _Optional[_Union[ErrorContext, _Mapping]] = ...) -> None: ...
    RESTORED_ITEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    restored_item_info_vec: _containers.RepeatedCompositeFieldContainer[PutSPListItemsResult.RestoredItemInfo]
    def __init__(self, restored_item_info_vec: _Optional[_Iterable[_Union[PutSPListItemsResult.RestoredItemInfo, _Mapping]]] = ...) -> None: ...

class GenericSPListItemsResponse(_message.Message):
    __slots__ = ("root",)
    ROOT_FIELD_NUMBER: _ClassVar[int]
    root: _struct_pb2.Value
    def __init__(self, root: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class GetSPListChangesArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "change_token_start", "max_pages_to_fetch", "fetch_changes_in_pages", "page_size")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TOKEN_START_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHANGES_IN_PAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    change_token_start: _sharepoint_pb2.ChangeToken
    max_pages_to_fetch: int
    fetch_changes_in_pages: bool
    page_size: int
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., change_token_start: _Optional[_Union[_sharepoint_pb2.ChangeToken, _Mapping]] = ..., max_pages_to_fetch: _Optional[int] = ..., fetch_changes_in_pages: bool = ..., page_size: _Optional[int] = ...) -> None: ...

class GetSPListChangesResult(_message.Message):
    __slots__ = ("list_changes", "fetched_all_changes", "next_change_token_start")
    LIST_CHANGES_FIELD_NUMBER: _ClassVar[int]
    FETCHED_ALL_CHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CHANGE_TOKEN_START_FIELD_NUMBER: _ClassVar[int]
    list_changes: _struct_pb2.ListValue
    fetched_all_changes: bool
    next_change_token_start: _sharepoint_pb2.ChangeToken
    def __init__(self, list_changes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., fetched_all_changes: bool = ..., next_change_token_start: _Optional[_Union[_sharepoint_pb2.ChangeToken, _Mapping]] = ...) -> None: ...

class GetSiteAdminsArg(_message.Message):
    __slots__ = ("base_arg",)
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ...) -> None: ...

class GetSiteAdminsResult(_message.Message):
    __slots__ = ("site_admin_vec",)
    SITE_ADMIN_VEC_FIELD_NUMBER: _ClassVar[int]
    site_admin_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    def __init__(self, site_admin_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ...) -> None: ...

class SetSiteAdminsArg(_message.Message):
    __slots__ = ("base_arg", "site_admin_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    SITE_ADMIN_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    site_admin_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., site_admin_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ...) -> None: ...

class SetSiteAdminsResult(_message.Message):
    __slots__ = ("site_admin_error_vec",)
    SITE_ADMIN_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    site_admin_error_vec: _containers.RepeatedCompositeFieldContainer[_o365_error_pb2.O365ErrorProto]
    def __init__(self, site_admin_error_vec: _Optional[_Iterable[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]]] = ...) -> None: ...

class GetSiteUsersArg(_message.Message):
    __slots__ = ("base_arg", "fetch_user_type_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    FETCH_USER_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    fetch_user_type_vec: _containers.RepeatedScalarFieldContainer[_sharepoint_pb2.User.UserType]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., fetch_user_type_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User.UserType, str]]] = ...) -> None: ...

class SiteUsersResponse(_message.Message):
    __slots__ = ("users_vec",)
    USERS_VEC_FIELD_NUMBER: _ClassVar[int]
    users_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    def __init__(self, users_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ...) -> None: ...

class GetSiteUsersResult(_message.Message):
    __slots__ = ("site_owners_vec", "site_members_vec", "site_visitors_vec")
    SITE_OWNERS_VEC_FIELD_NUMBER: _ClassVar[int]
    SITE_MEMBERS_VEC_FIELD_NUMBER: _ClassVar[int]
    SITE_VISITORS_VEC_FIELD_NUMBER: _ClassVar[int]
    site_owners_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    site_members_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    site_visitors_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.User]
    def __init__(self, site_owners_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ..., site_members_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ..., site_visitors_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.User, _Mapping]]] = ...) -> None: ...

class GetSPListItemCommentsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id", "next_link", "max_pages_to_fetch", "fetch_changes_in_pages", "page_size")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGES_TO_FETCH_FIELD_NUMBER: _ClassVar[int]
    FETCH_CHANGES_IN_PAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    next_link: str
    max_pages_to_fetch: int
    fetch_changes_in_pages: bool
    page_size: int
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ..., next_link: _Optional[str] = ..., max_pages_to_fetch: _Optional[int] = ..., fetch_changes_in_pages: bool = ..., page_size: _Optional[int] = ...) -> None: ...

class GetSPListItemCommentsResult(_message.Message):
    __slots__ = ("root", "next_link")
    class RootNode(_message.Message):
        __slots__ = ("list_item_comments",)
        LIST_ITEM_COMMENTS_FIELD_NUMBER: _ClassVar[int]
        list_item_comments: _struct_pb2.ListValue
        def __init__(self, list_item_comments: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...
    ROOT_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    root: GetSPListItemCommentsResult.RootNode
    next_link: str
    def __init__(self, root: _Optional[_Union[GetSPListItemCommentsResult.RootNode, _Mapping]] = ..., next_link: _Optional[str] = ...) -> None: ...

class PutSPListItemCommentsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id", "list_item_comments", "skip_mentions")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    SKIP_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    list_item_comments: _struct_pb2.ListValue
    skip_mentions: bool
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ..., list_item_comments: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ..., skip_mentions: bool = ...) -> None: ...

class PutSPListItemCommentsResult(_message.Message):
    __slots__ = ("comments_error_vec", "sharepoint_error")
    class PutSPListItemCommentsError(_message.Message):
        __slots__ = ("error", "comment_idx")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        COMMENT_IDX_FIELD_NUMBER: _ClassVar[int]
        error: _o365_error_pb2.O365ErrorProto
        comment_idx: int
        def __init__(self, error: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., comment_idx: _Optional[int] = ...) -> None: ...
    COMMENTS_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_ERROR_FIELD_NUMBER: _ClassVar[int]
    comments_error_vec: _containers.RepeatedCompositeFieldContainer[PutSPListItemCommentsResult.PutSPListItemCommentsError]
    sharepoint_error: ErrorContext
    def __init__(self, comments_error_vec: _Optional[_Iterable[_Union[PutSPListItemCommentsResult.PutSPListItemCommentsError, _Mapping]]] = ..., sharepoint_error: _Optional[_Union[ErrorContext, _Mapping]] = ...) -> None: ...

class CheckSPListItemUniqueRolesArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ...) -> None: ...

class CheckSPListItemUniqueRolesResult(_message.Message):
    __slots__ = ("is_unique_role_assignment_present",)
    IS_UNIQUE_ROLE_ASSIGNMENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
    is_unique_role_assignment_present: bool
    def __init__(self, is_unique_role_assignment_present: bool = ...) -> None: ...

class GetSPListItemPermissionsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id", "get_list_permission")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GET_LIST_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    get_list_permission: bool
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ..., get_list_permission: bool = ...) -> None: ...

class GetSPListItemPermissionsResult(_message.Message):
    __slots__ = ("permission_vec", "is_unique_role_assignment_present", "is_list_permission")
    PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_UNIQUE_ROLE_ASSIGNMENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
    IS_LIST_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.SPListItemPermissions]
    is_unique_role_assignment_present: bool
    is_list_permission: bool
    def __init__(self, permission_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.SPListItemPermissions, _Mapping]]] = ..., is_unique_role_assignment_present: bool = ..., is_list_permission: bool = ...) -> None: ...

class SPListItemBreakRoleInheritanceArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ...) -> None: ...

class SPListItemBreakRoleInheritanceResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PutSPListItemPermissionsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id", "permission_vec", "is_unique_role_assignment_present", "put_list_permission", "copy_role_assignments")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_UNIQUE_ROLE_ASSIGNMENT_PRESENT_FIELD_NUMBER: _ClassVar[int]
    PUT_LIST_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    COPY_ROLE_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    permission_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.SPListItemPermissions]
    is_unique_role_assignment_present: bool
    put_list_permission: bool
    copy_role_assignments: bool
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ..., permission_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.SPListItemPermissions, _Mapping]]] = ..., is_unique_role_assignment_present: bool = ..., put_list_permission: bool = ..., copy_role_assignments: bool = ...) -> None: ...

class PutSPListItemPermissionsResult(_message.Message):
    __slots__ = ("permissions_error_vec", "sharepoint_error")
    class PutSPListItemPermissionsError(_message.Message):
        __slots__ = ("error", "p_index", "r_index")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        P_INDEX_FIELD_NUMBER: _ClassVar[int]
        R_INDEX_FIELD_NUMBER: _ClassVar[int]
        error: _o365_error_pb2.O365ErrorProto
        p_index: int
        r_index: int
        def __init__(self, error: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., p_index: _Optional[int] = ..., r_index: _Optional[int] = ...) -> None: ...
    PERMISSIONS_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_ERROR_FIELD_NUMBER: _ClassVar[int]
    permissions_error_vec: _containers.RepeatedCompositeFieldContainer[PutSPListItemPermissionsResult.PutSPListItemPermissionsError]
    sharepoint_error: ErrorContext
    def __init__(self, permissions_error_vec: _Optional[_Iterable[_Union[PutSPListItemPermissionsResult.PutSPListItemPermissionsError, _Mapping]]] = ..., sharepoint_error: _Optional[_Union[ErrorContext, _Mapping]] = ...) -> None: ...

class GetSPListItemAttachmentsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ...) -> None: ...

class GetSPListItemAttachmentsResult(_message.Message):
    __slots__ = ("attachments_vec",)
    ATTACHMENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    attachments_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.SPListItemAttachments]
    def __init__(self, attachments_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.SPListItemAttachments, _Mapping]]] = ...) -> None: ...

class GetSPFileByServerRelativeUrlArg(_message.Message):
    __slots__ = ("base_arg", "server_relative_url", "attachment_name")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    server_relative_url: str
    attachment_name: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., server_relative_url: _Optional[str] = ..., attachment_name: _Optional[str] = ...) -> None: ...

class GetSPFileByServerRelativeUrlResult(_message.Message):
    __slots__ = ("file_name", "length")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    length: int
    def __init__(self, file_name: _Optional[str] = ..., length: _Optional[int] = ...) -> None: ...

class GetSPObjectByServerRelativePathArg(_message.Message):
    __slots__ = ("base_arg", "server_relative_path", "expand_storage_metrics", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[GetSPObjectByServerRelativePathArg.Type]
        kFolder: _ClassVar[GetSPObjectByServerRelativePathArg.Type]
    kFile: GetSPObjectByServerRelativePathArg.Type
    kFolder: GetSPObjectByServerRelativePathArg.Type
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    SERVER_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPAND_STORAGE_METRICS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    server_relative_path: str
    expand_storage_metrics: bool
    type: GetSPObjectByServerRelativePathArg.Type
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., server_relative_path: _Optional[str] = ..., expand_storage_metrics: bool = ..., type: _Optional[_Union[GetSPObjectByServerRelativePathArg.Type, str]] = ...) -> None: ...

class GetSPObjectByServerRelativePathResult(_message.Message):
    __slots__ = ("folder_name", "item_count", "storage_metrics", "length")
    FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_METRICS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    folder_name: str
    item_count: int
    storage_metrics: _sharepoint_pb2.StorageMetrics
    length: int
    def __init__(self, folder_name: _Optional[str] = ..., item_count: _Optional[int] = ..., storage_metrics: _Optional[_Union[_sharepoint_pb2.StorageMetrics, _Mapping]] = ..., length: _Optional[int] = ...) -> None: ...

class GetSPListItemAttachmentsContentArg(_message.Message):
    __slots__ = ("base_arg", "attachments_vec", "list_id", "list_title", "list_item_id")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    attachments_vec: _containers.RepeatedCompositeFieldContainer[_sharepoint_pb2.SPListItemAttachments]
    list_id: str
    list_title: str
    list_item_id: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., attachments_vec: _Optional[_Iterable[_Union[_sharepoint_pb2.SPListItemAttachments, _Mapping]]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ...) -> None: ...

class SPListItemAttachmentsData(_message.Message):
    __slots__ = ("attachment_name", "attachment_data", "sharepoint_error")
    ATTACHMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_ERROR_FIELD_NUMBER: _ClassVar[int]
    attachment_name: str
    attachment_data: bytes
    sharepoint_error: ErrorContext
    def __init__(self, attachment_name: _Optional[str] = ..., attachment_data: _Optional[bytes] = ..., sharepoint_error: _Optional[_Union[ErrorContext, _Mapping]] = ...) -> None: ...

class GetSPListItemAttachmentsContentResult(_message.Message):
    __slots__ = ("attachments_vec",)
    ATTACHMENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    attachments_vec: _containers.RepeatedCompositeFieldContainer[SPListItemAttachmentsData]
    def __init__(self, attachments_vec: _Optional[_Iterable[_Union[SPListItemAttachmentsData, _Mapping]]] = ...) -> None: ...

class PutSPListItemAttachmentsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title", "list_item_id", "attachments_vec")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    LIST_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    list_item_id: str
    attachments_vec: _containers.RepeatedCompositeFieldContainer[SPListItemAttachmentsData]
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ..., list_item_id: _Optional[str] = ..., attachments_vec: _Optional[_Iterable[_Union[SPListItemAttachmentsData, _Mapping]]] = ...) -> None: ...

class PutSPListItemAttachmentsResult(_message.Message):
    __slots__ = ("attachments_error_vec",)
    class PutSPListItemAttachmentsError(_message.Message):
        __slots__ = ("error", "attachment_idx")
        ERROR_FIELD_NUMBER: _ClassVar[int]
        ATTACHMENT_IDX_FIELD_NUMBER: _ClassVar[int]
        error: _o365_error_pb2.O365ErrorProto
        attachment_idx: int
        def __init__(self, error: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., attachment_idx: _Optional[int] = ...) -> None: ...
    ATTACHMENTS_ERROR_VEC_FIELD_NUMBER: _ClassVar[int]
    attachments_error_vec: _containers.RepeatedCompositeFieldContainer[PutSPListItemAttachmentsResult.PutSPListItemAttachmentsError]
    def __init__(self, attachments_error_vec: _Optional[_Iterable[_Union[PutSPListItemAttachmentsResult.PutSPListItemAttachmentsError, _Mapping]]] = ...) -> None: ...

class GetSPListFieldsArg(_message.Message):
    __slots__ = ("base_arg", "list_id", "list_title")
    BASE_ARG_FIELD_NUMBER: _ClassVar[int]
    LIST_ID_FIELD_NUMBER: _ClassVar[int]
    LIST_TITLE_FIELD_NUMBER: _ClassVar[int]
    base_arg: BaseArg
    list_id: str
    list_title: str
    def __init__(self, base_arg: _Optional[_Union[BaseArg, _Mapping]] = ..., list_id: _Optional[str] = ..., list_title: _Optional[str] = ...) -> None: ...

class GetSPListFieldsResult(_message.Message):
    __slots__ = ("root",)
    class RootNode(_message.Message):
        __slots__ = ("list_fields",)
        LIST_FIELDS_FIELD_NUMBER: _ClassVar[int]
        list_fields: _struct_pb2.ListValue
        def __init__(self, list_fields: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...
    ROOT_FIELD_NUMBER: _ClassVar[int]
    root: GetSPListFieldsResult.RootNode
    def __init__(self, root: _Optional[_Union[GetSPListFieldsResult.RootNode, _Mapping]] = ...) -> None: ...
