from magneto.base import credentials_pb2 as _credentials_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuroraClusterInfo(_message.Message):
    __slots__ = ("aws_region", "db_user_name", "host_name", "kms_key_arn", "database_port", "db_access_iam_role_arn")
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    DB_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ARN_FIELD_NUMBER: _ClassVar[int]
    DATABASE_PORT_FIELD_NUMBER: _ClassVar[int]
    DB_ACCESS_IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    aws_region: str
    db_user_name: str
    host_name: str
    kms_key_arn: str
    database_port: str
    db_access_iam_role_arn: str
    def __init__(self, aws_region: _Optional[str] = ..., db_user_name: _Optional[str] = ..., host_name: _Optional[str] = ..., kms_key_arn: _Optional[str] = ..., database_port: _Optional[str] = ..., db_access_iam_role_arn: _Optional[str] = ...) -> None: ...

class S3BucketInfo(_message.Message):
    __slots__ = ("bucket_name", "aws_region", "key_prefix")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    aws_region: str
    key_prefix: str
    def __init__(self, bucket_name: _Optional[str] = ..., aws_region: _Optional[str] = ..., key_prefix: _Optional[str] = ...) -> None: ...

class ObjectLevelParams(_message.Message):
    __slots__ = ("entity_id", "excluded_fields_vec")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FIELDS_VEC_FIELD_NUMBER: _ClassVar[int]
    entity_id: int
    excluded_fields_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entity_id: _Optional[int] = ..., excluded_fields_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class RegisteredEntitySfdcParams(_message.Message):
    __slots__ = ("endpoint_type", "endpoint", "refresh_token", "credentials", "use_bulk_api", "api_limit", "access_token", "consumer_key", "consumer_secret", "soap_endpoint_url", "metadata_endpoint_url", "concurrent_req_limit", "auth_token", "callback_url")
    class EndpointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROD: _ClassVar[RegisteredEntitySfdcParams.EndpointType]
        SANDBOX: _ClassVar[RegisteredEntitySfdcParams.EndpointType]
        OTHER: _ClassVar[RegisteredEntitySfdcParams.EndpointType]
    PROD: RegisteredEntitySfdcParams.EndpointType
    SANDBOX: RegisteredEntitySfdcParams.EndpointType
    OTHER: RegisteredEntitySfdcParams.EndpointType
    ENDPOINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    USE_BULK_API_FIELD_NUMBER: _ClassVar[int]
    API_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_KEY_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_SECRET_FIELD_NUMBER: _ClassVar[int]
    SOAP_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    METADATA_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_REQ_LIMIT_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    endpoint_type: RegisteredEntitySfdcParams.EndpointType
    endpoint: str
    refresh_token: str
    credentials: _credentials_pb2.Credentials
    use_bulk_api: bool
    api_limit: int
    access_token: str
    consumer_key: str
    consumer_secret: str
    soap_endpoint_url: str
    metadata_endpoint_url: str
    concurrent_req_limit: int
    auth_token: str
    callback_url: str
    def __init__(self, endpoint_type: _Optional[_Union[RegisteredEntitySfdcParams.EndpointType, str]] = ..., endpoint: _Optional[str] = ..., refresh_token: _Optional[str] = ..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]] = ..., use_bulk_api: bool = ..., api_limit: _Optional[int] = ..., access_token: _Optional[str] = ..., consumer_key: _Optional[str] = ..., consumer_secret: _Optional[str] = ..., soap_endpoint_url: _Optional[str] = ..., metadata_endpoint_url: _Optional[str] = ..., concurrent_req_limit: _Optional[int] = ..., auth_token: _Optional[str] = ..., callback_url: _Optional[str] = ...) -> None: ...

class SfdcBackupJobParams(_message.Message):
    __slots__ = ("aws_iam_role", "aurora_cluster_info", "object_info_vec", "registered_entity_sfdc_params", "s3_bucket_info", "sfdc_server_timestamp_usecs", "previous_run_sfdc_server_timestamp_usecs", "sfdc_object_metadata_proto_path", "backup_database_name", "tenant_id", "access_token_refresh_time_usecs")
    AWS_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    AURORA_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ENTITY_SFDC_PARAMS_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_INFO_FIELD_NUMBER: _ClassVar[int]
    SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RUN_SFDC_SERVER_TIMESTAMP_USECS_FIELD_NUMBER: _ClassVar[int]
    SFDC_OBJECT_METADATA_PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_REFRESH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    aws_iam_role: str
    aurora_cluster_info: AuroraClusterInfo
    object_info_vec: _containers.RepeatedCompositeFieldContainer[ObjectLevelParams]
    registered_entity_sfdc_params: RegisteredEntitySfdcParams
    s3_bucket_info: S3BucketInfo
    sfdc_server_timestamp_usecs: int
    previous_run_sfdc_server_timestamp_usecs: int
    sfdc_object_metadata_proto_path: str
    backup_database_name: str
    tenant_id: str
    access_token_refresh_time_usecs: int
    def __init__(self, aws_iam_role: _Optional[str] = ..., aurora_cluster_info: _Optional[_Union[AuroraClusterInfo, _Mapping]] = ..., object_info_vec: _Optional[_Iterable[_Union[ObjectLevelParams, _Mapping]]] = ..., registered_entity_sfdc_params: _Optional[_Union[RegisteredEntitySfdcParams, _Mapping]] = ..., s3_bucket_info: _Optional[_Union[S3BucketInfo, _Mapping]] = ..., sfdc_server_timestamp_usecs: _Optional[int] = ..., previous_run_sfdc_server_timestamp_usecs: _Optional[int] = ..., sfdc_object_metadata_proto_path: _Optional[str] = ..., backup_database_name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., access_token_refresh_time_usecs: _Optional[int] = ...) -> None: ...

class SfdcObjectMetadataStore(_message.Message):
    __slots__ = ("object_metadata_map",)
    class ObjectMetadataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SfdcObjectMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SfdcObjectMetadata, _Mapping]] = ...) -> None: ...
    OBJECT_METADATA_MAP_FIELD_NUMBER: _ClassVar[int]
    object_metadata_map: _containers.MessageMap[str, SfdcObjectMetadata]
    def __init__(self, object_metadata_map: _Optional[_Mapping[str, SfdcObjectMetadata]] = ...) -> None: ...

class SfdcObjectMetadata(_message.Message):
    __slots__ = ("api_name", "parent_api_name_to_relation_map", "child_api_name_to_relation_map", "field_map", "property_map", "has_is_deleted_field", "has_last_modified_date_field", "is_attachment_supported", "key_prefix")
    class ParentApiNameToRelationMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SfdcRelation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SfdcRelation, _Mapping]] = ...) -> None: ...
    class ChildApiNameToRelationMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SfdcRelation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SfdcRelation, _Mapping]] = ...) -> None: ...
    class FieldMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Field
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Field, _Mapping]] = ...) -> None: ...
    class PropertyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    API_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_API_NAME_TO_RELATION_MAP_FIELD_NUMBER: _ClassVar[int]
    CHILD_API_NAME_TO_RELATION_MAP_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAP_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_MAP_FIELD_NUMBER: _ClassVar[int]
    HAS_IS_DELETED_FIELD_FIELD_NUMBER: _ClassVar[int]
    HAS_LAST_MODIFIED_DATE_FIELD_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACHMENT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    api_name: str
    parent_api_name_to_relation_map: _containers.MessageMap[str, SfdcRelation]
    child_api_name_to_relation_map: _containers.MessageMap[str, SfdcRelation]
    field_map: _containers.MessageMap[str, Field]
    property_map: _containers.ScalarMap[str, str]
    has_is_deleted_field: bool
    has_last_modified_date_field: bool
    is_attachment_supported: bool
    key_prefix: str
    def __init__(self, api_name: _Optional[str] = ..., parent_api_name_to_relation_map: _Optional[_Mapping[str, SfdcRelation]] = ..., child_api_name_to_relation_map: _Optional[_Mapping[str, SfdcRelation]] = ..., field_map: _Optional[_Mapping[str, Field]] = ..., property_map: _Optional[_Mapping[str, str]] = ..., has_is_deleted_field: bool = ..., has_last_modified_date_field: bool = ..., is_attachment_supported: bool = ..., key_prefix: _Optional[str] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("api_name", "type", "data_type", "property_map", "reference_to_vec", "relationship_name")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[Field.Type]
        kMasterDetail: _ClassVar[Field.Type]
        kLookupRequired: _ClassVar[Field.Type]
        kLookupOptional: _ClassVar[Field.Type]
        kData: _ClassVar[Field.Type]
    kInvalid: Field.Type
    kMasterDetail: Field.Type
    kLookupRequired: Field.Type
    kLookupOptional: Field.Type
    kData: Field.Type
    class PropertyMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    API_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_MAP_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TO_VEC_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    api_name: str
    type: Field.Type
    data_type: str
    property_map: _containers.ScalarMap[str, str]
    reference_to_vec: _containers.RepeatedScalarFieldContainer[str]
    relationship_name: str
    def __init__(self, api_name: _Optional[str] = ..., type: _Optional[_Union[Field.Type, str]] = ..., data_type: _Optional[str] = ..., property_map: _Optional[_Mapping[str, str]] = ..., reference_to_vec: _Optional[_Iterable[str]] = ..., relationship_name: _Optional[str] = ...) -> None: ...

class SfdcRelation(_message.Message):
    __slots__ = ("lookup_field_apiname",)
    LOOKUP_FIELD_APINAME_FIELD_NUMBER: _ClassVar[int]
    lookup_field_apiname: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lookup_field_apiname: _Optional[_Iterable[str]] = ...) -> None: ...

class OrderOfObjects(_message.Message):
    __slots__ = ("objects_apiname_vec",)
    OBJECTS_APINAME_VEC_FIELD_NUMBER: _ClassVar[int]
    objects_apiname_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, objects_apiname_vec: _Optional[_Iterable[str]] = ...) -> None: ...

class OrgSubgraphList(_message.Message):
    __slots__ = ("org_subgraphs_vec",)
    ORG_SUBGRAPHS_VEC_FIELD_NUMBER: _ClassVar[int]
    org_subgraphs_vec: _containers.RepeatedCompositeFieldContainer[OrderOfObjects]
    def __init__(self, org_subgraphs_vec: _Optional[_Iterable[_Union[OrderOfObjects, _Mapping]]] = ...) -> None: ...

class DbRecord(_message.Message):
    __slots__ = ("sf_id", "data_map", "sf_snapshot_time", "last_modified_date", "is_deleted")
    class DataMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SF_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    SF_SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    sf_id: str
    data_map: _containers.ScalarMap[str, str]
    sf_snapshot_time: str
    last_modified_date: str
    is_deleted: bool
    def __init__(self, sf_id: _Optional[str] = ..., data_map: _Optional[_Mapping[str, str]] = ..., sf_snapshot_time: _Optional[str] = ..., last_modified_date: _Optional[str] = ..., is_deleted: bool = ...) -> None: ...

class SfdcQuery(_message.Message):
    __slots__ = ("query", "field_list", "operation_type")
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSOAP: _ClassVar[SfdcQuery.OperationType]
        kBULK: _ClassVar[SfdcQuery.OperationType]
    kSOAP: SfdcQuery.OperationType
    kBULK: SfdcQuery.OperationType
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FIELD_LIST_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    query: str
    field_list: _containers.RepeatedScalarFieldContainer[str]
    operation_type: SfdcQuery.OperationType
    def __init__(self, query: _Optional[str] = ..., field_list: _Optional[_Iterable[str]] = ..., operation_type: _Optional[_Union[SfdcQuery.OperationType, str]] = ...) -> None: ...

class SfdcRestoreObject(_message.Message):
    __slots__ = ("object_name", "restore_params", "entity_id")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    restore_params: SfdcRestoreObjectParams
    entity_id: int
    def __init__(self, object_name: _Optional[str] = ..., restore_params: _Optional[_Union[SfdcRestoreObjectParams, _Mapping]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class SfdcRestoreObjectParams(_message.Message):
    __slots__ = ("new_object_name", "sfdc_restore_type", "record_id_vec", "filter_query", "include_deleted_records", "mutation_type")
    class RestoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRestoreObject: _ClassVar[SfdcRestoreObjectParams.RestoreType]
        kRestoreRecords: _ClassVar[SfdcRestoreObjectParams.RestoreType]
        kRestoreFilter: _ClassVar[SfdcRestoreObjectParams.RestoreType]
        kRestoreOrg: _ClassVar[SfdcRestoreObjectParams.RestoreType]
    kRestoreObject: SfdcRestoreObjectParams.RestoreType
    kRestoreRecords: SfdcRestoreObjectParams.RestoreType
    kRestoreFilter: SfdcRestoreObjectParams.RestoreType
    kRestoreOrg: SfdcRestoreObjectParams.RestoreType
    class MutationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kAdded: _ClassVar[SfdcRestoreObjectParams.MutationType]
        kDeleted: _ClassVar[SfdcRestoreObjectParams.MutationType]
        kModified: _ClassVar[SfdcRestoreObjectParams.MutationType]
        kAll: _ClassVar[SfdcRestoreObjectParams.MutationType]
    kAdded: SfdcRestoreObjectParams.MutationType
    kDeleted: SfdcRestoreObjectParams.MutationType
    kModified: SfdcRestoreObjectParams.MutationType
    kAll: SfdcRestoreObjectParams.MutationType
    NEW_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SFDC_RESTORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    FILTER_QUERY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_RECORDS_FIELD_NUMBER: _ClassVar[int]
    MUTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    new_object_name: str
    sfdc_restore_type: SfdcRestoreObjectParams.RestoreType
    record_id_vec: _containers.RepeatedScalarFieldContainer[str]
    filter_query: str
    include_deleted_records: bool
    mutation_type: SfdcRestoreObjectParams.MutationType
    def __init__(self, new_object_name: _Optional[str] = ..., sfdc_restore_type: _Optional[_Union[SfdcRestoreObjectParams.RestoreType, str]] = ..., record_id_vec: _Optional[_Iterable[str]] = ..., filter_query: _Optional[str] = ..., include_deleted_records: bool = ..., mutation_type: _Optional[_Union[SfdcRestoreObjectParams.MutationType, str]] = ...) -> None: ...

class SfdcRecoverJobParams(_message.Message):
    __slots__ = ("run_start_time_usecs", "overwrite", "restore_parent_object_vec", "restore_childs_object_vec", "aws_iam_role", "aurora_cluster_info", "s3_bucket_info", "prev_full_sfdc_server_timestamp_usecs_map", "is_alternate_restore")
    class PrevFullSfdcServerTimestampUsecsMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARENT_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CHILDS_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    AWS_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    AURORA_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_INFO_FIELD_NUMBER: _ClassVar[int]
    PREV_FULL_SFDC_SERVER_TIMESTAMP_USECS_MAP_FIELD_NUMBER: _ClassVar[int]
    IS_ALTERNATE_RESTORE_FIELD_NUMBER: _ClassVar[int]
    run_start_time_usecs: int
    overwrite: bool
    restore_parent_object_vec: _containers.RepeatedScalarFieldContainer[str]
    restore_childs_object_vec: _containers.RepeatedScalarFieldContainer[str]
    aws_iam_role: str
    aurora_cluster_info: AuroraClusterInfo
    s3_bucket_info: S3BucketInfo
    prev_full_sfdc_server_timestamp_usecs_map: _containers.ScalarMap[str, int]
    is_alternate_restore: bool
    def __init__(self, run_start_time_usecs: _Optional[int] = ..., overwrite: bool = ..., restore_parent_object_vec: _Optional[_Iterable[str]] = ..., restore_childs_object_vec: _Optional[_Iterable[str]] = ..., aws_iam_role: _Optional[str] = ..., aurora_cluster_info: _Optional[_Union[AuroraClusterInfo, _Mapping]] = ..., s3_bucket_info: _Optional[_Union[S3BucketInfo, _Mapping]] = ..., prev_full_sfdc_server_timestamp_usecs_map: _Optional[_Mapping[str, int]] = ..., is_alternate_restore: bool = ...) -> None: ...

class SfdcBackupSourceParamsProto(_message.Message):
    __slots__ = ("excluded_object_ids_vec", "object_level_params_vec", "aurora_cluster_info", "aws_iam_role")
    EXCLUDED_OBJECT_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LEVEL_PARAMS_VEC_FIELD_NUMBER: _ClassVar[int]
    AURORA_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    AWS_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    excluded_object_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    object_level_params_vec: _containers.RepeatedCompositeFieldContainer[ObjectLevelParams]
    aurora_cluster_info: AuroraClusterInfo
    aws_iam_role: str
    def __init__(self, excluded_object_ids_vec: _Optional[_Iterable[int]] = ..., object_level_params_vec: _Optional[_Iterable[_Union[ObjectLevelParams, _Mapping]]] = ..., aurora_cluster_info: _Optional[_Union[AuroraClusterInfo, _Mapping]] = ..., aws_iam_role: _Optional[str] = ...) -> None: ...

class SfdcRecoverField(_message.Message):
    __slots__ = ("field_name", "is_referring_external_id", "relationship_name")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_REFERRING_EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    is_referring_external_id: bool
    relationship_name: str
    def __init__(self, field_name: _Optional[str] = ..., is_referring_external_id: bool = ..., relationship_name: _Optional[str] = ...) -> None: ...
