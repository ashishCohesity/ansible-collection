from bridge.magneto.base import magneto_actions_pb2 as _magneto_actions_pb2
from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloneBlobsArg(_message.Message):
    __slots__ = ("viewbox_id", "source_view_name", "source_blob_rel_path_vec", "dest_blob_name_vec", "crop_blob_vec", "dest_view_name", "dest_rel_dir")
    class CropBlobArg(_message.Message):
        __slots__ = ("start_offset", "end_offset")
        START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        END_OFFSET_FIELD_NUMBER: _ClassVar[int]
        start_offset: int
        end_offset: int
        def __init__(self, start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BLOB_REL_PATH_VEC_FIELD_NUMBER: _ClassVar[int]
    DEST_BLOB_NAME_VEC_FIELD_NUMBER: _ClassVar[int]
    CROP_BLOB_VEC_FIELD_NUMBER: _ClassVar[int]
    DEST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_REL_DIR_FIELD_NUMBER: _ClassVar[int]
    viewbox_id: int
    source_view_name: str
    source_blob_rel_path_vec: _containers.RepeatedScalarFieldContainer[str]
    dest_blob_name_vec: _containers.RepeatedScalarFieldContainer[str]
    crop_blob_vec: _containers.RepeatedCompositeFieldContainer[CloneBlobsArg.CropBlobArg]
    dest_view_name: str
    dest_rel_dir: str
    def __init__(self, viewbox_id: _Optional[int] = ..., source_view_name: _Optional[str] = ..., source_blob_rel_path_vec: _Optional[_Iterable[str]] = ..., dest_blob_name_vec: _Optional[_Iterable[str]] = ..., crop_blob_vec: _Optional[_Iterable[_Union[CloneBlobsArg.CropBlobArg, _Mapping]]] = ..., dest_view_name: _Optional[str] = ..., dest_rel_dir: _Optional[str] = ...) -> None: ...

class CloneBytesArg(_message.Message):
    __slots__ = ("viewbox_id", "source_view_name", "source_blob_rel_path", "source_start_offset", "size_bytes", "dest_view_name", "dest_blob_rel_path", "dest_start_offset", "volume_guid")
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BLOB_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    DEST_BLOB_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    DEST_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    viewbox_id: int
    source_view_name: str
    source_blob_rel_path: str
    source_start_offset: int
    size_bytes: int
    dest_view_name: str
    dest_blob_rel_path: str
    dest_start_offset: int
    volume_guid: str
    def __init__(self, viewbox_id: _Optional[int] = ..., source_view_name: _Optional[str] = ..., source_blob_rel_path: _Optional[str] = ..., source_start_offset: _Optional[int] = ..., size_bytes: _Optional[int] = ..., dest_view_name: _Optional[str] = ..., dest_blob_rel_path: _Optional[str] = ..., dest_start_offset: _Optional[int] = ..., volume_guid: _Optional[str] = ...) -> None: ...

class WriteMetadataArg(_message.Message):
    __slots__ = ("viewbox_id", "view_name", "fs_name", "rel_file_path", "metadata")
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    viewbox_id: int
    view_name: str
    fs_name: str
    rel_file_path: str
    metadata: bytes
    def __init__(self, viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., rel_file_path: _Optional[str] = ..., metadata: _Optional[bytes] = ...) -> None: ...

class ReadMetadataArg(_message.Message):
    __slots__ = ("viewbox_id", "view_name", "fs_name", "rel_file_path")
    VIEWBOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FS_NAME_FIELD_NUMBER: _ClassVar[int]
    REL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    viewbox_id: int
    view_name: str
    fs_name: str
    rel_file_path: str
    def __init__(self, viewbox_id: _Optional[int] = ..., view_name: _Optional[str] = ..., fs_name: _Optional[str] = ..., rel_file_path: _Optional[str] = ...) -> None: ...

class CloneVMsArg(_message.Message):
    __slots__ = ("vm_infos", "view_box_id", "dest_view_name", "separate_dir_for_each_vm")
    class VMInfo(_message.Message):
        __slots__ = ("view_name", "snapshot_relative_dir_path", "vm_entity", "previous_snapshot_relative_dir_path")
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_SNAPSHOT_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        view_name: str
        snapshot_relative_dir_path: str
        vm_entity: _entity_pb2.EntityProto
        previous_snapshot_relative_dir_path: str
        def __init__(self, view_name: _Optional[str] = ..., snapshot_relative_dir_path: _Optional[str] = ..., vm_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., previous_snapshot_relative_dir_path: _Optional[str] = ...) -> None: ...
    VM_INFOS_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    DEST_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    SEPARATE_DIR_FOR_EACH_VM_FIELD_NUMBER: _ClassVar[int]
    vm_infos: _containers.RepeatedCompositeFieldContainer[CloneVMsArg.VMInfo]
    view_box_id: int
    dest_view_name: str
    separate_dir_for_each_vm: bool
    def __init__(self, vm_infos: _Optional[_Iterable[_Union[CloneVMsArg.VMInfo, _Mapping]]] = ..., view_box_id: _Optional[int] = ..., dest_view_name: _Optional[str] = ..., separate_dir_for_each_vm: bool = ...) -> None: ...

class CreateVHDxFileArg(_message.Message):
    __slots__ = ("view_box_id", "view_name", "filepath", "filename", "volume_size_bytes", "logical_sector_size_bytes")
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_SECTOR_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    view_box_id: int
    view_name: str
    filepath: str
    filename: str
    volume_size_bytes: int
    logical_sector_size_bytes: int
    def __init__(self, view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., filepath: _Optional[str] = ..., filename: _Optional[str] = ..., volume_size_bytes: _Optional[int] = ..., logical_sector_size_bytes: _Optional[int] = ...) -> None: ...

class CloudActionArg(_message.Message):
    __slots__ = ("task_id", "sub_task_id", "clone_blobs_arg", "clone_bytes_arg", "cancel_task_arg", "write_metadata_arg", "read_metadata_arg", "clone_vms_arg", "create_vhdx_file_arg")
    CLOUD_ACTION_ARG_FIELD_NUMBER: _ClassVar[int]
    cloud_action_arg: _descriptor.FieldDescriptor
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CLONE_BLOBS_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_BYTES_ARG_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TASK_ARG_FIELD_NUMBER: _ClassVar[int]
    WRITE_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    READ_METADATA_ARG_FIELD_NUMBER: _ClassVar[int]
    CLONE_VMS_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_VHDX_FILE_ARG_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    sub_task_id: int
    clone_blobs_arg: CloneBlobsArg
    clone_bytes_arg: CloneBytesArg
    cancel_task_arg: _magneto_actions_pb2.CancelTaskArg
    write_metadata_arg: WriteMetadataArg
    read_metadata_arg: ReadMetadataArg
    clone_vms_arg: CloneVMsArg
    create_vhdx_file_arg: CreateVHDxFileArg
    def __init__(self, task_id: _Optional[int] = ..., sub_task_id: _Optional[int] = ..., clone_blobs_arg: _Optional[_Union[CloneBlobsArg, _Mapping]] = ..., clone_bytes_arg: _Optional[_Union[CloneBytesArg, _Mapping]] = ..., cancel_task_arg: _Optional[_Union[_magneto_actions_pb2.CancelTaskArg, _Mapping]] = ..., write_metadata_arg: _Optional[_Union[WriteMetadataArg, _Mapping]] = ..., read_metadata_arg: _Optional[_Union[ReadMetadataArg, _Mapping]] = ..., clone_vms_arg: _Optional[_Union[CloneVMsArg, _Mapping]] = ..., create_vhdx_file_arg: _Optional[_Union[CreateVHDxFileArg, _Mapping]] = ...) -> None: ...
