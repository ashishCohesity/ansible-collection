from magneto.base.entities import vmware_common_pb2 as _vmware_common_pb2
from magneto.connectors.vmware import vmware_pb2 as _vmware_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VsphereErrorProto(_message.Message):
    __slots__ = ("type", "soap_type", "error_message")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kNoError: _ClassVar[VsphereErrorProto.Type]
        kUnknown: _ClassVar[VsphereErrorProto.Type]
        kCancelled: _ClassVar[VsphereErrorProto.Type]
        kDuplicate: _ClassVar[VsphereErrorProto.Type]
        kNonExistent: _ClassVar[VsphereErrorProto.Type]
        kAlreadyExists: _ClassVar[VsphereErrorProto.Type]
        kRuntimeError: _ClassVar[VsphereErrorProto.Type]
        kTaskInProgress: _ClassVar[VsphereErrorProto.Type]
        kHostConfigError: _ClassVar[VsphereErrorProto.Type]
        kVmfsAmbiguousMount: _ClassVar[VsphereErrorProto.Type]
        kInvalidPowerState: _ClassVar[VsphereErrorProto.Type]
        kTooManySnapshotLevels: _ClassVar[VsphereErrorProto.Type]
        kInvalidDeviceSpec: _ClassVar[VsphereErrorProto.Type]
        kInvalidDeviceOperation: _ClassVar[VsphereErrorProto.Type]
        kInvalidDeviceBacking: _ClassVar[VsphereErrorProto.Type]
        kInvalidDatastore: _ClassVar[VsphereErrorProto.Type]
        kNotFound: _ClassVar[VsphereErrorProto.Type]
        kFileAlreadyExists: _ClassVar[VsphereErrorProto.Type]
    kNoError: VsphereErrorProto.Type
    kUnknown: VsphereErrorProto.Type
    kCancelled: VsphereErrorProto.Type
    kDuplicate: VsphereErrorProto.Type
    kNonExistent: VsphereErrorProto.Type
    kAlreadyExists: VsphereErrorProto.Type
    kRuntimeError: VsphereErrorProto.Type
    kTaskInProgress: VsphereErrorProto.Type
    kHostConfigError: VsphereErrorProto.Type
    kVmfsAmbiguousMount: VsphereErrorProto.Type
    kInvalidPowerState: VsphereErrorProto.Type
    kTooManySnapshotLevels: VsphereErrorProto.Type
    kInvalidDeviceSpec: VsphereErrorProto.Type
    kInvalidDeviceOperation: VsphereErrorProto.Type
    kInvalidDeviceBacking: VsphereErrorProto.Type
    kInvalidDatastore: VsphereErrorProto.Type
    kNotFound: VsphereErrorProto.Type
    kFileAlreadyExists: VsphereErrorProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: VsphereErrorProto.Type
    soap_type: int
    error_message: str
    def __init__(self, type: _Optional[_Union[VsphereErrorProto.Type, str]] = ..., soap_type: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class VsphereResultProto(_message.Message):
    __slots__ = ("error", "moref", "power_state", "power_on_vm_result", "cluster_io_filter_info")
    class ClusterPowerOnVmResult(_message.Message):
        __slots__ = ("already_powered_on", "cluster_recommendation_vec", "poweron_task_moref")
        class ClusterRecommendation(_message.Message):
            __slots__ = ("key", "target")
            KEY_FIELD_NUMBER: _ClassVar[int]
            TARGET_FIELD_NUMBER: _ClassVar[int]
            key: str
            target: _vmware_common_pb2.MORef
            def __init__(self, key: _Optional[str] = ..., target: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
        ALREADY_POWERED_ON_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_RECOMMENDATION_VEC_FIELD_NUMBER: _ClassVar[int]
        POWERON_TASK_MOREF_FIELD_NUMBER: _ClassVar[int]
        already_powered_on: bool
        cluster_recommendation_vec: _containers.RepeatedCompositeFieldContainer[VsphereResultProto.ClusterPowerOnVmResult.ClusterRecommendation]
        poweron_task_moref: _vmware_common_pb2.MORef
        def __init__(self, already_powered_on: bool = ..., cluster_recommendation_vec: _Optional[_Iterable[_Union[VsphereResultProto.ClusterPowerOnVmResult.ClusterRecommendation, _Mapping]]] = ..., poweron_task_moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MOREF_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    POWER_ON_VM_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IO_FILTER_INFO_FIELD_NUMBER: _ClassVar[int]
    error: VsphereErrorProto
    moref: _vmware_common_pb2.MORef
    power_state: _vmware_pb2.VirtualMachinePowerState
    power_on_vm_result: VsphereResultProto.ClusterPowerOnVmResult
    cluster_io_filter_info: _vmware_pb2.ClusterIoFilterInfo
    def __init__(self, error: _Optional[_Union[VsphereErrorProto, _Mapping]] = ..., moref: _Optional[_Union[_vmware_common_pb2.MORef, _Mapping]] = ..., power_state: _Optional[_Union[_vmware_pb2.VirtualMachinePowerState, str]] = ..., power_on_vm_result: _Optional[_Union[VsphereResultProto.ClusterPowerOnVmResult, _Mapping]] = ..., cluster_io_filter_info: _Optional[_Union[_vmware_pb2.ClusterIoFilterInfo, _Mapping]] = ...) -> None: ...
