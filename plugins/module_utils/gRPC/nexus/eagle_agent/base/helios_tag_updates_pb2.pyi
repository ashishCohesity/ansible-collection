from yoda.base import yoda_pb2 as _yoda_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagUpdatesBatch(_message.Message):
    __slots__ = ("tag_updates_vec",)
    TAG_UPDATES_VEC_FIELD_NUMBER: _ClassVar[int]
    tag_updates_vec: _containers.RepeatedCompositeFieldContainer[_yoda_pb2.TagUpdate]
    def __init__(self, tag_updates_vec: _Optional[_Iterable[_Union[_yoda_pb2.TagUpdate, _Mapping]]] = ...) -> None: ...
