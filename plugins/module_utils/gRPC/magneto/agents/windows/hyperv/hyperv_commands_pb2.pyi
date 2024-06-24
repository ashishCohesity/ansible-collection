from magneto.agents.windows.base import hyperv_pb2 as _hyperv_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PSInvocationInfo(_message.Message):
    __slots__ = ("ScriptLineNumber", "PSCommandPath")
    SCRIPTLINENUMBER_FIELD_NUMBER: _ClassVar[int]
    PSCOMMANDPATH_FIELD_NUMBER: _ClassVar[int]
    ScriptLineNumber: int
    PSCommandPath: str
    def __init__(self, ScriptLineNumber: _Optional[int] = ..., PSCommandPath: _Optional[str] = ...) -> None: ...

class PSCategoryInfo(_message.Message):
    __slots__ = ("Category", "Reason")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    Category: int
    Reason: str
    def __init__(self, Category: _Optional[int] = ..., Reason: _Optional[str] = ...) -> None: ...

class PSException(_message.Message):
    __slots__ = ("Message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Message: str
    def __init__(self, Message: _Optional[str] = ...) -> None: ...

class PSExceptionStack(_message.Message):
    __slots__ = ("Exception", "CategoryInfo", "InvocationInfo")
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORYINFO_FIELD_NUMBER: _ClassVar[int]
    INVOCATIONINFO_FIELD_NUMBER: _ClassVar[int]
    Exception: PSException
    CategoryInfo: PSCategoryInfo
    InvocationInfo: PSInvocationInfo
    def __init__(self, Exception: _Optional[_Union[PSException, _Mapping]] = ..., CategoryInfo: _Optional[_Union[PSCategoryInfo, _Mapping]] = ..., InvocationInfo: _Optional[_Union[PSInvocationInfo, _Mapping]] = ...) -> None: ...

class ManagedComputerInfo(_message.Message):
    __slots__ = ("Name", "FQDN", "ID", "State")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    Name: str
    FQDN: str
    ID: str
    State: int
    def __init__(self, Name: _Optional[str] = ..., FQDN: _Optional[str] = ..., ID: _Optional[str] = ..., State: _Optional[int] = ...) -> None: ...

class SCVMMServerInfo(_message.Message):
    __slots__ = ("Name", "ManagedComputer", "IsHighlyAvailable", "ProductVersion")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MANAGEDCOMPUTER_FIELD_NUMBER: _ClassVar[int]
    ISHIGHLYAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTVERSION_FIELD_NUMBER: _ClassVar[int]
    Name: str
    ManagedComputer: _containers.RepeatedCompositeFieldContainer[ManagedComputerInfo]
    IsHighlyAvailable: bool
    ProductVersion: str
    def __init__(self, Name: _Optional[str] = ..., ManagedComputer: _Optional[_Iterable[_Union[ManagedComputerInfo, _Mapping]]] = ..., IsHighlyAvailable: bool = ..., ProductVersion: _Optional[str] = ...) -> None: ...

class ParentID(_message.Message):
    __slots__ = ("ID",)
    ID_FIELD_NUMBER: _ClassVar[int]
    ID: str
    def __init__(self, ID: _Optional[str] = ...) -> None: ...

class HostGroup(_message.Message):
    __slots__ = ("ID", "Name", "IsRoot", "ParentVMHostGroup", "ParentHostGroup", "Path")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISROOT_FIELD_NUMBER: _ClassVar[int]
    PARENTVMHOSTGROUP_FIELD_NUMBER: _ClassVar[int]
    PARENTHOSTGROUP_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    IsRoot: bool
    ParentVMHostGroup: ParentID
    ParentHostGroup: ParentID
    Path: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., IsRoot: bool = ..., ParentVMHostGroup: _Optional[_Union[ParentID, _Mapping]] = ..., ParentHostGroup: _Optional[_Union[ParentID, _Mapping]] = ..., Path: _Optional[str] = ...) -> None: ...

class HostGroupList(_message.Message):
    __slots__ = ("host_group_vec",)
    HOST_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    host_group_vec: _containers.RepeatedCompositeFieldContainer[HostGroup]
    def __init__(self, host_group_vec: _Optional[_Iterable[_Union[HostGroup, _Mapping]]] = ...) -> None: ...

class HostCluster(_message.Message):
    __slots__ = ("ID", "Name", "ClusterName", "Description", "HostGroupID")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTERNAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOSTGROUPID_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    ClusterName: str
    Description: str
    HostGroupID: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., ClusterName: _Optional[str] = ..., Description: _Optional[str] = ..., HostGroupID: _Optional[str] = ...) -> None: ...

class HostClusterList(_message.Message):
    __slots__ = ("host_cluster_vec",)
    HOST_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    host_cluster_vec: _containers.RepeatedCompositeFieldContainer[HostCluster]
    def __init__(self, host_cluster_vec: _Optional[_Iterable[_Union[HostCluster, _Mapping]]] = ...) -> None: ...

class WindowsVersion(_message.Message):
    __slots__ = ("Major", "Minor", "Build", "Revision")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    Major: int
    Minor: int
    Build: int
    Revision: int
    def __init__(self, Major: _Optional[int] = ..., Minor: _Optional[int] = ..., Build: _Optional[int] = ..., Revision: _Optional[int] = ...) -> None: ...

class HostInfo(_message.Message):
    __slots__ = ("ID", "Name", "VMHostGroup", "HostCluster", "HyperVVersion", "DomainName")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VMHOSTGROUP_FIELD_NUMBER: _ClassVar[int]
    HOSTCLUSTER_FIELD_NUMBER: _ClassVar[int]
    HYPERVVERSION_FIELD_NUMBER: _ClassVar[int]
    DOMAINNAME_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    VMHostGroup: ParentID
    HostCluster: ParentID
    HyperVVersion: WindowsVersion
    DomainName: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., VMHostGroup: _Optional[_Union[ParentID, _Mapping]] = ..., HostCluster: _Optional[_Union[ParentID, _Mapping]] = ..., HyperVVersion: _Optional[_Union[WindowsVersion, _Mapping]] = ..., DomainName: _Optional[str] = ...) -> None: ...

class HostInfoList(_message.Message):
    __slots__ = ("host_info_vec",)
    HOST_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    host_info_vec: _containers.RepeatedCompositeFieldContainer[HostInfo]
    def __init__(self, host_info_vec: _Optional[_Iterable[_Union[HostInfo, _Mapping]]] = ...) -> None: ...

class ClusterAssociation(_message.Message):
    __slots__ = ("Name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    def __init__(self, Name: _Optional[str] = ...) -> None: ...

class HostAssociation(_message.Message):
    __slots__ = ("Name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    def __init__(self, Name: _Optional[str] = ...) -> None: ...

class StorageFileShareInfo(_message.Message):
    __slots__ = ("ID", "Name", "Capacity", "FreeSpace", "ObjectState", "MountPoints", "HostAssociations", "ClusterAssociations")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FREESPACE_FIELD_NUMBER: _ClassVar[int]
    OBJECTSTATE_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINTS_FIELD_NUMBER: _ClassVar[int]
    HOSTASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    CLUSTERASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    Capacity: int
    FreeSpace: int
    ObjectState: int
    MountPoints: _containers.RepeatedScalarFieldContainer[str]
    HostAssociations: _containers.RepeatedCompositeFieldContainer[HostAssociation]
    ClusterAssociations: _containers.RepeatedCompositeFieldContainer[ClusterAssociation]
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., Capacity: _Optional[int] = ..., FreeSpace: _Optional[int] = ..., ObjectState: _Optional[int] = ..., MountPoints: _Optional[_Iterable[str]] = ..., HostAssociations: _Optional[_Iterable[_Union[HostAssociation, _Mapping]]] = ..., ClusterAssociations: _Optional[_Iterable[_Union[ClusterAssociation, _Mapping]]] = ...) -> None: ...

class StorageFileShareList(_message.Message):
    __slots__ = ("storage_file_share_vec",)
    STORAGE_FILE_SHARE_VEC_FIELD_NUMBER: _ClassVar[int]
    storage_file_share_vec: _containers.RepeatedCompositeFieldContainer[StorageFileShareInfo]
    def __init__(self, storage_file_share_vec: _Optional[_Iterable[_Union[StorageFileShareInfo, _Mapping]]] = ...) -> None: ...

class VMHostInfo(_message.Message):
    __slots__ = ("ID",)
    ID_FIELD_NUMBER: _ClassVar[int]
    ID: str
    def __init__(self, ID: _Optional[str] = ...) -> None: ...

class StorageVolumeInfo(_message.Message):
    __slots__ = ("ID", "Name", "Capacity", "FreeSpace", "MountPoints", "VMHost", "IsClustered", "IsClusterSharedVolume", "StorageVolumeID")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FREESPACE_FIELD_NUMBER: _ClassVar[int]
    MOUNTPOINTS_FIELD_NUMBER: _ClassVar[int]
    VMHOST_FIELD_NUMBER: _ClassVar[int]
    ISCLUSTERED_FIELD_NUMBER: _ClassVar[int]
    ISCLUSTERSHAREDVOLUME_FIELD_NUMBER: _ClassVar[int]
    STORAGEVOLUMEID_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    Capacity: int
    FreeSpace: int
    MountPoints: _containers.RepeatedScalarFieldContainer[str]
    VMHost: str
    IsClustered: bool
    IsClusterSharedVolume: bool
    StorageVolumeID: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., Capacity: _Optional[int] = ..., FreeSpace: _Optional[int] = ..., MountPoints: _Optional[_Iterable[str]] = ..., VMHost: _Optional[str] = ..., IsClustered: bool = ..., IsClusterSharedVolume: bool = ..., StorageVolumeID: _Optional[str] = ...) -> None: ...

class StorageVolumeList(_message.Message):
    __slots__ = ("storage_volume_vec",)
    STORAGE_VOLUME_VEC_FIELD_NUMBER: _ClassVar[int]
    storage_volume_vec: _containers.RepeatedCompositeFieldContainer[StorageVolumeInfo]
    def __init__(self, storage_volume_vec: _Optional[_Iterable[_Union[StorageVolumeInfo, _Mapping]]] = ...) -> None: ...

class HostNetworkAdapterInfo(_message.Message):
    __slots__ = ("ID", "Name", "IPAddresses", "ConnectionState", "IPSubnets", "VMHost")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IPADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONSTATE_FIELD_NUMBER: _ClassVar[int]
    IPSUBNETS_FIELD_NUMBER: _ClassVar[int]
    VMHOST_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    IPAddresses: _containers.RepeatedScalarFieldContainer[str]
    ConnectionState: int
    IPSubnets: _containers.RepeatedScalarFieldContainer[str]
    VMHost: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., IPAddresses: _Optional[_Iterable[str]] = ..., ConnectionState: _Optional[int] = ..., IPSubnets: _Optional[_Iterable[str]] = ..., VMHost: _Optional[str] = ...) -> None: ...

class HostNetworkAdapterInfoList(_message.Message):
    __slots__ = ("host_adapter_vec",)
    HOST_ADAPTER_VEC_FIELD_NUMBER: _ClassVar[int]
    host_adapter_vec: _containers.RepeatedCompositeFieldContainer[HostNetworkAdapterInfo]
    def __init__(self, host_adapter_vec: _Optional[_Iterable[_Union[HostNetworkAdapterInfo, _Mapping]]] = ...) -> None: ...

class VirtualSwitchInfo(_message.Message):
    __slots__ = ("ID", "Name", "VMHostID", "VMHost")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VMHOSTID_FIELD_NUMBER: _ClassVar[int]
    VMHOST_FIELD_NUMBER: _ClassVar[int]
    ID: str
    Name: str
    VMHostID: str
    VMHost: str
    def __init__(self, ID: _Optional[str] = ..., Name: _Optional[str] = ..., VMHostID: _Optional[str] = ..., VMHost: _Optional[str] = ...) -> None: ...

class VirtualSwitchInfoList(_message.Message):
    __slots__ = ("virtual_switch_info_vec",)
    VIRTUAL_SWITCH_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    virtual_switch_info_vec: _containers.RepeatedCompositeFieldContainer[VirtualSwitchInfo]
    def __init__(self, virtual_switch_info_vec: _Optional[_Iterable[_Union[VirtualSwitchInfo, _Mapping]]] = ...) -> None: ...

class VirtualHardDiskInfo(_message.Message):
    __slots__ = ("ID", "VHDType", "DiskFormat", "MaximumSize", "Size", "Location", "Name", "Enabled", "HostVolumeId", "HostVolume")
    ID_FIELD_NUMBER: _ClassVar[int]
    VHDTYPE_FIELD_NUMBER: _ClassVar[int]
    DISKFORMAT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUMSIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOSTVOLUMEID_FIELD_NUMBER: _ClassVar[int]
    HOSTVOLUME_FIELD_NUMBER: _ClassVar[int]
    ID: str
    VHDType: int
    DiskFormat: int
    MaximumSize: int
    Size: int
    Location: str
    Name: str
    Enabled: bool
    HostVolumeId: str
    HostVolume: str
    def __init__(self, ID: _Optional[str] = ..., VHDType: _Optional[int] = ..., DiskFormat: _Optional[int] = ..., MaximumSize: _Optional[int] = ..., Size: _Optional[int] = ..., Location: _Optional[str] = ..., Name: _Optional[str] = ..., Enabled: bool = ..., HostVolumeId: _Optional[str] = ..., HostVolume: _Optional[str] = ...) -> None: ...

class VirtualDiskDriveInfo(_message.Message):
    __slots__ = ("ID", "VirtualHardDiskId", "BusType", "Bus", "Lun", "VolumeType")
    ID_FIELD_NUMBER: _ClassVar[int]
    VIRTUALHARDDISKID_FIELD_NUMBER: _ClassVar[int]
    BUSTYPE_FIELD_NUMBER: _ClassVar[int]
    BUS_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    VOLUMETYPE_FIELD_NUMBER: _ClassVar[int]
    ID: str
    VirtualHardDiskId: str
    BusType: int
    Bus: int
    Lun: int
    VolumeType: int
    def __init__(self, ID: _Optional[str] = ..., VirtualHardDiskId: _Optional[str] = ..., BusType: _Optional[int] = ..., Bus: _Optional[int] = ..., Lun: _Optional[int] = ..., VolumeType: _Optional[int] = ...) -> None: ...

class VMOperatingSystem(_message.Message):
    __slots__ = ("Name", "OSType")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OSTYPE_FIELD_NUMBER: _ClassVar[int]
    Name: str
    OSType: int
    def __init__(self, Name: _Optional[str] = ..., OSType: _Optional[int] = ...) -> None: ...

class VirtualNetworkAdapters(_message.Message):
    __slots__ = ("IPv4Addresses", "IPv6Addresses")
    IPV4ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    IPV6ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    IPv4Addresses: _containers.RepeatedScalarFieldContainer[str]
    IPv6Addresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, IPv4Addresses: _Optional[_Iterable[str]] = ..., IPv6Addresses: _Optional[_Iterable[str]] = ...) -> None: ...

class VMCheckpoint(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SCVMMVirtualHardDiskInfo(_message.Message):
    __slots__ = ("VirtualHardDiskId", "BusType", "Bus", "Lun", "ID")
    VIRTUALHARDDISKID_FIELD_NUMBER: _ClassVar[int]
    BUSTYPE_FIELD_NUMBER: _ClassVar[int]
    BUS_FIELD_NUMBER: _ClassVar[int]
    LUN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VirtualHardDiskId: str
    BusType: int
    Bus: int
    Lun: int
    ID: str
    def __init__(self, VirtualHardDiskId: _Optional[str] = ..., BusType: _Optional[int] = ..., Bus: _Optional[int] = ..., Lun: _Optional[int] = ..., ID: _Optional[str] = ...) -> None: ...

class SCVMMVirtualHardDiskInfoList(_message.Message):
    __slots__ = ("vhd_info_vec",)
    VHD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vhd_info_vec: _containers.RepeatedCompositeFieldContainer[SCVMMVirtualHardDiskInfo]
    def __init__(self, vhd_info_vec: _Optional[_Iterable[_Union[SCVMMVirtualHardDiskInfo, _Mapping]]] = ...) -> None: ...

class SCVMMCmdVMInfo(_message.Message):
    __slots__ = ("ID", "VMId", "Name", "HostId", "VirtualHardDisks", "IsHighlyAvailable", "Status", "Version", "Generation", "TotalSize", "ComputerName", "OperatingSystem", "Tag", "VirtualNetworkAdapters", "VMCheckpoints")
    ID_FIELD_NUMBER: _ClassVar[int]
    VMID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTID_FIELD_NUMBER: _ClassVar[int]
    VIRTUALHARDDISKS_FIELD_NUMBER: _ClassVar[int]
    ISHIGHLYAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    TOTALSIZE_FIELD_NUMBER: _ClassVar[int]
    COMPUTERNAME_FIELD_NUMBER: _ClassVar[int]
    OPERATINGSYSTEM_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    VIRTUALNETWORKADAPTERS_FIELD_NUMBER: _ClassVar[int]
    VMCHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    ID: str
    VMId: str
    Name: str
    HostId: str
    VirtualHardDisks: _containers.RepeatedCompositeFieldContainer[VirtualHardDiskInfo]
    IsHighlyAvailable: bool
    Status: int
    Version: str
    Generation: int
    TotalSize: int
    ComputerName: str
    OperatingSystem: VMOperatingSystem
    Tag: str
    VirtualNetworkAdapters: _containers.RepeatedCompositeFieldContainer[VirtualNetworkAdapters]
    VMCheckpoints: _containers.RepeatedCompositeFieldContainer[VMCheckpoint]
    def __init__(self, ID: _Optional[str] = ..., VMId: _Optional[str] = ..., Name: _Optional[str] = ..., HostId: _Optional[str] = ..., VirtualHardDisks: _Optional[_Iterable[_Union[VirtualHardDiskInfo, _Mapping]]] = ..., IsHighlyAvailable: bool = ..., Status: _Optional[int] = ..., Version: _Optional[str] = ..., Generation: _Optional[int] = ..., TotalSize: _Optional[int] = ..., ComputerName: _Optional[str] = ..., OperatingSystem: _Optional[_Union[VMOperatingSystem, _Mapping]] = ..., Tag: _Optional[str] = ..., VirtualNetworkAdapters: _Optional[_Iterable[_Union[VirtualNetworkAdapters, _Mapping]]] = ..., VMCheckpoints: _Optional[_Iterable[_Union[VMCheckpoint, _Mapping]]] = ...) -> None: ...

class VMInfoList(_message.Message):
    __slots__ = ("vm_info_vec",)
    VM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_info_vec: _containers.RepeatedCompositeFieldContainer[SCVMMCmdVMInfo]
    def __init__(self, vm_info_vec: _Optional[_Iterable[_Union[SCVMMCmdVMInfo, _Mapping]]] = ...) -> None: ...

class VMNetworkAdapterInfo(_message.Message):
    __slots__ = ("IPAddresses",)
    IPADDRESSES_FIELD_NUMBER: _ClassVar[int]
    IPAddresses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, IPAddresses: _Optional[_Iterable[str]] = ...) -> None: ...

class SCVMMVMCustomProperty(_message.Message):
    __slots__ = ("Name", "Value", "ObjectID", "CustomPropertyID")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMPROPERTYID_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Value: str
    ObjectID: str
    CustomPropertyID: str
    def __init__(self, Name: _Optional[str] = ..., Value: _Optional[str] = ..., ObjectID: _Optional[str] = ..., CustomPropertyID: _Optional[str] = ...) -> None: ...

class VMCustomPropertyList(_message.Message):
    __slots__ = ("vm_custom_property_vec",)
    VM_CUSTOM_PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_custom_property_vec: _containers.RepeatedCompositeFieldContainer[SCVMMVMCustomProperty]
    def __init__(self, vm_custom_property_vec: _Optional[_Iterable[_Union[SCVMMVMCustomProperty, _Mapping]]] = ...) -> None: ...

class HyperVCmdVMInfo(_message.Message):
    __slots__ = ("ID", "VMId", "Name", "Path", "ConfigurationLocation", "SmartPagingFilepath", "CheckpointFileLocation", "IsClustered", "SnapshotFileLocation", "State", "Version", "Generation", "NetworkAdapters", "HardDrives", "ComputerName")
    ID_FIELD_NUMBER: _ClassVar[int]
    VMID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONLOCATION_FIELD_NUMBER: _ClassVar[int]
    SMARTPAGINGFILEPATH_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINTFILELOCATION_FIELD_NUMBER: _ClassVar[int]
    ISCLUSTERED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTFILELOCATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    NETWORKADAPTERS_FIELD_NUMBER: _ClassVar[int]
    HARDDRIVES_FIELD_NUMBER: _ClassVar[int]
    COMPUTERNAME_FIELD_NUMBER: _ClassVar[int]
    ID: str
    VMId: str
    Name: str
    Path: str
    ConfigurationLocation: str
    SmartPagingFilepath: str
    CheckpointFileLocation: str
    IsClustered: bool
    SnapshotFileLocation: str
    State: int
    Version: str
    Generation: int
    NetworkAdapters: _containers.RepeatedCompositeFieldContainer[VMNetworkAdapterInfo]
    HardDrives: _containers.RepeatedCompositeFieldContainer[VMHardDiskDrive]
    ComputerName: str
    def __init__(self, ID: _Optional[str] = ..., VMId: _Optional[str] = ..., Name: _Optional[str] = ..., Path: _Optional[str] = ..., ConfigurationLocation: _Optional[str] = ..., SmartPagingFilepath: _Optional[str] = ..., CheckpointFileLocation: _Optional[str] = ..., IsClustered: bool = ..., SnapshotFileLocation: _Optional[str] = ..., State: _Optional[int] = ..., Version: _Optional[str] = ..., Generation: _Optional[int] = ..., NetworkAdapters: _Optional[_Iterable[_Union[VMNetworkAdapterInfo, _Mapping]]] = ..., HardDrives: _Optional[_Iterable[_Union[VMHardDiskDrive, _Mapping]]] = ..., ComputerName: _Optional[str] = ...) -> None: ...

class HyperVCmdVMInfoList(_message.Message):
    __slots__ = ("host_vm_info_vec",)
    HOST_VM_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    host_vm_info_vec: _containers.RepeatedCompositeFieldContainer[HyperVCmdVMInfo]
    def __init__(self, host_vm_info_vec: _Optional[_Iterable[_Union[HyperVCmdVMInfo, _Mapping]]] = ...) -> None: ...

class RealizedVMInfo(_message.Message):
    __slots__ = ("ID", "VMId", "Name", "ElementName", "HostId", "VirtualHardDisks", "VirtualDiskDrives")
    ID_FIELD_NUMBER: _ClassVar[int]
    VMID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ELEMENTNAME_FIELD_NUMBER: _ClassVar[int]
    HOSTID_FIELD_NUMBER: _ClassVar[int]
    VIRTUALHARDDISKS_FIELD_NUMBER: _ClassVar[int]
    VIRTUALDISKDRIVES_FIELD_NUMBER: _ClassVar[int]
    ID: str
    VMId: str
    Name: str
    ElementName: str
    HostId: str
    VirtualHardDisks: _containers.RepeatedCompositeFieldContainer[VirtualHardDiskInfo]
    VirtualDiskDrives: _containers.RepeatedCompositeFieldContainer[VirtualDiskDriveInfo]
    def __init__(self, ID: _Optional[str] = ..., VMId: _Optional[str] = ..., Name: _Optional[str] = ..., ElementName: _Optional[str] = ..., HostId: _Optional[str] = ..., VirtualHardDisks: _Optional[_Iterable[_Union[VirtualHardDiskInfo, _Mapping]]] = ..., VirtualDiskDrives: _Optional[_Iterable[_Union[VirtualDiskDriveInfo, _Mapping]]] = ...) -> None: ...

class VMCheckpointInfo(_message.Message):
    __slots__ = ("InstanceID", "ElementName", "UserSnapshotType", "ConfigurationDataRoot", "ConfigurationFile", "ConfigurationID", "VirtualSystemType")
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    ELEMENTNAME_FIELD_NUMBER: _ClassVar[int]
    USERSNAPSHOTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONDATAROOT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONFILE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONID_FIELD_NUMBER: _ClassVar[int]
    VIRTUALSYSTEMTYPE_FIELD_NUMBER: _ClassVar[int]
    InstanceID: str
    ElementName: str
    UserSnapshotType: int
    ConfigurationDataRoot: str
    ConfigurationFile: str
    ConfigurationID: str
    VirtualSystemType: str
    def __init__(self, InstanceID: _Optional[str] = ..., ElementName: _Optional[str] = ..., UserSnapshotType: _Optional[int] = ..., ConfigurationDataRoot: _Optional[str] = ..., ConfigurationFile: _Optional[str] = ..., ConfigurationID: _Optional[str] = ..., VirtualSystemType: _Optional[str] = ...) -> None: ...

class VMReferencepointInfo(_message.Message):
    __slots__ = ("InstanceID", "ElementName", "ConsistencyLevel", "ReferencePointType", "ResilientChangeTrackingIdentifiers", "VirtualDiskIdentifiers", "VirtualSystemIdentifier")
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    ELEMENTNAME_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCYLEVEL_FIELD_NUMBER: _ClassVar[int]
    REFERENCEPOINTTYPE_FIELD_NUMBER: _ClassVar[int]
    RESILIENTCHANGETRACKINGIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    VIRTUALDISKIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    VIRTUALSYSTEMIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    InstanceID: str
    ElementName: str
    ConsistencyLevel: _hyperv_pb2.ConsistencyLevel.Type
    ReferencePointType: _hyperv_pb2.ReferencePointType.Type
    ResilientChangeTrackingIdentifiers: _containers.RepeatedScalarFieldContainer[str]
    VirtualDiskIdentifiers: _containers.RepeatedScalarFieldContainer[str]
    VirtualSystemIdentifier: str
    def __init__(self, InstanceID: _Optional[str] = ..., ElementName: _Optional[str] = ..., ConsistencyLevel: _Optional[_Union[_hyperv_pb2.ConsistencyLevel.Type, str]] = ..., ReferencePointType: _Optional[_Union[_hyperv_pb2.ReferencePointType.Type, str]] = ..., ResilientChangeTrackingIdentifiers: _Optional[_Iterable[str]] = ..., VirtualDiskIdentifiers: _Optional[_Iterable[str]] = ..., VirtualSystemIdentifier: _Optional[str] = ...) -> None: ...

class VMDiskInfo(_message.Message):
    __slots__ = ("DiskPath", "DiskId", "VirtualSizeBytes", "InstanceID", "DiskFormat", "DiskType", "BlockSize", "LogicalSectorSize", "VMBaseDiskPath", "ParentPath", "IsShared", "ControllerType", "ControllerNumber", "ControllerLocation")
    DISKPATH_FIELD_NUMBER: _ClassVar[int]
    DISKID_FIELD_NUMBER: _ClassVar[int]
    VIRTUALSIZEBYTES_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    DISKFORMAT_FIELD_NUMBER: _ClassVar[int]
    DISKTYPE_FIELD_NUMBER: _ClassVar[int]
    BLOCKSIZE_FIELD_NUMBER: _ClassVar[int]
    LOGICALSECTORSIZE_FIELD_NUMBER: _ClassVar[int]
    VMBASEDISKPATH_FIELD_NUMBER: _ClassVar[int]
    PARENTPATH_FIELD_NUMBER: _ClassVar[int]
    ISSHARED_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERNUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERLOCATION_FIELD_NUMBER: _ClassVar[int]
    DiskPath: str
    DiskId: str
    VirtualSizeBytes: int
    InstanceID: str
    DiskFormat: int
    DiskType: int
    BlockSize: int
    LogicalSectorSize: int
    VMBaseDiskPath: str
    ParentPath: str
    IsShared: bool
    ControllerType: int
    ControllerNumber: int
    ControllerLocation: int
    def __init__(self, DiskPath: _Optional[str] = ..., DiskId: _Optional[str] = ..., VirtualSizeBytes: _Optional[int] = ..., InstanceID: _Optional[str] = ..., DiskFormat: _Optional[int] = ..., DiskType: _Optional[int] = ..., BlockSize: _Optional[int] = ..., LogicalSectorSize: _Optional[int] = ..., VMBaseDiskPath: _Optional[str] = ..., ParentPath: _Optional[str] = ..., IsShared: bool = ..., ControllerType: _Optional[int] = ..., ControllerNumber: _Optional[int] = ..., ControllerLocation: _Optional[int] = ...) -> None: ...

class VMDiskInfoList(_message.Message):
    __slots__ = ("vm_disk_info_vec",)
    VM_DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_disk_info_vec: _containers.RepeatedCompositeFieldContainer[VMDiskInfo]
    def __init__(self, vm_disk_info_vec: _Optional[_Iterable[_Union[VMDiskInfo, _Mapping]]] = ...) -> None: ...

class PlannedVMInfo(_message.Message):
    __slots__ = ("Name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    def __init__(self, Name: _Optional[str] = ...) -> None: ...

class WMIJob(_message.Message):
    __slots__ = ("ErrorCode", "ErrorDescription", "ErrorSummaryDescription", "InstanceID", "JobState", "PercentComplete")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ERRORSUMMARYDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    JOBSTATE_FIELD_NUMBER: _ClassVar[int]
    PERCENTCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    ErrorCode: int
    ErrorDescription: str
    ErrorSummaryDescription: str
    InstanceID: str
    JobState: int
    PercentComplete: int
    def __init__(self, ErrorCode: _Optional[int] = ..., ErrorDescription: _Optional[str] = ..., ErrorSummaryDescription: _Optional[str] = ..., InstanceID: _Optional[str] = ..., JobState: _Optional[int] = ..., PercentComplete: _Optional[int] = ...) -> None: ...

class WMIMethodReturn(_message.Message):
    __slots__ = ("ReturnValue", "Job", "ProcessId")
    RETURNVALUE_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    PROCESSID_FIELD_NUMBER: _ClassVar[int]
    ReturnValue: int
    Job: str
    ProcessId: int
    def __init__(self, ReturnValue: _Optional[int] = ..., Job: _Optional[str] = ..., ProcessId: _Optional[int] = ...) -> None: ...

class VMHardDiskDrive(_message.Message):
    __slots__ = ("ControllerLocation", "ControllerNumber", "Id", "VMId", "Size", "Path", "Name", "MaximumSize", "ControllerType")
    CONTROLLERLOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERNUMBER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VMID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAXIMUMSIZE_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERTYPE_FIELD_NUMBER: _ClassVar[int]
    ControllerLocation: int
    ControllerNumber: int
    Id: str
    VMId: str
    Size: int
    Path: str
    Name: str
    MaximumSize: int
    ControllerType: int
    def __init__(self, ControllerLocation: _Optional[int] = ..., ControllerNumber: _Optional[int] = ..., Id: _Optional[str] = ..., VMId: _Optional[str] = ..., Size: _Optional[int] = ..., Path: _Optional[str] = ..., Name: _Optional[str] = ..., MaximumSize: _Optional[int] = ..., ControllerType: _Optional[int] = ...) -> None: ...

class WMIProcess(_message.Message):
    __slots__ = ("Handle", "ProcessName")
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    PROCESSNAME_FIELD_NUMBER: _ClassVar[int]
    Handle: int
    ProcessName: str
    def __init__(self, Handle: _Optional[int] = ..., ProcessName: _Optional[str] = ...) -> None: ...

class WMIProcessList(_message.Message):
    __slots__ = ("wmi_process_vec",)
    WMI_PROCESS_VEC_FIELD_NUMBER: _ClassVar[int]
    wmi_process_vec: _containers.RepeatedCompositeFieldContainer[WMIProcess]
    def __init__(self, wmi_process_vec: _Optional[_Iterable[_Union[WMIProcess, _Mapping]]] = ...) -> None: ...

class WMIDirectory(_message.Message):
    __slots__ = ("Name", "CSName", "Readable", "Writeable")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CSNAME_FIELD_NUMBER: _ClassVar[int]
    READABLE_FIELD_NUMBER: _ClassVar[int]
    WRITEABLE_FIELD_NUMBER: _ClassVar[int]
    Name: str
    CSName: str
    Readable: bool
    Writeable: bool
    def __init__(self, Name: _Optional[str] = ..., CSName: _Optional[str] = ..., Readable: bool = ..., Writeable: bool = ...) -> None: ...

class WMIOsInfo(_message.Message):
    __slots__ = ("OSArchitecture", "Version")
    OSARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OSArchitecture: str
    Version: str
    def __init__(self, OSArchitecture: _Optional[str] = ..., Version: _Optional[str] = ...) -> None: ...

class ScsiController(_message.Message):
    __slots__ = ("Id", "Drives")
    ID_FIELD_NUMBER: _ClassVar[int]
    DRIVES_FIELD_NUMBER: _ClassVar[int]
    Id: str
    Drives: _containers.RepeatedCompositeFieldContainer[VMHardDiskDrive]
    def __init__(self, Id: _Optional[str] = ..., Drives: _Optional[_Iterable[_Union[VMHardDiskDrive, _Mapping]]] = ...) -> None: ...

class ScsiControllerList(_message.Message):
    __slots__ = ("scsi_controller_vec",)
    SCSI_CONTROLLER_VEC_FIELD_NUMBER: _ClassVar[int]
    scsi_controller_vec: _containers.RepeatedCompositeFieldContainer[ScsiController]
    def __init__(self, scsi_controller_vec: _Optional[_Iterable[_Union[ScsiController, _Mapping]]] = ...) -> None: ...

class ChildItem(_message.Message):
    __slots__ = ("Name", "DirectoryName", "FullName")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTORYNAME_FIELD_NUMBER: _ClassVar[int]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    DirectoryName: str
    FullName: str
    def __init__(self, Name: _Optional[str] = ..., DirectoryName: _Optional[str] = ..., FullName: _Optional[str] = ...) -> None: ...

class ChildItemList(_message.Message):
    __slots__ = ("child_item_vec",)
    CHILD_ITEM_VEC_FIELD_NUMBER: _ClassVar[int]
    child_item_vec: _containers.RepeatedCompositeFieldContainer[ChildItem]
    def __init__(self, child_item_vec: _Optional[_Iterable[_Union[ChildItem, _Mapping]]] = ...) -> None: ...

class ComputerSystem(_message.Message):
    __slots__ = ("Name", "Domain", "DNSHostName")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DNSHOSTNAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    Domain: str
    DNSHostName: str
    def __init__(self, Name: _Optional[str] = ..., Domain: _Optional[str] = ..., DNSHostName: _Optional[str] = ...) -> None: ...

class VMHardDiskDriveList(_message.Message):
    __slots__ = ("vm_hdd_info_vec",)
    VM_HDD_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    vm_hdd_info_vec: _containers.RepeatedCompositeFieldContainer[VMHardDiskDrive]
    def __init__(self, vm_hdd_info_vec: _Optional[_Iterable[_Union[VMHardDiskDrive, _Mapping]]] = ...) -> None: ...
