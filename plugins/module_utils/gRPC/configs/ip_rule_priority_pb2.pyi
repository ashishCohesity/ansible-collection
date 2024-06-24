from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IPRulePriorityProto(_message.Message):
    __slots__ = ("athena_subnet", "vip_default", "vip_range_start", "vip_range_end")
    ATHENA_SUBNET_FIELD_NUMBER: _ClassVar[int]
    VIP_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    VIP_RANGE_START_FIELD_NUMBER: _ClassVar[int]
    VIP_RANGE_END_FIELD_NUMBER: _ClassVar[int]
    athena_subnet: int
    vip_default: int
    vip_range_start: int
    vip_range_end: int
    def __init__(self, athena_subnet: _Optional[int] = ..., vip_default: _Optional[int] = ..., vip_range_start: _Optional[int] = ..., vip_range_end: _Optional[int] = ...) -> None: ...
