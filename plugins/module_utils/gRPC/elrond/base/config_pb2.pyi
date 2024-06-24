from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ElrondConfigProto(_message.Message):
    __slots__ = ("gandalf_master_lock_name", "master_status_url", "elrond_access_model_key", "elrond_access_model_column_key", "elrond_transition_model_column_key")
    GANDALF_MASTER_LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    ELROND_ACCESS_MODEL_KEY_FIELD_NUMBER: _ClassVar[int]
    ELROND_ACCESS_MODEL_COLUMN_KEY_FIELD_NUMBER: _ClassVar[int]
    ELROND_TRANSITION_MODEL_COLUMN_KEY_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_lock_name: str
    master_status_url: str
    elrond_access_model_key: str
    elrond_access_model_column_key: str
    elrond_transition_model_column_key: str
    def __init__(self, gandalf_master_lock_name: _Optional[str] = ..., master_status_url: _Optional[str] = ..., elrond_access_model_key: _Optional[str] = ..., elrond_access_model_column_key: _Optional[str] = ..., elrond_transition_model_column_key: _Optional[str] = ...) -> None: ...
