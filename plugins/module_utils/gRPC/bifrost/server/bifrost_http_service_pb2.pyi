from bifrost.base import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostHttpConfigProto(_message.Message):
    __slots__ = ("upload_configuration_file_url", "status_page_url", "get_hyx_health_url", "download_agent_installer_from_cluster_url", "get_hyx_config_url")
    UPLOAD_CONFIGURATION_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_HYX_HEALTH_URL_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_AGENT_INSTALLER_FROM_CLUSTER_URL_FIELD_NUMBER: _ClassVar[int]
    GET_HYX_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    upload_configuration_file_url: str
    status_page_url: str
    get_hyx_health_url: str
    download_agent_installer_from_cluster_url: str
    get_hyx_config_url: str
    def __init__(self, upload_configuration_file_url: _Optional[str] = ..., status_page_url: _Optional[str] = ..., get_hyx_health_url: _Optional[str] = ..., download_agent_installer_from_cluster_url: _Optional[str] = ..., get_hyx_config_url: _Optional[str] = ...) -> None: ...

class DownloadAgentFromClusterArg(_message.Message):
    __slots__ = ("filename", "sha512_sum")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SHA512_SUM_FIELD_NUMBER: _ClassVar[int]
    filename: str
    sha512_sum: bytes
    def __init__(self, filename: _Optional[str] = ..., sha512_sum: _Optional[bytes] = ...) -> None: ...

class DownloadAgentFromClusterResult(_message.Message):
    __slots__ = ("error", "message", "download_filepath")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    message: str
    download_filepath: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., message: _Optional[str] = ..., download_filepath: _Optional[str] = ...) -> None: ...
