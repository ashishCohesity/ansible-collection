from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetentionMode(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[RetentionMode.Type]
        kUnknown: _ClassVar[RetentionMode.Type]
        kGovernance: _ClassVar[RetentionMode.Type]
        kCompliance: _ClassVar[RetentionMode.Type]
    kNone: RetentionMode.Type
    kUnknown: RetentionMode.Type
    kGovernance: RetentionMode.Type
    kCompliance: RetentionMode.Type
    def __init__(self) -> None: ...

class WORMParams(_message.Message):
    __slots__ = ("minimum_retention_timestamp_secs", "target_retention_timestamp_secs", "retention_mode")
    MINIMUM_RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    TARGET_RETENTION_TIMESTAMP_SECS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    minimum_retention_timestamp_secs: int
    target_retention_timestamp_secs: int
    retention_mode: RetentionMode.Type
    def __init__(self, minimum_retention_timestamp_secs: _Optional[int] = ..., target_retention_timestamp_secs: _Optional[int] = ..., retention_mode: _Optional[_Union[RetentionMode.Type, str]] = ...) -> None: ...

class WORMRetentionExtendabilityInfo(_message.Message):
    __slots__ = ("is_worm_retention_extendable",)
    IS_WORM_RETENTION_EXTENDABLE_FIELD_NUMBER: _ClassVar[int]
    is_worm_retention_extendable: bool
    def __init__(self, is_worm_retention_extendable: bool = ...) -> None: ...
