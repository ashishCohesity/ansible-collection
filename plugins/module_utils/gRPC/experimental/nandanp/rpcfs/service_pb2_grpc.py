# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.nandanp.rpcfs import service_pb2 as experimental_dot_nandanp_dot_rpcfs_dot_service__pb2

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
        + f' but the generated code in experimental/nandanp/rpcfs/service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Greet = channel.unary_unary(
                '/cohesity.experimental.nandanp.rpcfs.FsService/Greet',
                request_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.HelloRequest.SerializeToString,
                response_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.HelloResult.FromString,
                _registered_method=True)
        self.CreateFile = channel.unary_unary(
                '/cohesity.experimental.nandanp.rpcfs.FsService/CreateFile',
                request_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.FromString,
                _registered_method=True)
        self.WriteFileRange = channel.unary_unary(
                '/cohesity.experimental.nandanp.rpcfs.FsService/WriteFileRange',
                request_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileRangeRequest.SerializeToString,
                response_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.FromString,
                _registered_method=True)
        self.ReadFileRange = channel.unary_unary(
                '/cohesity.experimental.nandanp.rpcfs.FsService/ReadFileRange',
                request_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileRangeRequest.SerializeToString,
                response_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.FromString,
                _registered_method=True)


class FsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Greet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteFileRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFileRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Greet': grpc.unary_unary_rpc_method_handler(
                    servicer.Greet,
                    request_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.HelloRequest.FromString,
                    response_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.HelloResult.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.CreateFileRequest.FromString,
                    response_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.SerializeToString,
            ),
            'WriteFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFileRange,
                    request_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileRangeRequest.FromString,
                    response_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.SerializeToString,
            ),
            'ReadFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFileRange,
                    request_deserializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileRangeRequest.FromString,
                    response_serializer=experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.nandanp.rpcfs.FsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.nandanp.rpcfs.FsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Greet(request,
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
            '/cohesity.experimental.nandanp.rpcfs.FsService/Greet',
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.HelloRequest.SerializeToString,
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.HelloResult.FromString,
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
            '/cohesity.experimental.nandanp.rpcfs.FsService/CreateFile',
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.CreateFileRequest.SerializeToString,
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.FromString,
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
    def WriteFileRange(request,
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
            '/cohesity.experimental.nandanp.rpcfs.FsService/WriteFileRange',
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileRangeRequest.SerializeToString,
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.FromString,
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
    def ReadFileRange(request,
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
            '/cohesity.experimental.nandanp.rpcfs.FsService/ReadFileRange',
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileRangeRequest.SerializeToString,
            experimental_dot_nandanp_dot_rpcfs_dot_service__pb2.FileSystemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
