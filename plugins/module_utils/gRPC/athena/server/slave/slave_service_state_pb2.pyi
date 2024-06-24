from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SlaveServiceStateProto(_message.Message):
    __slots__ = ("service_vec",)
    class ServiceName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        unknown: _ClassVar[SlaveServiceStateProto.ServiceName]
        docker: _ClassVar[SlaveServiceStateProto.ServiceName]
        kubeSlave: _ClassVar[SlaveServiceStateProto.ServiceName]
        kubelet: _ClassVar[SlaveServiceStateProto.ServiceName]
        athenaProxy: _ClassVar[SlaveServiceStateProto.ServiceName]
        vm: _ClassVar[SlaveServiceStateProto.ServiceName]
        kubeProxy: _ClassVar[SlaveServiceStateProto.ServiceName]
        flanneld: _ClassVar[SlaveServiceStateProto.ServiceName]
        athenaWatchdog: _ClassVar[SlaveServiceStateProto.ServiceName]
        yodaAgent: _ClassVar[SlaveServiceStateProto.ServiceName]
        flanneld2: _ClassVar[SlaveServiceStateProto.ServiceName]
        multus: _ClassVar[SlaveServiceStateProto.ServiceName]
        docker_registry_local: _ClassVar[SlaveServiceStateProto.ServiceName]
        containerd: _ClassVar[SlaveServiceStateProto.ServiceName]
        athenaCert: _ClassVar[SlaveServiceStateProto.ServiceName]
    unknown: SlaveServiceStateProto.ServiceName
    docker: SlaveServiceStateProto.ServiceName
    kubeSlave: SlaveServiceStateProto.ServiceName
    kubelet: SlaveServiceStateProto.ServiceName
    athenaProxy: SlaveServiceStateProto.ServiceName
    vm: SlaveServiceStateProto.ServiceName
    kubeProxy: SlaveServiceStateProto.ServiceName
    flanneld: SlaveServiceStateProto.ServiceName
    athenaWatchdog: SlaveServiceStateProto.ServiceName
    yodaAgent: SlaveServiceStateProto.ServiceName
    flanneld2: SlaveServiceStateProto.ServiceName
    multus: SlaveServiceStateProto.ServiceName
    docker_registry_local: SlaveServiceStateProto.ServiceName
    containerd: SlaveServiceStateProto.ServiceName
    athenaCert: SlaveServiceStateProto.ServiceName
    class ServiceInfo(_message.Message):
        __slots__ = ("name", "arg_vec", "fingerprint", "incarnation_id")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARG_VEC_FIELD_NUMBER: _ClassVar[int]
        FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        name: SlaveServiceStateProto.ServiceName
        arg_vec: _containers.RepeatedScalarFieldContainer[str]
        fingerprint: str
        incarnation_id: int
        def __init__(self, name: _Optional[_Union[SlaveServiceStateProto.ServiceName, str]] = ..., arg_vec: _Optional[_Iterable[str]] = ..., fingerprint: _Optional[str] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
    SERVICE_VEC_FIELD_NUMBER: _ClassVar[int]
    service_vec: _containers.RepeatedCompositeFieldContainer[SlaveServiceStateProto.ServiceInfo]
    def __init__(self, service_vec: _Optional[_Iterable[_Union[SlaveServiceStateProto.ServiceInfo, _Mapping]]] = ...) -> None: ...
