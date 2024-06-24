from atom.base import mongodb_pb2 as _mongodb_pb2
from atom.base import event_pb2 as _event_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MongoDBDataEvent(_message.Message):
    __slots__ = ("data_type", "start_seq_num", "end_seq_num")
    MONGODB_DATA_EVENT_FIELD_NUMBER: _ClassVar[int]
    mongodb_data_event: _descriptor.FieldDescriptor
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    END_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    data_type: _mongodb_pb2.DataType
    start_seq_num: _mongodb_pb2.SequenceNumber
    end_seq_num: _mongodb_pb2.SequenceNumber
    def __init__(self, data_type: _Optional[_Union[_mongodb_pb2.DataType, str]] = ..., start_seq_num: _Optional[_Union[_mongodb_pb2.SequenceNumber, _Mapping]] = ..., end_seq_num: _Optional[_Union[_mongodb_pb2.SequenceNumber, _Mapping]] = ...) -> None: ...
