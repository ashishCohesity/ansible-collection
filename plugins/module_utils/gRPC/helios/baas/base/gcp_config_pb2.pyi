from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigProto(_message.Message):
    __slots__ = ("cluster_name_prefix", "project_id", "initial_num_vms", "encrypted_key", "cloud_ops_email_vec")
    CLUSTER_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_NUM_VMS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
    CLOUD_OPS_EMAIL_VEC_FIELD_NUMBER: _ClassVar[int]
    cluster_name_prefix: str
    project_id: str
    initial_num_vms: int
    encrypted_key: str
    cloud_ops_email_vec: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cluster_name_prefix: _Optional[str] = ..., project_id: _Optional[str] = ..., initial_num_vms: _Optional[int] = ..., encrypted_key: _Optional[str] = ..., cloud_ops_email_vec: _Optional[_Iterable[str]] = ...) -> None: ...
