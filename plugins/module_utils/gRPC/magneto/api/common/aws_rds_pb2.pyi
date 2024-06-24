from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AwsEntity(_message.Message):
    __slots__ = ("id", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    display_name: str
    def __init__(self, id: _Optional[int] = ..., display_name: _Optional[str] = ...) -> None: ...

class AwsTargetParams(_message.Message):
    __slots__ = ("is_known_source", "known_source_config", "custom_server_config")
    class NetworkConfig(_message.Message):
        __slots__ = ("is_new_source", "source", "region", "instance", "ip", "port", "credentials")
        IS_NEW_SOURCE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        is_new_source: bool
        source: AwsEntity
        region: AwsEntity
        instance: AwsEntity
        ip: str
        port: int
        credentials: _magneto_external_base_pb2.CredentialsProto
        def __init__(self, is_new_source: bool = ..., source: _Optional[_Union[AwsEntity, _Mapping]] = ..., region: _Optional[_Union[AwsEntity, _Mapping]] = ..., instance: _Optional[_Union[AwsEntity, _Mapping]] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ..., credentials: _Optional[_Union[_magneto_external_base_pb2.CredentialsProto, _Mapping]] = ...) -> None: ...
    IS_KNOWN_SOURCE_FIELD_NUMBER: _ClassVar[int]
    KNOWN_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    is_known_source: bool
    known_source_config: AwsTargetParams.NetworkConfig
    custom_server_config: AwsTargetParams.NetworkConfig
    def __init__(self, is_known_source: bool = ..., known_source_config: _Optional[_Union[AwsTargetParams.NetworkConfig, _Mapping]] = ..., custom_server_config: _Optional[_Union[AwsTargetParams.NetworkConfig, _Mapping]] = ...) -> None: ...

class RestoreRDSPostgresParams(_message.Message):
    __slots__ = ("overwrite_database", "prefix_to_database_name", "aws_target_params", "suffix_to_database_name")
    OVERWRITE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_TO_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    AWS_TARGET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_TO_DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    overwrite_database: bool
    prefix_to_database_name: str
    aws_target_params: AwsTargetParams
    suffix_to_database_name: str
    def __init__(self, overwrite_database: bool = ..., prefix_to_database_name: _Optional[str] = ..., aws_target_params: _Optional[_Union[AwsTargetParams, _Mapping]] = ..., suffix_to_database_name: _Optional[str] = ...) -> None: ...
