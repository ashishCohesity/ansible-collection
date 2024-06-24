from magneto.base import enums_pb2 as _enums_pb2
from util.base import universal_id_pb2 as _universal_id_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduledBackupEventSpecProto(_message.Message):
    __slots__ = ("uid", "spec_uid", "backup_type", "ideal_start_time_secs")
    UID_FIELD_NUMBER: _ClassVar[int]
    SPEC_UID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDEAL_START_TIME_SECS_FIELD_NUMBER: _ClassVar[int]
    uid: _universal_id_pb2.UniversalIdProto
    spec_uid: _universal_id_pb2.UniversalIdProto
    backup_type: _enums_pb2.ScheduledBackupType.Type
    ideal_start_time_secs: int
    def __init__(self, uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., spec_uid: _Optional[_Union[_universal_id_pb2.UniversalIdProto, _Mapping]] = ..., backup_type: _Optional[_Union[_enums_pb2.ScheduledBackupType.Type, str]] = ..., ideal_start_time_secs: _Optional[int] = ...) -> None: ...
