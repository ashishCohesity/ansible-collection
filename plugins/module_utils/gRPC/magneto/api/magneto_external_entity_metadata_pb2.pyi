from magneto.api import magneto_external_base_pb2 as _magneto_external_base_pb2
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityExternalMetadataProto(_message.Message):
    __slots__ = ("credentials", "maintenance_mode_config")
    Extensions: _python_message._ExtensionDict
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    credentials: _magneto_external_base_pb2.CredentialsProto
    maintenance_mode_config: _magneto_external_base_pb2.MaintenanceModeConfigProto
    def __init__(self, credentials: _Optional[_Union[_magneto_external_base_pb2.CredentialsProto, _Mapping]] = ..., maintenance_mode_config: _Optional[_Union[_magneto_external_base_pb2.MaintenanceModeConfigProto, _Mapping]] = ...) -> None: ...
