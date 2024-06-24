# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from experimental.ravin.filer import filer_pb2 as experimental_dot_ravin_dot_filer_dot_filer__pb2

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
        + f' but the generated code in experimental/ravin/filer/filer_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FilerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/cohesity.experimental.ravin.filer.Filer/ListFiles',
                request_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ListFilesArg.SerializeToString,
                response_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ListFilesRet.FromString,
                _registered_method=True)
        self.CreateFile = channel.unary_unary(
                '/cohesity.experimental.ravin.filer.Filer/CreateFile',
                request_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.CreateFileArg.SerializeToString,
                response_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.CreateFileRet.FromString,
                _registered_method=True)
        self.ReadFileRange = channel.unary_unary(
                '/cohesity.experimental.ravin.filer.Filer/ReadFileRange',
                request_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ReadFileRangeArg.SerializeToString,
                response_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ReadFileRangeRet.FromString,
                _registered_method=True)
        self.WriteFileRange = channel.unary_unary(
                '/cohesity.experimental.ravin.filer.Filer/WriteFileRange',
                request_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.WriteFileRangeArg.SerializeToString,
                response_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.WriteFileRangeRet.FromString,
                _registered_method=True)


class FilerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Following is the API exposed by the filer service.
        All the return proto contain the last modification timestamp (denoting time
        since epoch) which can be used as the last op-id that modified the file.
        This can be used to do read-after-write verification.

        Get the list of files available for client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Create a new file at the base dir served by the filer.
        optionally the arg can include a buffer to write to the new file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFileRange(self, request, context):
        """Read the range of data from the file.
        Optionally the arg can include the last timestamp obtained from last write,
        so that read-after-write verification can be done.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteFileRange(self, request, context):
        """Write data at the specified range in the file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FilerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ListFilesArg.FromString,
                    response_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ListFilesRet.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.CreateFileArg.FromString,
                    response_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.CreateFileRet.SerializeToString,
            ),
            'ReadFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFileRange,
                    request_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ReadFileRangeArg.FromString,
                    response_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.ReadFileRangeRet.SerializeToString,
            ),
            'WriteFileRange': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFileRange,
                    request_deserializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.WriteFileRangeArg.FromString,
                    response_serializer=experimental_dot_ravin_dot_filer_dot_filer__pb2.WriteFileRangeRet.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cohesity.experimental.ravin.filer.Filer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cohesity.experimental.ravin.filer.Filer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Filer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
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
            '/cohesity.experimental.ravin.filer.Filer/ListFiles',
            experimental_dot_ravin_dot_filer_dot_filer__pb2.ListFilesArg.SerializeToString,
            experimental_dot_ravin_dot_filer_dot_filer__pb2.ListFilesRet.FromString,
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
            '/cohesity.experimental.ravin.filer.Filer/CreateFile',
            experimental_dot_ravin_dot_filer_dot_filer__pb2.CreateFileArg.SerializeToString,
            experimental_dot_ravin_dot_filer_dot_filer__pb2.CreateFileRet.FromString,
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
            '/cohesity.experimental.ravin.filer.Filer/ReadFileRange',
            experimental_dot_ravin_dot_filer_dot_filer__pb2.ReadFileRangeArg.SerializeToString,
            experimental_dot_ravin_dot_filer_dot_filer__pb2.ReadFileRangeRet.FromString,
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
            '/cohesity.experimental.ravin.filer.Filer/WriteFileRange',
            experimental_dot_ravin_dot_filer_dot_filer__pb2.WriteFileRangeArg.SerializeToString,
            experimental_dot_ravin_dot_filer_dot_filer__pb2.WriteFileRangeRet.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
