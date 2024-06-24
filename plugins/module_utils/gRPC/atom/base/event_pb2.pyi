from atom.base import entity_pb2 as _entity_pb2
from atom.base import vmware_pb2 as _vmware_pb2
from atom.base import mongodb_pb2 as _mongodb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataEvent(_message.Message):
    __slots__ = ("data_size", "file_path", "shard_locator_file_path", "epoch_id")
    Extensions: _python_message._ExtensionDict
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SHARD_LOCATOR_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    data_size: int
    file_path: str
    shard_locator_file_path: str
    epoch_id: int
    def __init__(self, data_size: _Optional[int] = ..., file_path: _Optional[str] = ..., shard_locator_file_path: _Optional[str] = ..., epoch_id: _Optional[int] = ...) -> None: ...

class EntityEventsProto(_message.Message):
    __slots__ = ("entity_id", "data_event_vec", "scribe_version")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_EVENT_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_VERSION_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    data_event_vec: _containers.RepeatedCompositeFieldContainer[DataEvent]
    scribe_version: int
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., data_event_vec: _Optional[_Iterable[_Union[DataEvent, _Mapping]]] = ..., scribe_version: _Optional[int] = ...) -> None: ...

class Sequencer(_message.Message):
    __slots__ = ("vmware_sequencer", "mongodb_sequencer")
    VMWARE_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    MONGODB_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    vmware_sequencer: _vmware_pb2.SequenceNumber
    mongodb_sequencer: _mongodb_pb2.SequenceNumber
    def __init__(self, vmware_sequencer: _Optional[_Union[_vmware_pb2.SequenceNumber, _Mapping]] = ..., mongodb_sequencer: _Optional[_Union[_mongodb_pb2.SequenceNumber, _Mapping]] = ...) -> None: ...

class ShardLocatorEntry(_message.Message):
    __slots__ = ("file_name", "file_offset", "data_size", "start_sequencer", "end_sequencer")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    START_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    END_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_offset: int
    data_size: int
    start_sequencer: Sequencer
    end_sequencer: Sequencer
    def __init__(self, file_name: _Optional[str] = ..., file_offset: _Optional[int] = ..., data_size: _Optional[int] = ..., start_sequencer: _Optional[_Union[Sequencer, _Mapping]] = ..., end_sequencer: _Optional[_Union[Sequencer, _Mapping]] = ...) -> None: ...
