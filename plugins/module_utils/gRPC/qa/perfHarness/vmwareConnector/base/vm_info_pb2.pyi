from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigureVMParams(_message.Message):
    __slots__ = ("new_dhcp_nic", "powering_on")
    NEW_DHCP_NIC_FIELD_NUMBER: _ClassVar[int]
    POWERING_ON_FIELD_NUMBER: _ClassVar[int]
    new_dhcp_nic: bool
    powering_on: bool
    def __init__(self, new_dhcp_nic: bool = ..., powering_on: bool = ...) -> None: ...
