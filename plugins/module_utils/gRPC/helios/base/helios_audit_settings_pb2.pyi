from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosAuditLogUserSetting(_message.Message):
    __slots__ = ("user_sid", "read_logging")
    USER_SID_FIELD_NUMBER: _ClassVar[int]
    READ_LOGGING_FIELD_NUMBER: _ClassVar[int]
    user_sid: str
    read_logging: bool
    def __init__(self, user_sid: _Optional[str] = ..., read_logging: bool = ...) -> None: ...

class HeliosAuditLogRoleSetting(_message.Message):
    __slots__ = ("role_name", "read_logging")
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    READ_LOGGING_FIELD_NUMBER: _ClassVar[int]
    role_name: str
    read_logging: bool
    def __init__(self, role_name: _Optional[str] = ..., read_logging: bool = ...) -> None: ...

class HeliosAuditLogSettingsProto(_message.Message):
    __slots__ = ("user_settings", "read_logging", "role_settings", "retention_period_days", "account_id")
    USER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    READ_LOGGING_FIELD_NUMBER: _ClassVar[int]
    ROLE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    user_settings: _containers.RepeatedCompositeFieldContainer[HeliosAuditLogUserSetting]
    read_logging: bool
    role_settings: _containers.RepeatedCompositeFieldContainer[HeliosAuditLogRoleSetting]
    retention_period_days: int
    account_id: str
    def __init__(self, user_settings: _Optional[_Iterable[_Union[HeliosAuditLogUserSetting, _Mapping]]] = ..., read_logging: bool = ..., role_settings: _Optional[_Iterable[_Union[HeliosAuditLogRoleSetting, _Mapping]]] = ..., retention_period_days: _Optional[int] = ..., account_id: _Optional[str] = ...) -> None: ...
