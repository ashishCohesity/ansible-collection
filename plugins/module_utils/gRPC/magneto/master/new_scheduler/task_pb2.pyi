from magneto.base import gatekeeper_pb2 as _gatekeeper_pb2
from magneto.base import entity_pb2 as _entity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[TaskProto.Type]
        kBackup: _ClassVar[TaskProto.Type]
        kRestore: _ClassVar[TaskProto.Type]
        kCopySubTask: _ClassVar[TaskProto.Type]
    kInvalid: TaskProto.Type
    kBackup: TaskProto.Type
    kRestore: TaskProto.Type
    kCopySubTask: TaskProto.Type
    def __init__(self) -> None: ...

class RequestorProto(_message.Message):
    __slots__ = ()
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        kInvalid: _ClassVar[RequestorProto.Type]
        kMagnetoMaster: _ClassVar[RequestorProto.Type]
        kMagnetoSlave: _ClassVar[RequestorProto.Type]
    kInvalid: RequestorProto.Type
    kMagnetoMaster: RequestorProto.Type
    kMagnetoSlave: RequestorProto.Type
    def __init__(self) -> None: ...

class RequestAttachmentProto(_message.Message):
    __slots__ = ("gk_task", "requestor_type", "task_type", "reserved_entity_vec")
    GK_TASK_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ENTITY_VEC_FIELD_NUMBER: _ClassVar[int]
    gk_task: _gatekeeper_pb2.Task
    requestor_type: RequestorProto.Type
    task_type: TaskProto.Type
    reserved_entity_vec: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, gk_task: _Optional[_Union[_gatekeeper_pb2.Task, _Mapping]] = ..., requestor_type: _Optional[_Union[RequestorProto.Type, str]] = ..., task_type: _Optional[_Union[TaskProto.Type, str]] = ..., reserved_entity_vec: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...
