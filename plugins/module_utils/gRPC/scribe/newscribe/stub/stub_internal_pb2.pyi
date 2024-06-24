from open_util.net import protorpc_pb2 as _protorpc_pb2
from scribe.base import scribe_pb2 as _scribe_pb2
from scribe.newscribe.server import data_format_pb2 as _data_format_pb2
from scribe.newscribe.stub import server_error_pb2 as _server_error_pb2
from scribe.newscribe.stub import stub_pb2 as _stub_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptArg(_message.Message):
    __slots__ = ("bucket_id", "table", "version_context", "request_vec", "scribe_qos_params")
    class Request(_message.Message):
        __slots__ = ("row_key", "chosen_instance", "value_for_accept", "payload_offset", "payload_size")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FOR_ACCEPT_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
        row_key: _scribe_pb2.RowColumnKey
        chosen_instance: _data_format_pb2.PaxosInstance
        value_for_accept: _data_format_pb2.AcceptedValue
        payload_offset: int
        payload_size: int
        def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., chosen_instance: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ..., value_for_accept: _Optional[_Union[_data_format_pb2.AcceptedValue, _Mapping]] = ..., payload_offset: _Optional[int] = ..., payload_size: _Optional[int] = ...) -> None: ...
    BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_QOS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket_id: int
    table: int
    version_context: _stub_pb2.VersionContext
    request_vec: _containers.RepeatedCompositeFieldContainer[AcceptArg.Request]
    scribe_qos_params: _scribe_pb2.ScribeQoSParams
    def __init__(self, bucket_id: _Optional[int] = ..., table: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., request_vec: _Optional[_Iterable[_Union[AcceptArg.Request, _Mapping]]] = ..., scribe_qos_params: _Optional[_Union[_scribe_pb2.ScribeQoSParams, _Mapping]] = ...) -> None: ...

class AcceptResult(_message.Message):
    __slots__ = ("result_vec",)
    class Result(_message.Message):
        __slots__ = ("row_key", "error")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        row_key: _scribe_pb2.RowColumnKey
        error: _server_error_pb2.ServerErrorProto
        def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., error: _Optional[_Union[_server_error_pb2.ServerErrorProto, _Mapping]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[AcceptResult.Result]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[AcceptResult.Result, _Mapping]]] = ...) -> None: ...

class RowState(_message.Message):
    __slots__ = ("row_key", "row_payload_start_offset", "scribe_row_md", "md_row_payload", "columns_vec")
    class Column(_message.Message):
        __slots__ = ("col_name", "col_data")
        COL_NAME_FIELD_NUMBER: _ClassVar[int]
        COL_DATA_FIELD_NUMBER: _ClassVar[int]
        col_name: _scribe_pb2.RowColumnKey
        col_data: _data_format_pb2.PayloadRange
        def __init__(self, col_name: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., col_data: _Optional[_Union[_data_format_pb2.PayloadRange, _Mapping]] = ...) -> None: ...
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    ROW_PAYLOAD_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_ROW_MD_FIELD_NUMBER: _ClassVar[int]
    MD_ROW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_VEC_FIELD_NUMBER: _ClassVar[int]
    row_key: _scribe_pb2.RowColumnKey
    row_payload_start_offset: int
    scribe_row_md: _data_format_pb2.ScribeRowMD
    md_row_payload: _data_format_pb2.PayloadRange
    columns_vec: _containers.RepeatedCompositeFieldContainer[RowState.Column]
    def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., row_payload_start_offset: _Optional[int] = ..., scribe_row_md: _Optional[_Union[_data_format_pb2.ScribeRowMD, _Mapping]] = ..., md_row_payload: _Optional[_Union[_data_format_pb2.PayloadRange, _Mapping]] = ..., columns_vec: _Optional[_Iterable[_Union[RowState.Column, _Mapping]]] = ...) -> None: ...

class PaxosInstanceInfo(_message.Message):
    __slots__ = ("chosen_instance", "accept_instance", "is_intent")
    CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    IS_INTENT_FIELD_NUMBER: _ClassVar[int]
    chosen_instance: _data_format_pb2.PaxosInstance
    accept_instance: _data_format_pb2.PaxosInstance
    is_intent: bool
    def __init__(self, chosen_instance: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ..., accept_instance: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ..., is_intent: bool = ...) -> None: ...

class FetchSingleRowProto(_message.Message):
    __slots__ = ("row_key", "sender_paxos_instance_info")
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    SENDER_PAXOS_INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    row_key: _scribe_pb2.RowColumnKey
    sender_paxos_instance_info: PaxosInstanceInfo
    def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., sender_paxos_instance_info: _Optional[_Union[PaxosInstanceInfo, _Mapping]] = ...) -> None: ...

class FetchRowsArg(_message.Message):
    __slots__ = ("bucket", "table", "version_context", "rows", "rx_constituent_id")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    RX_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    table: int
    version_context: _stub_pb2.VersionContext
    rows: _containers.RepeatedCompositeFieldContainer[FetchSingleRowProto]
    rx_constituent_id: int
    def __init__(self, bucket: _Optional[int] = ..., table: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[FetchSingleRowProto, _Mapping]]] = ..., rx_constituent_id: _Optional[int] = ...) -> None: ...

class RowData2(_message.Message):
    __slots__ = ("scribe_row_md", "md_payload_size", "columns")
    class Column(_message.Message):
        __slots__ = ("col_name", "col_data")
        COL_NAME_FIELD_NUMBER: _ClassVar[int]
        COL_DATA_FIELD_NUMBER: _ClassVar[int]
        col_name: _scribe_pb2.RowColumnKey
        col_data: _data_format_pb2.PayloadRange
        def __init__(self, col_name: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., col_data: _Optional[_Union[_data_format_pb2.PayloadRange, _Mapping]] = ...) -> None: ...
    SCRIBE_ROW_MD_FIELD_NUMBER: _ClassVar[int]
    MD_PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    scribe_row_md: _data_format_pb2.ScribeRowMD
    md_payload_size: int
    columns: _containers.RepeatedCompositeFieldContainer[RowData2.Column]
    def __init__(self, scribe_row_md: _Optional[_Union[_data_format_pb2.ScribeRowMD, _Mapping]] = ..., md_payload_size: _Optional[int] = ..., columns: _Optional[_Iterable[_Union[RowData2.Column, _Mapping]]] = ...) -> None: ...

class FetchSingleRowResultProto(_message.Message):
    __slots__ = ("row_key", "row_paxos_instance_info", "row_data", "row_data_payload_offset")
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    ROW_PAXOS_INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    ROW_DATA_FIELD_NUMBER: _ClassVar[int]
    ROW_DATA_PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    row_key: _scribe_pb2.RowColumnKey
    row_paxos_instance_info: PaxosInstanceInfo
    row_data: RowData2
    row_data_payload_offset: int
    def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., row_paxos_instance_info: _Optional[_Union[PaxosInstanceInfo, _Mapping]] = ..., row_data: _Optional[_Union[RowData2, _Mapping]] = ..., row_data_payload_offset: _Optional[int] = ...) -> None: ...

class FetchRowsResult(_message.Message):
    __slots__ = ("rows",)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[FetchSingleRowResultProto]
    def __init__(self, rows: _Optional[_Iterable[_Union[FetchSingleRowResultProto, _Mapping]]] = ...) -> None: ...

class PushSingleRowProto(_message.Message):
    __slots__ = ("row_key", "row_data", "accepted_value", "row_payload_offset", "bucket", "version_context")
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    ROW_DATA_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    ROW_PAYLOAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    row_key: _scribe_pb2.RowColumnKey
    row_data: RowData2
    accepted_value: _data_format_pb2.AcceptedValue
    row_payload_offset: int
    bucket: int
    version_context: _stub_pb2.VersionContext
    def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., row_data: _Optional[_Union[RowData2, _Mapping]] = ..., accepted_value: _Optional[_Union[_data_format_pb2.AcceptedValue, _Mapping]] = ..., row_payload_offset: _Optional[int] = ..., bucket: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ...) -> None: ...

class PushRowsArg(_message.Message):
    __slots__ = ("table", "rows", "rx_constituent_id", "is_transaction")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    RX_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    table: int
    rows: _containers.RepeatedCompositeFieldContainer[PushSingleRowProto]
    rx_constituent_id: int
    is_transaction: bool
    def __init__(self, table: _Optional[int] = ..., rows: _Optional[_Iterable[_Union[PushSingleRowProto, _Mapping]]] = ..., rx_constituent_id: _Optional[int] = ..., is_transaction: bool = ...) -> None: ...

class PushRowsResult(_message.Message):
    __slots__ = ("result_vec",)
    class Result(_message.Message):
        __slots__ = ("row_key", "error")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        row_key: _scribe_pb2.RowColumnKey
        error: _server_error_pb2.ServerErrorProto
        def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., error: _Optional[_Union[_server_error_pb2.ServerErrorProto, _Mapping]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[PushRowsResult.Result]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[PushRowsResult.Result, _Mapping]]] = ...) -> None: ...

class PushChosenValuesArg(_message.Message):
    __slots__ = ("bucket", "table", "version_context", "row_vec", "scribe_qos_params")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_QOS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    table: int
    version_context: _stub_pb2.VersionContext
    row_vec: _containers.RepeatedCompositeFieldContainer[RowState]
    scribe_qos_params: _scribe_pb2.ScribeQoSParams
    def __init__(self, bucket: _Optional[int] = ..., table: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., row_vec: _Optional[_Iterable[_Union[RowState, _Mapping]]] = ..., scribe_qos_params: _Optional[_Union[_scribe_pb2.ScribeQoSParams, _Mapping]] = ...) -> None: ...

class PushChosenValuesResult(_message.Message):
    __slots__ = ("result_vec",)
    class Result(_message.Message):
        __slots__ = ("row_key", "error")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        row_key: _scribe_pb2.RowColumnKey
        error: _server_error_pb2.ServerErrorProto
        def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., error: _Optional[_Union[_server_error_pb2.ServerErrorProto, _Mapping]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[PushChosenValuesResult.Result]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[PushChosenValuesResult.Result, _Mapping]]] = ...) -> None: ...

class FetchReplicaStateArg(_message.Message):
    __slots__ = ("bucket", "table", "version_context", "row_key_vec", "include_all_columns", "scribe_qos_params")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_VEC_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    SCRIBE_QOS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    table: int
    version_context: _stub_pb2.VersionContext
    row_key_vec: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
    include_all_columns: bool
    scribe_qos_params: _scribe_pb2.ScribeQoSParams
    def __init__(self, bucket: _Optional[int] = ..., table: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., row_key_vec: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., include_all_columns: bool = ..., scribe_qos_params: _Optional[_Union[_scribe_pb2.ScribeQoSParams, _Mapping]] = ...) -> None: ...

class FetchReplicaStateResult(_message.Message):
    __slots__ = ("row_vec", "partial_result")
    ROW_VEC_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_RESULT_FIELD_NUMBER: _ClassVar[int]
    row_vec: _containers.RepeatedCompositeFieldContainer[RowState]
    partial_result: bool
    def __init__(self, row_vec: _Optional[_Iterable[_Union[RowState, _Mapping]]] = ..., partial_result: bool = ...) -> None: ...

class SendChosenNotificationsArg(_message.Message):
    __slots__ = ("bucket", "table", "version_context", "chosen_notifications_vec")
    class ChosenNotification(_message.Message):
        __slots__ = ("row_key", "chosen_instance")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        row_key: _scribe_pb2.RowColumnKey
        chosen_instance: _data_format_pb2.PaxosInstance
        def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., chosen_instance: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ...) -> None: ...
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_NOTIFICATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    table: int
    version_context: _stub_pb2.VersionContext
    chosen_notifications_vec: _containers.RepeatedCompositeFieldContainer[SendChosenNotificationsArg.ChosenNotification]
    def __init__(self, bucket: _Optional[int] = ..., table: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., chosen_notifications_vec: _Optional[_Iterable[_Union[SendChosenNotificationsArg.ChosenNotification, _Mapping]]] = ...) -> None: ...

class SendChosenNotificationsResult(_message.Message):
    __slots__ = ("result_vec",)
    class Result(_message.Message):
        __slots__ = ("row_key", "error")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        row_key: _scribe_pb2.RowColumnKey
        error: _server_error_pb2.ServerErrorProto
        def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., error: _Optional[_Union[_server_error_pb2.ServerErrorProto, _Mapping]] = ...) -> None: ...
    RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    result_vec: _containers.RepeatedCompositeFieldContainer[SendChosenNotificationsResult.Result]
    def __init__(self, result_vec: _Optional[_Iterable[_Union[SendChosenNotificationsResult.Result, _Mapping]]] = ...) -> None: ...

class SendBulkChosenNotificationsArg(_message.Message):
    __slots__ = ("bucket", "chosen_notifications_vec")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_NOTIFICATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    chosen_notifications_vec: _containers.RepeatedCompositeFieldContainer[SendChosenNotificationsArg]
    def __init__(self, bucket: _Optional[int] = ..., chosen_notifications_vec: _Optional[_Iterable[_Union[SendChosenNotificationsArg, _Mapping]]] = ...) -> None: ...

class TransactionChosenNotificationArg(_message.Message):
    __slots__ = ("table", "bucket_arg")
    class BucketChosenNotificationsArg(_message.Message):
        __slots__ = ("bucket", "version_context", "chosen_notifications_vec")
        class ChosenNotification(_message.Message):
            __slots__ = ("row_key", "chosen_instance")
            ROW_KEY_FIELD_NUMBER: _ClassVar[int]
            CHOSEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
            row_key: _scribe_pb2.RowColumnKey
            chosen_instance: _data_format_pb2.PaxosInstance
            def __init__(self, row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ..., chosen_instance: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ...) -> None: ...
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_NOTIFICATIONS_VEC_FIELD_NUMBER: _ClassVar[int]
        bucket: int
        version_context: _stub_pb2.VersionContext
        chosen_notifications_vec: _containers.RepeatedCompositeFieldContainer[TransactionChosenNotificationArg.BucketChosenNotificationsArg.ChosenNotification]
        def __init__(self, bucket: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., chosen_notifications_vec: _Optional[_Iterable[_Union[TransactionChosenNotificationArg.BucketChosenNotificationsArg.ChosenNotification, _Mapping]]] = ...) -> None: ...
    TABLE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_ARG_FIELD_NUMBER: _ClassVar[int]
    table: int
    bucket_arg: _containers.RepeatedCompositeFieldContainer[TransactionChosenNotificationArg.BucketChosenNotificationsArg]
    def __init__(self, table: _Optional[int] = ..., bucket_arg: _Optional[_Iterable[_Union[TransactionChosenNotificationArg.BucketChosenNotificationsArg, _Mapping]]] = ...) -> None: ...

class CheckReadyForLiveMigrationArg(_message.Message):
    __slots__ = ("version_context", "bucket", "required_size_bytes")
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    version_context: _stub_pb2.VersionContext
    bucket: int
    required_size_bytes: int
    def __init__(self, version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., bucket: _Optional[int] = ..., required_size_bytes: _Optional[int] = ...) -> None: ...

class CheckReadyForLiveMigrationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CheckViewVersionArg(_message.Message):
    __slots__ = ("version_context", "bucket", "rx_constituent_id")
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    RX_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    version_context: _stub_pb2.VersionContext
    bucket: int
    rx_constituent_id: int
    def __init__(self, version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., bucket: _Optional[int] = ..., rx_constituent_id: _Optional[int] = ...) -> None: ...

class CheckViewVersionResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DbRecord(_message.Message):
    __slots__ = ("key_payload_range", "value_payload_range")
    KEY_PAYLOAD_RANGE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PAYLOAD_RANGE_FIELD_NUMBER: _ClassVar[int]
    key_payload_range: _data_format_pb2.PayloadRange
    value_payload_range: _data_format_pb2.PayloadRange
    def __init__(self, key_payload_range: _Optional[_Union[_data_format_pb2.PayloadRange, _Mapping]] = ..., value_payload_range: _Optional[_Union[_data_format_pb2.PayloadRange, _Mapping]] = ...) -> None: ...

class TransferDbRecordsArg(_message.Message):
    __slots__ = ("version_context", "bucket", "table", "records", "is_last")
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_FIELD_NUMBER: _ClassVar[int]
    version_context: _stub_pb2.VersionContext
    bucket: int
    table: int
    records: _containers.RepeatedCompositeFieldContainer[DbRecord]
    is_last: bool
    def __init__(self, version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., bucket: _Optional[int] = ..., table: _Optional[int] = ..., records: _Optional[_Iterable[_Union[DbRecord, _Mapping]]] = ..., is_last: bool = ...) -> None: ...

class TransferDbRecordsResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferSstFilesArg(_message.Message):
    __slots__ = ("version_context", "bucket", "tablet_id", "transfer_index", "offset", "is_last", "sst_file_metadata", "db_comparator_name", "is_last_for_file", "file_sha256", "file_md5")
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLET_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_INDEX_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_FIELD_NUMBER: _ClassVar[int]
    SST_FILE_METADATA_FIELD_NUMBER: _ClassVar[int]
    DB_COMPARATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_FOR_FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA256_FIELD_NUMBER: _ClassVar[int]
    FILE_MD5_FIELD_NUMBER: _ClassVar[int]
    version_context: _stub_pb2.VersionContext
    bucket: int
    tablet_id: int
    transfer_index: int
    offset: int
    is_last: bool
    sst_file_metadata: _containers.RepeatedCompositeFieldContainer[_data_format_pb2.SstFileMetaData]
    db_comparator_name: str
    is_last_for_file: bool
    file_sha256: bytes
    file_md5: bytes
    def __init__(self, version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., bucket: _Optional[int] = ..., tablet_id: _Optional[int] = ..., transfer_index: _Optional[int] = ..., offset: _Optional[int] = ..., is_last: bool = ..., sst_file_metadata: _Optional[_Iterable[_Union[_data_format_pb2.SstFileMetaData, _Mapping]]] = ..., db_comparator_name: _Optional[str] = ..., is_last_for_file: bool = ..., file_sha256: _Optional[bytes] = ..., file_md5: _Optional[bytes] = ...) -> None: ...

class TransferSstFilesResult(_message.Message):
    __slots__ = ("checksum_verified",)
    CHECKSUM_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    checksum_verified: bool
    def __init__(self, checksum_verified: bool = ...) -> None: ...

class WALRecord(_message.Message):
    __slots__ = ("logical_timestamp", "serialized_write_batch")
    LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_WRITE_BATCH_FIELD_NUMBER: _ClassVar[int]
    logical_timestamp: int
    serialized_write_batch: _data_format_pb2.PayloadRange
    def __init__(self, logical_timestamp: _Optional[int] = ..., serialized_write_batch: _Optional[_Union[_data_format_pb2.PayloadRange, _Mapping]] = ...) -> None: ...

class TransferWALRecordsArg(_message.Message):
    __slots__ = ("version_context", "bucket", "last_logical_timestamp_from_prev_transfer", "records")
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGICAL_TIMESTAMP_FROM_PREV_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    version_context: _stub_pb2.VersionContext
    bucket: int
    last_logical_timestamp_from_prev_transfer: int
    records: _containers.RepeatedCompositeFieldContainer[WALRecord]
    def __init__(self, version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., bucket: _Optional[int] = ..., last_logical_timestamp_from_prev_transfer: _Optional[int] = ..., records: _Optional[_Iterable[_Union[WALRecord, _Mapping]]] = ...) -> None: ...

class TransferWALRecordsResult(_message.Message):
    __slots__ = ("last_logical_timestamp",)
    LAST_LOGICAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    last_logical_timestamp: int
    def __init__(self, last_logical_timestamp: _Optional[int] = ...) -> None: ...

class TransferCaughtupSequencerArg(_message.Message):
    __slots__ = ("version_context", "bucket", "last_known_caughtup_sequencer")
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_CAUGHTUP_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    version_context: _stub_pb2.VersionContext
    bucket: int
    last_known_caughtup_sequencer: int
    def __init__(self, version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., bucket: _Optional[int] = ..., last_known_caughtup_sequencer: _Optional[int] = ...) -> None: ...

class TransferCaughtupSequencerResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RowKeyWithTable(_message.Message):
    __slots__ = ("table", "row_key")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    table: int
    row_key: _scribe_pb2.RowColumnKey
    def __init__(self, table: _Optional[int] = ..., row_key: _Optional[_Union[_scribe_pb2.RowColumnKey, _Mapping]] = ...) -> None: ...

class ListKeysToCatchupArg(_message.Message):
    __slots__ = ("bucket", "version_context", "cookie", "last_known_caughtup_sequencer")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    LAST_KNOWN_CAUGHTUP_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    version_context: _stub_pb2.VersionContext
    cookie: bytes
    last_known_caughtup_sequencer: int
    def __init__(self, bucket: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., cookie: _Optional[bytes] = ..., last_known_caughtup_sequencer: _Optional[int] = ...) -> None: ...

class ListKeysToCatchupResult(_message.Message):
    __slots__ = ("keys_to_catch_up", "next_scan_cookie", "constituent_id")
    KEYS_TO_CATCH_UP_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCAN_COOKIE_FIELD_NUMBER: _ClassVar[int]
    CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    keys_to_catch_up: _containers.RepeatedCompositeFieldContainer[RowKeyWithTable]
    next_scan_cookie: bytes
    constituent_id: int
    def __init__(self, keys_to_catch_up: _Optional[_Iterable[_Union[RowKeyWithTable, _Mapping]]] = ..., next_scan_cookie: _Optional[bytes] = ..., constituent_id: _Optional[int] = ...) -> None: ...

class GCKeysArg(_message.Message):
    __slots__ = ("bucket", "table", "version_context", "keys_to_delete", "gc_instance_id_threshold")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEYS_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    GC_INSTANCE_ID_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    bucket: int
    table: int
    version_context: _stub_pb2.VersionContext
    keys_to_delete: _containers.RepeatedCompositeFieldContainer[_scribe_pb2.RowColumnKey]
    gc_instance_id_threshold: _data_format_pb2.PaxosInstance
    def __init__(self, bucket: _Optional[int] = ..., table: _Optional[int] = ..., version_context: _Optional[_Union[_stub_pb2.VersionContext, _Mapping]] = ..., keys_to_delete: _Optional[_Iterable[_Union[_scribe_pb2.RowColumnKey, _Mapping]]] = ..., gc_instance_id_threshold: _Optional[_Union[_data_format_pb2.PaxosInstance, _Mapping]] = ...) -> None: ...

class GCKeysResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
