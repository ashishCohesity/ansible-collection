from atom.base import vmware_pb2 as _vmware_pb2
from atom.base import mongodb_pb2 as _mongodb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kUnknown: _ClassVar[SourceType]
    kVMware: _ClassVar[SourceType]
    kMongoDB: _ClassVar[SourceType]
kUnknown: SourceType
kVMware: SourceType
kMongoDB: SourceType

class EntityID(_message.Message):
    __slots__ = ("source_type", "cohesity_entity_id", "vmware_entity_id", "mongodb_entity_id")
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COHESITY_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    MONGODB_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    source_type: SourceType
    cohesity_entity_id: int
    vmware_entity_id: _vmware_pb2.VMwareEntityID
    mongodb_entity_id: _mongodb_pb2.MongoDBEntityID
    def __init__(self, source_type: _Optional[_Union[SourceType, str]] = ..., cohesity_entity_id: _Optional[int] = ..., vmware_entity_id: _Optional[_Union[_vmware_pb2.VMwareEntityID, _Mapping]] = ..., mongodb_entity_id: _Optional[_Union[_mongodb_pb2.MongoDBEntityID, _Mapping]] = ...) -> None: ...

class EntityMiscData(_message.Message):
    __slots__ = ("vmware_vm_data",)
    class VMwareVMData(_message.Message):
        __slots__ = ("virtual_disk_entity_id_vec",)
        VIRTUAL_DISK_ENTITY_ID_VEC_FIELD_NUMBER: _ClassVar[int]
        virtual_disk_entity_id_vec: _containers.RepeatedCompositeFieldContainer[EntityID]
        def __init__(self, virtual_disk_entity_id_vec: _Optional[_Iterable[_Union[EntityID, _Mapping]]] = ...) -> None: ...
    VMWARE_VM_DATA_FIELD_NUMBER: _ClassVar[int]
    vmware_vm_data: EntityMiscData.VMwareVMData
    def __init__(self, vmware_vm_data: _Optional[_Union[EntityMiscData.VMwareVMData, _Mapping]] = ...) -> None: ...
