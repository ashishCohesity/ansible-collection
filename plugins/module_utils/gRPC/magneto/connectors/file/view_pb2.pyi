from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from magneto.connectors.file import file_pb2 as _file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreEnvironmentInfo(_message.Message):
    __slots__ = ("should_clone_file", "src_view_metadata", "dst_view_metadata", "dst_view_box_name")
    RESTORE_ENV_INFO_FIELD_NUMBER: _ClassVar[int]
    restore_env_info: _descriptor.FieldDescriptor
    SHOULD_CLONE_FILE_FIELD_NUMBER: _ClassVar[int]
    SRC_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    DST_VIEW_METADATA_FIELD_NUMBER: _ClassVar[int]
    DST_VIEW_BOX_NAME_FIELD_NUMBER: _ClassVar[int]
    should_clone_file: bool
    src_view_metadata: _view_metadata_pb2.ViewIdMappingProto
    dst_view_metadata: _view_metadata_pb2.ViewIdMappingProto
    dst_view_box_name: str
    def __init__(self, should_clone_file: bool = ..., src_view_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ..., dst_view_metadata: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ..., dst_view_box_name: _Optional[str] = ...) -> None: ...
