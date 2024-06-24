from alerts.base import alert_pb2 as _alert_pb2
from alerts.base import error_pb2 as _error_pb2
from open_util.net import protorpc_pb2 as _protorpc_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RaiseAlertsArg(_message.Message):
    __slots__ = ("alert_list",)
    ALERT_LIST_FIELD_NUMBER: _ClassVar[int]
    alert_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertProto]
    def __init__(self, alert_list: _Optional[_Iterable[_Union[_alert_pb2.AlertProto, _Mapping]]] = ...) -> None: ...

class RaiseAlertsResult(_message.Message):
    __slots__ = ("error_list", "alert_id_list")
    ERROR_LIST_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    error_list: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    alert_id_list: _containers.RepeatedCompositeFieldContainer[_alert_pb2.AlertIdProto]
    def __init__(self, error_list: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., alert_id_list: _Optional[_Iterable[_Union[_alert_pb2.AlertIdProto, _Mapping]]] = ...) -> None: ...

class GetMasterInfoArg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMasterInfoResult(_message.Message):
    __slots__ = ("error", "ip", "port")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.ErrorProto
    ip: str
    port: int
    def __init__(self, error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
