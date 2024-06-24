from nexus.cloud.base import credentials_pb2 as _credentials_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityCommonInfo(_message.Message):
    __slots__ = ("name", "id", "physical_entity_id", "restore_task_id", "subscription_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    physical_entity_id: int
    restore_task_id: int
    subscription_type: _credentials_pb2.SubscriptionType
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., physical_entity_id: _Optional[int] = ..., restore_task_id: _Optional[int] = ..., subscription_type: _Optional[_Union[_credentials_pb2.SubscriptionType, str]] = ...) -> None: ...
