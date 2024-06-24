from qa.perfHarness.base import harness_spec_pb2 as _harness_spec_pb2
from qa.environment.base import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PSHostInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "ip", "login_info")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    ip: str
    login_info: _common_pb2.Credentials
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., ip: _Optional[str] = ..., login_info: _Optional[_Union[_common_pb2.Credentials, _Mapping]] = ...) -> None: ...

class DataStoreInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "nfs_server_ip", "nfs_server_folder")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NFS_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    NFS_SERVER_FOLDER_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    nfs_server_ip: str
    nfs_server_folder: str
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., nfs_server_ip: _Optional[str] = ..., nfs_server_folder: _Optional[str] = ...) -> None: ...

class ResourcePoolInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "moref")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    MOREF_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    moref: str
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., moref: _Optional[str] = ...) -> None: ...

class EsxHostInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "ip", "data_store_vec", "resource_pool_vec")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_VEC_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    ip: str
    data_store_vec: _containers.RepeatedCompositeFieldContainer[DataStoreInfo]
    resource_pool_vec: _containers.RepeatedCompositeFieldContainer[ResourcePoolInfo]
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., ip: _Optional[str] = ..., data_store_vec: _Optional[_Iterable[_Union[DataStoreInfo, _Mapping]]] = ..., resource_pool_vec: _Optional[_Iterable[_Union[ResourcePoolInfo, _Mapping]]] = ...) -> None: ...

class VmwareClusterInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "esx_host_vec", "resource_pool_vec")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ESX_HOST_VEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_VEC_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    esx_host_vec: _containers.RepeatedCompositeFieldContainer[EsxHostInfo]
    resource_pool_vec: _containers.RepeatedCompositeFieldContainer[ResourcePoolInfo]
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., esx_host_vec: _Optional[_Iterable[_Union[EsxHostInfo, _Mapping]]] = ..., resource_pool_vec: _Optional[_Iterable[_Union[ResourcePoolInfo, _Mapping]]] = ...) -> None: ...

class VmwareDataCenterInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "vmware_cluster_vec", "esx_host_vec")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VMWARE_CLUSTER_VEC_FIELD_NUMBER: _ClassVar[int]
    ESX_HOST_VEC_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    vmware_cluster_vec: _containers.RepeatedCompositeFieldContainer[VmwareClusterInfo]
    esx_host_vec: _containers.RepeatedCompositeFieldContainer[EsxHostInfo]
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., vmware_cluster_vec: _Optional[_Iterable[_Union[VmwareClusterInfo, _Mapping]]] = ..., esx_host_vec: _Optional[_Iterable[_Union[EsxHostInfo, _Mapping]]] = ...) -> None: ...

class VCenterInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "ip", "datacenter_vec", "login_info")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    DATACENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    ip: str
    datacenter_vec: _containers.RepeatedCompositeFieldContainer[VmwareDataCenterInfo]
    login_info: _common_pb2.Credentials
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., ip: _Optional[str] = ..., datacenter_vec: _Optional[_Iterable[_Union[VmwareDataCenterInfo, _Mapping]]] = ..., login_info: _Optional[_Union[_common_pb2.Credentials, _Mapping]] = ...) -> None: ...

class VMSetupLocationInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "cluster_info", "esx_host_vec", "data_store_info")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    ESX_HOST_VEC_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_INFO_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    cluster_info: VmwareClusterInfo
    esx_host_vec: _containers.RepeatedCompositeFieldContainer[EsxHostInfo]
    data_store_info: DataStoreInfo
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., cluster_info: _Optional[_Union[VmwareClusterInfo, _Mapping]] = ..., esx_host_vec: _Optional[_Iterable[_Union[EsxHostInfo, _Mapping]]] = ..., data_store_info: _Optional[_Union[DataStoreInfo, _Mapping]] = ...) -> None: ...

class VMSetupInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "template_name", "login_info", "vm_name_prefix", "num_vms", "location", "extra_virtual_disk_vec", "os_type", "disk_prep_info")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NUM_VMS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_VIRTUAL_DISK_VEC_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_PREP_INFO_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    template_name: str
    login_info: _common_pb2.Credentials
    vm_name_prefix: str
    num_vms: int
    location: VMSetupLocationInfo
    extra_virtual_disk_vec: _containers.RepeatedCompositeFieldContainer[_harness_spec_pb2.VirtualDiskInfo]
    os_type: _harness_spec_pb2.OSType
    disk_prep_info: _harness_spec_pb2.DiskPrepInfo
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., template_name: _Optional[str] = ..., login_info: _Optional[_Union[_common_pb2.Credentials, _Mapping]] = ..., vm_name_prefix: _Optional[str] = ..., num_vms: _Optional[int] = ..., location: _Optional[_Union[VMSetupLocationInfo, _Mapping]] = ..., extra_virtual_disk_vec: _Optional[_Iterable[_Union[_harness_spec_pb2.VirtualDiskInfo, _Mapping]]] = ..., os_type: _Optional[_Union[_harness_spec_pb2.OSType, str]] = ..., disk_prep_info: _Optional[_Union[_harness_spec_pb2.DiskPrepInfo, _Mapping]] = ...) -> None: ...
