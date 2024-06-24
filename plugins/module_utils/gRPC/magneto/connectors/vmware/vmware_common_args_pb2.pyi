from magneto.base import credentials_pb2 as _credentials_pb2
from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GuestOperationArg(_message.Message):
    __slots__ = ("vm_moref", "vm_credentials")
    VM_MOREF_FIELD_NUMBER: _ClassVar[int]
    VM_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    vm_moref: _vmware_common_pb2.MORef
    vm_credentials: _credentials_pb2.Credentials
    def __init__(self, vm_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., vm_credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ...) -> None: ...
