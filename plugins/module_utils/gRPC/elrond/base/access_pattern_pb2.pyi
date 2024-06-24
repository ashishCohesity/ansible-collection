from bridge.snap_fs import entity_handle_pb2 as _entity_handle_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemoryAccessSequence(_message.Message):
    __slots__ = ("entity_handle", "access_sequence")
    class ReadIO(_message.Message):
        __slots__ = ("offset_bytes", "length_bytes", "access_time_usecs")
        OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
        LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        offset_bytes: int
        length_bytes: int
        access_time_usecs: int
        def __init__(self, offset_bytes: _Optional[int] = ..., length_bytes: _Optional[int] = ..., access_time_usecs: _Optional[int] = ...) -> None: ...
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    entity_handle: _entity_handle_pb2.EntityHandleProto
    access_sequence: _containers.RepeatedCompositeFieldContainer[MemoryAccessSequence.ReadIO]
    def __init__(self, entity_handle: _Optional[_Union[_entity_handle_pb2.EntityHandleProto, _Mapping]] = ..., access_sequence: _Optional[_Iterable[_Union[MemoryAccessSequence.ReadIO, _Mapping]]] = ...) -> None: ...
