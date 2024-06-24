from util.disklib.base import enums_pb2 as _enums_pb2
from yoda.base import yoda_types_pb2 as _yoda_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTree(_message.Message):
    __slots__ = ("type", "child_vec", "stripe_size", "device_length", "device_id", "thin_pool_chunk_size")
    class CombineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LINEAR: _ClassVar[DeviceTree.CombineType]
        STRIPE: _ClassVar[DeviceTree.CombineType]
        MIRROR: _ClassVar[DeviceTree.CombineType]
        RAID5: _ClassVar[DeviceTree.CombineType]
        RAID6: _ClassVar[DeviceTree.CombineType]
        ZERO: _ClassVar[DeviceTree.CombineType]
        THIN: _ClassVar[DeviceTree.CombineType]
        THINPOOL: _ClassVar[DeviceTree.CombineType]
        SNAPSHOT: _ClassVar[DeviceTree.CombineType]
        CACHE: _ClassVar[DeviceTree.CombineType]
        CACHEPOOL: _ClassVar[DeviceTree.CombineType]
    LINEAR: DeviceTree.CombineType
    STRIPE: DeviceTree.CombineType
    MIRROR: DeviceTree.CombineType
    RAID5: DeviceTree.CombineType
    RAID6: DeviceTree.CombineType
    ZERO: DeviceTree.CombineType
    THIN: DeviceTree.CombineType
    THINPOOL: DeviceTree.CombineType
    SNAPSHOT: DeviceTree.CombineType
    CACHE: DeviceTree.CombineType
    CACHEPOOL: DeviceTree.CombineType
    class PartitionSlice(_message.Message):
        __slots__ = ("disk_file_name", "partition_number", "offset", "length", "lvm_data_offset")
        DISK_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        PARTITION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        LVM_DATA_OFFSET_FIELD_NUMBER: _ClassVar[int]
        disk_file_name: str
        partition_number: int
        offset: int
        length: int
        lvm_data_offset: int
        def __init__(self, disk_file_name: _Optional[str] = ..., partition_number: _Optional[int] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., lvm_data_offset: _Optional[int] = ...) -> None: ...
    class ChildDevice(_message.Message):
        __slots__ = ("partition_slice", "device", "device_type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kUnknown: _ClassVar[DeviceTree.ChildDevice.Type]
            kThinPoolMetadata: _ClassVar[DeviceTree.ChildDevice.Type]
            kThinPoolData: _ClassVar[DeviceTree.ChildDevice.Type]
        kUnknown: DeviceTree.ChildDevice.Type
        kThinPoolMetadata: DeviceTree.ChildDevice.Type
        kThinPoolData: DeviceTree.ChildDevice.Type
        PARTITION_SLICE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        partition_slice: DeviceTree.PartitionSlice
        device: DeviceTree
        device_type: DeviceTree.ChildDevice.Type
        def __init__(self, partition_slice: _Optional[_Union[DeviceTree.PartitionSlice, _Mapping]] = ..., device: _Optional[_Union[DeviceTree, _Mapping]] = ..., device_type: _Optional[_Union[DeviceTree.ChildDevice.Type, str]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHILD_VEC_FIELD_NUMBER: _ClassVar[int]
    STRIPE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    THIN_POOL_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    type: DeviceTree.CombineType
    child_vec: _containers.RepeatedCompositeFieldContainer[DeviceTree.ChildDevice]
    stripe_size: int
    device_length: int
    device_id: int
    thin_pool_chunk_size: int
    def __init__(self, type: _Optional[_Union[DeviceTree.CombineType, str]] = ..., child_vec: _Optional[_Iterable[_Union[DeviceTree.ChildDevice, _Mapping]]] = ..., stripe_size: _Optional[int] = ..., device_length: _Optional[int] = ..., device_id: _Optional[int] = ..., thin_pool_chunk_size: _Optional[int] = ...) -> None: ...

class VolumeInfo(_message.Message):
    __slots__ = ("disk_vec", "is_supported", "volume_type", "fs_uuid", "fs_label", "volume_guid", "filesystem_type", "display_name", "lv_info", "is_bootable", "is_dedup", "volume_identifier", "subvol_info", "volume_source_type")
    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSimpleVolume: _ClassVar[VolumeInfo.VolumeType]
        kLVM: _ClassVar[VolumeInfo.VolumeType]
        kLDM: _ClassVar[VolumeInfo.VolumeType]
    kSimpleVolume: VolumeInfo.VolumeType
    kLVM: VolumeInfo.VolumeType
    kLDM: VolumeInfo.VolumeType
    class VolumeSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kLocal: _ClassVar[VolumeInfo.VolumeSourceType]
        kArchive: _ClassVar[VolumeInfo.VolumeSourceType]
    kLocal: VolumeInfo.VolumeSourceType
    kArchive: VolumeInfo.VolumeSourceType
    class DiskInfo(_message.Message):
        __slots__ = ("disk_file_name", "vmdk_size", "partition_type", "disk_uuid", "disk_format", "physical_range_vec", "sector_size", "partition_vec")
        class PhysicalRange(_message.Message):
            __slots__ = ("offset", "length")
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            LENGTH_FIELD_NUMBER: _ClassVar[int]
            offset: int
            length: int
            def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
        class PartitionInfo(_message.Message):
            __slots__ = ("partition_number", "start_offset", "length", "partition_uuid", "partition_type_uuid")
            PARTITION_NUMBER_FIELD_NUMBER: _ClassVar[int]
            START_OFFSET_FIELD_NUMBER: _ClassVar[int]
            LENGTH_FIELD_NUMBER: _ClassVar[int]
            PARTITION_UUID_FIELD_NUMBER: _ClassVar[int]
            PARTITION_TYPE_UUID_FIELD_NUMBER: _ClassVar[int]
            partition_number: int
            start_offset: int
            length: int
            partition_uuid: str
            partition_type_uuid: str
            def __init__(self, partition_number: _Optional[int] = ..., start_offset: _Optional[int] = ..., length: _Optional[int] = ..., partition_uuid: _Optional[str] = ..., partition_type_uuid: _Optional[str] = ...) -> None: ...
        DISK_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        VMDK_SIZE_FIELD_NUMBER: _ClassVar[int]
        PARTITION_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISK_UUID_FIELD_NUMBER: _ClassVar[int]
        DISK_FORMAT_FIELD_NUMBER: _ClassVar[int]
        PHYSICAL_RANGE_VEC_FIELD_NUMBER: _ClassVar[int]
        SECTOR_SIZE_FIELD_NUMBER: _ClassVar[int]
        PARTITION_VEC_FIELD_NUMBER: _ClassVar[int]
        disk_file_name: str
        vmdk_size: int
        partition_type: _yoda_types_pb2.DiskPartitionType.PartitionType
        disk_uuid: str
        disk_format: _enums_pb2.DiskFormat.Type
        physical_range_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfo.DiskInfo.PhysicalRange]
        sector_size: int
        partition_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfo.DiskInfo.PartitionInfo]
        def __init__(self, disk_file_name: _Optional[str] = ..., vmdk_size: _Optional[int] = ..., partition_type: _Optional[_Union[_yoda_types_pb2.DiskPartitionType.PartitionType, str]] = ..., disk_uuid: _Optional[str] = ..., disk_format: _Optional[_Union[_enums_pb2.DiskFormat.Type, str]] = ..., physical_range_vec: _Optional[_Iterable[_Union[VolumeInfo.DiskInfo.PhysicalRange, _Mapping]]] = ..., sector_size: _Optional[int] = ..., partition_vec: _Optional[_Iterable[_Union[VolumeInfo.DiskInfo.PartitionInfo, _Mapping]]] = ...) -> None: ...
    class LogicalVolumeInfo(_message.Message):
        __slots__ = ("volume_group_uuid", "volume_group_name", "logical_volume_uuid", "logical_volume_name", "device_tree")
        VOLUME_GROUP_UUID_FIELD_NUMBER: _ClassVar[int]
        VOLUME_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_VOLUME_UUID_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TREE_FIELD_NUMBER: _ClassVar[int]
        volume_group_uuid: str
        volume_group_name: str
        logical_volume_uuid: str
        logical_volume_name: str
        device_tree: DeviceTree
        def __init__(self, volume_group_uuid: _Optional[str] = ..., volume_group_name: _Optional[str] = ..., logical_volume_uuid: _Optional[str] = ..., logical_volume_name: _Optional[str] = ..., device_tree: _Optional[_Union[DeviceTree, _Mapping]] = ...) -> None: ...
    class SubVolumeInfo(_message.Message):
        __slots__ = ("subvolume_name",)
        SUBVOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
        subvolume_name: str
        def __init__(self, subvolume_name: _Optional[str] = ...) -> None: ...
    DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    IS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FS_UUID_FIELD_NUMBER: _ClassVar[int]
    FS_LABEL_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LV_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_BOOTABLE_FIELD_NUMBER: _ClassVar[int]
    IS_DEDUP_FIELD_NUMBER: _ClassVar[int]
    VOLUME_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SUBVOL_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    disk_vec: _containers.RepeatedCompositeFieldContainer[VolumeInfo.DiskInfo]
    is_supported: bool
    volume_type: VolumeInfo.VolumeType
    fs_uuid: str
    fs_label: str
    volume_guid: str
    filesystem_type: str
    display_name: str
    lv_info: VolumeInfo.LogicalVolumeInfo
    is_bootable: bool
    is_dedup: bool
    volume_identifier: int
    subvol_info: VolumeInfo.SubVolumeInfo
    volume_source_type: VolumeInfo.VolumeSourceType
    def __init__(self, disk_vec: _Optional[_Iterable[_Union[VolumeInfo.DiskInfo, _Mapping]]] = ..., is_supported: bool = ..., volume_type: _Optional[_Union[VolumeInfo.VolumeType, str]] = ..., fs_uuid: _Optional[str] = ..., fs_label: _Optional[str] = ..., volume_guid: _Optional[str] = ..., filesystem_type: _Optional[str] = ..., display_name: _Optional[str] = ..., lv_info: _Optional[_Union[VolumeInfo.LogicalVolumeInfo, _Mapping]] = ..., is_bootable: bool = ..., is_dedup: bool = ..., volume_identifier: _Optional[int] = ..., subvol_info: _Optional[_Union[VolumeInfo.SubVolumeInfo, _Mapping]] = ..., volume_source_type: _Optional[_Union[VolumeInfo.VolumeSourceType, str]] = ...) -> None: ...

class VolumeNameMap(_message.Message):
    __slots__ = ("volume_name_map",)
    class VolumeNameMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: VolumeInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[VolumeInfo, _Mapping]] = ...) -> None: ...
    VOLUME_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    volume_name_map: _containers.MessageMap[str, VolumeInfo]
    def __init__(self, volume_name_map: _Optional[_Mapping[str, VolumeInfo]] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("type", "path")
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[Device.DeviceType]
        kLoopBack: _ClassVar[Device.DeviceType]
        kDevMapper: _ClassVar[Device.DeviceType]
        kMountPoint: _ClassVar[Device.DeviceType]
    kUnknown: Device.DeviceType
    kLoopBack: Device.DeviceType
    kDevMapper: Device.DeviceType
    kMountPoint: Device.DeviceType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    type: Device.DeviceType
    path: str
    def __init__(self, type: _Optional[_Union[Device.DeviceType, str]] = ..., path: _Optional[str] = ...) -> None: ...
