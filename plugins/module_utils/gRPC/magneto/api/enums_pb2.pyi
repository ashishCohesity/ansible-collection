from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ArchivalTargetType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloud: _ClassVar[ArchivalTargetType.Type]
        kTape: _ClassVar[ArchivalTargetType.Type]
        kNas: _ClassVar[ArchivalTargetType.Type]
    kCloud: ArchivalTargetType.Type
    kTape: ArchivalTargetType.Type
    kNas: ArchivalTargetType.Type
    def __init__(self) -> None: ...

class RunInfoType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kBackup: _ClassVar[RunInfoType.Type]
        kReplication: _ClassVar[RunInfoType.Type]
        kArchival: _ClassVar[RunInfoType.Type]
        kCloudSpin: _ClassVar[RunInfoType.Type]
        kOnPremDeploy: _ClassVar[RunInfoType.Type]
    kBackup: RunInfoType.Type
    kReplication: RunInfoType.Type
    kArchival: RunInfoType.Type
    kCloudSpin: RunInfoType.Type
    kOnPremDeploy: RunInfoType.Type
    def __init__(self) -> None: ...

class PriorityProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLow: _ClassVar[PriorityProto.Type]
        kMedium: _ClassVar[PriorityProto.Type]
        kHigh: _ClassVar[PriorityProto.Type]
    kLow: PriorityProto.Type
    kMedium: PriorityProto.Type
    kHigh: PriorityProto.Type
    def __init__(self) -> None: ...

class ObjectBackupActionType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[ObjectBackupActionType.Type]
        kUnProtect: _ClassVar[ObjectBackupActionType.Type]
        kPause: _ClassVar[ObjectBackupActionType.Type]
        kResume: _ClassVar[ObjectBackupActionType.Type]
        kProtectNow: _ClassVar[ObjectBackupActionType.Type]
    kInvalid: ObjectBackupActionType.Type
    kUnProtect: ObjectBackupActionType.Type
    kPause: ObjectBackupActionType.Type
    kResume: ObjectBackupActionType.Type
    kProtectNow: ObjectBackupActionType.Type
    def __init__(self) -> None: ...

class DataFormatType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kJson: _ClassVar[DataFormatType.Type]
        kTextFormat: _ClassVar[DataFormatType.Type]
        kSerializedProtobuf: _ClassVar[DataFormatType.Type]
    kJson: DataFormatType.Type
    kTextFormat: DataFormatType.Type
    kSerializedProtobuf: DataFormatType.Type
    def __init__(self) -> None: ...

class Day(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSunday: _ClassVar[Day.Type]
        kMonday: _ClassVar[Day.Type]
        kTuesday: _ClassVar[Day.Type]
        kWednesday: _ClassVar[Day.Type]
        kThursday: _ClassVar[Day.Type]
        kFriday: _ClassVar[Day.Type]
        kSaturday: _ClassVar[Day.Type]
    kSunday: Day.Type
    kMonday: Day.Type
    kTuesday: Day.Type
    kWednesday: Day.Type
    kThursday: Day.Type
    kFriday: Day.Type
    kSaturday: Day.Type
    def __init__(self) -> None: ...
