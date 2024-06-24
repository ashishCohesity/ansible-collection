from magneto.slave.stub import bridge_updates_pb2 as _bridge_updates_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ViewActionUpdateArg(_message.Message):
    __slots__ = ()
    VIEW_ACTION_UPDATE_ARG_FIELD_NUMBER: _ClassVar[int]
    view_action_update_arg: _descriptor.FieldDescriptor
    def __init__(self) -> None: ...
