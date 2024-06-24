from bridge.base import error_pb2 as _error_pb2
from bridge.madrox import rsync_snap_tree_diff_pb2 as _rsync_snap_tree_diff_pb2
from bridge.snap_tree import snap_tree_pb2 as _snap_tree_pb2
from bridge.s3_portal.base import s3_metadata_pb2 as _s3_metadata_pb2
from bridge.view_keeper import view_metadata_pb2 as _view_metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RsyncCustomSnapTreeWorkProto(_message.Message):
    __slots__ = ("tree_info", "work_vec")
    class CustomSnapTreeWorkUnit(_message.Message):
        __slots__ = ("key", "operation", "s3object_tree_val_proto")
        KEY_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        S3OBJECT_TREE_VAL_PROTO_FIELD_NUMBER: _ClassVar[int]
        key: _rsync_snap_tree_diff_pb2.CustomSnapTreeKeyProto
        operation: _snap_tree_pb2.SnapTreeKeyOperation.Type
        s3object_tree_val_proto: _s3_metadata_pb2.S3ObjectSnapTreeValueProto
        def __init__(self, key: _Optional[_Union[_rsync_snap_tree_diff_pb2.CustomSnapTreeKeyProto, _Mapping]] = ..., operation: _Optional[_Union[_snap_tree_pb2.SnapTreeKeyOperation.Type, str]] = ..., s3object_tree_val_proto: _Optional[_Union[_s3_metadata_pb2.S3ObjectSnapTreeValueProto, _Mapping]] = ...) -> None: ...
    TREE_INFO_FIELD_NUMBER: _ClassVar[int]
    WORK_VEC_FIELD_NUMBER: _ClassVar[int]
    tree_info: _view_metadata_pb2.SnapTreeInfo
    work_vec: _containers.RepeatedCompositeFieldContainer[RsyncCustomSnapTreeWorkProto.CustomSnapTreeWorkUnit]
    def __init__(self, tree_info: _Optional[_Union[_view_metadata_pb2.SnapTreeInfo, _Mapping]] = ..., work_vec: _Optional[_Iterable[_Union[RsyncCustomSnapTreeWorkProto.CustomSnapTreeWorkUnit, _Mapping]]] = ...) -> None: ...

class RsyncCustomSnapTreeResultProto(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
