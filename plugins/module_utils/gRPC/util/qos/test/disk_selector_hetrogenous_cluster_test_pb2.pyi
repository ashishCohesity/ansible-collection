from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiskSelectorHetrogenousClusterProto(_message.Message):
    __slots__ = ("test_config", "cluster")
    class DiskSelectorHetrogenousTestConfig(_message.Message):
        __slots__ = ("test_iteration", "iteration_to_report", "data_size_per_io", "num_disk_to_return", "max_replica_failure", "max_entity_failure")
        TEST_ITERATION_FIELD_NUMBER: _ClassVar[int]
        ITERATION_TO_REPORT_FIELD_NUMBER: _ClassVar[int]
        DATA_SIZE_PER_IO_FIELD_NUMBER: _ClassVar[int]
        NUM_DISK_TO_RETURN_FIELD_NUMBER: _ClassVar[int]
        MAX_REPLICA_FAILURE_FIELD_NUMBER: _ClassVar[int]
        MAX_ENTITY_FAILURE_FIELD_NUMBER: _ClassVar[int]
        test_iteration: int
        iteration_to_report: int
        data_size_per_io: str
        num_disk_to_return: int
        max_replica_failure: int
        max_entity_failure: int
        def __init__(self, test_iteration: _Optional[int] = ..., iteration_to_report: _Optional[int] = ..., data_size_per_io: _Optional[str] = ..., num_disk_to_return: _Optional[int] = ..., max_replica_failure: _Optional[int] = ..., max_entity_failure: _Optional[int] = ...) -> None: ...
    class DiskSelectorHetrogenousNode(_message.Message):
        __slots__ = ("num_disk", "disk_size")
        NUM_DISK_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        num_disk: int
        disk_size: str
        def __init__(self, num_disk: _Optional[int] = ..., disk_size: _Optional[str] = ...) -> None: ...
    TEST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    test_config: DiskSelectorHetrogenousClusterProto.DiskSelectorHetrogenousTestConfig
    cluster: _containers.RepeatedCompositeFieldContainer[DiskSelectorHetrogenousClusterProto.DiskSelectorHetrogenousNode]
    def __init__(self, test_config: _Optional[_Union[DiskSelectorHetrogenousClusterProto.DiskSelectorHetrogenousTestConfig, _Mapping]] = ..., cluster: _Optional[_Iterable[_Union[DiskSelectorHetrogenousClusterProto.DiskSelectorHetrogenousNode, _Mapping]]] = ...) -> None: ...
