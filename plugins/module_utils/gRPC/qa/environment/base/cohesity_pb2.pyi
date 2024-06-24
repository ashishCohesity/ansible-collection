from qa.lib.cohesityConnector.base import platform_pb2 as _platform_pb2
from qa.lib.cohesityConnector.base import backup_pb2 as _backup_pb2
from qa.environment.base import common_pb2 as _common_pb2
from qa.environment.base import vmware_pb2 as _vmware_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CohesitySoftwareInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "version_name", "package_location", "latest_package_info", "halo_location")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LATEST_PACKAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    HALO_LOCATION_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    version_name: str
    package_location: str
    latest_package_info: str
    halo_location: str
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., version_name: _Optional[str] = ..., package_location: _Optional[str] = ..., latest_package_info: _Optional[str] = ..., halo_location: _Optional[str] = ...) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "ip", "login_info", "type", "ipmi_ip", "ipmi_login_info", "software_package")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IPMI_IP_FIELD_NUMBER: _ClassVar[int]
    IPMI_LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    ip: str
    login_info: _common_pb2.Credentials
    type: str
    ipmi_ip: str
    ipmi_login_info: _common_pb2.Credentials
    software_package: CohesitySoftwareInfo
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., ip: _Optional[str] = ..., login_info: _Optional[_Union[_common_pb2.Credentials, _Mapping]] = ..., type: _Optional[str] = ..., ipmi_ip: _Optional[str] = ..., ipmi_login_info: _Optional[_Union[_common_pb2.Credentials, _Mapping]] = ..., software_package: _Optional[_Union[CohesitySoftwareInfo, _Mapping]] = ...) -> None: ...

class ViewBoxInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "storage_policy")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    storage_policy: _platform_pb2.StoragePolicy
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., storage_policy: _Optional[_Union[_platform_pb2.StoragePolicy, _Mapping]] = ...) -> None: ...

class ClusterPartitionInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "node_vec", "vip_vec", "hostname", "viewbox_vec")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    VIP_VEC_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_VEC_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    node_vec: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    vip_vec: _containers.RepeatedScalarFieldContainer[str]
    hostname: str
    viewbox_vec: _containers.RepeatedCompositeFieldContainer[ViewBoxInfo]
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., node_vec: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ..., vip_vec: _Optional[_Iterable[str]] = ..., hostname: _Optional[str] = ..., viewbox_vec: _Optional[_Iterable[_Union[ViewBoxInfo, _Mapping]]] = ...) -> None: ...

class ClusterInfo(_message.Message):
    __slots__ = ("oid", "oid_ref", "name", "login_info", "dns_vec", "domain_name_vec", "ntp_vec", "node_vec", "subnet", "ipmi_subnet", "enable_encryption", "encryption_rotation_period_sec", "cluster_partition_vec", "protected_vcenter_vec", "job_vec")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
    DNS_VEC_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    NTP_VEC_FIELD_NUMBER: _ClassVar[int]
    NODE_VEC_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    IPMI_SUBNET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ROTATION_PERIOD_SEC_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_PARTITION_VEC_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_VCENTER_VEC_FIELD_NUMBER: _ClassVar[int]
    JOB_VEC_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    name: str
    login_info: _common_pb2.Credentials
    dns_vec: _containers.RepeatedScalarFieldContainer[str]
    domain_name_vec: _containers.RepeatedScalarFieldContainer[str]
    ntp_vec: _containers.RepeatedScalarFieldContainer[str]
    node_vec: _containers.RepeatedCompositeFieldContainer[NodeInfo]
    subnet: _common_pb2.SubnetInfo
    ipmi_subnet: _common_pb2.SubnetInfo
    enable_encryption: bool
    encryption_rotation_period_sec: int
    cluster_partition_vec: _containers.RepeatedCompositeFieldContainer[ClusterPartitionInfo]
    protected_vcenter_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.VCenterInfo]
    job_vec: _containers.RepeatedCompositeFieldContainer[CohesityJob]
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., name: _Optional[str] = ..., login_info: _Optional[_Union[_common_pb2.Credentials, _Mapping]] = ..., dns_vec: _Optional[_Iterable[str]] = ..., domain_name_vec: _Optional[_Iterable[str]] = ..., ntp_vec: _Optional[_Iterable[str]] = ..., node_vec: _Optional[_Iterable[_Union[NodeInfo, _Mapping]]] = ..., subnet: _Optional[_Union[_common_pb2.SubnetInfo, _Mapping]] = ..., ipmi_subnet: _Optional[_Union[_common_pb2.SubnetInfo, _Mapping]] = ..., enable_encryption: bool = ..., encryption_rotation_period_sec: _Optional[int] = ..., cluster_partition_vec: _Optional[_Iterable[_Union[ClusterPartitionInfo, _Mapping]]] = ..., protected_vcenter_vec: _Optional[_Iterable[_Union[_vmware_pb2.VCenterInfo, _Mapping]]] = ..., job_vec: _Optional[_Iterable[_Union[CohesityJob, _Mapping]]] = ...) -> None: ...

class JobPolicyCustomFields(_message.Message):
    __slots__ = ("policy_name", "replication_cluster_oid_ref_vec", "replication_cluster_id_vec", "schedule_end_usecs")
    POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_CLUSTER_OID_REF_VEC_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_CLUSTER_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_END_USECS_FIELD_NUMBER: _ClassVar[int]
    policy_name: str
    replication_cluster_oid_ref_vec: _containers.RepeatedScalarFieldContainer[str]
    replication_cluster_id_vec: _containers.RepeatedScalarFieldContainer[int]
    schedule_end_usecs: int
    def __init__(self, policy_name: _Optional[str] = ..., replication_cluster_oid_ref_vec: _Optional[_Iterable[str]] = ..., replication_cluster_id_vec: _Optional[_Iterable[int]] = ..., schedule_end_usecs: _Optional[int] = ...) -> None: ...

class JobPolicy(_message.Message):
    __slots__ = ("oid", "oid_ref", "type", "name", "template_file_name", "custom_fields")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    type: str
    name: str
    template_file_name: str
    custom_fields: JobPolicyCustomFields
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., template_file_name: _Optional[str] = ..., custom_fields: _Optional[_Union[JobPolicyCustomFields, _Mapping]] = ...) -> None: ...

class CohesityJob(_message.Message):
    __slots__ = ("oid", "oid_ref", "type", "name", "vcenter", "viewbox", "indexing_policy", "enable_app_consistency", "job_policy", "vm_setup_vec")
    OID_FIELD_NUMBER: _ClassVar[int]
    OID_REF_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VCENTER_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_FIELD_NUMBER: _ClassVar[int]
    INDEXING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_APP_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    JOB_POLICY_FIELD_NUMBER: _ClassVar[int]
    VM_SETUP_VEC_FIELD_NUMBER: _ClassVar[int]
    oid: str
    oid_ref: str
    type: str
    name: str
    vcenter: _vmware_pb2.VCenterInfo
    viewbox: ViewBoxInfo
    indexing_policy: _backup_pb2.IndexingPolicy
    enable_app_consistency: bool
    job_policy: JobPolicy
    vm_setup_vec: _containers.RepeatedCompositeFieldContainer[_vmware_pb2.VMSetupInfo]
    def __init__(self, oid: _Optional[str] = ..., oid_ref: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., vcenter: _Optional[_Union[_vmware_pb2.VCenterInfo, _Mapping]] = ..., viewbox: _Optional[_Union[ViewBoxInfo, _Mapping]] = ..., indexing_policy: _Optional[_Union[_backup_pb2.IndexingPolicy, _Mapping]] = ..., enable_app_consistency: bool = ..., job_policy: _Optional[_Union[JobPolicy, _Mapping]] = ..., vm_setup_vec: _Optional[_Iterable[_Union[_vmware_pb2.VMSetupInfo, _Mapping]]] = ...) -> None: ...
