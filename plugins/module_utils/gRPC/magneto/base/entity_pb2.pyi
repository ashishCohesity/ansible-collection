from magneto.api.common import additional_entity_info_pb2 as _additional_entity_info_pb2
from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from magneto.base.entities import ad_pb2 as _ad_pb2
from magneto.base.entities import agent_pb2 as _agent_pb2
from magneto.base.entities import acropolis_pb2 as _acropolis_pb2
from magneto.base.entities import aws_pb2 as _aws_pb2
from magneto.base.entities import azure_pb2 as _azure_pb2
from magneto.base.entities import cassandra_pb2 as _cassandra_pb2
from magneto.base.entities import couchbase_pb2 as _couchbase_pb2
from magneto.base.entities import exchange_pb2 as _exchange_pb2
from magneto.base.entities import elastifile_pb2 as _elastifile_pb2
from magneto.base.entities import flashblade_pb2 as _flashblade_pb2
from magneto.base.entities import gcp_pb2 as _gcp_pb2
from magneto.base.entities import uda_pb2 as _uda_pb2
from magneto.base.entities import gpfs_pb2 as _gpfs_pb2
from magneto.base.entities import generic_nas_pb2 as _generic_nas_pb2
from magneto.base.entities import hbase_pb2 as _hbase_pb2
from magneto.base.entities import hdfs_pb2 as _hdfs_pb2
from magneto.base.entities import hive_pb2 as _hive_pb2
from magneto.base.entities import hyperflex_pb2 as _hyperflex_pb2
from magneto.base.entities import hyperv_pb2 as _hyperv_pb2
from magneto.base.entities import isilon_pb2 as _isilon_pb2
from magneto.base.entities import kubernetes_pb2 as _kubernetes_pb2
from magneto.base.entities import kvm_pb2 as _kvm_pb2
from magneto.base.entities import mongodb_pb2 as _mongodb_pb2
from magneto.base.entities import netapp_pb2 as _netapp_pb2
from magneto.base.entities import oracle_pb2 as _oracle_pb2
from magneto.base.entities import o365_pb2 as _o365_pb2
from magneto.base.entities import physical_pb2 as _physical_pb2
from magneto.base.entities import san_entity_pb2 as _san_entity_pb2
from magneto.base.entities import sql_pb2 as _sql_pb2
from magneto.base.entities import view_pb2 as _view_pb2
from magneto.base.entities import vmware_pb2 as _vmware_pb2
from magneto.base.entities import sfdc_pb2 as _sfdc_pb2
from magneto.base import enums_pb2 as _enums_pb2
from magneto.base.v2 import internal_entity_pb2 as _internal_entity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StringEntityIdsProto(_message.Message):
    __slots__ = ("latest_id",)
    class StringId(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    LATEST_ID_FIELD_NUMBER: _ClassVar[int]
    latest_id: StringEntityIdsProto.StringId
    def __init__(self, latest_id: _Optional[_Union[StringEntityIdsProto.StringId, _Mapping]] = ...) -> None: ...

class EntityIdProto(_message.Message):
    __slots__ = ("string_ids", "int_id")
    STRING_IDS_FIELD_NUMBER: _ClassVar[int]
    INT_ID_FIELD_NUMBER: _ClassVar[int]
    string_ids: StringEntityIdsProto
    int_id: int
    def __init__(self, string_ids: _Optional[_Union[StringEntityIdsProto, _Mapping]] = ..., int_id: _Optional[int] = ...) -> None: ...

class EntityProto(_message.Message):
    __slots__ = ("type", "vmware_entity", "sql_entity", "view_entity", "physical_entity", "pure_entity", "azure_entity", "netapp_entity", "agent_entity", "hyperv_entity", "generic_nas_entity", "acropolis_entity", "kvm_entity", "isilon_entity", "aws_entity", "oracle_entity", "gcp_entity", "flashblade_entity", "o365_entity", "hyperflex_entity", "ad_entity", "gpfs_entity", "kubernetes_entity", "exchange_entity", "elastifile_entity", "cassandra_entity", "mongodb_entity", "couchbase_entity", "hbase_entity", "hdfs_entity", "hive_entity", "uda_entity", "id", "entity_id", "parent_id", "display_name", "is_clone", "clone_task_id", "network_realm_id", "connector_group_id", "sfdc_entity", "custom_name", "additional_entity_info_vec", "size_info")
    class SizeInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _magneto_external_base_pb2.EntitySizeInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_magneto_external_base_pb2.EntitySizeInfo, _Mapping]] = ...) -> None: ...
    V1_ENTITY_PROTO_FIELD_NUMBER: _ClassVar[int]
    v1_entity_proto: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SQL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VIEW_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ENTITY_FIELD_NUMBER: _ClassVar[int]
    PURE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    AZURE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    NETAPP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    AGENT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HYPERV_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GENERIC_NAS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ACROPOLIS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    KVM_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ISILON_ENTITY_FIELD_NUMBER: _ClassVar[int]
    AWS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ORACLE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GCP_ENTITY_FIELD_NUMBER: _ClassVar[int]
    FLASHBLADE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    O365_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HYPERFLEX_ENTITY_FIELD_NUMBER: _ClassVar[int]
    AD_ENTITY_FIELD_NUMBER: _ClassVar[int]
    GPFS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_ENTITY_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ELASTIFILE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CASSANDRA_ENTITY_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    COUCHBASE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HBASE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HDFS_ENTITY_FIELD_NUMBER: _ClassVar[int]
    HIVE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    UDA_ENTITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_CLONE_FIELD_NUMBER: _ClassVar[int]
    CLONE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_REALM_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SFDC_ENTITY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENTITY_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.Environment.Type
    vmware_entity: _vmware_pb2.Entity
    sql_entity: _sql_pb2.Entity
    view_entity: _view_pb2.Entity
    physical_entity: _physical_pb2.Entity
    pure_entity: _san_entity_pb2.Entity
    azure_entity: _azure_pb2.Entity
    netapp_entity: _netapp_pb2.Entity
    agent_entity: _agent_pb2.Entity
    hyperv_entity: _hyperv_pb2.Entity
    generic_nas_entity: _generic_nas_pb2.Entity
    acropolis_entity: _acropolis_pb2.Entity
    kvm_entity: _kvm_pb2.Entity
    isilon_entity: _isilon_pb2.Entity
    aws_entity: _aws_pb2.Entity
    oracle_entity: _oracle_pb2.Entity
    gcp_entity: _gcp_pb2.Entity
    flashblade_entity: _flashblade_pb2.Entity
    o365_entity: _o365_pb2.Entity
    hyperflex_entity: _hyperflex_pb2.Entity
    ad_entity: _ad_pb2.Entity
    gpfs_entity: _gpfs_pb2.Entity
    kubernetes_entity: _kubernetes_pb2.Entity
    exchange_entity: _exchange_pb2.Entity
    elastifile_entity: _elastifile_pb2.Entity
    cassandra_entity: _cassandra_pb2.Entity
    mongodb_entity: _mongodb_pb2.Entity
    couchbase_entity: _couchbase_pb2.Entity
    hbase_entity: _hbase_pb2.Entity
    hdfs_entity: _hdfs_pb2.Entity
    hive_entity: _hive_pb2.Entity
    uda_entity: _uda_pb2.Entity
    id: int
    entity_id: EntityIdProto
    parent_id: int
    display_name: str
    is_clone: bool
    clone_task_id: int
    network_realm_id: int
    connector_group_id: int
    sfdc_entity: _sfdc_pb2.Entity
    custom_name: str
    additional_entity_info_vec: _containers.RepeatedCompositeFieldContainer[_additional_entity_info_pb2.AdditionalEntityInfo]
    size_info: _containers.MessageMap[int, _magneto_external_base_pb2.EntitySizeInfo]
    def __init__(self, type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., vmware_entity: _Optional[_Union[_vmware_pb2.Entity, _Mapping]] = ..., sql_entity: _Optional[_Union[_sql_pb2.Entity, _Mapping]] = ..., view_entity: _Optional[_Union[_view_pb2.Entity, _Mapping]] = ..., physical_entity: _Optional[_Union[_physical_pb2.Entity, _Mapping]] = ..., pure_entity: _Optional[_Union[_san_entity_pb2.Entity, _Mapping]] = ..., azure_entity: _Optional[_Union[_azure_pb2.Entity, _Mapping]] = ..., netapp_entity: _Optional[_Union[_netapp_pb2.Entity, _Mapping]] = ..., agent_entity: _Optional[_Union[_agent_pb2.Entity, _Mapping]] = ..., hyperv_entity: _Optional[_Union[_hyperv_pb2.Entity, _Mapping]] = ..., generic_nas_entity: _Optional[_Union[_generic_nas_pb2.Entity, _Mapping]] = ..., acropolis_entity: _Optional[_Union[_acropolis_pb2.Entity, _Mapping]] = ..., kvm_entity: _Optional[_Union[_kvm_pb2.Entity, _Mapping]] = ..., isilon_entity: _Optional[_Union[_isilon_pb2.Entity, _Mapping]] = ..., aws_entity: _Optional[_Union[_aws_pb2.Entity, _Mapping]] = ..., oracle_entity: _Optional[_Union[_oracle_pb2.Entity, _Mapping]] = ..., gcp_entity: _Optional[_Union[_gcp_pb2.Entity, _Mapping]] = ..., flashblade_entity: _Optional[_Union[_flashblade_pb2.Entity, _Mapping]] = ..., o365_entity: _Optional[_Union[_o365_pb2.Entity, _Mapping]] = ..., hyperflex_entity: _Optional[_Union[_hyperflex_pb2.Entity, _Mapping]] = ..., ad_entity: _Optional[_Union[_ad_pb2.Entity, _Mapping]] = ..., gpfs_entity: _Optional[_Union[_gpfs_pb2.Entity, _Mapping]] = ..., kubernetes_entity: _Optional[_Union[_kubernetes_pb2.Entity, _Mapping]] = ..., exchange_entity: _Optional[_Union[_exchange_pb2.Entity, _Mapping]] = ..., elastifile_entity: _Optional[_Union[_elastifile_pb2.Entity, _Mapping]] = ..., cassandra_entity: _Optional[_Union[_cassandra_pb2.Entity, _Mapping]] = ..., mongodb_entity: _Optional[_Union[_mongodb_pb2.Entity, _Mapping]] = ..., couchbase_entity: _Optional[_Union[_couchbase_pb2.Entity, _Mapping]] = ..., hbase_entity: _Optional[_Union[_hbase_pb2.Entity, _Mapping]] = ..., hdfs_entity: _Optional[_Union[_hdfs_pb2.Entity, _Mapping]] = ..., hive_entity: _Optional[_Union[_hive_pb2.Entity, _Mapping]] = ..., uda_entity: _Optional[_Union[_uda_pb2.Entity, _Mapping]] = ..., id: _Optional[int] = ..., entity_id: _Optional[_Union[EntityIdProto, _Mapping]] = ..., parent_id: _Optional[int] = ..., display_name: _Optional[str] = ..., is_clone: bool = ..., clone_task_id: _Optional[int] = ..., network_realm_id: _Optional[int] = ..., connector_group_id: _Optional[int] = ..., sfdc_entity: _Optional[_Union[_sfdc_pb2.Entity, _Mapping]] = ..., custom_name: _Optional[str] = ..., additional_entity_info_vec: _Optional[_Iterable[_Union[_additional_entity_info_pb2.AdditionalEntityInfo, _Mapping]]] = ..., size_info: _Optional[_Mapping[int, _magneto_external_base_pb2.EntitySizeInfo]] = ...) -> None: ...
