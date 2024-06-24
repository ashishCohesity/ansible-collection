from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessModel(_message.Message):
    __slots__ = ("matched_predicted_blocks",)
    class MatchedPredictedBlocks(_message.Message):
        __slots__ = ("matched_blocks", "predicted_blocks")
        MATCHED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
        PREDICTED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
        matched_blocks: _containers.RepeatedScalarFieldContainer[int]
        predicted_blocks: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, matched_blocks: _Optional[_Iterable[int]] = ..., predicted_blocks: _Optional[_Iterable[int]] = ...) -> None: ...
    MATCHED_PREDICTED_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    matched_predicted_blocks: _containers.RepeatedCompositeFieldContainer[AccessModel.MatchedPredictedBlocks]
    def __init__(self, matched_predicted_blocks: _Optional[_Iterable[_Union[AccessModel.MatchedPredictedBlocks, _Mapping]]] = ...) -> None: ...

class AccessModelInfo(_message.Message):
    __slots__ = ("model_version",)
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    model_version: int
    def __init__(self, model_version: _Optional[int] = ...) -> None: ...
