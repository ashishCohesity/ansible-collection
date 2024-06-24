from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramProto(_message.Message):
    __slots__ = ("distribution_vec", "x_axis", "y_axis", "x_labels")
    DISTRIBUTION_VEC_FIELD_NUMBER: _ClassVar[int]
    X_AXIS_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_FIELD_NUMBER: _ClassVar[int]
    X_LABELS_FIELD_NUMBER: _ClassVar[int]
    distribution_vec: _containers.RepeatedScalarFieldContainer[int]
    x_axis: str
    y_axis: str
    x_labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, distribution_vec: _Optional[_Iterable[int]] = ..., x_axis: _Optional[str] = ..., y_axis: _Optional[str] = ..., x_labels: _Optional[_Iterable[str]] = ...) -> None: ...
