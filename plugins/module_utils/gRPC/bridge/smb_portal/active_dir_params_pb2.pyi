from configs import cluster_config_pb2 as _cluster_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddDomainArg(_message.Message):
    __slots__ = ("ad_domain_name", "ad_admin_name", "ad_admin_password", "machine_account_name_vec", "ad_org_unit", "ad_workgroup", "overwrite_existing_machine_accounts", "preferred_dc_vec", "trusted_domains_disabled", "tenant_id_vec", "task_path", "ldap_id", "nis_domain_name", "dns_hostname_vec", "encryption_type_vec", "network_realm_id", "machine_account_vec", "blacklisted_dc_vec")
    AD_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_ADMIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_ADMIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    AD_ORG_UNIT_FIELD_NUMBER: _ClassVar[int]
    AD_WORKGROUP_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_MACHINE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_DOMAINS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    LDAP_ID_FIELD_NUMBER: _ClassVar[int]
    NIS_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    DNS_HOSTNAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    ad_domain_name: str
    ad_admin_name: str
    ad_admin_password: str
    machine_account_name_vec: _containers.RepeatedScalarFieldContainer[str]
    ad_org_unit: str
    ad_workgroup: str
    overwrite_existing_machine_accounts: bool
    preferred_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    trusted_domains_disabled: bool
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    task_path: str
    ldap_id: int
    nis_domain_name: str
    dns_hostname_vec: _containers.RepeatedScalarFieldContainer[str]
    encryption_type_vec: _containers.RepeatedScalarFieldContainer[int]
    network_realm_id: int
    machine_account_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto]
    blacklisted_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ad_domain_name: _Optional[str] = ..., ad_admin_name: _Optional[str] = ..., ad_admin_password: _Optional[str] = ..., machine_account_name_vec: _Optional[_Iterable[str]] = ..., ad_org_unit: _Optional[str] = ..., ad_workgroup: _Optional[str] = ..., overwrite_existing_machine_accounts: bool = ..., preferred_dc_vec: _Optional[_Iterable[str]] = ..., trusted_domains_disabled: bool = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., task_path: _Optional[str] = ..., ldap_id: _Optional[int] = ..., nis_domain_name: _Optional[str] = ..., dns_hostname_vec: _Optional[_Iterable[str]] = ..., encryption_type_vec: _Optional[_Iterable[int]] = ..., network_realm_id: _Optional[int] = ..., machine_account_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto, _Mapping]]] = ..., blacklisted_dc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class AddDomainResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EditDomainArg(_message.Message):
    __slots__ = ("ad_domain_name", "ad_admin_name", "ad_admin_password", "machine_account_name_vec", "overwrite_existing_machine_accounts", "task_path", "dns_hostname_vec", "encryption_type_vec", "tenant_id_vec", "machine_account_vec")
    AD_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_ADMIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_ADMIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_MACHINE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    DNS_HOSTNAME_VEC_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TYPE_VEC_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNT_VEC_FIELD_NUMBER: _ClassVar[int]
    ad_domain_name: str
    ad_admin_name: str
    ad_admin_password: str
    machine_account_name_vec: _containers.RepeatedScalarFieldContainer[str]
    overwrite_existing_machine_accounts: bool
    task_path: str
    dns_hostname_vec: _containers.RepeatedScalarFieldContainer[str]
    encryption_type_vec: _containers.RepeatedScalarFieldContainer[int]
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    machine_account_vec: _containers.RepeatedCompositeFieldContainer[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto]
    def __init__(self, ad_domain_name: _Optional[str] = ..., ad_admin_name: _Optional[str] = ..., ad_admin_password: _Optional[str] = ..., machine_account_name_vec: _Optional[_Iterable[str]] = ..., overwrite_existing_machine_accounts: bool = ..., task_path: _Optional[str] = ..., dns_hostname_vec: _Optional[_Iterable[str]] = ..., encryption_type_vec: _Optional[_Iterable[int]] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., machine_account_vec: _Optional[_Iterable[_Union[_cluster_config_pb2.ClusterConfigProto.ActiveDirectoryConfig.ActiveDirectoryProvider.MachineAccountProto, _Mapping]]] = ...) -> None: ...

class EditDomainResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveDomainArg(_message.Message):
    __slots__ = ("ad_domain_name", "ad_admin_name", "ad_admin_password", "machine_account_name_vec", "task_path", "tenant_id_vec", "force_remove")
    AD_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_ADMIN_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_ADMIN_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ACCOUNT_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    TASK_PATH_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FORCE_REMOVE_FIELD_NUMBER: _ClassVar[int]
    ad_domain_name: str
    ad_admin_name: str
    ad_admin_password: str
    machine_account_name_vec: _containers.RepeatedScalarFieldContainer[str]
    task_path: str
    tenant_id_vec: _containers.RepeatedScalarFieldContainer[str]
    force_remove: bool
    def __init__(self, ad_domain_name: _Optional[str] = ..., ad_admin_name: _Optional[str] = ..., ad_admin_password: _Optional[str] = ..., machine_account_name_vec: _Optional[_Iterable[str]] = ..., task_path: _Optional[str] = ..., tenant_id_vec: _Optional[_Iterable[str]] = ..., force_remove: bool = ...) -> None: ...

class RemoveDomainResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdatePreferredDCsArg(_message.Message):
    __slots__ = ("domain_name", "preferred_dc_vec", "blacklisted_dc_vec")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    BLACKLISTED_DC_VEC_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    preferred_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    blacklisted_dc_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain_name: _Optional[str] = ..., preferred_dc_vec: _Optional[_Iterable[str]] = ..., blacklisted_dc_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdatePreferredDCsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModifyCapathsArg(_message.Message):
    __slots__ = ("is_add_op", "client_fqdn", "cluster_fqdn", "inter_fqdn")
    IS_ADD_OP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FQDN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FQDN_FIELD_NUMBER: _ClassVar[int]
    INTER_FQDN_FIELD_NUMBER: _ClassVar[int]
    is_add_op: bool
    client_fqdn: str
    cluster_fqdn: str
    inter_fqdn: str
    def __init__(self, is_add_op: bool = ..., client_fqdn: _Optional[str] = ..., cluster_fqdn: _Optional[str] = ..., inter_fqdn: _Optional[str] = ...) -> None: ...

class ModifyCapathsResult(_message.Message):
    __slots__ = ("err_msg",)
    ERR_MSG_FIELD_NUMBER: _ClassVar[int]
    err_msg: str
    def __init__(self, err_msg: _Optional[str] = ...) -> None: ...
