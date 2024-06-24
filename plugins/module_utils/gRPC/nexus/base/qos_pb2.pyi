from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QosProto(_message.Message):
    __slots__ = ("gandalf_key", "qos_enabled", "profile_vec", "attachment_vec", "version")
    class Profile(_message.Message):
        __slots__ = ("name", "priority", "direction", "port_protocols")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        PORT_PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
        name: str
        priority: int
        direction: str
        port_protocols: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., priority: _Optional[int] = ..., direction: _Optional[str] = ..., port_protocols: _Optional[_Iterable[str]] = ...) -> None: ...
    class Attachment(_message.Message):
        __slots__ = ("profile_name", "ipset_names", "action", "action_value", "description")
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Mark: _ClassVar[QosProto.Attachment.Action]
            Queue: _ClassVar[QosProto.Attachment.Action]
        Mark: QosProto.Attachment.Action
        Queue: QosProto.Attachment.Action
        PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
        IPSET_NAMES_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ACTION_VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        profile_name: str
        ipset_names: _containers.RepeatedScalarFieldContainer[str]
        action: QosProto.Attachment.Action
        action_value: int
        description: str
        def __init__(self, profile_name: _Optional[str] = ..., ipset_names: _Optional[_Iterable[str]] = ..., action: _Optional[_Union[QosProto.Attachment.Action, str]] = ..., action_value: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...
    GANDALF_KEY_FIELD_NUMBER: _ClassVar[int]
    QOS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROFILE_VEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_VEC_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    gandalf_key: str
    qos_enabled: bool
    profile_vec: _containers.RepeatedCompositeFieldContainer[QosProto.Profile]
    attachment_vec: _containers.RepeatedCompositeFieldContainer[QosProto.Attachment]
    version: int
    def __init__(self, gandalf_key: _Optional[str] = ..., qos_enabled: bool = ..., profile_vec: _Optional[_Iterable[_Union[QosProto.Profile, _Mapping]]] = ..., attachment_vec: _Optional[_Iterable[_Union[QosProto.Attachment, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...
