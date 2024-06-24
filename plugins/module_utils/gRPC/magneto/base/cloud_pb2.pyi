from magneto.agents.base import agent_pb2 as _agent_pb2
from magneto.base import disk_pb2 as _disk_pb2
from yoda.base import volume_info_pb2 as _volume_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DRToCloudVMInfo(_message.Message):
    __slots__ = ("host_info", "volume_name_map")
    HOST_INFO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_NAME_MAP_FIELD_NUMBER: _ClassVar[int]
    host_info: _agent_pb2.HostInfo
    volume_name_map: _volume_info_pb2.VolumeNameMap
    def __init__(self, host_info: _Optional[_Union[_agent_pb2.HostInfo, _Mapping]] = ..., volume_name_map: _Optional[_Union[_volume_info_pb2.VolumeNameMap, _Mapping]] = ...) -> None: ...

class ChainedDiskMappingInfo(_message.Message):
    __slots__ = ("head_filename", "encoded_filepath_map")
    class EncodedFilepathMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HEAD_FILENAME_FIELD_NUMBER: _ClassVar[int]
    ENCODED_FILEPATH_MAP_FIELD_NUMBER: _ClassVar[int]
    head_filename: str
    encoded_filepath_map: _containers.ScalarMap[str, str]
    def __init__(self, head_filename: _Optional[str] = ..., encoded_filepath_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ChainedLogicalDiskMapping(_message.Message):
    __slots__ = ("logical_to_physical_mapping_vec",)
    class LogicalToPhysicalMapping(_message.Message):
        __slots__ = ("head_file_path", "logical_disk_area_list_map", "logical_disk_size")
        class LogicalDiskAreaListMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _disk_pb2.DiskAreaListProto
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_disk_pb2.DiskAreaListProto, _Mapping]] = ...) -> None: ...
        HEAD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_DISK_AREA_LIST_MAP_FIELD_NUMBER: _ClassVar[int]
        LOGICAL_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        head_file_path: str
        logical_disk_area_list_map: _containers.MessageMap[str, _disk_pb2.DiskAreaListProto]
        logical_disk_size: int
        def __init__(self, head_file_path: _Optional[str] = ..., logical_disk_area_list_map: _Optional[_Mapping[str, _disk_pb2.DiskAreaListProto]] = ..., logical_disk_size: _Optional[int] = ...) -> None: ...
    LOGICAL_TO_PHYSICAL_MAPPING_VEC_FIELD_NUMBER: _ClassVar[int]
    logical_to_physical_mapping_vec: _containers.RepeatedCompositeFieldContainer[ChainedLogicalDiskMapping.LogicalToPhysicalMapping]
    def __init__(self, logical_to_physical_mapping_vec: _Optional[_Iterable[_Union[ChainedLogicalDiskMapping.LogicalToPhysicalMapping, _Mapping]]] = ...) -> None: ...
