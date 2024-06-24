from magneto.api.common import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("type", "uuid", "name", "description", "graph_uuid", "use_alternate_uuid_as_hash_string", "entity_mailbox_enabled", "entity_mailbox_enabled_atleast_once", "entity_archive_mailbox_enabled", "mailbox_id", "primary_smtp_address", "user_principal_name", "entity_mailbox_size", "entity_mailbox_type", "entity_one_drive_enabled", "entity_one_drive_enabled_atleast_once", "drive_id", "entity_one_drive_size", "department", "city", "country", "designation", "membership_info_vec", "proxy_entity_id_vec", "web_url", "group_params", "site_params", "team_params", "sharepoint_domain_name", "pst_download_option_expiry_time_secs", "front_end_size_info", "attribute_map")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kDomain: _ClassVar[Entity.Type]
        kOutlook: _ClassVar[Entity.Type]
        kMailbox: _ClassVar[Entity.Type]
        kUsers: _ClassVar[Entity.Type]
        kGroups: _ClassVar[Entity.Type]
        kSites: _ClassVar[Entity.Type]
        kUser: _ClassVar[Entity.Type]
        kGroup: _ClassVar[Entity.Type]
        kSite: _ClassVar[Entity.Type]
        kApplication: _ClassVar[Entity.Type]
        kGraphUser: _ClassVar[Entity.Type]
        kPublicFolders: _ClassVar[Entity.Type]
        kPublicFolder: _ClassVar[Entity.Type]
        kTeams: _ClassVar[Entity.Type]
        kTeam: _ClassVar[Entity.Type]
        kRootPublicFolder: _ClassVar[Entity.Type]
        kO365Exchange: _ClassVar[Entity.Type]
        kO365OneDrive: _ClassVar[Entity.Type]
        kO365Sharepoint: _ClassVar[Entity.Type]
    kDomain: Entity.Type
    kOutlook: Entity.Type
    kMailbox: Entity.Type
    kUsers: Entity.Type
    kGroups: Entity.Type
    kSites: Entity.Type
    kUser: Entity.Type
    kGroup: Entity.Type
    kSite: Entity.Type
    kApplication: Entity.Type
    kGraphUser: Entity.Type
    kPublicFolders: Entity.Type
    kPublicFolder: Entity.Type
    kTeams: Entity.Type
    kTeam: Entity.Type
    kRootPublicFolder: Entity.Type
    kO365Exchange: Entity.Type
    kO365OneDrive: Entity.Type
    kO365Sharepoint: Entity.Type
    class MailBoxType(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUserMailbox: _ClassVar[Entity.MailBoxType.Type]
            kSharedMailbox: _ClassVar[Entity.MailBoxType.Type]
            kLinkedMailbox: _ClassVar[Entity.MailBoxType.Type]
            kRoomMailbox: _ClassVar[Entity.MailBoxType.Type]
            kEquipmentMailbox: _ClassVar[Entity.MailBoxType.Type]
        kUserMailbox: Entity.MailBoxType.Type
        kSharedMailbox: Entity.MailBoxType.Type
        kLinkedMailbox: Entity.MailBoxType.Type
        kRoomMailbox: Entity.MailBoxType.Type
        kEquipmentMailbox: Entity.MailBoxType.Type
        def __init__(self) -> None: ...
    class GroupMembershipInfo(_message.Message):
        __slots__ = ("group_entity_id", "group_graph_uuid")
        GROUP_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_GRAPH_UUID_FIELD_NUMBER: _ClassVar[int]
        group_entity_id: int
        group_graph_uuid: str
        def __init__(self, group_entity_id: _Optional[int] = ..., group_graph_uuid: _Optional[str] = ...) -> None: ...
    class GroupParams(_message.Message):
        __slots__ = ("visibility", "resource_provisioning_options", "mail_enabled", "security_enabled", "group_type_vec", "site_id", "num_members")
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_PROVISIONING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        MAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SECURITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        GROUP_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
        SITE_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        visibility: str
        resource_provisioning_options: _containers.RepeatedScalarFieldContainer[str]
        mail_enabled: bool
        security_enabled: bool
        group_type_vec: _containers.RepeatedScalarFieldContainer[str]
        site_id: str
        num_members: int
        def __init__(self, visibility: _Optional[str] = ..., resource_provisioning_options: _Optional[_Iterable[str]] = ..., mail_enabled: bool = ..., security_enabled: bool = ..., group_type_vec: _Optional[_Iterable[str]] = ..., site_id: _Optional[str] = ..., num_members: _Optional[int] = ...) -> None: ...
    class SiteParams(_message.Message):
        __slots__ = ("is_group_site", "is_team_site", "is_private_channel_site")
        IS_GROUP_SITE_FIELD_NUMBER: _ClassVar[int]
        IS_TEAM_SITE_FIELD_NUMBER: _ClassVar[int]
        IS_PRIVATE_CHANNEL_SITE_FIELD_NUMBER: _ClassVar[int]
        is_group_site: bool
        is_team_site: bool
        is_private_channel_site: bool
        def __init__(self, is_group_site: bool = ..., is_team_site: bool = ..., is_private_channel_site: bool = ...) -> None: ...
    class TeamParams(_message.Message):
        __slots__ = ("site_id", "num_members", "channel_count")
        SITE_ID_FIELD_NUMBER: _ClassVar[int]
        NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        site_id: str
        num_members: int
        channel_count: int
        def __init__(self, site_id: _Optional[str] = ..., num_members: _Optional[int] = ..., channel_count: _Optional[int] = ...) -> None: ...
    class AttributeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GRAPH_UUID_FIELD_NUMBER: _ClassVar[int]
    USE_ALTERNATE_UUID_AS_HASH_STRING_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MAILBOX_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MAILBOX_ENABLED_ATLEAST_ONCE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ARCHIVE_MAILBOX_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_PRINCIPAL_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MAILBOX_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MAILBOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ONE_DRIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ONE_DRIVE_ENABLED_ATLEAST_ONCE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ONE_DRIVE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DESIGNATION_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PROXY_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    WEB_URL_FIELD_NUMBER: _ClassVar[int]
    GROUP_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SITE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TEAM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SHAREPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    PST_DOWNLOAD_OPTION_EXPIRY_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    FRONT_END_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_MAP_FIELD_NUMBER: _ClassVar[int]
    type: Entity.Type
    uuid: str
    name: str
    description: str
    graph_uuid: str
    use_alternate_uuid_as_hash_string: bool
    entity_mailbox_enabled: bool
    entity_mailbox_enabled_atleast_once: bool
    entity_archive_mailbox_enabled: bool
    mailbox_id: str
    primary_smtp_address: str
    user_principal_name: str
    entity_mailbox_size: int
    entity_mailbox_type: Entity.MailBoxType.Type
    entity_one_drive_enabled: bool
    entity_one_drive_enabled_atleast_once: bool
    drive_id: str
    entity_one_drive_size: int
    department: str
    city: str
    country: str
    designation: str
    membership_info_vec: _containers.RepeatedCompositeFieldContainer[Entity.GroupMembershipInfo]
    proxy_entity_id_vec: _containers.RepeatedScalarFieldContainer[int]
    web_url: str
    group_params: Entity.GroupParams
    site_params: Entity.SiteParams
    team_params: Entity.TeamParams
    sharepoint_domain_name: str
    pst_download_option_expiry_time_secs: int
    front_end_size_info: _stats_pb2.SizeInfo
    attribute_map: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[_Union[Entity.Type, str]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., graph_uuid: _Optional[str] = ..., use_alternate_uuid_as_hash_string: bool = ..., entity_mailbox_enabled: bool = ..., entity_mailbox_enabled_atleast_once: bool = ..., entity_archive_mailbox_enabled: bool = ..., mailbox_id: _Optional[str] = ..., primary_smtp_address: _Optional[str] = ..., user_principal_name: _Optional[str] = ..., entity_mailbox_size: _Optional[int] = ..., entity_mailbox_type: _Optional[_Union[Entity.MailBoxType.Type, str]] = ..., entity_one_drive_enabled: bool = ..., entity_one_drive_enabled_atleast_once: bool = ..., drive_id: _Optional[str] = ..., entity_one_drive_size: _Optional[int] = ..., department: _Optional[str] = ..., city: _Optional[str] = ..., country: _Optional[str] = ..., designation: _Optional[str] = ..., membership_info_vec: _Optional[_Iterable[_Union[Entity.GroupMembershipInfo, _Mapping]]] = ..., proxy_entity_id_vec: _Optional[_Iterable[int]] = ..., web_url: _Optional[str] = ..., group_params: _Optional[_Union[Entity.GroupParams, _Mapping]] = ..., site_params: _Optional[_Union[Entity.SiteParams, _Mapping]] = ..., team_params: _Optional[_Union[Entity.TeamParams, _Mapping]] = ..., sharepoint_domain_name: _Optional[str] = ..., pst_download_option_expiry_time_secs: _Optional[int] = ..., front_end_size_info: _Optional[_Union[_stats_pb2.SizeInfo, _Mapping]] = ..., attribute_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
