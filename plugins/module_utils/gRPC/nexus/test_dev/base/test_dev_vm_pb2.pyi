from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestDevVm(_message.Message):
    __slots__ = ("vm_name", "vm_uuid", "vm_vcpu", "vm_memory", "vm_devices")
    class Disk(_message.Message):
        __slots__ = ("disk_bootable", "disk_path", "disk_create", "disk_size")
        class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kDiskBootable: _ClassVar[TestDevVm.Disk.DiskType]
        kDiskBootable: TestDevVm.Disk.DiskType
        DISK_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
        DISK_PATH_FIELD_NUMBER: _ClassVar[int]
        DISK_CREATE_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        disk_bootable: TestDevVm.Disk.DiskType
        disk_path: str
        disk_create: bool
        disk_size: int
        def __init__(self, disk_bootable: _Optional[_Union[TestDevVm.Disk.DiskType, str]] = ..., disk_path: _Optional[str] = ..., disk_create: bool = ..., disk_size: _Optional[int] = ...) -> None: ...
    class PortMapping(_message.Message):
        __slots__ = ("hostport", "guestport", "protocol")
        HOSTPORT_FIELD_NUMBER: _ClassVar[int]
        GUESTPORT_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        hostport: int
        guestport: int
        protocol: str
        def __init__(self, hostport: _Optional[int] = ..., guestport: _Optional[int] = ..., protocol: _Optional[str] = ...) -> None: ...
    class Interface(_message.Message):
        __slots__ = ("network_type", "network_name", "interface_macaddr", "interface_ipv4addr", "vm_portmapping")
        class NetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kNat: _ClassVar[TestDevVm.Interface.NetworkType]
            kBridge: _ClassVar[TestDevVm.Interface.NetworkType]
        kNat: TestDevVm.Interface.NetworkType
        kBridge: TestDevVm.Interface.NetworkType
        NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_MACADDR_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_IPV4ADDR_FIELD_NUMBER: _ClassVar[int]
        VM_PORTMAPPING_FIELD_NUMBER: _ClassVar[int]
        network_type: TestDevVm.Interface.NetworkType
        network_name: str
        interface_macaddr: bytes
        interface_ipv4addr: str
        vm_portmapping: _containers.RepeatedCompositeFieldContainer[TestDevVm.PortMapping]
        def __init__(self, network_type: _Optional[_Union[TestDevVm.Interface.NetworkType, str]] = ..., network_name: _Optional[str] = ..., interface_macaddr: _Optional[bytes] = ..., interface_ipv4addr: _Optional[str] = ..., vm_portmapping: _Optional[_Iterable[_Union[TestDevVm.PortMapping, _Mapping]]] = ...) -> None: ...
    class Network(_message.Message):
        __slots__ = ("vm_interface",)
        VM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
        vm_interface: _containers.RepeatedCompositeFieldContainer[TestDevVm.Interface]
        def __init__(self, vm_interface: _Optional[_Iterable[_Union[TestDevVm.Interface, _Mapping]]] = ...) -> None: ...
    class Graphics(_message.Message):
        __slots__ = ("graphics_type", "graphics_ip", "graphics_port", "graphics_passwd")
        class GraphicsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kVnc: _ClassVar[TestDevVm.Graphics.GraphicsType]
        kVnc: TestDevVm.Graphics.GraphicsType
        GRAPHICS_TYPE_FIELD_NUMBER: _ClassVar[int]
        GRAPHICS_IP_FIELD_NUMBER: _ClassVar[int]
        GRAPHICS_PORT_FIELD_NUMBER: _ClassVar[int]
        GRAPHICS_PASSWD_FIELD_NUMBER: _ClassVar[int]
        graphics_type: TestDevVm.Graphics.GraphicsType
        graphics_ip: str
        graphics_port: int
        graphics_passwd: str
        def __init__(self, graphics_type: _Optional[_Union[TestDevVm.Graphics.GraphicsType, str]] = ..., graphics_ip: _Optional[str] = ..., graphics_port: _Optional[int] = ..., graphics_passwd: _Optional[str] = ...) -> None: ...
    class Devices(_message.Message):
        __slots__ = ("devices_disk", "devices_network", "devices_graphics")
        DEVICES_DISK_FIELD_NUMBER: _ClassVar[int]
        DEVICES_NETWORK_FIELD_NUMBER: _ClassVar[int]
        DEVICES_GRAPHICS_FIELD_NUMBER: _ClassVar[int]
        devices_disk: _containers.RepeatedCompositeFieldContainer[TestDevVm.Disk]
        devices_network: TestDevVm.Network
        devices_graphics: TestDevVm.Graphics
        def __init__(self, devices_disk: _Optional[_Iterable[_Union[TestDevVm.Disk, _Mapping]]] = ..., devices_network: _Optional[_Union[TestDevVm.Network, _Mapping]] = ..., devices_graphics: _Optional[_Union[TestDevVm.Graphics, _Mapping]] = ...) -> None: ...
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    VM_VCPU_FIELD_NUMBER: _ClassVar[int]
    VM_MEMORY_FIELD_NUMBER: _ClassVar[int]
    VM_DEVICES_FIELD_NUMBER: _ClassVar[int]
    vm_name: str
    vm_uuid: str
    vm_vcpu: int
    vm_memory: int
    vm_devices: TestDevVm.Devices
    def __init__(self, vm_name: _Optional[str] = ..., vm_uuid: _Optional[str] = ..., vm_vcpu: _Optional[int] = ..., vm_memory: _Optional[int] = ..., vm_devices: _Optional[_Union[TestDevVm.Devices, _Mapping]] = ...) -> None: ...
