from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostVmVec(_message.Message):
    __slots__ = ("vm_conf_vec",)
    class VmConf(_message.Message):
        __slots__ = ("interface_group", "vlan_tag", "tenant_id", "image_version", "cpu", "memory", "state", "tenant_proxy_config")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[BifrostVmVec.VmConf.State]
            PARTIAL_CONFIGURED: _ClassVar[BifrostVmVec.VmConf.State]
            UPGRADING: _ClassVar[BifrostVmVec.VmConf.State]
            DELETING: _ClassVar[BifrostVmVec.VmConf.State]
            CONFIGURED: _ClassVar[BifrostVmVec.VmConf.State]
            PROVISIONED: _ClassVar[BifrostVmVec.VmConf.State]
            ERROR: _ClassVar[BifrostVmVec.VmConf.State]
        UNKNOWN: BifrostVmVec.VmConf.State
        PARTIAL_CONFIGURED: BifrostVmVec.VmConf.State
        UPGRADING: BifrostVmVec.VmConf.State
        DELETING: BifrostVmVec.VmConf.State
        CONFIGURED: BifrostVmVec.VmConf.State
        PROVISIONED: BifrostVmVec.VmConf.State
        ERROR: BifrostVmVec.VmConf.State
        INTERFACE_GROUP_FIELD_NUMBER: _ClassVar[int]
        VLAN_TAG_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        TENANT_PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        interface_group: str
        vlan_tag: int
        tenant_id: str
        image_version: str
        cpu: int
        memory: int
        state: int
        tenant_proxy_config: str
        def __init__(self, interface_group: _Optional[str] = ..., vlan_tag: _Optional[int] = ..., tenant_id: _Optional[str] = ..., image_version: _Optional[str] = ..., cpu: _Optional[int] = ..., memory: _Optional[int] = ..., state: _Optional[int] = ..., tenant_proxy_config: _Optional[str] = ...) -> None: ...
    VM_CONF_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_conf_vec: _containers.RepeatedCompositeFieldContainer[BifrostVmVec.VmConf]
    def __init__(self, vm_conf_vec: _Optional[_Iterable[_Union[BifrostVmVec.VmConf, _Mapping]]] = ...) -> None: ...
