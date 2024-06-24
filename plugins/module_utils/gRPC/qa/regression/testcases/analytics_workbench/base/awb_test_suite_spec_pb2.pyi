from qa.regression.testcases.backup_tests.base import vm_backup_test_spec_pb2 as _vm_backup_test_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileLastModifiedTestInfo(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: int
    end_time: int
    def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...

class FilesOnServersTestInfo(_message.Message):
    __slots__ = ("job_names", "view_boxes", "servers", "file_types", "path", "latest_snapshot", "file_last_modified_test_data", "vm_backup_test_data")
    JOB_NAMES_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOXES_FIELD_NUMBER: _ClassVar[int]
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPES_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LATEST_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FILE_LAST_MODIFIED_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    VM_BACKUP_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    job_names: _containers.RepeatedScalarFieldContainer[str]
    view_boxes: _containers.RepeatedScalarFieldContainer[str]
    servers: _containers.RepeatedScalarFieldContainer[str]
    file_types: _containers.RepeatedScalarFieldContainer[str]
    path: str
    latest_snapshot: bool
    file_last_modified_test_data: FileLastModifiedTestInfo
    vm_backup_test_data: _vm_backup_test_spec_pb2.VmBackupInfo
    def __init__(self, job_names: _Optional[_Iterable[str]] = ..., view_boxes: _Optional[_Iterable[str]] = ..., servers: _Optional[_Iterable[str]] = ..., file_types: _Optional[_Iterable[str]] = ..., path: _Optional[str] = ..., latest_snapshot: bool = ..., file_last_modified_test_data: _Optional[_Union[FileLastModifiedTestInfo, _Mapping]] = ..., vm_backup_test_data: _Optional[_Union[_vm_backup_test_spec_pb2.VmBackupInfo, _Mapping]] = ...) -> None: ...

class FilesOnViewTestInfo(_message.Message):
    __slots__ = ("view_box", "view", "file_types", "path", "file_last_modified_test_data", "file_urls")
    VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPES_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_LAST_MODIFIED_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_URLS_FIELD_NUMBER: _ClassVar[int]
    view_box: str
    view: str
    file_types: _containers.RepeatedScalarFieldContainer[str]
    path: str
    file_last_modified_test_data: FileLastModifiedTestInfo
    file_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, view_box: _Optional[str] = ..., view: _Optional[str] = ..., file_types: _Optional[_Iterable[str]] = ..., path: _Optional[str] = ..., file_last_modified_test_data: _Optional[_Union[FileLastModifiedTestInfo, _Mapping]] = ..., file_urls: _Optional[_Iterable[str]] = ...) -> None: ...

class PatternFinderTestInfo(_message.Message):
    __slots__ = ("on_nfs", "files_on_servers_test_data", "files_on_view_test_data", "search_pattern", "results_location", "job_timeout")
    ON_NFS_FIELD_NUMBER: _ClassVar[int]
    FILES_ON_SERVERS_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    FILES_ON_VIEW_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RESULTS_LOCATION_FIELD_NUMBER: _ClassVar[int]
    JOB_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    on_nfs: bool
    files_on_servers_test_data: FilesOnServersTestInfo
    files_on_view_test_data: FilesOnViewTestInfo
    search_pattern: str
    results_location: str
    job_timeout: int
    def __init__(self, on_nfs: bool = ..., files_on_servers_test_data: _Optional[_Union[FilesOnServersTestInfo, _Mapping]] = ..., files_on_view_test_data: _Optional[_Union[FilesOnViewTestInfo, _Mapping]] = ..., search_pattern: _Optional[str] = ..., results_location: _Optional[str] = ..., job_timeout: _Optional[int] = ...) -> None: ...

class VideoCompressorTestInfo(_message.Message):
    __slots__ = ("view_box", "view", "extension", "video_codec", "audio_codec", "resolution", "output_extension", "file_types", "path", "file_last_modified_test_data", "results_location", "job_timeout", "video_file_url")
    VIEW_BOX_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODEC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CODEC_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPES_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_LAST_MODIFIED_TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    RESULTS_LOCATION_FIELD_NUMBER: _ClassVar[int]
    JOB_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    view_box: str
    view: str
    extension: str
    video_codec: str
    audio_codec: str
    resolution: str
    output_extension: str
    file_types: _containers.RepeatedScalarFieldContainer[str]
    path: str
    file_last_modified_test_data: FileLastModifiedTestInfo
    results_location: str
    job_timeout: int
    video_file_url: str
    def __init__(self, view_box: _Optional[str] = ..., view: _Optional[str] = ..., extension: _Optional[str] = ..., video_codec: _Optional[str] = ..., audio_codec: _Optional[str] = ..., resolution: _Optional[str] = ..., output_extension: _Optional[str] = ..., file_types: _Optional[_Iterable[str]] = ..., path: _Optional[str] = ..., file_last_modified_test_data: _Optional[_Union[FileLastModifiedTestInfo, _Mapping]] = ..., results_location: _Optional[str] = ..., job_timeout: _Optional[int] = ..., video_file_url: _Optional[str] = ...) -> None: ...

class AwbTestInfos(_message.Message):
    __slots__ = ("pattern_finder_test_data_vec", "video_compressor_test_data_vec")
    PATTERN_FINDER_TEST_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    VIDEO_COMPRESSOR_TEST_DATA_VEC_FIELD_NUMBER: _ClassVar[int]
    pattern_finder_test_data_vec: _containers.RepeatedCompositeFieldContainer[PatternFinderTestInfo]
    video_compressor_test_data_vec: _containers.RepeatedCompositeFieldContainer[VideoCompressorTestInfo]
    def __init__(self, pattern_finder_test_data_vec: _Optional[_Iterable[_Union[PatternFinderTestInfo, _Mapping]]] = ..., video_compressor_test_data_vec: _Optional[_Iterable[_Union[VideoCompressorTestInfo, _Mapping]]] = ...) -> None: ...
