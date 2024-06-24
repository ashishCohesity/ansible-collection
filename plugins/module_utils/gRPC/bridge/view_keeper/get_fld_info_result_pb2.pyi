from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileLevelDataLockResult(_message.Message):
    __slots__ = ("state", "lock_timestamp_usecs", "expiry_timestamp_usecs", "view_hold_timestamp_usecs", "lock_mode", "legal_hold_enabled")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnconfigured: _ClassVar[FileLevelDataLockResult.State]
        kUnlocked: _ClassVar[FileLevelDataLockResult.State]
        kLocked: _ClassVar[FileLevelDataLockResult.State]
        kExpired: _ClassVar[FileLevelDataLockResult.State]
        kHold: _ClassVar[FileLevelDataLockResult.State]
    kUnconfigured: FileLevelDataLockResult.State
    kUnlocked: FileLevelDataLockResult.State
    kLocked: FileLevelDataLockResult.State
    kExpired: FileLevelDataLockResult.State
    kHold: FileLevelDataLockResult.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    LOCK_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_HOLD_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    LOCK_MODE_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    state: FileLevelDataLockResult.State
    lock_timestamp_usecs: int
    expiry_timestamp_usecs: int
    view_hold_timestamp_usecs: int
    lock_mode: _view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode
    legal_hold_enabled: bool
    def __init__(self, state: _Optional[_Union[FileLevelDataLockResult.State, str]] = ..., lock_timestamp_usecs: _Optional[int] = ..., expiry_timestamp_usecs: _Optional[int] = ..., view_hold_timestamp_usecs: _Optional[int] = ..., lock_mode: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto.FileLevelDataLockConfig.ExplicitLockingMode, str]] = ..., legal_hold_enabled: bool = ...) -> None: ...
