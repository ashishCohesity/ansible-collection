from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MagnetoStateKafkaMessage(_message.Message):
    __slots__ = ("cluster_id", "magneto_state_object", "is_compressed", "is_unregistered", "source_type", "object_type", "is_batched")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPrana: _ClassVar[MagnetoStateKafkaMessage.SourceType]
        kIris: _ClassVar[MagnetoStateKafkaMessage.SourceType]
    kPrana: MagnetoStateKafkaMessage.SourceType
    kIris: MagnetoStateKafkaMessage.SourceType
    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegisteredSource: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kLeafEntity: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kEntity: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kJob: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kProtectionJobRun: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kCopyRun: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kProtectedObject: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kProtectedObjectRun: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kRestoreTask: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kRestoreObject: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
        kPolicy: _ClassVar[MagnetoStateKafkaMessage.ObjectType]
    kRegisteredSource: MagnetoStateKafkaMessage.ObjectType
    kLeafEntity: MagnetoStateKafkaMessage.ObjectType
    kEntity: MagnetoStateKafkaMessage.ObjectType
    kJob: MagnetoStateKafkaMessage.ObjectType
    kProtectionJobRun: MagnetoStateKafkaMessage.ObjectType
    kCopyRun: MagnetoStateKafkaMessage.ObjectType
    kProtectedObject: MagnetoStateKafkaMessage.ObjectType
    kProtectedObjectRun: MagnetoStateKafkaMessage.ObjectType
    kRestoreTask: MagnetoStateKafkaMessage.ObjectType
    kRestoreObject: MagnetoStateKafkaMessage.ObjectType
    kPolicy: MagnetoStateKafkaMessage.ObjectType
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MAGNETO_STATE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    IS_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_BATCHED_FIELD_NUMBER: _ClassVar[int]
    cluster_id: bytes
    magneto_state_object: bytes
    is_compressed: bool
    is_unregistered: bool
    source_type: MagnetoStateKafkaMessage.SourceType
    object_type: MagnetoStateKafkaMessage.ObjectType
    is_batched: bool
    def __init__(self, cluster_id: _Optional[bytes] = ..., magneto_state_object: _Optional[bytes] = ..., is_compressed: bool = ..., is_unregistered: bool = ..., source_type: _Optional[_Union[MagnetoStateKafkaMessage.SourceType, str]] = ..., object_type: _Optional[_Union[MagnetoStateKafkaMessage.ObjectType, str]] = ..., is_batched: bool = ...) -> None: ...
