from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFlag(_message.Message):
    __slots__ = ("flag_name", "flag_value")
    FLAG_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    flag_name: str
    flag_value: str
    def __init__(self, flag_name: _Optional[str] = ..., flag_value: _Optional[str] = ...) -> None: ...

class TestParam(_message.Message):
    __slots__ = ("testcase_id", "testcase_name", "enable_hydra", "disk_type", "dedup_type", "op", "blob_count", "outstanding_ops_count", "node_count", "run_count", "clean_data", "dedup_percentage", "additional_param", "gflags", "wait_for_hydra_flush", "compression_level", "encryption", "copyDir", "sourceDir", "block_size", "runtime", "ssd_benchmark_test", "qos_policy", "collect_hydra_flush_speed_metric", "bssplit", "dedup_test_overwrite_file", "dedup_data_change_percentage", "dedup_test", "rand_seed", "thread_count", "process_count", "filebench_filecount", "filer_benchmark_test", "filer_meandirwidth", "filer_filesize", "vb_name", "view_name")
    TESTCASE_ID_FIELD_NUMBER: _ClassVar[int]
    TESTCASE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HYDRA_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    BLOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    OUTSTANDING_OPS_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLEAN_DATA_FIELD_NUMBER: _ClassVar[int]
    DEDUP_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAM_FIELD_NUMBER: _ClassVar[int]
    GFLAGS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_HYDRA_FLUSH_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    COPYDIR_FIELD_NUMBER: _ClassVar[int]
    SOURCEDIR_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SSD_BENCHMARK_TEST_FIELD_NUMBER: _ClassVar[int]
    QOS_POLICY_FIELD_NUMBER: _ClassVar[int]
    COLLECT_HYDRA_FLUSH_SPEED_METRIC_FIELD_NUMBER: _ClassVar[int]
    BSSPLIT_FIELD_NUMBER: _ClassVar[int]
    DEDUP_TEST_OVERWRITE_FILE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_DATA_CHANGE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    DEDUP_TEST_FIELD_NUMBER: _ClassVar[int]
    RAND_SEED_FIELD_NUMBER: _ClassVar[int]
    THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FILEBENCH_FILECOUNT_FIELD_NUMBER: _ClassVar[int]
    FILER_BENCHMARK_TEST_FIELD_NUMBER: _ClassVar[int]
    FILER_MEANDIRWIDTH_FIELD_NUMBER: _ClassVar[int]
    FILER_FILESIZE_FIELD_NUMBER: _ClassVar[int]
    VB_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    testcase_id: int
    testcase_name: str
    enable_hydra: bool
    disk_type: str
    dedup_type: str
    op: str
    blob_count: int
    outstanding_ops_count: int
    node_count: int
    run_count: int
    clean_data: bool
    dedup_percentage: int
    additional_param: str
    gflags: _containers.RepeatedCompositeFieldContainer[GFlag]
    wait_for_hydra_flush: bool
    compression_level: str
    encryption: bool
    copyDir: str
    sourceDir: str
    block_size: str
    runtime: int
    ssd_benchmark_test: bool
    qos_policy: str
    collect_hydra_flush_speed_metric: bool
    bssplit: str
    dedup_test_overwrite_file: bool
    dedup_data_change_percentage: int
    dedup_test: bool
    rand_seed: int
    thread_count: int
    process_count: int
    filebench_filecount: int
    filer_benchmark_test: bool
    filer_meandirwidth: int
    filer_filesize: str
    vb_name: str
    view_name: str
    def __init__(self, testcase_id: _Optional[int] = ..., testcase_name: _Optional[str] = ..., enable_hydra: bool = ..., disk_type: _Optional[str] = ..., dedup_type: _Optional[str] = ..., op: _Optional[str] = ..., blob_count: _Optional[int] = ..., outstanding_ops_count: _Optional[int] = ..., node_count: _Optional[int] = ..., run_count: _Optional[int] = ..., clean_data: bool = ..., dedup_percentage: _Optional[int] = ..., additional_param: _Optional[str] = ..., gflags: _Optional[_Iterable[_Union[GFlag, _Mapping]]] = ..., wait_for_hydra_flush: bool = ..., compression_level: _Optional[str] = ..., encryption: bool = ..., copyDir: _Optional[str] = ..., sourceDir: _Optional[str] = ..., block_size: _Optional[str] = ..., runtime: _Optional[int] = ..., ssd_benchmark_test: bool = ..., qos_policy: _Optional[str] = ..., collect_hydra_flush_speed_metric: bool = ..., bssplit: _Optional[str] = ..., dedup_test_overwrite_file: bool = ..., dedup_data_change_percentage: _Optional[int] = ..., dedup_test: bool = ..., rand_seed: _Optional[int] = ..., thread_count: _Optional[int] = ..., process_count: _Optional[int] = ..., filebench_filecount: _Optional[int] = ..., filer_benchmark_test: bool = ..., filer_meandirwidth: _Optional[int] = ..., filer_filesize: _Optional[str] = ..., vb_name: _Optional[str] = ..., view_name: _Optional[str] = ...) -> None: ...

class TestResult(_message.Message):
    __slots__ = ("throughput_val", "throughput_std_dev", "throughput_unit", "latency_val", "latency_std_dev", "latency_unit", "iops", "iops_std_dev", "node_ip", "test_status", "hydra_flush_speed", "hydra_flush_unit", "hydra_flush_std_dev", "op_name", "test_case_id", "run_duration")
    THROUGHPUT_VAL_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_STD_DEV_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_UNIT_FIELD_NUMBER: _ClassVar[int]
    LATENCY_VAL_FIELD_NUMBER: _ClassVar[int]
    LATENCY_STD_DEV_FIELD_NUMBER: _ClassVar[int]
    LATENCY_UNIT_FIELD_NUMBER: _ClassVar[int]
    IOPS_FIELD_NUMBER: _ClassVar[int]
    IOPS_STD_DEV_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    HYDRA_FLUSH_SPEED_FIELD_NUMBER: _ClassVar[int]
    HYDRA_FLUSH_UNIT_FIELD_NUMBER: _ClassVar[int]
    HYDRA_FLUSH_STD_DEV_FIELD_NUMBER: _ClassVar[int]
    OP_NAME_FIELD_NUMBER: _ClassVar[int]
    TEST_CASE_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_DURATION_FIELD_NUMBER: _ClassVar[int]
    throughput_val: float
    throughput_std_dev: float
    throughput_unit: str
    latency_val: float
    latency_std_dev: float
    latency_unit: str
    iops: float
    iops_std_dev: float
    node_ip: str
    test_status: bool
    hydra_flush_speed: float
    hydra_flush_unit: str
    hydra_flush_std_dev: float
    op_name: str
    test_case_id: str
    run_duration: str
    def __init__(self, throughput_val: _Optional[float] = ..., throughput_std_dev: _Optional[float] = ..., throughput_unit: _Optional[str] = ..., latency_val: _Optional[float] = ..., latency_std_dev: _Optional[float] = ..., latency_unit: _Optional[str] = ..., iops: _Optional[float] = ..., iops_std_dev: _Optional[float] = ..., node_ip: _Optional[str] = ..., test_status: bool = ..., hydra_flush_speed: _Optional[float] = ..., hydra_flush_unit: _Optional[str] = ..., hydra_flush_std_dev: _Optional[float] = ..., op_name: _Optional[str] = ..., test_case_id: _Optional[str] = ..., run_duration: _Optional[str] = ...) -> None: ...

class TestData(_message.Message):
    __slots__ = ("test_param", "result_summary", "node_test_result_vec")
    TEST_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESULT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    NODE_TEST_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    test_param: TestParam
    result_summary: TestResult
    node_test_result_vec: _containers.RepeatedCompositeFieldContainer[TestResult]
    def __init__(self, test_param: _Optional[_Union[TestParam, _Mapping]] = ..., result_summary: _Optional[_Union[TestResult, _Mapping]] = ..., node_test_result_vec: _Optional[_Iterable[_Union[TestResult, _Mapping]]] = ...) -> None: ...

class BuildTestData(_message.Message):
    __slots__ = ("build_id", "timestamp", "test_data_vec", "compression_setting", "encryption_setting", "write_compression_pct", "erasure_coded_enabled", "num_data_stripes", "num_failure_stripes", "config_type", "minion_setting", "num_failures")
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TEST_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_SETTING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SETTING_FIELD_NUMBER: _ClassVar[int]
    WRITE_COMPRESSION_PCT_FIELD_NUMBER: _ClassVar[int]
    ERASURE_CODED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILURE_STRIPES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MINION_SETTING_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILURES_FIELD_NUMBER: _ClassVar[int]
    build_id: str
    timestamp: int
    test_data_vec: _containers.RepeatedCompositeFieldContainer[TestData]
    compression_setting: str
    encryption_setting: bool
    write_compression_pct: int
    erasure_coded_enabled: bool
    num_data_stripes: int
    num_failure_stripes: int
    config_type: str
    minion_setting: bool
    num_failures: int
    def __init__(self, build_id: _Optional[str] = ..., timestamp: _Optional[int] = ..., test_data_vec: _Optional[_Iterable[_Union[TestData, _Mapping]]] = ..., compression_setting: _Optional[str] = ..., encryption_setting: bool = ..., write_compression_pct: _Optional[int] = ..., erasure_coded_enabled: bool = ..., num_data_stripes: _Optional[int] = ..., num_failure_stripes: _Optional[int] = ..., config_type: _Optional[str] = ..., minion_setting: bool = ..., num_failures: _Optional[int] = ...) -> None: ...

class FilerTestResult(_message.Message):
    __slots__ = ("result_summary", "node_ip")
    RESULT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    result_summary: _containers.RepeatedCompositeFieldContainer[TestResult]
    node_ip: str
    def __init__(self, result_summary: _Optional[_Iterable[_Union[TestResult, _Mapping]]] = ..., node_ip: _Optional[str] = ...) -> None: ...

class FilerTestData(_message.Message):
    __slots__ = ("test_param", "result_summary", "node_test_result_vec")
    TEST_PARAM_FIELD_NUMBER: _ClassVar[int]
    RESULT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    NODE_TEST_RESULT_VEC_FIELD_NUMBER: _ClassVar[int]
    test_param: TestParam
    result_summary: FilerTestResult
    node_test_result_vec: _containers.RepeatedCompositeFieldContainer[FilerTestResult]
    def __init__(self, test_param: _Optional[_Union[TestParam, _Mapping]] = ..., result_summary: _Optional[_Union[FilerTestResult, _Mapping]] = ..., node_test_result_vec: _Optional[_Iterable[_Union[FilerTestResult, _Mapping]]] = ...) -> None: ...

class FilerBuildTestData(_message.Message):
    __slots__ = ("build_id", "timestamp", "test_data_vec", "compression_setting", "encryption_setting", "write_compression_pct", "config_type")
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TEST_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_SETTING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SETTING_FIELD_NUMBER: _ClassVar[int]
    WRITE_COMPRESSION_PCT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    build_id: str
    timestamp: int
    test_data_vec: _containers.RepeatedCompositeFieldContainer[FilerTestData]
    compression_setting: str
    encryption_setting: bool
    write_compression_pct: int
    config_type: str
    def __init__(self, build_id: _Optional[str] = ..., timestamp: _Optional[int] = ..., test_data_vec: _Optional[_Iterable[_Union[FilerTestData, _Mapping]]] = ..., compression_setting: _Optional[str] = ..., encryption_setting: bool = ..., write_compression_pct: _Optional[int] = ..., config_type: _Optional[str] = ...) -> None: ...
