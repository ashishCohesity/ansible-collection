from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExampleProto(_message.Message):
    __slots__ = ("str", "number", "long_number", "ids")
    class SubMessageProto(_message.Message):
        __slots__ = ("m_id",)
        M_ID_FIELD_NUMBER: _ClassVar[int]
        m_id: int
        def __init__(self, m_id: _Optional[int] = ...) -> None: ...
    STR_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    LONG_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    str: str
    number: int
    long_number: int
    ids: _containers.RepeatedCompositeFieldContainer[ExampleProto.SubMessageProto]
    def __init__(self, str: _Optional[str] = ..., number: _Optional[int] = ..., long_number: _Optional[int] = ..., ids: _Optional[_Iterable[_Union[ExampleProto.SubMessageProto, _Mapping]]] = ...) -> None: ...
