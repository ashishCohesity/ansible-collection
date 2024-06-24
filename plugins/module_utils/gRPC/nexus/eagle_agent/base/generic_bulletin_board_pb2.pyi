from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kClusterVersion: _ClassVar[DataKey]
    kMyApps: _ClassVar[DataKey]
    kApp: _ClassVar[DataKey]
    kGlobalPolicy: _ClassVar[DataKey]
    kSupportServer: _ClassVar[DataKey]
    kHeliosAuditLogSetting: _ClassVar[DataKey]
    kRpaasRegionPairing: _ClassVar[DataKey]
    kHeliosTenants: _ClassVar[DataKey]
kClusterVersion: DataKey
kMyApps: DataKey
kApp: DataKey
kGlobalPolicy: DataKey
kSupportServer: DataKey
kHeliosAuditLogSetting: DataKey
kRpaasRegionPairing: DataKey
kHeliosTenants: DataKey

class UserInfo(_message.Message):
    __slots__ = ("name", "sid", "domain")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    name: str
    sid: str
    domain: str
    def __init__(self, name: _Optional[str] = ..., sid: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class BulletinBoardRecord(_message.Message):
    __slots__ = ("data_key", "data_value", "custom_id", "timestamp_usecs", "user", "version", "is_account_wide", "is_deleted", "is_applied_successfully")
    DATA_KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_ACCOUNT_WIDE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_APPLIED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    data_key: DataKey
    data_value: bytes
    custom_id: str
    timestamp_usecs: int
    user: UserInfo
    version: int
    is_account_wide: bool
    is_deleted: bool
    is_applied_successfully: bool
    def __init__(self, data_key: _Optional[_Union[DataKey, str]] = ..., data_value: _Optional[bytes] = ..., custom_id: _Optional[str] = ..., timestamp_usecs: _Optional[int] = ..., user: _Optional[_Union[UserInfo, _Mapping]] = ..., version: _Optional[int] = ..., is_account_wide: bool = ..., is_deleted: bool = ..., is_applied_successfully: bool = ...) -> None: ...

class BulletinBoard(_message.Message):
    __slots__ = ("record_vec",)
    RECORD_VEC_FIELD_NUMBER: _ClassVar[int]
    record_vec: _containers.RepeatedCompositeFieldContainer[BulletinBoardRecord]
    def __init__(self, record_vec: _Optional[_Iterable[_Union[BulletinBoardRecord, _Mapping]]] = ...) -> None: ...
