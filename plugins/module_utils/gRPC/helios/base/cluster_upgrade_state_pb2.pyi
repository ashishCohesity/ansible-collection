from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterUpgradeState(_message.Message):
    __slots__ = ("current_sw_version", "target_sw_version", "current_upgrade_status")
    CURRENT_SW_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_SW_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
    current_sw_version: str
    target_sw_version: str
    current_upgrade_status: CurrentUpgradeStatus
    def __init__(self, current_sw_version: _Optional[str] = ..., target_sw_version: _Optional[str] = ..., current_upgrade_status: _Optional[_Union[CurrentUpgradeStatus, _Mapping]] = ...) -> None: ...

class CurrentUpgradeStatus(_message.Message):
    __slots__ = ("state", "percentage_finished", "message")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNone: _ClassVar[CurrentUpgradeStatus.State]
        kPending: _ClassVar[CurrentUpgradeStatus.State]
        kInProgress: _ClassVar[CurrentUpgradeStatus.State]
        kFailed: _ClassVar[CurrentUpgradeStatus.State]
        kFinished: _ClassVar[CurrentUpgradeStatus.State]
    kNone: CurrentUpgradeStatus.State
    kPending: CurrentUpgradeStatus.State
    kInProgress: CurrentUpgradeStatus.State
    kFailed: CurrentUpgradeStatus.State
    kFinished: CurrentUpgradeStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    state: CurrentUpgradeStatus.State
    percentage_finished: int
    message: str
    def __init__(self, state: _Optional[_Union[CurrentUpgradeStatus.State, str]] = ..., percentage_finished: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
