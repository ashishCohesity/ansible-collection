from google.protobuf import struct_pb2 as _struct_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import error_pb2 as _error_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.base import sub_task_pb2 as _sub_task_pb2
from magneto.connectors.ms_graph import graph_enums_pb2 as _graph_enums_pb2
from magneto.connectors.ms_graph import graph_external_pb2 as _graph_external_pb2
from magneto.connectors.o365 import o365_error_pb2 as _o365_error_pb2
from magneto.connectors.sharepoint import sharepoint_pb2 as _sharepoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenResult(_message.Message):
    __slots__ = ("access_token",)
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class EntityType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUser: _ClassVar[EntityType.Type]
        kGroup: _ClassVar[EntityType.Type]
        kSite: _ClassVar[EntityType.Type]
    kUser: EntityType.Type
    kGroup: EntityType.Type
    kSite: EntityType.Type
    def __init__(self) -> None: ...

class UserRoleInGroup(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOwner: _ClassVar[UserRoleInGroup.Type]
        kMember: _ClassVar[UserRoleInGroup.Type]
    kOwner: UserRoleInGroup.Type
    kMember: UserRoleInGroup.Type
    def __init__(self) -> None: ...

class User(_message.Message):
    __slots__ = ("display_name", "mail", "id", "provisioned_plans", "drive_id_vec", "drive_size_vec", "department", "city", "country", "designation", "assigned_plans", "user_principal_name", "proxy_addresses_vec", "on_premises_sync_enabled", "show_in_address_list", "user_type", "my_site", "account_enabled", "odata_type")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_PLANS_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    DRIVE_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DESIGNATION_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_PLANS_FIELD_NUMBER: _ClassVar[int]
    USER_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    PROXY_ADDRESSES_VEC_FIELD_NUMBER: _ClassVar[int]
    ON_PREMISES_SYNC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOW_IN_ADDRESS_LIST_FIELD_NUMBER: _ClassVar[int]
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MY_SITE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ODATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    mail: str
    id: str
    provisioned_plans: _containers.RepeatedCompositeFieldContainer[ProvisionedPlan]
    drive_id_vec: _containers.RepeatedScalarFieldContainer[str]
    drive_size_vec: _containers.RepeatedScalarFieldContainer[int]
    department: str
    city: str
    country: str
    designation: str
    assigned_plans: _containers.RepeatedCompositeFieldContainer[AssignedPlan]
    user_principal_name: str
    proxy_addresses_vec: _containers.RepeatedScalarFieldContainer[str]
    on_premises_sync_enabled: bool
    show_in_address_list: bool
    user_type: str
    my_site: str
    account_enabled: bool
    odata_type: str
    def __init__(self, display_name: _Optional[str] = ..., mail: _Optional[str] = ..., id: _Optional[str] = ..., provisioned_plans: _Optional[_Iterable[_Union[ProvisionedPlan, _Mapping]]] = ..., drive_id_vec: _Optional[_Iterable[str]] = ..., drive_size_vec: _Optional[_Iterable[int]] = ..., department: _Optional[str] = ..., city: _Optional[str] = ..., country: _Optional[str] = ..., designation: _Optional[str] = ..., assigned_plans: _Optional[_Iterable[_Union[AssignedPlan, _Mapping]]] = ..., user_principal_name: _Optional[str] = ..., proxy_addresses_vec: _Optional[_Iterable[str]] = ..., on_premises_sync_enabled: bool = ..., show_in_address_list: bool = ..., user_type: _Optional[str] = ..., my_site: _Optional[str] = ..., account_enabled: bool = ..., odata_type: _Optional[str] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("id", "created_date_time", "description", "display_name", "mail", "visibility", "resource_provisioning_options", "mail_enabled", "mail_nickname", "security_enabled", "group_type_vec", "owner_ids_vec", "member_ids_vec", "members_vec", "owners_vec", "allow_external_senders", "auto_subscribe_new_members", "hide_from_outlook_clients", "hide_from_address_lists", "membership_rule", "membership_rule_processing_state", "theme", "member_count", "site_id", "site_name", "site_url", "proxy_addresses_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PROVISIONING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAIL_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNER_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNERS_VEC_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXTERNAL_SENDERS_FIELD_NUMBER: _ClassVar[int]
    AUTO_SUBSCRIBE_NEW_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    HIDE_FROM_OUTLOOK_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    HIDE_FROM_ADDRESS_LISTS_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_RULE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_RULE_PROCESSING_STATE_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_URL_FIELD_NUMBER: _ClassVar[int]
    PROXY_ADDRESSES_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_date_time: str
    description: str
    display_name: str
    mail: str
    visibility: str
    resource_provisioning_options: _containers.RepeatedScalarFieldContainer[str]
    mail_enabled: bool
    mail_nickname: str
    security_enabled: bool
    group_type_vec: _containers.RepeatedScalarFieldContainer[str]
    owner_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    member_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    members_vec: _containers.RepeatedCompositeFieldContainer[DirectoryObject]
    owners_vec: _containers.RepeatedCompositeFieldContainer[DirectoryObject]
    allow_external_senders: bool
    auto_subscribe_new_members: bool
    hide_from_outlook_clients: bool
    hide_from_address_lists: bool
    membership_rule: str
    membership_rule_processing_state: str
    theme: str
    member_count: int
    site_id: str
    site_name: str
    site_url: str
    proxy_addresses_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., created_date_time: _Optional[str] = ..., description: _Optional[str] = ..., display_name: _Optional[str] = ..., mail: _Optional[str] = ..., visibility: _Optional[str] = ..., resource_provisioning_options: _Optional[_Iterable[str]] = ..., mail_enabled: bool = ..., mail_nickname: _Optional[str] = ..., security_enabled: bool = ..., group_type_vec: _Optional[_Iterable[str]] = ..., owner_ids_vec: _Optional[_Iterable[str]] = ..., member_ids_vec: _Optional[_Iterable[str]] = ..., members_vec: _Optional[_Iterable[_Union[DirectoryObject, _Mapping]]] = ..., owners_vec: _Optional[_Iterable[_Union[DirectoryObject, _Mapping]]] = ..., allow_external_senders: bool = ..., auto_subscribe_new_members: bool = ..., hide_from_outlook_clients: bool = ..., hide_from_address_lists: bool = ..., membership_rule: _Optional[str] = ..., membership_rule_processing_state: _Optional[str] = ..., theme: _Optional[str] = ..., member_count: _Optional[int] = ..., site_id: _Optional[str] = ..., site_name: _Optional[str] = ..., site_url: _Optional[str] = ..., proxy_addresses_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class Site(_message.Message):
    __slots__ = ("id", "created_date_time", "last_modified_date_time", "display_name", "web_url", "parent_reference", "description", "root", "site_collection", "sub_site_vec", "is_excluded")
    class ParentReference(_message.Message):
        __slots__ = ("site_id",)
        SITE_ID_FIELD_NUMBER: _ClassVar[int]
        site_id: str
        def __init__(self, site_id: _Optional[str] = ...) -> None: ...
    class SiteCollection(_message.Message):
        __slots__ = ("host_name", "data_location_code", "root")
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_LOCATION_CODE_FIELD_NUMBER: _ClassVar[int]
        ROOT_FIELD_NUMBER: _ClassVar[int]
        host_name: str
        data_location_code: str
        root: Root
        def __init__(self, host_name: _Optional[str] = ..., data_location_code: _Optional[str] = ..., root: _Optional[_Union[Root, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    SITE_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SUB_SITE_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_date_time: str
    last_modified_date_time: str
    display_name: str
    web_url: str
    parent_reference: Site.ParentReference
    description: str
    root: Root
    site_collection: Site.SiteCollection
    sub_site_vec: _containers.RepeatedCompositeFieldContainer[Site]
    is_excluded: bool
    def __init__(self, id: _Optional[str] = ..., created_date_time: _Optional[str] = ..., last_modified_date_time: _Optional[str] = ..., display_name: _Optional[str] = ..., web_url: _Optional[str] = ..., parent_reference: _Optional[_Union[Site.ParentReference, _Mapping]] = ..., description: _Optional[str] = ..., root: _Optional[_Union[Root, _Mapping]] = ..., site_collection: _Optional[_Union[Site.SiteCollection, _Mapping]] = ..., sub_site_vec: _Optional[_Iterable[_Union[Site, _Mapping]]] = ..., is_excluded: bool = ...) -> None: ...

class List(_message.Message):
    __slots__ = ("id", "name", "created_by", "created_date_time", "last_modified_by", "last_modified_date_time", "parent_reference", "web_url", "display_name", "list_info")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LIST_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_by: _graph_external_pb2.IdentitySet
    created_date_time: str
    last_modified_by: _graph_external_pb2.IdentitySet
    last_modified_date_time: str
    parent_reference: ItemReference
    web_url: str
    display_name: str
    list_info: ListInfo
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., created_date_time: _Optional[str] = ..., last_modified_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., last_modified_date_time: _Optional[str] = ..., parent_reference: _Optional[_Union[ItemReference, _Mapping]] = ..., web_url: _Optional[str] = ..., display_name: _Optional[str] = ..., list_info: _Optional[_Union[ListInfo, _Mapping]] = ...) -> None: ...

class ListInfo(_message.Message):
    __slots__ = ("content_types_enabled", "hidden", "list_template")
    CONTENT_TYPES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    LIST_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    content_types_enabled: bool
    hidden: bool
    list_template: str
    def __init__(self, content_types_enabled: bool = ..., hidden: bool = ..., list_template: _Optional[str] = ...) -> None: ...

class ListItem(_message.Message):
    __slots__ = ("id", "name", "created_by", "created_date_time", "last_modified_by", "last_modified_date_time", "parent_reference", "web_url", "fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_by: _graph_external_pb2.IdentitySet
    created_date_time: str
    last_modified_by: _graph_external_pb2.IdentitySet
    last_modified_date_time: str
    parent_reference: ItemReference
    web_url: str
    fields: _struct_pb2.Struct
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., created_date_time: _Optional[str] = ..., last_modified_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., last_modified_date_time: _Optional[str] = ..., parent_reference: _Optional[_Union[ItemReference, _Mapping]] = ..., web_url: _Optional[str] = ..., fields: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Quota(_message.Message):
    __slots__ = ("total", "used", "remaining", "deleted", "state")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    total: int
    used: int
    remaining: int
    deleted: int
    state: str
    def __init__(self, total: _Optional[int] = ..., used: _Optional[int] = ..., remaining: _Optional[int] = ..., deleted: _Optional[int] = ..., state: _Optional[str] = ...) -> None: ...

class Drive(_message.Message):
    __slots__ = ("created_by", "created_date_time", "description", "driveType", "id", "last_modified_by", "last_modified_date_time", "name", "owner", "quota", "web_url", "cohesity_drive_type", "list")
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DRIVETYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    COHESITY_DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    created_by: _graph_external_pb2.IdentitySet
    created_date_time: str
    description: str
    driveType: str
    id: str
    last_modified_by: _graph_external_pb2.IdentitySet
    last_modified_date_time: str
    name: str
    owner: _graph_external_pb2.IdentitySet
    quota: Quota
    web_url: str
    cohesity_drive_type: _graph_enums_pb2.DriveType.Type
    list: List
    def __init__(self, created_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., created_date_time: _Optional[str] = ..., description: _Optional[str] = ..., driveType: _Optional[str] = ..., id: _Optional[str] = ..., last_modified_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., last_modified_date_time: _Optional[str] = ..., name: _Optional[str] = ..., owner: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., quota: _Optional[_Union[Quota, _Mapping]] = ..., web_url: _Optional[str] = ..., cohesity_drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ..., list: _Optional[_Union[List, _Mapping]] = ...) -> None: ...

class Hashes(_message.Message):
    __slots__ = ("crc32_hash", "quick_Xor_hash", "sha1_hash", "sha256_hash")
    CRC32_HASH_FIELD_NUMBER: _ClassVar[int]
    QUICK_XOR_HASH_FIELD_NUMBER: _ClassVar[int]
    SHA1_HASH_FIELD_NUMBER: _ClassVar[int]
    SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    crc32_hash: str
    quick_Xor_hash: str
    sha1_hash: str
    sha256_hash: str
    def __init__(self, crc32_hash: _Optional[str] = ..., quick_Xor_hash: _Optional[str] = ..., sha1_hash: _Optional[str] = ..., sha256_hash: _Optional[str] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ("mime_type", "hashes")
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    hashes: Hashes
    def __init__(self, mime_type: _Optional[str] = ..., hashes: _Optional[_Union[Hashes, _Mapping]] = ...) -> None: ...

class FileSystemInfo(_message.Message):
    __slots__ = ("created_date_time", "last_modified_date_time", "last_accessed_date_time")
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    created_date_time: str
    last_modified_date_time: str
    last_accessed_date_time: str
    def __init__(self, created_date_time: _Optional[str] = ..., last_modified_date_time: _Optional[str] = ..., last_accessed_date_time: _Optional[str] = ...) -> None: ...

class Folder(_message.Message):
    __slots__ = ("child_count",)
    CHILD_COUNT_FIELD_NUMBER: _ClassVar[int]
    child_count: int
    def __init__(self, child_count: _Optional[int] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("height", "width")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ...) -> None: ...

class PublicationFacet(_message.Message):
    __slots__ = ("level", "version_id", "checked_out_by")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKED_OUT_BY_FIELD_NUMBER: _ClassVar[int]
    level: str
    version_id: str
    checked_out_by: _graph_external_pb2.IdentitySet
    def __init__(self, level: _Optional[str] = ..., version_id: _Optional[str] = ..., checked_out_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ...) -> None: ...

class PendingContentUpdate(_message.Message):
    __slots__ = ("queued_date_time",)
    QUEUED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    queued_date_time: str
    def __init__(self, queued_date_time: _Optional[str] = ...) -> None: ...

class Package(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    def __init__(self, type: _Optional[str] = ...) -> None: ...

class Malware(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class System(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ItemReference(_message.Message):
    __slots__ = ("drive_id", "drive_type", "id", "name", "path", "site_id", "share_id")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    drive_id: str
    drive_type: str
    id: str
    name: str
    path: str
    site_id: str
    share_id: str
    def __init__(self, drive_id: _Optional[str] = ..., drive_type: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., site_id: _Optional[str] = ..., share_id: _Optional[str] = ...) -> None: ...

class Root(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Shared(_message.Message):
    __slots__ = ("owner", "scope", "shared_by", "shared_date_time")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SHARED_BY_FIELD_NUMBER: _ClassVar[int]
    SHARED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    owner: _graph_external_pb2.IdentitySet
    scope: str
    shared_by: _graph_external_pb2.IdentitySet
    shared_date_time: str
    def __init__(self, owner: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., scope: _Optional[str] = ..., shared_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., shared_date_time: _Optional[str] = ...) -> None: ...

class SpecialFolder(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DriveItemType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRootFolder: _ClassVar[DriveItemType.Type]
        kFolder: _ClassVar[DriveItemType.Type]
        kFile: _ClassVar[DriveItemType.Type]
        kPackage: _ClassVar[DriveItemType.Type]
    kRootFolder: DriveItemType.Type
    kFolder: DriveItemType.Type
    kFile: DriveItemType.Type
    kPackage: DriveItemType.Type
    def __init__(self) -> None: ...

class DriveItem(_message.Message):
    __slots__ = ("created_by", "created_date_time", "file", "file_system_info", "id", "folder", "last_modified_by", "last_modified_date_time", "name", "package", "parent_reference", "root", "shared", "size", "special_folder", "web_url", "deleted", "conflict_behavior", "is_excluded", "permissions", "e_tag", "c_tag", "job_instance_id", "children_vec", "malware", "is_skipped", "exclusion_info", "relative_web_url", "download_url", "explicit_permission_vec", "deny_permission_vec", "hierarchial_permissions_enabled", "is_errordb_item", "image", "publication", "pending_update", "cohesity_item_data_version", "cohesity_item_metadata_version")
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_FOLDER_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    IS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    E_TAG_FIELD_NUMBER: _ClassVar[int]
    C_TAG_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_VEC_FIELD_NUMBER: _ClassVar[int]
    MALWARE_FIELD_NUMBER: _ClassVar[int]
    IS_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_INFO_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    DENY_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    HIERARCHIAL_PERMISSIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_ERRORDB_ITEM_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    PENDING_UPDATE_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ITEM_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ITEM_METADATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    created_by: _graph_external_pb2.IdentitySet
    created_date_time: str
    file: File
    file_system_info: FileSystemInfo
    id: str
    folder: Folder
    last_modified_by: _graph_external_pb2.IdentitySet
    last_modified_date_time: str
    name: str
    package: Package
    parent_reference: ItemReference
    root: Root
    shared: Shared
    size: int
    special_folder: SpecialFolder
    web_url: str
    deleted: DeletedFacet
    conflict_behavior: str
    is_excluded: bool
    permissions: _containers.RepeatedCompositeFieldContainer[Permissions]
    e_tag: str
    c_tag: str
    job_instance_id: str
    children_vec: _containers.RepeatedCompositeFieldContainer[ItemReference]
    malware: Malware
    is_skipped: bool
    exclusion_info: ExclusionInfo
    relative_web_url: str
    download_url: str
    explicit_permission_vec: _containers.RepeatedCompositeFieldContainer[Permissions]
    deny_permission_vec: _containers.RepeatedCompositeFieldContainer[Permissions]
    hierarchial_permissions_enabled: bool
    is_errordb_item: bool
    image: Image
    publication: PublicationFacet
    pending_update: PendingContentUpdate
    cohesity_item_data_version: int
    cohesity_item_metadata_version: int
    def __init__(self, created_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., created_date_time: _Optional[str] = ..., file: _Optional[_Union[File, _Mapping]] = ..., file_system_info: _Optional[_Union[FileSystemInfo, _Mapping]] = ..., id: _Optional[str] = ..., folder: _Optional[_Union[Folder, _Mapping]] = ..., last_modified_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., last_modified_date_time: _Optional[str] = ..., name: _Optional[str] = ..., package: _Optional[_Union[Package, _Mapping]] = ..., parent_reference: _Optional[_Union[ItemReference, _Mapping]] = ..., root: _Optional[_Union[Root, _Mapping]] = ..., shared: _Optional[_Union[Shared, _Mapping]] = ..., size: _Optional[int] = ..., special_folder: _Optional[_Union[SpecialFolder, _Mapping]] = ..., web_url: _Optional[str] = ..., deleted: _Optional[_Union[DeletedFacet, _Mapping]] = ..., conflict_behavior: _Optional[str] = ..., is_excluded: bool = ..., permissions: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ..., e_tag: _Optional[str] = ..., c_tag: _Optional[str] = ..., job_instance_id: _Optional[str] = ..., children_vec: _Optional[_Iterable[_Union[ItemReference, _Mapping]]] = ..., malware: _Optional[_Union[Malware, _Mapping]] = ..., is_skipped: bool = ..., exclusion_info: _Optional[_Union[ExclusionInfo, _Mapping]] = ..., relative_web_url: _Optional[str] = ..., download_url: _Optional[str] = ..., explicit_permission_vec: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ..., deny_permission_vec: _Optional[_Iterable[_Union[Permissions, _Mapping]]] = ..., hierarchial_permissions_enabled: bool = ..., is_errordb_item: bool = ..., image: _Optional[_Union[Image, _Mapping]] = ..., publication: _Optional[_Union[PublicationFacet, _Mapping]] = ..., pending_update: _Optional[_Union[PendingContentUpdate, _Mapping]] = ..., cohesity_item_data_version: _Optional[int] = ..., cohesity_item_metadata_version: _Optional[int] = ...) -> None: ...

class ExclusionInfo(_message.Message):
    __slots__ = ("exclusion_type", "details")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUserExcluded: _ClassVar[ExclusionInfo.Type]
        kOneNoteRelated: _ClassVar[ExclusionInfo.Type]
        kSkipByInheritance: _ClassVar[ExclusionInfo.Type]
        kBlackListed: _ClassVar[ExclusionInfo.Type]
        kMalware: _ClassVar[ExclusionInfo.Type]
        kDownloadSkipped: _ClassVar[ExclusionInfo.Type]
        kSkipBySameCTag: _ClassVar[ExclusionInfo.Type]
    kUserExcluded: ExclusionInfo.Type
    kOneNoteRelated: ExclusionInfo.Type
    kSkipByInheritance: ExclusionInfo.Type
    kBlackListed: ExclusionInfo.Type
    kMalware: ExclusionInfo.Type
    kDownloadSkipped: ExclusionInfo.Type
    kSkipBySameCTag: ExclusionInfo.Type
    EXCLUSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    exclusion_type: ExclusionInfo.Type
    details: str
    def __init__(self, exclusion_type: _Optional[_Union[ExclusionInfo.Type, str]] = ..., details: _Optional[str] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ("id", "granted_to", "inherited_from", "roles", "link", "invitation", "share_id", "has_password", "granted_to_identities_V2", "granted_to_V2")
    ID_FIELD_NUMBER: _ClassVar[int]
    GRANTED_TO_FIELD_NUMBER: _ClassVar[int]
    INHERITED_FROM_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    INVITATION_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    GRANTED_TO_IDENTITIES_V2_FIELD_NUMBER: _ClassVar[int]
    GRANTED_TO_V2_FIELD_NUMBER: _ClassVar[int]
    id: str
    granted_to: _graph_external_pb2.IdentitySet
    inherited_from: ItemReference
    roles: _containers.RepeatedScalarFieldContainer[str]
    link: SharingLink
    invitation: SharingInvitation
    share_id: str
    has_password: bool
    granted_to_identities_V2: _containers.RepeatedCompositeFieldContainer[_graph_external_pb2.SharepointIdentitySet]
    granted_to_V2: _graph_external_pb2.SharepointIdentitySet
    def __init__(self, id: _Optional[str] = ..., granted_to: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., inherited_from: _Optional[_Union[ItemReference, _Mapping]] = ..., roles: _Optional[_Iterable[str]] = ..., link: _Optional[_Union[SharingLink, _Mapping]] = ..., invitation: _Optional[_Union[SharingInvitation, _Mapping]] = ..., share_id: _Optional[str] = ..., has_password: bool = ..., granted_to_identities_V2: _Optional[_Iterable[_Union[_graph_external_pb2.SharepointIdentitySet, _Mapping]]] = ..., granted_to_V2: _Optional[_Union[_graph_external_pb2.SharepointIdentitySet, _Mapping]] = ...) -> None: ...

class DeletedFacet(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class MismatchedDriveItemSize(_message.Message):
    __slots__ = ("drive_item_id", "actual_size")
    DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    drive_item_id: str
    actual_size: int
    def __init__(self, drive_item_id: _Optional[str] = ..., actual_size: _Optional[int] = ...) -> None: ...

class SnapshotInfo(_message.Message):
    __slots__ = ("status", "job_instance_id", "attempt_num", "sub_tasks_vec", "error", "drive_item_change_vec", "one_drive_config", "drive_item_to_backup_vec", "drive_id", "curr_sub_task_to_fill", "next_link", "total_drive_data_size", "lookup_error_found", "request_throttled", "num_skipped_items_malware", "num_skipped_items_same_ctag", "malware_file_offset", "o365_error_proto", "backup_stat_details", "is_system_drive", "highest_sub_task_to_quisce", "process_metadata_inside_magneto", "use_magneto_data_puller", "file_data_distribution_table", "throttling_time_distribution_table", "prev_status", "prev_state_start_time", "incremental_file_offset", "fetch_only_permissions", "last_started_sub_task_idx", "one_drive_info_scribe_table_row_str", "num_skipped_permission_items", "total_skipped_items_during_download", "mismatched_drive_item_size_vec")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SnapshotInfo.Status]
        kPermitGranted: _ClassVar[SnapshotInfo.Status]
        kPrepareOneDriveFinished: _ClassVar[SnapshotInfo.Status]
        kDriveDeltaFetched: _ClassVar[SnapshotInfo.Status]
        kSetupInfoFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SnapshotInfo.Status]
    kStarted: SnapshotInfo.Status
    kPermitGranted: SnapshotInfo.Status
    kPrepareOneDriveFinished: SnapshotInfo.Status
    kDriveDeltaFetched: SnapshotInfo.Status
    kSetupInfoFinished: SnapshotInfo.Status
    kSubTasksFinished: SnapshotInfo.Status
    kEndBackupFinished: SnapshotInfo.Status
    kSubTasksCreated: SnapshotInfo.Status
    class BackupStatsDetail(_message.Message):
        __slots__ = ("op_stat_details_vec", "errored_item_info_vec")
        class OpName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDownloadFilesOp: _ClassVar[SnapshotInfo.BackupStatsDetail.OpName]
        kDownloadFilesOp: SnapshotInfo.BackupStatsDetail.OpName
        class OpStatDetails(_message.Message):
            __slots__ = ("op_name", "count", "average_throughput", "rolling_throughput")
            OP_NAME_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            AVERAGE_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
            ROLLING_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
            op_name: SnapshotInfo.BackupStatsDetail.OpName
            count: int
            average_throughput: float
            rolling_throughput: float
            def __init__(self, op_name: _Optional[_Union[SnapshotInfo.BackupStatsDetail.OpName, str]] = ..., count: _Optional[int] = ..., average_throughput: _Optional[float] = ..., rolling_throughput: _Optional[float] = ...) -> None: ...
        class ErroredItemInfo(_message.Message):
            __slots__ = ("drive_item", "error_reason")
            DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
            ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
            drive_item: DriveItem
            error_reason: str
            def __init__(self, drive_item: _Optional[_Union[DriveItem, _Mapping]] = ..., error_reason: _Optional[str] = ...) -> None: ...
        OP_STAT_DETAILS_VEC_FIELD_NUMBER: _ClassVar[int]
        ERRORED_ITEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        op_stat_details_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.BackupStatsDetail.OpStatDetails]
        errored_item_info_vec: _containers.RepeatedCompositeFieldContainer[SnapshotInfo.BackupStatsDetail.ErroredItemInfo]
        def __init__(self, op_stat_details_vec: _Optional[_Iterable[_Union[SnapshotInfo.BackupStatsDetail.OpStatDetails, _Mapping]]] = ..., errored_item_info_vec: _Optional[_Iterable[_Union[SnapshotInfo.BackupStatsDetail.ErroredItemInfo, _Mapping]]] = ...) -> None: ...
    ONE_DRIVE_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_CHANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_TO_BACKUP_VEC_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    CURR_SUB_TASK_TO_FILL_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DRIVE_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_ERROR_FOUND_FIELD_NUMBER: _ClassVar[int]
    REQUEST_THROTTLED_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_ITEMS_MALWARE_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_ITEMS_SAME_CTAG_FIELD_NUMBER: _ClassVar[int]
    MALWARE_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    O365_ERROR_PROTO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_STAT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DRIVE_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_SUB_TASK_TO_QUISCE_FIELD_NUMBER: _ClassVar[int]
    PROCESS_METADATA_INSIDE_MAGNETO_FIELD_NUMBER: _ClassVar[int]
    USE_MAGNETO_DATA_PULLER_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_DISTRIBUTION_TABLE_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TIME_DISTRIBUTION_TABLE_FIELD_NUMBER: _ClassVar[int]
    PREV_STATUS_FIELD_NUMBER: _ClassVar[int]
    PREV_STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FETCH_ONLY_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    LAST_STARTED_SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
    ONE_DRIVE_INFO_SCRIBE_TABLE_ROW_STR_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_PERMISSION_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SKIPPED_ITEMS_DURING_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    MISMATCHED_DRIVE_ITEM_SIZE_VEC_FIELD_NUMBER: _ClassVar[int]
    status: SnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    drive_item_change_vec: _containers.RepeatedCompositeFieldContainer[DriveItem]
    one_drive_config: OneDriveConfigFile
    drive_item_to_backup_vec: _containers.RepeatedCompositeFieldContainer[DriveItem]
    drive_id: str
    curr_sub_task_to_fill: int
    next_link: str
    total_drive_data_size: int
    lookup_error_found: bool
    request_throttled: bool
    num_skipped_items_malware: int
    num_skipped_items_same_ctag: int
    malware_file_offset: int
    o365_error_proto: _o365_error_pb2.O365ErrorProto
    backup_stat_details: SnapshotInfo.BackupStatsDetail
    is_system_drive: bool
    highest_sub_task_to_quisce: int
    process_metadata_inside_magneto: bool
    use_magneto_data_puller: bool
    file_data_distribution_table: DataDistributionTable
    throttling_time_distribution_table: ThrottlingErrorTimeDistributionTable
    prev_status: SnapshotInfo.Status
    prev_state_start_time: int
    incremental_file_offset: int
    fetch_only_permissions: bool
    last_started_sub_task_idx: int
    one_drive_info_scribe_table_row_str: str
    num_skipped_permission_items: int
    total_skipped_items_during_download: int
    mismatched_drive_item_size_vec: _containers.RepeatedCompositeFieldContainer[MismatchedDriveItemSize]
    def __init__(self, status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., drive_item_change_vec: _Optional[_Iterable[_Union[DriveItem, _Mapping]]] = ..., one_drive_config: _Optional[_Union[OneDriveConfigFile, _Mapping]] = ..., drive_item_to_backup_vec: _Optional[_Iterable[_Union[DriveItem, _Mapping]]] = ..., drive_id: _Optional[str] = ..., curr_sub_task_to_fill: _Optional[int] = ..., next_link: _Optional[str] = ..., total_drive_data_size: _Optional[int] = ..., lookup_error_found: bool = ..., request_throttled: bool = ..., num_skipped_items_malware: _Optional[int] = ..., num_skipped_items_same_ctag: _Optional[int] = ..., malware_file_offset: _Optional[int] = ..., o365_error_proto: _Optional[_Union[_o365_error_pb2.O365ErrorProto, _Mapping]] = ..., backup_stat_details: _Optional[_Union[SnapshotInfo.BackupStatsDetail, _Mapping]] = ..., is_system_drive: bool = ..., highest_sub_task_to_quisce: _Optional[int] = ..., process_metadata_inside_magneto: bool = ..., use_magneto_data_puller: bool = ..., file_data_distribution_table: _Optional[_Union[DataDistributionTable, _Mapping]] = ..., throttling_time_distribution_table: _Optional[_Union[ThrottlingErrorTimeDistributionTable, _Mapping]] = ..., prev_status: _Optional[_Union[SnapshotInfo.Status, str]] = ..., prev_state_start_time: _Optional[int] = ..., incremental_file_offset: _Optional[int] = ..., fetch_only_permissions: bool = ..., last_started_sub_task_idx: _Optional[int] = ..., one_drive_info_scribe_table_row_str: _Optional[str] = ..., num_skipped_permission_items: _Optional[int] = ..., total_skipped_items_during_download: _Optional[int] = ..., mismatched_drive_item_size_vec: _Optional[_Iterable[_Union[MismatchedDriveItemSize, _Mapping]]] = ...) -> None: ...

class SharepointListSnapshotInfo(_message.Message):
    __slots__ = ("status", "job_instance_id", "attempt_num", "sub_tasks_vec", "error", "curr_sub_task_to_fill", "next_link", "lists_info_vec", "current_list_idx", "lists_to_be_cleaned_vec", "skip_acquire_lists_permit")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[SharepointListSnapshotInfo.Status]
        kPermitGranted: _ClassVar[SharepointListSnapshotInfo.Status]
        kPrepareListsFinished: _ClassVar[SharepointListSnapshotInfo.Status]
        kListsFetched: _ClassVar[SharepointListSnapshotInfo.Status]
        kListsMetadataFetched: _ClassVar[SharepointListSnapshotInfo.Status]
        kSetupInfoFinished: _ClassVar[SharepointListSnapshotInfo.Status]
        kSubTasksFinished: _ClassVar[SharepointListSnapshotInfo.Status]
        kEndBackupFinished: _ClassVar[SharepointListSnapshotInfo.Status]
        kSubTasksCreated: _ClassVar[SharepointListSnapshotInfo.Status]
        kListItemsFetched: _ClassVar[SharepointListSnapshotInfo.Status]
        kHandledDeletedLists: _ClassVar[SharepointListSnapshotInfo.Status]
    kStarted: SharepointListSnapshotInfo.Status
    kPermitGranted: SharepointListSnapshotInfo.Status
    kPrepareListsFinished: SharepointListSnapshotInfo.Status
    kListsFetched: SharepointListSnapshotInfo.Status
    kListsMetadataFetched: SharepointListSnapshotInfo.Status
    kSetupInfoFinished: SharepointListSnapshotInfo.Status
    kSubTasksFinished: SharepointListSnapshotInfo.Status
    kEndBackupFinished: SharepointListSnapshotInfo.Status
    kSubTasksCreated: SharepointListSnapshotInfo.Status
    kListItemsFetched: SharepointListSnapshotInfo.Status
    kHandledDeletedLists: SharepointListSnapshotInfo.Status
    class ListInfo(_message.Message):
        __slots__ = ("id", "server_relative_url", "current_change_token_value", "is_full_backup", "next_link", "list_permissions", "hidden", "disable_commenting", "has_unique_role_assignments")
        ID_FIELD_NUMBER: _ClassVar[int]
        SERVER_RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
        CURRENT_CHANGE_TOKEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        IS_FULL_BACKUP_FIELD_NUMBER: _ClassVar[int]
        NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
        LIST_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        DISABLE_COMMENTING_FIELD_NUMBER: _ClassVar[int]
        HAS_UNIQUE_ROLE_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
        id: str
        server_relative_url: str
        current_change_token_value: str
        is_full_backup: bool
        next_link: str
        list_permissions: _sharepoint_pb2.SPListItemUniquePermissions
        hidden: bool
        disable_commenting: bool
        has_unique_role_assignments: bool
        def __init__(self, id: _Optional[str] = ..., server_relative_url: _Optional[str] = ..., current_change_token_value: _Optional[str] = ..., is_full_backup: bool = ..., next_link: _Optional[str] = ..., list_permissions: _Optional[_Union[_sharepoint_pb2.SPListItemUniquePermissions, _Mapping]] = ..., hidden: bool = ..., disable_commenting: bool = ..., has_unique_role_assignments: bool = ...) -> None: ...
    SHAREPOINT_LIST_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    sharepoint_list_snapshot_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CURR_SUB_TASK_TO_FILL_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINK_FIELD_NUMBER: _ClassVar[int]
    LISTS_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LIST_IDX_FIELD_NUMBER: _ClassVar[int]
    LISTS_TO_BE_CLEANED_VEC_FIELD_NUMBER: _ClassVar[int]
    SKIP_ACQUIRE_LISTS_PERMIT_FIELD_NUMBER: _ClassVar[int]
    status: SharepointListSnapshotInfo.Status
    job_instance_id: int
    attempt_num: int
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    curr_sub_task_to_fill: int
    next_link: str
    lists_info_vec: _containers.RepeatedCompositeFieldContainer[SharepointListSnapshotInfo.ListInfo]
    current_list_idx: int
    lists_to_be_cleaned_vec: _containers.RepeatedScalarFieldContainer[str]
    skip_acquire_lists_permit: bool
    def __init__(self, status: _Optional[_Union[SharepointListSnapshotInfo.Status, str]] = ..., job_instance_id: _Optional[int] = ..., attempt_num: _Optional[int] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., curr_sub_task_to_fill: _Optional[int] = ..., next_link: _Optional[str] = ..., lists_info_vec: _Optional[_Iterable[_Union[SharepointListSnapshotInfo.ListInfo, _Mapping]]] = ..., current_list_idx: _Optional[int] = ..., lists_to_be_cleaned_vec: _Optional[_Iterable[str]] = ..., skip_acquire_lists_permit: bool = ...) -> None: ...

class SharepointListData(_message.Message):
    __slots__ = ("script", "fields")
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    script: str
    fields: _struct_pb2.ListValue
    def __init__(self, script: _Optional[str] = ..., fields: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...) -> None: ...

class SnapshotScribeInfo(_message.Message):
    __slots__ = ("deleted_item_id_vec", "next_del_idx")
    ONE_DRIVE_SNAPSHOT_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_snapshot_scribe_info: _descriptor.FieldDescriptor
    DELETED_ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_DEL_IDX_FIELD_NUMBER: _ClassVar[int]
    deleted_item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    next_del_idx: int
    def __init__(self, deleted_item_id_vec: _Optional[_Iterable[str]] = ..., next_del_idx: _Optional[int] = ...) -> None: ...

class OneDriveReconcileInfo(_message.Message):
    __slots__ = ("recon_end_time_usecs", "error", "from_version", "to_version")
    RECON_END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FROM_VERSION_FIELD_NUMBER: _ClassVar[int]
    TO_VERSION_FIELD_NUMBER: _ClassVar[int]
    recon_end_time_usecs: int
    error: _error_pb2.ErrorProto
    from_version: int
    to_version: int
    def __init__(self, recon_end_time_usecs: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., from_version: _Optional[int] = ..., to_version: _Optional[int] = ...) -> None: ...

class OneDriveConfigFile(_message.Message):
    __slots__ = ("graph_delta_link", "backup_task_stats", "deny_filters", "excluded_drive_item_id_vec", "file_absent", "skip_storing_inherited_permissions", "fetched_all_permissions_in_inc_run", "is_with_hierarchical_permissions", "current_drive_data_version", "current_drive_metadata_version", "recon_data_runs_info", "recon_metadata_runs_info")
    GRAPH_DELTA_LINK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TASK_STATS_FIELD_NUMBER: _ClassVar[int]
    DENY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DRIVE_ITEM_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FILE_ABSENT_FIELD_NUMBER: _ClassVar[int]
    SKIP_STORING_INHERITED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    FETCHED_ALL_PERMISSIONS_IN_INC_RUN_FIELD_NUMBER: _ClassVar[int]
    IS_WITH_HIERARCHICAL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DRIVE_DATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DRIVE_METADATA_VERSION_FIELD_NUMBER: _ClassVar[int]
    RECON_DATA_RUNS_INFO_FIELD_NUMBER: _ClassVar[int]
    RECON_METADATA_RUNS_INFO_FIELD_NUMBER: _ClassVar[int]
    graph_delta_link: str
    backup_task_stats: BackupTaskStats
    deny_filters: _containers.RepeatedScalarFieldContainer[str]
    excluded_drive_item_id_vec: _containers.RepeatedScalarFieldContainer[str]
    file_absent: bool
    skip_storing_inherited_permissions: bool
    fetched_all_permissions_in_inc_run: bool
    is_with_hierarchical_permissions: bool
    current_drive_data_version: int
    current_drive_metadata_version: int
    recon_data_runs_info: _containers.RepeatedCompositeFieldContainer[OneDriveReconcileInfo]
    recon_metadata_runs_info: _containers.RepeatedCompositeFieldContainer[OneDriveReconcileInfo]
    def __init__(self, graph_delta_link: _Optional[str] = ..., backup_task_stats: _Optional[_Union[BackupTaskStats, _Mapping]] = ..., deny_filters: _Optional[_Iterable[str]] = ..., excluded_drive_item_id_vec: _Optional[_Iterable[str]] = ..., file_absent: bool = ..., skip_storing_inherited_permissions: bool = ..., fetched_all_permissions_in_inc_run: bool = ..., is_with_hierarchical_permissions: bool = ..., current_drive_data_version: _Optional[int] = ..., current_drive_metadata_version: _Optional[int] = ..., recon_data_runs_info: _Optional[_Iterable[_Union[OneDriveReconcileInfo, _Mapping]]] = ..., recon_metadata_runs_info: _Optional[_Iterable[_Union[OneDriveReconcileInfo, _Mapping]]] = ...) -> None: ...

class OneDriveSubTaskInfo(_message.Message):
    __slots__ = ("drive_item_info_vec", "restore_start_index", "restore_end_index", "total_file_size", "user_idx", "drive_id", "expected_api_call_count", "count_items", "use_mutable_progress_scribe_info", "errors_encountered", "application_id", "skipped_items_count", "errored_file_vec")
    ONE_DRIVE_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_sub_task_info: _descriptor.FieldDescriptor
    DRIVE_ITEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_START_INDEX_FIELD_NUMBER: _ClassVar[int]
    RESTORE_END_INDEX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    USER_IDX_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_API_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    COUNT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    USE_MUTABLE_PROGRESS_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERRORS_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERRORED_FILE_VEC_FIELD_NUMBER: _ClassVar[int]
    drive_item_info_vec: _containers.RepeatedCompositeFieldContainer[DriveItemInfoToSubTask]
    restore_start_index: int
    restore_end_index: int
    total_file_size: int
    user_idx: int
    drive_id: str
    expected_api_call_count: int
    count_items: int
    use_mutable_progress_scribe_info: bool
    errors_encountered: int
    application_id: str
    skipped_items_count: int
    errored_file_vec: _containers.RepeatedCompositeFieldContainer[O365ErroredFileInfo]
    def __init__(self, drive_item_info_vec: _Optional[_Iterable[_Union[DriveItemInfoToSubTask, _Mapping]]] = ..., restore_start_index: _Optional[int] = ..., restore_end_index: _Optional[int] = ..., total_file_size: _Optional[int] = ..., user_idx: _Optional[int] = ..., drive_id: _Optional[str] = ..., expected_api_call_count: _Optional[int] = ..., count_items: _Optional[int] = ..., use_mutable_progress_scribe_info: bool = ..., errors_encountered: _Optional[int] = ..., application_id: _Optional[str] = ..., skipped_items_count: _Optional[int] = ..., errored_file_vec: _Optional[_Iterable[_Union[O365ErroredFileInfo, _Mapping]]] = ...) -> None: ...

class SharepointListSubTaskInfo(_message.Message):
    __slots__ = ("site_id", "site_list_vec", "application_id")
    SHAREPOINT_LIST_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    sharepoint_list_sub_task_info: _descriptor.FieldDescriptor
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    site_list_vec: _containers.RepeatedCompositeFieldContainer[List]
    application_id: str
    def __init__(self, site_id: _Optional[str] = ..., site_list_vec: _Optional[_Iterable[_Union[List, _Mapping]]] = ..., application_id: _Optional[str] = ...) -> None: ...

class DriveItemInfoToSubTask(_message.Message):
    __slots__ = ("drive_item", "offset", "chunk_length", "is_small_drive_item")
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CHUNK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    IS_SMALL_DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    drive_item: DriveItem
    offset: int
    chunk_length: int
    is_small_drive_item: bool
    def __init__(self, drive_item: _Optional[_Union[DriveItem, _Mapping]] = ..., offset: _Optional[int] = ..., chunk_length: _Optional[int] = ..., is_small_drive_item: bool = ...) -> None: ...

class ProvisionedPlan(_message.Message):
    __slots__ = ("capability_status", "provisioning_status", "service_name")
    CAPABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    capability_status: str
    provisioning_status: str
    service_name: str
    def __init__(self, capability_status: _Optional[str] = ..., provisioning_status: _Optional[str] = ..., service_name: _Optional[str] = ...) -> None: ...

class AssignedPlan(_message.Message):
    __slots__ = ("id", "capability_status", "service_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    capability_status: str
    service_name: str
    def __init__(self, id: _Optional[str] = ..., capability_status: _Optional[str] = ..., service_name: _Optional[str] = ...) -> None: ...

class ServicePlanInfo(_message.Message):
    __slots__ = ("id", "name", "status", "applies_to")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPLIES_TO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: str
    applies_to: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[str] = ..., applies_to: _Optional[str] = ...) -> None: ...

class SubscribedSku(_message.Message):
    __slots__ = ("id", "sku_id", "sku_part_number", "applies_to", "status", "plan_info_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    SKU_ID_FIELD_NUMBER: _ClassVar[int]
    SKU_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    APPLIES_TO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    sku_id: str
    sku_part_number: str
    applies_to: str
    status: str
    plan_info_vec: _containers.RepeatedCompositeFieldContainer[ServicePlanInfo]
    def __init__(self, id: _Optional[str] = ..., sku_id: _Optional[str] = ..., sku_part_number: _Optional[str] = ..., applies_to: _Optional[str] = ..., status: _Optional[str] = ..., plan_info_vec: _Optional[_Iterable[_Union[ServicePlanInfo, _Mapping]]] = ...) -> None: ...

class OneDriveSubTaskScribeInfo(_message.Message):
    __slots__ = ("change_list_info_vec", "size_backed_up_items", "size_restored_items", "big_file_chunk_length")
    class DriveItemChangeListInfo(_message.Message):
        __slots__ = ("drive_item_info_vec", "size", "is_backed_up", "start_index_vec", "is_partial_file", "upload_web_url")
        DRIVE_ITEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        IS_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
        START_INDEX_VEC_FIELD_NUMBER: _ClassVar[int]
        IS_PARTIAL_FILE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_WEB_URL_FIELD_NUMBER: _ClassVar[int]
        drive_item_info_vec: _containers.RepeatedCompositeFieldContainer[DriveItemInfoToSubTask]
        size: int
        is_backed_up: bool
        start_index_vec: _containers.RepeatedScalarFieldContainer[int]
        is_partial_file: bool
        upload_web_url: str
        def __init__(self, drive_item_info_vec: _Optional[_Iterable[_Union[DriveItemInfoToSubTask, _Mapping]]] = ..., size: _Optional[int] = ..., is_backed_up: bool = ..., start_index_vec: _Optional[_Iterable[int]] = ..., is_partial_file: bool = ..., upload_web_url: _Optional[str] = ...) -> None: ...
    ONE_DRIVE_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_sub_task_scribe_info: _descriptor.FieldDescriptor
    CHANGE_LIST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SIZE_BACKED_UP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SIZE_RESTORED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    BIG_FILE_CHUNK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    change_list_info_vec: _containers.RepeatedCompositeFieldContainer[OneDriveSubTaskScribeInfo.DriveItemChangeListInfo]
    size_backed_up_items: int
    size_restored_items: int
    big_file_chunk_length: int
    def __init__(self, change_list_info_vec: _Optional[_Iterable[_Union[OneDriveSubTaskScribeInfo.DriveItemChangeListInfo, _Mapping]]] = ..., size_backed_up_items: _Optional[int] = ..., size_restored_items: _Optional[int] = ..., big_file_chunk_length: _Optional[int] = ...) -> None: ...

class OneDriveSubTaskProgressScribeInfo(_message.Message):
    __slots__ = ("hole_idx_map", "pending_holes_vec", "inflight_work_units_range_vec", "finish_line_idx")
    class HoleIdxMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class Hole(_message.Message):
        __slots__ = ("offset", "length")
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        offset: int
        length: int
        def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    class DisjointRange(_message.Message):
        __slots__ = ("start", "length")
        START_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        start: int
        length: int
        def __init__(self, start: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    ONE_DRIVE_SUB_TASK_MUTABLE_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_sub_task_mutable_scribe_info: _descriptor.FieldDescriptor
    HOLE_IDX_MAP_FIELD_NUMBER: _ClassVar[int]
    PENDING_HOLES_VEC_FIELD_NUMBER: _ClassVar[int]
    INFLIGHT_WORK_UNITS_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
    FINISH_LINE_IDX_FIELD_NUMBER: _ClassVar[int]
    hole_idx_map: _containers.ScalarMap[int, bool]
    pending_holes_vec: _containers.RepeatedCompositeFieldContainer[OneDriveSubTaskProgressScribeInfo.Hole]
    inflight_work_units_range_vec: _containers.RepeatedCompositeFieldContainer[OneDriveSubTaskProgressScribeInfo.DisjointRange]
    finish_line_idx: int
    def __init__(self, hole_idx_map: _Optional[_Mapping[int, bool]] = ..., pending_holes_vec: _Optional[_Iterable[_Union[OneDriveSubTaskProgressScribeInfo.Hole, _Mapping]]] = ..., inflight_work_units_range_vec: _Optional[_Iterable[_Union[OneDriveSubTaskProgressScribeInfo.DisjointRange, _Mapping]]] = ..., finish_line_idx: _Optional[int] = ...) -> None: ...

class OneDriveSubTaskChangeQueueEntry(_message.Message):
    __slots__ = ("orig_index", "offset", "create_info", "expanded_index", "check_file_integrity")
    class CreateInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotNeeded: _ClassVar[OneDriveSubTaskChangeQueueEntry.CreateInfo]
        kCreateToDispatch: _ClassVar[OneDriveSubTaskChangeQueueEntry.CreateInfo]
        kCreateDispatched: _ClassVar[OneDriveSubTaskChangeQueueEntry.CreateInfo]
    kNotNeeded: OneDriveSubTaskChangeQueueEntry.CreateInfo
    kCreateToDispatch: OneDriveSubTaskChangeQueueEntry.CreateInfo
    kCreateDispatched: OneDriveSubTaskChangeQueueEntry.CreateInfo
    ORIG_INDEX_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CREATE_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_INDEX_FIELD_NUMBER: _ClassVar[int]
    CHECK_FILE_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    orig_index: int
    offset: int
    create_info: OneDriveSubTaskChangeQueueEntry.CreateInfo
    expanded_index: int
    check_file_integrity: bool
    def __init__(self, orig_index: _Optional[int] = ..., offset: _Optional[int] = ..., create_info: _Optional[_Union[OneDriveSubTaskChangeQueueEntry.CreateInfo, str]] = ..., expanded_index: _Optional[int] = ..., check_file_integrity: bool = ...) -> None: ...

class UploadSession(_message.Message):
    __slots__ = ("upload_url", "expiration_date_time", "next_expected_ranges")
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_EXPECTED_RANGES_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    expiration_date_time: str
    next_expected_ranges: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, upload_url: _Optional[str] = ..., expiration_date_time: _Optional[str] = ..., next_expected_ranges: _Optional[_Iterable[str]] = ...) -> None: ...

class FileContent(_message.Message):
    __slots__ = ("file_content",)
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    file_content: bytes
    def __init__(self, file_content: _Optional[bytes] = ...) -> None: ...

class ErrorContext(_message.Message):
    __slots__ = ("error", "aadsts_error")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AADSTS_ERROR_FIELD_NUMBER: _ClassVar[int]
    error: GraphError
    aadsts_error: AzureADSecurityTokenServiceError
    def __init__(self, error: _Optional[_Union[GraphError, _Mapping]] = ..., aadsts_error: _Optional[_Union[AzureADSecurityTokenServiceError, _Mapping]] = ...) -> None: ...

class GraphError(_message.Message):
    __slots__ = ("code", "error_message", "inner_error", "inner_error_extended")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INNER_ERROR_FIELD_NUMBER: _ClassVar[int]
    INNER_ERROR_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    code: str
    error_message: str
    inner_error: GraphError
    inner_error_extended: GraphError
    def __init__(self, code: _Optional[str] = ..., error_message: _Optional[str] = ..., inner_error: _Optional[_Union[GraphError, _Mapping]] = ..., inner_error_extended: _Optional[_Union[GraphError, _Mapping]] = ...) -> None: ...

class AzureADSecurityTokenServiceError(_message.Message):
    __slots__ = ("error", "error_description", "error_codes", "timestamp", "trace_id", "correlation_id", "error_uri")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_URI_FIELD_NUMBER: _ClassVar[int]
    error: str
    error_description: str
    error_codes: _containers.RepeatedScalarFieldContainer[int]
    timestamp: str
    trace_id: str
    correlation_id: str
    error_uri: str
    def __init__(self, error: _Optional[str] = ..., error_description: _Optional[str] = ..., error_codes: _Optional[_Iterable[int]] = ..., timestamp: _Optional[str] = ..., trace_id: _Optional[str] = ..., correlation_id: _Optional[str] = ..., error_uri: _Optional[str] = ...) -> None: ...

class RestoreDriveItem(_message.Message):
    __slots__ = ("restore_drive_item", "user_idx", "drive_id", "error")
    RESTORE_DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    USER_IDX_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    restore_drive_item: DriveItem
    user_idx: int
    drive_id: str
    error: _error_pb2.ErrorProto
    def __init__(self, restore_drive_item: _Optional[_Union[DriveItem, _Mapping]] = ..., user_idx: _Optional[int] = ..., drive_id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RestoreInfo(_message.Message):
    __slots__ = ("status", "view_root_path_vec", "sub_tasks_vec", "error", "restore_drive_item_vec", "user_idx_to_be_discovered", "drive_idx_to_be_discovered", "item_idx_to_be_discovered", "last_visited_drive_item_id", "has_more_items", "total_api_call_count", "entity_root_drive_map", "target_drive_id", "total_errors_encountered")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kStarted: _ClassVar[RestoreInfo.Status]
        kViewCloned: _ClassVar[RestoreInfo.Status]
        kReadDirInfoFetched: _ClassVar[RestoreInfo.Status]
        kSubTasksCreated: _ClassVar[RestoreInfo.Status]
        kSubTasksFinished: _ClassVar[RestoreInfo.Status]
        kViewDeleted: _ClassVar[RestoreInfo.Status]
        kPulseCreated: _ClassVar[RestoreInfo.Status]
        kOwnersRootDriveFetched: _ClassVar[RestoreInfo.Status]
    kStarted: RestoreInfo.Status
    kViewCloned: RestoreInfo.Status
    kReadDirInfoFetched: RestoreInfo.Status
    kSubTasksCreated: RestoreInfo.Status
    kSubTasksFinished: RestoreInfo.Status
    kViewDeleted: RestoreInfo.Status
    kPulseCreated: RestoreInfo.Status
    kOwnersRootDriveFetched: RestoreInfo.Status
    class EntityRootDriveMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ONE_DRIVE_RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_restore_info: _descriptor.FieldDescriptor
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ROOT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASKS_VEC_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_DRIVE_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    USER_IDX_TO_BE_DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    DRIVE_IDX_TO_BE_DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    ITEM_IDX_TO_BE_DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    LAST_VISITED_DRIVE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_API_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ROOT_DRIVE_MAP_FIELD_NUMBER: _ClassVar[int]
    TARGET_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ERRORS_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    status: RestoreInfo.Status
    view_root_path_vec: _containers.RepeatedScalarFieldContainer[str]
    sub_tasks_vec: _containers.RepeatedCompositeFieldContainer[_sub_task_pb2.SubTaskInfo]
    error: _error_pb2.ErrorProto
    restore_drive_item_vec: _containers.RepeatedCompositeFieldContainer[RestoreDriveItem]
    user_idx_to_be_discovered: int
    drive_idx_to_be_discovered: int
    item_idx_to_be_discovered: int
    last_visited_drive_item_id: str
    has_more_items: bool
    total_api_call_count: int
    entity_root_drive_map: _containers.ScalarMap[int, str]
    target_drive_id: str
    total_errors_encountered: int
    def __init__(self, status: _Optional[_Union[RestoreInfo.Status, str]] = ..., view_root_path_vec: _Optional[_Iterable[str]] = ..., sub_tasks_vec: _Optional[_Iterable[_Union[_sub_task_pb2.SubTaskInfo, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., restore_drive_item_vec: _Optional[_Iterable[_Union[RestoreDriveItem, _Mapping]]] = ..., user_idx_to_be_discovered: _Optional[int] = ..., drive_idx_to_be_discovered: _Optional[int] = ..., item_idx_to_be_discovered: _Optional[int] = ..., last_visited_drive_item_id: _Optional[str] = ..., has_more_items: bool = ..., total_api_call_count: _Optional[int] = ..., entity_root_drive_map: _Optional[_Mapping[int, str]] = ..., target_drive_id: _Optional[str] = ..., total_errors_encountered: _Optional[int] = ...) -> None: ...

class RestoreEntityInfo(_message.Message):
    __slots__ = ("drive_info_vec",)
    class DriveItemStatus(_message.Message):
        __slots__ = ("restore_completed", "sub_task_idx", "sub_task_completed", "source_root_path", "src_relative_path", "src_folder_id", "error")
        RESTORE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_IDX_FIELD_NUMBER: _ClassVar[int]
        SUB_TASK_COMPLETED_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
        SRC_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        SRC_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        restore_completed: bool
        sub_task_idx: int
        sub_task_completed: bool
        source_root_path: str
        src_relative_path: str
        src_folder_id: str
        error: _error_pb2.ErrorProto
        def __init__(self, restore_completed: bool = ..., sub_task_idx: _Optional[int] = ..., sub_task_completed: bool = ..., source_root_path: _Optional[str] = ..., src_relative_path: _Optional[str] = ..., src_folder_id: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class DriveItemInfo(_message.Message):
        __slots__ = ("restore_drive_item_vec", "drive_item_status", "given_path")
        RESTORE_DRIVE_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ITEM_STATUS_FIELD_NUMBER: _ClassVar[int]
        GIVEN_PATH_FIELD_NUMBER: _ClassVar[int]
        restore_drive_item_vec: _containers.RepeatedCompositeFieldContainer[DriveItem]
        drive_item_status: RestoreEntityInfo.DriveItemStatus
        given_path: str
        def __init__(self, restore_drive_item_vec: _Optional[_Iterable[_Union[DriveItem, _Mapping]]] = ..., drive_item_status: _Optional[_Union[RestoreEntityInfo.DriveItemStatus, _Mapping]] = ..., given_path: _Optional[str] = ...) -> None: ...
    class DriveInfo(_message.Message):
        __slots__ = ("drive_item_info_vec",)
        DRIVE_ITEM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
        drive_item_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreEntityInfo.DriveItemInfo]
        def __init__(self, drive_item_info_vec: _Optional[_Iterable[_Union[RestoreEntityInfo.DriveItemInfo, _Mapping]]] = ...) -> None: ...
    ONE_DRIVE_RESTORE_ENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    one_drive_restore_entity_info: _descriptor.FieldDescriptor
    DRIVE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    drive_info_vec: _containers.RepeatedCompositeFieldContainer[RestoreEntityInfo.DriveInfo]
    def __init__(self, drive_info_vec: _Optional[_Iterable[_Union[RestoreEntityInfo.DriveInfo, _Mapping]]] = ...) -> None: ...

class SiteDrive(_message.Message):
    __slots__ = ("id", "name", "created_by", "created_date_time", "last_modified_by", "last_modified_date_time", "parent_reference", "web_url", "display_name", "system_facet", "quota", "template_name", "cohesity_drive_type", "list")
    class Quota(_message.Message):
        __slots__ = ("total_size_in_bytes", "used_size_in_bytes")
        TOTAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        USED_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
        total_size_in_bytes: int
        used_size_in_bytes: int
        def __init__(self, total_size_in_bytes: _Optional[int] = ..., used_size_in_bytes: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FACET_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    COHESITY_DRIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_by: _graph_external_pb2.IdentitySet
    created_date_time: str
    last_modified_by: _graph_external_pb2.IdentitySet
    last_modified_date_time: str
    parent_reference: ItemReference
    web_url: str
    display_name: str
    system_facet: System
    quota: SiteDrive.Quota
    template_name: str
    cohesity_drive_type: _graph_enums_pb2.DriveType.Type
    list: List
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., created_date_time: _Optional[str] = ..., last_modified_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., last_modified_date_time: _Optional[str] = ..., parent_reference: _Optional[_Union[ItemReference, _Mapping]] = ..., web_url: _Optional[str] = ..., display_name: _Optional[str] = ..., system_facet: _Optional[_Union[System, _Mapping]] = ..., quota: _Optional[_Union[SiteDrive.Quota, _Mapping]] = ..., template_name: _Optional[str] = ..., cohesity_drive_type: _Optional[_Union[_graph_enums_pb2.DriveType.Type, str]] = ..., list: _Optional[_Union[List, _Mapping]] = ...) -> None: ...

class SharepointListSubTaskScribeInfo(_message.Message):
    __slots__ = ("site_id", "site_list_vec")
    SHAREPOINT_LIST_SUB_TASK_SCRIBE_INFO_FIELD_NUMBER: _ClassVar[int]
    sharepoint_list_sub_task_scribe_info: _descriptor.FieldDescriptor
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_LIST_VEC_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    site_list_vec: _containers.RepeatedCompositeFieldContainer[List]
    def __init__(self, site_id: _Optional[str] = ..., site_list_vec: _Optional[_Iterable[_Union[List, _Mapping]]] = ...) -> None: ...

class DeadTimeInfo(_message.Message):
    __slots__ = ("reason", "time_usecs")
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kThrottling: _ClassVar[DeadTimeInfo.Reason]
        kWaitingForPermit: _ClassVar[DeadTimeInfo.Reason]
    kThrottling: DeadTimeInfo.Reason
    kWaitingForPermit: DeadTimeInfo.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    reason: DeadTimeInfo.Reason
    time_usecs: int
    def __init__(self, reason: _Optional[_Union[DeadTimeInfo.Reason, str]] = ..., time_usecs: _Optional[int] = ...) -> None: ...

class DBInfo(_message.Message):
    __slots__ = ("db_open_time_usecs", "cache_prepopulation_time", "final_flush_time", "estimated_num_keys")
    DB_OPEN_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CACHE_PREPOPULATION_TIME_FIELD_NUMBER: _ClassVar[int]
    FINAL_FLUSH_TIME_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_NUM_KEYS_FIELD_NUMBER: _ClassVar[int]
    db_open_time_usecs: int
    cache_prepopulation_time: int
    final_flush_time: int
    estimated_num_keys: int
    def __init__(self, db_open_time_usecs: _Optional[int] = ..., cache_prepopulation_time: _Optional[int] = ..., final_flush_time: _Optional[int] = ..., estimated_num_keys: _Optional[int] = ...) -> None: ...

class SetupInfoStats(_message.Message):
    __slots__ = ("num_drive_items_processed", "total_time_usecs", "total_created_file_size", "num_created_files", "num_created_folders", "total_deleted_file_size", "num_deleted_files", "num_deleted_folders", "total_updated_file_size", "num_updated_files", "num_updated_folders", "dead_time_info", "db_info")
    NUM_DRIVE_ITEMS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CREATED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELETED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UPDATED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_UPDATED_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_UPDATED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_INFO_FIELD_NUMBER: _ClassVar[int]
    DB_INFO_FIELD_NUMBER: _ClassVar[int]
    num_drive_items_processed: int
    total_time_usecs: int
    total_created_file_size: int
    num_created_files: int
    num_created_folders: int
    total_deleted_file_size: int
    num_deleted_files: int
    num_deleted_folders: int
    total_updated_file_size: int
    num_updated_files: int
    num_updated_folders: int
    dead_time_info: _containers.RepeatedCompositeFieldContainer[DeadTimeInfo]
    db_info: DBInfo
    def __init__(self, num_drive_items_processed: _Optional[int] = ..., total_time_usecs: _Optional[int] = ..., total_created_file_size: _Optional[int] = ..., num_created_files: _Optional[int] = ..., num_created_folders: _Optional[int] = ..., total_deleted_file_size: _Optional[int] = ..., num_deleted_files: _Optional[int] = ..., num_deleted_folders: _Optional[int] = ..., total_updated_file_size: _Optional[int] = ..., num_updated_files: _Optional[int] = ..., num_updated_folders: _Optional[int] = ..., dead_time_info: _Optional[_Iterable[_Union[DeadTimeInfo, _Mapping]]] = ..., db_info: _Optional[_Union[DBInfo, _Mapping]] = ...) -> None: ...

class SubTaskInfoStats(_message.Message):
    __slots__ = ("sub_task_id", "data_ingested", "total_time_usecs", "total_read_time_usecs", "total_write_time_usecs", "dead_time_info")
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_INGESTED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WRITE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_INFO_FIELD_NUMBER: _ClassVar[int]
    sub_task_id: str
    data_ingested: int
    total_time_usecs: int
    total_read_time_usecs: int
    total_write_time_usecs: int
    dead_time_info: _containers.RepeatedCompositeFieldContainer[DeadTimeInfo]
    def __init__(self, sub_task_id: _Optional[str] = ..., data_ingested: _Optional[int] = ..., total_time_usecs: _Optional[int] = ..., total_read_time_usecs: _Optional[int] = ..., total_write_time_usecs: _Optional[int] = ..., dead_time_info: _Optional[_Iterable[_Union[DeadTimeInfo, _Mapping]]] = ...) -> None: ...

class SubTaskActionInfo(_message.Message):
    __slots__ = ("read_time_usecs", "write_time_usecs", "dead_time_info")
    READ_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    WRITE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_INFO_FIELD_NUMBER: _ClassVar[int]
    read_time_usecs: int
    write_time_usecs: int
    dead_time_info: _containers.RepeatedCompositeFieldContainer[DeadTimeInfo]
    def __init__(self, read_time_usecs: _Optional[int] = ..., write_time_usecs: _Optional[int] = ..., dead_time_info: _Optional[_Iterable[_Union[DeadTimeInfo, _Mapping]]] = ...) -> None: ...

class BackupTaskStats(_message.Message):
    __slots__ = ("setup_info_stat_vec", "sub_task_info_stat_vec")
    SETUP_INFO_STAT_VEC_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_INFO_STAT_VEC_FIELD_NUMBER: _ClassVar[int]
    setup_info_stat_vec: _containers.RepeatedCompositeFieldContainer[SetupInfoStats]
    sub_task_info_stat_vec: _containers.RepeatedCompositeFieldContainer[SubTaskInfoStats]
    def __init__(self, setup_info_stat_vec: _Optional[_Iterable[_Union[SetupInfoStats, _Mapping]]] = ..., sub_task_info_stat_vec: _Optional[_Iterable[_Union[SubTaskInfoStats, _Mapping]]] = ...) -> None: ...

class Recipients(_message.Message):
    __slots__ = ("email", "alias", "object_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    alias: str
    object_id: str
    def __init__(self, email: _Optional[str] = ..., alias: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class SharingLink(_message.Message):
    __slots__ = ("application", "type", "scope", "web_url", "prevents_download")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    PREVENTS_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    application: _graph_external_pb2.Identity
    type: str
    scope: str
    web_url: str
    prevents_download: bool
    def __init__(self, application: _Optional[_Union[_graph_external_pb2.Identity, _Mapping]] = ..., type: _Optional[str] = ..., scope: _Optional[str] = ..., web_url: _Optional[str] = ..., prevents_download: bool = ...) -> None: ...

class SharingInvitation(_message.Message):
    __slots__ = ("email", "invited_by", "sign_in_required")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    INVITED_BY_FIELD_NUMBER: _ClassVar[int]
    SIGN_IN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    email: str
    invited_by: _graph_external_pb2.IdentitySet
    sign_in_required: bool
    def __init__(self, email: _Optional[str] = ..., invited_by: _Optional[_Union[_graph_external_pb2.IdentitySet, _Mapping]] = ..., sign_in_required: bool = ...) -> None: ...

class IncrementalChangesFileHeader(_message.Message):
    __slots__ = ("magic_number", "is_valid", "payload_offset")
    MAGIC_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    magic_number: int
    is_valid: int
    payload_offset: int
    def __init__(self, magic_number: _Optional[int] = ..., is_valid: _Optional[int] = ..., payload_offset: _Optional[int] = ...) -> None: ...

class IncrementalDriveItemChange(_message.Message):
    __slots__ = ("drive_item_type", "change_type", "old_full_path", "new_full_path", "size_bytes", "mtime_usecs", "changed_drive_item")
    class DriveItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[IncrementalDriveItemChange.DriveItemType]
        kFolder: _ClassVar[IncrementalDriveItemChange.DriveItemType]
    kFile: IncrementalDriveItemChange.DriveItemType
    kFolder: IncrementalDriveItemChange.DriveItemType
    class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCreated: _ClassVar[IncrementalDriveItemChange.ChangeType]
        kDeleted: _ClassVar[IncrementalDriveItemChange.ChangeType]
        kRenamed: _ClassVar[IncrementalDriveItemChange.ChangeType]
        kUpdated: _ClassVar[IncrementalDriveItemChange.ChangeType]
    kCreated: IncrementalDriveItemChange.ChangeType
    kDeleted: IncrementalDriveItemChange.ChangeType
    kRenamed: IncrementalDriveItemChange.ChangeType
    kUpdated: IncrementalDriveItemChange.ChangeType
    DRIVE_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OLD_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MTIME_USECS_FIELD_NUMBER: _ClassVar[int]
    CHANGED_DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    drive_item_type: IncrementalDriveItemChange.DriveItemType
    change_type: IncrementalDriveItemChange.ChangeType
    old_full_path: str
    new_full_path: str
    size_bytes: int
    mtime_usecs: int
    changed_drive_item: DriveItem
    def __init__(self, drive_item_type: _Optional[_Union[IncrementalDriveItemChange.DriveItemType, str]] = ..., change_type: _Optional[_Union[IncrementalDriveItemChange.ChangeType, str]] = ..., old_full_path: _Optional[str] = ..., new_full_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., mtime_usecs: _Optional[int] = ..., changed_drive_item: _Optional[_Union[DriveItem, _Mapping]] = ...) -> None: ...

class DirectoryObject(_message.Message):
    __slots__ = ("id", "type", "removed", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    removed: RemovalInformation
    display_name: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., removed: _Optional[_Union[RemovalInformation, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...

class RemovalInformation(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class UsersList(_message.Message):
    __slots__ = ("owner_ids_vec", "member_ids_vec")
    OWNER_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    owner_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    member_ids_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, owner_ids_vec: _Optional[_Iterable[str]] = ..., member_ids_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class Channel(_message.Message):
    __slots__ = ("id", "display_name", "description", "email", "web_url", "membership_type", "site_id", "drive_id", "channel_type", "members", "tabs", "is_site_provisioned", "moderation_settings", "channel_folder_name", "graph_error", "created_date_time", "site_name", "site_url")
    class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPublic: _ClassVar[Channel.ChannelType]
        kPrivate: _ClassVar[Channel.ChannelType]
        kUnknownFutureValue: _ClassVar[Channel.ChannelType]
        kShared: _ClassVar[Channel.ChannelType]
    kPublic: Channel.ChannelType
    kPrivate: Channel.ChannelType
    kUnknownFutureValue: Channel.ChannelType
    kShared: Channel.ChannelType
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    TABS_FIELD_NUMBER: _ClassVar[int]
    IS_SITE_PROVISIONED_FIELD_NUMBER: _ClassVar[int]
    MODERATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    GRAPH_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    SITE_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    description: str
    email: str
    web_url: str
    membership_type: str
    site_id: str
    drive_id: str
    channel_type: Channel.ChannelType
    members: _containers.RepeatedCompositeFieldContainer[ChannelMemberInfo]
    tabs: _containers.RepeatedCompositeFieldContainer[ChannelTabInfo]
    is_site_provisioned: bool
    moderation_settings: ChannelModerationSettings
    channel_folder_name: str
    graph_error: GraphError
    created_date_time: str
    site_name: str
    site_url: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., email: _Optional[str] = ..., web_url: _Optional[str] = ..., membership_type: _Optional[str] = ..., site_id: _Optional[str] = ..., drive_id: _Optional[str] = ..., channel_type: _Optional[_Union[Channel.ChannelType, str]] = ..., members: _Optional[_Iterable[_Union[ChannelMemberInfo, _Mapping]]] = ..., tabs: _Optional[_Iterable[_Union[ChannelTabInfo, _Mapping]]] = ..., is_site_provisioned: bool = ..., moderation_settings: _Optional[_Union[ChannelModerationSettings, _Mapping]] = ..., channel_folder_name: _Optional[str] = ..., graph_error: _Optional[_Union[GraphError, _Mapping]] = ..., created_date_time: _Optional[str] = ..., site_name: _Optional[str] = ..., site_url: _Optional[str] = ...) -> None: ...

class ChannelMemberInfo(_message.Message):
    __slots__ = ("odata_type", "id", "display_name", "user_id", "email_address", "roles", "user_bind", "is_favourite_by_default")
    ODATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_BIND_FIELD_NUMBER: _ClassVar[int]
    IS_FAVOURITE_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    odata_type: str
    id: str
    display_name: str
    user_id: str
    email_address: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    user_bind: str
    is_favourite_by_default: bool
    def __init__(self, odata_type: _Optional[str] = ..., id: _Optional[str] = ..., display_name: _Optional[str] = ..., user_id: _Optional[str] = ..., email_address: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., user_bind: _Optional[str] = ..., is_favourite_by_default: bool = ...) -> None: ...

class MemberDetails(_message.Message):
    __slots__ = ("odata_type", "roles", "user", "display_name", "user_id")
    ODATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    odata_type: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    user: str
    display_name: str
    user_id: str
    def __init__(self, odata_type: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., user: _Optional[str] = ..., display_name: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ("id", "created_date_time", "display_name", "description", "internal_id", "classification", "web_url", "is_archived", "is_membership_limited_to_owners", "discovery_settings", "member_settings", "guest_settings", "messaging_settings", "fun_settings", "team_template", "owners", "pub_channels", "priv_channels", "members", "mail_nickname")
    class TeamSpecialization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[Team.TeamSpecialization]
        kEducationStandard: _ClassVar[Team.TeamSpecialization]
        kEducationClass: _ClassVar[Team.TeamSpecialization]
        kEducationProfessionalLearningCommunity: _ClassVar[Team.TeamSpecialization]
        kEducationStaff: _ClassVar[Team.TeamSpecialization]
        kUnknownFutureValue: _ClassVar[Team.TeamSpecialization]
    kNone: Team.TeamSpecialization
    kEducationStandard: Team.TeamSpecialization
    kEducationClass: Team.TeamSpecialization
    kEducationProfessionalLearningCommunity: Team.TeamSpecialization
    kEducationStaff: Team.TeamSpecialization
    kUnknownFutureValue: Team.TeamSpecialization
    class TeamVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrivate: _ClassVar[Team.TeamVisibility]
        kPublic: _ClassVar[Team.TeamVisibility]
    kPrivate: Team.TeamVisibility
    kPublic: Team.TeamVisibility
    class DiscoverySettings(_message.Message):
        __slots__ = ("show_in_teams_search_and_suggestions",)
        SHOW_IN_TEAMS_SEARCH_AND_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        show_in_teams_search_and_suggestions: bool
        def __init__(self, show_in_teams_search_and_suggestions: bool = ...) -> None: ...
    class MemberSettings(_message.Message):
        __slots__ = ("allow_create_update_channels", "allow_create_private_channels", "allow_delete_channels", "allow_add_remove_apps", "allow_create_update_remove_tabs", "allow_create_update_remove_connectors")
        ALLOW_CREATE_UPDATE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CREATE_PRIVATE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DELETE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ADD_REMOVE_APPS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CREATE_UPDATE_REMOVE_TABS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CREATE_UPDATE_REMOVE_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
        allow_create_update_channels: bool
        allow_create_private_channels: bool
        allow_delete_channels: bool
        allow_add_remove_apps: bool
        allow_create_update_remove_tabs: bool
        allow_create_update_remove_connectors: bool
        def __init__(self, allow_create_update_channels: bool = ..., allow_create_private_channels: bool = ..., allow_delete_channels: bool = ..., allow_add_remove_apps: bool = ..., allow_create_update_remove_tabs: bool = ..., allow_create_update_remove_connectors: bool = ...) -> None: ...
    class GuestSettings(_message.Message):
        __slots__ = ("allow_create_update_channels", "allow_delete_channels")
        ALLOW_CREATE_UPDATE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_DELETE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        allow_create_update_channels: bool
        allow_delete_channels: bool
        def __init__(self, allow_create_update_channels: bool = ..., allow_delete_channels: bool = ...) -> None: ...
    class MessagingSettings(_message.Message):
        __slots__ = ("allow_user_edit_messages", "allow_user_delete_messages", "allow_owner_delete_messages", "allow_team_mentions", "allow_channel_mentions")
        ALLOW_USER_EDIT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_USER_DELETE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_OWNER_DELETE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_TEAM_MENTIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CHANNEL_MENTIONS_FIELD_NUMBER: _ClassVar[int]
        allow_user_edit_messages: bool
        allow_user_delete_messages: bool
        allow_owner_delete_messages: bool
        allow_team_mentions: bool
        allow_channel_mentions: bool
        def __init__(self, allow_user_edit_messages: bool = ..., allow_user_delete_messages: bool = ..., allow_owner_delete_messages: bool = ..., allow_team_mentions: bool = ..., allow_channel_mentions: bool = ...) -> None: ...
    class FunSettings(_message.Message):
        __slots__ = ("allow_giphy", "giphy_content_rating", "allow_stickers_and_memes", "allow_custom_memes")
        ALLOW_GIPHY_FIELD_NUMBER: _ClassVar[int]
        GIPHY_CONTENT_RATING_FIELD_NUMBER: _ClassVar[int]
        ALLOW_STICKERS_AND_MEMES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CUSTOM_MEMES_FIELD_NUMBER: _ClassVar[int]
        allow_giphy: bool
        giphy_content_rating: str
        allow_stickers_and_memes: bool
        allow_custom_memes: bool
        def __init__(self, allow_giphy: bool = ..., giphy_content_rating: _Optional[str] = ..., allow_stickers_and_memes: bool = ..., allow_custom_memes: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    IS_MEMBERSHIP_LIMITED_TO_OWNERS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GUEST_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MESSAGING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FUN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TEAM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    PUB_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    PRIV_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MAIL_NICKNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_date_time: str
    display_name: str
    description: str
    internal_id: str
    classification: str
    web_url: str
    is_archived: bool
    is_membership_limited_to_owners: bool
    discovery_settings: Team.DiscoverySettings
    member_settings: Team.MemberSettings
    guest_settings: Team.GuestSettings
    messaging_settings: Team.MessagingSettings
    fun_settings: Team.FunSettings
    team_template: str
    owners: _containers.RepeatedScalarFieldContainer[str]
    pub_channels: _containers.RepeatedCompositeFieldContainer[Channel]
    priv_channels: _containers.RepeatedCompositeFieldContainer[Channel]
    members: _containers.RepeatedCompositeFieldContainer[MemberDetails]
    mail_nickname: str
    def __init__(self, id: _Optional[str] = ..., created_date_time: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., internal_id: _Optional[str] = ..., classification: _Optional[str] = ..., web_url: _Optional[str] = ..., is_archived: bool = ..., is_membership_limited_to_owners: bool = ..., discovery_settings: _Optional[_Union[Team.DiscoverySettings, _Mapping]] = ..., member_settings: _Optional[_Union[Team.MemberSettings, _Mapping]] = ..., guest_settings: _Optional[_Union[Team.GuestSettings, _Mapping]] = ..., messaging_settings: _Optional[_Union[Team.MessagingSettings, _Mapping]] = ..., fun_settings: _Optional[_Union[Team.FunSettings, _Mapping]] = ..., team_template: _Optional[str] = ..., owners: _Optional[_Iterable[str]] = ..., pub_channels: _Optional[_Iterable[_Union[Channel, _Mapping]]] = ..., priv_channels: _Optional[_Iterable[_Union[Channel, _Mapping]]] = ..., members: _Optional[_Iterable[_Union[MemberDetails, _Mapping]]] = ..., mail_nickname: _Optional[str] = ...) -> None: ...

class ChannelTabInfo(_message.Message):
    __slots__ = ("id", "display_name", "web_url", "teams_tab_configuration", "app_id", "teams_app")
    class TeamsTabConfiguration(_message.Message):
        __slots__ = ("entity_id", "content_url", "website_url", "remove_url", "date_added")
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
        REMOVE_URL_FIELD_NUMBER: _ClassVar[int]
        DATE_ADDED_FIELD_NUMBER: _ClassVar[int]
        entity_id: str
        content_url: str
        website_url: str
        remove_url: str
        date_added: str
        def __init__(self, entity_id: _Optional[str] = ..., content_url: _Optional[str] = ..., website_url: _Optional[str] = ..., remove_url: _Optional[str] = ..., date_added: _Optional[str] = ...) -> None: ...
    class TeamsApp(_message.Message):
        __slots__ = ("id", "external_id", "display_name", "distribution_method")
        ID_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DISTRIBUTION_METHOD_FIELD_NUMBER: _ClassVar[int]
        id: str
        external_id: str
        display_name: str
        distribution_method: str
        def __init__(self, id: _Optional[str] = ..., external_id: _Optional[str] = ..., display_name: _Optional[str] = ..., distribution_method: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    TEAMS_TAB_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_APP_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    web_url: str
    teams_tab_configuration: ChannelTabInfo.TeamsTabConfiguration
    app_id: str
    teams_app: ChannelTabInfo.TeamsApp
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., web_url: _Optional[str] = ..., teams_tab_configuration: _Optional[_Union[ChannelTabInfo.TeamsTabConfiguration, _Mapping]] = ..., app_id: _Optional[str] = ..., teams_app: _Optional[_Union[ChannelTabInfo.TeamsApp, _Mapping]] = ...) -> None: ...

class ChannelModerationSettings(_message.Message):
    __slots__ = ("allow_new_message_from_bots", "allow_new_message_from_connectors", "reply_restriction", "user_new_message_restriction")
    ALLOW_NEW_MESSAGE_FROM_BOTS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NEW_MESSAGE_FROM_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    REPLY_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    USER_NEW_MESSAGE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    allow_new_message_from_bots: bool
    allow_new_message_from_connectors: bool
    reply_restriction: str
    user_new_message_restriction: str
    def __init__(self, allow_new_message_from_bots: bool = ..., allow_new_message_from_connectors: bool = ..., reply_restriction: _Optional[str] = ..., user_new_message_restriction: _Optional[str] = ...) -> None: ...

class OpenIdConfiguration(_message.Message):
    __slots__ = ("token_endpoint", "tenant_region_scope", "tenant_region_sub_scope", "cloud_instance_name", "cloud_graph_host_name", "msgraph_host")
    TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TENANT_REGION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    TENANT_REGION_SUB_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_GRAPH_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    MSGRAPH_HOST_FIELD_NUMBER: _ClassVar[int]
    token_endpoint: str
    tenant_region_scope: str
    tenant_region_sub_scope: str
    cloud_instance_name: str
    cloud_graph_host_name: str
    msgraph_host: str
    def __init__(self, token_endpoint: _Optional[str] = ..., tenant_region_scope: _Optional[str] = ..., tenant_region_sub_scope: _Optional[str] = ..., cloud_instance_name: _Optional[str] = ..., cloud_graph_host_name: _Optional[str] = ..., msgraph_host: _Optional[str] = ...) -> None: ...

class JWTPayloadClaims(_message.Message):
    __slots__ = ("audience", "security_token_service", "app_id", "app_id_v2", "app_displayname", "roles", "subject_id", "object_id", "tenant_id", "name_identifier")
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TOKEN_SERVICE_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_V2_FIELD_NUMBER: _ClassVar[int]
    APP_DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    audience: str
    security_token_service: str
    app_id: str
    app_id_v2: str
    app_displayname: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    subject_id: str
    object_id: str
    tenant_id: str
    name_identifier: str
    def __init__(self, audience: _Optional[str] = ..., security_token_service: _Optional[str] = ..., app_id: _Optional[str] = ..., app_id_v2: _Optional[str] = ..., app_displayname: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., subject_id: _Optional[str] = ..., object_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., name_identifier: _Optional[str] = ...) -> None: ...

class AppRoleAssignment(_message.Message):
    __slots__ = ("id", "principal_id", "principal_type", "principal_display_name", "resource_id", "resource_display_name", "app_role_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    principal_id: str
    principal_type: str
    principal_display_name: str
    resource_id: str
    resource_display_name: str
    app_role_id: str
    def __init__(self, id: _Optional[str] = ..., principal_id: _Optional[str] = ..., principal_type: _Optional[str] = ..., principal_display_name: _Optional[str] = ..., resource_id: _Optional[str] = ..., resource_display_name: _Optional[str] = ..., app_role_id: _Optional[str] = ...) -> None: ...

class OAuth2PermissionGrant(_message.Message):
    __slots__ = ("id", "client_id", "consent_type", "principal_id", "resource_id", "scope")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONSENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    client_id: str
    consent_type: str
    principal_id: str
    resource_id: str
    scope: str
    def __init__(self, id: _Optional[str] = ..., client_id: _Optional[str] = ..., consent_type: _Optional[str] = ..., principal_id: _Optional[str] = ..., resource_id: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...

class AppRole(_message.Message):
    __slots__ = ("id", "value", "display_name", "cohesity_env_type_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ENV_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    value: str
    display_name: str
    cohesity_env_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ..., display_name: _Optional[str] = ..., cohesity_env_type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ...) -> None: ...

class PermissionScope(_message.Message):
    __slots__ = ("id", "value", "display_name", "cohesity_env_type_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ENV_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    value: str
    display_name: str
    cohesity_env_type_vec: _containers.RepeatedScalarFieldContainer[_enums_pb2.Environment.Type]
    def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ..., display_name: _Optional[str] = ..., cohesity_env_type_vec: _Optional[_Iterable[_Union[_enums_pb2.Environment.Type, str]]] = ...) -> None: ...

class ServicePrincipal(_message.Message):
    __slots__ = ("id", "display_name", "app_id", "app_display_name", "application_permission_vec", "delegated_permission_vec", "app_role_assignments_vec", "oauth2_permission_grants_vec")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_ROLE_ASSIGNMENTS_VEC_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_PERMISSION_GRANTS_VEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    app_id: str
    app_display_name: str
    application_permission_vec: _containers.RepeatedCompositeFieldContainer[AppRole]
    delegated_permission_vec: _containers.RepeatedCompositeFieldContainer[PermissionScope]
    app_role_assignments_vec: _containers.RepeatedCompositeFieldContainer[AppRoleAssignment]
    oauth2_permission_grants_vec: _containers.RepeatedCompositeFieldContainer[OAuth2PermissionGrant]
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., app_id: _Optional[str] = ..., app_display_name: _Optional[str] = ..., application_permission_vec: _Optional[_Iterable[_Union[AppRole, _Mapping]]] = ..., delegated_permission_vec: _Optional[_Iterable[_Union[PermissionScope, _Mapping]]] = ..., app_role_assignments_vec: _Optional[_Iterable[_Union[AppRoleAssignment, _Mapping]]] = ..., oauth2_permission_grants_vec: _Optional[_Iterable[_Union[OAuth2PermissionGrant, _Mapping]]] = ...) -> None: ...

class AppApiPermissions(_message.Message):
    __slots__ = ("mailbox_api_permission_vec", "onedrive_api_permission_vec", "sharepoint_api_permission_vec", "ms_groups_api_permission_vec", "ms_teams_api_permission_vec", "application", "missing_application_permission_vec", "application_error")
    MAILBOX_API_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    ONEDRIVE_API_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_API_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    MS_GROUPS_API_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    MS_TEAMS_API_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    MISSING_APPLICATION_PERMISSION_VEC_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    mailbox_api_permission_vec: _containers.RepeatedCompositeFieldContainer[ServicePrincipal]
    onedrive_api_permission_vec: _containers.RepeatedCompositeFieldContainer[ServicePrincipal]
    sharepoint_api_permission_vec: _containers.RepeatedCompositeFieldContainer[ServicePrincipal]
    ms_groups_api_permission_vec: _containers.RepeatedCompositeFieldContainer[ServicePrincipal]
    ms_teams_api_permission_vec: _containers.RepeatedCompositeFieldContainer[ServicePrincipal]
    application: ServicePrincipal
    missing_application_permission_vec: _containers.RepeatedCompositeFieldContainer[ServicePrincipal]
    application_error: AzureADSecurityTokenServiceError
    def __init__(self, mailbox_api_permission_vec: _Optional[_Iterable[_Union[ServicePrincipal, _Mapping]]] = ..., onedrive_api_permission_vec: _Optional[_Iterable[_Union[ServicePrincipal, _Mapping]]] = ..., sharepoint_api_permission_vec: _Optional[_Iterable[_Union[ServicePrincipal, _Mapping]]] = ..., ms_groups_api_permission_vec: _Optional[_Iterable[_Union[ServicePrincipal, _Mapping]]] = ..., ms_teams_api_permission_vec: _Optional[_Iterable[_Union[ServicePrincipal, _Mapping]]] = ..., application: _Optional[_Union[ServicePrincipal, _Mapping]] = ..., missing_application_permission_vec: _Optional[_Iterable[_Union[ServicePrincipal, _Mapping]]] = ..., application_error: _Optional[_Union[AzureADSecurityTokenServiceError, _Mapping]] = ...) -> None: ...

class O365ErrorDBEntry(_message.Message):
    __slots__ = ("drive_item", "error_encountered", "timestamp", "is_retriable", "action_item")
    DRIVE_ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_ENCOUNTERED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_RETRIABLE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
    drive_item: DriveItem
    error_encountered: _error_pb2.ErrorProto
    timestamp: int
    is_retriable: bool
    action_item: str
    def __init__(self, drive_item: _Optional[_Union[DriveItem, _Mapping]] = ..., error_encountered: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., timestamp: _Optional[int] = ..., is_retriable: bool = ..., action_item: _Optional[str] = ...) -> None: ...

class SharepointDataStats(_message.Message):
    __slots__ = ("total_created_file_size", "num_created_files", "num_created_folders", "num_created_doclibs", "total_deleted_file_size", "num_deleted_files", "num_deleted_folders", "num_deleted_doclibs", "total_updated_file_size", "num_updated_files", "num_updated_folders", "num_updated_doclibs")
    TOTAL_CREATED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATED_DOCLIBS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELETED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_DELETED_DOCLIBS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_UPDATED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_UPDATED_FILES_FIELD_NUMBER: _ClassVar[int]
    NUM_UPDATED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_UPDATED_DOCLIBS_FIELD_NUMBER: _ClassVar[int]
    total_created_file_size: int
    num_created_files: int
    num_created_folders: int
    num_created_doclibs: int
    total_deleted_file_size: int
    num_deleted_files: int
    num_deleted_folders: int
    num_deleted_doclibs: int
    total_updated_file_size: int
    num_updated_files: int
    num_updated_folders: int
    num_updated_doclibs: int
    def __init__(self, total_created_file_size: _Optional[int] = ..., num_created_files: _Optional[int] = ..., num_created_folders: _Optional[int] = ..., num_created_doclibs: _Optional[int] = ..., total_deleted_file_size: _Optional[int] = ..., num_deleted_files: _Optional[int] = ..., num_deleted_folders: _Optional[int] = ..., num_deleted_doclibs: _Optional[int] = ..., total_updated_file_size: _Optional[int] = ..., num_updated_files: _Optional[int] = ..., num_updated_folders: _Optional[int] = ..., num_updated_doclibs: _Optional[int] = ...) -> None: ...

class ResourceAccess(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class RequiredResourceAccess(_message.Message):
    __slots__ = ("resource_app_id", "resource_access_vec")
    RESOURCE_APP_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ACCESS_VEC_FIELD_NUMBER: _ClassVar[int]
    resource_app_id: str
    resource_access_vec: _containers.RepeatedCompositeFieldContainer[ResourceAccess]
    def __init__(self, resource_app_id: _Optional[str] = ..., resource_access_vec: _Optional[_Iterable[_Union[ResourceAccess, _Mapping]]] = ...) -> None: ...

class PasswordCredential(_message.Message):
    __slots__ = ("display_name", "hint", "key_id", "secret_text")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_TEXT_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    hint: str
    key_id: str
    secret_text: str
    def __init__(self, display_name: _Optional[str] = ..., hint: _Optional[str] = ..., key_id: _Optional[str] = ..., secret_text: _Optional[str] = ...) -> None: ...

class PasswordCredentialWrapper(_message.Message):
    __slots__ = ("password_credential",)
    PASSWORD_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    password_credential: PasswordCredential
    def __init__(self, password_credential: _Optional[_Union[PasswordCredential, _Mapping]] = ...) -> None: ...

class KeyCredential(_message.Message):
    __slots__ = ("key", "key_id", "display_name", "usage", "type")
    KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    key_id: str
    display_name: str
    usage: str
    type: str
    def __init__(self, key: _Optional[str] = ..., key_id: _Optional[str] = ..., display_name: _Optional[str] = ..., usage: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class AzureActiveDirectoryAppManifest(_message.Message):
    __slots__ = ("id", "app_id", "display_name", "signin_audience", "key_credentials_vec", "password_credentials_vec", "required_resource_access_vec", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNIN_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    KEY_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CREDENTIALS_VEC_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_RESOURCE_ACCESS_VEC_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    app_id: str
    display_name: str
    signin_audience: str
    key_credentials_vec: _containers.RepeatedCompositeFieldContainer[KeyCredential]
    password_credentials_vec: _containers.RepeatedCompositeFieldContainer[PasswordCredential]
    required_resource_access_vec: _containers.RepeatedCompositeFieldContainer[RequiredResourceAccess]
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., app_id: _Optional[str] = ..., display_name: _Optional[str] = ..., signin_audience: _Optional[str] = ..., key_credentials_vec: _Optional[_Iterable[_Union[KeyCredential, _Mapping]]] = ..., password_credentials_vec: _Optional[_Iterable[_Union[PasswordCredential, _Mapping]]] = ..., required_resource_access_vec: _Optional[_Iterable[_Union[RequiredResourceAccess, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class DataDistributionTable(_message.Message):
    __slots__ = ("data_dist_bins_size_string", "data_dist_bin_vec")
    class DataDistributionBin(_message.Message):
        __slots__ = ("num_entities", "upper_limit")
        NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
        num_entities: int
        upper_limit: int
        def __init__(self, num_entities: _Optional[int] = ..., upper_limit: _Optional[int] = ...) -> None: ...
    DATA_DIST_BINS_SIZE_STRING_FIELD_NUMBER: _ClassVar[int]
    DATA_DIST_BIN_VEC_FIELD_NUMBER: _ClassVar[int]
    data_dist_bins_size_string: str
    data_dist_bin_vec: _containers.RepeatedCompositeFieldContainer[DataDistributionTable.DataDistributionBin]
    def __init__(self, data_dist_bins_size_string: _Optional[str] = ..., data_dist_bin_vec: _Optional[_Iterable[_Union[DataDistributionTable.DataDistributionBin, _Mapping]]] = ...) -> None: ...

class ThrottlingErrorTimeDistributionTable(_message.Message):
    __slots__ = ("throttling_time_bins_size_string", "throttling_time_bin_vec")
    class ThrottlingTimeBin(_message.Message):
        __slots__ = ("num_entities", "upper_limit")
        NUM_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
        num_entities: int
        upper_limit: int
        def __init__(self, num_entities: _Optional[int] = ..., upper_limit: _Optional[int] = ...) -> None: ...
    THROTTLING_TIME_BINS_SIZE_STRING_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_TIME_BIN_VEC_FIELD_NUMBER: _ClassVar[int]
    throttling_time_bins_size_string: str
    throttling_time_bin_vec: _containers.RepeatedCompositeFieldContainer[ThrottlingErrorTimeDistributionTable.ThrottlingTimeBin]
    def __init__(self, throttling_time_bins_size_string: _Optional[str] = ..., throttling_time_bin_vec: _Optional[_Iterable[_Union[ThrottlingErrorTimeDistributionTable.ThrottlingTimeBin, _Mapping]]] = ...) -> None: ...

class MailboxSettings(_message.Message):
    __slots__ = ("archive_folder", "user_purpose", "user_purpose_v2")
    ARCHIVE_FOLDER_FIELD_NUMBER: _ClassVar[int]
    USER_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    USER_PURPOSE_V2_FIELD_NUMBER: _ClassVar[int]
    archive_folder: str
    user_purpose: str
    user_purpose_v2: str
    def __init__(self, archive_folder: _Optional[str] = ..., user_purpose: _Optional[str] = ..., user_purpose_v2: _Optional[str] = ...) -> None: ...

class EmailItem(_message.Message):
    __slots__ = ("id", "subject", "sender", "to_recipient_vec", "cc_recipient_vec", "bcc_recipient_vec", "sent_date_time", "received_date_time", "parent_folder_id", "has_attachments", "reply_to_vec", "is_read", "is_draft", "weblink", "changekey", "last_modified_date_time", "categories", "internet_message_id", "is_delivery_receipt_requested", "is_read_receipt_requested", "body_preview", "importance", "conversation_id", "conversation_index", "inference_classification", "flag", "created_date_time", "internet_message_headers")
    class EmailUserDetails(_message.Message):
        __slots__ = ("email_address",)
        class EmailAddress(_message.Message):
            __slots__ = ("name", "address")
            NAME_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            name: str
            address: str
            def __init__(self, name: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        email_address: EmailItem.EmailUserDetails.EmailAddress
        def __init__(self, email_address: _Optional[_Union[EmailItem.EmailUserDetails.EmailAddress, _Mapping]] = ...) -> None: ...
    class MailBody(_message.Message):
        __slots__ = ("content", "content_type")
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        content: str
        content_type: str
        def __init__(self, content: _Optional[str] = ..., content_type: _Optional[str] = ...) -> None: ...
    class DateTimeTZone(_message.Message):
        __slots__ = ("date_time", "time_zone")
        DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
        date_time: str
        time_zone: str
        def __init__(self, date_time: _Optional[str] = ..., time_zone: _Optional[str] = ...) -> None: ...
    class Flag(_message.Message):
        __slots__ = ("completed_date_time", "due_date_time", "start_date_time", "flag_status")
        COMPLETED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        DUE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        FLAG_STATUS_FIELD_NUMBER: _ClassVar[int]
        completed_date_time: EmailItem.DateTimeTZone
        due_date_time: EmailItem.DateTimeTZone
        start_date_time: EmailItem.DateTimeTZone
        flag_status: str
        def __init__(self, completed_date_time: _Optional[_Union[EmailItem.DateTimeTZone, _Mapping]] = ..., due_date_time: _Optional[_Union[EmailItem.DateTimeTZone, _Mapping]] = ..., start_date_time: _Optional[_Union[EmailItem.DateTimeTZone, _Mapping]] = ..., flag_status: _Optional[str] = ...) -> None: ...
    class InternetMessageHeaders(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TO_RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    CC_RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    BCC_RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    SENT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    IS_DRAFT_FIELD_NUMBER: _ClassVar[int]
    WEBLINK_FIELD_NUMBER: _ClassVar[int]
    CHANGEKEY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    INTERNET_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELIVERY_RECEIPT_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    IS_READ_RECEIPT_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    BODY_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    INTERNET_MESSAGE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    subject: str
    sender: EmailItem.EmailUserDetails
    to_recipient_vec: _containers.RepeatedCompositeFieldContainer[EmailItem.EmailUserDetails]
    cc_recipient_vec: _containers.RepeatedCompositeFieldContainer[EmailItem.EmailUserDetails]
    bcc_recipient_vec: _containers.RepeatedCompositeFieldContainer[EmailItem.EmailUserDetails]
    sent_date_time: str
    received_date_time: str
    parent_folder_id: str
    has_attachments: bool
    reply_to_vec: _containers.RepeatedCompositeFieldContainer[EmailItem.EmailUserDetails]
    is_read: bool
    is_draft: bool
    weblink: str
    changekey: str
    last_modified_date_time: str
    categories: _containers.RepeatedScalarFieldContainer[str]
    internet_message_id: str
    is_delivery_receipt_requested: bool
    is_read_receipt_requested: bool
    body_preview: str
    importance: str
    conversation_id: str
    conversation_index: str
    inference_classification: str
    flag: EmailItem.Flag
    created_date_time: str
    internet_message_headers: EmailItem.InternetMessageHeaders
    def __init__(self, id: _Optional[str] = ..., subject: _Optional[str] = ..., sender: _Optional[_Union[EmailItem.EmailUserDetails, _Mapping]] = ..., to_recipient_vec: _Optional[_Iterable[_Union[EmailItem.EmailUserDetails, _Mapping]]] = ..., cc_recipient_vec: _Optional[_Iterable[_Union[EmailItem.EmailUserDetails, _Mapping]]] = ..., bcc_recipient_vec: _Optional[_Iterable[_Union[EmailItem.EmailUserDetails, _Mapping]]] = ..., sent_date_time: _Optional[str] = ..., received_date_time: _Optional[str] = ..., parent_folder_id: _Optional[str] = ..., has_attachments: bool = ..., reply_to_vec: _Optional[_Iterable[_Union[EmailItem.EmailUserDetails, _Mapping]]] = ..., is_read: bool = ..., is_draft: bool = ..., weblink: _Optional[str] = ..., changekey: _Optional[str] = ..., last_modified_date_time: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ..., internet_message_id: _Optional[str] = ..., is_delivery_receipt_requested: bool = ..., is_read_receipt_requested: bool = ..., body_preview: _Optional[str] = ..., importance: _Optional[str] = ..., conversation_id: _Optional[str] = ..., conversation_index: _Optional[str] = ..., inference_classification: _Optional[str] = ..., flag: _Optional[_Union[EmailItem.Flag, _Mapping]] = ..., created_date_time: _Optional[str] = ..., internet_message_headers: _Optional[_Union[EmailItem.InternetMessageHeaders, _Mapping]] = ..., **kwargs) -> None: ...

class O365ErroredFileInfo(_message.Message):
    __slots__ = ("file_path", "error_message")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    error_message: str
    def __init__(self, file_path: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class SharePointAdminPortalSiteInfo(_message.Message):
    __slots__ = ("title", "group_id", "hub_site_id", "num_of_files", "site_id", "site_url", "storage_quota", "storage_used", "storage_used_percentage", "template_name", "related_group_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_SITE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_FILES_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_URL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_QUOTA_FIELD_NUMBER: _ClassVar[int]
    STORAGE_USED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_USED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    group_id: str
    hub_site_id: str
    num_of_files: int
    site_id: str
    site_url: str
    storage_quota: float
    storage_used: float
    storage_used_percentage: float
    template_name: str
    related_group_id: str
    def __init__(self, title: _Optional[str] = ..., group_id: _Optional[str] = ..., hub_site_id: _Optional[str] = ..., num_of_files: _Optional[int] = ..., site_id: _Optional[str] = ..., site_url: _Optional[str] = ..., storage_quota: _Optional[float] = ..., storage_used: _Optional[float] = ..., storage_used_percentage: _Optional[float] = ..., template_name: _Optional[str] = ..., related_group_id: _Optional[str] = ...) -> None: ...

class Chat(_message.Message):
    __slots__ = ("id", "topic", "creation_date_time", "last_updated_date_time", "chat_type", "chat_type_str", "web_url", "tenant_id", "online_meeting_info", "viewpoint", "members", "cohesity_file_name", "online_meeting_details", "odata_context", "members_odata_context")
    class ChatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kOneOnOne: _ClassVar[Chat.ChatType]
        kGroup: _ClassVar[Chat.ChatType]
        kMeeting: _ClassVar[Chat.ChatType]
        kUnknownFutureValue: _ClassVar[Chat.ChatType]
    kOneOnOne: Chat.ChatType
    kGroup: Chat.ChatType
    kMeeting: Chat.ChatType
    kUnknownFutureValue: Chat.ChatType
    class Viewpoint(_message.Message):
        __slots__ = ("is_hidden", "last_message_read_date_time")
        IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
        LAST_MESSAGE_READ_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
        is_hidden: bool
        last_message_read_date_time: str
        def __init__(self, is_hidden: bool = ..., last_message_read_date_time: _Optional[str] = ...) -> None: ...
    class OnlineMeetingInfo(_message.Message):
        __slots__ = ("calendar_event_id", "join_web_url", "organizer")
        class Organizer(_message.Message):
            __slots__ = ("id", "display_name", "user_identity_type")
            ID_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            USER_IDENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
            id: str
            display_name: str
            user_identity_type: str
            def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., user_identity_type: _Optional[str] = ...) -> None: ...
        CALENDAR_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
        JOIN_WEB_URL_FIELD_NUMBER: _ClassVar[int]
        ORGANIZER_FIELD_NUMBER: _ClassVar[int]
        calendar_event_id: str
        join_web_url: str
        organizer: Chat.OnlineMeetingInfo.Organizer
        def __init__(self, calendar_event_id: _Optional[str] = ..., join_web_url: _Optional[str] = ..., organizer: _Optional[_Union[Chat.OnlineMeetingInfo.Organizer, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CHAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_TYPE_STR_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_MEETING_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEWPOINT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    COHESITY_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_MEETING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ODATA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_ODATA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    topic: str
    creation_date_time: str
    last_updated_date_time: str
    chat_type: Chat.ChatType
    chat_type_str: str
    web_url: str
    tenant_id: str
    online_meeting_info: str
    viewpoint: Chat.Viewpoint
    members: _containers.RepeatedCompositeFieldContainer[MemberDetails]
    cohesity_file_name: str
    online_meeting_details: Chat.OnlineMeetingInfo
    odata_context: str
    members_odata_context: str
    def __init__(self, id: _Optional[str] = ..., topic: _Optional[str] = ..., creation_date_time: _Optional[str] = ..., last_updated_date_time: _Optional[str] = ..., chat_type: _Optional[_Union[Chat.ChatType, str]] = ..., chat_type_str: _Optional[str] = ..., web_url: _Optional[str] = ..., tenant_id: _Optional[str] = ..., online_meeting_info: _Optional[str] = ..., viewpoint: _Optional[_Union[Chat.Viewpoint, _Mapping]] = ..., members: _Optional[_Iterable[_Union[MemberDetails, _Mapping]]] = ..., cohesity_file_name: _Optional[str] = ..., online_meeting_details: _Optional[_Union[Chat.OnlineMeetingInfo, _Mapping]] = ..., odata_context: _Optional[str] = ..., members_odata_context: _Optional[str] = ...) -> None: ...
