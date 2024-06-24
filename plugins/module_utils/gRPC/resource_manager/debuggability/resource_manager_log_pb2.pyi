from resource_manager import api_pb2 as _api_pb2
from resource_manager import persistent_state_pb2 as _persistent_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceManagerLogProto(_message.Message):
    __slots__ = ("acquire_arg", "release_arg", "add_or_update_providers_arg", "wal_record", "purged_request", "purged_entity_id", "checkpoint_triggered")
    ACQUIRE_ARG_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ARG_FIELD_NUMBER: _ClassVar[int]
    ADD_OR_UPDATE_PROVIDERS_ARG_FIELD_NUMBER: _ClassVar[int]
    WAL_RECORD_FIELD_NUMBER: _ClassVar[int]
    PURGED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PURGED_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    acquire_arg: _api_pb2.AcquireArg
    release_arg: _api_pb2.ReleaseArg
    add_or_update_providers_arg: _api_pb2.AddOrUpdateProvidersArg
    wal_record: _persistent_state_pb2.ResourceManagerWALRecordProto
    purged_request: _persistent_state_pb2.RequestStateProto
    purged_entity_id: str
    checkpoint_triggered: bool
    def __init__(self, acquire_arg: _Optional[_Union[_api_pb2.AcquireArg, _Mapping]] = ..., release_arg: _Optional[_Union[_api_pb2.ReleaseArg, _Mapping]] = ..., add_or_update_providers_arg: _Optional[_Union[_api_pb2.AddOrUpdateProvidersArg, _Mapping]] = ..., wal_record: _Optional[_Union[_persistent_state_pb2.ResourceManagerWALRecordProto, _Mapping]] = ..., purged_request: _Optional[_Union[_persistent_state_pb2.RequestStateProto, _Mapping]] = ..., purged_entity_id: _Optional[str] = ..., checkpoint_triggered: bool = ...) -> None: ...
