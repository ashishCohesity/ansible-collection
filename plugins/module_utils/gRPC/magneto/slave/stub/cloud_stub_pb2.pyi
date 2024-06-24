from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloneVMsUpdateArg(_message.Message):
    __slots__ = ("cloned_vms",)
    class ClonedVM(_message.Message):
        __slots__ = ("vm_entity", "relative_cloned_paths", "relative_dir_path", "previous_relative_cloned_paths", "previous_relative_dir_path")
        VM_ENTITY_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_CLONED_PATHS_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_RELATIVE_CLONED_PATHS_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_RELATIVE_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
        vm_entity: _entity_pb2.EntityProto
        relative_cloned_paths: _containers.RepeatedScalarFieldContainer[str]
        relative_dir_path: str
        previous_relative_cloned_paths: _containers.RepeatedScalarFieldContainer[str]
        previous_relative_dir_path: str
        def __init__(self, vm_entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., relative_cloned_paths: _Optional[_Iterable[str]] = ..., relative_dir_path: _Optional[str] = ..., previous_relative_cloned_paths: _Optional[_Iterable[str]] = ..., previous_relative_dir_path: _Optional[str] = ...) -> None: ...
    CLONED_VMS_FIELD_NUMBER: _ClassVar[int]
    cloned_vms: _containers.RepeatedCompositeFieldContainer[CloneVMsUpdateArg.ClonedVM]
    def __init__(self, cloned_vms: _Optional[_Iterable[_Union[CloneVMsUpdateArg.ClonedVM, _Mapping]]] = ...) -> None: ...

class CreateVHDxFileUpdateArg(_message.Message):
    __slots__ = ("disk_area_start_offset",)
    DISK_AREA_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    disk_area_start_offset: int
    def __init__(self, disk_area_start_offset: _Optional[int] = ...) -> None: ...

class CloudActionUpdateArg(_message.Message):
    __slots__ = ("type", "backed_up_vhd_file_rel_path", "volume_guid", "metadata", "clone_vms_update_arg", "create_vhdx_file_update_arg")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kCloneBlobs: _ClassVar[CloudActionUpdateArg.Type]
        kCloneBytes: _ClassVar[CloudActionUpdateArg.Type]
        kWriteMetadata: _ClassVar[CloudActionUpdateArg.Type]
        kReadMetadata: _ClassVar[CloudActionUpdateArg.Type]
        kCloneVMsUpdate: _ClassVar[CloudActionUpdateArg.Type]
        kCreateVHDxFileUpdate: _ClassVar[CloudActionUpdateArg.Type]
    kCloneBlobs: CloudActionUpdateArg.Type
    kCloneBytes: CloudActionUpdateArg.Type
    kWriteMetadata: CloudActionUpdateArg.Type
    kReadMetadata: CloudActionUpdateArg.Type
    kCloneVMsUpdate: CloudActionUpdateArg.Type
    kCreateVHDxFileUpdate: CloudActionUpdateArg.Type
    CLOUD_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    cloud_action_update_arg: _descriptor.FieldDescriptor
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKED_UP_VHD_FILE_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_GUID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CLONE_VMS_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    CREATE_VHDX_FILE_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    type: CloudActionUpdateArg.Type
    backed_up_vhd_file_rel_path: str
    volume_guid: str
    metadata: bytes
    clone_vms_update_arg: CloneVMsUpdateArg
    create_vhdx_file_update_arg: CreateVHDxFileUpdateArg
    def __init__(self, type: _Optional[_Union[CloudActionUpdateArg.Type, str]] = ..., backed_up_vhd_file_rel_path: _Optional[str] = ..., volume_guid: _Optional[str] = ..., metadata: _Optional[bytes] = ..., clone_vms_update_arg: _Optional[_Union[CloneVMsUpdateArg, _Mapping]] = ..., create_vhdx_file_update_arg: _Optional[_Union[CreateVHDxFileUpdateArg, _Mapping]] = ...) -> None: ...
