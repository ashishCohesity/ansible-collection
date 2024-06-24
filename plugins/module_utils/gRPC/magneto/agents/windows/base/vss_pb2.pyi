from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.agents.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VSSBackupType(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUndefined: _ClassVar[VSSBackupType.Type]
        kFull: _ClassVar[VSSBackupType.Type]
        kIncremental: _ClassVar[VSSBackupType.Type]
        kDifferential: _ClassVar[VSSBackupType.Type]
        kLog: _ClassVar[VSSBackupType.Type]
        kCopy: _ClassVar[VSSBackupType.Type]
    kUndefined: VSSBackupType.Type
    kFull: VSSBackupType.Type
    kIncremental: VSSBackupType.Type
    kDifferential: VSSBackupType.Type
    kLog: VSSBackupType.Type
    kCopy: VSSBackupType.Type
    def __init__(self) -> None: ...

class WriterDescription(_message.Message):
    __slots__ = ("writer_class_id", "name", "utf8_name", "instance_id", "state", "component_description_vec")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[WriterDescription.State]
        kStable: _ClassVar[WriterDescription.State]
        kWaitingForFreeze: _ClassVar[WriterDescription.State]
        kWaitingForThaw: _ClassVar[WriterDescription.State]
        kWaitingForPostSnapshot: _ClassVar[WriterDescription.State]
        kWaitingForBackupComplete: _ClassVar[WriterDescription.State]
        kFailedAtIdentify: _ClassVar[WriterDescription.State]
        kFailedAtPrepareBackup: _ClassVar[WriterDescription.State]
        kFailedAtPrepareSnapshot: _ClassVar[WriterDescription.State]
        kFailedAtFreeze: _ClassVar[WriterDescription.State]
        kFailedAtThaw: _ClassVar[WriterDescription.State]
        kFailedAtPostSnapshot: _ClassVar[WriterDescription.State]
        kFailedAtBackupComplete: _ClassVar[WriterDescription.State]
        kFailedAtPreRestore: _ClassVar[WriterDescription.State]
        kFailedAtPostRestore: _ClassVar[WriterDescription.State]
        kFailedAtBackupShutdown: _ClassVar[WriterDescription.State]
    kUnknown: WriterDescription.State
    kStable: WriterDescription.State
    kWaitingForFreeze: WriterDescription.State
    kWaitingForThaw: WriterDescription.State
    kWaitingForPostSnapshot: WriterDescription.State
    kWaitingForBackupComplete: WriterDescription.State
    kFailedAtIdentify: WriterDescription.State
    kFailedAtPrepareBackup: WriterDescription.State
    kFailedAtPrepareSnapshot: WriterDescription.State
    kFailedAtFreeze: WriterDescription.State
    kFailedAtThaw: WriterDescription.State
    kFailedAtPostSnapshot: WriterDescription.State
    kFailedAtBackupComplete: WriterDescription.State
    kFailedAtPreRestore: WriterDescription.State
    kFailedAtPostRestore: WriterDescription.State
    kFailedAtBackupShutdown: WriterDescription.State
    class ComponentDescription(_message.Message):
        __slots__ = ("component_logical_path", "component_name", "selectable_for_backup", "selectable_for_restore", "file_description_vec")
        class FileDescription(_message.Message):
            __slots__ = ("file_spec", "path", "alternate_backup_location", "backup_type_mask", "recursive")
            FILE_SPEC_FIELD_NUMBER: _ClassVar[int]
            PATH_FIELD_NUMBER: _ClassVar[int]
            ALTERNATE_BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
            BACKUP_TYPE_MASK_FIELD_NUMBER: _ClassVar[int]
            RECURSIVE_FIELD_NUMBER: _ClassVar[int]
            file_spec: bytes
            path: bytes
            alternate_backup_location: bytes
            backup_type_mask: int
            recursive: bool
            def __init__(self, file_spec: _Optional[bytes] = ..., path: _Optional[bytes] = ..., alternate_backup_location: _Optional[bytes] = ..., backup_type_mask: _Optional[int] = ..., recursive: bool = ...) -> None: ...
        COMPONENT_LOGICAL_PATH_FIELD_NUMBER: _ClassVar[int]
        COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
        SELECTABLE_FOR_BACKUP_FIELD_NUMBER: _ClassVar[int]
        SELECTABLE_FOR_RESTORE_FIELD_NUMBER: _ClassVar[int]
        FILE_DESCRIPTION_VEC_FIELD_NUMBER: _ClassVar[int]
        component_logical_path: bytes
        component_name: bytes
        selectable_for_backup: bool
        selectable_for_restore: bool
        file_description_vec: _containers.RepeatedCompositeFieldContainer[WriterDescription.ComponentDescription.FileDescription]
        def __init__(self, component_logical_path: _Optional[bytes] = ..., component_name: _Optional[bytes] = ..., selectable_for_backup: bool = ..., selectable_for_restore: bool = ..., file_description_vec: _Optional[_Iterable[_Union[WriterDescription.ComponentDescription.FileDescription, _Mapping]]] = ...) -> None: ...
    WRITER_CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UTF8_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_DESCRIPTION_VEC_FIELD_NUMBER: _ClassVar[int]
    writer_class_id: bytes
    name: bytes
    utf8_name: str
    instance_id: bytes
    state: WriterDescription.State
    component_description_vec: _containers.RepeatedCompositeFieldContainer[WriterDescription.ComponentDescription]
    def __init__(self, writer_class_id: _Optional[bytes] = ..., name: _Optional[bytes] = ..., utf8_name: _Optional[str] = ..., instance_id: _Optional[bytes] = ..., state: _Optional[_Union[WriterDescription.State, str]] = ..., component_description_vec: _Optional[_Iterable[_Union[WriterDescription.ComponentDescription, _Mapping]]] = ...) -> None: ...

class VSSWriterMetadataProto(_message.Message):
    __slots__ = ("writer_description_vec",)
    VSS_WRITER_METADATA_FIELD_NUMBER: _ClassVar[int]
    vss_writer_metadata: _descriptor.FieldDescriptor
    VSS_WRITER_METADATA_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    vss_writer_metadata_summary: _descriptor.FieldDescriptor
    WRITER_DESCRIPTION_VEC_FIELD_NUMBER: _ClassVar[int]
    writer_description_vec: _containers.RepeatedCompositeFieldContainer[WriterDescription]
    def __init__(self, writer_description_vec: _Optional[_Iterable[_Union[WriterDescription, _Mapping]]] = ...) -> None: ...

class VSSSnapshotMetadataProto(_message.Message):
    __slots__ = ("original_volume_name", "original_mount_point_vec")
    VSS_SNAPSHOT_METADATA_FIELD_NUMBER: _ClassVar[int]
    vss_snapshot_metadata: _descriptor.FieldDescriptor
    ORIGINAL_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MOUNT_POINT_VEC_FIELD_NUMBER: _ClassVar[int]
    original_volume_name: bytes
    original_mount_point_vec: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, original_volume_name: _Optional[bytes] = ..., original_mount_point_vec: _Optional[_Iterable[bytes]] = ...) -> None: ...

class VSSSnapshotSetMetadataProto(_message.Message):
    __slots__ = ("compressed_vss_snapshot_set_metadata_proto", "backup_components_xml", "writer_metadata_xml_vec", "writer_description_vec", "writer_to_error_map", "contains_shadow_copy")
    Extensions: _python_message._ExtensionDict
    class FileData(_message.Message):
        __slots__ = ("file_name", "data", "compressed")
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        COMPRESSED_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        data: bytes
        compressed: bool
        def __init__(self, file_name: _Optional[str] = ..., data: _Optional[bytes] = ..., compressed: bool = ...) -> None: ...
    class WriterToErrorMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorProto
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
    VSS_SNAPSHOT_SET_METADATA_FIELD_NUMBER: _ClassVar[int]
    vss_snapshot_set_metadata: _descriptor.FieldDescriptor
    COMPRESSED_VSS_SNAPSHOT_SET_METADATA_PROTO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_COMPONENTS_XML_FIELD_NUMBER: _ClassVar[int]
    WRITER_METADATA_XML_VEC_FIELD_NUMBER: _ClassVar[int]
    WRITER_DESCRIPTION_VEC_FIELD_NUMBER: _ClassVar[int]
    WRITER_TO_ERROR_MAP_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_SHADOW_COPY_FIELD_NUMBER: _ClassVar[int]
    compressed_vss_snapshot_set_metadata_proto: bytes
    backup_components_xml: VSSSnapshotSetMetadataProto.FileData
    writer_metadata_xml_vec: _containers.RepeatedCompositeFieldContainer[VSSSnapshotSetMetadataProto.FileData]
    writer_description_vec: _containers.RepeatedCompositeFieldContainer[WriterDescription]
    writer_to_error_map: _containers.MessageMap[str, _error_pb2.ErrorProto]
    contains_shadow_copy: bool
    def __init__(self, compressed_vss_snapshot_set_metadata_proto: _Optional[bytes] = ..., backup_components_xml: _Optional[_Union[VSSSnapshotSetMetadataProto.FileData, _Mapping]] = ..., writer_metadata_xml_vec: _Optional[_Iterable[_Union[VSSSnapshotSetMetadataProto.FileData, _Mapping]]] = ..., writer_description_vec: _Optional[_Iterable[_Union[WriterDescription, _Mapping]]] = ..., writer_to_error_map: _Optional[_Mapping[str, _error_pb2.ErrorProto]] = ..., contains_shadow_copy: bool = ...) -> None: ...

class VSSProviderPropertiesProto(_message.Message):
    __slots__ = ("provider_id", "provider_name", "provider_type", "provider_version", "provider_version_id")
    class ProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kUnknown: _ClassVar[VSSProviderPropertiesProto.ProviderType]
        kSystem: _ClassVar[VSSProviderPropertiesProto.ProviderType]
        kSoftware: _ClassVar[VSSProviderPropertiesProto.ProviderType]
        kHardware: _ClassVar[VSSProviderPropertiesProto.ProviderType]
        kFileshare: _ClassVar[VSSProviderPropertiesProto.ProviderType]
    kUnknown: VSSProviderPropertiesProto.ProviderType
    kSystem: VSSProviderPropertiesProto.ProviderType
    kSoftware: VSSProviderPropertiesProto.ProviderType
    kHardware: VSSProviderPropertiesProto.ProviderType
    kFileshare: VSSProviderPropertiesProto.ProviderType
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    provider_id: bytes
    provider_name: bytes
    provider_type: VSSProviderPropertiesProto.ProviderType
    provider_version: bytes
    provider_version_id: bytes
    def __init__(self, provider_id: _Optional[bytes] = ..., provider_name: _Optional[bytes] = ..., provider_type: _Optional[_Union[VSSProviderPropertiesProto.ProviderType, str]] = ..., provider_version: _Optional[bytes] = ..., provider_version_id: _Optional[bytes] = ...) -> None: ...

class VSSFileCopyInstruction(_message.Message):
    __slots__ = ("source_file_pattern", "destination_dir_path")
    Extensions: _python_message._ExtensionDict
    SOURCE_FILE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DIR_PATH_FIELD_NUMBER: _ClassVar[int]
    source_file_pattern: str
    destination_dir_path: str
    def __init__(self, source_file_pattern: _Optional[str] = ..., destination_dir_path: _Optional[str] = ...) -> None: ...

class VSSComponentActionResult(_message.Message):
    __slots__ = ("error", "skipped", "skipped_reason")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_REASON_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    skipped: bool
    skipped_reason: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., skipped: bool = ..., skipped_reason: _Optional[str] = ...) -> None: ...

class VSSWriterActionResult(_message.Message):
    __slots__ = ("component_to_result_map", "error", "user_message")
    class ComponentToResultMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: VSSComponentActionResult
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[VSSComponentActionResult, _Mapping]] = ...) -> None: ...
    COMPONENT_TO_RESULT_MAP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    component_to_result_map: _containers.MessageMap[str, VSSComponentActionResult]
    error: _error_pb2.ErrorProto
    user_message: str
    def __init__(self, component_to_result_map: _Optional[_Mapping[str, VSSComponentActionResult]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., user_message: _Optional[str] = ...) -> None: ...

class VSSWriterComponentInfo(_message.Message):
    __slots__ = ("writer_name_to_result_map",)
    class WriterNameToResultMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: VSSWriterActionResult
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[VSSWriterActionResult, _Mapping]] = ...) -> None: ...
    WRITER_NAME_TO_RESULT_MAP_FIELD_NUMBER: _ClassVar[int]
    writer_name_to_result_map: _containers.MessageMap[str, VSSWriterActionResult]
    def __init__(self, writer_name_to_result_map: _Optional[_Mapping[str, VSSWriterActionResult]] = ...) -> None: ...
