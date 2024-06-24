from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ETLogBackupProto(_message.Message):
    __slots__ = ("srt1", "srt2", "srt3", "cluster_id", "cluster_incarnation_id", "cluster_vips", "domain")
    SRT1_FIELD_NUMBER: _ClassVar[int]
    SRT2_FIELD_NUMBER: _ClassVar[int]
    SRT3_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_INCARNATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_VIPS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    srt1: str
    srt2: str
    srt3: str
    cluster_id: str
    cluster_incarnation_id: str
    cluster_vips: str
    domain: str
    def __init__(self, srt1: _Optional[str] = ..., srt2: _Optional[str] = ..., srt3: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_incarnation_id: _Optional[str] = ..., cluster_vips: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...
