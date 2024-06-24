from heimdall.master.base import master_pb2 as _master_pb2
from heimdall.master.stub import rpc_service_pb2 as _rpc_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kGP3: _ClassVar[DiskType]
    kGP2: _ClassVar[DiskType]
kGP3: DiskType
kGP2: DiskType

class AWSAcquireFleetArg(_message.Message):
    __slots__ = ("region", "vpc_id", "subnet", "tags", "os_type")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AWS_ACQUIRE_FLEET_ARG_FIELD_NUMBER: _ClassVar[int]
    aws_acquire_fleet_arg: _descriptor.FieldDescriptor
    AWS_ACQUIRE_FLEET_RESOURCE_ARG_FIELD_NUMBER: _ClassVar[int]
    aws_acquire_fleet_resource_arg: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    region: str
    vpc_id: str
    subnet: str
    tags: _containers.ScalarMap[str, str]
    os_type: _rpc_service_pb2.FleetOSType
    def __init__(self, region: _Optional[str] = ..., vpc_id: _Optional[str] = ..., subnet: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., os_type: _Optional[_Union[_rpc_service_pb2.FleetOSType, str]] = ...) -> None: ...

class AWSAcquireFleetResult(_message.Message):
    __slots__ = ("ip_address", "fleet_id")
    AWS_ACQUIRE_FLEET_RESULT_FIELD_NUMBER: _ClassVar[int]
    aws_acquire_fleet_result: _descriptor.FieldDescriptor
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FLEET_ID_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    fleet_id: str
    def __init__(self, ip_address: _Optional[str] = ..., fleet_id: _Optional[str] = ...) -> None: ...

class AWSFleetInfo(_message.Message):
    __slots__ = ("region", "availability_zone", "vpc_id", "subnet", "network_security_group_vec", "instance_type", "ami_id", "tags", "instance_id")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AWS_FLEET_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_fleet_info: _descriptor.FieldDescriptor
    AWS_CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    aws_connector_params: _descriptor.FieldDescriptor
    REGION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SECURITY_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AMI_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    region: str
    availability_zone: str
    vpc_id: str
    subnet: str
    network_security_group_vec: _containers.RepeatedScalarFieldContainer[str]
    instance_type: str
    ami_id: str
    tags: _containers.ScalarMap[str, str]
    instance_id: str
    def __init__(self, region: _Optional[str] = ..., availability_zone: _Optional[str] = ..., vpc_id: _Optional[str] = ..., subnet: _Optional[str] = ..., network_security_group_vec: _Optional[_Iterable[str]] = ..., instance_type: _Optional[str] = ..., ami_id: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., instance_id: _Optional[str] = ...) -> None: ...

class AWSAcquireDisksArg(_message.Message):
    __slots__ = ("availability_zone", "tags", "disk_type", "number_of_disks", "size_bytes", "attach_instance_id", "partition_type", "fs", "iops", "storage_throughput")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AWS_ACQUIRE_DISKS_ARG_FIELD_NUMBER: _ClassVar[int]
    aws_acquire_disks_arg: _descriptor.FieldDescriptor
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_DISKS_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ATTACH_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FS_FIELD_NUMBER: _ClassVar[int]
    IOPS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    availability_zone: str
    tags: _containers.ScalarMap[str, str]
    disk_type: DiskType
    number_of_disks: int
    size_bytes: int
    attach_instance_id: str
    partition_type: _master_pb2.DiskPartitionType
    fs: _master_pb2.FileSystemType
    iops: int
    storage_throughput: int
    def __init__(self, availability_zone: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., disk_type: _Optional[_Union[DiskType, str]] = ..., number_of_disks: _Optional[int] = ..., size_bytes: _Optional[int] = ..., attach_instance_id: _Optional[str] = ..., partition_type: _Optional[_Union[_master_pb2.DiskPartitionType, str]] = ..., fs: _Optional[_Union[_master_pb2.FileSystemType, str]] = ..., iops: _Optional[int] = ..., storage_throughput: _Optional[int] = ...) -> None: ...

class AWSAcquireDisksResult(_message.Message):
    __slots__ = ("disk_info_vec", "mount_point")
    class DiskInfo(_message.Message):
        __slots__ = ("disk_id", "device_name")
        DISK_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        disk_id: str
        device_name: str
        def __init__(self, disk_id: _Optional[str] = ..., device_name: _Optional[str] = ...) -> None: ...
    AWS_ACQUIRE_DISKS_RESULT_FIELD_NUMBER: _ClassVar[int]
    aws_acquire_disks_result: _descriptor.FieldDescriptor
    DISK_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    disk_info_vec: _containers.RepeatedCompositeFieldContainer[AWSAcquireDisksResult.DiskInfo]
    mount_point: str
    def __init__(self, disk_info_vec: _Optional[_Iterable[_Union[AWSAcquireDisksResult.DiskInfo, _Mapping]]] = ..., mount_point: _Optional[str] = ...) -> None: ...

class AWSDisksInfo(_message.Message):
    __slots__ = ("availability_zone", "tags", "disk_type", "attach_instance_id", "partition_type", "fs", "mount_point", "iops", "storage_throughput")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AWS_DISKS_INFO_FIELD_NUMBER: _ClassVar[int]
    aws_disks_info: _descriptor.FieldDescriptor
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTACH_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    IOPS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    availability_zone: str
    tags: _containers.ScalarMap[str, str]
    disk_type: DiskType
    attach_instance_id: str
    partition_type: _master_pb2.DiskPartitionType
    fs: _master_pb2.FileSystemType
    mount_point: str
    iops: int
    storage_throughput: int
    def __init__(self, availability_zone: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., disk_type: _Optional[_Union[DiskType, str]] = ..., attach_instance_id: _Optional[str] = ..., partition_type: _Optional[_Union[_master_pb2.DiskPartitionType, str]] = ..., fs: _Optional[_Union[_master_pb2.FileSystemType, str]] = ..., mount_point: _Optional[str] = ..., iops: _Optional[int] = ..., storage_throughput: _Optional[int] = ...) -> None: ...

class AWSConfig(_message.Message):
    __slots__ = ("workflow_to_instance_type_map", "default_instance_type_vec", "region_to_ami_id_map", "region_to_os_and_ami_id_map", "instance_type_capacity_map")
    class WorkflowToInstanceTypeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _master_pb2.ListOfString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_master_pb2.ListOfString, _Mapping]] = ...) -> None: ...
    class RegionToAmiIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RegionToOsAndAmiIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _master_pb2.OSToAMIMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_master_pb2.OSToAMIMap, _Mapping]] = ...) -> None: ...
    class InstanceTypeCapacityMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _rpc_service_pb2.ResourceWeightMap
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_rpc_service_pb2.ResourceWeightMap, _Mapping]] = ...) -> None: ...
    WORKFLOW_TO_INSTANCE_TYPE_MAP_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_INSTANCE_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    REGION_TO_AMI_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    REGION_TO_OS_AND_AMI_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_CAPACITY_MAP_FIELD_NUMBER: _ClassVar[int]
    workflow_to_instance_type_map: _containers.MessageMap[str, _master_pb2.ListOfString]
    default_instance_type_vec: _containers.RepeatedScalarFieldContainer[str]
    region_to_ami_id_map: _containers.ScalarMap[str, str]
    region_to_os_and_ami_id_map: _containers.MessageMap[str, _master_pb2.OSToAMIMap]
    instance_type_capacity_map: _containers.MessageMap[str, _rpc_service_pb2.ResourceWeightMap]
    def __init__(self, workflow_to_instance_type_map: _Optional[_Mapping[str, _master_pb2.ListOfString]] = ..., default_instance_type_vec: _Optional[_Iterable[str]] = ..., region_to_ami_id_map: _Optional[_Mapping[str, str]] = ..., region_to_os_and_ami_id_map: _Optional[_Mapping[str, _master_pb2.OSToAMIMap]] = ..., instance_type_capacity_map: _Optional[_Mapping[str, _rpc_service_pb2.ResourceWeightMap]] = ...) -> None: ...
