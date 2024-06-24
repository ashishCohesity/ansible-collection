# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.shyamb.fileservices.common import file_services_pb2 as experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2

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
        + f' but the generated code in experimental/shyamb/fileservices/common/file_services_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileServicesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFile = channel.unary_unary(
                '/cohesity.experimental.shyamb.fileservices.FileServices/CreateFile',
                request_serializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.CreateFileArg.SerializeToString,
                response_deserializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.CreateFileResult.FromString,
                _registered_method=True)
        self.ReadFile = channel.unary_unary(
                '/cohesity.experimental.shyamb.fileservices.FileServices/ReadFile',
                request_serializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.ReadFileArg.SerializeToString,
                response_deserializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.ReadFileResult.FromString,
                _registered_method=True)
        self.WriteFile = channel.unary_unary(
                '/cohesity.experimental.shyamb.fileservices.FileServices/WriteFile',
                request_serializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.WriteFileArg.SerializeToString,
                response_deserializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.WriteFileResult.FromString,
                _registered_method=True)


class FileServicesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.CreateFileArg.FromString,
                    response_serializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.CreateFileResult.SerializeToString,
            ),
            'ReadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFile,
                    request_deserializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.ReadFileArg.FromString,
                    response_serializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.ReadFileResult.SerializeToString,
            ),
            'WriteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFile,
                    request_deserializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.WriteFileArg.FromString,
                    response_serializer=experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.WriteFileResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.shyamb.fileservices.FileServices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.shyamb.fileservices.FileServices', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileServices(object):
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
            '/cohesity.experimental.shyamb.fileservices.FileServices/CreateFile',
            experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.CreateFileArg.SerializeToString,
            experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.CreateFileResult.FromString,
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
    def ReadFile(request,
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
            '/cohesity.experimental.shyamb.fileservices.FileServices/ReadFile',
            experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.ReadFileArg.SerializeToString,
            experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.ReadFileResult.FromString,
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
    def WriteFile(request,
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
            '/cohesity.experimental.shyamb.fileservices.FileServices/WriteFile',
            experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.WriteFileArg.SerializeToString,
            experimental_dot_shyamb_dot_fileservices_dot_common_dot_file__services__pb2.WriteFileResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
