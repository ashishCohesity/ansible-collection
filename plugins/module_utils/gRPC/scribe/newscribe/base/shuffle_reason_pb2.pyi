from scribe.newscribe.base import view_config_pb2 as _view_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShuffleInfoProto(_message.Message):
    __slots__ = ("shuffle_timestamp_msecs", "view_config_pre_trigger", "view_config_post_trigger", "shuffle_reason")
    class ShuffleReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknownTrigger: _ClassVar[ShuffleInfoProto.ShuffleReason]
        kConfigOrStateChange: _ClassVar[ShuffleInfoProto.ShuffleReason]
        kBucketOptionsChange: _ClassVar[ShuffleInfoProto.ShuffleReason]
        kMasterGflagChange: _ClassVar[ShuffleInfoProto.ShuffleReason]
        kTestTrigger: _ClassVar[ShuffleInfoProto.ShuffleReason]
    kUnknownTrigger: ShuffleInfoProto.ShuffleReason
    kConfigOrStateChange: ShuffleInfoProto.ShuffleReason
    kBucketOptionsChange: ShuffleInfoProto.ShuffleReason
    kMasterGflagChange: ShuffleInfoProto.ShuffleReason
    kTestTrigger: ShuffleInfoProto.ShuffleReason
    SHUFFLE_TIMESTAMP_MSECS_FIELD_NUMBER: _ClassVar[int]
    VIEW_CONFIG_PRE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    VIEW_CONFIG_POST_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_REASON_FIELD_NUMBER: _ClassVar[int]
    shuffle_timestamp_msecs: int
    view_config_pre_trigger: _view_config_pb2.ViewConfigProto
    view_config_post_trigger: _view_config_pb2.ViewConfigProto
    shuffle_reason: ShuffleInfoProto.ShuffleReason
    def __init__(self, shuffle_timestamp_msecs: _Optional[int] = ..., view_config_pre_trigger: _Optional[_Union[_view_config_pb2.ViewConfigProto, _Mapping]] = ..., view_config_post_trigger: _Optional[_Union[_view_config_pb2.ViewConfigProto, _Mapping]] = ..., shuffle_reason: _Optional[_Union[ShuffleInfoProto.ShuffleReason, str]] = ...) -> None: ...

class ShuffleRecordsProto(_message.Message):
    __slots__ = ("shuffle_info_vec",)
    SHUFFLE_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    shuffle_info_vec: _containers.RepeatedCompositeFieldContainer[ShuffleInfoProto]
    def __init__(self, shuffle_info_vec: _Optional[_Iterable[_Union[ShuffleInfoProto, _Mapping]]] = ...) -> None: ...
