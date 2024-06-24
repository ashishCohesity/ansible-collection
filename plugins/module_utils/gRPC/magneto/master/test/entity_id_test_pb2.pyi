from magneto.base import entity_pb2 as _entity_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import python_message as _python_message
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEntityIdProtoSubMessage(_message.Message):
    __slots__ = ("entity", "repeated_entity")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    repeated_entity: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., repeated_entity: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ...) -> None: ...

class TestEntityIdProto(_message.Message):
    __slots__ = ("entity", "repeated_entity", "sub_message", "repeated_sub_message")
    Extensions: _python_message._ExtensionDict
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    repeated_entity: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    sub_message: TestEntityIdProtoSubMessage
    repeated_sub_message: _containers.RepeatedCompositeFieldContainer[TestEntityIdProtoSubMessage]
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., repeated_entity: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., sub_message: _Optional[_Union[TestEntityIdProtoSubMessage, _Mapping]] = ..., repeated_sub_message: _Optional[_Iterable[_Union[TestEntityIdProtoSubMessage, _Mapping]]] = ...) -> None: ...

class TestEntityIdProtoExtension(_message.Message):
    __slots__ = ("entity", "repeated_entity", "sub_message", "repeated_sub_message")
    TEST_ENTITY_ID_EXT_FIELD_NUMBER: _ClassVar[int]
    test_entity_id_ext: _descriptor.FieldDescriptor
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    REPEATED_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPEATED_SUB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    entity: _entity_pb2.EntityProto
    repeated_entity: _containers.RepeatedCompositeFieldContainer[_entity_pb2.EntityProto]
    sub_message: TestEntityIdProtoSubMessage
    repeated_sub_message: _containers.RepeatedCompositeFieldContainer[TestEntityIdProtoSubMessage]
    def __init__(self, entity: _Optional[_Union[_entity_pb2.EntityProto, _Mapping]] = ..., repeated_entity: _Optional[_Iterable[_Union[_entity_pb2.EntityProto, _Mapping]]] = ..., sub_message: _Optional[_Union[TestEntityIdProtoSubMessage, _Mapping]] = ..., repeated_sub_message: _Optional[_Iterable[_Union[TestEntityIdProtoSubMessage, _Mapping]]] = ...) -> None: ...
