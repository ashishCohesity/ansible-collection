from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GoogleMessage1(_message.Message):
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
    field15: GoogleMessage1SubMessage
    field78: bool
    field67: int
    field68: int
    field128: int
    field129: str
    field131: int
    def __init__(self, field1: _Optional[str] = ..., field9: _Optional[str] = ..., field18: _Optional[str] = ..., field80: bool = ..., field81: bool = ..., field2: _Optional[int] = ..., field3: _Optional[int] = ..., field280: _Optional[int] = ..., field6: _Optional[int] = ..., field22: _Optional[int] = ..., field4: _Optional[str] = ..., field5: _Optional[_Iterable[int]] = ..., field59: bool = ..., field7: _Optional[str] = ..., field16: _Optional[int] = ..., field130: _Optional[int] = ..., field12: bool = ..., field17: bool = ..., field13: bool = ..., field14: bool = ..., field104: _Optional[int] = ..., field100: _Optional[int] = ..., field101: _Optional[int] = ..., field102: _Optional[str] = ..., field103: _Optional[str] = ..., field29: _Optional[int] = ..., field30: bool = ..., field60: _Optional[int] = ..., field271: _Optional[int] = ..., field272: _Optional[int] = ..., field150: _Optional[int] = ..., field23: _Optional[int] = ..., field24: bool = ..., field25: _Optional[int] = ..., field15: _Optional[_Union[GoogleMessage1SubMessage, _Mapping]] = ..., field78: bool = ..., field67: _Optional[int] = ..., field68: _Optional[int] = ..., field128: _Optional[int] = ..., field129: _Optional[str] = ..., field131: _Optional[int] = ...) -> None: ...

class GoogleMessage1SubMessage(_message.Message):
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
