from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HeliosConfigProto(_message.Message):
    __slots__ = ("storage_config_dirpath", "certs_path", "self_signed_cert_path", "self_signed_key_path", "config_json_path", "helios_app_url", "helios_app_port", "helios_app_data_port", "gflag_config_dirpath", "gflag_config_filename")
    STORAGE_CONFIG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    CERTS_PATH_FIELD_NUMBER: _ClassVar[int]
    SELF_SIGNED_CERT_PATH_FIELD_NUMBER: _ClassVar[int]
    SELF_SIGNED_KEY_PATH_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_PATH_FIELD_NUMBER: _ClassVar[int]
    HELIOS_APP_URL_FIELD_NUMBER: _ClassVar[int]
    HELIOS_APP_PORT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_APP_DATA_PORT_FIELD_NUMBER: _ClassVar[int]
    GFLAG_CONFIG_DIRPATH_FIELD_NUMBER: _ClassVar[int]
    GFLAG_CONFIG_FILENAME_FIELD_NUMBER: _ClassVar[int]
    storage_config_dirpath: str
    certs_path: str
    self_signed_cert_path: str
    self_signed_key_path: str
    config_json_path: str
    helios_app_url: str
    helios_app_port: str
    helios_app_data_port: str
    gflag_config_dirpath: str
    gflag_config_filename: str
    def __init__(self, storage_config_dirpath: _Optional[str] = ..., certs_path: _Optional[str] = ..., self_signed_cert_path: _Optional[str] = ..., self_signed_key_path: _Optional[str] = ..., config_json_path: _Optional[str] = ..., helios_app_url: _Optional[str] = ..., helios_app_port: _Optional[str] = ..., helios_app_data_port: _Optional[str] = ..., gflag_config_dirpath: _Optional[str] = ..., gflag_config_filename: _Optional[str] = ...) -> None: ...

class HeliosOnPremConfigProto(_message.Message):
    __slots__ = ("prana_service",)
    PRANA_SERVICE_FIELD_NUMBER: _ClassVar[int]
    prana_service: str
    def __init__(self, prana_service: _Optional[str] = ...) -> None: ...

class HeliosServicesProto(_message.Message):
    __slots__ = ("prana_service_name", "mcmetl_service_name", "datareceiver_service_name", "bookkeeper_service_name", "redis_service_name", "iris_service_name", "iris_he13_service_name", "iris_he14_service_name", "nginx_service_name", "zookeeper_service_name", "kafka_service_name", "postgres_service_name", "reporting_service_name", "optimus_service_name", "elasticsearch_service_name", "prometheus_service_name")
    PRANA_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    MCMETL_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATARECEIVER_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    BOOKKEEPER_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    REDIS_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    IRIS_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    IRIS_HE13_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    IRIS_HE14_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    NGINX_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ZOOKEEPER_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    KAFKA_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    POSTGRES_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORTING_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIMUS_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ELASTICSEARCH_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROMETHEUS_SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    prana_service_name: str
    mcmetl_service_name: str
    datareceiver_service_name: str
    bookkeeper_service_name: str
    redis_service_name: str
    iris_service_name: str
    iris_he13_service_name: str
    iris_he14_service_name: str
    nginx_service_name: str
    zookeeper_service_name: str
    kafka_service_name: str
    postgres_service_name: str
    reporting_service_name: str
    optimus_service_name: str
    elasticsearch_service_name: str
    prometheus_service_name: str
    def __init__(self, prana_service_name: _Optional[str] = ..., mcmetl_service_name: _Optional[str] = ..., datareceiver_service_name: _Optional[str] = ..., bookkeeper_service_name: _Optional[str] = ..., redis_service_name: _Optional[str] = ..., iris_service_name: _Optional[str] = ..., iris_he13_service_name: _Optional[str] = ..., iris_he14_service_name: _Optional[str] = ..., nginx_service_name: _Optional[str] = ..., zookeeper_service_name: _Optional[str] = ..., kafka_service_name: _Optional[str] = ..., postgres_service_name: _Optional[str] = ..., reporting_service_name: _Optional[str] = ..., optimus_service_name: _Optional[str] = ..., elasticsearch_service_name: _Optional[str] = ..., prometheus_service_name: _Optional[str] = ...) -> None: ...
