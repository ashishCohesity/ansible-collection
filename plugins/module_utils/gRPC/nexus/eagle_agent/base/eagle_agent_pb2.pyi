from alerts.base import alert_pb2 as _alert_pb2
from alerts.master.stub import master_service_pb2 as _master_service_pb2
from nexus.eagle_agent.base import helios_magneto_state_pb2 as _helios_magneto_state_pb2
from nexus.eagle_agent.base import helios_stats_state_pb2 as _helios_stats_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSmartCtlCollector: _ClassVar[CollectorType]
    kTimeCapsuleCollector: _ClassVar[CollectorType]
    kRealTimeBundleCollector: _ClassVar[CollectorType]
    kAlertsCollector: _ClassVar[CollectorType]
    kStatsCollector: _ClassVar[CollectorType]
    kFirmwareCollector: _ClassVar[CollectorType]
    kMagnetoStateCollector: _ClassVar[CollectorType]
    kIrisDataCollector: _ClassVar[CollectorType]
    kNightlyBundleCollector: _ClassVar[CollectorType]
    kClusterConfigCollector: _ClassVar[CollectorType]
    kTricorderTestsCollector: _ClassVar[CollectorType]
    kIndexingStatsCollector: _ClassVar[CollectorType]
    kRunbooksCollector: _ClassVar[CollectorType]
    kCustomScriptCollector: _ClassVar[CollectorType]
    kVulscanMetadataCollector: _ClassVar[CollectorType]
    kHealthcheckTestsCollector: _ClassVar[CollectorType]
    kDataClassificationCollector: _ClassVar[CollectorType]
    kMetriczStatsCollector: _ClassVar[CollectorType]
    kTagUpdatesCollector: _ClassVar[CollectorType]
    kRigelConnectivityCollector: _ClassVar[CollectorType]
    kAuditLogDataCollector: _ClassVar[CollectorType]
    kNodesConfigCollector: _ClassVar[CollectorType]

class SupportBundleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kNightlyBundle: _ClassVar[SupportBundleType]
    kRealTimeBundle: _ClassVar[SupportBundleType]
    kSupportBundle: _ClassVar[SupportBundleType]

class DataDestinationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kHeliosDataChannel: _ClassVar[DataDestinationType]
    kDataReceiverChannel: _ClassVar[DataDestinationType]
    kOnPremAppChannel: _ClassVar[DataDestinationType]
    kOnDemandBundle: _ClassVar[DataDestinationType]
    kMockCollection: _ClassVar[DataDestinationType]
    kLocalChannel: _ClassVar[DataDestinationType]

class HardwareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kDisk: _ClassVar[HardwareType]
    kNIC: _ClassVar[HardwareType]
    kBIOS: _ClassVar[HardwareType]
    kRAID: _ClassVar[HardwareType]

class MockDataSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    small: _ClassVar[MockDataSize]
    medium: _ClassVar[MockDataSize]
    large: _ClassVar[MockDataSize]

class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KAdded: _ClassVar[Op]
    kModified: _ClassVar[Op]
    kDeleted: _ClassVar[Op]
kSmartCtlCollector: CollectorType
kTimeCapsuleCollector: CollectorType
kRealTimeBundleCollector: CollectorType
kAlertsCollector: CollectorType
kStatsCollector: CollectorType
kFirmwareCollector: CollectorType
kMagnetoStateCollector: CollectorType
kIrisDataCollector: CollectorType
kNightlyBundleCollector: CollectorType
kClusterConfigCollector: CollectorType
kTricorderTestsCollector: CollectorType
kIndexingStatsCollector: CollectorType
kRunbooksCollector: CollectorType
kCustomScriptCollector: CollectorType
kVulscanMetadataCollector: CollectorType
kHealthcheckTestsCollector: CollectorType
kDataClassificationCollector: CollectorType
kMetriczStatsCollector: CollectorType
kTagUpdatesCollector: CollectorType
kRigelConnectivityCollector: CollectorType
kAuditLogDataCollector: CollectorType
kNodesConfigCollector: CollectorType
kNightlyBundle: SupportBundleType
kRealTimeBundle: SupportBundleType
kSupportBundle: SupportBundleType
kHeliosDataChannel: DataDestinationType
kDataReceiverChannel: DataDestinationType
kOnPremAppChannel: DataDestinationType
kOnDemandBundle: DataDestinationType
kMockCollection: DataDestinationType
kLocalChannel: DataDestinationType
kDisk: HardwareType
kNIC: HardwareType
kBIOS: HardwareType
kRAID: HardwareType
small: MockDataSize
medium: MockDataSize
large: MockDataSize
KAdded: Op
kModified: Op
kDeleted: Op

class HeliosDestinationData(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: DataDestinationType
    def __init__(self, type: _Optional[_Union[DataDestinationType, str]] = ...) -> None: ...

class CollectorOutput(_message.Message):
    __slots__ = ("name", "type", "time_stamp", "runs")
    class CollectorRun(_message.Message):
        __slots__ = ("time_stamp", "cluster_id", "node_id", "node_ip", "entity_identifier", "output", "alerts_list", "status", "incarnation_id", "query_alerts_result", "collector_run_type", "query_resolutions_result", "software_version")
        class RunStatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kSuccess: _ClassVar[CollectorOutput.CollectorRun.RunStatusCode]
            kOutputTooLarge: _ClassVar[CollectorOutput.CollectorRun.RunStatusCode]
            kInternalServiceError: _ClassVar[CollectorOutput.CollectorRun.RunStatusCode]
            kNoResultsReturned: _ClassVar[CollectorOutput.CollectorRun.RunStatusCode]
        kSuccess: CollectorOutput.CollectorRun.RunStatusCode
        kOutputTooLarge: CollectorOutput.CollectorRun.RunStatusCode
        kInternalServiceError: CollectorOutput.CollectorRun.RunStatusCode
        kNoResultsReturned: CollectorOutput.CollectorRun.RunStatusCode
        class CollectorRunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            kQueryAlertsResult: _ClassVar[CollectorOutput.CollectorRun.CollectorRunType]
            kQueryResolutionsResult: _ClassVar[CollectorOutput.CollectorRun.CollectorRunType]
        kQueryAlertsResult: CollectorOutput.CollectorRun.CollectorRunType
        kQueryResolutionsResult: CollectorOutput.CollectorRun.CollectorRunType
        TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_IP_FIELD_NUMBER: _ClassVar[int]
        ENTITY_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        ALERTS_LIST_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_ALERTS_RESULT_FIELD_NUMBER: _ClassVar[int]
        COLLECTOR_RUN_TYPE_FIELD_NUMBER: _ClassVar[int]
        QUERY_RESOLUTIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
        SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        time_stamp: int
        cluster_id: int
        node_id: int
        node_ip: str
        entity_identifier: str
        output: str
        alerts_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertProto]
        status: CollectorOutput.CollectorRun.RunStatusCode
        incarnation_id: int
        query_alerts_result: _master_service_pb2.QueryAlertsResult
        collector_run_type: CollectorOutput.CollectorRun.CollectorRunType
        query_resolutions_result: _master_service_pb2.QueryResolutionsResult
        software_version: str
        def __init__(self, time_stamp: _Optional[int] = ..., cluster_id: _Optional[int] = ..., node_id: _Optional[int] = ..., node_ip: _Optional[str] = ..., entity_identifier: _Optional[str] = ..., output: _Optional[str] = ..., alerts_list: _Optional[_Iterable[_Union[_alert_pb2.AlertProto, _Mapping]]] = ..., status: _Optional[_Union[CollectorOutput.CollectorRun.RunStatusCode, str]] = ..., incarnation_id: _Optional[int] = ..., query_alerts_result: _Optional[_Union[_master_service_pb2.QueryAlertsResult, _Mapping]] = ..., collector_run_type: _Optional[_Union[CollectorOutput.CollectorRun.CollectorRunType, str]] = ..., query_resolutions_result: _Optional[_Union[_master_service_pb2.QueryResolutionsResult, _Mapping]] = ..., software_version: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: CollectorType
    time_stamp: int
    runs: _containers.RepeatedCompositeFieldContainer[CollectorOutput.CollectorRun]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[CollectorType, str]] = ..., time_stamp: _Optional[int] = ..., runs: _Optional[_Iterable[_Union[CollectorOutput.CollectorRun, _Mapping]]] = ...) -> None: ...

class FirmwareProto(_message.Message):
    __slots__ = ("hardware_type", "hardware_id", "hardware_desc", "hardware_model", "firmware_version")
    HARDWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_DESC_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    hardware_type: HardwareType
    hardware_id: str
    hardware_desc: str
    hardware_model: str
    firmware_version: str
    def __init__(self, hardware_type: _Optional[_Union[HardwareType, str]] = ..., hardware_id: _Optional[str] = ..., hardware_desc: _Optional[str] = ..., hardware_model: _Optional[str] = ..., firmware_version: _Optional[str] = ...) -> None: ...

class GetFirmwareInfoResult(_message.Message):
    __slots__ = ("firmware_vec",)
    FIRMWARE_VEC_FIELD_NUMBER: _ClassVar[int]
    firmware_vec: _containers.RepeatedCompositeFieldContainer[FirmwareProto]
    def __init__(self, firmware_vec: _Optional[_Iterable[_Union[FirmwareProto, _Mapping]]] = ...) -> None: ...

class HeliosCollectorState(_message.Message):
    __slots__ = ("collector_type", "collector_state")
    class CollectorState(_message.Message):
        __slots__ = ("magneto_state_cookie", "stats_collector_state", "alerts_collector_state")
        MAGNETO_STATE_COOKIE_FIELD_NUMBER: _ClassVar[int]
        STATS_COLLECTOR_STATE_FIELD_NUMBER: _ClassVar[int]
        ALERTS_COLLECTOR_STATE_FIELD_NUMBER: _ClassVar[int]
        magneto_state_cookie: _helios_magneto_state_pb2.MagnetoStateCookie
        stats_collector_state: _helios_stats_state_pb2.StatsCollectionInfo
        alerts_collector_state: int
        def __init__(self, magneto_state_cookie: _Optional[_Union[_helios_magneto_state_pb2.MagnetoStateCookie, _Mapping]] = ..., stats_collector_state: _Optional[_Union[_helios_stats_state_pb2.StatsCollectionInfo, _Mapping]] = ..., alerts_collector_state: _Optional[int] = ...) -> None: ...
    COLLECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTOR_STATE_FIELD_NUMBER: _ClassVar[int]
    collector_type: CollectorType
    collector_state: HeliosCollectorState.CollectorState
    def __init__(self, collector_type: _Optional[_Union[CollectorType, str]] = ..., collector_state: _Optional[_Union[HeliosCollectorState.CollectorState, _Mapping]] = ...) -> None: ...

class HeliosEndPointsConfig(_message.Message):
    __slots__ = ("helios_sandbox_data_endpoint", "helios_data_endpoint", "helios_sandbox_server_endpoint", "helios_server_endpoint", "helios_data_port", "internal_host", "helios_demo_server_endpoint", "helios_sandbox2_server_endpoint", "helios_test1_server_endpoint", "helios_test2_server_endpoint", "helios_local_server_endpoint", "helios_dev_server_endpoint")
    HELIOS_SANDBOX_DATA_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_DATA_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_SANDBOX_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_DATA_PORT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_HOST_FIELD_NUMBER: _ClassVar[int]
    HELIOS_DEMO_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_SANDBOX2_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_TEST1_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_TEST2_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_LOCAL_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HELIOS_DEV_SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    helios_sandbox_data_endpoint: str
    helios_data_endpoint: str
    helios_sandbox_server_endpoint: str
    helios_server_endpoint: str
    helios_data_port: int
    internal_host: str
    helios_demo_server_endpoint: str
    helios_sandbox2_server_endpoint: str
    helios_test1_server_endpoint: str
    helios_test2_server_endpoint: str
    helios_local_server_endpoint: str
    helios_dev_server_endpoint: str
    def __init__(self, helios_sandbox_data_endpoint: _Optional[str] = ..., helios_data_endpoint: _Optional[str] = ..., helios_sandbox_server_endpoint: _Optional[str] = ..., helios_server_endpoint: _Optional[str] = ..., helios_data_port: _Optional[int] = ..., internal_host: _Optional[str] = ..., helios_demo_server_endpoint: _Optional[str] = ..., helios_sandbox2_server_endpoint: _Optional[str] = ..., helios_test1_server_endpoint: _Optional[str] = ..., helios_test2_server_endpoint: _Optional[str] = ..., helios_local_server_endpoint: _Optional[str] = ..., helios_dev_server_endpoint: _Optional[str] = ...) -> None: ...

class MasterInfoResponse(_message.Message):
    __slots__ = ("master_ip", "error_msg")
    MASTER_IP_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    master_ip: str
    error_msg: str
    def __init__(self, master_ip: _Optional[str] = ..., error_msg: _Optional[str] = ...) -> None: ...

class HeliosConnectionStatusResponse(_message.Message):
    __slots__ = ("connected", "error_msg")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    connected: bool
    error_msg: str
    def __init__(self, connected: bool = ..., error_msg: _Optional[str] = ...) -> None: ...

class BulletinBoardRefreshResponse(_message.Message):
    __slots__ = ("error_msg",)
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    error_msg: str
    def __init__(self, error_msg: _Optional[str] = ...) -> None: ...

class GetHeliosEndpointResponse(_message.Message):
    __slots__ = ("helios_endpoint", "error_msg", "disable_agent")
    HELIOS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AGENT_FIELD_NUMBER: _ClassVar[int]
    helios_endpoint: str
    error_msg: str
    disable_agent: bool
    def __init__(self, helios_endpoint: _Optional[str] = ..., error_msg: _Optional[str] = ..., disable_agent: bool = ...) -> None: ...

class SimulationModeProto(_message.Message):
    __slots__ = ("gcs_mock_data_bucket_id", "firmware_data_filename", "smart_ctl_data_map", "AlertsLatest", "timecapsule_data_filename", "tricorder_tests_data_filename_deprecated", "alerts_resolution_latest")
    GCS_MOCK_DATA_BUCKET_ID_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_DATA_FILENAME_FIELD_NUMBER: _ClassVar[int]
    SMART_CTL_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    ALERTSLATEST_FIELD_NUMBER: _ClassVar[int]
    TIMECAPSULE_DATA_FILENAME_FIELD_NUMBER: _ClassVar[int]
    TRICORDER_TESTS_DATA_FILENAME_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ALERTS_RESOLUTION_LATEST_FIELD_NUMBER: _ClassVar[int]
    gcs_mock_data_bucket_id: str
    firmware_data_filename: str
    smart_ctl_data_map: str
    AlertsLatest: str
    timecapsule_data_filename: str
    tricorder_tests_data_filename_deprecated: str
    alerts_resolution_latest: str
    def __init__(self, gcs_mock_data_bucket_id: _Optional[str] = ..., firmware_data_filename: _Optional[str] = ..., smart_ctl_data_map: _Optional[str] = ..., AlertsLatest: _Optional[str] = ..., timecapsule_data_filename: _Optional[str] = ..., tricorder_tests_data_filename_deprecated: _Optional[str] = ..., alerts_resolution_latest: _Optional[str] = ...) -> None: ...

class FileOp(_message.Message):
    __slots__ = ("filename", "operation", "is_directory", "is_symlink")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    IS_SYMLINK_FIELD_NUMBER: _ClassVar[int]
    filename: str
    operation: Op
    is_directory: bool
    is_symlink: bool
    def __init__(self, filename: _Optional[str] = ..., operation: _Optional[_Union[Op, str]] = ..., is_directory: bool = ..., is_symlink: bool = ...) -> None: ...
