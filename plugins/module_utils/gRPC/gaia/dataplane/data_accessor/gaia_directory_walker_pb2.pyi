from magneto.directory_walker import directory_walker_pb2 as _directory_walker_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GaiaOneDriveDirectoryWalkerEntityMetadata(_message.Message):
    __slots__ = ("human_readable_path",)
    GAIA_ONE_DRIVE_ENTITY_MD_FIELD_NUMBER: _ClassVar[int]
    gaia_one_drive_entity_md: _descriptor.FieldDescriptor
    HUMAN_READABLE_PATH_FIELD_NUMBER: _ClassVar[int]
    human_readable_path: str
    def __init__(self, human_readable_path: _Optional[str] = ...) -> None: ...
