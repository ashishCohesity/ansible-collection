from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NodeRebootInfoProto(_message.Message):
    __slots__ = ("gandalf_key_name", "node_id", "yoda_session_id", "dstate_thread_id_vec", "zombie_thread_id_vec")
    GANDALF_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    YODA_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DSTATE_THREAD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    ZOMBIE_THREAD_ID_VEC_FIELD_NUMBER: _ClassVar[int]
    gandalf_key_name: str
    node_id: int
    yoda_session_id: int
    dstate_thread_id_vec: _containers.RepeatedScalarFieldContainer[int]
    zombie_thread_id_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, gandalf_key_name: _Optional[str] = ..., node_id: _Optional[int] = ..., yoda_session_id: _Optional[int] = ..., dstate_thread_id_vec: _Optional[_Iterable[int]] = ..., zombie_thread_id_vec: _Optional[_Iterable[int]] = ...) -> None: ...
