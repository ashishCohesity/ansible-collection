from magneto.base import sub_task_pb2 as _sub_task_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SystemSubTaskInfo(_message.Message):
    __slots__ = ("system_backup_image_unc_path", "system_backup_image_nfs_path")
    SYSTEM_SUB_TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    system_sub_task_info: _descriptor.FieldDescriptor
    SYSTEM_BACKUP_IMAGE_UNC_PATH_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_BACKUP_IMAGE_NFS_PATH_FIELD_NUMBER: _ClassVar[int]
    system_backup_image_unc_path: str
    system_backup_image_nfs_path: str
    def __init__(self, system_backup_image_unc_path: _Optional[str] = ..., system_backup_image_nfs_path: _Optional[str] = ...) -> None: ...
