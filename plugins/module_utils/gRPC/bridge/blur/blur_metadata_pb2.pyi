from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlurBlobEntityProto(_message.Message):
    __slots__ = ("value_version", "value_size", "sequencer", "first_version_in_blur", "entity_type")
    VALUE_VERSION_FIELD_NUMBER: _ClassVar[int]
    VALUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    FIRST_VERSION_IN_BLUR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    value_version: _snap_tree_pb2.SnapTreeValueVersionProto
    value_size: int
    sequencer: int
    first_version_in_blur: int
    entity_type: int
    def __init__(self, value_version: _Optional[_Union[_snap_tree_pb2.SnapTreeValueVersionProto, _Mapping]] = ..., value_size: _Optional[int] = ..., sequencer: _Optional[int] = ..., first_version_in_blur: _Optional[int] = ..., entity_type: _Optional[int] = ...) -> None: ...
