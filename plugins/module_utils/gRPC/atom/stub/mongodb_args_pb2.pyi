from atom.base import mongodb_pb2 as _mongodb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MongoDBData(_message.Message):
    __slots__ = ("data_type", "change_events", "version")
    class ChangeEvent(_message.Message):
        __slots__ = ("sequence_num", "data")
        SEQUENCE_NUM_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        sequence_num: _mongodb_pb2.SequenceNumber
        data: bytes
        def __init__(self, sequence_num: _Optional[_Union[_mongodb_pb2.SequenceNumber, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    data_type: _mongodb_pb2.DataType
    change_events: _containers.RepeatedCompositeFieldContainer[MongoDBData.ChangeEvent]
    version: int
    def __init__(self, data_type: _Optional[_Union[_mongodb_pb2.DataType, str]] = ..., change_events: _Optional[_Iterable[_Union[MongoDBData.ChangeEvent, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class MongoDBAdditionalInfo(_message.Message):
    __slots__ = ("atom_instance_id",)
    ATOM_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    atom_instance_id: int
    def __init__(self, atom_instance_id: _Optional[int] = ...) -> None: ...
