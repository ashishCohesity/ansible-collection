from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SizeMessage1(_message.Message):
    __slots__ = ("field1", "field9", "field18", "field80", "field81", "field2", "field3", "field280", "field6", "field22", "field4", "field5", "field59", "field7", "field16", "field130", "field12", "field17", "field13", "field14", "field104", "field100", "field101", "field102", "field103", "field29", "field30", "field60", "field271", "field272", "field150", "field23", "field24", "field25", "field15", "field78", "field67", "field68", "field128", "field129", "field131")
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD9_FIELD_NUMBER: _ClassVar[int]
    FIELD18_FIELD_NUMBER: _ClassVar[int]
    FIELD80_FIELD_NUMBER: _ClassVar[int]
    FIELD81_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    FIELD280_FIELD_NUMBER: _ClassVar[int]
    FIELD6_FIELD_NUMBER: _ClassVar[int]
    FIELD22_FIELD_NUMBER: _ClassVar[int]
    FIELD4_FIELD_NUMBER: _ClassVar[int]
    FIELD5_FIELD_NUMBER: _ClassVar[int]
    FIELD59_FIELD_NUMBER: _ClassVar[int]
    FIELD7_FIELD_NUMBER: _ClassVar[int]
    FIELD16_FIELD_NUMBER: _ClassVar[int]
    FIELD130_FIELD_NUMBER: _ClassVar[int]
    FIELD12_FIELD_NUMBER: _ClassVar[int]
    FIELD17_FIELD_NUMBER: _ClassVar[int]
    FIELD13_FIELD_NUMBER: _ClassVar[int]
    FIELD14_FIELD_NUMBER: _ClassVar[int]
    FIELD104_FIELD_NUMBER: _ClassVar[int]
    FIELD100_FIELD_NUMBER: _ClassVar[int]
    FIELD101_FIELD_NUMBER: _ClassVar[int]
    FIELD102_FIELD_NUMBER: _ClassVar[int]
    FIELD103_FIELD_NUMBER: _ClassVar[int]
    FIELD29_FIELD_NUMBER: _ClassVar[int]
    FIELD30_FIELD_NUMBER: _ClassVar[int]
    FIELD60_FIELD_NUMBER: _ClassVar[int]
    FIELD271_FIELD_NUMBER: _ClassVar[int]
    FIELD272_FIELD_NUMBER: _ClassVar[int]
    FIELD150_FIELD_NUMBER: _ClassVar[int]
    FIELD23_FIELD_NUMBER: _ClassVar[int]
    FIELD24_FIELD_NUMBER: _ClassVar[int]
    FIELD25_FIELD_NUMBER: _ClassVar[int]
    FIELD15_FIELD_NUMBER: _ClassVar[int]
    FIELD78_FIELD_NUMBER: _ClassVar[int]
    FIELD67_FIELD_NUMBER: _ClassVar[int]
    FIELD68_FIELD_NUMBER: _ClassVar[int]
    FIELD128_FIELD_NUMBER: _ClassVar[int]
    FIELD129_FIELD_NUMBER: _ClassVar[int]
    FIELD131_FIELD_NUMBER: _ClassVar[int]
    field1: str
    field9: str
    field18: str
    field80: bool
    field81: bool
    field2: int
    field3: int
    field280: int
    field6: int
    field22: int
    field4: str
    field5: _containers.RepeatedScalarFieldContainer[int]
    field59: bool
    field7: str
    field16: int
    field130: int
    field12: bool
    field17: bool
    field13: bool
    field14: bool
    field104: int
    field100: int
    field101: int
    field102: str
    field103: str
    field29: int
    field30: bool
    field60: int
    field271: int
    field272: int
    field150: int
    field23: int
    field24: bool
    field25: int
    field15: SizeMessage1SubMessage
    field78: bool
    field67: int
    field68: int
    field128: int
    field129: str
    field131: int
    def __init__(self, field1: _Optional[str] = ..., field9: _Optional[str] = ..., field18: _Optional[str] = ..., field80: bool = ..., field81: bool = ..., field2: _Optional[int] = ..., field3: _Optional[int] = ..., field280: _Optional[int] = ..., field6: _Optional[int] = ..., field22: _Optional[int] = ..., field4: _Optional[str] = ..., field5: _Optional[_Iterable[int]] = ..., field59: bool = ..., field7: _Optional[str] = ..., field16: _Optional[int] = ..., field130: _Optional[int] = ..., field12: bool = ..., field17: bool = ..., field13: bool = ..., field14: bool = ..., field104: _Optional[int] = ..., field100: _Optional[int] = ..., field101: _Optional[int] = ..., field102: _Optional[str] = ..., field103: _Optional[str] = ..., field29: _Optional[int] = ..., field30: bool = ..., field60: _Optional[int] = ..., field271: _Optional[int] = ..., field272: _Optional[int] = ..., field150: _Optional[int] = ..., field23: _Optional[int] = ..., field24: bool = ..., field25: _Optional[int] = ..., field15: _Optional[_Union[SizeMessage1SubMessage, _Mapping]] = ..., field78: bool = ..., field67: _Optional[int] = ..., field68: _Optional[int] = ..., field128: _Optional[int] = ..., field129: _Optional[str] = ..., field131: _Optional[int] = ...) -> None: ...

class SizeMessage1SubMessage(_message.Message):
    __slots__ = ("field1", "field2", "field3", "field15", "field12", "field13", "field14", "field16", "field19", "field20", "field28", "field21", "field22", "field23", "field206", "field203", "field204", "field205", "field207", "field300")
    FIELD1_FIELD_NUMBER: _ClassVar[int]
    FIELD2_FIELD_NUMBER: _ClassVar[int]
    FIELD3_FIELD_NUMBER: _ClassVar[int]
    FIELD15_FIELD_NUMBER: _ClassVar[int]
    FIELD12_FIELD_NUMBER: _ClassVar[int]
    FIELD13_FIELD_NUMBER: _ClassVar[int]
    FIELD14_FIELD_NUMBER: _ClassVar[int]
    FIELD16_FIELD_NUMBER: _ClassVar[int]
    FIELD19_FIELD_NUMBER: _ClassVar[int]
    FIELD20_FIELD_NUMBER: _ClassVar[int]
    FIELD28_FIELD_NUMBER: _ClassVar[int]
    FIELD21_FIELD_NUMBER: _ClassVar[int]
    FIELD22_FIELD_NUMBER: _ClassVar[int]
    FIELD23_FIELD_NUMBER: _ClassVar[int]
    FIELD206_FIELD_NUMBER: _ClassVar[int]
    FIELD203_FIELD_NUMBER: _ClassVar[int]
    FIELD204_FIELD_NUMBER: _ClassVar[int]
    FIELD205_FIELD_NUMBER: _ClassVar[int]
    FIELD207_FIELD_NUMBER: _ClassVar[int]
    FIELD300_FIELD_NUMBER: _ClassVar[int]
    field1: int
    field2: int
    field3: int
    field15: str
    field12: bool
    field13: int
    field14: int
    field16: int
    field19: int
    field20: bool
    field28: bool
    field21: int
    field22: int
    field23: bool
    field206: bool
    field203: int
    field204: int
    field205: str
    field207: int
    field300: int
    def __init__(self, field1: _Optional[int] = ..., field2: _Optional[int] = ..., field3: _Optional[int] = ..., field15: _Optional[str] = ..., field12: bool = ..., field13: _Optional[int] = ..., field14: _Optional[int] = ..., field16: _Optional[int] = ..., field19: _Optional[int] = ..., field20: bool = ..., field28: bool = ..., field21: _Optional[int] = ..., field22: _Optional[int] = ..., field23: bool = ..., field206: bool = ..., field203: _Optional[int] = ..., field204: _Optional[int] = ..., field205: _Optional[str] = ..., field207: _Optional[int] = ..., field300: _Optional[int] = ...) -> None: ...

class SizeMessage2(_message.Message):
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
        field31: SizeMessage2GroupedMessage
        def __init__(self, field11: _Optional[float] = ..., field26: _Optional[float] = ..., field12: _Optional[str] = ..., field13: _Optional[str] = ..., field14: _Optional[_Iterable[str]] = ..., field15: _Optional[int] = ..., field5: _Optional[int] = ..., field27: _Optional[str] = ..., field28: _Optional[int] = ..., field29: _Optional[str] = ..., field16: _Optional[str] = ..., field22: _Optional[_Iterable[str]] = ..., field73: _Optional[_Iterable[int]] = ..., field20: _Optional[int] = ..., field24: _Optional[str] = ..., field31: _Optional[_Union[SizeMessage2GroupedMessage, _Mapping]] = ...) -> None: ...
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
    group1: _containers.RepeatedCompositeFieldContainer[SizeMessage2.Group1]
    field128: _containers.RepeatedScalarFieldContainer[str]
    field131: int
    field127: _containers.RepeatedScalarFieldContainer[str]
    field129: int
    field130: _containers.RepeatedScalarFieldContainer[int]
    field205: bool
    field206: bool
    def __init__(self, field1: _Optional[str] = ..., field3: _Optional[int] = ..., field4: _Optional[int] = ..., field30: _Optional[int] = ..., field75: bool = ..., field6: _Optional[str] = ..., field2: _Optional[bytes] = ..., field21: _Optional[int] = ..., field71: _Optional[int] = ..., field25: _Optional[float] = ..., field109: _Optional[int] = ..., field210: _Optional[int] = ..., field211: _Optional[int] = ..., field212: _Optional[int] = ..., field213: _Optional[int] = ..., field216: _Optional[int] = ..., field217: _Optional[int] = ..., field218: _Optional[int] = ..., field220: _Optional[int] = ..., field221: _Optional[int] = ..., field222: _Optional[float] = ..., field63: _Optional[int] = ..., group1: _Optional[_Iterable[_Union[SizeMessage2.Group1, _Mapping]]] = ..., field128: _Optional[_Iterable[str]] = ..., field131: _Optional[int] = ..., field127: _Optional[_Iterable[str]] = ..., field129: _Optional[int] = ..., field130: _Optional[_Iterable[int]] = ..., field205: bool = ..., field206: bool = ...) -> None: ...

class SizeMessage2GroupedMessage(_message.Message):
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
