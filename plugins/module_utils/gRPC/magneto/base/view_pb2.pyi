from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotInfo(_message.Message):
    __slots__ = ("source_inode_id_floor", "cloned_view_id", "cloned_view_logical_size_bytes", "source_view_id_mapping")
    VIEW_SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    view_snapshot_info: _descriptor.FieldDescriptor
    SOURCE_INODE_ID_FLOOR_FIELD_NUMBER: _ClassVar[int]
    CLONED_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    CLONED_VIEW_LOGICAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIEW_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    source_inode_id_floor: int
    cloned_view_id: int
    cloned_view_logical_size_bytes: int
    source_view_id_mapping: _view_metadata_pb2.ViewIdMappingProto
    def __init__(self, source_inode_id_floor: _Optional[int] = ..., cloned_view_id: _Optional[int] = ..., cloned_view_logical_size_bytes: _Optional[int] = ..., source_view_id_mapping: _Optional[_Union[_view_metadata_pb2.ViewIdMappingProto, _Mapping]] = ...) -> None: ...
