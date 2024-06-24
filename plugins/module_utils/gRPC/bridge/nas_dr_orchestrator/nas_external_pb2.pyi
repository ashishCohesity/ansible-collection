from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FailoverOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[FailoverOperation]
    kUnplannedFailover: _ClassVar[FailoverOperation]
    kPrepareFailover: _ClassVar[FailoverOperation]
    kFailover: _ClassVar[FailoverOperation]
    kCancel: _ClassVar[FailoverOperation]

class ReplEventName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUndefined: _ClassVar[ReplEventName]
    kRxBeforeReplStart: _ClassVar[ReplEventName]
    kRxAfterReplCompletion: _ClassVar[ReplEventName]
kUnknown: FailoverOperation
kUnplannedFailover: FailoverOperation
kPrepareFailover: FailoverOperation
kFailover: FailoverOperation
kCancel: FailoverOperation
kUndefined: ReplEventName
kRxBeforeReplStart: ReplEventName
kRxAfterReplCompletion: ReplEventName
