# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.slee.rpc import file_rpc_pb2 as experimental_dot_slee_dot_rpc_dot_file__rpc__pb2

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
        + f' but the generated code in experimental/slee/rpc/file_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RemoteFileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Greet = channel.unary_unary(
                '/cohesity.experimental.slee.rpc.RemoteFileService/Greet',
                request_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.SayHelloPayload.SerializeToString,
                response_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.SayHelloResult.FromString,
                _registered_method=True)
        self.CreateFile = channel.unary_unary(
                '/cohesity.experimental.slee.rpc.RemoteFileService/CreateFile',
                request_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.CreateFilePayload.SerializeToString,
                response_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.CreateFileResult.FromString,
                _registered_method=True)
        self.ReadFileRange = channel.unary_unary(
                '/cohesity.experimental.slee.rpc.RemoteFileService/ReadFileRange',
                request_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.ReadFileRangePayload.SerializeToString,
                response_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.ReadFileRangeResult.FromString,
                _registered_method=True)
        self.WriteFileRange = channel.unary_unary(
                '/cohesity.experimental.slee.rpc.RemoteFileService/WriteFileRange',
                request_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.WriteFileRangePayload.SerializeToString,
                response_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.WriteFileRangeResult.FromString,
                _registered_method=True)


class RemoteFileServiceServicer(object):
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

    def ReadFileRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteFileRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteFileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Greet': grpc.unary_unary_rpc_method_handler(
                    servicer.Greet,
                    request_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.SayHelloPayload.FromString,
                    response_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.SayHelloResult.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.CreateFilePayload.FromString,
                    response_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.CreateFileResult.SerializeToString,
            ),
            'ReadFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFileRange,
                    request_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.ReadFileRangePayload.FromString,
                    response_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.ReadFileRangeResult.SerializeToString,
            ),
            'WriteFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFileRange,
                    request_deserializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.WriteFileRangePayload.FromString,
                    response_serializer=experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.WriteFileRangeResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.slee.rpc.RemoteFileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.slee.rpc.RemoteFileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RemoteFileService(object):
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
            '/cohesity.experimental.slee.rpc.RemoteFileService/Greet',
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.SayHelloPayload.SerializeToString,
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.SayHelloResult.FromString,
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
            '/cohesity.experimental.slee.rpc.RemoteFileService/CreateFile',
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.CreateFilePayload.SerializeToString,
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.CreateFileResult.FromString,
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
            '/cohesity.experimental.slee.rpc.RemoteFileService/ReadFileRange',
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.ReadFileRangePayload.SerializeToString,
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.ReadFileRangeResult.FromString,
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
            '/cohesity.experimental.slee.rpc.RemoteFileService/WriteFileRange',
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.WriteFileRangePayload.SerializeToString,
            experimental_dot_slee_dot_rpc_dot_file__rpc__pb2.WriteFileRangeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)