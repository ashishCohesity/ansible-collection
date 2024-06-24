# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.devershi.file_service import file_service_pb2 as experimental_dot_devershi_dot_file__service_dot_file__service__pb2

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
        + f' but the generated code in experimental/devershi/file_service/file_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFile = channel.unary_unary(
                '/experimental.devershi.file_service.FileService/CreateFile',
                request_serializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.FromString,
                _registered_method=True)
        self.ReadFileBlock = channel.unary_unary(
                '/experimental.devershi.file_service.FileService/ReadFileBlock',
                request_serializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.ReadFileBlockRequest.SerializeToString,
                response_deserializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.FromString,
                _registered_method=True)
        self.WriteFileBlock = channel.unary_unary(
                '/experimental.devershi.file_service.FileService/WriteFileBlock',
                request_serializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.WriteFileBlockRequest.SerializeToString,
                response_deserializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.FromString,
                _registered_method=True)


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateFile(self, request, context):
        """Create file only if file is not already present.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFileBlock(self, request, context):
        """Read Block of data if:
        a) File exists
        b) (offset + block_size_to_read <= file_size)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteFileBlock(self, request, context):
        """Write block of data if:
        1) File exists
        2) either of the two conditions are met: a) offset = EOF b) offest +
        block_size_to_write <= EOF
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.CreateFileRequest.FromString,
                    response_serializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.SerializeToString,
            ),
            'ReadFileBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFileBlock,
                    request_deserializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.ReadFileBlockRequest.FromString,
                    response_serializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.SerializeToString,
            ),
            'WriteFileBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFileBlock,
                    request_deserializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.WriteFileBlockRequest.FromString,
                    response_serializer=experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'experimental.devershi.file_service.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('experimental.devershi.file_service.FileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

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
            '/experimental.devershi.file_service.FileService/CreateFile',
            experimental_dot_devershi_dot_file__service_dot_file__service__pb2.CreateFileRequest.SerializeToString,
            experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.FromString,
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
    def ReadFileBlock(request,
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
            '/experimental.devershi.file_service.FileService/ReadFileBlock',
            experimental_dot_devershi_dot_file__service_dot_file__service__pb2.ReadFileBlockRequest.SerializeToString,
            experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.FromString,
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
    def WriteFileBlock(request,
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
            '/experimental.devershi.file_service.FileService/WriteFileBlock',
            experimental_dot_devershi_dot_file__service_dot_file__service__pb2.WriteFileBlockRequest.SerializeToString,
            experimental_dot_devershi_dot_file__service_dot_file__service__pb2.FileOpResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
