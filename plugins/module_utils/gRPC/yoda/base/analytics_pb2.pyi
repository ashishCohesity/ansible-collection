from yoda.base import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JAVA: _ClassVar[Language]

class MapReduceEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kMapperInfo: _ClassVar[MapReduceEntityType]
    kReducerInfo: _ClassVar[MapReduceEntityType]
    kMapReduceInfo: _ClassVar[MapReduceEntityType]
    kMapReduceInstance: _ClassVar[MapReduceEntityType]

class MapReduceAuxDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kPattern: _ClassVar[MapReduceAuxDataType]
JAVA: Language
kMapperInfo: MapReduceEntityType
kReducerInfo: MapReduceEntityType
kMapReduceInfo: MapReduceEntityType
kMapReduceInstance: MapReduceEntityType
kPattern: MapReduceAuxDataType

class MapperInfo(_message.Message):
    __slots__ = ("id", "name", "language", "code", "jar_name", "jar_path", "is_system_defined")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    JAR_NAME_FIELD_NUMBER: _ClassVar[int]
    JAR_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DEFINED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    language: Language
    code: str
    jar_name: str
    jar_path: str
    is_system_defined: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., language: _Optional[_Union[Language, str]] = ..., code: _Optional[str] = ..., jar_name: _Optional[str] = ..., jar_path: _Optional[str] = ..., is_system_defined: bool = ...) -> None: ...

class ReducerInfo(_message.Message):
    __slots__ = ("id", "name", "language", "code", "jar_name", "jar_path", "is_system_defined")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    JAR_NAME_FIELD_NUMBER: _ClassVar[int]
    JAR_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DEFINED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    language: Language
    code: str
    jar_name: str
    jar_path: str
    is_system_defined: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., language: _Optional[_Union[Language, str]] = ..., code: _Optional[str] = ..., jar_name: _Optional[str] = ..., jar_path: _Optional[str] = ..., is_system_defined: bool = ...) -> None: ...

class InputSpec(_message.Message):
    __slots__ = ("on_nfs_files", "vm_selector", "files_selector")
    class FileTimeFilter(_message.Message):
        __slots__ = ("change_time_range_start_secs", "change_time_range_end_secs")
        CHANGE_TIME_RANGE_START_SECS_FIELD_NUMBER: _ClassVar[int]
        CHANGE_TIME_RANGE_END_SECS_FIELD_NUMBER: _ClassVar[int]
        change_time_range_start_secs: int
        change_time_range_end_secs: int
        def __init__(self, change_time_range_start_secs: _Optional[int] = ..., change_time_range_end_secs: _Optional[int] = ...) -> None: ...
    class InputVMsSelector(_message.Message):
        __slots__ = ("partition_ids", "job_ids", "source_entity_ids", "view_box_ids", "view_names", "min_snapshot_timestamp", "max_snapshot_timestamp", "process_latest_only", "filename_glob", "root_dir", "file_time_filter")
        PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
        JOB_IDS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_IDS_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAMES_FIELD_NUMBER: _ClassVar[int]
        MIN_SNAPSHOT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MAX_SNAPSHOT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PROCESS_LATEST_ONLY_FIELD_NUMBER: _ClassVar[int]
        FILENAME_GLOB_FIELD_NUMBER: _ClassVar[int]
        ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
        FILE_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
        partition_ids: _containers.RepeatedScalarFieldContainer[int]
        job_ids: _containers.RepeatedScalarFieldContainer[int]
        source_entity_ids: _containers.RepeatedScalarFieldContainer[int]
        view_box_ids: _containers.RepeatedScalarFieldContainer[int]
        view_names: _containers.RepeatedScalarFieldContainer[str]
        min_snapshot_timestamp: int
        max_snapshot_timestamp: int
        process_latest_only: bool
        filename_glob: _containers.RepeatedScalarFieldContainer[str]
        root_dir: str
        file_time_filter: InputSpec.FileTimeFilter
        def __init__(self, partition_ids: _Optional[_Iterable[int]] = ..., job_ids: _Optional[_Iterable[int]] = ..., source_entity_ids: _Optional[_Iterable[int]] = ..., view_box_ids: _Optional[_Iterable[int]] = ..., view_names: _Optional[_Iterable[str]] = ..., min_snapshot_timestamp: _Optional[int] = ..., max_snapshot_timestamp: _Optional[int] = ..., process_latest_only: bool = ..., filename_glob: _Optional[_Iterable[str]] = ..., root_dir: _Optional[str] = ..., file_time_filter: _Optional[_Union[InputSpec.FileTimeFilter, _Mapping]] = ...) -> None: ...
    class InputFilesSelector(_message.Message):
        __slots__ = ("partition_ids", "view_box_ids", "view_name", "filename_glob", "root_dir", "file_time_filter", "job_ids", "min_snapshot_timestamp", "max_snapshot_timestamp", "process_latest_only")
        PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
        VIEW_BOX_IDS_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        FILENAME_GLOB_FIELD_NUMBER: _ClassVar[int]
        ROOT_DIR_FIELD_NUMBER: _ClassVar[int]
        FILE_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
        JOB_IDS_FIELD_NUMBER: _ClassVar[int]
        MIN_SNAPSHOT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MAX_SNAPSHOT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        PROCESS_LATEST_ONLY_FIELD_NUMBER: _ClassVar[int]
        partition_ids: _containers.RepeatedScalarFieldContainer[int]
        view_box_ids: _containers.RepeatedScalarFieldContainer[int]
        view_name: str
        filename_glob: _containers.RepeatedScalarFieldContainer[str]
        root_dir: str
        file_time_filter: InputSpec.FileTimeFilter
        job_ids: _containers.RepeatedScalarFieldContainer[int]
        min_snapshot_timestamp: int
        max_snapshot_timestamp: int
        process_latest_only: bool
        def __init__(self, partition_ids: _Optional[_Iterable[int]] = ..., view_box_ids: _Optional[_Iterable[int]] = ..., view_name: _Optional[str] = ..., filename_glob: _Optional[_Iterable[str]] = ..., root_dir: _Optional[str] = ..., file_time_filter: _Optional[_Union[InputSpec.FileTimeFilter, _Mapping]] = ..., job_ids: _Optional[_Iterable[int]] = ..., min_snapshot_timestamp: _Optional[int] = ..., max_snapshot_timestamp: _Optional[int] = ..., process_latest_only: bool = ...) -> None: ...
    ON_NFS_FILES_FIELD_NUMBER: _ClassVar[int]
    VM_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    FILES_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    on_nfs_files: bool
    vm_selector: InputSpec.InputVMsSelector
    files_selector: InputSpec.InputFilesSelector
    def __init__(self, on_nfs_files: bool = ..., vm_selector: _Optional[_Union[InputSpec.InputVMsSelector, _Mapping]] = ..., files_selector: _Optional[_Union[InputSpec.InputFilesSelector, _Mapping]] = ...) -> None: ...

class OutputSpec(_message.Message):
    __slots__ = ("partition_id", "view_box_id", "view_name", "output_dir", "num_reduce_shards", "reduce_output_prefix")
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_BOX_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DIR_FIELD_NUMBER: _ClassVar[int]
    NUM_REDUCE_SHARDS_FIELD_NUMBER: _ClassVar[int]
    REDUCE_OUTPUT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    partition_id: int
    view_box_id: int
    view_name: str
    output_dir: str
    num_reduce_shards: int
    reduce_output_prefix: str
    def __init__(self, partition_id: _Optional[int] = ..., view_box_id: _Optional[int] = ..., view_name: _Optional[str] = ..., output_dir: _Optional[str] = ..., num_reduce_shards: _Optional[int] = ..., reduce_output_prefix: _Optional[str] = ...) -> None: ...

class MapReduceInfo(_message.Message):
    __slots__ = ("id", "name", "description", "mapper_id", "reducer_id", "is_system_defined", "required_property_vec", "app_property", "excluded_data_source_vec", "aux_data")
    class DataSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VM: _ClassVar[MapReduceInfo.DataSource]
        VIEW: _ClassVar[MapReduceInfo.DataSource]
    VM: MapReduceInfo.DataSource
    VIEW: MapReduceInfo.DataSource
    class RequiredProperty(_message.Message):
        __slots__ = ("name", "description", "is_required", "default_value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        is_required: bool
        default_value: str
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., is_required: bool = ..., default_value: _Optional[str] = ...) -> None: ...
    class AppProperty(_message.Message):
        __slots__ = ("csv_header",)
        CSV_HEADER_FIELD_NUMBER: _ClassVar[int]
        csv_header: str
        def __init__(self, csv_header: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAPPER_ID_FIELD_NUMBER: _ClassVar[int]
    REDUCER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DEFINED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PROPERTY_VEC_FIELD_NUMBER: _ClassVar[int]
    APP_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DATA_SOURCE_VEC_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    mapper_id: int
    reducer_id: int
    is_system_defined: bool
    required_property_vec: _containers.RepeatedCompositeFieldContainer[MapReduceInfo.RequiredProperty]
    app_property: MapReduceInfo.AppProperty
    excluded_data_source_vec: _containers.RepeatedScalarFieldContainer[MapReduceInfo.DataSource]
    aux_data: MapReduceAuxData
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., mapper_id: _Optional[int] = ..., reducer_id: _Optional[int] = ..., is_system_defined: bool = ..., required_property_vec: _Optional[_Iterable[_Union[MapReduceInfo.RequiredProperty, _Mapping]]] = ..., app_property: _Optional[_Union[MapReduceInfo.AppProperty, _Mapping]] = ..., excluded_data_source_vec: _Optional[_Iterable[_Union[MapReduceInfo.DataSource, str]]] = ..., aux_data: _Optional[_Union[MapReduceAuxData, _Mapping]] = ...) -> None: ...

class MapReduceInstance(_message.Message):
    __slots__ = ("id", "map_reduce_info_id", "input_spec", "output_spec", "input_params", "run_info")
    class InputParam(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RunInfo(_message.Message):
        __slots__ = ("status", "mappers_spawned", "reducers_spawned", "total_num_mappers", "total_num_reducers", "percentage_mapper_completion", "percentage_reducer_completion", "start_time", "execution_start_time_usecs", "map_done_time_usecs", "end_time", "percentage_completion", "remaining_time_mins", "error_message", "files_processed", "num_map_outputs", "num_reduce_outputs", "map_input_bytes")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            QUEUED: _ClassVar[MapReduceInstance.RunInfo.Status]
            RUNNING: _ClassVar[MapReduceInstance.RunInfo.Status]
            ABORTED: _ClassVar[MapReduceInstance.RunInfo.Status]
            COMPLETED: _ClassVar[MapReduceInstance.RunInfo.Status]
            FAILURE: _ClassVar[MapReduceInstance.RunInfo.Status]
        QUEUED: MapReduceInstance.RunInfo.Status
        RUNNING: MapReduceInstance.RunInfo.Status
        ABORTED: MapReduceInstance.RunInfo.Status
        COMPLETED: MapReduceInstance.RunInfo.Status
        FAILURE: MapReduceInstance.RunInfo.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        MAPPERS_SPAWNED_FIELD_NUMBER: _ClassVar[int]
        REDUCERS_SPAWNED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_NUM_MAPPERS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_NUM_REDUCERS_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_MAPPER_COMPLETION_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_REDUCER_COMPLETION_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        EXECUTION_START_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        MAP_DONE_TIME_USECS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_COMPLETION_FIELD_NUMBER: _ClassVar[int]
        REMAINING_TIME_MINS_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        FILES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        NUM_MAP_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        NUM_REDUCE_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        MAP_INPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
        status: MapReduceInstance.RunInfo.Status
        mappers_spawned: int
        reducers_spawned: int
        total_num_mappers: int
        total_num_reducers: int
        percentage_mapper_completion: float
        percentage_reducer_completion: float
        start_time: int
        execution_start_time_usecs: int
        map_done_time_usecs: int
        end_time: int
        percentage_completion: float
        remaining_time_mins: int
        error_message: str
        files_processed: int
        num_map_outputs: int
        num_reduce_outputs: int
        map_input_bytes: int
        def __init__(self, status: _Optional[_Union[MapReduceInstance.RunInfo.Status, str]] = ..., mappers_spawned: _Optional[int] = ..., reducers_spawned: _Optional[int] = ..., total_num_mappers: _Optional[int] = ..., total_num_reducers: _Optional[int] = ..., percentage_mapper_completion: _Optional[float] = ..., percentage_reducer_completion: _Optional[float] = ..., start_time: _Optional[int] = ..., execution_start_time_usecs: _Optional[int] = ..., map_done_time_usecs: _Optional[int] = ..., end_time: _Optional[int] = ..., percentage_completion: _Optional[float] = ..., remaining_time_mins: _Optional[int] = ..., error_message: _Optional[str] = ..., files_processed: _Optional[int] = ..., num_map_outputs: _Optional[int] = ..., num_reduce_outputs: _Optional[int] = ..., map_input_bytes: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MAP_REDUCE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_SPEC_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SPEC_FIELD_NUMBER: _ClassVar[int]
    INPUT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RUN_INFO_FIELD_NUMBER: _ClassVar[int]
    id: int
    map_reduce_info_id: int
    input_spec: InputSpec
    output_spec: OutputSpec
    input_params: _containers.RepeatedCompositeFieldContainer[MapReduceInstance.InputParam]
    run_info: MapReduceInstance.RunInfo
    def __init__(self, id: _Optional[int] = ..., map_reduce_info_id: _Optional[int] = ..., input_spec: _Optional[_Union[InputSpec, _Mapping]] = ..., output_spec: _Optional[_Union[OutputSpec, _Mapping]] = ..., input_params: _Optional[_Iterable[_Union[MapReduceInstance.InputParam, _Mapping]]] = ..., run_info: _Optional[_Union[MapReduceInstance.RunInfo, _Mapping]] = ...) -> None: ...

class GetMRJarUploadPathResult(_message.Message):
    __slots__ = ("error", "jar_upload_path")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JAR_UPLOAD_PATH_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    jar_upload_path: str
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., jar_upload_path: _Optional[str] = ...) -> None: ...

class SaveMapReduceEntityArg(_message.Message):
    __slots__ = ("entity_type", "mapper_info", "reducer_info", "map_reduce_info")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAPPER_INFO_FIELD_NUMBER: _ClassVar[int]
    REDUCER_INFO_FIELD_NUMBER: _ClassVar[int]
    MAP_REDUCE_INFO_FIELD_NUMBER: _ClassVar[int]
    entity_type: MapReduceEntityType
    mapper_info: MapperInfo
    reducer_info: ReducerInfo
    map_reduce_info: MapReduceInfo
    def __init__(self, entity_type: _Optional[_Union[MapReduceEntityType, str]] = ..., mapper_info: _Optional[_Union[MapperInfo, _Mapping]] = ..., reducer_info: _Optional[_Union[ReducerInfo, _Mapping]] = ..., map_reduce_info: _Optional[_Union[MapReduceInfo, _Mapping]] = ...) -> None: ...

class SaveMapReduceEntityResult(_message.Message):
    __slots__ = ("error", "id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., id: _Optional[int] = ...) -> None: ...

class GetMapReduceEntityArg(_message.Message):
    __slots__ = ("id", "entity_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    entity_type: MapReduceEntityType
    def __init__(self, id: _Optional[int] = ..., entity_type: _Optional[_Union[MapReduceEntityType, str]] = ...) -> None: ...

class GetMapReduceEntityResult(_message.Message):
    __slots__ = ("error", "results_maybe_stale", "mapper_info_list", "reducer_info_list", "map_reduce_info_list")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_MAYBE_STALE_FIELD_NUMBER: _ClassVar[int]
    MAPPER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    REDUCER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    MAP_REDUCE_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    results_maybe_stale: bool
    mapper_info_list: _containers.RepeatedCompositeFieldContainer[MapperInfo]
    reducer_info_list: _containers.RepeatedCompositeFieldContainer[ReducerInfo]
    map_reduce_info_list: _containers.RepeatedCompositeFieldContainer[MapReduceInfo]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., results_maybe_stale: bool = ..., mapper_info_list: _Optional[_Iterable[_Union[MapperInfo, _Mapping]]] = ..., reducer_info_list: _Optional[_Iterable[_Union[ReducerInfo, _Mapping]]] = ..., map_reduce_info_list: _Optional[_Iterable[_Union[MapReduceInfo, _Mapping]]] = ...) -> None: ...

class DeleteMapReduceEntityArg(_message.Message):
    __slots__ = ("id", "entity_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    entity_type: MapReduceEntityType
    def __init__(self, id: _Optional[int] = ..., entity_type: _Optional[_Union[MapReduceEntityType, str]] = ...) -> None: ...

class DeleteMapReduceEntityResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class RunMapReduceInstanceArg(_message.Message):
    __slots__ = ("map_reduce_instance",)
    MAP_REDUCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    map_reduce_instance: MapReduceInstance
    def __init__(self, map_reduce_instance: _Optional[_Union[MapReduceInstance, _Mapping]] = ...) -> None: ...

class RunMapReduceInstanceResult(_message.Message):
    __slots__ = ("error", "map_reduce_instance_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MAP_REDUCE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    map_reduce_instance_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., map_reduce_instance_id: _Optional[int] = ...) -> None: ...

class GetMapReduceInstanceArg(_message.Message):
    __slots__ = ("map_reduce_info_id", "map_reduce_instance_id", "start_time_filter", "end_time_filter", "last_num_instances", "status", "include_details", "start_offset", "page_size")
    class TimeRangeFilter(_message.Message):
        __slots__ = ("min_timestamp", "max_timestamp")
        MIN_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MAX_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        min_timestamp: int
        max_timestamp: int
        def __init__(self, min_timestamp: _Optional[int] = ..., max_timestamp: _Optional[int] = ...) -> None: ...
    MAP_REDUCE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_REDUCE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    LAST_NUM_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    map_reduce_info_id: int
    map_reduce_instance_id: int
    start_time_filter: GetMapReduceInstanceArg.TimeRangeFilter
    end_time_filter: GetMapReduceInstanceArg.TimeRangeFilter
    last_num_instances: int
    status: MapReduceInstance.RunInfo.Status
    include_details: bool
    start_offset: int
    page_size: int
    def __init__(self, map_reduce_info_id: _Optional[int] = ..., map_reduce_instance_id: _Optional[int] = ..., start_time_filter: _Optional[_Union[GetMapReduceInstanceArg.TimeRangeFilter, _Mapping]] = ..., end_time_filter: _Optional[_Union[GetMapReduceInstanceArg.TimeRangeFilter, _Mapping]] = ..., last_num_instances: _Optional[int] = ..., status: _Optional[_Union[MapReduceInstance.RunInfo.Status, str]] = ..., include_details: bool = ..., start_offset: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class GetMapReduceInstanceResult(_message.Message):
    __slots__ = ("error", "results_maybe_stale", "map_reduce_instance", "total_num_results")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_MAYBE_STALE_FIELD_NUMBER: _ClassVar[int]
    MAP_REDUCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    results_maybe_stale: bool
    map_reduce_instance: _containers.RepeatedCompositeFieldContainer[MapReduceInstance]
    total_num_results: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., results_maybe_stale: bool = ..., map_reduce_instance: _Optional[_Iterable[_Union[MapReduceInstance, _Mapping]]] = ..., total_num_results: _Optional[int] = ...) -> None: ...

class KillMapReduceInstanceArg(_message.Message):
    __slots__ = ("map_reduce_instance_id",)
    MAP_REDUCE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    map_reduce_instance_id: int
    def __init__(self, map_reduce_instance_id: _Optional[int] = ...) -> None: ...

class KillMapReduceInstanceResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class AnalyseJarArg(_message.Message):
    __slots__ = ("jar_name", "jar_path", "save_entities", "jar_relative_path")
    JAR_NAME_FIELD_NUMBER: _ClassVar[int]
    JAR_PATH_FIELD_NUMBER: _ClassVar[int]
    SAVE_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    JAR_RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    jar_name: str
    jar_path: str
    save_entities: bool
    jar_relative_path: str
    def __init__(self, jar_name: _Optional[str] = ..., jar_path: _Optional[str] = ..., save_entities: bool = ..., jar_relative_path: _Optional[str] = ...) -> None: ...

class AnalyseJarResult(_message.Message):
    __slots__ = ("error", "mappers", "reducers")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MAPPERS_FIELD_NUMBER: _ClassVar[int]
    REDUCERS_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    mappers: _containers.RepeatedScalarFieldContainer[str]
    reducers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mappers: _Optional[_Iterable[str]] = ..., reducers: _Optional[_Iterable[str]] = ...) -> None: ...

class MRConfigProto(_message.Message):
    __slots__ = ("mr_jar_repo_dir",)
    MR_JAR_REPO_DIR_FIELD_NUMBER: _ClassVar[int]
    mr_jar_repo_dir: str
    def __init__(self, mr_jar_repo_dir: _Optional[str] = ...) -> None: ...

class Pattern(_message.Message):
    __slots__ = ("name", "value", "type", "is_system_defined")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kRegular: _ClassVar[Pattern.Type]
        kDate: _ClassVar[Pattern.Type]
        kSsn: _ClassVar[Pattern.Type]
    kRegular: Pattern.Type
    kDate: Pattern.Type
    kSsn: Pattern.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_DEFINED_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    type: Pattern.Type
    is_system_defined: bool
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[_Union[Pattern.Type, str]] = ..., is_system_defined: bool = ...) -> None: ...

class MapReduceAuxData(_message.Message):
    __slots__ = ("pattern_vec",)
    PATTERN_VEC_FIELD_NUMBER: _ClassVar[int]
    pattern_vec: _containers.RepeatedCompositeFieldContainer[Pattern]
    def __init__(self, pattern_vec: _Optional[_Iterable[_Union[Pattern, _Mapping]]] = ...) -> None: ...

class GetMapReduceAuxDataArg(_message.Message):
    __slots__ = ("map_reduce_info_id", "data_type", "pattern_name")
    MAP_REDUCE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_NAME_FIELD_NUMBER: _ClassVar[int]
    map_reduce_info_id: int
    data_type: MapReduceAuxDataType
    pattern_name: str
    def __init__(self, map_reduce_info_id: _Optional[int] = ..., data_type: _Optional[_Union[MapReduceAuxDataType, str]] = ..., pattern_name: _Optional[str] = ...) -> None: ...

class GetMapReduceAuxDataResult(_message.Message):
    __slots__ = ("error", "pattern_vec")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PATTERN_VEC_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    pattern_vec: _containers.RepeatedCompositeFieldContainer[Pattern]
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., pattern_vec: _Optional[_Iterable[_Union[Pattern, _Mapping]]] = ...) -> None: ...

class SaveMapReduceAuxDataArg(_message.Message):
    __slots__ = ("map_reduce_info_id", "data_type", "pattern")
    MAP_REDUCE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    map_reduce_info_id: int
    data_type: MapReduceAuxDataType
    pattern: Pattern
    def __init__(self, map_reduce_info_id: _Optional[int] = ..., data_type: _Optional[_Union[MapReduceAuxDataType, str]] = ..., pattern: _Optional[_Union[Pattern, _Mapping]] = ...) -> None: ...

class SaveMapReduceAuxDataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class DeleteMapReduceAuxDataArg(_message.Message):
    __slots__ = ("map_reduce_info_id", "data_type", "pattern_name")
    MAP_REDUCE_INFO_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_NAME_FIELD_NUMBER: _ClassVar[int]
    map_reduce_info_id: int
    data_type: MapReduceAuxDataType
    pattern_name: str
    def __init__(self, map_reduce_info_id: _Optional[int] = ..., data_type: _Optional[_Union[MapReduceAuxDataType, str]] = ..., pattern_name: _Optional[str] = ...) -> None: ...

class DeleteMapReduceAuxDataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...
