from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmailRequestProto(_message.Message):
    __slots__ = ("smtp_server", "smtp_port", "smtp_username", "smtp_password", "admin_email_address", "recipient_email_list", "notification_subject", "notification_body", "use_smtps", "cc_email_list", "send_mail_with_plain_text")
    SMTP_SERVER_FIELD_NUMBER: _ClassVar[int]
    SMTP_PORT_FIELD_NUMBER: _ClassVar[int]
    SMTP_USERNAME_FIELD_NUMBER: _ClassVar[int]
    SMTP_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ADMIN_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_EMAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_BODY_FIELD_NUMBER: _ClassVar[int]
    USE_SMTPS_FIELD_NUMBER: _ClassVar[int]
    CC_EMAIL_LIST_FIELD_NUMBER: _ClassVar[int]
    SEND_MAIL_WITH_PLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    admin_email_address: str
    recipient_email_list: _containers.RepeatedScalarFieldContainer[str]
    notification_subject: bytes
    notification_body: bytes
    use_smtps: bool
    cc_email_list: _containers.RepeatedScalarFieldContainer[str]
    send_mail_with_plain_text: bool
    def __init__(self, smtp_server: _Optional[str] = ..., smtp_port: _Optional[int] = ..., smtp_username: _Optional[str] = ..., smtp_password: _Optional[str] = ..., admin_email_address: _Optional[str] = ..., recipient_email_list: _Optional[_Iterable[str]] = ..., notification_subject: _Optional[bytes] = ..., notification_body: _Optional[bytes] = ..., use_smtps: bool = ..., cc_email_list: _Optional[_Iterable[str]] = ..., send_mail_with_plain_text: bool = ...) -> None: ...

class SnmpNotifRequestProto(_message.Message):
    __slots__ = ("snmp_version", "engine_id", "trap_receiver", "trap_oid", "mib_object")
    class MibObject(_message.Message):
        __slots__ = ("obj_name", "obj_type", "obj_value")
        OBJ_NAME_FIELD_NUMBER: _ClassVar[int]
        OBJ_TYPE_FIELD_NUMBER: _ClassVar[int]
        OBJ_VALUE_FIELD_NUMBER: _ClassVar[int]
        obj_name: str
        obj_type: str
        obj_value: str
        def __init__(self, obj_name: _Optional[str] = ..., obj_type: _Optional[str] = ..., obj_value: _Optional[str] = ...) -> None: ...
    SNMP_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    TRAP_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    TRAP_OID_FIELD_NUMBER: _ClassVar[int]
    MIB_OBJECT_FIELD_NUMBER: _ClassVar[int]
    snmp_version: int
    engine_id: str
    trap_receiver: str
    trap_oid: str
    mib_object: _containers.RepeatedCompositeFieldContainer[SnmpNotifRequestProto.MibObject]
    def __init__(self, snmp_version: _Optional[int] = ..., engine_id: _Optional[str] = ..., trap_receiver: _Optional[str] = ..., trap_oid: _Optional[str] = ..., mib_object: _Optional[_Iterable[_Union[SnmpNotifRequestProto.MibObject, _Mapping]]] = ...) -> None: ...
