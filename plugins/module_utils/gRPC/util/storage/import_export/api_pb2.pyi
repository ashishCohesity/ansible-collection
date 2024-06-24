from util.storage import error_pb2 as _error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ExportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    kSuccess: _ClassVar[ExportStatus]
    kFailed: _ClassVar[ExportStatus]
kSuccess: ExportStatus
kFailed: ExportStatus
