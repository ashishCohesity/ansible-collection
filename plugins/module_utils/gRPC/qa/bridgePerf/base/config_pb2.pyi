from qa.bridgePerf.base import bridge_perf_pb2 as _bridge_perf_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ("mongo_url", "mongodb_name", "node_ip_vec", "VIP_list", "partition_host_name", "partition_name", "CLI_path", "FIO_path", "testcase_vec", "num_builds_in_report", "comparison_window_size", "lean_run_testcase_group_vec", "summary_report_testcase_vec", "report_file_path", "send_mail", "mail_config", "update_db", "force_install_script", "config_name", "test_mode", "disk_bench_exec_path", "blob_size", "skip_qa_build_check", "global_compression", "global_encryption", "hydra_flush_timeout_mins", "global_write_compression_pct", "global_write_compress_pattern_chunk_size", "filebench_path", "configFilePath", "erasure_coded_viewbox", "num_data_stripes", "num_failure_stripes", "global_config_type", "global_minion", "num_failures", "version_specific_commands")
    class TestcaseGroup(_message.Message):
        __slots__ = ("testcase_vec",)
        TESTCASE_VEC_FIELD_NUMBER: _ClassVar[int]
        testcase_vec: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, testcase_vec: _Optional[_Iterable[int]] = ...) -> None: ...
    class MailConfig(_message.Message):
        __slots__ = ("server", "port", "sender", "sender_name", "recipients", "subject")
        SERVER_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        SENDER_FIELD_NUMBER: _ClassVar[int]
        SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
        RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        server: str
        port: int
        sender: str
        sender_name: str
        recipients: _containers.RepeatedScalarFieldContainer[str]
        subject: str
        def __init__(self, server: _Optional[str] = ..., port: _Optional[int] = ..., sender: _Optional[str] = ..., sender_name: _Optional[str] = ..., recipients: _Optional[_Iterable[str]] = ..., subject: _Optional[str] = ...) -> None: ...
    class VersionSpecificCommands(_message.Message):
        __slots__ = ("subnet_whitelist_add", "subnet_whitelist_list")
        SUBNET_WHITELIST_ADD_FIELD_NUMBER: _ClassVar[int]
        SUBNET_WHITELIST_LIST_FIELD_NUMBER: _ClassVar[int]
        subnet_whitelist_add: str
        subnet_whitelist_list: str
        def __init__(self, subnet_whitelist_add: _Optional[str] = ..., subnet_whitelist_list: _Optional[str] = ...) -> None: ...
    MONGO_URL_FIELD_NUMBER: _ClassVar[int]
    MONGODB_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_VEC_FIELD_NUMBER: _ClassVar[int]
    VIP_LIST_FIELD_NUMBER: _ClassVar[int]
    PARTITION_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    CLI_PATH_FIELD_NUMBER: _ClassVar[int]
    FIO_PATH_FIELD_NUMBER: _ClassVar[int]
    TESTCASE_VEC_FIELD_NUMBER: _ClassVar[int]
    NUM_BUILDS_IN_REPORT_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    LEAN_RUN_TESTCASE_GROUP_VEC_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_REPORT_TESTCASE_VEC_FIELD_NUMBER: _ClassVar[int]
    REPORT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SEND_MAIL_FIELD_NUMBER: _ClassVar[int]
    MAIL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DB_FIELD_NUMBER: _ClassVar[int]
    FORCE_INSTALL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    TEST_MODE_FIELD_NUMBER: _ClassVar[int]
    DISK_BENCH_EXEC_PATH_FIELD_NUMBER: _ClassVar[int]
    BLOB_SIZE_FIELD_NUMBER: _ClassVar[int]
    SKIP_QA_BUILD_CHECK_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    HYDRA_FLUSH_TIMEOUT_MINS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_WRITE_COMPRESSION_PCT_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_WRITE_COMPRESS_PATTERN_CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILEBENCH_PATH_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILEPATH_FIELD_NUMBER: _ClassVar[int]
    ERASURE_CODED_VIEWBOX_FIELD_NUMBER: _ClassVar[int]
    NUM_DATA_STRIPES_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILURE_STRIPES_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_MINION_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILURES_FIELD_NUMBER: _ClassVar[int]
    VERSION_SPECIFIC_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    mongo_url: str
    mongodb_name: str
    node_ip_vec: _containers.RepeatedScalarFieldContainer[str]
    VIP_list: _containers.RepeatedScalarFieldContainer[str]
    partition_host_name: str
    partition_name: str
    CLI_path: str
    FIO_path: str
    testcase_vec: _containers.RepeatedCompositeFieldContainer[_bridge_perf_pb2.TestParam]
    num_builds_in_report: int
    comparison_window_size: int
    lean_run_testcase_group_vec: _containers.RepeatedCompositeFieldContainer[Config.TestcaseGroup]
    summary_report_testcase_vec: _containers.RepeatedScalarFieldContainer[int]
    report_file_path: str
    send_mail: bool
    mail_config: Config.MailConfig
    update_db: bool
    force_install_script: str
    config_name: str
    test_mode: str
    disk_bench_exec_path: str
    blob_size: int
    skip_qa_build_check: bool
    global_compression: str
    global_encryption: bool
    hydra_flush_timeout_mins: int
    global_write_compression_pct: int
    global_write_compress_pattern_chunk_size: int
    filebench_path: str
    configFilePath: str
    erasure_coded_viewbox: bool
    num_data_stripes: int
    num_failure_stripes: int
    global_config_type: str
    global_minion: bool
    num_failures: int
    version_specific_commands: Config.VersionSpecificCommands
    def __init__(self, mongo_url: _Optional[str] = ..., mongodb_name: _Optional[str] = ..., node_ip_vec: _Optional[_Iterable[str]] = ..., VIP_list: _Optional[_Iterable[str]] = ..., partition_host_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., CLI_path: _Optional[str] = ..., FIO_path: _Optional[str] = ..., testcase_vec: _Optional[_Iterable[_Union[_bridge_perf_pb2.TestParam, _Mapping]]] = ..., num_builds_in_report: _Optional[int] = ..., comparison_window_size: _Optional[int] = ..., lean_run_testcase_group_vec: _Optional[_Iterable[_Union[Config.TestcaseGroup, _Mapping]]] = ..., summary_report_testcase_vec: _Optional[_Iterable[int]] = ..., report_file_path: _Optional[str] = ..., send_mail: bool = ..., mail_config: _Optional[_Union[Config.MailConfig, _Mapping]] = ..., update_db: bool = ..., force_install_script: _Optional[str] = ..., config_name: _Optional[str] = ..., test_mode: _Optional[str] = ..., disk_bench_exec_path: _Optional[str] = ..., blob_size: _Optional[int] = ..., skip_qa_build_check: bool = ..., global_compression: _Optional[str] = ..., global_encryption: bool = ..., hydra_flush_timeout_mins: _Optional[int] = ..., global_write_compression_pct: _Optional[int] = ..., global_write_compress_pattern_chunk_size: _Optional[int] = ..., filebench_path: _Optional[str] = ..., configFilePath: _Optional[str] = ..., erasure_coded_viewbox: bool = ..., num_data_stripes: _Optional[int] = ..., num_failure_stripes: _Optional[int] = ..., global_config_type: _Optional[str] = ..., global_minion: bool = ..., num_failures: _Optional[int] = ..., version_specific_commands: _Optional[_Union[Config.VersionSpecificCommands, _Mapping]] = ...) -> None: ...
