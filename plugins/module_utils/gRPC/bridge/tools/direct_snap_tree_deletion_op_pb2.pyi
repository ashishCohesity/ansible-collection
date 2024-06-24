from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeletionEntities(_message.Message):
    __slots__ = ("root_snap_tree_id", "snaptree_key_vec")
    ROOT_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPTREE_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    root_snap_tree_id: int
    snaptree_key_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, root_snap_tree_id: _Optional[int] = ..., snaptree_key_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class CheckpointInfoProto(_message.Message):
    __slots__ = ("last_visited_entity", "deletion_status", "next_offset_in_deletion_file")
    class DeletionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kPhase1InProgress: _ClassVar[CheckpointInfoProto.DeletionStatus]
        kPhase2InProgress: _ClassVar[CheckpointInfoProto.DeletionStatus]
        kCleanupInProgress: _ClassVar[CheckpointInfoProto.DeletionStatus]
    kPhase1InProgress: CheckpointInfoProto.DeletionStatus
    kPhase2InProgress: CheckpointInfoProto.DeletionStatus
    kCleanupInProgress: CheckpointInfoProto.DeletionStatus
    LAST_VISITED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DELETION_STATUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_IN_DELETION_FILE_FIELD_NUMBER: _ClassVar[int]
    last_visited_entity: _directory_walker_pb2.EntityMetadata
    deletion_status: CheckpointInfoProto.DeletionStatus
    next_offset_in_deletion_file: int
    def __init__(self, last_visited_entity: _Optional[_Union[_directory_walker_pb2.EntityMetadata, _Mapping]] = ..., deletion_status: _Optional[_Union[CheckpointInfoProto.DeletionStatus, str]] = ..., next_offset_in_deletion_file: _Optional[int] = ...) -> None: ...
