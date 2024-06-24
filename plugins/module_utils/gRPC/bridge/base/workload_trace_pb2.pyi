from bridge.snap_fs import snap_fs_metadata_pb2 as _snap_fs_metadata_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkloadTraceProto(_message.Message):
    __slots__ = ("request_type", "offset", "length", "entity_handle", "blob_snap_tree_id", "start_usecs", "error", "is_forwarded", "is_random", "bytes_read_from_data_cache", "bytes_read_from_faa", "bytes_read_from_hydra", "view_box_id", "num_prefetch_levels", "name", "inode_type", "num_chunk_files_read", "version", "minion_blob_id", "minion_blob_offset", "iscsi_wl_trace")
    class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kSnapFSRead: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSMegaFileRead: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSWrite: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSMegaFileWrite: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSSetAttr: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSReadDir: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSLookupPath: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSCreate: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSRemove: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSLookupInode: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSUpdateInode: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSLookupDirEntry: _ClassVar[WorkloadTraceProto.RequestType]
        kSnapFSFlushEntity: _ClassVar[WorkloadTraceProto.RequestType]
        kBlobRead: _ClassVar[WorkloadTraceProto.RequestType]
        kBlobWrite: _ClassVar[WorkloadTraceProto.RequestType]
        kBlobReadAhead: _ClassVar[WorkloadTraceProto.RequestType]
        kIscsi: _ClassVar[WorkloadTraceProto.RequestType]
        kHydraFlush: _ClassVar[WorkloadTraceProto.RequestType]
    kSnapFSRead: WorkloadTraceProto.RequestType
    kSnapFSMegaFileRead: WorkloadTraceProto.RequestType
    kSnapFSWrite: WorkloadTraceProto.RequestType
    kSnapFSMegaFileWrite: WorkloadTraceProto.RequestType
    kSnapFSSetAttr: WorkloadTraceProto.RequestType
    kSnapFSReadDir: WorkloadTraceProto.RequestType
    kSnapFSLookupPath: WorkloadTraceProto.RequestType
    kSnapFSCreate: WorkloadTraceProto.RequestType
    kSnapFSRemove: WorkloadTraceProto.RequestType
    kSnapFSLookupInode: WorkloadTraceProto.RequestType
    kSnapFSUpdateInode: WorkloadTraceProto.RequestType
    kSnapFSLookupDirEntry: WorkloadTraceProto.RequestType
    kSnapFSFlushEntity: WorkloadTraceProto.RequestType
    kBlobRead: WorkloadTraceProto.RequestType
    kBlobWrite: WorkloadTraceProto.RequestType
    kBlobReadAhead: WorkloadTraceProto.RequestType
    kIscsi: WorkloadTraceProto.RequestType
    kHydraFlush: WorkloadTraceProto.RequestType
    class SnapFSHandleProto(_message.Message):
        __slots__ = ("view_id", "root_inode_id", "entity_id")
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        ROOT_INODE_ID_FIELD_NUMBER: _ClassVar[int]
        ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
        view_id: int
        root_inode_id: int
        entity_id: int
        def __init__(self, view_id: _Optional[int] = ..., root_inode_id: _Optional[int] = ..., entity_id: _Optional[int] = ...) -> None: ...
    class IscsiWorkloadTraceProto(_message.Message):
        __slots__ = ("request_type", "lun", "view_name", "view_id", "op_code", "command_status", "size", "updated_size", "reservation_action", "reservation_scope", "reservation_type", "src_file_name", "error", "task_management_function")
        class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kScsiFormatUnitOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiInquiryOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiPersistentReserveInOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiPersistentReserveOutOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiReadCapacityOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiReadOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiReportLunsOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiTaskManagementOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiTestUnitReadyOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiWriteOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiCloneToLUNOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiCreateLUNOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiRemoveLUNOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
            kScsiUpdateLUNSizeOp: _ClassVar[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType]
        kScsiFormatUnitOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiInquiryOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiPersistentReserveInOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiPersistentReserveOutOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiReadCapacityOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiReadOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiReportLunsOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiTaskManagementOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiTestUnitReadyOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiWriteOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiCloneToLUNOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiCreateLUNOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiRemoveLUNOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        kScsiUpdateLUNSizeOp: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
        LUN_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_ID_FIELD_NUMBER: _ClassVar[int]
        OP_CODE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_STATUS_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_SIZE_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_SCOPE_FIELD_NUMBER: _ClassVar[int]
        RESERVATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        SRC_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        TASK_MANAGEMENT_FUNCTION_FIELD_NUMBER: _ClassVar[int]
        request_type: WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType
        lun: int
        view_name: str
        view_id: int
        op_code: str
        command_status: str
        size: int
        updated_size: int
        reservation_action: str
        reservation_scope: str
        reservation_type: str
        src_file_name: str
        error: int
        task_management_function: str
        def __init__(self, request_type: _Optional[_Union[WorkloadTraceProto.IscsiWorkloadTraceProto.RequestType, str]] = ..., lun: _Optional[int] = ..., view_name: _Optional[str] = ..., view_id: _Optional[int] = ..., op_code: _Optional[str] = ..., command_status: _Optional[str] = ..., size: _Optional[int] = ..., updated_size: _Optional[int] = ..., reservation_action: _Optional[str] = ..., reservation_scope: _Optional[str] = ..., reservation_type: _Optional[str] = ..., src_file_name: _Optional[str] = ..., error: _Optional[int] = ..., task_management_function: _Optional[str] = ...) -> None: ...
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    ENTITY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BLOB_SNAP_TREE_ID_FIELD_NUMBER: _ClassVar[int]
    START_USECS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_FORWARDED_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FROM_DATA_CACHE_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FROM_FAA_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FROM_HYDRA_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_PREFETCH_LEVELS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_CHUNK_FILES_READ_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    MINION_BLOB_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ISCSI_WL_TRACE_FIELD_NUMBER: _ClassVar[int]
    request_type: WorkloadTraceProto.RequestType
    offset: int
    length: int
    entity_handle: WorkloadTraceProto.SnapFSHandleProto
    blob_snap_tree_id: int
    start_usecs: int
    error: int
    is_forwarded: bool
    is_random: bool
    bytes_read_from_data_cache: int
    bytes_read_from_faa: int
    bytes_read_from_hydra: int
    view_box_id: int
    num_prefetch_levels: int
    name: str
    inode_type: _snap_fs_metadata_pb2.InodeMetadataProto.InodeType
    num_chunk_files_read: int
    version: int
    minion_blob_id: int
    minion_blob_offset: int
    iscsi_wl_trace: WorkloadTraceProto.IscsiWorkloadTraceProto
    def __init__(self, request_type: _Optional[_Union[WorkloadTraceProto.RequestType, str]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., entity_handle: _Optional[_Union[WorkloadTraceProto.SnapFSHandleProto, _Mapping]] = ..., blob_snap_tree_id: _Optional[int] = ..., start_usecs: _Optional[int] = ..., error: _Optional[int] = ..., is_forwarded: bool = ..., is_random: bool = ..., bytes_read_from_data_cache: _Optional[int] = ..., bytes_read_from_faa: _Optional[int] = ..., bytes_read_from_hydra: _Optional[int] = ..., view_box_id: _Optional[int] = ..., num_prefetch_levels: _Optional[int] = ..., name: _Optional[str] = ..., inode_type: _Optional[_Union[_snap_fs_metadata_pb2.InodeMetadataProto.InodeType, str]] = ..., num_chunk_files_read: _Optional[int] = ..., version: _Optional[int] = ..., minion_blob_id: _Optional[int] = ..., minion_blob_offset: _Optional[int] = ..., iscsi_wl_trace: _Optional[_Union[WorkloadTraceProto.IscsiWorkloadTraceProto, _Mapping]] = ...) -> None: ...
