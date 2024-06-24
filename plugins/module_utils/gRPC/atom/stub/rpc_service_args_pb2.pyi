from atom.base import error_pb2 as _error_pb2
from atom.base import entity_pb2 as _entity_pb2
from atom.base import event_pb2 as _event_pb2
from atom.stub import vmware_args_pb2 as _vmware_args_pb2
from atom.stub import mongodb_args_pb2 as _mongodb_args_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllocateNodeArg(_message.Message):
    __slots__ = ("entity_id", "cohesity_id")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    cohesity_id: str
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., cohesity_id: _Optional[str] = ...) -> None: ...

class AllocateNodeResult(_message.Message):
    __slots__ = ("error", "node_address", "cohesity_entity_id", "vmware_vmsd_file_path", "node_constituent_id")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_VMSD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    NODE_CONSTITUENT_ID_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    node_address: str
    cohesity_entity_id: int
    vmware_vmsd_file_path: str
    node_constituent_id: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., node_address: _Optional[str] = ..., cohesity_entity_id: _Optional[int] = ..., vmware_vmsd_file_path: _Optional[str] = ..., node_constituent_id: _Optional[int] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("timestamp", "data", "vmware_data", "mongodb_data")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VMWARE_DATA_FIELD_NUMBER: _ClassVar[int]
    MONGODB_DATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    data: bytes
    vmware_data: _vmware_args_pb2.VMwareData
    mongodb_data: _mongodb_args_pb2.MongoDBData
    def __init__(self, timestamp: _Optional[int] = ..., data: _Optional[bytes] = ..., vmware_data: _Optional[_Union[_vmware_args_pb2.VMwareData, _Mapping]] = ..., mongodb_data: _Optional[_Union[_mongodb_args_pb2.MongoDBData, _Mapping]] = ...) -> None: ...

class WriteDataArg(_message.Message):
    __slots__ = ("entity_id", "data", "mongodb_additional_info")
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    data: Data
    mongodb_additional_info: _mongodb_args_pb2.MongoDBAdditionalInfo
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ..., mongodb_additional_info: _Optional[_Union[_mongodb_args_pb2.MongoDBAdditionalInfo, _Mapping]] = ...) -> None: ...

class WriteDataResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class GetLatestDataEventArg(_message.Message):
    __slots__ = ("entity_id",)
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: _entity_pb2.EntityID
    def __init__(self, entity_id: _Optional[_Union[_entity_pb2.EntityID, _Mapping]] = ...) -> None: ...

class GetLatestDataEventResult(_message.Message):
    __slots__ = ("data_event", "error", "mongodb_additional_info")
    DATA_EVENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    data_event: _event_pb2.DataEvent
    error: _error_pb2.ErrorProto
    mongodb_additional_info: _mongodb_args_pb2.MongoDBAdditionalInfo
    def __init__(self, data_event: _Optional[_Union[_event_pb2.DataEvent, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., mongodb_additional_info: _Optional[_Union[_mongodb_args_pb2.MongoDBAdditionalInfo, _Mapping]] = ...) -> None: ...
