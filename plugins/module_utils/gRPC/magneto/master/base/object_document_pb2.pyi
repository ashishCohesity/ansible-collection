from magneto.base import enums_pb2 as _enums_pb2
from magneto.base import policy_pb2 as _policy_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityDoc(_message.Message):
    __slots__ = ("id", "name", "type", "is_deleted", "total_logical_size_bytes", "num_total_leaf_entities", "num_protected_leaf_entities", "last_refresh_time_usecs", "parent_entity_id", "parent_entity_name", "owner_entity_id", "owner_entity_name", "job_info_vec", "snapshot_info_vec", "view_details")
    class JobInfo(_message.Message):
        __slots__ = ("uid", "name")
        UID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        uid: _universal_id_pb2.UniversalIdProto
        name: str
        def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
    class SnapshotInfo(_message.Message):
        __slots__ = ("snapshot_target", "num_snapshots", "last_snapshot_time_usecs")
        SNAPSHOT_TARGET_FIELD_NUMBER: _ClassVar[int]
        NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        LAST_SNAPSHOT_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        snapshot_target: _policy_pb2.SnapshotTarget
        num_snapshots: int
        last_snapshot_time_usecs: int
        def __init__(self, snapshot_target: _Optional[_Union[_policy_pb2.SnapshotTarget, _Mapping]] = ..., num_snapshots: _Optional[int] = ..., last_snapshot_time_usecs: _Optional[int] = ...) -> None: ...
    class ViewDetails(_message.Message):
        __slots__ = ("view_id", "view_box_id", "create_time_usecs", "description")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        view_box_id: int
        create_time_usecs: int
        description: str
        def __init__(self, view_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., create_time_usecs: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_LEAF_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    NUM_PROTECTED_LEAF_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_VEC_FIELD_NUMBER: _ClassVar[int]
    VIEW_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: _enums_pb2.Environment.Type
    is_deleted: bool
    total_logical_size_bytes: int
    num_total_leaf_entities: int
    num_protected_leaf_entities: int
    last_refresh_time_usecs: int
    parent_entity_id: int
    parent_entity_name: str
    owner_entity_id: int
    owner_entity_name: str
    job_info_vec: _containers.RepeatedCompositeFieldContainer[EntityDoc.JobInfo]
    snapshot_info_vec: _containers.RepeatedCompositeFieldContainer[EntityDoc.SnapshotInfo]
    view_details: EntityDoc.ViewDetails
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.Environment.Type, str]] = ..., is_deleted: bool = ..., total_logical_size_bytes: _Optional[int] = ..., num_total_leaf_entities: _Optional[int] = ..., num_protected_leaf_entities: _Optional[int] = ..., last_refresh_time_usecs: _Optional[int] = ..., parent_entity_id: _Optional[int] = ..., parent_entity_name: _Optional[str] = ..., owner_entity_id: _Optional[int] = ..., owner_entity_name: _Optional[str] = ..., job_info_vec: _Optional[_Iterable[_Union[EntityDoc.JobInfo, _Mapping]]] = ..., snapshot_info_vec: _Optional[_Iterable[_Union[EntityDoc.SnapshotInfo, _Mapping]]] = ..., view_details: _Optional[_Union[EntityDoc.ViewDetails, _Mapping]] = ...) -> None: ...
