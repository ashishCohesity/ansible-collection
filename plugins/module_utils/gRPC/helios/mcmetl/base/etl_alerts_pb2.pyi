from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[Severity]
    kInfo: _ClassVar[Severity]
    kWarning: _ClassVar[Severity]
    kCritical: _ClassVar[Severity]
kUnknown: Severity
kInfo: Severity
kWarning: Severity
kCritical: Severity

class AlertPrimaryKeyProto(_message.Message):
    __slots__ = ("alert_instance_id", "first_occurrence_timestamp_usecs")
    ALERT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_OCCURRENCE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    alert_instance_id: int
    first_occurrence_timestamp_usecs: int
    def __init__(self, alert_instance_id: _Optional[int] = ..., first_occurrence_timestamp_usecs: _Optional[int] = ...) -> None: ...

class AlertDocumentProto(_message.Message):
    __slots__ = ("language_code", "name", "description", "cause", "help_text")
    class LanguageCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        k_unknown: _ClassVar[AlertDocumentProto.LanguageCode]
        k_en_us: _ClassVar[AlertDocumentProto.LanguageCode]
        k_en_uk: _ClassVar[AlertDocumentProto.LanguageCode]
        k_ja_jp: _ClassVar[AlertDocumentProto.LanguageCode]
        k_zh_cn: _ClassVar[AlertDocumentProto.LanguageCode]
    k_unknown: AlertDocumentProto.LanguageCode
    k_en_us: AlertDocumentProto.LanguageCode
    k_en_uk: AlertDocumentProto.LanguageCode
    k_ja_jp: AlertDocumentProto.LanguageCode
    k_zh_cn: AlertDocumentProto.LanguageCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: _descriptor.FieldDescriptor
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
    language_code: AlertDocumentProto.LanguageCode
    name: bytes
    description: bytes
    cause: bytes
    help_text: bytes
    def __init__(self, language_code: _Optional[_Union[AlertDocumentProto.LanguageCode, str]] = ..., name: _Optional[bytes] = ..., description: _Optional[bytes] = ..., cause: _Optional[bytes] = ..., help_text: _Optional[bytes] = ...) -> None: ...

class AlertCategoryProto(_message.Message):
    __slots__ = ("bucket", "sub_category", "code")
    class Bucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AlertCategoryProto.Bucket]
        kSoftware: _ClassVar[AlertCategoryProto.Bucket]
        kHardware: _ClassVar[AlertCategoryProto.Bucket]
        kMaintenance: _ClassVar[AlertCategoryProto.Bucket]
        kDataService: _ClassVar[AlertCategoryProto.Bucket]
    kUnknown: AlertCategoryProto.Bucket
    kSoftware: AlertCategoryProto.Bucket
    kHardware: AlertCategoryProto.Bucket
    kMaintenance: AlertCategoryProto.Bucket
    kDataService: AlertCategoryProto.Bucket
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    SUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    bucket: AlertCategoryProto.Bucket
    sub_category: int
    code: int
    def __init__(self, bucket: _Optional[_Union[AlertCategoryProto.Bucket, str]] = ..., sub_category: _Optional[int] = ..., code: _Optional[int] = ...) -> None: ...

class AlertDescriptionProto(_message.Message):
    __slots__ = ("alert_instance_id", "severity", "first_occurrence_timestamp_usecs", "last_n_occurrences_timestamp_usecs", "category", "document", "visible_to_user")
    ALERT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FIRST_OCCURRENCE_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LAST_N_OCCURRENCES_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_TO_USER_FIELD_NUMBER: _ClassVar[int]
    alert_instance_id: int
    severity: Severity
    first_occurrence_timestamp_usecs: int
    last_n_occurrences_timestamp_usecs: _containers.RepeatedScalarFieldContainer[int]
    category: AlertCategoryProto
    document: AlertDocumentProto
    visible_to_user: bool
    def __init__(self, alert_instance_id: _Optional[int] = ..., severity: _Optional[_Union[Severity, str]] = ..., first_occurrence_timestamp_usecs: _Optional[int] = ..., last_n_occurrences_timestamp_usecs: _Optional[_Iterable[int]] = ..., category: _Optional[_Union[AlertCategoryProto, _Mapping]] = ..., document: _Optional[_Union[AlertDocumentProto, _Mapping]] = ..., visible_to_user: bool = ...) -> None: ...

class AlertResolutionProto(_message.Message):
    __slots__ = ("alert_resolution_instance_id", "alert_primary_key_vec", "summary", "details", "resolved_timestamp_usecs", "user_id")
    ALERT_RESOLUTION_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_PRIMARY_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    alert_resolution_instance_id: int
    alert_primary_key_vec: _containers.RepeatedCompositeFieldContainer[AlertPrimaryKeyProto]
    summary: bytes
    details: bytes
    resolved_timestamp_usecs: int
    user_id: str
    def __init__(self, alert_resolution_instance_id: _Optional[int] = ..., alert_primary_key_vec: _Optional[_Iterable[_Union[AlertPrimaryKeyProto, _Mapping]]] = ..., summary: _Optional[bytes] = ..., details: _Optional[bytes] = ..., resolved_timestamp_usecs: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...
