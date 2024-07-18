# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from bridge.ddw_portal.stub import rpc_service_args_pb2 as bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in bridge/ddw_portal/stub/rpc_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LookupFileHandle = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/LookupFileHandle',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.LookupFileHandleArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.LookupFileHandleResult.FromString,
                _registered_method=True)
        self.GetFileSize = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/GetFileSize',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileSizeArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileSizeResult.FromString,
                _registered_method=True)
        self.SetFileSize = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/SetFileSize',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.SetFileSizeArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.SetFileSizeResult.FromString,
                _registered_method=True)
        self.GetFileStat = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/GetFileStat',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileStatArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileStatResult.FromString,
                _registered_method=True)
        self.Read = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/Read',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadResult.FromString,
                _registered_method=True)
        self.Write = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/Write',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.WriteArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.WriteResult.FromString,
                _registered_method=True)
        self.ReadDir = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/ReadDir',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadDirArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadDirResult.FromString,
                _registered_method=True)
        self.CloneDirectory = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/CloneDirectory',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryResult.FromString,
                _registered_method=True)
        self.CreateFile = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/CreateFile',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirResult.FromString,
                _registered_method=True)
        self.CreateDirectory = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/CreateDirectory',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirResult.FromString,
                _registered_method=True)
        self.CreateEntities = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/CreateEntities',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateEntitiesArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateEntitiesResult.FromString,
                _registered_method=True)
        self.RemoveFile = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/RemoveFile',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RemoveFileArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RemoveFileResult.FromString,
                _registered_method=True)
        self.Rename = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/Rename',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RenameArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RenameResult.FromString,
                _registered_method=True)
        self.CloneDirRecursive = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/CloneDirRecursive',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryResult.FromString,
                _registered_method=True)
        self.GetInodeMetadata = channel.unary_unary(
                '/cohesity.bridge.ddw_portal.stub.RpcService/GetInodeMetadata',
                request_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetInodeMetadataArg.SerializeToString,
                response_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetInodeMetadataResult.FromString,
                _registered_method=True)


class RpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LookupFileHandle(self, request, context):
        """Call to lookup a file handle.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileSize(self, request, context):
        """Call to get the file size.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFileSize(self, request, context):
        """Call to set the file size.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFileStat(self, request, context):
        """Call to get the file stat information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Call to read data from a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Call to write data to a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadDir(self, request, context):
        """Call to read entries of a directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloneDirectory(self, request, context):
        """Call to clone a directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Call to create a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDirectory(self, request, context):
        """Call to create a directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEntities(self, request, context):
        """Call to create multiple entities in a directory.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFile(self, request, context):
        """Call to remove a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rename(self, request, context):
        """Call to rename a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloneDirRecursive(self, request, context):
        """Call to clone a directory recursively.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInodeMetadata(self, request, context):
        """Call to fetch inode metadata from SnapFS.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LookupFileHandle': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupFileHandle,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.LookupFileHandleArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.LookupFileHandleResult.SerializeToString,
            ),
            'GetFileSize': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFileSize,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileSizeArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileSizeResult.SerializeToString,
            ),
            'SetFileSize': grpc.unary_unary_rpc_method_handler(
                    servicer.SetFileSize,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.SetFileSizeArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.SetFileSizeResult.SerializeToString,
            ),
            'GetFileStat': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFileStat,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileStatArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileStatResult.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadResult.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.WriteArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.WriteResult.SerializeToString,
            ),
            'ReadDir': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadDir,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadDirArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadDirResult.SerializeToString,
            ),
            'CloneDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.CloneDirectory,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryResult.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirResult.SerializeToString,
            ),
            'CreateDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDirectory,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirResult.SerializeToString,
            ),
            'CreateEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEntities,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateEntitiesArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateEntitiesResult.SerializeToString,
            ),
            'RemoveFile': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFile,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RemoveFileArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RemoveFileResult.SerializeToString,
            ),
            'Rename': grpc.unary_unary_rpc_method_handler(
                    servicer.Rename,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RenameArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RenameResult.SerializeToString,
            ),
            'CloneDirRecursive': grpc.unary_unary_rpc_method_handler(
                    servicer.CloneDirRecursive,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryResult.SerializeToString,
            ),
            'GetInodeMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInodeMetadata,
                    request_deserializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetInodeMetadataArg.FromString,
                    response_serializer=bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetInodeMetadataResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.bridge.ddw_portal.stub.RpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.bridge.ddw_portal.stub.RpcService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LookupFileHandle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/LookupFileHandle',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.LookupFileHandleArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.LookupFileHandleResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFileSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/GetFileSize',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileSizeArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileSizeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetFileSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/SetFileSize',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.SetFileSizeArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.SetFileSizeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFileStat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/GetFileStat',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileStatArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetFileStatResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/Read',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/Write',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.WriteArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.WriteResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/ReadDir',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadDirArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.ReadDirResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CloneDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/CloneDirectory',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/CreateFile',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/CreateDirectory',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateFileOrDirResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateEntities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/CreateEntities',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateEntitiesArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CreateEntitiesResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RemoveFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/RemoveFile',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RemoveFileArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RemoveFileResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Rename(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/Rename',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RenameArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.RenameResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CloneDirRecursive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/CloneDirRecursive',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.CloneDirectoryResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetInodeMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cohesity.bridge.ddw_portal.stub.RpcService/GetInodeMetadata',
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetInodeMetadataArg.SerializeToString,
            bridge_dot_ddw__portal_dot_stub_dot_rpc__service__args__pb2.GetInodeMetadataResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)