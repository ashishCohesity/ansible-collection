from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDPVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCDPVersionV1: _ClassVar[CDPVersion]
    kCDPVersionV2: _ClassVar[CDPVersion]

class CDPHydrationVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kCDPHydrationV1: _ClassVar[CDPHydrationVersion]
    kCDPHydrationV2: _ClassVar[CDPHydrationVersion]
kCDPVersionV1: CDPVersion
kCDPVersionV2: CDPVersion
kCDPHydrationV1: CDPHydrationVersion
kCDPHydrationV2: CDPHydrationVersion

class UpgradeStatus(_message.Message):
    __slots__ = ()
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kIdle: _ClassVar[UpgradeStatus.State]
        kAccepted: _ClassVar[UpgradeStatus.State]
        kStarted: _ClassVar[UpgradeStatus.State]
        kFinished: _ClassVar[UpgradeStatus.State]
    kIdle: UpgradeStatus.State
    kAccepted: UpgradeStatus.State
    kStarted: UpgradeStatus.State
    kFinished: UpgradeStatus.State
    def __init__(self) -> None: ...

class Upgradability(_message.Message):
    __slots__ = ()
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUpgradable: _ClassVar[Upgradability.State]
        kCurrent: _ClassVar[Upgradability.State]
        kUnknown: _ClassVar[Upgradability.State]
        kNonUpgradableInvalidVersion: _ClassVar[Upgradability.State]
        kNonUpgradableIsNewer: _ClassVar[Upgradability.State]
        kNonUpgradableIsOld: _ClassVar[Upgradability.State]
    kUpgradable: Upgradability.State
    kCurrent: Upgradability.State
    kUnknown: Upgradability.State
    kNonUpgradableInvalidVersion: Upgradability.State
    kNonUpgradableIsNewer: Upgradability.State
    kNonUpgradableIsOld: Upgradability.State
    def __init__(self) -> None: ...

class FilesToDirectoryMapping(_message.Message):
    __slots__ = ("file_pattern", "target_directory")
    FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    file_pattern: str
    target_directory: str
    def __init__(self, file_pattern: _Optional[str] = ..., target_directory: _Optional[str] = ...) -> None: ...

class SystemResourceInfo(_message.Message):
    __slots__ = ("number_of_processors", "total_physical_memory_in_bytes")
    NUMBER_OF_PROCESSORS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PHYSICAL_MEMORY_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    number_of_processors: int
    total_physical_memory_in_bytes: int
    def __init__(self, number_of_processors: _Optional[int] = ..., total_physical_memory_in_bytes: _Optional[int] = ...) -> None: ...

class VlanParams(_message.Message):
    __slots__ = ("vlan_id", "disable_vlan", "interface_name")
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_VLAN_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    vlan_id: int
    disable_vlan: bool
    interface_name: str
    def __init__(self, vlan_id: _Optional[int] = ..., disable_vlan: bool = ..., interface_name: _Optional[str] = ...) -> None: ...

class OrgVDCNetwork(_message.Message):
    __slots__ = ("vcd_uuid", "name", "vcenter_moref_uuid", "network_type")
    VCD_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VCENTER_MOREF_UUID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    vcd_uuid: str
    name: str
    vcenter_moref_uuid: str
    network_type: str
    def __init__(self, vcd_uuid: _Optional[str] = ..., name: _Optional[str] = ..., vcenter_moref_uuid: _Optional[str] = ..., network_type: _Optional[str] = ...) -> None: ...

class IPAddress(_message.Message):
    __slots__ = ("address", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IPV4: _ClassVar[IPAddress.Type]
        IPV6: _ClassVar[IPAddress.Type]
        kUnknown: _ClassVar[IPAddress.Type]
    IPV4: IPAddress.Type
    IPV6: IPAddress.Type
    kUnknown: IPAddress.Type
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    address: str
    type: IPAddress.Type
    def __init__(self, address: _Optional[str] = ..., type: _Optional[_Union[IPAddress.Type, str]] = ...) -> None: ...
