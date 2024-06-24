from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadIODataProto(_message.Message):
    __slots__ = ("track_data_vec",)
    class ReadIO(_message.Message):
        __slots__ = ("entity_handle_index", "offset_bytes", "count_bytes")
        ENTITY_HANDLE_INDEX_FIELD_NUMBER: _ClassVar[int]
        OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
        COUNT_BYTES_FIELD_NUMBER: _ClassVar[int]
        entity_handle_index: int
        offset_bytes: int
        count_bytes: int
        def __init__(self, entity_handle_index: _Optional[int] = ..., offset_bytes: _Optional[int] = ..., count_bytes: _Optional[int] = ...) -> None: ...
    TRACK_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    track_data_vec: _containers.RepeatedCompositeFieldContainer[ReadIODataProto.ReadIO]
    def __init__(self, track_data_vec: _Optional[_Iterable[_Union[ReadIODataProto.ReadIO, _Mapping]]] = ...) -> None: ...
