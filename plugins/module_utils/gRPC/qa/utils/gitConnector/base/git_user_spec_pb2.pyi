from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GitUser(_message.Message):
    __slots__ = ("cohesity_username", "git_base_dir", "git_toolchain_dir", "git_local_workspace_path", "artifact_download_path")
    COHESITY_USERNAME_FIELD_NUMBER: _ClassVar[int]
    GIT_BASE_DIR_FIELD_NUMBER: _ClassVar[int]
    GIT_TOOLCHAIN_DIR_FIELD_NUMBER: _ClassVar[int]
    GIT_LOCAL_WORKSPACE_PATH_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_DOWNLOAD_PATH_FIELD_NUMBER: _ClassVar[int]
    cohesity_username: str
    git_base_dir: str
    git_toolchain_dir: str
    git_local_workspace_path: str
    artifact_download_path: str
    def __init__(self, cohesity_username: _Optional[str] = ..., git_base_dir: _Optional[str] = ..., git_toolchain_dir: _Optional[str] = ..., git_local_workspace_path: _Optional[str] = ..., artifact_download_path: _Optional[str] = ...) -> None: ...

class GitSyncData(_message.Message):
    __slots__ = ("git_base_branch", "git_base_sha1", "git_toolchain_branch", "git_toolchain_sha1")
    GIT_BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    GIT_BASE_SHA1_FIELD_NUMBER: _ClassVar[int]
    GIT_TOOLCHAIN_BRANCH_FIELD_NUMBER: _ClassVar[int]
    GIT_TOOLCHAIN_SHA1_FIELD_NUMBER: _ClassVar[int]
    git_base_branch: str
    git_base_sha1: str
    git_toolchain_branch: str
    git_toolchain_sha1: str
    def __init__(self, git_base_branch: _Optional[str] = ..., git_base_sha1: _Optional[str] = ..., git_toolchain_branch: _Optional[str] = ..., git_toolchain_sha1: _Optional[str] = ...) -> None: ...
