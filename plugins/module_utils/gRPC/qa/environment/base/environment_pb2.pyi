from qa.environment.base import common_pb2 as _common_pb2
from qa.environment.base import cohesity_pb2 as _cohesity_pb2
from qa.environment.base import vmware_pb2 as _vmware_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnvironment(_message.Message):
    __slots__ = ("node_vec", "login_info_vec", "cohesity_version_vec", "vcenter_vec", "vm_setup_info_vec", "ps_host", "cluster_vec")
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    COHESITY_VERSION_VEC_FIELD_NUMBER: _ClassVar[int]
    VCENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    VM_SETUP_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    PS_HOST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    node_vec: _containers.RepeatedCompositeFieldContainer[_cohesity_pb2.NodeInfo]
    login_info_vec: _containers.RepeatedCompositeFieldContainer[_common_pb2.Credentials]
    cohesity_version_vec: _containers.RepeatedCompositeFieldContainer[_cohesity_pb2.CohesitySoftwareInfo]
    vcenter_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.VCenterInfo]
    vm_setup_info_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.VMSetupInfo]
    ps_host: _vmware_pb2.PSHostInfo
    cluster_vec: _containers.RepeatedCompositeFieldContainer[_cohesity_pb2.ClusterInfo]
    def __init__(self, node_vec: _Optional[_Iterable[_Union[_cohesity_pb2.NodeInfo, _Mapping]]] = ..., login_info_vec: _Optional[_Iterable[_Union[_common_pb2.Credentials, _Mapping]]] = ..., cohesity_version_vec: _Optional[_Iterable[_Union[_cohesity_pb2.CohesitySoftwareInfo, _Mapping]]] = ..., vcenter_vec: _Optional[_Iterable[_Union[_vmware_pb2.VCenterInfo, _Mapping]]] = ..., vm_setup_info_vec: _Optional[_Iterable[_Union[_vmware_pb2.VMSetupInfo, _Mapping]]] = ..., ps_host: _Optional[_Union[_vmware_pb2.PSHostInfo, _Mapping]] = ..., cluster_vec: _Optional[_Iterable[_Union[_cohesity_pb2.ClusterInfo, _Mapping]]] = ...) -> None: ...
