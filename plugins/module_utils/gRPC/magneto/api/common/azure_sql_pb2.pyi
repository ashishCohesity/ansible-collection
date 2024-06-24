from magneto.api import magneto_external_entity_metadata_pb2 as _magneto_external_entity_metadata_pb2
from magneto.base.entities import azure_pb2 as _azure_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AzureSqlEnvBackupParamsProto(_message.Message):
    __slots__ = ("disk_type", "copy_database", "sql_package_options", "copy_db_sku", "temp_disk_size_gb")
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    COPY_DATABASE_FIELD_NUMBER: _ClassVar[int]
    SQL_PACKAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    COPY_DB_SKU_FIELD_NUMBER: _ClassVar[int]
    TEMP_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    disk_type: _azure_pb2.AzureDisk.Type
    copy_database: bool
    sql_package_options: SqlPackage
    copy_db_sku: _azure_pb2.Entity.SKU
    temp_disk_size_gb: int
    def __init__(self, disk_type: _Optional[_Union[_azure_pb2.AzureDisk.Type, str]] = ..., copy_database: bool = ..., sql_package_options: _Optional[_Union[SqlPackage, _Mapping]] = ..., copy_db_sku: _Optional[_Union[_azure_pb2.Entity.SKU, _Mapping]] = ..., temp_disk_size_gb: _Optional[int] = ...) -> None: ...

class RestoreAzureSQLParams(_message.Message):
    __slots__ = ("disk_type", "overwrite_database", "new_database_name", "sql_package_options", "restored_db_sku")
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    NEW_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    SQL_PACKAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORED_DB_SKU_FIELD_NUMBER: _ClassVar[int]
    disk_type: _azure_pb2.AzureDisk.Type
    overwrite_database: bool
    new_database_name: str
    sql_package_options: SqlPackage
    restored_db_sku: _azure_pb2.Entity.SKU
    def __init__(self, disk_type: _Optional[_Union[_azure_pb2.AzureDisk.Type, str]] = ..., overwrite_database: bool = ..., new_database_name: _Optional[str] = ..., sql_package_options: _Optional[_Union[SqlPackage, _Mapping]] = ..., restored_db_sku: _Optional[_Union[_azure_pb2.Entity.SKU, _Mapping]] = ...) -> None: ...

class AzureSQLMetadata(_message.Message):
    __slots__ = ("auth_type",)
    class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[AzureSQLMetadata.AuthType]
        kManagedIdentity: _ClassVar[AzureSQLMetadata.AuthType]
        kCredentials: _ClassVar[AzureSQLMetadata.AuthType]
    kUnknown: AzureSQLMetadata.AuthType
    kManagedIdentity: AzureSQLMetadata.AuthType
    kCredentials: AzureSQLMetadata.AuthType
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    auth_type: AzureSQLMetadata.AuthType
    def __init__(self, auth_type: _Optional[_Union[AzureSQLMetadata.AuthType, str]] = ...) -> None: ...

class ApiEntityExternalMetadata(_message.Message):
    __slots__ = ("azure_sql_metadata",)
    AZURE_SQL_ENTITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    azure_sql_entity_metadata: _descriptor.FieldDescriptor
    AZURE_SQL_METADATA_FIELD_NUMBER: _ClassVar[int]
    azure_sql_metadata: AzureSQLMetadata
    def __init__(self, azure_sql_metadata: _Optional[_Union[AzureSQLMetadata, _Mapping]] = ...) -> None: ...

class SqlPackage(_message.Message):
    __slots__ = ("compression", "max_parallelism", "verify_extraction")
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    MAX_PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    VERIFY_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    compression: _azure_pb2.Entity.CompressionOption
    max_parallelism: int
    verify_extraction: bool
    def __init__(self, compression: _Optional[_Union[_azure_pb2.Entity.CompressionOption, str]] = ..., max_parallelism: _Optional[int] = ..., verify_extraction: bool = ...) -> None: ...
