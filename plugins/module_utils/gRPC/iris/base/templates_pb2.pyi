from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateProto(_message.Message):
    __slots__ = ("id", "name", "description", "last_modified_time_msecs", "template_details")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_MSECS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    last_modified_time_msecs: int
    template_details: _magneto_pb2.BackupJobProto
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., last_modified_time_msecs: _Optional[int] = ..., template_details: _Optional[_Union[_magneto_pb2.BackupJobProto, _Mapping]] = ...) -> None: ...
