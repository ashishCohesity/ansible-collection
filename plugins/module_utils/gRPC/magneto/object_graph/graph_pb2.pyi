from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.object_graph import backup_pb2 as _backup_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttributeNamesProto(_message.Message):
    __slots__ = ("name", "ctime", "mtime", "operation", "operation_status", "expiration_time", "user_label", "is_hidden")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    ctime: str
    mtime: str
    operation: str
    operation_status: str
    expiration_time: str
    user_label: str
    is_hidden: str
    def __init__(self, name: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., operation: _Optional[str] = ..., operation_status: _Optional[str] = ..., expiration_time: _Optional[str] = ..., user_label: _Optional[str] = ..., is_hidden: _Optional[str] = ...) -> None: ...

class NodeAttributeNamesProto(_message.Message):
    __slots__ = ("physical_storage_consumed", "created_by_user", "is_active")
    PHYSICAL_STORAGE_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    physical_storage_consumed: str
    created_by_user: str
    is_active: str
    def __init__(self, physical_storage_consumed: _Optional[str] = ..., created_by_user: _Optional[str] = ..., is_active: _Optional[str] = ...) -> None: ...

class EntityNodeAttributeNamesProto(_message.Message):
    __slots__ = ("host_uid", "entity_hierarchy_uid", "display_name", "host_environment", "ip_addr_str", "logical_size", "incarnation", "permissions")
    HOST_UID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HIERARCHY_UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HOST_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDR_STR_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    INCARNATION_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    host_uid: str
    entity_hierarchy_uid: str
    display_name: str
    host_environment: str
    ip_addr_str: str
    logical_size: str
    incarnation: str
    permissions: str
    def __init__(self, host_uid: _Optional[str] = ..., entity_hierarchy_uid: _Optional[str] = ..., display_name: _Optional[str] = ..., host_environment: _Optional[str] = ..., ip_addr_str: _Optional[str] = ..., logical_size: _Optional[str] = ..., incarnation: _Optional[str] = ..., permissions: _Optional[str] = ...) -> None: ...

class SnapshotNodeAttributeNamesProto(_message.Message):
    __slots__ = ("magneto_snapshot_locater", "snapshot_info")
    MAGNETO_SNAPSHOT_LOCATER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    magneto_snapshot_locater: str
    snapshot_info: str
    def __init__(self, magneto_snapshot_locater: _Optional[str] = ..., snapshot_info: _Optional[str] = ...) -> None: ...

class DataNodeAttributeNamesProto(_message.Message):
    __slots__ = ("storage_domain_id", "view_id", "view_name", "namespace_root_name", "snapshot_dir_relative_path", "view_policy")
    STORAGE_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ROOT_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIR_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    VIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    storage_domain_id: str
    view_id: str
    view_name: str
    namespace_root_name: str
    snapshot_dir_relative_path: str
    view_policy: str
    def __init__(self, storage_domain_id: _Optional[str] = ..., view_id: _Optional[str] = ..., view_name: _Optional[str] = ..., namespace_root_name: _Optional[str] = ..., snapshot_dir_relative_path: _Optional[str] = ..., view_policy: _Optional[str] = ...) -> None: ...

class TaskNodeAttributeNamesProto(_message.Message):
    __slots__ = ("magneto_task_id", "protection_task_state", "user_description", "start_time_usecs", "end_time_usecs", "error_detail", "pulse_path")
    MAGNETO_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PROTECTION_TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    USER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    PULSE_PATH_FIELD_NUMBER: _ClassVar[int]
    magneto_task_id: str
    protection_task_state: str
    user_description: str
    start_time_usecs: str
    end_time_usecs: str
    error_detail: str
    pulse_path: str
    def __init__(self, magneto_task_id: _Optional[str] = ..., protection_task_state: _Optional[str] = ..., user_description: _Optional[str] = ..., start_time_usecs: _Optional[str] = ..., end_time_usecs: _Optional[str] = ..., error_detail: _Optional[str] = ..., pulse_path: _Optional[str] = ...) -> None: ...

class PolicyAttributeNamesProto(_message.Message):
    __slots__ = ("mangeto_policy_id",)
    MANGETO_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    mangeto_policy_id: str
    def __init__(self, mangeto_policy_id: _Optional[str] = ...) -> None: ...

class JobNodeAttributeNamesProto(_message.Message):
    __slots__ = ("view_params", "pre_script", "post_scipt", "run_once")
    VIEW_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_SCIPT_FIELD_NUMBER: _ClassVar[int]
    RUN_ONCE_FIELD_NUMBER: _ClassVar[int]
    view_params: str
    pre_script: str
    post_scipt: str
    run_once: str
    def __init__(self, view_params: _Optional[str] = ..., pre_script: _Optional[str] = ..., post_scipt: _Optional[str] = ..., run_once: _Optional[str] = ...) -> None: ...

class EdgeAttributeNamesProto(_message.Message):
    __slots__ = ("task_uid", "operation_error", "clone_entity_incarnation")
    TASK_UID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    CLONE_ENTITY_INCARNATION_FIELD_NUMBER: _ClassVar[int]
    task_uid: str
    operation_error: str
    clone_entity_incarnation: str
    def __init__(self, task_uid: _Optional[str] = ..., operation_error: _Optional[str] = ..., clone_entity_incarnation: _Optional[str] = ...) -> None: ...

class LabelProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[LabelProto.Type]
        kClone: _ClassVar[LabelProto.Type]
        kProtected: _ClassVar[LabelProto.Type]
    kUnused: LabelProto.Type
    kClone: LabelProto.Type
    kProtected: LabelProto.Type
    def __init__(self) -> None: ...

class NodeBaseProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[NodeBaseProto.Type]
        kEntity: _ClassVar[NodeBaseProto.Type]
        kSnapshot: _ClassVar[NodeBaseProto.Type]
        kPolicy: _ClassVar[NodeBaseProto.Type]
        kData: _ClassVar[NodeBaseProto.Type]
        kJob: _ClassVar[NodeBaseProto.Type]
        kTask: _ClassVar[NodeBaseProto.Type]
    kUnused: NodeBaseProto.Type
    kEntity: NodeBaseProto.Type
    kSnapshot: NodeBaseProto.Type
    kPolicy: NodeBaseProto.Type
    kData: NodeBaseProto.Type
    kJob: NodeBaseProto.Type
    kTask: NodeBaseProto.Type
    def __init__(self) -> None: ...

class EntityBaseProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[EntityBaseProto.Type]
        kPhysicalHost: _ClassVar[EntityBaseProto.Type]
        kDatabaseServer: _ClassVar[EntityBaseProto.Type]
        kDatabase: _ClassVar[EntityBaseProto.Type]
    kUnused: EntityBaseProto.Type
    kPhysicalHost: EntityBaseProto.Type
    kDatabaseServer: EntityBaseProto.Type
    kDatabase: EntityBaseProto.Type
    def __init__(self) -> None: ...

class EdgeBaseProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[EdgeBaseProto.Type]
        kSelf: _ClassVar[EdgeBaseProto.Type]
        kChildOf: _ClassVar[EdgeBaseProto.Type]
        kParentOf: _ClassVar[EdgeBaseProto.Type]
        kSnapshot: _ClassVar[EdgeBaseProto.Type]
        kData: _ClassVar[EdgeBaseProto.Type]
        kClone: _ClassVar[EdgeBaseProto.Type]
        kJob: _ClassVar[EdgeBaseProto.Type]
        kPolicy: _ClassVar[EdgeBaseProto.Type]
        kTask: _ClassVar[EdgeBaseProto.Type]
        kBookMark: _ClassVar[EdgeBaseProto.Type]
    kUnused: EdgeBaseProto.Type
    kSelf: EdgeBaseProto.Type
    kChildOf: EdgeBaseProto.Type
    kParentOf: EdgeBaseProto.Type
    kSnapshot: EdgeBaseProto.Type
    kData: EdgeBaseProto.Type
    kClone: EdgeBaseProto.Type
    kJob: EdgeBaseProto.Type
    kPolicy: EdgeBaseProto.Type
    kTask: EdgeBaseProto.Type
    kBookMark: EdgeBaseProto.Type
    def __init__(self) -> None: ...

class OperationStatusProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[OperationStatusProto.Type]
        kScheduled: _ClassVar[OperationStatusProto.Type]
        kInProgress: _ClassVar[OperationStatusProto.Type]
        kFinished: _ClassVar[OperationStatusProto.Type]
        kCancelled: _ClassVar[OperationStatusProto.Type]
    kUnused: OperationStatusProto.Type
    kScheduled: OperationStatusProto.Type
    kInProgress: OperationStatusProto.Type
    kFinished: OperationStatusProto.Type
    kCancelled: OperationStatusProto.Type
    def __init__(self) -> None: ...

class MagnetoSnapshotLocaterProto(_message.Message):
    __slots__ = ("source_entity_hierarchy_uid", "job_uid", "job_instance_id", "run_start_time_usecs", "app_entity_hierarchy_uid")
    SOURCE_ENTITY_HIERARCHY_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    JOB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
    APP_ENTITY_HIERARCHY_UID_FIELD_NUMBER: _ClassVar[int]
    source_entity_hierarchy_uid: _universal_id_pb2.UniversalIdProto
    job_uid: _universal_id_pb2.UniversalIdProto
    job_instance_id: int
    run_start_time_usecs: int
    app_entity_hierarchy_uid: _universal_id_pb2.UniversalIdProto
    def __init__(self, source_entity_hierarchy_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., job_instance_id: _Optional[int] = ..., run_start_time_usecs: _Optional[int] = ..., app_entity_hierarchy_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ...) -> None: ...

class ProtectionTaskStateProto(_message.Message):
    __slots__ = ("snapshot_of_clone_vec",)
    SNAPSHOT_OF_CLONE_VEC_FIELD_NUMBER: _ClassVar[int]
    snapshot_of_clone_vec: _containers.RepeatedCompositeFieldContainer[_backup_pb2.EntityBackupTaskStateProto]
    def __init__(self, snapshot_of_clone_vec: _Optional[_Iterable[_Union[_backup_pb2.EntityBackupTaskStateProto, _Mapping]]] = ...) -> None: ...

class PolicyNodeProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JobNodeProto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DataNodeViewPolicyProto(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnused: _ClassVar[DataNodeViewPolicyProto.Type]
        kViewPerClone: _ClassVar[DataNodeViewPolicyProto.Type]
        kViewPerStorageDomainPerHost: _ClassVar[DataNodeViewPolicyProto.Type]
    kUnused: DataNodeViewPolicyProto.Type
    kViewPerClone: DataNodeViewPolicyProto.Type
    kViewPerStorageDomainPerHost: DataNodeViewPolicyProto.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: DataNodeViewPolicyProto.Type
    def __init__(self, type: _Optional[_Union[DataNodeViewPolicyProto.Type, str]] = ...) -> None: ...
