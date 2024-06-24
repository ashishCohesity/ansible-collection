from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VMwareEntityAttributesNamesProto(_message.Message):
    __slots__ = ("host_type", "vmware_tools_status", "logical_size_in_bytes")
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_TOOLS_STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    host_type: str
    vmware_tools_status: str
    logical_size_in_bytes: str
    def __init__(self, host_type: _Optional[str] = ..., vmware_tools_status: _Optional[str] = ..., logical_size_in_bytes: _Optional[str] = ...) -> None: ...
