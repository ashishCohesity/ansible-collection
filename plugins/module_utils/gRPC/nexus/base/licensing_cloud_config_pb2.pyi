from nexus.base import baas_kafka_reader_pb2 as _baas_kafka_reader_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KafkaAirflowAccountStatsEvent(_message.Message):
    __slots__ = ("header", "account_id")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    header: _baas_kafka_reader_pb2.KafkaEventAirflowHeader
    account_id: str
    def __init__(self, header: _Optional[_Union[_baas_kafka_reader_pb2.KafkaEventAirflowHeader, _Mapping]] = ..., account_id: _Optional[str] = ...) -> None: ...
