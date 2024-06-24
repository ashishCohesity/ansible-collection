from bridge.audit_log import audit_log_pb2 as _audit_log_pb2
from bridge.smb_portal import smb_portal_metadata_pb2 as _smb_portal_metadata_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilerEventRecord(_message.Message):
    __slots__ = ("audit_record", "smb_entity_metadata_proto")
    AUDIT_RECORD_FIELD_NUMBER: _ClassVar[int]
    SMB_ENTITY_METADATA_PROTO_FIELD_NUMBER: _ClassVar[int]
    audit_record: _audit_log_pb2.AuditRecord
    smb_entity_metadata_proto: _smb_portal_metadata_pb2.SmbEntityMetadataProto
    def __init__(self, audit_record: _Optional[_Union[_audit_log_pb2.AuditRecord, _Mapping]] = ..., smb_entity_metadata_proto: _Optional[_Union[_smb_portal_metadata_pb2.SmbEntityMetadataProto, _Mapping]] = ...) -> None: ...
