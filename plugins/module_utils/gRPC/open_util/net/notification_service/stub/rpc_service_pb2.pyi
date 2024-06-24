from open_util.net.notification_service import notification_service_pb2 as _notification_service_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendNotificationArg(_message.Message):
    __slots__ = ("entity_id",)
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_id: _notification_service_pb2.EntityIdProto
    def __init__(self, entity_id: _Optional[_Union[_notification_service_pb2.EntityIdProto, _Mapping]] = ...) -> None: ...

class SendNotificationResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
