from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APIVersion(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class WALPersisterTestProto(_message.Message):
    __slots__ = ("api_version", "persistent_state_proto_vec", "record_id", "message", "ignored_delta_record_limit")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_STATE_PROTO_VEC_FIELD_NUMBER: _ClassVar[int]
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IGNORED_DELTA_RECORD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    api_version: APIVersion
    persistent_state_proto_vec: _containers.RepeatedCompositeFieldContainer[WALPersisterTestProto]
    record_id: int
    message: str
    ignored_delta_record_limit: int
    def __init__(self, api_version: _Optional[_Union[APIVersion, _Mapping]] = ..., persistent_state_proto_vec: _Optional[_Iterable[_Union[WALPersisterTestProto, _Mapping]]] = ..., record_id: _Optional[int] = ..., message: _Optional[str] = ..., ignored_delta_record_limit: _Optional[int] = ...) -> None: ...
