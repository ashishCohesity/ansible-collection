from apollo.mr.base import utils_pb2 as _utils_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleIceboxDirectArchivePipelineArg(_message.Message):
    __slots__ = ("job_uid", "cluster_id", "viewbox_id", "view_name", "fs_name", "expired_snap_tree_object_path_vec", "live_snap_tree_object_path_vec", "max_snap_tree_height", "output_view_name", "output_fs_name", "output_directory_path", "expired_archive_uid_vec", "live_archive_uid_vec", "version", "vault_id")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_SNAP_TREE_OBJECT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    LIVE_SNAP_TREE_OBJECT_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    MAX_SNAP_TREE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FS_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    LIVE_ARCHIVE_UID_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    job_uid: _utils_pb2.ObjectUidProto
    cluster_id: int
    viewbox_id: int
    view_name: str
    fs_name: str
    expired_snap_tree_object_path_vec: _containers.RepeatedScalarFieldContainer[str]
    live_snap_tree_object_path_vec: _containers.RepeatedScalarFieldContainer[str]
    max_snap_tree_height: int
    output_view_name: str
    output_fs_name: str
    output_directory_path: str
    expired_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    live_archive_uid_vec: _containers.RepeatedCompositeFieldContainer[_universal_id_pb2.UniversalIdProto]
    version: int
    vault_id: int
    def __init__(self, job_uid: _Optional[_Union[_utils_pb2.ObjectUidProto, _Mapping]] = ..., cluster_id: _Optional[int] = ..., viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., expired_snap_tree_object_path_vec: _Optional[_Iterable[str]] = ..., live_snap_tree_object_path_vec: _Optional[_Iterable[str]] = ..., max_snap_tree_height: _Optional[int] = ..., output_view_name: _Optional[str] = ..., output_fs_name: _Optional[str] = ..., output_directory_path: _Optional[str] = ..., expired_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., live_archive_uid_vec: _Optional[_Iterable[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]]] = ..., version: _Optional[int] = ..., vault_id: _Optional[int] = ...) -> None: ...

class ScheduleIceboxCloudDomainMigrationPipelineArg(_message.Message):
    __slots__ = ("job_uid", "cloud_domain_id", "wait_for_ccfm_population")
    JOB_UID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_CCFM_POPULATION_FIELD_NUMBER: _ClassVar[int]
    job_uid: _utils_pb2.ObjectUidProto
    cloud_domain_id: int
    wait_for_ccfm_population: bool
    def __init__(self, job_uid: _Optional[_Union[_utils_pb2.ObjectUidProto, _Mapping]] = ..., cloud_domain_id: _Optional[int] = ..., wait_for_ccfm_population: bool = ...) -> None: ...
