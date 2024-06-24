from librarian.base import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LibrarianConfigProto(_message.Message):
    __slots__ = ("gandalf_master_lock_name", "master_status_url", "lookup_master_url", "data_store_version", "node_bucket_multiplier", "bucket_replica_data_url", "master_index_info_url", "docid_bucket_mapping_url", "bucket_replica_url", "initiate_datastore_reshard_url", "delete_index_url")
    GANDALF_MASTER_LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_BUCKET_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    BUCKET_REPLICA_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    MASTER_INDEX_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    DOCID_BUCKET_MAPPING_URL_FIELD_NUMBER: _ClassVar[int]
    BUCKET_REPLICA_URL_FIELD_NUMBER: _ClassVar[int]
    INITIATE_DATASTORE_RESHARD_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_INDEX_URL_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_lock_name: str
    master_status_url: str
    lookup_master_url: str
    data_store_version: int
    node_bucket_multiplier: int
    bucket_replica_data_url: str
    master_index_info_url: str
    docid_bucket_mapping_url: str
    bucket_replica_url: str
    initiate_datastore_reshard_url: str
    delete_index_url: str
    def __init__(self, gandalf_master_lock_name: _Optional[str] = ..., master_status_url: _Optional[str] = ..., lookup_master_url: _Optional[str] = ..., data_store_version: _Optional[int] = ..., node_bucket_multiplier: _Optional[int] = ..., bucket_replica_data_url: _Optional[str] = ..., master_index_info_url: _Optional[str] = ..., docid_bucket_mapping_url: _Optional[str] = ..., bucket_replica_url: _Optional[str] = ..., initiate_datastore_reshard_url: _Optional[str] = ..., delete_index_url: _Optional[str] = ...) -> None: ...

class IndexInfo(_message.Message):
    __slots__ = ("schema", "bucket_vec", "read_only_DEPRECATED", "incarnation_id", "deleted", "for_search_index", "cloud_config")
    class BucketInfo(_message.Message):
        __slots__ = ("bucket_id", "replica_vec", "incarnation_id")
        class ReplicaInfo(_message.Message):
            __slots__ = ("disk_id", "read_only", "lost")
            DISK_ID_FIELD_NUMBER: _ClassVar[int]
            READ_ONLY_FIELD_NUMBER: _ClassVar[int]
            LOST_FIELD_NUMBER: _ClassVar[int]
            disk_id: int
            read_only: bool
            lost: bool
            def __init__(self, disk_id: _Optional[int] = ..., read_only: bool = ..., lost: bool = ...) -> None: ...
        BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
        REPLICA_VEC_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        bucket_id: int
        replica_vec: _containers.RepeatedCompositeFieldContainer[IndexInfo.BucketInfo.ReplicaInfo]
        incarnation_id: int
        def __init__(self, bucket_id: _Optional[int] = ..., replica_vec: _Optional[_Iterable[_Union[IndexInfo.BucketInfo.ReplicaInfo, _Mapping]]] = ..., incarnation_id: _Optional[int] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    BUCKET_VEC_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    FOR_SEARCH_INDEX_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    schema: _schema_pb2.IndexSchema
    bucket_vec: _containers.RepeatedCompositeFieldContainer[IndexInfo.BucketInfo]
    read_only_DEPRECATED: bool
    incarnation_id: int
    deleted: bool
    for_search_index: bool
    cloud_config: CloudConfig
    def __init__(self, schema: _Optional[_Union[_schema_pb2.IndexSchema, _Mapping]] = ..., bucket_vec: _Optional[_Iterable[_Union[IndexInfo.BucketInfo, _Mapping]]] = ..., read_only_DEPRECATED: bool = ..., incarnation_id: _Optional[int] = ..., deleted: bool = ..., for_search_index: bool = ..., cloud_config: _Optional[_Union[CloudConfig, _Mapping]] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ("indices_vec",)
    INDICES_VEC_FIELD_NUMBER: _ClassVar[int]
    indices_vec: _containers.RepeatedCompositeFieldContainer[IndexInfo]
    def __init__(self, indices_vec: _Optional[_Iterable[_Union[IndexInfo, _Mapping]]] = ...) -> None: ...

class CloudConfig(_message.Message):
    __slots__ = ("region", "s3_bucket_name", "s3_prefix", "es_fqdn", "es_iam_role_arn", "s3_iam_role_arn", "azure_config", "tenant_version")
    class AzureCloudConfig(_message.Message):
        __slots__ = ("vault_url", "client_id", "secret_name", "container_name", "storage_account_name")
        VAULT_URL_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        SECRET_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
        STORAGE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        vault_url: str
        client_id: str
        secret_name: str
        container_name: str
        storage_account_name: str
        def __init__(self, vault_url: _Optional[str] = ..., client_id: _Optional[str] = ..., secret_name: _Optional[str] = ..., container_name: _Optional[str] = ..., storage_account_name: _Optional[str] = ...) -> None: ...
    REGION_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    S3_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ES_FQDN_FIELD_NUMBER: _ClassVar[int]
    ES_IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    S3_IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    AZURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TENANT_VERSION_FIELD_NUMBER: _ClassVar[int]
    region: str
    s3_bucket_name: str
    s3_prefix: str
    es_fqdn: str
    es_iam_role_arn: str
    s3_iam_role_arn: str
    azure_config: CloudConfig.AzureCloudConfig
    tenant_version: int
    def __init__(self, region: _Optional[str] = ..., s3_bucket_name: _Optional[str] = ..., s3_prefix: _Optional[str] = ..., es_fqdn: _Optional[str] = ..., es_iam_role_arn: _Optional[str] = ..., s3_iam_role_arn: _Optional[str] = ..., azure_config: _Optional[_Union[CloudConfig.AzureCloudConfig, _Mapping]] = ..., tenant_version: _Optional[int] = ...) -> None: ...
