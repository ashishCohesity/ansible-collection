from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SfdcBackupSourceParamsProto(_message.Message):
    __slots__ = ("excluded_object_ids_vec", "exclude_fields_in_object_vec", "aurora_cluster_info", "aws_iam_role", "s3_bucket_info", "tenant_id")
    class ExcludeFieldsInObject(_message.Message):
        __slots__ = ("object_id", "field_api_names_vec")
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        FIELD_API_NAMES_VEC_FIELD_NUMBER: _ClassVar[int]
        object_id: int
        field_api_names_vec: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, object_id: _Optional[int] = ..., field_api_names_vec: _Optional[_Iterable[str]] = ...) -> None: ...
    EXCLUDED_OBJECT_IDS_VEC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELDS_IN_OBJECT_VEC_FIELD_NUMBER: _ClassVar[int]
    AURORA_CLUSTER_INFO_FIELD_NUMBER: _ClassVar[int]
    AWS_IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
    S3_BUCKET_INFO_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    excluded_object_ids_vec: _containers.RepeatedScalarFieldContainer[int]
    exclude_fields_in_object_vec: _containers.RepeatedCompositeFieldContainer[SfdcBackupSourceParamsProto.ExcludeFieldsInObject]
    aurora_cluster_info: AuroraClusterInfo
    aws_iam_role: str
    s3_bucket_info: S3BucketInfo
    tenant_id: str
    def __init__(self, excluded_object_ids_vec: _Optional[_Iterable[int]] = ..., exclude_fields_in_object_vec: _Optional[_Iterable[_Union[SfdcBackupSourceParamsProto.ExcludeFieldsInObject, _Mapping]]] = ..., aurora_cluster_info: _Optional[_Union[AuroraClusterInfo, _Mapping]] = ..., aws_iam_role: _Optional[str] = ..., s3_bucket_info: _Optional[_Union[S3BucketInfo, _Mapping]] = ..., tenant_id: _Optional[str] = ...) -> None: ...

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

class EnvBackupParamsProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class S3BucketInfo(_message.Message):
    __slots__ = ("bucket_name", "aws_region", "key_prefix")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    aws_region: str
    key_prefix: str
    def __init__(self, bucket_name: _Optional[str] = ..., aws_region: _Optional[str] = ..., key_prefix: _Optional[str] = ...) -> None: ...
