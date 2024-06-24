from yoda.util import work_item_pb2 as _work_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkQueueWALEntry(_message.Message):
    __slots__ = ("pending_item", "finished_work_id")
    PENDING_ITEM_FIELD_NUMBER: _ClassVar[int]
    FINISHED_WORK_ID_FIELD_NUMBER: _ClassVar[int]
    pending_item: _containers.RepeatedCompositeFieldContainer[_work_item_pb2.WorkItem]
    finished_work_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pending_item: _Optional[_Iterable[_Union[_work_item_pb2.WorkItem, _Mapping]]] = ..., finished_work_id: _Optional[_Iterable[int]] = ...) -> None: ...
