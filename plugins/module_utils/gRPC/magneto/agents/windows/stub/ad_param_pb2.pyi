from magneto.agents.base import error_pb2 as _error_pb2
from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import ad_pb2 as _ad_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetADHierarchyArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetADHierarchyResult(_message.Message):
    __slots__ = ("dc",)
    DC_FIELD_NUMBER: _ClassVar[int]
    dc: _ad_pb2.ADDomainController
    def __init__(self, dc: _Optional[_Union[_ad_pb2.ADDomainController, _Mapping]] = ...) -> None: ...

class MountADSnapshotDatabaseArg(_message.Message):
    __slots__ = ("db_file_path", "is_adam_database", "ldap_port", "allow_nonadmin_access", "allow_upgrade")
    DB_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_ADAM_DATABASE_FIELD_NUMBER: _ClassVar[int]
    LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NONADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    db_file_path: str
    is_adam_database: bool
    ldap_port: int
    allow_nonadmin_access: bool
    allow_upgrade: bool
    def __init__(self, db_file_path: _Optional[str] = ..., is_adam_database: bool = ..., ldap_port: _Optional[int] = ..., allow_nonadmin_access: bool = ..., allow_upgrade: bool = ...) -> None: ...

class MountADSnapshotDatabaseResult(_message.Message):
    __slots__ = ("dsamain_proc_id",)
    DSAMAIN_PROC_ID_FIELD_NUMBER: _ClassVar[int]
    dsamain_proc_id: int
    def __init__(self, dsamain_proc_id: _Optional[int] = ...) -> None: ...

class UnmountADSnapshotDatabaseArg(_message.Message):
    __slots__ = ("db_file_path", "dsamain_proc_id")
    DB_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DSAMAIN_PROC_ID_FIELD_NUMBER: _ClassVar[int]
    db_file_path: str
    dsamain_proc_id: int
    def __init__(self, db_file_path: _Optional[str] = ..., dsamain_proc_id: _Optional[int] = ...) -> None: ...

class UnmountADSnapshotDatabaseResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ADServerEndpoint(_message.Message):
    __slots__ = ("host", "ldap_port")
    HOST_FIELD_NUMBER: _ClassVar[int]
    LDAP_PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    ldap_port: int
    def __init__(self, host: _Optional[str] = ..., ldap_port: _Optional[int] = ...) -> None: ...

class ADGuidPair(_message.Message):
    __slots__ = ("source", "destination")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    source: str
    destination: str
    def __init__(self, source: _Optional[str] = ..., destination: _Optional[str] = ...) -> None: ...

class ADConnectionParam(_message.Message):
    __slots__ = ("source_server", "dest_server", "credentials")
    SOURCE_SERVER_FIELD_NUMBER: _ClassVar[int]
    DEST_SERVER_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    source_server: ADServerEndpoint
    dest_server: ADServerEndpoint
    credentials: _credentials_pb2.Credentials
    def __init__(self, source_server: _Optional[_Union[ADServerEndpoint, _Mapping]] = ..., dest_server: _Optional[_Union[ADServerEndpoint, _Mapping]] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...

class GetADDomainRootTopologyArg(_message.Message):
    __slots__ = ("connection_param", "option_flags")
    class ADGetTopologyOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[GetADDomainRootTopologyArg.ADGetTopologyOptionFlags]
        kResolveDestination: _ClassVar[GetADDomainRootTopologyArg.ADGetTopologyOptionFlags]
    kNone: GetADDomainRootTopologyArg.ADGetTopologyOptionFlags
    kResolveDestination: GetADDomainRootTopologyArg.ADGetTopologyOptionFlags
    CONNECTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    connection_param: ADConnectionParam
    option_flags: int
    def __init__(self, connection_param: _Optional[_Union[ADConnectionParam, _Mapping]] = ..., option_flags: _Optional[int] = ...) -> None: ...

class GetADDomainRootTopologyResult(_message.Message):
    __slots__ = ("object_vec",)
    class ADRootTopologyObject(_message.Message):
        __slots__ = ("display_name", "distinguished_name", "source_guid", "dest_guid", "object_class", "description", "object_flags", "status", "child_vec")
        class ADTopologyResultFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[GetADDomainRootTopologyResult.ADRootTopologyObject.ADTopologyResultFlags]
        kNone: GetADDomainRootTopologyResult.ADRootTopologyObject.ADTopologyResultFlags
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_GUID_FIELD_NUMBER: _ClassVar[int]
        DEST_GUID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FLAGS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CHILD_VEC_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        distinguished_name: str
        source_guid: str
        dest_guid: str
        object_class: str
        description: str
        object_flags: int
        status: _error_pb2.ErrorProto
        child_vec: _containers.RepeatedCompositeFieldContainer[GetADDomainRootTopologyResult.ADRootTopologyObject]
        def __init__(self, display_name: _Optional[str] = ..., distinguished_name: _Optional[str] = ..., source_guid: _Optional[str] = ..., dest_guid: _Optional[str] = ..., object_class: _Optional[str] = ..., description: _Optional[str] = ..., object_flags: _Optional[int] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., child_vec: _Optional[_Iterable[_Union[GetADDomainRootTopologyResult.ADRootTopologyObject, _Mapping]]] = ...) -> None: ...
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    object_vec: _containers.RepeatedCompositeFieldContainer[GetADDomainRootTopologyResult.ADRootTopologyObject]
    def __init__(self, object_vec: _Optional[_Iterable[_Union[GetADDomainRootTopologyResult.ADRootTopologyObject, _Mapping]]] = ...) -> None: ...

class SearchADObjectsArg(_message.Message):
    __slots__ = ("connection_param", "search_base_dn", "search_scope", "ldap_filter", "sort_property_name", "record_offset", "num_record", "option_flags", "partition")
    class ADSearchOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[SearchADObjectsArg.ADSearchOptionFlags]
        kSortDescending: _ClassVar[SearchADObjectsArg.ADSearchOptionFlags]
        kCompareObjects: _ClassVar[SearchADObjectsArg.ADSearchOptionFlags]
        kCompareObjectsExcludeSysProps: _ClassVar[SearchADObjectsArg.ADSearchOptionFlags]
        kCompareCaseSensitive: _ClassVar[SearchADObjectsArg.ADSearchOptionFlags]
    kNone: SearchADObjectsArg.ADSearchOptionFlags
    kSortDescending: SearchADObjectsArg.ADSearchOptionFlags
    kCompareObjects: SearchADObjectsArg.ADSearchOptionFlags
    kCompareObjectsExcludeSysProps: SearchADObjectsArg.ADSearchOptionFlags
    kCompareCaseSensitive: SearchADObjectsArg.ADSearchOptionFlags
    class SearchScope(_message.Message):
        __slots__ = ()
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kBase: _ClassVar[SearchADObjectsArg.SearchScope.Type]
            kOneLevel: _ClassVar[SearchADObjectsArg.SearchScope.Type]
            kSubtree: _ClassVar[SearchADObjectsArg.SearchScope.Type]
        kBase: SearchADObjectsArg.SearchScope.Type
        kOneLevel: SearchADObjectsArg.SearchScope.Type
        kSubtree: SearchADObjectsArg.SearchScope.Type
        def __init__(self) -> None: ...
    CONNECTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    SEARCH_BASE_DN_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    LDAP_FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    RECORD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NUM_RECORD_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    connection_param: ADConnectionParam
    search_base_dn: str
    search_scope: SearchADObjectsArg.SearchScope.Type
    ldap_filter: str
    sort_property_name: str
    record_offset: int
    num_record: int
    option_flags: int
    partition: str
    def __init__(self, connection_param: _Optional[_Union[ADConnectionParam, _Mapping]] = ..., search_base_dn: _Optional[str] = ..., search_scope: _Optional[_Union[SearchADObjectsArg.SearchScope.Type, str]] = ..., ldap_filter: _Optional[str] = ..., sort_property_name: _Optional[str] = ..., record_offset: _Optional[int] = ..., num_record: _Optional[int] = ..., option_flags: _Optional[int] = ..., partition: _Optional[str] = ...) -> None: ...

class SearchADObjectsResult(_message.Message):
    __slots__ = ("object_vec",)
    class ADObject(_message.Message):
        __slots__ = ("display_name", "distinguished_name", "source_guid", "dest_guid", "object_class", "description", "object_flags", "status", "source_prop_count", "dest_prop_count", "mismatch_prop_name")
        class ADSearchResultFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[SearchADObjectsResult.ADObject.ADSearchResultFlags]
            kEqual: _ClassVar[SearchADObjectsResult.ADObject.ADSearchResultFlags]
            kNotEqual: _ClassVar[SearchADObjectsResult.ADObject.ADSearchResultFlags]
            kRestorePasswordRequired: _ClassVar[SearchADObjectsResult.ADObject.ADSearchResultFlags]
            kMovedOnDestination: _ClassVar[SearchADObjectsResult.ADObject.ADSearchResultFlags]
            kDisableSupported: _ClassVar[SearchADObjectsResult.ADObject.ADSearchResultFlags]
        kNone: SearchADObjectsResult.ADObject.ADSearchResultFlags
        kEqual: SearchADObjectsResult.ADObject.ADSearchResultFlags
        kNotEqual: SearchADObjectsResult.ADObject.ADSearchResultFlags
        kRestorePasswordRequired: SearchADObjectsResult.ADObject.ADSearchResultFlags
        kMovedOnDestination: SearchADObjectsResult.ADObject.ADSearchResultFlags
        kDisableSupported: SearchADObjectsResult.ADObject.ADSearchResultFlags
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DISTINGUISHED_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_GUID_FIELD_NUMBER: _ClassVar[int]
        DEST_GUID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FLAGS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PROP_COUNT_FIELD_NUMBER: _ClassVar[int]
        DEST_PROP_COUNT_FIELD_NUMBER: _ClassVar[int]
        MISMATCH_PROP_NAME_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        distinguished_name: str
        source_guid: str
        dest_guid: str
        object_class: str
        description: str
        object_flags: int
        status: _error_pb2.ErrorProto
        source_prop_count: int
        dest_prop_count: int
        mismatch_prop_name: str
        def __init__(self, display_name: _Optional[str] = ..., distinguished_name: _Optional[str] = ..., source_guid: _Optional[str] = ..., dest_guid: _Optional[str] = ..., object_class: _Optional[str] = ..., description: _Optional[str] = ..., object_flags: _Optional[int] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., source_prop_count: _Optional[int] = ..., dest_prop_count: _Optional[int] = ..., mismatch_prop_name: _Optional[str] = ...) -> None: ...
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    object_vec: _containers.RepeatedCompositeFieldContainer[SearchADObjectsResult.ADObject]
    def __init__(self, object_vec: _Optional[_Iterable[_Union[SearchADObjectsResult.ADObject, _Mapping]]] = ...) -> None: ...

class CompareADObjectsArg(_message.Message):
    __slots__ = ("connection_param", "guidpair_vec", "option_flags", "truncate_multivalues")
    class ADCompareOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kExcludeSysProps: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kFilterNullValueProps: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kFilterSameValueProps: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kCaseSensitive: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kGetSourceValueForEmptyDestGuids: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kGetResolvedGuidIdentity: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
        kQuickCompare: _ClassVar[CompareADObjectsArg.ADCompareOptionFlags]
    kNone: CompareADObjectsArg.ADCompareOptionFlags
    kExcludeSysProps: CompareADObjectsArg.ADCompareOptionFlags
    kFilterNullValueProps: CompareADObjectsArg.ADCompareOptionFlags
    kFilterSameValueProps: CompareADObjectsArg.ADCompareOptionFlags
    kCaseSensitive: CompareADObjectsArg.ADCompareOptionFlags
    kGetSourceValueForEmptyDestGuids: CompareADObjectsArg.ADCompareOptionFlags
    kGetResolvedGuidIdentity: CompareADObjectsArg.ADCompareOptionFlags
    kQuickCompare: CompareADObjectsArg.ADCompareOptionFlags
    CONNECTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    GUIDPAIR_VEC_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_MULTIVALUES_FIELD_NUMBER: _ClassVar[int]
    connection_param: ADConnectionParam
    guidpair_vec: _containers.RepeatedCompositeFieldContainer[ADGuidPair]
    option_flags: int
    truncate_multivalues: int
    def __init__(self, connection_param: _Optional[_Union[ADConnectionParam, _Mapping]] = ..., guidpair_vec: _Optional[_Iterable[_Union[ADGuidPair, _Mapping]]] = ..., option_flags: _Optional[int] = ..., truncate_multivalues: _Optional[int] = ...) -> None: ...

class CompareADObjectsResult(_message.Message):
    __slots__ = ("object_vec",)
    class ADAttributeValue(_message.Message):
        __slots__ = ("value_vec", "value_flags")
        class ADAttributeValueFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags]
            kError: _ClassVar[CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags]
            kTruncated: _ClassVar[CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags]
            kCSV: _ClassVar[CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags]
        kNone: CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags
        kError: CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags
        kTruncated: CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags
        kCSV: CompareADObjectsResult.ADAttributeValue.ADAttributeValueFlags
        VALUE_VEC_FIELD_NUMBER: _ClassVar[int]
        VALUE_FLAGS_FIELD_NUMBER: _ClassVar[int]
        value_vec: _containers.RepeatedScalarFieldContainer[str]
        value_flags: int
        def __init__(self, value_vec: _Optional[_Iterable[str]] = ..., value_flags: _Optional[int] = ...) -> None: ...
    class ADAttribute(_message.Message):
        __slots__ = ("ldap_name", "source_value", "dest_value", "same_value", "attr_flags", "status")
        class ADAttributeFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[CompareADObjectsResult.ADAttribute.ADAttributeFlags]
            kEqual: _ClassVar[CompareADObjectsResult.ADAttribute.ADAttributeFlags]
            kNotEqual: _ClassVar[CompareADObjectsResult.ADAttribute.ADAttributeFlags]
            kNotFound: _ClassVar[CompareADObjectsResult.ADAttribute.ADAttributeFlags]
            kSystem: _ClassVar[CompareADObjectsResult.ADAttribute.ADAttributeFlags]
            kMultiValue: _ClassVar[CompareADObjectsResult.ADAttribute.ADAttributeFlags]
        kNone: CompareADObjectsResult.ADAttribute.ADAttributeFlags
        kEqual: CompareADObjectsResult.ADAttribute.ADAttributeFlags
        kNotEqual: CompareADObjectsResult.ADAttribute.ADAttributeFlags
        kNotFound: CompareADObjectsResult.ADAttribute.ADAttributeFlags
        kSystem: CompareADObjectsResult.ADAttribute.ADAttributeFlags
        kMultiValue: CompareADObjectsResult.ADAttribute.ADAttributeFlags
        LDAP_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VALUE_FIELD_NUMBER: _ClassVar[int]
        DEST_VALUE_FIELD_NUMBER: _ClassVar[int]
        SAME_VALUE_FIELD_NUMBER: _ClassVar[int]
        ATTR_FLAGS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ldap_name: str
        source_value: CompareADObjectsResult.ADAttributeValue
        dest_value: CompareADObjectsResult.ADAttributeValue
        same_value: CompareADObjectsResult.ADAttributeValue
        attr_flags: int
        status: _error_pb2.ErrorProto
        def __init__(self, ldap_name: _Optional[str] = ..., source_value: _Optional[_Union[CompareADObjectsResult.ADAttributeValue, _Mapping]] = ..., dest_value: _Optional[_Union[CompareADObjectsResult.ADAttributeValue, _Mapping]] = ..., same_value: _Optional[_Union[CompareADObjectsResult.ADAttributeValue, _Mapping]] = ..., attr_flags: _Optional[int] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    class ADObject(_message.Message):
        __slots__ = ("source_guid", "dest_guid", "object_flags", "mismatch_prop_count", "source_prop_count", "dest_prop_count", "excluded_prop_count", "status", "attribute_vec")
        class ADObjectFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNone: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
            kEqual: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
            kNotEqual: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
            kRestorePasswordRequired: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
            kMovedOnDestination: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
            kDestinationNotFound: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
            kDisableSupported: _ClassVar[CompareADObjectsResult.ADObject.ADObjectFlags]
        kNone: CompareADObjectsResult.ADObject.ADObjectFlags
        kEqual: CompareADObjectsResult.ADObject.ADObjectFlags
        kNotEqual: CompareADObjectsResult.ADObject.ADObjectFlags
        kRestorePasswordRequired: CompareADObjectsResult.ADObject.ADObjectFlags
        kMovedOnDestination: CompareADObjectsResult.ADObject.ADObjectFlags
        kDestinationNotFound: CompareADObjectsResult.ADObject.ADObjectFlags
        kDisableSupported: CompareADObjectsResult.ADObject.ADObjectFlags
        SOURCE_GUID_FIELD_NUMBER: _ClassVar[int]
        DEST_GUID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_FLAGS_FIELD_NUMBER: _ClassVar[int]
        MISMATCH_PROP_COUNT_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PROP_COUNT_FIELD_NUMBER: _ClassVar[int]
        DEST_PROP_COUNT_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_PROP_COUNT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_VEC_FIELD_NUMBER: _ClassVar[int]
        source_guid: str
        dest_guid: str
        object_flags: int
        mismatch_prop_count: int
        source_prop_count: int
        dest_prop_count: int
        excluded_prop_count: int
        status: _error_pb2.ErrorProto
        attribute_vec: _containers.RepeatedCompositeFieldContainer[CompareADObjectsResult.ADAttribute]
        def __init__(self, source_guid: _Optional[str] = ..., dest_guid: _Optional[str] = ..., object_flags: _Optional[int] = ..., mismatch_prop_count: _Optional[int] = ..., source_prop_count: _Optional[int] = ..., dest_prop_count: _Optional[int] = ..., excluded_prop_count: _Optional[int] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., attribute_vec: _Optional[_Iterable[_Union[CompareADObjectsResult.ADAttribute, _Mapping]]] = ...) -> None: ...
    OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    object_vec: _containers.RepeatedCompositeFieldContainer[CompareADObjectsResult.ADObject]
    def __init__(self, object_vec: _Optional[_Iterable[_Union[CompareADObjectsResult.ADObject, _Mapping]]] = ...) -> None: ...

class ADObjectRestoreStatus(_message.Message):
    __slots__ = ("source_guid", "dest_guid", "status", "object_flags", "property_status_vec", "timetaken_ms")
    class ADObjectFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ADObjectRestoreStatus.ADObjectFlags]
        kRecycleBin: _ClassVar[ADObjectRestoreStatus.ADObjectFlags]
    kNone: ADObjectRestoreStatus.ADObjectFlags
    kRecycleBin: ADObjectRestoreStatus.ADObjectFlags
    class ADAttributeRestoreStatus(_message.Message):
        __slots__ = ("ldap_name", "attrstatus_vec")
        LDAP_NAME_FIELD_NUMBER: _ClassVar[int]
        ATTRSTATUS_VEC_FIELD_NUMBER: _ClassVar[int]
        ldap_name: str
        attrstatus_vec: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
        def __init__(self, ldap_name: _Optional[str] = ..., attrstatus_vec: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ...) -> None: ...
    SOURCE_GUID_FIELD_NUMBER: _ClassVar[int]
    DEST_GUID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    TIMETAKEN_MS_FIELD_NUMBER: _ClassVar[int]
    source_guid: str
    dest_guid: str
    status: _error_pb2.ErrorProto
    object_flags: int
    property_status_vec: _containers.RepeatedCompositeFieldContainer[ADObjectRestoreStatus.ADAttributeRestoreStatus]
    timetaken_ms: int
    def __init__(self, source_guid: _Optional[str] = ..., dest_guid: _Optional[str] = ..., status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., object_flags: _Optional[int] = ..., property_status_vec: _Optional[_Iterable[_Union[ADObjectRestoreStatus.ADAttributeRestoreStatus, _Mapping]]] = ..., timetaken_ms: _Optional[int] = ...) -> None: ...

class ADAttributeRestoreParam(_message.Message):
    __slots__ = ("guidpair_vec", "property_vec", "excluded_property_vec", "option_flags", "src_sysvol_folder")
    class ADAttributeOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ADAttributeRestoreParam.ADAttributeOptionFlags]
        kMergeMultiValueProps: _ClassVar[ADAttributeRestoreParam.ADAttributeOptionFlags]
        kExcludeSysProps: _ClassVar[ADAttributeRestoreParam.ADAttributeOptionFlags]
        kLogEvent: _ClassVar[ADAttributeRestoreParam.ADAttributeOptionFlags]
    kNone: ADAttributeRestoreParam.ADAttributeOptionFlags
    kMergeMultiValueProps: ADAttributeRestoreParam.ADAttributeOptionFlags
    kExcludeSysProps: ADAttributeRestoreParam.ADAttributeOptionFlags
    kLogEvent: ADAttributeRestoreParam.ADAttributeOptionFlags
    GUIDPAIR_VEC_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SRC_SYSVOL_FOLDER_FIELD_NUMBER: _ClassVar[int]
    guidpair_vec: _containers.RepeatedCompositeFieldContainer[ADGuidPair]
    property_vec: _containers.RepeatedScalarFieldContainer[str]
    excluded_property_vec: _containers.RepeatedScalarFieldContainer[str]
    option_flags: int
    src_sysvol_folder: str
    def __init__(self, guidpair_vec: _Optional[_Iterable[_Union[ADGuidPair, _Mapping]]] = ..., property_vec: _Optional[_Iterable[str]] = ..., excluded_property_vec: _Optional[_Iterable[str]] = ..., option_flags: _Optional[int] = ..., src_sysvol_folder: _Optional[str] = ...) -> None: ...

class RestoreADObjectAttributesArg(_message.Message):
    __slots__ = ("connection_param", "attrib_param")
    CONNECTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    ATTRIB_PARAM_FIELD_NUMBER: _ClassVar[int]
    connection_param: ADConnectionParam
    attrib_param: ADAttributeRestoreParam
    def __init__(self, connection_param: _Optional[_Union[ADConnectionParam, _Mapping]] = ..., attrib_param: _Optional[_Union[ADAttributeRestoreParam, _Mapping]] = ...) -> None: ...

class RestoreADObjectAttributesResult(_message.Message):
    __slots__ = ("status_vec",)
    STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    status_vec: _containers.RepeatedCompositeFieldContainer[ADObjectRestoreStatus]
    def __init__(self, status_vec: _Optional[_Iterable[_Union[ADObjectRestoreStatus, _Mapping]]] = ...) -> None: ...

class ADObjectRestoreParam(_message.Message):
    __slots__ = ("guid_vec", "ou_path", "option_flags", "credentials", "src_sysvol_folder")
    class ADObjectRestoreOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
        kGroupMembership: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
        kChangePwdNextLogon: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
        kLeaveDisabled: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
        kLogEvent: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
        kRecycleBin: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
        kRecycleBinRestoreResetPwd: _ClassVar[ADObjectRestoreParam.ADObjectRestoreOptionFlags]
    kNone: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    kGroupMembership: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    kChangePwdNextLogon: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    kLeaveDisabled: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    kLogEvent: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    kRecycleBin: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    kRecycleBinRestoreResetPwd: ADObjectRestoreParam.ADObjectRestoreOptionFlags
    GUID_VEC_FIELD_NUMBER: _ClassVar[int]
    OU_PATH_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SRC_SYSVOL_FOLDER_FIELD_NUMBER: _ClassVar[int]
    guid_vec: _containers.RepeatedScalarFieldContainer[str]
    ou_path: str
    option_flags: int
    credentials: _credentials_pb2.Credentials
    src_sysvol_folder: str
    def __init__(self, guid_vec: _Optional[_Iterable[str]] = ..., ou_path: _Optional[str] = ..., option_flags: _Optional[int] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., src_sysvol_folder: _Optional[str] = ...) -> None: ...

class RestoreADObjectsArg(_message.Message):
    __slots__ = ("connection_param", "object_param")
    CONNECTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PARAM_FIELD_NUMBER: _ClassVar[int]
    connection_param: ADConnectionParam
    object_param: ADObjectRestoreParam
    def __init__(self, connection_param: _Optional[_Union[ADConnectionParam, _Mapping]] = ..., object_param: _Optional[_Union[ADObjectRestoreParam, _Mapping]] = ...) -> None: ...

class RestoreADObjectsResult(_message.Message):
    __slots__ = ("status_vec",)
    STATUS_VEC_FIELD_NUMBER: _ClassVar[int]
    status_vec: _containers.RepeatedCompositeFieldContainer[ADObjectRestoreStatus]
    def __init__(self, status_vec: _Optional[_Iterable[_Union[ADObjectRestoreStatus, _Mapping]]] = ...) -> None: ...

class ValidateADCredentialArg(_message.Message):
    __slots__ = ("connection_param", "domain_dn", "option_flags")
    class ADCredentialOptionFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ValidateADCredentialArg.ADCredentialOptionFlags]
    kNone: ValidateADCredentialArg.ADCredentialOptionFlags
    CONNECTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_DN_FIELD_NUMBER: _ClassVar[int]
    OPTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    connection_param: ADConnectionParam
    domain_dn: str
    option_flags: int
    def __init__(self, connection_param: _Optional[_Union[ADConnectionParam, _Mapping]] = ..., domain_dn: _Optional[str] = ..., option_flags: _Optional[int] = ...) -> None: ...

class ValidateADCredentialResult(_message.Message):
    __slots__ = ("result_flags", "schema_version")
    class Flags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[ValidateADCredentialResult.Flags]
        kReadOnlyDC: _ClassVar[ValidateADCredentialResult.Flags]
    kNone: ValidateADCredentialResult.Flags
    kReadOnlyDC: ValidateADCredentialResult.Flags
    RESULT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    result_flags: int
    schema_version: int
    def __init__(self, result_flags: _Optional[int] = ..., schema_version: _Optional[int] = ...) -> None: ...

class ADActionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kGetADRootTopology: _ClassVar[ADActionType.Type]
        kSearchADObjects: _ClassVar[ADActionType.Type]
        kCompareADObjects: _ClassVar[ADActionType.Type]
        kRestoreADObjects: _ClassVar[ADActionType.Type]
        kRestoreADObjectAttributes: _ClassVar[ADActionType.Type]
        kValidateADCredential: _ClassVar[ADActionType.Type]
        kGetADHierarchy: _ClassVar[ADActionType.Type]
        kMountADSnapshotDatabase: _ClassVar[ADActionType.Type]
        kUnmountADSnapshotDatabase: _ClassVar[ADActionType.Type]
    kGetADRootTopology: ADActionType.Type
    kSearchADObjects: ADActionType.Type
    kCompareADObjects: ADActionType.Type
    kRestoreADObjects: ADActionType.Type
    kRestoreADObjectAttributes: ADActionType.Type
    kValidateADCredential: ADActionType.Type
    kGetADHierarchy: ADActionType.Type
    kMountADSnapshotDatabase: ADActionType.Type
    kUnmountADSnapshotDatabase: ADActionType.Type
    def __init__(self) -> None: ...

class ExecuteADActionArg(_message.Message):
    __slots__ = ("action_type", "timeout_sec", "num_retries", "get_topology_arg", "search_arg", "compare_arg", "restore_object_arg", "restore_attribute_arg", "validate_cred_arg", "get_entity_arg", "mount_arg", "unmount_arg")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    GET_TOPOLOGY_ARG_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ARG_FIELD_NUMBER: _ClassVar[int]
    COMPARE_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_ARG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ATTRIBUTE_ARG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_CRED_ARG_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_ARG_FIELD_NUMBER: _ClassVar[int]
    MOUNT_ARG_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_ARG_FIELD_NUMBER: _ClassVar[int]
    action_type: ADActionType.Type
    timeout_sec: int
    num_retries: int
    get_topology_arg: GetADDomainRootTopologyArg
    search_arg: SearchADObjectsArg
    compare_arg: CompareADObjectsArg
    restore_object_arg: RestoreADObjectsArg
    restore_attribute_arg: RestoreADObjectAttributesArg
    validate_cred_arg: ValidateADCredentialArg
    get_entity_arg: GetADHierarchyArg
    mount_arg: MountADSnapshotDatabaseArg
    unmount_arg: UnmountADSnapshotDatabaseArg
    def __init__(self, action_type: _Optional[_Union[ADActionType.Type, str]] = ..., timeout_sec: _Optional[int] = ..., num_retries: _Optional[int] = ..., get_topology_arg: _Optional[_Union[GetADDomainRootTopologyArg, _Mapping]] = ..., search_arg: _Optional[_Union[SearchADObjectsArg, _Mapping]] = ..., compare_arg: _Optional[_Union[CompareADObjectsArg, _Mapping]] = ..., restore_object_arg: _Optional[_Union[RestoreADObjectsArg, _Mapping]] = ..., restore_attribute_arg: _Optional[_Union[RestoreADObjectAttributesArg, _Mapping]] = ..., validate_cred_arg: _Optional[_Union[ValidateADCredentialArg, _Mapping]] = ..., get_entity_arg: _Optional[_Union[GetADHierarchyArg, _Mapping]] = ..., mount_arg: _Optional[_Union[MountADSnapshotDatabaseArg, _Mapping]] = ..., unmount_arg: _Optional[_Union[UnmountADSnapshotDatabaseArg, _Mapping]] = ...) -> None: ...

class ExecuteADActionResult(_message.Message):
    __slots__ = ("action_type", "get_topology_result", "search_result", "compare_result", "restore_object_result", "restore_attribute_result", "validate_cred_result", "get_entity_result", "mount_result", "unmount_result")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    GET_TOPOLOGY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    COMPARE_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OBJECT_RESULT_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ATTRIBUTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_CRED_RESULT_FIELD_NUMBER: _ClassVar[int]
    GET_ENTITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_RESULT_FIELD_NUMBER: _ClassVar[int]
    UNMOUNT_RESULT_FIELD_NUMBER: _ClassVar[int]
    action_type: ADActionType.Type
    get_topology_result: GetADDomainRootTopologyResult
    search_result: SearchADObjectsResult
    compare_result: CompareADObjectsResult
    restore_object_result: RestoreADObjectsResult
    restore_attribute_result: RestoreADObjectAttributesResult
    validate_cred_result: ValidateADCredentialResult
    get_entity_result: GetADHierarchyResult
    mount_result: MountADSnapshotDatabaseResult
    unmount_result: UnmountADSnapshotDatabaseResult
    def __init__(self, action_type: _Optional[_Union[ADActionType.Type, str]] = ..., get_topology_result: _Optional[_Union[GetADDomainRootTopologyResult, _Mapping]] = ..., search_result: _Optional[_Union[SearchADObjectsResult, _Mapping]] = ..., compare_result: _Optional[_Union[CompareADObjectsResult, _Mapping]] = ..., restore_object_result: _Optional[_Union[RestoreADObjectsResult, _Mapping]] = ..., restore_attribute_result: _Optional[_Union[RestoreADObjectAttributesResult, _Mapping]] = ..., validate_cred_result: _Optional[_Union[ValidateADCredentialResult, _Mapping]] = ..., get_entity_result: _Optional[_Union[GetADHierarchyResult, _Mapping]] = ..., mount_result: _Optional[_Union[MountADSnapshotDatabaseResult, _Mapping]] = ..., unmount_result: _Optional[_Union[UnmountADSnapshotDatabaseResult, _Mapping]] = ...) -> None: ...
