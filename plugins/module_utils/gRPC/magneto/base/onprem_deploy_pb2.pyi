from magneto.base import vmware_common_pb2 as _vmware_common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeployVMsToOnPremParams(_message.Message):
    __slots__ = ("deploy_vms_to_vmware_params",)
    DEPLOY_VMS_TO_VMWARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    deploy_vms_to_vmware_params: _vmware_common_pb2.RestoreVMwareVMParams
    def __init__(self, deploy_vms_to_vmware_params: _Optional[_Union[_vmware_common_pb2.RestoreVMwareVMParams, _Mapping]] = ...) -> None: ...
