from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GoogleMessage2(_message.Message):
    __slots__ = ("field1", "field3", "field4", "field30", "field75", "field6", "field2", "field21", "field71", "field25", "field109", "field210", "field211", "field212", "field213", "field216", "field217", "field218", "field220", "field221", "field222", "field63", "group1", "field128", "field131", "field127", "field129", "field130", "field205", "field206")
    class Group1(_message.Message):
        __slots__ = ("field11", "field26", "field12", "field13", "field14", "field15", "field5", "field27", "field28", "field29", "field16", "field22", "field73", "field20", "field24", "field31")
        FIELD11_FIELD_NUMBER: _ClassVar[int]
        FIELD26_FIELD_NUMBER: _ClassVar[int]
        FIELD12_FIELD_NUMBER: _ClassVar[int]
        FIELD13_FIELD_NUMBER: _ClassVar[int]
        FIELD14_FIELD_NUMBER: _ClassVar[int]
        FIELD15_FIELD_NUMBER: _ClassVar[int]
        FIELD5_FIELD_NUMBER: _ClassVar[int]
        FIELD27_FIELD_NUMBER: _ClassVar[int]
        FIELD28_FIELD_NUMBER: _ClassVar[int]
        FIELD29_FIELD_NUMBER: _ClassVar[int]
        FIELD16_FIELD_NUMBER: _ClassVar[int]
        FIELD22_FIELD_NUMBER: _ClassVar[int]
        FIELD73_FIELD_NUMBER: _ClassVar[int]
        FIELD20_FIELD_NUMBER: _ClassVar[int]
        FIELD24_FIELD_NUMBER: _ClassVar[int]
        FIELD31_FIELD_NUMBER: _ClassVar[int]
        field11: float
        field26: float
        field12: str
        field13: str
        field14: _containers.RepeatedScalarFieldContainer[str]
        field15: int
        field5: int
        field27: str
        field28: int
        field29: str
        field16: str
        field22: _containers.RepeatedScalarFieldContainer[str]
        field73: _containers.RepeatedScalarFieldContainer[int]
        field20: int
        field24: str
        field31: GoogleMessage2GroupedMessage
        def __init__(self, field11: _Optional[float] = ..., field26: _Optional[float] = ..., field12: _Optional[str] = ..., field13: _Optional[str] = ..., field14: _Optional[_Iterable[str]] = ..., field15: _Optional[int] = ..., field5: _Optional[int] = ..., field27: _Optional[str] = ..., field28: _Optional[int] = ..., field29: _Optional[str] = ..., field16: _Optional[str] = ..., field22: _Optional[_Iterable[str]] = ..., field73: _Optional[_Iterable[int]] = ..., field20: _Optional[int] = ..., field24: _Optional[str] = ..., field31: _Optional[_Union[GoogleMessage2GroupedMessage, _Mapping]] = ...) -> None: ...
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    FIELD4_FIELD_NUMBER: _ClassVar[int]
    FIELD30_FIELD_NUMBER: _ClassVar[int]
    FIELD75_FIELD_NUMBER: _ClassVar[int]
    FIELD6_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD21_FIELD_NUMBER: _ClassVar[int]
    FIELD71_FIELD_NUMBER: _ClassVar[int]
    FIELD25_FIELD_NUMBER: _ClassVar[int]
    FIELD109_FIELD_NUMBER: _ClassVar[int]
    FIELD210_FIELD_NUMBER: _ClassVar[int]
    FIELD211_FIELD_NUMBER: _ClassVar[int]
    FIELD212_FIELD_NUMBER: _ClassVar[int]
    FIELD213_FIELD_NUMBER: _ClassVar[int]
    FIELD216_FIELD_NUMBER: _ClassVar[int]
    FIELD217_FIELD_NUMBER: _ClassVar[int]
    FIELD218_FIELD_NUMBER: _ClassVar[int]
    FIELD220_FIELD_NUMBER: _ClassVar[int]
    FIELD221_FIELD_NUMBER: _ClassVar[int]
    FIELD222_FIELD_NUMBER: _ClassVar[int]
    FIELD63_FIELD_NUMBER: _ClassVar[int]
    GROUP1_FIELD_NUMBER: _ClassVar[int]
    FIELD128_FIELD_NUMBER: _ClassVar[int]
    FIELD131_FIELD_NUMBER: _ClassVar[int]
    FIELD127_FIELD_NUMBER: _ClassVar[int]
    FIELD129_FIELD_NUMBER: _ClassVar[int]
    FIELD130_FIELD_NUMBER: _ClassVar[int]
    FIELD205_FIELD_NUMBER: _ClassVar[int]
    FIELD206_FIELD_NUMBER: _ClassVar[int]
    field1: str
    field3: int
    field4: int
    field30: int
    field75: bool
    field6: str
    field2: bytes
    field21: int
    field71: int
    field25: float
    field109: int
    field210: int
    field211: int
    field212: int
    field213: int
    field216: int
    field217: int
    field218: int
    field220: int
    field221: int
    field222: float
    field63: int
    group1: _containers.RepeatedCompositeFieldContainer[GoogleMessage2.Group1]
    field128: _containers.RepeatedScalarFieldContainer[str]
    field131: int
    field127: _containers.RepeatedScalarFieldContainer[str]
    field129: int
    field130: _containers.RepeatedScalarFieldContainer[int]
    field205: bool
    field206: bool
    def __init__(self, field1: _Optional[str] = ..., field3: _Optional[int] = ..., field4: _Optional[int] = ..., field30: _Optional[int] = ..., field75: bool = ..., field6: _Optional[str] = ..., field2: _Optional[bytes] = ..., field21: _Optional[int] = ..., field71: _Optional[int] = ..., field25: _Optional[float] = ..., field109: _Optional[int] = ..., field210: _Optional[int] = ..., field211: _Optional[int] = ..., field212: _Optional[int] = ..., field213: _Optional[int] = ..., field216: _Optional[int] = ..., field217: _Optional[int] = ..., field218: _Optional[int] = ..., field220: _Optional[int] = ..., field221: _Optional[int] = ..., field222: _Optional[float] = ..., field63: _Optional[int] = ..., group1: _Optional[_Iterable[_Union[GoogleMessage2.Group1, _Mapping]]] = ..., field128: _Optional[_Iterable[str]] = ..., field131: _Optional[int] = ..., field127: _Optional[_Iterable[str]] = ..., field129: _Optional[int] = ..., field130: _Optional[_Iterable[int]] = ..., field205: bool = ..., field206: bool = ...) -> None: ...

class GoogleMessage2GroupedMessage(_message.Message):
    __slots__ = ("field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8", "field9", "field10", "field11")
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    FIELD4_FIELD_NUMBER: _ClassVar[int]
    FIELD5_FIELD_NUMBER: _ClassVar[int]
    FIELD6_FIELD_NUMBER: _ClassVar[int]
    FIELD7_FIELD_NUMBER: _ClassVar[int]
    FIELD8_FIELD_NUMBER: _ClassVar[int]
    FIELD9_FIELD_NUMBER: _ClassVar[int]
    FIELD10_FIELD_NUMBER: _ClassVar[int]
    FIELD11_FIELD_NUMBER: _ClassVar[int]
    field1: float
    field2: float
    field3: float
    field4: bool
    field5: bool
    field6: bool
    field7: bool
    field8: float
    field9: bool
    field10: float
    field11: int
    def __init__(self, field1: _Optional[float] = ..., field2: _Optional[float] = ..., field3: _Optional[float] = ..., field4: bool = ..., field5: bool = ..., field6: bool = ..., field7: bool = ..., field8: _Optional[float] = ..., field9: bool = ..., field10: _Optional[float] = ..., field11: _Optional[int] = ...) -> None: ...
