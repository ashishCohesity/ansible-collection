from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kActionNone: _ClassVar[PermissionActionType]
    kOwned: _ClassVar[PermissionActionType]
    kAll: _ClassVar[PermissionActionType]

class PermissionLevelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNone: _ClassVar[PermissionLevelType]
    kOwner: _ClassVar[PermissionLevelType]
    kPublishingEditor: _ClassVar[PermissionLevelType]
    kEditor: _ClassVar[PermissionLevelType]
    kPublishingAuthor: _ClassVar[PermissionLevelType]
    kAuthor: _ClassVar[PermissionLevelType]
    kNoneditingAuthor: _ClassVar[PermissionLevelType]
    kReviewer: _ClassVar[PermissionLevelType]
    kContributor: _ClassVar[PermissionLevelType]
    kCustom: _ClassVar[PermissionLevelType]

class PermissionReadAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kReadNone: _ClassVar[PermissionReadAccessType]
    kFullDetails: _ClassVar[PermissionReadAccessType]

class DistinguishedUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDefault: _ClassVar[DistinguishedUserType]
    kAnonymous: _ClassVar[DistinguishedUserType]
kActionNone: PermissionActionType
kOwned: PermissionActionType
kAll: PermissionActionType
kNone: PermissionLevelType
kOwner: PermissionLevelType
kPublishingEditor: PermissionLevelType
kEditor: PermissionLevelType
kPublishingAuthor: PermissionLevelType
kAuthor: PermissionLevelType
kNoneditingAuthor: PermissionLevelType
kReviewer: PermissionLevelType
kContributor: PermissionLevelType
kCustom: PermissionLevelType
kReadNone: PermissionReadAccessType
kFullDetails: PermissionReadAccessType
kDefault: DistinguishedUserType
kAnonymous: DistinguishedUserType

class FolderRootType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kMsgFolderRoot: _ClassVar[FolderRootType.Type]
        kArchiveMsgFolderRoot: _ClassVar[FolderRootType.Type]
        kRecoverableItemsFolderRoot: _ClassVar[FolderRootType.Type]
        kArchiveRecoverableItemsFolderRoot: _ClassVar[FolderRootType.Type]
    kMsgFolderRoot: FolderRootType.Type
    kArchiveMsgFolderRoot: FolderRootType.Type
    kRecoverableItemsFolderRoot: FolderRootType.Type
    kArchiveRecoverableItemsFolderRoot: FolderRootType.Type
    def __init__(self) -> None: ...

class FolderType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEmailMessages: _ClassVar[FolderType.Type]
        kCalendar: _ClassVar[FolderType.Type]
        kContacts: _ClassVar[FolderType.Type]
        kSearch: _ClassVar[FolderType.Type]
        kTasks: _ClassVar[FolderType.Type]
        kFolder: _ClassVar[FolderType.Type]
    kEmailMessages: FolderType.Type
    kCalendar: FolderType.Type
    kContacts: FolderType.Type
    kSearch: FolderType.Type
    kTasks: FolderType.Type
    kFolder: FolderType.Type
    def __init__(self) -> None: ...

class ItemType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kEmailMessage: _ClassVar[ItemType.Type]
        kCalendar: _ClassVar[ItemType.Type]
        kTask: _ClassVar[ItemType.Type]
        kContact: _ClassVar[ItemType.Type]
        kItem: _ClassVar[ItemType.Type]
        kSharingMessage: _ClassVar[ItemType.Type]
        kMeetingMessage: _ClassVar[ItemType.Type]
        kMeetingRequest: _ClassVar[ItemType.Type]
        kMeetingResponse: _ClassVar[ItemType.Type]
        kMeetingCancellation: _ClassVar[ItemType.Type]
        kPostItem: _ClassVar[ItemType.Type]
        kRoleMember: _ClassVar[ItemType.Type]
        kNetwork: _ClassVar[ItemType.Type]
        kPerson: _ClassVar[ItemType.Type]
        kDistributionList: _ClassVar[ItemType.Type]
    kEmailMessage: ItemType.Type
    kCalendar: ItemType.Type
    kTask: ItemType.Type
    kContact: ItemType.Type
    kItem: ItemType.Type
    kSharingMessage: ItemType.Type
    kMeetingMessage: ItemType.Type
    kMeetingRequest: ItemType.Type
    kMeetingResponse: ItemType.Type
    kMeetingCancellation: ItemType.Type
    kPostItem: ItemType.Type
    kRoleMember: ItemType.Type
    kNetwork: ItemType.Type
    kPerson: ItemType.Type
    kDistributionList: ItemType.Type
    def __init__(self) -> None: ...

class User(_message.Message):
    __slots__ = ("email_address", "name")
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    name: str
    def __init__(self, email_address: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AttachmentType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kFile: _ClassVar[AttachmentType.Type]
        kItem: _ClassVar[AttachmentType.Type]
        kReference: _ClassVar[AttachmentType.Type]
    kFile: AttachmentType.Type
    kItem: AttachmentType.Type
    kReference: AttachmentType.Type
    def __init__(self) -> None: ...

class Attachment(_message.Message):
    __slots__ = ("id", "type", "name", "content_type", "size_bytes", "inline")
    Extensions: _python_message._ExtensionDict
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    INLINE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: AttachmentType.Type
    name: str
    content_type: str
    size_bytes: int
    inline: bool
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[AttachmentType.Type, str]] = ..., name: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., inline: bool = ...) -> None: ...

class ItemMetaData(_message.Message):
    __slots__ = ("id", "type", "parent_folder_id", "has_attachments", "to_recipient_vec", "cc_recipient_vec", "bcc_recipient_vec", "sent_time", "received_time", "attachment_vec", "change_key", "size", "subject", "item_class", "metadata_parent_folder_id", "creation_time", "sensitivity", "importance", "last_modified_name", "last_modified_time", "organizer", "required_attendees_vec", "optional_attendees_vec", "is_recurring", "start_time", "end_time", "first_occurrence", "last_occurrence", "recurrence_pattern", "first_name", "middle_name", "last_name", "birthday", "email_addresses_vec", "owner", "due_date", "completion_date", "task_status", "sha_256_checksum")
    class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNormal: _ClassVar[ItemMetaData.Sensitivity]
        kPersonal: _ClassVar[ItemMetaData.Sensitivity]
        kPrivate: _ClassVar[ItemMetaData.Sensitivity]
        kConfidential: _ClassVar[ItemMetaData.Sensitivity]
    kNormal: ItemMetaData.Sensitivity
    kPersonal: ItemMetaData.Sensitivity
    kPrivate: ItemMetaData.Sensitivity
    kConfidential: ItemMetaData.Sensitivity
    class Importance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLowImportance: _ClassVar[ItemMetaData.Importance]
        kNormalImportance: _ClassVar[ItemMetaData.Importance]
        kHighImportance: _ClassVar[ItemMetaData.Importance]
    kLowImportance: ItemMetaData.Importance
    kNormalImportance: ItemMetaData.Importance
    kHighImportance: ItemMetaData.Importance
    class RecurrencePattern(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ItemMetaData.RecurrencePattern]
        kYearly: _ClassVar[ItemMetaData.RecurrencePattern]
        kMonthly: _ClassVar[ItemMetaData.RecurrencePattern]
        kWeekly: _ClassVar[ItemMetaData.RecurrencePattern]
        kDaily: _ClassVar[ItemMetaData.RecurrencePattern]
    kNone: ItemMetaData.RecurrencePattern
    kYearly: ItemMetaData.RecurrencePattern
    kMonthly: ItemMetaData.RecurrencePattern
    kWeekly: ItemMetaData.RecurrencePattern
    kDaily: ItemMetaData.RecurrencePattern
    class TaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNotStarted: _ClassVar[ItemMetaData.TaskStatus]
        kInProgress: _ClassVar[ItemMetaData.TaskStatus]
        kCompleted: _ClassVar[ItemMetaData.TaskStatus]
        kWaitingOnOthers: _ClassVar[ItemMetaData.TaskStatus]
        kDeferred: _ClassVar[ItemMetaData.TaskStatus]
    kNotStarted: ItemMetaData.TaskStatus
    kInProgress: ItemMetaData.TaskStatus
    kCompleted: ItemMetaData.TaskStatus
    kWaitingOnOthers: ItemMetaData.TaskStatus
    kDeferred: ItemMetaData.TaskStatus
    class Occurrence(_message.Message):
        __slots__ = ("start_time", "end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: int
        end_time: int
        def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    CC_RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    BCC_RECIPIENT_VEC_FIELD_NUMBER: _ClassVar[int]
    SENT_TIME_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    CHANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ITEM_CLASS_FIELD_NUMBER: _ClassVar[int]
    METADATA_PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZER_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ATTENDEES_VEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ATTENDEES_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_RECURRING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FIRST_OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    LAST_OCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_DATE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATUS_FIELD_NUMBER: _ClassVar[int]
    SHA_256_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: ItemType.Type
    parent_folder_id: str
    has_attachments: bool
    to_recipient_vec: _containers.RepeatedCompositeFieldContainer[User]
    cc_recipient_vec: _containers.RepeatedCompositeFieldContainer[User]
    bcc_recipient_vec: _containers.RepeatedCompositeFieldContainer[User]
    sent_time: int
    received_time: int
    attachment_vec: _containers.RepeatedCompositeFieldContainer[Attachment]
    change_key: str
    size: int
    subject: str
    item_class: str
    metadata_parent_folder_id: str
    creation_time: int
    sensitivity: ItemMetaData.Sensitivity
    importance: ItemMetaData.Importance
    last_modified_name: str
    last_modified_time: int
    organizer: User
    required_attendees_vec: _containers.RepeatedCompositeFieldContainer[User]
    optional_attendees_vec: _containers.RepeatedCompositeFieldContainer[User]
    is_recurring: bool
    start_time: int
    end_time: int
    first_occurrence: ItemMetaData.Occurrence
    last_occurrence: ItemMetaData.Occurrence
    recurrence_pattern: ItemMetaData.RecurrencePattern
    first_name: str
    middle_name: str
    last_name: str
    birthday: int
    email_addresses_vec: _containers.RepeatedScalarFieldContainer[str]
    owner: str
    due_date: int
    completion_date: int
    task_status: ItemMetaData.TaskStatus
    sha_256_checksum: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[ItemType.Type, str]] = ..., parent_folder_id: _Optional[str] = ..., has_attachments: bool = ..., to_recipient_vec: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., cc_recipient_vec: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., bcc_recipient_vec: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., sent_time: _Optional[int] = ..., received_time: _Optional[int] = ..., attachment_vec: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., change_key: _Optional[str] = ..., size: _Optional[int] = ..., subject: _Optional[str] = ..., item_class: _Optional[str] = ..., metadata_parent_folder_id: _Optional[str] = ..., creation_time: _Optional[int] = ..., sensitivity: _Optional[_Union[ItemMetaData.Sensitivity, str]] = ..., importance: _Optional[_Union[ItemMetaData.Importance, str]] = ..., last_modified_name: _Optional[str] = ..., last_modified_time: _Optional[int] = ..., organizer: _Optional[_Union[User, _Mapping]] = ..., required_attendees_vec: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., optional_attendees_vec: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., is_recurring: bool = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., first_occurrence: _Optional[_Union[ItemMetaData.Occurrence, _Mapping]] = ..., last_occurrence: _Optional[_Union[ItemMetaData.Occurrence, _Mapping]] = ..., recurrence_pattern: _Optional[_Union[ItemMetaData.RecurrencePattern, str]] = ..., first_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., last_name: _Optional[str] = ..., birthday: _Optional[int] = ..., email_addresses_vec: _Optional[_Iterable[str]] = ..., owner: _Optional[str] = ..., due_date: _Optional[int] = ..., completion_date: _Optional[int] = ..., task_status: _Optional[_Union[ItemMetaData.TaskStatus, str]] = ..., sha_256_checksum: _Optional[str] = ..., **kwargs) -> None: ...

class PropertyType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBinary: _ClassVar[PropertyType.Type]
        kBoolean: _ClassVar[PropertyType.Type]
        kString: _ClassVar[PropertyType.Type]
        kLong: _ClassVar[PropertyType.Type]
    kBinary: PropertyType.Type
    kBoolean: PropertyType.Type
    kString: PropertyType.Type
    kLong: PropertyType.Type
    def __init__(self) -> None: ...

class FolderId(_message.Message):
    __slots__ = ("id", "change_key", "replica_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_KEY_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    change_key: str
    replica_id: str
    def __init__(self, id: _Optional[str] = ..., change_key: _Optional[str] = ..., replica_id: _Optional[str] = ...) -> None: ...

class ExtendedFieldURI(_message.Message):
    __slots__ = ("property_tag", "property_type")
    PROPERTY_TAG_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    property_tag: str
    property_type: PropertyType.Type
    def __init__(self, property_tag: _Optional[str] = ..., property_type: _Optional[_Union[PropertyType.Type, str]] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ("sid", "primary_smtp_address", "display_name", "distinguished_user", "external_user_identity")
    SID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_USER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_USER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    sid: str
    primary_smtp_address: str
    display_name: str
    distinguished_user: DistinguishedUserType
    external_user_identity: str
    def __init__(self, sid: _Optional[str] = ..., primary_smtp_address: _Optional[str] = ..., display_name: _Optional[str] = ..., distinguished_user: _Optional[_Union[DistinguishedUserType, str]] = ..., external_user_identity: _Optional[str] = ...) -> None: ...

class Permission(_message.Message):
    __slots__ = ("can_create_items", "can_create_sub_folders", "is_folder_owner", "is_folder_visible", "is_folder_contact", "edit_items", "delete_items", "permission_level", "read_items", "user_id")
    CAN_CREATE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_SUB_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    IS_FOLDER_OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_FOLDER_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    IS_FOLDER_CONTACT_FIELD_NUMBER: _ClassVar[int]
    EDIT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    DELETE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    READ_ITEMS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    can_create_items: bool
    can_create_sub_folders: bool
    is_folder_owner: bool
    is_folder_visible: bool
    is_folder_contact: bool
    edit_items: PermissionActionType
    delete_items: PermissionActionType
    permission_level: PermissionLevelType
    read_items: PermissionReadAccessType
    user_id: UserId
    def __init__(self, can_create_items: bool = ..., can_create_sub_folders: bool = ..., is_folder_owner: bool = ..., is_folder_visible: bool = ..., is_folder_contact: bool = ..., edit_items: _Optional[_Union[PermissionActionType, str]] = ..., delete_items: _Optional[_Union[PermissionActionType, str]] = ..., permission_level: _Optional[_Union[PermissionLevelType, str]] = ..., read_items: _Optional[_Union[PermissionReadAccessType, str]] = ..., user_id: _Optional[_Union[UserId, _Mapping]] = ...) -> None: ...

class PermissionSet(_message.Message):
    __slots__ = ("permissions", "unknown_entries")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    unknown_entries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ..., unknown_entries: _Optional[_Iterable[str]] = ...) -> None: ...

class FolderContentInfo(_message.Message):
    __slots__ = ("display_name", "parent_folder_id", "total_count", "unread_count", "child_folder_count", "permission_set", "folder_id", "folder_class", "sync_state", "extended_property_vec", "type")
    class ExtendedProperty(_message.Message):
        __slots__ = ("extended_field_uri", "value")
        EXTENDED_FIELD_URI_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        extended_field_uri: ExtendedFieldURI
        value: str
        def __init__(self, extended_field_uri: _Optional[_Union[ExtendedFieldURI, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHILD_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_SET_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_CLASS_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    parent_folder_id: FolderId
    total_count: int
    unread_count: int
    child_folder_count: int
    permission_set: PermissionSet
    folder_id: FolderId
    folder_class: str
    sync_state: str
    extended_property_vec: _containers.RepeatedCompositeFieldContainer[FolderContentInfo.ExtendedProperty]
    type: FolderType.Type
    def __init__(self, display_name: _Optional[str] = ..., parent_folder_id: _Optional[_Union[FolderId, _Mapping]] = ..., total_count: _Optional[int] = ..., unread_count: _Optional[int] = ..., child_folder_count: _Optional[int] = ..., permission_set: _Optional[_Union[PermissionSet, _Mapping]] = ..., folder_id: _Optional[_Union[FolderId, _Mapping]] = ..., folder_class: _Optional[str] = ..., sync_state: _Optional[str] = ..., extended_property_vec: _Optional[_Iterable[_Union[FolderContentInfo.ExtendedProperty, _Mapping]]] = ..., type: _Optional[_Union[FolderType.Type, str]] = ...) -> None: ...
